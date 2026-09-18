"""Two finite controls for the proposed smooth-h whole-double slice.

The first method checks invariant Hensel-shear and coefficient certificates
used in the shortest smooth-h exclusion. The second is a separate optional
conic-slice control, not a necessary step of that proof. Finite formal-root
truncations accompany both. These tests do
not prove Hensel existence in all orders, actual flat division, scalar
contraction through completion, divisor primeness after base change,
or realization by an original frame. No retained checker or solver is
imported. The initial shear coefficient tau may have nonzero residue.
"""

import unittest

import sympy as sp


class WholeDoubleHenselSliceChecks(unittest.TestCase):
    def test_hensel_shear_certificates(self):
        a, h, k, tau, eta, xi, t, eps, G, H = sp.symbols(
            "a h k tau eta xi t eps G H"
        )
        B2 = h * eta + a**2 * xi
        b = a * tau + h * k
        P = a * h + b * B2
        polynomial = eta * t**2 + (1 + xi * a * k - eta * tau) * t - tau
        unit = 1 + eta * t
        hp, bp, kp = h + t * B2, b - t * a, k / unit
        self.assertEqual(sp.cancel((bp - hp * kp) * unit + a * polynomial), 0)
        self.assertEqual(sp.expand(a * hp + bp * B2 - P), 0)
        self.assertEqual(sp.expand(B2 * unit - eta * hp - a**2 * xi), 0)
        # With unprimed k, clearing k'=k/unit requires unit squared here.
        coefficient_certificate = (P * unit**2
                                   - hp * (a * unit**2 + k * a**2 * xi)
                                   - k * eta * hp**2)
        self.assertEqual(sp.expand(coefficient_certificate
                                   + a * B2 * unit * polynomial), 0)
        Gp = G + t * H
        r = a * G + b * H
        self.assertEqual(sp.expand(a * Gp + bp * H - r), 0)
        self.assertEqual(sp.expand((eps * r**2 - 2 * B2 * Gp + 2 * hp * H)
                                   - (eps * r**2 - 2 * B2 * G + 2 * h * H)), 0)
        self.assertEqual(sp.diff(polynomial, t).subs({a: 0, eta: 0, xi: 0}), 1)

        # One finite bivariate lifting, with tau(0,0)=2 rather than zero.
        x, y = sp.symbols("x y")
        specialized = polynomial.subs(
            {a: x, k: 1 + y, tau: 2 + x + y**2, eta: x + y, xi: x - y}
        )

        def homogeneous(expr, degree):
            return sp.Add(*(coefficient * x**i * y**j
                            for (i, j), coefficient in sp.Poly(expr, x, y).terms()
                            if i + j == degree))

        lifted = sp.Integer(2)
        for degree in range(1, 5):
            error = sp.expand(specialized.subs(t, lifted))
            lifted -= homogeneous(error, degree)
            new_error = sp.expand(specialized.subs(t, lifted))
            for j in range(degree + 1):
                self.assertEqual(homogeneous(new_error, j), 0)
        self.assertEqual(lifted.subs({x: 0, y: 0}), 2)
        self.assertEqual((1 + (x + y) * lifted).subs({x: 0, y: 0}), 1)

    def test_conic_slice_certificates(self):
        a, hp, kp, B2, eps, v, G, H = sp.symbols("a hp kp B2 eps v G H")
        r = a * G + hp * kp * H
        R0 = a + kp * B2
        P = hp * R0
        Q = eps * r**2 - 2 * B2 * G + 2 * hp * H
        NG, NH = hp * (1 + eps * kp * r), -eps * a * r + B2

        def N(value):
            return sp.diff(value, G) * NG + sp.diff(value, H) * NH

        self.assertEqual(sp.expand(N(r) - P), 0)
        self.assertEqual(sp.expand(N(Q)), 0)
        self.assertEqual(sp.expand(2 * R0 * G - (2 * r + eps * kp * r**2 - kp * Q)), 0)

        denominator = 1 + eps * kp * r + v
        square_residual = 1 + eps * kp**2 * Q - v**2
        T = 2 * G / denominator
        self.assertEqual(sp.cancel((N(T) - hp) * denominator**2
                                   - hp * square_residual), 0)
        # Clearing both possible denominators proves the alternate rational form.
        comparison = (2 * R0 * G * (1 + v)
                      - ((1 + v) * r - kp * Q) * denominator)
        self.assertEqual(sp.expand(comparison - r * square_residual), 0)
        numerator = r - kp * Q / (1 + v)
        self.assertEqual(sp.cancel(N(numerator) - P), 0)

        # A finite binomial-root control, not an all-order convergence argument.
        z = sp.symbols("z")
        root4 = sum(sp.binomial(sp.Rational(1, 2), j) * z**j for j in range(5))
        residual = sp.Poly(sp.expand(root4**2 - 1 - z), z)
        for j in range(5):
            self.assertEqual(residual.nth(j), 0)
        self.assertEqual(root4.subs(z, 0), 1)
        self.assertEqual(denominator.subs({a: 0, hp: 0, B2: 0, v: 1}), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
