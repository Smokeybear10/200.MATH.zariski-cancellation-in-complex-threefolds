"""Standalone finite controls for the held double-cover line note303.

No retained checker is imported. These tests reconstruct the formal surface,
discriminant and corrected U-gradient, the literal invariant family, and the
two actual auxiliary coordinate changes. They do not certify the exact-field
projection theorem, the universal minor-unit theorem, normality, or BGL3.5.
Only the coordinating parent may execute this saved suite.
"""

import unittest

import sympy as sp


def raw_surface():
    U, P, V = sp.symbols("U P V")
    names = "m mt ms mtt mts mss kt ktt kttt nt ns ntt nts nss ell ellt ells h0"
    j = dict(zip(names.split(), sp.symbols(names)))
    m = j["m"]
    F = (
        j["ktt"] * P**2 / 2 + j["mt"] * P * V + j["ms"] * V**2 / 2
        + j["nt"] * P + j["ns"] * V
    )
    D = (2 * P + j["kt"]) / m
    lam = sp.diff(F, V) / m
    w = (j["ell"] - (2 * P + j["kt"]) * U - F) / m
    H3 = (
        j["kttt"] * P**3 / 6 + j["mtt"] * P**2 * V / 2
        + j["mts"] * P * V**2 / 2 + j["mss"] * V**3 / 6
    )
    H2 = j["ntt"] * P**2 / 2 + j["nts"] * P * V + j["nss"] * V**2 / 2
    H = (
        U**2 + sp.diff(F, P) * U + sp.diff(F, V) * w + H3 + H2
        - j["ellt"] * P - j["ells"] * V
    )
    A1 = sp.diff(H, U).subs(U, 0)
    A0 = H.subs(U, 0) - j["h0"]
    discriminant = sp.expand(A1**2 - 4 * A0)
    QU = sp.diff(H, P) - D * sp.diff(H, V) + lam * sp.diff(H, U)
    e = sp.diff(QU, U) / 2
    R = sp.expand(QU.subs(U, 0) - e * A1)
    return U, P, V, j, A1, discriminant, R


class DoubleCoverLineControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.together(expression)), 0)

    def nonzero(self, expression):
        self.assertNotEqual(sp.cancel(sp.together(expression)), 0)

    def test_trace_and_nonconstant_sigma_remainder(self):
        _, P, V, j, A1, _, R = raw_surface()
        r = sp.symbols("r")
        p1, p0, q1, q0 = sp.symbols("p1 p0 q1 q0")
        m, mt = j["m"], j["mt"]
        no_s = {j["ms"]: 0, j["mts"]: 0, j["mss"]: 0}
        trace = sp.expand(
            A1.subs(no_s).subs({P: p1 * r + p0, V: q1 * r + q0}, simultaneous=True)
        )
        self.zero(sp.Poly(trace, r).coeff_monomial(r**2) + 2 * mt * p1**2 / m)
        # A quadratic trace cannot have linear discriminant against a cubic A0.
        a2, a1, a0, b3, b2, b1, b0 = sp.symbols("a2 a1 a0 b3 b2 b1 b0")
        Delta = (a2 * r**2 + a1 * r + a0)**2 - 4 * (
            b3 * r**3 + b2 * r**2 + b1 * r + b0
        )
        self.zero(sp.Poly(Delta, r).coeff_monomial(r**4) - a2**2)
        constant_m = {**no_s, mt: 0, j["mtt"]: 0}
        reduced = sp.Poly(sp.expand(R.subs(constant_m)), P, V)
        self.assertLessEqual(reduced.total_degree(), 2)
        self.zero(
            reduced.coeff_monomial(P**2) - j["kttt"] / 2 + 2 * j["nts"] / m
        )
        self.zero(reduced.coeff_monomial(P * V) + 2 * j["nss"] / m)
        self.zero(reduced.coeff_monomial(V**2))
        # Finite coefficient fixture for the missing V² in a squared non-P line.
        A, B, slope, multiplier = sp.symbols("A B slope multiplier")
        difference = P * (A * P + B * V) - multiplier * (V - slope * P)**2
        self.zero(sp.Poly(difference, P, V).coeff_monomial(V**2) + multiplier)

    def test_constant_sigma_coefficients_and_constant_ratio(self):
        _, P, V, j, _, Delta, R = raw_surface()
        m, mt, ms, mss = (j[name] for name in ("m", "mt", "ms", "mss"))
        self.zero(
            sp.Poly(Delta, V).coeff_monomial(V**3)
            + 2 * (m * mss - 3 * ms**2) / (3 * m)
        )
        self.zero(
            sp.Poly(sp.diff(R, P), V).coeff_monomial(V**2)
            + (m * mss - ms**2) / m**2
        )
        # The two cubic/quadratic equations disagree unless m_s=0.
        self.zero((m * mss - ms**2) - (m * mss - 3 * ms**2) - 2 * ms**2)
        no_s = {ms: 0, j["mts"]: 0, mss: 0}
        Dr = sp.Poly(sp.expand(Delta.subs(no_s)), V)
        Rr = sp.expand(R.subs(no_s))
        self.zero(Dr.coeff_monomial(V**2) - mt**2 + 2 * j["nss"])
        self.zero(
            sp.Poly(sp.diff(Rr, P), V).coeff_monomial(V)
            - (m * j["mtt"] + mt**2 - 2 * j["nss"]) / m
        )
        final = {j["mtt"]: 0, j["nss"]: mt**2 / 2}
        Rv = sp.Poly(Rr, V).coeff_monomial(V).subs(final)
        expected = (
            j["kt"] * mt**2 - j["ktt"] * m * mt
            + 2 * m * j["nts"] - 2 * mt * j["ns"]
        ) / (2 * m)
        self.zero(Rv - expected)
        self.zero(sp.diff(Rv, P))
        eta = (mt * j["kt"] / 2 - j["ns"]) / m
        eta_t = (
            sp.diff(eta, m) * mt + sp.diff(eta, j["kt"]) * j["ktt"]
            + sp.diff(eta, j["ns"]) * j["nts"]
        )
        eta_s = sp.diff(eta, j["kt"]) * mt + sp.diff(eta, j["ns"]) * mt**2 / 2
        self.zero(eta_s)
        self.zero(eta_t + Rv / m)

    def test_full_invariant_family_and_actual_inverse(self):
        X, t, s, y, sigma, theta = sp.symbols("X t s y sigma theta")
        nu, alpha, beta, delta, ell0 = sp.symbols("nu alpha beta delta ell0")
        f = alpha * t**2 / 2 + beta * t + delta
        z = 2 * t * y + sigma**2 + theta + nu * s + f
        w = -alpha * s / 2 + ell0 - 2 * sigma * y - sp.diff(f, t) * sigma - nu * theta
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + s) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        Y0, Z0, W0 = Y + beta / 2, Z - delta, W - ell0
        eps = alpha / 2 - nu**2
        invariant = Y0**2 + (alpha / 2 - X**2) * Z0 + (X + nu) * W0
        expected = (
            (y + beta / 2 + alpha * t / 2 - nu * sigma)**2
            + eps * (sigma**2 + theta)
        )
        self.zero(invariant - expected)
        for power in range(1, 5):
            self.zero(sp.Poly(sp.expand(invariant), X).coeff_monomial(X**power))
        YY, ZZ, WW, II, VV = sp.symbols("YY ZZ WW II VV")
        Iforward = YY**2 + (alpha / 2 - X**2) * ZZ + (X + nu) * WW
        Vforward = WW - (X - nu) * ZZ
        Zback = (II - YY**2 - (X + nu) * VV) / eps
        Wback = VV + (X - nu) * Zback
        self.zero(Iforward.subs({ZZ: Zback, WW: Wback}, simultaneous=True) - II)
        self.zero(Vforward.subs({ZZ: Zback, WW: Wback}, simultaneous=True) - VV)
        self.zero(Zback.subs({II: Iforward, VV: Vforward}, simultaneous=True) - ZZ)
        self.zero(Wback.subs({II: Iforward, VV: Vforward}, simultaneous=True) - WW)
        degenerate = YY**2 + (X + nu) * VV
        self.assertEqual(sp.Poly(degenerate, VV).degree(), 1)
        self.nonzero(sp.diff(degenerate, VV))
        self.zero(
            expected.subs(alpha, 2 * nu**2)
            - (y + beta / 2 + nu**2 * t - nu * sigma)**2
        )
        # Normality and the impossibility of a polynomial square of odd degree
        # are human proof steps, not asserted consequences of this finite test.

    def test_actual_auxiliary_two_good_frames(self):
        X, x, t, s, sigma = sp.symbols("X x t s sigma")
        a, tau, q1 = sp.symbols("a tau q1", nonzero=True)
        c, d, eta, D0, b0, q0, z0, w0, k = sp.symbols("c d eta D0 b0 q0 z0 w0 k")
        m = c * t + d
        theta = q1 * x**2 + q0
        y = -c * theta / 2 + b0 + tau * x
        lam = c * D0 / 2 - eta
        z = 2 * t * y + m * theta + z0
        w = -D0 * y - lam * theta + w0
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        deriv = lambda expression: a * sp.diff(expression, x)
        row = (-c / 2, d, X + eta)
        for expression, factor in zip((Y, Z, W), row):
            self.zero(deriv(deriv(expression)) - a**2 * 2 * q1 * factor)
            self.zero(deriv(deriv(deriv(expression))))
        U = Z + 2 * d * Y / c
        V = W + 2 * (X + eta) * Y / c
        self.zero(deriv(U) - 2 * a * m * tau / c)
        self.zero(deriv(V) - a * tau * (2 * (X + eta) / c - D0))
        self.zero(deriv(deriv(U)))
        self.zero(deriv(deriv(V)))
        YY, ZZ, WW, UU, VV = sp.symbols("YY ZZ WW UU VV")
        forwardU = ZZ + 2 * d * YY / c
        forwardV = WW + 2 * (X + eta) * YY / c
        backZ = UU - 2 * d * YY / c
        backW = VV - 2 * (X + eta) * YY / c
        self.zero(forwardU.subs(ZZ, backZ) - UU)
        self.zero(forwardV.subs(WW, backW) - VV)
        self.zero(backZ.subs(UU, forwardU) - ZZ)
        self.zero(backW.subs(VV, forwardV) - WW)

        Yc, Zc, Wc = (expression.subs(c, 0) for expression in (Y, Z, W))
        Vc = Wc - (X + eta) * Zc / d
        self.zero(deriv(Yc) - a * tau)
        self.zero(deriv(Vc) + a * tau * (D0 + 2 * t * (X + eta) / d))
        self.zero(deriv(deriv(Yc)))
        self.zero(deriv(deriv(Vc)))
        inverse_c = VV + (X + eta) * ZZ / d
        self.zero((WW - (X + eta) * ZZ / d).subs(WW, inverse_c) - VV)
        self.zero(inverse_c.subs(VV, WW - (X + eta) * ZZ / d) - WW)
        # The c != 0 inverse is not used at c=0. No auxiliary slice is inferred.


if __name__ == "__main__":
    unittest.main()
