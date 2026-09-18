"""Bounded nice-action adjoint and constant-direction controls.

The positive actions are actual polynomial nice LNDs with a linear slice.
Jordan matrices are only linear-algebra controls. Neither finite examples
nor this suite prove the general vertical exclusion or source theorem.
No research modules are imported.
"""

import unittest

import sympy as sp


class NiceSliceAdjointChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    @staticmethod
    def examples(x):
        first, second, third, fourth = x
        invariant = first * third - second**2 + fourth
        return (
            sp.Matrix([1, third, 0, second - first * third]),
            sp.Matrix([1, invariant, invariant**2,
                       -invariant**2 * first + 2 * invariant * second - third]),
        )

    def test_actual_nice_flows_and_all_partial_adjoint_formulas(self):
        x = sp.Matrix(sp.symbols("x y z w"))
        time, other_time = sp.symbols("time other_time")
        identity = sp.eye(4)
        expected_profiles = ((1, 1, 2, 0), (2, 2, 2, 1))
        for velocity, expected in zip(self.examples(x), expected_profiles):
            with self.subTest(velocity=velocity):
                jacobian = velocity.jacobian(x)

                def act(expression):
                    return sum(value * sp.diff(expression, variable)
                               for variable, value in zip(x, velocity))

                def bracket(field):
                    return (field.applyfunc(act) - jacobian * field).applyfunc(sp.expand)

                def flow(parameter):
                    return x + parameter * velocity

                self.assert_zero(jacobian * velocity)
                self.assert_zero(velocity.applyfunc(act))
                self.assert_zero(act(x[0]) - 1)
                self.assert_zero(jacobian.applyfunc(act) + jacobian**2)
                self.assert_zero(jacobian**3)
                self.assert_zero((identity + time * jacobian).det() - 1)
                self.assert_zero(velocity.subs(dict(zip(x, flow(time))), simultaneous=True)
                                 - velocity)
                self.assert_zero(flow(time).subs(dict(zip(x, flow(other_time))),
                                                simultaneous=True) - flow(time + other_time))
                self.assert_zero(flow(time).subs(dict(zip(x, flow(-time))),
                                                simultaneous=True) - x)
                self.assert_zero(flow(-time).subs(dict(zip(x, flow(time))),
                                                 simultaneous=True) - x)
                inverse_matrix = sum(((-time)**power * jacobian**power
                                      for power in range(4)), sp.zeros(4))
                self.assert_zero((identity + time * jacobian) * inverse_matrix - identity)
                self.assert_zero(inverse_matrix * (identity + time * jacobian) - identity)
                transported = identity - time * jacobian.subs(
                    dict(zip(x, flow(time))), simultaneous=True)
                self.assert_zero(transported - inverse_matrix)

                profiles = []
                for column in range(4):
                    field = identity[:, column]
                    height = 0
                    for power in range(1, 5):
                        field = bracket(field)
                        self.assert_zero(field - (-1)**power * sp.factorial(power)
                                         * jacobian**power * identity[:, column])
                        if any(entry != 0 for entry in field):
                            height = power
                    profiles.append(height)
                self.assertEqual(tuple(profiles), expected)

    def test_jordan_data_and_exact_constant_good_boundary(self):
        # These five representatives are formal constant nilpotent matrices,
        # not asserted to be Jacobians of sliced nice actions.
        partitions = ((4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1))
        for partition in partitions:
            matrix = sp.zeros(4)
            offset = 0
            for size in partition:
                for index in range(size - 1):
                    matrix[offset + index, offset + index + 1] = 1
                offset += size
            self.assert_zero(matrix**4)
            if any(entry != 0 for entry in matrix**3):
                self.assertEqual(partition, (4,))
                self.assertEqual(matrix.rank(), 3)
                self.assertEqual(len(matrix.nullspace()), 1)
                self.assert_zero(matrix * matrix**3)
            else:
                self.assertLessEqual(matrix.rank(), 2)
                if any(entry != 0 for entry in matrix**2):
                    self.assertEqual(partition, (3, 1))
                    self.assertEqual((matrix**2).rank(), 1)

        x, y, z, w = sp.symbols("x y z w")
        variables = sp.Matrix([x, y, z, w])
        invariant = x * z - y**2 + w
        velocity = self.examples(variables)[1]
        jacobian = velocity.jacobian(variables)
        square = (jacobian**2).applyfunc(sp.expand)
        self.assert_zero(square[1, :] - sp.Matrix([[-invariant**2, 2 * invariant, -1, 0]]))
        self.assert_zero(square[:, 3])
        constants = sp.symbols("c0:4")
        equations = sp.Poly((square * sp.Matrix(constants))[1], x, y, z, w).coeffs()
        coefficient_matrix, right = sp.linear_eq_to_matrix(equations, constants)
        self.assert_zero(right)
        self.assertEqual(coefficient_matrix.nullspace(), [sp.Matrix([0, 0, 0, 1])])
        self.assertEqual(jacobian.rank(), 2)
        self.assertEqual(square.rank(), 1)
        self.assertEqual(velocity.row_join(square).rank(), 2)
        self.assertEqual(sum(height + 1 for height in (2, 2, 2, 1)), 11)

        # The reused example is already a translation in these actual
        # polynomial coordinates; absence of two constant good directions
        # is not a failure of nonlinear recognition.
        S, A, Y, Z = sp.symbols("S A Y Z")
        target = sp.Matrix([S, A, Y, Z])
        forward = sp.Matrix([x, invariant, y - x * invariant, z - x * invariant**2])
        inverse = sp.Matrix([S, Y + S * A, Z + S * A**2,
                             A - S * Z + Y**2 + 2 * S * A * Y])
        self.assert_zero(forward.subs(dict(zip(variables, inverse)), simultaneous=True) - target)
        self.assert_zero(inverse.subs(dict(zip(target, forward)), simultaneous=True) - variables)
        self.assert_zero(forward.jacobian(variables) * velocity - sp.Matrix([1, 0, 0, 0]))

    def test_actual_nonslice_replica_realizes_the_forbidden_four_block(self):
        x, y, z, w, time = sp.symbols("x y z w time")
        variables = sp.Matrix([x, y, z, w])
        q = y - x * z
        multiplier = w - x * q
        original = sp.Matrix([1, z, 0, q])
        velocity = multiplier * original
        jacobian = velocity.jacobian(variables)

        def act_original(expression):
            return sum(value * sp.diff(expression, variable)
                       for variable, value in zip(variables, original))

        def act(expression):
            return sum(value * sp.diff(expression, variable)
                       for variable, value in zip(variables, velocity))

        def bracket(field):
            return (field.applyfunc(act) - jacobian * field).applyfunc(sp.expand)

        self.assert_zero(act_original(multiplier))
        self.assert_zero(original.applyfunc(act_original))
        self.assert_zero(velocity.applyfunc(act))
        self.assert_zero(velocity - multiplier * original)
        self.assertGreater(sp.Poly(multiplier, *variables).total_degree(), 0)
        self.assert_zero(velocity.subs(dict.fromkeys(variables, 0)))
        flow = variables + time * velocity
        reverse = variables - time * velocity
        self.assert_zero(flow.subs(dict(zip(variables, reverse)), simultaneous=True) - variables)
        self.assert_zero(reverse.subs(dict(zip(variables, flow)), simultaneous=True) - variables)
        self.assert_zero(jacobian.applyfunc(act) + jacobian**2)
        self.assertEqual(tuple((jacobian**power).rank() for power in (1, 2, 3)), (3, 2, 1))
        self.assert_zero(jacobian**4)
        self.assert_zero(jacobian**3 - multiplier * velocity * sp.Matrix([[0, 0, 1, 0]]))
        highest = sp.Matrix([0, 0, 1, 0])
        for _ in range(3):
            highest = bracket(highest)
        self.assert_zero(highest + 6 * multiplier * velocity)
        self.assertTrue(any(entry != 0 for entry in highest))
        self.assert_zero(bracket(highest))
        self.assert_zero(act(x / multiplier) - 1)
        self.assert_zero(sp.diff(multiplier, z) - x**2)
        self.assertNotEqual(sp.diff(multiplier, z), 0)
        # No slice exists by evaluation at the displayed fixed point.
        # The polynomial divisibility and fixed-point identities, not
        # finitely many probes, are the written all-polynomial argument.
        # The localized slice x/g does not preserve the hypotheses for
        # the original partial: it moves the unit g, so is not an LND
        # on the localized ring.


if __name__ == "__main__":
    unittest.main(verbosity=2)
