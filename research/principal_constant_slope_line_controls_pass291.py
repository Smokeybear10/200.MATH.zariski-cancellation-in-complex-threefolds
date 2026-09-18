"""Finite exact identities for291, not a proof of cancellation.

This standalone checker imports no project solver or prior checker. It
tests the formal gradient, moving-line scalar, and full coordinate
transport. It does not certify coefficient-field intersections, actual
coordinate entry, local nilpotence, or the imported recognition theorems.
"""

import unittest

import sympy as s


class ConstantSlopeLineControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_high_gradient_coefficients(self):
        t, n, U, P = s.symbols("t n U P")
        h, slope, intercept = s.symbols("h slope intercept", nonzero=True)
        k, c = s.Function("k")(t), s.Function("c")(t)
        T, omega = s.Function("T")(t, n), s.Function("omega")(t, n)
        aa = (2 * P + s.diff(k, t)) * U + s.diff(k, t, 2) * P**2 / 2
        cc = U**2 + s.diff(k, t, 2) * P * U + s.diff(k, t, 3) * P**3 / 6
        raw = (omega - s.diff(T, n) * aa - h * cc + s.diff(c, t) * U
               + s.diff(c, t, 2) * P**2 / 2 + s.diff(T, t) * P)
        qu = (2 * P + s.diff(k, t)) * s.diff(raw, n) - s.diff(raw, P)
        coefficient = s.expand(qu.subs(U, slope * P + intercept)).coeff(P, 3)
        self.assert_zero(coefficient + (4 * slope + s.diff(k, t, 2)) * s.diff(T, n, 2))
        p, q = s.Function("p")(t), s.Function("q")(t)
        raw_affine = raw.subs(T, p * n + q).doit()
        qp = (2 * U + s.diff(k, t, 2) * P) * s.diff(raw_affine, n) - s.diff(raw_affine, t)
        coefficient = s.expand(qp.subs(U, slope * P + intercept)).coeff(P, 3)
        self.assert_zero(coefficient - h * s.diff(k, t, 4) / 6)

    def test_complete_formal_primitive(self):
        t, n, U, P = s.symbols("t n U P")
        h = s.symbols("h", nonzero=True)
        k, c, p, q = [s.Function(name)(t) for name in ("k", "c", "p", "q")]
        omega = s.Function("omega")(t, n)
        k1, k2, k3, k4 = [s.diff(k, t, j) for j in range(1, 5)]
        aa = (2 * P + k1) * U + k2 * P**2 / 2
        cc = U**2 + k2 * P * U + k3 * P**3 / 6
        raw = (omega - p * aa - h * cc + s.diff(c, t) * U
               + s.diff(c, t, 2) * P**2 / 2 + (s.diff(p, t) * n + s.diff(q, t)) * P)
        B = h * k2 / 2 + p
        a2 = h * k3 / 2 + 2 * s.diff(p, t)
        a1 = p * k2 - s.diff(c, t, 2) + k1 * s.diff(p, t) + 2 * s.diff(omega, n)
        a0 = -n * s.diff(p, t) + k1 * s.diff(omega, n) - s.diff(q, t)
        d3 = (p * k3 - s.diff(c, t, 3) + 3 * k2 * s.diff(p, t)) / 6
        d2 = -n * s.diff(p, t, 2) / 2 + k2 * s.diff(omega, n) / 2 - s.diff(q, t, 2) / 2
        primitive = (B * U**2 + (a2 * P**2 + a1 * P + a0) * U
                     + h * k4 * P**4 / 24 + d3 * P**3 + d2 * P**2 - s.diff(omega, t) * P)
        self.assert_zero(s.diff(primitive, U) - ((2 * P + k1) * s.diff(raw, n) - s.diff(raw, P)))
        self.assert_zero(s.diff(primitive, P) - ((2 * U + k2 * P) * s.diff(raw, n) - s.diff(raw, t)))

    def test_moving_line_scalar(self):
        t, n, P = s.symbols("t n P")
        slope, intercept = s.Function("A")(t, n), s.Function("C")(t, n)
        k1, k2, st, sn, sv = s.symbols("k1 k2 sigma_t sigma_n sigma_v")
        y = slope * P + intercept
        yt = s.diff(y, t) + slope * st
        yn = s.diff(y, n) + slope * sn
        yv = slope * sv
        gamma, b1 = 2 * P + k1, 2 * y + k2 * P
        du = (b1 * yn - yt) * sv + (st - b1 * sn) * yv
        dp = (1 + gamma * sn) * yv - gamma * yn * sv
        ell = 4 * slope + k2
        scalar = (ell * s.diff(slope, n) * P**2
                  + (ell * s.diff(intercept, n) + (2 * intercept + slope * k1) * s.diff(slope, n)
                     - s.diff(slope, t)) * P
                  + (2 * intercept + slope * k1) * s.diff(intercept, n)
                  - s.diff(intercept, t) - slope**2)
        self.assert_zero(du - slope * dp - sv * scalar)

    def test_nonzero_r_compatibility_and_full_transport(self):
        B, r, slope, k2 = s.symbols("B r slope k2", nonzero=True)
        a1 = -2 * B * slope
        v1prime = a1 * r / (2 * B)
        a1prime = -r * k2 + 2 * v1prime
        slopeprime = r * (4 * slope + k2) / (2 * B)
        self.assert_zero(a1prime - (2 * r * slope - 2 * B * slopeprime))
        self.assert_zero(2 * B * (slopeprime / (4 * slope + k2)) - r)

        t, y, P, X = s.symbols("t y P X")
        h, r = s.symbols("h r", nonzero=True)
        p, k, k1, c, c1, q, q1, v0, v1, a1, chi = s.symbols("p k k1 c c1 q q1 v0 v1 a1 chi")
        k2 = 2 * (-t * r - p) / h
        k3 = -4 * r / h
        c2 = p * k2 + k1 * r + 2 * v1 - a1
        n = -2 * t * y + (a1 * P + k1 * v1 - q1 - chi) / r
        aa = (2 * P + k1) * y + k2 * P**2 / 2
        cc = y**2 + k2 * P * y + k3 * P**3 / 6
        z = 2 * t * y + P**2 + k1 * P + n
        w = v1 * n + v0 - p * aa - h * cc + c1 * y + c2 * P**2 / 2 + (r * n + q1) * P
        theta = p * n + q + c1 * P - h * aa
        H = h * n + c
        Y = y + P * X + t * X**2
        Z = z + (2 * t * P + k) * X + t**2 * X**2
        W = w + theta * X + H * X**2
        kappa = h * k1 + 2 * t * p
        lam = c1 - p * k1 - 2 * t * v1
        J = W + h * Y**2 + kappa * X * Y - lam * Y
        self.assert_zero(s.diff(z, y))
        self.assert_zero(s.diff(w, y) - (-2 * h * y + lam))
        self.assert_zero(s.diff(theta, y) + kappa + 2 * h * P)
        self.assert_zero(s.diff(Z, y))
        self.assert_zero(s.diff(J, y))
        self.assert_zero(h * k2 + 2 * p + 2 * t * r)
        self.assert_zero(-a1 - 2 * t * a1 * r / (2 * (-t * r)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
