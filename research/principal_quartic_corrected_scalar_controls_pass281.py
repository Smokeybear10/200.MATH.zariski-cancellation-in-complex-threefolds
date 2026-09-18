"""Fresh independent finite controls of the corrected 281 scalar.

Includes a raw three-by-three determinant fixture, not just a replay of
the reduced formula. These tests cannot prove field return or recognition.
No saved checker is imported.
"""

import unittest

import sympy as S


class CorrectedQuarticScalarControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_discriminant_gradient_and_complete_generic_scalar(self):
        U, P, x = S.symbols("U P x")
        B, Bt, k1, k2, v = S.symbols("B Bt k1 k2 v")
        a2, a1, a0, a2t, a1t, a0t = S.symbols("a2 a1 a0 a2t a1t a0t")
        d, f, dt, ft, dn, fn = S.symbols("d f dt ft dn fn")
        C = a2 * P**2 + a1 * P + a0
        Ct = a2t * P**2 + a1t * P + a0t
        Cp = S.diff(C, P)
        Q = B * U**2 + C * U + (C**2 - d * P - f) / (4 * B)
        y = (x - C) / (2 * B)
        QP = S.diff(Q, P).subs(U, y)
        self.assert_zero(QP - (2 * x * Cp - d) / (4 * B))
        self.assert_zero(QP - (x * Cp - d) / (2 * B) - d / (4 * B))
        yn = ((dn * P + fn) / (2 * x) + v) / (2 * B)
        yt = ((dt * P + ft) / (2 * x) - Ct - 2 * Bt * y) / (2 * B)
        yp = (d / (2 * x) - Cp) / (2 * B)
        scalar = (2 * x / d) * (x * (-yt + (2 * y + k2 * P) * yn)
                               + QP * (yp - (2 * P + k1) * yn))
        scaled = S.cancel(4 * B**2 * d * scalar)
        remainder = S.rem(S.Poly(scaled, x), S.Poly(x**2 - d * P - f, x)).as_expr()
        odd = S.expand(remainder).coeff(x, 1)
        self.assert_zero(S.expand(odd).coeff(P, 3) + 6 * a2 * dn)
        self.assert_zero(S.expand(odd).coeff(P, 2)
                         - (2 * B * k2 * dn - 2 * a2 * k1 * dn - 6 * a2 * fn - 4 * a1 * dn))
        restricted = S.expand(remainder.subs({dn: 0, fn: 0}))
        odd = restricted.coeff(x, 1)
        self.assert_zero(odd - ((-2 * B * dt + (4 * Bt + 4 * a2 + 6 * v) * d) * P
                               - 2 * B * ft + 4 * Bt * f + 2 * a1 * d + d * k1 * v + 4 * f * v))
        rules = {
            Bt: a2 - v,
            a2t: (3 * a2**2 + 2 * a2 * v) / B,
            a1t: -k2 * v + k1 * a2 * v / B + 3 * a2 * a1 / B + a1 * v / B,
            a0t: (a1**2 + 2 * a2 * a0 + k1 * a1 * v) / (2 * B),
            dt: (4 * a2 + v) * d / B,
            ft: (2 * a2 * f + (a1 + k1 * v / 2) * d) / B,
        }
        self.assert_zero(restricted.subs(rules, simultaneous=True) + d**2 / 2)

    def test_raw_map_determinant_catches_old_factor(self):
        r, x, n = S.symbols("r x n", nonzero=True)
        t = r**2
        derivative = lambda value: S.diff(value, r) / (2 * r)
        k = 8 * r**3 / 3
        sigma = x**2 * r**4
        y = r * x / 2 + sigma**2 / (4 * r**2)
        z = n + 2 * t * y + sigma**2 + derivative(k) * sigma
        w = (-1 / (2 * r) - y**2 - derivative(derivative(k)) * sigma * y
             - derivative(derivative(derivative(k))) * sigma**3 / 6)
        raw = S.Matrix([[derivative(value), S.diff(value, n), S.diff(value, x)]
                        for value in (y, z, w)]).det()
        self.assert_zero(raw + 1 / (8 * r**2))
        self.assert_zero(raw + 1 / (4 * r**2) - 1 / (8 * r**2))
        self.assertNotEqual(S.cancel(raw + 1 / (4 * r**2)), 0)

    def test_actual_weighted_translation_and_corrected_integrations(self):
        X, Y, Z, Ystar, Zstar, tau = S.symbols("X Y Z Ystar Zstar tau")
        forward_y, forward_z = Y - tau * X**2, Z - 2 * tau * Y + tau**2 * X**2
        back_y, back_z = Ystar + tau * X**2, Zstar + 2 * tau * Ystar + tau**2 * X**2
        for value, expected in ((forward_y, Ystar), (forward_z, Zstar)):
            self.assert_zero(value.subs({Y: back_y, Z: back_z}, simultaneous=True) - expected)
        for value, expected in ((back_y, Y), (back_z, Z)):
            self.assert_zero(value.subs({Ystar: forward_y, Zstar: forward_z}, simultaneous=True) - expected)
        self.assert_zero(X**2 * forward_z - forward_y**2 - X**2 * Z + Y**2)
        t = S.symbols("t", nonzero=True)
        B, v = S.Function("B")(t), S.Function("v")(t)
        d0 = B**4
        self.assert_zero(B * S.diff(d0, t) - 4 * S.diff(B, t) * d0)
        d1, B1 = v**4 / t, -t * v
        self.assert_zero(B1 * S.diff(d1, t) - (4 * S.diff(B1, t) + 5 * v) * d1)
        old = v**5 / t**2
        self.assertNotEqual(S.factor(B1 * S.diff(old, t) - (4 * S.diff(B1, t) + 5 * v) * old), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
