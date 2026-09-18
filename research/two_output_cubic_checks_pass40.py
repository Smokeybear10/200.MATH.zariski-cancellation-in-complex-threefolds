"""Four finite controls, not a constructed degree-five residual action."""

import unittest

import sympy as sp


def clean(vector):
    return sp.Matrix(vector).applyfunc(lambda value: sp.cancel(sp.expand(value)))


def act(field, polynomial, variables):
    return sp.cancel(sp.expand(sum(coefficient*sp.diff(polynomial, variable)
                                   for coefficient, variable in zip(field, variables))))


def bracket(left, right, variables):
    return clean([act(left, right[i], variables) - act(right, left[i], variables)
                  for i in range(len(variables))])


class TwoOutputCubicChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(sp.cancel(sp.expand(value)), 0)

    def test_actual_localized_flow_and_the_missing_unit_contrast(self):
        u, v, a, b, time = sp.symbols("u v a b time")
        variables = (u, v, a, b)
        x = sp.Matrix(variables)
        fraction = (v + 1)/u**2
        field = sp.Matrix([0, 0, fraction, 1])
        forward = x + time*field
        inverse = x - time*field
        self.assertZero(forward.jacobian(variables).det() - 1)
        self.assertZero(field.jacobian(variables)*field)
        self.assertZero(act(field, u, variables))
        self.assertZero(inverse.subs(dict(zip(variables, forward)),
                                    simultaneous=True) - x)
        self.assertZero(forward.subs(dict(zip(variables, inverse)),
                                    simultaneous=True) - x)
        self.assertZero(sp.diff(fraction, a))
        self.assertZero(sp.diff(fraction, b))
        # This rational nice field does not act locally nilpotently on B_b.
        bad = sp.Matrix([0, 0, a/b, 1])
        self.assertZero(bad.jacobian(variables)*bad)
        self.assertZero((x + time*bad).jacobian(variables).det()
                        - (1 + time/b))
        self.assertNotEqual(sp.diff(1 + time/b, time), 0)
        iterate = 1/b
        for order in range(1, 5):
            iterate = act(bad, iterate, variables)
            self.assertZero(iterate - (-1)**order*sp.factorial(order)
                            / b**(order + 1))
            self.assertNotEqual(iterate, 0)
        self.assertEqual(sp.degree(sp.denom(1/(b + time)), time), 1)

    def test_actual_nonunit_kernel_restriction_and_double_bracket(self):
        u, v, a, b, j = sp.symbols("u v a b j")
        variables = (u, v, a, b)
        invariant = u*a - v*b
        nice = sp.Matrix([0, 0, v, u])
        partial = sp.Matrix([0, 0, 1, 0])
        action = sp.Matrix([0, u**2*invariant, 1 + u*b*invariant, 0])
        self.assertEqual(sp.gcd(u, v), 1)
        self.assertTrue(all(value.subs({u: 0, v: 0}) == 0 for value in nice))
        self.assertZero(act(nice, invariant, variables))
        self.assertZero(bracket(action, nice, variables))
        self.assertZero(act(action, a - b*invariant**2/2, variables) - 1)
        self.assertZero(act(action, u, variables))
        self.assertZero(act(action, invariant, variables) - u)
        self.assertZero(act(partial, invariant, variables) - u)
        self.assertZero(bracket(action, bracket(action, partial, variables), variables))
        self.assertZero(invariant.subs(a, (j + v*b)/u) - j)
        self.assertZero(((j + v*b)/u).subs(j, invariant) - a)
        # The section modulo u has J=-v*b, a nonconstant polynomial in b.
        self.assertEqual(invariant.subs(u, 0), -v*b)
        residue_polynomial = 2 + 3*j + j**2
        self.assertEqual(sp.degree(residue_polynomial.subs(j, -v*b), b), 2)
        quotient_variables = (u, v, j)
        restricted = sp.Matrix([0, u**2*j, u])
        pj = sp.Matrix([0, 0, 1])
        first = bracket(restricted, pj, quotient_variables)
        self.assertZero(bracket(restricted, first, quotient_variables))
        self.assertZero(bracket(restricted, u*pj, quotient_variables) - u*first)
        self.assertZero(bracket(restricted, bracket(restricted, u*pj,
                                                    quotient_variables),
                                quotient_variables))

    def test_both_cases_of_the_three_variable_single_partial_split(self):
        u, v, j = sp.symbols("u v j")
        variables = (u, v, j)
        pj = sp.Matrix([0, 0, 1])
        independent = sp.Matrix([0, u**2*j, u])
        commutator = bracket(independent, pj, variables)
        self.assertZero(commutator - sp.Matrix([0, -u**2, 0]))
        self.assertZero(bracket(independent, commutator, variables))
        self.assertZero(sp.Matrix.hstack(independent, commutator)[1:3, :].det()
                        - u**3)
        self.assertNotEqual(u**3, 0)
        self.assertZero(act(independent, u, variables))
        self.assertZero(act(commutator, u, variables))
        primitive = sp.Matrix([0, u, 1])
        multiplier = v - u*j
        dependent = multiplier*primitive
        dependent_commutator = bracket(dependent, pj, variables)
        self.assertZero(dependent_commutator - u*primitive)
        self.assertZero(bracket(dependent, dependent_commutator, variables))
        self.assertZero(act(primitive, multiplier, variables))
        gcd = sp.gcd(dependent[1], dependent[2])
        divided = clean(dependent/gcd)
        # A gcd is only determined up to a nonzero constant.
        self.assertZero(divided - divided[2]*primitive)
        self.assertNotEqual(divided[2], 0)
        self.assertTrue(all(sp.diff(value, j) == 0 for value in divided))
        self.assertZero(act(dependent, u, variables))
        self.assertZero(act(divided, u, variables))

    def test_explicit_stable_plane_coordinate_and_unit_section_inverses(self):
        u, v, j, z, y, q = sp.symbols("u v j z y q")
        variables = (u, v, j)
        target = sp.Matrix([z, y, q])
        plane_coordinate = u + v**2
        forward = sp.Matrix([plane_coordinate, v + plane_coordinate*j, j])
        inverse = sp.Matrix([z - (y-z*q)**2, y-z*q, q])
        self.assertZero(forward.subs(dict(zip(variables, inverse)),
                                     simultaneous=True) - target)
        self.assertZero(inverse.subs(dict(zip((z, y, q), forward)),
                                     simultaneous=True) - sp.Matrix(variables))
        # This is an explicit illustration, not a machine proof of Hamann.
        self.assertZero((u + v**2).subs(u, z-v**2) - z)
        self.assertZero((z-v**2).subs(z, plane_coordinate) - u)
        self.assertEqual(sp.degree(plane_coordinate, j), 0)
        self.assertEqual(sp.degree((plane_coordinate + j)**3
                                   + plane_coordinate + j, j), 3)
        a, b = sp.symbols("a b")
        coefficient = u**2 + v
        section = a - coefficient*b
        self.assertZero(section.subs(a, j + coefficient*b) - j)
        self.assertZero((j + coefficient*b).subs(j, section) - a)


if __name__ == "__main__":
    unittest.main(verbosity=2)
