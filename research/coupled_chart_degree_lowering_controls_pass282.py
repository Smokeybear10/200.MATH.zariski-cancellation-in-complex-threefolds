"""Finite algebra controls for the new degree-lowering part of282.

These verify coefficient identities and a literal ambient shear, not
the historical recognition chain or the universal cofactor case split.
No other checker is imported.
"""

import unittest

import sympy as S


class CoupledChartDegreeLoweringControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_reciprocal_and_fourth_derivative_gate(self):
        t = S.symbols("t")
        m = S.Function("m")(t)
        e = 1 / m
        M = S.diff(m, t, 2) / 2 - S.diff(m, t)**2 / m
        self.assert_zero(S.diff(e, t, 2) + 2 * e**2 * M)
        alpha, beta = S.symbols("alpha beta")
        e = alpha * t + beta
        m = 1 / e
        q, r = S.Function("q")(t), S.Function("r")(t)
        a4 = (S.diff(q, t, 4) - m * S.diff(r, t, 4) - 4 * S.diff(q, t, 3) * S.diff(m, t) / m) / 24
        R = r - e * q
        self.assert_zero(S.diff(R, t, 4) + 24 * e * a4)
        self.assert_zero(S.diff(m, t, 2) / 2 - S.diff(m, t)**2 / m)

    def test_full_actual_monic_shear_degree_and_both_inverses(self):
        t, X, Y, Z, W, Wstar = S.symbols("t X Y Z W Wstar")
        y, z, w, theta, lam, k = S.symbols("y z w theta lam k")
        alpha, beta = S.symbols("alpha beta")
        r0, r1, r2, r3 = S.symbols("r0 r1 r2 r3")
        q = S.Function("q")(t)
        e = alpha * t + beta
        R = r0 + r1 * t + r2 * t**2 + r3 * t**3
        r = e * q + R
        PR = r0 * X**3 + r1 * X**2 * Y + r2 * X * Y**2 + r3 * Y**3
        correction = (alpha * Y + beta * X) * Z + PR
        forward, backward = W - correction, Wstar + correction
        self.assert_zero(forward.subs(W, backward) - Wstar)
        self.assert_zero(backward.subs(Wstar, forward) - W)
        self.assert_zero(S.Matrix([X, Y, Z, forward]).jacobian([X, Y, Z, W]).det() - 1)
        raw = {
            Y: y + t * X,
            Z: z + (S.diff(q, t) * y + k) * X + q * X**2,
            W: w + theta * X + (S.diff(r, t) * y + lam) * X**2 + r * X**3,
        }
        literal = S.expand(forward.subs(raw, simultaneous=True))
        self.assertLessEqual(S.Poly(literal, X).degree(), 2)
        self.assert_zero(S.diff(literal, X, 3))
        self.assert_zero(PR.subs({X: 1, Y: t}, simultaneous=True) - R)
        self.assert_zero(literal.subs(X, 0) - w + alpha * y * z + r3 * y**3)
        # The actual coefficient field may be arbitrary; only the leader cancels.
        self.assertTrue(literal.has(q, S.diff(q, t), k, lam))
        omitted = S.expand((W - (alpha * Y + beta * X) * Z).subs(raw, simultaneous=True))
        self.assert_zero(S.Poly(omitted, X).nth(3) - R)
        self.assertEqual(S.Poly(omitted, X).nth(3).subs({r0: 1, r1: 0, r2: 0, r3: 0}), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
