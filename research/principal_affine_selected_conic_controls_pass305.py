"""Finite exact controls for pass305, with no earlier checker imports.

The tests reconstruct cubic coefficients, a selected-factor gradient
identity, and exact differential algebra. They do not prove actual chart
entry, the minor-unit theorem, whole-ring return, or global cancellation.
The source must be read in full before its sole canonical execution.
"""

import unittest

import sympy as sp


def exact(expression):
    return sp.cancel(sp.expand(expression))


class AffineSelectedConicControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(exact(expression), 0)

    def test_generic_surface_cubic_coefficients_determine_slopes(self):
        t, s, U, P, V, h = sp.symbols("t s U P V h")
        m, f = sp.Function("m")(t), sp.Function("f")(t)
        k = m * s + f
        n, ell = sp.Function("n")(t, s), sp.Function("ell")(t, s)
        mt, mtt = sp.diff(m, t), sp.diff(m, t, 2)
        F = sp.diff(k, t, 2) * P**2 / 2 + mt * P * V
        F += sp.diff(n, t) * P + sp.diff(n, s) * V
        g = (ell - (2 * P + sp.diff(k, t)) * U - F) / m
        H3 = sp.diff(k, t, 3) * P**3 / 6 + mtt * P**2 * V / 2
        H2 = sp.diff(n, t, 2) * P**2 / 2
        H2 += sp.diff(n, t, s) * P * V + sp.diff(n, s, 2) * V**2 / 2
        H = U**2 + sp.diff(F, P) * U + sp.diff(F, V) * g
        H += H3 + H2 - sp.diff(ell, t) * P - sp.diff(ell, s) * V - h
        H = exact(H)
        A1 = sp.Poly(H, U).coeff_monomial(U)
        A0 = H.subs(U, 0)

        def homogeneous(poly, degree):
            return sp.Add(*(
                coefficient * P**i * V**j
                for (i, j), coefficient in sp.Poly(poly, P, V).terms()
                if i + j == degree
            ))

        self.assert_zero(homogeneous(A1, 2) + 2 * mt * P**2 / m)
        bp = sp.diff(k, t, 2) / 4 - m * sp.diff(k, t, 3) / (12 * mt)
        bv = mt / 2 - m * mtt / (4 * mt)
        self.assert_zero(homogeneous(A0, 3) + 2 * mt * P**2 * (bp * P + bv * V) / m)
        self.assert_zero(mt - 2 * bv - m * mtt / (2 * mt))
        self.assert_zero(sp.diff(bv, s))

    def test_selected_factor_chain_rule_and_unit_fixture(self):
        U, P, V, eta, bp, bv, b0 = sp.symbols("U P V eta bp bv b0")
        B = bp * P + bv * V + b0
        G = V - P**2
        A = B + eta + G
        H = (U + A) * (U + B)
        Q = G + (U + B) * (U * V + P)
        evaluation = {U: -B.subs(V, P**2), V: P**2}
        hu, hp, hv = [sp.diff(H, x).subs(evaluation, simultaneous=True) for x in (U, P, V)]
        qu, qp, qv = [sp.diff(Q, x).subs(evaluation, simultaneous=True) for x in (U, P, V)]
        self.assert_zero(hu - eta)
        self.assert_zero(hp - eta * bp)
        self.assert_zero(hv - eta * bv)
        q = sp.expand(Q.subs(U, -B))
        self.assert_zero(q - G)
        self.assert_zero(qp - bp * qu + 2 * P)
        self.assert_zero(qv - bv * qu - 1)
        self.assert_zero(hu * qv - hv * qu - eta)
        self.assert_zero(hp * qv - hv * qp - eta * (bp + 2 * bv * P))
        # A zero eta would remove the nonzero first gradient on the curve.
        self.assert_zero(hu.subs(eta, 0))

    def test_formal_slope_and_exact_ode_integration(self):
        t, s, P, V = sp.symbols("t s P V")
        m, f = sp.Function("m")(t), sp.Function("f")(t)
        n, b0 = sp.Function("n")(t, s), sp.Function("b0")(t, s)
        k = m * s + f
        mt, mtt, mttt = [sp.diff(m, t, order) for order in (1, 2, 3)]
        bp = sp.diff(k, t, 2) / 4 - m * sp.diff(k, t, 3) / (12 * mt)
        bv = mt / 2 - m * mtt / (4 * mt)
        B = bp * P + bv * V + b0
        D, lam = (2 * P + sp.diff(k, t)) / m, (mt * P + sp.diff(n, s)) / m
        bracket = exact(sp.diff(B, s) - bv * (bp - D * bv + lam))
        slope = sp.Poly(bracket, P, V).coeff_monomial(P)
        self.assert_zero(sp.diff(bracket, V))
        self.assert_zero(slope + m * (2 * mt * mttt - 3 * mtt**2) / (24 * mt**2))
        r = mtt / (2 * mt)
        self.assert_zero((sp.diff(r, t) - r**2).subs(mttt, 3 * mtt**2 / (2 * mt)))
        tau = t + 1 / r
        self.assert_zero(sp.diff(tau, t).subs(mttt, 3 * mtt**2 / (2 * mt)))
        T = -2 * mt / mtt
        self.assert_zero(2 * T * mt + T**2 * mtt)
        # The zero-curvature solution also solves the ODE, but cannot
        # support the genuine conic because its formal V slope is zero.
        linear = t + 1
        self.assert_zero(2 * sp.diff(linear, t) * sp.diff(linear, t, 3) - 3 * sp.diff(linear, t, 2)**2)
        self.assert_zero(linear * sp.diff(linear, t, 2) / (2 * sp.diff(linear, t)))

    def test_reciprocal_family_and_non_solution_control(self):
        t, d, c, tau = sp.symbols("t d c tau")
        m = d + c / (t - tau)
        mt, mtt, mttt = [sp.diff(m, t, order) for order in (1, 2, 3)]
        self.assert_zero(2 * mt * mttt - 3 * mtt**2)
        self.assert_zero(mt / 2 - m * mtt / (4 * mt) - d / (2 * (t - tau)))
        self.assert_zero((t - tau)**2 * mt + c)
        self.assert_zero((mt / 2 - m * mtt / (4 * mt)).subs(d, 0))
        wrong = t**2
        residual = 2 * sp.diff(wrong, t) * sp.diff(wrong, t, 3) - 3 * sp.diff(wrong, t, 2)**2
        self.assertEqual(residual, -12)


if __name__ == "__main__":
    unittest.main()
