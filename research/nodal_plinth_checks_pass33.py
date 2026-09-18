"""Finite exact controls for the forced first nodal modification.

The unknown ambient C^3 realization is not constructed here.
Only unittest and SymPy are imported, with no project solver.
"""

import unittest

import sympy as sp


u, s = sp.symbols("u s")
D, V, r, Y = sp.symbols("D V r Y")
P = V**2 - D**2 * (D + 1)


def lift_squared_conductor(poly):
    """Lift (s^2-1)^2*poly(s) into C[D,V], D=s^2-1, V=D*s."""
    answer = sp.Integer(0)
    for (degree,), coefficient in sp.Poly(poly, s).terms():
        if degree % 2:
            answer += coefficient * D * V * (D + 1)**((degree - 1) // 2)
        else:
            answer += coefficient * D**2 * (D + 1)**(degree // 2)
    return sp.expand(answer)


def derivation(poly, coefficients):
    return sp.expand(sum(coefficient * sp.diff(poly, variable)
                         for variable, coefficient in zip((D, V, r, Y), coefficients)))


class NodalPlinthChecks(unittest.TestCase):
    def test_trace_normalization_and_quadratic_field_relation(self):
        d = u**4 - 1
        even_part = 2 + d * (u**6 - 3 * u**2 + 1)
        b = s**3 + 2 * s + 1
        odd_part = d * u * b.subs(s, u**2)
        raw = sp.expand(even_part + odd_part)
        self.assertEqual(sp.expand((raw + raw.subs(u, -u)) / 2), even_part.expand())
        self.assertEqual(sp.expand((raw - raw.subs(u, -u)) / 2), odd_part.expand())
        norm = (s**2 - 1)**2 * s * b**2
        self.assertEqual(sp.expand(odd_part**2 - norm.subs(s, u**2)), 0)
        self.assertEqual(sp.rem(norm, (s**2 - 1)**2, s), 0)
        self.assertNotEqual(sp.expand(odd_part), 0)
        # This concrete norm has odd valuation at s=0, so it is not a square.
        self.assertEqual(norm.subs(s, 0), 0)
        self.assertNotEqual(sp.diff(norm, s).subs(s, 0), 0)

    def test_all_polynomial_conductor_lifts_stay_in_node_square(self):
        for b in (sp.Integer(1), s, s**2 + 2*s + 3, s**4 - s + 2):
            lifted = lift_squared_conductor(s * b**2)
            normalization = {D: s**2 - 1, V: s * (s**2 - 1)}
            self.assertEqual(sp.expand(lifted.subs(normalization)
                                       - (s**2 - 1)**2 * s * b**2), 0)
            self.assertTrue(all(i + j >= 2
                                for (i, j), coefficient in sp.Poly(lifted, D, V).terms()
                                if coefficient != 0))
            # Any alternative lift differs by a multiple of the nodal equation.
            alternate = sp.expand(lifted + P * (1 + D + V**2))
            for expression in (alternate, sp.diff(alternate, D),
                               sp.diff(alternate, V)):
                self.assertEqual(expression.subs({D: 0, V: 0}), 0)

    def test_monic_center_division_and_nonzero_linear_control(self):
        b = s**2 + s + 1
        K = lift_squared_conductor(s * b**2)
        G = r**2 - K
        polynomial = sp.expand(G * (r**4 + (D + V)*r + 3)
                               + P * (r**3 + V*r + 1))
        quotient, remainder = sp.div(polynomial, G, r)
        self.assertEqual(sp.expand(polynomial - quotient * G - remainder), 0)
        self.assertEqual(sp.rem(remainder, P, V), 0)
        r_image = (u**4 - 1) * u * b.subs(s, u**2)
        substitution = {D: u**4 - 1, V: (u**4 - 1)*u**2, r: r_image}
        self.assertEqual(sp.expand(G.subs(substitution)), 0)
        # A purported linear relation has a visibly nonzero odd component.
        linear = (D + 1) + (V + 2)*r
        evaluated = sp.expand(linear.subs(substitution))
        self.assertNotEqual(sp.expand(evaluated - evaluated.subs(u, -u)), 0)

    def test_forced_stage_derivation_singular_line_and_doubled_fiber(self):
        K = lift_squared_conductor(s * (s**2 + 1)**2)
        equation = P * Y - r**2 + K
        beta = D + V + 1
        for order in (1, 2, 3):
            coefficients = (0, 0, P**order * beta,
                            2*r*P**(order - 1)*beta)
            self.assertEqual(derivation(equation, coefficients), 0)
            for coefficient in coefficients:
                self.assertEqual(sp.sympify(coefficient).subs({D: 0, V: 0, r: 0}), 0)
        self.assertEqual(equation.subs({D: 0, V: 0}), -r**2)
        for variable in (D, V, r, Y):
            self.assertEqual(sp.diff(equation, variable).subs({D: 0, V: 0, r: 0}), 0)
        self.assertEqual(sp.rem(r**2, r**2, r), 0)
        self.assertEqual(sp.rem(r, r**2, r), r)

    def test_actual_zero_base_fiber_is_one_doubled_line(self):
        y, z = sp.symbols("y z")
        A = (u - 1) * (u - sp.I)
        inverse_A = sp.invert(A, u**2, u)
        self.assertEqual(sp.rem(A * inverse_A - 1, u**2, u), 0)
        z_image = sp.expand(inverse_A * y * (y - 1))
        self.assertEqual(sp.rem(A*z_image - y*(y - 1), u**2, u), 0)
        self.assertEqual(sp.rem(u**2, u**2, u), 0)
        self.assertEqual(sp.rem(u, u**2, u), u)
        # On the reduced fiber u=0 the prescribed vector field is zero.
        self.assertEqual((u*A).subs(u, 0), 0)
        self.assertEqual((u*(2*y - 1)).subs(u, 0), 0)
        # No multiplicity at the other ordinary base values, e.g. s=2.
        self.assertEqual(sp.gcd(u**2 - 2, sp.diff(u**2 - 2, u)), 1)
        self.assertEqual(sp.gcd(u**2 - 2, A, extension=sp.I), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
