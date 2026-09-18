"""Finite exact controls for the reducible-surface reduction in pass302.

The generic potential identities use arbitrary coefficient functions, with
their commuting derivatives, rather than sampled polynomials. The separate
factor/conic fixtures check only their displayed finite algebra and expose
the need for whole-ring return. They are not asserted actual frames.

These tests do not prove actual entry, field constants, a factorization
theorem, an LND or whole-ring theorem, the universal conic bound, or ambient
recognition. No later pass303 conclusion is included. No saved proof or
checker is imported. Root owns the sole canonical execution after a full
saved-source read; the author does not execute or compile this file.
"""

import unittest

import sympy as sp


def reduce_exact(expression):
    return sp.cancel(sp.expand(expression))


def repeat_derivative(operator, expression, count):
    for _ in range(count):
        expression = operator(expression)
    return expression


def raw_potentials(k, n, ell, dt, ds, U, P, V):
    """Rebuild both potentials and the monic surface from derivative rules."""
    def taylor(function, degree):
        return sp.Add(*(
            repeat_derivative(
                dt, repeat_derivative(ds, function, degree - i), i
            ) * P**i * V**(degree - i)
            / (sp.factorial(i) * sp.factorial(degree - i))
            for i in range(degree + 1)
        ))

    m = reduce_exact(ds(k))
    kt = reduce_exact(dt(k))
    F = reduce_exact(taylor(k, 2) + taylor(n, 1))
    gamma = 2 * P + kt
    g = reduce_exact((ell - gamma * U - F) / m)
    H = reduce_exact(
        U**2 + sp.diff(F, P) * U + sp.diff(F, V) * g
        + taylor(k, 3) + taylor(n, 2) - dt(ell) * P - ds(ell) * V
    )
    return {"m": m, "kt": kt, "F": F, "g": g, "H": H}


class PrincipalReducibleSurfaceConicControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(reduce_exact(expression), 0)

    def test_generic_discriminant_top_and_quadratic_factor_rigidity(self):
        t, s, U, P, V, h0 = sp.symbols("t s U P V h0")
        k, n, ell = (sp.Function(name)(t, s) for name in ("k", "n", "ell"))
        dt = lambda expression: sp.diff(expression, t)
        ds = lambda expression: sp.diff(expression, s)
        raw = raw_potentials(k, n, ell, dt, ds, U, P, V)
        H, m = raw["H"], raw["m"]
        A1 = sp.Poly(H, U).coeff_monomial(U)
        A0 = H.subs(U, 0) - h0
        delta = reduce_exact(A1**2 - 4 * A0)
        top_A1 = sum(
            coefficient * P**i * V**j
            for (i, j), coefficient in sp.Poly(A1, P, V).terms()
            if i + j == 2
        )
        expected_top = -2 * P * (dt(m) * P + ds(m) * V) / m
        self.assert_zero(top_A1 - expected_top)
        top_delta = sum(
            coefficient * P**i * V**j
            for (i, j), coefficient in sp.Poly(delta, P, V).terms()
            if i + j == 4
        )
        self.assert_zero(top_delta - expected_top**2)

        # For the displayed binary quadratic, the square criterion keeps
        # both coupling derivatives and the nonunit denominator m.
        mt, ms, M = sp.symbols("mt ms M")
        quadratic = -2 * P * (mt * P + ms * V) / M
        coefficients = sp.Poly(quadratic, P, V)
        aa = coefficients.coeff_monomial(P**2)
        bb = coefficients.coeff_monomial(P * V)
        cc = coefficients.coeff_monomial(V**2)
        self.assert_zero(bb**2 - 4 * aa * cc - 4 * ms**2 / M**2)
        self.assert_zero(quadratic.subs(ms, 0) + 2 * mt * P**2 / M)

        # Once m is constant, k=m*s+k0(t) still permits arbitrary k0.
        k0 = sp.Function("k0")(t)
        constant_m = raw_potentials(M * s + k0, n, ell, dt, ds, U, P, V)
        cubic = sum(
            coefficient * U**i * P**j * V**l
            for (i, j, l), coefficient in sp.Poly(
                constant_m["H"], U, P, V
            ).terms()
            if i + j + l == 3
        )
        self.assert_zero(cubic - sp.diff(k0, t, 3) * P**3 / 6)

    def test_actual_reframe_both_orders_and_generic_surface_level_transport(self):
        t, s, X, U, P, V, Vstar = sp.symbols("t s X U P V Vstar")
        M, kappa, b, d = sp.symbols("M kappa b d")
        n, ell = (sp.Function(name)(t, s) for name in ("n", "ell"))
        k = M * s + kappa * t**2 / 2 + b * t + d
        kt = sp.diff(k, t)
        dt = lambda expression: sp.diff(expression, t)
        ds = lambda expression: sp.diff(expression, s)
        dt_star = lambda expression: dt(expression) - kt * ds(expression) / M
        ds_star = lambda expression: ds(expression) / M
        self.assert_zero(dt_star(k))
        self.assert_zero(ds_star(k) - 1)
        self.assert_zero(dt_star(ds_star(n)) - ds_star(dt_star(n)))

        old = raw_potentials(k, n, ell, dt, ds, U, P, V)
        nstar = n - kappa * k / 2
        nustar = ds(n) / M - kappa / 2
        ellstar = ell + kappa * n / 2 + kappa * k * nustar / 2
        new = raw_potentials(
            k, nstar, ellstar, dt_star, ds_star, U, P, Vstar
        )
        self.assert_zero(new["m"] - 1)
        self.assert_zero(new["kt"])
        self.assert_zero(dt_star(nstar) - dt(n) + kt * ds(n) / M)
        self.assert_zero(ds_star(nstar) - nustar)
        phi = M * V + kt * P + kappa * k / 2
        z = 2 * t * U + P**2 + kt * P + M * V + n
        wstar = M * old["g"] + kappa * z / 2 + b * U
        self.assert_zero(z - (2 * t * U + P**2 + phi + nstar))
        self.assert_zero(new["g"].subs(Vstar, phi) - wstar)

        Y = U + P * X + t * X**2
        Z = z + (2 * t * P + k) * X + t**2 * X**2
        W = old["g"] + V * X + s * X**2
        transformed_W = M * W + kappa * Z / 2 + b * Y + d * X**2
        self.assert_zero(transformed_W - (wstar + phi * X + k * X**2))

        # This uses independent original-coordinate symbols, not intercepts.
        x0, y0, z0, w0, wnew = sp.symbols("x0 y0 z0 w0 wnew")
        forward = M * w0 + kappa * z0 / 2 + b * y0 + d * x0**2
        inverse = (wnew - kappa * z0 / 2 - b * y0 - d * x0**2) / M
        self.assert_zero(inverse.subs(wnew, forward) - w0)
        self.assert_zero(forward.subs(w0, inverse) - wnew)
        coefficient_jacobian = sp.Matrix([[1, 0], [kt, M]]).det()
        actual_jacobian = sp.Matrix([
            [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
            [2 * d * x0, b, kappa / 2, M],
        ]).det()
        self.assert_zero(actual_jacobian / coefficient_jacobian - 1)

        # The level shift must be rebuilt, not assumed absent or constant
        # under coefficient differentiation. n_s remains arbitrary here.
        difference = reduce_exact(new["H"].subs(Vstar, phi) - old["H"])
        c1 = kappa * k / 2
        cstar = nustar * ellstar - c1 * nustar**2
        cstar += c1**2 * ds(ds(n)) / (2 * M**2)
        cstar -= c1 * ds_star(ellstar) + ds(n) * ell / M
        self.assert_zero(difference - cstar)
        for variable in (U, P, V):
            self.assert_zero(sp.diff(difference, variable))
        h0 = sp.symbols("h0")
        self.assert_zero(
            new["H"].subs(Vstar, phi) - (h0 + cstar) - (old["H"] - h0)
        )
        # A normalization that kept the old level would in general fail.
        self.assertNotEqual(reduce_exact(cstar), 0)

    def test_normalized_discriminant_and_affine_fourth_gradients(self):
        t, s, U, P, V, h0 = sp.symbols("t s U P V h0")
        n, ell = (sp.Function(name)(t, s) for name in ("n", "ell"))
        dt = lambda expression: sp.diff(expression, t)
        ds = lambda expression: sp.diff(expression, s)
        raw = raw_potentials(s, n, ell, dt, ds, U, P, V)
        H = raw["H"]
        A1 = sp.Poly(H, U).coeff_monomial(U)
        delta = reduce_exact(A1**2 - 4 * (H.subs(U, 0) - h0))
        expected = (4 * ds(n)**2 - 2 * dt(dt(n))) * P**2
        expected -= 4 * dt(ds(n)) * P * V + 2 * ds(ds(n)) * V**2
        expected += 4 * dt(ell) * P + 4 * (ds(ell) + ds(n)**2) * V
        expected += dt(n)**2 - 4 * ds(n) * ell + 4 * h0
        self.assert_zero(delta - expected)

        nu, b1, c2, ell0 = sp.symbols("nu b1 c2 ell0")
        f = nu**2 * t**2 + b1 * t + c2
        nfamily = nu * s + f
        ellfamily = -nu**2 * s + ell0
        family = raw_potentials(s, nfamily, ellfamily, dt, ds, U, P, V)
        H = family["H"]
        expected_H = U**2 + (dt(f) - 2 * nu * P) * U
        expected_H += -nu * dt(f) * P + nu**2 * P**2 + nu * ellfamily
        self.assert_zero(H - expected_H)
        hu, hp, hv = (sp.diff(H, variable) for variable in (U, P, V))
        level = sp.Function("level")(t, s)
        qu = hp - 2 * P * hv + nu * hu
        qp = dt(H) - dt(level) - (2 * U + dt(f)) * hv + nu * hp
        qv = ds(H) - ds(level)
        self.assert_zero(qu)
        self.assert_zero(qp + dt(level) + nu**2 * dt(f))
        self.assert_zero(qv + ds(level) + nu**3)

        # Wrong half-sized t^2 term fails the P^2 discriminant gate for
        # nonzero nu. The legitimate family above also retains nu=0.
        wrong_n = nu * s + nu**2 * t**2 / 2 + b1 * t + c2
        wrong_gate = 4 * ds(wrong_n)**2 - 2 * dt(dt(wrong_n))
        self.assert_zero(wrong_gate - 2 * nu**2)
        self.assertNotEqual(reduce_exact(wrong_gate), 0)

    def test_constant_difference_and_conic_return_fixtures(self):
        U, P, V, r = sp.symbols("U P V r")
        a0, a1, a2, eta = sp.symbols("a0 a1 a2 eta")
        A = a0 + a1 * P + a2 * V
        B = A + eta
        H0 = sp.expand((U + A) * (U + B))
        self.assert_zero((A + B)**2 - 4 * A * B - eta**2)
        self.assertLessEqual(sp.Poly(H0, U, P, V).total_degree(), 2)
        line_slope, line_intercept = sp.symbols("line_slope line_intercept")
        affine_y = -A.subs({P: r, V: line_slope * r + line_intercept})
        self.assertLessEqual(sp.Poly(affine_y, r).degree(), 1)

        g2, g1, gv, g0 = sp.symbols("g2 g1 gv g0")
        G = g2 * P**2 + g1 * P + gv * V + g0
        theta = -(g2 * r**2 + g1 * r + g0) / gv
        self.assert_zero(G.subs({P: r, V: theta}))
        self.assertEqual(sp.Poly(theta, r).degree(), 2)
        M, mt, kt, ktt, nt, ns = sp.symbols("M mt kt ktt nt ns")
        F = ktt * P**2 / 2 + mt * P * V + nt * P + ns * V
        A1 = sp.diff(F, P) - (2 * P + kt) * sp.diff(F, V) / M
        expected_A1 = -2 * mt * P**2 / M + mt * V
        expected_A1 += (ktt - (kt * mt + 2 * ns) / M) * P + nt - kt * ns / M
        self.assert_zero(A1 - expected_A1)
        y = (eta - A1.subs({P: r, V: theta})) / 2
        self.assertLessEqual(sp.Poly(y, r).degree(), 2)

        # A conic equation alone does not force an affine first generator:
        # P=r^2,V=r^4 generate an involution-fixed proper subring. This is
        # a formal negative control, not an actual chart or whole-return case.
        sigma_bad, theta_bad = r**2, r**4
        self.assert_zero(theta_bad - sigma_bad**2)
        self.assert_zero(sigma_bad.subs(r, -r) - sigma_bad)
        self.assert_zero(theta_bad.subs(r, -r) - theta_bad)
        self.assertNotEqual(sp.expand((-r) - r), 0)
        self.assertEqual(sp.Poly(sigma_bad, r).degree(), 2)


if __name__ == "__main__":
    unittest.main()
