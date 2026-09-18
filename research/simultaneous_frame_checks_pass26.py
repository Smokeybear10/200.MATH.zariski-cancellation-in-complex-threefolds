"""Exact standalone controls for simultaneous-frame-pass26.md.

Only unittest and SymPy are imported. The all-degree completion theorem
is a written proof, not an inference from these finite examples.
"""

import unittest

import sympy as sp


u, v, z, t = sp.symbols("u v z t")
P0, Q0 = sp.symbols("P0 Q0")
old = (u, v, z, t)
F = v**2 + z * v + t
P = u + F
G = P**2 + t * P + z
Q = v + G
new = (P, Q, z, t)
f = 2 * v + z
g = 2 * P + t
WP = (1 + f * g, -g, sp.Integer(0), sp.Integer(0))
WQ = (-f, sp.Integer(1), sp.Integer(0), sp.Integer(0))
Wz = (-v + f, sp.Integer(-1), sp.Integer(1), sp.Integer(0))
Wt = (-1 + f * P, -P, sp.Integer(0), sp.Integer(1))
frame = (WP, WQ, Wz, Wt)
inverse_v = Q0 - P0**2 - t * P0 - z
inverse_u = P0 - inverse_v**2 - z * inverse_v - t
inverse = (inverse_u, inverse_v, z, t)


def act(field, polynomial, variables=old):
    return sp.expand(sum(coefficient * sp.diff(polynomial, variable)
                         for coefficient, variable in zip(field, variables)))


def bracket(left, right, variables=old):
    return tuple(sp.expand(act(left, coefficient, variables)
                           - act(right, old_coefficient, variables))
                 for old_coefficient, coefficient in zip(left, right))


def integrate_closed_form(first, second):
    integration_variable = sp.Dummy("integration_variable")
    along_u = sp.integrate(first.subs({u: integration_variable, v: 0}),
                          (integration_variable, 0, u))
    along_v = sp.integrate(second.subs(v, integration_variable),
                          (integration_variable, 0, v))
    return sp.expand(along_u + along_v)


class SimultaneousFrameChecks(unittest.TestCase):
    def test_two_shear_inverse_forward(self):
        replacement = {P0: P, Q0: Q}
        result = tuple(sp.expand(poly.subs(replacement, simultaneous=True))
                       for poly in inverse)
        self.assertEqual(result, old)

    def test_two_shear_inverse_backward(self):
        replacement = dict(zip(old, inverse))
        result = tuple(sp.expand(poly.subs(replacement, simultaneous=True))
                       for poly in new)
        self.assertEqual(result, (P0, Q0, z, t))

    def test_all_four_corrected_coordinate_partials(self):
        pairings = sp.Matrix([[act(field, coordinate) for coordinate in new]
                              for field in frame])
        self.assertEqual(pairings, sp.eye(4))

    def test_all_six_brackets_vanish(self):
        for left_index in range(4):
            for right_index in range(left_index + 1, 4):
                self.assertEqual(bracket(frame[left_index], frame[right_index]),
                                 (0, 0, 0, 0))

    def test_old_base_partials_cannot_be_left_uncorrected(self):
        old_z = (sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(0))
        old_t = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(1))
        self.assertNotEqual(bracket(WP, old_z), (0, 0, 0, 0))
        self.assertNotEqual(bracket(WP, old_t), (0, 0, 0, 0))

    def test_unimodular_coefficient_and_jacobian_matrices(self):
        coefficient_matrix = sp.Matrix([WP[:2], WQ[:2]])
        self.assertEqual(sp.expand(coefficient_matrix.det()), 1)
        jacobian = sp.Matrix((P, Q)).jacobian((u, v))
        self.assertEqual(sp.expand(jacobian.det()), 1)
        self.assertEqual(sp.simplify(coefficient_matrix * jacobian.T), sp.eye(2))

    def test_dual_forms_closed_and_correctly_integrated(self):
        first_form = (WQ[1], -WQ[0])
        second_form = (-WP[1], WP[0])
        for form in (first_form, second_form):
            self.assertEqual(sp.expand(sp.diff(form[1], u)
                                       - sp.diff(form[0], v)), 0)
        integrated_p = integrate_closed_form(*first_form)
        integrated_q = integrate_closed_form(*second_form)
        self.assertEqual(sp.expand(integrated_p - (P - t)), 0)
        self.assertEqual(sp.expand(integrated_q - (Q - 2 * t**2 - z)), 0)
        self.assertEqual(act(WP, integrated_p), 1)
        self.assertEqual(act(WP, integrated_q), 0)
        self.assertEqual(act(WQ, integrated_p), 0)
        self.assertEqual(act(WQ, integrated_q), 1)

    def test_nilpotence_bounds_come_from_actual_inverse(self):
        for new_variable, field in zip((P0, Q0, z, t), frame):
            for old_variable, inverse_polynomial in zip(old, inverse):
                bound = sp.degree(sp.expand(inverse_polynomial), new_variable)
                polynomial = old_variable
                for unused in range(int(bound) + 1):
                    polynomial = act(field, polynomial)
                self.assertEqual(polynomial, 0)

    def test_noncommuting_unit_determinant_control(self):
        variables = (u, v)
        first = (sp.Integer(1), u)
        second = (v, 1 + u * v)
        self.assertEqual(sp.Matrix([first, second]).det(), 1)
        self.assertEqual(bracket(first, second, variables), (u, u**2))
        self.assertEqual(act(first, u, variables), 1)
        self.assertEqual(act(first, act(first, act(first, v, variables), variables),
                             variables), 0)
        dual_form = (1 + u * v, -v)
        self.assertEqual(sp.diff(dual_form[1], u) - sp.diff(dual_form[0], v), -u)

    def test_noncommuting_control_coordinate_inverse_and_recurrence(self):
        p, q = sp.symbols("p q")
        second = (v, 1 + u * v)
        q_old = v - u**2 / 2
        self.assertEqual(act(second, q_old, (u, v)), 1)
        self.assertEqual(sp.expand(q_old.subs({u: p, v: q + p**2 / 2},
                                              simultaneous=True)), q)
        transformed = (q + p**2 / 2, sp.Integer(1))
        polynomial = p
        for order in range(1, 8):
            polynomial = act(transformed, polynomial, (p, q))
            as_poly = sp.Poly(polynomial, p)
            self.assertEqual(as_poly.degree(), order + 1)
            self.assertEqual(as_poly.LC(), sp.factorial(order) / 2**order)

    def test_successful_word_inverse_and_coordinate_pairings(self):
        a, s = sp.symbols("a s")
        for m, n in ((2, 2), (2, 3), (3, 2), (3, 3)):
            first_coordinate = a + s**m
            second_coordinate = s + first_coordinate**n
            inverse_s = v - u**n
            inverse_a = u - inverse_s**m
            replacement = {u: first_coordinate, v: second_coordinate}
            self.assertEqual(sp.expand(inverse_s.subs(replacement, simultaneous=True)), s)
            self.assertEqual(sp.expand(inverse_a.subs(replacement, simultaneous=True)), a)
            first = (1 + m * n * first_coordinate**(n - 1) * s**(m - 1),
                     -n * first_coordinate**(n - 1))
            second = (-m * s**(m - 1), sp.Integer(1))
            self.assertEqual(act(first, first_coordinate, (a, s)), 1)
            self.assertEqual(act(first, second_coordinate, (a, s)), 0)
            self.assertEqual(act(second, first_coordinate, (a, s)), 0)
            self.assertEqual(act(second, second_coordinate, (a, s)), 1)

    def test_exact_intrinsic_height_sequence(self):
        a, s = sp.symbols("a s")

        def filtered_degree(field):
            return max(sp.degree(sp.expand(field[0]), s),
                       sp.degree(sp.expand(field[1]), s) - 1)

        for m, n in ((2, 2), (2, 4), (3, 2), (3, 3)):
            first_coordinate = a + s**m
            first = (1 + m * n * first_coordinate**(n - 1) * s**(m - 1),
                     -n * first_coordinate**(n - 1))
            second = (-m * s**(m - 1), sp.Integer(1))
            q_first = filtered_degree(first)
            q_second = filtered_degree(second)
            self.assertEqual((q_first, q_second), (m * n - 1, m - 1))
            initial = q_first + q_second + 4
            after_first = filtered_degree((sp.Integer(1), sp.Integer(0))) + q_second + 4
            final = (filtered_degree((sp.Integer(1), sp.Integer(0)))
                     + filtered_degree((sp.Integer(0), sp.Integer(1))) + 4)
            self.assertEqual((initial, after_first, final),
                             (m * (n + 1) + 2, m + 3, 3))
            self.assertGreater(initial, after_first)
            self.assertGreater(after_first, final)


if __name__ == "__main__":
    unittest.main(verbosity=2)
