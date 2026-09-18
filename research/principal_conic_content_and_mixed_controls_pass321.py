"""Standalone finite controls for the working notes320 and321.

This source reconstructs polynomial and differential identities directly.
It imports no retained solver, proof, packet, or checker.

Coverage is deliberately finite. These tests do NOT establish the universal
original-content argument, irreducibility after localization, exact constant
fields, valuation or residue-field assertions, triangularization, polynomial
generation in every case, coordinate descent, or cancellation recognition.
The proof notes retain responsibility for those mathematical arguments.

Authoring restriction: do not execute, import, or compile this saved source.
Root owns complete source review and the sole canonical execution.
"""

import unittest

import sympy as sp


def reduced(expression):
    """Exact simplification over the displayed symbolic coefficient field."""
    return sp.factor(sp.cancel(sp.together(expression)))


class PrincipalConicContentAndMixedControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(reduced(expression), 0)

    def test_01_literal_zero_constant_rows_and_primitive_rescaling(self):
        """Rebuild all original X terms; a formal rescaling is not a gcd proof."""
        T, s, X, sigma = sp.symbols("T s X sigma")
        c, a, h, content = sp.symbols("c a h content", nonzero=True)
        tau = sp.symbols("tau")
        t = T + tau
        f = sp.Function("f")(T)
        n1 = sp.Function("n1")(T)
        n0 = sp.Function("n0")(T)
        b0 = sp.Function("b0")(T, s)
        ell = sp.Function("ell")(T, s)
        eta = sp.Function("eta")(T, s)

        m = c / T
        p = sp.diff(m, T)
        delta = p
        k = m * s + f
        n = n1 * s + n0
        kt = sp.diff(k, T)
        ktt = sp.diff(k, T, 2)
        bp = reduced(ktt / 4 - m * sp.diff(k, T, 3) / (12 * p))
        mu = ktt - (kt * p + 2 * sp.diff(n, s)) / m
        nu = sp.diff(n, T) - kt * sp.diff(n, s) / m
        theta = (
            eta + (2 * p / m) * sigma**2
            + (2 * bp - mu) * sigma + 2 * b0 - nu
        ) / delta
        y = -bp * sigma - b0
        z = 2 * t * y + sigma**2 + kt * sigma + m * theta + n
        potential = (
            ktt * sigma**2 / 2 + p * sigma * theta
            + sp.diff(n, T) * sigma + sp.diff(n, s) * theta
        )
        w = (ell - (2 * sigma + kt) * y - potential) / m

        Y = y + sigma * X + t * X**2
        Z = z + (2 * t * sigma + k) * X + t**2 * X**2
        W = w + theta * X + s * X**2
        omega = a * h

        def apply_p(expression, order=1):
            return omega**order * sp.diff(expression, sigma, order)

        self.assert_zero(apply_p(X))
        self.assert_zero(apply_p(Y) - omega * (X - bp))
        self.assert_zero(apply_p(Y, 2))
        self.assert_zero(apply_p(Z, 2) - 6 * omega**2)
        self.assert_zero(apply_p(Z, 3))
        self.assert_zero(apply_p(W, 3) - 12 * omega**3 / c)
        self.assert_zero(apply_p(W, 4))
        self.assert_zero(sp.diff(apply_p(Y), X) - omega)

        # Here content is explicitly a coefficient-field scalar. The proof,
        # not this symbolic rescaling, establishes where the actual gcd lies.
        kappa = omega / content
        self.assert_zero(kappa * sp.diff(Y, sigma) - kappa * (X - bp))
        self.assert_zero(kappa**2 * sp.diff(Z, sigma, 2) - 6 * kappa**2)
        self.assert_zero(
            kappa**3 * sp.diff(W, sigma, 3) - 12 * kappa**3 / c
        )

        # Negative boundary: arbitrary rational normalization can hide the
        # moving root at infinity. It does not certify an original-ring gcd.
        moving = X - bp
        self.assert_zero(sp.diff(Y, sigma) / moving - 1)
        bad_second = reduced(sp.diff(Z, sigma, 2) / moving**2)
        self.assert_zero(bad_second - 6 / moving**2)
        self.assertTrue(sp.denom(bad_second).has(X))

    def test_02_generic_quadratic_cubic_translation(self):
        """Check the reversible coefficient changes used before parity."""
        v, xi = sp.symbols("v xi")
        a2, b3 = sp.symbols("a2 b3", nonzero=True)
        a1, a0, b2, b1, b0 = sp.symbols("a1 a0 b2 b1 b0")
        quadratic = a2 * v**2 + a1 * v + a0
        cubic = b3 * v**3 + b2 * v**2 + b1 * v + b0
        shift = -a1 / (2 * a2)
        q_shift = sp.expand(quadratic.subs(v, xi + shift))
        c_shift = sp.expand(cubic.subs(v, xi + shift))
        q_constant = q_shift.subs(xi, 0)
        normalized_q = (q_shift - q_constant) / a2
        cubic_even2 = c_shift.coeff(xi, 2)
        cubic_constant = c_shift.subs(xi, 0)
        normalized_c = c_shift - cubic_even2 * normalized_q - cubic_constant
        odd_linear = b1 - a1 * b2 / a2 + 3 * a1**2 * b3 / (4 * a2**2)

        self.assert_zero(normalized_q - xi**2)
        self.assert_zero(normalized_c - xi * (b3 * xi**2 + odd_linear))
        self.assert_zero(a2 * normalized_q + q_constant - q_shift)
        self.assert_zero(
            normalized_c + cubic_even2 * normalized_q + cubic_constant
            - c_shift
        )
        self.assert_zero(q_shift.subs(xi, v - shift) - quadratic)
        self.assert_zero(c_shift.subs(xi, v - shift) - cubic)

    def test_03_parity_module_product_and_constant_boundary(self):
        """Finite module products and the nonunit distinction, not a field proof."""
        u, xi = sp.symbols("u xi")
        A, B = sp.symbols("A B")
        p00, p01, p10, p11, q00, q01, q10, q11 = sp.symbols(
            "p00 p01 p10 p11 q00 q01 q10 q11"
        )
        p0, p1 = p00 + p01 * u, p10 + p11 * u
        q0, q1 = q00 + q01 * u, q10 + q11 * u
        factor = A * u + B
        odd_generator = xi * factor.subs(u, xi**2)
        left = p0.subs(u, xi**2) + odd_generator * p1.subs(u, xi**2)
        right = q0.subs(u, xi**2) + odd_generator * q1.subs(u, xi**2)
        even_product = p0 * q0 + u * factor**2 * p1 * q1
        odd_product = p0 * q1 + p1 * q0
        represented_product = (
            even_product.subs(u, xi**2)
            + odd_generator * odd_product.subs(u, xi**2)
        )
        self.assert_zero(left * right - represented_product)
        self.assert_zero(odd_generator**2 - (u * factor**2).subs(u, xi**2))

        # Generic A is nonzero in Q(A,B), so the linear factor is not a unit.
        field = sp.QQ.frac_field(A, B)
        factor_poly = sp.Poly(factor, u, domain=field)
        quotient, remainder = sp.div(sp.Poly(1, u, domain=field), factor_poly)
        self.assertEqual(factor_poly.degree(), 1)
        self.assertEqual(quotient.as_expr(), 0)
        self.assertEqual(remainder.as_expr(), 1)

        # Required negative boundary: A=0,B=1 makes the odd generator xi.
        unit_factor = factor.subs({A: 0, B: 1})
        self.assertEqual(sp.Poly(unit_factor, u).degree(), 0)
        self.assert_zero(odd_generator.subs({A: 0, B: 1}) - xi)
        self.assertEqual(sp.div(sp.Integer(1), unit_factor, u), (1, 0))
        self.assert_zero(odd_generator.subs({A: 1, B: 0}) - xi**3)

    def test_04_raw_mixed_surface_and_exact_integrating_factor(self):
        """Retain arbitrary f,n1,n0; compare the entire formal PV equation."""
        T, s, c, d = sp.symbols("T s c d")
        f = sp.Function("f")(T)
        n1 = sp.Function("n1")(T)
        n0 = sp.Function("n0")(T)
        m = d + c / T
        p = sp.diff(m, T)
        delta = m * sp.diff(m, T, 2) / (2 * p)
        k = m * s + f
        n = (p**2 - delta**2) * s**2 / 4 + n1 * s + n0
        bp = sp.diff(k, T, 2) / 4 - m * sp.diff(k, T, 3) / (12 * p)
        bv = (p - delta) / 2
        mu = sp.diff(k, T, 2) - (
            sp.diff(k, T) * p + 2 * sp.diff(n, s)
        ) / m
        raw = sp.diff(n, T, s) - 2 * p * sp.diff(n, s) / m - mu * bv - delta * bp

        expected = (
            sp.diff(n1, T) + (2 * c + d * T) * n1 / (T * (c + d * T))
            + (c + d * T)**2 * sp.diff(f, T, 3) / (12 * c * T)
            + (c - d * T) * sp.diff(f, T, 2) / (4 * T**2)
            - c * d * sp.diff(f, T) / (2 * T**2 * (c + d * T))
        )
        G = T**2 / (c + d * T)
        H = T * (c + d * T) / (12 * c)
        J = (c - d * T) / (4 * (c + d * T)) - (c + 2 * d * T) / (12 * c)
        integral = G * n1 + H * sp.diff(f, T, 2) + J * sp.diff(f, T) + d * f / (6 * c)

        self.assert_zero(raw - expected)
        self.assert_zero(sp.diff(raw, s))
        self.assert_zero(sp.diff(integral, T) - G * raw)
        self.assertFalse(raw.has(n0))
        dropped_term_residual = sp.diff(integral - d * f / (6 * c), T) - G * raw
        self.assert_zero(dropped_term_residual + d * sp.diff(f, T) / (6 * c))
        self.assertNotEqual(reduced(dropped_term_residual), 0)

    def test_05_raw_restricted_coefficient_and_zero_constant_boundary(self):
        """Rebuild C from bP, including its full s coefficient."""
        T, s, c, d = sp.symbols("T s c d")
        f = sp.Function("f")(T)
        m = d + c / T
        p = sp.diff(m, T)
        delta = m * sp.diff(m, T, 2) / (2 * p)
        bv = (p - delta) / 2
        k = m * s + f
        bp = sp.diff(k, T, 2) / 4 - m * sp.diff(k, T, 3) / (12 * p)
        raw_left = sp.diff(bp, T) - bv * sp.diff(k, T, 2) / m + 4 * bp * bv / m
        C_raw = -m * delta * raw_left / (4 * p)
        C_expected = -(c + d * T)**3 * (
            T * sp.diff(f, T, 4) + 4 * sp.diff(f, T, 3)
        ) / (48 * c**2 * T)

        self.assert_zero(C_raw - C_expected)
        self.assert_zero(sp.diff(C_raw, s))
        bp_zero = reduced(bp.subs(d, 0))
        C_zero = reduced(C_raw.subs(d, 0))
        self.assert_zero(bp_zero - sp.diff(f, T, 2) / 4 - T * sp.diff(f, T, 3) / 12)
        self.assert_zero(sp.diff(bp_zero, T) + 4 * T * C_zero / c)
        self.assert_zero(
            C_zero + c * (T * sp.diff(f, T, 4) + 4 * sp.diff(f, T, 3)) / (48 * T)
        )

    def test_06_differential_family_and_nonzero_cubic_control(self):
        """Check the displayed solutions, not exhaustiveness over an exact field."""
        T, c, d = sp.symbols("T c d")
        f = sp.Function("f")(T)
        q, A0, A1, A2, Aminus = sp.symbols("q A0 A1 A2 Aminus")

        def operator(expression):
            return T * sp.diff(expression, T, 4) + 4 * sp.diff(expression, T, 3)

        self.assert_zero(sp.diff(T**4 * sp.diff(f, T, 3), T) - T**3 * operator(f))
        for basis_function in (sp.Integer(1), T, T**2, 1 / T):
            self.assert_zero(operator(basis_function))
        family = A0 + A1 * T + A2 * T**2 + Aminus / T
        self.assert_zero(operator(family))
        self.assert_zero(sp.diff(-q / (6 * T), T, 3) - q / T**4)

        self.assertEqual(operator(T**3), 24)
        cubic_C = -(c + d * T)**3 * operator(T**3) / (48 * c**2 * T)
        self.assert_zero(cubic_C + (c + d * T)**3 / (2 * c**2 * T))
        self.assertNotEqual(reduced(cubic_C), 0)
        self.assert_zero(cubic_C.subs(d, 0) + c / (2 * T))


if __name__ == "__main__":
    unittest.main()
