"""Finite exact controls for the reviewed split reductions178 and179.

The coefficient charts are formal inputs, not newly realized dense frames.
The constant translations, quadratic shear and final matrix map are genuine
polynomial automorphisms, checked independently of any realization claim.
Only d is assumed nonzero among their complex-symbol coefficients; missing
leading terms and zero coefficients remain allowed in these identities.

These controls do not prove exact-field descent, transcendence, recognition,
the source hypotheses, or novelty.  In particular Ny is not replaced by one
in the determinant calibration.  No proof/solver internals or older checker
are imported.  Canonical execution belongs to Root after full source review.
"""

import unittest

import sympy as sp


class SplitNonlinearGraphControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_eliminant_and_actual_translation(self):
        U, V, r, ell, ell_t, ell_r, m = sp.symbols("U V r ell ell_t ell_r m")
        k20, k11, k02, k30, k21, k12, k03 = sp.symbols("k20 k11 k02 k30 k21 k12 k03")
        n10, n01, n20, n11, n02 = sp.symbols("n10 n01 n20 n11 n02")
        f = k20 * U**2 / 2 + k11 * U * V + k02 * V**2 / 2 + n10 * U + n01 * V
        g3 = (k30 * U**3 / 6 + k21 * U**2 * V / 2 + k12 * U * V**2 / 2
              + k03 * V**3 / 6 + n20 * U**2 / 2 + n11 * U * V + n02 * V**2 / 2)
        eliminant = (r - U) * (g3 - ell_t * U - ell_r * V - m) + sp.diff(f, V) * (ell - f)
        cubic = sp.expand(eliminant).coeff(V, 3)
        self.zero(cubic - ((r - U) * k03 / 6 - k02**2 / 2))
        # r_rho=0 also kills its t and rho derivatives in the next coefficient.
        prior = {k02: 0, k12: 0, k03: 0}
        quadratic = sp.expand(eliminant.subs(prior, simultaneous=True)).coeff(V, 2)
        lam = sp.Symbol("lam")
        self.zero(quadratic - (r - U) * n02 / 2)
        self.zero(sp.expand(quadratic - lam).coeff(U) + n02 / 2)
        self.zero((quadratic - lam).subs(n02, 0) + lam)
        linear = sp.expand(eliminant.subs({**prior, n02: 0}, simultaneous=True)).coeff(V)
        expected = (r - U) * (k21 * U**2 / 2 + n11 * U - ell_r) - (k11 * U + n01)**2
        self.zero(linear - expected)
        final_priors = {k21: 0, n11: -k11**2, ell_r: 2 * k11 * n01 + r * k11**2}
        self.zero(linear.subs(final_priors, simultaneous=True) + (r * k11 + n01)**2)

        x, xb, y, theta, w, t, rho, mu, nu = sp.symbols("x xb y theta w t rho mu nu")
        d = sp.Symbol("d", nonzero=True)
        k0, n0, ell0 = [sp.Function(name)(t) for name in ("k0", "n0", "ell0")]
        r = mu * t + nu
        s = d - mu * r
        k, n = r * rho + k0, s * rho + n0
        ell = (2 * mu * d - mu**2 * r) * rho + ell0
        sigma = -t * theta - rho * y + k
        z = sp.diff(k, t) * y + (r - y) * theta + n - t * w
        old_Y, old_Z, old_W = y + t * x, z + sigma * x - t * rho * x**2, w + theta * x + rho * x**2
        yb, tb, wb = y - r, theta - 2 * mu * rho, w - mu * theta + mu**2 * rho
        sb, zb = sigma + 2 * mu * t * rho, z - mu * sigma - mu**2 * t * rho
        kb = k - r * rho
        nb = n - mu * k + r * sp.diff(k, t) + mu * r * rho
        nb0 = n0 - mu * k0 + r * sp.diff(k0, t)
        ellb = ell0 - r * sp.diff(n0, t) - r**2 * sp.diff(k0, t, 2) / 2
        self.zero(kb - k0)
        self.zero(nb - (d * rho + nb0))
        self.zero(sb - (-t * tb - rho * yb + kb))
        self.zero(zb + t * wb - (sp.diff(kb, t) * yb - yb * tb + nb))
        new_images = (yb + t * xb, zb + sb * xb - t * rho * xb**2, wb + tb * xb + rho * xb**2)
        for original, translated in zip((old_Y - nu, old_Z, old_W), new_images):
            self.zero(original.subs(x, xb - mu) - translated)
            self.zero(translated.subs(xb, x + mu) - original)
        old_f = (sp.diff(k0, t, 2) * y**2 / 2 + (mu * y + s) * theta
                 + (sp.diff(n0, t) - mu**2 * rho) * y)
        old_residual = (r - y) * w + old_f - ell
        new_residual = (-yb * wb + sp.diff(kb, t, 2) * yb**2 / 2
                        + d * tb + sp.diff(nb0, t) * yb - ellb)
        # Exact residual equality, before imposing the first potential.
        self.zero(new_residual - old_residual)

    def test_normalized_determinant_and_parameter_factor(self):
        t, rho, y, v = sp.symbols("t rho y v")
        d = sp.Symbol("d", nonzero=True)
        k, n, ell = [sp.Function(name)(t) for name in ("k", "n", "ell")]
        m = sp.Function("m")(t, rho)
        A1 = sp.diff(m, rho)
        w = (m - sp.diff(k, t, 3) * y**3 / 6
             - sp.diff(n, t, 2) * y**2 / 2 + sp.diff(ell, t) * y) / d
        theta = (ell + y * w - sp.diff(k, t, 2) * y**2 / 2 - sp.diff(n, t) * y) / d
        z = sp.diff(k, t) * y - y * theta + d * rho + n - t * w
        self.zero(sp.diff(w, rho) - A1 / d)
        self.zero(sp.diff(theta, rho) - A1 * y / d**2)
        literal = sp.Matrix([y, z, w]).jacobian((t, rho, y)).det()
        self.zero(literal - (sp.diff(z, t) * sp.diff(w, rho) - sp.diff(z, rho) * sp.diff(w, t)))
        coefficients = [
            -sp.diff(m, t) + A1 / d * (sp.diff(n, t) - m / d),
            -sp.diff(ell, t, 2) + A1 / d * (sp.diff(k, t, 2) - 2 * sp.diff(ell, t) / d),
            (sp.diff(n, t, 3) + 3 * A1 * sp.diff(n, t, 2) / d**2) / 2,
            (sp.diff(k, t, 4) + 4 * A1 * sp.diff(k, t, 3) / d**2) / 6,
        ]
        self.zero(d**3 * (literal - sum(coefficient * y**i for i, coefficient in enumerate(coefficients))))
        A, B = sp.Function("A")(t), sp.Function("B")(t)
        scalar = coefficients[0].subs({
            m: A * rho + B,
            sp.diff(m, rho): A,
            sp.diff(m, t): sp.diff(A, t) * rho + sp.diff(B, t),
        }, simultaneous=True)
        expected = -(sp.diff(A, t) + A**2 / d**2) * rho - sp.diff(B, t) + A / d * (sp.diff(n, t) - B / d)
        self.zero(scalar - expected)

        # Independent change of separating parameter.  Its Jacobian is gamma,
        # so the actual old determinant -a^3 becomes -a^3/gamma, not -a^3.
        gamma, eta = sp.Function("gamma")(t, rho), sp.Function("eta")(t, rho)
        y_source = gamma * v + eta
        change_det = sp.Matrix([t, rho, y_source]).jacobian((t, rho, v)).det()
        self.zero(change_det - gamma)
        probe = t * y**2 + rho * y + t * rho
        source_probe = probe.subs(y, y_source)
        for direction in (t, rho):
            self.zero(gamma * sp.diff(source_probe, direction)
                      - sp.diff(y_source, direction) * sp.diff(source_probe, v)
                      - gamma * sp.diff(probe, direction).subs(y, y_source))
        self.zero(sp.diff(source_probe, v) - gamma * sp.diff(probe, y).subs(y, y_source))
        a = sp.Symbol("a", nonzero=True)
        calibrated_new = -a**3 / gamma
        self.zero(gamma * calibrated_new + a**3)
        # No assertion that the rho-linear scalar above is a rational cube.

    def test_quadratic_graph_actual_shear_and_time_tops(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        A0, B1, C0, D0, F0 = sp.symbols("A0 B1 C0 D0 F0")
        d = sp.Symbol("d", nonzero=True)
        H = X * Z + Y * W
        good = C0 * X**2 + B1 * X * Y + A0 * Y**2 + F0 * X + D0 * Y
        P0 = (good - H) / d
        Delta = lambda f: Y * sp.diff(f, Z) - X * sp.diff(f, W)
        self.zero(Delta(P0))
        # The two choices check inverse-after-forward and forward-after-inverse.
        for sign in (1, -1):
            new_Z, new_W = Z - sign * Y * P0, W + sign * X * P0
            new_H = X * new_Z + Y * new_W
            self.zero(new_H - H)
            new_P0 = (good - new_H) / d
            self.zero(new_P0 - P0)
            self.zero(new_Z + sign * Y * new_P0 - Z)
            self.zero(new_W - sign * X * new_P0 - W)

        # Formal actual-chart identities: E=a*d/dx, with coefficients fixed.
        # These are not an additional inverse-verified dense-frame fixture.
        x, y, t, rho, w, theta, a = sp.symbols("x y t rho w theta a")
        k, n = A0 * t**2 + B1 * t + C0, D0 * t + F0
        chart_Y = y + t * x
        chart_z = sp.diff(k, t) * y - y * theta + d * rho + n - t * w
        chart_sigma = -t * theta - rho * y + k
        chart_Z = chart_z + chart_sigma * x - t * rho * x**2
        chart_W = w + theta * x + rho * x**2
        chart_H = x * chart_Z + chart_Y * chart_W
        expected_H = y * w + (sp.diff(k, t) * y + d * rho + n) * x + k * x**2
        self.zero(chart_H - expected_H)
        chart_good = good.subs({X: x, Y: chart_Y}, simultaneous=True)
        chart_P0 = (chart_good - chart_H) / d
        self.zero(sp.diff(chart_good, x) - (2 * k * x + sp.diff(k, t) * y + n))
        self.zero(sp.diff(chart_P0, x) + rho)
        self.zero(a**2 * sp.diff(chart_P0, x, 2))
        self.zero(a**2 * sp.diff(chart_Z, x, 2) / 2 + a**2 * t * rho)
        self.zero(a**2 * sp.diff(chart_W, x, 2) / 2 - a**2 * rho)
        self.zero(a**2 * sp.diff(chart_Y * chart_P0, x, 2) / 2 + a**2 * t * rho)
        self.zero(a**2 * sp.diff(x * chart_P0, x, 2) / 2 + a**2 * rho)
        for coordinate in (x, chart_Y, chart_Z - chart_Y * chart_P0, chart_W + x * chart_P0):
            self.zero(a**2 * sp.diff(coordinate, x, 2))

    def test_rho_constant_invariant_and_both_polynomial_inverse_orders(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        d = sp.Symbol("d", nonzero=True)
        k3, k2, k1, k0, n2, n1, n00, ell1, ell0 = sp.symbols(
            "k3 k2 k1 k0 n2 n1 n00 ell1 ell0"
        )
        K3 = k3 * Y**3 + k2 * X * Y**2 + k1 * X**2 * Y + k0 * X**3
        N2 = n2 * Y**2 + n1 * X * Y + n00 * X**2
        Q = K3 + N2 - ell1 * Y - ell0 * X
        H = X * Z + Y * W
        I = d * W - X * H + Q
        J = (d + X * Y) * Z + Y**2 * W
        matrix = sp.Matrix([[-X**2, d - X * Y], [d + X * Y, Y**2]])
        self.zero(matrix.det() + d**2)
        self.zero(I - Q - (-X**2 * Z + (d - X * Y) * W))
        self.zero((d - X * Y) * J - Y**2 * (I - Q) - d**2 * Z)
        self.zero((d + X * Y) * (I - Q) + X**2 * J - d**2 * W)
        # Reverse order in independent target coordinates; no X or Y inverse.
        x1, y1, i1, j1 = sp.symbols("x1 y1 i1 j1")
        Q1 = Q.subs({X: x1, Y: y1}, simultaneous=True)
        U0 = i1 - Q1
        inv_Z = ((d - x1 * y1) * j1 - y1**2 * U0) / d**2
        inv_W = ((d + x1 * y1) * U0 + x1**2 * j1) / d**2
        self.zero(-x1**2 * inv_Z + (d - x1 * y1) * inv_W + Q1 - i1)
        self.zero((d + x1 * y1) * inv_Z + y1**2 * inv_W - j1)

        x, y, t, rho, m = sp.symbols("x y t rho m")
        k = k3 * t**3 + k2 * t**2 + k1 * t + k0
        n, ell = n2 * t**2 + n1 * t + n00, ell1 * t + ell0
        w = (m - k3 * y**3 - n2 * y**2 + ell1 * y) / d
        theta = (ell + y * w - sp.diff(k, t, 2) * y**2 / 2 - sp.diff(n, t) * y) / d
        z = sp.diff(k, t) * y - y * theta + d * rho + n - t * w
        chart_Y = y + t * x
        chart_Z = z + (-t * theta - rho * y + k) * x - t * rho * x**2
        chart_W = w + theta * x + rho * x**2
        chart_H = x * chart_Z + chart_Y * chart_W
        K3_chart = K3.subs({X: x, Y: chart_Y}, simultaneous=True)
        N2_chart = N2.subs({X: x, Y: chart_Y}, simultaneous=True)
        self.zero(K3_chart - (k * x**3 + sp.diff(k, t) * y * x**2
                             + sp.diff(k, t, 2) * y**2 * x / 2 + k3 * y**3))
        self.zero(N2_chart - (n * x**2 + sp.diff(n, t) * y * x + n2 * y**2))
        self.zero(x * chart_H - K3_chart - N2_chart
                  - (d * rho * x**2 + (d * theta - ell) * x - k3 * y**3 - n2 * y**2))
        returned_I = d * chart_W - x * chart_H + Q.subs({X: x, Y: chart_Y}, simultaneous=True)
        self.zero(d**2 * (returned_I - m))
        # These polynomial identities remain valid when top coefficients vanish.
        # This does not assert that every such specialization meets the graph
        # degree assumptions or the remaining actual-frame hypotheses.
        self.zero(d**2 * (returned_I - m).subs({k3: 0, n2: 0}, simultaneous=True))


if __name__ == "__main__":
    unittest.main()
