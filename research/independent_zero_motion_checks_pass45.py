"""Finite actual-action mechanisms for independent zero-motion descent.

These are lower-level polynomial controls for the gradient alternatives,
not realizations of the entire independent nonconstant high-top frame.
The binary control deliberately does not preserve the actual bad plane.
"""

import unittest

import sympy as sp


def act(field, polynomial, variables):
    return sp.expand(sum(c * sp.diff(polynomial, x)
                         for c, x in zip(field, variables)))


def bracket(left, right, variables):
    return tuple(sp.expand(act(left, r, variables) - act(right, l, variables))
                 for l, r in zip(left, right))


def sub(polynomial, mapping):
    return sp.expand(polynomial.subs(mapping, simultaneous=True))


class IndependentZeroMotionChecks(unittest.TestCase):
    def test_surface_good_gradient_and_polynomial_replica_relation(self):
        a, b, y, z = sp.symbols("a b y z")
        variables = (a, b, y, z)
        e = (sp.Integer(1), sp.Integer(0), a, sp.Integer(0))
        tc = (1, 0, 0, 0)
        other = (0, 1, 0, 0)
        g = b * z + 1
        u = bracket(e, tc, variables)
        v = (0, 0, g, 0)
        self.assertEqual(tuple(sp.expand(g * c + d) for c, d in zip(u, v)),
                         (0, 0, 0, 0))
        self.assertEqual(bracket(e, v, variables), (0, 0, 0, 0))
        self.assertEqual(sp.Matrix.hstack(sp.Matrix(e), sp.Matrix(v)).rank(), 2)
        good_gradient = (g, sp.diff(g, a), sp.diff(g, b))
        self.assertEqual(sp.Matrix(good_gradient).jacobian(variables).rank(), 2)
        for f in good_gradient:
            self.assertEqual(act(e, f, variables), 0)
            self.assertEqual(act(v, f, variables), 0)
            self.assertEqual(act(tc, f, variables), 0)
        for field in (tc, other):
            top = bracket(e, field, variables)
            identity = tuple(sp.expand(c + d) for c, d in zip(
                bracket(tc, top, variables), bracket(u, field, variables)))
            self.assertEqual(identity, (0, 0, 0, 0))
        # Actual original slice and two-sided coordinate inverse.
        s, bb, j, zz = sp.symbols("s bb j zz")
        new = (s, bb, j, zz)
        forward = (a, b, y - a**2 / 2, z)
        inverse = (s, bb, j + s**2 / 2, zz)
        self.assertEqual(tuple(sub(f, dict(zip(new, forward))) for f in inverse),
                         variables)
        self.assertEqual(tuple(sub(f, dict(zip(variables, inverse))) for f in forward),
                         new)

    def test_curve_good_gradient_with_actual_triangular_coordinate(self):
        a, b, y, z = sp.symbols("a b y z")
        variables = (a, b, y, z)
        e = (sp.Integer(1), -2 * a * y, a, sp.Integer(0))
        primitive = (0, -2 * y, 1, 0)
        coordinate = b + y**2
        g = coordinate**3 + coordinate
        self.assertEqual(act(e, g, variables), 0)
        self.assertEqual(act(primitive, g, variables), 0)
        self.assertEqual(sp.diff(coordinate, a), 0)
        self.assertEqual(sp.diff(coordinate, b), 1)
        gradient = (g, sp.diff(g, a), sp.diff(g, b))
        self.assertEqual(sp.Matrix(gradient).jacobian(variables).rank(), 1)
        self.assertEqual(sp.cancel(sp.diff(g, b) / (3 * coordinate**2 + 1)), 1)
        s, vv, w, zz = sp.symbols("s vv w zz")
        new = (s, vv, w, zz)
        forward = (a, coordinate, y - a**2 / 2, z)
        yy = w + s**2 / 2
        inverse = (s, vv - yy**2, yy, zz)
        self.assertEqual(tuple(sub(f, dict(zip(new, forward))) for f in inverse),
                         variables)
        self.assertEqual(tuple(sub(f, dict(zip(variables, inverse))) for f in forward),
                         new)
        reconstructed = tuple(sub(sp.diff(f, s), dict(zip(new, forward)))
                              for f in inverse)
        self.assertEqual(reconstructed, e)
        self.assertEqual(tuple(act(e, f, variables) for f in forward), (1, 0, 0, 0))

    def test_binary_invariant_without_plane_preservation(self):
        a, b, y, z = sp.symbols("a b y z")
        variables = (a, b, y, z)
        e = (sp.Integer(1), sp.Integer(0), a, 2 * a * y)
        coordinate = z - y**2
        g = coordinate**2 + 1
        self.assertEqual(act(e, coordinate, variables), 0)
        self.assertEqual(act(e, g, variables), 0)
        self.assertEqual((sp.diff(g, a), sp.diff(g, b)), (0, 0))
        self.assertIn(a, act(e, y, variables).free_symbols)
        self.assertIn(a, act(e, z, variables).free_symbols)
        # The full-gradient inference would be false in this actual action.
        self.assertNotEqual(act(e, sp.diff(g, y), variables), 0)
        self.assertEqual(act(e, sp.diff(g, y), variables), sp.expand(-4 * a * coordinate))
        s, bb, w, p = sp.symbols("s bb w p")
        new = (s, bb, w, p)
        forward = (a, b, y - a**2 / 2, coordinate)
        yy = w + s**2 / 2
        inverse = (s, bb, yy, p + yy**2)
        self.assertEqual(tuple(sub(f, dict(zip(new, forward))) for f in inverse),
                         variables)
        self.assertEqual(tuple(sub(f, dict(zip(variables, inverse))) for f in forward),
                         new)
        self.assertEqual(tuple(act(e, f, variables) for f in forward), (1, 0, 0, 0))
        # Separate actual inverse within the fixed two-variable subring.
        q, h = sp.symbols("q h")
        plane_forward = (y, coordinate)
        plane_inverse = (q, h + q**2)
        self.assertEqual(tuple(sub(f, dict(zip((q, h), plane_forward)))
                               for f in plane_inverse), (y, z))
        self.assertEqual(tuple(sub(f, dict(zip((y, z), plane_inverse)))
                               for f in plane_forward), (q, h))


if __name__ == "__main__":
    unittest.main(verbosity=2)
