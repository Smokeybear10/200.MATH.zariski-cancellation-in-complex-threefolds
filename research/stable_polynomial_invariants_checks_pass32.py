"""Independent exact controls for the cross-frame certificate note.

The finite examples have genuine polynomial cylinders. These tests do
not assert universal existence of a cross-frame determinant certificate,
pairwise commutation of its fields, cancellation, or formal proof of the
published invariant theorems. No project solver is imported.
"""

import unittest

import sympy as sp


a, b, c, s = sp.symbols("a b c s")
X1, X2, X3, X4 = sp.symbols("X1 X2 X3 X4")
u, beta, gamma, sigma = sp.symbols("u beta gamma sigma")
variables = (a, b, c, s)
formal_coordinates = (X1, X2, X3, X4)
E = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(1))


def expand_tuple(values):
    return tuple(sp.expand(value) for value in values)


def substitute(expr, mapping):
    return sp.expand(expr.subs(mapping, simultaneous=True))


def apply(field, polynomial):
    return sp.expand(sum(coefficient * sp.diff(polynomial, coordinate)
                         for coefficient, coordinate in zip(field, variables)))


def bracket(left, right):
    return tuple(sp.expand(apply(left, coefficient_right)
                           - apply(right, coefficient_left))
                 for coefficient_left, coefficient_right in zip(left, right))


def triangular_frame(order):
    first, second, third = order
    forward = (first, second + first**3 * s**2, third + second * s, s)
    inverse = {
        first: X1,
        second: X2 - X1**3 * X4**2,
        third: X3 - (X2 - X1**3 * X4**2) * X4,
        s: X4,
    }
    return forward, inverse


def coordinate_partials(forward, inverse):
    back_to_actual = dict(zip(formal_coordinates, forward))
    return tuple(
        tuple(substitute(sp.diff(inverse[coordinate], parameter), back_to_actual)
              for coordinate in variables)
        for parameter in formal_coordinates
    )


def highest_adjoint(field, order):
    result = field
    for _ in range(order):
        result = bracket(E, result)
    return tuple(sp.expand(value / sp.factorial(order)) for value in result)


class StablePolynomialInvariantsChecks(unittest.TestCase):
    def test_actual_two_sided_inverses_for_all_three_cyclic_frames(self):
        for order in ((a, b, c), (b, c, a), (c, a, b)):
            forward, inverse = triangular_frame(order)
            for expression, parameter in zip(forward, formal_coordinates):
                self.assertEqual(substitute(expression, inverse), parameter)
            substitution = dict(zip(formal_coordinates, forward))
            for coordinate in variables:
                self.assertEqual(substitute(inverse[coordinate], substitution),
                                 coordinate)
            for expression in forward:
                self.assertEqual(sp.Poly(expression, *variables, domain=sp.QQ)
                                 .as_expr(), expression)

    def test_all_actual_coordinate_partials_and_their_duality(self):
        forward, inverse = triangular_frame((a, b, c))
        partials = coordinate_partials(forward, inverse)
        expected = (
            (1, -3 * a**2 * s**2, 3 * a**2 * s**3, 0),
            (0, 1, -s, 0),
            (0, 0, 1, 0),
            (0, -2 * a**3 * s, 2 * a**3 * s**2 - b, 1),
        )
        self.assertEqual(partials, tuple(expand_tuple(row) for row in expected))
        for i, field in enumerate(partials):
            for j, coordinate in enumerate(forward):
                self.assertEqual(apply(field, coordinate), int(i == j))
            for other in partials:
                self.assertEqual(bracket(field, other), (0, 0, 0, 0))

    def test_affine_translation_target_loss_and_an_actual_invariant_replica(self):
        forward, inverse = triangular_frame((a, b, c))
        partials = coordinate_partials(forward, inverse)
        degrees = tuple(max(sp.Poly(value, s).degree()
                            for value in field if value != 0)
                        for field in partials)
        self.assertEqual(degrees, (3, 1, 0, 2))
        self.assertEqual(len(set(degrees)), 4)
        self.assertEqual(tuple(apply(field, a) for field in partials), (1, 0, 0, 0))
        coefficients = sp.symbols("alpha1:5")
        combination = tuple(sp.expand(sum(coefficients[i] * partials[i][j]
                                           for i in range(4)))
                            for j in range(4))
        self.assertEqual(apply(combination, a), coefficients[0])
        top = tuple(sp.expand(value).coeff(s, 3) for value in combination)
        self.assertEqual(top, (0, 0, 3 * coefficients[0] * a**2, 0))
        self.assertEqual(apply(top, a), 0)

        invariant_multiplier = forward[1]
        self.assertEqual(apply(partials[0], invariant_multiplier), 0)
        replica = expand_tuple(invariant_multiplier * value for value in partials[0])
        replica_top = tuple(value.coeff(s, 5) for value in replica)
        self.assertEqual(replica_top, (0, 0, 3 * a**5, 0))
        self.assertEqual(sp.Poly(apply(replica, a), s).degree(), 2)
        self.assertEqual(max(sp.Poly(value, s).degree()
                             for value in replica if value != 0), 5)
        self.assertEqual(apply(replica_top, a), 0)
        for coordinate in variables:
            iterate = coordinate
            for _ in range(4):
                iterate = apply(replica, iterate)
            self.assertEqual(iterate, 0)

    def test_cyclic_highest_adjoints_certificate_and_noncommutation(self):
        tops = []
        for order in ((a, b, c), (b, c, a), (c, a, b)):
            forward, inverse = triangular_frame(order)
            first_partial = coordinate_partials(forward, inverse)[0]
            top = highest_adjoint(first_partial, 3)
            self.assertNotEqual(top, (0, 0, 0, 0))
            self.assertEqual(bracket(E, top), (0, 0, 0, 0))
            tops.append(top)
        expected = (
            (0, 0, 3 * a**2, 0),
            (3 * b**2, 0, 0, 0),
            (0, 3 * c**2, 0, 0),
        )
        self.assertEqual(tuple(tops), tuple(expand_tuple(row) for row in expected))
        intrinsic_matrix = sp.Matrix.hstack(*(sp.Matrix(top[:3]) for top in tops))
        actual_matrix = sp.Matrix.hstack(sp.Matrix(E),
                                        *(sp.Matrix(top) for top in tops))
        self.assertEqual(sp.expand(intrinsic_matrix.det()), 27 * a**2 * b**2 * c**2)
        determinant = sp.expand(actual_matrix.det())
        self.assertEqual(determinant, -27 * a**2 * b**2 * c**2)
        self.assertEqual(apply(E, determinant), 0)
        self.assertEqual(bracket(tops[0], tops[1]),
                         (0, 0, -18 * a * b**2, 0))
        self.assertEqual(bracket(tops[1], tops[2]),
                         (-18 * b * c**2, 0, 0, 0))
        self.assertEqual(bracket(tops[2], tops[0]),
                         (0, -18 * a**2 * c, 0, 0))
        for top in tops:
            self.assertEqual(tuple(value.subs({a: 0, b: 0, c: 0})
                                   for value in top), (0, 0, 0, 0))
            for coordinate in variables:
                self.assertEqual(apply(top, apply(top, coordinate)), 0)

    def test_two_shear_inverse_and_derived_coordinate_partial(self):
        forward = (a - s, b - s * c, -s * b + (1 + s**2) * c, s)
        inverse = {
            a: u + sigma,
            b: (1 + sigma**2) * beta + sigma * gamma,
            c: sigma * beta + gamma,
            s: sigma,
        }
        parameters = (u, beta, gamma, sigma)
        for expression, parameter in zip(forward, parameters):
            self.assertEqual(substitute(expression, inverse), parameter)
        to_actual = dict(zip(parameters, forward))
        for coordinate in variables:
            self.assertEqual(substitute(inverse[coordinate], to_actual), coordinate)
        actual_partial = tuple(substitute(sp.diff(inverse[coordinate], sigma),
                                          to_actual)
                               for coordinate in variables)
        expected = (1, s * b + (1 - s**2) * c, b - s * c, 1)
        self.assertEqual(actual_partial, expand_tuple(expected))
        self.assertEqual(tuple(apply(actual_partial, expression)
                               for expression in forward), (0, 0, 0, 1))
        for coordinate in variables:
            value = coordinate
            for _ in range(3):
                value = apply(actual_partial, value)
            self.assertEqual(value, 0)

    def test_target_selected_lower_coefficient_is_not_locally_nilpotent(self):
        actual_partial = expand_tuple(
            (1, s * b + (1 - s**2) * c, b - s * c, 1))
        intrinsic_coefficients = tuple(
            tuple(sp.expand(value).coeff(s, degree) if index < 3 else sp.Integer(0)
                  for index, value in enumerate(actual_partial))
            for degree in range(3)
        )
        D0, D1, D2 = intrinsic_coefficients
        self.assertEqual(D0, (1, c, b, 0))
        self.assertEqual(D1, (0, b, -c, 0))
        self.assertEqual(D2, (0, -c, 0, 0))
        self.assertEqual(tuple(apply(field, a) for field in (D0, D1, D2)),
                         (1, 0, 0))
        self.assertEqual(apply(actual_partial, a), 1)
        value = b
        slope_value = b
        for iteration in range(1, 13):
            value = apply(D0, value)
            slope_value = apply(D1, slope_value)
            self.assertEqual(value, c if iteration % 2 else b)
            self.assertEqual(slope_value, b)
        self.assertEqual(highest_adjoint(actual_partial, 2), D2)
        for coordinate in variables:
            self.assertEqual(apply(D2, apply(D2, coordinate)), 0)
        self.assertEqual(bracket(E, D2), (0, 0, 0, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
