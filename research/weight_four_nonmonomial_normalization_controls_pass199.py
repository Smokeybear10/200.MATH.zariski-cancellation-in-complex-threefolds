"""Finite identities for nonmonomial square-root normalization199.

These controls start from raw coefficient derivatives and actual polynomial
maps. They do not prove exact-field constant arguments, completeness of the
Wronskian basis, whole-line or field return, actualness, or recognition.
No proof solver, older checker, or earlier implementation is imported.
"""

import unittest

import sympy as sp


class NonmonomialNormalizationControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def lower_coefficients(self, q, k0, s0, n0, dt):
        """Extract the needed rho coefficients before any lower-gate substitution."""
        R = 1 / (q * (q + 1))
        nu = 1 / (q**3 * (q + 1)**3 * (3 * q - 1))
        Rp = sp.factor(dt(R))
        Rpp = sp.factor(dt(Rp))
        vp = sp.factor(dt(nu))
        vpp = sp.factor(dt(vp))
        Delta = sp.factor(R * Rpp / 2 - Rp**2)
        d = 1 / (16 * q**5)
        # B=[V U]H and C2=[U^2]H at V=0, in ascending rho degree.
        b1 = sp.factor(R * vp - 2 * Rp * nu)
        b0 = sp.factor(R * dt(s0) - 2 * Rp * s0)
        c2 = sp.factor(R * vpp / 4 - Rp * vp / 2 - nu * Rpp / 2)
        c1 = sp.factor(R * dt(dt(s0)) / 2 - Rp * dt(s0)
                       - (nu * dt(dt(k0)) + s0 * Rpp) / 2)
        c0 = sp.factor(R * dt(dt(n0)) / 2 - Rp * dt(n0)
                       - s0 * dt(dt(k0)) / 2)
        # Coefficients of ell_rho follow from completing the literal V-square.
        a2 = sp.factor(b1**2 / (2 * Delta * R) - nu * c2 / Delta - nu**2 / R)
        a1 = sp.factor(b1 * b0 / (Delta * R) - nu * c1 / Delta - 2 * nu * s0 / R)
        a0 = sp.factor(b0**2 / (2 * Delta * R) - nu * c0 / Delta - s0**2 / R)
        C2 = -R * a2 - nu**2
        C1 = -R * a1 - 2 * nu * s0
        C0 = -R * a0 - s0**2
        U3_constant = sp.factor(R * dt(dt(dt(k0))) / 6
                                - Rp * dt(dt(k0)) / 2 - d * s0
                                - Delta * b0 / (R * nu))
        U3_rho = sp.factor(R * dt(Rpp) / 6 - Rp * Rpp / 2
                           - d * nu - Delta * b1 / (R * nu))
        B1_rho3 = sp.factor(-R * dt(a2 / 3) + Rp * a2 / 3
                            - nu * vp / 2 - b1 * C2 / (R * nu))
        B1_rho2 = sp.factor(-R * dt(a1 / 2) + Rp * a1 / 2
                            - nu * dt(s0) - s0 * vp / 2
                            - (b1 * C1 + b0 * C2) / (R * nu))
        B1_rho1 = sp.factor(-R * dt(a0) + Rp * a0
                            - nu * dt(n0) - s0 * dt(s0)
                            - (b1 * C0 + b0 * C1) / (R * nu))
        return (U3_constant, U3_rho, B1_rho3, B1_rho2, B1_rho1, a2 / 3)

    def test_raw_linear_gates_and_exact_rational_basis(self):
        q = sp.symbols("q")
        k = sp.symbols("k0:6")
        s = sp.symbols("s0:4")
        n = sp.symbols("n0:4")
        chains = list(zip(k, k[1:])) + list(zip(s, s[1:])) + list(zip(n, n[1:]))

        def dq(expression):
            return sp.diff(expression, q) + sum(
                sp.diff(expression, slot) * successor for slot, successor in chains
            )

        def dt(expression):
            return dq(expression) / (2 * q)

        U3, U3rho, B3, B2, _, _ = self.lower_coefficients(q, k[0], s[0], n[0], dt)
        A = q * (q + 1)**2 * (3 * q - 1)
        raw_U3 = (q * (q + 1) * k[3] + 3 * q * k[2] - 3 * k[1]
                  - 3 * dq(A * s[0])) / (48 * q**5 * (q + 1)**2)
        raw_B2 = (dq(dq(dq(q * A * s[0]))) - k[3]) / (
            4 * q**4 * (q + 1)**4 * (3 * q - 1)**2
        )
        self.zero(U3 - raw_U3)
        self.zero(U3rho)
        self.zero(B3)
        self.zero(B2 - raw_B2)
        primitive = q * (q + 1) * k[2] + (q - 1) * k[1] - 4 * k[0]
        self.zero(dq(primitive) - q * (q + 1) * k[3] - 3 * q * k[2] + 3 * k[1])

        def operator(expression):
            return (q**2 * (q + 1) * sp.diff(expression, q, 2)
                    + q * (q - 1) * sp.diff(expression, q)
                    - (4 * q + 3) * expression)

        R = 1 / (q * (q + 1))
        for expression, expected in (
            (R, 0), (q**4 * R, 0), (1, -4 * q - 3),
            (q**2, -3 * q**2), (q**2 * R, -4 * q),
        ):
            self.zero(operator(expression) - expected)
        wronskian = R * sp.diff(q**4 * R, q) - sp.diff(R, q) * q**4 * R
        self.zero(wronskian - 4 * q**3 * R**2)
        self.assertNotEqual(sp.cancel(wronskian), 0)
        # The constant-field proof, not this finite basis check, establishes
        # completeness among algebraic solutions in every allowed K.

    def test_last_rho_gate_primitive_and_bare_scalar(self):
        q, C, N0, N1, N2 = sp.symbols("q C N0 N1 N2")
        n = sp.symbols("n0:4")

        def dq(expression):
            return sp.diff(expression, q) + sum(
                sp.diff(expression, slot) * successor for slot, successor in zip(n, n[1:])
            )

        def dt(expression):
            return dq(expression) / (2 * q)

        R = 1 / (q * (q + 1))
        A = q * (q + 1)**2 * (3 * q - 1)
        _, _, _, _, B1, _ = self.lower_coefficients(q, 0, C / A, n[0], dt)
        grouped = ((3 * q - 1)**4 * dq(dq(dq(q * (q + 1) * n[0]))) + 9 * C**2) / (
            2 * q**3 * (q + 1)**3 * (3 * q - 1)**5
        )
        self.zero(B1 - grouped)
        self.zero(sp.diff(1 / (3 * q - 1), q, 3) + 162 / (3 * q - 1)**4)
        n_solution = R * (C**2 / (18 * (3 * q - 1)) + N0 + N1 * q + N2 * q**2)
        self.zero(sp.diff(q * (q + 1) * n_solution, q, 3)
                  + 9 * C**2 / (3 * q - 1)**4)
        self.zero(n_solution - N1 - R * (N0 + (N2 - N1) * q**2)
                  - R * C**2 / (18 * (3 * q - 1)))
        ordinary_dt = lambda expression: sp.diff(expression, q) / (2 * q)
        U3, U3rho, B3, B2, B1, L3 = self.lower_coefficients(q, 0, 0, 0, ordinary_dt)
        for residual in (U3, U3rho, B3, B2, B1):
            self.zero(residual)
        expected_L3 = -(q**2 + 4 * q - 1) / (
            2 * q**5 * (q + 1)**5 * (3 * q - 1)**3
        )
        self.zero(L3 - expected_L3)
        ell0 = sp.Function("ell0")(q)
        bare_B1 = -R * ordinary_dt(ell0) + ordinary_dt(R) * ell0
        self.zero(bare_B1 + R**2 * ordinary_dt(ell0 / R))
        lam = sp.symbols("lam")
        self.zero(bare_B1.subs(ell0, lam * R).doit())

    def test_actual_scaling_shears_columns_and_both_inverse_orders(self):
        X, Y, Z, W = slots = sp.symbols("X Y Z W")
        a, b, tau, C = sp.symbols("a b tau C")
        c, e = a / b, a**2 / b**3
        q, rho, y, theta = sp.symbols("q rho y theta")
        kappa0, kappa2, p0, p1, p2 = sp.symbols("kappa0 kappa2 p0 p1 p2")
        N0, N1, N2, lam = sp.symbols("N0 N1 N2 lam")
        self.zero(e / c * (a * (q / c)**2 + b * q / c) - q * (q + 1))
        old_q = q / c
        old_R = 1 / (old_q * (a * old_q + b))
        old_nu = b**2 / (old_q**3 * (a * old_q + b)**3 * (3 * a * old_q - b))
        self.zero(c * old_R / e - 1 / (q * (q + 1)))
        self.zero(c * old_nu / e**2 - 1 / (q**3 * (q + 1)**3 * (3 * q - 1)))
        P2 = p0 * X**2 + p1 * X * Y + p2 * Y**2
        pairs = [
            ((X, c**2 * Y, c * Z, e * W), (X, Y / c**2, Z / c, W / e), 1 / c),
            ((X, Y, Z - kappa0 * X - kappa2 * Y, W + P2),
             (X, Y, Z + kappa0 * X + kappa2 * Y, W - P2), 1),
            ((X, Y, Z - N1, W + N0 * X + (N2 - N1) * Y),
             (X, Y, Z + N1, W - N0 * X - (N2 - N1) * Y), 1),
            ((X + tau, Y, Z + 3 * tau * Y / 2,
              W + 3 * tau * (Y**2 - (X + tau) * Y) / 2),
             (X - tau, Y, Z - 3 * tau * Y / 2,
              W - 3 * tau * (Y**2 - X * Y) / 2), 1),
            ((X, Y, Z + C**2 / 6, W - C**2 * X / 18 + 7 * C**2 * Y / 6),
             (X, Y, Z - C**2 / 6, W + C**2 * X / 18 - 7 * C**2 * Y / 6), 1),
            ((X, Y, Z, W - lam), (X, Y, Z, W + lam), 1),
        ]
        for forward, inverse, selected_scale in pairs:
            for outer, inner in ((forward, inverse), (inverse, forward)):
                substitution = dict(zip(slots, inner))
                for expression, expected in zip(outer, slots):
                    self.zero(expression.subs(substitution, simultaneous=True) - expected)
            for index in (0, 1, 3):
                self.zero(sp.diff(inverse[index], Z))
            self.zero(sp.diff(inverse[2], Z) - selected_scale)

        R = 1 / (q * (q + 1))
        nu = 1 / (q**3 * (q + 1)**3 * (3 * q - 1))
        A = q * (q + 1)**2 * (3 * q - 1)
        Q = -1 / (8 * q**3)
        dt = lambda expression: sp.diff(expression, q) / (2 * q)
        P = p0 + p1 * q**2 + p2 * q**4
        k0 = kappa0 + kappa2 * q**2 + R * P
        slow, nlow = sp.symbols("slow nlow")
        k = R * rho + k0
        n = nu * rho**2 / 2 + slow * rho + nlow
        z = Q * y**2 + dt(k) * y + R * theta + n
        shifted_rho, shifted_theta = rho + P, theta + dt(P) * y
        shifted_z = z - kappa2 * y
        self.zero(k - kappa0 - kappa2 * q**2 - R * shifted_rho)
        self.zero(shifted_z - Q * y**2 - dt(R) * shifted_rho * y
                  - R * shifted_theta - n)

        n = nu * rho**2 / 2 + C * rho / A + R * C**2 / (18 * (3 * q - 1))
        z = Q * y**2 + dt(R) * rho * y + R * theta + n
        sigma = y / (2 * q) + R * rho
        Pt = 3 * tau * (q**4 - q**2) / 2
        yn, rn = y - tau * q**2, rho + Pt
        tn = theta - 2 * tau * rho + dt(Pt) * yn
        zn = z - tau * sigma + tau**2 * q + 3 * tau * yn / 2
        nnew = zn - Q * yn**2 - dt(R) * rn * yn - R * tn
        correction = (-9 * C * tau * q**2 + 6 * C * tau * q + 2 * C * tau
                      + 9 * tau**2 * q**2 + 3 * tau**2 * q + tau**2) / 18
        expected = (nu * rn**2 / 2 + (C + tau) * rn / A
                    + R * ((C + tau)**2 / (18 * (3 * q - 1)) + correction))
        self.zero(nnew - expected)
        self.zero(R * Pt + 3 * tau * q / 2 - 3 * tau * q**2 / 2)
        self.zero(correction.subs(tau, -C) - C**2 * (q**2 - q / 6 - sp.Rational(1, 18)))
        self.zero(R * correction.subs(tau, -C) + C**2 / 6
                  - R * (-C**2 / 18 + 7 * C**2 * q**2 / 6))


if __name__ == "__main__":
    unittest.main()
