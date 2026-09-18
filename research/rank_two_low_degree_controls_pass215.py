"""Independent finite algebra controls for the three pass215 notes.

These are polynomial identities and bounded controls, not universal proofs
of determinant support, conductor geometry, actual field return or descent.
Only the specified complex-coefficient shears represent ambient maps.
No retained checker or solver is imported or executed.
"""

import unittest

import sympy as s


class RankTwoLowDegreeControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_quadratic_center_affine_second_leading_contradiction(self):
        U, V = s.symbols("U V")
        rho, h, p2 = s.symbols("rho h p2", nonzero=True)
        ht, p1, p0 = s.symbols("ht p1 p0")
        a4, b32 = h**2 / (4 * rho**3), 2 * ht / (3 * rho**6)
        b31, b30 = s.symbols("b31 b30")
        B2 = sum(co * V**i for i, co in enumerate(s.symbols("b20:24")))
        B1 = sum(co * V**i for i, co in enumerate(s.symbols("b10:15")))
        B0 = sum(co * V**i for i, co in enumerate(s.symbols("b00:07")))
        H = a4 * U**4 + (b32 * V**2 + b31 * V + b30) * U**3
        H += B2 * U**2 + B1 * U + B0
        P = p2 * V**2 + p1 * V + p0
        value = s.Poly(s.expand(H.subs(U, P)), V)
        derivative = s.Poly(s.expand(s.diff(H, U).subs(U, P)), V)
        self.zero(value.nth(8) - p2**3 * (a4 * p2 + b32))
        self.zero(derivative.nth(6) - p2**2 * (4 * a4 * p2 + 3 * b32))
        forced_ht = -3 * rho**6 * a4 * p2 / 2
        self.zero(value.nth(8).subs(ht, forced_ht))
        self.zero(derivative.nth(6).subs(ht, forced_ht) - a4 * p2**3)
        self.assertNotEqual(s.cancel(a4 * p2**3), 0)
        self.zero(value.nth(8).subs(ht, 0) - a4 * p2**4)
        # The supplied upper degree bounds, not arbitrary curves, are tested.
        self.assertEqual(s.Poly(B2, V).degree(), 3)
        self.assertEqual(s.Poly(B1, V).degree(), 4)
        self.assertEqual(s.Poly(B0, V).degree(), 6)

    def test_cubic_quadratic_center_fiber_and_cofactor_comparison(self):
        x, U, V, c0, c1, a0, a1, a2 = s.symbols("x U V c0 c1 a0 a1 a2")
        A2, a3, rho, h, beta = s.symbols("A2 a3 rho h beta", nonzero=True)
        theta = A2 * x**2 + c0
        y = a3 * x**3 + a2 * x**2 + a3 * c1 * x + a0
        Vc, yc = c0 - A2 * c1, a0 - a2 * c1
        R = 2 * (V - Vc) / rho**3
        J = a0 + a2 * (V - c0) / A2
        G = (U - J)**2 - a3**2 * (V - c0) * (V - Vc)**2 / A2**3
        self.zero(G.subs({U: y, V: theta}, simultaneous=True))
        self.zero(G.subs(V, Vc) - (U - yc)**2)
        self.zero(R.subs(V, theta) - 2 * A2 * (x**2 + c1) / rho**3)
        self.zero(y - yc - (x**2 + c1) * (a3 * x + a2))
        self.zero(s.Poly(s.expand(G), U).LC() - 1)
        self.assertEqual(s.Poly(s.expand(G), U, V).total_degree(), 3)
        self.zero(s.discriminant(G, U) - 4 * a3**2 * (V - c0) * (V - Vc)**2 / A2**3)
        self.zero(G.subs({V: c0, c1: 0}, simultaneous=True) - (U - a0)**2)
        # Bounded parity controls for the conductor, including its double root.
        z = s.symbols("z")
        even = sum(co * z**i for i, co in enumerate(s.symbols("e0:4")))
        odd = sum(co * z**i for i, co in enumerate(s.symbols("o0:4")))
        member = (x**2 + c1) * (even.subs(z, x**2) + x * odd.subs(z, x**2))
        self.zero(member - ((z + c1) * even).subs(z, x**2)
                  - (x**3 + c1 * x) * odd.subs(z, x**2))
        self.zero(x * member - (x**3 + c1 * x) * even.subs(z, x**2)
                  - (z * (z + c1) * odd).subs(z, x**2))
        ys = s.symbols("ys")
        alpha = h**2 / (4 * rho**3)
        p = h * (U - yc) * (U - ys) / 2
        Qcenter = alpha * (U - ys)**2
        self.zero((U - yc)**2 * Qcenter - p**2 / rho**3)
        difference = s.Poly(s.expand(Qcenter - alpha * (U - yc)**2 - beta), U)
        self.zero(difference.nth(1) - 2 * alpha * (yc - ys))
        self.zero(difference.as_expr().subs(ys, yc) + beta)
        self.zero(Qcenter.subs(U, yc) - alpha * (yc - ys)**2)

    def test_linear_center_local_order_and_coefficient_equations(self):
        b, r, eta, J = s.symbols("b r eta J", nonzero=True)
        pt, pr, pv, wt, wr, wp, C, Lt, Lr = s.symbols("pt pr pv wt wr wp C Lt Lr")
        determinant = s.Matrix([[pt, pr, pv], [b, C, 0], [wt, wr, wp]]).det()
        # At the center, C=0 forces pv=0, Lr=0, then pr=0 in succession.
        first_v = b * pv + C
        second_v = -Lt * pv - Lr + C * wp
        first_r = b * pr - Lr
        self.zero(first_v.subs(C, 0) - b * pv)
        self.zero(second_v.subs({C: 0, pv: 0}, simultaneous=True) + Lr)
        self.zero(first_r.subs(Lr, 0) - b * pr)
        self.zero(determinant.subs({C: 0, pv: 0, pr: 0}, simultaneous=True))
        q = -r * (C * b + r * Lt)
        self.zero(s.cancel(q / r).subs(r, 0) + C * b)
        self.zero(-(-J * r / eta) * (eta * r) - r**2 * J)

        V, rho, delta, p2, p1, p0, j = s.symbols("V rho delta p2 p1 p0 j", nonzero=True)
        RR = 2 * V / rho**3 + j
        A = b**2 / rho**3 + delta * RR**2 / 4
        P = p2 * V**2 + p1 * V + p0
        DD = s.Poly(s.expand(eta * RR - 2 * A * P), V)
        CC = s.Poly(s.expand(A * P**2 - eta * RR * P), V)
        self.zero(CC.nth(6) - delta * p2**2 / rho**6)
        self.zero(DD.nth(4) + 2 * delta * p2 / rho**6)
        self.zero(DD.nth(3) + 2 * delta * p1 / rho**6 + 2 * delta * j * p2 / rho**3)
        self.assertLessEqual(s.Poly(CC.as_expr().subs(delta, 0), V).degree(), 4)

    def test_scalar_euler_reduction_and_actual_normalization(self):
        rho, c = s.symbols("rho c", nonzero=True)
        T = s.Function("T")(rho)
        K = s.Function("K")(rho)
        delta = -rho**3 * T**2
        p2 = rho**-4 / T
        w2 = (T - K) / (2 * rho * T)
        first = rho**3 * K * p2 - (delta + rho * s.diff(delta, rho)) / (delta * rho)
        expected_first = K / (rho * T) - 4 / rho - 2 * s.diff(T, rho) / T
        second = -s.diff(p2, rho) / (2 * p2) - 2 * w2
        expected_second = 1 / rho + K / (rho * T) + s.diff(T, rho) / (2 * T)
        self.zero(first - expected_first)
        self.zero(second - expected_second)
        self.zero(first - second + 5 / rho + s.Rational(5, 2) * s.diff(T, rho) / T)
        self.zero((first - second).subs(T, c / rho**2).doit())
        d, c0 = s.symbols("d c0")
        kt = c0 - c / rho - d / (2 * rho**2)
        KK = s.diff(kt, rho)
        self.zero(KK - c / rho**2 - d / rho**3)
        self.zero(3 * KK + rho * s.diff(KK, rho) - c / rho**2)
        self.zero(kt + d / (2 * rho**2) - c0 + c / rho)
        Knew, Tnew = c / rho**2, c / rho**2
        self.zero((Tnew - Knew) / (2 * rho * Tnew))
        self.zero(rho**-3 - c / rho / (c * rho**2))
        X, Y, Z, W, xp, yp, zp, wp = s.symbols("X Y Z W xp yp zp wp")
        forward = (X, Y, Z - c0 * Y, W + d * Y / 2)
        inverse = (xp, yp, zp + c0 * yp, wp - d * yp / 2)
        for target, expression in zip((X, Y, Z, W), inverse):
            self.zero(expression.subs(dict(zip((xp, yp, zp, wp), forward)), simultaneous=True) - target)
        for target, expression in zip((xp, yp, zp, wp), forward):
            self.zero(expression.subs(dict(zip((X, Y, Z, W), inverse)), simultaneous=True) - target)
        self.assertEqual(tuple(s.diff(value, Z) for value in forward), (0, 0, 1, 0))
        theta, p1, tau, lam, kap = s.symbols("theta p1 tau lambda kappa")
        action = lambda expression: tau * s.diff(expression, theta)
        PY = tau * (2 * theta / (c * rho**2) + p1)
        self.zero(action(PY) - 2 * tau**2 / (c * rho**2))
        self.zero(action(action(PY)))
        self.zero(action(tau * (X + lam)))
        self.zero(action(tau * (kap - X / rho**2)))


if __name__ == "__main__":
    unittest.main()
