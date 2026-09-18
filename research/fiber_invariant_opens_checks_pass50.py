"""Finite actual square-root slice control for pass50.

This checks a genuine lower-profile polynomial coordinate frame, not
the unresolved independent (1,1,2,2) frame. It tests the exact failure
of finite intrinsic degree for the constructed etale slice. The
universal denominator and fiber-generation statements remain proofs.
"""

import unittest
import sympy as sp


class FiberInvariantOpensChecks(unittest.TestCase):
    def test_actual_etale_slice_has_infinite_derivative_recurrence(self):
        u, v, a, s, k = sp.symbols("u v a s k")
        xx, ss, uu, vv = sp.symbols("X S U V")
        variables = (a, s, u, v)
        physical = (a + s + u*s**2/2, s, u, v)
        inverse = (xx - ss - uu*ss**2/2, ss, uu, vv)

        for expr, expected in zip(
                inverse, (a, s, u, v)):
            self.assertEqual(
                sp.expand(expr.subs(
                    dict(zip((xx, ss, uu, vv), physical)),
                    simultaneous=True) - expected), 0)
        for expr, expected in zip(physical, (xx, ss, uu, vv)):
            self.assertEqual(
                sp.expand(expr.subs(dict(zip(variables, inverse)),
                                    simultaneous=True) - expected), 0)

        def act(field, expr):
            return sp.expand(sum(c * sp.diff(expr, z)
                                 for c, z in zip(field, variables)))

        def bracket(first, second):
            return tuple(sp.expand(act(first, c) - act(second, b))
                         for b, c in zip(first, second))

        efield = (sp.Integer(0), sp.Integer(1),
                  sp.Integer(0), sp.Integer(0))
        partials = (
            (1, 0, 0, 0),
            (-1-u*s, 1, 0, 0),
            (-s**2/2, 0, 1, 0),
            (0, 0, 0, 1),
        )
        for i, field in enumerate(partials):
            self.assertEqual(tuple(act(field, expr) for expr in physical),
                             tuple(sp.Integer(i == j) for j in range(4)))
        heights = []
        for partial in partials:
            field = tuple(sp.sympify(c) for c in partial)
            height = 0
            while True:
                next_field = bracket(efield, field)
                if all(c == 0 for c in next_field):
                    heights.append(height)
                    break
                height += 1
                self.assertLess(height, 4)
                field = next_field
        self.assertEqual(heights, [0, 1, 2, 0])

        x = physical[0]
        p = act(efield, x)
        h = act(efield, p)
        invariant = sp.expand(p**2 - 2*h*x)
        self.assertEqual(p, 1 + u*s)
        self.assertEqual(h, u)
        self.assertEqual(invariant, 1 - 2*u*a)
        relation = k**2 - invariant

        def zero_on_cover(expr):
            numerator = sp.fraction(sp.cancel(expr))[0]
            remainder = sp.rem(numerator, relation, k)
            return sp.expand(remainder) == 0

        sigma = s + 2*a/(1+k)
        self.assertEqual(sp.diff(sigma, s), 1)
        self.assertTrue(zero_on_cover(h*sigma - p + k))
        self.assertTrue(zero_on_cover(
            sigma - s - (1-k)/u))
        self.assertTrue(zero_on_cover(
            sigma - 2*x/(p+k)))
        # The latter denominator is not killed by E, so its
        # localization does not preserve local nilpotence.
        self.assertEqual(sp.diff(p+k, s), u)

        def intrinsic(expr):
            return sp.cancel(sp.diff(expr, a) -
                             u*sp.diff(expr, k)/k)

        self.assertEqual(intrinsic(relation), 0)
        iterated_k = k
        falling = sp.Integer(1)
        for n in range(1, 8):
            falling *= sp.Rational(1, 2) - (n-1)
            iterated_k = intrinsic(iterated_k)
            expected = (-2*u)**n * falling * k**(1-2*n)
            self.assertEqual(sp.cancel(iterated_k-expected), 0)
            self.assertNotEqual(falling, 0)
            self.assertNotEqual(sp.cancel(expected), 0)

        projected_s = sp.cancel(s-sigma)
        derivative = projected_s
        iterated_k = k
        for n in range(1, 8):
            derivative = intrinsic(derivative)
            iterated_k = intrinsic(iterated_k)
            self.assertTrue(zero_on_cover(derivative-iterated_k/u))
            self.assertNotEqual(sp.cancel(iterated_k/u), 0)

        # The original actual coordinate slice still exists. The
        # example only refutes the etale-to-bounded-degree inference.
        self.assertEqual(act(efield, s), 1)
        self.assertEqual(intrinsic(s), 0)


if __name__ == "__main__":
    unittest.main()

