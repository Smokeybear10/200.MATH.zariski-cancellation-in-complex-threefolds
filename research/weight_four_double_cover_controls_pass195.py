"""Finite new identities for the two double-cover reductions in pass195.

Algebraic coefficient elements are not original polynomial coordinates.
The controls do not prove field return, curve pole degrees, the exact pencil
lemma, constant-field descent, or recognition. Those are written-proof inputs.
No earlier checker, proof implementation, or solver is imported.
"""

import unittest

import sympy as sp


class DoubleCoverControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def quadratic_reduce(self, expression, q, g):
        # Exact reduction in C(t)[q]/(q^2-g), including inversion by conjugation.
        numerator, denominator = sp.cancel(expression).as_numer_denom()
        relation = q**2 - g
        numerator = sp.rem(numerator, relation, q)
        denominator = sp.rem(denominator, relation, q)
        polynomial = sp.Poly(denominator, q)
        b = polynomial.coeff_monomial(1)
        a = polynomial.coeff_monomial(q)
        product = sp.rem(numerator * (b - a * q), relation, q)
        return sp.cancel(product / (b**2 - a**2 * g))

    def test_algebraic_curvatures_and_rational_primitive(self):
        t, q = sp.symbols("t q")
        cases = (
            (t, 1 / (16 * q**5), 15 / (4 * t**2)),
            (t * (1 - t), (1 - 2 * t) / (16 * q**5),
             5 * (4 * t - 3) * (4 * t - 1)
             / (4 * t**2 * (t - 1)**2 * (2 * t - 1)**2)),
        )
        for g, expected_d, expected_curvature in cases:
            def reduce(expression):
                return self.quadratic_reduce(expression, q, g)

            def derivative(expression):
                return reduce(sp.diff(expression, t)
                              + sp.diff(g, t) * sp.diff(expression, q) / (2 * q))

            self.zero(reduce(q**2 - g))
            self.zero(derivative(q**2) - sp.diff(g, t))
            Q = derivative(derivative(q)) / 2
            d = derivative(Q) / 3
            self.zero(reduce(d - expected_d))
            curvature = reduce((4 * d * derivative(derivative(d))
                                - 5 * derivative(d)**2) / d**2)
            self.zero(curvature - expected_curvature)
            self.assertNotEqual(curvature, 0)
            # The defining rational square has a simple zero at t=0. This
            # arithmetic slot supports, but does not replace, the valuation proof.
            self.zero(g.subs(t, 0))
            self.zero(sp.diff(g, t).subs(t, 0) - 1)

        alpha, beta, c0 = sp.symbols("alpha beta c0", nonzero=True)
        chi = alpha * t + beta
        primitive = -c0 / (6 * alpha**3 * chi)
        self.zero(sp.diff(primitive, t, 3) - c0 / chi**4)
        self.zero(chi * sp.diff(primitive, t, 4) + 4 * alpha * sp.diff(primitive, t, 3))
        # The alpha=0 homogeneous equation permits only a cubic after four
        # exact primitive subtractions; the displayed polynomial is a control.
        coefficients = sp.symbols("c0:4")
        cubic = sum(coefficients[j] * t**j for j in range(4))
        self.zero(sp.diff(cubic, t, 4))

    def test_euler_gamma_and_projected_quadratic_shear(self):
        v = sp.symbols("v", nonzero=True)  # Formal v^4=t, v^2=q, not the line parameter.
        A, B, lam = sp.symbols("A B lam")

        def derivative(expression):
            return sp.diff(expression, v) / (4 * v**3)

        d = 1 / (16 * v**10)
        a_cover = A * v**5
        b_cover = A * v**2 + B * v**7
        self.zero(2 * d * derivative(a_cover) + a_cover * derivative(d))
        self.zero(derivative(derivative(derivative(a_cover))) / (18 * d)
                  + 5 * A * v**3 / 24)
        self.zero(10 * d * derivative(derivative(b_cover))
                  + 5 * derivative(d) * derivative(b_cover)
                  + derivative(derivative(d)) * b_cover)
        self.zero(derivative(derivative(derivative(b_cover))) / (12 * d)
                  - A / 2 + 7 * B * v**5 / 16)
        mu = sp.symbols("mu")
        self.zero(mu * (mu - 1) - sp.Rational(5, 4) * mu + sp.Rational(7, 8)
                  - (mu - sp.Rational(1, 2)) * (mu - sp.Rational(7, 4)))
        # Pole multiplicities 3 and 5 are arithmetic on this formal cover.
        # Exhaustiveness over finite fields and pole-degree consequences are not tests.
        self.assertEqual(sp.Poly(v**3, v).degree(), 3)
        self.assertEqual(sp.Poly(v**5, v).degree(), 5)
        q = v**2
        Q = derivative(derivative(q)) / 2
        b_survives = lam * q
        W4 = -derivative(b_survives) * d - b_survives * derivative(d) / 4
        self.zero(W4 - lam * Q**2 / 2)
        self.zero(derivative(derivative(b_survives)) / 2 - lam * Q)

        U, n, z = sp.symbols("U n z")
        Q, d, kp, h, hp, M1, M1p = sp.symbols("Q d kp h hp M1 M1p")
        W3, W3p, c2, c3, M0p, M0pp = sp.symbols("W3 W3p c2 c3 M0p M0pp")
        alpha, D, Dp, g0 = sp.symbols("alpha D Dp g0")
        affine_shift = Q * U**2 + kp * U
        w = (lam * n**2 / 2 + (lam * Q * U**2 + (lam * kp + alpha) * U + D) * n
             + lam * Q**2 * U**4 / 2 + W3 * U**3
             + (c2 / 2 - h * M1) * U**2 + M0p * U + g0)
        g3 = W3 - lam * Q * kp - alpha * Q
        g2 = c2 / 2 - h * M1 - lam * kp**2 / 2 - D * Q - alpha * kp
        g1 = M0p - D * kp
        self.zero(w.subs(n, z - affine_shift) - lam * z**2 / 2
                  - (alpha * U + D) * z - g3 * U**3 - g2 * U**2 - g1 * U - g0)
        jets = {Q: 3 * d, kp: 2 * h, h: hp, M1: M1p,
                W3: W3p, c2: c3, M0p: M0pp, D: Dp}

        def jet_derivative(expression):
            return sum(sp.diff(expression, slot) * value for slot, value in jets.items())

        relations = {M1p: lam * kp + alpha,
                     W3p: 3 * d * (lam * kp + alpha) + 2 * lam * h * Q,
                     c3: 6 * d * D + 2 * hp * M1 + 6 * h * (lam * kp + alpha),
                     M0pp: 2 * h * D}
        self.zero(jet_derivative(g3).subs(relations, simultaneous=True))
        self.zero((jet_derivative(g2) + Q * Dp).subs(relations, simultaneous=True))
        self.zero((jet_derivative(g1) + kp * Dp).subs(relations, simultaneous=True))

    def test_original_columns_transport_and_both_inverse_orders(self):
        q = sp.symbols("q", nonzero=True)
        X, y, n = sp.symbols("X y n")
        lam, alpha, beta, D = sp.symbols("lam alpha beta D")
        k = sp.Function("k")(q)
        c = sp.Function("c")(q)
        M0 = sp.Function("M0")(q)
        g0 = sp.Function("g0")(q)
        G = sp.Function("G")(y)  # Stands for any complex polynomial correction.

        def derivative(expression):
            return sp.diff(expression, q) / (2 * q)

        t = q**2
        Q = derivative(derivative(q)) / 2
        d = derivative(Q) / 3
        h = derivative(derivative(k)) / 2
        F = d * y**3 + h * y**2
        FU = sp.diff(F, y)
        b = lam * q
        M1 = lam * k + alpha * t + beta
        rho = b * n + c
        P = derivative(rho) * y - b * F + M1 * n + M0
        z0 = n + Q * y**2 + derivative(k) * y
        w0 = lam * z0**2 / 2 + (alpha * y + D) * z0 + G + g0
        Ychart = y + t * X
        Zchart = z0 + (derivative(q) * y + k) * X + q * X**2
        Wchart = w0 + P * X + rho * X**2
        A0chart = alpha * Ychart + beta * X + D
        corrected = Wchart - lam * Zchart**2 / 2 - A0chart * Zchart
        self.zero(sp.diff(corrected, n))
        self.zero(corrected.subs(X, 0) - G - g0)

        def transverse(expression):
            return derivative(expression) - X * sp.diff(expression, y) - FU * sp.diff(expression, n)

        self.zero(transverse(X))
        self.zero(transverse(Ychart))
        self.zero(transverse(Zchart))
        self.zero(transverse(A0chart))
        # Check the exact transport decomposition before imposing the two
        # scalar PDEs. These unrestricted inputs need not satisfy those PDEs.
        script_w = sp.Function("script_w")(q, n, y)
        script_p = sp.Function("script_p")(q, n, y)
        literal_W = script_w + X * script_p + X**2 * rho

        def delta(expression):
            return derivative(expression) - FU * sp.diff(expression, n)

        self.zero(transverse(literal_W) - delta(script_w)
                  - X * (delta(script_p) - sp.diff(script_w, y))
                  - X**2 * (delta(rho) - sp.diff(script_p, y)))

        Y, Z, W, I = sp.symbols("Y Z W I")
        Q0 = sp.Function("Q0")(X, Y)
        A0 = alpha * Y + beta * X + D
        Imap = W - lam * Z**2 / 2 - A0 * Z - Q0
        Wback = I + lam * Z**2 / 2 + A0 * Z + Q0
        self.zero(Imap.subs(W, Wback) - I)
        self.zero(Wback.subs(I, Imap) - W)
        transported = g0 + Q0.subs(Y, Ychart)
        self.zero(derivative(transported) - X * sp.diff(transported, y) - derivative(g0))


if __name__ == "__main__":
    unittest.main()
