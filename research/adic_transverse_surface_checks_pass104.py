"""Finite controls for the transverse surface argument, not a proof checker."""

import unittest

import sympy as sp


class AdicTransverseSurfaceChecks(unittest.TestCase):
    def test_finite_lengths_bases_and_corrected_base(self):
        x, y, r = sp.symbols("x y r")
        for h in (y**2, y**2 * (y - 1)):
            degree = sp.degree(h, y)
            for k in range(1, 7):
                with self.subTest(h=h, k=k):
                    ideal = [x**a * h ** (k - a) for a in range(k + 1)]
                    basis = sp.groebner(ideal, x, y, r, order="lex")
                    exponents = [
                        (a, b)
                        for a in range(k)
                        for b in range(int(degree) * (k - a))
                    ]
                    self.assertEqual(len(exponents), degree * k * (k + 1) // 2)
                    # These exact normal forms have distinct monomials.
                    for a, b in exponents:
                        monomial = x**a * y**b
                        self.assertEqual(basis.reduce(monomial)[1], monomial)
                    for generator in ideal:
                        self.assertEqual(basis.reduce(sp.expand(generator))[1], 0)
                    # Divisibility boundaries generate the initial monomial ideal.
                    leading = {p.LM(order="lex").exponents for p in basis.polys}
                    expected = {(a, int(degree) * (k - a), 0) for a in range(k + 1)}
                    self.assertEqual(leading, expected)
                    for e in range(1, 5):
                        original_f = h - x**e * r
                        corrected_f = original_f.subs(r, 0)
                        self.assertEqual(corrected_f, h)
                        self.assertEqual(sp.diff(original_f, r), -x**e)
                        difference = basis.reduce(original_f - corrected_f)[1]
                        self.assertEqual(difference, 0 if e >= k else -x**e * r)

    def test_mixed_ramification_truncation(self):
        y = sp.symbols("y")
        h = y**2 * (y - 1)
        self.assertEqual(sp.diff(h, y).subs(y, 0), 0)
        self.assertEqual(sp.diff(h, y, 2).subs(y, 0), -2)
        self.assertEqual(sp.diff(h, y).subs(y, 1), 1)
        for order in range(2, 11):
            with self.subTest(order=order):
                formal_y = y * sum(
                    (sp.binomial(sp.Rational(1, 2), j) * (-y) ** j for j in range(order)),
                    sp.S.Zero,
                )
                self.assertEqual(sp.diff(formal_y, y).subs(y, 0), 1)
                error = sp.Poly(sp.expand(formal_y**2 + h), y)
                self.assertTrue(all(power[0] >= order + 2 for power, _ in error.terms()))


if __name__ == "__main__":
    unittest.main()
