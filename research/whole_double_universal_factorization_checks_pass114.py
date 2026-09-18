"""Two finite controls for the whole-double universal factorization.

The first checks polynomial certificates without imposing a relation by
division or assuming a reduced quotient. The second checks five formal
root coefficients and a truncated cofactor for one coefficient tuple
with nonsmooth a,b. Neither constructs an actual frame nor certifies
an all-order root, analytic-prime support, geometric hypotheses, or
cancellation. No solver or retained checker is imported.
"""

import unittest

import sympy as sp


class WholeDoubleUniversalFactorizationChecks(unittest.TestCase):
    def test_denominator_free_factor_and_ideal_certificates(self):
        a, b, h, s, u, v, eta, z, t, rho, T = sp.symbols(
            "a b h s u v eta z t rho T"
        )
        E = b**2 - s * h - a**2 * u - a * b * v
        zeta = a * z + b * t
        P = a * h + b * (h * eta + a * zeta)
        F = (T + eta) * (1 - T**2 * u - T * v) + s * T**2 * z + s * T * t
        D, L = 1 - rho**2 * u - rho * v, a - rho * b
        M = u * (a + rho * b) + b * v
        Knum = rho * b * (rho * z + t)
        Hnum = D * (h + b * zeta + rho * b**2 * z) + Knum * M
        Cnum = D * (2 * rho * z + t) + rho * (rho * z + t) * (2 * rho * u + v)

        self.assertEqual(sp.expand(D * P - L * Hnum
                                   - b * h * F.subs(T, rho) - Knum * E), 0)
        self.assertEqual(sp.expand(D * b**2 - s * h - L * M - E), 0)
        self.assertEqual(sp.expand(Hnum - D * h - b**2 * Cnum
                                   - L * (D * b * z + u * Knum)), 0)
        # This is the unit-modulo-L ideal equality with all denominators cleared.
        self.assertEqual(sp.expand(D * Hnum - (D**2 + s * Cnum) * h
                                   - L * (D**2 * b * z + D * u * Knum + Cnum * M)
                                   - Cnum * E), 0)
        self.assertEqual(sp.expand(a * b - L * b - rho * b**2), 0)
        self.assertEqual(sp.expand(a**2 - L * (a + rho * b) - rho**2 * b**2), 0)

        self.assertEqual(F.subs(T, 0), eta)
        self.assertEqual(sp.expand(sp.diff(F, T).subs(T, 0) - (1 - eta * v + s * t)), 0)
        self.assertEqual(sp.diff(F, T).subs({T: 0, eta: 0, z: 0, t: 0}), 1)
        self.assertEqual(D.subs(rho, 0), 1)
        self.assertEqual(Cnum.subs({rho: 0, z: 0, t: 0}), 0)
        self.assertEqual((D**2 + s * Cnum).subs({rho: 0, z: 0, t: 0}), 1)

    def test_finite_root_and_cofactor_for_singular_coefficients(self):
        x, y, T = sp.symbols("x y T")

        def homogeneous(value, degree):
            return sp.Add(*(coefficient * x**i * y**j
                            for (i, j), coefficient in sp.Poly(
                                sp.expand(value), x, y).terms() if i + j == degree))

        def truncate(value, bound):
            return sp.Add(*(coefficient * x**i * y**j
                            for (i, j), coefficient in sp.Poly(
                                sp.expand(value), x, y).terms() if i + j < bound))

        def order(value):
            polynomial = sp.Poly(sp.expand(value), x, y)
            if polynomial.is_zero:
                return sp.oo
            return min(i + j for (i, j), _ in polynomial.terms())

        a, b = x**2, y**2
        h = b**2 - a**2 - a * b
        eta, z, t = x + y, x - y, x + 2 * y
        s = u = v = sp.Integer(1)
        self.assertEqual(sp.expand(b**2 - s * h - a**2 * u - a * b * v), 0)
        zeta = a * z + b * t
        P = sp.expand(a * h + b * (h * eta + a * zeta))
        F = (T + eta) * (1 - T**2 * u - T * v) + s * T**2 * z + s * T * t
        root = sp.Integer(0)
        for degree in range(1, 6):
            root -= homogeneous(F.subs(T, root), degree)
            self.assertEqual(truncate(F.subs(T, root), degree + 1), 0)
        self.assertGreaterEqual(order(F.subs(T, root)), 6)
        self.assertEqual(homogeneous(root, 1), -x - y)

        D = 1 - root**2 * u - root * v
        inverse, power = sp.Integer(1), sp.Integer(1)
        for _ in range(1, 6):
            power = truncate(power * (1 - D), 6)
            inverse += power
        self.assertEqual(truncate(D * inverse - 1, 6), 0)

        L = a - root * b
        M = u * (a + root * b) + b * v
        Knum = root * b * (root * z + t)
        H = truncate(h + b * zeta + root * b**2 * z + Knum * inverse * M, 10)
        self.assertEqual(order(L), 2)
        self.assertEqual(order(H), 4)
        self.assertGreaterEqual(order(P - L * H), 12)
        # These are only finite approximations to the completed factorization.
        self.assertNotEqual(sp.expand(P - L * H), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
