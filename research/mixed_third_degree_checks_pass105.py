"""Finite coefficient controls, not proofs of the actual frame hypotheses.

The first method checks the two weighted derivative formulas for an
arbitrary symbolic coefficient. The second checks an intrinsic polynomial
line whose selected degree-four function specializes to degree three.
It has no mixed closed fiber or verified original four-coordinate frame.
"""

import unittest

import sympy as sp


class MixedThirdDegreeChecks(unittest.TestCase):
    def test_weighted_fourth_and_fifth_derivatives(self):
        x, y, c, gamma, delta = sp.symbols("x y c gamma delta")
        beta = sp.Function("beta")(c)

        def leading(value):
            return sp.expand(gamma * x * sp.diff(value, y)
                             + delta * y * sp.diff(value, c))

        iterates = [beta * y]
        for _ in range(5):
            iterates.append(leading(iterates[-1]))
        fourth = (15 * gamma ** 2 * delta ** 2 * sp.diff(beta, c, 2) * x ** 2 * y
                  + 10 * gamma * delta ** 3 * sp.diff(beta, c, 3) * x * y ** 3
                  + delta ** 4 * sp.diff(beta, c, 4) * y ** 5)
        fifth = (15 * gamma ** 3 * delta ** 2 * sp.diff(beta, c, 2) * x ** 3
                 + 45 * gamma ** 2 * delta ** 3 * sp.diff(beta, c, 3) * x ** 2 * y ** 2
                 + 15 * gamma * delta ** 4 * sp.diff(beta, c, 4) * x * y ** 4
                 + delta ** 5 * sp.diff(beta, c, 5) * y ** 6)
        self.assertEqual(sp.expand(iterates[4] - fourth), 0)
        self.assertEqual(sp.expand(iterates[5] - fifth), 0)
        for order in (4, 5):
            self.assertEqual(
                sp.expand(iterates[order].subs(gamma, 0)
                          - delta ** order * sp.diff(beta, c, order) * y ** (order + 1)),
                0,
            )

    def test_intrinsic_odd_specialization_is_possible(self):
        x, z, v, w, t = sp.symbols("x z v w t")
        selected = x * v ** 4 + v ** 3 - v ** 2
        self.assertEqual(sp.degree(selected, v), 4)
        self.assertEqual(sp.degree(selected.subs(x, 0), v), 3)
        self.assertEqual(sp.diff(selected, v, 4), 24 * x)
        self.assertEqual(sp.diff(selected, v, 5), 0)
        self.assertEqual(sp.diff(selected.subs(x, 0), v, 3), 6)
        self.assertEqual(sp.diff(x, v), 0)
        self.assertEqual(sp.diff(z, v), 0)
        # An integral generic rescaling detects a possible escaping branch.
        relation = w ** 4 + w ** 3 - x * w ** 2 - t * x ** 3
        self.assertEqual(sp.expand(relation.subs({w: x * v, t: selected})), 0)
        self.assertEqual(sp.factor(relation.subs(x, 0)), w ** 3 * (w + 1))
        self.assertEqual(sp.diff(relation, w).subs({x: 0, w: -1}), -1)
        # This calculation does not assert that this monic model is normal.
        # The original ring is S[v], so its original closed fiber is reduced A1.


if __name__ == "__main__":
    unittest.main(verbosity=2)
