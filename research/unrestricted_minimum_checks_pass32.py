"""Exact controls for the actual nonsliced degree-minimizer counterexample.

Only unittest and SymPy are used. The written polynomial-divisibility
and determinant proof establishes the global inverse; no numerical
sampling or unverified Jacobian-conjecture inference is used here.
"""

import unittest

import sympy as sp


x, lam, b, c, w, z, alpha, h = sp.symbols("x lam b c w z alpha h")
Q = sp.Rational(2, 3)
v = 1 + lam * x
u = 1 + Q * lam * x
P = (1 - Q * lam * x) * (1 + Q**2 * lam**2 * x**2)
e = Q**4 * lam**3 * x**2
H0 = x**2 * c - b**2
W = sp.expand(P * b + e * H0)
H = sp.expand(u * H0 - lam * x**2 * b)
I = x**2 * z - v**2 * w**2
Binv = sp.expand(u * w - e * I)
H0inv = sp.expand(lam * x**2 * w + P * I)


def polynomial_quotient(numerator):
    quotient, remainder = sp.div(sp.expand(numerator), x**2, x)
    if sp.expand(remainder) != 0:
        raise ValueError("The asserted global polynomial quotient has a remainder")
    return sp.expand(quotient)


Z = polynomial_quotient(H + v**2 * W**2)
Cinv = polynomial_quotient(H0inv + Binv**2)


def zero(expr):
    return sp.expand(expr) == 0


def sub(expr, mapping):
    return sp.expand(expr.subs(mapping, simultaneous=True))


def physical_vertical(expr):
    return sp.expand(x**2 * sp.diff(expr, w)
                     + 2 * v**2 * w * sp.diff(expr, z))


def target_vertical(expr):
    return sp.expand(u * x**2 * sp.diff(expr, b)
                     + (2 * u * b + lam * x**2) * sp.diff(expr, c))


T = Q * x * (1 - Q * lam * x + Q**2 * lam**2 * x**2)
K = 3 - 2 * Q * lam * x + Q**2 * lam**2 * x**2
U = Q**4 * lam**2 * x**2 * K
E = (1 - Q) + (Q**2 - Q) * lam * x + Q**2 * lam**2 * x**2
horizontal_w = sp.expand(-T * w + U * I)
horizontal_z = sp.expand(
    -w + T * z - 2 * lam * v * E * w**2
    + 2 * Q**4 * lam**2 * v**2 * K * w * I
)


def physical_horizontal(expr):
    return sp.expand(sp.diff(expr, lam)
                     + horizontal_w * sp.diff(expr, w)
                     + horizontal_z * sp.diff(expr, z))


def primitive_top(expr):
    return sp.expand(x**2 * sp.diff(expr, b)
                     + (2 * b + sp.Rational(3, 2) * x) * sp.diff(expr, c))


class UnrestrictedMinimumChecks(unittest.TestCase):
    def test_formal_determinant_and_inverse_matrix(self):
        formal_u = 1 + alpha * lam * x
        formal_P = ((1 - alpha * lam * x)
                    * (1 + alpha**2 * lam**2 * x**2))
        formal_e = alpha**4 * lam**3 * x**2
        matrix = sp.Matrix([[formal_P, formal_e],
                            [-lam * x**2, formal_u]])
        inverse = sp.Matrix([[formal_u, -formal_e],
                             [lam * x**2, formal_P]])
        self.assertTrue(zero(matrix.det() - 1))
        self.assertEqual((matrix * inverse).applyfunc(sp.expand), sp.eye(2))
        self.assertEqual((inverse * matrix).applyfunc(sp.expand), sp.eye(2))

    def test_both_remainders_force_the_exact_parameter(self):
        formal_u = 1 + alpha * lam * x
        formal_P = ((1 - alpha * lam * x)
                    * (1 + alpha**2 * lam**2 * x**2))
        formal_e = alpha**4 * lam**3 * x**2
        formal_W = formal_P * b + formal_e * H0
        formal_H = formal_u * H0 - lam * x**2 * b
        forward_rem = sp.rem(sp.expand(formal_H + v**2 * formal_W**2),
                             x**2, x)
        inverse_rem = sp.rem(sp.expand(
            lam * x**2 * w + formal_P * I
            + (formal_u * w - formal_e * I)**2), x**2, x)
        self.assertTrue(zero(forward_rem - (2 - 3 * alpha) * lam * x * b**2))
        self.assertTrue(zero(inverse_rem - (3 * alpha - 2) * lam * x * w**2))
        self.assertEqual(sp.solve(sp.Poly(forward_rem, x, lam, b).coeffs(),
                                  alpha), {alpha: Q})
        for rejected in (sp.Integer(0), sp.Integer(1), sp.Rational(1, 2)):
            self.assertNotEqual(forward_rem.subs(alpha, rejected), 0)
            self.assertNotEqual(inverse_rem.subs(alpha, rejected), 0)

    def test_global_polynomiality_and_normalization(self):
        for polynomial in (W, H, Z):
            self.assertEqual(sp.Poly(polynomial, x, lam, b, c, domain=sp.QQ)
                             .as_expr(), polynomial)
        for polynomial in (Binv, Cinv):
            self.assertEqual(sp.Poly(polynomial, x, lam, w, z, domain=sp.QQ)
                             .as_expr(), polynomial)
        self.assertTrue(zero(x**2 * Z - H - v**2 * W**2))
        self.assertTrue(zero(x**2 * Cinv - H0inv - Binv**2))
        self.assertEqual(W.subs(lam, 0), b)
        self.assertEqual(Z.subs(lam, 0), c)
        self.assertEqual(Binv.subs(lam, 0), w)
        self.assertEqual(Cinv.subs(lam, 0), z)

    def test_actual_full_inverse_compositions(self):
        to_physical = {b: Binv, c: Cinv}
        to_target = {w: W, z: Z}
        self.assertTrue(zero(sub(W, to_physical) - w))
        self.assertTrue(zero(sub(Z, to_physical) - z))
        self.assertTrue(zero(sub(Binv, to_target) - b))
        self.assertTrue(zero(sub(Cinv, to_target) - c))
        self.assertTrue(zero(sub(I, to_target) - H))

    def test_actual_canonical_action_intertwining(self):
        self.assertTrue(zero(target_vertical(W) - x**2))
        self.assertTrue(zero(target_vertical(H)))
        self.assertTrue(zero(target_vertical(Z) - 2 * v**2 * W))
        self.assertTrue(zero(target_vertical(H0) - lam * x**4))
        self.assertTrue(zero(target_vertical(target_vertical(b))))
        self.assertTrue(zero(target_vertical(target_vertical(target_vertical(c)))))
        self.assertTrue(zero(sub(physical_vertical(Binv), {w: W, z: Z})
                                   - u * x**2))
        self.assertTrue(zero(sub(physical_vertical(Cinv), {w: W, z: Z})
                                   - 2 * u * b - lam * x**2))

    def test_actual_horizontal_and_failure_of_triangular_preservation(self):
        self.assertEqual(physical_horizontal(x), 0)
        self.assertEqual(physical_horizontal(lam), 1)
        self.assertTrue(zero(physical_horizontal(Binv)))
        self.assertTrue(zero(physical_horizontal(Cinv)))
        self.assertTrue(zero(sub(horizontal_w, {w: W, z: Z})
                                   - sp.diff(W, lam)))
        self.assertTrue(zero(sub(horizontal_z, {w: W, z: Z})
                                   - sp.diff(Z, lam)))
        self.assertTrue(zero(physical_horizontal(I) + x**2 * w - T * I))
        self.assertTrue(zero(sp.diff(horizontal_w, z) - U * x**2))
        self.assertNotEqual(sp.diff(horizontal_w, z), 0)
        self.assertEqual(horizontal_w.subs(x, 0), 0)

    def test_actual_relative_degree_and_first_adjoint(self):
        target_values = (target_vertical(b), target_vertical(c))
        self.assertEqual(max(sp.Poly(value, lam).degree()
                             for value in target_values), 1)
        expected = (Q * x**3, sp.Rational(4, 3) * x * b + x**2)
        self.assertEqual(tuple(sp.expand(value).coeff(lam, 1)
                               for value in target_values), expected)
        for coordinate in (w, z):
            actual_bracket = sp.expand(
                physical_horizontal(physical_vertical(coordinate))
                - physical_vertical(physical_horizontal(coordinate)))
            coordinate_in_target = W if coordinate == w else Z
            top_on_coordinate = sp.expand(Q * x * primitive_top(coordinate_in_target))
            self.assertTrue(zero(sub(actual_bracket, {w: W, z: Z})
                                       - top_on_coordinate))
        # The pulled-back commutator is independent of lambda as a
        # coefficient field, so the second adjoint vanishes on b,c.
        self.assertEqual(tuple(sp.diff(value, lam) for value in expected), (0, 0))

    def test_primitive_top_shift_and_actual_fixed_line(self):
        top_values = (Q * x**3, sp.Rational(4, 3) * x * b + x**2)
        self.assertEqual(sp.gcd(*top_values), x)
        self.assertTrue(zero(top_values[0] - Q * x * primitive_top(b)))
        self.assertTrue(zero(top_values[1] - Q * x * primitive_top(c)))
        self.assertEqual(sp.gcd(primitive_top(b), primitive_top(c)), 1)
        shifted_b = b + sp.Rational(3, 4) * x
        self.assertEqual(primitive_top(shifted_b), x**2)
        self.assertTrue(zero(primitive_top(c) - 2 * shifted_b))
        for coordinate in (x, b, c):
            self.assertEqual(primitive_top(coordinate).subs({x: 0, b: 0}), 0)
        for polynomial in (b * c + c**3, x + b**4, x * c**2 + b * c**2):
            self.assertEqual(primitive_top(polynomial).subs({x: 0, b: 0}), 0)

    def test_kernel_and_all_degree_parity_controls(self):
        shifted_b = b + sp.Rational(3, 4) * x
        J = x**2 * c - shifted_b**2
        self.assertTrue(zero(primitive_top(J)))
        self.assertTrue(zero(primitive_top(primitive_top(shifted_b))))
        coefficients = sp.symbols("a0:5") + sp.symbols("d0:5")
        even = sum(coefficients[k] * h**k for k in range(5))
        odd = sum(coefficients[k + 5] * h**k for k in range(5))
        residue = sub(even + b * odd, {h: -b**2})
        solution = sp.solve(sp.Poly(residue, b).all_coeffs(),
                            coefficients, dict=True)
        self.assertEqual(solution, [{coefficient: 0 for coefficient in coefficients}])
        for kernel_poly in (x + J, J**2 + x**3, x**2 * J + 1):
            image = primitive_top(kernel_poly * shifted_b)
            self.assertTrue(zero(image - x**2 * kernel_poly))

    def test_same_canonical_model_has_a_good_minimizer_too(self):
        good_c = z - lam**2 * w**2
        good_vertical = physical_vertical(good_c)
        self.assertTrue(zero(good_vertical - 2 * w - 4 * lam * x * w))
        self.assertEqual(sp.Poly(good_vertical, lam).degree(), 1)
        self.assertEqual(sp.Poly(target_vertical(c), lam).degree(), 1)
        # The good top has only a c coefficient, whose primitive field
        # is the coordinate partial. The bad primitive has a fixed line.
        self.assertEqual(sp.diff(c, c), 1)
        self.assertEqual(primitive_top(c).subs({x: 0, b: 0}), 0)
        self.assertNotEqual(primitive_top(c), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
