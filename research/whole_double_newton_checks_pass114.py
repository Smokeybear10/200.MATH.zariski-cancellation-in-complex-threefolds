"""One finite Newton-splitting control, with q=2,3,4 subtests.

These polynomial coefficient examples have distinguished smooth a and
J=(a,t**2). They check the exact scalar identity, the stated ideal
membership, orders after an invertible formal base change, and roots
through t**6. They are not actual-frame realizations or counterexamples.
No finite check proves the all-order splitting, the general colength
argument, analytic primeness, or cancellation. No solver or retained
checker is imported.
"""

import unittest

import sympy as sp


class WholeDoubleNewtonChecks(unittest.TestCase):
    def test_distinguished_a_colength_two_controls(self):
        a, b, h, eta, zeta = sp.symbols("a b h eta zeta")
        B2 = h * eta + a * zeta
        P = a * h + b * B2
        self.assertEqual(sp.expand(P - ((a + b * eta) * (h + b * zeta)
                                       - b**2 * eta * zeta)), 0)

        t, X, Z = sp.symbols("t X Z")
        unit = 1 + t**2
        transformed_a = (X - t**3) / unit
        self.assertEqual(sp.cancel(transformed_a + t**2 * (transformed_a + t)
                                   - X), 0)

        def order(value):
            numerator, denominator = sp.fraction(sp.cancel(value))
            self.assertNotEqual(numerator, 0)
            numerator_order = min(m[0] for m, _ in sp.Poly(numerator, t).terms())
            denominator_order = min(m[0] for m, _ in sp.Poly(denominator, t).terms())
            return numerator_order - denominator_order

        def truncate(value, bound):
            return sp.Add(*(coefficient * t**monomial[0]
                            for monomial, coefficient in sp.Poly(
                                sp.expand(value), t).terms()
                            if monomial[0] < bound))

        for q in (2, 3, 4):
            with self.subTest(q=q):
                # Cross terms in h retain the exact original b**2 relation.
                h0 = t**q + a * t**2 + a**2
                eta0, zeta0 = a + t, a**2 + a * t + t**3
                membership = (t**(4 - q) * h0
                              - t**(4 - q) * a * t**2
                              - t**(4 - q) * a**2)
                self.assertEqual(sp.expand(membership - t**4), 0)
                self.assertEqual(sp.gcd(sp.Poly(a, a, t),
                                        sp.Poly(h0, a, t)).as_expr(), 1)
                self.assertEqual(sp.expand(zeta0 - a * (a + t) - t**2 * t), 0)
                self.assertEqual(eta0.subs({a: 0, t: 0}), 0)
                specialized_P = sp.expand(P.subs(
                    {b: t**2, h: h0, eta: eta0, zeta: zeta0}, simultaneous=True))
                hx = sp.cancel(h0.subs(a, transformed_a))
                ex = sp.cancel(eta0.subs(a, transformed_a))
                zx = sp.cancel(zeta0.subs(a, transformed_a))
                Hx, Rx = hx + t**2 * zx, t**4 * ex * zx
                Px = sp.cancel(specialized_P.subs(a, transformed_a))
                self.assertEqual(sp.cancel(Px - X * Hx + Rx), 0)
                self.assertEqual(order(hx.subs(X, 0)), q)
                self.assertEqual(order(Hx.subs(X, 0)), q)
                self.assertEqual(order(Rx.subs(X, 0)), 8)

                # Clear a unit only; the normalized expression is polynomial.
                cleared = sp.Poly(sp.cancel(unit**3 * Px), X, t).as_expr()
                scale = 8 - q
                scaled = sp.Poly(sp.expand(cleared.subs(X, t**scale * Z)), t)
                quotient, remainder = scaled.div(sp.Poly(t**8, t))
                self.assertTrue(remainder.is_zero)
                normalized = quotient.as_expr()
                self.assertEqual(normalized.subs(t, 0), Z - 1)
                self.assertEqual(sp.diff(normalized, Z).subs(t, 0), 1)

                # Six finite corrections, not an infinite formal-root proof.
                root = sp.Integer(1)
                for degree in range(1, 7):
                    error = truncate(normalized.subs(Z, root), degree + 1)
                    root -= sp.Poly(error, t).nth(degree) * t**degree
                    self.assertEqual(truncate(normalized.subs(Z, root), degree + 1), 0)
                root_X = sp.expand(t**scale * root)
                self.assertEqual(order(root_X), scale)
                self.assertGreaterEqual(order(cleared.subs(X, root_X)), 15)
                self.assertEqual(order(Hx.subs(X, root_X)), q)
                self.assertGreaterEqual(order(root_X * sp.diff(Hx, X).subs(X, root_X)), 5)
                self.assertGreaterEqual(order(sp.diff(Rx, X).subs(X, root_X)), 6)
                self.assertEqual(order(sp.diff(Px, X).subs(X, root_X)), q)

                # The finite quotient is a nonunit, nonzero at this truncation.
                factor = sp.Poly(X - root_X, X)
                quotient, remainder = sp.Poly(cleared, X).div(factor)
                self.assertEqual(sp.expand(remainder.as_expr()
                                           - cleared.subs(X, root_X)), 0)
                self.assertEqual(quotient.as_expr().subs({X: 0, t: 0}), 0)
                self.assertEqual(order(quotient.as_expr().subs(X, root_X)), q)


if __name__ == "__main__":
    unittest.main(verbosity=2)
