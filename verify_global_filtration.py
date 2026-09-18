#!/usr/bin/env python3
"""Exact controls for the global slice-filtration argument.

Independent of the fixed-Delta solver and its theorem. These tests verify
explicit polynomial examples, not the universal cancellation conjecture.
Run with /opt/anaconda3/bin/python verify_global_filtration.py.
"""

import unittest
from itertools import combinations

import sympy as sp


a, b, c, s = sp.symbols("a b c s")
variables = (a, b, c, s)
x = sp.symbols("x1:5")
forward = (a, b + a*s, c + b*s, s)
inverse = (x[0], x[1] - x[0]*x[3],
           x[2] - x[1]*x[3] + x[0]*x[3]**2, x[3])
fields = ((1, -s, s**2, 0), (0, 1, -s, 0),
          (0, 0, 1, 0), (0, -a, a*s-b, 1))


def apply(field, polynomial):
    return sp.expand(sum(v*sp.diff(polynomial, z)
                         for v, z in zip(field, variables)))


def bracket(left, right):
    return tuple(sp.expand(apply(left, v)-apply(right, u))
                 for u, v in zip(left, right))


def filtration_top(field):
    """Weights (0,0,0,1), including the -1 weight of d/ds."""
    degrees = [sp.degree(v, s)-(i == 3)
               for i, v in enumerate(field) if v != 0]
    if not degrees:
        raise ValueError("The zero derivation has no top symbol")
    degree = max(degrees)
    top = tuple(sp.expand(v).coeff(s, degree+(i == 3))
                * s**(degree+(i == 3))
                if degree+(i == 3) >= 0 else sp.Integer(0)
                for i, v in enumerate(field))
    return degree, top


class GlobalFiltrationTests(unittest.TestCase):
    def test_polynomial_inverse_both_directions(self):
        for expression, expected in zip(inverse, variables):
            self.assertEqual(sp.expand(expression.subs(dict(zip(x, forward)),
                                                      simultaneous=True)
                                       - expected), 0)
        for expression, expected in zip(forward, x):
            self.assertEqual(sp.expand(expression.subs(dict(zip(variables, inverse)),
                                                      simultaneous=True)
                                       - expected), 0)

    def test_jacobian_and_coordinate_partial_pairing(self):
        self.assertEqual(sp.Matrix(forward).jacobian(variables).det(), 1)
        self.assertEqual(sp.Matrix([[apply(t, f) for f in forward]
                                    for t in fields]), sp.eye(4))

    def test_all_coordinate_partials_commute(self):
        for left, right in combinations(fields, 2):
            self.assertEqual(bracket(left, right), (0, 0, 0, 0))

    def test_generators_are_locally_nilpotent_controls(self):
        for field in fields:
            for generator in variables:
                value = generator
                for _ in range(5):
                    value = apply(field, value)
                self.assertEqual(value, 0)

    def test_top_degrees_and_symbols(self):
        results = [filtration_top(t) for t in fields]
        self.assertEqual([d for d, _ in results], [2, 1, 0, 1])
        self.assertEqual([v for _, v in results],
                         [(0, 0, s**2, 0), (0, 0, -s, 0),
                          (0, 0, 1, 0), (0, 0, a*s, 0)])

    def test_top_rank_loss_and_commutativity(self):
        intrinsic = [(0, 0, 1, 0), (0, 0, -1, 0),
                     (0, 0, 1, 0), (0, 0, a, 0)]
        self.assertEqual(sp.Matrix(fields).rank(), 4)
        self.assertEqual(sp.Matrix([t[:3] for t in intrinsic]).rank(), 1)
        for left, right in combinations(intrinsic, 2):
            self.assertEqual(bracket(left, right), (0, 0, 0, 0))

    def test_recovery_uses_special_common_invariant(self):
        # s is killed by T1,T2,T3 in this example. This is extra structure,
        # not a claim about arbitrary slice polynomials and coordinates.
        first = tuple(sp.expand(u+s*v) for u, v in zip(fields[0], fields[1]))
        second = tuple(sp.expand(u+s*v) for u, v in zip(fields[1], fields[2]))
        self.assertEqual(first, (1, 0, 0, 0))
        self.assertEqual(second, (0, 1, 0, 0))
        self.assertEqual(sp.Matrix([first[:3], second[:3], fields[2][:3]]).det(), 1)

    def test_vertical_negative_degree_control(self):
        self.assertEqual(filtration_top((0, 0, 0, 1)), (-1, (0, 0, 0, 1)))

    def test_zero_degree_need_not_give_intrinsic_slice(self):
        # Proper coordinate action T=d/ds+a*d/db descends to a*d/db,
        # which vanishes on a=0 and therefore cannot have a slice.
        field = (0, a, 0, 1)
        self.assertEqual(filtration_top(field), (0, (0, a, 0, 0)))
        self.assertEqual(apply(field, b-a*s), 0)
        self.assertEqual(apply(field, s), 1)
        for monomial in (1, a, b, c, a*b, b**3, b*c):
            self.assertEqual(apply((0, a, 0, 0), monomial).subs(a, 0), 0)

    def test_wrong_top_rank_is_rejected(self):
        # Negative control for the tempting rank-preservation assertion.
        original_rank = sp.Matrix(fields).rank()
        top_rank = sp.Matrix([filtration_top(t)[1] for t in fields]).rank()
        self.assertNotEqual(original_rank, top_rank)
        with self.assertRaises(ValueError):
            filtration_top((0, 0, 0, 0))

    def test_nonlinear_control_inverse_and_coordinate_partial(self):
        nonlinear = (a+s**2, b, c, s+(a+s**2)**2)
        nonlinear_inverse = (x[0]-(x[3]-x[0]**2)**2,
                             x[1], x[2], x[3]-x[0]**2)
        for expression, expected in zip(nonlinear_inverse, variables):
            self.assertEqual(sp.expand(expression.subs(dict(zip(x, nonlinear)),
                                                      simultaneous=True)-expected), 0)
        for expression, expected in zip(nonlinear, x):
            self.assertEqual(sp.expand(expression.subs(dict(zip(variables, nonlinear_inverse)),
                                                      simultaneous=True)-expected), 0)
        coordinate_partial = (1+4*a*s+4*s**3, 0, 0, -2*a-2*s**2)
        self.assertEqual(tuple(apply(coordinate_partial, value) for value in nonlinear),
                         (1, 0, 0, 0))
        self.assertEqual(filtration_top(coordinate_partial),
                         (3, (4*s**3, 0, 0, 0)))
        for generator in variables:
            value = generator
            for _ in range(5):
                value = apply(coordinate_partial, value)
            self.assertEqual(value, 0)

    def test_lower_coefficient_and_commutator_are_not_lnd(self):
        coordinate_partial = (1+4*a*s+4*s**3, 0, 0, -2*a-2*s**2)
        coefficient = tuple(sp.expand(value).coeff(s, 1)
                            for value in coordinate_partial[:3])+(0,)
        self.assertEqual(coefficient, (4*a, 0, 0, 0))
        commutator = bracket((0, 0, 0, 1), coordinate_partial)
        self.assertEqual(commutator, (4*a+12*s**2, 0, 0, -4*s))
        value_a, value_s = a, s
        for n in range(1, 9):
            value_a = apply(coefficient, value_a)
            value_s = apply(commutator, value_s)
            self.assertEqual(value_a, 4**n*a)
            self.assertEqual(value_s, (-4)**n*s)
        # These exact recurrences prove non-nilpotence for every n, not merely
        # failure of this finite iteration cutoff.

    @staticmethod
    def _nonlinear_rank_one_data():
        nonlinear = (a+s**2, b+a*s, c+b*s, s+(a+s**2)**2)
        si = x[3]-x[0]**2
        ai = x[0]-si**2
        bi = x[1]-ai*si
        nonlinear_inverse = (ai, bi, x[2]-bi*si, si)
        first = (1+4*a*s+4*s**3,
                 2*a**2-s-2*a*s**2-4*s**4,
                 2*a*b-2*a**2*s+(1+2*b)*s**2+2*a*s**3+4*s**5,
                 -2*a-2*s**2)
        last = (-2*s, 2*s**2-a, -2*s**3+a*s-b, 1)
        return nonlinear, nonlinear_inverse, (first, fields[1], fields[2], last)

    def test_rank_one_nonlinear_control_inverse_and_pairing(self):
        nonlinear, nonlinear_inverse, nonlinear_fields = self._nonlinear_rank_one_data()
        for expression, expected in zip(nonlinear_inverse, variables):
            self.assertEqual(sp.expand(expression.subs(dict(zip(x, nonlinear)),
                                                      simultaneous=True)-expected), 0)
        for expression, expected in zip(nonlinear, x):
            self.assertEqual(sp.expand(expression.subs(dict(zip(variables, nonlinear_inverse)),
                                                      simultaneous=True)-expected), 0)
        self.assertEqual(sp.Matrix([[apply(t, value) for value in nonlinear]
                                    for t in nonlinear_fields]), sp.eye(4))
        for left, right in combinations(nonlinear_fields, 2):
            self.assertEqual(bracket(left, right), (0, 0, 0, 0))

    def test_rank_one_nonlinear_top_rank_and_bad_lower_coefficient(self):
        _, _, nonlinear_fields = self._nonlinear_rank_one_data()
        tops = [filtration_top(t) for t in nonlinear_fields]
        self.assertEqual([degree for degree, _ in tops], [5, 1, 0, 3])
        self.assertEqual([top for _, top in tops],
                         [(0, 0, 4*s**5, 0), (0, 0, -s, 0),
                          (0, 0, 1, 0), (0, 0, -2*s**3, 0)])
        self.assertEqual(sp.Matrix([top[:3] for _, top in tops]).rank(), 1)
        bad_coefficient = tuple(sp.expand(value).coeff(s, 1)
                                for value in nonlinear_fields[0][:3])+(0,)
        self.assertEqual(bad_coefficient, (4*a, -1, -2*a**2, 0))
        self.assertEqual(apply(bad_coefficient, a), 4*a)
        bad_bracket = bracket((0, 0, 0, 1), nonlinear_fields[0])
        self.assertEqual(apply(bad_bracket, s), -4*s)

    def test_rank_one_control_still_allows_a_specific_repair(self):
        # The negative example refutes preservation rules, not every possible
        # selection of lower coefficients or every polynomial coordinate change.
        _, _, nonlinear_fields = self._nonlinear_rank_one_data()
        useful = tuple(sp.expand(value).coeff(s, 3)
                       for value in nonlinear_fields[0][:3])+(0,)
        self.assertEqual(useful, (4, 0, 2*a, 0))
        recovered = (useful, (0, 1, 0, 0), (0, 0, 1, 0))
        self.assertEqual(sp.Matrix([t[:3] for t in recovered]).det(), 4)
        for left, right in combinations(recovered, 2):
            self.assertEqual(bracket(left, right), (0, 0, 0, 0))
        for generator in variables:
            value = generator
            for _ in range(3):
                value = apply(useful, value)
            self.assertEqual(value, 0)

    def test_bad_interior_coefficient_even_when_partial_fixes_slice(self):
        matrix = sp.Matrix([[s, -s**2], [1, -s]])
        self.assertEqual(matrix**2, sp.zeros(2))
        nonlinear = (a-c*(s*a-s**2*b), b-c*(a-s*b), c, s)
        nonlinear_inverse = ((1+x[2]*x[3])*x[0]-x[2]*x[3]**2*x[1],
                             x[2]*x[0]+(1-x[2]*x[3])*x[1], x[2], x[3])
        for expression, expected in zip(nonlinear_inverse, variables):
            self.assertEqual(sp.expand(expression.subs(dict(zip(x, nonlinear)),
                                                      simultaneous=True)-expected), 0)
        for expression, expected in zip(nonlinear, x):
            self.assertEqual(sp.expand(expression.subs(dict(zip(variables, nonlinear_inverse)),
                                                      simultaneous=True)-expected), 0)
        nonlinear_fields = (
            (1+c*s, c, 0, 0),
            (-c*s**2, 1-c*s, 0, 0),
            (s*a-s**2*b, a-s*b, 1, 0),
            (c*a-2*c*s*b+c**2*s*a-c**2*s**2*b,
             -c*b+c**2*a-c**2*s*b, 0, 1))
        self.assertEqual(sp.Matrix([[apply(t, value) for value in nonlinear]
                                    for t in nonlinear_fields]), sp.eye(4))
        tops = [filtration_top(t) for t in nonlinear_fields]
        self.assertEqual([degree for degree, _ in tops], [1, 2, 2, 2])
        self.assertEqual([top for _, top in tops],
                         [(c*s, 0, 0, 0), (-c*s**2, 0, 0, 0),
                          (-b*s**2, 0, 0, 0), (-c**2*b*s**2, 0, 0, 0)])
        self.assertEqual(sp.Matrix([top[:3] for _, top in tops]).rank(), 1)
        chosen = nonlinear_fields[2]
        self.assertEqual(apply(chosen, s), 0)
        interior = tuple(sp.expand(v).coeff(s, 1) for v in chosen[:3])+(0,)
        self.assertEqual(interior, (a, -b, 0, 0))
        self.assertEqual(apply(interior, a), a)
        commutator = bracket((0, 0, 0, 1), chosen)
        self.assertEqual(commutator, (a-2*s*b, -b, 0, 0))
        self.assertEqual(apply(commutator, b), -b)
        self.assertEqual(apply(commutator, s), 0)
        self.assertEqual(bracket((0, a, 1, 0), (-b, 0, 0, 0)),
                         (-a, b, 0, 0))

    def test_slice_projection_of_coordinate_partial_need_not_be_lnd(self):
        nonlinear = (s+a**2, b, c, a+(s+a**2)**2)
        nonlinear_inverse = (x[3]-x[0]**2, x[1], x[2],
                             x[0]-(x[3]-x[0]**2)**2)
        for expression, expected in zip(nonlinear_inverse, variables):
            self.assertEqual(sp.expand(expression.subs(dict(zip(x, nonlinear)),
                                                      simultaneous=True)-expected), 0)
        for expression, expected in zip(nonlinear, x):
            self.assertEqual(sp.expand(expression.subs(dict(zip(variables, nonlinear_inverse)),
                                                      simultaneous=True)-expected), 0)
        coordinate_partial = (-2*(s+a**2), 0, 0, 1+4*a*(s+a**2))
        self.assertEqual(tuple(apply(coordinate_partial, v) for v in nonlinear),
                         (1, 0, 0, 0))
        horizontal = coordinate_partial[:3]+(0,)
        projected = tuple(sp.sympify(v).subs(s, 0) for v in horizontal)
        self.assertEqual(projected, (-2*a**2, 0, 0, 0))
        value = a
        for n in range(1, 9):
            value = apply(projected, value)
            self.assertEqual(value, (-2)**n*sp.factorial(n)*a**(n+1))
        # The displayed formula follows inductively for every n, so this
        # projection is not locally nilpotent despite its ambient origin.

    def test_invertible_linear_mix_can_have_one_nonunit_top(self):
        old_forward = (a, b+a**2*s, c+b*s, s)
        old_fields = ((1, -2*a*s, 2*a*s**2, 0), (0, 1, -s, 0),
                      (0, 0, 1, 0), (0, -a**2, a**2*s-b, 1))
        mixing = sp.Matrix([[1, 0, 0, 0], [1, 1, 0, 0],
                            [1, 0, 1, 0], [1, 0, 0, 1]])
        self.assertEqual(mixing.det(), 1)
        mixed = tuple(tuple(value for value in row)
                      for row in (mixing*sp.Matrix(old_fields)).tolist())
        new_forward = tuple(mixing.inv().T*sp.Matrix(old_forward))
        ai = sum(x)
        si = x[3]
        bi = x[1]-ai**2*si
        new_inverse = (ai, bi, x[2]-bi*si, si)
        for expression, expected in zip(new_inverse, variables):
            self.assertEqual(sp.expand(expression.subs(dict(zip(x, new_forward)),
                                                      simultaneous=True)-expected), 0)
        for expression, expected in zip(new_forward, x):
            self.assertEqual(sp.expand(expression.subs(dict(zip(variables, new_inverse)),
                                                      simultaneous=True)-expected), 0)
        self.assertEqual(sp.Matrix([[apply(t, value) for value in new_forward]
                                    for t in mixed]), sp.eye(4))
        self.assertEqual([filtration_top(t) for t in mixed],
                         [(2, (0, 0, 2*a*s**2, 0))]*4)

    def test_common_nonunit_intrinsic_top_has_no_slice(self):
        intrinsic = (0, 0, 2*a, 0)
        self.assertEqual(apply(intrinsic, a), 0)
        self.assertEqual(apply(intrinsic, b), 0)
        self.assertEqual(apply(intrinsic, c/2), a)
        for i in range(4):
            for j in range(4-i):
                for k in range(4-i-j):
                    image = apply(intrinsic, a**i*b**j*c**k)
                    self.assertEqual(image.subs(a, 0), 0)
        self.assertNotEqual(apply(intrinsic, c), 1)
        # General reason: every image under 2a*d/dc lies in the proper ideal
        # (a); its kernel is C[a,b] and its plinth ideal is (a), so it has no slice.


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O; exact checks must remain enabled.")
    unittest.main(verbosity=2)
