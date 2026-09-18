"""Independent exact controls for an actual nonremovable quadratic frame.

The first method checks both polynomial inverse orders of the cubic example,
its original bad partial, and failure of first-commutator stability even though
the acceleration is outside the constant quadratic good-speed span. The second
checks the corresponding cubic divided-difference identities with arbitrary
constant coefficients. These are actual translation examples, not cancellation
counterexamples or obstructions to arbitrary coordinate changes. The coefficient
rank test has only the fixed-good-shear meaning justified in the written proof.
No earlier checker or solver is imported. Runtime execution is left to Root.
"""

import unittest

import sympy as sp


class ThreeGoodCubicDividedDifferenceChecks(unittest.TestCase):
    @staticmethod
    def act(field, value, variables):
        return sp.expand(sum(coefficient*sp.diff(value, variable)
                             for coefficient, variable in zip(field, variables)))

    @classmethod
    def bracket(cls, left, right, variables):
        return sp.Matrix([cls.act(left, right[i], variables)
                          - cls.act(right, left[i], variables)
                          for i in range(len(variables))])

    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def assert_matrix_equal(self, left, right):
        self.assertEqual(left.shape, right.shape)
        for value in left-right:
            self.assert_zero(value)

    def test_actual_cubic_inverse_nonremovability_and_commutator(self):
        a, b, v, u, scale = sp.symbols("a b v u scale")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, original = (a, b, v, u), (X, Y, Z, W)
        half = sp.Rational(1, 2)
        frame = sp.Matrix([
            u,
            v+a*u,
            a-half*v**3+b*u,
            b+3*half*a*v**2+3*half*a**2*v*u+half*a**3*u**2,
        ])
        inv_a = Z-X*W+half*Y**3
        inv_v = Y-inv_a*X
        inv_b = (W-3*half*inv_a*inv_v**2
                 - 3*half*inv_a**2*inv_v*X-half*inv_a**3*X**2)
        inverse = sp.Matrix([inv_a, inv_b, inv_v, X])
        forward_sub = dict(zip(original, frame))
        inverse_sub = dict(zip(adapted, inverse))
        self.assert_matrix_equal(inverse.subs(forward_sub, simultaneous=True),
                                 sp.Matrix(adapted))
        self.assert_matrix_equal(frame.subs(inverse_sub, simultaneous=True),
                                 sp.Matrix(original))
        # This sign uses the explicitly ordered bases (a,b,v,u) and (X,Y,Z,W).
        self.assert_zero(frame.jacobian(adapted).det()+1)
        self.assert_zero(frame[2]-frame[0]*frame[3]+half*frame[1]**3-a)

        E = sp.Matrix([0, 0, 0, 1])
        speeds = sp.Matrix([self.act(E, value, adapted) for value in frame[:3]])
        self.assert_matrix_equal(speeds, sp.Matrix([1, a, b]))
        for value in speeds:
            self.assert_zero(self.act(E, value, adapted))
        self.assertEqual(speeds[0], 1)
        self.assertEqual(speeds.jacobian(adapted).rank(), 2)
        speed_coefficients = sp.Matrix([
            [sp.Poly(value, a, b).coeff_monomial(monomial)
             for monomial in (1, a, b)] for value in speeds])
        self.assertEqual(speed_coefficients.det(), 1)
        omega = sp.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(b)).det()
        self.assertEqual(omega, 1)
        self.assert_zero((scale*speeds).jacobian((scale, a, b)).det()-scale**2)
        acceleration = self.act(E, self.act(E, frame[3], adapted), adapted)
        self.assert_zero(acceleration-a**3)
        self.assert_zero(self.act(E, acceleration, adapted))
        self.assertEqual(sp.Poly(frame[3], u).degree(), 2)

        # Exact constant-coefficient membership test, not an arbitrary-frame
        # minimality claim: the six products span precisely degree <=2 in a,b.
        products = [speeds[i]*speeds[j] for i in range(3) for j in range(i, 3)]
        monomials = (1, a, b, a**2, a*b, b**2, a**3)
        coefficient_matrix = sp.Matrix([
            [sp.Poly(value, a, b).coeff_monomial(monomial)
             for value in products+[acceleration]] for monomial in monomials])
        self.assertEqual(coefficient_matrix[:, :6].rank(), 6)
        self.assertEqual(coefficient_matrix.rank(), 7)

        # Derive the actual partial holding X,Y,Z fixed from the inverse.
        T = inverse.jacobian(original)[:, 3].subs(
            forward_sub, simultaneous=True).applyfunc(sp.expand)
        self.assert_matrix_equal(T, sp.Matrix([-u, 1+3*half*v**2*u, u**2, 0]))
        for index, value in enumerate(frame):
            self.assert_zero(self.act(T, value, adapted)-int(index == 3))
        degree = max([sp.Poly(value, u).degree() for value in T[:3]]
                     + [sp.Poly(T[3], u).degree()-1])
        self.assertEqual(degree, 2)
        N = sp.Matrix([sp.Poly(value, u).coeff_monomial(u**degree)
                       for value in T[:3]]+[0])
        self.assert_matrix_equal(N, sp.Matrix([0, 0, 1, 0]))
        Q = self.bracket(E, T, adapted)
        self.assert_matrix_equal(Q, sp.Matrix([-1, 3*half*v**2, 2*u, 0]))
        self.assert_matrix_equal(self.bracket(E, Q, adapted), 2*N)
        self.assert_matrix_equal(self.bracket(E, 2*N, adapted), sp.zeros(4, 1))
        for value in (a, b, acceleration, *tuple(speeds)):
            self.assert_zero(self.act(N, value, adapted))
        self.assertEqual(self.act(N, v, adapted), 1)
        Qb = self.act(Q, b, adapted)
        self.assert_zero(self.act(E, Qb, adapted))
        self.assert_zero(self.act(N, Qb, adapted)-3*v)
        self.assertNotEqual(sp.expand(self.act(N, Qb, adapted)), 0)
        # A=C[a,b,v], so N=partial_v has S=C[a,b]. Thus Q(b) is in A but
        # not S, while X=u is still an actual coordinate slice recognizing A.
        self.assertEqual(self.act(E, frame[0], adapted), 1)

    def test_generic_cubic_divided_difference_identities(self):
        a, b, v, u, t = sp.symbols("a b v u t")
        gamma, beta, alpha, delta = sp.symbols("gamma beta alpha delta")
        variables = (a, b, v, u)
        polynomial = gamma*t**3+beta*t**2+alpha*t+delta
        Fv = polynomial.subs(t, v)
        Fy = polynomial.subs(t, v+a*u)
        divided_difference = (gamma*(3*a*v**2+3*a**2*v*u+a**3*u**2)
                              + beta*(2*a*v+a**2*u)+alpha*a)
        self.assert_zero(u*divided_difference-Fy+Fv)
        frame = sp.Matrix([u, v+a*u, a-Fv+b*u, b+divided_difference])
        self.assert_zero(frame[2]-u*frame[3]+Fy-a)
        self.assert_zero(frame.jacobian(variables).det()+1)
        self.assert_zero(sp.diff(frame[3], u, 2)-2*gamma*a**3)
        self.assert_zero(sp.diff(frame[3], u, 3))
        # A nonzero complex gamma gives degree exactly two; the identity is
        # valid also at gamma=0, where that degree claim is no longer made.
        self.assert_zero(sp.Poly(frame[3], u).coeff_monomial(u**2)-gamma*a**3)
        self.assert_zero(sp.diff(frame[3].subs(gamma, 0), u, 2))
        Fprime = sp.diff(polynomial, t).subs(t, v)
        T = sp.Matrix([-u, 1+u*Fprime, u**2, 0])
        for index, value in enumerate(frame):
            self.assert_zero(self.act(T, value, variables)-int(index == 3))
        E, N = sp.Matrix([0, 0, 0, 1]), sp.Matrix([0, 0, 1, 0])
        Q = self.bracket(E, T, variables)
        self.assert_matrix_equal(Q, sp.Matrix([-1, Fprime, 2*u, 0]))
        self.assert_matrix_equal(self.bracket(E, Q, variables), 2*N)
        self.assert_zero(self.act(N, self.act(Q, b, variables), variables)
                         - sp.diff(polynomial, t, 2).subs(t, v))
        specialized = frame.subs({gamma: sp.Rational(1, 2), beta: 0,
                                  alpha: 0, delta: 0}, simultaneous=True)
        self.assert_zero(sp.diff(specialized[3], u, 2)-a**3)
        # These cubic identities do not replace the all-polynomial F proof,
        # and the example's fixed-good nonremovability is not global minimality.


if __name__ == "__main__":
    unittest.main(verbosity=2)
