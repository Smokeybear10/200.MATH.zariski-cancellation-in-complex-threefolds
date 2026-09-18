"""Finite differential-algebra controls for the principal paraboloid chart264.

The tests differentiate literal polynomial rows and retain all lower jets.
They do not establish chart entry, exact field return, or recognition.
A polynomial relation in THREE formal variables is a surface relation,
not a plane-curve presentation. No retained checker module is imported.
"""

import unittest

import sympy as sp


class PrincipalParaboloidChartControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_fifth_coefficient_and_fourth_cofactor(self):
        t, X, speed, J = sp.symbols("t X speed J", nonzero=True)
        yt, ys, yv, zt, zs, zv, wt, ws, wv = sp.symbols(
            "yt ys yv zt zs zv wt ws wv"
        )
        pt, ps, pv, taut, taus, tauv, vt, vs, vv = sp.symbols(
            "pt ps pv taut taus tauv vt vs vv"
        )
        literal = sp.Matrix(
            [
                [yt + pt * X + X**2, ys + ps * X, yv + pv * X],
                [zt + taut * X + 2 * t * X**2, zs + taus * X, zv + tauv * X],
                [wt + vt * X, ws + vs * X + X**2, wv + vv * X],
            ]
        )
        determinant = sp.Poly(sp.expand(literal.det()), X)
        self.assertLessEqual(determinant.degree(), 5)
        self.assert_zero(determinant.nth(5) - (2 * t * pv - tauv))
        # Inverse entry (v,Z) uses the cofactor with row Z, column v.
        numerator = literal.cofactor(1, 2)
        self.assert_zero(sp.Poly(numerator, X).nth(4) + 1)
        self.assert_zero((-1 / J - 1 / speed**4).subs(J, -speed**4))
        self.assertNotEqual(
            sp.cancel((-1 / J - 1 / speed**4).subs(J, speed**4)), 0
        )
        # The calibration has fourth speed power, not the old cubic power.
        self.assertNotEqual(
            sp.cancel((-1 / J - 1 / speed**4).subs(J, -speed**3)), 0
        )

    def test_first_and_second_potentials_with_zero_coupling_allowed(self):
        X, y, p, v, m, kt, z0t, z0s, z0v = sp.symbols(
            "X y p v m kt z0t z0s z0v"
        )
        yt, ys, yv, pt, ps, pv, vt, vs, vv, wt, ws, wv = sp.symbols(
            "yt ys yv pt ps pv vt vs vv wt ws wv"
        )
        gamma = 2 * p + kt
        first_row = [yt + X * pt + X**2, ys + X * ps, yv + X * pv]
        last_row = [wt + X * vt, ws + X * vs + X**2, wv + X * vv]
        before_first = sp.Matrix(
            [
                first_row,
                [z0t + 2 * y + X * gamma, z0s + X * m, z0v],
                last_row,
            ]
        )
        coefficient = sp.Poly(sp.expand(before_first.det()), X).nth(4)
        self.assert_zero(coefficient - (-z0v + gamma * pv + m * vv))
        self.assert_zero(coefficient.subs(z0v, gamma * pv + m * vv))

        ktt, kts, kss, nt, ns, ell = sp.symbols("ktt kts kss nt ns ell")
        F = ktt * p**2 / 2 + kts * p * v + kss * v**2 / 2 + nt * p + ns * v
        B = 2 * y + sp.diff(F, p)
        C = sp.diff(F, v)
        after_first = sp.Matrix(
            [
                first_row,
                [
                    gamma * pt + m * vt + B + X * gamma,
                    gamma * ps + m * vs + C + X * m,
                    gamma * pv + m * vv,
                ],
                last_row,
            ]
        )
        full = sp.Poly(sp.expand(after_first.det()), X)
        self.assert_zero(full.nth(4))
        expected = m * wv + B * pv + C * vv + gamma * yv
        self.assert_zero(full.nth(3) - expected)
        w = sp.symbols("w")
        potential = m * w + gamma * y + F - ell
        derivative = sum(
            sp.diff(potential, variable) * jet
            for variable, jet in [(y, yv), (p, pv), (v, vv), (w, wv)]
        )
        self.assert_zero(derivative - expected)
        self.assert_zero((full.nth(3) - derivative).subs(m, 0))

    def test_full_cubic_primitive_and_raw_second_coefficient(self):
        t, s, X, U, P, V, level = sp.symbols("t s X U P V level")
        k, n, ell = (sp.Function(name)(t, s) for name in ("k", "n", "ell"))
        m = sp.diff(k, s)
        gamma = 2 * P + sp.diff(k, t)
        F = (
            sp.diff(k, t, 2) * P**2 / 2
            + sp.diff(k, t, s) * P * V
            + sp.diff(k, s, 2) * V**2 / 2
            + sp.diff(n, t) * P
            + sp.diff(n, s) * V
        )
        g = (ell - gamma * U - F) / m
        B, C = 2 * U + sp.diff(F, P), sp.diff(F, V)
        self.assert_zero(sp.diff(g, U) + gamma / m)
        self.assert_zero(sp.diff(g, P) + B / m)
        self.assert_zero(sp.diff(g, V) + C / m)

        def H(order, coefficient):
            return sum(
                sp.diff(coefficient, t, order - i, s, i)
                * P ** (order - i) * V**i
                / sp.factorial(order - i) / sp.factorial(i)
                for i in range(order + 1)
            )

        primitive = (
            U**2 + sp.diff(F, P) * U + sp.diff(F, V) * g
            + H(3, k) + H(2, n) - sp.diff(ell, t) * P - sp.diff(ell, s) * V
        )
        gradients = [
            2 * U + sp.diff(F, P) - gamma * C / m,
            -m * sp.diff(g, t) + C * sp.diff(g, P),
            -m * sp.diff(g, s) + C * sp.diff(g, V),
        ]
        for variable, expected in zip([U, P, V], gradients):
            self.assert_zero(sp.diff(primitive, variable) - expected)

        yt, ys, yv, pt, ps, pv, vt, vs, vv = sp.symbols(
            "yt ys yv pt ps pv vt vs vv"
        )
        gt = sp.diff(g, t) + sp.diff(g, U) * yt + sp.diff(g, P) * pt + sp.diff(g, V) * vt
        gs = sp.diff(g, s) + sp.diff(g, U) * ys + sp.diff(g, P) * ps + sp.diff(g, V) * vs
        gv = sp.diff(g, U) * yv + sp.diff(g, P) * pv + sp.diff(g, V) * vv
        raw = sp.Matrix(
            [
                [yt + X * pt + X**2, ys + X * ps, yv + X * pv],
                [
                    gamma * pt + m * vt + B + X * gamma,
                    gamma * ps + m * vs + C + X * m,
                    gamma * pv + m * vv,
                ],
                [gt + X * vt, gs + X * vs + X**2, gv + X * vv],
            ]
        )
        raw_coefficients = sp.Poly(sp.expand(raw.det()), X)
        raw_coefficient = raw_coefficients.nth(2)
        derivative = sum(
            sp.diff(primitive, variable) * jet
            for variable, jet in [(U, yv), (P, pv), (V, vv)]
        )
        self.assert_zero(raw_coefficient - derivative)
        self.assert_zero(raw_coefficients.nth(3))
        relation = sp.Poly(sp.expand(primitive - level), U, P, V)
        normalized = sp.Poly.from_dict(
            {monomial: sp.cancel(coefficient) for monomial, coefficient in relation.terms()},
            (U, P, V),
        )
        self.assertLessEqual(normalized.total_degree(), 3)
        self.assertEqual(normalized.degree(U), 2)
        self.assert_zero(normalized.coeff_monomial(U**2) - 1)
        # These three generators are deliberately not called a plane pair.
        self.assertEqual(normalized.gens, (U, P, V))
        # Omitting the coefficient derivative of m gives the wrong P-gradient.
        wrong_g_t = (sp.diff(ell, t) - sp.diff(gamma, t) * U - sp.diff(F, t)) / m
        self.assertNotEqual(sp.cancel(wrong_g_t - sp.diff(g, t)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
