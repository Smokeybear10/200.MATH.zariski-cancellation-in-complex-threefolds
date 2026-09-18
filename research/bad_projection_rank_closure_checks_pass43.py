"""Three exact controls for bad-projection rank-one exclusion.

The inconsistent universal rank-one branch is excluded by the written
proof, not realized by a test example. Controls distinguish the needed
polynomial/invariant-gcd gates from rational proportionality.
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


class BadProjectionRankClosureChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_wronskian_forces_the_invariant_parameter_derivative(self):
        v, x, y, b = sp.symbols("v x y b")
        variables = (v, x, y, b)
        p, q = v, v**2+1
        j = q*x-p*y
        d = (j+v)**2
        E = sp.Matrix([0, d*p, d*q, 0])
        H = sp.Matrix([b, 0, 0, 0])
        self.assertZero(act(E, j, variables))
        self.assertZero(act(E, d, variables))
        self.assertZero(act(E, act(H, v, variables), variables))
        hj = act(H, j, variables)
        self.assertZero(hj-(sp.diff(q, v)*x-sp.diff(p, v)*y)*b)
        obstruction = act(E, hj, variables)
        self.assertZero(obstruction-d*(sp.diff(q, v)*p-sp.diff(p, v)*q)*b)
        self.assertNotEqual(obstruction, 0)
        # This computes the obstruction; it does not assert [E,H](j)=0.
        self.assertZero(act(bracket(E, H, variables), j, variables)-obstruction)

    def test_polynomial_riccati_and_two_missing_gate_countercontrols(self):
        a, s, x = sp.symbols("a s x")
        polynomial_field = sp.Matrix([-a**2])
        current = a
        for n in range(1, 10):
            current = act(polynomial_field, current, (a,))
            self.assertZero(current-(-1)**n*sp.factorial(n)*a**(n+1))
            self.assertNotEqual(current, 0)
        # The genuine polynomial LND d/ds admits a rational Riccati solution.
        rational_a = 1/s
        self.assertZero(sp.diff(rational_a, s)+rational_a**2)
        self.assertEqual(sp.denom(rational_a), s)
        # Proportional double-commutator-zero fields can have moving gcd.
        variables = (s, x)
        E = sp.Matrix([1, 0])
        H = sp.Matrix([0, s])
        commutator = bracket(E, H, variables)
        self.assertZero(commutator-rational_a*H)
        self.assertZero(bracket(E, commutator, variables))
        self.assertZero(act(E, s, variables)-1)
        primitive = sp.Matrix([0, 1])
        self.assertZero(bracket(E, primitive, variables))
        # The original proof has E(gcd H)=0, unlike this countercontrol.

    def test_actual_rank_two_projection_retains_the_proportionality_boundary(self):
        u, v, a, c = sp.symbols("u v a c")
        variables = (u, v, a, c)
        g = u*v-1
        E = sp.Matrix([0, 0, u, g])
        physical = sp.Matrix([u+a**2/2, v+c**2/2, a, c])
        partials = physical.jacobian(variables).inv()
        V = [bracket(E, bracket(E, partials[:, i], variables), variables)
             for i in (2, 3)]
        second = sp.Matrix([act(E, act(E, point, variables), variables)
                            for point in physical])
        H = clean(partials*second)
        L = bracket(E, H, variables)
        self.assertZero(L+(u*V[0]+g*V[1])/2)
        self.assertZero(bracket(E, L, variables))
        self.assertZero(second[2:, :])
        bad = sp.Matrix([[act(field, point, variables) for field in V]
                         for point in (a, c)])
        self.assertEqual(bad.rank(), 2)
        self.assertEqual(sp.Matrix.hstack(H, L).rank(), 2)
        self.assertEqual(sp.gcd(H[0], H[1]), 1)
        self.assertZero(act(H, u, variables)-u**2)
        self.assertNotEqual(act(H, g, variables), 0)
        # Actual H does not kill the common kernel in this surviving branch.


if __name__ == "__main__":
    unittest.main()

