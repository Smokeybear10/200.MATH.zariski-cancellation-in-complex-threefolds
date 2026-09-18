#!/usr/bin/env python3
"""Independent exact controls for two pass-18 obstruction arguments.

These finite identities do not prove general cancellation, rank-three
connectedness, or any all-parameter statement in the research notes.
No solver or other checker is imported.
"""

import math
import unittest

import sympy as sp


x, y, z, w, q, T, u, v, t = sp.symbols("x y z w q T u v t")


class RescalingCurveControls(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.cancel(value), 0)

    def test_finite_binomial_derivative(self):
        for bound in range(1, 11):
            polynomial = sum(sp.prod(T-j for j in range(k))*q**k
                             /sp.factorial(k) for k in range(1, bound+1))
            expected = sum((-1)**(k-1)*q**k/sp.Integer(k)
                           for k in range(1, bound+1))
            self.assertZero(sp.diff(polynomial, T).subs(T, 0)-expected)
            self.assertZero(polynomial.subs(T, 0))

    def test_binomial_tail_divisibility(self):
        for bound in range(1, 8):
            for integer in range(0, bound+5):
                truncation = sum(sp.binomial(integer, k)*q**k
                                 for k in range(1, bound+1))
                tail = sp.Poly(sp.expand((1+q)**integer-1-truncation), q)
                self.assertEqual(tail.rem(sp.Poly(q**(bound+1), q)),
                                 sp.Poly(0, q))

    def test_integer_vandermonde_determinants(self):
        for degree in range(1, 9):
            matrix = sp.Matrix([[sp.Integer(i)**j for j in range(degree+1)]
                                for i in range(degree+1)])
            self.assertEqual(matrix.det(), math.prod(math.factorial(j)
                                                     for j in range(1, degree+1)))

    def test_rescaling_poles_and_full_congruence(self):
        for multiplicity in range(2, 7):
            for order in range(1, multiplicity+2):
                lam = 1+x**order
                coefficient = sp.cancel((lam**2-1)/x**multiplicity)
                if order < multiplicity:
                    self.assertEqual(sp.denom(coefficient),
                                     x**(multiplicity-order))
                else:
                    self.assertEqual(sp.denom(coefficient), 1)
                image_y = lam*y
                image_z = z+coefficient*y*y
                self.assertZero(x**multiplicity*image_z-image_y**2
                                -(x**multiplicity*z-y*y))

    def test_modification_inclusion_jacobian(self):
        for power in range(1, 5):
            divisor = 1+x**power
            inclusion = sp.Matrix([x, divisor*w, z])
            self.assertZero(inclusion.jacobian([x, w, z]).det()-divisor)
            for bound in range(1, 7):
                inverse = sum((-x**power)**j for j in range(bound))
                self.assertEqual(sp.rem(sp.expand(divisor*inverse-1),
                                        x**bound, x), 0)

    def test_balanced_free_coordinate_matrix(self):
        for bound in range(1, 7):
            inverse_jet = sum((-x)**j for j in range(2*bound))
            matrix = sp.Matrix([[1+x, x**bound], [-x**bound, inverse_jet]])
            self.assertZero(matrix.det()-1)
            for entry in matrix*matrix.adjugate()-sp.eye(2):
                self.assertZero(entry)

    def test_disjoint_nodal_cubic_parametrizations(self):
        polynomial = v*v-u**3+3*u
        for value, up, vp in [(2, t*t-2, t*(t*t-3)),
                              (-2, t*t+2, t*(t*t+3))]:
            self.assertZero(polynomial.subs({u: up, v: vp})-value)
        self.assertZero(polynomial-2-(v*v-(u-1)**2*(u+2)))
        self.assertZero(polynomial+2-(v*v-(u+1)**2*(u-2)))

    def test_finite_birational_normalization_relations(self):
        for shift in (-2, 2):
            up = t*t+shift
            divisor = up+1 if shift == 2 else up-1
            vp = t*divisor
            self.assertZero(t*t-up+shift)
            self.assertZero(vp-t*divisor)
            self.assertZero(sp.cancel(vp/divisor)-t)

    def test_nodes_and_noncoordinate_gradient(self):
        polynomial = v*v-u**3+3*u
        gradient = [sp.diff(polynomial, a) for a in (u, v)]
        hessian = sp.hessian(polynomial, (u, v))
        for point, value in [(1, 2), (-1, -2)]:
            for entry in gradient:
                self.assertZero(entry.subs({u: point, v: 0}))
            self.assertEqual(polynomial.subs({u: point, v: 0}), value)
            self.assertNotEqual(hessian.det().subs(u, point), 0)

    def test_disconnected_unit_and_interpolation(self):
        polynomial = v*v-u**3+3*u
        plinth_control = polynomial**2-4
        coefficient = polynomial+3
        self.assertZero(plinth_control/5-(polynomial-3)*coefficient/5-1)
        interpolant = sp.interpolate([(sp.Integer(-2), sp.Integer(1)),
                                      (sp.Integer(2), sp.Integer(5))], T)
        self.assertZero(interpolant-(T+3))
        self.assertEqual(sp.gcd(interpolant, T*T-4), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
