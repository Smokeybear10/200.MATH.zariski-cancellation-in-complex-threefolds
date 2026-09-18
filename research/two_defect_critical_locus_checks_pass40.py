"""Independent finite controls, not a classification of all two-defect actions."""

import unittest

import sympy as sp


u, v, a, c = sp.symbols("u v a c")
b, d, r, s = sp.symbols("b d r s")
OLD = (u, v, a, c)
PHYSICAL = (b, d, a, c)
FORWARD = (u + a**2 / 2, v + c**2 / 2, a, c)
INVERSE = (b - a**2 / 2, d - c**2 / 2, a, c)


def clean(vector):
    return sp.Matrix([sp.expand(value) for value in vector])


def act(field, polynomial):
    return sp.expand(sum(coefficient * sp.diff(polynomial, variable)
                         for coefficient, variable in zip(field, OLD)))


def bracket(left, right):
    return clean([act(left, right[i]) - act(right, left[i])
                  for i in range(4)])


def ad_power(left, right, order):
    result = sp.Matrix(right)
    for _ in range(order):
        result = bracket(left, result)
    return result


def actual_partials():
    inverse_jacobian = sp.Matrix(INVERSE).jacobian(PHYSICAL)
    substituted = inverse_jacobian.subs(
        dict(zip(PHYSICAL, FORWARD)), simultaneous=True)
    return [clean(substituted[:, i]) for i in range(4)]


def degree_or_minus_infinity(polynomial):
    polynomial = sp.expand(polynomial)
    return -sp.oo if polynomial == 0 else int(sp.degree(polynomial, s))


def isolated_data():
    f = u**2 + v**2
    return f, u*f - 1, u, sp.Integer(-1)


def repeated_data(polynomial):
    return polynomial, v*polynomial - 1, v, sp.Integer(-1)


class TwoDefectCriticalLocusChecks(unittest.TestCase):
    def assertVectorZero(self, vector):
        self.assertTrue(all(sp.expand(value) == 0 for value in vector))

    def test_supplied_bezout_and_both_actual_coordinate_inverses(self):
        self.assertVectorZero(sp.Matrix(INVERSE).subs(
            dict(zip(PHYSICAL, FORWARD)), simultaneous=True) - sp.Matrix(OLD))
        self.assertVectorZero(sp.Matrix(FORWARD).subs(
            dict(zip(OLD, INVERSE)), simultaneous=True) - sp.Matrix(PHYSICAL))
        for f, g, alpha, beta in (
                isolated_data(), repeated_data(u**3 - u)):
            with self.subTest(f=f):
                self.assertEqual(sp.expand(alpha*f + beta*g), 1)
                invariant = g*a - f*c
                slice_value = alpha*a + beta*c
                new = (u, v, invariant, slice_value)
                inverse = (u, v, f*s + beta*r, g*s - alpha*r)
                self.assertVectorZero(sp.Matrix(inverse).subs(
                    {r: invariant, s: slice_value}, simultaneous=True)
                    - sp.Matrix(OLD))
                self.assertVectorZero(sp.Matrix(new).subs(
                    {a: inverse[2], c: inverse[3]}, simultaneous=True)
                    - sp.Matrix([u, v, r, s]))
                action = sp.Matrix([0, 0, f, g])
                self.assertEqual(act(action, invariant), 0)
                self.assertEqual(act(action, slice_value), 1)

    def test_actual_brackets_both_exact_profiles_and_defect_ranks(self):
        partials = actual_partials()
        for f, g, alpha, beta in (
                isolated_data(), repeated_data(u**2)):
            action = sp.Matrix([0, 0, f, g])
            au = sp.Matrix([0, 0, sp.diff(f, u), sp.diff(g, u)])
            av = sp.Matrix([0, 0, sp.diff(f, v), sp.diff(g, v)])
            expected = (-au, -av, 2*f*au, 2*g*av)
            invariant = g*a - f*c
            slice_value = alpha*a + beta*c
            inverse_substitution = {a: f*s + beta*r, c: g*s - alpha*r}
            shifts = []
            for partial, height, highest in zip(
                    partials, (1, 1, 2, 2), expected):
                self.assertVectorZero(ad_power(action, partial, height) - highest)
                self.assertTrue(any(value != 0 for value in clean(highest)))
                self.assertVectorZero(ad_power(action, partial, height + 1))
                coefficients = [act(partial, coordinate).subs(
                    inverse_substitution, simultaneous=True)
                    for coordinate in (u, v, invariant, slice_value)]
                degrees = [degree_or_minus_infinity(value)
                           for value in coefficients]
                shifts.append(max(degrees[:3] + [degrees[3] - 1]))
            self.assertEqual(shifts, [1, 1, 2, 2])
            self.assertEqual(sum(value + 1 for value in shifts), 10)
            defects = sp.Matrix.hstack(expected[2], expected[3])
            determinant = sp.Matrix([f, g]).jacobian((u, v)).det()
            self.assertNotEqual(sp.expand(determinant), 0)
            self.assertEqual(sp.expand(defects[2:4, :].det()
                                       - 4*f*g*determinant), 0)
            leading = sp.Matrix([act(action, act(action, coordinate))
                                 for coordinate in FORWARD])
            self.assertVectorZero(leading - sp.Matrix([f**2, g**2, 0, 0]))
            self.assertVectorZero([act(action, value) for value in leading])
            self.assertEqual(sp.expand(
                leading[:2, :].jacobian((u, v)).det()
                - 4*f*g*determinant), 0)

    def test_full_intrinsic_restriction_ideal_and_signs(self):
        f, g, _, _ = isolated_data()
        action = sp.Matrix([0, 0, f, g])
        partials = actual_partials()
        highest = [ad_power(action, partial, height)
                   for partial, height in zip(partials, (1, 1, 2, 2))]
        invariant = g*a - f*c
        delta_u = sp.expand(f*sp.diff(g, u) - g*sp.diff(f, u))
        delta_v = sp.expand(f*sp.diff(g, v) - g*sp.diff(f, v))
        actual_coefficients = [act(field, invariant) for field in highest]
        self.assertVectorZero(sp.Matrix(actual_coefficients)
                              - sp.Matrix([delta_u, delta_v,
                                           -2*f*delta_u, -2*g*delta_v]))
        for field in highest:
            self.assertEqual(act(field, u), 0)
            self.assertEqual(act(field, v), 0)
            self.assertVectorZero(bracket(action, field))
        complete = sp.groebner(actual_coefficients, u, v, domain=sp.QQ)
        first_two = sp.groebner(actual_coefficients[:2], u, v, domain=sp.QQ)
        self.assertEqual([p.as_expr() for p in complete.polys],
                         [p.as_expr() for p in first_two.polys])

    def test_gcd_one_nonunit_ideal_has_exactly_four_reduced_points(self):
        f, g, _, _ = isolated_data()
        generators = [sp.expand(f*sp.diff(g, variable)
                                - g*sp.diff(f, variable))
                      for variable in (u, v)]
        self.assertVectorZero(sp.Matrix(generators)
                              - sp.Matrix([f**2 + 2*u, 2*v]))
        self.assertEqual(sp.gcd(*generators), 1)
        self.assertTrue(all(value.subs({u: 0, v: 0}) == 0
                            for value in generators))
        basis = sp.groebner(generators, u, v, domain=sp.QQ)
        polynomial = u**4 + 2*u
        self.assertEqual([p.as_expr() for p in basis.polys], [polynomial, v])
        # The quotient is C[u]/(polynomial): length four, and squarefree.
        self.assertEqual(sp.degree(polynomial, u), 4)
        self.assertEqual(sp.gcd(polynomial, sp.diff(polynomial, u)), 1)
        self.assertEqual(sp.diff(polynomial, u).subs(u, 0), 2)
        self.assertEqual(sp.rem(sp.diff(polynomial, u), u**3 + 2, u), -6)
        self.assertEqual(basis.reduce(sp.Integer(1))[1], 1)

    def test_every_root_multiplicity_in_the_univariate_family(self):
        polynomials = [u*(u - 1)*(u + 2),
                       (u - 1)**4*(u + 2)**2*(u - 3)]
        expected_gcds = [sp.Integer(1), (u - 1)**3*(u + 2)]
        for polynomial, expected in zip(polynomials, expected_gcds):
            f, g, _, _ = repeated_data(polynomial)
            delta_u = sp.expand(f*sp.diff(g, u) - g*sp.diff(f, u))
            delta_v = sp.expand(f*sp.diff(g, v) - g*sp.diff(f, v))
            self.assertEqual(sp.expand(delta_u - sp.diff(polynomial, u)), 0)
            self.assertEqual(sp.expand(delta_v - polynomial**2), 0)
            monic = sp.Poly(sp.gcd(delta_u, delta_v), u).monic().as_expr()
            self.assertEqual(sp.expand(monic - expected), 0)
        for exponent in range(2, 6):
            polynomial = u**exponent
            monic = sp.Poly(sp.gcd(sp.diff(polynomial, u), polynomial**2),
                            u).monic().as_expr()
            self.assertEqual(monic, u**(exponent - 1))

    def test_actual_top_field_is_nonnilpotent_despite_unit_ideal(self):
        partials = actual_partials()
        for exponent in (2, 3):
            f, g, _, _ = repeated_data(u**exponent)
            action = sp.Matrix([0, 0, f, g])
            leading = [act(action, act(action, coordinate))
                       for coordinate in FORWARD]
            top_field = clean(sum((coefficient*partial for coefficient, partial
                                   in zip(leading, partials)), sp.zeros(4, 1)))
            self.assertEqual(act(top_field, u), u**(2*exponent))
            iterate = u
            coefficient = sp.Integer(1)
            for order in range(1, 6):
                iterate = act(top_field, iterate)
                coefficient *= 1 + (order - 1)*(2*exponent - 1)
                self.assertEqual(sp.expand(iterate - coefficient
                    * u**(1 + order*(2*exponent - 1))), 0)
                self.assertNotEqual(iterate, 0)
            self.assertEqual(sp.expand(
                f**2*v**2*(1 - 2*g) + g**2*(3 + 2*g)), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
