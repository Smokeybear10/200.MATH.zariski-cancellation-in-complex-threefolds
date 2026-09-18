"""Finite polynomial identities for297, not a recognition theorem.

Checks both actual inverse directions and full degree lowering. The
integrality obstruction and retained156 theorem are written arguments.
No solver, previous checker, or project proof is imported.
"""

import unittest

import sympy as s


class NagataDegreeLoweringControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_both_polynomial_inverse_directions(self):
        X, Y, Z, W, V0, U20, mu = s.symbols("X Y Z W V0 U20 mu")
        lam = s.symbols("lambda", nonzero=True)
        U1 = W - mu - X * Z
        R = Y**2 + X * U1
        V = Y - X * R / lam
        U2 = U1 + 2 * Y * R / lam - X * R**2 / lam**2
        Rstar = s.expand(V**2 + X * U2)
        self.assert_zero(Rstar - R)
        Yback = V + X * Rstar / lam
        U1back = U2 - 2 * V * Rstar / lam - X * Rstar**2 / lam**2
        self.assert_zero(Yback - Y)
        self.assert_zero(U1back + mu + X * Z - W)
        R0 = V0**2 + X * U20
        Yinverse = V0 + X * R0 / lam
        U1inverse = U20 - 2 * V0 * R0 / lam - X * R0**2 / lam**2
        Rforward = s.expand(Yinverse**2 + X * U1inverse)
        self.assert_zero(Rforward - R0)
        self.assert_zero(Yinverse - X * Rforward / lam - V0)
        self.assert_zero(U1inverse + 2 * Yinverse * Rforward / lam
                         - X * Rforward**2 / lam**2 - U20)

    def test_full_raw_degree_lowering(self):
        X, y, t, ss, h, theta, mu = s.symbols("X y t ss h theta mu")
        lam = s.symbols("lambda", nonzero=True)
        sigma = (y**2 - h) / lam
        z = 2 * t * y + sigma**2 + theta
        w = lam * t + mu - 2 * sigma * y
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + ss) * X + t**2 * X**2
        W = w + theta * X + ss * X**2
        U1 = W - mu - X * Z
        R = s.expand(Y**2 + X * U1)
        V = s.expand(Y - X * R / lam)
        U2 = s.expand(U1 + 2 * Y * R / lam - X * R**2 / lam**2)
        self.assert_zero(R - (y**2 + lam * t * X))
        self.assert_zero(V - (y - h * X / lam))
        self.assert_zero(U2 - (lam * t + 2 * h * y / lam - h**2 * X / lam**2))
        self.assert_zero(s.diff(V, X, 2))
        self.assert_zero(s.diff(U2, X, 2))
        self.assert_zero(V.subs(h, 0) - y)
        self.assert_zero(U2.subs(h, 0) - lam * t)

    def test_constant_potential_square_boundary(self):
        X, y, t, ss, sigma, theta, mu = s.symbols("X y t ss sigma theta mu")
        Y = y + sigma * X + t * X**2
        z = 2 * t * y + sigma**2 + theta
        Z = z + (2 * t * sigma + ss) * X + t**2 * X**2
        W = mu - 2 * sigma * y + theta * X + ss * X**2
        self.assert_zero(Y**2 + X * (W - mu - X * Z) - y**2)
        xa, ya, za, wa = s.symbols("xa ya za wa")
        original = ya**2 + xa * (wa - mu) - xa**2 * za
        self.assertEqual(s.Poly(original, za).degree(), 1)
        self.assert_zero(s.diff(original, za) + xa**2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
