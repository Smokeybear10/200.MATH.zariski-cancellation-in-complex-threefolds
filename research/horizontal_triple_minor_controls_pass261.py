"""Finite controls for the horizontal triple-minor criterion in proof261.

The matrices below are differentiated from explicit actual polynomial
frames. These tests do not prove the universal selected-shift construction,
the unipotent closed-orbit theorem, or the global recognition implication.
No retained checker is imported. Root owns any saved-suite execution.
"""

import unittest

import sympy as sp


class HorizontalTripleMinorControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    @staticmethod
    def degree(expression, parameter):
        expression = sp.cancel(expression)
        if expression == 0:
            return -1
        return sp.Poly(expression, parameter).degree()

    def frame_data(self, frame, source):
        """Check all four exact signed minors and the slice unit identity."""
        u = source[3]
        matrix = sp.Matrix(frame).jacobian(source)
        determinant = sp.factor(matrix.det())
        self.assertNotEqual(determinant, 0)
        self.assert_zero(sp.diff(determinant, u))
        inverse = matrix.inv()
        horizontal = inverse[:3, :]
        degrees = [self.degree(value, u) for value in frame]
        shifts = [
            max(self.degree(horizontal[row, column], u) for row in range(3))
            for column in range(4)
        ]
        self.assertTrue(all(value > 0 for value in degrees))
        self.assertTrue(all(value >= 0 for value in shifts))
        tops = sp.zeros(3, 4)
        for column in range(4):
            for row in range(3):
                tops[row, column] = sp.Poly(
                    horizontal[row, column], u
                ).nth(shifts[column])

        for omitted in range(4):
            retained = [column for column in range(4) if column != omitted]
            minor = horizontal[:, retained].det()
            # One-based ell=omitted+1 gives (-1)^(4+ell).
            sign = (-1) ** (5 + omitted)
            expected = sign * sp.diff(frame[omitted], u) / determinant
            self.assert_zero(minor - expected)
            self.assertEqual(self.degree(minor, u), degrees[omitted] - 1)
            top_minor = sp.factor(tops[:, retained].det())
            shift_sum = sum(shifts[column] for column in retained)
            self.assertGreaterEqual(shift_sum, degrees[omitted] - 1)
            self.assertEqual(
                top_minor != 0, shift_sum == degrees[omitted] - 1
            )
            # The opposite sign is not an equally valid convention here.
            self.assertNotEqual(sp.cancel(minor + expected), 0)

        chain = sum(
            sp.diff(frame[column], u) * inverse[3, column]
            for column in range(4)
        )
        self.assert_zero(chain - 1)
        for residual in matrix * inverse - sp.eye(4):
            self.assert_zero(residual)
        return degrees, shifts, tops, inverse

    def test_affine_frame_all_triple_equalities(self):
        a, b, c, u = sp.symbols("a b c u")
        frame = [a + u, b + u, c + u, u]
        degrees, shifts, tops, inverse = self.frame_data(frame, [a, b, c, u])
        self.assertEqual(degrees, [1, 1, 1, 1])
        self.assertEqual(shifts, [0, 0, 0, 0])
        self.assertEqual(
            tops,
            sp.Matrix([[1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]]),
        )
        self.assertEqual(inverse[3, :], sp.Matrix([[0, 0, 0, 1]]))
        self.assertEqual(tops.rank(), 3)

    def test_actual_rank_collapse_and_both_inverse_orders(self):
        a, b, c, u = sp.symbols("a b c u")
        X1, X2, X3, X4 = sp.symbols("X1 X2 X3 X4")
        x2 = b + a**2 * u
        x3 = c + b * u
        frame = [a - x2 - x3 - u, x2, x3, u]
        degrees, shifts, tops, inverse = self.frame_data(frame, [a, b, c, u])
        self.assertEqual(degrees, [1, 1, 1, 1])
        self.assertEqual(shifts, [2, 2, 2, 2])
        self.assertEqual(
            tops, sp.Matrix([[0] * 4, [0] * 4, [2 * a] * 4])
        )
        self.assertEqual(tops.rank(), 1)
        self.assertEqual(inverse[3, :], sp.Matrix([[0, 0, 0, 1]]))

        restored_a = X1 + X2 + X3 + X4
        inverse_frame = [
            restored_a,
            X2 - restored_a**2 * X4,
            X3 - X2 * X4 + restored_a**2 * X4**2,
            X4,
        ]
        forward = dict(zip([X1, X2, X3, X4], frame))
        backward = dict(zip([a, b, c, u], inverse_frame))
        for original, expression in zip([a, b, c, u], inverse_frame):
            self.assert_zero(expression.subs(forward, simultaneous=True) - original)
        for original, expression in zip([X1, X2, X3, X4], frame):
            self.assert_zero(expression.subs(backward, simultaneous=True) - original)

    def test_mixed_positive_degrees_and_exact_top_cancellations(self):
        a, b, c, u = sp.symbols("a b c u")
        frame = [a + u, b + u**2, c + u**3, u]
        degrees, shifts, tops, inverse = self.frame_data(frame, [a, b, c, u])
        self.assertEqual(degrees, [1, 2, 3, 1])
        self.assertEqual(shifts, [0, 0, 0, 2])
        self.assertEqual(
            tops,
            sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, -3]]),
        )
        self.assertEqual(inverse[:3, 3], sp.Matrix([-1, -2 * u, -3 * u**2]))
        # Omitting the degree-three coordinate attains the exact bound.
        self.assertEqual(tops[:, [0, 1, 3]].det(), -3)
        # Omitting the degree-two coordinate has cancellation at degree two.
        self.assertEqual(tops[:, [0, 2, 3]].det(), 0)

    def test_unimodular_derivation_basis_need_not_be_coordinate_partials(self):
        a, b, c, u = sp.symbols("a b c u")
        basis = sp.Matrix(
            [[1, a, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        )
        self.assertEqual(basis.det(), 1)
        self.assertEqual(basis.inv(), basis.subs(a, -a))

        def first(expression):
            return sp.diff(expression, a)

        def second(expression):
            return a * sp.diff(expression, a) + sp.diff(expression, b)

        value = a
        for _ in range(6):
            value = second(value)
            self.assert_zero(value - a)
        bracket = [
            first(second(value)) - second(first(value))
            for value in [a, b, c, u]
        ]
        self.assertEqual(bracket, [1, 0, 0, 0])
        # The written all-iterate formula D^n(a)=a, not six samples,
        # is what proves that the second basis element is not an LND.


if __name__ == "__main__":
    unittest.main(verbosity=2)
