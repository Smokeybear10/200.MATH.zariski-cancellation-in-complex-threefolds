"""Actual-frame and quotient controls, not an ambient realization theorem."""

import unittest

import sympy as S


class RankOneSpeedChecks(unittest.TestCase):
    def zero(self, value):
        for entry in list(value) if isinstance(value, S.MatrixBase) else [value]:
            self.assertEqual(S.cancel(S.expand(entry)), 0)

    @staticmethod
    def act(velocity, value, variables):
        def scalar(f):
            return S.expand(sum(v*S.diff(f, x) for v, x in zip(velocity, variables)))
        return value.applyfunc(scalar) if isinstance(value, S.MatrixBase) else scalar(value)

    @staticmethod
    def truncate(value, parameter, order):
        return S.rem(S.expand(value), parameter**order, parameter)

    def test_actual_nonprincipal_two_speed_frame_and_divergence(self):
        s, a, b, c = S.symbols("s a b c")
        A, X, Y, Z = S.symbols("A X Y Z")
        old, coordinates = S.Matrix([s, a, b, c]), S.Matrix([A, X, Y, Z])
        good_x, good_y = b + a*a*s, c + b*b*s
        forward = S.Matrix([a, good_x, good_y, s + good_x*good_y])
        sigma = Z-X*Y
        invariant_b = X-A*A*sigma
        inverse = S.Matrix([sigma, A, invariant_b, Y-invariant_b**2*sigma])
        self.zero(inverse.subs(dict(zip(coordinates, forward)), simultaneous=True)-old)
        self.zero(forward.subs(dict(zip(old, inverse)), simultaneous=True)-coordinates)
        velocity = S.Matrix([0, A*A, invariant_b**2, 1+A*A*Y+invariant_b**2*X])
        self.zero(forward.diff(s).subs(dict(zip(old, inverse)), simultaneous=True)-velocity)
        self.zero(self.act(velocity, inverse, coordinates)-S.Matrix([1, 0, 0, 0]))
        acceleration = self.act(velocity, velocity, coordinates)
        self.zero(acceleration-S.Matrix([0, 0, 0, 2*A*A*invariant_b**2]))
        self.zero(self.act(velocity, acceleration, coordinates))
        ideal = S.groebner([A*A, invariant_b**2], A, X, Y, Z)
        base_ideal = S.groebner([A*A, X*X], A, X, Y, Z)
        for generator in (A*A, invariant_b**2):
            self.zero(base_ideal.reduce(generator)[1])
        for generator in (A*A, X*X):
            self.zero(ideal.reduce(generator)[1])
        self.assertEqual(ideal.reduce(S.Integer(1))[1], 1)
        self.assertEqual(S.gcd(A*A, invariant_b**2), 1)
        self.zero(ideal.reduce(acceleration[3])[1])
        self.zero(ideal.reduce(S.diff(invariant_b**2, Z))[1])
        primitive_divergence = S.diff(velocity[0], A)+S.diff(velocity[1], X)+S.diff(velocity[2], Y)
        self.zero(primitive_divergence-2*A*A*X*invariant_b)
        self.zero(S.diff(velocity[3], Z)+primitive_divergence)
        self.zero(ideal.reduce(primitive_divergence)[1])
        self.zero(ideal.reduce(velocity[3]-1)[1])
        # This particular proper, nonprincipal ideal contains q. It does not
        # prove that every actual proper nonprincipal speed ideal does.

    def test_retained_principal_nagata_frame(self):
        s, a, b, c = S.symbols("s a b c")
        Y, B, C, Z = S.symbols("Y B C Z")
        old, coordinates = S.Matrix([s, a, b, c]), S.Matrix([Y, B, C, Z])
        delta = a*a+s*b
        forward = S.Matrix([a+b*delta, b, c, s-2*a*delta-b*delta**2])
        recovered_delta = Y*Y+Z*B
        inverse = S.Matrix([Z+2*Y*recovered_delta-B*recovered_delta**2,
                            Y-B*recovered_delta, B, C])
        self.zero(inverse.subs(dict(zip(coordinates, forward)), simultaneous=True)-old)
        self.zero(forward.subs(dict(zip(old, inverse)), simultaneous=True)-coordinates)
        velocity = S.Matrix([B*B, 0, 0, 1-2*B*Y])
        self.zero(forward.diff(s).subs(dict(zip(old, inverse)), simultaneous=True)-velocity)
        self.zero(self.act(velocity, inverse, coordinates)-S.Matrix([1, 0, 0, 0]))
        acceleration = self.act(velocity, velocity, coordinates)
        self.zero(acceleration-S.Matrix([0, 0, 0, -2*B**3]))
        self.zero(self.act(velocity, acceleration, coordinates))
        g = B*B
        self.zero(S.diff(g, Z))
        self.zero(self.act(velocity, g, coordinates))
        self.zero(acceleration[3]/g-S.diff(velocity[3], Y))
        self.zero(S.rem(acceleration[3], g, B))
        self.assertEqual(S.rem(acceleration[3], g*g, B), -2*B**3)

    def test_nilpotent_catalan_quotient_inverses_and_units(self):
        epsilon, s, z = S.symbols("epsilon s z")
        forward = s+epsilon*s*s/2
        for order in range(2, 7):
            with self.subTest(nilpotence_order=order):
                reduce = lambda f: self.truncate(f, epsilon, order)
                inverse = sum((-1)**j*S.catalan(j)*epsilon**j*z**(j+1)/2**j for j in range(order))
                self.zero(reduce(inverse.subs(z, forward)-s))
                self.zero(reduce(forward.subs(s, inverse)-z))
                speed = reduce(1+epsilon*inverse)
                inverse_speed = reduce(sum((-epsilon*inverse)**j for j in range(order)))
                self.zero(reduce(speed*inverse_speed-1))
                self.zero(reduce(speed*S.diff(inverse, z)-1))
                acceleration = reduce(speed*S.diff(speed, z))
                self.zero(acceleration-epsilon)
                self.zero(reduce(speed*S.diff(acceleration, z)))
                divergence = reduce(S.diff(speed, z))
                self.zero(S.Poly(divergence, epsilon).nth(1)-1)
                self.assertNotEqual(divergence, 0)
                self.assertEqual(reduce(epsilon**(order-1)), epsilon**(order-1))
                self.zero(reduce(epsilon**order))
                if order >= 5:
                    self.assertEqual(reduce(acceleration**4), epsilon**4)
                else:
                    self.zero(reduce(acceleration**4))
        # All these are quotient-ring LNDs. Orders >=5 cannot be the full
        # speed quotient of the ambient C4 hypotheses by the separate theorem.

    def test_formal_ambient_determinant_recurrence_and_nilpotence(self):
        t, d, e1, e2, e3 = S.symbols("t d e1 e2 e3")
        entries = S.symbols("l0:9")
        L = S.Matrix(3, 3, entries)
        r1, r2, r3, h1, h2, h3 = S.symbols("r1 r2 r3 h1 h2 h3")
        top = (S.eye(3)+t*L).row_join(S.zeros(3, 1))
        bottom = S.Matrix([[t*r1+t*t*h1/2, t*r2+t*t*h2/2, t*r3+t*t*h3/2, 1+t*d]])
        flow_matrix = top.col_join(bottom)
        self.zero(flow_matrix.det()-(1+t*d)*(S.eye(3)+t*L).det())
        product = S.Poly(S.expand((1+t*d)*(1+e1*t+e2*t*t+e3*t**3)), t)
        self.zero(product.nth(1)-(e1+d))
        self.zero(product.nth(2)-(e2+d*e1))
        self.zero(product.nth(3)-(e3+d*e2))
        self.zero(product.nth(4)-d*e3)
        self.zero(product.as_expr().subs({e1:-d,e2:d*d,e3:-d**3})-(1-d**4*t**4))
        companion = S.Matrix([[0, 0, -d**3], [1, 0, -d*d], [0, 1, -d]])
        N = companion.row_join(S.zeros(3, 1)).col_join(S.Matrix([[r1, r2, r3, d]]))
        lam = S.symbols("lambda")
        self.zero(N.charpoly(lam).as_expr()-(lam**4-d**4))
        self.zero(N**4-d**4*S.eye(4))
        for entry in N**4:
            self.zero(S.rem(entry, d**4, d))
        # Formal matrix identities only. This companion table is not an
        # actual velocity Jacobian, ambient action or sharpness realization.


if __name__ == "__main__":
    unittest.main(verbosity=2)
