"""Independent exact controls for commuting-leading-pass25.md.

Only unittest and SymPy are imported. Finite controls verify identities,
not the all-degree or universal claims proved in the companion note.
"""

import unittest

import sympy as sp


a, b, c, s = sp.symbols("a b c s")
xi, zeta = sp.symbols("xi zeta")
u, v, z, uprime = sp.symbols("u v z uprime")
physical = (a, b, c, s)
new_coords = (a - c * (s * a - s**2 * b),
              b - c * (a - s * b), c, s)
inverse = (xi + c * (s * xi - s**2 * zeta),
           zeta + c * (xi - s * zeta), c, s)
Tc = (s * a - s**2 * b, a - s * b, sp.Integer(1), sp.Integer(0))
Ts = (c * a - 2 * c * s * b + c**2 * s * a - c**2 * s**2 * b,
      -c * b + c**2 * a - c**2 * s * b, sp.Integer(0), sp.Integer(1))
W = (c * a - 2 * c * s * b, -c * b, -c**2, sp.Integer(1))


def act(field, polynomial, variables=physical):
    return sp.expand(sum(coef * sp.diff(polynomial, var)
                         for coef, var in zip(field, variables)))


def bracket(left, right, variables=physical):
    return tuple(sp.expand(act(left, coef, variables)
                           - act(right, old, variables))
                 for old, coef in zip(left, right))


def gate_act(h, polynomial):
    return sp.expand(sp.diff(polynomial, v) - h * sp.diff(polynomial, u))


class CommutingLeadingControls(unittest.TestCase):
    def test_coordinate_inverse_forward(self):
        replacement = dict(zip((xi, zeta, c, s), new_coords))
        result = tuple(sp.expand(poly.subs(replacement, simultaneous=True))
                       for poly in inverse)
        self.assertEqual(result, physical)

    def test_coordinate_inverse_backward(self):
        replacement = dict(zip(physical, inverse))
        result = tuple(sp.expand(poly.subs(replacement, simultaneous=True))
                       for poly in new_coords)
        self.assertEqual(result, (xi, zeta, c, s))

    def test_actual_coordinate_partial_pairings(self):
        self.assertEqual(tuple(act(Tc, poly) for poly in new_coords),
                         (0, 0, 1, 0))
        self.assertEqual(tuple(act(Ts, poly) for poly in new_coords),
                         (0, 0, 0, 1))

    def test_original_coordinate_pair_commutes(self):
        self.assertEqual(bracket(Tc, Ts), (0, 0, 0, 0))

    def test_leading_relation_and_intrinsic_invariance(self):
        lead_c = tuple(sp.expand(poly).coeff(s, 2) for poly in Tc[:3])
        lead_s = tuple(sp.expand(poly).coeff(s, 2) for poly in Ts[:3])
        self.assertEqual(lead_c, (-b, 0, 0))
        self.assertEqual(lead_s, tuple(c**2 * poly for poly in lead_c))
        self.assertEqual(act(lead_c, c**2, (a, b, c)), 0)
        self.assertEqual(act(lead_s, c**2, (a, b, c)), 0)
        self.assertEqual(act(Tc, c**2), 2 * c)

    def test_exact_coefficient_matched_subtraction(self):
        self.assertEqual(tuple(sp.expand(old - c**2 * other)
                               for old, other in zip(Ts, Tc)), W)
        self.assertEqual(act(W, s), 1)

    def test_subtraction_really_lowers_filtration_degree(self):
        for field in (Tc, Ts):
            horizontal_degree = max(sp.degree(poly, s) for poly in field[:3])
            vertical_degree = sp.degree(field[3], s) - 1
            self.assertEqual(max(horizontal_degree, vertical_degree), 2)
        horizontal_degree = max(sp.degree(poly, s) for poly in W[:3])
        vertical_degree = sp.degree(W[3], s) - 1
        self.assertEqual(max(horizontal_degree, vertical_degree), 1)

    def test_reduced_field_breaks_commutation(self):
        self.assertEqual(bracket(Tc, W),
                         tuple(sp.expand(-2 * c * poly) for poly in Tc))

    def test_exact_factorial_iterates(self):
        polynomial = c
        for order in range(1, 9):
            polynomial = act(W, polynomial)
            self.assertEqual(polynomial,
                             (-1)**order * sp.factorial(order) * c**(order + 1))

    def test_nonlinear_all_degree_induction_identity(self):
        for degree in (2, 3, 4):
            leading = v + z
            h = leading * u**degree + v * u + v**2
            polynomial = u
            coefficient = sp.Integer(1)
            for order in range(1, 5):
                coefficient = sp.expand(-leading * coefficient
                                        * (1 + (order - 1) * (degree - 1)))
                polynomial = gate_act(h, polynomial)
                as_poly = sp.Poly(polynomial, u)
                self.assertEqual(as_poly.degree(), 1 + order * (degree - 1))
                self.assertEqual(sp.expand(as_poly.LC() - coefficient), 0)

    def test_affine_variable_coefficient_recurrence(self):
        alpha = v**2 + z
        beta = v**3 + z**2
        h = alpha * u + beta
        polynomial = u
        coefficient = sp.Integer(1)
        for order in range(1, 7):
            coefficient = sp.expand(sp.diff(coefficient, v) - alpha * coefficient)
            polynomial = gate_act(h, polynomial)
            self.assertEqual(sp.expand(polynomial).coeff(u), coefficient)
            as_poly = sp.Poly(coefficient, v)
            self.assertEqual(as_poly.degree(), 2 * order)
            self.assertEqual(as_poly.LC(), (-1)**order)

    def test_affine_constant_coefficient_boundary(self):
        h = z * u + v**3
        polynomial = u
        for order in range(1, 7):
            polynomial = gate_act(h, polynomial)
            self.assertEqual(sp.expand(polynomial).coeff(u), (-z)**order)

    def test_admissible_shear_and_both_coordinate_inverses(self):
        h = v**2 + z * v + z**2
        primitive = v**3 / 3 + z * v**2 / 2 + z**2 * v
        new_u = u + primitive
        self.assertEqual(gate_act(h, new_u), 0)
        self.assertEqual(gate_act(h, v), 1)
        self.assertEqual(sp.expand(new_u.subs(u, uprime - primitive)), uprime)
        self.assertEqual(sp.expand((uprime - primitive).subs(uprime, new_u)), u)
        polynomial = u
        for unused in range(4):
            polynomial = gate_act(h, polynomial)
        self.assertEqual(polynomial, 0)
        self.assertNotEqual(sp.diff(h, v), 0)

    def test_bracket_gate_with_full_polynomial_coefficient(self):
        h = z * u**3 + u * v + v**2 + z
        variables = (u, v, z)
        partial_u = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
        reduced = (-h, sp.Integer(1), sp.Integer(0))
        self.assertEqual(bracket(partial_u, reduced, variables),
                         (-sp.diff(h, u), 0, 0))

    def test_full_frame_change_tracks_other_coordinate_partials(self):
        primitive = v**3 / 3 + z * v**2 / 2 + z**2 * v
        h = sp.diff(primitive, v)
        variables = (u, v, z)
        reduced_v = (-h, sp.Integer(1), sp.Integer(0))
        unchanged_z = (sp.Integer(0), sp.Integer(0), sp.Integer(1))
        corrected_z = (-sp.diff(primitive, z), sp.Integer(0), sp.Integer(1))
        self.assertNotEqual(bracket(reduced_v, unchanged_z, variables), (0, 0, 0))
        self.assertEqual(bracket(reduced_v, corrected_z, variables), (0, 0, 0))
        self.assertEqual(act(corrected_z, u + primitive, variables), 0)

    def test_rational_line_bracket_formula(self):
        variables = (a, b, c)
        delta = (sp.Integer(0), a, b)
        h = a + b**2
        g = c + a
        left = tuple(h * coef for coef in delta)
        right = tuple(g * coef for coef in delta)
        multiplier = sp.expand(h * act(delta, g, variables)
                               - g * act(delta, h, variables))
        self.assertEqual(bracket(left, right, variables),
                         tuple(sp.expand(multiplier * coef) for coef in delta))


if __name__ == "__main__":
    unittest.main(verbosity=2)
