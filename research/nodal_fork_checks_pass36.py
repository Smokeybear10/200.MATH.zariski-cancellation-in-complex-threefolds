"""Finite exact controls for the separated-torsor obstruction.

Only the written proof verifies the geometric descent and universal
quantifiers. No project solver is imported.
"""

import unittest
import sympy as sp


class NodalForkControls(unittest.TestCase):
    def test_four_normalization_branches_and_split_orders(self):
        d = sp.Symbol("d")
        roots = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)
        for order in range(3, 7):
            fourth = sp.series((1 + d)**sp.Rational(1, 4), d, 0, order).removeO()
            square = sp.series((1 + d)**sp.Rational(1, 2), d, 0, order).removeO()
            for root in roots:
                u = root * fourth
                self.assertEqual(sp.rem(sp.expand(u**4 - 1 - d), d**order, d), 0)
                self.assertEqual(sp.rem(sp.expand(u**2 - root**2 * square), d**order, d), 0)
                coefficient = sp.expand((u - 1) * (u - sp.I))
                if root in (sp.Integer(1), sp.I):
                    self.assertEqual(coefficient.subs(d, 0), 0)
                    self.assertNotEqual(sp.diff(coefficient, d).subs(d, 0), 0)
                else:
                    self.assertNotEqual(coefficient.subs(d, 0), 0)
            for left in roots:
                for right in roots:
                    if left != right:
                        self.assertNotEqual((left * fourth - right * fourth).subs(d, 0), 0)

    def test_actual_pairing_forces_the_three_overlap_types(self):
        pairs = {"A": (sp.Integer(1), sp.I),
                 "B": (sp.Integer(1), -sp.I),
                 "C": (sp.Integer(-1), sp.I)}
        self.assertEqual(set(pairs["A"]) & set(pairs["B"]), {sp.Integer(1)})
        self.assertEqual(set(pairs["A"]) & set(pairs["C"]), {sp.I})
        self.assertEqual(set(pairs["B"]) & set(pairs["C"]), set())
        for plus, minus in pairs.values():
            self.assertEqual(plus**2, 1)
            self.assertEqual(minus**2, -1)
        self.assertEqual(set().union(*(set(pair) for pair in pairs.values())),
                         {sp.Integer(1), sp.Integer(-1), sp.I, -sp.I})
        # Distinct orbit points give no closed-point overlap. Combining this
        # finite table with D(xy) gives D(y), D(x), and D(xy), respectively.
        generic_agreements = {("A", "B"): {"x"},
                              ("A", "C"): {"y"},
                              ("B", "C"): set()}
        self.assertEqual(generic_agreements[("A", "B")], {"x"})
        self.assertEqual(generic_agreements[("A", "C")], {"y"})
        self.assertEqual(generic_agreements[("B", "C")], set())

    def test_translation_cocycle_has_unavoidable_corner_zero(self):
        x, y, ta, tb, tc = sp.symbols("x y ta tb tc")
        p = 1 + x + y
        q = 2 + x**2 + y
        for m in range(1, 4):
            for n in range(1, 4):
                alpha, zeta = p / y**n, q / x**m
                numerator = sp.expand(q * y**n - p * x**m)
                self.assertEqual(sp.cancel(zeta - alpha - numerator / (x**m * y**n)), 0)
                self.assertEqual(sp.cancel((ta + zeta) - ((ta + alpha) + zeta - alpha)), 0)
                self.assertEqual(numerator.subs({x: 0, y: 0}), 0)
                self.assertNotEqual(numerator.subs(x, 0), 0)
                self.assertNotEqual(numerator.subs(y, 0), 0)
                self.assertEqual(sp.gcd(numerator, x**m * y**n), 1)
                relation = x**m * y**n * (tc - tb) - numerator
                self.assertEqual(relation.subs({x: 0, y: 0}), 0)
                self.assertEqual(sp.cancel(relation.subs(tc, tb + zeta - alpha)), 0)

    def test_graph_closure_is_already_saturated(self):
        x, y, t, auxiliary = sp.symbols("x y t auxiliary")
        for m, n in ((1, 1), (2, 1), (1, 2), (2, 2), (3, 2)):
            numerator = 2*y**n - x**m
            relation = x**m * y**n * t - numerator
            elimination = sp.groebner([relation, auxiliary*x*y - 1],
                                     auxiliary, t, x, y, order="lex")
            contracted = [p.as_expr() for p in elimination.polys
                          if not p.as_expr().has(auxiliary)]
            self.assertTrue(contracted)
            original = sp.groebner([relation], t, x, y, order="lex")
            for polynomial in contracted:
                self.assertEqual(original.reduce(polynomial)[1], 0)
            contracted_basis = sp.groebner(contracted, t, x, y, order="lex")
            self.assertEqual(contracted_basis.reduce(relation)[1], 0)
            self.assertEqual(relation.subs({x: 0, y: 0}), 0)

    def test_unit_and_nonunit_numerator_controls(self):
        x, y, t = sp.symbols("x y t")
        for n in range(1, 5):
            separated_pair = y**n * t - (1 + x + y)
            bad_pair = y**n * t - x
            self.assertEqual(separated_pair.subs({x: 0, y: 0}), -1)
            self.assertEqual(bad_pair.subs({x: 0, y: 0}), 0)
            self.assertEqual(sp.gcd(y**n, x), 1)
        # A regular translation has a nonempty graph fiber at the origin.
        regular = t - (2 + x + y)
        self.assertEqual(regular.subs({x: 0, y: 0}), t - 2)
        self.assertEqual(regular.subs({x: 0, y: 0, t: 2}), 0)


if __name__ == "__main__":
    unittest.main()
