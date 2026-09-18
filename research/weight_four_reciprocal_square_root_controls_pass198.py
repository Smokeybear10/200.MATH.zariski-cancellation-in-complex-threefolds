"""Finite exact controls for the three reciprocal square-root notes in pass198.

These independent symbolic identities do not prove completeness in algebraic
coefficient fields, exact field return, normality, irreducibility, the preservation
of an entire initial kernel, or recognition/exclusion. Those require the written
proofs and actual-frame hypotheses. No prior checker or solver is imported.
"""

import unittest

import sympy as sp


class ReciprocalSquareRootControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def coefficient(self, expression, variables, monomial):
        return sp.Poly(sp.expand(expression), *variables).coeff_monomial(monomial)

    def potentials(self, q, rho, U, V, k, n, ell, m):
        def dt(expression):
            return sp.diff(expression, q) / (2 * q)

        R = sp.diff(k, rho)
        S = (dt(dt(dt(q))) * U**3 / 6 + dt(dt(k)) * U**2 / 2
             + dt(R) * U * V + dt(n) * U + sp.diff(n, rho) * V)
        T = (dt(dt(dt(dt(q)))) * U**4 / 24 + dt(dt(dt(k))) * U**3 / 6
             + dt(dt(R)) * U**2 * V / 2 + dt(dt(n)) * U**2 / 2
             + dt(sp.diff(n, rho)) * U * V + sp.diff(n, rho, 2) * V**2 / 2)
        H = R * (T - dt(ell) * U - sp.diff(ell, rho) * V - m)
        H += (dt(R) * U + sp.diff(n, rho)) * (ell - S)
        return S, T, H

    def test_literal_lower_coefficients_and_euler_solutions(self):
        q, rho, U, V, m = sp.symbols("q rho U V m")
        k0, s0, n0, l0 = (sp.Function(name)(q) for name in ("k0", "s0", "n0", "l0"))
        k = q * rho + k0
        n = -q * rho**2 / 2 + s0 * rho + n0

        def dt(expression):
            return sp.diff(expression, q) / (2 * q)

        R, nu = q, -q
        Delta = R * dt(dt(R)) / 2 - dt(R)**2
        C4 = R * dt(dt(dt(dt(q)))) / 24 - dt(R) * dt(dt(dt(q))) / 6
        self.zero(Delta + 3 / (8 * q**2))
        self.zero(C4 + 9 / (128 * q**6))
        self.zero(Delta**2 / (2 * R * C4) - nu)
        Bcal = R * dt(sp.diff(n, rho)) - 2 * dt(R) * sp.diff(n, rho)
        C2 = R * dt(dt(n)) / 2 - dt(R) * dt(n) - sp.diff(n, rho) * dt(dt(k)) / 2
        ell_rho = sp.expand(Bcal**2 / (2 * Delta * R) - nu * C2 / Delta - sp.diff(n, rho)**2 / R)
        ell = l0 + sum(self.coefficient(ell_rho, (rho,), rho**j) * rho**(j + 1) / (j + 1)
                       for j in range(3))
        self.zero(sp.diff(ell, rho) - ell_rho)
        _, _, H = self.potentials(q, rho, U, V, k, n, ell, m)
        Ccal = -R * ell_rho - sp.diff(n, rho)**2
        P = -(Delta * U**2 + Bcal * U + Ccal) / (R * nu)
        remainder = sp.expand(H - R * nu * (V - P)**2 / 2)
        self.zero(sp.diff(remainder, V))
        raw_u3 = self.coefficient(remainder, (U, V), U**3)
        expected_u3 = (q**3 * sp.diff(k0, q, 3) - 6 * q**2 * sp.diff(k0, q, 2)
                       + 6 * q * sp.diff(k0, q) - 9 * q * sp.diff(s0, q) + 15 * s0) / (48 * q**5)
        self.zero(raw_u3 - expected_u3)
        B1 = self.coefficient(remainder, (U, V), U)
        h0 = k0 + s0
        self.zero(self.coefficient(B1, (rho,), rho**3))
        self.zero(self.coefficient(B1, (rho,), rho**2)
                  - (q**2 * sp.diff(h0, q, 3) + 2 * q * sp.diff(h0, q, 2)
                     - 2 * sp.diff(h0, q)) / 12)
        self.zero(self.coefficient(ell_rho, (rho,), rho)
                  - 3 * s0 - (q * sp.diff(h0, q) - q**2 * sp.diff(h0, q, 2)) / 3)
        bare_B1 = B1.subs({k0: 0, s0: 0}).doit()
        self.zero(self.coefficient(bare_B1, (rho,), rho)
                  - (q**2 * sp.diff(n0, q, 3) - q * sp.diff(n0, q, 2)) / 6)

        A0, A2, a, K1, K3, K5, N0, N1, N3 = sp.symbols("A0 A2 a K1 K3 K5 N0 N1 N3")
        hsol = A0 + A2 * q**2 + a / q
        ksol = A0 + A2 * q**2 + a / (2 * q) + K1 * q + K3 * q**3 + K5 * q**5
        ssol = a / (2 * q) - K1 * q - K3 * q**3 - K5 * q**5
        self.zero(hsol - ksol - ssol)
        self.zero(q**2 * sp.diff(hsol, q, 3) + 2 * q * sp.diff(hsol, q, 2) - 2 * sp.diff(hsol, q))
        self.zero(q**3 * sp.diff(ksol, q, 3) - 6 * q**2 * sp.diff(ksol, q, 2)
                  + 6 * q * sp.diff(ksol, q) - 9 * q * sp.diff(ssol, q) + 15 * ssol)
        nsol = N3 * q**3 + N1 * q + N0
        self.zero(q**2 * sp.diff(nsol, q, 3) - q * sp.diff(nsol, q, 2))
        # These solution identities do not replace the written exact-field
        # spectral-projection and primitive-subtraction completeness arguments.

    def test_actual_shears_both_orders_and_literal_chart_columns(self):
        X, Y, Z, W, X1, Y1, Z1, W1 = sp.symbols("X Y Z W X1 Y1 Z1 W1")
        beta0, A0, A2, a, K1, K3, K5, N0, N1, N3 = sp.symbols("beta0 A0 A2 a K1 K3 K5 N0 N1 N3")
        old, new = (X, Y, Z, W), (X1, Y1, Z1, W1)
        P2 = lambda x, y: K1 * x**2 + K3 * x * y + K5 * y**2
        stages = (
            ((X, Y, Z, W / beta0), (X1, Y1, Z1, beta0 * W1)),
            ((X, Y, Z - A0 * X - A2 * Y, W + P2(X, Y)),
             (X1, Y1, Z1 + A0 * X1 + A2 * Y1, W1 - P2(X1, Y1))),
            ((X, Y + a, Z, W), (X1, Y1 - a, Z1, W1)),
            ((X, Y, Z - N0, W + N1 * X + N3 * Y),
             (X1, Y1, Z1 + N0, W1 - N1 * X1 - N3 * Y1)),
        )
        for forward, inverse in stages:
            for expression, target in zip(inverse, old):
                self.zero(expression.subs(dict(zip(new, forward)), simultaneous=True) - target)
            for expression, target in zip(forward, new):
                self.zero(expression.subs(dict(zip(old, inverse)), simultaneous=True) - target)
            for entry, expected in zip(inverse, (0, 0, 1, 0)):
                self.zero(sp.diff(entry, Z1) - expected)

        q, rho, rho1, y, y2, z, theta, w, n0 = sp.symbols("q rho rho1 y y2 z theta w n0")
        P = K1 + K3 * q**2 + K5 * q**4
        dt = lambda expression: sp.diff(expression, q) / (2 * q)
        Q = -1 / (8 * q**3)
        k0 = A0 + A2 * q**2 + a / (2 * q) + q * P
        s0 = a / (2 * q) - q * P
        k = q * rho + k0
        n = -q * rho**2 / 2 + s0 * rho + n0
        Ychart = y + q**2 * X
        Zchart = z + (y / (2 * q) + k) * X + q * X**2
        Wchart = w + theta * X + rho * X**2
        self.zero(Zchart - A0 * X - A2 * Ychart
                  - (z - A2 * y + (y / (2 * q) + q * (rho + P) + a / (2 * q)) * X + q * X**2))
        self.zero(Wchart + P2(X, Ychart)
                  - (w + K5 * y**2 + (theta + dt(P) * y) * X + (rho + P) * X**2))
        k1 = q * rho1 + a / (2 * q)
        n1 = n.subs(rho, rho1 - P)
        nbar = n0 - s0 * P - q * P**2 / 2
        self.zero(n1 + q * rho1**2 / 2 - a * rho1 / (2 * q) - nbar)
        old_second = Q * y**2 + dt(k) * y + q * theta + n
        new_second = Q * y**2 + dt(k1) * y + q * (theta + dt(P) * y) + n1
        self.zero(new_second.subs(rho1, rho + P) - (old_second - A2 * y))
        n2 = n1 - a * rho1 / (2 * q) + a**2 / (8 * q**3)
        self.zero(Q * (y2 - a)**2 + dt(k1) * (y2 - a) + q * theta + n1
                  - (Q * y2**2 + dt(q * rho1) * y2 + q * theta + n2))
        self.zero(k1 - a / (2 * q) - q * rho1)
        self.zero((-q * rho1**2 / 2 + N3 * q**3 + N1 * q + N0)
                  - q * (N1 + N3 * q**2) - N0 + q * rho1**2 / 2)
        # Full initial-ideal and exact-degree preservation need the written
        # actual hypotheses, beyond these inverse/column identities.

    def test_normalized_graph_potentials_scalar_and_original_square(self):
        q, rho, U, V, m, y, X = sp.symbols("q rho U V m y X")
        l = sp.Function("l")(q)
        k, n = q * rho, -q * rho**2 / 2
        ell = -q * rho**3 / 2 + l
        S, _, H = self.potentials(q, rho, U, V, k, n, ell, m)
        P = rho**2 / 2 + rho * U / (2 * q**2) - 3 * U**2 / (8 * q**4)
        target = (-q**2 * (V - P)**2 / 2 + (l / q - sp.diff(l, q)) * U / 2
                  + 5 * q**2 * rho**4 / 8 - q * rho * l - q * m)
        self.zero(H - target)
        C = sp.symbols("C")
        gamma = sp.Function("gamma")(q, rho)
        a = y / (2 * q**2) - rho
        z = q * gamma - y * a / q
        w = C + y * a**2 / (2 * q**2) - a * gamma
        theta = P.subs(U, y) + gamma
        graph_ell = -q * rho**3 / 2 + C * q
        self.zero((graph_ell - S.subs({U: y, V: theta}, simultaneous=True)) / q - w)
        self.zero(-y**2 / (8 * q**3) + rho * y / (2 * q) + q * theta - q * rho**2 / 2 - z)
        scalar_m = q * (5 * rho**4 / 8 - C * rho - gamma**2 / 2)
        self.zero(target.subs({l: C * q}).doit().subs({U: y, V: theta, m: scalar_m}, simultaneous=True))
        determinant = sp.Matrix([y, z, w]).jacobian([q, rho, y]).det()
        self.zero(determinant - gamma * (gamma + q * sp.diff(gamma, q)
                  + rho * sp.diff(gamma, rho) - 3 * y * sp.diff(gamma, rho) / (2 * q**2)))
        self.zero(z**2 - 2 * y * (w - C) - q**2 * gamma**2)
        Ychart = y + q**2 * X
        Zchart = z + (y / (2 * q) + q * rho) * X + q * X**2
        Wchart = w + theta * X + rho * X**2
        self.zero(Zchart**2 - X**3 * Ychart - 2 * Ychart * (Wchart - C) - q**2 * gamma**2)
        b = sp.symbols("b")
        self.zero((b**2).subs(b, -b) - b**2)
        self.assertNotEqual(-b, b)
        # The involution is an algebra control, not a proof of actual field
        # equality. The normality/irreducibility argument is also not tested.

    def test_quadratic_scalar_laurent_and_field_containment_identities(self):
        q, rho, zeta, y, yq, yr, yz, g0, gp = sp.symbols("q rho zeta y yq yr yz g0 gp")
        h_over_q = rho / q - y / (2 * q**3)
        z = q * zeta + y * h_over_q
        w = h_over_q * z - y * h_over_q**2 / 2 + g0
        columns = ((q, yq, gp), (rho, yr, 0), (zeta, yz, 0))
        raw = sp.Matrix([[sp.diff(entry, variable) + sp.diff(entry, y) * yjet
                          + sp.diff(entry, g0) * gjet
                          for variable, yjet, gjet in columns] for entry in (y, z, w)]).det()
        reduced = (q * gp * yr - zeta * (q * yq + (rho - 3 * y / (2 * q**2)) * yr)
                   + yz * (zeta**2 - y * gp / q))
        self.zero(raw - reduced)
        g = sp.Function("g")(q)
        offset = sp.Function("offset")(q, rho)
        g1 = sp.diff(g, q)
        yvalue = -q * zeta**2 / g1 + offset
        evaluated = reduced.subs({y: yvalue, yq: sp.diff(yvalue, q),
                                 yr: sp.diff(yvalue, rho), yz: sp.diff(yvalue, zeta),
                                 gp: g1}, simultaneous=True)
        cubic = -(2 * q**3 * sp.diff(g, q, 2) + 6 * q**2 * g1
                  + 3 * sp.diff(offset, rho) * g1) / (2 * q * g1**2)
        linear = -(2 * q**3 * sp.diff(offset, q) + 2 * q**2 * rho * sp.diff(offset, rho)
                   - 4 * q**2 * offset - 3 * offset * sp.diff(offset, rho)) / (2 * q**2)
        self.zero(evaluated - cubic * zeta**3 - linear * zeta - q * sp.diff(offset, rho) * g1)
        slope = -2 * q**2 * (q * sp.diff(g, q, 2) / g1 + 3) / 3
        ode = q**2 * sp.diff(g, q, 3) + 8 * q * sp.diff(g, q, 2) + 12 * g1
        self.zero(2 * q**3 * sp.diff(slope, q) - 2 * q**2 * slope - 3 * slope**2
                  + 4 * q**4 * ode / (3 * g1))
        alpha_extract = -q**3 * (q * sp.diff(g, q, 2) + 4 * g1) / 2
        beta_extract = q**4 * (q * sp.diff(g, q, 2) + 3 * g1) / 3
        self.zero(sp.diff(alpha_extract, q) + q**2 * ode / 2)
        self.zero(sp.diff(beta_extract, q) - q**3 * ode / 3)

        alpha, beta, gamma, delta, xi = sp.symbols("alpha beta gamma delta xi")
        gsol = alpha / q**2 + beta / q**3 + gamma
        asol = 2 * beta * q**2 / (2 * alpha * q + 3 * beta)
        bsol = delta * q**3 / (2 * alpha * q + 3 * beta)
        self.zero(ode.subs(g, gsol).doit())
        self.zero(alpha_extract.subs(g, gsol).doit() - alpha)
        self.zero(beta_extract.subs(g, gsol).doit() - beta)
        self.zero(2 * q**3 * sp.diff(asol, q) - 2 * q**2 * asol - 3 * asol**2)
        self.zero(2 * q**3 * sp.diff(bsol, q) - 4 * q**2 * bsol - 3 * asol * bsol)
        rho_value = ((2 * alpha * q + 3 * beta) * y - q**3 * xi**2 - delta * q**3) / (2 * beta * q**2)
        self.zero(-q * (xi / q)**2 / sp.diff(gsol, q) + asol * rho_value + bsol - y)
        T = alpha / q**2 + beta / q**3
        calP = (T * y - (xi**2 + delta) / 2) / beta
        self.zero(rho_value / q - y / (2 * q**3) - calP)
        z_actual = q * (xi / q) + y * (rho_value - y / (2 * q**2)) / q
        w_actual = (rho_value - y / (2 * q**2)) * (xi / q) + y * (rho_value - y / (2 * q**2))**2 / (2 * q**2) + gsol
        self.zero(z_actual - (xi + y * calP))
        self.zero(w_actual - (xi * calP + y * calP**2 / 2 + T + gamma))
        p, S = sp.symbols("p S")
        cubic_polynomial = beta * p**3 + alpha * p**2 - S
        self.assertEqual(sp.Poly(cubic_polynomial, p).degree(), 3)
        self.zero(cubic_polynomial.subs({p: 1 / q, S: T}, simultaneous=True))
        # Degree as a polynomial is finite algebra. Irreducibility, K=C(T),
        # and the actual degree-three contradiction remain written proof steps.


if __name__ == "__main__":
    unittest.main()
