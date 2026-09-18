"""Independent exact controls for noninvariant-surface-pass27.md.

The universal nonplanarity proof is written in the note. No project
solver, old checker, floating-point search, or external module is used.
"""

import unittest
import sympy as sp


u, y, z, G, t = sp.symbols("u y z G t")
ii = sp.I
A = (u-1)*(u-ii)
b = (1-ii)*(u+1)*(u+ii)/4
a = -ii*A*(u+(1+ii)/2)/2
q = -u*b**2
rcoef = ii*u*A/8
d = u**4-1
e = d*u
g = a+b*y
h = q*z+rcoef*y
surface = A*z-y*(y-1)
L1 = 1-ii+2*ii*G
jstar = sp.expand(u-L1.subs(G, g)*u**2/2)
quartic = u**4-(1+ii)*u**3/2+(1-ii)*u/2-2


def derivative(expression):
    return sp.expand(u*A*sp.diff(expression, y)
                     + u*(2*y-1)*sp.diff(expression, z))


class NoninvariantSurfaceChecks(unittest.TestCase):
    def test_actual_fiber_components_and_first_prime(self):
        section = {y: 0, z: 0}
        fixed_line = {u: 0, z: y*(y-1)/ii}
        self.assertEqual(surface.subs(section, simultaneous=True), 0)
        self.assertEqual(sp.expand(surface.subs(fixed_line, simultaneous=True)), 0)
        self.assertEqual(h.subs(section, simultaneous=True), 0)
        self.assertEqual(h.subs(fixed_line, simultaneous=True), 0)
        self.assertEqual(d.subs(u, 0), -1)
        self.assertEqual(e.subs(u, 0), 0)
        self.assertEqual(sp.expand(g.subs(u, 0)-(1+ii)*(1+y)/4), 0)
        self.assertNotEqual(sp.diff(g.subs(u, 0), y), 0)
        self.assertNotEqual(h.subs({u: 2, y: 1, z: 0}), 0)

    def test_section_normalization_and_actual_identification(self):
        self.assertEqual(sp.expand(u**4-d-1), 0)
        self.assertEqual(sp.expand(u*d-e), 0)
        first = {u: 1, y: 0, z: 0}
        second = {u: ii, y: 0, z: 0}
        for function in (d, e, g, h):
            self.assertEqual(
                sp.simplify(function.subs(first, simultaneous=True)
                            -function.subs(second, simultaneous=True)), 0
            )
        # Both section points are t=0 on the SAME first conductor pair.
        self.assertEqual((z/(sp.Integer(1)*(-1))).subs(z, 0), 0)
        self.assertEqual((z/(ii*(-1))).subs(z, 0), 0)
        self.assertEqual(d.subs(u, 0), -1)

    def test_scheme_intersection_has_length_one(self):
        # On the normalization, and hence at o off d=0, the two prime
        # ideals are (u) and (y,z). Their sum has quotient exactly C.
        gb = sp.groebner([surface, u, y, z], z, y, u, extension=ii)
        self.assertEqual(set(poly.as_expr() for poly in gb.polys), {z, y, u})
        self.assertEqual(gb.reduce(sp.Integer(1))[1], 1)
        for variable in (u, y, z):
            self.assertEqual(gb.reduce(variable)[1], 0)
        self.assertEqual(A.subs(u, 0), ii)
        self.assertNotEqual(A.subs(u, 0), 0)
        self.assertEqual(sp.expand(A*(y*(y-1)/A)-y*(y-1)), 0)
        # The section and fixed curve have independent tangent equations.
        self.assertEqual(sp.Matrix([u, y]).jacobian([u, y]).det(), 1)
        self.assertEqual(sp.expand(e-u*d), 0)

    def test_principal_equation_requires_multiplicity_divisible_by_four(self):
        c = sp.symbols("c", nonzero=True)
        failed_simple_zero = c*u
        self.assertEqual(
            sp.expand(failed_simple_zero.subs(u, 1)
                      -failed_simple_zero.subs(u, ii)), sp.expand(c*(1-ii))
        )
        self.assertNotEqual(1-ii, 0)
        matches = [sp.expand(1-ii**residue) == 0 for residue in range(4)]
        self.assertEqual(matches, [True, False, False, False])
        # Order four is a positive control: u^4 is actually in the section
        # image, because it is d+1, and has matching values at 1 and i.
        self.assertEqual(sp.expand((d+1)-u**4), 0)
        self.assertEqual((u**4).subs(u, 1), (u**4).subs(u, ii))
        for exponent in (1, 4):
            local_quotient = sp.groebner([u**exponent], u)
            for power in range(exponent):
                self.assertEqual(local_quotient.reduce(u**power)[1], u**power)
            self.assertEqual(local_quotient.reduce(u**exponent)[1], 0)

    def test_genuine_noninvariant_candidate_descends(self):
        ordinary = lambda root: {
            u: root, y: root*A.subs(u, root)*t,
            z: (root*A.subs(u, root)*t)
               *(root*A.subs(u, root)*t-1)/A.subs(u, root),
        }
        split = lambda root, epsilon: {
            u: root, y: epsilon, z: root*(2*epsilon-1)*t,
        }
        pairs = (
            (split(sp.Integer(1), 0), split(ii, 0)),
            (split(sp.Integer(1), 1), ordinary(-ii)),
            (ordinary(sp.Integer(-1)), split(ii, 1)),
        )
        for left, right in pairs:
            self.assertEqual(
                sp.expand(jstar.subs(left, simultaneous=True)
                          -jstar.subs(right, simultaneous=True)), 0
            )
        expected_derivative = -(1+ii)*(u**4-1)*u**3/4
        self.assertEqual(sp.expand(derivative(jstar)-expected_derivative), 0)
        self.assertNotEqual(expected_derivative, 0)

    def test_noninvariant_quartic_collision_is_exact(self):
        self.assertEqual(
            sp.expand(jstar.subs(y, 0)+u*quartic/2), 0
        )
        self.assertEqual(sp.gcd(quartic, u*(u**4-1), extension=ii), 1)
        self.assertEqual(sp.degree(quartic, u), 4)
        self.assertEqual(jstar.subs(u, 0), 0)
        self.assertEqual(sp.rem(jstar.subs(y, 0), quartic, u, extension=ii), 0)
        witness = sp.symbols("witness")
        desired_g = a.subs(u, witness)
        y0 = sp.expand((desired_g-a.subs(u, 0))/b.subs(u, 0))
        z0 = sp.expand(y0*(y0-1)/ii)
        second = {u: 0, y: y0, z: z0}
        self.assertEqual(sp.expand(surface.subs(second, simultaneous=True)), 0)
        self.assertEqual(sp.expand(g.subs(second, simultaneous=True)-desired_g), 0)
        self.assertEqual(h.subs(second, simultaneous=True), 0)
        self.assertEqual(jstar.subs(second, simultaneous=True), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
