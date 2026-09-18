"""Three finite actual-action controls, not universal reduction proofs."""

import unittest

import sympy as sp


class QuadraticReductionControls(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    @staticmethod
    def act(vector, expression, coordinates):
        def scalar(value):
            return sp.expand(sum(vector[i] * sp.diff(value, coordinate) for i, coordinate in enumerate(coordinates)))
        return expression.applyfunc(scalar) if isinstance(expression, sp.MatrixBase) else scalar(expression)

    def test_actual_acceleration_unit_non_lnd_and_commutator(self):
        s, a, b, c = sp.symbols("s a b c")
        x, y, z, w = sp.symbols("x y z w")
        old = sp.Matrix([s, a, b, c])
        coordinates = sp.Matrix([x, y, z, w])
        forward = sp.Matrix([s, (1 + s**2) * a + s * b, s * a + b, c + s**2])
        inverse = sp.Matrix([x, y - x * z, (1 + x**2) * z - x * y, w - x**2])
        self.assert_zero(inverse.subs(dict(zip(coordinates, forward)), simultaneous=True) - old)
        self.assert_zero(forward.subs(dict(zip(old, inverse)), simultaneous=True) - coordinates)
        self.assert_zero(forward.jacobian(old).det() - 1)
        velocity = sp.Matrix([1, x * y + (1 - x**2) * z, y - x * z, 2 * x])
        self.assert_zero(forward.diff(s).subs(dict(zip(old, inverse)), simultaneous=True) - velocity)
        self.assert_zero(self.act(velocity, inverse, coordinates) - sp.Matrix([1, 0, 0, 0]))
        acceleration = self.act(velocity, velocity, coordinates)
        invariant = y - x * z
        self.assert_zero(acceleration - sp.Matrix([0, 2 * invariant, 0, 2]))
        self.assert_zero(self.act(velocity, acceleration, coordinates))
        self.assert_zero(self.act(acceleration, invariant, coordinates) - 2 * invariant)
        self.assert_zero(self.act(acceleration, w / 2, coordinates) - 1)
        iterate = y
        for n in range(1, 6):
            iterate = self.act(acceleration, iterate, coordinates)
            self.assert_zero(iterate - 2**n * invariant)
        self.assert_zero(self.act(acceleration, acceleration, coordinates) - sp.Matrix([0, 4 * invariant, 0, 0]))
        bracket = self.act(velocity, acceleration, coordinates) - self.act(acceleration, velocity, coordinates)
        self.assert_zero(bracket + 2 * invariant * sp.Matrix([0, x, 1, 0]))
        self.assert_zero(self.act(acceleration, inverse[2], coordinates) + 2 * x * invariant)
        self.assert_zero(self.act(velocity, self.act(acceleration, inverse[2], coordinates), coordinates) + 2 * invariant)
        # The all-n failure follows in the proof from H(invariant)=2*invariant.
        # Having H(w/2)=1 does not make H an LND or permit its slice theorem.

    def test_actual_flow_boxes_and_generic_degrees(self):
        t, a, b, c, x, y, z, w, T = sp.symbols("t a b c x y z w T")
        quadratic = sp.Matrix([a + t, 2 * a * t + t**2, b, c])
        coordinates = sp.Matrix([x, y, z, w])
        relation = y - 2 * T * x + T**2
        substitution = dict(zip(coordinates, quadratic)) | {T: t}
        self.assert_zero(relation.subs(substitution, simultaneous=True))
        self.assert_zero(quadratic[:2, :].jacobian((t, a)).det() + 2 * a)
        self.assert_zero((x**2 - y).subs(substitution, simultaneous=True) - a**2)
        transverse = sp.Matrix([x - T, y - 2 * T * x + T**2, z, w])
        self.assert_zero(transverse.subs(substitution, simultaneous=True) - sp.Matrix([a, 0, b, c]))
        self.assert_zero(sp.discriminant(relation, T) - 4 * (x**2 - y))
        self.assertEqual(sp.Poly(x**2 - y, y).degree(), 1)
        self.assert_zero(sp.Poly(x**2 - y, y).LC() + 1)
        self.assertEqual(sp.factor_list(x**2 - y)[1], [(x**2 - y, 1)])
        # The written odd-valuation/Gauss argument gives irreducibility over
        # C(x,y,z,w), not finite point evaluation or a test of every flow box.

        s0, A, S, Y, Z = sp.symbols("s0 A S Y Z")
        linear = sp.Matrix([s0 + t, A, A * t, Z])
        linear_coordinates = sp.Matrix([S, A, Y, Z])
        linear_relation = Y - A * T
        self.assert_zero(linear_relation.subs(dict(zip(linear_coordinates, linear)) | {T: t}, simultaneous=True))
        self.assert_zero(linear.jacobian((t, s0, A, Z)).det() - A)
        self.assert_zero(linear.subs(A, 0)[2])
        rational_inverse = sp.Matrix([Y / A, S - Y / A, A, Z])
        domain_coordinates = sp.Matrix([t, s0, A, Z])
        self.assert_zero(rational_inverse.subs(dict(zip(linear_coordinates, linear)), simultaneous=True) - domain_coordinates)
        self.assert_zero(linear.subs(dict(zip(domain_coordinates, rational_inverse)), simultaneous=True) - linear_coordinates)
        self.assert_zero(linear_relation.subs(T, Y / A))
        # A=0,Y!=0 is missed; this inverse is only asserted on A!=0.

    def test_rank_one_acceleration_without_square_speed_divisibility(self):
        a, x, y, z = sp.symbols("a x y z")
        A, V, S, Z = sp.symbols("A V S Z")
        coordinates = sp.Matrix([a, x, y, z])
        adapted_coordinates = sp.Matrix([A, V, S, Z])
        v = x + a * x**2 / 2 - a**2 * y
        sigma = sp.cancel(y + (v**2 - x**2) / (2 * a))
        # Poly construction checks regularity before any localization claim.
        sp.Poly(sigma, a, x, y, z)
        forward = sp.Matrix([a, v, sigma, z])
        inverse_x = V - A * V**2 / 2 + A**2 * S
        inverse_y = sp.cancel(S + (inverse_x**2 - V**2) / (2 * A))
        sp.Poly(inverse_y, A, V, S, Z)
        inverse = sp.Matrix([A, inverse_x, inverse_y, Z])
        self.assert_zero(inverse.subs(dict(zip(adapted_coordinates, forward)), simultaneous=True) - coordinates)
        self.assert_zero(forward.subs(dict(zip(coordinates, inverse)), simultaneous=True) - adapted_coordinates)
        self.assert_zero(forward.jacobian(coordinates).det() - 1)
        velocity = sp.Matrix([0, a**2, 1 + a * x, 0])
        self.assert_zero(self.act(velocity, forward, coordinates) - sp.Matrix([0, 0, 1, 0]))
        acceleration = self.act(velocity, velocity, coordinates)
        self.assert_zero(acceleration - sp.Matrix([0, 0, a**3, 0]))
        self.assert_zero(self.act(velocity, acceleration, coordinates))
        self.assert_zero(self.act(velocity, a**2, coordinates))
        self.assertEqual(sp.rem(a**3, a**4, a), a**3)
        self.assert_zero(velocity.subs(a, 0) - sp.Matrix([0, 0, 1, 0]))
        # q=a^3 is not in (f^2)=(a^4), even with actual polynomial inverse
        # coordinates and a global slice. No universal divisibility follows.


if __name__ == "__main__":
    unittest.main(verbosity=2)
