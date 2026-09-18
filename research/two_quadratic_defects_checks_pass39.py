"""Exact controls for the actual two-quadratic-defect cylinder.

Only unittest and SymPy are imported. These six finite tests do not prove
the universal block lemma or the existence of a suitable coordinate frame.
"""

import unittest

import sympy as sp


class TwoQuadraticDefectsChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a, cls.b, cls.c, cls.d, cls.t = sp.symbols("a b c d t")
        a, b, c, d = cls.a, cls.b, cls.c, cls.d
        cls.x = (b, d, a, c)
        cls.u = b - sp.Rational(1, 2) * a**2
        cls.v = d - sp.Rational(1, 2) * c**2
        cls.g = cls.u * cls.v - 1
        cls.s = cls.v * a - c
        cls.r = cls.g * a - cls.u * c
        cls.P = sp.Matrix([a * cls.u, c * cls.g, cls.u, cls.g])
        cls.J = cls.P.jacobian(cls.x)
        cls.partials = [sp.eye(4)[:, i] for i in range(4)]
        cls.first = [cls.bracket(cls.P, field) for field in cls.partials]
        cls.second = [cls.bracket(cls.P, field) for field in cls.first]
        cls.V = cls.second[2].row_join(cls.second[3])
        cls.selector = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1]])
        cls.h2 = cls.clean(cls.J * cls.P)
        cls.M = cls.J.row_join(-cls.V / 2).col_join(
            cls.selector.row_join(sp.zeros(2))
        )

        cls.U, cls.V0, cls.R, cls.S = sp.symbols("U V0 R S")
        U, V0, R, S = cls.U, cls.V0, cls.R, cls.S
        cls.G = U * V0 - 1
        inverse_a = U * S - R
        inverse_c = cls.G * S - V0 * R
        cls.inverse = sp.Matrix([
            U + inverse_a**2 / 2,
            V0 + inverse_c**2 / 2,
            inverse_a,
            inverse_c,
        ])
        cls.forward = sp.Matrix([cls.u, cls.v, cls.r, cls.s])

    @staticmethod
    def clean(matrix):
        return matrix.applyfunc(sp.expand)

    @classmethod
    def act(cls, field, polynomial):
        return sp.expand(sum(
            field[i] * sp.diff(polynomial, variable)
            for i, variable in enumerate(cls.x)
        ))

    @classmethod
    def bracket(cls, left, right):
        return cls.clean(right.jacobian(cls.x) * left
                         - left.jacobian(cls.x) * right)

    @staticmethod
    def compose(value, variables, replacements):
        return value.subs(dict(zip(variables, replacements)), simultaneous=True)

    @staticmethod
    def degree_or_minus_infinity(value, variable):
        value = sp.expand(value)
        return -sp.oo if value == 0 else sp.Poly(value, variable).degree()

    def assert_zero(self, value):
        self.assertEqual(sp.expand(value), 0)

    def assert_zero_matrix(self, matrix):
        self.assertEqual(self.clean(matrix), sp.zeros(*matrix.shape))

    def test_polynomial_inverse_and_actual_slice(self):
        target = (self.U, self.V0, self.R, self.S)
        self.assert_zero_matrix(
            self.compose(self.forward, self.x, self.inverse) - sp.Matrix(target)
        )
        self.assert_zero_matrix(
            self.compose(self.inverse, target, self.forward) - sp.Matrix(self.x)
        )
        self.assertEqual(
            [self.act(self.P, value) for value in self.forward], [0, 0, 0, 1]
        )
        self.assert_zero(self.r - self.u * self.s + self.a)
        self.assert_zero_matrix(self.clean(self.h2.jacobian(self.x) * self.P))
        self.assert_zero_matrix(
            self.h2 - sp.Matrix([self.u**2, self.g**2, 0, 0])
        )

    def test_exact_adjoint_and_slice_filtration_profile(self):
        u, v, g, a, c = self.u, self.v, self.g, self.a, self.c
        expected_top = [
            sp.Matrix([-a, -v * c, -1, -v]),
            sp.Matrix([0, -u * c, 0, -u]),
            sp.Matrix([2 * u * a, 2 * u * v * c, 2 * u, 2 * u * v]),
            sp.Matrix([0, 2 * u * g * c, 0, 2 * u * g]),
        ]
        expected_r = [1, u**2, -2 * u, -2 * u**2 * g]
        computed_shifts = []
        for index, height in enumerate((1, 1, 2, 2)):
            highest = self.partials[index]
            for _ in range(height):
                highest = self.bracket(self.P, highest)
            self.assert_zero_matrix(highest - expected_top[index])
            self.assertNotEqual(self.clean(highest), sp.zeros(4, 1))
            self.assert_zero_matrix(self.bracket(self.P, highest))
            self.assert_zero(self.act(highest, self.r) - expected_r[index])

            # A derivation's slice-filtration shift is the maximum horizontal
            # coefficient degree and the vertical coefficient degree minus one.
            pulled_coefficients = [
                sp.expand(self.compose(
                    self.act(self.partials[index], value), self.x, self.inverse
                ))
                for value in self.forward
            ]
            degrees = [self.degree_or_minus_infinity(value, self.S)
                       for value in pulled_coefficients]
            computed_shifts.append(max(*degrees[:3], degrees[3] - 1))
        self.assertEqual(computed_shifts, [1, 1, 2, 2])
        self.assertEqual(sum(shift + 1 for shift in computed_shifts), 10)

    def test_companion_and_jordan_data(self):
        self.assertEqual(self.V.rank(), 2)
        self.assertEqual(self.selector.rank(), 2)
        square = self.clean(self.M**2)
        cube = self.clean(square * self.M)
        self.assert_zero_matrix(cube)
        self.assertEqual(self.M.rank(), 4)
        self.assertEqual(square.rank(), 2)
        self.assert_zero_matrix(square[:4, :4] - self.h2.jacobian(self.x) / 2)

        # For the realized top power, both annihilation hypotheses of the
        # written block lemma hold, and the upper-left rank is retained.
        self.assert_zero_matrix(self.M * square)
        self.assert_zero_matrix(square * self.M)
        self.assertEqual(square[:4, :4].rank(), square.rank())
        self.assertEqual(self.M[:, 4:].rank(), 2)
        self.assertEqual(self.M[4:, :].rank(), 2)

    def test_top_factor_identities_and_commuting_defects(self):
        ell = self.selector * self.P
        self.assert_zero_matrix(ell - sp.Matrix([self.u, self.g]))
        self.assert_zero_matrix(self.selector * self.h2)
        self.assert_zero_matrix(ell.jacobian(self.x) * self.P)
        self.assert_zero_matrix(self.J * self.h2 - self.V * ell / 2)
        self.assert_zero_matrix(
            self.J * self.h2.jacobian(self.x) - self.V * ell.jacobian(self.x)
        )
        fields = [self.P, self.first[0], self.first[1],
                  self.second[2], self.second[3]]
        for i, left in enumerate(fields):
            for right in fields[i + 1:]:
                self.assert_zero_matrix(self.bracket(left, right))

    def test_highest_vector_rank_nonnilpotence_and_unit_ideal(self):
        top_jacobian = self.h2.jacobian(self.x)
        self.assertEqual(top_jacobian.rank(), 2)
        self.assert_zero(
            top_jacobian[:2, :2].det() - 4 * self.u**2 * self.g
        )
        self.assert_zero(self.act(self.h2, self.u) - self.u**2)
        iterate = self.u
        for exponent in range(1, 6):
            iterate = self.act(self.h2, iterate)
            self.assert_zero(iterate - sp.factorial(exponent) * self.u**(exponent + 1))
            self.assertNotEqual(iterate, 0)
        self.assert_zero(
            self.u**2 * self.v**2 * (1 - 2 * self.g)
            + self.g**2 * (3 + 2 * self.g) - 1
        )
        # In particular the highest vector is not even a quasi-translation.
        self.assertNotEqual(self.clean(top_jacobian * self.h2), sp.zeros(4, 1))

    def test_actual_polynomial_flow_and_inverse_jacobian(self):
        t = self.t
        flow = self.clean(sp.Matrix(self.x) + t * self.P + t**2 * self.h2 / 2)
        jacobian = flow.jacobian(self.x)
        inverse_jacobian = self.clean(
            sp.eye(4) - t * self.J + t**2 * self.V * self.selector / 2
        )
        self.assert_zero_matrix(jacobian * inverse_jacobian - sp.eye(4))
        self.assert_zero_matrix(inverse_jacobian * jacobian - sp.eye(4))
        self.assert_zero_matrix(
            self.compose(flow, self.x, self.inverse)
            - self.inverse.subs(self.S, self.S + t)
        )
        self.assert_zero_matrix(flow.diff(t).subs(t, 0) - self.P)
        self.assert_zero_matrix(flow.diff(t, 2) - self.h2)
        self.assert_zero_matrix(flow.diff(t, 3))
        self.assert_zero_matrix(jacobian.diff(t).subs(t, 0) - self.M[:4, :4])
        self.assert_zero_matrix(
            jacobian.diff(t, 2) / 2 - (self.M**2)[:4, :4]
        )


if __name__ == "__main__":
    unittest.main()
