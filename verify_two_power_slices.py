#!/usr/bin/env python3
"""Exact algebra for two-power slice proofs; no research-solver imports.

These finite checks do not implement Smith, Gysin, or rectification theory.
"""
import itertools
import unittest

import sympy as sp

a, b, u, z, x, y, c, T, V, W, lam, v = sp.symbols(
    "a b u z x y c T V W lambda v"
)


def exact_quotient(numerator, denominator, variable):
    quotient, remainder = sp.div(sp.expand(numerator), denominator, variable)
    if sp.expand(remainder) != 0:
        raise ValueError("Nonzero polynomial remainder")
    return sp.expand(quotient)


def root_residue_matrix(component_counts):
    matrix = sp.zeros(sum(component_counts), len(component_counts))
    row = 0
    for column, count in enumerate(component_counts):
        for _ in range(count):
            matrix[row, column] = 1
            row += 1
    return matrix


class TwoPowerChecks(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def check_shared_base(self, n, q, r, p):
        base_a = x+y**2
        base_b = y+base_a**3
        F = base_b+r.subs(a, base_a)*u**n+p.subs(a, base_a)*z**q
        inverse_b = T-r*u**n-p*z**q
        inverse_y = inverse_b-a**3
        inverse_x = a-inverse_y**2
        inverse_map = {x: inverse_x, y: inverse_y}
        forward_map = {T: F, a: base_a}
        self.zero(F.subs(inverse_map, simultaneous=True)-T)
        self.zero(base_a.subs(inverse_map, simultaneous=True)-a)
        self.zero(inverse_x.subs(forward_map, simultaneous=True)-x)
        self.zero(inverse_y.subs(forward_map, simultaneous=True)-y)

    def test_shared_nonlinear_base_inverse(self):
        self.check_shared_base(2, 3, a**2*(a-1), a**2+1)

    def test_constant_coefficient_branches(self):
        self.check_shared_base(3, 2, sp.Integer(2), a**2)
        self.check_shared_base(2, 4, a+1, sp.Integer(-3))

    def test_positive_quartic_normal_form(self):
        F = b+(a**2+1)*u**2+(a-1)**2*z**2
        self.assertEqual(sp.Poly(F, a, b, u, z).total_degree(), 4)
        inverse_b = T-(a**2+1)*u**2-(a-1)**2*z**2
        self.zero(F.subs(b, inverse_b)-T)
        self.zero(inverse_b.subs(T, F)-b)

    def test_one_linear_exponent_repeated_root_inverse(self):
        R = (1+a*b)*u**2+b+a*b**2
        F = a**2*z+R
        I0 = T-u**2
        I = T-u**2-a*(I0*u**2+I0**2)
        for expr in (R.subs(b, I)-T, I.subs(T, R)-b):
            self.zero(sp.div(sp.expand(expr), a**2, a)[1])
        mate = exact_quotient(b-I.subs(T, F), a**2, a)
        inverse_b = I+a**2*V
        inverse_z = exact_quotient(T-R.subs(b, inverse_b), a**2, a)
        inverse_map = {b: inverse_b, z: inverse_z}
        forward_map = {T: F, V: mate}
        self.zero(F.subs(inverse_map, simultaneous=True)-T)
        self.zero(mate.subs(inverse_map, simultaneous=True)-V)
        self.zero(inverse_b.subs(forward_map, simultaneous=True)-b)
        self.zero(inverse_z.subs(forward_map, simultaneous=True)-z)

    def test_one_linear_exponent_does_not_rectify_base_C(self):
        C = b+a*b**2
        self.zero(C.subs({b: v, a: (lam-v)/v**2}, simultaneous=True)-lam)
        self.zero(b*(1+a*b)-C)
        # At nonzero level lambda, b is a nonconstant unit.
        self.zero((b*(1+a*b)/lam).subs(
            {b: v, a: (lam-v)/v**2}, simultaneous=True)-1)

    def test_incompatible_quartic_is_critical_point_free(self):
        F = b+(a+b)**2*u**2+a**2*z**2
        self.assertEqual(sp.Poly(F, a, b, u, z).total_degree(), 4)
        db, du = sp.diff(F, b), sp.diff(F, u)
        self.zero(db*(2-db)+2*u**3*du-1)

    def test_incompatible_quartic_first_fixed_surface_coordinates(self):
        G = b+a**2*z**2
        inverse_b = T-a**2*z**2
        self.zero(G.subs(b, inverse_b)-T)
        self.zero(inverse_b.subs(T, G)-b)

    def test_incompatible_quartic_second_fixed_surface_coordinates(self):
        H = b+(a+b)**2*u**2
        companion = a+b
        inverse_b = T-c**2*u**2
        inverse_a = c-inverse_b
        backward = {a: inverse_a, b: inverse_b}
        forward = {T: H, c: companion}
        self.zero(H.subs(backward, simultaneous=True)-T)
        self.zero(companion.subs(backward, simultaneous=True)-c)
        self.zero(inverse_a.subs(forward, simultaneous=True)-a)
        self.zero(inverse_b.subs(forward, simultaneous=True)-b)

    def test_root_curve_parameterization_and_unit(self):
        R = b+b**2*u**2
        parameterization = {b: lam-v**2, u: v/(lam-v**2)}
        self.zero(R.subs(parameterization, simultaneous=True)-lam)
        self.zero((b*u).subs(parameterization, simultaneous=True)-v)
        self.zero((lam-(b*u)**2)-b+(R-lam))
        self.zero(b*(1+b*u**2)-R)
        self.zero((lam-v**2).subs(lam, 1)+(v-1)*(v+1))

    def test_two_cyclic_symmetries_and_quotient(self):
        F = b+(a+b)**2*u**2+a**2*z**2
        J = b+(a+b)**2*u**2+a**2*W
        self.zero(F.subs(u, -u)-F)
        self.zero(F.subs(z, -z)-F)
        self.zero(J.subs(W, z**2)-F)
        self.zero(J.subs(a, 0)-(b+b**2*u**2))

    def test_quotient_critical_point_lifting_chain_rule(self):
        p = (a-1)**2*(a+2)
        R = b+a*b*u+u**3
        J = p*W+R
        for exponent in (1, 2, 3, 5):
            F = J.subs(W, z**exponent)
            for variable in (a, b, u):
                self.zero(sp.diff(F, variable)
                          -sp.diff(J, variable).subs(W, z**exponent))
            self.zero(sp.diff(F, z)-exponent*p*z**(exponent-1))
            for root in (1, -2):
                self.zero(sp.diff(F, z).subs(a, root))

    def test_root_residue_isomorphism_requires_one_component_per_root(self):
        for roots in range(1, 5):
            for counts in itertools.product(range(3), repeat=roots):
                matrix = root_residue_matrix(counts)
                invertible = (matrix.rows == matrix.cols
                              and matrix.rank() == matrix.rows)
                self.assertEqual(invertible, all(count == 1 for count in counts))

    def test_constant_plane_coefficient_inverse(self):
        for coefficient in (sp.Integer(0), sp.Integer(2), sp.Rational(-1, 3)):
            for exponent in (1, 2, 5):
                H = b+coefficient*u**exponent
                inverse_b = T-coefficient*u**exponent
                self.zero(H.subs(b, inverse_b)-T)
                self.zero(inverse_b.subs(T, H)-b)

    def test_nonconstant_composition_degree_cannot_drop(self):
        for r in (a+1, a**2-3*a+2, a**3+1):
            for h in (b, b**2+1, 2*b**3-b):
                for root in (0, 1, sp.Rational(2, 3)):
                    composition = sp.expand(r.subs(a, root+h))
                    self.assertEqual(sp.degree(composition, b),
                                     sp.degree(r, a)*sp.degree(h, b))

    def test_surface_infinity_euler_formula(self):
        d = sp.Symbol("d", integer=True, positive=True)
        surface = d*sum(sp.binomial(4, j)*(-d)**(2-j) for j in range(3))
        curve = d*sum(sp.binomial(3, j)*(-d)**(1-j) for j in range(2))
        self.zero(surface-curve-(1+(d-1)**3))
        for degree in range(3, 12):
            minimum = 1+(degree-1)**3-(degree-1)**2
            self.assertGreater(minimum, 1)
        self.assertEqual(1+3**3-3**2, 19)

    def test_quadratic_generic_euler_rank_controls(self):
        self.assertEqual([1+(-1)**(rank-1) for rank in (1, 2, 3)], [2, 0, 2])
        # A radical linear term instead gives an explicit coordinate.
        G = a+b**2+z**2
        inverse_a = T-b**2-z**2
        self.zero(G.subs(a, inverse_a)-T)
        self.zero(inverse_a.subs(T, G)-a)

    def test_infinity_direction_and_nonreduced_guard(self):
        cubic_leading = b**3+z**3
        direction = {a: 1, b: 0, z: 0}
        for variable in (a, b, z):
            self.zero(sp.diff(cubic_leading, variable).subs(direction))
        self.assertEqual(sp.degree(a+cubic_leading, a), 1)
        quartic_leading = b**4
        for variable in (a, b, z):
            self.zero(sp.diff(quartic_leading, variable).subs(direction))
        # The reduced support is smooth; its gradient is not the same locus.
        self.assertEqual(sp.diff(b, b), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
