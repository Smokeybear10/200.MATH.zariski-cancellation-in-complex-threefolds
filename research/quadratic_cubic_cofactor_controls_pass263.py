#!/usr/bin/env python3
"""Source-only finite algebra controls for the supplied-frame note263.

This independently rebuilds finite symbolic identities and polynomial examples.
It does not prove the universal plane-degree theorem, the unit-cofactor argument,
primitive-gcd invariance, exact constant-field integration, or recognition.
Plane examples below are not claimed to be actual globally sliced frames.
No retained proof, solver, or checker is imported.
"""

import unittest

import sympy as S


def homogeneous_part(expression, variables, degree):
    polynomial = S.Poly(S.expand(expression), *variables)
    return S.Add(
        *(
            coefficient
            * S.prod(variable**power for variable, power in zip(variables, powers))
            for powers, coefficient in polynomial.terms()
            if sum(powers) == degree
        )
    )


class QuadraticCubicCofactorControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def test_literal_wedge_and_formal_gradient_coefficients(self):
        t, lam, U, V = S.symbols("t lam U V")
        q, r = S.Function("q")(t), S.Function("r")(t)
        k, n, ell = (S.Function(name)(t, lam) for name in ("k", "n", "ell"))
        m, d = S.diff(k, lam), S.diff(r, t, 2)
        f = (S.diff(q, t, 2) - d * m) * U**2 / 2 + S.diff(k, t) * U + n
        potential = (
            d**2 * S.diff(m, lam) * U**4 / 8
            + (S.diff(q, t, 3) - S.diff(r, t, 3) * m - 3 * d * S.diff(m, t))
            * U**3 / 6
            + (S.diff(k, t, 2) - d * S.diff(n, lam)) * U**2 / 2
            + S.diff(n, t) * U
        )
        g = (
            ell - potential - S.diff(m, lam) * V**2 / 2 - S.diff(f, lam) * V
        ) / m
        middle_t = S.diff(m, t) * V + S.diff(f, t)
        middle_lam = S.diff(m, lam) * V + S.diff(f, lam)
        grad_u = (
            -m * S.diff(g, t)
            + m * d * U * S.diff(g, lam)
            + middle_lam * S.diff(g, U)
        )
        grad_v = -m * S.diff(g, lam) + middle_lam * S.diff(g, V)

        self.assert_zero(S.diff(potential, U) - S.diff(f, t) + d * U * S.diff(f, lam))
        self.assert_zero(m * S.diff(g, U) + middle_t - d * U * middle_lam)
        self.assert_zero(m * S.diff(g, V) + middle_lam)
        self.assert_zero(S.diff(grad_u, V) - S.diff(grad_v, U))

        # Literal rows before the coefficient-field shear; no expected row arrays.
        rows = S.Matrix([U, m * V + f, g]).jacobian([t, lam, U, V])
        raw = [
            rows.extract([0, 1, 2], columns).det()
            for columns in ([2, 0, 1], [2, 0, 3], [2, 1, 3])
        ]
        expected = [
            middle_lam * grad_u / m + S.diff(g, U) * grad_v,
            grad_u + d * U * grad_v,
            grad_v,
        ]
        for actual, target in zip(raw, expected):
            self.assert_zero(actual - target)

        # The shear transports the gradient by its literal Jacobian.
        psi = S.symbols("psi")
        shear = S.Matrix([U, psi + d * U**2 / 2])
        transported = shear.jacobian([U, psi]).T * S.Matrix(
            [entry.subs(V, shear[1]) for entry in (grad_u, grad_v)]
        )
        self.assert_zero(transported[0] - expected[1].subs(V, shear[1]))
        self.assert_zero(transported[1] - expected[2].subs(V, shear[1]))

    def test_constant_first_auxiliary_components_keep_the_second_iterate(self):
        X, theta = S.symbols("X theta")
        a, tau, delta, content = S.symbols("a tau delta content", nonzero=True)
        m, ml = S.symbols("m ml", nonzero=True)
        y0, t, q, r, rp, lam, sigma, f0, ell, p0, fl = S.symbols(
            "y0 t q r rp lam sigma f0 ell p0 fl"
        )
        z = m * theta + f0
        w = (ell - p0 - ml * theta**2 / 2 - fl * theta) / m
        coordinates = [
            X,
            y0 + t * X,
            z + sigma * X + q * X**2,
            w + theta * X + (rp * y0 + lam) * X**2 + r * X**3,
        ]
        action = lambda expression: tau * S.diff(expression, theta)
        time = lambda expression: a * S.diff(expression, X)
        columns = [action(expression) for expression in coordinates]
        targets = [0, 0, tau * m, tau * (X + S.diff(w, theta))]
        for actual, target in zip(columns, targets):
            self.assert_zero(actual - target)
        for expression in coordinates:
            self.assert_zero(time(action(expression)) - action(time(expression)))
        self.assert_zero(action(columns[2]))
        second_w = action(columns[3])
        self.assert_zero(second_w + tau**2 * ml / m)
        self.assertNotEqual(S.cancel(second_w), 0)  # Not a nice derivation here.
        self.assert_zero(action(second_w))

        # Formal division models the component identities only, not a gcd theorem.
        primitive = [S.cancel(entry.subs(tau, delta * content) / content) for entry in columns]
        primitive_second_w = delta * S.diff(primitive[3], theta)
        self.assert_zero(primitive[2] - delta * m)
        self.assert_zero(primitive_second_w + delta**2 * ml / m)
        Z = S.symbols("Z")
        theta_inverse = (Z - sigma * X - q * X**2 - f0) / m
        dw_in_original_slots = S.expand(primitive[3].subs(theta, theta_inverse))
        z_coefficient = -delta * ml / m**2
        self.assert_zero(S.diff(dw_in_original_slots, Z) - z_coefficient)
        self.assert_zero(primitive_second_w - z_coefficient * primitive[2])

        # A finite leading-slot control for the actual E-degree argument.
        Y, A0 = S.symbols("Y A0")
        b20, b11, b02, b10, b01, b00 = S.symbols("b20 b11 b02 b10 b01 b00")
        correction = b20 * X**2 + b11 * X * Y + b02 * Y**2 + b10 * X + b01 * Y + b00
        candidate = A0 * coordinates[2] + correction.subs(Y, coordinates[1])
        x2 = S.Poly(S.expand(candidate), X).coeff_monomial(X**2)
        self.assert_zero(x2 - A0 * q - b20 - b11 * t - b02 * t**2)
        cubic_ratio = S.Poly(x2.subs(q, t**3), t)
        self.assert_zero(cubic_ratio.coeff_monomial(t**3) - A0)

        # Once the Z coefficient vanishes, the actual triangular inverse is exact.
        d0 = S.symbols("d0", nonzero=True)
        W, J = S.symbols("W J")
        linear = b10 * X + b01 * Y + b00
        invariant = W - linear * Z / d0
        inverse = J + linear * Z / d0
        self.assert_zero(invariant.subs(W, inverse) - J)
        self.assert_zero(inverse.subs(J, invariant) - W)

    def test_selected_cofactor_fixtures_and_reducible_equations(self):
        U, V = S.symbols("U V")
        eta = S.symbols("eta", nonzero=True)
        conic = V - U**2
        cofactor = eta + conic
        equation = S.expand(conic * cofactor)
        self.assert_zero(equation - eta * conic - conic**2)
        self.assert_zero(equation.subs(V, U**2))
        self.assert_zero(cofactor.subs(V, U**2) - eta)
        self.assertGreater(S.Poly(cofactor, U, V).total_degree(), 0)
        for variable in (U, V):
            self.assert_zero(
                S.diff(equation, variable).subs(V, U**2)
                - eta * S.diff(conic, variable).subs(V, U**2)
            )
        self.assert_zero(homogeneous_part(equation, (U, V), 4) - U**4)

        # Keeping a nonunit evaluated cofactor destroys the gradient-unit gate.
        bad_cofactor = U**2 + 1
        bad_equation = conic * bad_cofactor
        bad_gradients = [S.diff(bad_equation, variable).subs(V, U**2) for variable in (U, V)]
        self.assert_zero(S.gcd(*bad_gradients) - bad_cofactor)
        for entry in bad_gradients:
            self.assert_zero(entry.subs(U, S.I))

        # A selected line can have the mixed top formally. Actual endpoint263
        # is additional information, not a conclusion of this plane fixture.
        line = U - 1
        line_equation = eta * line + line**2 * U * V
        self.assert_zero(line_equation.subs(U, 1))
        self.assert_zero((eta + line * U * V).subs(U, 1) - eta)
        self.assert_zero(homogeneous_part(line_equation, (U, V), 4) - U**3 * V)
        for degree in (3, 4):
            graph = V - U**degree
            h = eta * graph
            self.assertEqual(S.Poly(h, U, V).total_degree(), degree)
            self.assert_zero(h.subs(V, U**degree))

    def test_quartic_planes_discriminant_and_exact_coefficient_fixtures(self):
        x, U, V = S.symbols("x U V")
        graph = V - U**4
        self.assert_zero(graph.subs({U: x, V: x**4}))
        self.assert_zero(S.resultant(x - U, x**4 - V, x) + graph)

        a2, beta, p2, eta = S.symbols("a2 beta p2 eta", nonzero=True)
        c2, p1, p0 = S.symbols("c2 p1 p0")
        polynomial = p2 * U**2 + p1 * U + p0
        quadratic_first = a2 * x**2 + c2
        quartic_second = polynomial.subs(U, quadratic_first) + beta * x
        relation = (V - polynomial)**2 - beta**2 * (U - c2) / a2
        self.assert_zero(relation.subs({U: quadratic_first, V: quartic_second}))
        self.assert_zero(
            S.resultant(a2 * x**2 + c2 - U, beta * x + polynomial - V, x)
            - a2 * relation
        )
        x_inverse = (V - polynomial) / beta
        self.assert_zero(x_inverse.subs({U: quadratic_first, V: quartic_second}) - x)
        u_return = a2 * x_inverse**2 + c2
        self.assert_zero(u_return - U - a2 * relation / beta**2)
        v_return = polynomial.subs(U, u_return) + beta * x_inverse
        self.assert_zero(
            v_return - V - a2 * relation * (p2 * (u_return + U) + p1) / beta**2
        )
        equation = S.expand(eta * relation)
        self.assert_zero(S.discriminant(equation, V) - 4 * eta**2 * beta**2 * (U - c2) / a2)
        cross = S.Poly(equation, U, V).coeff_monomial(U**2 * V)
        top = S.Poly(equation, U, V).coeff_monomial(U**4)
        nll = 2 * eta
        self.assert_zero(cross**2 - 2 * nll * top)

        t, lam = S.symbols("t lam")
        slope, offset, gamma = S.symbols("slope offset gamma")
        m = 1 / (slope * t + offset)
        nu = gamma * m**2
        k = m * lam + t**3
        n = nu * lam + t**4
        self.assert_zero(S.diff(1 / m, t, 2))
        self.assert_zero(S.diff(nu / m**2, t))
        self.assert_zero(S.diff(k, lam) - m)
        self.assert_zero(S.diff(n, lam, 2))
        self.assert_zero(S.diff(m, t, 2) / 2 - S.diff(m, t)**2 / m)
        self.assert_zero(S.diff(n, t, lam) - 2 * S.diff(n, lam) * S.diff(m, t) / m)
        self.assertNotEqual(S.diff(1 / t, t, 2), 0)
        self.assertEqual(S.diff(t, t), 1)  # m=1, nu=t fails the second gate.

        # A rational fixture for the quadratic-in-lambda necessary identity.
        # Only the displayed leading coefficient gate is claimed, not an
        # entire calibrated chart or an ambient realization.
        m2, q, r = t, t**4, t**3
        n2 = -lam**2 / (12 * t**2)
        alpha = (S.diff(q, t, 4) - m2 * S.diff(r, t, 4)
                 - 4 * S.diff(q, t, 3) * S.diff(m2, t) / m2) / 24
        cross2 = S.diff(m2, t, 2) / 2 - S.diff(m2, t)**2 / m2
        self.assert_zero(cross2**2 - 2 * S.diff(n2, lam, 2) * alpha)
        self.assert_zero(S.diff(n2, lam, 3))
        self.assertNotEqual(S.diff(n2, lam, 2), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

