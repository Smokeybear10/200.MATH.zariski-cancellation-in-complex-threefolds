"""Finite exact controls, not a proof of frame existence or classification."""

import unittest

import sympy as sp


def act(field, value, variables):
    return sp.expand(sum(a * sp.diff(value, x) for a, x in zip(field, variables)))


def bracket(left, right, variables):
    return sp.Matrix([
        act(left, b, variables) - act(right, a, variables)
        for a, b in zip(left, right)
    ]).applyfunc(sp.expand)


class ActualFrameControls(unittest.TestCase):
    def setUp(self):
        self.x, self.y, self.z, self.w, self.t, self.h = sp.symbols("x y z w t h")
        self.variables = (self.x, self.y, self.z, self.w)
        self.partials = [sp.eye(4)[:, i] for i in range(4)]

    def assert_zero_matrix(self, matrix):
        self.assertEqual(matrix.applyfunc(sp.simplify), sp.zeros(*matrix.shape))

    def test_coordinate_double_commutator_matrix_identity(self):
        x, y, z, w = self.variables
        fields = [
            sp.Matrix([1, x, 0, 0]),
            sp.Matrix([1, 0, y, y**2]),
            sp.Matrix([0, x**2, 3*x**2*y, 1]),
            sp.Matrix([x*y, z + x**2, w*y, x + z**2]),
        ]
        for field in fields:
            jac = field.jacobian(self.variables)
            derivative = jac.applyfunc(lambda a: act(field, a, self.variables))
            for i, partial in enumerate(self.partials):
                actual = bracket(field, bracket(field, partial, self.variables), self.variables)
                self.assert_zero_matrix(actual - (-derivative + jac**2)[:, i])

    def test_whole_height_one_first_commutators_commute(self):
        x, y, z, w = self.variables
        for field in [sp.Matrix([1, x, 0, 0]), sp.Matrix([1, 0, y, y**2]),
                      sp.Matrix([0, x**2, 3*x**2*y, 1])]:
            first = [bracket(field, partial, self.variables) for partial in self.partials]
            for left in first:
                self.assert_zero_matrix(bracket(field, left, self.variables))
                for right in first:
                    self.assert_zero_matrix(bracket(left, right, self.variables))

    def test_nilpotent_chain_and_factorial_derivative(self):
        x, y, z, w = self.variables
        field = sp.Matrix([0, x**2, 3*x**2*y, 1])
        jac = field.jacobian(self.variables)
        self.assertNotEqual(jac**2, sp.zeros(4))
        derivative = jac
        for m in range(4):
            self.assert_zero_matrix(derivative - sp.factorial(m) * jac**(m + 1))
            derivative = derivative.applyfunc(lambda a: act(field, a, self.variables))
        jordan = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])
        vector = sp.Matrix([0, 0, 0, 1])
        self.assertEqual(sp.Matrix.hstack(vector, jordan*vector, jordan**2*vector).rank(), 3)
        self.assertGreaterEqual(sp.Matrix.hstack(vector, jordan).rank(), 3)

    def test_non_quasi_translation_projective_line_flow(self):
        x, y, z, w = self.variables
        t = self.t
        field = sp.Matrix([1, x, 0, 0])
        jac = field.jacobian(self.variables)
        flow = {x: x + t, y: y + t*x + t**2/sp.Integer(2), z: z, w: w}
        actual = field.subs(flow, simultaneous=True)
        first = field.applyfunc(lambda a: act(field, a, self.variables))
        self.assert_zero_matrix(actual - field - t*first)
        self.assertNotEqual(first, sp.zeros(4, 1))
        self.assert_zero_matrix(first.applyfunc(lambda a: act(field, a, self.variables)))
        self.assertEqual(sp.Matrix.hstack(field, jac).rank(), 2)
        self.assertEqual(sp.Matrix.hstack(field, first).rank(), 2)
        reverse = {x: x - t, y: y - t*x + t**2/sp.Integer(2), z: z, w: w}
        for coordinate in self.variables:
            self.assertEqual(sp.expand(flow[coordinate].subs(reverse, simultaneous=True)), coordinate)

    def test_low_rank_quasi_translation_homogenization(self):
        x, y, z, w = self.variables
        h = self.h
        field = sp.Matrix([1, 0, y, y**2])
        jac = field.jacobian(self.variables)
        self.assert_zero_matrix(jac*field)
        self.assert_zero_matrix(jac**2)
        self.assertEqual(jac.rank(), 1)
        self.assertEqual(sp.Matrix.hstack(field, jac).rank(), 2)
        homogeneous = sp.Matrix([h**2, 0, h*y, y**2, 0])
        full_jac = homogeneous.jacobian((*self.variables, h))
        self.assertEqual(full_jac.rank(), 2)
        self.assert_zero_matrix(full_jac*homogeneous)
        self.assertEqual(homogeneous[2]**2 - homogeneous[0]*homogeneous[3], 0)
        self.assertEqual(len([sp.expand(value) for value in homogeneous if value != 0]), 3)
        for row in [sp.Matrix([[0, 1, 0, 0, 0]]), sp.Matrix([[0, 0, 0, 0, 1]])]:
            self.assert_zero_matrix(row*homogeneous)

    def test_full_homogenized_jacobian_column_and_high_rank_control(self):
        x, y, z, w = self.variables
        h = self.h
        field = sp.Matrix([1 + x*y, z + x**2, w*y, x + z**2])
        degree = 2
        substitution = {a: a/h for a in self.variables}
        value = field.subs(substitution, simultaneous=True)
        old_jac = field.jacobian(self.variables).subs(substitution, simultaneous=True)
        homogeneous = sp.Matrix([sp.expand(h**degree*a) for a in value] + [0])
        full_jac = homogeneous.jacobian((*self.variables, h))
        expected_top = h**(degree - 1) * sp.Matrix.hstack(
            old_jac, degree*value - old_jac*sp.Matrix([a/h for a in self.variables])
        )
        expected = expected_top.col_join(sp.zeros(1, 5))
        self.assert_zero_matrix(full_jac - expected)
        corrected = full_jac[:, 4] + sum(
            ((self.variables[i]/h)*full_jac[:, i] for i in range(4)),
            sp.zeros(5, 1),
        )
        self.assert_zero_matrix(corrected - sp.Matrix([degree*h**(degree - 1)*a for a in value] + [0]))
        high = sp.Matrix([0, x**2, 3*x**2*y, 1])
        high_jac = high.jacobian(self.variables)
        self.assertEqual(sp.Matrix.hstack(high, high_jac).rank(), 3)
        self.assertNotEqual(high_jac**2, sp.zeros(4))
        self.assert_zero_matrix(high_jac.applyfunc(lambda a: act(high, a, self.variables)) - high_jac**2)


if __name__ == "__main__":
    unittest.main()
