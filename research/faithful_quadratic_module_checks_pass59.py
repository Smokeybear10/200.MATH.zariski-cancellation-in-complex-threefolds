"""One exact control for the complete quadratic coefficient module.

This checks the monic expansion and reconstruction, not universal
ring membership or existence of an actual ambient coordinate frame.
"""

import unittest

import sympy as S


class FaithfulQuadraticModuleChecks(unittest.TestCase):
    def test_complete_monic_expansion_and_six_element_basis(self):
        a, v, t, z, s, X, T = S.symbols("a v t z s X T")
        A, B, C, D, J, F0 = S.symbols("A B C D J F0")
        generic = A * X**2 + B * X * T + C * T**2 + D * X + J * T + F0
        substituted = S.expand(generic.subs({X: a * s + t * z, T: t}))
        normal = S.rem(substituted, t**2 - v - a * z, t)
        claimed = (
            a**2 * A * s**2
            + s * (2 * a * A * t * z + a * B * t + a * D)
            + a * A * z**3
            + (v * A + a * B) * z**2
            + (v * B + a * C) * z
            + v * C + F0
            + t * (D * z + J)
        )
        self.assertEqual(S.expand(normal - claimed), 0)

        # Independent extraction retains every coefficient that must be regular.
        s_coeff = S.Poly(normal, s).coeff_monomial(s)
        self.assertEqual(S.Poly(s_coeff, t, z).coeff_monomial(t * z), 2 * a * A)
        self.assertEqual(S.Poly(s_coeff, t, z).coeff_monomial(t), a * B)
        self.assertEqual(S.Poly(s_coeff, t, z).coeff_monomial(1), a * D)
        constant = S.Poly(normal, s).coeff_monomial(1)
        odd = S.Poly(constant, t).coeff_monomial(t)
        even = S.Poly(constant, t).coeff_monomial(1)
        self.assertEqual(S.expand(odd - (D * z + J)), 0)
        self.assertEqual(
            [S.Poly(even, z).coeff_monomial(z**k) for k in range(3, -1, -1)],
            [a * A, v * A + a * B, v * B + a * C, v * C + F0],
        )

        z_generic = (T**2 - v) / a
        q_generic = X * T / a - v * (T**2 - v) / a**2
        b_coefficient = a * B
        c_coefficient = a * C + v * B
        f_coefficient = F0 + v * C
        reconstructed = (
            A * X**2 + D * X + J * T + f_coefficient
            + c_coefficient * z_generic + b_coefficient * q_generic
        )
        self.assertEqual(S.cancel(generic - reconstructed), 0)

        # This checks linear independence over L, not generation over the actual ring.
        basis = [S.Integer(1), T, X, X**2, z_generic, q_generic]
        monomials = [S.Integer(1), T, X, X**2, T**2, X * T]
        columns = [
            S.Matrix([S.Poly(element, X, T).coeff_monomial(m) for m in monomials])
            for element in basis
        ]
        coefficient_matrix = S.Matrix.hstack(*columns)
        self.assertEqual(S.factor(coefficient_matrix.det()), 1 / a**2)
        self.assertEqual(S.expand(v * z_generic + a * q_generic - X * T), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
