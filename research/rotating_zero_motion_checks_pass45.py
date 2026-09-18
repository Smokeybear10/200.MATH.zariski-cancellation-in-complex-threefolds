"""Finite exact controls for rotating-zero-motion-closure-pass45.md.

The two polynomial actions below test individual descent mechanisms.
Neither is asserted to realize the complete nonconstant high-flow,
nonzero-r dependent frame of the theorem. The last control is explicitly
a non-LND and tests the forbidden vertical leading term.
"""

import unittest

import sympy as sp


def act(coefficients, polynomial, variables):
    return sp.expand(sum(c * sp.diff(polynomial, v)
                         for c, v in zip(coefficients, variables)))


def bracket(left, right, variables):
    return tuple(sp.expand(act(left, c, variables)
                           - act(right, d, variables))
                 for c, d in zip(right, left))


def substitute(polynomial, mapping):
    return sp.expand(polynomial.subs(mapping, simultaneous=True))


class RotatingZeroMotionChecks(unittest.TestCase):
    def test_actual_gradient_and_mixed_columns(self):
        a, b, y, z, t = sp.symbols("a b y z t")
        variables = (a, b, y, z)
        fields = tuple(tuple(sp.Integer(i == j) for i in range(4))
                       for j in range(4))
        e = (sp.Integer(1), sp.Integer(0), a, sp.Integer(0))
        d = fields[2]
        tops = tuple(bracket(e, field, variables) for field in fields)
        self.assertEqual(tops[0], (0, 0, -1, 0))
        flow = (a + t, b, y + a * t + t**2 / 2, z)
        conjugates = tuple(tuple(fields[j][i] + t * tops[j][i]
                                 for i in range(4)) for j in range(4))
        for j in range(4):
            self.assertEqual(tuple(act(conjugates[j], f, variables)
                                   for f in flow), fields[j])
            mixed = tuple(sp.expand(v + w) for v, w in zip(
                bracket(fields[0], tops[j], variables),
                bracket(tops[0], fields[j], variables)))
            self.assertEqual(mixed, (0, 0, 0, 0))

        u = b * z
        gradient = [sp.diff(u, v) for v in variables]
        self.assertEqual(sp.Matrix([u] + gradient).jacobian(variables).rank(), 2)
        for f in [u] + gradient:
            self.assertEqual(act(e, f, variables), 0)
            self.assertEqual(act(d, f, variables), 0)
        # A separate curve-valued gradient gives an actual linear coordinate.
        v = b + 2 * z
        curve_u = v**3 + v
        self.assertEqual(sp.Matrix([curve_u] + [sp.diff(curve_u, x)
                                               for x in variables])
                         .jacobian(variables).rank(), 1)
        for x in variables:
            self.assertEqual(sp.cancel(sp.diff(curve_u, x) / (3 * v**2 + 1)),
                             sp.diff(v, x))
        s, j, vv, zz = sp.symbols("s j vv zz")
        forward = (a, y - a**2 / 2, v, z)
        inverse = (s, vv - 2 * zz, j + s**2 / 2, zz)
        new = (s, j, vv, zz)
        self.assertEqual(tuple(substitute(f, dict(zip(new, forward)))
                               for f in inverse), variables)
        self.assertEqual(tuple(substitute(f, dict(zip(variables, inverse)))
                               for f in forward), new)

    def test_actual_horizontal_top_and_polynomial_inverse(self):
        a, b, y, z = sp.symbols("a b y z")
        variables = (a, b, y, z)
        e = (sp.Integer(1), a * y**2, a, 2 * a * y)
        horizontal_top = tuple(sp.Poly(c, a).coeff_monomial(a)
                               for c in e[1:])
        self.assertEqual(horizontal_top, (y**2, 1, 2 * y))
        self.assertEqual(sp.Poly(e[0], a).degree(), 0)
        self.assertEqual(max(sp.Poly(c, a).degree() for c in e[1:]), 1)

        s, j, p, w = sp.symbols("s j p w")
        new = (s, j, p, w)
        forward = (a, b - y**3 / 3, z - y**2, y - a**2 / 2)
        yy = w + s**2 / 2
        inverse = (s, j + yy**3 / 3, yy, p + yy**2)
        self.assertEqual(tuple(substitute(f, dict(zip(new, forward)))
                               for f in inverse), variables)
        self.assertEqual(tuple(substitute(f, dict(zip(variables, inverse)))
                               for f in forward), new)
        # Differentiate the independent inverse to reconstruct E.
        reconstructed = tuple(substitute(sp.diff(f, s), dict(zip(new, forward)))
                              for f in inverse)
        self.assertEqual(reconstructed, e)
        self.assertEqual(tuple(act(e, f, variables) for f in forward),
                         (1, 0, 0, 0))
        for x in variables:
            value = x
            for _ in range(7):
                value = act(e, value, variables)
            self.assertEqual(value, 0)

        base = (b, y, z)
        self.assertEqual(act(horizontal_top, z - y**2, base), 0)
        self.assertEqual(act(horizontal_top, b - y**3 / 3, base), 0)
        self.assertEqual(act(horizontal_top, y, base), 1)
        self.assertEqual(bracket((1, 0, 0), horizontal_top, base), (0, 0, 0))
        # The invariant of the actual bad plane has a two-sided plane inverse.
        yy0, pp0 = sp.symbols("yy0 pp0")
        plane_forward = (y, z - y**2)
        plane_inverse = (yy0, pp0 + yy0**2)
        self.assertEqual(tuple(substitute(f, dict(zip((yy0, pp0), plane_forward)))
                               for f in plane_inverse), (y, z))
        self.assertEqual(tuple(substitute(f, dict(zip((y, z), plane_inverse)))
                               for f in plane_forward), (yy0, pp0))

    def test_primitive_conjugation_and_replica_warning(self):
        b, y, z, t = sp.symbols("b y z t")
        variables = (b, y, z)
        primitive = (y**2, sp.Integer(1), 2 * y)
        j = b - y**3 / 3
        p = z - y**2
        multiplier = (j**2 + 1) * (p + 1)
        replica = tuple(sp.expand(multiplier * c) for c in primitive)
        self.assertEqual(act(primitive, multiplier, variables), 0)
        self.assertEqual(sp.gcd_list(primitive), 1)
        self.assertEqual(sp.Poly(sp.gcd_list(replica), *variables).monic(),
                         sp.Poly(multiplier, *variables).monic())

        phi = {b: b + t, y: y, z: z}
        phi_inverse = {b: b - t, y: y, z: z}

        def conjugate(field):
            return tuple(substitute(act(field, substitute(x, phi_inverse), variables),
                                    phi) for x in variables)

        self.assertEqual(conjugate(primitive), primitive)
        shifted_multiplier = substitute(multiplier, phi)
        self.assertEqual(conjugate(replica),
                         tuple(sp.expand(shifted_multiplier * c) for c in primitive))
        ratio = sp.cancel(shifted_multiplier / multiplier)
        self.assertNotEqual(sp.denom(ratio), 1)
        self.assertNotEqual(bracket((1, 0, 0), replica, variables), (0, 0, 0))
        # Removing the actual common factor, not asserting a Bezout identity,
        # is what restores the primitive normalizer conclusion.
        divided = tuple(sp.cancel(c / multiplier) for c in replica)
        self.assertEqual(divided, primitive)

    def test_forbidden_vertical_homogeneous_top(self):
        a, b = sp.symbols("a b")
        # These are deliberately NOT LNDs or realized adjoint frames.
        for q in (0, 1, 3):
            field = (a**(q + 1), a**q)
            value = a
            factor = sp.Integer(1)
            for n in range(1, 7):
                value = act(field, value, (a, b))
                factor *= 1 + (n - 1) * q
                self.assertEqual(value, factor * a**(1 + n * q))
                self.assertNotEqual(value, 0)
            self.assertEqual(sp.rem(field[0], a, a), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
