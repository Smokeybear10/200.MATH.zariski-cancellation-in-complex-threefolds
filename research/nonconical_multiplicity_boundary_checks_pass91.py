"""Exact finite controls for the pass91 multiplicity boundary.

This checks a changed presentation of the retained Weitzenbock model.
It does not supply an original nonconical highest-adjoint frame or test
the general DVR descent theorem, faithful flatness, or normalization.
"""

import unittest

import sympy as sp


class MultiplicityBoundaryChecks(unittest.TestCase):
    def test_presentation_fibers_and_original_coordinate_boundary(self):
        u, p, y, z, eta, Y, Z, tau = sp.symbols("u p y z eta Y Z tau")
        coords = (u, p, y, z)
        invariant = p * z - y**2

        def derive(field, expression):
            return sp.expand(sum(f * sp.diff(expression, x)
                                 for f, x in zip(field, coords)))

        def bracket(left, right):
            return tuple(sp.expand(derive(left, r) - derive(right, l))
                         for l, r in zip(left, right))

        def substitute(expressions, replacements):
            return tuple(sp.expand(f.subs(replacements, simultaneous=True))
                         for f in expressions)

        E = (1, 0, 0, 0)
        N = (0, 0, p, 2 * y)
        self.assertEqual(derive(N, invariant), 0)
        self.assertEqual(bracket(E, N), (0, 0, 0, 0))
        self.assertEqual(sp.gcd(p, 2 * y), 1)
        for x in coords:
            self.assertEqual(derive(N, derive(N, derive(N, x))), 0)

        # The exact smaller-ring relation and the integral extra generator.
        relation = p**3 * Z - Y**2 - p**2 * eta
        self.assertEqual(
            sp.expand(relation.subs(
                {Y: p * y, Z: z, eta: invariant}, simultaneous=True)), 0)
        self.assertEqual(sp.expand(y**2 - (p * z - invariant)), 0)
        self.assertEqual(sp.cancel((p * y) / p - y), 0)
        self.assertEqual(sp.cancel((invariant + y**2) / p - z), 0)

        # h=0 gives the exact displayed generator pencil, without a frame claim.
        h, c = sp.Integer(0), y
        self.assertEqual(sp.expand(c + tau * h - y), 0)

        # The full R divisor fiber is nonreduced; its image kills Y.
        self.assertEqual(sp.expand(relation.subs(p, 0)), -Y**2)
        full_fiber = sp.groebner([Y**2], Y, Z)
        self.assertEqual(full_fiber.reduce(Y**2)[1], 0)
        self.assertEqual(full_fiber.reduce(Y)[1], Y)
        self.assertEqual(sp.expand((p * y).subs(p, 0)), 0)

        # In the whole A fiber, 2y is a unit over C(eta).
        fiber_polynomial = y**2 + eta
        inverse_product = sp.cancel((2 * y) * (-y / (2 * eta)) - 1)
        self.assertEqual(
            sp.rem(inverse_product, fiber_polynomial, y,
                   domain=sp.QQ.frac_field(eta)), 0)
        self.assertEqual(derive(N, z).subs(p, 0), 2 * y)
        self.assertEqual(derive(N, y).subs(p, 0), 0)

        # A genuine polynomial coordinate tuple, with both inverse orders.
        U, P, Z0, W = sp.symbols("U P Z0 W")
        forward = (u, p, z, y + u**2)
        inverse = (U, P, W - U**2, Z0)
        self.assertEqual(
            substitute(forward, dict(zip(coords, inverse))), (U, P, Z0, W))
        self.assertEqual(
            substitute(inverse, dict(zip((U, P, Z0, W), forward))), coords)
        self.assertEqual(sp.Matrix(forward).jacobian(coords).det(), -1)
        for x in forward[:3]:
            self.assertEqual(derive(E, derive(E, x)), 0)
        self.assertEqual(derive(E, derive(E, forward[3])), 2)

        # Its true top field differs from the chosen Weitzenbock field.
        original_u_partial = (1, 0, -2 * u, 0)
        highest = bracket(E, original_u_partial)
        self.assertEqual(highest, (0, 0, -2, 0))
        self.assertEqual(derive(highest, z), 0)
        self.assertEqual(derive(N, z), 2 * y)

        # Substituting py into that tuple destroys coordinate generation.
        candidate = sp.Matrix((u, p * y, z, y + u**2))
        self.assertEqual(sp.expand(candidate.jacobian(coords).det()), -y)


if __name__ == "__main__":
    unittest.main(verbosity=2)
