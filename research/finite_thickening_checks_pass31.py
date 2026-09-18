"""Finite controls for the written all-thickening/algebraization distinction."""

import unittest
import sympy as sp


f, s, z, t = sp.symbols("f s z t")
variables = (f, s, z, t)


def apply(field, expr):
    return sp.expand(sum(c*sp.diff(expr, v) for c, v in zip(field, variables)))


def iterate(field, expr, count):
    for _ in range(count):
        expr = apply(field, expr)
    return expr


def remainder(expr, order):
    return sp.rem(expr, f**order, f)


class FiniteThickeningChecks(unittest.TestCase):
    def test_non_lnd_sliced_lifts_and_exact_jet_indices(self):
        for a in range(1, 5):
            field = (0, 1, f**a*z, 0)
            self.assertEqual(apply(field, f), 0)
            self.assertEqual(apply(field, s), 1)
            for q in range(1, 9):
                self.assertEqual(iterate(field, z, q), f**(a*q)*z)
            for order in range(1, 15):
                index = (order+a-1)//a
                self.assertEqual(remainder(iterate(field, z, index), order), 0)
                self.assertNotEqual(remainder(iterate(field, z, index-1), order), 0)
                self.assertGreaterEqual(1+index*a, order)

    def test_double_thickening_normal_operator(self):
        # g=s is a forbidden nonzero first normal coefficient.
        field = (f*s, 1, 0, 0)
        h = sp.Integer(1)
        for q in range(1, 9):
            h = sp.expand(sp.diff(h, s)+s*h)
            self.assertEqual(remainder(iterate(field, f, q), 2), f*h)
            self.assertEqual(sp.Poly(h, s).degree(), q)
            self.assertEqual(sp.Poly(h, s).LC(), 1)

    def test_exact_F_preservation_not_necessary_for_all_jets(self):
        field = (f**2, 1, 0, 0)
        for q in range(1, 10):
            self.assertEqual(iterate(field, f, q), sp.factorial(q)*f**(q+1))
        for order in range(2, 12):
            self.assertEqual(remainder(iterate(field, f, order-1), order), 0)
            self.assertNotEqual(remainder(iterate(field, f, order-2), order), 0)

    def test_positive_finite_degree_certificate(self):
        field = (0, 1, s**2, 0)
        degree = 2
        for variable, index in ((f, 1), (s, 2), (z, 4), (t, 1)):
            order = 2+index*(degree-1)
            actual = iterate(field, variable, index)
            self.assertEqual(remainder(actual, order), 0)
            self.assertGreater(order, 1+index*(degree-1))
            self.assertEqual(actual, 0)

    def test_compatible_finite_exponentials_have_unbounded_degree(self):
        parameter = sp.symbols("parameter")
        for a in range(1, 4):
            for order in range(2, 12):
                index = (order+a-1)//a
                truncated = sum(parameter**j*f**(a*j)/sp.factorial(j) for j in range(index))
                higher_index = (order+1+a-1)//a
                higher = sum(parameter**j*f**(a*j)/sp.factorial(j) for j in range(higher_index))
                self.assertEqual(remainder(sp.expand(higher-truncated), order), 0)
                self.assertEqual(sp.Poly(truncated, parameter).degree(), index-1)
                self.assertEqual(remainder(sp.expand(truncated*truncated.subs(parameter, -parameter)-1), order), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
