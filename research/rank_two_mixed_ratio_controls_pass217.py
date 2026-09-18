"""Finite algebra controls for the supplied mixed-ratio frame, pass217.

These controls do not prove actual chart existence, exact field return,
normalization, a universal conductor theorem, a published LND theorem,
or original-ring recognition. Coefficient-field fixtures are not asserted
to be actual frames. This file imports no retained checker or solver.
The author does not execute, import, or compile the saved source.
"""

import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, W0 = sp.symbols("U V W0")


def hj(coefficient, order):
    return sum(
        sp.diff(coefficient, t, i, rho, order - i)
        * U**i * V**(order - i)
        / (sp.factorial(i) * sp.factorial(order - i))
        for i in range(order + 1)
    )


def mixed_potentials():
    k, n, ell, m = [sp.Function(name)(t, rho)
                    for name in ("k", "n", "ell", "m")]
    q = t**2 / rho
    f = hj(q, 2) + hj(k, 1) + n
    ret = sp.diff(f, V)
    third = hj(q, 3) + hj(k, 2) + hj(n, 1)
    remainder = ell - third
    middle = sp.diff(f, rho)
    fourth = (hj(q, 4) + hj(k, 3) + hj(n, 2)
              - sp.diff(ell, t) * U - sp.diff(ell, rho) * V - m)
    eliminant = (t**2 / rho**3 * remainder**2
                 + ret * middle * remainder + ret**2 * fourth)
    return k, n, ell, m, q, f, ret, third, middle, fourth, eliminant


def weighted_part(expression, variables, weights, weight):
    return sum(
        coefficient * sp.prod(variable**power
                              for variable, power in zip(variables, powers))
        for powers, coefficient in sp.Poly(sp.expand(expression), *variables).terms()
        if sum(power * unit for power, unit in zip(powers, weights)) == weight
    )


class MixedRatioControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.factor(sp.together(sp.expand(expression))), 0)

    def test_full_potentials_and_original_formal_gradients(self):
        k, n, ell, _, q, f, ret, third, middle, fourth, _ = mixed_potentials()
        j = rho * U - t * V
        self.assert_zero(hj(q, 2) - j**2 / rho**3)
        self.assert_zero(hj(q, 3) + V * j**2 / rho**4)
        self.assert_zero(hj(q, 4) - V**2 * j**2 / rho**5)
        self.assert_zero(ret - (sp.diff(k, rho) - 2 * t * j / rho**3))
        self.assert_zero(
            middle + (rho * U - 3 * t * V) * j / rho**4
            - sp.diff(k, t, rho) * U - sp.diff(k, rho, 2) * V
            - sp.diff(n, rho)
        )
        b1 = sp.diff(third, U) + sp.diff(ret, U) * W0
        c1 = sp.diff(third, V) + sp.diff(ret, V) * W0
        lt = sp.diff(ell, t) - sp.diff(third, t) - sp.diff(ret, t) * W0
        lr = sp.diff(ell, rho) - sp.diff(third, rho) - sp.diff(ret, rho) * W0
        potential = t**2 / rho**3 * W0**2 + middle * W0 + fourth
        self.assert_zero(b1 - sp.diff(f, t) - sp.diff(q, t, rho) * W0)
        self.assert_zero(c1 - sp.diff(f, rho) - sp.diff(q, rho, 2) * W0)
        self.assert_zero(sp.diff(potential, U) + lt)
        self.assert_zero(sp.diff(potential, V) + lr)
        self.assert_zero(sp.diff(potential, W0) - c1)
        # Dropping the mixed derivative would change an actual gradient.
        self.assert_zero(b1 - sp.diff(f, t) + 2 * t * W0 / rho**2)
        self.assertNotEqual(sp.diff(q, t, rho), 0)

        # Generic quotient-free gradient calculation, valid for either slot.
        aa, cc, rr, bb, ll, ww, rj, cj = sp.symbols("aa cc rr bb ll ww rj cj")
        tj = -bb + rj * ww
        qj = -ll - cj * ww
        derivative = (
            2 * aa * rr * ww * tj + rj * cc * rr * ww
            + rr**2 * cj * ww + rr * cc * tj
            + 2 * rr * rj * (-aa * ww**2 - cc * ww) + rr**2 * qj
        )
        self.assert_zero(derivative + rr * ((2 * aa * ww + cc) * bb + rr * ll))

    def test_wedge_sextic_top_and_finite_degree_controls(self):
        rr, bb, cc, lt, lr = sp.symbols("rr bb cc lt lr")
        yt, yr, yv, vt, vr, vv = sp.symbols("yt yr yv vt vr vv")
        wrow = [(-bb * yt - cc * vt + lt) / rr,
                (-bb * yr - cc * vr + lr) / rr,
                (-bb * yv - cc * vv) / rr]
        jacobian = sp.det(sp.Matrix([
            [yt, yr, yv], [rr * vt + bb, rr * vr + cc, rr * vv], wrow
        ]))
        du = rr * (yv * vr - yr * vv) + cc * yv
        dv = rr * (yt * vv - yv * vt) - bb * yv
        hu = -rr * (cc * bb + rr * lt)
        hv = -rr * (cc**2 + rr * lr)
        self.assert_zero(rr**3 * jacobian - du * hu - dv * hv)

        *_, eliminant = mixed_potentials()
        top = weighted_part(eliminant, (U, V), (1, 1), 6)
        self.assert_zero(top - t * V * (rho * U - t * V)**4
                         * (2 * rho * U - t * V) / rho**11)
        xi, v = sp.symbols("xi v")
        transformed = top.subs(U, xi + t * V / rho)
        self.assert_zero(transformed - t * xi**4 * V * (2 * rho * xi + t * V)
                         / rho**7)
        a20, a11, a02, a10, a01, a00 = sp.symbols("a20 a11 a02 a10 a01 a00")
        cubic_cofactor = (xi * V * (2 * rho * xi + t * V)
                         + a20 * xi**2 + a11 * xi * V + a02 * V**2
                         + a10 * xi + a01 * V + a00)
        quadratic_cofactor = V * (2 * rho * xi + t * V) + a10 * xi + a01 * V + a00
        for degree in (1, 2):
            evaluated = sp.Poly(cubic_cofactor.subs({xi: v**degree, V: v**3 + v}), v)
            self.assertEqual(evaluated.degree(), degree + 6)
            self.assert_zero(evaluated.LC() - t)
            self.assertGreater(degree + 6, 3 * degree)
            evaluated = sp.Poly(quadratic_cofactor.subs({xi: v**degree, V: v**4 + v}), v)
            self.assertEqual(evaluated.degree(), 8)
            self.assert_zero(evaluated.LC() - t)
            self.assertGreater(8, 3 * degree)
        # Finite gap arithmetic, not a test of the module/conductor theorem.
        small_semigroup = {3 * i + 4 * j for i in range(4) for j in range(4)}
        self.assertNotIn(5, small_semigroup)
        self.assertTrue({3, 4, 6, 7, 8}.issubset(small_semigroup))
        self.assertEqual(3 + 2, 5)
        # The conic really permits equal weighted orders across total degrees.
        self.assert_zero((xi**2 * V**2 - V**3).subs(V, xi**2))
        self.assertEqual(2 * 1 + 2 * 2, 3 * 2)

    def test_zero_return_scalar_and_nice_leading_row(self):
        k, n, _, _, q, f, ret, _, _, _, _ = mixed_potentials()
        p = t / rho
        xi, lam, omega, kap, zet = sp.symbols("xi lam omega kap zet")
        beta, tau, aa = sp.symbols("beta tau aa", nonzero=True)
        b1 = (sp.diff(f, t) + sp.diff(q, t, rho) * W0).subs(U, p * V + xi)
        slope = p * sp.diff(k, t, 2) + sp.diff(k, t, rho) - 2 * xi / rho**2
        intercept = sp.diff(k, t, 2) * xi + sp.diff(n, t)
        self.assert_zero(b1 - slope * V - intercept + 2 * p * W0 / rho)
        self.assert_zero(ret.subs(U, p * V + xi) - sp.diff(k, rho)
                         + 2 * t * xi / rho**2)
        self.assert_zero(b1.subs(W0, rho * (slope * V + intercept - beta) / (2 * p))
                         - beta)
        kap_raw = p * sp.diff(k, t) + sp.diff(k, rho) - p**2 * lam
        zet_raw = xi**2 / rho + sp.diff(k, t) * xi + n - p**2 * omega
        z_raw = (-p**2 * W0 + f).subs({U: p * V + xi, W0: lam * V + omega})
        self.assert_zero(z_raw - kap_raw * V - zet_raw)

        yt, yr, yv, wt, wr, wv, bb = sp.symbols("yt yr yv wt wr wv bb")
        scalar = sp.det(sp.Matrix([[yt, yr, yv], [bb, -p * bb, 0], [wt, wr, wv]]))
        self.assert_zero(scalar - bb * (yv * (wr + p * wt) - (yr + p * yt) * wv))
        # Formal coefficient chart only. Polynomiality and LND existence come
        # from the written actual proof, not from these differentiated rows.
        x, v, theta0, kval = sp.symbols("x v theta0 kval")
        nv = sp.symbols("nv", nonzero=True)
        theta = theta0 + nv * v
        y = p * theta + xi
        sigma = p**2 * theta + 2 * p * xi + kval
        coordinates = [x, y + t * x, kap * theta + zet + sigma * x + q * x**2,
                       lam * theta + omega + theta * x + rho * x**2]
        row = [sp.diff(value, v) * tau / nv for value in coordinates]
        expected = [0, tau * p, tau * (p**2 * x + kap), tau * (x + lam)]
        for actual, target in zip(row, expected):
            self.assert_zero(actual - target)
            self.assert_zero(sp.diff(actual, v))
        self.assert_zero(aa * sp.diff(row[3], x) - aa * tau)
        # These finite polynomial rows retain possible zero kappa or lambda;
        # the written highest-degree argument treats every polynomial degree.
        pp = sp.symbols("pp")
        for degree in range(4):
            ls = sp.symbols(f"l0:{degree + 1}")
            ms = sp.symbols(f"m0:{degree}")
            ns = sp.symbols(f"n0:{degree}")
            ll = sum(value * x**j for j, value in enumerate(ls))
            mm = sum(value * x**j for j, value in enumerate(ms))
            nn = sum(value * x**j for j, value in enumerate(ns))
            expression = sp.expand(ll * pp + mm * (pp**2 * x + kap) + nn * (x + lam))
            leading = ls[-1] * pp
            if degree:
                leading += ms[-1] * pp**2 + ns[-1]
            self.assert_zero(expression.coeff(x, degree) - leading)
            self.assert_zero(sp.diff(expression.coeff(x, degree), kap))
            self.assert_zero(sp.diff(expression.coeff(x, degree), lam))

    def test_quadratic_cofactor_radial_branches_and_actual_swap(self):
        rr, bb, cc, hp, pp, xv, wv = sp.symbols("rr bb cc hp pp xv wv")
        yt, yr, vt, vr = sp.symbols("yt yr vt vr")
        yv, vv = (1 + hp * pp) * xv, pp * xv
        du = rr * (yv * vr - yr * vv) + cc * yv
        dv = rr * (yt * vv - yv * vt) - bb * yv
        k0 = (-pp * (yv * vr - yr * vv)
              + (1 + hp * pp) * (yt * vv - yv * vt) + (1 + hp * pp) * wv)
        third_constraint = xv * ((1 + hp * pp) * bb + pp * cc) + rr * wv
        self.assert_zero(-pp * du + (1 + hp * pp) * dv - rr * k0
                         + (1 + hp * pp) * third_constraint)

        k, _, _, _, _, _, _, _, _, _, eliminant = mixed_potentials()
        h = t / rho
        radial = lambda expression: h * sp.diff(expression, t) + sp.diff(expression, rho)
        self.assert_zero(radial(h))
        kval = radial(radial(k)) / 2
        d3 = radial(radial(radial(k)))
        xi = sp.symbols("xi")
        transformed = eliminant.subs(U, xi + h * V)
        top = weighted_part(transformed, (xi, V), (1, 2), 8)
        expected = h**2 / rho * V**2 * (
            kval**2 * V**2 + (2 * kval / rho**2 + 2 * d3 / (3 * rho)) * xi**2 * V
            + xi**4 / rho**4)
        self.assert_zero(top - expected)
        kval0, alpha = sp.symbols("K alpha", nonzero=True)
        d30 = sp.symbols("D3")
        b0 = 2 * kval0 / rho**2 + 2 * d30 / (3 * rho)
        leading_equation = kval0**2 * alpha**2 + b0 * alpha + rho**-4
        derivative_equation = 2 * kval0**2 * alpha + b0
        radial_top = h**2 / rho * V**2 * (
            kval0**2 * V**2 + b0 * xi**2 * V + xi**4 / rho**4)
        self.assert_zero(radial_top.subs(V, alpha * xi**2)
                         - h**2 / rho * alpha**2 * leading_equation * xi**8)
        self.assert_zero(sp.diff(radial_top, V).subs(V, alpha * xi**2)
                         - h**2 / rho * (2 * alpha * leading_equation
                                          + alpha**2 * derivative_equation) * xi**6)
        for d3value, avalue in [(0, -1 / (kval0 * rho**2)),
                                (-6 * kval0 / rho, 1 / (kval0 * rho**2))]:
            self.assert_zero(leading_equation.subs({d30: d3value, alpha: avalue}))
            self.assert_zero(derivative_equation.subs({d30: d3value, alpha: avalue}))
        # K=0 would first force B0=0, leaving the nonzero constant rho^-4.
        self.assert_zero(leading_equation.subs({kval0: 0, d30: 0}) - rho**-4)
        self.assertNotEqual(rho**-4, 0)

        X, Y, Z, W, XP = sp.symbols("X Y Z W XP")
        swap = {X: Y, Y: X, Z: Z, W: W}
        for coordinate in (X, Y, Z, W):
            self.assert_zero(coordinate.subs(swap, simultaneous=True)
                             .subs(swap, simultaneous=True) - coordinate)
        self.assert_zero((Z * W - X**2 * Y**2).subs(swap, simultaneous=True)
                         - (Z * W - X**2 * Y**2))
        self.assertEqual([sp.diff(swap[coordinate], Z) for coordinate in (X, Y, Z, W)],
                         [0, 0, 1, 0])
        p1, p0, c3, c2, c1, c0, kt, kr, nn, kk = sp.symbols(
            "p1 p0 c3 c2 c1 c0 kt kr nn kk")
        theta = alpha * xi**2 + p1 * xi + p0
        y = xi + h * theta
        w = c3 * xi**3 + c2 * xi**2 + c1 * xi + c0
        sigma = 2 * h * y - h**2 * theta + kk
        z = -h**2 * w + xi**2 / rho + kt * xi + (h * kt + kr) * theta + nn
        old_w = w + theta * X + rho * X**2
        old_z = z + sigma * X + t**2 / rho * X**2
        returned_w = sp.expand(old_w.subs(X, (XP - y) / t))
        returned_z = sp.expand(old_z.subs(X, (XP - y) / t))
        thetap = -theta / t - 2 * xi / (h * t)
        yp = -y / t
        wp = w + xi * theta / t + rho * xi**2 / t**2
        zp = (-h**2 * wp + xi**2 / rho + (kt - kk / t) * xi
              + (h * kt + kr - kk / rho) * theta + nn)
        self.assert_zero(returned_w - (wp + thetap * XP + rho / t**2 * XP**2))
        self.assert_zero(returned_z.coeff(XP, 0) - zp)
        self.assert_zero(returned_z.coeff(XP, 2) - 1 / rho)
        self.assert_zero(yp - h * thetap - xi / t)
        self.assert_zero((1 / t) / (rho / t**2) - h)
        branch_one = {alpha: -1 / (kval0 * rho**2), c3: 1 / (kval0 * h * rho**3)}
        self.assert_zero(sp.diff(wp.subs(branch_one), xi, 3))
        self.assert_zero(sp.diff(zp.subs(branch_one), xi, 3))
        self.assert_zero(sp.diff(returned_z.subs(branch_one), xi, 3))
        self.assert_zero(sp.diff(returned_w.subs(branch_one), xi, 3))
        self.assert_zero(sp.diff(yp, xi, 3))
        self.assert_zero(sp.diff(thetap, xi, 3))

    def test_line_scalar_complex_slope_and_actual_slice_inverses(self):
        k, _, ell, _, _, _, ret, third, middle, fourth, _ = mixed_potentials()
        yy = sp.symbols("yy")
        theta = sp.Function("theta_constant")(t, rho)
        lam = sp.Function("lambda")(t, rho)
        omega = sp.Function("omega")(t, rho)
        zet = sp.Function("zeta")(t, rho)
        kap = sp.Function("kappa")(t, rho)
        w = lam * yy + omega
        evaluation = {U: yy, V: theta}
        third_row = ret.subs(evaluation) * w + third.subs(evaluation) - ell
        fourth_row = (t**2 / rho**3 * w**2
                      + middle.subs(evaluation) * w + fourth.subs(evaluation))
        e2 = (rho**2 * sp.diff(k, t, 2) - 4 * t * lam - 2 * theta) / (2 * rho**2)
        e3 = (rho**2 * sp.diff(k, t, 3) - 6 * lam) / (6 * rho**2)
        self.assert_zero(sp.expand(third_row).coeff(yy, 2) - e2)
        self.assert_zero(sp.expand(fourth_row).coeff(yy, 3) - e3)
        self.assert_zero(sp.diff(e2, t) - 3 * e3
                         - (lam - 2 * t * sp.diff(lam, t) - sp.diff(theta, t)) / rho**2)
        kap_raw = sp.diff(k, t) - 2 * t * theta / rho**2 - t**2 * lam / rho**2
        kap_t = sp.diff(kap_raw, t).subs({
            sp.diff(k, t, 2): (4 * t * lam + 2 * theta) / rho**2,
            sp.diff(theta, t): lam - 2 * t * sp.diff(lam, t)
        })
        self.assert_zero(kap_t - 3 * t**2 * sp.diff(lam, t) / rho**2)
        z = yy**2 / rho + kap * yy + zet
        scalar = sp.expand(sp.diff(z, t) * sp.diff(w, rho)
                           - sp.diff(z, rho) * sp.diff(w, t))
        self.assert_zero(scalar.coeff(yy, 3) - sp.diff(lam, t) / rho**2)
        after_t = sp.expand(scalar.subs({sp.diff(lam, t): 0, sp.diff(kap, t): 0}))
        self.assert_zero(after_t.coeff(yy, 2) - sp.diff(omega, t) / rho**2)
        after_omega = sp.expand(after_t.subs(sp.diff(omega, t), 0))
        self.assert_zero(after_omega.coeff(yy, 1) - sp.diff(zet, t) * sp.diff(lam, rho))
        self.assert_zero(after_omega.coeff(yy, 0) - sp.diff(zet, t) * sp.diff(omega, rho))

        # The two other line directions: one actual good-slot interchange,
        # and the essential quartic coefficient preceding the nice-row gate.
        v, nu, w2, w1, w0 = sp.symbols("v nu w2 w1 w0")
        swapped_theta = v / t - 2 * rho * (t * v / (2 * rho) + nu) / t**2
        self.assert_zero(swapped_theta + 2 * rho * nu / t**2)
        self.assert_zero(sp.diff(swapped_theta, v))
        line_eval = {U: t * V / rho + nu}
        wpoly = w2 * V**2 + w1 * V + w0
        fourth_line = (t**2 / rho**3 * wpoly**2
                       + middle.subs(line_eval) * wpoly + fourth.subs(line_eval))
        self.assert_zero(sp.expand(fourth_line).coeff(V, 4) - t**2 * w2**2 / rho**3)

        # Finite weighted-leading identities, not a test of the actual
        # irreducible-derivation lemma or transcendence of the leading ratio.
        speed, time, xx, uu = sp.symbols("speed time xx uu", nonzero=True)
        for weight in range(1, 6):
            coefficients = sp.symbols(f"c0:{weight // 2 + 1}")
            homogeneous = sum(coefficient * xx**(weight - 2 * j) * uu**j
                              for j, coefficient in enumerate(coefficients))
            result = homogeneous.subs({xx: speed * time, uu: speed**2 * rho * time**2})
            expected = speed**weight * time**weight * sum(
                coefficient * rho**j for j, coefficient in enumerate(coefficients))
            self.assert_zero(result - expected)

        # Both orders of the literal original shear followed by the slice
        # correction. F and G retain arbitrary dependence on the fixed base.
        X, Y, Z, W, UB, HB = sp.symbols("X Y Z W UB HB")
        lam0 = sp.symbols("lam0")
        dd = sp.symbols("dd", nonzero=True)
        fbase = sp.Function("F")
        gbase = sp.Function("G")
        uexpr = W - lam0 * Y
        hexpr = Z - fbase(X, uexpr) * Y**2 / (2 * dd) - gbase(X, uexpr) * Y / dd
        inverse_w = UB + lam0 * Y
        inverse_z = HB + fbase(X, UB) * Y**2 / (2 * dd) + gbase(X, UB) * Y / dd
        self.assert_zero(uexpr.subs(W, inverse_w) - UB)
        self.assert_zero(hexpr.subs({W: inverse_w, Z: inverse_z}, simultaneous=True) - HB)
        self.assert_zero(inverse_w.subs(UB, uexpr) - W)
        self.assert_zero(inverse_z.subs({UB: uexpr, HB: hexpr}, simultaneous=True) - Z)
        fixed_correction = Z - fbase(X, UB) * Y**2 / (2 * dd) - gbase(X, UB) * Y / dd
        derivation = lambda expression: (dd * sp.diff(expression, Y)
                                         + (fbase(X, UB) * Y + gbase(X, UB))
                                         * sp.diff(expression, Z))
        self.assert_zero(derivation(fixed_correction))
        self.assert_zero(derivation(Y / dd) - 1)
        self.assert_zero(derivation(derivation(derivation(Z))))
        self.assert_zero(derivation(X))
        self.assert_zero(derivation(UB))


if __name__ == "__main__":
    unittest.main()
