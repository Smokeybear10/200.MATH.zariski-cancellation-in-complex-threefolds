"""Finite exact controls for the two coprime-quartic exclusion branches.

These independent coefficient jets are formal, not inverse-verified actual
frames.  They check determinant, potential and differential identities only.
The actual field extensions, constant determinant, unit selected cofactor,
whole-plane return and algebraic-function valuation arguments remain written
proofs.  No finite identity establishes their universal hypotheses.

No earlier checker or proof internal is imported.  This file is authored
source-only; Root owns its canonical execution after complete source review.
"""

import unittest

import sympy as sp


class WeightFourCoprimeExclusionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_constant_projection_raw_determinant_and_staged_coefficients(self):
        t, y, X, theta = sp.symbols("t y X theta")
        R, A0, K0, rho, alpha, beta, g = sp.symbols(
            "R A0 K0 rho alpha beta g")
        Rt, At, Kt, rhot, alphat, betat, gt = sp.symbols(
            "R_t A0_t K0_t rho_t alpha_t beta_t g_t")
        Ry, Ay, Ky, rhoy, alphay, betay, gy = sp.symbols(
            "R_y A0_y K0_y rho_y alpha_y beta_y g_y")
        coefficients = (R, A0, K0, rho, alpha, beta, g)
        t_jets = (Rt, At, Kt, rhot, alphat, betat, gt)
        y_jets = (Ry, Ay, Ky, rhoy, alphay, betay, gy)

        def dt(expression):
            return sp.diff(expression, t) + sum(
                sp.diff(expression, coefficient) * derivative
                for coefficient, derivative in zip(coefficients, t_jets))

        def dy(expression):
            return sp.diff(expression, y) + sum(
                sp.diff(expression, coefficient) * derivative
                for coefficient, derivative in zip(coefficients, y_jets))

        w = alpha * theta**2 + beta * theta + g
        Y = y + t * X
        W = w + theta * X + rho * X**2
        # Literal original Z is differentiated before doing the row addition.
        Z = R * theta + A0 + K0 * X - t**2 * W
        raw = sp.Matrix([[dt(value), dy(value), sp.diff(value, theta)]
                         for value in (Y, Z, W)])
        reduced = raw.copy()
        reduced[1, :] = raw[1, :] + t**2 * raw[2, :]
        expected_middle = [
            Rt * theta + At - 2 * t * w
            + (Kt - 2 * t * theta) * X - 2 * t * rho * X**2,
            Ry * theta + Ay + Ky * X,
            R,
        ]
        for actual, expected in zip(reduced[1, :], expected_middle):
            self.zero(actual - expected)
        self.zero(raw.det() - reduced.det())

        determinant = sp.expand(reduced.det())
        literal = (
            (sp.diff(w, theta) + X)
            * (2 * t * w - Rt * theta - At
               + X * ((Ry + 2 * t) * theta + Ay - Kt)
               + X**2 * (Ky + 2 * t * rho))
            + R * (dt(w) - X * dy(w) + rhot * X**2 - rhoy * X**3)
        )
        self.zero(determinant - literal)
        self.zero(determinant.coeff(X, 0).coeff(theta, 3)
                  - 4 * t * alpha**2)

        # In the written proof t != 0 in a field forces alpha=0.
        # Its coefficient derivatives must also be set to zero.
        affine = sp.expand(determinant.subs(
            {alpha: 0, alphat: 0, alphay: 0}, simultaneous=True))
        self.zero(affine.coeff(X, 2).coeff(theta, 1) - (Ry + 2 * t))
        x_theta = affine.coeff(X, 1).coeff(theta, 1)
        self.zero(x_theta - (2 * t * beta - Rt
                            + beta * (Ry + 2 * t) - R * betay))
        reduced_x_theta = sp.expand(x_theta.subs(Ry, -2 * t))
        self.zero(reduced_x_theta - (2 * t * beta - Rt - R * betay))
        theta_only = affine.coeff(X, 0).coeff(theta, 1)
        self.zero(theta_only - (beta * (2 * t * beta - Rt) + R * betat))
        # Exact elimination of the preceding coefficient equation.
        self.zero(theta_only - beta * reduced_x_theta
                  - R * (betat + beta * betay))

    def test_forced_rational_beta_and_cleared_riccati_residual(self):
        t, R = sp.symbols("t R", nonzero=True)
        B, e, Bp, ep = sp.symbols("B e B_prime e_prime")
        beta = R / (4 * t**2) + B + e / R
        Rt, Ry = R / t + 2 * t * B, -2 * t

        def dt(expression):
            return (sp.diff(expression, t) + sp.diff(expression, R) * Rt
                    + sp.diff(expression, B) * Bp
                    + sp.diff(expression, e) * ep)

        def dy(expression):
            return sp.diff(expression, R) * Ry

        expected_dt = (-R / (4 * t**3) + B / (2 * t) + Bp
                       + ep / R - 2 * t * B * e / R**2 - e / (t * R))
        expected_product = (-R / (8 * t**3) - B / (2 * t)
                            + 2 * t * B * e / R**2 + 2 * t * e**2 / R**3)
        self.zero(dt(beta) - expected_dt)
        self.zero(beta * dy(beta) - expected_product)
        self.zero(dt(Ry) - dy(Rt))
        residual = dt(beta) + beta * dy(beta)
        self.zero(residual - (-3 * R / (8 * t**3) + Bp
                              + (ep - e / t) / R + 2 * t * e**2 / R**3))
        # Clear only certified nonzero monomial denominators.
        cleared = sp.expand(8 * t**3 * R**3 * residual)
        self.zero(cleared - (-3 * R**4 + 8 * t**3 * Bp * R**3
                            + (8 * t**3 * ep - 8 * t**2 * e) * R**2
                            + 16 * t**4 * e**2))
        self.assertEqual(sp.degree(cleared, R), 4)
        self.assertEqual(cleared.coeff(R, 4), -3)
        # Its impossibility requires the written proof that R is
        # transcendental over ker(partial_y), not this degree calculation.

        r, rp, d, y = sp.symbols("r r_prime d y")
        R0 = r - 2 * t * y
        B0 = rp / (2 * t) - r / (2 * t**2)
        e0 = d - rp * r / (2 * t) + r**2 / (4 * t**2)
        # Numerator comparison verifies the integrated expression without
        # asking a rational simplifier to cancel a coordinate denominator.
        self.zero(R0**2 / (4 * t**2) + B0 * R0 + e0
                  - (-rp * y + y**2 + d))
        self.zero((r - R0) / (2 * t) - y)
        self.zero(R0 / t + 2 * t * B0 - (rp - 2 * y))

    def test_literal_graph_coefficients_and_euler_compatibility(self):
        t, U, V = sp.symbols("t U V")
        ell, ellt, ellr, m = sp.symbols("ell ell_t ell_r m")

        def jets(prefix, order):
            return {(i, j): sp.Symbol(f"{prefix}{i}{j}")
                    for i in range(order + 1)
                    for j in range(order + 1 - i)}

        def H(coefficients, degree):
            return sum(coefficients[i, degree - i] * U**i * V**(degree - i)
                       / (sp.factorial(i) * sp.factorial(degree - i))
                       for i in range(degree + 1))

        k, n = jets("k", 3), jets("n", 2)
        R = k[0, 1] - 2 * t * U
        S = -U**2 * V + H(k, 2) + H(n, 1)
        A = sp.diff(S, V)
        g4 = H(k, 3) + H(n, 2)
        literal = sp.expand(R * (g4 - ellt * U - ellr * V - m)
                            + A * (ell - S))
        self.zero(A - (-U**2 + k[1, 1] * U + k[0, 2] * V + n[0, 1]))
        v3 = literal.coeff(V, 3)
        v2 = literal.coeff(V, 2)
        self.zero(v3 - (R * k[0, 3] / 6 - k[0, 2]**2 / 2))
        self.zero(v2 - (R * (k[1, 2] * U + n[0, 2]) / 2
                       - 3 * k[0, 2] * (-U**2 + k[1, 1] * U + n[0, 1]) / 2))
        self.zero(v2.coeff(U, 2) - (-t * k[1, 2] + 3 * k[0, 2] / 2))
        polynomial = sp.Poly(literal, U, V)
        self.assertEqual(polynomial.total_degree(), 5)
        self.assertLessEqual(polynomial.degree(V), 3)
        top = sum(coefficient * U**powers[0] * V**powers[1]
                  for powers, coefficient in polynomial.terms()
                  if sum(powers) == 5)
        self.zero(top + U**4 * V)

        p2 = sp.Symbol("p2", nonzero=True)
        p1, p0, omega, L0 = sp.symbols("p1 p0 omega L0")
        G = V - (p2 * U**2 + p1 * U + p0)
        graph_model = sp.expand(omega * G + (L0 - V / p2**2) * G**2)
        model_polynomial = sp.Poly(graph_model, U, V)
        model_top = sum(coefficient * U**powers[0] * V**powers[1]
                        for powers, coefficient in model_polynomial.terms()
                        if sum(powers) == 5)
        self.zero(model_top + U**4 * V)
        self.zero(graph_model.coeff(V, 3) + 1 / p2**2)
        self.zero(graph_model.coeff(V, 2).coeff(U, 2) - 2 / p2)
        v3_error = sp.expand(v3 - graph_model.coeff(V, 3))
        self.zero(v3_error.coeff(U, 1) + t * k[0, 3] / 3)
        self.zero(2 * p2**2 * v3_error.subs(k[0, 3], 0)
                  - (2 - k[0, 2]**2 * p2**2))

        h, hp, delta = sp.symbols("h h_prime delta")
        literal_quadratic_error = -t * hp + 3 * h / 2 - 2 / p2
        euler_error = -t * hp + 3 * h / 2 - h**2 * p2
        self.zero(literal_quadratic_error - euler_error
                  - (h**2 * p2**2 - 2) / p2)
        # Under delta=h*p2 and delta^2=2, the Euler exponent is 3/2-delta.
        exponent = sp.Rational(3, 2) - delta
        self.zero(4 * exponent**2 - 12 * exponent + 1
                  - 4 * (delta**2 - 2))
        lam = sp.Symbol("lambda")
        self.assertEqual(sp.discriminant(4 * lam**2 - 12 * lam + 1, lam), 128)

        # Finite generic minimal-polynomial controls reconstruct the
        # coefficient identity used in the written Euler lemma.  They do
        # not replace minimality or prove its universal rational-exponent claim.
        z = sp.Symbol("z")
        for degree in (2, 3, 5):
            coefficients = sp.symbols(f"a0:{degree}")
            derivatives = sp.symbols(f"da0:{degree}")
            relation = z**degree + sum(
                coefficient * z**i for i, coefficient in enumerate(coefficients))
            differentiated = lam * z * sp.diff(relation, z) + sum(
                t * derivative * z**i for i, derivative in enumerate(derivatives))
            remainder = sp.expand(differentiated - degree * lam * relation)
            expected = sum((t * derivative - (degree - i) * lam * coefficient) * z**i
                           for i, (coefficient, derivative)
                           in enumerate(zip(coefficients, derivatives)))
            self.zero(remainder - expected)
            self.zero(remainder.coeff(z, 0)
                      - (t * derivatives[0] - degree * lam * coefficients[0]))

        # Exact leading-form boundaries for linear and constant graphs.
        # Nonconstant linear P requires p1!=0 in the written argument.
        self.zero(top.subs(V, p1 * U) + p1 * U**5)
        s0, s1, s2, s3 = sp.symbols("s0 s1 s2 s3")
        T3 = s0 * U**3 + s1 * U**2 * V + s2 * U * V**2 + s3 * V**3
        constant_graph = sp.expand(omega * (V - p0) + (V - p0)**2 * T3)
        constant_top = sum(coefficient * U**powers[0] * V**powers[1]
                           for powers, coefficient in sp.Poly(constant_graph, U, V).terms()
                           if sum(powers) == 5)
        self.zero(constant_top - V**2 * T3)
        self.assertEqual(sp.expand(constant_top).coeff(U, 4).coeff(V, 1), 0)
        self.assertEqual(sp.expand(top).coeff(U, 4).coeff(V, 1), -1)
        # For degree>=3 a nonzero G^2 term already has degree>=6.
        # The following are finite leading-term controls, not exhaustion.
        for degree in (3, 4, 5):
            graph = V - U**degree - p1 * U - p0
            self.assertEqual(sp.Poly(graph**2, U, V).total_degree(), 2 * degree)
            self.assertEqual(sp.Poly(graph, U, V).total_degree(), degree)
            self.zero(sp.Poly(graph, U, V).coeff_monomial(U**degree) + 1)


if __name__ == "__main__":
    unittest.main()
