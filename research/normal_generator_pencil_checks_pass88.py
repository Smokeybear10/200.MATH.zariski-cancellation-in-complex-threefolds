"""One S-flat polynomial-ring pencil with a provably noncoordinate bad output."""

import unittest

import sympy as S


class NormalGeneratorPencilChecks(unittest.TestCase):
    def test_relative_modification_and_failed_coordinate(self):
        a, t, c, tau, sigma = S.symbols("a t c tau sigma")
        h = a * c
        d = c + tau * h
        self.assertEqual(S.expand((1 - tau * a) * d + tau**2 * a**2 * c - c), 0)

        X, Y = S.symbols("X Y")
        tensor = S.groebner([a**2 * (X - Y)], X, Y, a, t)
        dh = a * (X - Y)
        self.assertEqual(S.expand(tensor.reduce(dh)[1] - dh), 0)
        self.assertNotEqual(tensor.reduce(dh)[1], 0)
        self.assertEqual(tensor.reduce(S.expand(dh**2))[1], 0)
        self.assertEqual(tensor.reduce(a**2 * (X - Y))[1], 0)

        u = sigma + h
        z = c + 2 * a * sigma * c + sigma**2
        self.assertEqual(S.diff(u, sigma), 1)
        self.assertEqual(S.expand(S.diff(z, sigma) - 2 * u), 0)
        self.assertEqual(S.diff(z, sigma, 2), 2)
        self.assertEqual(S.diff(z, sigma, 3), 0)
        self.assertEqual(S.expand((1 - 2 * a * sigma) * (z - sigma**2)
                                 + 4 * sigma**2 * a**2 * c - c), 0)

        v = 1 + 2 * a * sigma
        inverse_mod_z = 1 - 2 * a * sigma - 4 * a**2 * c
        self.assertEqual(S.expand(v * inverse_mod_z - 1 + 4 * a**2 * z), 0)
        points = ({a: 0, t: 0, sigma: 0, c: 0},
                  {a: 1, t: 0, sigma: 1, c: -S.Rational(1, 3)})
        self.assertEqual([z.subs(point) for point in points], [0, 0])
        self.assertEqual([v.subs(point) for point in points], [1, 3])
        self.assertEqual([S.cancel(v * inverse_mod_z).subs(point) for point in points], [1, 1])

        # In R=C[a,t,b], h=b/a has a genuine a-adic pole.
        b = S.symbols("b")
        self.assertEqual(S.fraction(b / a), (b, a))
        self.assertEqual(S.cancel((b / a).subs(b, a**2 * c) - h), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
