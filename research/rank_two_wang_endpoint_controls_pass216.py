"""Independent finite algebra controls for the written pass216 endpoint.

These tests check literal potential coefficients, derivative and Laurent
identities, rational-mode substitutions, and a constant polynomial translation.
They do not prove Wang's theorem, ratio transcendence over C(X), exact-field
integration completeness, the actual whole-line return, or original-ring
recognition. Formal coefficient charts below are not claimed to be realized
globally sliced frames. No retained checker or solver implementation is imported.
"""

import unittest

import sympy as s


class RankTwoWangEndpointControls(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(s.cancel(s.expand(value)), 0)

    def test_full_lower_potentials_with_free_intercepts(self):
        t, U, V = s.symbols("t U V")
        rho, c = s.symbols("rho c", nonzero=True)
        f = s.Function("f")(rho)
        g = s.Function("g")(rho)
        h = s.Function("h")(rho)
        p0 = s.Function("p0")(t, rho)
        omega = s.Function("omega")(t, rho)
        ell = s.Function("ell")(t, rho)
        m = s.Function("m")(t, rho)
        k, n = -c * t / rho + f, g * t + h
        kr, K = s.diff(k, rho), s.diff(k, t, rho)
        center_slope = s.diff(n, t) - rho**3 * kr * K / 2
        p1 = rho * kr / c + 2 * (center_slope + rho * s.diff(center_slope, rho)) / c**2
        expected_p1 = t / rho - rho * s.diff(f, rho) / c - rho**2 * s.diff(f, rho, 2) / c
        expected_p1 += 2 * (g + rho * s.diff(g, rho)) / c**2
        self.zero(p1 - expected_p1)
        self.zero(s.diff(p1, t) - 1 / rho)
        projected_y = V**2 / (c * rho**2) + p1 * V + p0

        lam = rho**2 * s.diff(f, rho) / 2 + rho**3 * s.diff(f, rho, 2) / 4
        lam -= rho * (3 * g + 2 * rho * s.diff(g, rho)) / (2 * c)
        projected_w = lam * V + omega
        R = 2 * V / rho**3 + kr
        S = -V**3 / rho**4 + s.diff(k, t, 2) * U**2 / 2 + K * U * V
        S += s.diff(k, rho, 2) * V**2 / 2 + s.diff(n, t) * U + s.diff(n, rho) * V
        c0 = -3 * V**2 / rho**4 + K * U + s.diff(k, rho, 2) * V + s.diff(n, rho)

        def jet(value, order):
            return sum(
                s.diff(value, t, j, rho, order - j) * U**j * V**(order - j)
                / (s.factorial(j) * s.factorial(order - j))
                for j in range(order + 1)
            )

        Q = V**4 / rho**5 + jet(k, 3) + jet(n, 2)
        Q -= s.diff(ell, t) * U + s.diff(ell, rho) * V + m
        third = s.expand(R * projected_w + S.subs(U, projected_y) - ell)
        fourth = s.expand(projected_w**2 / rho**3
                          + c0.subs(U, projected_y) * projected_w + Q.subs(U, projected_y))
        self.zero(third.coeff(V, 3))
        self.zero(third.coeff(V, 2))
        self.assertTrue(third.has(p0))
        self.assertTrue(fourth.has(p0))
        self.assertTrue(fourth.has(s.diff(h, rho, 2)))
        self.zero(fourth.coeff(V, 4))

        # The literal second potential, not an assumed affine z formula.
        projected_z = -projected_w / rho**2 + V**2 / rho**3
        projected_z += s.diff(k, t) * projected_y + kr * V + n
        projected_z = s.expand(projected_z)
        self.zero(projected_z.coeff(V, 2))
        kappa = projected_z.coeff(V, 1)
        M = g / (c * rho) + s.diff(f, rho) + rho * s.diff(f, rho, 2) / 2
        self.zero(kappa - lam / rho**2 - M)
        self.zero(s.diff(lam, t))
        self.zero(s.diff(kappa, t))

        raw_cubic = -2 * lam / rho**4 - c * p1 / rho**3 + c * t / rho**4
        raw_cubic += s.diff(f, rho, 3) / 6 + s.diff(g, rho) / (c * rho**2)
        required_cubic = (g + rho * s.diff(g, rho)) / (c * rho**3)
        required_cubic += s.diff(f, rho, 2) / (2 * rho) + s.diff(f, rho, 3) / 6
        self.zero(fourth.coeff(V, 3) - raw_cubic)
        self.zero(raw_cubic - required_cubic)
        integral = rho * g + c * rho**3 * s.diff(f, rho, 2) / 6
        self.zero(s.diff(integral, rho) - c * rho**3 * required_cubic)
        self.zero(M - integral / (c * rho**2) - s.diff(f, rho)
                  - rho * s.diff(f, rho, 2) / 3)

        # Dropping either of these full-potential terms changes the critical gate.
        without_rho_cubic = fourth - s.diff(k, rho, 3) * V**3 / 6
        without_mixed_n = fourth - s.diff(n, t, rho) * projected_y * V
        error1 = s.expand(without_rho_cubic).coeff(V, 3) - required_cubic
        error2 = s.expand(without_mixed_n).coeff(V, 3) - required_cubic
        self.zero(error1 + s.diff(k, rho, 3) / 6)
        self.zero(error2 + s.diff(g, rho) / (c * rho**2))
        self.assertNotEqual(s.cancel(s.expand(error1)), 0)
        self.assertNotEqual(s.cancel(s.expand(error2)), 0)

    def test_laurent_coefficients_and_degree_negative_controls(self):
        X, z, w, z0, w0, v, slope, lam, kappa = s.symbols("X z w z0 w0 v slope lam kappa")
        a, b, eps = s.symbols("a b eps")
        c = s.symbols("c", nonzero=True)
        a2, b2, g2, a3, b3, g3, a4, b4, g4 = s.symbols("a2 b2 g2 a3 b3 g3 a4 b4 g4")
        leading = a2 * slope**2 - b2 * slope + g2 + slope / c
        self.zero(leading.subs({a2: 0, b2: 1 / c, g2: 0}, simultaneous=True))
        self.zero(s.Poly(leading, slope).coeff_monomial(slope**2) - a2)
        self.zero(s.Poly(leading, slope).coeff_monomial(slope) - (1 / c - b2))
        self.zero(s.Poly(leading, slope).coeff_monomial(1) - g2)

        alpha = a3 * eps**3 + a4 * eps**4
        beta = eps**2 / c + b3 * eps**3 + b4 * eps**4
        gamma = g3 * eps**3 + g4 * eps**4
        good_z, good_w = kappa - slope / eps, 1 / eps + lam
        identity = s.expand(slope / c + alpha * good_z**2
                            + beta * good_z * good_w + gamma * good_w**2)
        self.zero(identity.coeff(eps, 0))
        self.zero(identity.coeff(eps, 1)
                  - ((kappa - slope * lam) / c + a3 * slope**2 - b3 * slope + g3))
        m0, m1, m2 = -c * g3, c * b3, -c * a3
        self.zero(identity.coeff(eps, 1).subs(kappa, slope * lam + m0 + m1 * slope + m2 * slope**2))

        # Finite algebra behind applying D^j to a homogeneous polynomial.
        # Transcendence of the actual good-coordinate ratio is a prose input.
        for degree in range(1, 5):
            coefficients = s.symbols("q0:" + str(degree + 1))
            homogeneous = sum(coefficients[j] * z**j * w**(degree - j)
                              for j in range(degree + 1))
            along_line = homogeneous.subs({z: z0 + a * v, w: w0 + b * v}, simultaneous=True)
            self.zero(s.diff(along_line, v, degree)
                      - s.factorial(degree) * homogeneous.subs({z: a, w: b}, simultaneous=True))

        ratio_at_infinity = (kappa * eps - slope) / (1 + lam * eps)
        finite_relation = (eps**2 + 1) * ratio_at_infinity**2
        finite_relation += (2 - eps) * ratio_at_infinity + 3 + 7 * eps**2
        self.zero(finite_relation.subs(eps, 0) - (slope**2 - 2 * slope + 3))

        # Enlarging the coefficient field by the slope invalidates the degree gate.
        forbidden_field_polynomial = (z + slope * w)**3
        self.zero(forbidden_field_polynomial.subs({z: -slope * X, w: X}, simultaneous=True))
        self.assertEqual(s.Poly(forbidden_field_polynomial, z, w).total_degree(), 3)
        # The leading quadratic identity alone admits formal data. It is not an
        # actual-frame existence or exclusion test without the lower potentials.
        formal_good_z, formal_good_w = -slope * X, X
        self.zero(slope / c + formal_good_z * formal_good_w / (c * X**2))

    def test_exact_modes_and_two_pole_exclusions(self):
        rho, c = s.symbols("rho c", nonzero=True)
        X, slope, m0, m1, m2, epsilon, d0, e0 = s.symbols("X slope m0 m1 m2 epsilon d0 e0")
        alpha, beta, gamma = s.symbols("alpha beta gamma")
        b0 = 3 * (epsilon / c - m1)
        f = m0 * rho + b0 / rho + d0 / rho**2 + m2 / rho**3 + e0
        g = c * m1 / rho - c * d0 / rho**2 - 2 * c * m2 / rho**3
        self.zero(rho * s.diff(f, rho, 2) + 3 * s.diff(f, rho)
                  - 3 * m0 - 3 * (m1 - epsilon / c) / rho**2 - 3 * m2 / rho**4)
        self.zero(rho * g + c * rho**3 * s.diff(f, rho, 2) / 6 - epsilon)
        raw_lambda = rho**2 * s.diff(f, rho) / 2 + rho**3 * s.diff(f, rho, 2) / 4
        raw_lambda -= rho * (3 * g + 2 * rho * s.diff(g, rho)) / (2 * c)
        raw_M = g / (c * rho) + s.diff(f, rho) + rho * s.diff(f, rho, 2) / 2
        lam = (m0 / slope - m1 - 3 * m2 * slope) / 2
        kappa = (3 * m0 + m1 * slope - m2 * slope**2) / 2
        self.zero(raw_lambda - lam.subs(slope, rho**-2))
        self.zero(raw_M - (m0 + m1 * slope + m2 * slope**2).subs(slope, rho**-2))
        self.zero(raw_M + raw_lambda / rho**2 - kappa.subs(slope, rho**-2))

        good_z, good_w = kappa - slope * X, X + lam
        identity = slope / c + alpha * good_z**2 + beta * good_z * good_w + gamma * good_w**2
        # Multiplying by slope^2 retains the exact successive poles at zero.
        cleared = s.Poly(s.expand(slope**2 * identity), slope)
        self.zero(cleared.coeff_monomial(1) - gamma * m0**2 / 4)
        self.zero(cleared.as_expr().subs(gamma, 0).expand().coeff(slope, 1) - 3 * beta * m0**2 / 4)
        self.zero(cleared.as_expr().subs({gamma: 0, beta: 0}, simultaneous=True).expand().coeff(slope, 2)
                  - 9 * alpha * m0**2 / 4)

        at_infinity = s.Poly(s.expand(identity.subs(m0, 0)), slope)
        self.zero(at_infinity.coeff_monomial(slope**4) - alpha * m2**2 / 4)
        self.zero(at_infinity.as_expr().subs(alpha, 0).expand().coeff(slope, 3) - 3 * beta * m2**2 / 4)
        self.zero(at_infinity.as_expr().subs({alpha: 0, beta: 0}, simultaneous=True).expand().coeff(slope, 2)
                  - 9 * gamma * m2**2 / 4)
        self.zero(identity.subs({alpha: 0, beta: 0, gamma: 0}, simultaneous=True) - slope / c)

        # The surviving formal slope identity does not certify actual realization.
        surviving = identity.subs({m0: 0, m2: 0, alpha: 0, gamma: 0,
                                   beta: 1 / (c * (X - m1 / 2)**2)}, simultaneous=True)
        self.zero(surviving)
        self.zero((lam + m1 / 2).subs({m0: 0, m2: 0}, simultaneous=True))
        self.zero((kappa + slope * lam).subs({m0: 0, m2: 0}, simultaneous=True))

    def test_actual_translation_and_even_degree_boundary(self):
        X, Y, Z, W, Xn, Yn, Zn, Wn = s.symbols("X Y Z W Xn Yn Zn Wn")
        lam, t, V, p1, p0, omega, zeta, k, u, x0 = s.symbols("lam t V p1 p0 omega zeta k u x0")
        rho, c, a = s.symbols("rho c a", nonzero=True)
        originals, new_names = (X, Y, Z, W), (Xn, Yn, Zn, Wn)
        forward = (X + lam, Y, Z, W)
        inverse = (Xn - lam, Yn, Zn, Wn)
        for old, recovered in zip(originals, inverse):
            self.zero(recovered.subs(dict(zip(new_names, forward)), simultaneous=True) - old)
        for new, recovered in zip(new_names, forward):
            self.zero(recovered.subs(dict(zip(originals, inverse)), simultaneous=True) - new)
        self.assertEqual(tuple(s.diff(value, Z) for value in forward), (0, 0, 1, 0))
        self.assertEqual(tuple(s.diff(value, Zn) for value in inverse), (0, 0, 1, 0))

        y = V**2 / (c * rho**2) + p1 * V + p0
        w = lam * V + omega
        z = -lam * V / rho**2 + zeta
        sigma = -V / rho**2 + k
        actual_X = a * u + x0
        actual_Y = y + t * actual_X
        actual_Z = z + sigma * actual_X + actual_X**2 / rho
        actual_W = w + V * actual_X + rho * actual_X**2
        old_chart = (actual_X, actual_Y, actual_Z, actual_W)
        new_chart = (actual_X + lam, actual_Y, actual_Z, actual_W)
        for old, new, degree in zip(old_chart, new_chart, (1, 1, 2, 2)):
            old_poly, new_poly = s.Poly(s.expand(old), u), s.Poly(s.expand(new), u)
            self.assertEqual(old_poly.degree(), degree)
            self.assertEqual(new_poly.degree(), degree)
            self.zero(old_poly.LC() - new_poly.LC())
        # Exact leaders only, not proof that this free coefficient chart is actual.
        self.zero(s.Poly(actual_Z, u).LC() * s.Poly(actual_W, u).LC() - a**4)

        theta_new, sigma_new = V - 2 * rho * lam, sigma - 2 * lam / rho
        projected_y = actual_Y - t * new_chart[0]
        projected_w = actual_W - theta_new * new_chart[0] - rho * new_chart[0]**2
        projected_z = actual_Z - sigma_new * new_chart[0] - new_chart[0]**2 / rho
        self.zero(projected_y - (y - lam * t))
        self.zero(projected_w - (omega + rho * lam**2))
        self.zero(projected_z - (zeta - lam * k + lam**2 / rho))
        self.zero(s.diff(projected_w, V))
        self.zero(s.diff(projected_z, V))
        self.assertEqual(s.Poly(s.expand(projected_y), V).degree(), 2)
        self.assertEqual(s.Poly(theta_new, V).degree(), 1)

        # Finite polynomial controls for the written even-degree obstruction.
        x, variable, leading = s.symbols("x variable leading", nonzero=True)
        p2 = 1 / (c * rho**2)
        centered_y = s.expand(projected_y.subs(V, x - p1 / (2 * p2)))
        self.zero(centered_y - (p2 * x**2 + p0 - lam * t - p1**2 / (4 * p2)))
        for degree in range(1, 5):
            lower = s.symbols("r0:" + str(degree))
            polynomial = leading * variable**degree + sum(lower[j] * variable**j for j in range(degree))
            composed = s.Poly(s.expand(polynomial.subs(variable, centered_y)), x)
            self.assertEqual(composed.degree(), 2 * degree)
            self.zero(composed.LC() - leading * p2**degree)
            for power in range(1, 2 * degree, 2):
                self.zero(composed.coeff_monomial(x**power))
        self.assertNotEqual(2 * x, 0)


if __name__ == "__main__":
    unittest.main()
