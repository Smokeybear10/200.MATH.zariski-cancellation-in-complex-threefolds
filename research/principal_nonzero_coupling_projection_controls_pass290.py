"""Finite algebra controls for290, not actual cancellation examples.

The countercontrol deliberately FAILS the full Jacobian condition. No
solver, proof source, or completed checker is imported.
"""

import unittest

import sympy as s


class NonzeroCouplingProjectionControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_formal_covector_identity(self):
        gamma, m, b1, c1, gt, gs = s.symbols("gamma m b1 c1 gt gs", nonzero=True)
        dy, dp, dv, dt, ds = s.symbols("dy dp dv dt ds")
        lam = c1 / m
        dg = -gamma * dy / m - b1 * dp / m - c1 * dv / m + gt * dt + gs * ds
        row_a = dy + lam * dp + lam**2 * dt
        row_c = dg + lam * dv + lam**2 * ds
        hu = b1 - gamma * c1 / m
        hp = -m * gt - c1 * b1 / m
        hv = -m * gs - c1**2 / m
        self.assert_zero(row_c + gamma * row_a / m + (hu * (dp + lam * dt) + hp * dt + hv * ds) / m)

    def test_uniform_boundary_family_and_inverse(self):
        t, ss, x, X = s.symbols("t ss x X")
        q = s.Function("q")(x)
        sigma = x**2 - ss
        theta = q + 6 * ss * x**2 - ss**2 + ss
        y = x
        w = t - 2 * sigma * x
        z = 2 * t * x + sigma**2 + theta
        s_return = z - 2 * y * w - 5 * y**4 - q
        t_return = w + 2 * y**3 - 2 * s_return * y
        self.assert_zero(s_return - ss)
        self.assert_zero(t_return - t)
        y0, z0, w0 = s.symbols("y0 z0 w0")
        inverse_s = z0 - 2 * y0 * w0 - 5 * y0**4 - s.Function("q")(y0)
        inverse_t = w0 + 2 * y0**3 - 2 * inverse_s * y0
        inverse_subs = {t: inverse_t, ss: inverse_s, x: y0}
        self.assert_zero(z.subs(inverse_subs, simultaneous=True) - z0)
        self.assert_zero(w.subs(inverse_subs, simultaneous=True) - w0)
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + ss) * X + t**2 * X**2
        W = w + theta * X + ss * X**2
        jacobian = s.Matrix([Y, Z, W]).jacobian([t, ss, x]).det()
        expected = -1 - (12 * ss * x + s.diff(q, x) + 1) * X
        self.assert_zero(jacobian - expected)
        self.assert_zero(s.expand(jacobian).coeff(X, 0) + 1)
        self.assert_zero(x**2 - sigma - ss)


if __name__ == "__main__":
    unittest.main(verbosity=2)
