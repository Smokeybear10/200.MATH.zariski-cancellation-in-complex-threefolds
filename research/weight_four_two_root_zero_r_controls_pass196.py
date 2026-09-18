"""Finite symbolic identities for the two-root zero-R proof in pass196.

The quadratic and quartic field elements below are formal coefficient elements,
not an asserted actual fourfold frame or original polynomial coordinates.
These controls do not prove the pole-degree contradiction, nonexistence of an
algebraic primitive, field return, the pencil lemma, or global recognition.
No older checker, proof implementation, or solver is imported.
"""

import unittest

import sympy as sp


class TwoRootZeroRControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def quadratic_reduce(self, expression, root, square):
        """Reduce in a quadratic fraction field using the conjugate denominator."""
        numerator, denominator = sp.cancel(expression).as_numer_denom()
        relation = root**2 - square
        numerator = sp.rem(numerator, relation, root)
        denominator = sp.rem(denominator, relation, root)
        polynomial = sp.Poly(denominator, root)
        constant = polynomial.coeff_monomial(1)
        linear = polynomial.coeff_monomial(root)
        product = sp.rem(numerator * (constant - linear * root), relation, root)
        return sp.cancel(product / (constant**2 - linear**2 * square))

    def test_two_root_slope_and_square_subtraction(self):
        t, q = sp.symbols("t q")
        square = t * (1 - t)
        s = 1 - 2 * t

        def reduce(expression):
            return self.quadratic_reduce(expression, q, square)

        def derivative(expression):
            return reduce(sp.diff(expression, t) + s * sp.diff(expression, q) / (2 * q))

        q1 = derivative(q)
        q2 = derivative(q1)
        q3 = derivative(q2)
        d = q3 / 6
        d1 = derivative(d)
        d2 = derivative(d1)
        self.zero(reduce(q**2 - square))
        self.zero(reduce(q1 - s / (2 * q)))
        self.zero(reduce(q2 + 1 / (4 * q**3)))
        self.zero(reduce(d - s / (16 * q**5)))
        self.zero(reduce(10 * d * q2 + 5 * d1 * q1 + d2 * q))

        # Independent product-rule jets for b=q*phi. The old scalar equation
        # reduces to a first-order equation for j=phi', not to j=0 by algebra alone.
        phi, j, jp = sp.symbols("phi j jp")
        b = q * phi
        b1 = q1 * phi + q * j
        b2 = q2 * phi + 2 * q1 * j + q * jp
        residual = 10 * d * b2 + 5 * d1 * b1 + d2 * b
        self.zero(reduce(residual - 10 * d * q * jp - (20 * d * q1 + 5 * d1 * q) * j))
        first_integral_derivative = (2 * j * jp * q**4 * d
                                     + 4 * j**2 * q**3 * q1 * d + j**2 * q**4 * d1)
        jp_forced = -(2 * q1 / q + d1 / (2 * d)) * j
        self.zero(reduce(first_integral_derivative.subs(jp, jp_forced)))
        self.zero(reduce(j**2 * q**4 * d - j**2 * s / (16 * q)))

        # Arithmetic of the simple-zero pole, not a test of the valuation theorem.
        self.zero(square.subs(t, sp.Rational(1, 2)) - sp.Rational(1, 4))
        self.zero(s.subs(t, sp.Rational(1, 2)))
        self.zero(sp.diff(s, t) + 2)
        exponent = sp.Rational(-1, 2)
        self.zero(exponent * (exponent - 1) * (exponent - 2) + sp.Rational(15, 8))
        self.zero(exponent - 3 - 1 + sp.Rational(9, 2))
        self.assertEqual(2 * sp.Rational(9, 2), 9)

        lam = sp.symbols("lam")
        Q = q2 / 2
        self.zero(reduce(lam * q3 / (12 * d) - lam / 2))
        W4 = -lam * q1 * d - lam * q * d1 / 4
        self.zero(reduce(W4 - lam * Q**2 / 2))
        # Literal general-q identity explains why the square subtraction survives
        # for both quadratic defining squares, without imposing a root formula.
        formal_q = sp.Function("formal_q")(t)
        formal_d = sp.diff(formal_q, t, 3) / 6
        formal_Q = sp.diff(formal_q, t, 2) / 2
        formal_W4 = -lam * sp.diff(formal_q, t) * formal_d - lam * formal_q * sp.diff(formal_d, t) / 4
        self.zero(formal_W4 - lam * formal_Q**2 / 2
                  + lam * sp.diff(formal_q**2, t, 4) / 48)

    def test_quartic_differential_and_infinity_identities(self):
        r, zeta = sp.symbols("r zeta")
        square = 1 + 4 * r**4

        def reduce(expression):
            return self.quadratic_reduce(expression, zeta, square)

        def derivative_r(expression):
            return reduce(sp.diff(expression, r) + 8 * r**3 * sp.diff(expression, zeta) / zeta)

        t = (1 - 1 / zeta) / 2
        q = r**2 / zeta
        s = 1 / zeta
        self.zero(reduce(q**2 - t * (1 - t)))
        self.zero(reduce(s - (1 - 2 * t)))
        self.zero(reduce(r**2 - q / s))
        dt_dr = derivative_r(t)
        self.zero(reduce(dt_dr - 4 * r**3 / zeta**3))
        # For j=mu*r, dphi/mu=r*dt. Check the exact correction, including its sign.
        self.zero(reduce(2 * r * dt_dr + derivative_r(r / zeta) - 1 / zeta))
        self.zero(reduce(derivative_r(zeta) / (8 * r**3) - 1 / zeta))
        self.assertEqual(sp.gcd(square, sp.diff(square, r)), 1)

        x, z_infinity = sp.symbols("x z_infinity")
        to_infinity = {r: 1 / x, zeta: z_infinity / x**2}
        transformed_relation = (zeta**2 - square).subs(to_infinity, simultaneous=True) * x**4
        self.zero(transformed_relation - (z_infinity**2 - x**4 - 4))
        differential_coefficient = sp.diff(1 / x, x) / (z_infinity / x**2)
        self.zero(differential_coefficient + 1 / z_infinity)
        for infinity_value in (-2, 2):
            self.zero((z_infinity**2 - x**4 - 4).subs({x: 0, z_infinity: infinity_value}))
            self.assertNotEqual(2 * infinity_value, 0)
            self.assertNotEqual((-1 / z_infinity).subs(z_infinity, infinity_value), 0)
        # The displayed local coefficients support the written regularity proof.
        # No finite test establishes regular pullback or absence of algebraic primitives.

    def test_projected_square_original_columns_transport_and_inverse(self):
        X, y, n, t = sp.symbols("X y n t")
        q, q1, Q, d, k, k1, h = sp.symbols("q q1 Q d k k1 h")
        c, c1, c2, M0, M0p, W3, g0 = sp.symbols("c c1 c2 M0 M0p W3 g0")
        lam, alpha, beta, D = sp.symbols("lam alpha beta D")
        M1 = lam * k + alpha * t + beta
        F = d * y**3 + h * y**2
        FU = sp.diff(F, y)
        z0 = n + Q * y**2 + k1 * y
        w0 = (lam * n**2 / 2
              + (lam * Q * y**2 + (lam * k1 + alpha) * y + D) * n
              + lam * Q**2 * y**4 / 2 + W3 * y**3
              + (c2 / 2 - h * M1) * y**2 + M0p * y + g0)
        G = ((W3 - lam * Q * k1 - alpha * Q) * y**3
             + (c2 / 2 - h * M1 - lam * k1**2 / 2 - D * Q - alpha * k1) * y**2
             + (M0p - D * k1) * y)
        self.zero(w0 - lam * z0**2 / 2 - (alpha * y + D) * z0 - G - g0)
        rho = lam * q * n + c
        P = (lam * q1 * n + c1) * y - lam * q * F + M1 * n + M0
        Ychart = y + t * X
        Zchart = z0 + (q1 * y + k) * X + q * X**2
        Wchart = w0 + P * X + rho * X**2
        A0chart = alpha * Ychart + beta * X + D
        corrected = Wchart - lam * Zchart**2 / 2 - A0chart * Zchart
        self.zero(sp.diff(corrected, n))
        self.zero(corrected.subs(X, 0) - G - g0)

        # These are independent coefficient jets needed by the literal columns.
        # Unrestricted lower slots do not assert the remaining scalar PDEs.
        jets = {t: 1, q: q1, q1: 2 * Q, Q: 3 * d, k: k1, k1: 2 * h, c: c1}

        def derivative(expression):
            return sum(sp.diff(expression, slot) * value for slot, value in jets.items())

        def delta(expression):
            return derivative(expression) - FU * sp.diff(expression, n)

        def transverse(expression):
            return delta(expression) - X * sp.diff(expression, y)

        self.zero(transverse(X))
        self.zero(transverse(Ychart))
        self.zero(transverse(Zchart))
        self.zero(transverse(A0chart))
        self.zero(delta(rho) - sp.diff(P, y))
        script_w = sp.Function("script_w")(t, n, y)
        script_p = sp.Function("script_p")(t, n, y)
        literal_W = script_w + X * script_p + X**2 * rho
        self.zero(transverse(literal_W) - delta(script_w)
                  - X * (delta(script_p) - sp.diff(script_w, y))
                  - X**2 * (delta(rho) - sp.diff(script_p, y)))

        Y, Z, W, I = sp.symbols("Y Z W I")
        Q0 = sp.Function("Q0")(X, Y)  # Placeholder for any complex polynomial.
        A0 = alpha * Y + beta * X + D
        Imap = W - lam * Z**2 / 2 - A0 * Z - Q0
        Wback = I + lam * Z**2 / 2 + A0 * Z + Q0
        self.zero(Imap.subs(W, Wback) - I)
        self.zero(Wback.subs(I, Imap) - W)
        correction_in_chart = Q0.subs(Y, Ychart)
        self.zero(derivative(correction_in_chart) - X * sp.diff(correction_in_chart, y))


if __name__ == "__main__":
    unittest.main()
