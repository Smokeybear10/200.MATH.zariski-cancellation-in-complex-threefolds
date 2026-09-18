"""Finite algebra controls for nonzero-R quartic-graph reduction189.

The literal eliminant, square-completion coefficients, reciprocal ODE
identity and local-leading coefficient arithmetic are checked independently
of any earlier checker. These finite identities do not prove whole-line
return, the evaluated-unit assertion, existence of a place at infinity, or
the exhaustive algebraic-function lemma. Those remain written-proof gates.
Formal nested lines and ramified fields below are not actual 1122 frames.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


class AbsentNonzeroRQuarticGraphControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_eliminant_degree_drop_and_two_square_models(self):
        U, V, t = sp.symbols("U V t")
        R = sp.symbols("R", nonzero=True)
        r1, r2, k2, k3 = sp.symbols("r1 r2 k2 k3")
        nt, nr, ntt, ntr, nrr = sp.symbols("nt nr ntt ntr nrr")
        ell, ellt, ellr, m = sp.symbols("ell ellt ellr m")
        S = 4 * t * U**3 + k2 * U**2 / 2 + r1 * U * V + nt * U + nr * V
        T = (U**4 + k3 * U**3 / 6 + r2 * U**2 * V / 2
             + ntt * U**2 / 2 + ntr * U * V + nrr * V**2 / 2)
        A1 = r1 * U + nr
        H = sp.expand(R * (T - ellt * U - ellr * V - m) + A1 * (ell - S))
        delta = R * r2 / 2 - r1**2
        C4 = R - 4 * t * r1
        C3 = R * k3 / 6 - r1 * k2 / 2 - 4 * t * nr
        self.assertEqual(sp.Poly(H, V).degree(), 2)
        self.zero(H.coeff(V, 2) - R * nrr / 2)
        self.zero(H.coeff(V, 1) - (
            delta * U**2 + (R * ntr - 2 * r1 * nr) * U
            - R * ellr - nr**2
        ))
        self.zero(H.coeff(U, 4) - C4)
        self.zero(H.coeff(U, 3).coeff(V, 0) - C3)
        top4 = sum(coefficient * U**i * V**j
                   for (i, j), coefficient in sp.Poly(H, U, V).terms()
                   if i + j == 4)
        self.zero(top4 - C4 * U**4)

        # Staged prior relations C4=0 and its t derivative. Their actual
        # impossibility also needs the written unit-cofactor/infinity proof.
        dropped = sp.expand(H.subs(
            {r1: R / (4 * t), r2: -3 * R / (16 * t**2)}, simultaneous=True
        ))
        self.assertEqual(sp.Poly(dropped, U, V).total_degree(), 3)
        self.zero(delta.subs(
            {r1: R / (4 * t), r2: -3 * R / (16 * t**2)}, simultaneous=True
        ) + 5 * R**2 / (32 * t**2))
        top3 = sum(coefficient * U**i * V**j
                   for (i, j), coefficient in sp.Poly(dropped, U, V).terms()
                   if i + j == 3)
        self.zero(top3 - U**2 * (
            (R * k3 / 6 - R * k2 / (8 * t) - 4 * t * nr) * U
            - 5 * R**2 * V / (32 * t**2)
        ))

        # R^4=t really is possible in an algebraic coefficient field.
        # It is not excluded just because R is nonrational in t.
        s = sp.symbols("s", nonzero=True)

        def ramified_t_derivative(expression):
            return sp.diff(expression, s) / (4 * s**3)

        R_alg, t_alg = s, s**4
        r1_alg = ramified_t_derivative(R_alg)
        r2_alg = ramified_t_derivative(r1_alg)
        self.zero(R_alg**4 - t_alg)
        self.zero(R_alg - 4 * t_alg * r1_alg)
        self.zero(R_alg * r2_alg / 2 - r1_alg**2 + 5 / (32 * s**6))

        # The two exact plane models, not actual chart realizations.
        d, omega, a = sp.symbols("d omega a", nonzero=True)
        p2 = sp.symbols("p2", nonzero=True)
        p1, p0, b, zeta = sp.symbols("p1 p0 b zeta")
        P = p2 * U**2 + p1 * U + p0
        G = V - P
        graph_model = omega * G + d * G**2
        shifted_P = P - omega / (2 * d)
        self.zero(graph_model - (
            d * (V - shifted_P)**2 - omega**2 / (4 * d)
        ))
        nested_model = d * ((V - P)**2 - a * U - b)
        y = (zeta**2 - b) / a
        theta = P.subs(U, y) + zeta
        self.zero(nested_model.subs({U: y, V: theta}, simultaneous=True))
        self.zero(theta - P.subs(U, y) - zeta)
        for model in (graph_model, nested_model):
            self.assertEqual(sp.Poly(model, U, V).total_degree(), 4)
            self.assertEqual(sp.Poly(model, V).degree(), 2)
            self.zero(sp.expand(model).coeff(U, 4) - d * p2**2)
            self.zero(sp.expand(model).coeff(U, 2).coeff(V, 1) + 2 * d * p2)

    def test_square_coefficients_and_exact_reciprocal_ode(self):
        t, rho = sp.symbols("t rho")
        R, N = sp.symbols("R N", nonzero=True)
        r1, r2, r3, N1 = sp.symbols("r1 r2 r3 N1")
        s0, s1, k2, k3 = sp.symbols("s0 s1 k2 k3")
        delta = R * r2 / 2 - r1**2
        C4 = R - 4 * t * r1
        nr = N * rho + s0
        ntr = N1 * rho + s1
        b1 = R * ntr - 2 * r1 * nr
        C3 = R * (r3 * rho + k3) / 6 - r1 * (r2 * rho + k2) / 2 - 4 * t * nr
        d = R * N / 2
        p2, p1 = -delta / (R * N), -b1 / (R * N)
        self.zero(-2 * d * p2 - delta)
        self.zero(-2 * d * p1 - b1)
        self.zero(2 * d * p2 * p1 - delta * b1 / (R * N))
        N_forced = delta**2 / (2 * R * C4)
        self.zero((d * p2**2 - C4).subs(N, N_forced))
        residual = R * r3 / 6 - r1 * r2 / 2 - 4 * t * N - delta * (
            N1 / N - 2 * r1 / R
        )
        self.zero(sp.diff(C3 - 2 * d * p2 * p1, rho) - residual)

        # Independent differential jets for f=1/R; differentiation does not
        # presume a rational actual coefficient field.
        f0, f2 = sp.symbols("f0 f2", nonzero=True)
        f1, f3 = sp.symbols("f1 f3")

        def Dt(expression):
            return (sp.diff(expression, t)
                    + sp.diff(expression, f0) * f1
                    + sp.diff(expression, f1) * f2
                    + sp.diff(expression, f2) * f3)

        r0f = 1 / f0
        r1f, r2f = Dt(r0f), Dt(Dt(r0f))
        r3f = Dt(r2f)
        deltaf = r0f * r2f / 2 - r1f**2
        Df = f0 + 4 * t * f1
        C4f = r0f - 4 * t * r1f
        Nf = f2**2 / (8 * f0**3 * Df)
        self.zero(deltaf + f2 / (2 * f0**3))
        self.zero(C4f - Df / f0**2)
        self.zero(Nf - deltaf**2 / (2 * r0f * C4f))
        self.zero(Dt(Nf) / Nf - (
            2 * f3 / f2 - 3 * f1 / f0 - (5 * f1 + 4 * t * f2) / Df
        ))
        rf = (r0f * r3f / 6 - r1f * r2f / 2 - 4 * t * Nf
              - deltaf * (Dt(Nf) / Nf - 2 * r1f / r0f))
        ode = Df * f3 - 3 * f1 * f2 - 3 * t * f2**2
        self.zero(6 * f0**3 * Df * rf - 5 * ode)

        # Surviving pure quartic-graph coefficient equations. These identities
        # allow A=0 or C=0; they are not an actual realization or an inverse.
        A, B, C = sp.symbols("A B C")
        r = 1 / (A * t + B)
        sn = C * r**2
        self.zero(r * sp.diff(r, t, 2) / 2 - sp.diff(r, t)**2)
        self.zero(r * sp.diff(sn, t) - 2 * sp.diff(r, t) * sn)
        self.zero(r - 4 * t * sp.diff(r, t) - (5 * A * t + B) / (A * t + B)**2)

    def test_puiseux_indicial_and_first_tail_arithmetic(self):
        mu, p, t, eps = sp.symbols("mu p t eps")
        a, b, c = sp.symbols("a b c")
        fall2_mu = mu * (mu - 1)
        fall3_mu = fall2_mu * (mu - 2)
        indicial = (1 + 4 * mu) * fall3_mu - 3 * mu * fall2_mu - 3 * fall2_mu**2
        self.zero(indicial - mu * (mu - 1) * (mu**2 - 7 * mu - 2))
        self.assertEqual(sp.discriminant(mu**2 - 7 * mu - 2, mu), 57)
        self.assertFalse(sp.sqrt(57).is_rational)

        h0, h1, h2, h3 = sp.symbols("h0 h1 h2 h3")
        F, Ft, Ftt, Fttt = a * t + b + eps * h0, a + eps * h1, eps * h2, eps * h3
        equation = sp.expand((F + 4 * t * Ft) * Fttt - 3 * Ft * Ftt - 3 * t * Ftt**2)
        self.zero(equation.coeff(eps, 0))
        self.zero(equation.coeff(eps, 1) - ((5 * a * t + b) * h3 - 3 * a * h2))
        self.zero(equation.coeff(eps, 2) - (
            h0 * h3 + 4 * t * h1 * h3 - 3 * h1 * h2 - 3 * t * h2**2
        ))
        self.assertEqual(sp.Poly(equation, eps).degree(), 2)
        fall2, fall3 = p * (p - 1), p * (p - 1) * (p - 2)
        self.zero(5 * fall3 - 3 * fall2 - p * (p - 1) * (5 * p - 13))
        # The strict exponent comparisons for every rational p in the written
        # ranges are proof steps. These identities exhibit the exact gaps.
        self.zero((2 * p - 3) - (p - 3) - p)
        self.zero((2 * p - 3) - (p - 2) - (p - 1))

        # Ramified local derivative compatibility, not existence of the place.
        local_s = sp.symbols("local_s", nonzero=True)
        for e in (1, 2, 5):
            t_local = local_s**(-e)

            def local_Dt(expression):
                return -local_s**(e + 1) * sp.diff(expression, local_s) / e

            self.zero(local_Dt(t_local) - 1)
            tail = local_s**3
            exponent = -sp.Rational(3, e)
            self.zero(local_Dt(tail) - exponent * tail / t_local)
            self.zero(local_Dt(local_Dt(tail)) - exponent * (exponent - 1) * tail / t_local**2)
        # No finite set of tails substitutes for the general local expansion
        # and injectivity argument in the proof.


if __name__ == "__main__":
    unittest.main()
