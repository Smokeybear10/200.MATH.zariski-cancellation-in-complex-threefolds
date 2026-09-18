"""Four exact controls for the determinant-field reduction.

Only the second method reuses the actual independent-defect frame.
The commuting-pair and two-quasi models test the relevant algebra,
not existence of an unclosed rank-one-projection residual.
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


class BadProjectionDeterminantChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_commuting_translation_straightening_and_finite_flow(self):
        u, v, r, s, tau, time = sp.symbols("u v r s tau time")
        variables = (u, v, r, s)
        f, b, c = u*v-1, u, v**2+1
        Q = r**4/4+u*r**2/2
        q = r**5+v*r**2
        a3 = sp.diff(Q, r)
        E = sp.Matrix([0, 0, 0, 1])
        V3 = sp.Matrix([0, 0, 1, a3])
        V4 = sp.Matrix([0, 0, b, b*a3+c])
        x3 = f*(s-Q)+q
        self.assertZero(bracket(V3, V4, variables))
        self.assertZero(bracket(E, V3, variables))
        self.assertZero(bracket(E, V4, variables))
        self.assertZero(act(E, x3, variables)-f)
        K = clean(act(V4, x3, variables)*V3-act(V3, x3, variables)*V4)
        self.assertZero(K-sp.Matrix([0, 0, c*f, c*(f*a3-sp.diff(q, r))]))
        self.assertZero(act(K, x3, variables))
        self.assertZero(bracket(E, K, variables))
        self.assertZero(act(K, s-Q, variables)+c*sp.diff(q, r))
        r_new = r+c*f*time
        tau_new = tau+(q-q.subs(r, r_new))/f
        # This division cancels even globally in this illustrative model.
        self.assertEqual(sp.denom(clean(tau_new)), 1)
        images = {r: r_new, tau: clean(tau_new)}
        inverse = {r: r-c*f*time,
                   tau: clean(tau+(q-q.subs(r, r-c*f*time))/f)}
        self.assertZero(images[r].subs(inverse, simultaneous=True)-r)
        self.assertZero(images[tau].subs(inverse, simultaneous=True)-tau)
        self.assertZero(inverse[r].subs(images, simultaneous=True)-r)
        self.assertZero(inverse[tau].subs(images, simultaneous=True)-tau)
        current = s
        for unused in range(7):
            current = act(K, current, variables)
        self.assertZero(current)

    def test_actual_independent_defect_determinant_field(self):
        u, v, a, c = sp.symbols("u v a c")
        variables = (u, v, a, c)
        g = u*v-1
        E = sp.Matrix([0, 0, u, g])
        physical = sp.Matrix([u+a**2/2, v+c**2/2, a, c])
        partials = physical.jacobian(variables).inv()
        V = [bracket(E, bracket(E, partials[:, i], variables), variables)
             for i in (2, 3)]
        K = clean(act(V[1], a, variables)*V[0]-act(V[0], a, variables)*V[1])
        self.assertZero(K-sp.Matrix([0, 0, 0, -4*u**2*g]))
        self.assertZero(bracket(E, K, variables))
        bad = sp.Matrix([[act(field, point, variables) for field in V]
                         for point in (a, c)])
        self.assertEqual(bad.rank(), 2)
        self.assertZero(act(K, c, variables)+bad.det())
        self.assertZero(act(K, a, variables))
        r, s = g*a-u*c, v*a-c
        self.assertZero(act(E, s, variables)-1)
        self.assertZero(act(E, r, variables))
        self.assertZero(act(K, r, variables)-4*u**3*g)
        self.assertZero(act(K, u, variables))
        self.assertZero(act(K, v, variables))
        for point in physical:
            current = point
            for unused in range(3):
                current = act(K, current, variables)
            self.assertZero(current)
        # The actual determinant field is not claimed to have a slice.
        self.assertZero(K.subs(u, 0))

    def test_rank_one_projection_keeps_an_actual_coordinate_pair(self):
        u, v, r, s = sp.symbols("u v r s")
        variables = (u, v, r, s)
        E = sp.Matrix([0, 0, 0, 1])
        V3 = sp.Matrix([0, 0, 1, 0])
        V4 = E
        x3 = s+r**2
        x4 = v*x3+u
        bad = sp.Matrix([[act(field, point, variables) for field in (V3, V4)]
                         for point in (x3, x4)])
        self.assertEqual(bad.rank(), 1)
        K = clean(act(V4, x3, variables)*V3-act(V3, x3, variables)*V4)
        self.assertZero(K-sp.Matrix([0, 0, 1, -2*r]))
        for invariant in (u, v, x3, x4):
            self.assertZero(act(K, invariant, variables))
        self.assertZero(act(K, r, variables)-1)
        U, V, X, R = sp.symbols("U V X R")
        coordinate_map = sp.Matrix([x4, v, x3, r])
        inverse = sp.Matrix([U-V*X, V, R, X-R**2])
        self.assertZero(coordinate_map.subs(dict(zip(variables, inverse)),
                                            simultaneous=True)
                        - sp.Matrix([U, V, X, R]))
        self.assertZero(inverse.subs(dict(zip((U, V, X, R), coordinate_map)),
                                    simultaneous=True)-sp.Matrix(variables))
        # This is a model for the determinant lemma, not actual quadratic tops.
        self.assertZero(bracket(E, V3, variables))

    def test_exact_two_quasi_inverse_and_repeated_common_factor(self):
        v, j, t, x3, x4 = sp.symbols("v j t x3 x4")
        p, q = v, v**2+1
        alpha, beta = -v, sp.Integer(1)
        self.assertZero(alpha*p+beta*q-1)
        forward_j = q*x3-p*x4
        forward_t = alpha*x3+beta*x4
        inverse = {x3: p*t+beta*j, x4: q*t-alpha*j}
        self.assertZero(forward_j.subs(inverse, simultaneous=True)-j)
        self.assertZero(forward_t.subs(inverse, simultaneous=True)-t)
        self.assertZero(inverse[x3].subs({j: forward_j, t: forward_t},
                                         simultaneous=True)-x3)
        self.assertZero(inverse[x4].subs({j: forward_j, t: forward_t},
                                         simultaneous=True)-x4)
        d = (j+v)**2
        f, g = d*p, d*q
        self.assertZero(sp.gcd(f, g)-d)
        self.assertZero(alpha*f+beta*g-d)
        determinant = sp.Matrix([f, g]).jacobian((v, j)).det()
        expected = d*sp.diff(d, j)*(sp.diff(p, v)*q-p*sp.diff(q, v))
        self.assertZero(determinant-expected)
        self.assertNotEqual(clean(determinant), 0)
        L = sp.Matrix([0, 0, d])
        for point in inverse.values():
            self.assertZero(act(L, act(L, point, (v, j, t)), (v, j, t)))
        self.assertZero(L.subs(j, -v))
        # This verifies the restricted normal form, not a realization in B.


if __name__ == "__main__":
    unittest.main()
