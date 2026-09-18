"""Finite exact controls for the pass52 fourth-image boundary.

The coefficient identities and generic basis determinant do not
verify actual flatness, image-ideal equality or a cylinder example.
Those assertions retain the hypotheses and written proof in the note.
"""

import unittest
import sympy as sp


class FourthImageBoundaryChecks(unittest.TestCase):
    def test_coherent_cubic_quartic_syzygies(self):
        a, b, z, w, epsilon = sp.symbols("a b z w epsilon")
        c, d, e, f, g, h, q1, q2, q3 = sp.symbols(
            "c d e f g h q1 q2 q3")
        b1 = a**2*c+a*b*d+b**2*e
        b2 = a**2*f+a*b*g+b**2*h
        q = a**2*q1+a*b*q2+b**2*q3
        r = a*z+b*w
        p = a*b1+b*b2
        conic = epsilon*r**2-2*b2*z+2*b1*w-q
        ta = (epsilon*w**2-2*h*z+2*e*w-q3)/a
        tb = (epsilon*z**2-2*f*z+2*c*w-q1)/b
        t = (epsilon*r*z-2*(a*f+b*g)*z
             + 2*(a*c+b*d)*w-a*q1-b*q2)/b
        # One identity is exact before the conic quotient; the other
        # has exactly the displayed conic numerator, not an omitted error.
        self.assertEqual(sp.cancel(
            a*tb-t+epsilon*z*w-2*g*z+2*d*w-q2), 0)
        self.assertEqual(sp.cancel(
            b*ta+t+epsilon*z*w-conic/(a*b)), 0)
        self.assertEqual(sp.cancel(
            b*ta-a*tb+2*t+2*g*z-2*d*w+q2-conic/(a*b)), 0)

        def derive(value):
            return sp.expand(sp.diff(value, z)*(epsilon*b*r+b1)
                             + sp.diff(value, w)*(-epsilon*a*r+b2))

        def iterate(value, n):
            for _ in range(n):
                value = derive(value)
            return value

        self.assertEqual(sp.cancel(iterate(t, 3)-3*epsilon**2*p**2), 0)
        self.assertEqual(sp.cancel(
            iterate(b*ta-a*tb, 3)+6*epsilon**2*p**2), 0)
        self.assertEqual(iterate(b*ta-a*tb, 4), 0)

    def test_generic_fourth_basis_has_the_expected_determinant(self):
        a, b, r, b1, b2, q, epsilon = sp.symbols(
            "a b r B1 B2 Q epsilon", nonzero=True)
        c, e, f, h, q1, q3 = sp.symbols("c e f h q1 q3")
        p = a*b1+b*b2
        # Independent generic conic inverse, obtained from the two
        # equations r=aZ+bW and epsilon*r²-2B2*Z+2B1*W=Q.
        z = (epsilon*b*r**2+2*b1*r-b*q)/(2*p)
        w = (-epsilon*a*r**2+2*b2*r+a*q)/(2*p)
        self.assertEqual(sp.cancel(a*z+b*w-r), 0)
        self.assertEqual(sp.cancel(
            epsilon*r**2-2*b2*z+2*b1*w-q), 0)
        ta = (epsilon*w**2-2*h*z+2*e*w-q3)/a
        tb = (epsilon*z**2-2*f*z+2*c*w-q1)/b
        polynomials = [sp.Poly(value, r) for value in
                       (sp.Integer(1), z, w, ta, tb)]
        matrix = sp.Matrix([
            [poly.coeff_monomial(r**i) for i in range(5)]
            for poly in polynomials])
        # The first three rows have no cubic or quartic coefficients,
        # so two small determinants compute the full determinant.
        low = matrix.extract([0, 1, 2], [0, 1, 2]).det()
        high = matrix.extract([3, 4], [3, 4]).det()
        self.assertEqual(sp.cancel(low+epsilon/(2*p)), 0)
        self.assertEqual(sp.cancel(high+epsilon**5/(4*p**3)), 0)
        self.assertEqual(sp.cancel(
            low*high-epsilon**6/(8*p**4)), 0)


if __name__ == "__main__":
    unittest.main()
