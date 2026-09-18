"""Finite algebra controls for the standalone split coefficients191/192.

The generalized square-completion residual, its old specialization, the
nonaffine split candidate, and local derivative/order calculations are exact
symbolic identities. They do not prove that an actual split chart satisfies
the coefficient premises, that a regular differential has no algebraic
primitive, or that pole degree equals field degree. Those are written-proof
gates. The rational candidate is not an actual frame or a solution of every
remaining potential/cofactor equation. All denominators are coefficient-field
elements, not asserted original-ring units. No earlier checker is imported.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


class SplitCoefficientControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_general_square_completion_and_reciprocal_residual(self):
        U, V, rho = sp.symbols("U V rho")
        R, N = sp.symbols("R N", nonzero=True)
        r1, r2, r3, N1, d, e = sp.symbols("r1 r2 r3 N1 d e")
        k2, k3, nt, nr, ntt, ntr, nrr = sp.symbols("k2 k3 nt nr ntt ntr nrr")
        ell, ellt, ellrho, m = sp.symbols("ell ellt ellrho m")
        S = d * U**3 + k2 * U**2 / 2 + r1 * U * V + nt * U + nr * V
        T = (e * U**4 + k3 * U**3 / 6 + r2 * U**2 * V / 2
             + ntt * U**2 / 2 + ntr * U * V + nrr * V**2 / 2)
        H = sp.expand(R * (T - ellt * U - ellrho * V - m) + (r1 * U + nr) * (ell - S))
        Delta, C4 = R * r2 / 2 - r1**2, e * R - d * r1
        C3 = R * k3 / 6 - r1 * k2 / 2 - d * nr
        self.zero(H.coeff(V, 2) - R * nrr / 2)
        self.zero(H.coeff(V, 1) - (
            Delta * U**2 + (R * ntr - 2 * r1 * nr) * U - R * ellrho - nr**2
        ))
        self.zero(H.coeff(U, 4) - C4)
        self.zero(H.coeff(U, 3).coeff(V, 0) - C3)

        s0, s1, k20, k30 = sp.symbols("s0 s1 k20 k30")
        nrho, ntrho = N * rho + s0, N1 * rho + s1
        C3_rho = R * (r3 * rho + k30) / 6 - r1 * (r2 * rho + k20) / 2 - d * nrho
        b1 = R * ntrho - 2 * r1 * nrho
        amplitude, p2, p1 = R * N / 2, -Delta / (R * N), -b1 / (R * N)
        self.zero(-2 * amplitude * p2 - Delta)
        self.zero(-2 * amplitude * p1 - b1)
        self.zero((amplitude * p2**2 - C4).subs(N, Delta**2 / (2 * R * C4)))
        residual = R * r3 / 6 - r1 * r2 / 2 - d * N - Delta * (N1 / N - 2 * r1 / R)
        self.zero(sp.diff(C3_rho - 2 * amplitude * p2 * p1, rho) - residual)

        # Independent differential jets. e=d'/4, with no fixed choice of q.
        f0, f2 = sp.symbols("f0 f2", nonzero=True)
        f1, f3, d0, d1, d2 = sp.symbols("f1 f3 d0 d1 d2")
        steps = {f0: f1, f1: f2, f2: f3, d0: d1, d1: d2}

        def Dt(expression):
            return sum(sp.diff(expression, variable) * derivative
                       for variable, derivative in steps.items())

        rf0 = 1 / f0
        rf1, rf2, rf3 = Dt(rf0), Dt(Dt(rf0)), Dt(Dt(Dt(rf0)))
        D = d1 * f0 / 4 + d0 * f1
        Dprime = d2 * f0 / 4 + 5 * d1 * f1 / 4 + d0 * f2
        Delta_f = rf0 * rf2 / 2 - rf1**2
        C4_f = d1 * rf0 / 4 - d0 * rf1
        N_f = f2**2 / (8 * f0**3 * D)
        self.zero(Dt(D) - Dprime)
        self.zero(Delta_f + f2 / (2 * f0**3))
        self.zero(C4_f - D / f0**2)
        self.zero(N_f - Delta_f**2 / (2 * rf0 * C4_f))
        self.zero(Dt(N_f) / N_f - (2 * f3 / f2 - 3 * f1 / f0 - Dprime / D))
        reciprocal_residual = (rf0 * rf3 / 6 - rf1 * rf2 / 2 - d0 * N_f
                               - Delta_f * (Dt(N_f) / N_f - 2 * rf1 / rf0))
        general_ode = 20 * D * f3 - 3 * d0 * f2**2 - 12 * f2 * Dprime
        self.zero(24 * f0**3 * D * reciprocal_residual - general_ode)
        expanded_ode = (5 * (d1 * f0 + 4 * d0 * f1) * f3
                        - 15 * d0 * f2**2 - 15 * d1 * f1 * f2 - 3 * d2 * f0 * f2)
        self.zero(general_ode - expanded_ode)
        t = sp.symbols("t")
        old_ode = (f0 + 4 * t * f1) * f3 - 3 * f1 * f2 - 3 * t * f2**2
        self.zero(general_ode.subs({d0: 4 * t, d1: 4, d2: 0}, simultaneous=True) - 20 * old_ode)

    def test_nonaffine_split_candidate_and_all_nonzero_field_gates(self):
        t = sp.symbols("t", nonzero=True)
        q = -t**3 - 1 / t
        d, e = t**(-4) - 1, -t**(-5)
        self.zero(sp.diff(q, t, 3) / 6 - d)
        self.zero(sp.diff(q, t, 4) / 24 - e)
        self.zero(sp.diff(d, t) / 4 - e)
        f = t**5 + 3 * t
        f1, f2, f3 = sp.diff(f, t), sp.diff(f, t, 2), sp.diff(f, t, 3)
        D = e * f + d * f1
        self.zero(D - (1 - 5 * t**4))
        self.zero(sp.diff(D, t) + 20 * t**3)
        terms = (20 * D * f3, -3 * d * f2**2, -12 * f2 * sp.diff(D, t))
        expected = (1200 * t**2 - 6000 * t**6,
                    -1200 * t**2 + 1200 * t**6, 4800 * t**6)
        for term, value in zip(terms, expected):
            self.zero(term - value)
        self.zero(sum(terms))
        self.assertEqual(sp.Poly(f, t).degree(), 5)

        R = 1 / f
        Delta = R * sp.diff(R, t, 2) / 2 - sp.diff(R, t)**2
        C4 = e * R - d * sp.diff(R, t)
        N2 = f2**2 / (8 * f**3 * D)
        self.zero(Delta + 10 / (t**4 + 3)**3)
        self.zero(C4 - (1 - 5 * t**4) / (t**2 * (t**4 + 3)**2))
        self.zero(N2 - 50 * t**3 / ((t**4 + 3)**3 * (1 - 5 * t**4)))
        self.zero(N2 - Delta**2 / (2 * R * C4))
        original_residual = (R * sp.diff(R, t, 3) / 6
                             - sp.diff(R, t) * sp.diff(R, t, 2) / 2 - d * N2
                             - Delta * (sp.diff(N2, t) / N2 - 2 * sp.diff(R, t) / R))
        self.zero(original_residual)
        for expression in (d, e, f, f2, D, R, Delta, C4, N2):
            numerator, denominator = sp.cancel(expression).as_numer_denom()
            self.assertNotEqual(sp.expand(numerator), 0)
            self.assertNotEqual(sp.expand(denominator), 0)
        # Nonzero as rational functions is not nowhere-vanishing on C.
        # This candidate does not satisfy the different old qt4 equation.
        old_residual = (f + 4 * t * f1) * f3 - 3 * f1 * f2 - 3 * t * f2**2
        self.zero(old_residual - 240 * t**3 * (3 - t**4))
        self.assertNotEqual(sp.expand(old_residual), 0)

    def test_split_linear_slope_and_local_pole_arithmetic(self):
        t = sp.symbols("t", nonzero=True)
        d = t**(-4) - 1
        f = sp.Function("f")(t)
        slope = t * f
        residual = 10 * d * sp.diff(slope, t, 2) + 5 * sp.diff(d, t) * sp.diff(slope, t) + sp.diff(d, t, 2) * slope
        self.zero(residual - (10 * d * t * sp.diff(f, t, 2) - 20 * sp.diff(f, t)))
        lam = sp.symbols("lam")
        self.zero(10 * d * sp.diff(lam * t, t, 2)
                  + 5 * sp.diff(d, t) * sp.diff(lam * t, t) + sp.diff(d, t, 2) * lam * t)
        j = sp.symbols("j")
        jprime = 2 * t**3 * j / (1 - t**4)
        self.zero(d * t * jprime - 2 * j)
        self.zero(2 * j * jprime * (1 - t**4) - 4 * t**3 * j**2)

        # Algebraic curve chart identities behind the regular differential.
        # They do not test its nonzero pullback or the no-primitive theorem.
        v = sp.symbols("v", nonzero=True)
        vprime = -2 * t**3 / v
        self.zero(2 * v * vprime + 4 * t**3)
        self.zero((jprime * v + j * vprime) * v * (1 - t**4)
                  - 2 * t**3 * j * (v**2 - (1 - t**4)))
        s, V = sp.symbols("s V", nonzero=True)
        self.zero((v**2 - (1 - t**4)).subs({t: 1 / s, v: V / s**2}, simultaneous=True)
                  * s**4 - (V**2 - s**4 + 1))
        self.zero(sp.diff(1 / s, s) / (V / s**2) + 1 / V)

        # Finite even-ramification leading-term controls at the simple root t=1.
        # Actual existence, evenness, and pole-degree interpretation are proved
        # in191, not inferred from these selected values of the ramification.
        A = sp.symbols("A", nonzero=True)
        falling = sp.Rational(-1, 2) * sp.Rational(-3, 2) * sp.Rational(-5, 2)
        self.assertEqual(falling, sp.Rational(-15, 8))
        self.zero(sp.diff(d, t).subs(t, 1) + 4)
        for ramification in (2, 4, 6):
            t_local = 1 + s**ramification

            def local_Dt(expression):
                return sp.diff(expression, s) / (ramification * s**(ramification - 1))

            a_leading = A * s**sp.Rational(-ramification, 2)
            third = local_Dt(local_Dt(local_Dt(a_leading)))
            self.zero(local_Dt(t_local) - 1)
            self.zero(third - falling * A * s**sp.Rational(-7 * ramification, 2))
            gamma_leading = third / (18 * (-4 * s**ramification))
            self.zero(gamma_leading - 5 * A * s**sp.Rational(-9 * ramification, 2) / 192)
            pole_order = sp.Rational(9 * ramification, 2)
            self.assertTrue(pole_order.is_integer)
            self.assertGreaterEqual(pole_order, 9)


if __name__ == "__main__":
    unittest.main()
