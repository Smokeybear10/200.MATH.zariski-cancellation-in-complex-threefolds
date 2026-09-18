"""Finite actual-return, failed-lift and ideal controls, not universal proofs."""

import unittest

import sympy as S


class RankOneReturnChecks(unittest.TestCase):
    def zero(self, value):
        entries = list(value) if isinstance(value, S.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(S.cancel(S.expand(entry)), 0)

    @staticmethod
    def act(velocity, value, variables):
        def scalar(f):
            return S.expand(sum(v*S.diff(f, x) for v, x in zip(velocity, variables)))
        return value.applyfunc(scalar) if isinstance(value, S.MatrixBase) else scalar(value)

    def test_actual_two_speed_return_and_frozen_taylor_equation(self):
        s, a, b, c = S.symbols("s a b c")
        A, X, Y, Z, t = S.symbols("A X Y Z t")
        old, coordinates = S.Matrix([s, a, b, c]), S.Matrix([A, X, Y, Z])
        x, y = b+a*s, c+b*s
        forward = S.Matrix([a, x, y, s+x*y])
        sigma, invariant_b = Z-X*Y, X-A*(Z-X*Y)
        inverse = S.Matrix([sigma, A, invariant_b, Y-invariant_b*sigma])
        self.zero(inverse.subs(dict(zip(coordinates, forward)), simultaneous=True)-old)
        self.zero(forward.subs(dict(zip(old, inverse)), simultaneous=True)-coordinates)
        velocity = S.Matrix([0, A, invariant_b, 1+A*Y+invariant_b*X])
        self.zero(forward.diff(s).subs(dict(zip(old, inverse)), simultaneous=True)-velocity)
        self.zero(self.act(velocity, inverse, coordinates)-S.Matrix([1, 0, 0, 0]))
        acceleration = self.act(velocity, velocity, coordinates)
        self.zero(acceleration-S.Matrix([0, 0, 0, 2*A*invariant_b]))
        self.zero(self.act(velocity, acceleration, coordinates))

        good = S.Matrix([A, X, Y])
        f = velocity[:3, :].subs(Z, 0)
        b0, q0 = velocity[3].subs(Z, 0), acceleration[3].subs(Z, 0)
        r = 1+A*Y
        self.zero(f-S.Matrix([0, A, X*r]))
        self.zero(b0-r*(1+X*X))
        self.zero(q0-2*A*X*r)
        rho = (good-2*b0*f/q0).applyfunc(S.cancel)
        substitution = dict(zip(good, rho))
        self.zero(rho[1]+1/X)
        self.zero(1+A*rho[2]+X*X*r)
        self.zero(f.subs(substitution, simultaneous=True)-f)
        self.zero(q0.subs(substitution, simultaneous=True)-q0)
        self.zero(b0.subs(substitution, simultaneous=True)+b0)
        self.zero(rho.subs(substitution, simultaneous=True)-good)
        self.zero((-2*b0/q0)*b0+(-2*b0/q0)**2*q0/2)

        # Simultaneous substitution freezes f at the original good point.
        shifted = S.Poly(S.expand(b0.subs(dict(zip(good, good+t*f)), simultaneous=True)), t)
        degree = S.Poly(b0, *good).total_degree()
        self.assertEqual(degree, 4)
        monic_value = q0**degree
        for k in range(1, degree+1):
            Hk = S.factor(S.factorial(k)*shifted.nth(k))
            coefficient = (-1)**k*(2*b0)**(k-1)*Hk/S.factorial(k)
            # Here the actual specialized ideal (A,X*r) equals (A,X).
            power = S.groebner([A**j*X**(k-j) for j in range(k+1)], A, X, Y)
            self.zero(power.reduce(S.expand(coefficient))[1])
            monic_value += coefficient*q0**(degree-k)
        self.zero(monic_value)
        self.assertNotEqual(S.factorial(3)*shifted.nth(3), 0)
        # rho has a pole at X=0 even though this example has q0 in I0.
        self.assertEqual(S.fraction(rho[1])[1], X)

    def test_integrable_isolated_jet_and_failed_full_lift(self):
        x, y, z, s, e, h, t, lam = S.symbols("x y z s e h t lambda")
        f3 = e**3*x**4/4+e*x*z+h*y*y-e*e*x*x*y
        f = S.Matrix([y, z, f3])
        L = f.jacobian([x, y, z])
        q0, b0 = -e*x, S.Integer(1)
        domain = S.QQ.frac_field(e, h)
        ideal = S.groebner(list(f), x, y, z, domain=domain)
        standard = S.groebner([y, z, x**4], x, y, z, domain=domain)
        for generator in f:
            self.zero(standard.reduce(generator)[1])
        for generator in (y, z, x**4):
            self.zero(ideal.reduce(generator)[1])
        reduce = lambda p: ideal.reduce(S.expand(p))[1]
        self.zero(reduce(q0**4))
        self.zero(reduce(q0**3)+e**3*x**3)
        self.assertNotEqual(reduce(q0**3), 0)
        self.zero(reduce(q0**3+b0**3*L.det()))
        for generator in (x, y, z):
            self.zero(reduce(generator*q0**3))
        quotient_flow = S.Poly(S.expand((1+t*q0)*(S.eye(3)+t*L).det()-1), t)
        for coefficient in quotient_flow.all_coeffs():
            self.zero(reduce(coefficient))
        N = L.row_join(S.zeros(3, 1)).col_join(S.Matrix([[0, 0, 0, q0]]))
        for coefficient in S.Poly(N.charpoly(lam).as_expr()-lam**4, lam).all_coeffs():
            self.zero(reduce(coefficient))
        for entry in N**4:
            self.zero(reduce(entry))

        attempted = S.Matrix([x+s*y, y+s*z, z+s*f3, s-e*x*s*s/2])
        failure = S.Poly(S.expand(attempted.jacobian([x, y, z, s]).det()-1), s)
        expected = {
            0: 0,
            1: 0,
            2: y*(e-4*h)/2,
            3: -e*(3*e*x*y-4*h*x*y-z)/2,
            4: -e*(7*e**3*x**4-16*e**2*x*x*y+8*e*x*z+4*h*y*y)/8,
        }
        self.assertLessEqual(failure.degree(), 4)
        for k, value in expected.items():
            self.zero(failure.nth(k)-value)
        # Killing the second coefficient cannot kill the third when e != 0.
        self.assertEqual(S.Poly(failure.nth(3).subs(h, e/4), z).nth(1), e/2)
        # A nonzero constant b0 also contradicts the actual return sign.
        self.assertEqual(b0+b0, 2)
        # f is an actual polynomial triple, but this is not an ambient action.

    def test_integral_closure_is_not_membership_and_jet_valuation(self):
        x, y, z, tau, e, h = S.symbols("x y z tau e h")
        ideal = S.groebner([x*x, y*y], x, y, z)
        square = S.groebner([x**4, x*x*y*y, y**4], x, y, z)
        q = x*y
        self.assertEqual(ideal.reduce(q)[1], q)
        monic = tau*tau-x*x*y*y
        self.zero(monic.subs(tau, q))
        self.zero(square.reduce(-x*x*y*y)[1])
        self.zero(square.reduce(q*q)[1])

        # One weighted monomial valuation separates the preceding jet from
        # integral closure: v(x)=1, v(y)=v(z)=4, v(e)=v(h)=0.
        f = [y, z, e**3*x**4/4+e*x*z+h*y*y-e*e*x*x*y]
        field = S.QQ.frac_field(e, h)
        weight = lambda p: min(i+4*j+4*k for (i,j,k), coefficient in S.Poly(p, x, y, z, domain=field).terms())
        self.assertEqual(min(map(weight, f)), 4)
        self.assertEqual(weight(-e*x), 1)
        # This checks finite weights, not the general ideal-valuative theorem.


if __name__ == "__main__":
    unittest.main(verbosity=2)
