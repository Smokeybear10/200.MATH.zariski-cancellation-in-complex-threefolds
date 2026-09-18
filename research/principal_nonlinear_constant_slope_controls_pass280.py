"""Independent finite polynomial controls for nonlinear restriction280.

This checks full formal gradients, the homogeneous degree gates,
whole-line fixtures, discriminant coefficients and the reciprocal gate.
It does not certify pure-top multiplicities, exact-field integration,
actual chart entry, or recognition. No retained checker is imported.
"""

import unittest

import sympy as S


class NonlinearConstantSlopeControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    @staticmethod
    def data():
        t, n, U, P = S.symbols("t n U P")
        b, c, k = (S.Function(name)(t) for name in ("b", "c", "k"))
        T, omega = (S.Function(name)(t, n) for name in ("T", "omega"))
        H = b * n + c
        A = (2 * P + S.diff(k, t)) * U + S.diff(k, t, 2) * P**2 / 2
        C = U**2 + S.diff(k, t, 2) * P * U + S.diff(k, t, 3) * P**3 / 6
        W = (
            omega - (S.diff(H, n, t) * P + S.diff(T, n)) * A
            - b * C + S.diff(H, t) * U
            + S.diff(H, t, 2) * P**2 / 2 + S.diff(T, t) * P
        )
        QU = S.expand((2 * P + S.diff(k, t)) * S.diff(W, n) - S.diff(W, P))
        QP = S.expand((2 * U + S.diff(k, t, 2) * P) * S.diff(W, n) - S.diff(W, t))
        primitive = S.integrate(QU, U)
        primitive += S.integrate(S.expand(QP - S.diff(primitive, P)), P)
        return t, n, U, P, b, c, k, T, omega, QU, QP, S.expand(primitive)

    @staticmethod
    def homogeneous(expression, U, P, degree):
        return sum(
            coefficient * U**i * P**j
            for (i, j), coefficient in S.Poly(expression, U, P).terms()
            if i + j == degree
        )

    def test_full_primitive_and_quartic_top_before_restriction(self):
        t, n, U, P, b, c, k, T, omega, QU, QP, Q = self.data()
        self.assert_zero(S.diff(Q, U) - QU)
        self.assert_zero(S.diff(Q, P) - QP)
        self.assert_zero(Q.subs({U: 0, P: 0}))
        self.assertLessEqual(S.Poly(Q, U, P).total_degree(), 4)
        expected = P**2 * (
            -2 * S.diff(T, n, 2) * U**2
            + (S.diff(b, t, 2) - S.diff(T, n, 2) * S.diff(k, t, 2)) * U * P
            + (b * S.diff(k, t, 4) + 4 * S.diff(b, t) * S.diff(k, t, 3)
               + 6 * S.diff(b, t, 2) * S.diff(k, t, 2)
               - 3 * S.diff(T, n, 2) * S.diff(k, t, 2)**2) * P**2 / 24
        )
        self.assert_zero(self.homogeneous(Q, U, P, 4) - expected)
        p, q = S.Function("p")(t), S.Function("q")(t)
        reduced = Q.subs(T, p * n + q).doit()
        reduced = S.expand(reduced.subs({S.diff(b, t, 3): 0, S.diff(b, t, 2): 0}))
        self.assert_zero(reduced.coeff(U, 2) - 3 * S.diff(b, t) * P - b * S.diff(k, t, 2) / 2 - p - S.diff(b, t) * S.diff(k, t))
        self.assert_zero(self.homogeneous(reduced, U, P, 4) - (b * S.diff(k, t, 4) + 4 * S.diff(b, t) * S.diff(k, t, 3)) * P**4 / 24)
        self.assert_zero(self.homogeneous(reduced, U, P, 3).subs(P, 0))
        self.assert_zero(S.Poly(reduced, U, P).coeff_monomial(U**2 * P) - 3 * S.diff(b, t))

    def test_entire_constant_slope_coefficient_table(self):
        t, n, U, P, b, c, k, T, omega, QU, QP, Q = self.data()
        h = S.symbols("h", nonzero=True)
        p, q = S.Function("p")(t), S.Function("q")(t)
        reduced = S.expand(Q.subs(T, p * n + q).doit().subs(b, h).doit())
        B = h * S.diff(k, t, 2) / 2 + p
        C2 = h * S.diff(k, t, 3) / 2 + 2 * S.diff(p, t)
        C1 = p * S.diff(k, t, 2) - S.diff(c, t, 2) + S.diff(k, t) * S.diff(p, t) + 2 * S.diff(omega, n)
        C0 = -n * S.diff(p, t) + S.diff(k, t) * S.diff(omega, n) - S.diff(q, t)
        D4 = h * S.diff(k, t, 4) / 24
        D3 = (p * S.diff(k, t, 3) - S.diff(c, t, 3) + 3 * S.diff(k, t, 2) * S.diff(p, t)) / 6
        D2 = -n * S.diff(p, t, 2) / 2 + S.diff(k, t, 2) * S.diff(omega, n) / 2 - S.diff(q, t, 2) / 2
        D1 = -S.diff(omega, t)
        target = B * U**2 + (C2 * P**2 + C1 * P + C0) * U + D4 * P**4 + D3 * P**3 + D2 * P**2 + D1 * P
        self.assert_zero(reduced - target)
        self.assert_zero(C2 - S.diff(B, t) - S.diff(p, t))
        graph_value = -h * S.diff(k, t, 2) / 2
        self.assert_zero(C2.subs(p, graph_value).doit() + h * S.diff(k, t, 3) / 2)
        # Dropping omega's coefficient derivatives changes two gradient entries.
        omitted = target.subs({S.diff(omega, n): 0, S.diff(omega, t): 0})
        self.assertNotEqual(S.expand(target - omitted), 0)
        self.assert_zero(S.expand(target - omitted).coeff(U, 1) - (2 * P + S.diff(k, t)) * S.diff(omega, n))

    def test_whole_line_fixtures_and_discriminant_reciprocal_gate(self):
        U, P, x, n = S.symbols("U P x n")
        a, beta, B = S.symbols("a beta B", nonzero=True)
        c, r, s, q, level = S.symbols("c r s q level")
        sigma = a * x**2 + c
        poly = r * P**2 + s * P + q
        y = poly.subs(P, sigma) + beta * x
        relation = (U - poly)**2 - beta**2 * (P - c) / a
        self.assert_zero(relation.subs({U: y, P: sigma}, simultaneous=True))
        self.assert_zero(S.Poly(relation, U).LC() - 1)
        self.assert_zero(S.discriminant(relation, U) - 4 * beta**2 * (P - c) / a)
        # A nonconstant odd multiplier does not generate the line in this fixture.
        bad_sigma, bad_y = x**2, x**4 + x**3
        self.assert_zero(S.diff(bad_sigma, x).subs(x, 0))
        self.assert_zero(S.diff(bad_y, x).subs(x, 0))
        self.assertEqual(S.diff(x**4 + x, x).subs(x, 0), 1)

        C2, C1, z0, pt, ptt, z2, D3, D4, D1 = S.symbols("C2 C1 z0 pt ptt z2 D3 D4 D1")
        C0, D2 = -n * pt + z0, -n * ptt / 2 + z2
        disc = (C2 * P**2 + C1 * P + C0)**2 - 4 * B * (D4 * P**4 + D3 * P**3 + D2 * P**2 + D1 * P - level)
        self.assert_zero(S.expand(disc).coeff(P, 4) - C2**2 + 4 * B * D4)
        self.assert_zero(S.expand(disc).coeff(P, 3) - 2 * C2 * C1 + 4 * B * D3)
        self.assert_zero(S.expand(disc).coeff(P, 2).coeff(n, 1) + 2 * C2 * pt - 2 * B * ptt)
        Bt = S.symbols("Bt")
        derivative_reciprocal = (Bt * pt - B * ptt) / pt**2
        self.assert_zero(derivative_reciprocal.subs(ptt, (Bt + pt) * pt / B) + 1)
        # The zero-p' alternative satisfies the undivided gate and must remain.
        gate = B * ptt - (Bt + pt) * pt
        self.assert_zero(gate.subs({pt: 0, ptt: 0}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
