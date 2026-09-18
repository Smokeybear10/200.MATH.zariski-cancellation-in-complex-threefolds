"""Finite exact-algebra controls for the two rank-two quartic notes221.

Standalone: only standard Python and SymPy are imported. No retained
checker, proof, solver, or workspace data is loaded. The controls check
literal coefficient identities, projective degenerations, actual linear
map formulas, and uniform leading-form identities.

They do not prove actual-chart existence, whole-line return, the constant
field, primitive local nilpotence, Wang's theorem, transcendence, or the
all-orders Laurent argument. Those are written-proof inputs. In particular,
the fixture counts are not a substitute for the universal root argument.
Root alone may execute this saved source after complete source review.
"""

from math import factorial
import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, X, Y, Z, W = sp.symbols("U V X Y Z W")


def clean(expr):
    return sp.cancel(sp.expand(expr))


def taylor(expr, order):
    return sum(
        sp.diff(expr, t, i, rho, order - i)
        * U**i * V**(order - i)
        / (factorial(i) * factorial(order - i))
        for i in range(order + 1)
    )


def obstruction(poly):
    return (
        4 * poly**2 * sp.diff(poly, t, 3)
        - 6 * poly * sp.diff(poly, t) * sp.diff(poly, t, 2)
        + 3 * sp.diff(poly, t)**3
    )


class BinaryQuarticZeroReturnLineControls(unittest.TestCase):
    def zero(self, expr):
        self.assertEqual(clean(expr), 0)

    def test_literal_zero_return_affine_substitution_and_cubic(self):
        f = sp.Function("f")(t)
        q = f / rho
        kt, kr, ktt, ktr, krr, nt, nr = sp.symbols(
            "kt kr ktt ktr krr nt nr"
        )
        h2q, h3q = taylor(q, 2), taylor(q, 3)
        return_poly = sp.diff(h2q + kt * U + kr * V, V)
        affine_V = rho * sp.diff(f, t) * U / (2 * f) - rho**3 * kr / (2 * f)
        self.zero(return_poly.subs(V, affine_V))
        complete_third = (
            h3q + ktt * U**2 / 2 + ktr * U * V + krr * V**2 / 2
            + nt * U + nr * V
        )
        substituted = sp.Poly(sp.expand(complete_third.subs(V, affine_V)), U)
        self.assertEqual(substituted.degree(), 3)
        self.zero(substituted.coeff_monomial(U**3) - obstruction(f) / (24 * rho * f**2))
        self.zero(
            h3q.subs({U: 1, V: rho * sp.diff(f, t) / (2 * f)}, simultaneous=True)
            - obstruction(f) / (24 * rho * f**2)
        )
        self.zero(sp.diff(q, rho, 2) / 2 - f / rho**3)

    def test_square_identity_root_orders_and_all_infinity_types(self):
        g = sp.Function("g")(t)
        self.zero(obstruction(g**2) - 8 * g**5 * sp.diff(g, t, 3))
        multiplicity = sp.symbols("multiplicity", integer=True, positive=True)
        local_coefficient = (
            4 * multiplicity * (multiplicity - 1) * (multiplicity - 2)
            - 6 * multiplicity**2 * (multiplicity - 1) + 3 * multiplicity**3
        )
        self.zero(local_coefficient - multiplicity * (multiplicity - 2) * (multiplicity - 4))
        self.assertEqual(local_coefficient.subs(multiplicity, 1), 3)
        self.assertEqual(local_coefficient.subs(multiplicity, 3), -3)

        # Include every partition and each possible infinity multiplicity.
        fixtures = [
            ("1111-finite", t * (t - 1) * (t - 2) * (t - 3), False, 0),
            ("1111-infinity1", t * (t - 1) * (t - 2), False, 1),
            ("211-finite", t**2 * (t - 1) * (t - 2), False, 0),
            ("211-infinity1", t**2 * (t - 1), False, 1),
            ("211-infinity2", t * (t - 1), False, 2),
            ("22-finite", t**2 * (t - 1)**2, True, 0),
            ("22-infinity2", t**2, True, 2),
            ("31-finite", t**3 * (t - 1), False, 0),
            ("31-infinity1", t**3, False, 1),
            ("31-infinity3", t, False, 3),
            ("4-finite", t**4, True, 0),
            ("4-infinity4", sp.Integer(1), True, 4),
        ]
        for name, poly, square, infinity_order in fixtures:
            with self.subTest(partition=name):
                self.assertEqual(clean(obstruction(poly)) == 0, square)
                self.assertEqual(4 - sp.Poly(poly, t).degree(), infinity_order)
                if square:
                    self.assertEqual(infinity_order % 2, 0)
        g0, g1, g2 = sp.symbols("g0 g1 g2")
        quadratic = g0 + g1 * t + g2 * t**2
        self.zero(obstruction(quadratic**2))
        self.zero(X**4 * quadratic.subs(t, Y / X)**2 - (g0 * X**2 + g1 * X * Y + g2 * Y**2)**2)
        # A square outside the degree-at-most-four hypothesis need not have J=0.
        self.zero(obstruction(t**6) - 48 * t**15)
        self.assertNotEqual(clean(obstruction(t**6)), 0)

    def test_normalized_cubic_direction_return_and_actual_auxiliary_rows(self):
        A, B, C = sp.symbols("A B C")
        f = A * t**3 + B * t**2 + C * t
        q = f / rho
        h = t / rho
        eta, nu, kt, kr, k0 = sp.symbols("eta nu kt kr k0")
        direction = {U: h, V: 1}
        self.zero(taylor(q, 2).subs(direction, simultaneous=True) - A * h**3)
        self.zero(taylor(q, 3).subs(direction, simultaneous=True))
        radial = lambda expr: h * sp.diff(expr, t) + sp.diff(expr, rho)
        self.zero(radial(h))
        self.zero(radial(q) - 2 * A * h**3 * rho - B * h**2)
        self.zero(radial(radial(q)) - 2 * A * h**3)
        self.zero(radial(radial(radial(q))))
        line = {U: h * eta + nu, V: eta}
        raw_return = sp.diff(taylor(q, 2), V) + kr
        normalized_return = sp.Poly(sp.expand(raw_return.subs(line, simultaneous=True)), eta)
        self.zero(normalized_return.coeff_monomial(eta) - t * (C - A * t**2) / rho**3)
        self.zero(normalized_return.coeff_monomial(1) - kr + sp.diff(f, t) * nu / rho**2)
        self.zero(sp.expand(taylor(q, 3).subs(line, simultaneous=True)).coeff(eta, 3))

        lam, omega, kap, zeta, tau = sp.symbols("lam omega kap zeta tau")
        w = lam * eta + omega
        projected_z = sp.diff(q, rho) * w + taylor(q, 2).subs(line, simultaneous=True) + kt * (h * eta + nu) + kr * eta
        self.zero(sp.expand(projected_z).coeff(eta, 2) - A * h**3)
        sigma = sp.diff(q, t) * (h * eta + nu) + sp.diff(q, rho) * eta + k0
        self.zero(sp.expand(sigma).coeff(eta) - (2 * A * h**3 * rho + B * h**2))
        capital_y = h * eta + nu + t * X
        capital_w = w + eta * X + rho * X**2
        capital_z = A * h**3 * eta**2 + kap * eta + zeta + sigma * X + q * X**2
        P = lambda expr: tau * sp.diff(expr, eta)
        self.zero(P(capital_y) - tau * h)
        self.zero(P(capital_w) - tau * (X + lam))
        self.zero(P(P(capital_z)) - 2 * A * h**3 * tau**2)
        self.zero(P(P(capital_y)))
        self.zero(P(P(capital_w)))
        self.zero(P(P(P(capital_z))))
        aa, bb, cc = sp.symbols("aa bb cc")
        quadratic_correction = aa * capital_y**2 + bb * capital_y * capital_w + cc * capital_w**2
        self.zero(
            P(P(capital_z + quadratic_correction))
            - 2 * tau**2 * (A * h**3 + aa * h**2 + bb * h * (X + lam) + cc * (X + lam)**2)
        )

    def test_actual_good_GL2_inverse_chart_and_selected_pair_transport(self):
        a, b, c, d = sp.symbols("a b c d")
        determinant = a * d - b * c
        XP, YP = sp.symbols("XP YP")
        forward = {XP: a * X + b * Y, YP: c * X + d * Y}
        inverse = {X: (d * XP - b * YP) / determinant, Y: (-c * XP + a * YP) / determinant}
        for variable, expr in forward.items():
            self.zero(expr.subs(inverse, simultaneous=True) - variable)
        for variable, expr in inverse.items():
            self.zero(expr.subs(forward, simultaneous=True) - variable)
        self.assertEqual([sp.diff(expr, Z) for expr in (forward[XP], forward[YP], Z, W)], [0, 0, 1, 0])

        y, theta, w, q, sigma, zz = sp.symbols("y theta w q sigma zz")
        l, m = a + b * t, c + d * t
        tp, rp = m / l, rho / l**2
        yp = determinant * y / l
        thetap = theta / l - 2 * rho * b * y / l**2
        wp = w - b * y * theta / l + rho * b**2 * y**2 / l**2
        sigmap = sigma / l - 2 * q * b * y / l**2
        zp = zz - b * y * sigma / l + q * b**2 * y**2 / l**2
        old_X = (XP - b * y) / l
        self.zero(c * old_X + d * (y + t * old_X) - yp - tp * XP)
        self.zero(w + theta * old_X + rho * old_X**2 - wp - thetap * XP - rp * XP**2)
        self.zero(zz + sigma * old_X + q * old_X**2 - zp - sigmap * XP - q * XP**2 / l**2)
        self.zero(yp - tp * thetap / rp + (l * m * theta - rho * (b * m + d * l) * y) / (rho * l))
        self.zero(sp.Matrix([yp, thetap]).jacobian([y, theta]).det() - determinant / l**2)
        self.zero((a * tp - c) / (d - b * tp) - t)
        self.zero(rp * determinant**2 / (d - b * tp)**2 - rho)

        e, ff, g, hh = sp.symbols("e ff g hh")
        original_quartic = (a * X + b * Y) * (c * X + d * Y) * (e * X + ff * Y) * (g * X + hh * Y)
        e0, e1 = (e * d - ff * c) / determinant, (ff * a - e * b) / determinant
        g0, g1 = (g * d - hh * c) / determinant, (hh * a - g * b) / determinant
        normalized = XP * YP * (e0 * XP + e1 * YP) * (g0 * XP + g1 * YP)
        self.zero(original_quartic.subs(inverse, simultaneous=True) - normalized)
        cubic = e1 * g1 * t**3 + (e0 * g1 + e1 * g0) * t**2 + e0 * g0 * t
        self.zero(normalized.subs({XP: 1, YP: t}, simultaneous=True) - cubic)

    def test_uniform_Laurent_leading_forms_and_transcendence_boundary(self):
        h, epsilon, scale = sp.symbols("h epsilon scale", nonzero=True)
        lam = sp.symbols("lam")
        aa, bb, cc = sp.symbols("aa bb cc")
        # A common symbolic scale stands for X^m for ANY adjusted order m.
        # No sampled list of Laurent orders is being used as a proof.
        scaled_expression = (
            scale * aa * h**2
            + scale * epsilon * bb * h * (1 / epsilon + lam)
            + scale * epsilon**2 * cc * (1 / epsilon + lam)**2
        ) / scale
        leading = aa * h**2 + bb * h + cc
        self.zero(scaled_expression - leading - epsilon * (lam * bb * h + 2 * lam * cc + epsilon * lam**2 * cc))
        self.zero(clean(scaled_expression).subs(epsilon, 0) - leading)
        self.assertEqual(sp.Poly(leading, h).all_coeffs(), [aa, bb, cc])
        A = sp.symbols("A", nonzero=True)
        self.assertEqual(sp.Poly(A * h**3 + leading, h).LC(), A)
        self.assertEqual(sp.Poly(A * h**3 + leading, h).degree(), 3)

        power = sp.symbols("power", integer=True, nonnegative=True)
        ratio_power = ((1 + lam * epsilon) / h)**power
        self.zero(ratio_power.subs(epsilon, 0) - (1 / h)**power)
        i, j = sp.symbols("i j", integer=True, nonnegative=True)
        good_leading = (h + epsilon * Y)**i * (X + lam + epsilon * W)**j
        self.zero(good_leading.subs(epsilon, 0) - h**i * (X + lam)**j)
        # When h is instead a fixed scalar, the final polynomial comparison
        # can vanish. The written transcendence gate is genuinely required.
        h0 = sp.symbols("h0", nonzero=True)
        self.zero(A * h0**3 + (-A * h0) * h0**2)


if __name__ == "__main__":
    unittest.main()
