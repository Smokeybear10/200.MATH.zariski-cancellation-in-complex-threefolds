"""Finite exact controls for the conditional pass-31 lifting theorem.

The unknown embedding equation is not provided or discovered here.
The global theorem and its normal-cone hypotheses require the written proof.
Only unittest and SymPy are imported; no project solver is used.
"""

import unittest

import sympy as sp


X, Y, Z = sp.symbols("X Y Z")
a, b, t = sp.symbols("a b t")
f, s, w = sp.symbols("f s w")
F = Y**2 - X**2 * (X + 1)


def derive(expr, variables, coefficients):
    return sp.expand(sum(c * sp.diff(expr, v)
                         for v, c in zip(variables, coefficients)))


def zero(expr):
    return sp.expand(expr) == 0


def hamiltonian(expr):
    return derive(expr, (X, Y), (2 * Y, 3 * X**2 + 2 * X))


def nodal_lift(expr):
    return sp.expand(sp.diff(expr, Z) + F * hamiltonian(expr))


def simple_lift(expr):
    return derive(expr, (s, w), (sp.Integer(1), f * w))


class HypersurfaceLiftingChecks(unittest.TestCase):
    def test_actual_three_normal_frames_and_constant_quadratics(self):
        pairs = ((sp.Integer(1), sp.I),
                 (sp.Integer(1), -sp.I),
                 (sp.Integer(-1), sp.I))
        for left, right in pairs:
            matrix = sp.Matrix([[4 * left**3, 4 * right**3],
                                [4 * left**4, 4 * right**4]])
            self.assertFalse(zero(matrix.det()))
            self.assertTrue(zero(matrix.det()
                                 - 16 * left**3 * right**3 * (right - left)))
            quadratic = sp.expand((b - left * a) * (b - right * a))
            self.assertEqual(sp.diff(quadratic, t), 0)
            self.assertTrue(zero(quadratic.subs(b, left * a)))
            self.assertTrue(zero(quadratic.subs(b, right * a)))
            local_control = quadratic + a**3
            lift = (local_control * (a + t), local_control * (b - 1), 1)
            derivative = derive(local_control, (a, b, t), lift)
            self.assertTrue(all(i + j >= 3
                                for (i, j), coeff in
                                sp.Poly(derivative, a, b).terms() if coeff != 0))
            # A nonconstant coefficient can vanish: the whole-line
            # ordinary-crossing hypothesis would fail at t=2.
            self.assertTrue(zero(((t - 2) * quadratic).subs(t, 2)))

    def test_genuine_jacobian_annihilator_obstruction_and_off_surface_point(self):
        fx, fy = sp.diff(F, X), sp.diff(F, Y)
        jacobian = sp.groebner([fx, fy], X, Y, Z, domain=sp.QQ)
        g = (3 * X + 2) / 2
        coefficients = (X * (X + 1) / 2, Y * (3 * X + 2) / 4, 0)
        self.assertTrue(zero(derive(F, (X, Y, Z), coefficients) - F * g))
        self.assertTrue(zero(jacobian.reduce(sp.expand(F * g))[1]))
        self.assertFalse(zero(jacobian.reduce(g)[1]))
        self.assertEqual(g.subs(X, 0), 1)
        other = {X: sp.Rational(-2, 3), Y: 0}
        self.assertEqual(fx.subs(other), 0)
        self.assertEqual(fy.subs(other), 0)
        self.assertEqual(F.subs(other), sp.Rational(-4, 27))
        self.assertEqual(g.subs(other), 0)
        # The full Jacobian critical scheme includes a point outside F=0.
        self.assertFalse(zero(jacobian.reduce(F)[1]))

    def test_exact_f_and_divergence_preserving_polynomial_corrections(self):
        vector = (X + Z, Y * Z, Z**2 + 1)
        initial = (F * vector[0], F * vector[1], 1 + F * vector[2])
        g = derive(F, (X, Y, Z), vector)
        self.assertTrue(zero(derive(F, (X, Y, Z), initial) - F * g))
        corrected = tuple(sp.expand(v - F * correction)
                          for v, correction in zip(initial, vector))
        self.assertEqual(corrected, (0, 0, 1))
        self.assertEqual(derive(F, (X, Y, Z), corrected), 0)
        for old, new in zip(initial, corrected):
            self.assertTrue(zero(sp.rem(old - new, F, Y)))
        # A second correction stays inside the exactly F-preserving fields.
        tangent = (sp.Integer(0), sp.Integer(0), Z**2)
        self.assertEqual(derive(F, (X, Y, Z), tangent), 0)
        with_divergence = (sp.Integer(0), sp.Integer(0), 1 + F * Z**2)
        div = sum(sp.diff(v, x) for v, x in zip(with_divergence, (X, Y, Z)))
        self.assertTrue(zero(div - 2 * F * Z))
        corrected_again = tuple(sp.expand(v - F * correction)
                                for v, correction in zip(with_divergence, tangent))
        self.assertEqual(corrected_again, (0, 0, 1))
        self.assertEqual(sum(sp.diff(v, x) for v, x in
                             zip(corrected_again, (X, Y, Z))), 0)

    def test_all_jet_slice_control_has_nonuniform_ambient_iterates(self):
        self.assertEqual(simple_lift(f), 0)
        self.assertEqual(simple_lift(s), 1)
        current = w
        for n in range(1, 8):
            current = simple_lift(current)
            self.assertTrue(zero(current - f**n * w))
            self.assertFalse(zero(current))
        for order in range(1, 5):
            for degree in range(3):
                current = s**degree * w**2
                for unused in range(order + degree):
                    current = simple_lift(current)
                self.assertTrue(zero(sp.rem(current, f**order, f)))

    def test_irreducible_nodal_divergence_free_countercontrol(self):
        self.assertEqual(hamiltonian(F), 0)
        self.assertEqual(nodal_lift(F), 0)
        self.assertEqual(nodal_lift(Z), 1)
        coefficients = (2 * F * Y, F * (3 * X**2 + 2 * X), sp.Integer(1))
        divergence = sum(sp.diff(c, v) for c, v in zip(coefficients, (X, Y, Z)))
        self.assertTrue(zero(divergence))
        # The discriminant has an odd-order factor X+1; it is not a square.
        discriminant = sp.discriminant(F, Y)
        self.assertTrue(zero(discriminant - 4 * X**2 * (X + 1)))
        self.assertEqual(sp.diff(discriminant, X).subs(X, -1), 4)
        h_iterate, e_iterate = X, X
        for n in range(1, 6):
            h_iterate = hamiltonian(h_iterate)
            e_iterate = nodal_lift(e_iterate)
            self.assertTrue(zero(e_iterate - F**n * h_iterate))
            self.assertFalse(zero(h_iterate))
            self.assertTrue(all(coefficient > 0
                                for coefficient in sp.Poly(h_iterate, X, Y).coeffs()))
            self.assertTrue(zero(sp.rem(e_iterate, F**n, Y)))
        # There IS another ambient LND lift in this control; only the
        # implication about the chosen lift is refuted.
        self.assertEqual(sp.diff(F, Z), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
