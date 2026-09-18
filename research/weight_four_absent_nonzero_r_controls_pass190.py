"""Finite exact controls for the absent-variable nonzero-R return190.

Literal potential elimination, coefficient partial changes, unrestricted
scalar residuals, pencil-coefficient derivatives and the two original
polynomial shears are checked independently of earlier implementations.
The symbolic coefficient charts are not asserted to be realized frames.
Exact field return, pole-divisor budgets, constant-field descent and the
published regular-kernel theorem remain written-proof inputs. Finite
identities do not prove those inputs or establish historical novelty.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


class AbsentNonzeroRReturnControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_h_elimination_and_retained_calibration(self):
        t, rho, U, V, Zp = sp.symbols("t rho U V Zp")
        r = sp.symbols("r", nonzero=True)
        alpha, c = sp.symbols("alpha c")
        k0, k1, k2, k3, n0, n1, n2 = sp.symbols("k0 k1 k2 k3 n0 n1 n2")
        ell, ellt, ellrho, m = sp.symbols("ell ellt ellrho m")
        jets = {r: -alpha * r**2, k0: k1, k1: k2, k2: k3,
                n0: n1, n1: n2, ell: ellt}

        def Dt(expression):
            return sp.diff(expression, t) + sum(
                sp.diff(expression, variable) * derivative
                for variable, derivative in jets.items()
            )

        # chi=1/r, with beta=chi-alpha*t constant under this independent jet.
        # This avoids introducing large common reciprocal denominators.
        chi = 1 / r
        self.zero(Dt(chi - alpha * t))
        k = r * rho + k0
        n = c * r**2 * rho + n0
        kt, ktt, kttt = Dt(k), Dt(Dt(k)), Dt(Dt(Dt(k)))
        nt, ntt = Dt(n), Dt(Dt(n))
        nr, ntr = sp.diff(n, rho), sp.diff(nt, rho)
        S = 4 * t * U**3 + ktt * U**2 / 2 + Dt(r) * U * V + nt * U + nr * V
        T = (U**4 + kttt * U**3 / 6 + Dt(Dt(r)) * U**2 * V / 2
             + ntt * U**2 / 2 + ntr * U * V)
        A1 = Dt(r) * U + nr
        h = chi * ell + c**2 * r**2 * rho + c * n0
        hrho = chi * ellrho + c**2 * r**2
        ht = Dt(h)
        omega = -r * ellrho - c**2 * r**4
        self.zero(hrho + omega / r**2)
        D = chi + 4 * alpha * t
        F3 = chi * k3 / 6 + alpha * k2 / 2 - 4 * c * t
        F2 = chi * n2 / 2 + alpha * n1 - c * k2 / 2
        p = ((-4 * t * chi - 6 * alpha * t**2) * U**3
             + (6 * c * t**2 - chi * k2 / 2 - alpha * k1) * U**2
             + (c * k1 - chi * n1 - alpha * n0) * U)
        F = D * U**4 + F3 * U**3 + F2 * U**2
        self.zero(Dt(p) + sp.diff(F, U))

        theta = (Zp - 6 * t**2 * U**2 - kt * U - n) / r
        w_first = (ell - S.subs(V, theta)) / r
        self.zero(w_first - ((alpha * U - c) * Zp + p + h))
        second = A1 * w_first + T.subs(V, theta) - ellt * U - ellrho * theta - m
        # This numerator is hrho*z in the claimed new h-coordinate formula.
        # We clear the certified nonzero hrho rather than solving numerically.
        z_numerator = (r * F + hrho * 6 * t**2 * U**2
                       + (hrho * kt - r * ht) * U
                       + hrho * n - m + c * r * ell)
        self.zero(second + hrho * Zp - z_numerator)

        zt, zr, zy = sp.symbols("zt zr zy")
        old_matrix = sp.Matrix([
            [0, 0, 1],
            [zt, zr, zy],
            [(alpha * U - c) * zt + Dt(p) + ht,
             (alpha * U - c) * zr + hrho,
             (alpha * U - c) * zy + alpha * Zp + sp.diff(p, U)],
        ])
        old_det = old_matrix.det()
        self.zero(old_det - (hrho * zt - (Dt(p) + ht) * zr))
        new_scalar = zt - ht * zr / hrho + sp.diff(F, U) * zr / hrho
        self.zero(old_det - hrho * new_scalar)
        a_E, Gamma = sp.symbols("a_E Gamma", nonzero=True)
        rho_h = 1 / hrho
        # No assumption a_E=1 or Gamma=1 is made in the parameter change.
        self.zero((-a_E**3 / Gamma) / hrho + a_E**3 * rho_h / Gamma)

    def test_unrestricted_scalar_residual_and_direct_alpha_gate(self):
        t, h, U = sp.symbols("t h U")
        alpha, beta = sp.symbols("alpha beta")
        r = 1 / (alpha * t + beta)
        D = 5 * alpha * t + beta
        F3, F2 = (sp.Function(name)(t) for name in ("F3", "F2"))
        rho = sp.Function("rho")(t, h)
        k0 = sp.Function("k0")(t)
        z0 = sp.Function("z0")(t, h)
        F = D * U**4 + F3 * U**3 + F2 * U**2

        def delta(expression):
            return sp.diff(expression, t) + sp.diff(F, U) * sp.diff(expression, h)

        z = (r * sp.diff(rho, h) * F + 6 * t**2 * U**2
             + sp.diff(r * rho + k0, t) * U + z0)
        residual = sp.expand(delta(z))
        self.assertLessEqual(sp.Poly(residual, U).degree(), 7)
        self.zero(residual.coeff(U, 7) - 4 * r * D**2 * sp.diff(rho, h, 2))

        TT, u = (sp.Function(name)(t) for name in ("TT", "u0"))
        z_linear = (TT * D * U**4 + TT * F3 * U**3
                    + (6 * t**2 + TT * F2) * U**2
                    + (sp.diff(TT, t) * h + u) * U + z0)
        reduced = sp.expand(delta(z_linear))
        E4 = D * sp.diff(TT, t) + alpha * TT
        expected = (
            5 * E4 * U**4
            + (TT * sp.diff(F3, t) + 4 * sp.diff(TT, t) * F3
               + 4 * D * sp.diff(z0, h)) * U**3
            + (12 * t + TT * sp.diff(F2, t) + 3 * sp.diff(TT, t) * F2
               + 3 * F3 * sp.diff(z0, h)) * U**2
            + (sp.diff(TT, t, 2) * h + sp.diff(u, t)
               + 2 * F2 * sp.diff(z0, h)) * U
            + sp.diff(z0, t)
        )
        self.zero(reduced - expected)
        bb, g0 = (sp.Function(name)(t) for name in ("bb", "g0"))
        staged = sp.expand(delta(z_linear - z0 + bb * h + g0))
        self.zero(staged.coeff(U, 1).coeff(h, 1) - sp.diff(TT, t, 2))
        self.zero(staged.coeff(U, 0) - sp.diff(bb, t) * h - sp.diff(g0, t))
        # With E4=0 and TT''=0, the left side vanishes. The exact identity
        # then forces alpha=0 in the proof because TT is a nonzero field element.
        self.zero(6 * alpha * E4 - D * sp.diff(E4, t)
                  + D**2 * sp.diff(TT, t, 2) - 6 * alpha**2 * TT)
        self.zero(E4.subs(alpha, 0) - beta * sp.diff(TT, t))

    def test_pencil_derivatives_two_shears_and_determinant_transport(self):
        t, U = sp.symbols("t U")
        beta, TT, r = sp.symbols("beta TT r", nonzero=True)
        b, bp, c = sp.symbols("b bp c")
        f3, f3t, f2, f2t, p2, p2t, p1, p1t, u, ut = sp.symbols(
            "f3 f3t f2 f2t p2 p2t p1 p1t u ut"
        )
        jet = {b: bp, f3: f3t, f2: f2t, p2: p2t, p1: p1t, u: ut}

        def Dt(expression):
            return sp.diff(expression, t) + sum(
                sp.diff(expression, variable) * derivative
                for variable, derivative in jet.items()
            )

        p = -4 * beta * t * U**3 + p2 * U**2 + p1 * U
        g = (TT * beta * U**4 + TT * f3 * U**3
             + (6 * t**2 + TT * f2) * U**2 + u * U - b * p)
        prior = {f3t: -4 * beta * b / TT, f2t: -(12 * t + 3 * f3 * b) / TT,
                 ut: -2 * f2 * b, p2t: -3 * f3, p1t: -2 * f2}
        g = sp.expand(g)
        self.zero(g.coeff(U, 4) - TT * beta)
        self.zero((Dt(g.coeff(U, 3)) - 4 * beta * t * bp).subs(prior, simultaneous=True))
        self.zero((Dt(g.coeff(U, 2)) + p2 * bp).subs(prior, simultaneous=True))
        self.zero((Dt(g.coeff(U, 1)) + p1 * bp).subs(prior, simultaneous=True))
        # A universal pole-budget argument, not these coefficient checks,
        # makes every nonconstant coefficient affine in b and forces b'=0.

        X, Y, Z, W, I, J, y, h = sp.symbols("X Y Z W I J y h")
        zbase, pbase, kap, kbase, kprime, nbase = sp.symbols(
            "zbase pbase kap kbase kprime nbase"
        )
        rho = (TT / r) * h + kap
        z = b * h + zbase
        n = c * r**2 * rho + nbase
        k = r * rho + kbase
        theta = (z - 6 * t**2 * y**2 - kprime * y - n) / r
        w = -c * z + pbase + h
        Z_chart = z + (4 * t**3 * y + k) * X + t**4 * X**2
        W_chart = w + theta * X + rho * X**2
        B0, lam = b + TT * X, X / r - c
        self.zero(sp.diff(Z_chart, h) - B0)
        self.zero(sp.diff(theta, h) - (b / r - c * TT))
        self.zero(sp.diff(W_chart, h) - (1 + lam * B0))
        J_chart = W_chart - lam * Z_chart
        Istar_chart = Z_chart - B0 * J_chart
        self.zero(sp.diff(J_chart, h) - 1)
        self.zero(sp.diff(Istar_chart, h))
        self.zero(J_chart.subs(X, 0) - h - pbase)
        self.zero(Istar_chart.subs(X, 0) - zbase + b * pbase)

        # Q0 stands for an arbitrary polynomial in the two fixed coordinates.
        # Its precise degree is immaterial to these symbolic inverse identities.
        Q0 = sp.Function("Q0")(X, Y)
        J_forward = W - lam * Z
        I_forward = Z - B0 * J_forward - Q0
        Z_inverse = I + Q0 + B0 * J
        W_inverse = J + lam * Z_inverse
        inverse = {Z: Z_inverse, W: W_inverse}
        forward = {I: I_forward, J: J_forward}
        self.zero(I_forward.subs(inverse, simultaneous=True) - I)
        self.zero(J_forward.subs(inverse, simultaneous=True) - J)
        self.zero(Z_inverse.subs(forward, simultaneous=True) - Z)
        self.zero(W_inverse.subs(forward, simultaneous=True) - W)
        self.zero(sp.Matrix([I_forward, J_forward]).jacobian([Z, W]).det() - 1)

        rho_t, It, Iy, Jt, Jy, g0_prime = sp.symbols("rho_t It Iy Jt Jy g0_prime")
        coordinate_change = sp.Matrix([[1, 0, 0], [rho_t, 0, TT / r], [0, 1, 0]])
        self.zero(coordinate_change.det() + TT / r)
        transported = sp.Matrix([[X, 1, 0], [It, Iy, 0], [Jt, Jy, 1]]).det()
        self.zero(transported - (X * Iy - It))
        self.zero(transported.subs({X: 0, It: g0_prime}, simultaneous=True) + g0_prime)
        a_E, Gamma = sp.symbols("a_E Gamma", nonzero=True)
        self.zero((-a_E**3 / Gamma) * coordinate_change.det() - a_E**3 * TT / (r * Gamma))
        self.zero((-g0_prime).subs(g0_prime, -a_E**3 * TT / (r * Gamma))
                  - a_E**3 * TT / (r * Gamma))
        # Finite polynomial transport control, independent of the field proof.
        q00, q10, q01, q21, q04 = sp.symbols("q00 q10 q01 q21 q04")
        Qpoly = q00 + q10 * X + q01 * Y + q21 * X**2 * Y + q04 * Y**4
        Qchart = Qpoly.subs(Y, y + t * X)
        self.zero(sp.diff(Qchart, t) - X * sp.diff(Qchart, y))
        self.zero(Qchart.subs(y, Y - t * X) - Qpoly)


if __name__ == "__main__":
    unittest.main()
