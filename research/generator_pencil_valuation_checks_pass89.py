"""One finite-case test for an all-integer, algebra-only pencil family."""

import unittest

import sympy as S


class GeneratorPencilValuationChecks(unittest.TestCase):
    def test_pole_orders_geometric_recovery_and_boundaries(self):
        a, t, b, c, tau = S.symbols("a t b c tau")

        def order_at_a_zero(expression):
            numerator, denominator = S.fraction(S.cancel(expression))
            order_n = min(monomial[0] for monomial in S.Poly(numerator, a).monoms())
            order_d = min(monomial[0] for monomial in S.Poly(denominator, a).monoms())
            return order_n - order_d

        for d, j in ((2, 1), (3, 1), (3, 2), (5, 2), (6, 4)):
            with self.subTest(d=d, j=j):
                N = (d + j - 1) // j
                self.assertGreaterEqual(j * N - d, 0)
                G = sum((-tau * a**j)**k for k in range(N))
                h = a**j * c
                recovered = G * (c + tau * h) + (-tau)**N * a**(j * N - d) * b
                self.assertEqual(S.expand(recovered.subs(b, a**d * c) - c), 0)
                self.assertEqual(S.expand(G * (1 + tau * a**j)
                                         - 1 + (-tau * a**j)**N), 0)
                c_fraction, h_fraction = b / a**d, b / a**(d - j)
                self.assertEqual(order_at_a_zero(c_fraction), -d)
                self.assertEqual(order_at_a_zero(h_fraction), -(d - j))
                self.assertLess(order_at_a_zero(c_fraction), order_at_a_zero(h_fraction))
                self.assertEqual(S.cancel(a**d * c_fraction - b), 0)
                self.assertEqual(order_at_a_zero(a**d), d)
                self.assertGreaterEqual(d, d - j + 1)
                if j == 1:
                    self.assertEqual(d, -(order_at_a_zero(h_fraction)) + 1)

        # d=j=1: squarefree leading coefficient and slope already in R.
        squarefree_generator = c + tau * a * c
        self.assertEqual(S.expand((squarefree_generator - tau * b).subs(b, a * c) - c), 0)
        self.assertEqual(S.cancel((a * c).subs(c, b / a) - b), 0)
        # j=0: the proposed generator collapses at tau=-1.
        self.assertEqual((c + tau * c).subs(tau, -1), 0)
        self.assertEqual(order_at_a_zero(b / a**2), -2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
