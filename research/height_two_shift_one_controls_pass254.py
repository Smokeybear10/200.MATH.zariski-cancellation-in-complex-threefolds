"""Finite controls for the shift-one chart253 and pencil endpoint254.

Sources:
  height-two-shift-one-affine-chart-pass253-working.md
  SHA256 3ed0e8e2e1875467135446e1e434f844a72efb70699c23b9c0cc1ab39542b841
  height-two-shift-one-pencil-recognition-pass254-working.md
  SHA256 d5edfd942cab66a9e63b7456fd0cbed0c9b652f89ec2551e465bb97cdfa0138c

These checks reconstruct raw determinants and polynomial/rational identities.
They do not certify local slices, exact field return, the universal pole-degree
lemma, extension of derivatives, or the retained recognition theorem156.
The pole fixtures use independent symbolic parameters, not numerical samples.
The index-two negative control deliberately fails actual field return.

Standalone source: no retained checker is imported.
The author has not executed, imported, or compiled this saved file.
"""

import unittest

import sympy as sp


class ShiftOneControls(unittest.TestCase):
    def assert_zero(self, value):
        self.assertEqual(sp.cancel(sp.expand(value)), 0)

    def test_raw_top_cofactors_and_residual_hamiltonian(self):
        X, qp, rp = sp.symbols("X qp rp")
        yt, yr, ys, zt, zr, zs, wt, wr, ws = sp.symbols(
            "yt yr ys zt zr zs wt wr ws"
        )
        sigt, sigr, sigs, thetat, thetar, thetas = sp.symbols(
            "sigt sigr sigs thetat thetar thetas"
        )
        # Raw fixed-X derivatives before imposing either shift-one gate.
        matrix = sp.Matrix([
            [yt + X, yr, ys],
            [zt + sigt * X + qp * X**2, zr + sigr * X, zs + sigs * X],
            [wt + thetat * X + rp * X**2, wr + thetar * X, ws + thetas * X],
        ])
        Sr, Ss = sigr - qp * yr, sigs - qp * ys
        Hr, Hs = thetar - rp * yr, thetas - rp * ys
        jacobian = sp.Poly(sp.expand(matrix.det()), X)
        self.assertLessEqual(jacobian.degree(), 3)
        self.assert_zero(jacobian.nth(3) - (Sr * Hs - Ss * Hr))

        # Inverse entries for T_Z and T_W have the following numerators.
        z_top = [0, Hs, -Hr]
        w_top = [0, -Ss, Sr]
        for column in range(3):
            self.assert_zero(
                sp.Poly(matrix.cofactor(1, column), X).nth(2) - z_top[column]
            )
            self.assert_zero(
                sp.Poly(matrix.cofactor(2, column), X).nth(2) - w_top[column]
            )
        vanished_top = {
            sigr: qp * yr, sigs: qp * ys,
            thetar: rp * yr, thetas: rp * ys,
        }
        for row in (1, 2):
            for column in range(3):
                top = sp.Poly(matrix.cofactor(row, column), X).nth(2)
                self.assert_zero(top.subs(vanished_top, simultaneous=True))

        # After the exact two row reductions, keep all lower jets arbitrary.
        xi_t, xi_r, xi_s, ze_t, ze_r, ze_s, A, B = sp.symbols(
            "xi_t xi_r xi_s ze_t ze_r ze_s A B"
        )
        reduced = sp.Matrix([
            [yt + X, yr, ys],
            [xi_t + A, xi_r, xi_s],
            [ze_t + B, ze_r, ze_s],
        ])
        self.assert_zero(
            sp.Poly(reduced.det(), X).nth(1) - (xi_r * ze_s - xi_s * ze_r)
        )
        for column, value in enumerate((0, ze_s, -ze_r)):
            self.assert_zero(
                sp.Poly(reduced.cofactor(1, column), X).nth(1) - value
            )

    def test_completed_literal_chart_and_exact_cofactors(self):
        X, t, lam, y, a = sp.symbols("X t lam y a")
        q, rho = sp.Function("q")(t), sp.Function("rho")(t)
        S, H = sp.Function("S")(t), sp.Function("H")(t)
        n = sp.Function("n")(t, lam)
        Y = y + t * X
        Z = (
            n + sp.diff(q, t, 2) * y**2 / 2 + sp.diff(S, t) * y
            + (sp.diff(q, t) * y + S) * X + q * X**2
        )
        W = (
            lam + sp.diff(rho, t, 2) * y**2 / 2 + sp.diff(H, t) * y
            + (sp.diff(rho, t) * y + H) * X + rho * X**2
        )
        matrix = sp.Matrix([Y, Z, W]).jacobian([t, lam, y])
        jacobian = sp.expand(matrix.det())
        expected = (
            sp.diff(n, t)
            + (sp.diff(q, t, 3) - sp.diff(n, lam) * sp.diff(rho, t, 3))
            * y**2 / 2
            + (sp.diff(S, t, 2) - sp.diff(n, lam) * sp.diff(H, t, 2)) * y
        )
        self.assert_zero(jacobian - expected)
        self.assert_zero(sp.diff(jacobian, X))
        self.assert_zero(matrix.cofactor(1, 2) + X)
        self.assert_zero(matrix.cofactor(2, 2) - X * sp.diff(n, lam))

        coefficient_gates = {
            sp.diff(q, t, 3): sp.diff(n, lam) * sp.diff(rho, t, 3),
            sp.diff(S, t, 2): sp.diff(n, lam) * sp.diff(H, t, 2),
        }
        scalar = jacobian.subs(coefficient_gates, simultaneous=True)
        self.assert_zero(scalar - sp.diff(n, t))
        Nz_y = -a / scalar
        Nw_y = a * sp.diff(n, lam) / scalar
        self.assert_zero(Nw_y + sp.diff(n, lam) * Nz_y)
        self.assert_zero(scalar * Nz_y + a)
        # Nonvanishing and its exact-field interpretation belong to253.

    def test_differential_gate_and_actual_shear_inverse_orders(self):
        t = sp.symbols("t")
        q, rho, m = (
            sp.Function("q")(t), sp.Function("rho")(t), sp.Function("m")(t)
        )
        C = (sp.diff(q, t, 2) - m * sp.diff(rho, t, 2)) / 2
        residual = sp.diff(C, t) + sp.diff(m, t) * sp.diff(rho, t, 2) / 2
        self.assert_zero(residual - (sp.diff(q, t, 3) - m * sp.diff(rho, t, 3)) / 2)
        self.assert_zero(residual.subs(sp.diff(q, t, 3), m * sp.diff(rho, t, 3)))
        c1, mp, rpp = sp.symbols("c1 mp rpp")
        # If C=c1*m+c0 and m' is nonzero, the cleared gate is rho''=-2*c1.
        cleared = 2 * c1 * mp + mp * rpp
        self.assert_zero(cleared - mp * (rpp + 2 * c1))
        self.assert_zero(cleared.subs(rpp, -2 * c1))
        m0 = sp.symbols("m0")
        self.assert_zero(
            sp.diff(q - m0 * rho, t, 3).subs(
                sp.diff(q, t, 3), m0 * sp.diff(rho, t, 3)
            )
        )

        X, Y, Z, W, Z1, c, r0, r1, r2 = sp.symbols("X Y Z W Z1 c r0 r1 r2")
        correction = r2 * Y**2 + r1 * X * Y + r0 * X**2
        forward = Z - c * W - correction
        inverse = Z1 + c * W + correction
        self.assert_zero(inverse.subs(Z1, forward) - Z)
        self.assert_zero(forward.subs(Z, inverse) - Z1)
        actual_jacobian = sp.Matrix([X, Y, forward, W]).jacobian([X, Y, Z, W])
        self.assert_zero(actual_jacobian.det() - 1)

        u, x0, y0, z0, z1, w0, w1, a, b, e, h = sp.symbols(
            "u x0 y0 z0 z1 w0 w1 a b e h"
        )
        time_entries = {
            X: x0 + a * u, Y: y0 + b * u,
            Z: z0 + z1 * u + e * u**2,
            W: w0 + w1 * u + h * u**2,
        }
        sheared = forward.subs(time_entries, simultaneous=True)
        leader = sp.Poly(sp.expand(sheared), u).nth(2)
        self.assert_zero(leader - (e - c * h - r2 * b**2 - r1 * a * b - r0 * a**2))
        relation = {e: c * h + r2 * b**2 + r1 * a * b + r0 * a**2}
        self.assert_zero(sp.diff(sheared, u, 2).subs(relation))

    def test_generic_pole_fixtures_and_specialization_warning(self):
        alpha, y, w, z = sp.symbols("alpha y w z")
        # All coefficients have at most the one simple pole alpha=infinity.
        coefficients = (2 * alpha + 3, -alpha + 5, 7 * alpha - 1, 4 * alpha + 6)
        pencil = (
            coefficients[0] * w + coefficients[1] * y**2
            + coefficients[2] * y + coefficients[3]
        )
        slope = 2 * w - y**2 + 7 * y + 4
        intercept = 3 * w + 5 * y**2 - y + 6
        self.assert_zero(pencil - slope * alpha - intercept)
        self.assertNotEqual(sp.Poly(slope, y, w), sp.Poly(0, y, w))
        self.assert_zero(((z - intercept) / slope).subs(z, pencil) - alpha)
        self.assertEqual(sp.Poly(pencil, alpha).degree(), 1)

        # Two different simple coefficient poles give rational degree two.
        two_poles = w * alpha + y**2 / alpha
        numerator, denominator = sp.fraction(sp.cancel(two_poles))
        num_poly = sp.Poly(numerator, alpha)
        den_poly = sp.Poly(denominator, alpha)
        self.assertEqual(num_poly.degree(), 2)
        self.assertEqual(den_poly.degree(), 1)
        self.assertEqual(sp.gcd(num_poly, den_poly).degree(), 0)
        self.assert_zero(sp.cancel(alpha * two_poles).subs(alpha, 0) - y**2)
        self.assert_zero(sp.Poly(numerator, alpha).LC() - w)

        higher_pole = w * alpha + y**2 * alpha**3 + y
        self.assertEqual(sp.Poly(higher_pole, alpha).degree(), 3)
        self.assert_zero(sp.Poly(higher_pole, alpha).LC() - y**2)
        dangerous_specialization = (w - 1) * alpha + 1
        self.assertEqual(sp.Poly(dangerous_specialization, alpha).degree(), 1)
        self.assertEqual(sp.Poly(dangerous_specialization.subs(w, 1), alpha).degree(), 0)
        # Such a numerical specialization cannot prove the universal pole lemma.

    def test_nonzero_scalar_jacobian_does_not_give_actual_field_return(self):
        X, t, lam, y, z0, w0 = sp.symbols("X t lam y z0 w0")
        q, rho, n = t**4 / 4, t**3, t * lam
        z = t * lam + sp.Rational(3, 2) * t**2 * y**2
        w = lam + 3 * t * y**2
        Y = y + t * X
        Z = z + t**3 * y * X + q * X**2
        W = w + 3 * t**2 * y * X + rho * X**2
        matrix = sp.Matrix([Y, Z, W]).jacobian([t, lam, y])
        self.assert_zero(matrix.det() - lam)
        self.assert_zero(sp.diff(q, t, 3) - sp.diff(n, lam) * sp.diff(rho, t, 3))
        self.assert_zero(sp.diff(n, t) - lam)
        self.assert_zero(sp.diff(n, lam, 2))
        self.assert_zero(z - (t * w - sp.Rational(3, 2) * t**2 * y**2))

        # Over C(y,w0), this is a genuine rational map of degree two in t.
        generic_function = t * w0 - sp.Rational(3, 2) * t**2 * y**2
        self.assertEqual(sp.Poly(generic_function, t).degree(), 2)
        equation = sp.Rational(3, 2) * y**2 * t**2 - w0 * t + z0
        self.assert_zero(equation.subs({w0: w, z0: z}, simultaneous=True))
        discriminant = sp.discriminant(equation, t)
        self.assert_zero(discriminant - (w0**2 - 6 * y**2 * z0))
        self.assertEqual(sp.Poly(discriminant, z0).degree(), 1)
        self.assert_zero(sp.Poly(discriminant, z0).LC() + 6 * y**2)
        # The degree-one polynomial in z0 has odd valuation at its simple zero,
        # so it is not a rational square over C(y,w0)(z0). Thus the displayed
        # quadratic defines index two, not the actual field equality of253.


if __name__ == "__main__":
    unittest.main()
