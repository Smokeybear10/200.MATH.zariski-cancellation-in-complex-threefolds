"""Finite exact conic controls, not a proof of the topological criterion.

No solver or research-package imports. The universal flatness and
peripheral-cycle arguments are written separately.
"""

import unittest
import sympy as s


class FlatConicGateChecks(unittest.TestCase):
    def test_formal_conic_action_and_second_image(self):
        a, b, c, d, e, q, z, w = s.symbols("a b c d e q z w")
        r = a*z+b*w
        p = a*c+b*d
        dz, dw = e*b*r+c, -e*a*r+d

        def deriv(f):
            return s.expand(s.diff(f, z)*dz+s.diff(f, w)*dw)

        relation = e*r*r-2*d*z+2*c*w-q
        self.assertEqual(deriv(r), p)
        self.assertEqual(deriv(relation), 0)
        self.assertEqual(deriv(dz), s.expand(e*b*p))
        self.assertEqual(deriv(dw), s.expand(-e*a*p))
        self.assertEqual(deriv(deriv(dz)), 0)
        self.assertEqual(deriv(deriv(dw)), 0)
        # The coefficient matrix of linear coordinates r and -d*z+c*w
        # has determinant p, so the generic conic solves its companion.
        self.assertEqual(s.det(s.Matrix([[a, b], [-d, c]])), p)

    def test_linear_and_vertical_closed_fibers_are_distinct(self):
        u, v, z, w = s.symbols("u v z w")
        r = u*z+v*w
        # Weak-hypothesis example: at the origin the conic is a line.
        linear = r*r+2*w-v
        self.assertEqual(linear.subs({u: 0, v: 0}), 2*w)
        self.assertEqual((1+v*r).subs({u: 0, v: 0}), 1)
        # Auxiliary conic only: its whole closed fiber is a plane.
        # This ring is NOT asserted faithfully flat or stably polynomial.
        vertical = r*r-2*v*z+2*u*w
        p = u*u+v*v
        self.assertEqual(vertical.subs({u: 0, v: 0}), 0)
        self.assertEqual((v*r+u).subs({u: 0, v: 0}), 0)
        self.assertEqual((-u*r+v).subs({u: 0, v: 0}), 0)
        self.assertEqual(s.diff(p, u).subs({u: 0, v: 0}), 0)
        self.assertEqual(s.diff(p, v).subs({u: 0, v: 0}), 0)
        self.assertEqual(s.expand(p-u*u-v*v), 0)
        self.assertNotEqual(s.Poly(vertical, z, w).as_expr(), 0)


if __name__ == "__main__":
    unittest.main()
