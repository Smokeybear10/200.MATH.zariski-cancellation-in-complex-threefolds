"""One finite Artinian-coefficient factor-lifting control.

The coefficient ring is Q[e]/(e**3), realized as R/J for R=Q[[x,y]]
and J=(x,y**3). The initial cubic has a simple linear factor and a
quadratic cofactor whose reduction has a double root. Noncanonical,
varying coefficient lifts exercise the absence of a ring section.
Only three J-adic correction steps are checked. This does not prove
all-order factorization, analytic-prime support, an actual-frame
realization, the geometric exclusion, or cancellation. No solver or
other checker is imported.
"""

import unittest

import sympy as sp


class WholeDoubleSquareIdealChecks(unittest.TestCase):
    def test_nilpotent_coefficients_and_finite_ideal_lifts(self):
        e, A, B, T, x, y = sp.symbols("e A B T x y")

        def reduce_coefficient(value):
            return sp.rem(sp.Poly(sp.expand(value), e), sp.Poly(e**3, e)).as_expr()

        def inverse_unit(value):
            self.assertEqual(reduce_coefficient(value).subs(e, 0), 1)
            delta = reduce_coefficient(value - 1)
            inverse = reduce_coefficient(1 - delta + delta**2)
            self.assertEqual(reduce_coefficient(value * inverse), 1)
            return inverse

        def homogeneous_j(value, degree):
            return sp.Add(*(coefficient * e**(j % 3) * A**i * B**(j // 3)
                            for (i, j), coefficient in sp.Poly(
                                sp.expand(value), x, y).terms()
                            if i + j // 3 == degree))

        def j_order(value):
            polynomial = sp.Poly(sp.expand(value), x, y)
            if polynomial.is_zero:
                return sp.oo
            return min(i + j // 3 for (i, j), _ in polynomial.terms())

        def lift(value, sign):
            # e -> y + x + sign*y**3 is only a coefficient lift, not a section.
            value = reduce_coefficient(value)
            return sp.expand(value.subs(
                {e: y + x + sign * y**3, A: x, B: y**3}, simultaneous=True))

        self.assertNotEqual(reduce_coefficient(e**2), 0)
        self.assertEqual(reduce_coefficient(e**3), 0)
        self.assertNotEqual((y + x + y**3)**3, 0)

        a, b = x, y**3
        h = (b - a)**2 + a * b**2 + y**2 * a**3
        B2 = y * b**2 + y**2 * a * b + a**3 + (1 + y) * b**3
        P = sp.expand(a * h + b * B2)
        self.assertEqual(sp.expand(h - a**2 * (1 + y**2 * a)
                                   + a * b * (2 - b) - b**2), 0)
        self.assertGreaterEqual(j_order(h), 2)
        self.assertEqual(j_order(P), 3)
        P3 = homogeneous_j(P, 3)
        self.assertEqual(sp.expand(P3 - (A * (B - A)**2 + e * B**3
                                        + e**2 * A * B**2)), 0)

        # Exact simple-root lifting through the nilpotent coefficient ideal.
        polynomial = P3.subs({A: T, B: 1})
        root = sp.Integer(0)
        for _ in range(2):
            derivative = reduce_coefficient(sp.diff(polynomial, T).subs(T, root))
            root = reduce_coefficient(root - polynomial.subs(T, root)
                                      * inverse_unit(derivative))
        self.assertEqual(root, -e + 2 * e**2)
        self.assertEqual(reduce_coefficient(polynomial.subs(T, root)), 0)

        L1 = A - root * B
        quotient, remainder = sp.div(P3, L1, A)
        Q2 = reduce_coefficient(quotient)
        self.assertEqual(reduce_coefficient(remainder), 0)
        self.assertEqual(reduce_coefficient(L1 * Q2 - P3), 0)
        self.assertEqual(sp.expand(Q2.subs(e, 0) - (B - A)**2), 0)
        self.assertEqual(sp.discriminant(Q2.subs({e: 0, B: 1}), A), 0)
        derivative = reduce_coefficient(Q2.subs({A: root, B: 1}))
        derivative_inverse = inverse_unit(derivative)

        # Distinct coefficient lifts still have the same prescribed initials.
        L, H = lift(L1, 1), lift(Q2, -1)
        self.assertGreaterEqual(j_order(L - lift(L1, -1)), 2)
        self.assertGreaterEqual(j_order(H - lift(Q2, 1)), 3)
        self.assertEqual(homogeneous_j(L, 1), sp.expand(L1))
        self.assertEqual(homogeneous_j(H, 2), sp.expand(Q2))
        self.assertGreaterEqual(j_order(P - L * H), 4)

        for degree in range(4, 7):
            error = homogeneous_j(P - L * H, degree)
            residue = reduce_coefficient(error.subs({A: root, B: 1}))
            correction_L = reduce_coefficient(
                residue * derivative_inverse * B**(degree - 2))
            numerator = reduce_coefficient(error - Q2 * correction_L)
            correction_H, remainder = sp.div(numerator, L1, A)
            correction_H = reduce_coefficient(correction_H)
            self.assertEqual(reduce_coefficient(remainder), 0)
            self.assertEqual(reduce_coefficient(
                L1 * correction_H + Q2 * correction_L - error), 0)
            delta_L = lift(correction_L, (-1)**degree)
            delta_H = lift(correction_H, (-1)**(degree + 1))
            self.assertGreaterEqual(j_order(delta_L), degree - 2)
            self.assertGreaterEqual(j_order(delta_H), degree - 1)
            self.assertGreater(j_order(delta_L * delta_H), degree)
            L, H = sp.expand(L + delta_L), sp.expand(H + delta_H)
            self.assertGreaterEqual(j_order(P - L * H), degree + 1)
        self.assertEqual(j_order(L), 1)
        self.assertEqual(j_order(H), 2)
        self.assertGreaterEqual(j_order(P - L * H), 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
