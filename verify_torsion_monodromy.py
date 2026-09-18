#!/usr/bin/env python3
"""Finite cyclic-group controls, not a verification of the topology."""

import itertools
import math
import unittest


def graph_cohomology_orders(order, multipliers):
    """Orders of ker(delta), coker(delta) on Z/order -> (Z/order)^s."""
    if type(order) is not int or order < 1 or not multipliers:
        raise ValueError("Positive integer order and at least one loop required")
    if any(type(m) is not int or math.gcd(m, order) != 1 for m in multipliers):
        raise ValueError("Each multiplier must act as a cyclic-group automorphism")
    values = [tuple(((m-1)*t) % order for m in multipliers)
              for t in range(order)]
    zero = (0,)*len(multipliers)
    kernel = sum(value == zero for value in values)
    image = len(set(values))
    return kernel, order**len(multipliers)//image


class TorsionMonodromyChecks(unittest.TestCase):
    def test_order_formula_exhaustive_small_cyclic_groups(self):
        for order in range(1, 19):
            units = [m for m in range(order) if math.gcd(m, order) == 1]
            for loops in (1, 2):
                for multipliers in itertools.product(units, repeat=loops):
                    h0, h1 = graph_cohomology_orders(order, multipliers)
                    self.assertEqual(h1, order**(loops-1)*h0)

    def test_one_loop_nonzero_torsion_with_zero_invariants(self):
        self.assertEqual(graph_cohomology_orders(3, [-1]), (1, 1))
        for order in (5, 7, 9, 15):
            self.assertEqual(graph_cohomology_orders(order, [-1]), (1, 1))

    def test_even_order_minus_identity_is_not_fixed_free(self):
        for order in (2, 4, 6, 8, 10, 12):
            self.assertEqual(graph_cohomology_orders(order, [-1]), (2, 2))

    def test_trivial_monodromy_retains_every_invariant(self):
        for order in range(1, 15):
            for loops in (1, 2, 3):
                self.assertEqual(graph_cohomology_orders(order, [1]*loops),
                                 (order, order**loops))

    def test_adding_regular_value_multiplies_cokernel_order(self):
        for order, multipliers in [(3, [-1]), (5, [2, 3]), (15, [4, 2])]:
            h0, h1 = graph_cohomology_orders(order, multipliers)
            added_h0, added_h1 = graph_cohomology_orders(order, multipliers+[1])
            self.assertEqual(added_h0, h0)
            self.assertEqual(added_h1, order*h1)

    def test_invalid_monodromies_rejected(self):
        for order, multipliers in [(0, [1]), (3, []), (4, [2]),
                                   (3.0, [1]), (5, [1.0])]:
            with self.subTest(order=order, multipliers=multipliers):
                with self.assertRaises(ValueError):
                    graph_cohomology_orders(order, multipliers)


if __name__ == "__main__":
    unittest.main(verbosity=2)
