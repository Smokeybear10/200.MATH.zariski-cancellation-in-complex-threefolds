"""Finite exact controls for the denominator-free coefficient fiber143.

These tests use the actual sharp and finite-cover source projections from
140, and the constant-first-speed source projection from129. They check
polynomial invariant return and full small ideals, without saturation.
The all-degree primitive-element choice, actual projection theorem and
graph-presentation proof are written arguments, not conclusions from the
finite Groebner calculations. No automatic first-tail compatibility or
cancellation theorem is claimed. No earlier checker or solver is imported.
"""

import unittest

import sympy as sp


class PolynomialCoefficientFiberControls(unittest.TestCase):
    def setUp(self):
        self.a, self.b, self.v = sp.symbols("a b v")
        self.U, self.V, self.t = sp.symbols("U V t")
        self.xi = sp.symbols("xi1 xi2 xi3")

    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def exact_ideal(self, rows, g):
        U, V, a, b = self.U, self.V, self.a, self.b
        coefficient_field = sp.QQ.frac_field(a, b)
        basis = sp.groebner(rows, U, V, order="lex", domain=coefficient_field)
        self.assertEqual(len(basis.polys), 1)
        expected = sp.Poly(g, U, V, domain=coefficient_field).monic()
        self.assertEqual(basis.polys[0].monic(), expected)

    def polynomial_returns(self, representatives, values, projected_source, omega):
        actual = dict(zip(self.xi, projected_source))
        formal = dict(zip(self.xi, (self.U, self.V, omega)))
        for representative, value in zip(representatives, values):
            self.zero(representative.subs(actual, simultaneous=True) - value)
        pulled = [sp.cancel(p.subs(formal, simultaneous=True)) for p in representatives]
        return pulled, [sp.cancel(p - value) for p, value in zip(pulled, values)]

    def normalized_comparison(self, pulled, values, g):
        ps, pt, pb, pe = pulled
        s, t, b, e = values
        for power in (1, 2, 3):
            # Positive powers only. M=0 is treated independently below.
            rows = [ps ** (power - 1) * (pt - t * ps / s),
                    ps ** (power - 1) * (pb - b * ps / s),
                    ps**power * (pe - e), ps - s]
            self.exact_ideal(rows, g)
            geometric_sum = sum((ps ** (power - 1 - j) * s**j
                                 for j in range(power)), sp.S.Zero)
            self.zero(ps**power - s**power - (ps - s) * geometric_sum)

    def test_actual_sharp_polynomial_return_and_four_equations(self):
        a, b, v, U, V = self.a, self.b, self.v, self.U, self.V
        p, q, r = self.xi
        F = self.t**3 / 2 + self.t + 2
        Fv = F.subs(self.t, v)
        # The actual140 first coordinate is X=v+a*u. Its X=0 projection
        # is obtained by u=-v/a, so the source generators may have poles.
        projected = (a - Fv - (b + 1) * v / a,
                     a - Fv - (b + 2) * v / a,
                     b + a * (v**2 / 2 + 1))
        source_a = 2 * p - q + (p - q) * r + 2
        source_b = r - source_a - source_a**3 * (p - q)**2 / 2
        representatives = (source_a, source_b + 1, source_b + 2, source_a)
        values = (a, b + 1, b + 2, a)
        omega = b + a + a**3 * (U - V)**2 / 2
        self.zero(omega.subs({U: projected[0], V: projected[1]}, simultaneous=True) - projected[2])
        pulled, rows = self.polynomial_returns(representatives, values, projected, omega)
        g = (b + 2) * U - (b + 1) * V + F.subs(self.t, a * (U - V)) - a
        self.zero(rows[0] - g)
        self.zero(rows[3] - g)
        self.exact_ideal(rows, g)
        self.normalized_comparison(pulled, values, g)
        # The source return is polynomial even though y itself is not in A.
        y_denominator = sp.denom(sp.cancel(projected[0]))
        self.assertGreater(sp.degree(y_denominator, a), 0)

    def test_actual_covers_need_the_polynomial_primitive_element(self):
        a, b, v, U, V = self.a, self.b, self.v, self.U, self.V
        p, q, r = self.xi
        source_b = q - r
        source_a = p - source_b * r
        for n in (2, 3):
            with self.subTest(n=n):
                # Actual140: X=v+a^n*u, Y=a+b*u, Z=b+u, W=u.
                projected = (a - b * v / a**n, b - v / a**n, -v / a**n)
                representatives = (source_a**n, source_b, sp.S.One, source_a)
                values = (a**n, b, sp.S.One, a)
                omega = V - b
                pulled, rows = self.polynomial_returns(representatives, values, projected, omega)
                recovered_a = U - b * V + b**2
                g = recovered_a - a
                self.zero(rows[0] - recovered_a**n + a**n)
                self.zero(rows[1])
                self.zero(rows[2])
                self.zero(rows[3] - g)
                self.exact_ideal(rows, g)
                self.normalized_comparison(pulled, values, g)
                # Omitting e really leaves all n conjugate lines in this
                # source fiber. This is not a nonprimitive actual Phi claim.
                base = sp.groebner(rows[:3], U, V, order="lex",
                                   domain=sp.QQ.frac_field(a, b))
                self.assertEqual(len(base.polys), 1)
                self.assertEqual(base.polys[0].total_degree(), n)

    def test_constant_first_speed_has_three_polynomial_equations(self):
        a, b, v, U, V = self.a, self.b, self.v, self.U, self.V
        p, q, r = self.xi
        F = self.t**3 / 2 + self.t + 2
        slope_p = sp.diff(F.subs(self.t, p), p)
        # Actual129: X=u, Y=v+a*u, Z=a-F(v)+b*u, W=b+Delta_F.
        source_a = q + F.subs(self.t, p)
        source_b = r - source_a * slope_p
        projected = (v, a - F.subs(self.t, v),
                     b + a * sp.diff(F.subs(self.t, v), v))
        omega = b + a * sp.diff(F.subs(self.t, U), U)
        representatives = (sp.S.One, source_a, source_b, sp.S.Zero)
        values = (sp.S.One, a, b, sp.S.Zero)
        pulled, rows = self.polynomial_returns(representatives, values, projected, omega)
        g = V + F.subs(self.t, U) - a
        self.zero(rows[0])
        self.zero(rows[1] - g)
        self.zero(rows[2] + sp.diff(F.subs(self.t, U), U) * g)
        self.exact_ideal(rows[1:], g)
        # M=0 means q=1 from the outset; no negative power is evaluated.
        normalized_rows = [pulled[1] - a, pulled[2] - b, pulled[3]]
        self.exact_ideal(normalized_rows, g)


if __name__ == "__main__":
    unittest.main()
