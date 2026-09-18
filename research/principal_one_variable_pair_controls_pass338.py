"""One-use exact identity controls for the one-variable-potential argument.

No project-checker imports. These are fraction-field identities, not a
certificate of localization, primeness, derivation descent, or recognition.
The conic-line test assumes alpha != 0, with g = -alpha**2, and treats gp
as the independent coefficient g'. Dividing by alpha/g is illegal in the
separately handled f'' = 0 branch. The constant-generator test assumes the
hypotheses of the written actual-chart proof, not existence of its data.
"""
import unittest

import sympy as sp


class OneVariablePotentialControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_conic_factor_and_fourth_potential_coefficients(self):
        U, P, alpha, ell1, ell2, gp, h = sp.symbols("U P alpha ell1 ell2 gp h")
        g = -alpha**2
        shifted = P - ell1 / (2 * g)
        self.zero((U - alpha * shifted) * (U + alpha * shifted)
                  - (U**2 + g * P**2 - ell1 * P + ell1**2 / (4 * g)))
        beta = ell1 / (2 * alpha)
        selected = alpha * P + beta
        hbar = -ell1**2 / (4 * g)
        self.zero(selected**2 + g * P**2 - ell1 * P - hbar)
        hbt = -ell1 * ell2 / (2 * g) + ell1**2 * gp / (4 * g**2)
        Q = sp.expand((2 * g * P - ell1) * selected + gp * P**3 / 3
                      - ell2 * P**2 / 2 - hbt * P)
        self.zero(Q.coeff(P, 3) - gp / 3)
        self.zero(Q.coeff(P, 2) - (2 * g * alpha - ell2 / 2))
        self.zero(Q.coeff(P, 1).subs({gp: 0, ell2: 4 * g * alpha}))
        self.assertNotEqual(Q.coeff(P, 3), 0)

    def test_actual_translation_has_zero_intercept(self):
        X, t, sig, alpha, f1, ell1c = sp.symbols("X t sig alpha f1 ell1c")
        g = -alpha**2
        ellprime = 4 * g * alpha * t + ell1c
        p = g * t + f1 / 2
        x = alpha * sig + ellprime / (2 * alpha)
        y = x - p
        Y = y + sig * X + t * X**2
        b0 = ell1c / (2 * alpha)
        Ystar = Y + f1 / 2 - b0
        self.zero(Ystar - (X + alpha) * (sig + t * (X - alpha)))
        self.zero(Ystar.subs(X, -alpha))

    def test_constant_generators_preserve_actual_three_ring(self):
        X, t, s, y, sig, theta, ell, p, f, a, h = sp.symbols(
            "X t s y sig theta ell p f a h")
        z = 2 * t * y + sig**2 + theta + f
        w = ell - 2 * sig * (y + p)
        Y = y + sig * X + t * X**2
        Z = z + (2 * t * sig + s) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        S = W - X * Z
        self.zero(a * h * sp.diff(Y, theta))
        self.zero(a * h * sp.diff(Z, theta) - a * h)
        self.zero(a * h * sp.diff(W, theta) - X * a * h)
        self.zero(a * h * sp.diff(S, theta))
        self.zero(sp.diff(a * sp.diff(S, X), theta))


if __name__ == "__main__":
    unittest.main(verbosity=2)

