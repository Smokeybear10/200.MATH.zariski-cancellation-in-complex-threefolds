"""Finite raw-determinant and actual-coordinate controls for 283.

These do not prove the whole-line classification or retained recognition
theorem. No saved checker is imported.
"""

import unittest

import sympy as S


class CubicAndConicControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_cubic_raw_determinant_and_top_obstruction(self):
        t, n, P, h = S.symbols("t n P h")
        c1, c2, c3, c4, q1, q2, q3, om, om1, om2, D, Dt, Dn = S.symbols(
            "c1 c2 c3 c4 q1 q2 q3 om om1 om2 D Dt Dn")
        t_jets = {c1: c2, c2: c3, c3: c4, q1: q2, q2: q3,
                  om: om1, om1: om2, D: Dt}
        partial_t = lambda value: S.diff(value, t) + sum(
            jet * S.diff(value, variable) for variable, jet in t_jets.items())
        partial_n = lambda value: S.diff(value, n) + Dn * S.diff(value, D)
        y = -c3 * P**3 / (6 * q1) - q2 * P**2 / (2 * q1) - (c3 * n / 2 + om1) * P / q1 + D
        z = 2 * t * y + P**2 + n
        w = -h * y**2 + c1 * y + c2 * (P**2 + n) / 2 + q1 * P + om
        raw = S.Matrix([[partial_t(value), partial_n(value), S.diff(value, P)]
                        for value in (y, z, w)]).det(method="domain-ge")
        psi = c3 * (P**2 + n) / 2 + q2 * P + om1
        reduced = q1 * partial_t(y) - 2 * q1 * y * partial_n(y) + 2 * P * psi * partial_n(y) + psi**2 / q1
        self.assert_zero(raw - reduced)
        self.assert_zero(S.expand(reduced).coeff(P, 4) + 5 * c3**2 / (12 * q1))
        self.assertEqual(S.Poly(S.expand(reduced), P).degree(), 4)
        self.assert_zero(S.diff(S.expand(reduced).coeff(P, 4), Dn))

    def test_conic_full_actual_shear_and_inverse(self):
        X, Y, Z, W, V = S.symbols("X Y Z W V")
        t, n, y, sigma, h, c0, c1, c2, q, q1, omega = S.symbols(
            "t n y sigma h c0 c1 c2 q q1 omega")
        c = c2 * t**2 / 2 + c1 * t + c0
        z = 2 * t * y + sigma**2 + n
        theta = q + (c2 * t + c1) * sigma - 2 * h * sigma * y
        w = -h * y**2 + (c2 * t + c1) * y + c2 * (sigma**2 + n) / 2 + q1 * sigma + omega
        raw = {Y: y + sigma * X + t * X**2,
               Z: z + 2 * t * sigma * X + t**2 * X**2,
               W: w + theta * X + (h * n + c) * X**2}
        correction = h * (X**2 * Z - Y**2) + c2 * Z / 2 + c1 * Y + c0 * X**2
        forward, backward = W - correction, V + correction
        self.assert_zero(forward.subs(raw, simultaneous=True) - omega - q1 * sigma - q * X)
        self.assert_zero(forward.subs(W, backward) - V)
        self.assert_zero(backward.subs(V, forward) - W)
        omitted = W - correction + c0 * X**2
        self.assert_zero(S.expand(omitted.subs(raw, simultaneous=True)).coeff(X, 2) - c0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
