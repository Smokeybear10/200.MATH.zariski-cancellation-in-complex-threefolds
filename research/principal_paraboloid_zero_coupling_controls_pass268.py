"""Finite algebra controls for the zero-coupling recognition subcase268.

These controls check polynomial division and literal determinant identities.
They do not prove the exact coefficient field, actual field return,
separating-basis argument, or the published recognition theorems.
No retained checker is imported. Execution is reserved to Root.
"""

import unittest

import sympy as sp


class PrincipalParaboloidZeroCouplingControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_division_identity_and_remainder_controls(self):
        p, kt, ktt, nt, level = sp.symbols("p kt ktt nt level")
        denominator = 2 * p + kt
        numerator = level - ktt * p**2 / 2 - nt * p
        quotient = -ktt * p / 4 + ktt * kt / 8 - nt / 2
        remainder = level - ktt * kt**2 / 8 + nt * kt / 2
        computed_quotient, computed_remainder = sp.div(
            numerator, denominator, p
        )
        self.assert_zero(computed_quotient - quotient)
        self.assert_zero(computed_remainder - remainder)
        self.assert_zero(numerator - denominator * quotient - remainder)
        self.assert_zero(remainder.subs(level, ktt * kt**2 / 8 - nt * kt / 2))

        # This identity survives a composite, non-affine polynomial p(v).
        v, alpha, beta, defect = sp.symbols("v alpha beta defect")
        composite = v**2 + alpha * v + beta
        good_level = ktt * kt**2 / 8 - nt * kt / 2
        numerator_v = numerator.subs(
            {p: composite, level: good_level + defect}, simultaneous=True
        )
        denominator_v = denominator.subs(p, composite)
        quotient_v = quotient.subs(p, composite)
        self.assert_zero(
            numerator_v - denominator_v * quotient_v - defect
        )
        self.assert_zero(sp.rem(numerator_v, denominator_v, v) - defect)
        self.assertEqual(sp.degree(denominator_v, v), 2)
        self.assertNotEqual(sp.rem(numerator_v, denominator_v, v), 0)
        self.assert_zero(sp.rem(numerator_v.subs(defect, 0), denominator_v, v))
        # k_tt=0 is not an excluded branch of the division argument.
        self.assert_zero(
            (numerator - denominator * quotient - remainder).subs(ktt, 0)
        )
        # The scalar gamma=0 branch cannot use this division.
        self.assert_zero(denominator.subs(p, -kt / 2))
        self.assert_zero(
            numerator.subs(p, -kt / 2) - remainder
        )

    def test_generic_block_jacobian_and_nonzero_requirement(self):
        t, h, w, X = sp.symbols("t h w X")
        y, z, sigma = (
            sp.Function(name)(t, h) for name in ("y", "z", "sigma")
        )
        k = sp.Function("k")(t)
        theta, s = (
            sp.Function(name)(t, h, w) for name in ("theta", "s")
        )
        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        raw = sp.Matrix([Y, Z, W]).jacobian([t, h, w]).det()
        block = sp.Matrix([Y, Z]).jacobian([t, h]).det()
        factor = 1 + sp.diff(theta, w) * X + sp.diff(s, w) * X**2
        self.assert_zero(raw - block * factor)
        self.assert_zero(factor.subs(X, 0) - 1)

        # Symbolic coefficient fixture: if the block is a nonzero scalar,
        # the two positive coefficients of this second factor must vanish.
        j0 = sp.symbols("j0", nonzero=True)
        theta_w, s_w = sp.symbols("theta_w s_w")
        coefficients = sp.Poly(j0 * (1 + theta_w * X + s_w * X**2), X)
        self.assert_zero(coefficients.nth(1) / j0 - theta_w)
        self.assert_zero(coefficients.nth(2) / j0 - s_w)

        # A zero block makes the determinant vanish for arbitrary s_w.
        # Therefore the nonzero actual Jacobian assumption cannot be dropped.
        zero_Y = h * X + t * X**2
        zero_Z = (h + t * X)**2
        free_W = w + w * X**2
        zero_block = sp.Matrix([zero_Y, zero_Z]).jacobian([t, h]).det()
        self.assert_zero(zero_block)
        self.assert_zero(
            sp.Matrix([zero_Y, zero_Z, free_W]).jacobian([t, h, w]).det()
        )
        self.assert_zero(sp.diff(free_W, w) - (1 + X**2))
        self.assertNotEqual(sp.diff(free_W, w), 1)

    def test_nonconstant_sigma_mode_retains_all_t_derivatives(self):
        t, h, w, X = sp.symbols("t h w X")
        k, n = (sp.Function(name)(t) for name in ("k", "n"))
        theta, s = (
            sp.Function(name)(t, h, w) for name in ("theta", "s")
        )
        kt, ktt, nt = sp.diff(k, t), sp.diff(k, t, 2), sp.diff(n, t)
        slope = -ktt / 4
        intercept = ktt * kt / 8 - nt / 2
        y = slope * h + intercept
        z = 2 * t * y + h**2 + kt * h + n
        level = ktt * kt**2 / 8 - nt * kt / 2
        self.assert_zero((2 * h + kt) * y + ktt * h**2 / 2 + nt * h - level)

        Y = y + h * X + t * X**2
        Z = z + (2 * t * h + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        block = sp.Matrix([Y, Z]).jacobian([t, h]).det()
        expected = (
            (2 * h + kt) * (sp.diff(slope, t) * h + sp.diff(intercept, t))
            - slope * ((2 * slope + ktt) * h + 2 * intercept + nt)
        )
        self.assert_zero(block - expected)
        self.assert_zero(sp.diff(block, X))
        self.assert_zero(
            sp.Poly(sp.expand(expected), h).nth(2) + sp.diff(k, t, 3) / 2
        )
        raw = sp.Matrix([Y, Z, W]).jacobian([t, h, w]).det()
        self.assert_zero(
            raw - expected * (1 + sp.diff(theta, w) * X + sp.diff(s, w) * X**2)
        )
        # Omitting coefficient derivatives in the block loses this term.
        wrong = -slope * ((2 * slope + ktt) * h + 2 * intercept + nt)
        self.assertNotEqual(sp.cancel(expected - wrong), 0)

    def test_scalar_gamma_zero_mode(self):
        t, h, w, X = sp.symbols("t h w X")
        k, n = (sp.Function(name)(t) for name in ("k", "n"))
        theta, s = (
            sp.Function(name)(t, h, w) for name in ("theta", "s")
        )
        kt, ktt, nt = sp.diff(k, t), sp.diff(k, t, 2), sp.diff(n, t)
        sigma = -kt / 2
        z = 2 * t * h + n - kt**2 / 4
        self.assert_zero(2 * sigma + kt)
        self.assert_zero(z - (2 * t * h + sigma**2 + kt * sigma + n))
        Y = h + sigma * X + t * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        expected = -2 * h - nt + kt * ktt / 2
        block = sp.Matrix([Y, Z]).jacobian([t, h]).det()
        self.assert_zero(block - expected)
        self.assert_zero(sp.diff(block, X))
        self.assertEqual(sp.diff(expected, h), -2)
        raw = sp.Matrix([Y, Z, W]).jacobian([t, h, w]).det()
        self.assert_zero(
            raw - expected * (1 + sp.diff(theta, w) * X + sp.diff(s, w) * X**2)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

