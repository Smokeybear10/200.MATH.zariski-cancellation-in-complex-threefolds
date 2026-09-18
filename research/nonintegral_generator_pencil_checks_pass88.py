"""One Laurent-ring control, not an actual additive-action realization."""

import unittest

import sympy as S


class NonintegralGeneratorPencilChecks(unittest.TestCase):
    def test_laurent_recovery_localization_and_order(self):
        v, tau = S.symbols("v tau")
        c, h = v**-2, v**-1
        d = c + tau * h
        recovered_v = v**3 * d - tau * v**2
        recovered_h = recovered_v * d - tau
        recovered_c = recovered_h**2
        for left, right in ((recovered_v, v), (recovered_h, h),
                            (recovered_c, c), (recovered_c + tau * recovered_h, d),
                            (v**3 * c, v), (v**3 * c**2, h)):
            self.assertEqual(S.cancel(left - right), 0)

        # A=R[1/v^2]: shared inverse in the tensor square has zero difference.
        p, c1, c2 = S.symbols("p c1 c2")
        localization = S.groebner([p * c1 - 1, p * c2 - 1], c1, c2, p)
        self.assertEqual(localization.reduce(c1 - c2)[1], 0)
        self.assertEqual(localization.reduce(c1**2 - c2**2)[1], 0)

        def order_at_zero(expression):
            numerator, denominator = S.fraction(S.cancel(expression))
            numerator_order = min(monomial[0] for monomial in S.Poly(numerator, v).monoms())
            denominator_order = min(monomial[0] for monomial in S.Poly(denominator, v).monoms())
            return numerator_order - denominator_order

        self.assertEqual(order_at_zero(h), -1)
        self.assertEqual(order_at_zero(v**2), 2)
        self.assertEqual(order_at_zero(v**3), 3)
        self.assertEqual(S.expand((v**2) * c), 1)
        # These finite degrees only check the pattern used by the written proof.
        for n in (1, 2, 5):
            self.assertEqual(order_at_zero(h**n), -n)
            self.assertTrue(all(order_at_zero(h**j) > -n for j in range(n)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
