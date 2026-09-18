"""Standalone finite controls for constant-sigma double-cover recognition307.

The raw surface and remainder are reconstructed here, with no retained-checker
imports. These symbolic tests do not certify the exact constant-field theorem,
relative algebraic closedness, the actual whole-field return, the double-cover
cofactor theorem, or the polynomial-entry theorem266. The separate mathematical
proof retains those gates. Only the coordinating parent may execute this file.
"""

import unittest

import sympy as sp


def raw_surface(t, s, U, P, V, k, n, ell):
    def taylor(expression, degree):
        return sum(
            sp.diff(expression, t, degree - i, s, i)
            * P ** (degree - i) * V**i
            / sp.factorial(degree - i) / sp.factorial(i)
            for i in range(degree + 1)
        )

    m = sp.diff(k, s)
    F = taylor(k, 2) + taylor(n, 1)
    D = (2 * P + sp.diff(k, t)) / m
    lam = sp.diff(F, V) / m
    w = (ell - (2 * P + sp.diff(k, t)) * U - F) / m
    H = (
        U**2 + sp.diff(F, P) * U + sp.diff(F, V) * w
        + taylor(k, 3) + taylor(n, 2)
        - sp.diff(ell, t) * P - sp.diff(ell, s) * V
    )
    A1 = sp.diff(H, U).subs(U, 0)
    A0 = H.subs(U, 0)
    e = (
        sp.diff(k, t, 2) - 2 * D * sp.diff(m, t)
        + D**2 * sp.diff(m, s)
    ) / 2
    R = sp.cancel(sp.diff(A0, P) - D * sp.diff(A0, V) + (lam - e) * A1)
    return H, R, e


def affine_data(t, s, c, d, eta):
    m = c * t + d
    f, n0, l1, l0 = (sp.Function(name)(t) for name in ("f", "n0", "l1", "l0"))
    k = m * s + f
    n = c**2 * s**2 / 4 + (c * sp.diff(f, t) / 2 - eta * m) * s + n0
    ell = c**2 * (eta - sp.diff(f, t, 2) / 4) * s**2 / 2 + l1 * s + l0
    C = -eta**2 * m + c * eta * sp.diff(f, t) / 2 - c * sp.diff(n0, t) / 2 - l1
    return m, f, n0, l1, l0, k, n, ell, C


class ConstantSigmaDoubleCoverControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.together(expression)), 0)

    def nonzero(self, expression):
        self.assertNotEqual(sp.cancel(sp.together(expression)), 0)

    def test_centered_surface_and_level_derivative(self):
        t, s, U, P, V, j = sp.symbols("t s U P V j")
        c, d, eta, h0, h0s = sp.symbols("c d eta h0 h0s")
        m, f, n0, l1, l0, k, n, ell_integrated, C_integrated = affine_data(t, s, c, d, eta)
        ell = sp.Function("ell")(t, s)
        H, _, e = raw_surface(t, s, U, P, V, k, n, ell)
        centered = sp.Poly(sp.expand(H.subs(U, j - c * V / 2)), j, V)
        A = centered.coeff_monomial(j)
        C = centered.coeff_monomial(V)
        B = centered.coeff_monomial(1)
        expected_C = (
            c**2 * (eta - sp.diff(f, t, 2) / 4) * s - eta**2 * m
            + c * eta * sp.diff(f, t) / 2 - c * sp.diff(n0, t) / 2
            - sp.diff(ell, s)
        )
        gamma = 2 * P + c * s + sp.diff(f, t)
        self.zero(centered.as_expr() - j**2 - A * j - C * V - B)
        self.zero(C - expected_C)
        self.zero(sp.diff(C, P))
        self.zero(A - (sp.diff(f, t, 2) * P + sp.diff(n, t) + eta * gamma - c * gamma**2 / (2 * m)))
        self.zero(sp.diff(A, s) - c * e)
        original_HV = sp.diff(H, V).subs(U, j - c * V / 2)
        self.zero(original_HV - c * j - c * A / 2 - C)

        # Formal coefficient derivatives precede restriction to the level.
        row = (sp.diff(H, s) - h0s - e * sp.diff(H, V)).subs(U, j - c * V / 2)
        on_level = sp.expand(row.subs(V, (h0 - j**2 - A * j - B) / C))
        self.zero(sp.Poly(on_level, j).coeff_monomial(j**2) + sp.diff(C, s) / C)
        integrated_row = row.subs(ell, ell_integrated).doit()
        Ai = A.subs(ell, ell_integrated).doit()
        Bi = B.subs(ell, ell_integrated).doit()
        self.zero(C.subs(ell, ell_integrated).doit() - C_integrated)
        self.zero(sp.diff(C_integrated, s))
        self.zero(integrated_row - (sp.diff(Bi, s) - h0s - e * (c * Ai / 2 + C_integrated)))
        # Missing the c*A/2 chain-rule term is a genuine generic error.
        incorrect = sp.diff(Bi, s) - h0s - e * C_integrated
        self.zero(integrated_row - incorrect + e * c * Ai / 2)
        self.nonzero(e * c * Ai / 2)
        # C=0 leaves a monic j-quadratic, not an actual affine parameter.
        self.zero(sp.Poly(j**2 + Ai * j + Bi - h0, j).LC() - 1)

    def test_moving_gamma_remainder_with_all_lower_derivatives(self):
        t, s, U, P, V, gamma = sp.symbols("t s U P V gamma")
        c, d, eta = sp.symbols("c d eta")
        m, f, n0, l1, l0, k, n, ell, C = affine_data(t, s, c, d, eta)
        _, R, _ = raw_surface(t, s, U, P, V, k, n, ell)
        self.zero(sp.diff(R, V))
        Rgamma = R.subs(P, (gamma - c * s - sp.diff(f, t)) / 2)
        self.zero(sp.diff(Rgamma, s) - sp.diff(C, t) + c * C / m)
        self.zero(sp.diff(Rgamma, s, gamma))
        self.zero(sp.Poly(sp.expand(R), P).coeff_monomial(P**3) + 4 * c**2 / m**2)
        self.zero(sp.Poly(sp.expand(R.subs(c, 0)), P).coeff_monomial(P**2) - sp.diff(f, t, 3) / 2)
        expanded_rhs = (
            c * eta * m * sp.diff(f, t, 2) - c * m * sp.diff(n0, t, 2)
            - 2 * m * sp.diff(l1, t) - c**2 * eta * sp.diff(f, t)
            + c**2 * sp.diff(n0, t) + 2 * c * l1
        ) / (2 * m)
        self.zero(sp.diff(C, t) - c * C / m - expanded_rhs)
        # A moving double root alone is insufficient: this violates (13).
        bad_remainder = (gamma - s)**2
        self.zero(sp.diff(bad_remainder, s, gamma) + 2)
        self.nonzero(sp.diff(bad_remainder, s, gamma))

    def test_full_actual_frames_and_polynomial_parameter_solves(self):
        t, s, X, j, theta, UU, VV = sp.symbols("t s X j theta UU VV")
        c, d, eta = sp.symbols("c d eta")
        m, f, n0, l1, l0, k, n, ell, C = affine_data(t, s, c, d, eta)
        sigma0 = sp.Function("sigma0")(t)
        sigma, y = -c * s / 2 + sigma0, j - c * theta / 2
        F = sp.diff(k, t, 2) * sigma**2 / 2 + c * sigma * theta + sp.diff(n, t) * sigma + sp.diff(n, s) * theta
        z = 2 * t * y + sigma**2 + sp.diff(k, t) * sigma + m * theta + n
        w = (ell - (2 * sigma + sp.diff(k, t)) * y - F) / m
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        D0 = (2 * sigma0 + sp.diff(f, t)) / m
        z00 = sigma0**2 + sp.diff(f, t) * sigma0 + n0
        w00 = (l0 - sp.diff(f, t, 2) * sigma0**2 / 2 - sp.diff(n0, t) * sigma0) / m
        u0 = z00 + (2 * m * sigma0 / c + f) * X + (t**2 + 2 * d * t / c) * X**2
        v0 = w00 + 2 * sigma0 * (X + eta) * X / c + 2 * t * (X + eta) * X**2 / c
        J = j - eta * c * s / 2
        Lcoef = 2 * (X + eta) / c - D0
        actual_U, actual_V = Z + 2 * d * Y / c, W + 2 * (X + eta) * Y / c
        self.zero(actual_U - 2 * m * J / c - u0)
        self.zero(actual_V - Lcoef * J + C * s / m - v0)
        Jback = c * (UU - u0) / (2 * m)
        sback = -m * (VV - Lcoef * Jback - v0) / C
        self.zero(2 * m * Jback / c + u0 - UU)
        self.zero(Lcoef * Jback - C * sback / m + v0 - VV)
        sp.Poly(sp.cancel(Jback), X, UU, VV)
        sp.Poly(sp.cancel(sback), X, UU, VV)
        self.zero(sp.det(sp.Matrix([[2 * m / c, 0], [Lcoef, -C / m]])) + 2 * C / c)
        YY, ZZ, WW = sp.symbols("YY ZZ WW")
        forwardU = ZZ + 2 * d * YY / c
        forwardV = WW + 2 * (X + eta) * YY / c
        backZ, backW = UU - 2 * d * YY / c, VV - 2 * (X + eta) * YY / c
        self.zero(forwardU.subs(ZZ, backZ) - UU)
        self.zero(forwardV.subs(WW, backW) - VV)
        self.zero(backZ.subs(UU, forwardU) - ZZ)
        self.zero(backW.subs(VV, forwardV) - WW)

        # A separate c=0 frame, never a specialization of an inverse with 1/c.
        Yc, Zc, Wc = (expression.subs(c, 0) for expression in (Y, Z, W))
        Cc, Dc = C.subs(c, 0), D0.subs(c, 0)
        v00 = w00.subs(c, 0) - (X + eta) * (z00 + (2 * t * sigma0 + f) * X + t**2 * X**2) / d
        Vc = Wc - (X + eta) * Zc / d
        Lc = -Dc - 2 * t * (X + eta) / d
        self.zero(Yc - j - sigma0 * X - t * X**2)
        self.zero(Vc - Lc * j + Cc * s / d - v00)
        yback = UU - sigma0 * X - t * X**2
        scback = -d * (VV - Lc * yback - v00) / Cc
        self.zero(yback + sigma0 * X + t * X**2 - UU)
        self.zero(Lc * yback - Cc * scback / d + v00 - VV)
        sp.Poly(sp.cancel(scback), X, UU, VV)
        self.zero((WW - (X + eta) * ZZ / d).subs(WW, VV + (X + eta) * ZZ / d) - VV)
        self.zero((VV + (X + eta) * ZZ / d).subs(VV, WW - (X + eta) * ZZ / d) - WW)

        # A nonzero determinant with an X factor gives only rational entry.
        Cbad, Lbad = sp.symbols("Cbad Lbad", nonzero=True)
        bad_s = (VV - Lbad * UU) / (Cbad * X)
        self.zero(Cbad * X * bad_s - VV + Lbad * UU)
        self.nonzero((VV - Lbad * UU).subs(X, 0))
        self.zero(sp.denom(sp.cancel(bad_s)).subs(X, 0))

    def test_zero_remainder_rebuild_and_actual_W_normalization(self):
        t, s, X, U, P, V, y, sigma, theta = sp.symbols("t s X U P V y sigma theta")
        m, kap, b, d0, nu = sp.symbols("m kap b d0 nu")
        f0 = sp.Function("f0")(t)
        ell = sp.Function("ell")(t, s)
        k = m * s + kap * t**2 / 2 + b * t + d0
        n = nu * s + f0
        H, R, _ = raw_surface(t, s, U, P, V, k, n, ell)
        F = kap * sigma**2 / 2 + sp.diff(f0, t) * sigma + nu * theta
        z = 2 * t * y + sigma**2 + sp.diff(k, t) * sigma + m * theta + n
        w = (ell - (2 * sigma + sp.diff(k, t)) * y - F) / m
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        theta_star = m * theta + (kap * t + b) * sigma + kap * k / 2
        nstar = n - kap * k / 2
        wstar = m * w + kap * z / 2 + b * y
        self.zero(m * W + kap * Z / 2 + b * Y + d0 * X**2 - wstar - theta_star * X - k * X**2)
        self.zero(z - 2 * t * y - sigma**2 - theta_star - nstar)
        nustar = nu / m - kap / 2
        ellstar = ell + kap * n / 2 + kap * nustar * k / 2
        dtstar = lambda expression: sp.diff(expression, t) - sp.diff(k, t) * sp.diff(expression, s) / m
        self.zero(sp.diff(nstar, s) / m - nustar)
        self.zero(wstar + 2 * sigma * y + dtstar(nstar) * sigma + nustar * theta_star - ellstar)
        WS, YY, ZZ, WW = sp.symbols("WS YY ZZ WW")
        forward = m * WW + kap * ZZ / 2 + b * YY + d0 * X**2
        inverse = (WS - kap * ZZ / 2 - b * YY - d0 * X**2) / m
        self.zero(forward.subs(WW, inverse) - WS)
        self.zero(inverse.subs(WS, forward) - WW)
        # Recompute the normalized remainder; old R=0 is not transported.
        g = sp.Function("g")(t)
        _, Rnew, _ = raw_surface(t, s, U, P, V, s, nu * s + g, ell)
        self.zero(Rnew - (sp.diff(g, t, 2) + 2 * sp.diff(ell, s)) * P + sp.diff(ell, t))
        self.assertLessEqual(sp.Poly(sp.expand(Rnew), P, V).total_degree(), 1)
        # Optional old-frame coefficient ledger, independent of the rebuild.
        ells = m * kap**2 / 4 - kap * nu / 2 - m * sp.diff(f0, t, 2) / 2
        ellt = kap**2 * sp.diff(k, t) / 4 - sp.diff(k, t) * sp.diff(f0, t, 2) / 2 - kap * sp.diff(f0, t) / 2
        self.zero(R.subs({sp.diff(ell, s): ells, sp.diff(ell, t): ellt}))
        self.zero(sp.diff(ells, t) - sp.diff(ellt, s) + m * sp.diff(f0, t, 3) / 2)


if __name__ == "__main__":
    unittest.main()
