"""Independent exact differential-algebra controls for chart258.

No proof/solver/checker module is imported. Formal coefficients are rebuilt
as arbitrary differentiable symbols. These identities do not certify chart
entry, actual field return, polynomial-line geometry, or recognition.
"""

import unittest

import sympy as sp


class QuadraticCubicChartControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_top_cofactors_and_determinant(self):
        X, y = sp.symbols("X y")
        yt, yl, yv, zt, zl, zv = sp.symbols("yt yl yv zt zl zv")
        wt, wl, wv, ht, hl, hv = sp.symbols("wt wl wv ht hl hv")
        q1, q2, r1, r2, kt, m = sp.symbols("q1 q2 r1 r2 kt m")
        row_y = [yt + X, yl, yv]
        row_z = [
            zt + (q2 * y + q1 * yt + kt) * X + q1 * X**2,
            zl + (q1 * yl + m) * X,
            zv + q1 * yv * X,
        ]
        row_w = [
            wt + ht * X + (r2 * y + r1 * yt) * X**2 + r1 * X**3,
            wl + hl * X + (r1 * yl + 1) * X**2,
            wv + hv * X + r1 * yv * X**2,
        ]
        matrix = sp.Matrix([row_y, row_z, row_w])
        determinant = sp.Poly(sp.expand(matrix.det()), X)
        self.assertLessEqual(determinant.degree(), 3)
        self.assert_zero(
            determinant.nth(3) - (-zv + m * hv + ((q2 - r2 * m) * y + kt) * yv)
        )
        # Inverse entry (v,Z) has numerator cofactor (Z,v).
        numerator_z = matrix.cofactor(1, 2)
        numerator_w = matrix.cofactor(2, 2)
        self.assert_zero(sp.Poly(numerator_z, X).nth(3) + 1)
        self.assert_zero(sp.Poly(numerator_w, X).nth(2) - m)
        self.assertNotEqual(sp.Poly(numerator_z, X).nth(3), 1)

    def test_two_potentials_and_all_quartic_coefficients(self):
        t, lam, U, V, level = sp.symbols("t lam U V level")
        q, r = sp.Function("q")(t), sp.Function("r")(t)
        k, n, ell = (sp.Function(name)(t, lam) for name in ("k", "n", "ell"))
        m, d = sp.diff(k, lam), sp.diff(r, t, 2)
        mt, ml = sp.diff(m, t), sp.diff(m, lam)
        nt, nl = sp.diff(n, t), sp.diff(n, lam)
        f = (sp.diff(q, t, 2) - d * m) * U**2 / 2 + sp.diff(k, t) * U + n
        P = (
            d**2 * ml * U**4 / 8
            + (sp.diff(q, t, 3) - sp.diff(r, t, 3) * m - 3 * d * mt) * U**3 / 6
            + (sp.diff(k, t, 2) - d * nl) * U**2 / 2
            + nt * U
        )
        fl = sp.diff(f, lam)
        self.assert_zero(sp.diff(P, U) - sp.diff(f, t) + d * U * fl)
        self.assert_zero(sp.diff(fl, U) - mt + d * U * ml)
        g = (ell - P - ml * V**2 / 2 - fl * V) / m
        C = ml * V + fl
        A = -m * sp.diff(g, t) + m * d * U * sp.diff(g, lam) + C * sp.diff(g, U)
        B = -m * sp.diff(g, lam) + C * sp.diff(g, V)
        self.assert_zero(sp.diff(A, V) - sp.diff(B, U))
        # Reconstruct a primitive from its gradients, not the note's table.
        primitive_v = sp.integrate(sp.expand(B), V)
        correction = sp.expand(A - sp.diff(primitive_v, U))
        self.assert_zero(sp.diff(correction, V))
        primitive = primitive_v + sp.integrate(correction, U)
        self.assert_zero(sp.diff(primitive, U) - A)
        self.assert_zero(sp.diff(primitive, V) - B)
        sheared = sp.Poly(sp.expand(primitive.subs(V, V + d * U**2 / 2) - level), U, V)
        expected = {
            (4, 0): (sp.diff(q, t, 4) - m * sp.diff(r, t, 4) - 4 * sp.diff(q, t, 3) * mt / m) / 24,
            (3, 1): -sp.diff(q, t, 3) * ml / (6 * m),
            (3, 0): (m * sp.diff(k, t, 3) - 3 * sp.diff(k, t, 2) * mt - nl * sp.diff(q, t, 3)) / (6 * m),
            (2, 1): (m * sp.diff(m, t, 2) - ml * sp.diff(k, t, 2) - 2 * mt**2) / (2 * m),
            (2, 0): (m * sp.diff(n, t, 2) - sp.diff(k, t, 2) * nl - 2 * nt * mt) / (2 * m),
            (1, 2): sp.diff(m, t, lam) / 2 - 3 * ml * mt / (2 * m),
            (1, 1): (m * sp.diff(n, t, lam) - ml * nt - 2 * nl * mt) / m,
            (1, 0): (ell * mt - m * sp.diff(ell, t) - nl * nt) / m,
            (0, 3): sp.diff(m, lam, 2) / 6 - ml**2 / (2 * m),
            (0, 2): sp.diff(n, lam, 2) / 2 - 3 * ml * nl / (2 * m),
            (0, 1): (ell * ml - m * sp.diff(ell, lam) - nl**2) / m,
            (0, 0): -level,
        }
        for monomial in set(sheared.monoms()) | set(expected):
            with self.subTest(monomial=monomial):
                self.assert_zero(sheared.coeff_monomial(monomial) - expected.get(monomial, 0))
        normalized = sp.Poly.from_dict(
            {monomial: sp.cancel(coefficient) for monomial, coefficient in sheared.terms()},
            (U, V),
        )
        self.assertLessEqual(normalized.total_degree(), 4)

    def test_zero_coupling_graph_degree_and_derivative(self):
        t, lam, U = sp.symbols("t lam U")
        q, r, k = (sp.Function(name)(t) for name in ("q", "r", "k"))
        n, ell = (sp.Function(name)(t, lam) for name in ("n", "ell"))
        nu = sp.diff(n, lam)
        f = sp.diff(q, t, 2) * U**2 / 2 + sp.diff(k, t) * U + n
        P = (
            sp.diff(q, t, 3) * U**3 / 6
            + (sp.diff(k, t, 2) - sp.diff(r, t, 2) * nu) * U**2 / 2
            + sp.diff(n, t) * U
        )
        G = (ell - P) / nu
        graph_derivative = sp.diff(G, t) - sp.diff(f, t) * sp.diff(G, lam) / nu
        graph = sp.integrate(sp.expand(graph_derivative), U)
        self.assert_zero(sp.diff(graph, U) - graph_derivative)
        self.assertLessEqual(sp.Poly(graph, U).degree(), 6)
        self.assert_zero(nu * sp.diff(graph, U) + sp.diff(f, t) * sp.diff(G, lam) - nu * sp.diff(G, t))


if __name__ == "__main__":
    unittest.main(verbosity=2)
