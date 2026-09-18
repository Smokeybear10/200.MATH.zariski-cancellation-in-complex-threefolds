"""One exact method for the zero-normal conormal restriction in pass98.

Formal row/weighted identities and a separate primitive intrinsic LND are
controls, not actual original-frame realizations or proofs of the global
whole-component length and volume hypotheses. No old checker is imported.
"""

import unittest

import sympy as S


class QuadraticZeroNormalChecks(unittest.TestCase):
    def test_weighted_rows_charts_and_intrinsic_square_boundary(self):
        c, x, y, v, F, G = S.symbols("c x y v F G")
        nu, k = S.symbols("nu k", nonzero=True)
        p0, p1, p2, q0, q1, q2 = S.symbols("p0 p1 p2 q0 q1 q2")
        p = p0 + p1 * c + p2 * c**2
        q = q0 + q1 * c + q2 * c**2
        a = k / p**2

        def weighted(expr):
            return S.cancel(
                -nu * p * S.diff(a, c) * y**2 * S.diff(expr, y)
                + 2 * nu * p * a * y * S.diff(expr, c)
            )

        def translated(expr):
            return S.expand(2 * nu * k * v * S.diff(expr, c))

        self.assertEqual(weighted(y / p), 0)
        self.assertEqual(S.cancel(weighted(c) - 2 * nu * k * y / p), 0)
        self.assertEqual(weighted(weighted(c)), 0)
        self.assertEqual(weighted(x), 0)
        for first_form in (-q * v, p * v):
            value = first_form
            for _ in range(3):
                value = translated(value)
            self.assertEqual(value, 0)
        bad = c**3 * v
        for _ in range(3):
            bad = translated(bad)
        self.assertEqual(bad, 6 * (2 * nu * k)**3 * v**4)
        self.assertNotEqual(bad, 0)

        # This formal polynomial row is unimodular even where p=c vanishes.
        chart_p, chart_q = c, c**2 + 1
        self.assertEqual(S.expand(-c * chart_p + chart_q), 1)
        quadratic = k * (-F - c * G)**2
        transverse = S.expand(
            quadratic.subs({F: -chart_q, G: chart_p}, simultaneous=True)
        )
        self.assertEqual(transverse, k)
        self.assertEqual(chart_p.subs(c, 0), 0)
        self.assertEqual(chart_q.subs(c, 0), 1)
        self.assertEqual(transverse.subs(c, 0), k)

        # Separate actual intrinsic polynomial LND, not the original frame.
        def intrinsic(expr):
            return S.expand(-x**2 * S.diff(expr, y) + 2 * y * S.diff(expr, c))

        f = y**2 + x**2 * c
        self.assertEqual(intrinsic(f), 0)
        self.assertEqual(S.gcd(-x**2, 2 * y), 1)
        self.assertEqual(f.subs(x, 0), y**2)
        for generator in (x, y):
            value = generator
            for _ in range(3):
                value = intrinsic(value)
            self.assertEqual(value, 0)
        value = c
        for _ in range(5):
            value = intrinsic(value)
        self.assertEqual(value, 0)
        self.assertEqual(intrinsic(x), 0)
        self.assertEqual(intrinsic(y), -x**2)
        self.assertEqual(intrinsic(c), 2 * y)
        self.assertEqual(intrinsic(intrinsic(c)), -2 * x**2)
        self.assertNotEqual(intrinsic(intrinsic(c)), 0)
        # Constant transverse coefficient for the row (1,0).
        self.assertEqual(f.subs({x: 0, y: 1}, simultaneous=True), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

