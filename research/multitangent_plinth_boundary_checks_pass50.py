"""Exact triple-conic controls, not tests of an actual polynomial-cylinder example."""

import unittest

import sympy as sp


class MultitangentPlinthBoundaryChecks(unittest.TestCase):
    def setUp(self):
        self.a, self.b, self.z, self.w = sp.symbols("a b z w")
        a, b, z, w = self.a, self.b, self.z, self.w
        self.r = a * z + b * w
        self.p = b**3 - a**3
        self.relation = self.r**2 - 2 * b**2 * z - 2 * a**2 * w + a * b - a**3

    def test_actual_derivation_and_polynomial_flow_on_the_weaker_ring(self):
        a, b, z, w, r, p = self.a, self.b, self.z, self.w, self.r, self.p
        tau = sp.symbols("tau")
        dz, dw = b * r - a**2, -a * r + b**2

        def deriv(value):
            return sp.expand(sp.diff(value, z) * dz + sp.diff(value, w) * dw)

        self.assertEqual(deriv(r), p)
        self.assertEqual(deriv(self.relation), 0)
        self.assertEqual(deriv(dz), sp.expand(b * p))
        self.assertEqual(deriv(dw), sp.expand(-a * p))
        self.assertEqual(deriv(deriv(dz)), 0)
        self.assertEqual(deriv(deriv(dw)), 0)
        self.assertEqual(sp.det(sp.Matrix([[a, b], [-b**2, -a**2]])), p)

        flow = {z: z + tau * dz + tau**2 * b * p / 2,
                w: w + tau * dw - tau**2 * a * p / 2}
        self.assertEqual(sp.expand(r.subs(flow, simultaneous=True) - r - tau * p), 0)
        self.assertEqual(sp.expand(self.relation.subs(flow, simultaneous=True) - self.relation), 0)
        inverse = {key: value.subs(tau, -tau) for key, value in flow.items()}
        for key in (z, w):
            self.assertEqual(sp.expand(flow[key].subs(inverse, simultaneous=True) - key), 0)
            self.assertEqual(sp.expand(inverse[key].subs(flow, simultaneous=True) - key), 0)

    def test_all_three_branches_normalization_and_trace(self):
        a, b, z, w = self.a, self.b, self.z, self.w
        xi, t, s, rr = sp.symbols("xi t s rr")

        def root_remainder(value):
            return sp.rem(sp.expand(value), xi**3 - 1, xi)

        full = self.relation.subs({a: t, b: xi * t}, simultaneous=True)
        surface = (z + xi * w - xi**2)**2 - t
        self.assertEqual(root_remainder(full - t**2 * surface), 0)
        minimal = (rr - xi**2 * t)**2 - t**3
        self.assertEqual(root_remainder(minimal.subs({t: s**2, rr: xi**2 * s**2 + s**3}, simultaneous=True)), 0)
        # Polynomial surface inverse, using xi^-1=xi^2 for all cube roots of one.
        w_of_s = xi**2 * s + xi - xi**2 * z
        self.assertEqual(root_remainder((z + xi * w - xi**2).subs(w, w_of_s) - s), 0)
        self.assertEqual(root_remainder(w_of_s.subs(s, z + xi * w - xi**2) - w), 0)
        self.assertEqual(root_remainder(surface.subs({w: w_of_s, t: s**2}, simultaneous=True)), 0)

        multiplication = sp.Matrix([[xi**2 * t, t**2], [t, xi**2 * t]])
        self.assertEqual(multiplication.trace(), 2 * xi**2 * t)
        self.assertEqual(root_remainder(multiplication.det() - (xi * t**2 - t**3)), 0)
        self.assertEqual(multiplication.subs(t, 0), sp.zeros(2))
        # The nontrivial odd term gives the field inverse s=(r-xi^2*t)/t.
        self.assertEqual(sp.expand((xi**2 * s**2 + s**3) - xi**2 * s**2 - s * s**2), 0)

        dz_on_surface = (b * self.r - a**2).subs(
            {a: s**2, b: xi * s**2, w: w_of_s}, simultaneous=True
        )
        self.assertEqual(root_remainder(dz_on_surface - xi * s**5), 0)

    def test_missing_flatness_prime_pullback_and_smoothness(self):
        a, b, z, w = self.a, self.b, self.z, self.w
        self.assertEqual(self.relation.subs({a: 0, b: 0}), 0)
        for variable in (a, b, z, w):
            self.assertEqual(sp.diff(self.relation, variable).subs({a: 0, b: 0}), 0)
        factor = z**2 - 2 * w - a
        reduced = self.relation.subs(b, 0)
        self.assertEqual(sp.expand(reduced - a**2 * factor), 0)
        witness = a * factor
        self.assertEqual(sp.expand(a * witness - reduced), 0)
        _, remainder = sp.div(witness, reduced, a, z, w)
        self.assertNotEqual(remainder, 0)

        # A literal branch pullback has a double vertical factor, not a prime ideal.
        t = sp.symbols("t")
        branch = self.relation.subs({a: t, b: t}, simultaneous=True)
        other = (z + w - 1)**2 - t
        self.assertEqual(sp.expand(branch - t**2 * other), 0)
        self.assertNotEqual(sp.rem(t * other, branch, t), 0)
        self.assertEqual(sp.rem(t * (t * other), branch, t), 0)


if __name__ == "__main__":
    unittest.main()
