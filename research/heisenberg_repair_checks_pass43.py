"""Six exact controls for the global Heisenberg repair and fiber criterion.

These controls test polynomial identities, actual finite flows, a nonunit
plinth, and a finite exceptional-fiber minor. They do not realize the full
high-degree power-law profile or verify external classification theorems.
"""

import unittest

import sympy as sp


def clean(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda item: sp.cancel(sp.expand(item)))
    return sp.cancel(sp.expand(value))


def act(field, value, variables):
    return clean(sum(a*sp.diff(value, x) for a, x in zip(field, variables)))


def bracket(left, right, variables):
    return clean(sp.Matrix([act(left, b, variables)-act(right, a, variables)
                            for a, b in zip(left, right)]))


class HeisenbergRepairChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def normalizer_data(self):
        g, v, b, z, u = sp.symbols("g v b z u")
        variables = (g, v, b, z)
        E = sp.Matrix([0, 1, g*v, b])
        Tc = sp.Matrix([0, 0, 1, 0])
        Tlambda = sp.Matrix([0, 1, 0, 0])
        Wc = bracket(E, Tc, variables)
        W = bracket(E, Tlambda, variables)
        V = bracket(E, W, variables)
        return variables, u, E, Tc, Tlambda, Wc, W, V

    def test_actual_laurent_conjugation_cancels_before_specialization(self):
        variables, u, E, Tc, Tlambda, Wc, W, V = self.normalizer_data()
        g, v, b, z = variables
        self.assertZero(g*Wc+V)
        P = g*Tc+2*u*Tlambda
        ad1 = bracket(E/u, P, variables)
        ad2 = bracket(E/u, ad1, variables)
        self.assertZero(bracket(E/u, ad2, variables))
        conjugate = clean(P+ad1+ad2/2)
        Y = clean(g*Tc+2*W)
        self.assertZero(conjugate-Y-2*u*Tlambda)
        self.assertTrue(all(sp.denom(item) == 1 for item in conjugate))
        self.assertZero(conjugate.subs(u, 0)-Y)
        for field in (P, conjugate):
            for point in variables:
                current = point
                for unused in range(4):
                    current = act(field, current, variables)
                self.assertZero(current)
        # This is an actual normalizer model, not a power-law-profile example.
        self.assertZero(act(E, v, variables)-1)

    def test_heisenberg_brackets_and_global_finite_nilpotence(self):
        variables, unused, E, Tc, Tlambda, Wc, W, V = self.normalizer_data()
        g, v, b, z = variables
        Y = clean(g*Tc+2*W)
        self.assertZero(Y-sp.Matrix([0, 0, -g, 0]))
        self.assertZero(V-sp.Matrix([0, 0, 0, g]))
        self.assertZero(bracket(E, Y, variables)-V)
        self.assertZero(bracket(E, V, variables))
        self.assertZero(bracket(Y, V, variables))
        for field in (E, Y, V):
            self.assertZero(act(field, g, variables))
            for point in variables:
                current = point
                for unused in range(4):
                    current = act(field, current, variables)
                self.assertZero(current)

    def test_explicit_replica_and_independence(self):
        variables, unused, E, Tc, Tlambda, Wc, W, V = self.normalizer_data()
        g, v, b, z = variables
        Y = clean(g*Tc+2*W)
        tau = g**3*v
        self.assertZero(act(E, tau, variables)-g**3)
        self.assertZero(act(V, tau, variables))
        R = clean(g**3*Y-tau*V-act(Y, tau, variables)*E)
        self.assertZero(R-sp.Matrix([0, 0, -g**4, -g**4*v]))
        for field in (E, V):
            self.assertZero(bracket(field, R, variables))
        for point in (g, tau):
            self.assertZero(act(R, point, variables))
        self.assertEqual(sp.Matrix.hstack(E, Y, V).rank(), 3)
        self.assertEqual(sp.Matrix.hstack(E, V, R).rank(), 3)
        for point in variables:
            self.assertZero(act(R, act(R, point, variables), variables))
        delta, L, C = E/g, Y/g, V/g**2
        sigma = tau/g**2
        D0 = clean(L-sigma*C-act(L, sigma, variables)*delta)
        self.assertZero(g**4*D0-R)

    def test_slice_projection_with_nonconstant_horizontal_coefficient(self):
        q, s, r, z = sp.symbols("q s r z")
        variables = (q, s, r, z)
        delta = sp.Matrix([0, 1, 0, 0])
        C = sp.Matrix([0, 0, 1, 0])
        L = sp.Matrix([1, q**2, s, 0])
        self.assertZero(bracket(delta, L, variables)-C)
        self.assertZero(bracket(delta, C, variables))
        self.assertZero(bracket(L, C, variables))
        b = act(L, s, variables)
        self.assertZero(b-q**2)
        self.assertZero(act(delta, b, variables))
        self.assertZero(act(C, b, variables))
        D0 = clean(L-s*C-b*delta)
        self.assertZero(D0-sp.Matrix([1, 0, 0, 0]))
        for field in (delta, C):
            self.assertZero(bracket(field, D0, variables))
        for field in (L, D0):
            for point in variables:
                current = point
                for unused in range(5):
                    current = act(field, current, variables)
                self.assertZero(current)

    def test_invariant_nonunit_plinth_via_highest_derivative(self):
        u, v, r, q = sp.symbols("u v r q")
        variables = (u, v, r)
        C = sp.Matrix([0, 0, u])
        D = sp.Matrix([0, 1, v])
        self.assertZero(bracket(C, D, variables))
        r0 = v**2*r
        c0 = act(C, r0, variables)
        self.assertZero(c0-u*v**2)
        c = act(D, act(D, c0, variables), variables)
        r2 = act(D, act(D, r0, variables), variables)
        self.assertZero(c-2*u)
        self.assertZero(r2-2*r-5*v**2)
        self.assertZero(act(D, c, variables))
        self.assertZero(act(C, r2, variables)-c)
        local_slice = r2/c
        self.assertZero(act(C, local_slice, variables)-1)
        self.assertZero(act(D, local_slice, variables)-6*v/u)
        inverse_r = u*q-sp.Rational(5, 2)*v**2
        self.assertZero(local_slice.subs(r, inverse_r)-q)
        self.assertZero(inverse_r.subs(q, local_slice)-r)
        for point in variables:
            current = point
            for unused in range(4):
                current = act(D, current, variables)
            self.assertZero(current)

    def test_omitted_coordinate_and_finite_exceptional_fiber_minor(self):
        b, w, v, z, p = sp.symbols("b w v z p")
        variables = (b, w, v, z)
        invariant = w+v**2
        D1 = sp.Matrix([invariant, 0, 0, 0])
        D2 = sp.Matrix([0, 0, 0, invariant-1])
        D3 = sp.Matrix([0, -2*v*(invariant+1)**2, (invariant+1)**2, 0])
        fields = (D1, D2, D3)
        self.assertZero(sp.diff(invariant, b))
        for field in fields:
            self.assertZero(act(field, invariant, variables))
            for point in variables:
                current = point
                for unused in range(3):
                    current = act(field, current, variables)
                self.assertZero(current)
        for index, left in enumerate(fields):
            for right in fields[index+1:]:
                self.assertZero(bracket(left, right, variables))
        matrix = sp.Matrix.hstack(*fields)
        minor = matrix.extract((0, 3, 2), (0, 1, 2)).det()
        self.assertZero(minor-invariant*(invariant-1)*(invariant+1)**2)
        self.assertEqual(matrix.rank(), 3)
        self.assertZero(invariant.subs(w, p-v**2)-p)
        self.assertZero((p-v**2).subs(p, invariant)-w)
        # At the exceptional fibers rank can drop; the proof excludes them.
        for alpha in (0, 1, -1):
            self.assertZero(minor.subs(w, alpha-v**2))
        self.assertNotEqual(clean(minor.subs(w, 2-v**2)), 0)


if __name__ == "__main__":
    unittest.main()

