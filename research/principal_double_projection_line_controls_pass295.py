"""Finite algebra controls for the held double-projection reduction295.

This standalone source imports no retained checker. It reconstructs the
formal surface before extracting the remainder, and checks the actual
polynomial W reframe in both directions.

These tests do not prove the exact-field odd-module lemma, the pure-top
plane theorem, the universal minor-unit theorem296, the shift bounds, or
any recognition claim. The final fixture deliberately separates those
structural conditions from the actual corrected-potential identities.
Only the coordinating parent is authorized to execute this saved suite.
"""

import unittest

import sympy as sp


def raw_jets():
    """Independent coefficient jets through the third potential."""
    U, P, V = sp.symbols("U P V")
    names = (
        "m mt ms k1 k2 k3 mtt mts mss "
        "nt ns ntt nts nss ell ellt ells h0"
    )
    jets = dict(zip(names.split(), sp.symbols(names)))
    m, mt, ms = (jets[name] for name in ("m", "mt", "ms"))
    k1, k2, k3 = (jets[name] for name in ("k1", "k2", "k3"))
    F = (
        k2 * P**2 / 2 + mt * P * V + ms * V**2 / 2
        + jets["nt"] * P + jets["ns"] * V
    )
    gamma = 2 * P + k1
    D = gamma / m
    lam = sp.diff(F, V) / m
    w = (jets["ell"] - gamma * U - F) / m
    taylor3 = (
        k3 * P**3 / 6 + jets["mtt"] * P**2 * V / 2
        + jets["mts"] * P * V**2 / 2 + jets["mss"] * V**3 / 6
    )
    taylor2 = (
        jets["ntt"] * P**2 / 2 + jets["nts"] * P * V
        + jets["nss"] * V**2 / 2
    )
    H = (
        U**2 + sp.diff(F, P) * U + sp.diff(F, V) * w
        + taylor3 + taylor2 - jets["ellt"] * P - jets["ells"] * V
    )
    # Reconstruct from the corrected gradient, not from the printed R table.
    QU = sp.diff(H, P) - D * sp.diff(H, V) + lam * sp.diff(H, U)
    e = sp.diff(QU, U) / 2
    A1 = sp.diff(H, U).subs(U, 0)
    R = sp.expand(QU.subs(U, 0) - e * A1)
    return U, P, V, jets, H, QU, e, R


def homogeneous_part(expr, degree, *variables):
    poly = sp.Poly(sp.expand(expr), *variables)
    return sp.expand(sum(
        coefficient * sp.prod(var**power for var, power in zip(variables, powers))
        for powers, coefficient in poly.terms()
        if sum(powers) == degree
    ))


class DoubleProjectionLineControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.together(expression)), 0)

    def nonzero(self, expression):
        self.assertNotEqual(sp.cancel(sp.together(expression)), 0)

    def test_raw_remainder_coefficients_and_factor_boundaries(self):
        U, P, V, j, H, QU, e, R = raw_jets()
        m, mt, ms = (j[name] for name in ("m", "mt", "ms"))
        k1, k2, k3 = (j[name] for name in ("k1", "k2", "k3"))
        mtt = j["mtt"]
        D = (2 * P + k1) / m
        self.zero(sp.diff(QU, U, 2))
        self.zero(e - (k2 - 2 * D * mt + D**2 * ms) / 2)
        self.assertLessEqual(sp.Poly(sp.expand(H), U, P, V).total_degree(), 3)
        self.assertLessEqual(sp.Poly(R, P, V).total_degree(), 4)
        top = 4 * P**3 * ms * (mt * P + ms * V) / m**3
        self.zero(homogeneous_part(R, 4, P, V) - top)
        # Generic m_s != 0: exact multiplicities three and one.
        self.zero(sp.cancel(top / P**3).subs(P, 0) - 4 * ms**2 * V / m**3)
        self.nonzero(sp.cancel(top / P**3).subs(P, 0))
        self.zero(top.subs(V, -mt * P / ms))
        self.nonzero(sp.diff(top, V).subs(V, -mt * P / ms))
        # Specializing m_s to zero destroys the degree-four part.
        self.zero(top.subs(ms, 0))

        no_s = {ms: 0, j["mts"]: 0, j["mss"]: 0}
        reduced = sp.Poly(sp.expand(R.subs(no_s)), P, V)
        self.assertLessEqual(reduced.total_degree(), 3)
        self.zero(
            reduced.coeff_monomial(P**3) + (m * mtt + 4 * mt**2) / m**2
        )
        self.zero(
            reduced.coeff_monomial(P * V)
            - (m * mtt + mt**2 - 2 * j["nss"]) / m
        )
        printed_p2 = (
            -k1 * m**2 * mtt - 8 * k1 * m * mt**2
            + 5 * k2 * m**2 * mt + k3 * m**3
            - 4 * m**2 * j["nts"] - 8 * m * mt * j["ns"]
        ) / (2 * m**3)
        self.zero(reduced.coeff_monomial(P**2) - printed_p2)
        constant_m = {mt: 0, mtt: 0, j["nss"]: 0}
        self.zero(reduced.coeff_monomial(V).subs(constant_m) - j["nts"])
        self.zero(
            reduced.coeff_monomial(P**2).subs(constant_m)
            - k3 / 2 + 2 * j["nts"] / m
        )

    def test_differentiated_ode_and_nonconstant_fifth_root_control(self):
        _, P, V, j, _, _, _, R = raw_jets()
        t, s = sp.symbols("t s")
        M = sp.Function("M")(t)
        k0 = sp.Function("k0")(t)
        j0 = sp.Function("j0")(t)
        j1 = sp.Function("j1")(t)
        # Integrate only the n_ss equation, leaving both t-functions arbitrary.
        nss = (M * sp.diff(M, t, 2) + sp.diff(M, t)**2) / 2
        k = M * s + k0
        n = nss * s**2 / 2 + j1 * s + j0
        substitution = {
            j["m"]: M, j["mt"]: sp.diff(M, t), j["ms"]: 0,
            j["mtt"]: sp.diff(M, t, 2), j["mts"]: 0, j["mss"]: 0,
            j["k1"]: sp.diff(k, t), j["k2"]: sp.diff(k, t, 2),
            j["k3"]: sp.diff(k, t, 3),
            j["nt"]: sp.diff(n, t), j["ns"]: sp.diff(n, s),
            j["ntt"]: sp.diff(n, t, 2), j["nts"]: sp.diff(n, t, s),
            j["nss"]: sp.diff(n, s, 2),
        }
        raw_p2 = sp.Poly(R, P, V).coeff_monomial(P**2)
        differentiated = sp.diff(raw_p2.subs(substitution, simultaneous=True), s)
        expected = -(
            M**2 * sp.diff(M, t, 3)
            + 6 * M * sp.diff(M, t) * sp.diff(M, t, 2)
            + 12 * sp.diff(M, t)**3
        ) / (2 * M**2)
        self.zero(differentiated - expected)
        ode_substitution = {
            sp.diff(M, t, 2): -4 * sp.diff(M, t)**2 / M,
            sp.diff(M, t, 3): 36 * sp.diff(M, t)**3 / M**2,
        }
        self.zero(
            differentiated.subs(ode_substitution, simultaneous=True)
            + 12 * sp.diff(M, t)**3 / M**2
        )
        self.zero(
            sp.diff(M * sp.diff(M, t, 2) + 4 * sp.diff(M, t)**2, t)
            .subs(ode_substitution, simultaneous=True)
        )
        # Exact algebraic mode t=r^5: the first ODE alone is insufficient.
        r = sp.symbols("r", nonzero=True)
        dt = lambda expression: sp.diff(expression, r) / (5 * r**4)
        mode, mode_t = r, dt(r)
        mode_tt, mode_ttt = dt(mode_t), dt(dt(mode_t))
        self.zero(mode * mode_tt + 4 * mode_t**2)
        obstruction = -(
            mode**2 * mode_ttt + 6 * mode * mode_t * mode_tt + 12 * mode_t**3
        ) / (2 * mode**2)
        self.zero(obstruction + 12 / (125 * r**14))
        self.nonzero(obstruction)

    def test_literal_actual_w_reframe_and_derivative_convention(self):
        X, Y, Z, W, Wstar = sp.symbols("X Y Z W Wstar")
        t, s, y, sigma, theta = sp.symbols("t s y sigma theta")
        m = sp.symbols("m", nonzero=True)
        kap, b, d, nu = sp.symbols("kap b d nu")
        f0 = sp.Function("f0")(t)
        ell = sp.Function("ell")(t, s)
        forward = m * W + kap * Z / 2 + b * Y + d * X**2
        inverse = (Wstar - kap * Z / 2 - b * Y - d * X**2) / m
        self.zero(inverse.subs(Wstar, forward) - W)
        self.zero(forward.subs(W, inverse) - Wstar)
        self.zero(sp.diff(forward, Z) - kap * sp.diff(forward, W) / (2 * m))
        self.zero(sp.diff(forward, W) / m - 1)

        k = m * s + kap * t**2 / 2 + b * t + d
        kt = sp.diff(k, t)
        n = nu * s + f0
        F = kap * sigma**2 / 2 + sp.diff(f0, t) * sigma + nu * theta
        w = (ell - (2 * sigma + kt) * y - F) / m
        z = 2 * t * y + sigma**2 + kt * sigma + m * theta + n
        Yraw = y + sigma * X + t * X**2
        Zraw = z + (2 * t * sigma + k) * X + t**2 * X**2
        Wraw = w + theta * X + s * X**2
        full_star = forward.subs({Y: Yraw, Z: Zraw, W: Wraw}, simultaneous=True)
        theta_star = m * theta + kt * sigma + kap * k / 2
        w_star = m * w + kap * z / 2 + b * y
        n_star = n - kap * k / 2
        nu_star = nu / m - kap / 2
        self.zero(full_star - w_star - theta_star * X - k * X**2)
        self.zero(z - 2 * t * y - sigma**2 - theta_star - n_star)
        self.zero(
            n_star - nu_star * k
            - f0 + (nu / m) * (kap * t**2 / 2 + b * t + d)
        )
        dt_star = lambda expression: sp.diff(expression, t) - kt * sp.diff(expression, s) / m
        ds_star = lambda expression: sp.diff(expression, s) / m
        self.zero(dt_star(k))
        self.zero(ds_star(k) - 1)
        self.zero(ds_star(n_star) - nu_star)
        ell_star = ell + kap * n / 2 + kap * nu_star * k / 2
        self.zero(
            w_star + 2 * sigma * y + dt_star(n_star) * sigma
            + nu_star * theta_star - ell_star
        )
        # Using the old t partial in the new coefficient basis is generally wrong.
        wrong = (
            w_star + 2 * sigma * y + sp.diff(n_star, t) * sigma
            + nu_star * theta_star - ell_star
        )
        self.zero(wrong - kt * nu_star * sigma)
        self.nonzero(wrong)
        self.zero(
            sp.det(sp.Matrix([t, k]).jacobian([t, s])) - m
        )
        # Actual row determinant multiplies by m, base reparameterization divides by m.
        self.zero(sp.diff(forward, W) / sp.det(sp.Matrix([t, k]).jacobian([t, s])) - 1)

    def test_normalized_remainder_and_affine_fourth_gradient(self):
        U, P, V, t, s = sp.symbols("U P V t s")
        nu, alpha, beta, delta, ell0 = sp.symbols("nu alpha beta delta ell0")
        f = sp.Function("f")(t)
        ell = sp.Function("ell")(t, s)
        h0 = sp.Function("h0")(t, s)
        F = sp.diff(f, t) * P + nu * V
        w = ell - 2 * P * U - F
        H = (
            U**2 + sp.diff(F, P) * U + sp.diff(F, V) * w
            + sp.diff(f, t, 2) * P**2 / 2
            - sp.diff(ell, t) * P - sp.diff(ell, s) * V
        )
        gradient = sp.Matrix([
            sp.diff(H, P) - 2 * P * sp.diff(H, V) + nu * sp.diff(H, U),
            sp.diff(H, t) - sp.diff(h0, t)
            - (2 * U + sp.diff(F, P)) * sp.diff(H, V) + nu * sp.diff(H, P),
            sp.diff(H, s) - sp.diff(h0, s),
        ])
        self.zero(
            gradient[0] - (sp.diff(f, t, 2) + 2 * sp.diff(ell, s)) * P
            + sp.diff(ell, t)
        )
        fq = alpha * t**2 / 2 + beta * t + delta
        ellq = -alpha * s / 2 + ell0
        substitution = {f: fq, ell: ellq}
        Hq = H.subs(substitution, simultaneous=True).doit()
        expected_H = (
            U**2 + (sp.diff(fq, t) - 2 * nu * P) * U
            - nu * sp.diff(fq, t) * P + alpha * P**2 / 2
            + (alpha / 2 - nu**2) * V + nu * ellq
        )
        self.zero(Hq - expected_H)
        actual_gradient = gradient.subs(substitution, simultaneous=True).doit()
        expected_gradient = sp.Matrix([
            0, -sp.diff(h0, t) - alpha * sp.diff(fq, t) / 2,
            -sp.diff(h0, s) - nu * alpha / 2,
        ])
        for residual in actual_gradient - expected_gradient:
            self.zero(residual)
        Q = expected_gradient[1] * P + expected_gradient[2] * V
        self.assertLessEqual(sp.Poly(Q, U, P, V).total_degree(), 1)
        for variable, entry in zip((U, P, V), expected_gradient):
            self.zero(sp.diff(Q, variable) - entry)
        # This formal choice annihilates Q's gradient and is forbidden by the actual
        # minor-unit theorem. Do not infer nonvanishing from generic coefficients.
        h0_bad = -alpha * fq / 2 - nu * alpha * s / 2
        for entry in actual_gradient:
            self.zero(entry.subs(h0, h0_bad).doit())

    def test_formal_double_cover_minor_fixture_and_raw_identity_boundary(self):
        U, P, V, x = sp.symbols("U P V x")
        c, eta = sp.symbols("c eta", nonzero=True)
        e, gamma = sp.symbols("e gamma")
        G = V - P**2
        H = U**2 - c**2 * P
        Q = e * H + eta * G + gamma * G**2
        point = {U: c * x, P: x**2, V: x**4}
        self.zero(H.subs(point, simultaneous=True))
        self.zero(Q.subs(point, simultaneous=True))
        self.assertEqual(sp.Poly(H, U, P, V).total_degree(), 2)
        self.assertEqual(sp.Poly(Q, U, P, V).total_degree(), 4)
        gradH = sp.Matrix([sp.diff(H, variable) for variable in (U, P, V)])
        gradQ = sp.Matrix([sp.diff(Q, variable) for variable in (U, P, V)])
        minors = {
            (i, j): sp.expand(gradH[i] * gradQ[j] - gradH[j] * gradQ[i])
            .subs(point, simultaneous=True)
            for i, j in ((0, 1), (0, 2), (1, 2))
        }
        self.zero(minors[(1, 2)] + c**2 * eta)
        self.nonzero(minors[(1, 2)])  # Already a coefficient-field unit.
        # Even this conic fixture with unit minors is not a chart296 fourth
        # potential for k=s,n=0,ell=c²t: then Q_U must equal H_P=-c².
        self.zero(sp.diff(Q, U) - 2 * e * U)
        self.nonzero(sp.diff(Q, U) - sp.diff(H, P))
        # Bounded odd-module calculation underlying the extra square in R.
        a0, a1, a2, r0, r1, s0, s1 = sp.symbols("a0 a1 a2 r0 r1 s0 s1")
        y = a0 + a1 * x**2 + a2 * x**4 + c * x
        cofactor = (r0 + r1 * x**2) * y + s0 + s1 * x**2
        odd_part = sp.expand((cofactor - cofactor.subs(x, -x)) / 2)
        self.zero(odd_part - c * x * (r0 + r1 * x**2))
        self.nonzero(odd_part)


if __name__ == "__main__":
    unittest.main()
