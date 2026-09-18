"""Fresh identity controls for332--334, not an unrestricted proof certificate.

Root-only single execution after complete source read and independent review.
No imports of any earlier project checker or solver. The checks concern
polynomial identities over an exact coefficient field, not field descent,
the full initial-kernel hypothesis, whole-line generation, or recognition.
The inverse identities are in fraction fields with m != 0 and, for the
1123 transfer only, Delta = D - B**2 != 0. The plane transformation
requires Hr != 0. Cancellation of rational expressions does not test or
authorize singular specializations of those maps. The separate residual
method checks Delta = 0 without applying the inverse-transfer formula.
"""
import unittest

import sympy as sp


class QuadraticNormalizationControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_combined_actual_inverse_and_constant_jacobian(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        xp, yp, zp, wp = sp.symbols("xp yp zp wp")
        m, kap, b, d, A, B, C = sp.symbols("m kap b d A B C")
        forward = (X + B, Y + A / 2, Z - C,
                   m * W + (kap / 2 + 2 * B) * Z + b * Y + d * X**2)
        inverse = (xp - B, yp - A / 2, zp + C,
                   (wp - (kap / 2 + 2 * B) * (zp + C)
                    - b * (yp - A / 2) - d * (xp - B)**2) / m)
        old, new = (X, Y, Z, W), (xp, yp, zp, wp)
        for original, expression in zip(old, inverse):
            self.zero(expression.subs(dict(zip(new, forward)), simultaneous=True)
                      - original)
        for original, expression in zip(new, forward):
            self.zero(expression.subs(dict(zip(old, inverse)), simultaneous=True)
                      - original)
        self.zero(sp.Matrix(forward).jacobian(old).det() - m)

    def test_complete_literal_reframe_and_both_potentials(self):
        X, t, s, y, sig, theta, ell = sp.symbols("X t s y sig theta ell")
        m, kap, b, d, A, B, C, D = sp.symbols("m kap b d A B C D")
        k = m * s + kap * t**2 / 2 + b * t + d
        n = (B + kap / 2) * k + D * t**2 + A * t + C
        F = kap * sig**2 / 2 + sp.diff(n, t) * sig + sp.diff(n, s) * theta
        z = 2 * t * y + sig**2 + sp.diff(k, t) * sig + m * theta + n
        w = (ell - (2 * sig + sp.diff(k, t)) * y - F) / m
        Y = y + sig * X + t * X**2
        Z = z + (2 * t * sig + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        xp = X + B
        sp_new = k + 2 * B * t**2
        theta1 = m * theta + sp.diff(k, t) * sig + kap * k / 2
        w1 = m * w + kap * z / 2 + b * y
        yn = y - B * sig + B**2 * t + A / 2
        sign = sig - 2 * B * t
        zn = z - 2 * B * t * sig - B * k + B**2 * t**2 - C
        thetan = theta1 + 4 * B * t * sig - 4 * B**2 * t**2
        wn = w1 + 2 * B * z - B * theta1 - 4 * B**2 * t * sig \
            - B**2 * k + 2 * B**3 * t**2
        delta = D - B**2
        ell1 = ell + kap * n / 2 + kap * B * k / 2
        elln = ell1 + B**2 * k + 2 * B * C - 2 * B * delta * t**2
        self.zero(Y + A / 2 - (yn + sign * xp + t * xp**2))
        self.zero(Z - C - (zn + (2 * t * sign + sp_new) * xp + t**2 * xp**2))
        self.zero(m * W + (kap / 2 + 2 * B) * Z + b * Y + d * X**2
                  - (wn + thetan * xp + sp_new * xp**2))
        self.zero(zn - 2 * t * yn - sign**2 - thetan - delta * t**2)
        self.zero(wn + 2 * sign * yn + 2 * delta * t * sign - elln)
        self.zero(elln + delta * sp_new - ell1 - D * k - 2 * B * C)
        self.zero(sp.Matrix([t, sp_new]).jacobian([t, s]).det() - m)

    def test_residual_formula_and_translation_boundary(self):
        t, s, m, kap, b, d, A, B, C, D, shift = sp.symbols(
            "t s m kap b d A B C D shift")
        k = m * s + kap * t**2 / 2 + b * t + d
        n = (B + kap / 2) * k + D * t**2 + A * t + C
        ratio = sp.diff(n, s) / m
        residual = sp.diff(n, t, 2) / 2 - ratio**2 + kap * ratio / 2 - kap**2 / 4
        self.zero(residual - (D - B**2))
        self.zero(D + shift**2 - 2 * B * shift - (B - shift)**2 - residual)
        self.zero(residual.subs(D, B**2))
        self.zero(residual.subs(D, 0) + B**2)
        for variables in ((s, s), (t, s), (t, t, t)):
            self.zero(sp.diff(n, *variables))
        self.zero(sp.diff(k, t, 3))

    def test_nonzero_residual_coordinate_transfer(self):
        X, Y, Z, W, T, S, A, B, C, D = sp.symbols("X Y Z W T S A B C D")
        delta = D - B**2
        Tf = Y**2 + X * W - X**2 * Z + A * Y + B * W + D * Z + C * X**2
        Sf = (X - B) * Z - W
        U0 = T - Y**2 - A * Y - C * X**2
        Zi = (U0 + (X + B) * S) / delta
        Wi = ((X - B) * U0 + (X**2 - D) * S) / delta
        self.zero(Zi.subs({T: Tf, S: Sf}, simultaneous=True) - Z)
        self.zero(Wi.subs({T: Tf, S: Sf}, simultaneous=True) - W)
        self.zero(Tf.subs({Z: Zi, W: Wi}, simultaneous=True) - T)
        self.zero(Sf.subs({Z: Zi, W: Wi}, simultaneous=True) - S)
        t, s, y, sig, theta, ell = sp.symbols("t s y sig theta ell")
        n = D * t**2 + A * t + B * s + C
        z = 2 * t * y + sig**2 + theta + n
        w = ell - 2 * sig * y - (2 * D * t + A) * sig - B * theta
        actual = {Y: y + sig * X + t * X**2,
                  Z: z + (2 * t * sig + s) * X + t**2 * X**2,
                  W: w + theta * X + s * X**2}
        self.zero(Tf.subs(actual, simultaneous=True)
                  - (y**2 + A * y + B * w + D * z + (ell + D * s) * X))
        self.zero(sp.expand(Sf.subs(actual, simultaneous=True)).coeff(X, 3) - t**2)

    def test_centered_plane_primitive_with_arbitrary_jets(self):
        U, P, g, gp = sp.symbols("U P g gp")
        Hr, Ht, Hrr, Htr, Htt, Lc, Lr, Lt = sp.symbols("Hr Ht Hrr Htr Htt Lc Lr Lt")
        theta = Hr * (U**2 + g * P**2) + Ht * P - Lc
        ellt, ells = -Ht / Hr, 1 / Hr
        elltt = -Htt / Hr + 2 * Ht * Htr / Hr**2 - Ht**2 * Hrr / Hr**3
        ellts, ellss = -Htr / Hr**2 + Ht * Hrr / Hr**3, -Hrr / Hr**3
        hbt = Lt / Hr - Lc * Htr / Hr**2 - Ht * Lr / Hr**2 \
            + Ht * Lc * Hrr / Hr**3
        hbs = Lr / Hr**2 - Lc * Hrr / Hr**3
        centered = (2 * (g + ells) * P - ellt) * U + gp * P**3 / 3 \
            - elltt * P**2 / 2 - ellts * P * theta - ellss * theta**2 / 2 \
            - hbt * P - hbs * theta
        plane = Hrr * (U**2 + g * P**2)**2 / 2 + Htr * (U**2 + g * P**2) * P \
            + Htt * P**2 / 2 + 2 * (1 + g * Hr) * U * P + Ht * U \
            + Hr * gp * P**3 / 3 - Lr * (U**2 + g * P**2) - Lt * P
        self.zero(Hr * centered - plane - Lc * Lr / Hr + Lc**2 * Hrr / (2 * Hr**2))
        self.zero(sp.Poly(plane, U, P).coeff_monomial(U**4) - Hrr / 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
