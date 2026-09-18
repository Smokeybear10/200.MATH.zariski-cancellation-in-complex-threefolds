"""Finite exact controls for three-output-cubic-speed-pass41.md.

These six methods check displayed rational identities and illustrative
positive/negative controls. They do not machine-prove the rational-function
classification, the published nice-derivation theorem, or the existence of
an actual degree-five frame. No project solver is imported.

Run: /opt/anaconda3/bin/python research/three_output_cubic_speed_checks_pass41.py
"""

import unittest

import sympy as sp


class ThreeOutputCubicSpeedChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w, cls.s = sp.symbols("w sigma")
        cls.ell = sp.symbols("ell", nonzero=True)
        cls.a = sp.Function("a")(cls.w)
        cls.b = sp.Function("b")(cls.w)
        cls.H = sp.diff(cls.a, cls.w) + sp.diff(cls.b, cls.w) * cls.s
        cls.p = cls.ell * cls.s - cls.b
        cls.V = cls.p / cls.H

        def delta(value):
            return sp.diff(value, cls.s) + cls.V * sp.diff(value, cls.w)

        # Compute the third iterate directly, independently of the recurrence
        # used to organize the polynomial numerator in the written proof.
        cls.numerator = sp.cancel(cls.H**5 * delta(delta(cls.V)))

    def assertZero(self, value):
        self.assertEqual(sp.cancel(value), 0)

    def test_generic_numerator_and_highest_coefficient(self):
        w, s, ell, a, b = self.w, self.s, self.ell, self.a, self.b
        H, p = self.H, self.p
        first = ell * H**2 - 2 * sp.diff(b, w) * p * H - p**2 * sp.diff(H, w)
        organized = (
            H**2 * sp.diff(first, s)
            + p * H * sp.diff(first, w)
            - 3 * first * sp.diff(b, w) * H
            - 3 * first * p * sp.diff(H, w)
        )
        self.assertZero(self.numerator - organized)
        polynomial = sp.Poly(self.numerator, s)
        self.assertLessEqual(polynomial.degree(), 5)
        self.assertZero(
            polynomial.coeff_monomial(s**5)
            - ell**3 * (3 * sp.diff(b, w, 2) ** 2 - sp.diff(b, w) * sp.diff(b, w, 3))
        )
        # H cannot be identically zero as a polynomial in sigma unless both
        # coefficient derivatives vanish. Its required numerator still has
        # the nonzero sigma coefficient ell in that case.
        A, B, b0 = sp.symbols("A B b0")
        self.assertEqual(sp.Poly(A + B * s, s).all_coeffs(), [B, A])
        self.assertEqual(sp.Poly(ell * s - b0, s).coeff_monomial(s), ell)

    def test_nonzero_affine_b_full_tail(self):
        w, s, ell, a, b = self.w, self.s, self.ell, self.a, self.b
        beta = sp.symbols("beta", nonzero=True)
        b0, a0, a1 = sp.symbols("b0 a0 a1")
        affine = self.numerator.subs(b, beta * w + b0).doit()
        polynomial = sp.Poly(affine, s)
        self.assertZero(polynomial.coeff_monomial(s**4) + beta * ell**3 * sp.diff(a, w, 3))
        degree_three = polynomial.coeff_monomial(s**3).subs(sp.diff(a, w, 3), 0)
        self.assertZero(degree_three - 3 * ell * (ell * sp.diff(a, w, 2) + beta**2) ** 2)
        chosen_a = -beta**2 * w**2 / (2 * ell) + a1 * w + a0
        H = sp.diff(chosen_a, w) + beta * s
        V = (ell * s - beta * w - b0) / H
        delta = lambda value: sp.diff(value, s) + V * sp.diff(value, w)
        expected = (
            -3 * beta * ell**3 * (beta * b0 + ell * a1) ** 3
            / (-beta**2 * w + beta * ell * s + ell * a1) ** 5
        )
        self.assertZero(delta(delta(V)) - expected)
        self.assertZero(V.subs(a1, -beta * b0 / ell) - ell / beta)
        # Before the tail condition, the top two vanishing coefficients alone
        # do not force the third iterate to vanish.
        self.assertNotEqual(sp.cancel(expected.subs({beta: 1, ell: 1, b0: 0, a1: 1})), 0)

    def test_constant_b_branch_and_nonzero_denominator(self):
        w, s, ell, a, b = self.w, self.s, self.ell, self.a, self.b
        b0, a0 = sp.symbols("b0 a0")
        alpha = sp.symbols("alpha", nonzero=True)
        reduced = self.numerator.subs(b, b0).doit()
        coefficient = sp.Poly(reduced, s).coeff_monomial(s**3)
        self.assertZero(
            coefficient - ell**3 * (3 * sp.diff(a, w, 2) ** 2 - sp.diff(a, w) * sp.diff(a, w, 3))
        )
        self.assertZero(reduced.subs(a, alpha * w + a0).doit())
        self.assertEqual(sp.diff(alpha * w + a0, w), alpha)
        V = (ell * s - b0) / alpha
        delta = lambda value: sp.diff(value, s) + V * sp.diff(value, w)
        self.assertZero(delta(delta(V)))
        self.assertZero(delta(V) - ell / alpha)
        # A constant a as well as constant b makes H zero, not a third
        # unaccounted branch of the rational formula.
        self.assertEqual(sp.diff(a0, w), 0)

    def test_both_positive_quadratic_relation_families(self):
        w, s, ell = self.w, self.s, self.ell
        nu, kappa = sp.symbols("nu kappa", nonzero=True)
        a0, b0 = sp.symbols("a0 b0")
        families = [
            (nu * s + kappa, ell / nu * (w - kappa * s - nu * s**2 / 2) + a0),
            (kappa, -ell * (s - w / kappa) ** 2 / 2 + b0 * (s - w / kappa) + a0),
        ]
        for V, tau in families:
            with self.subTest(speed=V):
                delta = lambda value: sp.diff(value, s) + V * sp.diff(value, w)
                self.assertZero(delta(tau))
                self.assertZero(delta(delta(V)))
                self.assertNotEqual(sp.cancel(sp.diff(tau, w)), 0)
        # In the nonconstant-speed survivor, the apparent quadratic nice
        # coefficient cancels globally as a rational-function identity.
        tau = families[0][1]
        R = s**2 / 12 + tau / (6 * ell)
        self.assertZero(R - (w - kappa * s) / (6 * nu) - a0 / (6 * ell))
        g, t = sp.symbols("g t", nonzero=True)
        self.assertZero(
            (g * R).subs(s, t / g)
            - g * (w / (6 * nu) + a0 / (6 * ell))
            + kappa * t / (6 * nu)
        )
        # The other survivor has sigma affine in w. Its p=g(tau+lambda*s^2/2)
        # identity gives the polynomial first replica coefficient in (16).
        p = g * (tau + ell * s**2)
        self.assertZero(g * (s**2 / 12 + tau / (6 * ell)) - (p / (6 * ell) - g * s**2 / 12))

    def test_rational_ode_pole_and_degree_controls(self):
        w = self.w
        n = sp.symbols("n", integer=True)
        leading = n * (n - 1) - 3 * n**2
        self.assertEqual(sp.factor(leading), -n * (2 * n + 1))
        for order in (-7, -3, -1, 1, 2, 8):
            with self.subTest(order=order):
                self.assertNotEqual(leading.subs(n, order), 0)
        for value in (1 / w, (w + 1) / (w - 2) ** 2, w**3 + w + 1):
            with self.subTest(value=value):
                self.assertNotEqual(sp.cancel(value * sp.diff(value, w, 2) - 3 * sp.diff(value, w) ** 2), 0)
        self.assertZero(sp.Integer(4) * sp.diff(sp.Integer(4), w, 2))
        # The rationality requirement in the ODE lemma is material: a
        # nonrational square-root solution exists. It is not asserted to
        # solve all the additional speed-classification coefficients.
        fractional = w ** (-sp.Rational(1, 2))
        self.assertZero(fractional * sp.diff(fractional, w, 2) - 3 * sp.diff(fractional, w) ** 2)
        self.assertFalse(fractional.is_rational_function(w))

    def test_no_quadratic_coefficient_field_controls(self):
        w = self.w
        kappa = sp.symbols("kappa", nonzero=True)
        mu = sp.symbols("mu")
        for sigma, expected_zero in ((w / kappa + mu, True), (w**2, False), (1 / w, False)):
            with self.subTest(sigma=sigma):
                V = 1 / sp.diff(sigma, w)
                delta = lambda value: V * sp.diff(value, w)
                self.assertZero(delta(sigma) - 1)
                third = sp.cancel(delta(delta(V)))
                self.assertEqual(third == 0, expected_zero)
        self.assertZero((1 / (2 * w)) * sp.diff((1 / (2 * w)) * sp.diff(1 / (2 * w), w), w) - 3 / (8 * w**5))
        # delta^3(w)=0 alone allows a quadratic w=sigma^2. The field equality
        # supplied by sigma in C(w) is the separate necessary gate.
        s = self.s
        self.assertEqual(sp.diff(s**2, s, 3), 0)
        self.assertEqual(sp.Poly(s**2 - w, s, domain=sp.QQ.frac_field(w)).degree(), 2)
        self.assertTrue(sp.Poly(s**2 - w, s, domain=sp.QQ.frac_field(w)).is_irreducible)
        self.assertFalse(sp.sqrt(w).is_rational_function(w))


if __name__ == "__main__":
    unittest.main()
