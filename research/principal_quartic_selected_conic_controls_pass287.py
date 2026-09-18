"""Finite exact controls for the constant-discriminant conic in 287.

The constant chi is not the line parameter. No retained checker is
imported, and finite identities do not prove field return or recognition.
"""

import unittest

import sympy as S


class QuarticSelectedConicControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_complete_constant_discriminant_scalar(self):
        P, B, Bt, r, k1, k2, a2, a1, a0, a2t, a1t, a0t, chi, chit, chin = S.symbols(
            "P B Bt r k1 k2 a2 a1 a0 a2t a1t a0t chi chit chin")
        C = a2 * P**2 + a1 * P + a0
        Cp, Ct = S.diff(C, P), a2t * P**2 + a1t * P + a0t
        y = (chi - C) / (2 * B)
        yn = (chin + r) / (2 * B)
        yt = (chit - Ct - 2 * Bt * y) / (2 * B)
        yp = -Cp / (2 * B)
        scalar = chi * (-yt + (2 * y + k2 * P) * yn) + chi * Cp * (yp - (2 * P + k1) * yn) / (2 * B)
        rules = {
            Bt: a2 - r,
            a2t: (3 * a2**2 + 2 * a2 * r) / B,
            a1t: -k2 * r + k1 * a2 * r / B + 3 * a2 * a1 / B + a1 * r / B,
            a0t: (a1**2 + 2 * a2 * a0 + k1 * a1 * r) / (2 * B),
        }
        reduced = S.expand(scalar.subs(rules, simultaneous=True))
        self.assert_zero(S.expand(4 * B**2 * reduced / chi).coeff(P, 2) + 6 * a2 * chin)
        self.assert_zero(reduced.subs(chin, 0) - chi * (a2 * chi - B * chit) / (2 * B**2))

    def test_constant_p_literal_cubic_with_all_correction_constants(self):
        B, alpha, beta, gamma, h, p, v1, t, n, k1, ell, om, sigma, chi, T = S.symbols(
            "B alpha beta gamma h p v1 t n k1 ell om sigma chi T")
        y = chi / (2 * B) + alpha * T**2 / 4 - gamma / 2
        k2, k3 = 2 * (B - p) / h, -alpha * B**3 / h
        c1 = p * k1 + 2 * t * v1 + 2 * beta * B / alpha + ell
        c2 = p * k2 + 2 * v1 - beta * B**3
        a0 = gamma * B - beta**2 * B**3 / (2 * alpha)
        q1 = v1 * k1 - a0
        v0 = beta * gamma * B / alpha - beta**3 * B**3 / (6 * alpha**2) + om
        z = 2 * t * y + sigma**2 + k1 * sigma + n
        w = (v1 * n + v0 - p * ((2 * sigma + k1) * y + k2 * sigma**2 / 2)
             - h * (y**2 + k2 * sigma * y + k3 * sigma**3 / 6)
             + c1 * y + c2 * sigma**2 / 2 + q1 * sigma)
        W0 = (w - v1 * z + h * y**2 - ell * y - om).subs(sigma, T / B + beta / alpha)
        Y0 = y + gamma / 2
        self.assert_zero(W0 + 2 * T * Y0 - alpha * T**3 / 6)
        self.assert_zero(alpha * T**3 - 12 * Y0 * T - 6 * W0)
        U, V = S.symbols("U V")
        formal = alpha * T**3 - 12 * U * T - 6 * V
        self.assertEqual(S.degree(formal, T), 3)
        self.assertEqual(S.degree(formal, V), 1)
        self.assertEqual(S.gcd(S.diff(formal, V), formal.subs(V, 0)), 1)

    def test_direct_slope_shortcut_and_actual_pencil(self):
        t, B, r, h, p, k1, k2, c2, v1, a1 = S.symbols("t B r h p k1 k2 c2 v1 a1")
        slope_prime = c2 - r * k1 - p * k2 - 2 * v1 - t * a1 * r / B
        expected = -a1 * (1 + t * r / B)
        self.assert_zero((slope_prime - expected).subs(a1, p * k2 - c2 + k1 * r + 2 * v1))
        self.assert_zero(expected.subs(B, -t * r))
        X, Y, sigma, chi, a2, q1, q, c, c1, k3, v0 = S.symbols("X Y sigma chi a2 q1 q c c1 k3 v0")
        y = Y - sigma * X - t * X**2
        n = -2 * t * y + (a2 * sigma**2 + a1 * sigma + k1 * v1 - q1 - chi) / r
        w = (v1 * n + v0 - p * ((2 * sigma + k1) * y + k2 * sigma**2 / 2)
             - h * (y**2 + k2 * sigma * y + k3 * sigma**3 / 6)
             + c1 * y + c2 * sigma**2 / 2 + (r * n + q1) * sigma)
        theta = p * n + q + c1 * sigma - h * ((2 * sigma + k1) * y + k2 * sigma**2 / 2)
        W = w + theta * X + (h * n + c) * X**2
        J = W + h * Y**2 + (h * k1 + 2 * t * p) * X * Y - (c1 - p * k1 - 2 * t * v1) * Y
        self.assert_zero(S.diff(J, Y).subs(k2, -2 * (p + t * r) / h))


if __name__ == "__main__":
    unittest.main(verbosity=2)
