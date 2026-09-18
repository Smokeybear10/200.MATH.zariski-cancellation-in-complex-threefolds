"""Finite exact controls; no project solver or proof-module imports."""

import unittest

import sympy as sp


a, b, c, s, t, u = sp.symbols("a b c s t u")
X, Y, B, C = sp.symbols("X Y B C")
OLD = (a, b, c, s)
NEW = (X, Y, B, C)
E = sp.Matrix([0, 0, 0, 1])


def expand_vector(vector):
    return sp.Matrix([sp.expand(value) for value in vector])


def act(vector, expression):
    return sp.expand(sum(vector[i] * sp.diff(expression, OLD[i])
                         for i in range(4)))


def bracket(left, right):
    return sp.Matrix([act(left, value) - act(right, left[i])
                      for i, value in enumerate(right)])


def ad_power(left, right, order):
    result = sp.Matrix(right)
    for _ in range(order):
        result = expand_vector(bracket(left, result))
    return result


def coefficient_list(vectors):
    result = []
    for vector in vectors:
        for expression in vector:
            result.extend(sp.Poly(sp.expand(expression), *OLD).coeffs())
    return [sp.expand(value) for value in result if value != 0]


def success_gcd(fields, profile):
    coeffs = coefficient_list(
        [ad_power(E, field, bound + 1)
         for field, bound in zip(fields, profile)])
    result = sp.Poly(0, t, domain=sp.QQ)
    for coefficient in coeffs:
        result = sp.gcd(result, sp.Poly(coefficient, t, domain=sp.QQ))
    return result.monic().as_expr() if result else sp.Integer(0)


def height(field):
    return max(int(sp.degree(value, s)) for value in field if value != 0)


def partials_from_inverse(forward, inverse):
    # Differentiate the supplied inverse, not a guessed inverse Jacobian.
    matrix = sp.Matrix(inverse).jacobian(NEW)
    matrix = matrix.subs(dict(zip(NEW, forward)), simultaneous=True)
    return [expand_vector(matrix[:, i]) for i in range(4)]


def model(n, m):
    x = a + s**n
    y = s + x**m
    forward = (x, y, b, c)
    ss = Y - X**m
    inverse = (X - ss**n, B, C, ss)
    return forward, inverse


def conjugate(field, images, inverse):
    values = [act(field, value) for value in inverse]
    return expand_vector(sp.Matrix(values).subs(
        dict(zip(OLD, images)), simultaneous=True))


class CoordinateReductionChecks(unittest.TestCase):
    def assertVectorZero(self, vector):
        self.assertTrue(all(sp.expand(value) == 0 for value in vector))

    def assertInverse(self, forward, inverse):
        self.assertVectorZero(sp.Matrix(inverse).subs(
            dict(zip(NEW, forward)), simultaneous=True) - sp.Matrix(OLD))
        self.assertVectorZero(sp.Matrix(forward).subs(
            dict(zip(OLD, inverse)), simultaneous=True) - sp.Matrix(NEW))

    def test_actual_two_shear_inverses(self):
        for n, m in ((2, 2), (3, 2), (2, 3)):
            with self.subTest(n=n, m=m):
                forward, inverse = model(n, m)
                self.assertInverse(forward, inverse)
                slice_expression = Y - X**m
                self.assertEqual(
                    sp.expand(slice_expression.subs(
                        dict(zip(NEW, forward)), simultaneous=True)), s)

    def test_partial_pairings_and_exact_initial_heights(self):
        for n, m in ((2, 2), (3, 2), (2, 3)):
            forward, inverse = model(n, m)
            fields = partials_from_inverse(forward, inverse)
            ty = sp.Matrix([-n * s**(n - 1), 0, 0, 1])
            tx = sp.Matrix([1, 0, 0, 0]) - m * forward[0]**(m - 1) * ty
            self.assertVectorZero(fields[0] - tx)
            self.assertVectorZero(fields[1] - ty)
            for i in range(4):
                for j in range(4):
                    self.assertEqual(act(fields[i], forward[j]),
                                     sp.Integer(i == j))
            expected = (n*m - 1, n - 1, 0, 0)
            self.assertEqual(tuple(map(height, fields)), expected)
            for field, bound in zip(fields, expected):
                self.assertVectorZero(ad_power(E, field, bound + 1))
                self.assertTrue(any(value != 0 for value in
                                    ad_power(E, field, bound)))

    def test_wrong_shear_direction_all_coefficient_controls(self):
        n, m = 2, 2
        forward, inverse = model(n, m)
        fields = partials_from_inverse(forward, inverse)
        z = sp.Symbol("z")
        for polynomial in (3, z + 2, z**2 - 3*z + 1,
                           2*z**3 + z**2 - 5):
            polynomial = sp.sympify(polynomial)
            derivative = sp.diff(polynomial, z).subs(z, forward[1])
            candidate = fields[1] - derivative * fields[0]
            degree = sp.degree(polynomial, z)
            expected = n - 1 if degree == 0 else n*m*int(degree) - 1
            self.assertEqual(height(expand_vector(candidate)), expected)
            changed = (forward[0] + polynomial.subs(z, forward[1]),
                       forward[1], b, c)
            xx = X - polynomial.subs(z, Y)
            ss = Y - xx**m
            changed_inverse = (xx - ss**n, B, C, ss)
            self.assertInverse(changed, changed_inverse)
            actual = partials_from_inverse(changed, changed_inverse)
            self.assertVectorZero(actual[0] - fields[0])
            self.assertVectorZero(actual[1] - candidate)
        flow = [fields[0], fields[1] - t * fields[0],
                fields[2], fields[3]]
        self.assertEqual(success_gcd(flow, (3, 1, 0, 0)), t)
        self.assertEqual(success_gcd(flow, (0, 1, 0, 0)), 1)

    def test_transverse_flow_exact_exception_and_final_inverse(self):
        n, m = 3, 2
        forward, _ = model(n, m)
        changed = (forward[0], forward[1] - t*forward[0]**m, b, c)
        ss = Y - (1-t)*X**m
        inverse = (X - ss**n, B, C, ss)
        self.assertInverse(changed, inverse)
        fields = partials_from_inverse(changed, inverse)
        self.assertEqual(success_gcd(fields, (0, 2, 0, 0)), t - 1)
        self.assertEqual(success_gcd(fields, (5, 2, 0, 0)), 0)
        self.assertEqual(tuple(height(field.subs(t, 1))
                               for field in fields), (0, 2, 0, 0))
        for parameter in (0, 2, sp.Rational(1, 3)):
            self.assertEqual(tuple(height(field.subs(t, parameter))
                                   for field in fields), (5, 2, 0, 0))
        at_one = [sp.expand(value.subs(t, 1)) for value in changed]
        final = (sp.expand(at_one[0] - at_one[1]**n),
                 at_one[1], b, c)
        self.assertEqual(final, (a, s, b, c))
        self.assertInverse(final, (X, B, C, Y))

    def test_two_parameter_success_need_not_be_finite(self):
        forward, _ = model(2, 2)
        changed = (forward[0], forward[1] - t*u*forward[0]**2, b, c)
        ss = Y - (1-t*u)*X**2
        inverse = (X - ss**2, B, C, ss)
        self.assertInverse(changed, inverse)
        fields = partials_from_inverse(changed, inverse)
        coeffs = coefficient_list([
            ad_power(E, fields[0], 1),
            ad_power(E, fields[1], 2)])
        basis = sp.groebner(coeffs, t, u, domain=sp.QQ)
        self.assertEqual([poly.as_expr() for poly in basis.polys],
                         [t*u - 1])
        for parameter in (1, 2, 3):
            specialized = [field.subs(
                {t: parameter, u: sp.Rational(1, parameter)})
                for field in fields]
            self.assertEqual(tuple(map(height, specialized)), (0, 1, 0, 0))

    def test_complete_bounded_linear_ansatz(self):
        forward, inverse = model(2, 2)
        fields = partials_from_inverse(forward, inverse)
        c0, c1, c2 = sp.symbols("c0 c1 c2")
        derivative = c1 + 2*c2*forward[0]
        candidate = fields[0] - derivative*fields[1]
        equations = coefficient_list([ad_power(E, candidate, 1)])
        self.assertEqual(sp.linsolve(equations, (c0, c1, c2)),
                         sp.FiniteSet((c0, 0, -1)))
        lower_bound = [value.subs(c2, 0) for value in equations]
        self.assertEqual(sp.linsolve(lower_bound, (c0, c1)),
                         sp.EmptySet)
        repaired = expand_vector(candidate.subs({c1: 0, c2: -1}))
        self.assertEqual(repaired, sp.Matrix([1, 0, 0, 0]))

    def test_iterated_bracket_product_rule(self):
        derivation = sp.Matrix([0, a**2, b, 1])
        field = sp.Matrix([1, a*b, s**2, a*c])
        multiplier = s**2 + a*c
        for order in range(1, 5):
            expected = sp.zeros(4, 1)
            e_power = multiplier
            for j in range(order + 1):
                if j:
                    e_power = act(derivation, e_power)
                expected += sp.binomial(order, j)*e_power*ad_power(
                    derivation, field, order - j)
            actual = ad_power(derivation, multiplier*field, order)
            self.assertVectorZero(actual - expected)

    def test_setwise_kernel_normalizer_preserves_heights(self):
        images = (a+b**2, b, c+a*b, 2*s+a**2)
        inverse = (a-b**2, b, c-(a-b**2)*b,
                   (s-(a-b**2)**2)/2)
        self.assertVectorZero(sp.Matrix(inverse).subs(
            dict(zip(OLD, images)), simultaneous=True) - sp.Matrix(OLD))
        self.assertVectorZero(sp.Matrix(images).subs(
            dict(zip(OLD, inverse)), simultaneous=True) - sp.Matrix(OLD))
        self.assertVectorZero(conjugate(E, images, inverse) - E/2)
        forward, original_inverse = model(2, 2)
        fields = partials_from_inverse(forward, original_inverse)
        for field in fields:
            transported = conjugate(field, images, inverse)
            self.assertEqual(height(transported), height(field))
            for order in range(5):
                self.assertVectorZero(
                    ad_power(E, transported, order)
                    - 2**order*conjugate(
                        ad_power(E, field, order), images, inverse))


if __name__ == "__main__":
    unittest.main(verbosity=2)
