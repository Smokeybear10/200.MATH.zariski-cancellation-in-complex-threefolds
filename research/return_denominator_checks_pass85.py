"""Two actual-action controls for a reduced return and its centered invariant pair."""

import unittest

import sympy as S


class ReturnDenominatorChecks(unittest.TestCase):
    def zero(self, value):
        entries = list(value) if isinstance(value, S.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(S.cancel(S.expand(entry)), 0)

    def test_common_factor_removed_from_actual_return(self):
        a, x, c, z = S.symbols("a x c z")
        A, V, C, T = S.symbols("A V C T")
        original = S.Matrix([a, x, c, z])
        adapted = S.Matrix([A, V, C, T])
        v = (a-1)*(x+a*x*x/2)-a*a*z
        H = lambda aa, vv: -vv-aa*vv-aa*vv*vv/2
        sigma = S.cancel((x-H(a, v))/a**2)
        forward = S.Matrix([a, v, c, sigma])
        inverse_x = H(A, V)+A*A*T
        inverse_z = S.cancel(((A-1)*(inverse_x+A*inverse_x**2/2)-V)/A**2)
        inverse = S.Matrix([A, inverse_x, C, inverse_z])
        # Apparent a^2 denominators cancel in the actual coordinate maps.
        S.Poly(sigma, *original, domain=S.QQ)
        S.Poly(inverse_z, *adapted, domain=S.QQ)
        self.zero(forward.subs(dict(zip(original, inverse)), simultaneous=True)-adapted)
        self.zero(inverse.subs(dict(zip(adapted, forward)), simultaneous=True)-original)

        b = (a-1)*(1+a*x)
        velocity = S.Matrix([0, a*a, 0, b])
        def act(value):
            def scalar(f):
                return S.expand(sum(p*S.diff(f, y) for p, y in zip(velocity, original)))
            return value.applyfunc(scalar) if isinstance(value, S.MatrixBase) else scalar(value)
        self.zero(act(forward)-S.Matrix([0, 0, 0, 1]))
        acceleration = act(velocity)
        q = a**3*(a-1)
        self.zero(acceleration-S.Matrix([0, 0, 0, q]))
        self.zero(act(acceleration))
        self.assertNotEqual(q, 0)

        # I=(a^2) is proper; b and its common factor with q are units modulo I.
        self.zero(S.rem(b*(-1-a*(1-x))-1, a*a, a))
        self.zero((a-1)*(-1-a)-(1-a*a))
        self.zero(S.gcd(b, q)-(a-1))
        self.zero(S.cancel(q/S.gcd(b, q))-a**3)
        tau = S.cancel(-2*b/q)
        self.zero(tau+2*(1+a*x)/a**3)
        rho = S.Matrix([a, S.cancel(x+tau*a*a), c, z])
        self.zero(rho-S.Matrix([a, -x-2/a, c, z]))
        substitution = dict(zip(original, rho))
        self.zero(rho.subs(substitution, simultaneous=True)-original)
        self.zero(q.subs(substitution, simultaneous=True)-q)
        self.zero(b.subs(substitution, simultaneous=True)+b)
        self.zero(sigma.subs(substitution, simultaneous=True)-sigma-tau)
        self.zero(rho.jacobian(original).det()+1)

        # Evaluate only the reduced rational functions at the removed divisor.
        self.zero(b.subs(a, 1))
        self.zero(q.subs(a, 1))
        self.zero(rho.subs(a, 1)-S.Matrix([1, -x-2, c, z]))
        self.zero(tau.subs(a, 1)+2*(1+x))
        numerator, denominator = S.fraction(S.cancel(rho[1]))
        self.zero(denominator-a)
        self.zero(numerator.subs(a, 0)+2)

    def test_centered_two_speed_pair_and_fibers(self):
        s, a, b, c = S.symbols("s a b c")
        A, X, Y, Z = S.symbols("A X Y Z")
        old = S.Matrix([s, a, b, c])
        original = S.Matrix([A, X, Y, Z])
        x, y = b+a*s, c+b*s
        forward = S.Matrix([a, x, y, s+x*y])
        sigma = Z-X*Y
        invariant_b = X-A*sigma
        inverse = S.Matrix([sigma, A, invariant_b, Y-invariant_b*sigma])
        self.zero(inverse.subs(dict(zip(original, forward)), simultaneous=True)-old)
        self.zero(forward.subs(dict(zip(old, inverse)), simultaneous=True)-original)

        h, v = 2*a*b, 1+a*c+b*b
        bad_speed = S.diff(forward[3], s)
        self.zero(bad_speed-h*s-v)
        self.zero(forward.diff(s, 2)-S.Matrix([0, 0, 0, h]))
        self.zero(forward.diff(s, 3))
        self.zero(S.gcd(h, bad_speed)-1)
        self.zero(S.gcd(h, v)-1)
        centered = h*s*s+2*v*s
        self.zero(forward[3]-b*c-centered/2)
        reflection = -s-2*v/h
        self.zero(centered.subs(s, reflection)-centered)
        self.zero((h*s+v).subs(s, reflection)+(h*s+v))
        self.zero((h*s+v)**2-v*v-h*centered)
        self.zero(reflection.subs(s, reflection)-s)
        self.zero(forward[3].subs(s, reflection)-forward[3])

        # A common zero of the coprime pair lies outside the speed-zero set.
        common_zero = {a: 0, b: S.I}
        self.zero(h.subs(common_zero))
        self.zero(v.subs(common_zero))
        self.zero(centered.subs(common_zero))
        self.assertNotEqual(b.subs(common_zero), 0)
        # At actual speed zeros the quotient map is linear, not constant.
        speed_zero = {a: 0, b: 0}
        self.zero(h.subs(speed_zero))
        self.zero(v.subs(speed_zero)-1)
        self.zero(centered.subs(speed_zero)-2*s)
        self.assertEqual(S.Poly(centered.subs({a: 1, b: 1, c: 0}), s).degree(), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
