"""Exact controls for the pass51 quartic divisions.

Formal coefficients and the inherited weak conic are not asserted
actual unresolved-cylinder examples. Flatness and the branch theorem
remain mathematical proof obligations, not finite-test conclusions.
"""

import unittest
import sympy as sp


class TriplePointQuarticChecks(unittest.TestCase):
    def test_two_independent_quartic_divisions_and_derivatives(self):
        a, b, z, w, epsilon = sp.symbols("a b z w epsilon")
        c, d, e, f, g, h, q1, q2, q3 = sp.symbols(
            "c d e f g h q1 q2 q3")
        b1 = a**2*c+a*b*d+b**2*e
        b2 = a**2*f+a*b*g+b**2*h
        q = a**2*q1+a*b*q2+b**2*q3
        r = a*z+b*w
        p = a*b1+b*b2
        conic = epsilon*r**2-2*b2*z+2*b1*w-q

        def derive(value):
            return sp.expand(sp.diff(value, z)*(epsilon*b*r+b1)
                             + sp.diff(value, w)*(-epsilon*a*r+b2))

        def iterate(value, n):
            for _ in range(n):
                value = derive(value)
            return value

        ha = epsilon*w**2-2*h*z+2*e*w-q3
        ga = (epsilon*a*z**2+2*epsilon*b*z*w
              - 2*(a*f+b*g)*z+2*(a*c+b*d)*w-(a*q1+b*q2))
        hb = epsilon*z**2-2*f*z+2*c*w-q1
        gb = (2*epsilon*a*z*w+epsilon*b*w**2
              - 2*(a*g+b*h)*z+2*(a*d+b*e)*w-(a*q2+b*q3))
        self.assertEqual(sp.expand(a*ga+b**2*ha-conic), 0)
        self.assertEqual(sp.expand(a**2*hb+b*gb-conic), 0)
        self.assertEqual(derive(conic), 0)
        self.assertEqual(sp.expand(derive(r)-p), 0)
        self.assertEqual(sp.expand(iterate(ha, 4)-6*epsilon**3*a**2*p**2), 0)
        self.assertEqual(sp.expand(iterate(hb, 4)-6*epsilon**3*b**2*p**2), 0)
        self.assertEqual(iterate(ha, 5), 0)
        self.assertEqual(iterate(hb, 5), 0)
        # These fraction-field identities do not assert denominator
        # removal. The written proof supplies that by actual flatness.
        self.assertEqual(sp.expand(iterate(ha/a, 4)-6*epsilon**3*a*p**2), 0)
        self.assertEqual(sp.expand(iterate(hb/b, 4)-6*epsilon**3*b*p**2), 0)

    def test_full_divisor_basis_and_basis_change_covariance(self):
        p, t, y, eta = sp.symbols("p t y eta")

        def derive(value):
            return sp.expand(p*sp.diff(value, t)+2*t*sp.diff(value, y))

        def fourth(value):
            for _ in range(4):
                value = derive(value)
            return value

        self.assertEqual(derive(p*y-t**2+eta), 0)
        self.assertEqual([fourth(v) for v in
                          (sp.Integer(1), t, y, t*y, y**2)],
                         [0, 0, 0, 0, 24*p**2])
        m11, m12, m21, m22 = sp.symbols("m11 m12 m21 m22")
        matrix = sp.Matrix([[m11, m12], [m21, m22]])
        skew = sp.Matrix([[0, 1], [-1, 0]])
        self.assertEqual((matrix*skew*matrix.T
                          - matrix.det()*skew).applyfunc(sp.expand),
                         sp.zeros(2, 2))

    def test_weak_conic_does_not_allow_either_actual_division(self):
        a, b, z, w = sp.symbols("a b z w")
        r = a*z+b*w
        conic = r**2-2*b**2*z-2*a**2*w+a*b-a**3
        ha, hb = w**2-2*z, z**2-2*w-a
        self.assertEqual(sp.expand(conic.subs(a, 0)-b**2*ha), 0)
        self.assertEqual(sp.expand(conic.subs(b, 0)-a**2*hb), 0)
        modulo_a = sp.groebner([conic, a], a, b, z, w, domain=sp.QQ)
        modulo_b = sp.groebner([conic, b], a, b, z, w, domain=sp.QQ)
        self.assertNotEqual(modulo_a.reduce(ha)[1], 0)
        self.assertNotEqual(modulo_b.reduce(hb)[1], 0)
        self.assertEqual(modulo_a.reduce(b**2*ha)[1], 0)
        self.assertEqual(modulo_b.reduce(a**2*hb)[1], 0)


if __name__ == "__main__":
    unittest.main()
