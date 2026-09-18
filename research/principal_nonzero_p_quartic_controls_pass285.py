"""Finite controls of 285's full raw pencil and two degree regimes.

The curve-pole lemma, actual field descent and recognition theorem are
written proof inputs, not conclusions of this suite. No checker imports.
"""

import unittest

import sympy as S


class NonzeroPQuarticControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_full_raw_pencil_and_actual_inverse(self):
        h, t, X, Y, sigma, x, v, p = S.symbols("h t X Y sigma x v p")
        k, k1, k2, k3, c, c1, c2, q, q1, a1, a2, w0, v1 = S.symbols(
            "k k1 k2 k3 c c1 c2 q q1 a1 a2 w0 v1")
        y = Y - sigma * X - t * X**2
        n = -2 * t * y + (-x + a2 * sigma**2 + a1 * sigma + k1 * v1 - q1) / v
        z = 2 * t * y + sigma**2 + k1 * sigma + n
        w = (v1 * n + w0 - p * ((2 * sigma + k1) * y + k2 * sigma**2 / 2)
             - h * (y**2 + k2 * sigma * y + k3 * sigma**3 / 6)
             + c1 * y + c2 * sigma**2 / 2 + (v * n + q1) * sigma)
        theta = p * n + q + c1 * sigma - h * ((2 * sigma + k1) * y + k2 * sigma**2 / 2)
        W = w + theta * X + (h * n + c) * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        kappa = h * k1 + 2 * t * p
        slope = c1 - p * k1 - 2 * t * v1
        Jstar = S.expand(W + h * Y**2 + kappa * X * Y - slope * Y)
        self.assert_zero(S.diff(Jstar, Y).subs(k2, (-2 * t * v - 2 * p) / h))
        self.assert_zero(S.diff(Z, Y))
        Zmodel = ((1 + a2 / v) * sigma**2 + (k1 + a1 / v + 2 * t * X) * sigma
                  - x / v + (k1 * v1 - q1) / v + k * X + t**2 * X**2)
        self.assert_zero(Z - Zmodel)
        Wvar, Jvar, K, L = S.symbols("Wvar Jvar K L")
        correction = h * Y**2 + K * X * Y - L * Y
        forward, backward = Wvar + correction, Jvar - correction
        self.assert_zero(forward.subs(Wvar, backward) - Jvar)
        self.assert_zero(backward.subs(Jvar, forward) - Wvar)
        self.assert_zero(S.diff(forward, Wvar) - 1)

    def test_full_generic_x_degree_keeps_degenerate_case(self):
        X, x, t, v, d, f, alpha, k1, a1 = S.symbols("X x t v d f alpha k1 a1")
        sigma = (x**2 - f) / d
        Z = alpha * v**2 * sigma**2 + (k1 + a1 / v + 2 * t * X) * sigma - x / v
        self.assertEqual(S.Poly(Z, x).degree(), 4)
        self.assert_zero(S.Poly(Z, x).nth(4) - alpha * v**2 / d**2)
        degenerate = Z.subs(alpha, 0)
        self.assertEqual(S.Poly(degenerate, x).degree(), 2)
        self.assert_zero(S.Poly(degenerate, x).nth(2) - (k1 + a1 / v + 2 * t * X) / d)
        special_intercept = degenerate.subs({a1: -v * k1, X: 0}, simultaneous=True)
        self.assertEqual(S.Poly(special_intercept, x).degree(), 1)
        self.assertEqual(S.Poly(degenerate.subs(a1, -v * k1), x).degree(), 2)

    def test_slice_content_positive_and_missing_slice_control(self):
        X, Z, J, Y = S.symbols("X Z J Y")
        row = [S.Integer(1), X, Z + 1, X**2 + J]
        variables = [X, Z, J, Y]
        derivative = lambda value: S.expand(sum(coefficient * S.diff(value, variable)
                                              for coefficient, variable in zip(row, variables)))
        self.assert_zero(derivative(X) - 1)
        self.assert_zero(derivative(derivative(X)))
        self.assertTrue(all(not coefficient.has(Y) for coefficient in row))
        for variable in variables:
            value = variable
            for _ in range(8):
                value = derivative(value)
            self.assert_zero(value)
        # Rational direction ratios alone cannot remove a common multiplier.
        bad_row = [Y, S.Integer(0), S.Integer(0), S.Integer(0)]
        self.assertEqual(S.gcd_list(bad_row), Y)
        self.assertEqual(S.cancel(bad_row[0] / Y), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
