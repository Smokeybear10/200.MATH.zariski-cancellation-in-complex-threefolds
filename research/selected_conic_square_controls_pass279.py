"""Finite algebra controls for the conic exclusion279.

These rebuild the selected conic, its constant-discriminant scalar, and
the full actual coordinate transport. Normality, exact field constants,
irreducibility over function fields, and chart entry remain written
arguments. No retained checker or solver is imported.
"""

import unittest

import sympy as S


class SelectedConicSquareControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_selected_conic_discriminant_and_constant_completed_square(self):
        U, V, y = S.symbols("U V y")
        gamma, eta, r = S.symbols("gamma eta r", nonzero=True)
        s, c = S.symbols("s c")
        P = r * U**2 + s * U + c
        H = gamma * (V - P)**2 + eta * (V - P)
        N = 2 * gamma
        linear = S.expand(H).coeff(V, 1)
        constant = S.expand(H).coeff(V, 0)
        self.assert_zero(linear**2 - 2 * N * constant - eta**2)
        chi = N * V + linear
        self.assert_zero(chi.subs(V, P) - eta)
        self.assert_zero(S.diff(chi.subs(V, P).subs(U, y), y))
        self.assert_zero(H.subs(V, P))
        self.assert_zero(S.diff(H, V).subs(V, P) - eta)
        a4 = S.expand(H).coeff(U, 4)
        M = S.expand(linear).coeff(U, 2)
        self.assert_zero(M**2 - 2 * N * a4)
        self.assert_zero(a4 - gamma * r**2)
        # A repeated component alone has no unit evaluated cofactor.
        bad = gamma * (V - P)**2
        self.assert_zero(S.diff(bad, U).subs(V, P))
        self.assert_zero(S.diff(bad, V).subs(V, P))

    def test_raw_constant_discriminant_scalar_and_primitive_degree(self):
        U, h, e, M, chi = S.symbols("U h e M chi", nonzero=True)
        ht, chit, chil, b1, A, P, Pt, Pl = S.symbols("ht chit chil b1 A P Pt Pl")
        At, Al = -e**2 * (2 * M * U + b1), -e / h
        Bt, Bl = -At * P, e * P / h
        z = h * chi + P
        zt, zl = ht * chi + h * chit + Pt, h * chil + Pl
        wt, wl = At * z + A * zt + Bt, Al * z + A * zl + Bl
        determinant = zt * wl - zl * wt
        reduced = determinant.subs(Pt, -h * At * Pl / e)
        target = -chi * (e * ht * chi + e * h * chit + h**2 * At * chil)
        self.assert_zero(reduced - target)
        self.assert_zero(S.expand(reduced).coeff(U, 1) - 2 * M * e**2 * h**2 * chi * chil)
        self.assert_zero(reduced.subs(chil, 0) + e * chi * (ht * chi + h * chit))
        # Omitting Bt from the raw derivative creates an uncancelled term.
        wrong = zt * wl - zl * (At * z + A * zt)
        self.assert_zero(wrong - determinant - zl * Bt)
        self.assertNotEqual(S.expand(zl * Bt).subs({M: 1, U: 1, b1: 0, e: 1, P: 1, h: 1, chil: 1, Pl: 0}), 0)

        U, V, Z, W = S.symbols("U V Z W")
        q20, q11, q02, q10, q01, q00 = S.symbols("q20 q11 q02 q10 q01 q00")
        Q = q20 * U**2 + q11 * U * V + q02 * V**2 + q10 * U + q01 * V + q00
        g = S.Function("g")(U)
        Pi = S.integrate(Q, V) + g
        relation = W - Pi + V * Z
        self.assert_zero(S.diff(Pi, V) - Q)
        self.assert_zero(S.diff(relation, W) - 1)
        self.assert_zero(S.expand(relation).coeff(V, 3) + q02 / 3)
        self.assert_zero(S.expand(relation).coeff(V, 2) + (q11 * U + q01) / 2)
        final = relation.subs({q02: 0, q11: 0, q01: 0})
        self.assert_zero(final - W + g - V * (Z - q20 * U**2 - q10 * U - q00))

    def test_full_actual_transport_and_odd_degree_square_obstruction(self):
        t, X, y, s, zeta, lam = S.symbols("t X y s zeta lam")
        j = S.symbols("j", nonzero=True)
        e = S.Function("e")(t)
        q2, q1, q0, c1, c0, c2 = S.symbols("q2 q1 q0 c1 c0 c2")
        g3, g2, g1, g0, r2, r1, r0, l1, l0, kap = S.symbols("g3 g2 g1 g0 r2 r1 r0 l1 l0 kap")
        Lambda = g2 * t**2 + l1 * t + l0
        b = -Lambda / (j * e)
        N, m = 1 / (j * e**3), 1 / e
        k0 = j * b + q1 * t + c2
        n0 = q0 + (j * b**2 / 2 - g1 * t - kap) / e
        q = q2 * t**2 + c1 * t + c0 - j * e
        r = g3 * t**3 + r2 * t**2 + r1 * t + r0 - j * e**2 / 2
        k, n = m * lam + k0, N * lam**2 / 2 + b * lam / e**2 + n0
        f = (S.diff(q, t, 2) - S.diff(r, t, 2) * m) * y**2 / 2 + S.diff(k, t) * y + n
        replace_lam = j * e * (zeta - b + S.diff(e, t) * y)
        f, k = f.subs(lam, replace_lam), k.subs(lam, replace_lam)
        Q0 = lambda value: q2 * value**2 + q1 * value + q0
        g = lambda value: g3 * value**3 + g2 * value**2 + g1 * value + g0
        z, w = s + Q0(y), g(y) - s * zeta
        Y = y + t * X
        Z = z + (S.diff(q, t) * y + k) * X + q * X**2
        W = w + e * (z - f) * X + (S.diff(r, t) * y + replace_lam) * X**2 + r * X**3
        V = Z - Q0(Y) - c1 * X * Y - c2 * X - c0 * X**2
        Wbar = W - g(Y) - r2 * X * Y**2 - r1 * X**2 * Y - r0 * X**3 - l1 * X * Y - l0 * X**2 - kap * X
        parameter = zeta - e * X
        for residual in (V - s - j * X * parameter, Wbar + s * parameter + j * X * parameter**2 / 2):
            poly = S.Poly(S.expand(residual), X)
            self.assertLessEqual(poly.degree(), 3)
            for degree in range(4):
                self.assert_zero(poly.nth(degree))
        self.assert_zero((s + j * X * parameter)**2 + 2 * j * X * (-s * parameter - j * X * parameter**2 / 2) - s**2)

        V0, W0, Y0, Z0, WW = S.symbols("V0 W0 Y0 Z0 WW")
        square_target = V0**2 + 2 * j * X * W0
        self.assertEqual(S.degree(square_target, W0), 1)
        self.assertEqual(S.degree(square_target.subs(X, 0), W0), 0)
        # The zero-X fiber alone loses the odd-degree obstruction.
        self.assert_zero(square_target.subs(X, 0) - V0**2)
        correction_z = Q0(Y0) + c1 * X * Y0 + c2 * X + c0 * X**2
        correction_w = g(Y0) + r2 * X * Y0**2 + r1 * X**2 * Y0 + r0 * X**3 + l1 * X * Y0 + l0 * X**2 + kap * X
        self.assert_zero((Z0 - correction_z).subs(Z0, V0 + correction_z) - V0)
        self.assert_zero((V0 + correction_z).subs(V0, Z0 - correction_z) - Z0)
        self.assert_zero((WW - correction_w).subs(WW, W0 + correction_w) - W0)
        self.assert_zero((W0 + correction_w).subs(W0, WW - correction_w) - WW)


if __name__ == "__main__":
    unittest.main(verbosity=2)
