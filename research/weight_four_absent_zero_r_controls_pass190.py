"""Finite exact controls for the absent-variable zero-R return in pass190.

These independent symbolic identities check the residual scalar equations,
the coefficient derivatives used by the pencil argument, and literal
transport to an original-coordinate shear with both polynomial inverse
orders. They do not prove exact field return, the pencil-degree lemma,
constant-field descent, or the published recognition theorem. The chart
expressions below are formal coefficient data, not new actual dense frames.
Only the displayed triangular coordinate map has its actual inverse checked.
No earlier checker or solver implementation is imported.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


class AbsentZeroRReturnControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_unrestricted_integral_and_residual_coefficients(self):
        t, n, U = sp.symbols("t n U")
        b = sp.symbols("b", nonzero=True)
        h, c = (sp.Function(name)(t) for name in ("h", "c"))
        M1, M0 = (sp.Function(name)(t) for name in ("M1", "M0"))
        W0 = sp.Function("W0")(t, n)
        F = 4 * t * U**3 + h * U**2
        rho = b * n + c
        P = sp.diff(c, t) * U - b * F + M1 * n + M0

        def delta(expression):
            return sp.diff(expression, t) - sp.diff(F, U) * sp.diff(expression, n)

        W = (-b * U**4 - b * sp.diff(h, t) * U**3 / 3
             + sp.diff(c, t, 2) * U**2 / 2
             + (sp.diff(M1, t) * n + sp.diff(M0, t)) * U
             - M1 * F + W0)
        self.zero(sp.diff(W, U) - delta(P))
        self.zero(delta(rho) - sp.diff(P, U))
        residual = sp.expand(delta(W))
        expected = (
            (-b * sp.diff(h, t, 2) / 3 - 4 * M1 - 16 * t * sp.diff(M1, t)) * U**3
            + (sp.diff(c, t, 3) / 2 - sp.diff(h, t) * M1
               - 3 * h * sp.diff(M1, t) - 12 * t * sp.diff(W0, n)) * U**2
            + (sp.diff(M1, t, 2) * n + sp.diff(M0, t, 2)
               - 2 * h * sp.diff(W0, n)) * U
            + sp.diff(W0, t)
        )
        self.zero(residual - expected)
        self.assertEqual(sp.Poly(W, U).degree(), 4)
        self.zero(sp.expand(W).coeff(U, 4) + b)
        self.zero(residual.coeff(U, 4))

        D, g0 = (sp.Function(name)(t) for name in ("D", "g0"))
        W_linear = W - W0 + D * n + g0
        linear_residual = sp.expand(delta(W_linear))
        D_forced = (sp.diff(c, t, 3) / (24 * t)
                    - sp.diff(h, t) * M1 / (12 * t)
                    - h * sp.diff(M1, t) / (4 * t))
        self.zero(linear_residual.coeff(U, 2).subs(D, D_forced))
        self.zero(linear_residual.coeff(U, 1) - (
            sp.diff(M1, t, 2) * n + sp.diff(M0, t, 2) - 2 * h * D
        ))
        # Scalarity in U alone does NOT force D'=0: this is an element of K(n).
        self.zero(linear_residual.coeff(U, 0) - sp.diff(D, t) * n - sp.diff(g0, t))

    def test_normal_form_and_pencil_derivative_gates(self):
        t, y, z = sp.symbols("t y z")
        b = sp.symbols("b", nonzero=True)
        A, B, C, H0, E0, F0 = sp.symbols("A B C H0 E0 F0")
        D, G2, G1, C1, C0, M00 = sp.symbols("D G2 G1 C1 C0 M00")
        M1 = A * t + B
        h = -10 * A * t**3 / b - 6 * B * t**2 / b + C * t + H0
        k = -A * t**5 / b - B * t**4 / b + C * t**3 / 3 + H0 * t**2 + E0 * t + F0
        c = (-A**2 * t**6 / b - 2 * A * B * t**5 / b
             + (A * C / 3 - B**2 / b + D) * t**4
             + (A * H0 + B * C / 3) * t**3
             + (B * H0 + A * E0 + G2) * t**2 + C1 * t + C0)
        M0 = D * k + G1 * t + M00
        self.zero(sp.diff(k, t, 2) - 2 * h)
        self.zero(16 * t * sp.diff(M1, t) + 4 * M1 + b * sp.diff(h, t, 2) / 3)
        self.zero(sp.diff(M1, t, 2))
        self.zero(sp.diff(c, t, 3) / 2 - sp.diff(h, t) * M1
                  - 3 * h * sp.diff(M1, t) - 12 * t * D)
        self.zero(sp.diff(M0, t, 2) - 2 * h * D)
        g3 = -b * sp.diff(h, t) / 3 - 10 * A * t**2 - 4 * B * t
        g2 = sp.diff(c, t, 2) / 2 - h * M1 - A * sp.diff(k, t) - 6 * t**2 * D
        g1 = sp.diff(M0, t) - D * sp.diff(k, t)
        self.zero(g3 + b * C / 3)
        self.zero(g2 - G2)
        self.zero(g1 - G1)

        # Independent unrestricted first jets before proving D constant.
        h0, h1, k1, k2, c2, c3, D0, D1, m01, m02 = sp.symbols(
            "h0 h1 k1 k2 c2 c3 D0 D1 m01 m02"
        )
        jet_step = {h0: h1, k1: k2, c2: c3, D0: D1, m01: m02}

        def Dt(expression):
            return sp.diff(expression, t) + sum(
                sp.diff(expression, variable) * derivative
                for variable, derivative in jet_step.items()
            )

        g2_jet = c2 / 2 - h0 * M1 - A * k1 - 6 * t**2 * D0
        g1_jet = m01 - D0 * k1
        prior = {k2: 2 * h0, c3: 24 * t * D0 + 2 * h1 * M1 + 6 * h0 * A,
                 m02: 2 * h0 * D0}
        self.zero((Dt(g2_jet) + 6 * t**2 * D1).subs(prior, simultaneous=True))
        self.zero((Dt(g1_jet) + k1 * D1).subs(prior, simultaneous=True))

        # Synthetic proper-degree pencil. It illustrates why coefficient
        # differential identities alone are not the actual field equality.
        S, V = sp.symbols("S V")
        slope, intercept = t, -2 * t**3 * y**2
        relation = V + 2 * y**2 * S**3
        pencil = sp.expand(relation.subs(V, V - z * S))
        self.zero(relation.subs({S: slope, V: intercept}, simultaneous=True))
        self.zero(sp.diff(-2 * t**3, t) + 6 * t**2 * sp.diff(slope, t))
        self.assertEqual(sp.Poly(pencil, S).degree(), 3)
        self.zero(pencil.coeff(S, 3) - 2 * y**2)
        # Irreducibility and exact field index use the written pencil lemma.

    def test_literal_transport_and_both_coordinate_inverse_orders(self):
        X, y, t, n, g0, g0_prime = sp.symbols("X y t n g0 g0_prime")
        Y, Z, W, I = sp.symbols("Y Z W I")
        b = sp.symbols("b", nonzero=True)
        A, B, C, H0, E0, F0 = sp.symbols("A B C H0 E0 F0")
        D, G2, G1, C1, C0, M00 = sp.symbols("D G2 G1 C1 C0 M00")
        M1 = A * t + B
        k = -A * t**5 / b - B * t**4 / b + C * t**3 / 3 + H0 * t**2 + E0 * t + F0
        h = sp.diff(k, t, 2) / 2
        c = (-A**2 * t**6 / b - 2 * A * B * t**5 / b
             + (A * C / 3 - B**2 / b + D) * t**4
             + (A * H0 + B * C / 3) * t**3
             + (B * H0 + A * E0 + G2) * t**2 + C1 * t + C0)
        M0 = D * k + G1 * t + M00
        rho = b * n + c
        F = 4 * t * y**3 + h * y**2
        theta = sp.diff(c, t) * y - b * F + M1 * n + M0
        z = n + 6 * t**2 * y**2 + sp.diff(k, t) * y
        w = (-b * y**4 - b * sp.diff(h, t) * y**3 / 3
             + sp.diff(c, t, 2) * y**2 / 2
             + (sp.diff(M1, t) * n + sp.diff(M0, t)) * y
             - M1 * F + D * n + g0)
        Y_chart = y + t * X
        Z_chart = z + (4 * t**3 * y + k) * X + t**4 * X**2
        W_chart = w + theta * X + rho * X**2

        def T(expression):
            return (sp.diff(expression, t) - X * sp.diff(expression, y)
                    - sp.diff(F, y) * sp.diff(expression, n)
                    + g0_prime * sp.diff(expression, g0))

        self.zero(T(X))
        self.zero(T(Y_chart))
        self.zero(T(Z_chart))
        self.zero(T(W_chart) - g0_prime)
        A0 = b * X**2 + B * X + A * Y + D
        G = -b * Y**4 - b * C * Y**3 / 3 + G2 * Y**2 + G1 * Y
        Q0 = (G + X * (-b * H0 * Y**2 + (C1 - B * E0 - A * F0) * Y + M00)
              + X**2 * (C0 - b * E0 * Y - B * F0) - b * F0 * X**3)
        A0_chart, Q0_chart = A0.subs(Y, Y_chart), Q0.subs(Y, Y_chart)
        self.zero(sp.diff(W_chart, n) - A0_chart)
        self.zero(sp.diff(Z_chart, n) - 1)
        self.zero(W_chart - A0_chart * Z_chart - Q0_chart - g0)
        Q_chart = sp.expand(W_chart - A0_chart * Z_chart - g0)
        self.zero(sp.diff(Q_chart, n))
        self.zero(sp.diff(Q_chart, t) - X * sp.diff(Q_chart, y))
        self.zero(Q_chart.subs(y, Y - t * X) - Q0)

        # This is an actual polynomial automorphism for every displayed
        # constant choice, including zero A, B, D and all lower constants.
        # The generic coefficient chart above is not a new realized frame.
        forward = (X, Y, Z, W - A0 * Z - Q0)
        inverse = (X, Y, Z, I + A0 * Z + Q0)
        for expression, expected in zip(forward, (X, Y, Z, I)):
            self.zero(expression.subs(W, inverse[3]) - expected)
        for expression, expected in zip(inverse, (X, Y, Z, W)):
            self.zero(expression.subs(I, forward[3]) - expected)


if __name__ == "__main__":
    unittest.main()
