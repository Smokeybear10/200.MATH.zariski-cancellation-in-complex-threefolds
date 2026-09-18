"""Independent finite algebra controls for the three working pass211 notes.

These symbolic identities check actual coordinate maps, displayed derivation
columns, and bounded coefficient controls. They do not prove local nilpotence,
primitive division, normality, differential constants, Wang's alternatives,
polynomial contraction, factorial closure, or either recognition theorem.
Formal slope data below are not asserted to be realizable actual frames.
No earlier checker or solver implementation is imported.
"""

import unittest

import sympy as s


class RadicalAffinePairControls(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(s.cancel(s.expand(value)), 0)

    def inverse_orders(self, inputs, outputs, forward, backward):
        to_outputs = dict(zip(outputs, forward))
        to_inputs = dict(zip(inputs, backward))
        for original, expression in zip(inputs, backward):
            self.zero(expression.subs(to_outputs, simultaneous=True) - original)
        for original, expression in zip(outputs, forward):
            self.zero(expression.subs(to_inputs, simultaneous=True) - original)

    def test_literal_auxiliary_columns_and_constant_mu_coordinates(self):
        X, Y, Z, W, h = s.symbols("X Y Z W h")
        mu = s.symbols("mu", nonzero=True)
        nu, lam, omega, t, rho, k, kt, kr, n, tau, a = s.symbols(
            "nu lam omega t rho k kt kr n tau a"
        )
        y, w = mu * h + nu, lam * h + omega
        z = 2 * rho * w + h**2 + kt * y + kr * h + n
        yf = y + t * X
        wf = w + h * X + rho * X**2
        zf = z + (2 * rho * h + k) * X + rho**2 * X**2
        P = lambda expression: tau * s.diff(expression, h)
        self.zero(P(yf) - tau * mu)
        self.zero(P(wf) - tau * (X + lam))
        self.zero(P(zf) - tau * (2 * h + 2 * rho * X + 2 * rho * lam + kt * mu + kr))
        self.zero(P(P(yf)))
        self.zero(P(P(wf)))
        self.zero(P(P(zf)) - 2 * tau**2)
        self.zero(P(P(P(zf))))
        M = 2 * (rho - t / mu)
        H = 2 * rho * lam + kt * mu + kr - 2 * nu / mu
        self.zero(P(zf - yf**2 / mu**2) - tau * (M * X + H))
        self.zero(P(P(zf - yf**2 / mu**2)))

        # The parameters in each displayed polynomial coordinate map are complex
        # scalars. The preceding independent jet symbols are not a field proof.
        x0, u0, y0, v0 = s.symbols("x0 u0 y0 v0")
        T = Z - Y**2 / mu**2
        U = (X + lam) * Y - mu * W
        self.inverse_orders(
            (X, Y, Z, W), (x0, u0, y0, v0), (X, U, Y, T),
            (x0, y0, v0 + y0**2 / mu**2, ((x0 + lam) * y0 - u0) / mu),
        )
        self.zero(P((X + lam) * yf - mu * wf))
        leader = s.Poly(s.expand((X + lam) * yf - mu * wf), X).coeff_monomial(X**2)
        self.zero(a**2 * leader - a**2 * (t - mu * rho))

        m1, m0, h1, h0 = s.symbols("m1 m0 h1 h0")
        row = m1 * X + h1
        correction = (row * X - m0 * X - h0) / mu
        U2 = T - row * W + correction * Y
        self.inverse_orders(
            (X, Y, Z, W), (x0, u0, y0, v0), (X, U2, Y, W),
            (x0, y0,
             u0 + (m1 * x0 + h1) * v0
             - ((m1 * x0 + h1) * x0 - m0 * x0 - h0) * y0 / mu
             + y0**2 / mu**2, v0),
        )
        # Independent abstract nice columns, with the stated two slope relations.
        p_u2 = (m1 * lam + m0) * X + h1 * lam + h0
        p_u2 -= row * (X + lam)
        p_u2 += correction * mu
        self.zero(p_u2)
        chart_u2 = U2.subs({Y: yf, Z: zf, W: wf}, simultaneous=True)
        leader = s.Poly(s.expand(chart_u2), X).coeff_monomial(X**3)
        self.zero(a**3 * leader - m1 * a**3 * (t / mu - rho))

    def test_auxiliary_slice_and_finite_weighted_leader_controls(self):
        X, U, Y, V = s.symbols("X U Y V")
        b = s.symbols("b", nonzero=True)
        c = s.Function("c")(X, U)
        D = lambda expression: b * s.diff(expression, Y) + c * s.diff(expression, V)
        H = V - c * Y / b
        self.zero(D(H))
        self.zero(D(Y / b) - 1)
        self.zero(D(D(Y)))
        self.zero(D(D(V)))
        x0, u0, h0, y0 = s.symbols("x0 u0 h0 y0")
        self.inverse_orders(
            (X, U, Y, V), (x0, u0, h0, y0), (X, U, H, Y),
            (x0, u0, y0, h0 + s.Function("c")(x0, u0) * y0 / b),
        )

        # Fixed weight-six controls exhibit the common speed factor without
        # postulating algebraic independence of that speed. The general
        # noncancellation statement belongs to the written transcendence proof.
        a, f = s.symbols("a f")
        for degree in (2, 3):
            coefficients = s.symbols("c0:" + str(6 // degree + 1))
            homogeneous = sum(cj * X**(6 - degree * j) * U**j
                              for j, cj in enumerate(coefficients))
            evaluated = homogeneous.subs({X: a, U: a**degree * f}, simultaneous=True)
            reduced = sum(cj * f**j for j, cj in enumerate(coefficients))
            self.zero(evaluated - a**6 * reduced)
            self.assertEqual(s.Poly(reduced, f).all_coeffs(), list(reversed(coefficients)))
            self.zero(evaluated.subs(a, 1) - reduced)

    def test_linear_exception_and_actual_normalization(self):
        X, Y, Z, W, M, L = s.symbols("X Y Z W M L")
        aa, bb, cc, r, shift, tau = s.symbols("aa bb cc r shift tau")
        formal = s.Poly(1 + aa * M**2 + bb * M * (X + L) + cc * (X + L)**2, M, L)
        self.zero(formal.coeff_monomial(L) - 2 * X * formal.coeff_monomial(L**2))
        self.zero(formal.coeff_monomial(M) - X * formal.coeff_monomial(M * L))
        # This valid formal exception must not be rejected by the quadratic gate.
        lam = r * M + shift
        self.zero(1 - (X + lam - r * M)**2 / (X + shift)**2)
        self.zero(s.diff((X + lam) / M, M) + (X + shift) / M**2)
        q2 = -(W - r * Y)**2 / (X + shift)**2
        slope = lambda expression: tau * M * s.diff(expression, Y) + tau * (X + lam) * s.diff(expression, W)
        self.zero(slope(slope(q2)) + 2 * tau**2)

        x0, y0, z0, w0 = s.symbols("x0 y0 z0 w0")
        forward1 = (X + shift, Y, Z, W - r * Y)
        self.inverse_orders(
            (X, Y, Z, W), (x0, y0, z0, w0), forward1,
            (x0 - shift, y0, z0, w0 + r * y0),
        )
        h, nu, omega, t, rho, k, kt, kr, n = s.symbols("h nu omega t rho k kt kr n")
        y, w = M * h + nu, lam * h + omega
        z = 2 * rho * w + h**2 + kt * y + kr * h + n
        old_x = x0 - shift
        new_y = y - shift * t
        new_h = h - r * t - 2 * shift * rho
        new_w = omega - r * nu + r * shift * t + shift**2 * rho
        new_k = k + 2 * r * rho * t + 2 * shift * rho**2
        self.zero(y + t * old_x - new_y - t * x0)
        self.zero(w + h * old_x + rho * old_x**2 - r * (y + t * old_x)
                  - new_w - new_h * x0 - rho * x0**2)
        new_z = z - shift * (2 * rho * h + k) + shift**2 * rho**2
        self.zero(z + (2 * rho * h + k) * old_x + rho**2 * old_x**2
                  - new_z - (2 * rho * new_h + new_k) * x0 - rho**2 * x0**2)
        self.zero(s.diff(new_y, h) - M)
        self.zero(s.diff(new_h, h) - 1)
        self.zero(s.diff(new_w, h))

        c1, c0, d1, d0 = s.symbols("c1 c0 d1 d0")
        forward2 = (X, Y, Z - c1 * Y, W + c0 * X / 2 - d0)
        self.inverse_orders(
            (X, Y, Z, W), (x0, y0, z0, w0), forward2,
            (x0, y0, z0 + c1 * y0, w0 - c0 * x0 / 2 + d0),
        )
        self.zero(((kt - c1) * M + kr - c0).subs(kr, c1 * M + c0 - kt * M))
        self.zero((d1 * M + d0) - d0 - d1 * M)
        self.zero((2 * rho * h + k - c1 * t)
                  - (2 * rho * (h + c0 / 2) + k - c1 * t - c0 * rho))
        # Literal partial_Z columns and weighted initial entries survive both maps.
        scale = s.symbols("scale")
        weighted = {X: scale * X, Y: scale * Y, Z: scale**2 * Z, W: scale**2 * W}
        for mapping in (forward1, forward2):
            self.assertEqual(tuple(s.diff(entry, Z) for entry in mapping), (0, 0, 1, 0))
            for expression, variable, weight in zip(mapping, (X, Y, Z, W), (1, 1, 2, 2)):
                lifted = s.Poly(s.expand(expression.subs(weighted, simultaneous=True)), scale)
                self.zero(lifted.coeff_monomial(scale**weight) - variable)

    def test_fixed_polynomial_fiber_and_parity_identities(self):
        X, Y, Z, W, h, rho, mu, omega, K0, tau = s.symbols("X Y Z W h rho mu omega K0 tau")
        q1, q2, q0, d = s.symbols("q1 q2 q0 d")
        # Literal chart columns before the last normalization retain both lower terms.
        wf = omega + h * X + rho * X**2
        F = Z - W**2 / X**2 + q1 * Y + q2 * W + q0
        PF = tau * mu * s.diff(F, Y) + tau * X * s.diff(F, W)
        PF += tau * (2 * h + 2 * rho * X + K0) * s.diff(F, Z)
        expected = tau * (K0 - 2 * omega / X + q1 * mu + q2 * X)
        self.zero(PF.subs(W, wf) - expected)
        self.zero(expected.subs({K0: 0, omega: d * mu, q1: 2 * d / X, q2: 0}, simultaneous=True))

        F0 = X**2 * Z - W**2 + 2 * d * X * Y
        self.zero((F - q0).subs({q1: 2 * d / X, q2: 0}, simultaneous=True) - F0 / X**2)
        b0, tau0, dz = s.symbols("b0 tau0 dz")
        DF0 = b0 * s.diff(F0, Y) + tau0 * X * s.diff(F0, W) + dz * s.diff(F0, Z)
        self.zero(DF0 - X * (X * dz - 2 * tau0 * W + 2 * d * b0))
        at_chart = DF0.subs(
            {b0: tau * mu, tau0: tau, dz: tau * (2 * h + 2 * rho * X),
             W: d * mu + h * X + rho * X**2}, simultaneous=True,
        )
        self.zero(at_chart)
        c = s.symbols("c")
        fiber = F0.subs(X, c)
        self.zero(s.diff(fiber, Z) - c**2)
        self.zero(fiber.subs(c, 0) + W**2)

        # Bounded degree-four coefficient controls for the original odd/even
        # identity. They do not certify contraction or factorial closure.
        variable = s.symbols("variable")
        ac = s.symbols("a0:5")
        bc = s.symbols("b0:5")
        A = sum(coefficient * variable**j for j, coefficient in enumerate(ac))
        B = sum(coefficient * variable**j for j, coefficient in enumerate(bc))
        odd = W * A.subs(variable, -W**2)
        even = -d * B.subs(variable, -W**2)
        relation = s.Poly(s.expand(odd + even), W)
        for j in range(5):
            self.zero(relation.coeff_monomial(W**(2 * j + 1)) - (-1)**j * ac[j])
            self.zero(relation.coeff_monomial(W**(2 * j)) + d * (-1)**j * bc[j])
        self.zero((odd + even - (odd + even).subs(W, -W)) / 2 - odd)
        self.zero((odd + even + (odd + even).subs(W, -W)) / 2 - even)
        self.zero(relation.as_expr().subs(d, 0) - odd)


if __name__ == "__main__":
    unittest.main()
