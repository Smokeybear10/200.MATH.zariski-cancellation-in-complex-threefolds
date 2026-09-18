"""Three finite centralizer controls, not a degree-five residual example."""

import unittest

import sympy as sp


w, u, v, t = sp.symbols("w u v t")
VARIABLES = (w, u, v, t)
X = sp.Matrix(VARIABLES)
D = sp.Matrix([0, 0, w, u])
E0 = sp.Matrix([0, 0, 1, 0])
R = u*v - w*t


def clean(vector):
    return sp.Matrix(vector).applyfunc(sp.expand)


def act(field, value):
    return sp.expand(sum(coefficient*sp.diff(value, variable)
                         for coefficient, variable in zip(field, VARIABLES)))


def bracket(left, right):
    return clean([act(left, right[i]) - act(right, left[i])
                  for i in range(4)])


class NiceCentralizerChecks(unittest.TestCase):
    def assertVectorZero(self, vector):
        self.assertEqual(clean(vector), sp.zeros(*sp.Matrix(vector).shape))

    def test_primitive_gcd_division_and_commutation_hypothesis(self):
        multiplier = w**2 + u**3
        field = multiplier*D
        coefficient_gcd = sp.gcd(field[2], field[3])
        self.assertEqual(sp.expand(coefficient_gcd - multiplier), 0)
        self.assertEqual(sp.gcd(D[2], D[3]), 1)
        self.assertEqual(act(field, multiplier), 0)
        self.assertEqual(act(E0, multiplier), 0)
        self.assertVectorZero(bracket(E0, field))
        self.assertVectorZero(bracket(E0, D))
        self.assertVectorZero([act(field, value) for value in field])
        self.assertVectorZero([act(D, value) for value in D])
        self.assertVectorZero(clean(field/coefficient_gcd) - D)
        # An invariant for D need not be invariant for the commuting E0.
        # Multiplying D by it really destroys E0-commutation.
        other = R*D
        self.assertEqual(act(D, R), 0)
        self.assertEqual(act(E0, R), u)
        self.assertVectorZero([act(other, value) for value in other])
        self.assertVectorZero(bracket(E0, other) - u*D)
        self.assertNotEqual(clean(bracket(E0, other)), sp.zeros(4, 1))

    def test_sliced_ambient_action_has_nonsliced_auxiliary_restriction(self):
        self.assertVectorZero(bracket(E0, D))
        self.assertEqual(act(E0, v), 1)
        self.assertEqual(act(D, R), 0)
        self.assertVectorZero([act(E0, w), act(E0, u), act(E0, R) - u])
        rr = sp.Symbol("rr")
        # The exact induced coefficient vector is (0,0,u), so all images
        # are in (u). These finite polynomials only illustrate that formula.
        for polynomial in (rr, w*rr**2 + u, rr**3 + w*u*rr):
            induced = u*sp.diff(polynomial, rr)
            actual = act(E0, polynomial.subs(rr, R))
            self.assertEqual(sp.expand(actual - induced.subs(rr, R)), 0)
            self.assertEqual(sp.expand(induced.subs(u, 0)), 0)
        self.assertEqual(sp.Integer(1).subs(u, 0), 1)
        self.assertTrue(all(value.subs({w: 0, u: 0}) == 0 for value in D))

    def test_conjugated_slice_and_failure_of_the_supplied_plane(self):
        linear = sp.Matrix([u, 0, t, 0])
        self.assertEqual(act(linear, R), 0)
        self.assertVectorZero(bracket(linear, D))
        forward = sp.Matrix([w + u*R**2, u, v + t*R**2, t])
        inverse = sp.Matrix([w - u*R**2, u, v - t*R**2, t])
        forward_substitution = dict(zip(VARIABLES, forward))
        inverse_substitution = dict(zip(VARIABLES, inverse))
        self.assertEqual(sp.expand(R.subs(forward_substitution,
                                          simultaneous=True) - R), 0)
        self.assertEqual(sp.expand(R.subs(inverse_substitution,
                                          simultaneous=True) - R), 0)
        self.assertVectorZero(inverse.subs(forward_substitution,
                                           simultaneous=True) - X)
        self.assertVectorZero(forward.subs(inverse_substitution,
                                           simultaneous=True) - X)
        conjugated = clean(sp.Matrix([act(E0, value) for value in inverse]).subs(
            forward_substitution, simultaneous=True))
        expected = sp.Matrix([-2*R*u**2, 0, 1 - 2*R*u*t, 0])
        self.assertVectorZero(conjugated - expected)
        self.assertVectorZero(bracket(conjugated, D))
        self.assertEqual(act(conjugated, forward[2]), 1)
        self.assertVectorZero([act(conjugated, coordinate)
                               for coordinate in (u, t, forward[0])])
        self.assertEqual(sp.diff(conjugated[0], v), -2*u**3)
        self.assertNotEqual(sp.diff(conjugated[0], v), 0)
        self.assertVectorZero([act(D, forward[0]), act(D, u)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
