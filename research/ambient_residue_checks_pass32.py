"""Exact controls for the written conditional ambient residue obstruction.

Only unittest and SymPy are imported. These finite identities do not
prove Miyanishi's theorem, normalization classification, or existence
of a hypersurface embedding of the fixed surface.
"""

import unittest

import sympy as sp


u, t, d, v, x, y, z, c = sp.symbols("u t d v x y z c")
disc = u**4 - 1
roots = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)


def zero(expr):
    return sp.cancel(expr) == 0


def deriv(expr, coefficients):
    return sp.expand(sum(a * sp.diff(expr, b)
                         for a, b in zip(coefficients, (x, y, z))))


class AmbientResidueChecks(unittest.TestCase):
    def test_actual_multiplier_preserves_normalization_and_line_speed(self):
        A = (u - 1) * (u - sp.I)
        relation = A * z - y * (y - 1)
        p = u + disc
        image = p * A * sp.diff(relation, y) + p * (2 * y - 1) * sp.diff(relation, z)
        self.assertTrue(zero(image))
        for r in roots:
            self.assertTrue(zero(p.subs(u, r) / r - 1))
        self.assertTrue(zero(p + p.subs(u, -u) - 2 * disc))
        self.assertNotEqual(sp.expand(p + p.subs(u, -u)), 0)

    def test_ambient_jacobian_and_invariant_replica_control(self):
        f = x
        g = x**2 * z - y**2
        J = sp.Matrix([sp.diff(f, a) for a in (x, y, z)]).cross(
            sp.Matrix([sp.diff(g, a) for a in (x, y, z)]))
        self.assertEqual(tuple(J), (0, -x**2, -2 * y))
        self.assertEqual(sp.gcd_list(list(J)), 1)
        multiplier = 1 + f**2 + g**2
        E = tuple(sp.expand(multiplier * a) for a in J)
        self.assertTrue(zero(deriv(multiplier, J)))
        self.assertTrue(zero(sum(sp.diff(a, b) for a, b in zip(E, (x, y, z)))))
        for coordinate in (x, y, z):
            j_iterate, e_iterate = coordinate, coordinate
            for n in range(1, 4):
                j_iterate = deriv(j_iterate, J)
                e_iterate = deriv(e_iterate, E)
                self.assertTrue(zero(e_iterate - multiplier**n * j_iterate))

    def test_residue_signs_and_only_possible_two_branch_partition(self):
        q0, q1, q2 = sp.symbols("q0 q1 q2")
        p = c * u + disc * (q0 + q1 * u + q2 * u**2)
        values = [sp.simplify(p.subs(u, r) / sp.diff(disc, u).subs(u, r))
                  for r in roots]
        self.assertEqual(values, [c / 4, c / 4, -c / 4, -c / 4])
        possible = []
        signs = (1, 1, -1, -1)
        for mask in range(1, 15):
            first = [i for i in range(4) if mask & (1 << i)]
            second = [i for i in range(4) if not mask & (1 << i)]
            # A common nonzero residue times positive integers has
            # the same sign ratio at every point over one branch.
            if len({signs[i] for i in first}) == 1 and len(
                    {signs[i] for i in second}) == 1:
                possible.append(mask)
        self.assertEqual(possible, [3, 12])

    def test_cover_power_difference_and_exact_quadratic_pullback(self):
        for ell in range(1, 9):
            difference = sp.expand((u**2 - 1)**ell - (u**2 + 1)**ell)
            self.assertEqual(sp.Poly(difference, u).degree(), 2 * ell - 2)
            self.assertEqual(sp.Poly(difference, u).LC(), -2 * ell)
            self.assertEqual(sp.Poly(difference, u).degree() == 0, ell == 1)
        scale, shift = sp.symbols("scale shift", nonzero=True)
        phi = scale * u**2 + shift
        a, b = shift + scale, shift - scale
        pullback = sp.diff(phi, u) / ((phi - a) * (phi - b))
        self.assertTrue(zero(pullback - 2 * u / (scale * disc)))

    def test_exact_nodal_ring_generators_and_dualizing_pullback(self):
        plane = v**2 - d**2 * (d + 1)
        curve_map = {d: t**2 - 1, v: (t**2 - 1) * t}
        self.assertTrue(zero(plane.subs(curve_map, simultaneous=True)))
        singular = sp.groebner(
            [plane, sp.diff(plane, d), sp.diff(plane, v)],
            d, v, domain=sp.QQ)
        self.assertEqual(list(singular), [d, v])
        self.assertEqual(sp.hessian(plane, (d, v)).subs({d: 0, v: 0}).det(), -4)
        for k in range(12):
            if k % 2 == 0:
                represented = d * (d + 1)**(k // 2)
            else:
                represented = v * (d + 1)**((k - 1) // 2)
            self.assertTrue(zero(represented.subs(curve_map, simultaneous=True)
                                 - (t**2 - 1) * t**k))
        differential = sp.diff(t**2 - 1, t) / (2 * (t**2 - 1) * t)
        self.assertTrue(zero(differential - 1 / (t**2 - 1)))
        self.assertTrue(zero(differential.subs(t, u**2) * 2 * u
                             - 2 * u / disc))

    def test_allowed_replica_parity_and_nonzero_speed_boundary(self):
        for q in (sp.Integer(0), t, t**3 - 2 * t + 1):
            h = 3 + (t**2 - 1) * q
            p = sp.expand(u * h.subs(t, u**2))
            self.assertTrue(zero(p + p.subs(u, -u)))
            for r in roots:
                self.assertTrue(zero(p.subs(u, r) / r - 3))
        # Zero-speed actions are deliberately outside the theorem.
        zero_speed = disc
        self.assertNotEqual(zero_speed + zero_speed.subs(u, -u), 0)
        self.assertTrue(all(zero_speed.subs(u, r) == 0 for r in roots))


if __name__ == "__main__":
    unittest.main(verbosity=2)
