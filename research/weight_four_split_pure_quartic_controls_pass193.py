"""Finite exact controls for the conditional pure-quartic split proof193.

This standalone source does not import a proof or another checker. Its
unrestricted coefficient functions are formal differential inputs, not
claimed actual polynomial frames. Exact field return, the pencil lemma,
constant-field descent, and the published recognition theorem remain
written-proof inputs. These finite identities do not certify cancellation.

Source-only authorship: no execution, import, or compilation by the author.
"""

import unittest

import sympy as sp


class SplitPureQuarticControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.together(expression)), 0)

    def test_general_q_elimination_and_exact_partial_change(self):
        t, rho, U, V = sp.symbols("t rho U V")
        alpha, beta, c = sp.symbols("alpha beta c")
        chi = alpha * t + beta
        r = 1 / chi
        q = sp.Function("q")(t)
        k0 = sp.Function("k0")(t)
        n0 = sp.Function("n0")(t)
        ell = sp.Function("ell")(t, rho)
        m = sp.Function("m")(t, rho)
        k = r * rho + k0
        n = c * r**2 * rho + n0
        Q = sp.diff(q, t, 2) / 2
        d = sp.diff(q, t, 3) / 6
        S = (
            d * U**3 + sp.diff(k, t, 2) * U**2 / 2
            + sp.diff(r, t) * U * V + sp.diff(n, t) * U
            + c * r**2 * V
        )
        Vpot = (
            sp.diff(d, t) * U**4 / 4
            + sp.diff(k, t, 3) * U**3 / 6
            + sp.diff(r, t, 2) * U**2 * V / 2
            + sp.diff(n, t, 2) * U**2 / 2
            + sp.diff(c * r**2, t) * U * V
        )
        H = (
            r * (Vpot - sp.diff(ell, t) * U
                 - sp.diff(ell, rho) * V - m)
            + (sp.diff(r, t) * U + c * r**2) * (ell - S)
        )
        Hpoly = sp.Poly(sp.expand(H), U, V)
        omega = -r * sp.diff(ell, rho) - c**2 * r**4
        self.assertEqual(Hpoly.degree(V), 1)
        self.assert_zero(Hpoly.coeff_monomial(V) - omega)
        self.assert_zero(Hpoly.coeff_monomial(U * V))
        self.assert_zero(Hpoly.coeff_monomial(U**2 * V))

        D = chi * sp.diff(d, t) / 4 + alpha * d
        F3 = chi * sp.diff(k0, t, 3) / 6 + alpha * sp.diff(k0, t, 2) / 2 - c * d
        F2 = chi * sp.diff(n0, t, 2) / 2 + alpha * sp.diff(n0, t) - c * sp.diff(k0, t, 2) / 2
        F = D * U**4 + F3 * U**3 + F2 * U**2
        p = (
            (-chi * d - alpha * Q) * U**3
            + (c * Q - chi * sp.diff(k0, t, 2) / 2
               - alpha * sp.diff(k0, t)) * U**2
            + (c * sp.diff(k0, t) - chi * sp.diff(n0, t)
               - alpha * n0) * U
        )
        h = chi * ell + c**2 * r**2 * rho + c * n0
        hp, ht = sp.diff(h, rho), sp.diff(h, t)
        z_literal = Q * U**2 + sp.diff(k, t) * U + r * V + n
        w_literal = (ell - S) / r
        self.assert_zero(w_literal - (alpha * U - c) * z_literal - p - h)
        self.assert_zero(sp.diff(p, t) + sp.diff(F, U))
        self.assert_zero(hp + omega / r**2)
        self.assert_zero(Hpoly.coeff_monomial(U**4) - r**2 * D)

        # Clear h_rho before solving H=0. This checks every z coefficient
        # and the old/new t-partial correction, without setting h_rho=1.
        H0 = H.subs(V, 0)
        solved_z_times_hp = hp * (Q * U**2 + sp.diff(k, t) * U + n) + H0 / r
        predicted_z_times_hp = (
            r * F + hp * Q * U**2
            + (hp * sp.diff(k, t) - r * ht) * U
            + hp * n - m + c * r * ell
        )
        self.assert_zero(solved_z_times_hp - predicted_z_times_hp)

        zt, zr, zu, zv, pt, pu, htj, hpj = sp.symbols(
            "zt zr zu zv pt pu htj hpj", nonzero=True
        )
        matrix = sp.Matrix([
            [0, 0, 1],
            [zt, zr, zu],
            [(alpha * U - c) * zt + pt + htj,
             (alpha * U - c) * zr + hpj,
             (alpha * U - c) * zu + alpha * zv + pu],
        ])
        old_J = matrix.det()
        self.assert_zero(old_J - (hpj * zt - (pt + htj) * zr))
        zth, zh, aE, Gamma = sp.symbols("zth zh aE Gamma", nonzero=True)
        changed = old_J.subs({zt: zth + htj * zh, zr: hpj * zh}, simultaneous=True)
        self.assert_zero(changed - hpj * (zth - pt * zh))
        # The normalized determinant is -aE^3/Gamma, not -aE^3.
        calibrated_delta = -aE**3 / (Gamma * hpj)
        self.assert_zero(hpj * calibrated_delta + aE**3 / Gamma)

    def test_scalar_coefficients_split_cases_and_unfixed_pencil_slope(self):
        t, h, U = sp.symbols("t h U")
        r = sp.Function("r")(t)
        rho = sp.Function("rho")(t, h)
        k0 = sp.Function("k0")(t)
        D, F3, F2, Q = [sp.Function(name)(t) for name in ("D", "F3", "F2", "Q")]
        z0 = sp.Function("z0")(t, h)
        F = D * U**4 + F3 * U**3 + F2 * U**2
        FU = sp.diff(F, U)
        pre_z = r * sp.diff(rho, h) * F + Q * U**2 + sp.diff(r * rho + k0, t) * U + z0
        pre_scalar = sp.Poly(sp.expand(sp.diff(pre_z, t) + FU * sp.diff(pre_z, h)), U)
        self.assert_zero(pre_scalar.coeff_monomial(U**7) - 4 * r * D**2 * sp.diff(rho, h, 2))

        T, u0 = sp.Function("T")(t), sp.Function("u0")(t)
        z = T * F + Q * U**2 + (sp.diff(T, t) * h + u0) * U + z0
        scalar = sp.Poly(sp.expand(sp.diff(z, t) + FU * sp.diff(z, h)), U)
        expected = {
            4: 5 * D * sp.diff(T, t) + sp.diff(D, t) * T,
            3: T * sp.diff(F3, t) + 4 * sp.diff(T, t) * F3 + 4 * D * sp.diff(z0, h),
            2: sp.diff(Q, t) + T * sp.diff(F2, t) + 3 * sp.diff(T, t) * F2 + 3 * F3 * sp.diff(z0, h),
            1: sp.diff(T, t, 2) * h + sp.diff(u0, t) + 2 * F2 * sp.diff(z0, h),
            0: sp.diff(z0, t),
        }
        self.assertEqual(scalar.degree(), 4)
        for power, value in expected.items():
            self.assert_zero(scalar.coeff_monomial(U**power) - value)

        alpha, beta, A, B = sp.symbols("alpha beta A B")
        split_D = -alpha - beta / t**5
        split_T = A * t + B
        split_p3 = 4 * alpha * t + beta - beta / t**4
        residual = 5 * split_D * sp.diff(split_T, t) + sp.diff(split_D, t) * split_T
        self.assert_zero(residual - (-5 * alpha * A + 5 * beta * B / t**6))
        for branch in ({alpha: 0, B: 0}, {beta: 0, A: 0}):
            self.assert_zero(residual.subs(branch, simultaneous=True))
        self.assertNotEqual(sp.cancel(residual.subs({alpha: 1, beta: 1, A: 1, B: 1})), 0)
        self.assert_zero(sp.diff(split_p3.subs(alpha, 0), t) - 4 * beta / t**5)
        self.assert_zero(sp.diff(split_p3.subs(beta, 0), t) - 4 * alpha)
        g4 = split_T * split_D - A * split_p3
        self.assert_zero(g4.subs({alpha: 0, B: 0}, simultaneous=True) + beta * A)
        self.assert_zero(g4.subs({beta: 0, A: 0}, simultaneous=True) + alpha * B)

        b = sp.Function("b")(t)  # Deliberately not constant in this control.
        p3, p2, p1 = [sp.Function(name)(t) for name in ("p3", "p2", "p1")]
        relations = {
            sp.diff(p3, t): -4 * D,
            sp.diff(p2, t): -3 * F3,
            sp.diff(p1, t): -2 * F2,
        }
        g3 = split_T * F3 - A * p2 - b * p3
        g2 = Q + split_T * F2 - A * p1 - b * p2
        g1 = u0 - b * p1
        scalar3 = split_T * sp.diff(F3, t) + 4 * A * F3 + 4 * D * b
        scalar2 = sp.diff(Q, t) + split_T * sp.diff(F2, t) + 3 * A * F2 + 3 * F3 * b
        scalar1 = sp.diff(u0, t) + 2 * F2 * b
        for gj, pj, residual_j in ((g3, p3, scalar3), (g2, p2, scalar2), (g1, p1, scalar1)):
            self.assert_zero((sp.diff(gj, t) + pj * sp.diff(b, t)).subs(relations, simultaneous=True) - residual_j)

    def test_unified_original_columns_inverse_and_determinant_transport(self):
        X, Y, Z, W, I, J, t, y = sp.symbols("X Y Z W I J t y")
        alpha, beta, A, B, b, c = sp.symbols("alpha beta A B b c")
        chi, T = alpha * t + beta, A * t + B
        r = 1 / chi
        Ychart = y + t * X
        zh = A * y + b
        theta_h = chi * zh + (alpha * y - c) * T
        # Literal k_t here is the old rho-fixed partial; its h derivative
        # is r' rho_h. This check retains that distinct derivative.
        rho_h = chi * T
        self.assert_zero(r * theta_h - (zh - sp.diff(r, t) * rho_h * y - c * r**2 * rho_h))
        Z_h = zh + T * X
        W_h = 1 + (alpha * y - c) * zh + theta_h * X + rho_h * X**2
        B0 = A * Y + B * X + b
        lam = alpha * Y + beta * X - c
        self.assert_zero(Z_h - B0.subs(Y, Ychart))
        self.assert_zero(W_h - (1 + lam * B0).subs(Y, Ychart))

        Q0 = sp.Function("Q0")(X, Y)
        Jmap = W - lam * Z
        Istar = Z - B0 * Jmap
        Imap = Istar - Q0
        Zback = I + Q0 + B0 * J
        Wback = J + lam * Zback
        self.assert_zero(Zback.subs({I: Imap, J: Jmap}, simultaneous=True) - Z)
        self.assert_zero(Wback.subs({I: Imap, J: Jmap}, simultaneous=True) - W)
        self.assert_zero(Imap.subs({Z: Zback, W: Wback}, simultaneous=True) - I)
        self.assert_zero(Jmap.subs({Z: Zback, W: Wback}, simultaneous=True) - J)
        self.assert_zero(sp.Matrix([Y, Istar, Jmap]).jacobian([Y, Z, W]).det() - 1)
        h_column = {Z: B0, W: 1 + lam * B0}
        self.assert_zero(sum(sp.diff(Jmap, slot) * value for slot, value in h_column.items()) - 1)
        self.assert_zero(sum(sp.diff(Istar, slot) * value for slot, value in h_column.items()))

        Ft, Fy, Jt, Jy, rhot, rhoh = sp.symbols("Ft Fy Jt Jy rhot rhoh")
        new_J = sp.Matrix([[X, 1, 0], [Ft, Fy, 0], [Jt, Jy, 1]]).det()
        self.assert_zero(new_J - (X * Fy - Ft))
        change = sp.Matrix([[1, 0, 0], [rhot, 0, rhoh], [0, 1, 0]]).det()
        self.assert_zero(change + rhoh)
        aE, Gamma = sp.symbols("aE Gamma", nonzero=True)
        self.assert_zero((-aE**3 / Gamma) * change - aE**3 * rhoh / Gamma)

        # A generic transported correction, not an assumed actual frame.
        g0 = sp.Function("g0")(t)
        transported = g0 + Q0.subs(Y, Ychart)
        self.assert_zero(sp.diff(transported, t) - X * sp.diff(transported, y) - sp.diff(g0, t))


if __name__ == "__main__":
    unittest.main()
