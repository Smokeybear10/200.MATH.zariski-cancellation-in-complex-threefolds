"""Finite identities for the scoped noncoordinate speed-row control96."""

import unittest

import sympy as sp


class QuadraticGlobalBridgeControl(unittest.TestCase):
    def test_exact_relative_structure_and_failed_ambient_inverse(self):
        u, a, y, v, t, tau, zz = sp.symbols("u a y v t tau zz")
        base_b = sp.Matrix([a, a * t - 1, t**2])
        frame = sp.Matrix([[a, 1, 0], [a * t - 1, t, 0], [t**2, 0, 1]])
        self.assertEqual(sp.expand(frame.det()), 1)
        self.assertEqual(sp.expand((sp.Matrix([[t, -1, 0]]) * base_b)[0]), 1)
        omega = sp.Matrix.hstack(base_b, base_b.diff(a), base_b.diff(t)).det()
        self.assertEqual(sp.expand(omega - t * (a * t + 2)), 0)

        t_actual = 2 * a * v - y**2
        coords = sp.Matrix([u, a, y, v])

        def n(poly):
            return sp.expand(a * sp.diff(poly, y) + y * sp.diff(poly, v))

        self.assertEqual(n(t_actual), 0)
        self.assertEqual(n(n(y)), 0)
        self.assertEqual(n(n(n(v))), 0)

        good = (frame * sp.Matrix([u, y, v])).subs(t, t_actual)
        bad = a + u**2
        self.assertEqual(
            sp.simplify(good.diff(u) - base_b.subs(t, t_actual)),
            sp.zeros(3, 1),
        )
        self.assertEqual(good.diff(u, 2), sp.zeros(3, 1))
        self.assertEqual(sp.diff(bad, u, 2), 2)
        sigma = sp.expand(t_actual * good[0] - good[1])
        self.assertEqual(sigma, u)
        self.assertEqual(sp.expand(good[0] - a * sigma), y)
        self.assertEqual(sp.expand(good[2] - t_actual**2 * sigma), v)
        self.assertEqual(sp.expand(bad - sigma**2), a)
        self.assertEqual(sp.expand(a + tau * (u - sigma)), a)

        # Both directions for the true coordinate Z, not the failed tuple.
        true_forward = sp.Matrix([u, bad, y, v])
        true_inverse = sp.Matrix([u, zz - u**2, y, v])
        self.assertEqual(
            true_inverse.subs(zz, bad).applyfunc(sp.expand),
            coords,
        )
        self.assertEqual(
            true_forward.subs(a, zz - u**2).applyfunc(sp.expand),
            sp.Matrix([u, zz, y, v]),
        )

        candidate = sp.Matrix([*good, bad])
        delta = sp.expand(candidate.jacobian(coords).det())
        expected = (
            1 + 2 * a * y * (t_actual**2 - y)
            + (2 * a**2 * t_actual**2 - 2 * a**2 * y
               + 4 * a * t_actual + 4 * y * v) * u
            + 4 * (a * v + y**2) * u**2
            + 4 * a * y * u**3
        )
        self.assertEqual(sp.expand(delta - expected), 0)
        self.assertEqual(delta.subs({a: 0, y: 1, v: 0}), 1 + 4 * u**2)
        point = {u: sp.I / 2, a: 0, y: 1, v: 0}
        self.assertEqual(delta.subs(point), 0)
        self.assertEqual(t_actual.subs(point), -1)
        self.assertEqual(omega.subs(t, t_actual).subs(point), -2)
        tangent = sp.Matrix([1, -sp.I, -sp.Rational(1, 2), -1 + sp.I])
        self.assertEqual(
            sp.simplify(candidate.jacobian(coords).subs(point) * tangent),
            sp.zeros(4, 1),
        )
        self.assertEqual(tangent[0], 1)
        self.assertEqual(tangent[1], -sp.I)
        self.assertEqual(
            (sp.Matrix([t_actual]).jacobian(coords).subs(point) * tangent)[0], 1
        )

        # Actual Jacobian quotient field, up to a constant scalar.
        for f in coords:
            jac = sp.Matrix([a, t_actual, u, f]).jacobian(coords).det()
            self.assertEqual(sp.expand(jac + 2 * n(f)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
