#!/usr/bin/env python3
"""Standalone finite algebra controls for the restricted note270.

These controls rebuild coefficient, completion, literal-potential and scalar
parity identities. They do not prove actual chart entry, the evaluated-unit
cofactor theorem, the exact constant-field integration, the strong field
return, or recognition. Polynomial primitives below test ordinary algebra,
not descent from a finite field extension. No retained checker is imported.
The generic jets and plane fixtures are not asserted to be actual frames.
"""

import unittest

import sympy as S


def polynomial_and_jet(prefix, degree, variable):
    """Independent coefficient values and their first coefficient derivatives."""
    coefficients = S.symbols(f"{prefix}_0:{degree + 1}")
    derivatives = S.symbols(f"{prefix}t_0:{degree + 1}")
    return (
        sum(value * variable**j for j, value in enumerate(coefficients)),
        sum(value * variable**j for j, value in enumerate(derivatives)),
    )


class QuadraticFirstQuarticControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(S.cancel(S.expand(expression)), 0)

    def assert_degree_at_most(self, expression, variable, degree):
        self.assertLessEqual(S.Poly(S.cancel(expression), variable).degree(), degree)

    def test_discriminant_u2_and_parameter_polynomiality(self):
        lam, U, V = S.symbols("lam U V")
        m, N = S.symbols("m N", nonzero=True)
        mt, mtt, k0tt = S.symbols("mt mtt k0tt")
        Nt, Ntt = S.symbols("Nt Ntt")
        n1, n1t, n1tt, n0t, n0tt = S.symbols("n1 n1t n1tt n0t n0tt")
        M = mtt / 2 - mt**2 / m
        nu = N * lam + n1
        nt = Nt * lam**2 / 2 + n1t * lam + n0t
        ntt = Ntt * lam**2 / 2 + n1tt * lam + n0tt
        ktt = mtt * lam + k0tt
        b1 = Nt * lam + n1t - 2 * nu * mt / m
        c2 = ntt / 2 - ktt * nu / (2 * m) - nt * mt / m

        ell_lam = S.symbols("ell_lam")
        b0 = -ell_lam - nu**2 / m
        c4 = M**2 / (2 * N)
        c3, c1, c0 = S.symbols("c3 c1 c0")
        H = N * V**2 / 2 + (M * U**2 + b1 * U + b0) * V
        H += c4 * U**4 + c3 * U**3 + c2 * U**2 + c1 * U + c0
        discriminant = S.discriminant(H, V)
        raw_u2 = S.expand(discriminant).coeff(U, 2)
        self.assert_zero(raw_u2 - (b1**2 - 2 * M * ell_lam - 2 * M * nu**2 / m - 2 * N * c2))
        self.assert_zero(S.expand(discriminant).coeff(U, 4))

        solved = S.cancel((b1**2 - 2 * M * nu**2 / m - 2 * N * c2) / (2 * M))
        self.assert_zero(raw_u2.subs(ell_lam, solved))
        self.assert_degree_at_most(solved, lam, 2)
        coefficients = S.Poly(solved, lam)
        primitive = S.symbols("ell_constant") + sum(
            coefficients.nth(j) * lam**(j + 1) / (j + 1) for j in range(3)
        )
        self.assert_zero(S.diff(primitive, lam) - solved)
        self.assert_degree_at_most(primitive, lam, 3)

        # Independent arbitrary cubic jets control the resulting D1 degree.
        ell, ell_t = polynomial_and_jet("ell", 3, lam)
        b0_poly = -S.diff(ell, lam) - nu**2 / m
        c1_poly = ell * mt / m - ell_t - nu * nt / m
        D1 = 2 * b1 * b0_poly - 2 * N * c1_poly
        self.assert_degree_at_most(b0_poly, lam, 2)
        self.assert_degree_at_most(c1_poly, lam, 3)
        self.assert_degree_at_most(D1, lam, 3)

    def test_square_completion_and_exact_affine_parameter(self):
        U, V, parameter, x = S.symbols("U V parameter x")
        N, a, beta = S.symbols("N a beta", nonzero=True)
        p2, p1, p0, center = S.symbols("p2 p1 p0 center")
        P2 = p2 * U**2 + p1 * U + p0
        H = N * ((V - P2)**2 - beta**2 * (U - center) / a) / 2
        B = S.expand(H).coeff(V, 1)
        C = H.subs(V, 0)
        discriminant = S.discriminant(H, V)
        d, c = N**2 * beta**2 / a, -N**2 * beta**2 * center / a
        self.assert_zero(discriminant - d * U - c)
        self.assert_zero(2 * N * H - ((N * V + B)**2 - discriminant))

        y = a * parameter**2 + center
        psi = P2.subs(U, y) + beta * parameter
        affine_x = N * psi + B.subs(U, y)
        self.assert_zero(affine_x - N * beta * parameter)
        self.assertEqual(S.Poly(affine_x, parameter).degree(), 1)
        self.assert_zero(H.subs({U: y, V: psi}, simultaneous=True))
        self.assert_zero(affine_x**2 - d * y - c)
        self.assert_zero(((x**2 - c) / d).subs(x, affine_x) - y)
        self.assert_zero(affine_x.subs(parameter, x / (N * beta)) - x)

        # Losing the odd parameter is a genuine failure of the whole-line gate.
        even_psi = P2.subs(U, y)
        self.assert_zero(N * even_psi + B.subs(U, y))
        self.assert_zero(even_psi.subs(parameter, -parameter) - even_psi)
        self.assert_zero(y.subs(parameter, -parameter) - y)

    def test_literal_potentials_and_actual_two_parameter_polynomial(self):
        t, lam, U, theta, z, X, Y, Z = S.symbols("t lam U theta z X Y Z")
        q, r, m, N, k0, n1, n0 = (
            S.Function(name)(t) for name in ("q", "r", "m", "N", "k0", "n1", "n0")
        )
        ell_coefficients = [S.Function(f"ell{j}")(t) for j in range(4)]
        ell = sum(value * lam**j for j, value in enumerate(ell_coefficients))
        k = m * lam + k0
        n = N * lam**2 / 2 + n1 * lam + n0
        nu = S.diff(n, lam)
        f = (S.diff(q, t, 2) - S.diff(r, t, 2) * m) * U**2 / 2 + S.diff(k, t) * U + n
        potential = (
            (S.diff(q, t, 3) - m * S.diff(r, t, 3) - 3 * S.diff(r, t, 2) * S.diff(m, t)) * U**3 / 6
            + (S.diff(k, t, 2) - S.diff(r, t, 2) * nu) * U**2 / 2
            + S.diff(n, t) * U
        )
        raw_w = (ell - (S.diff(m, t) * U + nu) * theta - potential) / m
        solved_w = ell / m - (S.diff(m, t) * U + nu) * (z - f) / m**2 - potential / m
        self.assert_zero(raw_w.subs(theta, (z - f) / m) - solved_w)
        self.assert_degree_at_most(solved_w, lam, 3)

        e = 1 / m
        Aw = S.diff(e, t) * U - nu * e**2
        Bw = e * ell - Aw * f - e * potential
        self.assert_zero(solved_w - Aw * z - Bw)
        for j in range(4):
            self.assert_degree_at_most(S.expand(Bw).coeff(U, j), lam, 3 - j)

        yhat = Y - t * X
        zhat = Z - (S.diff(q, t) * yhat + k) * X - q * X**2
        theta_hat = (zhat - f.subs(U, yhat)) / m
        W_poly = solved_w.subs({U: yhat, z: zhat}, simultaneous=True)
        W_poly += theta_hat * X + (S.diff(r, t) * yhat + lam) * X**2 + r * X**3
        self.assert_degree_at_most(W_poly, lam, 3)
        # Compare after the literal forward map, not a presumed ambient shear.
        forward_Y = U + t * X
        forward_Z = m * theta + f + (S.diff(q, t) * U + k) * X + q * X**2
        expected_W = raw_w + theta * X + (S.diff(r, t) * U + lam) * X**2 + r * X**3
        self.assert_zero(W_poly.subs({Y: forward_Y, Z: forward_Z}, simultaneous=True) - expected_W)

    def test_full_generic_scalar_odd_part_and_missing_ct_control(self):
        U, x = S.symbols("U x")
        d, h, e = S.symbols("d h e", nonzero=True)
        dt, dl, c, ct, cl, ht, et, ett = S.symbols("dt dl c ct cl ht et ett")
        p, pt, u, ut, ul, v, vt, vl, a0, a0t = S.symbols("p pt u ut ul v vt vl a0 a0t")
        b = S.symbols("b0:4")
        bt = S.symbols("bt0:4")
        bl = S.symbols("bl0:3")
        P = p * U**2 + u * U + v
        Pt, Pl = pt * U**2 + ut * U + vt, ul * U + vl
        A, At, Al = et * U + a0, ett * U + a0t, -e / h
        B = sum(value * U**j for j, value in enumerate(b))
        Bt = sum(value * U**j for j, value in enumerate(bt))
        Bl = sum(value * U**j for j, value in enumerate(bl))
        z = h * x + P

        # Differentiate the literal maps y=(x²-c)/d,z=h*x+P(y),w=A(y)z+B(y).
        yt, yl, yx = -(dt * U + ct) / d, -(dl * U + cl) / d, 2 * x / d
        zt = ht * x + Pt + S.diff(P, U) * yt
        zl = Pl + S.diff(P, U) * yl
        zx = h + S.diff(P, U) * yx
        extra = S.diff(A, U) * z + S.diff(B, U)
        wt = At * z + A * zt + Bt + extra * yt
        wl = Al * z + A * zl + Bl + extra * yl
        wx = A * zx + extra * yx
        determinant = S.Matrix([[yt, yl, yx], [zt, zl, zx], [wt, wl, wx]]).det()
        reduced = S.rem(S.Poly(S.expand(determinant), x), S.Poly(x**2 - d * U - c, x)).as_expr()

        V0, T0 = Bl - e * P / h, At * P + Bt
        odd_polynomial = (
            Pt * V0 - Pl * T0 - h**2 * At * (dl * U + cl) / 2
            - e * h * (dt * U + ct) / 2 - e * ht * (d * U + c)
        )
        self.assert_zero(S.expand(reduced).coeff(x, 1) - 2 * odd_polynomial / d)
        gate = -e * ht * d - e * h * dt / 2
        gate += S.expand(Pt * V0 - Pl * T0).coeff(U, 1)
        gate -= h**2 * (ett * cl + a0t * dl) / 2
        self.assert_zero(S.expand(odd_polynomial).coeff(U, 1) - gate)
        self.assertFalse(gate.has(c, ct))
        self.assert_zero(S.diff(gate, cl) + h**2 * ett / 2)

        # c_t is absent only from the linear-U gate, not from full scalar parity.
        self.assert_zero(S.diff(odd_polynomial, ct) + e * h / 2)
        omitted_ct = odd_polynomial + e * h * ct / 2
        missing_residual = S.expand(reduced).coeff(x, 1) - 2 * omitted_ct / d
        self.assert_zero(missing_residual + e * h * ct / d)
        self.assertEqual(S.cancel(S.expand(missing_residual.subs({e: 1, h: 1, ct: 1, d: 1}))), -1)

    def test_arbitrary_coefficient_jet_degree_bound_and_polynomial_primitive(self):
        lam, U = S.symbols("lam U")
        e, h, ett = S.symbols("e h ett", nonzero=True)
        ht = S.symbols("ht")
        P, Pt, B, Bt = 0, 0, 0, 0
        for j in range(3):
            value, derivative = polynomial_and_jet(f"P{j}", 2 - j, lam)
            P += value * U**j
            Pt += derivative * U**j
        for j in range(4):
            value, derivative = polynomial_and_jet(f"B{j}", 3 - j, lam)
            B += value * U**j
            Bt += derivative * U**j
        d, dt = polynomial_and_jet("d", 3, lam)
        a0t, _unused = polynomial_and_jet("a0t", 1, lam)
        Pl, Bl, dl = S.diff(P, lam), S.diff(B, lam), S.diff(d, lam)
        V0 = Bl - e * P / h
        T0 = (ett * U + a0t) * P + Bt
        for j in range(3):
            self.assert_degree_at_most(S.expand(V0).coeff(U, j), lam, 2 - j)
        for j in range(4):
            self.assert_degree_at_most(S.expand(T0).coeff(U, j), lam, 3 - j)
        product_gate = S.expand(Pt * V0 - Pl * T0).coeff(U, 1)
        self.assert_degree_at_most(product_gate, lam, 3)
        solved_cl = 2 * (-e * ht * d - e * h * dt / 2 + product_gate) / (h**2 * ett)
        solved_cl -= a0t * dl / ett
        self.assert_degree_at_most(solved_cl, lam, 3)
        primitive = S.symbols("c_constant") + sum(
            S.Poly(S.expand(solved_cl), lam).nth(j) * lam**(j + 1) / (j + 1)
            for j in range(4)
        )
        self.assert_zero(S.diff(primitive, lam) - solved_cl)
        self.assert_degree_at_most(primitive, lam, 4)
        # The genuine quartic gate is what makes division by e'' legitimate.
        M = -ett / (2 * e**2)
        self.assert_zero(ett + 2 * e**2 * M)


if __name__ == "__main__":
    unittest.main()
