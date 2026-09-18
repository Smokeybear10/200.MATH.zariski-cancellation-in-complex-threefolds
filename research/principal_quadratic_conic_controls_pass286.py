"""Finite controls of 286's quadratic scalar and actual degree lowering.

No retained checker imports. Field return and the nonzero-r three-ring
endpoint are separate written arguments, not conclusions of these tests.
"""

import unittest

import sympy as S


class QuadraticConicControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_complete_two_parameter_scalar_and_sequential_gates(self):
        x, B, r, b, bt, C0, k1, k2, d, f, dt, ft, dn, fn = S.symbols(
            "x B r b bt C0 k1 k2 d f dt ft dn fn")
        sigma = (x**2 - f) / d
        sx = 2 * x / d
        sn, st = -(fn + sigma * dn) / d, -(ft + sigma * dt) / d
        y = (x - b * sigma - C0) / (2 * B)
        C0t = k1 * (bt + r * k2) / 2 + b**2 / (2 * B)
        yn = (-b * sn + r) / (2 * B)
        yt = (-bt * sigma - b * st - C0t + 2 * r * y) / (2 * B)
        yx = (1 - b * sx) / (2 * B)
        gamma, B1 = 2 * sigma + k1, 2 * y + k2 * sigma
        DU = (B1 * yn - yt) * sx + (st - B1 * sn) * yx
        DP = (1 + gamma * sn) * yx - gamma * yn * sx
        scalar = x * DU + (b * x / (2 * B) - d / (4 * B)) * DP
        scalar = S.expand(scalar.subs(bt, dn / (2 * B) - r * k2 + b * r / B))
        self.assert_zero(scalar.coeff(x, 4) - 5 * dn / (4 * B**2 * d**2))
        self.assert_zero(S.expand(scalar.subs(dn, 0)).coeff(x, 2) - 3 * fn / (4 * B**2 * d))
        gate = B * dt - r * d
        expected = (-gate * x**3 / (2 * B**2 * d**2)
                    + (-2 * B * d * ft + 2 * gate * f + (2 * b + r * k1) * d**2)
                    * x / (4 * B**2 * d**2) - d / (8 * B**2))
        self.assert_zero(scalar.subs({dn: 0, fn: 0}) - expected)
        self.assert_zero(expected.subs({dt: r * d / B, ft: (2 * b + r * k1) * d / (2 * B)}, simultaneous=True)
                         + d / (8 * B**2))

    def test_constant_r_zero_actual_shear_retains_pn(self):
        X, Y, Z, W, V = S.symbols("X Y Z W V")
        t, n, y, sigma, h, p, q, q1, c0, c1, c2, omega = S.symbols(
            "t n y sigma h p q q1 c0 c1 c2 omega")
        c = c2 * t**2 / 2 + c1 * t + c0
        z = 2 * t * y + sigma**2 + n
        theta = p * n + q + (c2 * t + c1) * sigma - 2 * h * sigma * y
        w = omega - 2 * p * sigma * y - h * y**2 + (c2 * t + c1) * y + c2 * sigma**2 / 2 + q1 * sigma
        raw = {Y: y + sigma * X + t * X**2,
               Z: z + 2 * t * sigma * X + t**2 * X**2,
               W: w + theta * X + (h * n + c) * X**2}
        correction = h * (X**2 * Z - Y**2) + c2 * Z / 2 + c1 * Y + c0 * X**2
        forward, backward = W - correction, V + correction
        literal = S.expand(forward.subs(raw, simultaneous=True))
        expected = omega - c2 * n / 2 - 2 * p * sigma * y + q1 * sigma + (p * n + q) * X
        self.assert_zero(literal - expected)
        self.assert_zero(forward.subs(W, backward) - V)
        self.assert_zero(backward.subs(V, forward) - W)
        self.assert_zero(literal.coeff(X, 1) - q - p * n)
        self.assertNotEqual(S.expand(literal.coeff(X, 1) - q), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
