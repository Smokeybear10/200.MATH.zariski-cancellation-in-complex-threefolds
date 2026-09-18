"""Finite identities for actual square-root normalization and graph exclusion196.

These checks do not establish actualness, integral closure, irreducibility,
finite-field ODE completeness, or the unrestricted cancellation conjecture.
No earlier checker or solver is imported.
"""

import unittest

import sympy as sp


class SquareRootGraphControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_raw_lower_coefficient_gates_and_laurent_solutions(self):
        q, rho, c = sp.symbols("q rho c")
        k0 = sp.Function("k")(q)
        s0 = sp.Function("s")(q)
        n0 = sp.Function("n")(q)
        ell0 = sp.Function("ell0")(q)

        def derivative(expression):
            return sp.diff(expression, q) / (2 * q)

        R, nu, Delta, d = 1 / q, -1 / q**3, 1 / (8 * q**6), 1 / (16 * q**5)

        def raw_coefficients(k_lower, s_lower, n_lower):
            k = rho / q + k_lower
            n = -rho**2 / (2 * q**3) + s_lower * rho + n_lower
            nr = sp.diff(n, rho)
            B = R * derivative(nr) - 2 * derivative(R) * nr
            C2 = (R * derivative(derivative(n)) / 2
                  - derivative(R) * derivative(n) - nr * derivative(derivative(k)) / 2)
            ell_rho = B**2 / (2 * Delta * R) - nu * C2 / Delta - nr**2 / R
            ell = sp.integrate(sp.Poly(sp.expand(ell_rho), rho).as_expr(), rho) + ell0
            C = -R * sp.diff(ell, rho) - nr**2
            B1 = (-R * derivative(ell) + derivative(R) * ell
                  - nr * derivative(n) - B * C / (R * nu))
            U3 = (R * derivative(derivative(derivative(k))) / 6
                  - derivative(R) * derivative(derivative(k)) / 2
                  - nr * d - Delta * B / (R * nu))
            return sp.factor(U3), sp.Poly(sp.expand(B1), rho)

        U3, _ = raw_coefficients(k0, s0, n0)
        self.zero(U3 - (q * sp.diff(k0, q, 3)
                        + 3 * q * sp.diff(s0, q) + 3 * s0) / (48 * q**5))
        forced_s = (sp.diff(k0, q) - q * sp.diff(k0, q, 2) + c) / (3 * q)
        U3, B1 = raw_coefficients(k0, forced_s, n0)
        self.zero(U3)
        self.zero(B1.coeff_monomial(rho**2)
                  - (q * sp.diff(k0, q, 5) + 5 * sp.diff(k0, q, 4)) / (12 * q**3))

        u, A0, A1, A2, h, S, Nm, N0, Np = sp.symbols("u A0 A1 A2 h S Nm N0 Np")
        k_solution = u / q + A0 + A1 * q + A2 * q**2 + h * q**3
        s_solution = S / q - h * q - u / q**3
        n_solution = (-h**2 * q**5 / 2 + h * S * q**3 - u**2 / (2 * q**3)
                      + Nm / q + N0 + Np * q)
        U3, B1 = raw_coefficients(k_solution, s_solution, n0)
        n_gate = -(sp.diff(n0, q, 3) + 3 * sp.diff(n0, q, 2) / q
                   + 60 * h**2 * q**2 - 24 * h * S - 12 * u**2 / q**6) / (2 * q**2)
        self.zero(U3)
        self.zero(B1.coeff_monomial(rho) - n_gate)
        _, final_B1 = raw_coefficients(k_solution, s_solution, n_solution)
        for power in (1, 2, 3):
            self.zero(final_B1.coeff_monomial(rho**power))

    def test_actual_shear_columns_and_inverse_orders(self):
        q, rho, y, theta = sp.symbols("q rho y theta")
        u, A0, A1, A2, h, S, Nm, N0, Np = sp.symbols("u A0 A1 A2 h S Nm N0 Np")
        k0 = u / q + A0 + A1 * q + A2 * q**2 + h * q**3
        slower = S / q - h * q - u / q**3
        nlower = (-h**2 * q**5 / 2 + h * S * q**3 - u**2 / (2 * q**3)
                  + Nm / q + N0 + Np * q)
        k = rho / q + k0
        n = -rho**2 / (2 * q**3) + slower * rho + nlower
        sigma = y / (2 * q) + k
        z = -y**2 / (8 * q**3) + sp.diff(k, q) * y / (2 * q) + theta / q + n
        shifted_rho = rho + u + A1 * q**2 + h * q**4
        shifted_theta = theta + (A1 + 2 * h * q**2) * y
        shifted_z = z - A2 * y
        self.zero(sigma - A0 - A2 * q**2 - y / (2 * q) - shifted_rho / q)
        new_n = shifted_z + y**2 / (8 * q**3) + shifted_rho * y / (2 * q**3) - shifted_theta / q
        C = S + A1
        nlower_new = ((Nm - S * u) / q + N0
                      + (Np - S * A1 + h * u - A1**2 / 2) * q)
        self.zero(new_n + shifted_rho**2 / (2 * q**3) - C * shifted_rho / q - nlower_new)

        a, C, Nm, N0, Np = sp.symbols("a C Nm N0 Np")
        old_n = -rho**2 / (2 * q**3) + C * rho / q + Nm / q + N0 + Np * q
        old_sigma = y / (2 * q) + rho / q
        old_z = -y**2 / (8 * q**3) - rho * y / (2 * q**3) + theta / q + old_n
        ynew = y - a * q**2
        rnew = rho - sp.Rational(3, 2) * a * q**2
        znew = old_z - a * old_sigma + a**2 * q
        tnew = theta - 2 * a * rho - sp.Rational(3, 2) * a * ynew
        nnew = znew + ynew**2 / (8 * q**3) + rnew * ynew / (2 * q**3) - tnew / q
        self.zero(nnew + rnew**2 / (2 * q**3) - (C - a) * rnew / q
                  - Nm / q - N0 - (Np + sp.Rational(3, 2) * C * a) * q)
        self.zero((Nm / q + N0 + Np * q) - (Nm + Np * q**2) / q - N0)

        X, Y, Z, W = variables = sp.symbols("X Y Z W")
        P = u * X**2 + A1 * X * Y + h * Y**2
        pairs = [
            ((X, Y, Z - A0 * X - A2 * Y, W + P),
             (X, Y, Z + A0 * X + A2 * Y, W - P)),
            ((X + a, Y, Z, W - sp.Rational(3, 2) * a * (X + a) * Y),
             (X - a, Y, Z, W + sp.Rational(3, 2) * a * X * Y)),
            ((X, Y, Z - N0, W + Nm * X + Np * Y),
             (X, Y, Z + N0, W - Nm * X - Np * Y)),
        ]
        for forward, inverse in pairs:
            for outer, inner in ((forward, inverse), (inverse, forward)):
                substitutions = dict(zip(variables, inner))
                for slot, expression in zip(variables, outer):
                    self.zero(expression.subs(substitutions, simultaneous=True) - slot)

    def test_graph_square_identity_scalar_gate_and_formal_fixture(self):
        X, y, q, rho, g, C = sp.symbols("X y q rho g C")
        h = y / 2 + rho
        Y = y + q**2 * X
        Z = g + h * X / q + q * X**2
        W = h * g / q + C + (h**2 / (2 * q**2) + q * g) * X + rho * X**2
        self.zero(Z**2 - X**3 * Y - 2 * X * (W - C) - g**2)
        gq, gr = sp.symbols("gq gr")
        wq = h * gq / q - h * g / q**2
        wr = g / q + h * gr / q
        determinant_q = gq * wr - gr * wq
        determinant_t = determinant_q / (2 * q)
        self.zero(determinant_t - g * gq / (2 * q**2) - h * g * gr / (2 * q**3))
        self.zero(sp.diff(determinant_t, y) - g * gr / (4 * q**3))
        fixture = [Y, Z.subs(g, q), W.subs({g: q, C: 0})]
        self.zero(sp.Matrix(fixture).jacobian([y, q, rho]).det() - 1)
        # The W-linear polynomial has primitive coefficients. The field-index
        # and normality arguments themselves remain written, not tested here.
        YY, ZZ, WW = sp.symbols("YY ZZ WW")
        primitive_constant = ZZ**2 - X**3 * YY + 2 * C * X
        self.assertEqual(sp.gcd(-2 * X, primitive_constant), 1)
        self.zero(primitive_constant.subs(X, 0) - ZZ**2)


if __name__ == "__main__":
    unittest.main()
