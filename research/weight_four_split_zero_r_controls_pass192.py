"""Independent finite identities for the split zero-R recognition192.

The coefficient recurrence is checked with an unrestricted d(t), before
specializing the split ratio. The later controls retain D' until the written
field-pencil proof forces it to vanish. A fully symbolic Laurent-coefficient
fixture checks literal original-chart transport and both polynomial inverse
orders. This fixture is not asserted to be an actual globally sliced frame.
No finite calculation proves exact field return, the regular-differential
obstruction, curve degree, constant-field descent, or the recognition theorem.
No previous checker is imported. Authored source-only; Root owns execution.
"""

import unittest

import sympy as sp


class SplitZeroRRecognitionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_general_cover_integral_and_field_return_coefficients(self):
        t, n, U = sp.symbols("t n U")
        a, b, c, d, h = (sp.Function(name)(t) for name in ("a", "b", "c", "d", "h"))
        M, W0 = sp.Function("M")(t, n), sp.Function("W0")(t, n)
        rho, eta = a * n**2 + b * n + c, 2 * a * n + b
        F = d * U**3 + h * U**2

        def delta(expression):
            return sp.diff(expression, t) - sp.diff(F, U) * sp.diff(expression, n)

        def integral(M_expr, W0_expr):
            return (a * F**2 - sp.diff(eta, t) * U * F
                    - eta * (sp.diff(d, t) * U**4 / 4 + sp.diff(h, t) * U**3 / 3)
                    + sp.diff(rho, t, 2) * U**2 / 2
                    + sp.diff(M_expr, t) * U - sp.diff(M_expr, n) * F + W0_expr)

        P = sp.diff(rho, t) * U - eta * F + M
        W = integral(M, W0)
        self.zero(sp.diff(W, U) - delta(P))
        self.zero(delta(rho) - sp.diff(P, U))
        residual = sp.expand(delta(W))
        expected6 = sp.Rational(7, 2) * d * (a * sp.diff(d, t) + 2 * d * sp.diff(a, t))
        expected5 = (12 * sp.diff(a, t) * d * h + 3 * a * sp.diff(d, t) * h
                     + 4 * a * d * sp.diff(h, t) + 3 * d**2 * sp.diff(M, n, 2))
        self.zero(residual.coeff(U, 6) - expected6)
        self.zero(residual.coeff(U, 5) - expected5)
        self.assertLessEqual(sp.Poly(residual, U).degree(), 6)
        mu_forced = a * h * sp.diff(d, t) / d**2 - 4 * a * sp.diff(h, t) / (3 * d)
        self.zero(expected5.subs({
            sp.diff(a, t): -a * sp.diff(d, t) / (2 * d),
            sp.diff(M, n, 2): mu_forced,
        }, simultaneous=True))

        mu, M1, M0, g0 = (sp.Function(name)(t) for name in ("mu", "M1", "M0", "g0"))
        M_quad = mu * n**2 / 2 + M1 * n + M0
        W_quad = integral(M_quad, W0)
        rhs2 = (sp.diff(a, t, 3) * n**2 / 2
                + (sp.diff(b, t, 3) / 2 - sp.diff(h, t) * mu
                   - 3 * h * sp.diff(mu, t)) * n
                + sp.diff(c, t, 3) / 2 - sp.diff(h, t) * M1
                - 3 * h * sp.diff(M1, t))
        self.zero(sp.expand(delta(W_quad)).coeff(U, 2) - rhs2 + 3 * d * sp.diff(W0, n))
        W0_poly = (sp.diff(a, t, 3) * n**3 / (18 * d)
                   + (sp.diff(b, t, 3) / 2 - sp.diff(h, t) * mu
                      - 3 * h * sp.diff(mu, t)) * n**2 / (6 * d)
                   + (sp.diff(c, t, 3) / 2 - sp.diff(h, t) * M1
                      - 3 * h * sp.diff(M1, t)) * n / (3 * d) + g0)
        self.zero(3 * d * sp.diff(W0_poly, n) - rhs2)
        W_poly = sp.expand(integral(M_quad, W0_poly))
        gamma = sp.diff(a, t, 3) / (18 * d)
        self.zero(W_poly.coeff(n, 3) - gamma)
        self.zero(sp.diff(W_poly, n, 4))
        z, Q, kprime = sp.symbols("z Q kprime")
        shifted = sp.expand(W_poly.subs(n, z - Q * U**2 - kprime * U))
        self.zero(shifted.coeff(z, 3) - gamma)
        # The actual field equality and pole degree exclude this coefficient;
        # this algebra control alone does not establish either statement.

    def test_linear_cover_residuals_and_unrestricted_pencil_jets(self):
        t, n, U = sp.symbols("t n U")
        b, c, d, h, M1, M0 = (
            sp.Function(name)(t) for name in ("b", "c", "d", "h", "M1", "M0")
        )
        W0 = sp.Function("W0")(t, n)
        F = d * U**3 + h * U**2
        W = (-sp.diff(b, t) * U * F
             - b * (sp.diff(d, t) * U**4 / 4 + sp.diff(h, t) * U**3 / 3)
             + (sp.diff(b, t, 2) * n + sp.diff(c, t, 2)) * U**2 / 2
             + (sp.diff(M1, t) * n + sp.diff(M0, t)) * U - M1 * F + W0)
        residual = sp.expand(sp.diff(W, t) - sp.diff(F, U) * sp.diff(W, n))
        self.zero(residual.coeff(U, 4) + (
            10 * d * sp.diff(b, t, 2) + 5 * sp.diff(d, t) * sp.diff(b, t)
            + sp.diff(d, t, 2) * b
        ) / 4)

        lam = sp.symbols("lam", nonzero=True)
        alpha, beta = sp.symbols("alpha beta")
        k, c0, m0, D, g0 = (
            sp.Function(name)(t) for name in ("k", "c0", "m0", "D", "g0")
        )
        q = -t**3 - 1 / t
        ds, hs, Q = sp.diff(q, t, 3) / 6, sp.diff(k, t, 2) / 2, sp.diff(q, t, 2) / 2
        ms = alpha * t + beta
        Fs = ds * U**3 + hs * U**2
        Ws = (-lam * U * Fs
              - lam * t * (sp.diff(ds, t) * U**4 / 4 + sp.diff(hs, t) * U**3 / 3)
              + sp.diff(c0, t, 2) * U**2 / 2
              + (alpha * n + sp.diff(m0, t)) * U - ms * Fs + D * n + g0)
        rs = sp.expand(sp.diff(Ws, t) - sp.diff(Fs, U) * sp.diff(Ws, n))
        coefficients = sp.Poly(sp.expand(Ws), U)
        self.zero(coefficients.coeff_monomial(U**4) - lam)
        self.zero(rs.coeff(U, 3) + (
            lam * t * sp.diff(hs, t, 2) + 4 * lam * sp.diff(hs, t)
            + 3 * sp.diff(ds, t) * ms + 12 * ds * alpha
        ) / 3)
        self.zero(rs.coeff(U, 2) - (
            sp.diff(c0, t, 3) / 2 - sp.diff(hs, t) * ms - 3 * hs * alpha - 3 * ds * D
        ))
        self.zero(rs.coeff(U, 1) - sp.diff(m0, t, 2) + 2 * hs * D)
        self.zero(rs.coeff(U, 0) - sp.diff(D, t) * n - sp.diff(g0, t))
        g3 = coefficients.coeff_monomial(U**3) - alpha * Q
        g2 = sp.diff(c0, t, 2) / 2 - hs * ms - alpha * sp.diff(k, t) - Q * D
        g1 = sp.diff(m0, t) - sp.diff(k, t) * D
        self.zero(sp.diff(g3, t) - rs.coeff(U, 3))
        self.zero(sp.diff(g2, t) + Q * sp.diff(D, t) - rs.coeff(U, 2))
        self.zero(sp.diff(g1, t) + sp.diff(k, t) * sp.diff(D, t) - rs.coeff(U, 1))
        # Only the written exact pencil argument makes D constant.

    def test_symbolic_laurent_fixture_transport_and_original_inverse(self):
        t, n, y, X = sp.symbols("t n y X")
        Y, Z, W, I = sp.symbols("Y Z W I")
        lam = sp.symbols("lam", nonzero=True)
        alpha, beta, H1, H0, k1, k0, D, g2, g1, c1, c0, m00 = sp.symbols(
            "alpha beta H1 H0 k1 k0 D g2 g1 c1 c0 m00"
        )
        g0, g0_prime = sp.symbols("g0 g0_prime")
        q = -t**3 - 1 / t
        d, Q = sp.diff(q, t, 3) / 6, sp.diff(q, t, 2) / 2
        k = (alpha * t**3 / lam + beta / (lam * t**2) + H1 / t
             + H0 * t**2 + k1 * t + k0)
        h = sp.diff(k, t, 2) / 2
        self.zero(h - (3 * alpha * t / lam + 3 * beta / (lam * t**4) + H1 / t**3 + H0))
        M1 = alpha * t + beta
        M0 = D * k + g1 * t + m00
        c = (alpha**2 * t**4 / lam + (alpha * beta / lam + alpha * H0 - D) * t**3
             + (beta * H0 + alpha * k1 + g2) * t**2 + c1 * t + c0
             + (alpha * beta / lam + beta * H1 - D) / t + beta**2 / (lam * t**2))
        self.zero(lam * t * sp.diff(h, t, 2) + 4 * lam * sp.diff(h, t)
                  + 3 * sp.diff(d, t) * M1 + 12 * d * alpha)
        self.zero(sp.diff(c, t, 2) - 2 * g2 - 2 * h * M1 - 2 * alpha * sp.diff(k, t) - 2 * Q * D)
        self.zero(sp.diff(M0, t, 2) - 2 * h * D)

        F = d * y**3 + h * y**2
        rho = lam * t * n + c
        theta = (lam * n + sp.diff(c, t)) * y - lam * t * F + M1 * n + M0
        z = n + Q * y**2 + sp.diff(k, t) * y
        w = (-lam * y * F
             - lam * t * (sp.diff(d, t) * y**4 / 4 + sp.diff(h, t) * y**3 / 3)
             + sp.diff(c, t, 2) * y**2 / 2 + (alpha * n + sp.diff(M0, t)) * y
             - M1 * F + D * n + g0)
        Y_chart = y + t * X
        Z_chart = z + (sp.diff(q, t) * y + k) * X + q * X**2
        W_chart = w + theta * X + rho * X**2

        def T(expression):
            return (sp.diff(expression, t) - X * sp.diff(expression, y)
                    - sp.diff(F, y) * sp.diff(expression, n)
                    + g0_prime * sp.diff(expression, g0))

        self.zero(T(Y_chart))
        self.zero(T(Z_chart))
        self.zero(T(W_chart) - g0_prime)
        G = lam * y**4 + (beta - lam * H0) * y**3 + g2 * y**2 + g1 * y
        self.zero(w - (alpha * y + D) * z - G - g0)
        A0 = lam * X * Y + beta * X + alpha * Y + D
        A_chart = A0.subs(Y, Y_chart)
        self.zero(sp.diff(W_chart, n) - A_chart)
        self.zero(sp.diff(Z_chart, n) - 1)
        Qchart = sp.cancel(sp.expand(W_chart - A_chart * Z_chart - g0))
        self.zero(sp.diff(Qchart, n))
        self.zero(sp.diff(Qchart, t) - X * sp.diff(Qchart, y))
        # This is evaluation of the displayed Laurent-polynomial fixture
        # after g0 cancels, not specialization of an arbitrary element of K.
        Q0 = sp.cancel(Qchart.subs({t: 1, y: Y - X}, simultaneous=True))
        self.assertFalse(Q0.free_symbols.intersection({t, n, y, g0}))
        sp.Poly(Q0, X, Y)
        self.zero(Qchart.subs(y, Y - t * X) - Q0)
        self.zero(W_chart - A_chart * Z_chart - Q0.subs(Y, Y_chart) - g0)
        forward = W - A0 * Z - Q0
        inverse = I + A0 * Z + Q0
        self.zero(forward.subs(W, inverse) - I)
        self.zero(inverse.subs(I, forward) - W)


if __name__ == "__main__":
    unittest.main()

