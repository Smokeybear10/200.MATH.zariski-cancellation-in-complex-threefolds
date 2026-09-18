"""Standalone exact finite controls for the retained 341 and 342 endpoints.

These identities do not certify finite-field descent, local nilpotence,
original-ring membership, or the retained recognition theorems. The source
does not import any retained checker. Its author has not executed, imported,
or compiled this saved file. Canonical execution belongs to the root agent.

Domains used below: characteristic zero; g, b, and rho are nonzero when
inverted. The explicit genuine-conic inverse additionally has kappa != 0.
The independent jet identities themselves retain all resonance factors.
"""

import unittest

import sympy as sp


def scalar_from_reduced_rows(b, kap, rho, U, P, Pt, Pr, Pu, j, bp, g):
    """Formula checked against literal actual rows in the first method."""
    h = kap / b
    hp = -kap * bp / b**2
    x = U + h * P
    delta = j - 2 * b * U
    constant = 2 * kap * U + rho - h * j
    return (
        constant - 2 * constant * Pr * x + constant * Pu * h
        + 2 * g * P * Pr * delta - P * Pu * delta * hp
        + Pt * delta + Pu * delta * g
    )


class QuadraticPlaneEndpointControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.factor(sp.expand(expression)), 0)

    def test_generic_literal_scalar_and_leading_gate(self):
        t, r, U, X, P = sp.symbols("t r U X P")
        g, b, kap, rho = sp.symbols("g b kap rho", nonzero=True)
        bp, j, d, e, Pt, Pr, Pu = sp.symbols("bp j d e Pt Pr Pu")
        c = (kap - 1) / g
        h, hp = kap / b, -kap * bp / b**2
        jp = 2 * g * b - 2 * kap**2 / b
        ep = h * j - bp * r - rho
        x = U + h * P
        theta = c * (x**2 + g * P**2) + j * P - b * r - e
        s = c * r + d
        y = x - g * t
        z = P**2 + theta + 2 * t * x - g * t**2
        w = r - 2 * P * x
        actual = (
            y + P * X + t * X**2,
            z + (2 * t * P + s) * X + t**2 * X**2,
            w + theta * X + s * X**2,
        )

        def dt(f):
            return (sp.diff(f, t) + sp.diff(f, b) * bp
                    + sp.diff(f, j) * jp + sp.diff(f, d) * j
                    + sp.diff(f, e) * ep + sp.diff(f, P) * Pt)

        def dr(f):
            return sp.diff(f, r) + sp.diff(f, P) * Pr

        def du(f):
            return sp.diff(f, U) + sp.diff(f, P) * Pu

        rows = [sp.Matrix([sp.expand(fn(f)) for fn in (dt, dr, du)])
                for f in actual]
        literal = sp.expand(rows[0].dot(rows[1].cross(rows[2])))
        reduced = scalar_from_reduced_rows(
            b, kap, rho, U, P, Pt, Pr, Pu, j, bp, g
        )
        # This retains all X coefficients before imposing the line equation.
        self.zero(literal - reduced - X * (rho * Pu + j - 2 * b * U))

        row_a = sp.Matrix([h * Pt + hp * P - g, h * Pr, 1 + h * Pu])
        row_b = sp.Matrix([(j - 2 * b * U) * Pt + 2 * kap * U + rho - h * j,
                           (j - 2 * b * U) * Pr, (j - 2 * b * U) * Pu])
        row_c = sp.Matrix([-2 * x * Pt - 2 * g * P, 1 - 2 * x * Pr,
                           -2 * x * Pu])
        self.zero(row_a.dot(row_b.cross(row_c)) - reduced)

        q, qt, qr, rhot = sp.symbols("q qt qr rhot")
        p = (q + b * U**2 - j * U) / rho
        jets = {
            P: p,
            Pt: (qt + bp * U**2 - jp * U - p * rhot) / rho,
            Pr: (qr + p * bp) / rho,
            Pu: (2 * b * U - j) / rho,
        }
        # Simultaneous substitution avoids differentiating or rewriting the
        # newly inserted polynomial a second time through formal P.
        full = sp.expand(reduced.subs(jets, simultaneous=True))
        self.zero((rho * Pu + j - 2 * b * U).subs(jets, simultaneous=True))
        top = sp.Poly(sp.expand(rho**3 * b**2 * full), U).coeff_monomial(U**5)
        self.zero(top + 4 * b**3 * bp * (b**2 * g + kap**2))
        self.zero(top.subs(kap, 0) + 4 * g * b**5 * bp)
        # The second factor can vanish. Its exact derivative, with g and
        # kappa constant, is the extra identity used in the written proof.
        self.zero(sp.diff(b**2 * g + kap**2, b) * bp - 2 * g * b * bp)
        self.assertNotEqual(sp.expand(top), 0)

    def test_constant_b_scalar_coefficients_without_resonance_division(self):
        U = sp.symbols("U")
        b, h, g, rho = sp.symbols("b h g rho", nonzero=True)
        j, q, qt, qr, rhot = sp.symbols("j q qt qr rhot")
        kap = b * h
        delta = g - h**2
        p = (q + b * U**2 - j * U) / rho
        pt = (qt - 2 * b * delta * U - p * rhot) / rho
        pr, pu = qr / rho, (2 * b * U - j) / rho
        jac = sp.Poly(sp.expand(scalar_from_reduced_rows(
            b, kap, rho, U, p, pt, pr, pu, j, 0, g
        )), U)
        self.assertLessEqual(jac.degree(), 3)
        self.zero(rho**2 * jac.coeff_monomial(U**3)
                  - 2 * b**2 * (rhot - 2 * (g + h**2) * qr))
        quadratic = jac.coeff_monomial(U**2).subs(rhot, 2 * (g + h**2) * qr)
        self.zero(rho**2 * quadratic + 6 * rho * kap * qr)
        zero_qr = {qr: 0, rhot: 0}
        self.zero(jac.coeff_monomial(U).subs(zero_qr)
                  - 2 * b * (2 * rho * h + delta * j - qt) / rho)
        final = jac.as_expr().subs(
            {qr: 0, rhot: 0, qt: delta * j + 2 * rho * h}, simultaneous=True
        )
        self.zero(final - rho)
        # Neither resonance factor may be canceled in these identities.
        self.zero((final - rho).subs(g, h**2))
        self.zero((final - rho).subs(g, -h**2))
        self.assertNotEqual(sp.expand(quadratic), 0)

    def test_full_constant_family_and_polynomial_inverse_factorization(self):
        X, t, r, V = sp.symbols("X t r V")
        g, b, h, rho = sp.symbols("g b h rho", nonzero=True)
        j0, d0, e0, q0 = sp.symbols("j0 d0 e0 q0")
        c, delta = (b * h - 1) / g, g - h**2
        j = 2 * b * delta * t + j0
        d = b * delta * t**2 + j0 * t + d0
        e, q = h * d - rho * t + e0, delta * d + 2 * rho * h * t + q0
        U = V + delta * t + j0 / (2 * b)
        p = sp.cancel((q + b * U**2 - j * U) / rho)
        x = U + h * p
        theta = c * (x**2 + g * p**2) + j * p - b * r - e
        s = c * r + d
        y, z, w = x - g * t, p**2 + theta + 2 * t * x - g * t**2, r - 2 * p * x
        Y = sp.expand(y + p * X + t * X**2)
        Z = sp.expand(z + (2 * t * p + s) * X + t**2 * X**2)
        W = sp.expand(w + theta * X + s * X**2)
        C, L = delta * d0 + q0 - j0**2 / (4 * b), X + h
        F = L * t + (b / rho) * V**2 + C / rho
        N = t - (b / rho) * (2 * V * F + L * F**2)
        S = sp.expand(W - X * Z)
        Ztilde = sp.expand(Z - (c * X - b) * S)
        self.zero(p - ((b / rho) * V**2 + 2 * h * t + C / rho))
        self.zero(Y - j0 / (2 * b) - (V + L * F))
        self.zero(S - (r - 2 * x * (p + t * X) - X * (p + t * X)**2 + g * t**2 * X))
        self.zero(Ztilde - (rho * N + c * Y**2 + d0 * (X - h) - e0))
        self.zero(sp.diff(S, r) - 1)
        self.zero(sp.diff(Ztilde, r))
        self.zero(S + 2 * x * (p + t * X) + X * (p + t * X)**2 - g * t**2 * X - r)
        rows = [sp.Matrix([sp.diff(f, v) for v in (t, r, V)]) for f in (Y, Z, W)]
        self.zero(rows[0].dot(rows[1].cross(rows[2])) - rho)

        Yhat, Nnew = sp.symbols("Yhat Nnew")
        Fnew = L * Nnew + (b / rho) * Yhat**2 + C / rho
        Vi = Yhat - L * Fnew
        ti = Nnew + (b / rho) * (2 * Yhat * Fnew - L * Fnew**2)
        # Prove the invariant F in both directions before reusing it in
        # compositions. This avoids expression swell, not any inverse step.
        self.zero(L * N + (b / rho) * (V + L * F)**2 + C / rho - F)
        self.zero(L * ti + (b / rho) * Vi**2 + C / rho - Fnew)
        self.zero(Vi + L * Fnew - Yhat)
        self.zero(ti - (b / rho) * (2 * Vi * Fnew + L * Fnew**2) - Nnew)
        self.zero((V + L * F) - L * F - V)
        self.zero(N + (b / rho) * (2 * (V + L * F) * F - L * F**2) - t)

        ZZ, WW, Sc, Zc = sp.symbols("ZZ WW Sc Zc")
        sf, zf = WW - X * ZZ, ZZ - (c * X - b) * (WW - X * ZZ)
        zi, wi = Zc + (c * X - b) * Sc, Sc + X * (Zc + (c * X - b) * Sc)
        for residual in (
            zi.subs({Sc: sf, Zc: zf}, simultaneous=True) - ZZ,
            wi.subs({Sc: sf, Zc: zf}, simultaneous=True) - WW,
            sf.subs({ZZ: zi, WW: wi}, simultaneous=True) - Sc,
            zf.subs({ZZ: zi, WW: wi}, simultaneous=True) - Zc,
        ):
            self.zero(residual)
        # A sign error in the e0 correction is not masked by special constants.
        wrong_n = (Ztilde - c * Y**2 - d0 * (X - h) - e0) / rho
        self.zero(wrong_n - N + 2 * e0 / rho)
        self.assertNotEqual(sp.expand(2 * e0 / rho), 0)

    def test_zero_kappa_actual_cubic_shear(self):
        X, t, r, x, P, e = sp.symbols("X t r x P e")
        g, b = sp.symbols("g b", nonzero=True)
        d1, d0 = sp.symbols("d1 d0")
        d2 = g * b
        d, j, c = d2 * t**2 + d1 * t + d0, 2 * d2 * t + d1, -1 / g
        theta = c * (x**2 + g * P**2) + j * P - b * r - e
        s = c * r + d
        y, z, w = x - g * t, P**2 + theta + 2 * t * x - g * t**2, r - 2 * P * x
        Y, Z, W = y + P * X + t * X**2, z + (2 * t * P + s) * X + t**2 * X**2, w + theta * X + s * X**2
        T = sp.expand(Y**2 + X * W - X**2 * Z + g * Z)
        S1 = sp.expand(X * Z - W)
        S2 = sp.expand(S1 - X**2 * T / (g * d2) + (d1 / d2) * X * Y + (d0 / d2) * X**3)
        self.assertLessEqual(sp.Poly(T, X).degree(), 1)
        self.zero(sp.Poly(T, X).coeff_monomial(X) - g * d)
        self.zero(sp.Poly(S1, X).coeff_monomial(X**3) - t**2)
        self.assertLessEqual(sp.Poly(S2, X).degree(), 2)
        wrong = sp.expand(S1 - X**2 * T / (g * d2))
        self.zero(sp.Poly(wrong, X).coeff_monomial(X**3) + (d1 * t + d0) / d2)
        self.assertNotEqual(sp.Poly(wrong, X).coeff_monomial(X**3), 0)
        YY, ZZ, WW, TT, SS, RR = sp.symbols("YY ZZ WW TT SS RR")
        ft, fs = YY**2 + X * WW - X**2 * ZZ + g * ZZ, X * ZZ - WW
        iz = (TT - YY**2 + X * SS) / g
        iw = X * iz - SS
        for residual in (
            iz.subs({TT: ft, SS: fs}, simultaneous=True) - ZZ,
            iw.subs({TT: ft, SS: fs}, simultaneous=True) - WW,
            ft.subs({ZZ: iz, WW: iw}, simultaneous=True) - TT,
            fs.subs({ZZ: iz, WW: iw}, simultaneous=True) - SS,
        ):
            self.zero(residual)
        forward = SS - X**2 * TT / (g * d2) + (d1 / d2) * X * YY + (d0 / d2) * X**3
        inverse = RR + X**2 * TT / (g * d2) - (d1 / d2) * X * YY - (d0 / d2) * X**3
        self.zero(forward.subs(SS, inverse) - RR)
        self.zero(inverse.subs(RR, forward) - SS)

    def test_selected_line_scalar_actual_partial_and_resonant_relation(self):
        X, t, r, P, zeta, zt, zr = sp.symbols("X t r P zeta zt zr")
        g, b = sp.symbols("g b", nonzero=True)
        h, d1, d0, e0 = sp.symbols("h d1 d0 e0")
        c, kap, delta = (b * h - 1) / g, b * h, g - h**2
        d, j = b * delta * t**2 + d1 * t + d0, 2 * b * delta * t + d1
        x = h * P + zeta
        theta = c * (x**2 + g * P**2) + j * P - b * r - h * d - e0
        y, z, w = x - g * t, 2 * t * x - g * t**2 + P**2 + theta, r - 2 * P * x
        actual = (
            y + P * X + t * X**2,
            z + (2 * t * P + c * r + d) * X + t**2 * X**2,
            w + theta * X + (c * r + d) * X**2,
        )

        def dt(f):
            return sp.diff(f, t) + sp.diff(f, zeta) * zt

        def dr(f):
            return sp.diff(f, r) + sp.diff(f, zeta) * zr

        rows = [sp.Matrix([dt(f), dr(f), sp.diff(f, P)]) for f in actual]
        jac = sp.expand(rows[0].dot(rows[1].cross(rows[2])))
        eta = j - 2 * b * zeta
        expected = -eta * (2 * (g + h**2) * zr * P + zt - g + h**2 + 2 * h * zeta * zr)
        self.zero(jac - expected)
        self.zero(sp.Poly(jac, P).coeff_monomial(P) + 2 * eta * (g + h**2) * zr)
        for f, wanted in zip(actual, (0, c * X - b, 1 - b * X + c * X**2)):
            self.zero(dr(f).subs(zr, 0) - wanted)
        # h=0 is a retained nonresonant boundary, not a divided-out case.
        self.zero((jac - expected).subs(h, 0))

        Z, W, Qc, Sc = sp.symbols("Z W Qc Sc")
        sf = X * Z - W
        qf = Z + (c * X - b) * sf
        zi = Qc - (c * X - b) * Sc
        wi = X * Qc - (c * X**2 - b * X + 1) * Sc
        for residual in (
            zi.subs({Qc: qf, Sc: sf}, simultaneous=True) - Z,
            wi.subs({Qc: qf, Sc: sf}, simultaneous=True) - W,
            qf.subs({Z: zi, W: wi}, simultaneous=True) - Qc,
            sf.subs({Z: zi, W: wi}, simultaneous=True) - Sc,
        ):
            self.zero(residual)
        deriv = lambda f: ((c * X - b) * sp.diff(f, Z)
                           + (1 - b * X + c * X**2) * sp.diff(f, W))
        self.zero(deriv(sf) + 1)
        self.zero(deriv(qf))

        R = P - h * t
        Z0 = z + b * w - c * y**2 + h * d0 + e0
        relation = Z0 - (kap * R**2 + (d1 - 2 * b * y) * R)
        self.zero(relation.subs(g, -h**2))
        yy, zz0, rr0 = sp.symbols("yy zz0 rr0")
        discriminant = (d1 - 2 * b * yy)**2 + 4 * kap * zz0
        self.assertEqual(sp.Poly(discriminant, zz0).degree(), 1)
        self.zero(sp.diff(discriminant, zz0) - 4 * kap)
        # Without the exact rational K-return, the same discriminant becomes
        # a square on a quadratic cover. This is a field-boundary control,
        # not a sample-based proof of universal irreducibility.
        covered = discriminant.subs(zz0, kap * rr0**2 + (d1 - 2 * b * yy) * rr0)
        self.zero(covered - (2 * kap * rr0 + d1 - 2 * b * yy)**2)


if __name__ == "__main__":
    unittest.main()
