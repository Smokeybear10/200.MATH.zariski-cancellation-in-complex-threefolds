"""Independent finite coefficient controls for the two split square gates.

The formal jets and rational functions below are not actual fourfold frames.
These controls do not prove the whole-line hypothesis, scalar-Jacobian gate,
Puiseux exhaustiveness, or a geometric recognition theorem. Those require the
separate written193/194 arguments. No earlier checker or solver is imported.
"""

import unittest

import sympy as sp


class SplitTwoGateControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def leading(self, expression, variable):
        numerator, denominator = sp.cancel(expression).as_numer_denom()
        numerator = sp.Poly(numerator, variable)
        denominator = sp.Poly(denominator, variable)
        return (numerator.degree() - denominator.degree(),
                sp.cancel(numerator.LC() / denominator.LC()))

    def test_general_cubic_rho_and_odd_jacobian_coefficients(self):
        U, V, rho, zeta = sp.symbols("U V rho zeta")
        R, R1, R2 = sp.symbols("R R1 R2")
        N, N1, N2 = sp.symbols("N N1 N2")
        k2, k3, s, s1, s2, n1, n2 = sp.symbols("k2 k3 s s1 s2 n1 n2")
        ell_coeff = sp.symbols("ell0:4")
        ell_t_coeff = sp.symbols("ellt0:4")
        ell = sum(ell_coeff[j] * rho**j for j in range(4))
        ellt = sum(ell_t_coeff[j] * rho**j for j in range(4))
        nr = N * rho + s
        nt = N1 * rho**2 / 2 + s1 * rho + n1
        ntt = N2 * rho**2 / 2 + s2 * rho + n2
        ntr = N1 * rho + s1
        ktt = R2 * rho + k2
        d, e, m = sp.symbols("d e m")
        S = d * U**3 + ktt * U**2 / 2 + R1 * U * V + nt * U + nr * V
        T = (e * U**4 + k3 * U**3 / 6 + R2 * U**2 * V / 2
             + ntt * U**2 / 2 + ntr * U * V + N * V**2 / 2)
        H = sp.Poly(sp.expand(R * (T - ellt * U - sp.diff(ell, rho) * V - m)
                             + (R1 * U + nr) * (ell - S)), U, V)
        Delta = R * R2 / 2 - R1**2
        B = R * ntr - 2 * R1 * nr
        C2 = R * ntt / 2 - R1 * nt - nr * ktt / 2
        C = -R * sp.diff(ell, rho) - nr**2
        self.zero(H.coeff_monomial(U * V) - B)
        self.zero(H.coeff_monomial(U**2) - C2)
        self.zero(H.coeff_monomial(V) - C)
        self.zero(H.coeff_monomial(U) + R * ellt - R1 * ell + nr * nt)
        B1 = H.coeff_monomial(U) - B * C / (R * N)
        cubic_rho = sp.Poly(sp.expand(B1), rho).coeff_monomial(rho**3)
        B_high = R * N1 - 2 * R1 * N
        C2_high = R * N2 / 4 - R1 * N1 / 2 - N * R2 / 2
        E3, E3t = ell_coeff[3], ell_t_coeff[3]
        expected_cubic = (-R * E3t + R1 * E3 - N * N1 / 2
                          + B_high * (3 * R * E3 + N**2) / (R * N))
        self.zero(cubic_rho - expected_cubic)
        ell_r = B**2 / (2 * Delta * R) - N * C2 / Delta - nr**2 / R
        L3 = sp.Poly(sp.expand(ell_r), rho).coeff_monomial(rho**2) / 3
        self.zero(L3 - (B_high**2 / (2 * Delta * R)
                        - N * C2_high / Delta - N**2 / R) / 3)
        p2 = -Delta / (R * N)
        p1_rho = 2 * R1 / R - N1 / N
        root_L3 = (C2_high - R * N * p1_rho**2 / 2 - N**2 * p2) / (3 * R * p2)
        self.zero(L3 - root_L3)
        self.zero(expected_cubic - (-R * E3t + R1 * E3 - N * N1 / 2
                                     - p1_rho * (3 * R * E3 + N**2)))

        # Independent differential rows, with coefficient partials fixing U
        # before U=y is substituted. The phi relation is not differentiated
        # as if its evaluated coefficients were fixed.
        a, b, at, ar, bt, br, B1_symbol = sp.symbols("a b at ar bt br B1")
        p2_symbol, p1, l = sp.symbols("p2 p1 l")
        Z2t, Z1t, Z0t, Z1r, Z0r = sp.symbols("Z2t Z1t Z0t Z1r Z0r")
        y = a * zeta**2 + b
        yt, yr, yz = at * zeta**2 + bt, ar * zeta**2 + br, 2 * a * zeta
        Py = 2 * p2_symbol * y + p1
        zt = Z2t * y**2 + Z1t * y + Z0t + R1 * zeta
        zr = Z1r * y + Z0r
        Ft = N * Py * zeta - B1_symbol / R
        Fr = -N * zeta
        rows = sp.Matrix([[yt, yr, yz], [zt, zr, R],
                          [(Ft - l * zt) / R, (Fr - l * zr) / R, -l]])
        determinant = sp.expand(rows.det())
        wedge = yr * Ft - yt * Fr + yz * (zt * Fr - zr * Ft) / R
        self.zero(determinant - wedge)
        self.zero(sp.Poly(determinant, zeta).coeff_monomial(zeta**5)
                  - 2 * N * p2_symbol * a * ar)
        rewritten = (-B1_symbol * yr / R
                     + N * zeta * (Py * yr + yt - zr / R)
                     + N**2 * zeta**2 * (zt + Py * zr) / B1_symbol)
        self.zero((wedge - rewritten).subs(a, -R * N / (2 * B1_symbol)))

    def test_symbolic_dominant_coefficients(self):
        t = sp.symbols("t")
        a, b, c, mu, lam = sp.symbols("a b c mu lam", nonzero=True)
        fall2 = mu * (mu - 1)
        fall3 = mu * (mu - 1) * (mu - 2)
        self.zero(a**2 * (-20 * mu * fall3 + 15 * fall2**2)
                  + 5 * a**2 * mu**2 * (mu - 1) * (mu - 5))
        tail_linear = -20 * b * c * lam * (lam - 1) * (lam - 2)
        tail_linear -= 60 * b * c * lam * (lam - 1)
        self.zero(tail_linear + 20 * b * c * lam * (lam - 1) * (lam + 1))
        tail_nonlinear = -5 * c**2 * lam**2 * (lam - 1) * (lam - 5)
        self.zero((tail_linear + tail_nonlinear).subs(lam, -4)
                  - 1200 * c * (b - 3 * c))
        # Strict exponent comparisons in the proof are universal inequalities,
        # not established by sampling. Here their differences are checked.
        self.zero((lam - 3) - (2 * lam - 4) - (1 - lam))
        self.zero((2 * lam - 4) - (lam - 8) - (lam + 4))

        R = 1 / (a * t**5)
        N = -10 / (a**2 * t**13)
        p2, p1 = -a * t**6, 3 / t
        L_terms = [R * sp.diff(N, t, 2) / 4,
                   -sp.diff(R, t) * sp.diff(N, t) / 2,
                   -N * sp.diff(R, t, 2) / 2,
                   -R * N * p1**2 / 2, -N**2 * p2]
        for term, coefficient in zip(L_terms, (-455, 325, 150, 45, 100)):
            self.zero(term - coefficient / (a**3 * t**20))
        L3 = sp.cancel(sum(L_terms) / (3 * R * p2))
        self.zero(L3 + 55 / (a**3 * t**21))
        J_terms = [-R * sp.diff(L3, t), sp.diff(R, t) * L3,
                   -N * sp.diff(N, t) / 2, -p1 * (3 * R * L3 + N**2)]
        for term, coefficient in zip(J_terms, (-1155, 275, 650, 195)):
            self.zero(term - coefficient / (a**4 * t**27))
        self.zero(sum(J_terms) + 35 / (a**4 * t**27))

        # Truncated leading models retain R's first nonconstant correction.
        # They control arithmetic only, not the existence of Puiseux series.
        R = 1 / b - 1 / (3 * b * t**4)
        N = 50 / (3 * b**2 * t**7)
        p2, p1 = b * t / 5, 7 / t
        L_terms = [R * sp.diff(N, t, 2) / 4,
                   -sp.diff(R, t) * sp.diff(N, t) / 2,
                   -N * sp.diff(R, t, 2) / 2,
                   -R * N * p1**2 / 2, -N**2 * p2]
        for term, degree in zip(L_terms, (-9, -13, -13, -9, -13)):
            self.assertEqual(self.leading(term, t)[0], degree)
        L3 = sp.cancel(sum(L_terms) / (3 * R * p2))
        degree, coefficient = self.leading(L3, t)
        self.assertEqual(degree, -10)
        self.zero(coefficient + 875 / (3 * b**3))
        L_lead = -875 / (3 * b**3 * t**10)
        J = (-R * sp.diff(L_lead, t) + sp.diff(R, t) * L_lead
             - N * sp.diff(N, t) / 2 - p1 * (3 * R * L_lead + N**2))
        degree, coefficient = self.leading(J, t)
        self.assertEqual(degree, -11)
        self.zero(coefficient - 9625 / (3 * b**4))

    def test_both_exact_rational_first_gate_candidates(self):
        t = sp.symbols("t")
        d = t**-4 - 1

        def gates(f):
            R = sp.cancel(1 / f)
            D = sp.cancel(sp.diff(d, t) * f / 4 + d * sp.diff(f, t))
            residual = (20 * D * sp.diff(f, t, 3) - 3 * d * sp.diff(f, t, 2)**2
                        - 12 * sp.diff(f, t, 2) * sp.diff(D, t))
            N = sp.cancel(sp.diff(f, t, 2)**2 / (8 * f**3 * D))
            Delta = sp.cancel(R * sp.diff(R, t, 2) / 2 - sp.diff(R, t)**2)
            p2 = sp.cancel(-Delta / (R * N))
            p1 = sp.cancel(2 * sp.diff(R, t) / R - sp.diff(N, t) / N)
            C2_high = sp.cancel(R * sp.diff(N, t, 2) / 4
                                - sp.diff(R, t) * sp.diff(N, t) / 2
                                - N * sp.diff(R, t, 2) / 2)
            L3 = sp.cancel((C2_high - R * N * p1**2 / 2 - N**2 * p2)
                           / (3 * R * p2))
            J3 = sp.cancel(-R * sp.diff(L3, t) + sp.diff(R, t) * L3
                           - N * sp.diff(N, t) / 2 - p1 * (3 * R * L3 + N**2))
            return residual, L3, J3

        A, B = sp.symbols("A B")
        f = A + B / t**4
        D = sp.diff(d, t) * f / 4 + d * sp.diff(f, t)
        residual = (20 * D * sp.diff(f, t, 3) - 3 * d * sp.diff(f, t, 2)**2
                    - 12 * sp.diff(f, t, 2) * sp.diff(D, t))
        self.zero(residual - 1200 * B * (A - 3 * B) / t**12)
        residual, L3, J3 = gates(t**5 + 3 * t)
        denominator = (t**4 + 3)**5 * (5 * t**4 - 1)**3
        self.zero(residual)
        self.zero(L3 + 125 * t**3 * (5 * t**4 + 3) * (11 * t**4 - 7) / denominator)
        self.zero(J3 + 875 * t * (5 * t**4 - 11) / denominator)
        self.assertNotEqual(sp.cancel(J3), 0)
        residual, L3, J3 = gates(3 + t**-4)
        denominator = (t**4 - 5)**3 * (3 * t**4 + 1)**5
        self.zero(residual)
        self.zero(L3 + 125 * t**14 * (3 * t**4 + 5) * (7 * t**4 - 11) / denominator)
        self.zero(J3 - 875 * t**17 * (11 * t**4 - 5) / denominator)
        degree, coefficient = self.leading(J3, t)
        self.assertEqual(degree, -11)
        self.zero(coefficient - sp.Rational(9625, 243))
        self.assertNotEqual(sp.cancel(J3), 0)


if __name__ == "__main__":
    unittest.main()
