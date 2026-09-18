"""Finite algebraic controls for the whole-double pass112 arguments.

The two methods check a rational product determinant and exact conormal/
weighted connection identities. They do not establish actual coordinate
charts, flat division, degree-module generation, purity, divisor valuations,
or realization by an original constant-acceleration frame. Constant nu in
the final weighted compatibility is an explicit hypothesis, not inferred
by this checker. No solver or retained checker is imported.
"""

import unittest

import sympy as sp


class WholeDoubleConormalChecks(unittest.TestCase):
    def test_product_index_determinant(self):
        r, a, b, eps, P, g0, g1, g2 = sp.symbols(
            "r a b eps P g0 g1 g2", nonzero=True
        )
        G = g2 * r**2 + g1 * r + g0
        H = (r - a * G) / b

        def coefficient_matrix(elements):
            return sp.Matrix(
                [[sp.expand(v).coeff(r, j) for v in elements] for j in range(5)]
            )

        matrix = coefficient_matrix([1, G, H, G**2, G * H])
        determinant = sp.factor(matrix.det())
        self.assertEqual(determinant, g2**4 / b**2)
        self.assertEqual(
            sp.factor(determinant.subs(g2, eps * b / (2 * P))),
            eps**4 * b**2 / (16 * P**4),
        )
        # Both displayed column operations preserve the determinant sign.
        reduced = coefficient_matrix([1, G, r, G**2, r * G])
        triangular = coefficient_matrix([1, r, G, r * G, G**2])
        self.assertEqual(sp.factor(reduced.det()), g2**4)
        self.assertEqual(sp.factor(triangular.det()), g2**4)
        self.assertEqual(sp.factor(matrix.det() - reduced.det() / b**2), 0)

    def test_conormal_and_weighted_connections(self):
        F, G, c = sp.symbols("F G c")
        nu = sp.symbols("nu", nonzero=True)
        w = sp.Matrix([sp.Function("w1")(c), sp.Function("w2")(c)])
        t = sp.Matrix([sp.Function("t1")(c), sp.Function("t2")(c)])

        def det(u, v):
            return sp.Matrix.hstack(u, v).det()

        s = w * F + t * G**2

        def jacobian_N(value):
            return nu * sp.Matrix([s[0], s[1], value]).jacobian([F, G, c]).det()

        self.assertEqual(
            sp.simplify(jacobian_N(G) + nu * (det(w, w.diff(c)) * F
                                             + det(w, t.diff(c)) * G**2)),
            0,
        )
        self.assertEqual(sp.simplify(jacobian_N(c) - 2 * nu * det(w, t) * G), 0)
        self.assertEqual(
            sp.simplify(sp.diff(det(w, t), c)
                        - det(w.diff(c), t) - det(w, t.diff(c))),
            0,
        )

        # Constant det(w,t) and the two stated contractions determine w'.
        w1, w2, t1, t2, v1, v2, ell1, ell2 = sp.symbols(
            "w1 w2 t1 t2 v1 v2 ell1 ell2"
        )
        W, T, V = sp.Matrix([w1, w2]), sp.Matrix([t1, t2]), sp.Matrix([v1, v2])
        d = det(W, T)
        self.assertEqual(sp.simplify(d * V - det(V, T) * W - det(W, V) * T),
                         sp.zeros(2, 1))
        prescribed = ((ell1 * t1 + ell2 * t2) * W
                      - (ell1 * w1 + ell2 * w2) * T) / nu
        self.assertEqual(sp.simplify(prescribed - d * sp.Matrix([ell2, -ell1]) / nu),
                         sp.zeros(2, 1))

        x = sp.symbols("x")
        gamma, B = sp.symbols("gamma B")
        beta, A = sp.Function("beta")(c), sp.Function("A")(c)
        lam = 2 * nu * B

        def D(value):
            return gamma * x * sp.diff(value, G) + lam * G * sp.diff(value, c)

        weighted = D(beta * G)
        self.assertEqual(sp.expand(weighted - gamma * beta * x
                                   - lam * sp.diff(beta, c) * G**2), 0)
        u, v = sp.symbols("u v")
        comparison = sp.expand(weighted - u * x - v * (A * x + B * G**2))
        self.assertEqual(comparison.coeff(x, 1), gamma * beta - u - v * A)
        self.assertEqual(sp.expand(comparison.coeff(G, 2)
                                   - B * (2 * nu * sp.diff(beta, c) - v)), 0)
        compatibility = sp.diff(gamma * beta - u - v * A, c).subs(
            {sp.diff(beta, c): v / (2 * nu), sp.diff(A, c): -gamma / nu}
        )
        self.assertEqual(sp.simplify(compatibility), 3 * gamma * v / (2 * nu))

        # Conditional positive branches, not assertions of geometric existence.
        a0, beta0 = sp.symbols("a0 beta0")
        affine_A = a0 - gamma * c / nu
        self.assertEqual(sp.expand(D(beta0 * G) - gamma * beta0 * x), 0)
        self.assertEqual(sp.simplify(sp.diff(affine_A, c) + gamma / nu), 0)
        self.assertEqual(sp.expand(D(affine_A * x + B * G**2)), 0)
        affine_beta = beta0 + v * c / (2 * nu)
        self.assertEqual(sp.expand(D(affine_beta * G).subs(gamma, 0)
                                   - (-v * a0 * x + v * (a0 * x + B * G**2))), 0)
        # Quadratic beta would require a nonconstant v when nu,B are constants.
        self.assertEqual(sp.diff(2 * nu * sp.diff(c**2, c), c), 4 * nu)


if __name__ == "__main__":
    unittest.main(verbosity=2)
