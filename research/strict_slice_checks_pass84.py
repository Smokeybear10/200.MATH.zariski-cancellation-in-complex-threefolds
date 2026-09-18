"""Two exact actual-slice controls, not a universal proof or action search."""

import unittest

import sympy as S


class StrictSliceChecks(unittest.TestCase):
    def zero(self, value):
        entries = list(value) if isinstance(value, S.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(S.cancel(S.expand(entry)), 0)

    @staticmethod
    def act(velocity, value, variables):
        def scalar(f):
            return S.expand(sum(v*S.diff(f, x) for v, x in zip(velocity, variables)))
        return value.applyfunc(scalar) if isinstance(value, S.MatrixBase) else scalar(value)

    def check_certificate(self, coordinates, velocity, sigma, expected_degree):
        good = coordinates[:3, :]
        a, b = velocity[:3, :], velocity[3]
        acceleration = self.act(velocity, velocity, coordinates)
        q = acceleration[3]
        self.zero(acceleration[:3, :])
        self.zero(self.act(velocity, q, coordinates))
        self.zero(self.act(velocity, sigma, coordinates)-1)
        rho = coordinates.copy()
        rho[:3, :] = (good-2*b*a/q).applyfunc(S.cancel)
        substitution = dict(zip(coordinates, rho))
        self.zero(a.subs(substitution, simultaneous=True)-a)
        self.zero(q.subs(substitution, simultaneous=True)-q)
        self.zero(b.subs(substitution, simultaneous=True)+b)
        self.zero(sigma.subs(substitution, simultaneous=True)-sigma+2*b/q)
        self.zero(rho.subs(substitution, simultaneous=True)-coordinates)
        self.zero(rho.jacobian(coordinates).det()+1)

        # Degree is only in the good coordinates, with z held as coefficient.
        degree = S.Poly(sigma, *good).total_degree()
        self.assertEqual(degree, expected_degree)
        t = S.Symbol("t")
        shifted = S.Poly(S.expand(sigma.subs(
            dict(zip(good, good+t*a)), simultaneous=True)), t)
        H = {k: S.factor(S.factorial(k)*shifted.nth(k)) for k in range(1, degree+1)}
        U = 1-H[1]
        self.zero(U-b*S.diff(sigma, coordinates[3]))
        residual = U*q**(degree-1)
        for k in range(2, degree+1):
            residual -= (-2*b)**(k-1)*H[k]*q**(degree-k)/S.factorial(k)
        self.zero(residual)
        return q, degree, H

    def test_degree_two_slice_actual_two_speed_frame(self):
        s, a, b, c = S.symbols("s a b c")
        A, X, Y, Z = S.symbols("A X Y Z")
        old, coordinates = S.Matrix([s, a, b, c]), S.Matrix([A, X, Y, Z])
        x, y = b+a*s, c+b*s
        forward = S.Matrix([a, x, y, s+x*y])
        sigma = Z-X*Y
        invariant_b = X-A*sigma
        inverse = S.Matrix([sigma, A, invariant_b, Y-invariant_b*sigma])
        self.zero(inverse.subs(dict(zip(coordinates, forward)), simultaneous=True)-old)
        self.zero(forward.subs(dict(zip(old, inverse)), simultaneous=True)-coordinates)
        velocity = S.Matrix([0, A, invariant_b, 1+A*Y+invariant_b*X])
        self.zero(self.act(velocity, inverse, coordinates)-S.Matrix([1, 0, 0, 0]))
        q, degree, H = self.check_certificate(coordinates, velocity, sigma, 2)
        self.zero(q-2*A*invariant_b)
        self.zero(H[2]+q)
        # The full ideal (A,invariant_b) equals (A,X), including all z.
        self.zero(invariant_b-X+A*sigma)
        square = S.groebner([A*A, A*X, X*X], A, X, Y, Z, domain=S.QQ)
        self.zero(square.reduce(S.expand(q))[1])
        self.assertEqual((degree-1)**2, 1)

    def test_higher_degree_slice_and_sharp_extra_divisor(self):
        a, x, c, z = S.symbols("a x c z")
        A, V, C, T = S.symbols("A V C T")
        coordinates = S.Matrix([a, x, c, z])
        adapted = S.Matrix([A, V, C, T])
        v = x+a*x*x/2-a*a*z
        sigma = S.cancel(z+(v*v-x*x)/(2*a))
        S.Poly(sigma, *coordinates)
        forward = S.Matrix([a, v, c, sigma])
        inverse_x = V-A*V*V/2+A*A*T
        inverse_z = S.cancel(T+(inverse_x*inverse_x-V*V)/(2*A))
        S.Poly(inverse_z, *adapted)
        inverse = S.Matrix([A, inverse_x, C, inverse_z])
        self.zero(inverse.subs(dict(zip(adapted, forward)), simultaneous=True)-coordinates)
        self.zero(forward.subs(dict(zip(coordinates, inverse)), simultaneous=True)-adapted)
        velocity = S.Matrix([0, a*a, 0, 1+a*x])
        self.zero(self.act(velocity, forward, coordinates)-S.Matrix([0, 0, 0, 1]))
        q, degree, H = self.check_certificate(coordinates, velocity, sigma, 5)
        self.zero(q-a**3)
        # I=(a^2), q=a^3: one extra divisor copy is attained, but q not in I^2.
        self.assertEqual(S.rem(q, a**4, a), q)
        N = (degree-1)**2
        self.assertEqual(N, 16)
        self.assertEqual(S.rem(q**N, a**(2*(N+1)), a), 0)
        for k, value in H.items():
            self.assertEqual(S.rem(S.expand(value), a**(2*k), a), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
