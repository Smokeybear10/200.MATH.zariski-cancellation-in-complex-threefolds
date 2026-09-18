"""Finite exact-algebra controls for the n-parameter affine-graph argument.

The source independently rebuilds scalar determinant coefficients. It does
not prove exact coefficient-field descent, the curve-pencil theorem, or a
universal original-ring coordinate assertion. No retained module is imported.
"""

import unittest

import sympy as sp


class AffineGraphReparameterizationControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    @staticmethod
    def graph(t, n, U, H, L, w0, c, b, d):
        h = c * U**2 / 2 + b * U
        G = L + sp.diff(H, t) * U
        G += (d - sp.diff(H, n) * b) * U**2 / 2
        G -= sp.diff(H, n) * c * U**3 / 6
        w = sp.integrate(sp.expand(sp.diff(G, t) - h * sp.diff(G, n)), U) + w0
        scalar = sp.Poly(sp.expand(h * sp.diff(w, n) - sp.diff(w, t)), U)
        return G, w, scalar

    def test_arbitrary_algebraic_coefficient_formal_eighth_gate(self):
        t, n, U = sp.symbols("t n U")
        H, L, w0 = (sp.Function(name)(t, n) for name in ("H", "L", "w0"))
        c, b, d = (sp.Function(name)(t) for name in ("c", "b", "d"))
        G, w, scalar = self.graph(t, n, U, H, L, w0, c, b, d)
        self.assertLessEqual(sp.Poly(w, U).degree(), 6)
        self.assertLessEqual(scalar.degree(), 8)
        self.assert_zero(
            sp.Poly(w, U).nth(6) - c**2 * sp.diff(H, n, 2) / 72
        )
        self.assert_zero(scalar.nth(8) - c**3 * sp.diff(H, n, 3) / 144)
        # The old t derivative holds lambda=H(t,n) fixed.
        def old_t(expression):
            return sp.diff(expression, t) - sp.diff(H, t) / sp.diff(H, n) * sp.diff(expression, n)

        nu = 1 / sp.diff(H, n)
        old_f_t = c * U**2 / 2 + b * U - sp.diff(H, t) / sp.diff(H, n)
        old_G_lambda = nu * sp.diff(G, n)
        self.assert_zero(
            old_t(G) - old_f_t * old_G_lambda / nu - sp.diff(w, U)
        )

    def test_quadratic_H_forces_polynomial_remaining_coefficients(self):
        t, n, U = sp.symbols("t n U")
        A, B, C, c, b, d = (
            sp.Function(name)(t) for name in ("A", "B", "C", "c", "b", "d")
        )
        L, w0 = (sp.Function(name)(t, n) for name in ("L", "w0"))
        H = A * n**2 / 2 + B * n + C
        _, _, scalar = self.graph(t, n, U, H, L, w0, c, b, d)
        expected_fifth = -(
            3 * A * b * sp.diff(c, t)
            + 4 * A * c * sp.diff(b, t)
            + 12 * b * c * sp.diff(A, t)
            + 2 * c**2 * sp.diff(L, n, 2)
        ) / 24
        expected_second = -(
            n**2 * sp.diff(A, t, 3) + 2 * n * sp.diff(B, t, 3)
            - 6 * b * sp.diff(L, n, t) - 2 * c * sp.diff(w0, n)
            + 2 * sp.diff(C, t, 3) - 2 * sp.diff(L, n) * sp.diff(b, t)
        ) / 4
        self.assert_zero(scalar.nth(5) - expected_fifth)
        self.assert_zero(scalar.nth(2) - expected_second)
        self.assert_zero(scalar.nth(6) + 7 * c * (A * sp.diff(c, t) + 2 * c * sp.diff(A, t)) / 144)
        D, E, F = (sp.Function(name)(t) for name in ("D", "E", "F"))
        polynomial_L = D * n**2 / 2 + E * n + F
        forced_w0_n = (
            n**2 * sp.diff(A, t, 3) + 2 * n * sp.diff(B, t, 3)
            - 6 * b * sp.diff(polynomial_L, n, t)
            + 2 * sp.diff(C, t, 3) - 2 * sp.diff(polynomial_L, n) * sp.diff(b, t)
        ) / (2 * c)
        polynomial_w0 = sp.integrate(sp.expand(forced_w0_n), n)
        self.assertLessEqual(sp.Poly(polynomial_w0, n).degree(), 3)
        self.assert_zero(sp.diff(polynomial_w0, n) - forced_w0_n)
        _, polynomial_w, _ = self.graph(t, n, U, H, polynomial_L, polynomial_w0, c, b, d)
        self.assertLessEqual(sp.Poly(polynomial_w, U).degree(), 6)
        self.assertLessEqual(sp.Poly(polynomial_w, n).degree(), 3)

    def test_actual_shear_calibration_chain_rule(self):
        t, n, y, X, Y, Z, W, I = sp.symbols("t n y X Y Z W I")
        f2, f1, q1, k, q, C = (
            sp.Function(name)(t) for name in ("f2", "f1", "q1", "k", "q", "C")
        )
        coeff = [sp.Function(f"c{i}")(t) for i in range(5)]
        polynomial = coeff[0] + coeff[1] * X * Y + coeff[2] * Z
        polynomial += coeff[3] * Y**3 + coeff[4] * X**2 * Z**2
        actual_Y = y + t * X
        actual_Z = n + f2 * y**2 + f1 * y + (q1 * y + k) * X + q * X**2
        substitution = {Y: actual_Y, Z: actual_Z}
        actual_W = C + polynomial.subs(substitution, simultaneous=True)
        matrix = sp.Matrix([actual_Y, actual_Z, actual_W]).jacobian([t, n, y])
        expected = -(sp.diff(C, t) + sp.diff(polynomial, t).subs(substitution, simultaneous=True))
        self.assert_zero(matrix.det() - expected)
        self.assert_zero(
            sp.Matrix([t, actual_Y, actual_Z]).jacobian([t, n, y]).det() + 1
        )
        # Finite ordinary-polynomial instance of the final coordinate shear.
        complex_polynomial = polynomial.subs(dict(zip(coeff, [2, -1, 3, 5, 7])))
        image_I = W - complex_polynomial
        inverse_W = I + complex_polynomial
        self.assert_zero(image_I.subs(W, inverse_W) - I)
        self.assert_zero(inverse_W.subs(I, image_I) - W)


if __name__ == "__main__":
    unittest.main(verbosity=2)
