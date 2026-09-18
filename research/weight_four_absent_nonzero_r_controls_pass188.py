"""Necessary algebra controls for absent-variable nonzero-R rigidity188.

These formal jets check elimination, cleared determinants, and leading-form
algebra only. They do not supply an actual frame, scalar Jacobian, geometric
integrality, a projective closure, or a one-point-at-infinity theorem. Those
are written-proof inputs or arguments. The constant-y fixture is explicitly
formal and is not a realization of the actual chart.
No older checker, proof implementation, or solver internals are imported.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


class AbsentVariableNonzeroRControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_elimination_gradients_and_cleared_determinant(self):
        U, V, W0 = sp.symbols("U V W0")
        R = sp.symbols("R", nonzero=True)
        Rt, Rr, q3, q4 = sp.symbols("R_t R_rho q3 q4")
        k20, k30, k21, k12, k03 = sp.symbols("k20 k30 k21 k12 k03")
        nt, nr, ntt, ntr, nrr = sp.symbols("n_t n_rho n_tt n_trho n_rhorho")
        ell, ellt, ellr, m = sp.symbols("ell ell_t ell_rho m")
        S = (q3 * U**3 / 6
             + (k20 * U**2 + 2 * Rt * U * V + Rr * V**2) / 2
             + nt * U + nr * V)
        T = (q4 * U**4 / 24
             + (k30 * U**3 + 3 * k21 * U**2 * V
                + 3 * k12 * U * V**2 + k03 * V**3) / 6
             + (ntt * U**2 + 2 * ntr * U * V + nrr * V**2) / 2)
        coefficients = (q3, k20, Rt, Rr, nt, nr)
        t_jets = (q4, k30, k21, k12, ntt, ntr)
        rho_jets = (0, k21, k12, k03, ntr, nrr)
        St = sum(sp.diff(S, coefficient) * jet
                 for coefficient, jet in zip(coefficients, t_jets))
        Sr = sum(sp.diff(S, coefficient) * jet
                 for coefficient, jet in zip(coefficients, rho_jets))
        self.zero(sp.diff(T, U) - St)
        self.zero(sp.diff(T, V) - Sr)
        A = sp.diff(S, V)
        B = sp.diff(S, U)
        P = R * W0 + S - ell
        Psi = A * W0 + T - ellt * U - ellr * V
        Ct = St + Rt * W0 - ellt
        Cr = Sr + Rr * W0 - ellr
        for actual, expected in zip(
            (sp.diff(P, U), sp.diff(P, V), sp.diff(P, W0)), (B, A, R)
        ):
            self.zero(actual - expected)
        for actual, expected in zip(
            (sp.diff(Psi, U), sp.diff(Psi, V), sp.diff(Psi, W0)), (Ct, Cr, A)
        ):
            self.zero(actual - expected)
        H = sp.expand(R * (Psi - m) - A * P)
        self.zero(sp.diff(H, W0))
        # Exact errors before imposing the first potential P=0. This keeps
        # coefficient derivatives separate from later evaluation on the line.
        self.zero(sp.diff(H, U) - (R * Ct - A * B) + Rt * P)
        self.zero(sp.diff(H, V) - (R * Cr - A**2) + Rr * P)
        explicit = R * (T - ellt * U - ellr * V - m) + A * (ell - S)
        self.zero(H - explicit)
        top = sum(
            coefficient * U**i * V**j
            for (i, j), coefficient in sp.Poly(H, U, V).terms()
            if i + j == 4
        )
        self.zero(top - U**3 * ((R * q4 / 24 - Rt * q3 / 6) * U
                               - Rr * q3 * V / 6))
        self.assertLessEqual(sp.Poly(H, U, V).total_degree(), 4)

        # Independent evaluated row algebra. The third row is R*dw,
        # obtained from dP=0. Thus R times this determinant is R^2 J0.
        av, bv, ct, cr = sp.symbols("A_eval B_eval Ct_eval Cr_eval")
        yt, yr, yv, vt, vr, vv = sp.symbols(
            "y_t y_rho y_v theta_t theta_rho theta_v"
        )
        dy = sp.Matrix([[yt, yr, yv]])
        middle = sp.Matrix([[R * vt + bv, R * vr + av, R * vv]])
        r_dw = sp.Matrix([[
            -bv * yt - av * vt - ct,
            -bv * yr - av * vr - cr,
            -bv * yv - av * vv,
        ]])
        rows = dy.col_join(middle).col_join(r_dw)
        HU, HV = R * ct - av * bv, R * cr - av**2
        CU = R * (vr * yv - yr * vv) + av * yv
        CV = R * (yt * vv - vt * yv) - bv * yv
        self.zero(R * rows.det() - CU * HU - CV * HV)
        # No scalar/nonvanishing assertion about J0 is inferred from this
        # identity. That is exactly the actual-coordinate calibration input.

    def test_top_factor_multiplicities_and_constant_projection_boundary(self):
        U, V, L = sp.symbols("U V L")
        a = sp.symbols("a")
        b = sp.symbols("b", nonzero=True)
        Lambda = a * U + b * V
        top = U**3 * Lambda
        self.assertEqual(sp.gcd(U, Lambda), 1)
        for order in (0, 1, 2):
            self.zero(sp.diff(top, U, order).subs(U, 0))
        self.zero(sp.diff(top, U, 3).subs(U, 0) - 6 * b * V)
        self.assertNotEqual(sp.diff(top, U, 3).subs(U, 0), 0)
        separated = sp.expand(top.subs(V, (L - a * U) / b))
        self.zero(separated - U**3 * L)
        self.zero(separated.subs(L, 0))
        self.zero(sp.diff(separated, L).subs(L, 0) - U**3)

        # Algebra accompanying the geometric leading-power input in degree4.
        lu, lv = sp.symbols("lu lv")
        fourth_power = sp.expand((lu * U + lv * V)**4)
        self.zero(fourth_power.coeff(V, 4) - lv**4)
        self.zero(fourth_power.coeff(U, 3).coeff(V, 1) - 4 * lu**3 * lv)
        self.zero(fourth_power.subs(lv, 0).coeff(V, 1))
        self.zero(sp.expand(top).coeff(U, 3).coeff(V, 1) - b)
        # If lv^4 vanishes in a field, lv=0; then the nonzero b coefficient
        # cannot match. The one-point-at-infinity assertion is not tested here.

        d = sp.symbols("d", nonzero=True)
        g20, g11, g02 = sp.symbols("g20 g11 g02")
        quadratic = g20 * U**2 + g11 * U * V + g02 * V**2
        square = sp.expand(d * quadratic**2)
        self.zero(square.coeff(V, 4) - d * g02**2)
        self.zero(square.subs(g02, 0).coeff(V, 2) - d * g11**2 * U**2)
        self.zero(square.subs({g02: 0, g11: 0}, simultaneous=True).coeff(V, 1))
        # This coefficient route gives the same odd-multiplicity obstruction:
        # matching V^4 and U^2V^2 forces g02=g11=0, losing U^3V.

        quotient, remainder = sp.div(separated, L**2, L)
        self.zero(quotient)
        self.zero(remainder - U**3 * L)
        self.assertNotEqual(remainder, 0)
        self.zero(top - U**2 * (U * Lambda))
        # Therefore the repeated leading linear factor can be U, not Lambda.
        # Degree3 is controlled by deg(Q)=1<deg(G), together with the written
        # divisibility G|(Q-omega); that field/ideal inference is not sampled.

        y0 = sp.symbols("y0")
        omega = sp.symbols("omega", nonzero=True)
        G = U - y0
        formal_H = sp.expand(omega * G + G**2 * U * Lambda)
        formal_Q = omega + G * U * Lambda
        self.zero(formal_H - G * formal_Q)
        self.zero(formal_H.subs(U, y0))
        self.zero(formal_Q.subs(U, y0) - omega)
        formal_top = sum(
            coefficient * U**i * V**j
            for (i, j), coefficient in sp.Poly(formal_H, U, V).terms()
            if i + j == 4
        )
        self.zero(formal_top - top)
        # The formal plane (y,theta)=(y0,v) has the whole polynomial line
        # and unit cofactor. It guards the exact conclusion: these leading
        # identities allow constant y and do not by themselves exclude it.
        self.zero(top.subs(b, 0) - a * U**4)
        # If b=0, the multiplicity obstruction disappears. No excluded
        # hypothesis or actual realization is inferred from this boundary.


if __name__ == "__main__":
    unittest.main()
