"""Exact all-coefficient leading determinant identity.

The odd pair is base-polynomial data, not an actual full frame.
"""

import unittest

import sympy as S


class SquareSpeedLeadingChecks(unittest.TestCase):
    def test_all_quartics_have_the_exact_rank_one_leading_factor(self):
        a, b, X, Y = S.symbols("a b X Y")
        coefficients = S.symbols("c10 alpha1 c12 beta1 c14 c20 alpha2 c22 beta2 c24")
        c10, alpha1, c12, beta1, c14, c20, alpha2, c22, beta2, c24 = coefficients
        monomials = [a**4, a**3 * b, a**2 * b**2, a * b**3, b**4]
        h = [
            sum(c * m for c, m in zip(coefficients[:5], monomials)),
            sum(c * m for c, m in zip(coefficients[5:], monomials)),
        ]

        def df(F):
            return S.cancel(S.diff(F, a) / (2 * a))

        def dg(F):
            return S.cancel(S.diff(F, b) / (2 * b))

        leading_rows = []
        for polynomial in h:
            self.assertEqual(
                S.expand((a * S.diff(polynomial, a) + b * S.diff(polynomial, b)) / 2
                         - 2 * polynomial),
                0,
            )
            quadratic = (
                df(df(polynomial)) * X**2
                + 2 * df(dg(polynomial)) * X * Y
                + dg(dg(polynomial)) * Y**2
            ) / 4
            leading_rows.append([df(quadratic), dg(quadratic)])
        leading = S.Matrix(leading_rows)
        J = b**2 * X - a**2 * Y
        expected = (
            3 * J**2 / (32 * a**5 * b**5)
            * S.Matrix([beta1 * b**2 - alpha1 * a**2,
                        beta2 * b**2 - alpha2 * a**2])
            * S.Matrix([[b**2, -a**2]])
        )
        self.assertEqual((leading - expected).applyfunc(S.cancel), S.zeros(2))
        self.assertEqual((leading * S.Matrix([a**2, b**2])).applyfunc(S.cancel),
                         S.zeros(2, 1))
        self.assertEqual(S.cancel(leading.det()), 0)
        self.assertEqual(
            leading.subs({alpha1: 0, beta1: 0, alpha2: 0, beta2: 0}),
            S.zeros(2),
        )

        odd_pair = S.Matrix([a**3 * b, a * b**3])
        self.assertEqual(S.factor(odd_pair.jacobian([a, b]).det()), 8 * a**3 * b**3)
        pure_odd_substitution = {
            c10: 0, alpha1: 1, c12: 0, beta1: 0, c14: 0,
            c20: 0, alpha2: 0, c22: 0, beta2: 1, c24: 0,
        }
        odd_leading = leading.subs(pure_odd_substitution)
        self.assertEqual(S.cancel(odd_leading[0, 0] + 3 * J**2 / (32 * a**3 * b**3)), 0)
        self.assertEqual(S.cancel(odd_leading.det()), 0)

        n11, n12, n21, n22 = S.symbols("n11 n12 n21 n22")
        output_change = S.Matrix([[n11, n12], [n21, n22]])
        changed = output_change * odd_pair
        odd_coefficients = S.Matrix([
            [S.Poly(F, a, b).coeff_monomial(a**3 * b),
             S.Poly(F, a, b).coeff_monomial(a * b**3)]
            for F in changed
        ])
        self.assertEqual(odd_coefficients, output_change)


if __name__ == "__main__":
    unittest.main(verbosity=2)
