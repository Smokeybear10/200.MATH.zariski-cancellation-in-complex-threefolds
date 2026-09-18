"""Finite exact controls for the saved low-degree split-graph proof181.

Only the evaluated cofactor is assumed constant in the written proof.  The
literal eliminant below is not replaced by a pure linear graph equation.
Residual identities retain the first and second potentials until the exact
prior relation is explicitly imposed.  Coefficient jets are formal algebra,
not an assertion that an arbitrary formal chart is an actual split frame.

The full actual field-return contradiction, joint-constant arguments, and
regular-kernel recognition remain written proofs.  The polynomial coordinate
maps and both inverse orders are tested independently of those assertions.
No earlier checker or proof internal is imported.  Root owns the one canonical
execution after saved-source review; authoring entails no run or compilation.
These finite controls are not a formal proof or a novelty certification.
"""

import unittest

import sympy as sp


class SplitLowDegreeGraphControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_potential_residuals_and_evaluated_cofactor(self):
        U, V, r, ell, ell_t, ell_r, m = sp.symbols("U V r ell ell_t ell_r m")
        k20, k11, k02, k30, k21, k12, k03 = sp.symbols("k20 k11 k02 k30 k21 k12 k03")
        n10, n01, n20, n11, n02 = sp.symbols("n10 n01 n20 n11 n02")
        beta, chi, h, j = sp.symbols("beta chi h j")
        theta, w = beta * U + chi, h * U + j
        f = k20 * U**2 / 2 + k11 * U * V + k02 * V**2 / 2 + n10 * U + n01 * V
        g3 = (k30 * U**3 / 6 + k21 * U**2 * V / 2 + k12 * U * V**2 / 2
              + k03 * V**3 / 6 + n20 * U**2 / 2 + n11 * U * V + n02 * V**2 / 2)
        # These coefficient partials are independent symmetric Taylor jets.
        f_t = k30 * U**2 / 2 + k21 * U * V + k12 * V**2 / 2 + n20 * U + n11 * V
        f_r = k21 * U**2 / 2 + k12 * U * V + k03 * V**2 / 2 + n11 * U + n02 * V
        self.zero(sp.diff(g3, U) - f_t)
        self.zero(sp.diff(g3, V) - f_r)
        R = r - U
        F = sp.diff(f, V).subs(V, theta)
        first = R * w + f.subs(V, theta) - ell
        second = F * w + g3.subs(V, theta) - ell_t * U - ell_r * theta - m
        eliminant = R * (g3 - ell_t * U - ell_r * V - m) + sp.diff(f, V) * (ell - f)
        B1 = sp.diff(f, U).subs(V, theta) - w
        C_t = f_t.subs(V, theta) + k11 * w - ell_t
        C_r = f_r.subs(V, theta) + k02 * w - ell_r
        # Exact errors before either potential is assumed.  Thus the test
        # does not silently identify eliminant with a pure graph equation.
        self.zero(sp.diff(eliminant, U).subs(V, theta)
                  - (R * C_t - F * B1) + second + k11 * first)
        self.zero(sp.diff(eliminant, V).subs(V, theta)
                  - (R * C_r - F**2) + k02 * first)
        cubic_second = (k30 + 3 * beta * k21 + 3 * beta**2 * k12 + beta**3 * k03) / 6
        self.zero(sp.expand(second).coeff(U, 3) - cubic_second)

        T = k11 + beta * k02
        epsilon = k02 * chi + n01
        h_value = (k20 + 2 * beta * k11 + beta**2 * k02) / 2
        j_value = r * h_value + T * chi + n10 + beta * n01
        ell_value = r * j_value + k02 * chi**2 / 2 + n01 * chi
        prior_first = {h: h_value, j: j_value, ell: ell_value}
        self.zero(first.subs(prior_first, simultaneous=True))
        self.zero(F - (T * U + epsilon))
        self.zero(B1.subs({h: h_value, j: j_value}, simultaneous=True)
                  + beta * F + R * h_value)

        # Rebuild the differentiated first potential using independent
        # coefficient jets.  Its derivative, not a purity assumption,
        # supplies C_i = -R*w_i-F*theta_i.
        T, epsilon, h, beta = sp.symbols("T epsilon h beta")
        hr, jr, br, cr, bt = sp.symbols("hr jr br cr bt")
        S = sp.Symbol("S")
        F = T * U + epsilon
        d0 = r * T + epsilon
        gradient_v = -R**2 * (hr * U + jr) - R * F * (br * U + cr) - F**2
        shifted = sp.expand(gradient_v.subs(U, r - S))
        self.zero(shifted.coeff(S, 3) - (hr - T * br))
        reduced = sp.expand(shifted.subs(hr, T * br))
        expected = (-d0**2 + d0 * (2 * T - r * br - cr) * S
                    + (epsilon * br - jr + T * (r * br + cr) - T**2) * S**2)
        self.zero(reduced - expected)
        rho_prior = {cr: 2 * T - r * br, jr: epsilon * br + T**2}
        self.zero(reduced.subs(rho_prior, simultaneous=True) + d0**2)
        # The written unit-ideal input is d0 != 0.  It is that input which
        # permits coefficient forcing; this finite identity does not prove it.
        W = bt + beta * br
        ht, hr = T * bt, T * br
        ct, cr = h - 2 * beta * T - r * bt, 2 * T - r * br
        jt, jr = epsilon * bt - beta * T**2, epsilon * br + T**2
        Dh, Dj, Dchi = ht + beta * hr, jt + beta * jr, ct + beta * cr
        self.zero(Dh - T * W)
        self.zero(Dj - epsilon * W)
        self.zero(Dchi - (h - r * W))
        self.zero(R * (Dh * U + Dj) + F * (W * U + Dchi - h))

    def test_mixed_derivatives_and_zero_direction_residuals(self):
        t, rho, y = sp.symbols("t rho y")
        beta, r, h = [sp.Function(name)(t, rho) for name in ("beta", "r", "h")]
        T = sp.diff(r, t) + beta * sp.diff(r, rho)
        W = sp.diff(beta, t) + beta * sp.diff(beta, rho)
        DT = sp.diff(T, t) + beta * sp.diff(T, rho)
        chi_t = h - 2 * beta * T - r * sp.diff(beta, t)
        chi_r = 2 * T - r * sp.diff(beta, rho)
        mixed = sp.diff(chi_t, rho) - sp.diff(chi_r, t)
        self.zero(mixed - (sp.diff(h, rho) - T * sp.diff(beta, rho))
                  + sp.diff(r, rho) * W + 2 * DT)
        second_r = (sp.diff(r, t, 2) + 2 * beta * sp.diff(r, t, rho)
                    + beta**2 * sp.diff(r, rho, 2))
        self.zero(DT - second_r - sp.diff(r, rho) * W)
        mixed_prior = {
            sp.diff(h, rho): T * sp.diff(beta, rho),
            sp.diff(r, t, 2): -2 * beta * sp.diff(r, t, rho) - beta**2 * sp.diff(r, rho, 2),
        }
        self.zero(mixed.subs(mixed_prior, simultaneous=True) + 3 * sp.diff(r, rho) * W)

        # Independent differentiation of h's first-potential formula uses
        # r=k_rho, with no unrelated coefficient derivative discarded.
        k = sp.Function("k")(t, rho)
        rk = sp.diff(k, rho)
        Tk = sp.diff(rk, t) + beta * sp.diff(rk, rho)
        hk = (sp.diff(k, t, 2) + 2 * beta * sp.diff(rk, t)
              + beta**2 * sp.diff(rk, rho)) / 2
        rk_second = (sp.diff(rk, t, 2) + 2 * beta * sp.diff(rk, t, rho)
                     + beta**2 * sp.diff(rk, rho, 2))
        self.zero(2 * (sp.diff(hk, rho) - Tk * sp.diff(beta, rho)) - rk_second)

        # Under W=0 the written proof derives Dh=Dj=0 and Dtheta=h.
        # The following is the remaining exact Dz cancellation.  Concluding
        # that D vanishes on the whole field requires actual field return,
        # which is intentionally not replaced by a finite formal example.
        beta0, chi, h0, r0, T0, nt, nr = sp.symbols("beta0 chi h0 r0 T0 nt nr")
        j0 = r0 * h0 + T0 * chi + nt + beta0 * nr
        w0 = h0 * y + j0
        Dz = ((2 * h0 - beta0 * T0) * y + T0 * (beta0 * y + chi)
              + (r0 - y) * h0 + nt + beta0 * nr - w0)
        self.zero(Dz)
        self.zero(sp.diff(t, t) + beta * sp.diff(t, rho) - 1)
        self.zero(sp.diff(y, t) + beta * sp.diff(y, rho))

        # Compatibility of the two j partials isolates s_rho*W after the
        # first n equation, rather than assuming n is rho-linear in advance.
        mu = sp.Symbol("mu")
        s = sp.Function("s")(t, rho)
        jt = s * sp.diff(beta, t) - beta * mu**2
        jr = s * sp.diff(beta, rho) + mu**2
        Fs = sp.diff(s, t) + beta * sp.diff(s, rho) + mu**2
        self.zero(sp.diff(jt, rho) - sp.diff(jr, t)
                  - sp.diff(s, rho) * W + Fs * sp.diff(beta, rho))

    def test_actual_translation_shear_and_invariant_coordinate(self):
        t, rho, mu, nu, h0, k1, k00, n1, n00 = sp.symbols("t rho mu nu h0 k1 k00 n1 n00")
        d = sp.Symbol("d", nonzero=True)
        r = mu * t + nu
        s0 = d - mu * nu
        k0 = h0 * t**2 + k1 * t + k00
        n0 = -mu * h0 * t**2 + n1 * t + n00
        k, n = r * rho + k0, (-mu**2 * t + s0) * rho + n0
        kb = k - r * rho
        nb = n - mu * k + r * sp.diff(k, t) + mu * r * rho
        A0, B0, C0 = h0, k1, k00
        D0, F0 = n1 + 2 * nu * h0, n00 - mu * k00 + nu * k1
        self.zero(kb - (A0 * t**2 + B0 * t + C0))
        self.zero(nb - (d * rho + D0 * t + F0))
        self.zero(sp.diff(nb, t, 2))

        X, Y, Z, W = sp.symbols("X Y Z W")
        original = (X, Y, Z, W)
        translated = (X + mu, Y - nu, Z, W)
        translation_inverse = (X - mu, Y + nu, Z, W)
        for expression, target in zip(translated, original):
            self.zero(expression.subs(dict(zip(original, translation_inverse)), simultaneous=True) - target)
        for expression, target in zip(translation_inverse, original):
            self.zero(expression.subs(dict(zip(original, translated)), simultaneous=True) - target)

        # The actual affine translation agrees with all literal chart jets.
        x, xb, y, theta, w = sp.symbols("x xb y theta w")
        sigma = -t * theta - rho * y + k
        z = sp.diff(k, t) * y + (r - y) * theta + n - t * w
        old_Y, old_Z, old_W = y + t * x, z + sigma * x - t * rho * x**2, w + theta * x + rho * x**2
        yb, theta_b, wb = y - r, theta - 2 * mu * rho, w - mu * theta + mu**2 * rho
        sigma_b, zb = sigma + 2 * mu * t * rho, z - mu * sigma - mu**2 * t * rho
        new_chart = (yb + t * xb, zb + sigma_b * xb - t * rho * xb**2,
                     wb + theta_b * xb + rho * xb**2)
        for old, new in zip((old_Y - nu, old_Z, old_W), new_chart):
            self.zero(old.subs(x, xb - mu) - new)
            self.zero(new.subs(xb, x + mu) - old)
        self.zero(sigma_b - (-t * theta_b - rho * yb + kb))
        self.zero(zb + t * wb - (sp.diff(kb, t) * yb - yb * theta_b + nb))

        c0 = sp.Symbol("c0")
        Hsp = X * Z + Y * W
        Fgood = C0 * X**2 + B0 * X * Y + A0 * Y**2 + F0 * X + D0 * Y
        P0 = (Fgood - Hsp) / d
        shear = (X, Y, Z - Y * P0, W + X * P0)
        shear_inverse = (X, Y, Z + Y * P0, W - X * P0)
        self.zero(shear[0] * shear[2] + shear[1] * shear[3] - Hsp)
        for expression, target in zip(shear, original):
            self.zero(expression.subs(dict(zip(original, shear_inverse)), simultaneous=True) - target)
        for expression, target in zip(shear_inverse, original):
            self.zero(expression.subs(dict(zip(original, shear)), simultaneous=True) - target)

        # Include the final invariant-coordinate shear, not only a nice frame.
        coordinate_map = (X, Y, shear[2], shear[3] - h0 * Y - c0 * X)
        W1 = W + h0 * Y + c0 * X
        P1 = (Fgood - (X * Z + Y * W1)) / d
        coordinate_inverse = (X, Y, Z + Y * P1, W1 - X * P1)
        for expression, target in zip(coordinate_map, original):
            self.zero(expression.subs(dict(zip(original, coordinate_inverse)), simultaneous=True) - target)
        for expression, target in zip(coordinate_inverse, original):
            self.zero(expression.subs(dict(zip(original, coordinate_map)), simultaneous=True) - target)

        # This last formal chart asserts no new actual realization.  It
        # verifies the literal invariant return once the proved normalized
        # low-graph coefficients are imposed, with beta still independent.
        beta = sp.Symbol("beta")
        kn, nn = A0 * t**2 + B0 * t + C0, d * rho + D0 * t + F0
        theta_n, wn = beta * y + h0 * t + c0, h0 * y + d * beta + D0
        zn = sp.diff(kn, t) * y - y * theta_n + nn - t * wn
        sn = -t * theta_n - rho * y + kn
        chart = (x, y + t * x, zn + sn * x - t * rho * x**2, wn + theta_n * x + rho * x**2)
        chart_subs = dict(zip(original, chart))
        Px = sp.expand(P0.subs(chart_subs, simultaneous=True))
        self.zero(Px + beta * y + rho * x)
        self.zero(sp.diff(Px, x) + rho)
        self.zero(sp.diff(Px, x, 2))
        for expression in shear:
            self.zero(sp.diff(expression.subs(chart_subs, simultaneous=True), x, 2))
        W1x = sp.expand(shear[3].subs(chart_subs, simultaneous=True))
        Ix = sp.expand(coordinate_map[3].subs(chart_subs, simultaneous=True))
        self.zero(W1x - (wn + (h0 * t + c0) * x))
        self.zero(Ix - (d * beta + D0))
        self.zero(sp.diff(Ix, x))


if __name__ == "__main__":
    unittest.main()
