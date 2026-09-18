"""Finite necessary-identity controls for the absent-variable zero-R note187.

All coefficient jets and cover fixtures below are formal. They do not give
an actual frame, a global invariant coordinate, L=K(n), or recognition.
The written argument supplies actual inverse/field hypotheses, Wang's
classification, transcendence, and coefficient-field primitive subtraction.
No previous checker, proof implementation, or solver internals are imported.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


class AbsentVariableZeroRControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_constant_projection_factorization_and_original_partial(self):
        X, y, yt, yr = sp.symbols("X y y_t y_rho")
        q0, q1, q2, q3, k0, k1, k2, n, nt, nr = sp.symbols(
            "q0 q1 q2 q3 k0 k1 k2 n n_t n_rho"
        )
        wt, wr, wv, theta, thetat, thetar, thetav = sp.symbols(
            "w_t w_rho w_v theta theta_t theta_rho theta_v"
        )
        variables = (y, q0, q1, q2, k0, k1, n)
        t_jets = (yt, q1, q2, q3, k1, k2, nt)
        rho_jets = (yr, 0, 0, 0, 0, 0, nr)

        def dt(expression):
            return sum(sp.diff(expression, value) * jet
                       for value, jet in zip(variables, t_jets))

        def dr(expression):
            return sum(sp.diff(expression, value) * jet
                       for value, jet in zip(variables, rho_jets))

        sigma = q1 * y + k0
        z = q2 * y**2 / 2 + k1 * y + n
        matrix = sp.Matrix([
            [yt + X, yr, 0],
            [dt(z) + dt(sigma) * X + q1 * X**2,
             dr(z) + dr(sigma) * X, 0],
            [wt + thetat * X, wr + thetar * X + X**2, wv + thetav * X],
        ])
        C0 = yt * dr(z) - yr * dt(z)
        self.zero(matrix.det() - (wv + thetav * X) * (nr * X + C0))
        self.zero(dr(sigma) - yr * q1)
        self.zero(dr(z) + yt * dr(sigma) - yr * dt(sigma) - nr)
        self.zero(C0 - (yt * nr - yr * (q3 * y**2 / 2 + k2 * y + nt)))

        # After n_rho=0, its mixed partial vanishes too. The cubic identity
        # then has a generally NONZERO rho derivative; theta is not independent.
        ell_without_nr = q3 * y**3 / 6 + k2 * y**2 / 2 + nt * y
        ell_rho = yr * sp.diff(ell_without_nr, y)
        self.zero(C0.subs(nr, 0) + ell_rho)
        self.assertNotEqual(sp.expand(ell_rho), 0)
        self.zero(matrix.det().subs({nr: 0, thetav: 0}, simultaneous=True)
                  + wv * ell_rho)

        t, rho, w, a = sp.symbols("t rho w a")
        # This is the conditional chart after the constant-y field step:
        # y,z,sigma,theta,a belong to L and are independent of X,w.
        chart = (X, y + t * X, z + sigma * X + t**4 * X**2,
                 w + theta * X + rho * X**2)
        for expression, expected in zip(chart, (0, 0, 0, 1)):
            self.zero(sp.diff(expression, w) - expected)
            self.zero(a * sp.diff(sp.diff(expression, w), X)
                      - sp.diff(a * sp.diff(expression, X), w))

        c = sp.symbols("c", nonzero=True)
        b0, b1, b2 = sp.symbols("b0 b1 b2")
        obstruction = c * t**4 + b0 + b1 * t + b2 * t**2
        self.assertEqual(sp.degree(obstruction, t), 4)
        self.zero(sp.diff(obstruction, t, 3) - 24 * c * t)
        # The theorem supplying c*Z+Q(X,Y), and the degree/transcendence
        # comparison excluding it, are written arguments, not test outputs.

    def test_affine_parameter_determinant_and_literal_graph_degrees(self):
        U, V, X, yt, yr = sp.symbols("U V X y_t y_rho")
        s, gamma = sp.symbols("s gamma", nonzero=True)
        p = sp.symbols("p0:4")
        pt = sp.symbols("pt0:4")
        pr = sp.symbols("pr0:4")
        b = sp.symbols("b0:7")
        bt = sp.symbols("bt0:7")
        br = sp.symbols("br0:7")
        P = sum(p[j] * U**j for j in range(4))
        Pt = sum(pt[j] * U**j for j in range(4))
        Pr = sum(pr[j] * U**j for j in range(4))
        W = sum(b[j] * U**j for j in range(7))
        Wt = sum(bt[j] * U**j for j in range(7))
        Wr = sum(br[j] * U**j for j in range(7))
        PU, WU = sp.diff(P, U), sp.diff(W, U)
        # Chain-rule columns in (t,rho,v), retaining gamma=y_v and both
        # coefficient derivatives of y. The reduced middle row is undivided.
        rows = sp.Matrix([
            [yt + X, yr, gamma],
            [-s * PU, s, 0],
            [Wt + WU * yt + X * (Pt + PU * yt),
             Wr + WU * yr + X * (Pr + PU * yr) + X**2,
             gamma * (WU + X * PU)],
        ])
        determinant = sp.expand(rows.det())
        self.zero(determinant.coeff(X, 0) + s * gamma * (Wt + PU * Wr))
        self.zero(determinant.coeff(X, 1) - s * gamma * (WU - Pt - PU * Pr))
        self.zero(determinant.coeff(X, 2))
        self.zero(determinant.coeff(X, 3))
        self.zero(determinant - s * gamma * (
            X * (WU - Pt - PU * Pr) - (Wt + PU * Wr)))

        q3 = sp.symbols("q3", nonzero=True)
        q4, k2, k3, nt, ntt, ntr, nrr = sp.symbols("q4 k2 k3 nt ntt ntr nrr")
        ell, ellt, ellr, m = sp.symbols("ell ell_t ell_rho m")
        literal_P = (ell - q3 * U**3 / 6 - k2 * U**2 / 2 - nt * U) / s
        literal_T = (q4 * U**4 / 24 + k3 * U**3 / 6 + ntt * U**2 / 2
                     + ntr * U * V + nrr * V**2 / 2)
        literal_W = sp.expand(
            (m - literal_T.subs(V, literal_P) + ellt * U + ellr * literal_P) / s
        )
        self.zero(s * sp.diff(literal_P, U) + q3 * U**2 / 2 + k2 * U + nt)
        self.assertEqual(sp.Poly(literal_P, U).degree(), 3)
        self.assertLessEqual(sp.Poly(literal_W, U).degree(), 6)
        self.zero(s**3 * literal_W.coeff(U, 6) + nrr * q3**2 / 72)

    def test_top_coefficient_and_quadratic_cover_identity(self):
        U = sp.symbols("U")
        p = sp.symbols("p0:4")
        pr = sp.symbols("pr0:4")
        prr = sp.symbols("prr0:4")
        pt = sp.symbols("pt0:4")
        ptr = sp.symbols("ptr0:4")
        w0, w0r = sp.symbols("w0 w0_rho")
        P = sum(p[j] * U**j for j in range(4))
        Pr = sum(pr[j] * U**j for j in range(4))
        Pt = sum(pt[j] * U**j for j in range(4))
        slope = sp.expand(Pt + sp.diff(P, U) * Pr)
        # Integrate only a polynomial in the independent formal U. This is
        # coefficient division by integers, not integration in a field K.
        W = w0 + sum(slope.coeff(U, j) * U**(j + 1) / (j + 1) for j in range(6))
        self.zero(sp.diff(W, U) - slope)
        self.zero(sp.expand(W).coeff(U, 6) - p[3] * pr[3] / 2)
        Wr = w0r + sum(
            sp.diff(W, p[j]) * pr[j] + sp.diff(W, pr[j]) * prr[j]
            + sp.diff(W, pt[j]) * ptr[j] for j in range(4)
        )
        arbitrary_Wt = sum(sp.Symbol(f"wt{j}") * U**j for j in range(7))
        scalar_equation = sp.expand(arbitrary_Wt + sp.diff(P, U) * Wr)
        self.zero(scalar_equation.coeff(U, 8)
                  - sp.Rational(3, 2) * p[3] * (pr[3]**2 + p[3] * prr[3]))

        s = sp.symbols("s", nonzero=True)
        sr, srr, q3 = sp.symbols("sr srr q3")
        A3 = -q3 / (6 * s)
        Ar = sp.diff(A3, s) * sr
        Arr = sp.diff(Ar, s) * sr + sp.diff(Ar, sr) * srr
        reciprocal_second = 6 * sr**2 / s**4 - 2 * srr / s**3
        self.zero(s**4 * (Ar**2 + A3 * Arr - q3**2 * reciprocal_second / 72))
        eta, etar, etarr = sp.symbols("eta eta_rho eta_rhorho")
        dn_twice_eta = eta * (etar**2 + eta * etarr)
        self.zero(dn_twice_eta - eta * (2 * etar**2 + 2 * eta * etarr) / 2)

        n, ac, bc, cc = sp.symbols("n ac bc cc")
        cover_rho = ac * n**2 / 2 + bc * n + cc
        eta_n = ac * n + bc
        dr = lambda expression: sp.diff(expression, n) / eta_n
        self.zero(dr(cover_rho) - 1)
        self.zero(dr(dr(eta_n**2)))
        self.zero(sp.diff(eta_n, n, 2))
        # These quadratic-cover fixtures are coefficient-field identities,
        # not actual fourfold examples or evidence that L equals K(n).
        cubic_eta = 3 * n**2
        cubic_dr = lambda expression: sp.diff(expression, n) / cubic_eta
        cubic_residual = cubic_dr(cubic_dr(cubic_eta**2))
        self.zero(n**2 * cubic_residual - 4)
        self.assertNotEqual(cubic_residual, 0)


if __name__ == "__main__":
    unittest.main()
