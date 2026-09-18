"""Exact actual-frame controls for dependent-quadratic-defects-pass42.md.

Only unittest and SymPy are imported. These finite controls do not prove
the general primitive-division statement or universal frame recognition.
"""

import unittest

import sympy as sp


def reduce(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda item: sp.cancel(sp.expand(item)))
    return sp.cancel(sp.expand(value))


def apply(field, value, variables):
    return reduce(sum(coefficient * sp.diff(value, variable)
                      for coefficient, variable in zip(field, variables)))


def bracket(left, right, variables):
    return reduce(right.jacobian(variables) * left - left.jacobian(variables) * right)


def substitute(value, variables, images):
    return reduce(value.subs(dict(zip(variables, images)), simultaneous=True))


class DependentQuadraticDefectChecks(unittest.TestCase):
    def setUp(self):
        self.u, self.v, self.A, self.C = sp.symbols("u v A C")
        self.variables = (self.u, self.v, self.A, self.C)
        self.x = sp.Matrix(self.variables)
        self.f = self.u + self.v
        self.q = self.f**2 + 1
        self.E = sp.Matrix([0, 0, self.f, self.q])
        self.H = sp.Matrix([0, 0, 1, 2 * self.f])
        self.partials = (
            sp.Matrix([1, 0, 0, 0]),
            sp.Matrix([0, 1, 0, 0]),
            sp.Matrix([-self.A, 0, 1, 0]),
            sp.Matrix([0, -self.C, 0, 1]),
        )

    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(reduce(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(reduce(value), 0)

    def test_slice_and_both_polynomial_inverse_compositions(self):
        u, v, A, C = self.variables
        f, q = self.f, self.q
        r, s = sp.symbols("r s")
        target = (u, v, r, s)
        forward = sp.Matrix([u, v, q * A - f * C, C - f * A])
        inverse = sp.Matrix([u, v, r + f * s, f * r + q * s])
        self.assertZero(substitute(forward, self.variables, inverse) - sp.Matrix(target))
        self.assertZero(substitute(inverse, target, forward) - self.x)
        self.assertZero(forward.jacobian(self.variables) * self.E - sp.Matrix([0, 0, 0, 1]))
        self.assertZero(q - f**2 - 1)
        self.assertZero(forward.jacobian(self.variables).det() - 1)

    def test_actual_physical_frame_and_exact_adjoint_heights(self):
        u, v, A, C = self.variables
        B0, D0 = sp.symbols("B0 D0")
        physical = sp.Matrix([u + A**2 / 2, v + C**2 / 2, A, C])
        physical_variables = (B0, D0, A, C)
        inverse = sp.Matrix([B0 - A**2 / 2, D0 - C**2 / 2, A, C])
        self.assertZero(substitute(physical, self.variables, inverse) - sp.Matrix(physical_variables))
        self.assertZero(substitute(inverse, physical_variables, physical) - self.x)
        self.assertZero(physical.jacobian(self.variables) * sp.Matrix.hstack(*self.partials) - sp.eye(4))
        expected = (-self.H, -self.H, 2 * self.f * self.H, 2 * self.q * self.H)
        for index, (partial, height, top) in enumerate(zip(self.partials, (1, 1, 2, 2), expected)):
            with self.subTest(index=index):
                field = partial
                for _ in range(height):
                    field = bracket(self.E, field, self.variables)
                self.assertZero(field - top)
                self.assertNotEqual(field, sp.zeros(4, 1))
                self.assertZero(bracket(self.E, field, self.variables))
        self.assertZero(bracket(self.E, self.H, self.variables))

    def test_fraction_field_rank_one_but_no_constant_relation(self):
        pair = sp.Matrix.hstack(2 * self.f * self.H, 2 * self.q * self.H)
        self.assertEqual(pair.rank(), 1)
        self.assertEqual(sp.gcd(2 * self.f, 2 * self.q), 2)
        alpha, beta, F = sp.symbols("alpha beta F")
        relation = sp.Poly(alpha * F + beta * (F**2 + 1), F)
        coefficient_matrix = sp.Matrix([relation.coeff_monomial(F**degree) for degree in (0, 1, 2)]).jacobian((alpha, beta))
        self.assertEqual(coefficient_matrix.rank(), 2)
        # The second-adjoint map on the constant four-space has exactly two
        # independent polynomial coefficient columns, hence kernel dimension2.
        all_columns = sp.Matrix([[0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.assertEqual(all_columns.rank(), 2)
        self.assertEqual(len(all_columns.nullspace()), 2)
        self.assertZero(apply(self.E, self.f, self.variables))
        self.assertZero(apply(self.H, self.f, self.variables))
        self.assertZero(apply(self.E, self.q, self.variables))
        self.assertZero(apply(self.H, self.q, self.variables))

    def test_polynomial_syzygy_has_zero_second_adjoint_but_nonzero_divergence(self):
        field = self.q * self.partials[2] - self.f * self.partials[3]
        self.assertZero(bracket(self.E, bracket(self.E, field, self.variables), self.variables))
        divergence = sum(sp.diff(component, variable) for component, variable in zip(field, self.variables))
        self.assertZero(divergence - self.C + 2 * self.f * self.A)
        self.assertNotEqual(reduce(divergence), 0)
        # Independently reconstruct divergence in the physical frame, not
        # merely by trusting its invariance under the coordinate change.
        B0, D0 = sp.symbols("B0 D0")
        physical_f = B0 + D0 - (self.A**2 + self.C**2) / 2
        physical_q = physical_f**2 + 1
        physical_divergence = sp.diff(physical_q, self.A) - sp.diff(physical_f, self.C)
        self.assertZero(physical_divergence - self.C + 2 * physical_f * self.A)
        self.assertEqual(sp.gcd(physical_f, physical_q), 1)
        self.assertZero(physical_q - physical_f**2 - 1)

    def test_actual_degree_two_flow_and_rank_one_top(self):
        time = sp.symbols("time")
        physical = sp.Matrix([self.u + self.A**2 / 2, self.v + self.C**2 / 2, self.A, self.C])
        first = physical.applyfunc(lambda item: apply(self.E, item, self.variables))
        second = first.applyfunc(lambda item: apply(self.E, item, self.variables))
        third = second.applyfunc(lambda item: apply(self.E, item, self.variables))
        self.assertZero(second - sp.Matrix([self.f**2, self.q**2, 0, 0]))
        self.assertZero(third)
        self.assertEqual(second.jacobian(self.variables).rank(), 1)
        linear_flow = self.x + time * self.E
        self.assertZero(substitute(physical, self.variables, linear_flow)
                        - physical - time * first - time**2 * second / 2)
        self.assertZero(substitute(self.x - time * self.E, self.variables, linear_flow) - self.x)
        self.assertZero(linear_flow.jacobian(self.variables).det() - 1)


if __name__ == "__main__":
    unittest.main()
