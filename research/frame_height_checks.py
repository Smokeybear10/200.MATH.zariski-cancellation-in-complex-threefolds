#!/usr/bin/env python3
"""Exact coordinate-frame controls, not a cancellation decision procedure.

Independent of research modules and the existing filtration checker.
Run with /opt/anaconda3/bin/python research/frame_height_checks.py.
"""

import unittest
from functools import lru_cache
from itertools import combinations

import sympy as sp


a, b, c, s = variables = sp.symbols("a b c s")
x1, x2, x3, x4 = x = sp.symbols("x1 x2 x3 x4")


def apply(field, value):
    return sp.expand(sum(coefficient * sp.diff(value, variable)
                         for coefficient, variable in zip(field, variables)))


def bracket(left, right):
    return tuple(sp.expand(apply(left, v) - apply(right, u))
                 for u, v in zip(left, right))


@lru_cache(None)
def partials(frame):
    inverse_jacobian = sp.Matrix(frame).jacobian(variables).inv().T
    return tuple(tuple(sp.expand(v) for v in row)
                 for row in inverse_jacobian.tolist())


def top(field):
    degree = max(sp.degree(v, s) - (j == 3)
                 for j, v in enumerate(field) if v != 0)
    intrinsic = tuple(v.coeff(s, degree) if degree >= 0 else sp.Integer(0)
                      for v in field[:3])
    return int(degree), intrinsic


def profile(frame):
    tops = [top(field) for field in partials(frame)]
    return (tuple(q for q, _ in tops),
            sum(q + 1 for q, _ in tops),
            sp.Matrix([field for _, field in tops]).rank())


def elementary_sequence(initial, changes):
    frames = [tuple(initial)]
    for target, addition in changes:
        if sp.diff(addition, x[target]) != 0:
            raise ValueError("An elementary shear must omit its target variable")
        new = list(frames[-1])
        new[target] = sp.expand(new[target] + addition.subs(
            dict(zip(x, frames[-1])), simultaneous=True))
        frames.append(tuple(new))
    return tuple(frames)


def controls():
    r = a - s*b
    return (
        (elementary_sequence(
            (a-(b+a*a*s)-(c+b*s)-s, b+a*a*s, c+b*s, s),
            ((0, x2+x3+x4), (2, -x2*x4+x1*x1*x4*x4),
             (1, -x1*x1*x4))),
         (12, 8, 5, 3), (1, 1, 2, 3)),
        (elementary_sequence(
            (a+s*s, b+a*s, c+b*s, s+(a+s*s)**2),
            ((3, -x1*x1), (0, -x4*x4),
             (2, -x2*x4+x1*x4*x4), (1, -x1*x4))),
         (13, 10, 8, 5, 3), (1, 1, 1, 2, 3)),
        (elementary_sequence(
            (a-c*s*r, b-c*r, c, s),
            ((0, -x4*x2), (1, x3*x1), (0, x4*x2))),
         (11, 8, 5, 3), (1, 1, 2, 3)),
    )


class CoordinateFrameTests(unittest.TestCase):
    def test_elementary_sequences_finish_at_adapted_frame(self):
        for frames, _, _ in controls():
            self.assertEqual(frames[-1], variables)

    def test_exact_height_and_rank_profiles(self):
        for frames, heights, ranks in controls():
            self.assertEqual(tuple(profile(f)[1] for f in frames), heights)
            self.assertEqual(tuple(profile(f)[2] for f in frames), ranks)
            self.assertTrue(all(left > right
                                for left, right in zip(heights, heights[1:])))

    def test_coordinate_partial_pairings(self):
        for frames, _, _ in controls():
            for frame in frames:
                self.assertEqual(sp.expand(
                    sp.Matrix(frame).jacobian(variables).det()), 1)
                self.assertEqual(
                    sp.Matrix([[apply(t, value) for value in frame]
                               for t in partials(frame)]), sp.eye(4))

    def test_all_frame_partials_commute(self):
        for frames, _, _ in controls():
            for frame in frames:
                for left, right in combinations(partials(frame), 2):
                    self.assertEqual(bracket(left, right), (0, 0, 0, 0))

    def test_degree_zero_partials_commute_with_slice_action(self):
        vertical = (0, 0, 0, 1)
        for frames, _, _ in controls():
            for frame in frames:
                for field in partials(frame):
                    if top(field)[0] == 0:
                        self.assertEqual(bracket(field, vertical), (0, 0, 0, 0))

    def test_sharp_small_height_rank_controls(self):
        self.assertEqual(profile((a, b, c+(a+b)*s, s)), ((1, 1, 0, 0), 6, 1))
        self.assertEqual(profile((a, b+a*s, c, s)), ((1, 0, 0, 0), 5, 2))
        self.assertEqual(profile((a+s, b, c, a-s)), ((0, 0, 0, 0), 4, 3))
        self.assertEqual(profile(variables), ((0, 0, 0, -1), 3, 3))

    def test_uncertified_cancellation_really_lowers_degree(self):
        frame = controls()[1][0][0]
        first, _, _, last = partials(frame)
        bad = tuple(sp.expand(v + 2*s*s*w) for v, w in zip(first, last))
        self.assertEqual(top(first)[0], 5)
        self.assertEqual(top(last)[0], 3)
        self.assertEqual(top(bad)[0], 3)
        self.assertEqual(apply(bad, a), 1+4*a*s)
        self.assertEqual(apply(bad, s), -2*a)
        self.assertEqual(bracket(bad, last),
                         tuple(sp.expand(-4*s*v) for v in last))

    def test_bad_cancellation_restriction_has_non_nilpotent_top(self):
        highest = (4*a*s, 0, 0, 0)
        value = a
        for n in range(1, 9):
            value = apply(highest, value)
            self.assertEqual(value, (4*s)**n*a)
        # Induction gives this nonzero expression for every n, not just eight.

    def test_common_nonunit_control_has_equal_tops(self):
        frame = controls()[0][0][0]
        self.assertEqual([top(t) for t in partials(frame)],
                         [(2, (0, 0, 2*a))]*4)

    def test_freudenburg_primitive_fixed_point_control(self):
        f = a*c-b*b
        g = c*f*f+2*a*a*b*f+a**5
        vector = tuple(sp.expand(v) for v in
                       sp.Matrix([sp.diff(f, t) for t in variables[:3]]).cross(
                           sp.Matrix([sp.diff(g, t) for t in variables[:3]])))
        self.assertEqual(sp.gcd_list(vector), 1)
        self.assertEqual(tuple(v.subs({a: 0, b: 0, c: 0}) for v in vector),
                         (0, 0, 0))
        self.assertEqual(apply(vector+(0,), f), 0)
        self.assertEqual(apply(vector+(0,), g), 0)
        # LND and rank-three assertions use the cited theorem, not this test.


class SinglePartialCommutatorTests(unittest.TestCase):
    @staticmethod
    def partial(index):
        return tuple(sp.Integer(j == index) for j in range(4))

    def test_all_double_commutators_vanish_for_cubic_flow(self):
        field = (1, a, b+a*a/2, 0)
        for index in range(3):
            self.assertEqual(bracket(field, bracket(field, self.partial(index))),
                             (0, 0, 0, 0))
        jacobian = sp.Matrix(field[:3]).jacobian(variables[:3])
        self.assertEqual(jacobian.applyfunc(lambda value: apply(field, value)),
                         jacobian**2)

    def test_cubic_flow_has_nonlinear_coordinate_but_no_linear_invariant(self):
        field = (1, a, b+a*a/2, 0)
        self.assertEqual(apply(field, apply(field, apply(field, c))), 2)
        self.assertEqual(apply(field, apply(field, apply(field, apply(field, c)))),
                         0)
        linear = sp.symbols("linear_a linear_b linear_c")
        derivative = apply(field, sum(v*w for v, w in zip(linear, variables[:3])))
        self.assertEqual(sp.solve(sp.Poly(derivative, a, b, c).coeffs(), linear),
                         dict.fromkeys(linear, 0))
        invariant = b-a*a/2
        self.assertEqual(apply(field, invariant), 0)
        forward = (a, invariant, c)
        inverse = (a, b+a*a/2, c)
        for outer, inner in ((forward, inverse), (inverse, forward)):
            self.assertEqual(tuple(sp.expand(value.subs(
                dict(zip(variables[:3], inner)), simultaneous=True)) for value in outer),
                variables[:3])

    def test_reducible_dependent_commutator_has_plane_primitive(self):
        invariant = 2*c-b*b
        common = a*invariant
        primitive = (0, 1, b, 0)
        field = tuple(sp.expand(common*v) for v in primitive)
        commutator = bracket(field, self.partial(0))
        self.assertEqual(commutator,
                         tuple(sp.expand(-invariant*v) for v in primitive))
        self.assertEqual(bracket(field, commutator), (0, 0, 0, 0))
        self.assertEqual(apply(field, common), 0)
        self.assertIn(sp.cancel(sp.gcd_list(field)/common), (1, -1))
        self.assertEqual(tuple(sp.diff(v, a) for v in primitive), (0, 0, 0, 0))
        self.assertEqual(apply(primitive, invariant), 0)
        self.assertEqual(sp.Matrix((b, invariant)).jacobian((b, c)).det(), 2)
        # The proportionality factor -1/a is rational, not polynomial.
        self.assertEqual(tuple(sp.cancel(w+v/a) for w, v in zip(commutator, field)),
                         (0, 0, 0, 0))

    def test_nonlinear_triangular_lnd_has_nonzero_double_commutator(self):
        field = (b*b, c, 0, 0)
        self.assertEqual(bracket(field, bracket(field, self.partial(2))),
                         (2*b, 0, 0, 0))
        value = a
        for expected in (b*b, 2*b*c, 2*c*c, 0):
            value = apply(field, value)
            self.assertEqual(value, expected)

    def test_cube_zero_generators_do_not_imply_double_commutator_zero(self):
        invariant = a*c+b*b
        field = (-2*b*invariant, c*invariant, 0, 0)
        for value in variables[:3]:
            self.assertEqual(apply(field, apply(field, apply(field, value))), 0)
        self.assertEqual(bracket(field, bracket(field, self.partial(1))),
                         tuple(sp.expand(-4*c*v) for v in field))
        self.assertNotEqual(bracket(field, bracket(field, self.partial(1))),
                            (0, 0, 0, 0))

    def test_height_seven_flow_frame_satisfies_degree_one_commutators(self):
        flow_a = a+s
        flow_b = b+a*s+s*s/2
        flow_c = c+s*(b+a*a/2)+a*s*s+s**3/3
        frame = tuple(sp.expand(v) for v in
                      (flow_a+flow_c, flow_b+flow_c, flow_c, s))
        self.assertEqual(profile(frame), ((1, 1, 1, 0), 7, 3))
        vertical = self.partial(3)
        for field in partials(frame):
            if top(field)[0] == 1:
                self.assertEqual(bracket(vertical, bracket(vertical, field)),
                                 (0, 0, 0, 0))


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O; exact checks must remain enabled.")
    unittest.main(verbosity=2)
