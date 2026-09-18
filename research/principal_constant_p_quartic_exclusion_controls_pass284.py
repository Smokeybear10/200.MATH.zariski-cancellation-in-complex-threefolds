"""Finite exact controls for 284, with all displayed constants retained.

The universal irreducibility and strong-field-return contradiction remain
written arguments. No retained checker is imported.
"""

import unittest

import sympy as S


class ConstantPQuarticExclusionControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_complete_coefficient_integrations(self):
        B, alpha, beta, gamma, delta, phi, omega = S.symbols(
            "B alpha beta gamma delta phi omega")
        derivative = lambda value: -alpha * B**3 * S.diff(value, B) / 2
        Bt = derivative(B)
        a1 = beta * B**3
        a0 = gamma * B - beta**2 * B**3 / (2 * alpha)
        d = delta * B**4
        f = phi * B**2 - beta * delta * B**4 / alpha
        v0 = -(delta - 2 * beta * gamma) * B / (2 * alpha) - beta**3 * B**3 / (6 * alpha**2) + omega
        self.assert_zero(derivative(a1) - 3 * Bt * a1 / B)
        self.assert_zero(derivative(a0) - (a1**2 + 2 * Bt * a0) / (2 * B))
        self.assert_zero(derivative(d) - 4 * Bt * d / B)
        self.assert_zero(B * derivative(f) - 2 * Bt * f - a1 * d)
        self.assert_zero(d - 2 * a1 * a0 - 4 * B * derivative(v0))
        self.assert_zero(derivative(2 * beta * B / alpha) + beta * B**3)

    def test_literal_intercept_correction_and_quartic(self):
        B, alpha, beta, gamma, delta, h, p, v1 = S.symbols("B alpha beta gamma delta h p v1")
        t, n, k1, ell, omega, sigma, xi, Svar, phi = S.symbols("t n k1 ell omega sigma xi Svar phi")
        y = xi / 2 + alpha * Svar**2 / 4 - gamma / 2
        k2, k3 = 2 * (B - p) / h, -alpha * B**3 / h
        a0 = gamma * B - beta**2 * B**3 / (2 * alpha)
        c1 = p * k1 + 2 * t * v1 + 2 * beta * B / alpha + ell
        c2 = p * k2 + 2 * v1 - beta * B**3
        q1 = v1 * k1 - a0
        v0 = -(delta - 2 * beta * gamma) * B / (2 * alpha) - beta**3 * B**3 / (6 * alpha**2) + omega
        z = 2 * t * y + sigma**2 + k1 * sigma + n
        w = (v1 * n + v0 - p * ((2 * sigma + k1) * y + k2 * sigma**2 / 2)
             - h * (y**2 + k2 * sigma * y + k3 * sigma**3 / 6)
             + c1 * y + c2 * sigma**2 / 2 + q1 * sigma)
        corrected = (w - v1 * z + h * y**2 - ell * y - omega).subs(sigma, Svar / B + beta / alpha)
        Y0 = y + gamma / 2
        expected = -2 * Svar * Y0 + alpha * Svar**3 / 6 - delta * B / (2 * alpha)
        self.assert_zero(corrected - expected)
        relation = alpha**2 * Svar**4 - 24 * alpha * Y0 * Svar**2 - 24 * alpha * expected * Svar - 48 * Y0**2 + 12 * phi
        self.assert_zero(relation - 12 * (delta * B * Svar - xi**2 + phi))
        # Clearing the completed-square identity gives the quartic exactly.
        self.assert_zero(relation.subs(phi, xi**2 - delta * B * Svar))

    def test_primitive_polynomial_and_intercept_inverse(self):
        U, V, T, alpha, phi = S.symbols("U V T alpha phi")
        relation = alpha**2 * T**4 - 24 * alpha * U * T**2 - 24 * alpha * V * T - 48 * U**2 + 12 * phi
        coefficient_ring = S.QQ.frac_field(alpha, phi)
        coefficient_v = S.diff(relation, V)
        constant_v = relation.subs(V, 0)
        self.assertEqual(S.Poly(S.gcd(S.Poly(coefficient_v, U, T, domain=coefficient_ring),
                                      S.Poly(constant_v, U, T, domain=coefficient_ring)), U, T).total_degree(), 0)
        self.assertEqual(S.Poly(relation, T).degree(), 4)
        self.assertEqual(S.Poly(relation, V).degree(), 1)
        y, z, w, Y0, W0, gamma, v1, h, ell, omega = S.symbols("y z w Y0 W0 gamma v1 h ell omega")
        forward_y = y + gamma / 2
        forward_w = w - v1 * z + h * y**2 - ell * y - omega
        back_y = Y0 - gamma / 2
        back_w = W0 + v1 * z - h * back_y**2 + ell * back_y + omega
        self.assert_zero(forward_y.subs(y, back_y) - Y0)
        self.assert_zero(forward_w.subs({y: back_y, w: back_w}, simultaneous=True) - W0)
        self.assert_zero(back_y.subs(Y0, forward_y) - y)
        self.assert_zero(back_w.subs({Y0: forward_y, W0: forward_w}, simultaneous=True) - w)


if __name__ == "__main__":
    unittest.main(verbosity=2)
