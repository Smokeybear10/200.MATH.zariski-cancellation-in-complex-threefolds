"""Independent exact controls for the canonical nonunit-plinth top example.

The all-degree assertions are proved in canonical-top-pass28.md.
Only unittest and SymPy are imported; no project solver is used.
"""

import unittest

import sympy as sp


lam, x, y, w, z, a, b, c, H, tau = sp.symbols("lam x y w z a b c H tau")
physical_variables = (lam, x, w, z)
frame_variables = (lam, a, b, c)
v = 1+lam*x
F = 2*x*z-w**2
kappa = 2*a*c-b**2
horizontal = (1, 0, F*x, F*w)
vertical = (0, 0, x**2, 2*v**2*w)
invariant_coordinates = (x, w-lam*F*x,
                         z-lam*F*w+lam**2*F**2*x/2)
physical_from_frame = {
    x: a, w: b+lam*kappa*a,
    z: c+lam*kappa*b+lam**2*kappa**2*a/2,
}
frame_from_physical = dict(zip((a, b, c), invariant_coordinates))
V = 1+lam*a
W = b+lam*kappa*a
T = 2*a*W*(2*V**2-a)
frame_vertical = (0, 0, a**2-lam*a*T,
                  2*V**2*W-lam*kappa*a**2-lam*b*T)
primitive_top = (0, 0, a, b)


def apply(values, expression, variables=physical_variables):
    return sp.expand(sum(value*sp.diff(expression, variable)
                         for value, variable in zip(values, variables)))


def input_d(expression):
    return sp.expand(x**2*sp.diff(expression, y)+2*y*sp.diff(expression, z))


class CanonicalTopChecks(unittest.TestCase):
    def test_actual_input_and_full_plinth_controls(self):
        h0 = x**2*z-y**2
        self.assertEqual(input_d(h0), 0)
        self.assertEqual(input_d(y), x**2)
        self.assertEqual(sp.gcd(x**2, 2*y), 1)
        for generator in (x, y, z):
            self.assertEqual(input_d(input_d(input_d(generator))), 0)
        for q0, q1 in ((x+H, H**2+1), (x*H**2+3, x**2+H**3)):
            candidate = q0.subs(H, h0)+y*q1.subs(H, h0)
            self.assertEqual(input_d(candidate), sp.expand(x**2*q1.subs(H, h0)))
        self.assertEqual(sp.rem(x, x**2, x), x)
        self.assertEqual(sp.rem(x**2, x**2, x), 0)

    def test_exact_even_odd_residue_independence(self):
        for variable in (y, w, b):
            for degree in (1, 3):
                even = sp.symbols(f"e0:{degree+1}")
                odd = sp.symbols(f"o0:{degree+1}")
                expression = sum(even[j]*(-variable**2)**j
                                 +variable*odd[j]*(-variable**2)**j
                                 for j in range(degree+1))
                actual = sp.solve(sp.Poly(expression, variable).all_coeffs(),
                                  (*even, *odd), dict=True)
                self.assertEqual(actual, [{q: 0 for q in (*even, *odd)}])

    def test_actual_canonical_modification_and_plinth_controls(self):
        relation = v*w-y
        self.assertEqual(relation.subs(y, v*w), 0)
        self.assertEqual(apply(vertical, v*w), sp.expand(v*x**2))
        self.assertEqual(apply(vertical, z), sp.expand((2*v*y).subs(y, v*w)))
        self.assertEqual(sp.gcd(x**2, 2*v**2*w), 1)
        h = x**2*z-v**2*w**2
        self.assertEqual(apply(vertical, h), 0)
        self.assertEqual(h.subs(x, 0), -w**2)
        self.assertEqual(apply(vertical, w), x**2)
        candidate = h**2+lam*x+w*(h+lam)
        self.assertEqual(apply(vertical, candidate), sp.expand(x**2*(h+lam)))
        for generator in physical_variables:
            self.assertEqual(apply(vertical, apply(vertical, apply(vertical, generator))), 0)

    def test_replica_and_actual_horizontal_flow(self):
        linear = (0, 0, x, w)
        self.assertEqual(apply(linear, F), 0)
        self.assertEqual(apply(horizontal, lam), 1)
        self.assertEqual(apply(horizontal, F), 0)
        flow = {lam: lam+tau, x: x, w: w+tau*F*x,
                z: z+tau*F*w+tau**2*F**2*x/2}
        self.assertEqual(sp.expand(F.subs(flow, simultaneous=True)-F), 0)
        for generator, value in zip(physical_variables, horizontal):
            self.assertEqual(
                sp.expand(sp.diff(flow[generator], tau)
                          -sp.sympify(value).subs(flow, simultaneous=True)), 0
            )
            self.assertEqual(apply(horizontal, apply(horizontal,
                                                     apply(horizontal, generator))), 0)

    def test_full_polynomial_inverse_physical_to_frame(self):
        for actual, expected in zip(invariant_coordinates, (a, b, c)):
            self.assertEqual(sp.expand(actual.subs(physical_from_frame,
                                                  simultaneous=True)-expected), 0)
        self.assertEqual(sp.expand(F.subs(physical_from_frame,
                                         simultaneous=True)-kappa), 0)

    def test_full_polynomial_inverse_frame_to_physical(self):
        for generator in (x, w, z):
            actual = physical_from_frame[generator].subs(frame_from_physical,
                                                         simultaneous=True)
            self.assertEqual(sp.expand(actual-generator), 0)
        self.assertEqual(sp.expand(kappa.subs(frame_from_physical,
                                             simultaneous=True)-F), 0)

    def test_actual_horizontal_invariant_coordinates(self):
        for coordinate in invariant_coordinates:
            self.assertEqual(apply(horizontal, coordinate), 0)
        self.assertEqual(apply(horizontal, lam), 1)

    def test_full_conjugated_vertical_values(self):
        for coordinate, expected in zip(invariant_coordinates, frame_vertical[1:]):
            actual = apply(vertical, coordinate).subs(physical_from_frame,
                                                       simultaneous=True)
            self.assertEqual(sp.expand(actual-expected), 0)
        self.assertEqual(sp.expand(apply(vertical, F).subs(physical_from_frame,
                                                          simultaneous=True)-T), 0)

    def test_highest_coefficient_and_actual_adjoint(self):
        expected_top = tuple(sp.expand(-4*a**4*kappa*value) for value in primitive_top)
        for value, expected in zip(frame_vertical, expected_top):
            polynomial = sp.Poly(value, lam)
            self.assertLessEqual(polynomial.degree(), 4)
            self.assertEqual(sp.expand(polynomial.coeff_monomial(lam**4)-expected), 0)
            self.assertEqual(sp.expand(sp.diff(value, lam, 4)-24*expected), 0)
            self.assertEqual(sp.diff(value, lam, 5), 0)
        self.assertNotEqual(expected_top[2], 0)
        # Check one physical commutator directly, independently of coefficient extraction.
        for coordinate, expected in zip(invariant_coordinates, frame_vertical[1:]):
            actual = apply(horizontal, apply(vertical, coordinate))
            actual -= apply(vertical, apply(horizontal, coordinate))
            actual = actual.subs(physical_from_frame, simultaneous=True)
            self.assertEqual(sp.expand(actual-sp.diff(expected, lam)), 0)

    def test_primitive_top_kernel_plinth_and_fixed_locus(self):
        self.assertEqual(sp.gcd(a, b), 1)
        self.assertEqual(apply(primitive_top, kappa, frame_variables), 0)
        self.assertEqual(apply(primitive_top, b, frame_variables), a)
        for generator in frame_variables:
            self.assertEqual(apply(primitive_top, generator, frame_variables)
                             .subs({a: 0, b: 0}), 0)
        candidate = a+kappa**2+b*(1+a*kappa)
        self.assertEqual(apply(primitive_top, candidate, frame_variables),
                         sp.expand(a*(1+a*kappa)))
        self.assertEqual(apply(primitive_top,
                              apply(primitive_top, candidate, frame_variables),
                              frame_variables), 0)

    def test_joint_field_coefficients_and_old_plane_movement(self):
        constant = tuple(sp.expand(value).coeff(lam, 0) for value in frame_vertical)
        self.assertEqual(constant, (0, 0, a**2, 2*b))
        matrix = sp.Matrix([[constant[2], constant[3]],
                            [primitive_top[2], primitive_top[3]]])
        self.assertEqual(sp.factor(matrix.det()), a*b*(a-2))
        self.assertNotEqual(matrix.det(), 0)
        h = x**2*z-v**2*w**2
        actual = apply(vertical, apply(horizontal, h))
        self.assertEqual(actual.subs({lam: 0, x: 1, w: 0, z: 1}), -2)

    def test_good_horizontal_choice_on_same_canonical_action(self):
        expected_top = (0, 0, 0, 2*x**2*w)
        for value, expected in zip(vertical, expected_top):
            self.assertEqual(sp.expand(value).coeff(lam, 2), expected)
            self.assertEqual(sp.diff(value, lam, 3), 0)
        sliced_primitive = (0, 0, 0, 1)
        self.assertEqual(apply(sliced_primitive, z), 1)
        self.assertEqual(apply(sliced_primitive, lam), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
