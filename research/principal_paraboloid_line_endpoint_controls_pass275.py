"""Finite exact controls for the actual normalization272 and line endpoint275.

The tests reconstruct literal coordinate substitutions, formal gradients,
moving-evaluation and exterior coefficients, and the final actual shear.
They do not prove chart entry, field constants, cofactor-unit theorems,
local nilpotence, or the retained recognition theorem257. Formal field
parameters are never asserted to be ambient coordinates by these tests.
No retained checker or solver is imported.
"""

import unittest

import sympy as sp


class PrincipalParaboloidLineEndpointControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_actual_affine_normalization_with_generic_first_intercept(self):
        X, Y, Z, W, Xs, Ys, Zs, Ws = sp.symbols("X Y Z W Xs Ys Zs Ws")
        t, n, y, sigma, theta, w, H = sp.symbols("t n y sigma theta w H")
        kappa, alpha, beta, C = sp.symbols("kappa alpha beta C")
        c = kappa / 4
        k = kappa * t**2 / 2 + alpha * t + beta
        z = 2 * t * y + sigma**2 + sp.diff(k, t) * sigma + n
        actual = sp.Matrix([X - c, Y + alpha * (X - c) / 2, Z - beta * (X - c), W])
        inverse = sp.Matrix([Xs + c, Ys - alpha * Xs / 2, Zs + beta * Xs, Ws])
        for residual in actual.subs(dict(zip((X, Y, Z, W), inverse)), simultaneous=True) - sp.Matrix([Xs, Ys, Zs, Ws]):
            self.assert_zero(residual)
        for residual in inverse.subs(dict(zip((Xs, Ys, Zs, Ws), actual)), simultaneous=True) - sp.Matrix([X, Y, Z, W]):
            self.assert_zero(residual)
        self.assert_zero(actual.jacobian((X, Y, Z, W)).det() - 1)
        self.assertEqual(inverse.diff(Zs), sp.Matrix([0, 0, 1, 0]))

        old_rows = {
            X: Xs + c,
            Y: y + sigma * (Xs + c) + t * (Xs + c)**2,
            Z: z + (2 * t * sigma + k) * (Xs + c) + t**2 * (Xs + c)**2,
            W: w + theta * (Xs + c) + H * (Xs + c)**2,
        }
        new_rows = actual.subs(old_rows, simultaneous=True)
        # Generic y is retained here. Only the later specialization uses a line.
        ys = y + c * sigma + t * c**2
        sigmas = sigma + 2 * c * t + alpha / 2
        zs = z + c * (2 * t * sigma + k) + t**2 * c**2
        ws, thetas = w + c * theta + c**2 * H, theta + 2 * c * H
        target = sp.Matrix([
            Xs, ys + sigmas * Xs + t * Xs**2,
            zs + 2 * t * sigmas * Xs + t**2 * Xs**2,
            ws + thetas * Xs + H * Xs**2,
        ])
        for residual in new_rows - target:
            self.assert_zero(residual)
        ns = n - 3 * c**2 * t**2 - alpha * c * t + beta * c - alpha**2 / 4
        self.assert_zero(zs - 2 * t * ys - sigmas**2 - ns)
        self.assert_zero(ys.subs(y, C - c * sigma) - C - t * c**2)
        self.assert_zero(sp.diff(ns, n) - 1)
        self.assert_zero(sp.Poly(target[1], Xs).nth(2) - t)
        self.assert_zero(sp.Poly(target[2], Xs).nth(2) - t**2)
        self.assert_zero(sp.Poly(target[3], Xs).nth(2) - H)

    def test_formal_gradients_are_taken_before_line_evaluation(self):
        t, n, U, P, C = sp.symbols("t n U P C")
        H, T, omega = (sp.Function(name)(t, n) for name in ("H", "T", "omega"))
        k = sp.Function("k")(t)
        gamma = 2 * P + sp.diff(k, t)
        B = 2 * U + sp.diff(k, t, 2) * P
        AA = gamma * U + sp.diff(k, t, 2) * P**2 / 2
        CC = U**2 + sp.diff(k, t, 2) * P * U + sp.diff(k, t, 3) * P**3 / 6
        raw_w = (
            omega + sp.diff(H, n, 2) * AA**2 / 2
            - (sp.diff(H, n, t) * P + sp.diff(T, n)) * AA
            - sp.diff(H, n) * CC + sp.diff(H, t) * U
            + sp.diff(H, t, 2) * P**2 / 2 + sp.diff(T, t) * P
        )
        QU = gamma * sp.diff(raw_w, n) - sp.diff(raw_w, P)
        QP = B * sp.diff(raw_w, n) - sp.diff(raw_w, t)
        first = sp.Poly(sp.expand(QU), U).nth(2)
        second = sp.Poly(sp.expand(QP), U).nth(3)
        self.assert_zero(first - gamma**3 * sp.diff(H, n, 3) / 2 + 3 * gamma * sp.diff(H, n, 2))
        self.assert_zero(second - gamma**2 * sp.diff(H, n, 3) + 2 * sp.diff(H, n, 2))
        self.assert_zero(2 * first - gamma * second + 4 * gamma * sp.diff(H, n, 2))
        oblique = sp.Poly(sp.expand(QU.subs(U, C - sp.diff(k, t, 2) * P / 4)), P)
        self.assert_zero(oblique.nth(4) + sp.diff(H, n, 2) * sp.diff(k, t, 3) / 3)

        D = 2 * sp.diff(H, n, 2) * U**2 - 2 * sp.diff(H, n, t) * U + sp.diff(H, t, 2) / 2
        B1 = sp.diff(T, t) - 2 * U * sp.diff(T, n)
        C1 = omega - sp.diff(H, n) * U**2 + sp.diff(H, t) * U
        canonical = D * P**2 + B1 * P + C1
        q_u = 2 * P * sp.diff(canonical, n) - sp.diff(canonical, P)
        q_p = 2 * U * sp.diff(canonical, n) - sp.diff(canonical, t)
        expected_u = 2 * sp.diff(D, n) * P**3 + 2 * sp.diff(B1, n) * P**2 + 2 * (sp.diff(C1, n) - D) * P - B1
        expected_p = (2 * U * sp.diff(D, n) - sp.diff(D, t)) * P**2 + (2 * U * sp.diff(B1, n) - sp.diff(B1, t)) * P + 2 * U * sp.diff(C1, n) - sp.diff(C1, t)
        self.assert_zero(q_u - expected_u)
        self.assert_zero(q_p - expected_p)

    def test_moving_evaluation_exterior_and_scalar_compatibility(self):
        t, n, U = sp.symbols("t n U")
        H, c = sp.Function("H")(t, n), sp.Function("c")(t, n)
        D = 2 * sp.diff(H, n, 2) * U**2 - 2 * sp.diff(H, n, t) * U + sp.diff(H, t, 2) / 2
        Dn, Dt = sp.diff(D, n), sp.diff(D, t)
        moving = sp.diff(Dn.subs(U, c), t) - sp.diff(Dt.subs(U, c), n)
        expected = sp.diff(Dn, U).subs(U, c) * sp.diff(c, t) - sp.diff(Dt, U).subs(U, c) * sp.diff(c, n)
        self.assert_zero(moving - expected)
        self.assert_zero(sp.diff(Dt, U) - 2 * U * sp.diff(Dn, U) + 4 * Dn)
        third = sp.symbols("Hnnn")
        third_rules = {
            sp.diff(H, n, 3): third,
            sp.diff(H, n, 2, t): 2 * c * third,
            sp.diff(H, n, t, 2): 4 * c**2 * third,
            sp.diff(H, t, 3): 8 * c**3 * third,
        }
        self.assert_zero(Dn.subs(U, c).subs(third_rules, simultaneous=True))
        self.assert_zero(Dt.subs(U, c).subs(third_rules, simultaneous=True))
        R = sp.diff(c, t) - 2 * c * sp.diff(c, n)
        wedge = sp.diff(c, t) * third - sp.diff(c, n) * (2 * c * third)
        self.assert_zero(wedge - R * third)
        # Countercontrol: evaluating U=c(t,n) before differentiating adds terms.
        example_Dn = 2 * U**2  # H=n**3/6 gives D_n=2U**2.
        formal = sp.diff(example_Dn, t).subs(U, t)
        moving_example = sp.diff(example_Dn.subs(U, t), t)
        self.assert_zero(moving_example - formal - 4 * t)
        self.assertNotEqual(sp.expand(moving_example - formal), 0)

        cv, ct, cn, sigma, st, sn, sv, dval, wu, eta = sp.symbols("cv ct cn sigma st sn sv dval wu eta")
        wp = 2 * dval * sigma - eta
        raw_rows = sp.Matrix([
            [ct, cn, 0],
            [2 * cv + 2 * t * ct + 2 * sigma * st, 1 + 2 * t * cn + 2 * sigma * sn, 2 * sigma * sv],
            [2 * cv * dval + wu * ct + wp * st, dval + wu * cn + wp * sn, wp * sv],
        ])
        literal = raw_rows.det()
        self.assert_zero(literal + eta * (ct - 2 * cv * cn) * sv)
        self.assert_zero(literal.subs(ct, 2 * cv * cn))

        T = sp.Function("T")(t, n)
        B1 = sp.diff(T, t) - 2 * U * sp.diff(T, n)
        self.assert_zero(sp.diff(B1, n).subs(U, c) - sp.diff(T, n, t) + 2 * c * sp.diff(T, n, 2))
        second = sp.symbols("Tnn")
        t_wedge = sp.diff(c, t) * second - sp.diff(c, n) * (2 * c * second)
        self.assert_zero(t_wedge - R * second)

    def test_remaining_omega_compatibility_retains_all_constants(self):
        t, n, U = sp.symbols("t n U")
        alpha, beta, gamma, delta, epsilon, zeta = sp.symbols("alpha beta gamma delta epsilon zeta")
        c = sp.Function("c")(t, n)
        omega = sp.Function("omega")(t, n)
        H = alpha * n**2 / 2 + beta * t * n + gamma * t**2 / 2 + delta * n + epsilon * t + zeta
        D = 2 * sp.diff(H, n, 2) * U**2 - 2 * sp.diff(H, n, t) * U + sp.diff(H, t, 2) / 2
        C1 = omega - sp.diff(H, n) * U**2 + sp.diff(H, t) * U
        on = 3 * alpha * c**2 - 3 * beta * c + gamma / 2
        ot = 4 * alpha * c**3 - 3 * beta * c**2
        self.assert_zero((sp.diff(C1, n) - D).subs(U, c).subs(sp.diff(omega, n), on))
        self.assert_zero((sp.diff(C1, t) - 2 * U * D).subs(U, c).subs(sp.diff(omega, t), ot))
        R = sp.diff(c, t) - 2 * c * sp.diff(c, n)
        self.assert_zero(sp.diff(on, t) - sp.diff(ot, n) - (6 * alpha * c - 3 * beta) * R)
        p, q, rr, omega0 = sp.symbols("p q rr omega0")
        final_H = H.subs({alpha: 0, beta: 0})
        final_T, final_omega = p * t + q * n + rr, gamma * n / 2 + omega0
        self.assert_zero(sp.diff(final_H, n) - delta)
        self.assert_zero(sp.diff(final_T, t) - 2 * c * sp.diff(final_T, n) - p + 2 * q * c)
        self.assert_zero(sp.diff(final_omega, n) - gamma / 2)
        self.assert_zero(sp.diff(final_omega, t))

    def test_full_actual_shear_both_inverses_and_exact_leader(self):
        X, Y, Z, W, Ws = sp.symbols("X Y Z W Ws")
        t, n, c, sigma, a = sp.symbols("t n c sigma a")
        gamma, delta, epsilon, zeta, p, q, rr, omega0 = sp.symbols("gamma delta epsilon zeta p q rr omega0")
        z = 2 * t * c + sigma**2 + n
        w = gamma * z / 2 + (p - 2 * q * c) * sigma - delta * c**2 + epsilon * c + omega0
        theta = p * t + q * n + rr + (gamma * t + epsilon - 2 * delta * c) * sigma
        H = gamma * t**2 / 2 + delta * n + epsilon * t + zeta
        y_row = c + sigma * X + t * X**2
        z_row = z + 2 * t * sigma * X + t**2 * X**2
        w_row = w + theta * X + H * X**2
        self.assert_zero(X**2 * z_row - y_row**2 + c**2 + 2 * c * sigma * X - n * X**2)
        correction = gamma * Z / 2 + epsilon * Y + delta * (X**2 * Z - Y**2) + rr * X + zeta * X**2 + omega0
        forward, inverse = W - correction, Ws + correction
        self.assert_zero(forward.subs(W, inverse) - Ws)
        self.assert_zero(inverse.subs(Ws, forward) - W)
        self.assert_zero(sp.Matrix([X, Y, Z, forward]).jacobian((X, Y, Z, W)).det() - 1)
        literal = forward.subs({Y: y_row, Z: z_row, W: w_row}, simultaneous=True)
        target = (p - 2 * q * c) * sigma + (p * t + q * n) * X
        self.assert_zero(literal - target)
        self.assert_zero(a * sp.diff(literal, X) - a * (p * t + q * n))
        self.assert_zero(a**2 * sp.diff(literal, X, 2))
        leader = sp.Poly(p * t + q * n, t, n)
        self.assertEqual(leader.coeff_monomial(t), p)
        self.assertEqual(leader.coeff_monomial(n), q)
        self.assert_zero(leader.as_expr().subs({p: 0, q: 0}))
        self.assertNotEqual(leader.as_expr().subs({p: 1, q: 0}), 0)
        self.assertNotEqual(leader.as_expr().subs({p: 0, q: 1}), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
