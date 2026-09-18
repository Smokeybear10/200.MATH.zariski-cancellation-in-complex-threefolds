"""Finite algebra controls for 278; not a proof of its field or LND gates.

No retained checker is imported. These reconstruct the formal gradients,
the actual nice row, and the final monic coordinate including its inverse.
"""

import unittest

import sympy as S


class ConstantSecondLineControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_general_formal_line_coefficients(self):
        t, n, U, P = S.symbols("t n U P")
        h, j, k = [S.Function(name)(t) for name in ("h", "j", "k")]
        T, omega = [S.Function(name)(t, n) for name in ("T", "omega")]
        gamma = 2 * P + S.diff(k, t)
        A = gamma * U + S.diff(k, t, 2) * P**2 / 2
        C = U**2 + S.diff(k, t, 2) * P * U + S.diff(k, t, 3) * P**3 / 6
        W = (omega - (S.diff(h, t) * P + S.diff(T, n)) * A - h * C
             + (S.diff(h, t) * n + S.diff(j, t)) * U
             + (S.diff(h, t, 2) * n + S.diff(j, t, 2)) * P**2 / 2
             + S.diff(T, t) * P)
        QU = gamma * S.diff(W, n) - S.diff(W, P)
        QP = (2 * U + S.diff(k, t, 2) * P) * S.diff(W, n) - S.diff(W, t)
        expected_U = (-gamma**2 * S.diff(T, n, 2)
                      + (6 * P + 2 * S.diff(k, t)) * S.diff(h, t)
                      + 2 * S.diff(T, n) + h * S.diff(k, t, 2))
        self.assert_zero(S.expand(QU).coeff(U, 1) - expected_U)
        self.assert_zero(S.expand(QP).coeff(U, 2)
                         + 2 * gamma * S.diff(T, n, 2) - 3 * S.diff(h, t))

    def test_full_nice_row_with_constant_second_projection(self):
        t, n, y, sigma, X, h = S.symbols("t n y sigma X h")
        j, k, q = [S.Function(name)(t) for name in ("j", "k", "q")]
        omega = S.Function("omega")(t, n)
        T = -h * S.diff(k, t, 2) * n / 2 + q
        A = (2 * sigma + S.diff(k, t)) * y + S.diff(k, t, 2) * sigma**2 / 2
        C = y**2 + S.diff(k, t, 2) * sigma * y + S.diff(k, t, 3) * sigma**3 / 6
        w = (omega - S.diff(T, n) * A - h * C + S.diff(j, t) * y
             + S.diff(j, t, 2) * sigma**2 / 2 + S.diff(T, t) * sigma)
        theta = T + S.diff(j, t) * sigma - h * A
        z = 2 * t * y + sigma**2 + S.diff(k, t) * sigma + n
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        W = w + theta * X + (h * n + j) * X**2
        row = [S.diff(f, y) for f in (Y, Z, W + h * Y**2)]
        expected = [1, 2 * t, 2 * h * t * X**2 - h * S.diff(k, t) * X
                    + h * S.diff(k, t) * S.diff(k, t, 2) / 2 + S.diff(j, t)]
        for actual, wanted in zip(row, expected):
            self.assert_zero(actual - wanted)
            self.assert_zero(S.diff(actual, y))
        self.assertNotEqual(S.expand(S.diff(W, y, 2)), 0)

    def test_rebuilt_invariant_coordinate_and_both_inverses(self):
        X, Y, Z, W, I = S.symbols("X Y Z W I")
        t, n, y, sigma, h, q, j0, j1, j2, omega0 = S.symbols(
            "t n y sigma h q j0 j1 j2 omega0")
        j = j2 * t**2 / 2 + j1 * t + j0
        z = 2 * t * y + sigma**2 + n
        theta = q + (j2 * t + j1) * sigma - 2 * h * sigma * y
        w = -h * y**2 + j2 * z / 2 + j1 * y + omega0
        correction = h * (X**2 * Z - Y**2) + j2 * Z / 2 + j1 * Y + q * X + j0 * X**2
        forward, backward = W - correction, I + correction
        self.assert_zero(forward.subs(W, backward) - I)
        self.assert_zero(backward.subs(I, forward) - W)
        raw = {Y: y + sigma * X + t * X**2,
               Z: z + 2 * t * sigma * X + t**2 * X**2,
               W: w + theta * X + (h * n + j) * X**2}
        self.assert_zero(forward.subs(raw, simultaneous=True) - omega0)
        self.assert_zero(S.Matrix([X, Y, Z, forward]).jacobian([X, Y, Z, W]).det() - 1)
        wrong = W + h * (X**2 * Z - Y**2) - j2 * Z / 2 - j1 * Y - q * X - j0 * X**2
        self.assert_zero(S.expand(wrong.subs(raw, simultaneous=True) - omega0).coeff(X, 2) - 2 * h * n)


if __name__ == "__main__":
    unittest.main(verbosity=2)
