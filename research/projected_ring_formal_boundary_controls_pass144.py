"""Finite exact controls for the projected-ring criterion and its boundary.

Only the first method's two fixtures are actual polynomial coordinate
frames. The other methods use an explicitly noninvertible polynomial
tuple with a sliced source E and a polynomial, non-LND source T. Its
unit relative Jacobian and formal tails are not actualness certificates.
Finite examples do not prove the ring criterion, universal recognition,
or automatic base compatibility. No prior checker or solver is imported.
"""

import unittest

import sympy as sp


class ProjectedRingFormalBoundaryControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def inverse_orders(self, forward, source, target, inverse):
        for value, expected in zip(inverse, source):
            self.zero(value.subs(dict(zip(target, forward)), simultaneous=True) - expected)
        for value, expected in zip(forward, target):
            self.zero(value.subs(dict(zip(source, inverse)), simultaneous=True) - expected)

    def test_actual_constant_and_nonconstant_speed_projection(self):
        u, a, b, c, v, X, Y, Z, W = sp.symbols("u a b c v X Y Z W")
        targets = (X, Y, Z, W)
        forward = (u, a + b * u, b + c * u, c)
        inverse = (X, Y - (Z - W * X) * X, Z - W * X, W)
        self.inverse_orders(forward, (u, a, b, c), targets, inverse)
        self.zero(sp.diff(forward[0], u) - 1)
        projected = [sp.expand(f.subs(u, 0)) for f in forward[1:]]
        self.assertEqual(projected, [a, b, c])
        self.zero(u - forward[0])

        # Actual nonconstant-speed cover. The projected slice u0 is
        # -v/a^2, a specific rational invariant outside C[a,b,v].
        forward = (v + a**2 * u, a + b * u, b + u, u)
        recovered_a = Y - (Z - W) * W
        inverse = (W, recovered_a, Z - W, X - recovered_a**2 * W)
        self.inverse_orders(forward, (u, a, b, v), targets, inverse)
        fx, fy, fz, fw = forward
        speed = sp.diff(fx, u)
        u0 = sp.cancel(u - fx / speed)
        self.zero(speed - a**2)
        self.zero(u0 + v / a**2)
        numerator, denominator = sp.fraction(u0)
        self.zero(numerator + v)
        self.zero(denominator - a**2)
        self.assertEqual(sp.gcd(numerator, denominator), 1)
        y, z, w0 = [sp.cancel(value.subs(u, -v / a**2)) for value in (fy, fz, fw)]
        self.zero(w0 - u0)
        self.zero(y - (z - w0) * w0 - a)
        self.zero(z - w0 - b)
        self.zero(-(y - (z - w0) * w0)**2 * w0 - v)
        self.zero(fx - speed * (u - u0))

    def test_polynomial_source_partial_is_not_locally_nilpotent(self):
        u, a, beta, q = sp.symbols("u a beta q")
        X = a**2 * u
        Y = q + a**3 * u
        Z = a - a * beta * u / 2
        W = beta - beta**2 * u / 4
        forward = (X, Y, Z, W)

        def selected(f):
            return sp.expand(a * u * sp.diff(f, a) / 2
                             + (1 + beta * u / 2) * sp.diff(f, beta)
                             - a**3 * u**2 * sp.diff(f, q) / 2
                             - u**2 * sp.diff(f, u))

        for f, expected in zip(forward, (0, 0, 0, 1)):
            self.zero(selected(f) - expected)
        self.zero(selected(W + Y**2) - 1)
        for n in range(1, 5):
            value = u
            for _ in range(n):
                value = selected(value)
            self.zero(value - (-1)**n * sp.factorial(n) * u ** (n + 1))
        # The all-n non-LND conclusion is the written induction, not
        # a finite failure-to-vanish test.
        jacobian = sp.Matrix(forward).jacobian((u, a, beta, q)).det()
        self.zero(jacobian - a**2)
        self.zero(Z**2 + X * W - a**2)
        speeds = [sp.diff(f, u) for f in forward[:3]]
        self.assertEqual(speeds, [a**2, a**3, -a * beta / 2])
        tau, rho = a, -beta / (2 * a)
        self.zero(sp.Matrix((tau, rho)).jacobian((a, beta)).det() + 1 / (2 * a))
        for f in forward[:3]:
            self.zero(sp.diff(f, u, 2))

        def top(f):
            return -a**3 * sp.diff(f, q) / 2

        for f in (a, beta, q):
            self.zero(sp.Poly(selected(f), u).nth(2) - top(f))
        for f in (a, beta, *speeds):
            self.zero(top(f))
        self.zero(top(q) + a**3 / 2)
        intrinsic = -2 * a * q
        self.zero(top(intrinsic) / speeds[0]**2 - 1)
        for f, expected in zip(forward[1:], (q, a, beta)):
            self.zero(f.subs(u, 0) - expected)

        # Conditional rational branch reconstruction, not a polynomial
        # inverse. The residual vanishes only after imposing A^2=Q.
        x, y, z, w, A = sp.symbols("x y z w A")
        Q = z**2 + x * w
        branch = {u: x / A**2, a: A, beta: 2 * A * (A - z) / x, q: y - A * x}
        errors = (0, 0, 0, (A**2 - Q) / x)
        for f, target, error in zip(forward, (x, y, z, w), errors):
            self.zero(f.subs(branch, simultaneous=True) - target - error)
        self.assertEqual(sp.gcd(x, z**2), 1)
        # The proof, not this coefficient gcd alone, deduces that Q
        # has an odd prime valuation and the inverse field has degree2.

    def test_quadratic_bad_slot_retains_formal_base_failure(self):
        X, tau, rho, v, U, V = sp.symbols("X tau rho v U V")
        y, z = -v / (2 * tau), tau
        Y, Z = y + tau * X, z + rho * X
        W = -2 * tau * rho - rho**2 * X
        self.zero(sp.Matrix((Y, Z, W)).jacobian((tau, rho, v)).det() - 1)

        def H(f, order):
            return sp.expand(sum((sp.diff(f, tau, i, rho, order - i)
                                  * U**i * V ** (order - i)
                                  / (sp.factorial(i) * sp.factorial(order - i))
                                  for i in range(order + 1)), sp.S.Zero))

        tails = []
        for coefficients in ((0, -rho**2), (0, -rho**2, tau**2)):
            fm1 = tau**2
            omega = sum((H(f, j) for j, f in enumerate(coefficients)), sp.S.Zero)
            phi = -sum((H(f, j + 1) for j, f in enumerate(coefficients)), sp.S.Zero) - fm1
            psi = -sum((H(f, j + 2) for j, f in enumerate(coefficients)), sp.S.Zero) - H(fm1, 1)
            self.zero(phi - V**2 + tau**2)
            self.zero(psi + 2 * tau * U)
            self.zero(psi.subs({U: y, V: z}, simultaneous=True) - v)
            tails.append((omega, phi, psi))
        self.zero(tails[1][0] - tails[0][0] - U**2)
        self.zero(Y**2 - sum((X ** (2 - j) * H(tau**2, j).subs(
            {U: y, V: z}, simultaneous=True) for j in range(3)), sp.S.Zero))

        a, beta, q, u = sp.symbols("a beta q u")
        source_substitution = {tau: a, rho: -beta / (2 * a), v: -2 * a * q, X: a**2 * u}
        forward = [f.subs(source_substitution, simultaneous=True) for f in (X, Y, Z, W + Y**2)]
        self.zero(sp.diff(forward[3], u, 2) - 2 * a**6)
        self.zero(sp.diff(forward[3], u, 3))
        self.zero(sp.Matrix(forward).jacobian((u, a, beta, q)).det() - a**2)
        omega2 = tails[1][0].subs({tau: a, rho: -beta / (2 * a)}, simultaneous=True)
        returned_s, returned_t = V**2, V**3
        returned_b = -V * (omega2 - U**2) / 2
        self.zero(returned_s.subs(V, -a) - a**2)
        self.zero(returned_b.subs(V, -a) + a * beta / 2)
        self.zero((returned_t - a * returned_s).subs(V, -a) + 2 * a**3)
        self.zero((returned_b + beta * returned_s / (2 * a)).subs(V, -a))
        self.assertNotEqual(sp.expand(-2 * a**3), 0)


if __name__ == "__main__":
    unittest.main()
