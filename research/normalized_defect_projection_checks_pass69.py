"""Exact actual controls for localized defect projection and polynomial descent.

The first method starts from a polynomial coordinate automorphism and a true
coordinate partial, but its full adjoint profile is (5,5,3,2), not the target
moving frame. The other methods use actual commuting polynomial LNDs without
claiming that they are simultaneous columns of such a frame. Finite controls
do not establish universal coordinate recognition or cancellation.
"""

import unittest
import sympy as sp


class NormalizedDefectProjectionChecks(unittest.TestCase):
    def setUp(self):
        self.a, self.y, self.z, self.s = sp.symbols("a y z s")
        self.variables = sp.Matrix([self.a, self.y, self.z, self.s])
        self.e = sp.Matrix([0, 0, 0, 1])
        self.sigma = self.a * self.s + self.y / self.a
        self.f = self.a**2 * self.s + self.y

    def apply(self, field, expression):
        return sum(field[i] * sp.diff(expression, variable)
                   for i, variable in enumerate(self.variables))

    def bracket(self, first, second):
        return sp.Matrix([self.apply(first, second[i]) - self.apply(second, first[i])
                          for i in range(4)])

    def assert_zero(self, expression):
        entries = expression if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def project(self, field):
        return field - self.apply(field, self.sigma) * self.e / self.a

    def test_actual_coordinate_partial_and_minimal_clearing_power(self):
        a, y, z, s = self.variables
        aa = a + s * z / 2
        yy = y - a * s**2 * z / 2 - s**3 * z**2 / 8
        xx = z + a**2 * s**2 / 2 + y * s
        coordinates = sp.Matrix([s, aa, yy, xx])
        physical = sp.Matrix(sp.symbols("S A B X"))
        ss, av, yv, xv = physical
        zi = xv - av**2 * ss**2 / 2 - yv * ss
        ai = av - ss * zi / 2
        yi = yv + av * ss**2 * zi / 2 - ss**3 * zi**2 / 8
        inverse = sp.Matrix([ai, yi, zi, ss])
        self.assert_zero(coordinates.subs(dict(zip(self.variables, inverse)), simultaneous=True) - physical)
        self.assert_zero(inverse.subs(dict(zip(physical, coordinates)), simultaneous=True) - self.variables)
        jac = coordinates.jacobian(self.variables)
        self.assertEqual(sp.factor(jac.det()), -1)
        partials = jac.inv().applyfunc(sp.cancel)
        self.assert_zero(jac * partials - sp.eye(4))
        self.assert_zero(partials * jac - sp.eye(4))
        heights = [max(sp.degree(sp.expand(entry), s) for entry in partials[:, i] if entry != 0)
                   for i in range(4)]
        self.assertEqual(heights, [5, 5, 3, 2])
        self.assert_zero(coordinates.diff(s, 3) - sp.Matrix([0, 0, -3 * z**2 / 4, 0]))

        t = sp.Matrix([-s / 2, a * s**2 / 2, 1, 0])
        self.assert_zero(t - partials[:, 3])
        w = self.bracket(self.e, t)
        v = self.bracket(self.e, w)
        self.assert_zero(w - sp.Matrix([-sp.Rational(1, 2), a * s, 0, 0]))
        self.assert_zero(v - sp.Matrix([0, a, 0, 0]))
        self.assert_zero(self.bracket(self.e, v))
        delta = self.e / a
        normalized = self.bracket(delta, self.bracket(delta, t))
        projected = self.project(v)
        self.assert_zero(normalized - sp.Matrix([0, 1 / a, 0, -1 / a**3]))
        self.assert_zero(a**2 * normalized - projected)
        self.assert_zero(self.apply(delta, xx) - self.sigma)
        self.assert_zero(self.apply(delta, self.sigma) - 1)
        self.assert_zero(self.apply(v, self.sigma) - 1)
        self.assert_zero(self.apply(w, a) + sp.Rational(1, 2))
        self.assert_zero(self.apply(normalized, self.sigma))
        self.assertEqual(sp.denom(sp.cancel(projected[3])), a)
        self.assertEqual(sp.denom(sp.cancel(normalized[3])), a**3)
        global_field = a**3 * normalized
        self.assert_zero(global_field - sp.Matrix([0, a**2, 0, -1]))
        self.assert_zero(self.bracket(self.e, global_field))
        self.assert_zero(self.apply(global_field, a))
        self.assert_zero(self.apply(global_field, self.f))
        for variable in self.variables:
            self.assert_zero(self.apply(global_field, self.apply(global_field, variable)))
        self.assert_zero(self.apply(global_field, -s) - 1)

    def test_actual_commuting_fields_preserve_and_drop_generic_rank(self):
        a = self.a
        v = sp.Matrix([0, a, 0, 0])
        alternatives = [(v + self.e, 2, 1), (sp.Matrix([0, 0, 1, 0]), 3, 2)]
        for other, old_rank, projected_rank in alternatives:
            with self.subTest(old_rank=old_rank):
                fields = [v, other]
                global_fields = [a * self.project(field) for field in fields]
                self.assert_zero(self.bracket(v, other))
                self.assertEqual(sp.Matrix.hstack(self.e, *fields).rank(), old_rank)
                self.assertEqual(sp.Matrix.hstack(*global_fields).rank(), projected_rank)
                self.assertEqual(sp.Matrix.hstack(self.e, *global_fields).rank(), old_rank)
                self.assert_zero(self.bracket(*global_fields))
                for field in fields + global_fields:
                    self.assert_zero(self.bracket(self.e, field))
                    self.assert_zero(self.apply(field, a))
                    for variable in self.variables:
                        self.assert_zero(self.apply(field, self.apply(field, variable)))
                for field in global_fields:
                    self.assert_zero(self.apply(field, self.sigma))
                    self.assert_zero(self.apply(field, self.f))
        self.assert_zero(self.project(self.e))
        r1 = a * self.project(v)
        r2 = sp.Matrix([0, 0, a, 0])
        # Clearing preserves generic ranks, not ranks on every closed fiber.
        self.assertEqual(sp.Matrix.hstack(self.e, r1, r2).rank(), 3)
        self.assertEqual(sp.Matrix.hstack(self.e, r1, r2).subs(a, 0).rank(), 1)

    def test_local_projection_alone_does_not_give_one_power_descent(self):
        a = self.a
        field = sp.Matrix([0, 1, 0, 0])
        self.assert_zero(self.bracket(self.e, field))
        self.assert_zero(self.apply(field, a))
        self.assert_zero(self.apply(field, self.sigma) - 1 / a)
        projected = self.project(field)
        self.assert_zero(self.apply(projected, self.sigma))
        self.assert_zero(projected - sp.Matrix([0, 1, 0, -1 / a**2]))
        self.assertEqual(sp.denom(sp.cancel((a * projected)[3])), a)
        cleared = a**2 * projected
        self.assert_zero(cleared - sp.Matrix([0, a**2, 0, -1]))
        for variable in self.variables:
            self.assert_zero(self.apply(cleared, self.apply(cleared, variable)))
        # Vsigma has a pole here, so it cannot equal -2Wg for polynomial W.
        self.assertEqual(sp.denom(sp.cancel(self.apply(field, self.sigma))), a)


if __name__ == "__main__":
    unittest.main()
