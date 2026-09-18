"""Standalone exact algebra controls for the conditional restriction277.

The suite reconstructs formal gradients and homogeneous parts, evaluates
a moving parabola only after differentiation, and checks the lower line
gates and actual scalar contradiction. It does not prove field constants,
pure-top multiplicities, actual chart entry, or the retained theorem275.
No other checker is imported. Root owns the sole canonical execution.
"""

import unittest

import sympy as S


class AffineParameterControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    @staticmethod
    def formal_data(constant_a=False, zero_k=False, specialized_T=False):
        t, n, U, P = S.symbols("t n U P")
        a = S.symbols("a", nonzero=True) if constant_a else S.Function("a")(t)
        b, c = (S.Function(name)(t) for name in ("b", "c"))
        k = S.Integer(0) if zero_k else S.Function("k")(t)
        slope, p, q = (S.Function(name)(t) for name in ("slope", "p", "q"))
        T = -a * slope * n**2 + p * n + q if specialized_T else S.Function("T")(t, n)
        omega = S.Function("omega")(t, n)
        H = a * n**2 / 2 + b * n + c
        gamma = 2 * P + S.diff(k, t)
        B1 = 2 * U + S.diff(k, t, 2) * P
        A = gamma * U + S.diff(k, t, 2) * P**2 / 2
        C = U**2 + S.diff(k, t, 2) * P * U + S.diff(k, t, 3) * P**3 / 6
        W = (
            omega + S.diff(H, n, 2) * A**2 / 2
            - (S.diff(H, n, t) * P + S.diff(T, n)) * A
            - S.diff(H, n) * C + S.diff(H, t) * U
            + S.diff(H, t, 2) * P**2 / 2 + S.diff(T, t) * P
        )
        QU = S.expand(gamma * S.diff(W, n) - S.diff(W, P))
        QP = S.expand(B1 * S.diff(W, n) - S.diff(W, t))
        return t, n, U, P, a, b, c, k, T, omega, QU, QP, slope, p, q

    @staticmethod
    def homogeneous(expression, U, P, degree):
        return sum(
            coefficient * U**i * P**j
            for (i, j), coefficient in S.Poly(S.expand(expression), U, P).terms()
            if i + j == degree
        )

    def test_full_gradients_and_top_homogeneous_parts(self):
        t, n, U, P, a, b, c, k, T, omega, QU, QP, slope, p, q = self.formal_data()
        self.assert_zero(S.diff(QU, P) - S.diff(QP, U))
        self.assert_zero(self.homogeneous(QU, U, P, 5))
        self.assert_zero(self.homogeneous(QP, U, P, 5))
        Q5 = -P**3 * (S.diff(k, t, 2) * P + 4 * U) * (
            2 * a * S.diff(k, t, 3) * P
            + 3 * S.diff(a, t) * (S.diff(k, t, 2) * P + 4 * U)
        ) / 24
        self.assert_zero(self.homogeneous(QU, U, P, 4) - S.diff(Q5, U))
        self.assert_zero(self.homogeneous(QP, U, P, 4) - S.diff(Q5, P))

        t, n, U, P, a, b, c, k, T, omega, QU, QP, slope, p, q = self.formal_data(True, True)
        Q4 = U * P * (S.diff(b, t, 2) * P**2 - 2 * S.diff(T, n, 2) * U * P - 2 * a * U**2)
        self.assert_zero(self.homogeneous(QU, U, P, 3) - S.diff(Q4, U))
        self.assert_zero(self.homogeneous(QP, U, P, 3) - S.diff(Q4, P))
        self.assert_zero(self.homogeneous(QU, U, P, 4))
        self.assert_zero(self.homogeneous(QP, U, P, 4))
        self.assert_zero(S.Poly(Q4, U, P).coeff_monomial(U**3 * P) + 2 * a)

    def test_parabola_and_leading_line_coefficients(self):
        t, n, U, P, a, b, c, k, T, omega, QU, QP, slope, p, q = self.formal_data(True)
        r, s, intercept = S.symbols("r s intercept")
        on_parabola = QU.subs(U, r * P**2 + s * P + intercept)
        self.assert_zero(S.Poly(on_parabola, P).nth(5) + 6 * a * r**2)
        self.assertEqual(S.Poly(on_parabola, P).degree(), 5)
        self.assertNotEqual((-6 * a * r**2).subs({a: 1, r: 1}), 0)

        t, n, U, P, a, b, c, k, T, omega, QU, QP, slope, p, q = self.formal_data(True, True)
        first = S.Poly(QU.subs(U, s * P + intercept), P).nth(3)
        second = S.Poly(QP.subs(U, s * P + intercept), P).nth(3)
        expected_first = S.diff(b, t, 2) - 4 * S.diff(T, n, 2) * s - 6 * a * s**2
        expected_second = -2 * a * s**3 - 4 * S.diff(T, n, 2) * s**2 + 3 * S.diff(b, t, 2) * s
        self.assert_zero(first - expected_first)
        self.assert_zero(second - expected_second)
        solution = {S.diff(T, n, 2): -2 * a * s, S.diff(b, t, 2): -2 * a * s**2}
        self.assert_zero(first.subs(solution))
        self.assert_zero(second.subs(solution))
        self.assert_zero(second - 3 * s * first - 8 * s**2 * (S.diff(T, n, 2) + 2 * a * s))

    def test_lower_line_gates_with_all_coefficient_derivatives(self):
        t, n, U, P, a, b, c, k, T, omega, QU, QP, s, p, q = self.formal_data(True, True, True)
        C = S.Function("C")(t, n)
        restrictions = {
            S.diff(b, t, 3): -4 * a * s * S.diff(s, t),
            S.diff(b, t, 2): -2 * a * s**2,
        }
        first = S.Poly(S.expand(QU.subs(U, s * P + C).subs(restrictions)), P)
        second = S.Poly(S.expand(QP.subs(U, s * P + C).subs(restrictions)), P)
        expected_first = -2 * (2 * a * n * S.diff(s, t) + 2 * a * C * s - 3 * s * S.diff(b, t) - S.diff(p, t))
        expected_second = -(
            12 * a * n * s * S.diff(s, t) - 8 * a * C * s**2
            - 6 * s**2 * S.diff(b, t) - 8 * s * S.diff(p, t) + S.diff(c, t, 3)
        ) / 2
        self.assert_zero(first.nth(2) - expected_first)
        self.assert_zero(second.nth(2) - expected_second)
        solved_C = -n * S.diff(s, t) / s + 3 * S.diff(b, t) / (2 * a) + S.diff(p, t) / (2 * a * s)
        self.assert_zero(first.nth(2).subs(C, solved_C))
        gate = -2 * second.nth(2).subs(C, solved_C)
        expected_gate = 20 * a * n * s * S.diff(s, t) - 18 * s**2 * S.diff(b, t) - 12 * s * S.diff(p, t) + S.diff(c, t, 3)
        self.assert_zero(gate - expected_gate)
        self.assert_zero(S.diff(gate, n) - 20 * a * s * S.diff(s, t))
        self.assertNotEqual(S.diff(gate, n).subs({a: 1, s: 1, S.diff(s, t): 1}, simultaneous=True), 0)

        constants = {S.diff(s, t, 2): 0, S.diff(s, t): 0}
        omega_n = a * n * s**2 + 3 * a * C**2 - 3 * C * S.diff(b, t) - p * s + S.diff(c, t, 2) / 2
        self.assert_zero(first.nth(1).subs(constants) - 2 * (S.diff(omega, n) - omega_n))
        raw_last = second.nth(1).subs(constants).subs(S.diff(omega, n), omega_n)
        last = n * (4 * a * s**3 - S.diff(p, t, 2)) + 8 * a * C**2 * s + 4 * C * S.diff(p, t) - 2 * p * s**2 - S.diff(q, t, 2)
        self.assert_zero(raw_last - last)
        Ct = S.symbols("Ct")
        ptt = 2 * a * s * Ct + 6 * a * s**3
        self.assert_zero((4 * a * s**3 - ptt).subs(Ct, -s**2))

    def test_full_moving_line_scalar_and_degenerate_control(self):
        sigma, st, sn, sv = S.symbols("sigma st sn sv")
        s, slope_t, C, Ct, Cn = S.symbols("s slope_t C Ct Cn")
        y = s * sigma + C
        yt, yn, yv = slope_t * sigma + s * st + Ct, s * sn + Cn, s * sv
        DU = (2 * y * yn - yt) * sv + (st - 2 * y * sn) * yv
        DP = (1 + 2 * sigma * sn) * yv - 2 * sigma * yn * sv
        full = ((4 * s * Cn - slope_t) * sigma + 2 * C * Cn - Ct - s**2) * sv
        self.assert_zero(DU - s * DP - full)
        self.assert_zero(full.subs({Cn: 0, slope_t: 0, Ct: -s**2}))
        # If the moving derivatives are silently discarded this term is lost.
        wrongly_fixed_C = full.subs(Cn, 0)
        self.assert_zero(full - wrongly_fixed_C - Cn * (4 * s * sigma + 2 * C) * sv)
        self.assertEqual((full - wrongly_fixed_C).subs({Cn: 1, s: 1, sigma: 1, C: 0, sv: 1}), 4)
        # Vanishing calibration is essential to the final contradiction.
        self.assert_zero(full.subs({s: 1, slope_t: 0, Cn: 0, Ct: -1}))
        self.assertEqual(full.subs({s: 1, slope_t: 0, Cn: 0, Ct: 0, sv: 1}), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
