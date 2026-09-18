"""Finite identities for normalized square-root quadratic-projection recognition197.

These controls are independent of older solver/checker implementations.
They do not prove exact field return, field-intersection arguments, completeness
over finite algebraic coefficient fields, or unrestricted cancellation.
"""

import unittest

import sympy as sp


class SquareRootQuadraticProjectionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_projected_scalar_coefficients_and_exact_ode_identities(self):
        q, rho, zeta = sp.symbols("q rho zeta")
        g = sp.Function("g")(q)
        offset = sp.Function("offset")(q, rho)
        gp = sp.diff(g, q)
        y = -zeta**2 / (q * gp) + offset
        z = zeta / q
        w = (y / 2 + rho) * zeta / q**2 + g
        determinant = sp.Matrix([y, z, w]).jacobian([q, rho, zeta]).det()
        cubic = -(2 * q * sp.diff(g, q, 2) - sp.diff(offset, rho) * gp - 2 * gp) / (2 * q**5 * gp**2)
        linear = -(2 * q * sp.diff(offset, q) + (2 * rho + offset) * sp.diff(offset, rho)) / (2 * q**4)
        constant = sp.diff(offset, rho) * gp / q
        self.zero(determinant - cubic * zeta**3 - linear * zeta - constant)

        slope = 2 * q * sp.diff(g, q, 2) / gp - 2
        self.zero(2 * q * sp.diff(slope, q) + 2 * slope + slope**2
                  - 4 * q**2 * sp.diff(g, q, 3) / gp)
        A, B, C, D = sp.symbols("A B C D")
        gpoly = A * q**2 + B * q + C
        u = -2 * B / (2 * A * q + B)
        v = D * q / (2 * A * q + B)
        self.zero(u - (2 * q * sp.diff(gpoly, q, 2) / sp.diff(gpoly, q) - 2))
        self.zero(2 * q * sp.diff(u, q) + 2 * u + u**2)
        self.zero(2 * q * sp.diff(v, q) + u * v)
        self.zero(gpoly.subs(q, -B / A - q) - gpoly)
        # The last identity exhibits the nontrivial involution when A != 0.
        # It is not a finite test of the actual field-return exclusion of A.

    def test_raw_potentials_and_actual_intrinsic_derivation_columns(self):
        q, rho, U, V, m = sp.symbols("q rho U V m")
        B, C, D = sp.symbols("B C D")
        R = 1 / q
        k = rho / q
        n = -rho**2 / (2 * q**3)
        ell = -rho**3 / (2 * q**5) + B + C / q

        def dt(expression):
            return sp.diff(expression, q) / (2 * q)

        S = (dt(dt(dt(q))) * U**3 / 6 + dt(dt(k)) * U**2 / 2
             + dt(R) * U * V + dt(n) * U + sp.diff(n, rho) * V)
        T = (dt(dt(dt(dt(q)))) * U**4 / 24 + dt(dt(dt(k))) * U**3 / 6
             + dt(dt(R)) * U**2 * V / 2 + dt(dt(n)) * U**2 / 2
             + dt(sp.diff(n, rho)) * U * V + sp.diff(n, rho, 2) * V**2 / 2)
        eliminant = R * (T - dt(ell) * U - sp.diff(ell, rho) * V - m)
        eliminant += (dt(R) * U + sp.diff(n, rho)) * (ell - S)
        P = (U + 2 * rho)**2 / (8 * q**2)
        completed = (-(V - P)**2 / (2 * q**4) - B * U / (2 * q**3)
                     + 5 * rho**4 / (8 * q**8) - rho * (B * q + C) / q**4 - m / q)
        self.zero(eliminant - completed)

        z = sp.symbols("z")
        y = q * (D - z**2) / B - 2 * rho
        theta = (y + 2 * rho)**2 / (8 * q**2) + q * z
        w = (y / 2 + rho) * z / q + B * q + C
        scalar_m = 5 * rho**4 / (8 * q**7) - C * rho / q**3 - D / (2 * q)
        evaluated = {U: y, V: theta, m: scalar_m}
        self.zero(eliminant.subs(evaluated, simultaneous=True))
        self.zero((ell - S).subs({U: y, V: theta}, simultaneous=True) / R - w)
        self.zero(dt(dt(q)) * y**2 / 2 + dt(k) * y + R * theta + n - z)

        X, Y, Z, W, yy, zz = sp.symbols("X Y Z W yy zz")
        J = (D - Z**2 + X**3 * Y + 2 * X * (W - C)) / (2 * B)
        zback = Z - X * J
        qback = (W - C - zback * J - X * J**2 / 2 + X**2 * Y / 2) / B
        yback = Y - qback**2 * X
        self.zero(sp.diff(zback, Z) - (1 + X * Z / B))
        self.zero(sp.diff(qback, Z) + J / B - zback * Z / B**2)
        self.zero(sp.diff(yback, Z) + 2 * qback * X * sp.diff(qback, Z))

        H = (D - zz**2) / (2 * B)
        Zforward = zz + H * X + q * X**2
        Jforward = H + q * X
        dq_column = -Jforward / B + zz * Zforward / B**2
        dz_column = 1 + X * Zforward / B
        dy_column = -2 * q * X * dq_column
        Nq = sp.Poly(dq_column, X).coeff_monomial(X**3)
        Nz = sp.Poly(dz_column, X).coeff_monomial(X**3)
        Ny = sp.Poly(dy_column, X).coeff_monomial(X**3)
        self.zero(Nq)
        self.zero(Nz - q / B)
        self.zero(Ny + 2 * q**2 * zz / B**2)
        rho_actual = q * H - yy / 2
        self.zero(sp.diff(rho_actual, q) * Nq + sp.diff(rho_actual, zz) * Nz
                  + sp.diff(rho_actual, yy) * Ny)
        self.zero(q * Nz - q**2 / B)

    def test_general_polynomial_inverse_both_orders_and_profile(self):
        x, y, z, q, B, C, D = sp.symbols("x y z q B C D")
        X, Y, Z, W = sp.symbols("X Y Z W")
        H = (D - z**2) / (2 * B)
        rho = q * H - y / 2
        forward = (x, y + q**2 * x, z + H * x + q * x**2,
                   C + B * q + H * z + (q * z + H**2 / 2) * x + rho * x**2)
        J = (D - Z**2 + X**3 * Y + 2 * X * (W - C)) / (2 * B)
        zback = Z - X * J
        qback = (W - C - zback * J - X * J**2 / 2 + X**2 * Y / 2) / B
        yback = Y - qback**2 * X
        inverse = (X, yback, zback, qback)
        self.zero(D - zback**2 - 2 * B * (J - qback * X))
        for outer, inner, slots, expected in (
            (inverse, forward, (X, Y, Z, W), (x, y, z, q)),
            (forward, inverse, (x, y, z, q), (X, Y, Z, W)),
        ):
            substitutions = dict(zip(slots, inner))
            for expression, target in zip(outer, expected):
                self.zero(expression.subs(substitutions, simultaneous=True) - target)
        self.zero(sp.Matrix(forward).jacobian([x, y, z, q]).det() - B)
        self.assertEqual(tuple(sp.degree(entry, x) for entry in forward), (1, 1, 2, 2))
        leaders = tuple(sp.Poly(entry, x).LC() for entry in forward)
        for actual, expected in zip(leaders, (1, q**2, q, rho)):
            self.zero(actual - expected)
        xi = sp.symbols("xi")
        initial = (xi, q**2 * xi, q * xi**2, rho * xi**2)
        self.zero(initial[2]**2 - initial[0]**3 * initial[1])
        # The full height-one prime-kernel argument remains the written proof.


if __name__ == "__main__":
    unittest.main()

