"""Finite controls for the weighted rank-one companion reduction.

The cubic example is an actual sliced action in the zero-r branch.
The separate differential data are formal controls, not actions.
Only unittest and SymPy are imported; no solver internals are used.
"""

import unittest

import sympy as sp


def clean(expression):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(sp.cancel)
    return sp.cancel(expression)


def act(field, polynomial, variables):
    return sp.expand(sum(value * sp.diff(polynomial, variable)
                         for value, variable in zip(field, variables)))


def bracket(left, right, variables):
    return sp.Matrix([act(left, p, variables) - act(right, q, variables)
                      for p, q in zip(right, left)])


class DependentDefectTopLineChecks(unittest.TestCase):
    def setUp(self):
        self.u, self.v, self.A, self.C = sp.symbols("u v A C")
        u, v, A, C = self.variables = (self.u, self.v, self.A, self.C)
        self.G = v ** 2 + 1
        self.E = sp.Matrix([0, 0, v, self.G])
        self.D = sp.Matrix([1, 0, 0, 0])
        F = (A ** 3 + C ** 3) / 6
        self.physical = sp.Matrix([(u + F + v) / 2,
                                   (u + F - v) / 2, A, C])
        self.partials = [sp.Matrix([1, 1, 0, 0]),
                         sp.Matrix([1, -1, 0, 0]),
                         sp.Matrix([-A ** 2 / 2, 0, 1, 0]),
                         sp.Matrix([-C ** 2 / 2, 0, 0, 1])]

    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_actual_two_sided_frames_and_slice_coordinates(self):
        u, v, A, C = self.variables
        x1, x2, x3, x4 = target = sp.symbols("x1 x2 x3 x4")
        inverse = sp.Matrix([x1 + x2 - (x3 ** 3 + x4 ** 3) / 6,
                             x1 - x2, x3, x4])
        self.assertZero(self.physical.subs(dict(zip(self.variables, inverse)),
                                          simultaneous=True) - sp.Matrix(target))
        self.assertZero(inverse.subs(dict(zip(target, self.physical)),
                                    simultaneous=True) - sp.Matrix(self.variables))
        for i, partial in enumerate(self.partials):
            self.assertZero(sp.Matrix([act(partial, p, self.variables)
                                       for p in self.physical]) - sp.eye(4)[:, i])
        r, s = sp.symbols("r s")
        slice_polynomial = C - v * A
        invariant = self.G * A - v * C
        inverse_slice = {A: r + v * s, C: v * r + self.G * s}
        self.assertZero(slice_polynomial.subs(inverse_slice, simultaneous=True) - s)
        self.assertZero(invariant.subs(inverse_slice, simultaneous=True) - r)
        self.assertZero(invariant + v * slice_polynomial - A)
        self.assertZero(v * invariant + self.G * slice_polynomial - C)
        self.assertZero(act(self.E, slice_polynomial, self.variables) - 1)
        self.assertZero(act(self.E, invariant, self.variables))

    def test_actual_exact_heights_defect_rank_and_noncube_top(self):
        u, v, A, C = self.variables
        first = [bracket(self.E, p, self.variables) for p in self.partials]
        second = [bracket(self.E, p, self.variables) for p in first]
        self.assertZero(second[0])
        self.assertZero(second[1])
        self.assertNotEqual(first[0], sp.zeros(4, 1))
        self.assertNotEqual(first[1], sp.zeros(4, 1))
        self.assertZero(second[2] + v ** 2 * self.D)
        self.assertZero(second[3] + self.G ** 2 * self.D)
        for field in second[2:]:
            self.assertNotEqual(field, sp.zeros(4, 1))
            self.assertZero(bracket(self.E, field, self.variables))
        self.assertEqual(sp.Matrix.hstack(*second[2:]).rank(), 1)
        alpha, beta = sp.symbols("alpha beta")
        relation = sp.Poly(alpha * v ** 2 + beta * self.G ** 2, v)
        equations = sp.Matrix(relation.all_coeffs()).jacobian((alpha, beta))
        self.assertEqual(equations.rank(), 2)
        layers = [self.physical]
        for _ in range(4):
            layers.append(sp.Matrix([act(self.E, p, self.variables) for p in layers[-1]]))
        q = v ** 3 + self.G ** 3
        c = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2), 0, 0])
        self.assertZero(layers[3] - c * q)
        self.assertZero(layers[4])
        self.assertEqual(sp.gcd(q, sp.diff(q, v)), 1)
        self.assertGreater(sp.degree(q, v), 0)
        self.assertZero(act(self.E, q, self.variables))
        self.assertZero(act(self.D, q, self.variables))
        # This action lies in the recognized rho=r=0 branch.
        row = sp.Matrix([[0, 0, -v ** 2, -self.G ** 2]])
        self.assertZero(row * layers[2])

    def test_actual_five_dimensional_companion_and_full_velocity_rows(self):
        u, v, A, C = self.variables
        layers = [self.physical]
        for _ in range(5):
            layers.append(sp.Matrix([act(self.E, p, self.variables) for p in layers[-1]]))
        velocity = layers[1]
        jacobian = sp.Matrix(4, 4, lambda i, j:
                             act(self.partials[j], velocity[i], self.variables))
        d = sp.Matrix([act(self.D, p, self.variables) for p in self.physical])
        row = sp.Matrix([[0, 0, -v ** 2, -self.G ** 2]])
        matrix = jacobian.row_join(-d / 2).col_join(row.row_join(sp.zeros(1)))
        time = sp.symbols("time")
        self.assertZero((sp.eye(5) - time * matrix).det() - 1)
        self.assertZero(matrix ** 4)
        self.assertEqual((matrix ** 3).rank(), 1)
        self.assertEqual((matrix ** 2).rank() - (matrix ** 3).rank(), 1)
        for j in (1, 2, 3, 4):
            expected = layers[j].col_join((j - 1) * row * layers[j - 1])
            self.assertZero(sp.factorial(j - 1) * matrix ** (j - 1)
                            * velocity.col_join(sp.zeros(1, 1)) - expected)
            derivative = sp.Matrix(4, 4, lambda i, k:
                                   act(self.partials[k], layers[j][i], self.variables))
            self.assertZero(sp.factorial(j) * (matrix ** j)[:4, :4] - derivative)

    def test_variable_row_differential_is_not_the_derivative_of_its_product(self):
        # Formal necessary-data control only: no full action is asserted here.
        t = sp.symbols("t")
        for m in (3, 4):
            q, r = t, sp.Integer(1)
            row = sp.Matrix([[sp.Rational(m - 1, m), t / m]])
            previous = sp.Matrix([t, 1])
            rho = (row * previous)[0]
            self.assertZero(rho - q * r)
            weighted_differential = (row * previous.diff(t))[0]
            self.assertZero(m * q * weighted_differential
                            - (m - 1) * rho * sp.diff(q, t))
            correction = (row.diff(t) * previous)[0]
            self.assertZero(sp.diff(rho, t) - weighted_differential - correction)
            self.assertNotEqual(correction, 0)
            self.assertZero(r * sp.diff(q, t) + m * q * sp.diff(r, t)
                            - m * correction)
            self.assertEqual(sp.cancel(rho ** m / q ** (m - 1)), t)

    def test_primitive_valuation_gate_does_not_use_a_unit_coefficient_ideal(self):
        u, v, a, b = sp.symbols("u v a b")
        # u*partial_a+v*partial_b is primitive but vanishes at u=v=0.
        vector = sp.Matrix([0, 0, u, v])
        self.assertEqual(sp.gcd(u, v), 1)
        self.assertZero(vector.subs({u: 0, v: 0}))
        for exponent in range(1, 5):
            q = u ** exponent
            for order in range(6):
                rho = u ** order * (v + 1)
                divisible_components = [sp.rem(rho * coefficient, q, u) == 0
                                        for coefficient in vector]
                self.assertEqual(all(divisible_components), order >= exponent)
        polynomial_ratio = clean(u ** 3 * (v + 1) * vector / u ** 3)
        self.assertTrue(all(item.is_polynomial(u, v, a, b) for item in polynomial_ratio))
        pole_ratio = clean(u ** 2 * (v + 1) * vector / u ** 3)
        self.assertFalse(pole_ratio[3].is_polynomial(u, v, a, b))


if __name__ == "__main__":
    unittest.main()
