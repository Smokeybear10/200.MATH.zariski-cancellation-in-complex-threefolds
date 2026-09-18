#!/usr/bin/env python3
"""Standalone exact controls for intrinsic-quotient-surface-pass.md.

Uses unittest and SymPy only; imports no research solver or other checker.
Finite identities do not prove the quotient classification, miracle flatness,
or a no-retraction statement in arbitrary degree. The square-degree tests
illustrate the degree argument in the note rather than enumerate all maps.
Freudenburg's rank-three property is sourced, not computed by this script.
"""

import time
import unittest

import sympy as sp


x, y, z, v, t, h = sp.symbols("x y z v t h")
BASE = (x, y, z)
INVARIANT = x * z - y**2


def derivative(expression):
    """The derivation x*d/dy + 2*y*d/dz, also on its x-localization."""
    return sp.cancel(x * sp.diff(expression, y) + 2 * y * sp.diff(expression, z))


def flow(parameter):
    return {x: x, y: y + x * parameter, z: z + 2 * y * parameter + x * parameter**2}


def substitute(expression, values):
    return sp.cancel(sp.sympify(expression).subs(values, simultaneous=True))


def slice_projection(expression, limit=30):
    """Evaluate the finite local-slice Taylor expression, checking termination."""
    current = sp.sympify(expression)
    answer = sp.Integer(0)
    local_slice = y / x
    for exponent in range(limit):
        if current == 0:
            return sp.cancel(answer)
        answer += (-local_slice)**exponent * current / sp.factorial(exponent)
        current = derivative(current)
    raise AssertionError("The finite test did not verify the nilpotence bound")


def univariate_remainder(expression, divisor):
    return sp.rem(sp.expand(expression), sp.expand(divisor), y)


def freudenburg_data():
    """Reconstruct coefficients independently from the recorded f,g formula.

    The rank-three attribution is in the research note/global bridge and in
    Kaliman's survey, Example 10.5(2):
    https://www.math.miami.edu/~kaliman/library/seattle.paper.pdf
    """
    f = x * z - y**2
    g = z * f**2 + 2 * x**2 * y * f + x**5
    r = -x**3 - f * y
    jacobian_coefficients = tuple(
        sp.expand(sp.Matrix([[sp.diff(p, a) for a in BASE] for p in (f, g, c)]).det())
        for c in BASE
    )
    factored_coefficients = (
        2 * f * r,
        -g - 6 * x**2 * r,
        2 * x * f**2 - 10 * x * y * r,
    )
    return f, g, r, jacobian_coefficients, factored_coefficients


class IntrinsicQuotientChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_invariant_and_generator_nilpotence(self):
        self.assert_zero(derivative(x))
        self.assert_zero(derivative(INVARIANT))
        self.assert_zero(derivative(y) - x)
        self.assert_zero(derivative(z) - 2 * y)
        for generator, index in ((x, 1), (y, 2), (z, 3)):
            current = generator
            for _ in range(index - 1):
                current = derivative(current)
            self.assertNotEqual(current, 0)
            self.assert_zero(derivative(current))

    def test_flow_preserves_quotient_and_has_correct_tangent(self):
        self.assert_zero(substitute(INVARIANT, flow(t)) - INVARIANT)
        for coordinate in BASE:
            self.assert_zero(substitute(coordinate, flow(0)) - coordinate)
            tangent = sp.diff(flow(t)[coordinate], t).subs(t, 0)
            self.assert_zero(tangent - derivative(coordinate))

    def test_flow_group_law_and_inverse(self):
        for coordinate in BASE:
            composed = substitute(flow(t)[coordinate], flow(h))
            self.assert_zero(composed - flow(t + h)[coordinate])
            self.assert_zero(substitute(flow(t)[coordinate], flow(-t)) - coordinate)

    def test_localized_coordinate_inverse_and_slice(self):
        # Coordinates (x,v,t) on x != 0, with t = y/x.
        inverse = {x: x, y: x * t, z: v / x + x * t**2}
        forward = {v: INVARIANT, t: y / x}
        self.assert_zero(substitute(INVARIANT, inverse) - v)
        self.assert_zero(substitute(y / x, inverse) - t)
        for coordinate in BASE:
            self.assert_zero(substitute(inverse[coordinate], forward) - coordinate)
        self.assert_zero(derivative(y / x) - 1)
        self.assert_zero(derivative(v / x))

    def test_local_slice_projection_and_its_non_global_pole(self):
        samples = (1, x, y, z, y**3 + x * z, y**2 * z + x**2 * z**3)
        for polynomial in samples:
            projected = slice_projection(polynomial)
            expected = substitute(polynomial, {y: 0, z: INVARIANT / x})
            self.assert_zero(projected - expected)
            self.assert_zero(derivative(projected))
        projected_z = sp.cancel(slice_projection(z))
        self.assert_zero(projected_z - INVARIANT / x)
        self.assertEqual(sp.fraction(projected_z)[1], x)
        self.assertEqual(sp.gcd(sp.fraction(projected_z)[0], x), 1)

    def test_derivative_ideal_and_fixed_locus(self):
        images = [derivative(coordinate) for coordinate in BASE]
        basis = sp.groebner(images, x, y, z)
        self.assertEqual([p.as_expr() for p in basis.polys], [x, y])
        self.assertEqual(sp.gcd_list(images), 1)
        # Gcd one does not mean the derivative ideal is the unit ideal.
        self.assertEqual(basis.reduce(sp.Integer(1))[1], 1)
        for coordinate in BASE:
            displacement = flow(t)[coordinate] - coordinate
            self.assert_zero(substitute(displacement, {x: 0, y: 0}))
        self.assertNotEqual(substitute(flow(t)[y] - y, {x: 1, y: 0, z: 0}), 0)

    def test_nonzero_x_fiber_parametrizations(self):
        for alpha in (-2, 1, 3):
            for beta in (-3, 0, 4):
                with self.subTest(alpha=alpha, beta=beta):
                    inverse_z = (sp.Integer(beta) + y**2) / alpha
                    self.assert_zero(substitute(INVARIANT - beta, {x: alpha, z: inverse_z}))
                    self.assert_zero((beta + y**2) / alpha - inverse_z)
                    # y is retained freely; solving the fiber equation recovers z.
                    relation = alpha * z - y**2 - beta
                    self.assert_zero(inverse_z - z + relation / alpha)

    def test_disconnected_fibers_via_chinese_remainder_idempotents(self):
        # At (x,v)=(0,-a^2), the fiber ring is Q[y,z]/(y^2-a^2).
        for a in (sp.Integer(1), sp.Integer(2), sp.Rational(3, 2)):
            with self.subTest(a=a):
                relation = y**2 - a**2
                plus, minus = (y + a) / (2 * a), (a - y) / (2 * a)
                self.assert_zero(plus + minus - 1)
                for idempotent in (plus, minus):
                    self.assert_zero(univariate_remainder(idempotent**2 - idempotent, relation))
                self.assert_zero(univariate_remainder(plus * minus, relation))
                self.assertEqual((plus.subs(y, a), plus.subs(y, -a)), (1, 0))
                self.assertEqual((minus.subs(y, a), minus.subs(y, -a)), (0, 1))
                self.assertEqual(sp.gcd(y - a, y + a), 1)

    def test_special_fiber_regular_sequence_and_nonzero_nilpotent(self):
        # Modulo x, v becomes a nonzero polynomial in the domain Q[y,z].
        # This is the regular-sequence control; flatness itself is proved in the note.
        self.assertEqual(INVARIANT.subs(x, 0), -y**2)
        self.assertNotEqual(INVARIANT.subs(x, 0), 0)
        special = sp.groebner([x, INVARIANT], x, y, z)
        self.assertEqual([p.as_expr() for p in special.polys], [x, y**2])
        self.assertEqual(special.reduce(y)[1], y)
        self.assertEqual(special.reduce(y**2)[1], 0)
        self.assertEqual(special.reduce(z**5)[1], z**5)
        self.assertEqual(special.reduce(sp.Integer(1))[1], 1)

    def test_retraction_square_degree_obstruction_controls(self):
        # A retraction would give -P(v)^2=v after reduction modulo x.
        # Finite symbolic degrees only: the unbounded degree proof is in the note.
        c = sp.symbols("c0:8")
        for degree in range(8):
            polynomial = sum(c[j] * v**j for j in range(degree + 1))
            square = sp.Poly(polynomial**2, v)
            self.assertEqual(square.degree(), 2 * degree)
            self.assertEqual(square.LC(), c[degree]**2)
            obstruction = sp.Poly(-polynomial**2 - v, v)
            self.assertEqual(obstruction.degree(), 1 if degree == 0 else 2 * degree)
            self.assertFalse(obstruction.is_zero)
            if degree == 0:
                self.assertEqual(obstruction.coeff_monomial(v), -1)
            else:
                self.assertEqual(obstruction.LC(), -c[degree]**2)
        # Odd degree obstructs a polynomial square, but even degree alone is no certificate.
        self.assertEqual(sp.degree(-v, v) % 2, 1)
        self.assertEqual(sp.degree((v + 1)**2, v) % 2, 0)

    def test_freudenburg_coefficient_gcd_one(self):
        f, g, _, jacobian_coefficients, factored_coefficients = freudenburg_data()
        for actual, expected in zip(jacobian_coefficients, factored_coefficients):
            self.assert_zero(actual - expected)
        self.assertEqual(sp.gcd_list(jacobian_coefficients), 1)
        for invariant in (f, g):
            self.assert_zero(sum(c * sp.diff(invariant, a) for c, a in zip(jacobian_coefficients, BASE)))
        # No assertion about derivation rank is computed here.

    def test_freudenburg_fixed_origin_despite_coefficient_gcd_one(self):
        _, _, _, coefficients, _ = freudenburg_data()
        for coefficient in coefficients:
            self.assert_zero(substitute(coefficient, {x: 0, y: 0, z: 0}))
        self.assertTrue(any(coefficient != 0 for coefficient in coefficients))
        # Evaluation at the origin proves the coefficient ideal is proper.
        self.assertEqual(sp.gcd_list(coefficients), 1)


if __name__ == "__main__":
    started = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(IntrinsicQuotientChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"Exact quotient controls: {result.testsRun} tests in {time.perf_counter() - started:.3f}s")
    raise SystemExit(not result.wasSuccessful())
