"""Standalone finite polynomial controls for the held proof298.

This source reconstructs literal determinant coefficients, differential
syzygies, the intercept simplification/inverse, and the two quadratic
discriminants. It does not test exact-field constant theorems, whole-line
or strong field return, irreducibility after transcendental extension,
local nilpotence, actual coordinate recognition, or retained theorem156.

No retained proof, solver, or checker is imported. Authoring is source-only;
the parent controls any first execution after complete saved-source review.
"""

import unittest

import sympy as S


def expanded_coefficient(expression, variable, degree):
    return S.expand(expression).coeff(variable, degree)


class OneVariablePotentialControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.factor(expression), 0)

    def test_literal_linear_coefficient_and_parameter_calibration(self):
        t, s, v, X = S.symbols("t s v X")
        y = S.Function("y")(t, s, v)
        sigma = S.Function("sigma")(t, s, v)
        theta = S.Function("theta")(t, s, v)
        ell = S.Function("ell")(t)
        A = S.diff(ell, t)

        # All three full-X rows are rebuilt from the actual k=s,n=0 map.
        Y = y + sigma * X + t * X**2
        Z = (2 * t * y + sigma**2 + theta
             + (2 * t * sigma + s) * X + t**2 * X**2)
        W = ell - 2 * sigma * y + theta * X + s * X**2
        determinant = S.det(S.Matrix([
            [S.diff(f, coordinate) for coordinate in (t, s, v)]
            for f in (Y, Z, W)
        ]))
        h = y**2 - A * sigma
        linear = expanded_coefficient(determinant, X, 1)
        level_derivative = (
            -A * S.diff(y, v)
            - (S.diff(A, t) * sigma + S.diff(h, t)) * S.diff(sigma, v)
            - S.diff(h, s) * S.diff(theta, v)
        )
        # Keep the prior-level residual explicit instead of silently setting it0.
        residual_multiplier = S.diff(sigma, t) + S.diff(theta, s)
        self.assert_zero(
            linear - level_derivative - residual_multiplier * S.diff(h, v)
        )
        missing_h_t = level_derivative + S.diff(h, t) * S.diff(sigma, v)
        self.assertNotEqual(S.factor(missing_h_t - level_derivative), 0)

        Ht, Hr, vt, vr, yv = S.symbols("Ht Hr vt vr yv", nonzero=True)
        inverse_parameter_matrix = S.Matrix([
            [1, 0, 0], [Ht, Hr, 0], [vt, vr, 1 / yv]
        ])
        self.assert_zero(inverse_parameter_matrix.det() - Hr / yv)
        self.assertNotEqual(S.factor(inverse_parameter_matrix.det() - Hr * yv), 0)
        # This finite chain-rule control does not assert that Hr/yv is an
        # original-ring unit; proof298 only uses it in the exact field L.

    def test_raw_scalar_and_every_post_integration_coefficient(self):
        t, rho, U = S.symbols("t rho U")
        A = S.Function("A")(t)
        ell = S.Function("ell")(t)
        H = S.Function("H")(t, rho)
        T = S.Function("T")(t, rho)
        P = (U**2 - rho) / A
        theta = (S.diff(H, t) * P
                 - S.diff(H, rho) * (A * U + S.diff(A, t) * P**2 / 2)
                 - T)
        z = 2 * t * U + P**2 + theta
        w = ell - 2 * U * P

        def raw_scalar(z_expression):
            matrix = S.Matrix([
                [S.diff(f, coordinate) for coordinate in (t, rho, U)]
                for f in (U, z_expression, w)
            ])
            return S.expand(matrix.det()).subs(S.diff(ell, t), A)

        J = raw_scalar(z)
        leading = S.diff(A, t)**2 * S.diff(H, rho, 2) / A**4
        self.assert_zero(expanded_coefficient(J, U, 7) - leading)
        # Dropping the moving curvature contribution destroys the high gate.
        wrong_z = z + S.diff(A, t) * S.diff(H, rho) * P**2 / 2
        wrong_leading = expanded_coefficient(raw_scalar(wrong_z), U, 7)
        self.assertNotEqual(S.factor(wrong_leading - leading), 0)

        b = S.Function("b")(t)
        c = S.Function("c")(t)
        integrated_H = b * rho + c
        J_after = S.expand(J.subs(H, integrated_H).doit())
        V0 = b * S.diff(A, t, 2) + 3 * S.diff(A, t) * S.diff(b, t)
        D0 = S.diff(integrated_H, t, 2) + S.diff(A, t) * S.diff(T, rho)
        slope_gate = S.diff(A * b, t) - 2
        expected = {
            7: 0,
            6: 0,
            5: -V0 / A**3,
            4: 0,
            3: 2 * (rho * V0 + A * D0) / A**3,
            2: -3 * slope_gate / A,
            1: -(rho**2 * V0 + 2 * rho * A * D0
                 + 2 * A**2 * S.diff(T, t)) / A**3,
            0: rho * slope_gate / A + A * S.diff(T, rho)
               + S.diff(integrated_H, t),
        }
        self.assertLessEqual(S.degree(J_after, U), 7)
        for degree, target in expected.items():
            with self.subTest(degree=degree):
                self.assert_zero(expanded_coefficient(J_after, U, degree) - target)

    def test_exact_gate_syzygies_and_both_algebraic_integration_modes(self):
        t, rho = S.symbols("t rho")
        A = S.Function("A")(t)
        b = S.Function("b")(t)
        c = S.Function("c")(t)
        alpha, beta, gamma, delta, epsilon = S.symbols(
            "alpha beta gamma delta epsilon"
        )
        V0 = b * S.diff(A, t, 2) + 3 * S.diff(A, t) * S.diff(b, t)
        self.assert_zero(
            V0 - S.diff(A * b, t, 2)
            - S.diff(A, t) * (S.diff(b, t) + alpha * A)
            + A * (S.diff(b, t, 2) + alpha * S.diff(A, t))
        )
        integrated_T = alpha * rho**2 / 2 + beta * rho + gamma
        scalar_constant = A * S.diff(integrated_T, rho) + S.diff(b * rho + c, t)
        self.assert_zero(
            scalar_constant - (S.diff(b, t) + alpha * A) * rho
            - (S.diff(c, t) + beta * A)
        )
        # The identities above support the proof's deductions. They do not
        # establish that a derivative's kernel is the complex constant field.

        b0 = S.symbols("b0", nonzero=True)
        ell0, c0 = S.symbols("ell0 c0")
        A_affine = (2 * t + epsilon) / b0
        ell_quadratic = (t + epsilon / 2)**2 / b0 + ell0
        c_affine_mode = -beta * ell_quadratic + delta * t + c0
        self.assert_zero(S.diff(ell_quadratic, t) - A_affine)
        self.assert_zero(S.diff(A_affine * b0, t) - 2)
        self.assert_zero(S.diff(c_affine_mode, t) + beta * A_affine - delta)

        # The second mode is checked in a literal quadratic quotient field,
        # not by selecting a numerical square-root branch.
        b_symbol, alpha_nonzero, D = S.symbols("b alpha_nonzero D", nonzero=True)
        relation = b_symbol**2 + 2 * alpha_nonzero * (t + epsilon / 2)**2 - D
        b_t = -alpha_nonzero * (2 * t + epsilon) / b_symbol

        def exact_t(expression):
            return S.diff(expression, t) + b_t * S.diff(expression, b_symbol)

        def zero_mod_relation(expression):
            numerator = S.together(expression).as_numer_denom()[0]
            remainder = S.rem(S.expand(numerator), relation, b_symbol)
            self.assert_zero(remainder)

        radical_A = (2 * t + epsilon) / b_symbol
        radical_ell = ell0 - b_symbol / alpha_nonzero
        radical_c = -beta * radical_ell + delta * t + c0
        zero_mod_relation(exact_t(relation))
        zero_mod_relation(exact_t(radical_ell) - radical_A)
        zero_mod_relation(b_t + alpha_nonzero * radical_A)
        zero_mod_relation(exact_t(radical_c) + beta * radical_A - delta)
        zero_mod_relation(exact_t(radical_A * b_symbol) - 2)
        zero_mod_relation(
            b_symbol * exact_t(exact_t(radical_A))
            + 3 * exact_t(radical_A) * b_t
        )
        zero_mod_relation(exact_t(radical_A) - 2 * D / b_symbol**3)

    def test_literal_intercept_inverse_discriminants_and_actual_shear(self):
        U, rho, A, b = S.symbols("U rho A b", nonzero=True)
        alpha, beta, gamma, delta, epsilon, ell = S.symbols(
            "alpha beta gamma delta epsilon ell", nonzero=True
        )
        P = (U**2 - rho) / A
        # These substitutions are the exact stated gates, not a target z array.
        A_t = (2 + alpha * A**2) / b
        b_t = -alpha * A
        c_t = delta - beta * A
        t = (A * b - epsilon) / 2
        T = alpha * rho**2 / 2 + beta * rho + gamma
        raw_z = ((1 - A_t * b / 2) * P**2
                 + (b_t * rho + c_t) * P + (2 * t - A * b) * U - T)
        target_z = delta * P - alpha * U**4 / 2 - beta * U**2 - epsilon * U - gamma
        self.assert_zero(raw_z - target_z)

        p0, z0, w0 = S.symbols("p0 z0 w0")
        forward_z = delta * p0 - alpha * U**4 / 2 - beta * U**2 - epsilon * U - gamma
        forward_w = ell - 2 * U * p0
        inverse_p = (z0 + alpha * U**4 / 2 + beta * U**2 + epsilon * U + gamma) / delta
        inverse_ell = w0 + 2 * U * inverse_p
        self.assert_zero(inverse_p.subs(z0, forward_z) - p0)
        self.assert_zero(inverse_ell.subs({z0: forward_z, w0: forward_w}) - ell)
        self.assert_zero(forward_z.subs(p0, inverse_p) - z0)
        self.assert_zero(forward_w.subs({p0: inverse_p, ell: inverse_ell}, simultaneous=True) - w0)
        self.assertNotEqual(S.factor(inverse_p.subs(gamma, 0).subs(z0, forward_z) - p0), 0)

        T0, L0, ell0, D, b0 = S.symbols("T0 L0 ell0 D b0")
        quadratic_one = (T0 + epsilon / 2)**2 - b0 * (L0 - ell0)
        quadratic_two = (2 * alpha * (T0 + epsilon / 2)**2
                         - D + alpha**2 * (L0 - ell0)**2)
        self.assert_zero(S.discriminant(quadratic_one, T0) - 4 * b0 * (L0 - ell0))
        self.assert_zero(
            S.discriminant(quadratic_two, T0)
            - 8 * alpha * (D - alpha**2 * (L0 - ell0)**2)
        )
        root_polynomial = D - alpha**2 * (L0 - ell0)**2
        self.assert_zero(S.discriminant(root_polynomial, L0) - 4 * alpha**2 * D)
        self.assertEqual(S.discriminant(root_polynomial.subs(D, 0), L0), 0)
        # Discriminants only check the algebraic formulas and D=0 boundary.
        # Field irreducibility and independence of y,P,ell remain written proofs.

        X, Y, Z, W, tau, S0 = S.symbols("X Y Z W tau S0")
        shear = W - X * Z
        inverse_W = S0 + X * Z
        self.assert_zero(shear.subs(W, inverse_W) - S0)
        self.assert_zero(inverse_W.subs(S0, shear) - W)
        self.assert_zero(tau * S.diff(shear, Z) + X * tau * S.diff(shear, W))
        # This controls the explicit actual shear only, not the LND theorem.


if __name__ == "__main__":
    unittest.main()
