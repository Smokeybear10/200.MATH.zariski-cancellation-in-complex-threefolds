"""Two scoped exact controls for projected-derivation behavior103.

Method one is an abstract derivation with locally nilpotent reductions
at finite thickenings but nonzero global iterates. Method two is an
actual polynomial three-good coordinate frame with non-LND projected
D0, explicitly without a stable closed base fiber. Neither control
verifies the universal associated-graded/flat geometric proof.
"""

import math
import unittest

import sympy as S


class ProjectedDerivationThickeningChecks(unittest.TestCase):
    def test_abstract_finite_thickenings_without_global_nilpotence(self):
        x, r, tau, eta, Y = S.symbols("x r tau eta Y")

        def D(expr):
            return S.expand(S.diff(expr, r) + x**2*S.diff(expr, x))

        value = x
        for n in range(8):
            self.assertEqual(value, math.factorial(n)*x**(n+1))
            self.assertNotEqual(value, 0)
            value = D(value)
        self.assertEqual(D(r), 1)
        self.assertEqual(D(D(r)), 0)

        for k in range(1, 7):
            with self.subTest(thickening=k):
                def red(expr):
                    return S.expand(S.rem(S.expand(expr), x**k, x))

                flow_x = S.Add(*(tau**(j-1)*x**j for j in range(1, k)))
                flow_eta = flow_x.subs(tau, eta)
                composition = red(flow_x.subs(x, flow_eta))
                self.assertEqual(composition, red(flow_x.subs(tau, tau+eta)))
                inverse = red(flow_x.subs(x, flow_x.subs(tau, -tau)))
                self.assertEqual(inverse, red(x))
                self.assertEqual(red(S.diff(flow_x, tau).subs(tau, 0)),
                                 red(D(x)))
                next_flow = sum(tau**(j-1)*x**j for j in range(1, k+1))
                self.assertEqual(red(next_flow), flow_x)
                self.assertEqual((r+tau).subs(r, r-tau), r)
                invariant_y = S.Add(*((-r)**(j-1)*x**j for j in range(1, k)))
                inverse_x = S.Add(*(r**(j-1)*Y**j for j in range(1, k)))
                self.assertEqual(red(D(invariant_y)), 0)
                self.assertEqual(red(inverse_x.subs(Y, invariant_y)-x), 0)
                self.assertEqual(S.rem(S.expand(
                    invariant_y.subs(x, inverse_x)-Y), Y**k, Y), 0)
                if k >= 2:
                    # The inverse has increasing slice degree, so compatible
                    # finite polynomial rings do not imply one bounded degree.
                    self.assertEqual(S.Poly(inverse_x, r).degree(), k-2)
                    self.assertEqual(S.Poly(inverse_x, r).LC(), Y**(k-1))
                for i, j in ((0, 3), (1, 2), (2, 1)):
                    value = x**i*r**j
                    for _ in range(j+k):
                        value = red(D(value))
                    self.assertEqual(value, 0)
        # No uniform exponent kills x as k grows.
        self.assertEqual(S.rem(D(D(x)), x**3, x), 0)
        self.assertNotEqual(S.rem(D(D(x)), x**4, x), 0)

    def test_actual_three_good_frame_with_non_lnd_zeroth_coefficient(self):
        s, a, v, p, u = S.symbols("s a v p u")
        X, Y, W, Z = S.symbols("X Y W Z")
        canonical = (s, a, v, p)
        original = (X, Y, W, Z)
        forward = S.Matrix((s, v+a**2*s, a+v**2+p*s,
                            2*a**2*v-p+a**4*s+s**2/2))
        inverse_a = X*(Z-X**2/2)-Y**2+W
        backward = S.Matrix((X, inverse_a, Y-inverse_a**2*X,
                             2*inverse_a**2*Y-inverse_a**4*X-Z+X**2/2))
        self.assertEqual(
            backward.subs(dict(zip(original, forward)), simultaneous=True)
            .applyfunc(S.expand), S.Matrix(canonical))
        self.assertEqual(
            forward.subs(dict(zip(canonical, backward)), simultaneous=True)
            .applyfunc(S.expand), S.Matrix(original))
        self.assertEqual(S.factor(forward.jacobian(canonical).det()), 1)

        T_vector = S.Matrix((0, s, -2*a*s**2, 4*a*v*s-1))

        def T(expr):
            return S.expand(sum(coef*S.diff(expr, variable)
                                for variable, coef in zip(canonical, T_vector)))

        self.assertEqual((forward.jacobian(canonical)*T_vector).applyfunc(S.expand),
                         S.Matrix((0, 0, 0, 1)))
        self.assertEqual(forward.diff(s), S.Matrix((1, a**2, p, s+a**4)))
        self.assertEqual(forward.diff(s, 2), S.Matrix((0, 0, 0, 1)))
        canonical_u = s+a**4
        self.assertEqual(T(canonical_u), 4*a**3*s)
        for element in (*canonical, canonical_u):
            value = element
            for _ in range(5):
                value = T(value)
            self.assertEqual(value, 0)

        Tu_vector = S.Matrix((T(canonical_u), T(a), T(v), T(p)))
        Tu_vector = Tu_vector.subs(s, u-a**4).applyfunc(S.expand)
        self.assertEqual(Tu_vector.diff(u, 3), S.zeros(4, 1))
        H = Tu_vector.diff(u, 2)
        self.assertEqual(H, S.Matrix((0, 0, -4*a, 0)))
        speeds = S.Matrix((1, a**2, p))
        omega = S.det(S.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(p)))
        self.assertEqual(omega, 2*a)
        nambu_values = S.Matrix([
            S.det(S.Matrix((a, p, canonical_u, element)).jacobian(canonical))
            for element in (canonical_u, a, v, p)])
        self.assertEqual(nambu_values, S.Matrix((0, 0, -1, 0)))
        self.assertEqual(H, 2*omega*nambu_values)

        zero = Tu_vector[1:, 0].subs(u, 0)

        def D0(expr):
            return S.expand(sum(coef*S.diff(expr, variable)
                                for variable, coef in zip((a, v, p), zero)))

        self.assertEqual(zero, S.Matrix((-a**4, -2*a**9, -4*a**5*v-1)))
        critical = 2*a**2*v-p-a**8/2
        self.assertEqual(S.expand(forward[3]-canonical_u**2/2-critical), 0)
        self.assertEqual(D0(critical), 1)
        value = a
        factor = 1
        for n in range(8):
            self.assertEqual(value, (-1)**n*factor*a**(1+3*n))
            self.assertNotEqual(value, 0)
            value = D0(value)
            factor *= 1+3*n

        # The actual countercontrol does not satisfy the stable-fiber premise.
        self.assertEqual(S.diff(Tu_vector[1], u), 1)
        a0, p0 = S.symbols("a0 p0")
        self.assertEqual(T(a-a0).subs({a: a0, p: p0}), s)
        self.assertNotEqual(T(a-a0).subs({a: a0, p: p0}), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
