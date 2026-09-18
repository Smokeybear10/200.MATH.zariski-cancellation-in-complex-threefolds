#!/usr/bin/env python3
"""Standalone finite algebra controls for the restricted recognition note276.

The tests reconstruct scalar and polynomial identities from raw maps. They do
not establish actual chart entry, exact constant-field integration, Gauss's
lemma, strong field return, or the published recognition theorem. Formal jets
and negative fixtures are not claimed to be actual globally sliced frames.
No retained proof, solver, or checker is imported. Root owns any execution.
"""

import unittest

import sympy as S


class QuadraticFirstActualCoordinateControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def assert_x_coefficients_zero(self, expression, X, bound):
        polynomial = S.Poly(S.expand(expression), X)
        self.assertLessEqual(polynomial.degree(), bound)
        for j in range(bound + 1):
            self.assert_zero(polynomial.nth(j))

    def test_raw_scalar_and_primitive_relation_degree(self):
        U, V, x, Z, W = S.symbols("U V x Z W")
        h, B = S.symbols("h B", nonzero=True)
        ht, At, Bt, Ct, Tt = S.symbols("ht At Bt Ct Tt")
        q20, q11, q02, q10, q01, q00 = S.symbols("q20 q11 q02 q10 q01 q00")
        g3, g2, g1, g0 = S.symbols("g3 g2 g1 g0")
        Q = q20 * U**2 + q11 * U * V + q02 * V**2 + q10 * U + q01 * V + q00
        Pi = S.integrate(Q, V) + g3 * U**3 + g2 * U**2 + g1 * U + g0
        self.assert_zero(S.diff(Pi, V) - Q)

        # Fixed-U differentiation of eta=h*x and eta²=A*U+B*V+C.
        Vt = (2 * h * ht * x**2 - At * U - Bt * V - Ct) / B
        Vx = 2 * h**2 * x / B
        z = h * x + Q
        zt, zx = ht * x + S.diff(Q, V) * Vt, h + S.diff(Q, V) * Vx
        # These are the derivatives of Pi(U,V)-V*z+T, without a target row.
        wt = S.diff(Pi, V) * Vt - Vt * z - V * zt + Tt
        wx = S.diff(Pi, V) * Vx - Vx * z - V * zx
        raw_scalar = zt * wx - zx * wt
        target = -Tt * h - h**2 * x * (At * U + Bt * V + Ct + 2 * Tt * S.diff(Q, V)) / B
        self.assert_zero(raw_scalar - target)
        self.assert_zero(target.subs({At: -2 * q11 * Tt, Bt: -4 * q02 * Tt, Ct: -2 * q01 * Tt}) + Tt * h)

        # Literal coefficient-field Jacobian and the orientation of its first row.
        t, lam = S.symbols("t lam")
        N = S.symbols("N", nonzero=True)
        d, alpha, beta = (S.Function(name)(t) for name in ("d", "alpha", "beta"))
        y = (x**2 - alpha * lam - beta) / d
        parameter_jacobian = S.Matrix([t, y, x]).jacobian([t, lam, x]).det()
        self.assert_zero(parameter_jacobian + alpha / d)
        self.assert_zero((-alpha / (2 * N**2)) / parameter_jacobian - d / (2 * N**2))

        A0, B0, C0 = S.symbols("A0 B0 C0")
        relation = (Z - Q)**2 + 2 * (W + V * Z - Pi) * S.diff(Q, V) - A0 * U - B0 * V - C0
        self.assert_zero(S.expand(relation).coeff(V, 4) + q02**2 / 3)
        self.assert_zero(S.expand(relation).coeff(W, 1) - 2 * S.diff(Q, V))
        self.assert_zero(S.expand(relation.subs(W, 0)).coeff(Z, 2) - 1)
        # This coefficient is the written primitive-gcd certificate, not an
        # automated proof of the universal field irreducibility argument.
        linear_case = S.expand(relation.subs(q02, 0))
        Q0 = q20 * U**2 + q10 * U + q00
        L = q11 * U + q01
        g = g3 * U**3 + g2 * U**2 + g1 * U + g0
        expected = (Z - Q0)**2 + 2 * L * (W - g) - A0 * U - B0 * V - C0
        self.assert_zero(linear_case - expected)
        self.assert_zero(S.expand(linear_case).coeff(V, 1) + B0)

    def test_full_coefficient_ledger_and_complex_correction_gates(self):
        t, lam, U = S.symbols("t lam U")
        e, j, b, k0, n0, q, r = (
            S.Function(name)(t) for name in ("e", "j", "b", "k0", "n0", "q", "r")
        )
        l1, l0, l2, q2, q1, q0 = S.symbols("l1 l0 l2 q2 q1 q0")
        c1, c0, c2 = S.symbols("c1 c0 c2")
        m, N, n1 = 1 / e, 1 / (j * e**3), b / e**2
        k, n = m * lam + k0, N * lam**2 / 2 + n1 * lam + n0
        nu = S.diff(n, lam)
        b1 = S.diff(nu, t) - 2 * nu * S.diff(m, t) / m
        M = S.diff(m, t, 2) / 2 - S.diff(m, t)**2 / m
        h = m / N
        coefficient_u = S.diff(k, t) - h * b1
        coefficient_u2 = S.diff(q, t, 2) / 2 - h * M
        self.assert_zero(S.diff(coefficient_u, lam) - S.diff(j, t) / (j * e))
        self.assert_zero(coefficient_u.subs(lam, 0) - S.diff(k0, t) + j * S.diff(b, t))
        self.assert_zero(coefficient_u2 - (S.diff(q, t, 2) + j * S.diff(e, t, 2)) / 2)

        # Impose precisely the already integrated Q-coefficient identities;
        # e,b,n0,r remain arbitrary coefficient functions.
        jj = l1 * t + l2
        qq = q2 * t**2 + c1 * t + c0 - jj * e
        kk = jj * b - l0 * e + q1 * t + c2
        NN, mm = 1 / (jj * e**3), 1 / e
        raw_k = mm * lam + kk
        raw_n = NN * lam**2 / 2 + (b / e**2) * lam + n0
        raw_nu = S.diff(raw_n, lam)
        f = (S.diff(qq, t, 2) - S.diff(r, t, 2) * mm) * U**2 / 2 + S.diff(raw_k, t) * U + raw_n
        potential = (
            (S.diff(qq, t, 3) - mm * S.diff(r, t, 3) - 3 * S.diff(r, t, 2) * S.diff(mm, t)) * U**3 / 6
            + (S.diff(raw_k, t, 2) - S.diff(r, t, 2) * raw_nu) * U**2 / 2
            + S.diff(raw_n, t) * U
        )
        ell = S.Function("ell")(t, lam)
        A = S.diff(e, t) * U - raw_nu * e**2
        raw_B = e * ell - A * f - e * potential
        zeta_zero_lam = b - S.diff(e, t) * U
        g3, g2, g1, g0 = S.symbols("g3 g2 g1 g0")
        Q0 = q2 * U**2 + q1 * U + q0
        L = l1 * U + l0
        g = g3 * U**3 + g2 * U**2 + g1 * U + g0
        target_B = Q0 * zeta_zero_lam + L * zeta_zero_lam**2 / 2 + g
        coefficient_difference = S.expand(raw_B.subs(lam, 0) - target_B)
        R = r + jj * e**2 / 2
        Lambda = l0 * e**2 / 2 - jj * e * b
        C = e * (q0 - n0) + jj * b**2 / 2
        for power, expected in (
            (3, S.diff(R, t, 3) / 6 - g3),
            (2, S.diff(Lambda, t, 2) / 2 - g2),
            (1, S.diff(C, t) - g1),
        ):
            self.assert_zero(coefficient_difference.coeff(U, power) - expected)

        # The c3 integration uses both retained speed factors, not a unit-speed
        # assumption: h²d=2*j*T' when T'=e*d/(2*N).
        d = S.symbols("d")
        self.assert_zero((mm / NN)**2 * d - 2 * jj * e * d / (2 * NN))
        T = S.Function("T")(t)
        A0, B0 = S.symbols("A0 B0")
        derivative = S.diff(2 * jj * T + B0 * e - A0 * t, t)
        self.assert_zero(derivative - (2 * l1 * T + 2 * jj * S.diff(T, t) + B0 * S.diff(e, t) - A0))

    def test_full_literal_actual_map_transports_and_missing_constants(self):
        t, X, y, eta, zeta, T, lam = S.symbols("t X y eta zeta T lam")
        e = S.Function("e")(t)
        l1, l0, l2, q2, q1, q0, c1, c0, c2 = S.symbols("l1 l0 l2 q2 q1 q0 c1 c0 c2")
        g3, g2, g1, g0, r2, r1, r0, s1, s0, kappa = S.symbols("g3 g2 g1 g0 r2 r1 r0 s1 s0 kappa")
        j = l1 * t + l2
        Lambda = g2 * t**2 + s1 * t + s0
        b = (l0 * e**2 / 2 - Lambda) / (j * e)
        N, m, n1 = 1 / (j * e**3), 1 / e, b / e**2
        k0 = j * b - l0 * e + q1 * t + c2
        n0 = q0 + (j * b**2 / 2 - (g1 * t + kappa)) / e
        q = q2 * t**2 + c1 * t + c0 - j * e
        r = g3 * t**3 + r2 * t**2 + r1 * t + r0 - j * e**2 / 2
        k, n = m * lam + k0, N * lam**2 / 2 + n1 * lam + n0
        f = (S.diff(q, t, 2) - S.diff(r, t, 2) * m) * y**2 / 2 + S.diff(k, t) * y + n
        transported_lam = j * e * (zeta - b + S.diff(e, t) * y)
        # Form all derivatives before the field-parameter substitution.
        f = f.subs(lam, transported_lam)
        k = k.subs(lam, transported_lam)
        Q0 = lambda value: q2 * value**2 + q1 * value + q0
        g = lambda value: g3 * value**3 + g2 * value**2 + g1 * value + g0
        L = l1 * y + l0
        z = eta + Q0(y) + L * zeta
        w = T - zeta * eta - L * zeta**2 / 2 + g(y)
        Y = y + t * X
        Z = z + (S.diff(q, t) * y + k) * X + q * X**2
        W = w + e * (z - f) * X + (S.diff(r, t) * y + transported_lam) * X**2 + r * X**3
        LL, parameter = l1 * Y + l0 + l2 * X, zeta - e * X
        V = Z - Q0(Y) - c1 * X * Y - c2 * X - c0 * X**2
        Wbar = W - g(Y) - r2 * X * Y**2 - r1 * X**2 * Y - r0 * X**3
        Wbar -= s1 * X * Y + s0 * X**2 + kappa * X
        self.assert_x_coefficients_zero(V - eta - LL * parameter, X, 3)
        self.assert_x_coefficients_zero(Wbar - T + parameter * eta + LL * parameter**2 / 2, X, 3)

        # Removing only one complex integration constant spoils the literal map.
        self.assert_x_coefficients_zero((V + c2 * X) - eta - LL * parameter - c2 * X, X, 3)
        self.assertEqual(S.diff(c2 * X, X), c2)
        self.assert_x_coefficients_zero((Wbar + kappa * X) - T + parameter * eta + LL * parameter**2 / 2 - kappa * X, X, 3)
        self.assertNotEqual(kappa * X, 0)

    def test_quadratic_form_both_inverse_orders_and_actual_field_evaluation(self):
        V, Wbar, I, J, LL, linear = S.symbols("V Wbar I J LL linear")
        B0 = S.symbols("B0", nonzero=True)

        def forward(v, w):
            parameter = (v**2 + 2 * LL * w - linear) / B0
            return v - LL * parameter, w + parameter * v - LL * parameter**2 / 2

        def backward(i, j):
            parameter = (i**2 + 2 * LL * j - linear) / B0
            return i + LL * parameter, j - parameter * i - LL * parameter**2 / 2

        fi, fj = forward(V, Wbar)
        self.assert_zero(fi**2 + 2 * LL * fj - V**2 - 2 * LL * Wbar)
        bv, bw = backward(fi, fj)
        self.assert_zero(bv - V)
        self.assert_zero(bw - Wbar)
        bv, bw = backward(I, J)
        ri, rj = forward(bv, bw)
        self.assert_zero(ri - I)
        self.assert_zero(rj - J)
        # No division by LL occurs, including its zero specialization.
        for actual, expected in zip(forward(V, Wbar), (V, Wbar + V * (V**2 - linear) / B0)):
            self.assert_zero(actual.subs(LL, 0) - expected)

        X, y, t, eta, zeta, T, e = S.symbols("X y t eta zeta T e")
        l1, l0, l2, A0, C0, c3 = S.symbols("l1 l0 l2 A0 C0 c3")
        Y, jj = y + t * X, l1 * t + l2
        LL_actual = l1 * Y + l0 + l2 * X
        parameter = zeta - e * X
        actual_v = eta + LL_actual * parameter
        actual_w = T - parameter * eta - LL_actual * parameter**2 / 2
        numerator = actual_v**2 + 2 * LL_actual * actual_w - A0 * Y - c3 * X - C0
        square_residual = eta**2 - (A0 - 2 * l1 * T) * y - B0 * zeta - C0 + 2 * l0 * T
        curve_residual = 2 * jj * T + B0 * e - A0 * t - c3
        self.assert_zero(numerator - B0 * parameter - square_residual - X * curve_residual)
        evaluated_parameter = S.expand(numerator).subs(
            {eta**2: (A0 - 2 * l1 * T) * y + B0 * zeta + C0 - 2 * l0 * T,
             c3: 2 * jj * T + B0 * e - A0 * t}, simultaneous=True
        ) / B0
        self.assert_zero(evaluated_parameter - parameter)
        evaluated_i = actual_v - LL_actual * evaluated_parameter
        evaluated_j = actual_w + evaluated_parameter * actual_v - LL_actual * evaluated_parameter**2 / 2
        self.assert_zero(evaluated_i - eta)
        self.assert_zero(evaluated_j - T)

        # The intercept parameter alone is not the actual polynomial parameter.
        false_i = actual_v - LL_actual * zeta
        self.assert_zero(false_i - eta + LL_actual * e * X)
        self.assertEqual(S.diff(false_i, X).subs({l1: 0, l0: 1, l2: 0, e: 1}), -1)
        # Omitting the c3*X term likewise leaves a nonzero symbolic defect.
        self.assert_zero((numerator + c3 * X) / B0 - numerator / B0 - c3 * X / B0)


if __name__ == "__main__":
    unittest.main()
