"""Finite algebra controls for301 together with its separate correction.

This source is standalone and does not import a retained proof or checker.
It checks polynomial/rational identities, not exact-field constants, plane
classification, primitive derivations, or the retained recognition theorem.
The false fixed-Y assertion is an explicit negative control.  The author
does not execute, import, or compile this file; Root owns any canonical run.
"""

import unittest

import sympy as sp


class AffineSecondPotentialControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.factor(sp.cancel(expression)), 0)

    def test_full_coefficient_parameter_change(self):
        t, r, U, P, V = sp.symbols("t r U P V")
        H = sp.Function("H")(t, r)
        L = sp.Function("L")(t, r)
        ht, hr = sp.diff(H, t), sp.diff(H, r)

        def old_t(expression):
            return sp.diff(expression, t) - ht * sp.diff(expression, r) / hr

        def old_s(expression):
            return sp.diff(expression, r) / hr

        a, b, h = old_t(r), old_s(r), L / hr
        self.zero(a + ht / hr)
        self.zero(b * hr - 1)
        self.zero(old_t(H))
        self.zero(old_s(H) - 1)
        self.zero(old_s(a) - old_t(b))
        theta = (U**2 - a * P - h) / b
        self.zero(theta - (hr * U**2 + ht * P - L))

        hessian = old_t(a) * P**2 / 2 + old_s(a) * P * V
        hessian += old_s(b) * V**2 / 2
        old_Q = (-a + 2 * b * P) * U - hessian
        old_Q -= old_t(h) * P + old_s(h) * V
        transformed = sp.cancel(hr * old_Q.subs(V, theta))
        transformed -= transformed.subs({U: 0, P: 0}, simultaneous=True)
        expected = sp.diff(H, r, 2) * U**4 / 2
        expected += sp.diff(H, t, r) * U**2 * P
        expected += sp.diff(H, t, 2) * P**2 / 2 + 2 * U * P
        expected += ht * U - sp.diff(L, r) * U**2 - sp.diff(L, t) * P
        self.zero(transformed - expected)
        self.zero(sp.diff(transformed, U) - sp.diff(expected, U))
        self.zero(sp.diff(transformed, P) - sp.diff(expected, P))
        self.assertNotEqual(sp.expand(expected).coeff(U, 1).coeff(P, 1), 0)

    def test_correct_actual_row_and_constant_first_scalar(self):
        X, t, s, P, c0, a, b, h0, tau, ell = sp.symbols(
            "X t s P c0 a b h0 tau ell", nonzero=True
        )
        theta = (c0**2 - a * P - h0) / b
        intercept_z = 2 * t * c0 + P**2 + theta
        intercept_w = ell - 2 * P * c0
        Y = c0 + P * X + t * X**2
        Z = intercept_z + (2 * t * P + s) * X + t**2 * X**2
        W = intercept_w + theta * X + s * X**2
        rows = [tau * sp.diff(f, P) for f in (Y, Z, W)]
        self.zero(rows[0] - tau * X)
        self.assertNotEqual(sp.expand(rows[0]), 0)  # The invalid301 premise.
        self.zero(rows[1] - tau * (2 * P - a / b + 2 * t * X))
        self.zero(rows[2] - tau * (-2 * c0 - a * X / b))
        self.zero(tau * sp.diff(rows[1], P) - 2 * tau**2)
        self.zero(tau * sp.diff(rows[2], P))

        t, r, P = sp.symbols("t r P")
        H, L, c = [sp.Function(name)(t, r) for name in ("H", "L", "c")]
        z = P**2 + sp.diff(H, t) * P + sp.diff(H, r) * c**2 + 2 * t * c - L
        w = r - 2 * c * P
        actual = sp.det(sp.Matrix([[sp.diff(f, q) for q in (t, r, P)] for f in (c, z, w)]))
        gate0 = sp.diff(H, t, 2)
        gate1 = sp.diff(H, t, r) * c**2 + 2 * c - sp.diff(L, t)
        scalar = -sp.diff(c, t) * (
            2 * (1 + c * sp.diff(H, t, r)) * P
            + sp.diff(H, t)
            + 2 * c * (sp.diff(H, r, 2) * c**2 - sp.diff(L, r))
        )
        residual = 2 * c * sp.diff(c, r) * (gate0 * P + gate1)
        self.zero(actual - scalar - residual)
        Q = sp.diff(H, r, 2) * c**4 / 2 + sp.diff(H, t, r) * c**2 * P
        Q += sp.diff(H, t, 2) * P**2 / 2 + 2 * c * P + sp.diff(H, t) * c
        Q -= sp.diff(L, r) * c**2 + sp.diff(L, t) * P
        self.zero(sp.expand(Q).coeff(P, 2) - gate0 / 2)
        self.zero(sp.expand(Q).coeff(P, 1) - gate1)
        self.zero(sp.expand(scalar).coeff(P, 1) + 2 * sp.diff(c, t) * (1 + c * sp.diff(H, t, r)))
        self.zero(sp.diff(c * sp.diff(H, t, r) + 1, t)
                  - sp.diff(c, t) * sp.diff(H, t, r) - c * sp.diff(gate0, r))
        self.assertNotEqual(sp.expand(residual), 0)  # Lower potential gates matter.

        ht, hr, vt, vr, pv, a0 = sp.symbols("ht hr vt vr pv a0", nonzero=True)
        change = sp.Matrix([[1, 0, 0], [ht, hr, 0], [vt, vr, 1 / pv]])
        self.zero(change.det() - hr / pv)
        self.zero(-a0**4 * change.det() + a0**4 * hr / pv)
        self.assertNotEqual(sp.cancel(change.det() - pv / hr), 0)

    def test_raw_conic_row_and_fifth_coefficient(self):
        t, r, x, c = sp.symbols("t r x c")
        b, d, f = [sp.Function(name)(t) for name in ("b", "d", "f")]
        y = sp.Function("y")(t, r, x)
        sigma = b * y + x
        z = sigma**2 + sp.diff(f, t) * sigma + c * y**2 + 2 * t * y - b * r - d
        w = r - 2 * sigma * y
        raw = sp.det(sp.Matrix([[sp.diff(g, q) for q in (t, r, x)] for g in (y, z, w)]))
        l = sp.diff(b, t) * r + sp.diff(d, t)
        row = -(2 * x + sp.diff(f, t)) * sp.diff(y, t)
        row -= 2 * y * (2 * x / b + l) * sp.diff(y, r)
        row += (sp.diff(b, t) * (2 * x + sp.diff(f, t)) * y - 2 * x / b - l) * sp.diff(y, x)
        self.zero((raw - row).subs(sp.diff(f, t, 2), -2 / b))

        x, r, b, bp, bpp, fp, dp, dpp, q0, qt, qr = sp.symbols(
            "x r b bp bpp fp dp dpp q0 qt qr"
        )
        l = bp * r + dp
        D = fp - b * l
        A = x**2 / b + l * x + q0
        At = -bp * x**2 / b**2 + (bpp * r + dpp) * x + qt
        Ar = bp * x + qr
        Dt = -2 / b - bp * l - b * (bpp * r + dpp)
        Dr = -b * bp
        Tx, Rx = sp.diff(A, x), 2 * x + fp
        yp = A / D
        yt, yr, yx = (At * D - A * Dt) / D**2, (Ar * D - A * Dr) / D**2, Tx / D
        J = -Rx * yt - 2 * yp * Tx * yr + (bp * Rx * yp - Tx) * yx
        numerator = sp.cancel(D**3 * J)
        expected = -Rx * (At * D - Dt * A) * D
        expected -= 2 * A * Tx * (Ar * D + b * bp * A)
        expected += bp * Rx * A * Tx * D - Tx**2 * D**2
        self.zero(numerator - expected)
        coefficient = sp.Poly(sp.expand(numerator), x).coeff_monomial(x**5)
        self.zero(coefficient + 4 * bp / b**2)
        self.assertEqual(sp.Poly(sp.expand(numerator), x).degree(), 5)
        self.zero(coefficient.subs(bp, 0))
        wrong_yr = Ar / D  # Incorrectly freezing the denominator in r.
        wrong = -Rx * yt - 2 * yp * Tx * wrong_yr + (bp * Rx * yp - Tx) * yx
        self.assertNotEqual(sp.cancel(D**3 * (J - wrong)), 0)

    def test_full_actual_maps_and_both_inverse_orders(self):
        X, Y, Z, W, c, f0, f1, f2 = sp.symbols("X Y Z W c f0 f1 f2")
        R = Y**2 + X * W - X**2 * Z
        forward_z, forward_w = Z - c * R, W - c * X * R
        self.zero(Y**2 + X * forward_w - X**2 * forward_z - R)
        z1, w1 = sp.symbols("z1 w1")
        R1 = Y**2 + X * w1 - X**2 * z1
        inverse_z, inverse_w = z1 + c * R1, w1 + c * X * R1
        forward = {z1: forward_z, w1: forward_w}
        self.zero(inverse_z.subs(forward, simultaneous=True) - Z)
        self.zero(inverse_w.subs(forward, simultaneous=True) - W)
        inverse = {Z: inverse_z, W: inverse_w}
        self.zero(forward_z.subs(inverse, simultaneous=True) - z1)
        self.zero(forward_w.subs(inverse, simultaneous=True) - w1)
        self.assertNotEqual(sp.expand(Y**2 + X * W - X**2 * forward_z - R), 0)
        w2 = sp.symbols("w2")
        triangular = w1 - f2 * z1 - f1 * Y - f0 * X**2
        triangular_inverse = w2 + f2 * z1 + f1 * Y + f0 * X**2
        self.zero(triangular.subs(w1, triangular_inverse) - w2)
        self.zero(triangular_inverse.subs(w2, triangular) - w1)

        t, r, y, P, L = sp.symbols("t r y P L")
        f, ft = f2 * t**2 + f1 * t + f0, 2 * f2 * t + f1
        s = c * r + f
        theta = c * y**2 + ft * P - L
        z = P**2 + ft * P + c * y**2 + 2 * t * y - L
        w = r - 2 * P * y
        actual_Y = y + P * X + t * X**2
        actual_Z = z + (2 * t * P + s) * X + t**2 * X**2
        actual_W = w + theta * X + s * X**2
        literal = {Y: actual_Y, Z: actual_Z, W: actual_W}
        self.zero(R.subs(literal, simultaneous=True) - y**2 - r * X)
        actual_z1 = sp.expand(forward_z.subs(literal, simultaneous=True))
        actual_w1 = sp.expand(forward_w.subs(literal, simultaneous=True))
        self.zero(actual_z1.coeff(X, 2) - t**2)
        self.zero(actual_w1.coeff(X, 2) - f)
        actual_w2 = sp.expand(actual_w1 - f2 * actual_z1 - f1 * actual_Y - f0 * X**2)
        self.zero(sp.diff(actual_w2, X, 2))
        omitted_constant = sp.expand(actual_w1 - f2 * actual_z1 - f1 * actual_Y)
        self.zero(omitted_constant.coeff(X, 2) - f0)


if __name__ == "__main__":
    unittest.main()
