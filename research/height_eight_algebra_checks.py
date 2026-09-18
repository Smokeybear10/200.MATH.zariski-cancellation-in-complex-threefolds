#!/usr/bin/env python3
"""Exact controls for the height-eight proof, without research-module imports."""

import unittest
from math import factorial

import sympy as sp


a, b, c, d = x = sp.symbols("a b c d")
t, v = sp.symbols("t v")
A, B, S, U = target = sp.symbols("A B S U")


def apply(field, value, coordinates=x):
    return sp.expand(sum(coefficient*sp.diff(value, variable)
                         for coefficient, variable in zip(field, coordinates)))


def bracket(left, right):
    return tuple(sp.expand(apply(left, q)-apply(right, p))
                 for p, q in zip(left, right))


def partial(index):
    return tuple(sp.Integer(j == index) for j in range(4))


def matrix_zero(matrix):
    return all(sp.expand(value) == 0 for value in matrix)


def triangular_field():
    return (1, a, b+a*a/2, c+a*b+a**3/6)


class HeightEightAlgebraTests(unittest.TestCase):
    def test_riccati_and_iterated_jacobian_factorials(self):
        field = triangular_field()
        jacobian = sp.Matrix(field).jacobian(x)
        self.assertTrue(matrix_zero(jacobian**4))
        self.assertEqual(jacobian.applyfunc(lambda q: apply(field, q)), jacobian**2)
        for index in range(4):
            self.assertEqual(bracket(field, bracket(field, partial(index))), (0,)*4)
        iterate = sp.Matrix(x)
        for order in range(1, 5):
            iterate = iterate.applyfunc(lambda q: apply(field, q))
            self.assertTrue(matrix_zero(iterate.jacobian(x)-factorial(order)*jacobian**order))
        self.assertEqual(iterate, sp.Matrix((0, 0, 0, 6)))
        self.assertEqual(bracket(field, tuple(iterate)), (0,)*4)

    def test_quartic_time_flow_and_jacobian(self):
        field = triangular_field()
        jacobian = sp.Matrix(field).jacobian(x)
        iterate = sp.Matrix(x)
        flow = sp.Matrix(x)
        for order in range(1, 5):
            iterate = iterate.applyfunc(lambda q: apply(field, q))
            flow += t**order*iterate/factorial(order)
        expected_jacobian = sp.eye(4)+t*jacobian+t*t*jacobian**2+t**3*jacobian**3
        self.assertTrue(matrix_zero(flow.jacobian(x)-expected_jacobian))
        composed = flow.subs(dict(zip(x, flow.subs(t, v))), simultaneous=True)
        self.assertTrue(matrix_zero(composed-flow.subs(t, t+v)))
        self.assertEqual(sp.degree(flow[3], t), 4)

    def test_nice_unimodular_family_has_exact_coordinate_inverse(self):
        for exponent in (1, 7):
            field = (0, 0, a**exponent, a**exponent*b-1)
            jacobian = sp.Matrix(field).jacobian(x)
            self.assertEqual(jacobian.rank(), 2)
            self.assertTrue(matrix_zero(jacobian**2))
            self.assertTrue(matrix_zero(jacobian*sp.Matrix(field)))
            local_slice = b*c-d
            invariant = (a**exponent*b-1)*c-a**exponent*d
            self.assertEqual(apply(field, local_slice), 1)
            self.assertEqual(apply(field, invariant), 0)
            forward = (a, b, local_slice, invariant)
            inverse = (A, B, A**exponent*S-U, (A**exponent*B-1)*S-B*U)
            self.assertEqual(tuple(sp.expand(q.subs(dict(zip(x, inverse)), simultaneous=True))
                                   for q in forward), target)
            self.assertEqual(tuple(sp.expand(q.subs(dict(zip(target, forward)), simultaneous=True))
                                   for q in inverse), x)
            self.assertEqual(max(sp.Poly(q, x).total_degree() for q in field), exponent+1)

    def test_all_degree_one_frame_has_rank_collapse(self):
        # Adapted variables (A,B,U,S); the original c,d are AS-U,(AB-1)S-BU.
        coordinates = (A, B, U, S)
        old_c = A*S-U
        old_d = (A*B-1)*S-B*U
        frame = (A-old_c, B-old_d, old_c, old_d)
        fields = sp.Matrix(frame).jacobian(coordinates).inv().T.tolist()
        tops = []
        for field in fields:
            field = [sp.expand(q) for q in field]
            degree = max(sp.degree(q, S)-(j == 3)
                         for j, q in enumerate(field) if q != 0)
            self.assertEqual(degree, 1)
            tops.append([q.coeff(S, 1) for q in field[:3]])
        self.assertEqual(sp.Matrix(tops).rank(), 1)
        original = (0, 0, a, a*b-1)
        self.assertEqual(sp.Matrix([original]+[bracket(original, partial(j))
                                              for j in range(4)]).rank(), 2)

    def test_conical_homogenization_preserves_rank_two(self):
        homogeneous = sp.Matrix((0, 0, a*t, a*b-t*t, 0))
        coordinates = x+(t,)
        jacobian = homogeneous.jacobian(coordinates)
        self.assertEqual(jacobian.rank(), 2)
        self.assertTrue(matrix_zero(jacobian*homogeneous))
        for component in homogeneous:
            if component != 0:
                self.assertTrue(all(sum(monomial) == 2
                                    for monomial in sp.Poly(component, coordinates).monoms()))
        self.assertEqual(homogeneous.subs(t, 1), sp.Matrix((0, 0, a, a*b-1, 0)))

    def test_nice_with_slice_does_not_imply_double_commutator_identity(self):
        invariant = a+b*d-c*c
        field = (-d+2*c*invariant-b*invariant**2, 1, invariant, invariant**2)
        jacobian = sp.Matrix(field).jacobian(x)
        self.assertTrue(matrix_zero(jacobian*sp.Matrix(field)))
        self.assertEqual(apply(field, b), 1)
        self.assertEqual(jacobian.rank(), 2)
        self.assertFalse(matrix_zero(jacobian**2))
        self.assertTrue(any(bracket(field, bracket(field, partial(j))) != (0,)*4
                            for j in range(4)))

    def test_square_zero_jacobian_alone_is_not_the_riccati_identity(self):
        field = (0, a*a, a**3, 3*b*a*a-2*c*a)
        jacobian = sp.Matrix(field).jacobian(x)
        self.assertTrue(matrix_zero(jacobian**2))
        self.assertEqual((jacobian*sp.Matrix(field)).applyfunc(sp.expand),
                         sp.Matrix((0, 0, 0, a**4)))
        self.assertEqual(bracket(field, bracket(field, partial(0))),
                         (0, 0, 0, -4*a**3))


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run without -O; exact checks must remain enabled.")
    unittest.main(verbosity=2)
