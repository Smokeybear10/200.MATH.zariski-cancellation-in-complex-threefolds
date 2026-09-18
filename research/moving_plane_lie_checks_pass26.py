"""Exact finite controls for the written moving-plane Lie arguments."""

import unittest

import sympy as sp


lam, a, b, c, x, w, z, tau, H = sp.symbols("lam a b c x w z tau H")
variables = (lam, a, b, c)
V = 1 + a * lam + c * lam**2
delta = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0))
vertical = (sp.Integer(0), -2 * lam * V**2 * b,
            (a + lam * c)**2, 2 * V**2 * b)


def apply(values, expression):
    return sp.expand(sum(value * sp.diff(expression, q)
                         for value, q in zip(values, variables)))


def bracket(left, right):
    return tuple(sp.expand(apply(left, value) - apply(right, other))
                 for value, other in zip(right, left))


def scale(values, coefficient):
    return tuple(sp.expand(coefficient * value) for value in values)


class MovingPlaneLieControls(unittest.TestCase):
    def test_horizontal_coordinate_frame_and_inverse(self):
        old_variables = (lam, x, w, z)
        old_delta = (1, z, 0, 0)
        images = (lam, x - lam * z, w, z)
        for expression, expected in zip(images, (1, 0, 0, 0)):
            actual = sum(value * sp.diff(expression, q)
                         for value, q in zip(old_delta, old_variables))
            self.assertEqual(sp.expand(actual - expected), 0)
        forward = {a: x - lam * z, b: w, c: z}
        backward = {x: a + lam * c, w: b, z: c}
        for q in (a, b, c):
            self.assertEqual(sp.expand(forward[q].subs(backward, simultaneous=True)), q)
        for q in (x, w, z):
            self.assertEqual(sp.expand(backward[q].subs(forward, simultaneous=True)), q)

    def test_actual_vertical_action_and_primitivity(self):
        old_v = 1 + lam * x
        old_vertical = (0, 0, x**2, 2 * old_v**2 * w)
        old_variables = (lam, x, w, z)
        def old_apply(expression):
            return sp.expand(sum(value * sp.diff(expression, q)
                                 for value, q in zip(old_vertical, old_variables)))
        frame = (lam, x - lam * z, w, z)
        substitution = {x: a + lam * c, w: b, z: c}
        for expression, expected in zip(frame, vertical):
            actual = old_apply(expression).subs(substitution, simultaneous=True)
            self.assertEqual(sp.expand(actual - expected), 0)
        self.assertEqual(sp.gcd(x**2, 2 * old_v**2 * w), 1)
        old_h = x**2 * z - old_v**2 * w**2
        self.assertEqual(old_apply(old_h), 0)
        for q in old_variables:
            self.assertEqual(old_apply(old_apply(old_apply(q))), 0)

    def test_finite_adjoint_and_entire_conjugation_family(self):
        current = vertical
        coefficients = []
        for order in range(6):
            coefficients.append(scale(current, sp.Rational(1, sp.factorial(order))))
            current = bracket(delta, current)
        self.assertEqual(current, (0, 0, 0, 0))
        for index in range(4):
            reconstructed = sum(tau**j * coefficients[j][index] for j in range(6))
            # Direct coordinate conjugation sends the coefficient parameter
            # lambda to lambda+tau, independently of the bracket computation.
            conjugated = vertical[index].subs(lam, lam + tau)
            self.assertEqual(sp.expand(reconstructed - conjugated), 0)

    def test_top_and_penultimate_are_different_lnd_cases(self):
        current = vertical
        for _ in range(4):
            current = bracket(delta, current)
        q4 = scale(current, sp.Rational(1, 24))
        q5 = scale(bracket(delta, current), sp.Rational(1, 120))
        expected4 = (0, -4*a*b*c-10*lam*b*c**2, 0, 2*b*c**2)
        expected5 = (0, -2*b*c**2, 0, 0)
        self.assertEqual(q4, expected4)
        self.assertEqual(q5, expected5)
        iterate = c
        for j in range(1, 7):
            iterate = apply(q4, iterate)
            self.assertEqual(iterate, 2**j*b**j*sp.factorial(j)*c**(j+1))
            self.assertNotEqual(iterate, 0)

    def test_unbounded_lie_word_closed_form_controls(self):
        q4 = (0, -4*a*b*c-10*lam*b*c**2, 0, 2*b*c**2)
        current = (0, -2*b*c**2, 0, 0)
        degrees = []
        for j in range(7):
            coefficient = -2 * 2**j * sp.factorial(j+3) / sp.factorial(3)
            expected = coefficient*b**(j+1)*c**(j+2)
            self.assertEqual(current, (0, expected, 0, 0))
            degrees.append(sp.Poly(current[1], b, c).total_degree())
            current = bracket(q4, current)
        self.assertEqual(degrees, list(range(3, 17, 2)))

    def test_joint_kernel_coefficient_obstruction(self):
        d0 = tuple(sp.expand(value).coeff(lam, 0) for value in vertical)
        d1 = tuple(sp.expand(value).coeff(lam, 1) for value in vertical)
        invariant = a**2*c-b**2
        self.assertEqual(apply(d0, invariant), 0)
        self.assertEqual(apply(d0, a), 0)
        self.assertEqual(apply(d1, invariant), 4*a**3*b-8*a*b*c)
        self.assertEqual(apply(d1, a), -2*b)
        pa, ph = sp.symbols("pa ph")
        image = apply(d1, a)*pa + apply(d1, invariant)*ph
        cleared = sp.expand(a * image.subs(c, (H+b**2)/a**2))
        coefficients = sp.Poly(cleared, b).all_coeffs()
        self.assertEqual(sp.solve(coefficients, (pa, ph), dict=True), [{pa: 0, ph: 0}])

    def test_top_primitive_part_and_actual_slice(self):
        top = (0, -2*b*c**2, 0, 0)
        primitive = tuple(sp.cancel(value/(-2*b*c**2)) for value in top)
        self.assertEqual(primitive, (0, 1, 0, 0))
        self.assertEqual(apply(primitive, a), 1)
        self.assertEqual(bracket(delta, primitive), (0, 0, 0, 0))
        self.assertEqual(apply(top, a).subs(b, 0), 0)
        for q in variables:
            self.assertEqual(apply(top, q).subs(b, 0), 0)

    def test_new_joint_plane_is_not_the_old_joint_plane(self):
        primitive = (0, 1, 0, 0)
        for q in (b, c):
            self.assertEqual(apply(delta, q), 0)
            self.assertEqual(apply(primitive, q), 0)
            self.assertNotEqual(apply(vertical, q), 0)


if __name__ == "__main__":
    unittest.main()
