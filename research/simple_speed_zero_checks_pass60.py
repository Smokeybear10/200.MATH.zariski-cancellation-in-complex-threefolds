"""Exact base-field controls for the simple common-speed-zero theorem.

The nonlinear etale and ramified examples are not actual full frames.
These two methods check the specified differential identities and
denominator boundaries, not the universal local eigenfunction theorem.
"""

import unittest

import sympy as S


class SimpleSpeedZeroChecks(unittest.TestCase):
    def test_nonlinear_etale_speed_coordinates(self):
        a, b, lam, mu = S.symbols("a b lam mu")
        f = a + a**2
        g = b

        # The exact field partials on C(a,b), not a formal replacement a=f.
        def df(F):
            return S.cancel(S.diff(F, a) / (1 + 2 * a))

        def dg(F):
            return S.diff(F, b)

        def euler(F):
            return S.cancel(f * df(F) + g * dg(F))

        self.assertEqual(S.Matrix([f, g]).jacobian([a, b]).det(), 1 + 2 * a)
        self.assertEqual((1 + 2 * a).subs(a, 0), 1)
        self.assertEqual(S.cancel(f / (1 + a)), a)
        self.assertEqual((1 + a).subs(a, 0), 1)
        self.assertEqual([df(f), df(g), dg(f), dg(g)], [1, 0, 0, 1])
        for coordinate in (a, b):
            self.assertEqual(S.cancel(df(dg(coordinate)) - dg(df(coordinate))), 0)
            self.assertEqual(
                S.cancel(euler(df(coordinate)) - df(euler(coordinate)) + df(coordinate)),
                0,
            )
            self.assertEqual(
                S.cancel(euler(dg(coordinate)) - dg(euler(coordinate)) + dg(coordinate)),
                0,
            )

        h1, h2 = f**2 + g**2, f * g
        k = lam * f + mu * g
        self.assertEqual(S.cancel(euler(h1) - 2 * h1), 0)
        self.assertEqual(S.cancel(euler(h2) - 2 * h2), 0)
        self.assertEqual(S.cancel(euler(k) - k), 0)
        for h, expected in (
            (h1, S.Matrix([[2, 0], [0, 2]])),
            (h2, S.Matrix([[0, 1], [1, 0]])),
        ):
            actual_hessian = S.Matrix([[df(df(h)), df(dg(h))],
                                       [dg(df(h)), dg(dg(h))]])
            self.assertEqual(actual_hessian.applyfunc(S.cancel), expected)
        self.assertEqual([df(k), dg(k)], [lam, mu])

        # A first-order eigenvector approximation is not an exact eigenfunction.
        self.assertEqual(S.cancel(euler(a) - a + a**2 / (1 + 2 * a)), 0)
        F = S.symbols("F")
        self.assertEqual(S.discriminant(a**2 + a - F, a), 1 + 4 * F)

    def test_ramification_retains_weights_but_allows_poles(self):
        a, b = S.symbols("a b")
        f, g = a**2, b**2

        def df(F):
            return S.cancel(S.diff(F, a) / (2 * a))

        def dg(F):
            return S.cancel(S.diff(F, b) / (2 * b))

        def euler(F):
            return S.cancel((a * S.diff(F, a) + b * S.diff(F, b)) / 2)

        self.assertEqual(S.Matrix([f, g]).jacobian([a, b]).det(), 4 * a * b)
        self.assertEqual([df(f), df(g), dg(f), dg(g)], [1, 0, 0, 1])
        for coordinate in (a, b):
            self.assertEqual(S.cancel(df(dg(coordinate)) - dg(df(coordinate))), 0)
            self.assertEqual(S.cancel(f * df(coordinate) + g * dg(coordinate)
                                      - euler(coordinate)), 0)

        h1, h2, k = a**4, a**3 * b, a * b
        for h in (h1, h2):
            self.assertEqual(S.cancel(euler(h) - 2 * h), 0)
        self.assertEqual(S.cancel(euler(k) - k), 0)
        self.assertEqual(S.Matrix([h1, h2]).jacobian([a, b]).det(), 4 * a**6)
        hessian = S.Matrix([[df(df(h2)), df(dg(h2))],
                            [dg(df(h2)), dg(dg(h2))]])
        expected = S.Matrix([[3 * b / (4 * a), 3 * a / (4 * b)],
                             [3 * a / (4 * b), -a**3 / (4 * b**3)]])
        self.assertEqual((hessian - expected).applyfunc(S.cancel), S.zeros(2))
        self.assertEqual([df(k), dg(k)], [b / (2 * a), a / (2 * b)])
        for coefficient in list(hessian) + [df(k), dg(k)]:
            self.assertEqual(euler(coefficient), 0)

        # Exact orders: these identities exhibit uncancelled prime denominators.
        self.assertEqual(S.cancel(a * hessian[0, 0]), 3 * b / 4)
        self.assertEqual(S.cancel(b**3 * hessian[1, 1]), -a**3 / 4)
        self.assertEqual(S.cancel(a * df(k)), b / 2)
        self.assertEqual(S.cancel(b * dg(k)), a / 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
