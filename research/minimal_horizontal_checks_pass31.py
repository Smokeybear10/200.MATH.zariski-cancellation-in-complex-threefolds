"""Exact finite controls for the pass-31 minimum-horizontal proof.

These controls do not classify arbitrary polynomial plane automorphisms
or prove that all unrestricted degree-one minimizers have sliced tops.
No project solvers are imported.
"""

import unittest

import sympy as sp


x, lam, w, z, b, c, h = sp.symbols("x lam w z b c h")
v = 1 + lam * x
invariant = x**2 * z - v**2 * w**2


def exact_zero(expr):
    return sp.expand(expr) == 0


def vertical(expr):
    return sp.expand(x**2 * sp.diff(expr, w)
                     + 2 * v**2 * w * sp.diff(expr, z))


def substitute(expr, replacements):
    return sp.expand(expr.subs(replacements, simultaneous=True))


def horizontal(expr, shift, height):
    actual_b = w - shift
    return sp.expand(
        sp.diff(expr, lam)
        + sp.diff(shift, lam) * sp.diff(expr, w)
        + substitute(sp.diff(height, lam), {b: actual_b})
        * sp.diff(expr, z)
    )


def actual_frame(shift, height):
    actual_b = w - shift
    actual_c = z - substitute(height, {b: actual_b})
    inverse = {w: b + shift, z: c + height}
    return actual_b, actual_c, inverse


class MinimalHorizontalChecks(unittest.TestCase):
    def test_canonical_invariant_and_actual_degree_one_shear(self):
        self.assertTrue(exact_zero(vertical(invariant)))
        actual_c = z - lam**2 * w**2
        self.assertTrue(exact_zero(vertical(actual_c)
                                   - 2 * w - 4 * lam * x * w))
        self.assertEqual(sp.Poly(vertical(actual_c), lam).degree(), 1)
        self.assertTrue(exact_zero(
            sp.diff(actual_c, lam)
            + 2 * lam * w**2 * sp.diff(actual_c, z)))
        self.assertEqual(sp.Poly(vertical(z), lam).degree(), 2)

    def test_both_full_coordinate_compositions(self):
        examples = (
            (sp.Integer(0), lam**2 * b**2),
            (lam - 2 * x * lam**2,
             lam**2 * b**2 - 6 * lam**3 * b - 4 * x * lam**4 * b),
            (x * lam + lam**2 * x**2,
             lam * b**3 + lam**3 * b + x * lam**2 * b**2),
        )
        for shift, height in examples:
            actual_b, actual_c, inverse = actual_frame(shift, height)
            self.assertTrue(exact_zero(substitute(actual_b, inverse) - b))
            self.assertTrue(exact_zero(substitute(actual_c, inverse) - c))
            self.assertTrue(exact_zero(
                substitute(b + shift, {b: actual_b, c: actual_c}) - w))
            self.assertTrue(exact_zero(
                substitute(c + height, {b: actual_b, c: actual_c}) - z))
            self.assertTrue(exact_zero(horizontal(actual_b, shift, height)))
            self.assertTrue(exact_zero(horizontal(actual_c, shift, height)))
            self.assertEqual(horizontal(lam, shift, height), 1)
            self.assertEqual(horizontal(x, shift, height), 0)

    def test_degree_one_by_actual_second_adjoint(self):
        for shift, height in (
                (sp.Integer(0), lam**2 * b**2),
                (lam - 2 * x * lam**2,
                 lam**2 * b**2 - 6 * lam**3 * b - 4 * x * lam**4 * b)):
            def first(expr):
                return sp.expand(horizontal(vertical(expr), shift, height)
                                 - vertical(horizontal(expr, shift, height)))

            values = [first(f) for f in (x, lam, w, z)]
            self.assertTrue(any(value != 0 for value in values))
            for f in (x, lam, w, z):
                second = horizontal(first(f), shift, height) - first(
                    horizontal(f, shift, height))
                self.assertTrue(exact_zero(second))

    def test_nontangent_minimizer_and_exact_physical_formula(self):
        shift = lam - 2 * x * lam**2
        height = lam**2 * b**2 - 6 * lam**3 * b - 4 * x * lam**4 * b
        actual_b, actual_c, inverse = actual_frame(shift, height)
        self.assertEqual(horizontal(w, shift, height), 1 - 4 * x * lam)
        expected_z = (2 * lam * (w - shift)**2
                      - 18 * lam**2 * (w - shift)
                      - 16 * x * lam**3 * (w - shift))
        self.assertTrue(exact_zero(horizontal(z, shift, height) - expected_z))
        self.assertTrue(exact_zero(substitute(vertical(actual_b), inverse)
                                   - x**2))
        self.assertTrue(exact_zero(substitute(vertical(actual_c), inverse)
                                   - 2 * b - lam * (4 * x * b + 2)))
        self.assertEqual(horizontal(w, shift, height).subs(x, 0), 1)
        auxiliary = 2 * x * z - w**2
        self.assertTrue(exact_zero(
            horizontal(auxiliary, shift, height).subs(x, 0) + 2 * w))

    def test_general_triangular_formula_on_independent_physical_maps(self):
        cases = (
            (sp.Integer(0), sp.Integer(0), b**3 + x * b, lam**3),
            (sp.Integer(1), lam**2 + x * lam**3, b**2 + x, x * lam**2),
            (x + 1, lam**4, (x + 2) * b**3 + b, lam**4 * (x + 1)),
            (x**2 - 2, lam**2 * (x + lam), x * b**4, lam**2 + lam**5),
        )
        for j, remainder, linear_height, scalar_height in cases:
            shift = sp.expand(lam * j - 2 * x * lam**2 * j
                              + x**2 * remainder)
            numerator = sp.expand(v**2 * shift - lam * j)
            quotient, rem = sp.div(numerator, x**2, x)
            self.assertEqual(rem, 0)
            height = sp.expand(lam * linear_height + lam**2 * b**2
                               + 2 * quotient * b + scalar_height)
            actual_b, actual_c, inverse = actual_frame(shift, height)
            actual_value = substitute(vertical(actual_c), inverse)
            expected_top = sp.expand(4 * x * b + 2 * j
                                     - x**2 * sp.diff(linear_height, b))
            self.assertTrue(exact_zero(actual_value
                                       - 2 * b - lam * expected_top))
            self.assertEqual(sp.Poly(actual_value, lam).degree(), 1)
            self.assertTrue(exact_zero(horizontal(actual_c, shift, height)))
            self.assertTrue(exact_zero(substitute(actual_c, inverse) - c))
            self.assertNotEqual(expected_top, 0)

    def test_necessary_shift_residue_solved_from_raw_coefficients(self):
        aa = sp.symbols("a1:5")
        bb = sp.symbols("b1:5")
        shift = sum(lam**k * (aa[k - 1] + x * bb[k - 1])
                    for k in range(1, 5))
        residue = sp.rem(sp.expand(v**2 * shift), x**2, x)
        constraints = []
        for k in range(2, 7):
            coefficient = sp.expand(residue).coeff(lam, k)
            constraints.extend((coefficient.coeff(x, 0),
                                coefficient.coeff(x, 1)))
        unknowns = (aa[1], aa[2], aa[3], bb[1], bb[2], bb[3])
        solutions = sp.solve(constraints, unknowns, dict=True)
        self.assertEqual(solutions, [{
            aa[1]: 0, aa[2]: 0, aa[3]: 0,
            bb[1]: -2 * aa[0], bb[2]: 0, bb[3]: 0,
        }])

    def test_height_coefficients_recovered_from_actual_action(self):
        k22, k31, k41 = sp.symbols("k22 k31 k41")
        shift = lam - 2 * x * lam**2
        height = k22 * lam**2 * b**2 + k31 * lam**3 * b + k41 * lam**4 * b
        actual_b, actual_c, inverse = actual_frame(shift, height)
        value = substitute(vertical(actual_c), inverse)
        equations = []
        for k in range(2, 5):
            equations.extend(sp.Poly(value.coeff(lam, k), b).all_coeffs())
        result = sp.solve(equations, (k22, k31, k41), dict=True)
        self.assertEqual(result, [{k22: 1, k31: -6, k41: -4 * x}])
        rejected_shift = lam
        rejected = sp.rem(sp.expand(v**2 * rejected_shift), x**2, x)
        self.assertEqual(sp.expand(rejected).coeff(lam, 2), 2 * x)
        self.assertNotEqual(sp.expand(rejected).coeff(lam, 2), 0)

    def test_parity_forces_the_nonconstant_invariant_coefficient(self):
        beta_coeffs = sp.symbols("p0:4")
        g_coeffs = sp.symbols("g0:4")
        beta_poly = sum(beta_coeffs[k] * h**k for k in range(4))
        g_poly = sum(g_coeffs[k] * h**k for k in range(4))
        zeroth = substitute(g_poly + 2 * w * beta_poly, {h: -w**2})
        solution0 = sp.solve(sp.Poly(zeroth, w).all_coeffs(),
                             beta_coeffs + g_coeffs, dict=True)
        self.assertEqual(solution0, [{
            coefficient: 0 for coefficient in beta_coeffs + g_coeffs
        }])
        first = substitute(g_poly + 2 * w**2 + 2 * w * beta_poly,
                           {h: -w**2})
        solution1 = sp.solve(sp.Poly(first, w).all_coeffs(),
                             beta_coeffs + g_coeffs, dict=True)
        expected = {coefficient: 0 for coefficient in beta_coeffs + g_coeffs}
        expected[g_coeffs[1]] = 2
        self.assertEqual(solution1, [expected])

    def test_planar_lnd_gate_negative_degree_controls(self):
        for degree in (2, 3, 4):
            coefficient = (lam + 1) * h**degree + lam**2
            value = h
            for iteration in range(1, 6):
                value = sp.expand(sp.diff(value, lam)
                                  + coefficient * sp.diff(value, h))
                self.assertEqual(sp.Poly(value, h).degree(),
                                 1 + iteration * (degree - 1))
        for slope in (sp.Integer(2), lam + 1, lam**2 - lam):
            value = h
            for iteration in range(1, 7):
                value = sp.expand(sp.diff(value, lam)
                                  + (slope * h + lam**3) * sp.diff(value, h))
                leading = sp.expand(value).coeff(h, 1)
                self.assertNotEqual(leading, 0)
                self.assertEqual(sp.Poly(leading, lam).degree(),
                                 iteration * sp.Poly(slope, lam).degree())

    def test_primitive_top_and_zero_degree_divisibility_obstruction(self):
        j = x**3 + 1
        linear_height = b**4 + x * b**2
        shift = lam * j - 2 * x * lam**2 * j
        quotient = sp.div(sp.expand(v**2 * shift - lam * j), x**2, x)[0]
        height = lam * linear_height + lam**2 * b**2 + 2 * quotient * b
        actual_b, actual_c, inverse = actual_frame(shift, height)
        actual_top = tuple(
            substitute(vertical(f), inverse).coeff(lam, 1)
            for f in (x, actual_b, actual_c)
        )
        common = sp.gcd_list(actual_top)
        primitive = tuple(sp.cancel(value / common) for value in actual_top)
        self.assertEqual(primitive[:2], (0, 0))
        self.assertIn(primitive[2], (sp.Integer(-1), sp.Integer(1)))
        slice_value = sp.expand(primitive[2] * sp.diff(c / primitive[2], c))
        self.assertEqual(slice_value, 1)
        self.assertNotEqual(sp.Poly(common, x, b).total_degree(), 0)
        # No polynomial height correction can cancel this residue.
        self.assertEqual(sp.expand(4 * x * b + 2 * j).coeff(b, 1), 4 * x)
        self.assertEqual(sp.rem(4 * x, x**2, x), 4 * x)


if __name__ == "__main__":
    unittest.main(verbosity=2)
