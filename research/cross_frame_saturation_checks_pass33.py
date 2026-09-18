"""Finite exact controls for the nonlinear cross-frame saturation proof.

Only unittest and SymPy are imported. The all-LND conjugacy-orbit
quantifier, field-kernel theorem, and published open-orbit input remain
written proofs; no finite example here establishes those assertions.
"""

import unittest

import sympy as sp


a, b, c, s, t = sp.symbols("a b c s t")
X, Y, Z, S = sp.symbols("X Y Z S")
variables = (a, b, c, s)
formal = (X, Y, Z, S)
zero = (sp.Integer(0),) * 4
da = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
db = (sp.Integer(0), sp.Integer(1), sp.Integer(0), sp.Integer(0))
dc = (sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(0))
E = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(1))


def expand_field(field):
    return tuple(sp.expand(coefficient) for coefficient in field)


def apply(field, expression):
    return sp.expand(sum(coefficient * sp.diff(expression, variable)
                         for coefficient, variable in zip(field, variables)))


def bracket(left, right):
    return tuple(sp.expand(apply(left, right_coefficient)
                           - apply(right, left_coefficient))
                 for left_coefficient, right_coefficient in zip(left, right))


def compose(expression, substitution):
    return sp.expand(sp.sympify(expression).subs(substitution, simultaneous=True))


def conjugate(field, forward, inverse):
    """Compute psi * field * psi^-1 from supplied polynomial inverse maps."""
    substitution = dict(zip(variables, forward))
    return tuple(compose(apply(field, expression), substitution)
                 for expression in inverse)


def intrinsic_determinant(fields):
    return sp.expand(sp.Matrix.hstack(*(sp.Matrix(field[:3])
                                       for field in fields)).det())


class CrossFrameSaturationChecks(unittest.TestCase):
    def test_replica_bracket_identity_and_genuine_replica(self):
        L = expand_field((b, 0, 1, 0))
        h = db
        g = (a - b * c)**2 + b + 1
        self.assertEqual(apply(L, g), 0)
        replica = expand_field(g * coefficient for coefficient in L)
        left = bracket(replica, h)
        ordinary = bracket(L, h)
        recovered = tuple(sp.expand(value - g * other)
                          for value, other in zip(left, ordinary))
        expected = expand_field(-apply(h, g) * coefficient for coefficient in L)
        self.assertEqual(recovered, expected)
        self.assertEqual(apply(h, g), sp.expand(1 - 2 * c * (a - b * c)))
        self.assertNotEqual(apply(h, g), 0)
        for variable in variables:
            self.assertEqual(apply(replica, apply(replica, variable)), 0)
        self.assertEqual(bracket(E, replica), zero)

    def test_polynomial_conjugation_and_finite_vandermonde_recovery(self):
        L = expand_field((0, a, b, 0))
        forward = (a, b + t * a, c + t * b + t**2 * a / 2, s)
        inverse = (a, b - t * a, c - t * b + t**2 * a / 2, s)
        forward_substitution = dict(zip(variables, forward))
        inverse_substitution = dict(zip(variables, inverse))
        for variable, plus, minus in zip(variables, forward, inverse):
            self.assertEqual(compose(plus, inverse_substitution), variable)
            self.assertEqual(compose(minus, forward_substitution), variable)
        curve = conjugate(da, forward, inverse)
        self.assertEqual(curve, expand_field((1, -t, t**2 / 2, 0)))
        values = sp.Matrix([[coefficient.subs(t, time) for coefficient in curve]
                            for time in (0, 1, 2)])
        vandermonde = sp.Matrix([[sp.Integer(time)**degree for degree in range(3)]
                                 for time in (0, 1, 2)])
        recovered = vandermonde.inv() * values
        second_bracket = bracket(L, bracket(L, da))
        expected = sp.Matrix([da, bracket(L, da),
                              tuple(value / 2 for value in second_bracket)])
        self.assertEqual(recovered, expected)
        self.assertEqual(bracket(L, second_bracket), zero)
        self.assertEqual(bracket(E, curve), zero)
        for time in (0, 1, 2):
            actual = expand_field(value.subs(t, time) for value in curve)
            for variable in variables:
                self.assertEqual(apply(actual, apply(actual, variable)), 0)

    def test_two_replica_shear_steps_raise_generic_rank_from_one_to_three(self):
        h0 = dc
        self.assertEqual(bracket(da, h0), zero)
        self.assertEqual(bracket(db, h0), zero)
        self.assertEqual(apply(da, c**2), 0)
        self.assertEqual(apply(db, c**3), 0)
        first_replica = expand_field(c**2 * value for value in da)
        second_replica = expand_field(c**3 * value for value in db)
        first_bracket = bracket(first_replica, h0)
        second_bracket = bracket(second_replica, h0)
        self.assertEqual(first_bracket, expand_field((-2 * c, 0, 0, 0)))
        self.assertEqual(second_bracket, expand_field((0, -3 * c**2, 0, 0)))
        self.assertEqual(bracket(first_replica, first_bracket), zero)
        self.assertEqual(bracket(second_replica, second_bracket), zero)
        h1 = expand_field(left + right for left, right in zip(h0, first_bracket))
        h2 = expand_field(left + right for left, right in zip(h0, second_bracket))
        self.assertNotEqual(intrinsic_determinant((h0, h1, db)), 0)
        self.assertEqual(intrinsic_determinant((h0, h1, h2)), 6 * c**3)
        ambient_matrix = sp.Matrix.hstack(sp.Matrix(E), sp.Matrix(h0),
                                         sp.Matrix(h1), sp.Matrix(h2))
        self.assertEqual(sp.expand(ambient_matrix.det()), -6 * c**3)
        # This is generic independence, not a unit determinant assertion.
        self.assertEqual(ambient_matrix.det().subs(c, 0), 0)
        self.assertNotEqual(bracket(h0, h1), zero)

    def test_actual_transformed_coordinate_frames_have_two_sided_inverses(self):
        frames = (
            ((a + t * c**2, b, c, s), (X - t * Z**2, Y, Z, S),
             (1, 0, 0, 0), (-2 * t * c, 0, 1, 0)),
            ((a, b + t * c**3, c, s), (X, Y - t * Z**3, Z, S),
             (0, 1, 0, 0), (0, -3 * t * c**2, 1, 0)),
        )
        for forward, inverse, fixed_partial, expected in frames:
            to_actual = dict(zip(formal, forward))
            to_formal = dict(zip(variables, inverse))
            for expression, parameter in zip(forward, formal):
                self.assertEqual(compose(expression, to_formal), parameter)
            for variable, expression in zip(variables, inverse):
                self.assertEqual(compose(expression, to_actual), variable)
            derived_partial = tuple(compose(sp.diff(expression, Z), to_actual)
                                    for expression in inverse)
            self.assertEqual(derived_partial, expand_field(expected))
            self.assertEqual(tuple(apply(derived_partial, expression)
                                   for expression in forward), (0, 0, 1, 0))
            self.assertEqual(bracket(E, derived_partial), zero)
            self.assertEqual(bracket(fixed_partial, derived_partial), zero)

    def test_self_generated_saturation_does_not_supply_all_intrinsic_directions(self):
        g = a**2 + b
        h = a * b**3 + 2
        first = expand_field(g * value for value in dc)
        second = expand_field(h * value for value in dc)
        self.assertEqual(bracket(first, second), zero)
        self.assertEqual(apply(first, a), 0)
        self.assertEqual(apply(first, b), 0)
        self.assertEqual(apply(second, a), 0)
        self.assertEqual(apply(second, b), 0)
        forward = (a, b, c + t * g, s)
        inverse = (a, b, c - t * g, s)
        self.assertEqual(conjugate(second, forward, inverse), second)
        self.assertEqual(intrinsic_determinant((first, second, dc)), 0)
        # The full intrinsic group includes the excluded transverse shear.
        transverse_forward = (a + t * c, b, c, s)
        transverse_inverse = (a - t * c, b, c, s)
        transverse = conjugate(dc, transverse_forward, transverse_inverse)
        self.assertEqual(apply(transverse, a), -t)
        self.assertNotEqual(apply(transverse, a).subs(t, 1), 0)

    def test_target_recovery_checks_both_bracket_choices(self):
        target = a
        h0 = dc
        self.assertEqual(apply(h0, target), 0)
        # First case: an ordinary intrinsic conjugation already moves target.
        L = expand_field((c, 0, 1, 0))
        self.assertNotEqual(apply(L, target), 0)
        self.assertEqual(apply(bracket(L, h0), target), -1)
        forward = (a + t * c + t**2 / 2, b, c + t, s)
        inverse = (a - t * c + t**2 / 2, b, c - t, s)
        curve = conjugate(h0, forward, inverse)
        self.assertEqual(apply(curve, target), -t)
        # Second case: ordinary commutation fails to help, but its replica does.
        L = da
        g = c**3
        self.assertEqual(apply(L, target), 1)
        self.assertEqual(apply(L, g), 0)
        self.assertEqual(apply(bracket(L, h0), target), 0)
        replica = expand_field(g * value for value in L)
        self.assertEqual(apply(bracket(replica, h0), target),
                         -apply(h0, g) * apply(L, target))
        replica_curve = conjugate(h0, (a + t * c**3, b, c, s),
                                  (a - t * c**3, b, c, s))
        self.assertEqual(apply(replica_curve, target), -3 * t * c**2)
        self.assertNotEqual(apply(replica_curve, target).subs(t, 1), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
