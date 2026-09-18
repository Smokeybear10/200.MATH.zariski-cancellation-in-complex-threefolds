"""Finite exact controls for the zero-r coefficient normal forms in pass173.

The first two methods differentiate independent coefficient functions and
extract polynomial coefficients. They do not assume rationality of the
written proof's finite coefficient field, or prove its actual field-return
step. The third method separates a specialization from the actual171
square-root example, a new formal solution with nonconstant scalar D, and
a deliberately invalid lower-coefficient boundary. No formal solution is
asserted to be an actual cusp frame.

The chart derivation and a W-linear polynomial shear are checked literally.
The latter is a coordinate-map control, not existence of an invariant lift.
No older checker is imported or run. Root owns canonical execution.
"""

import unittest

import sympy as sp


def zero(expression):
    """All callers give polynomial expressions in the selected formal slots."""
    assert sp.expand(expression) == 0, sp.expand(expression)


def integrated_R(t, n, U, a, b, c, h, m, R0):
    rho = a * n**2 + b * n + c
    q = sp.diff(rho, n)
    F = U**3 + h * U**2
    P = sp.diff(rho, t) * U - q * F + m
    R = (
        a * F**2
        - sp.diff(q, t) * U * F
        - q * sp.diff(h, t) * U**3 / 3
        + sp.diff(rho, t, 2) * U**2 / 2
        + sp.diff(m, t) * U
        - sp.diff(m, n) * F
        + R0
    )
    return rho, q, F, P, R


class ZeroRCoefficientNormalFormControls(unittest.TestCase):
    def test_unrestricted_integration_and_highest_coefficients(self):
        t, n, U = sp.symbols("t n U")
        a, b, c, h = [sp.Function(name)(t) for name in ("a", "b", "c", "h")]
        m, R0 = sp.Function("m")(t, n), sp.Function("R0")(t, n)
        rho, q, F, P, R = integrated_R(t, n, U, a, b, c, h, m, R0)
        delta = lambda G: sp.diff(G, t) - sp.diff(F, U) * sp.diff(G, n)
        zero(sp.diff(R, U) - delta(P))
        zero(sp.diff(rho, n) - q)
        zero(sp.diff(q, n) - 2 * a)
        zero(sp.diff(P, U) - sp.diff(rho, t) + q * sp.diff(F, U))

        # Cleared transformation of old ∂t + P_U ∂rho into delta,
        # on an independent two-variable coefficient, with no inverse q.
        test = sp.Function("test")(t, n)
        zero(
            q * sp.diff(test, t)
            - sp.diff(rho, t) * sp.diff(test, n)
            + sp.diff(P, U) * sp.diff(test, n)
            - q * delta(test)
        )
        coefficients = sp.Poly(sp.expand(delta(R)), U)
        self.assertEqual(coefficients.degree(), 6)
        zero(coefficients.coeff_monomial(U**6) - 7 * sp.diff(a, t))
        zero(
            coefficients.coeff_monomial(U**5)
            - 12 * sp.diff(a, t) * h
            - 4 * a * sp.diff(h, t)
            - 3 * sp.diff(m, n, 2)
        )

    def test_full_lower_coefficient_recurrence_and_compatibility(self):
        t, n, U, a = sp.symbols("t n U a")
        b, c, h, M1, M0, R00 = [
            sp.Function(name)(t) for name in ("b", "c", "h", "M1", "M0", "R00")
        ]
        R0 = sp.Function("R0")(t, n)  # Kept unrestricted through the U² gate.
        hp, hpp, hppp = [sp.diff(h, t, j) for j in (1, 2, 3)]
        bp, bpp, bppp = [sp.diff(b, t, j) for j in (1, 2, 3)]
        m = -sp.Rational(2, 3) * a * hp * n**2 + M1 * n + M0
        rho, q, F, P, R = integrated_R(t, n, U, a, b, c, h, m, R0)
        delta = lambda G: sp.diff(G, t) - sp.diff(F, U) * sp.diff(G, n)
        expected = {
            6: a,
            5: 2 * a * h,
            4: a * h**2 - bp,
            3: 2 * a * hp * n / 3 - bp * h - b * hp / 3 - M1,
            2: (bpp / 2 + 4 * a * h * hp / 3) * n
            + sp.diff(c, t, 2) / 2 - h * M1,
            1: -2 * a * hpp * n**2 / 3 + sp.diff(M1, t) * n + sp.diff(M0, t),
            0: R0,
        }
        literal = sp.Poly(sp.expand(R), U)
        for j in range(7):
            zero(literal.coeff_monomial(U**j) - expected[j])

        direct = sp.Poly(sp.expand(delta(R)), U)
        for j in range(9):
            recurrence = (
                sp.diff(expected.get(j, sp.S.Zero), t)
                - 3 * sp.diff(expected.get(j - 2, sp.S.Zero), n)
                - 2 * h * sp.diff(expected.get(j - 1, sp.S.Zero), n)
            )
            zero(direct.coeff_monomial(U**j) - recurrence)
        zero(direct.coeff_monomial(U**6))
        zero(direct.coeff_monomial(U**5))
        zero(direct.coeff_monomial(U**4) + 5 * bpp / 2 + 10 * a * h * hp / 3)
        c3 = direct.coeff_monomial(U**3).subs(bpp, -4 * a * h * hp / 3)
        zero(c3 - 14 * a * hpp * n / 3 + 4 * bp * hp / 3
             + b * hpp / 3 + 4 * sp.diff(M1, t))

        # Do not silently discard a*h'' before its own coefficient gate.
        # The exact excess over the displayed reduced U² formula is recorded.
        raw_u2 = (
            (bppp / 2 + 4 * a * (hp**2 + h * hpp) / 3) * n
            + sp.diff(c, t, 3) / 2 - hp * M1 - 3 * h * sp.diff(M1, t)
            - 3 * sp.diff(R0, n)
        )
        zero(direct.coeff_monomial(U**2) - raw_u2 - 8 * a * h * hpp * n / 3)

        scalar_D = sp.diff(c, t, 3) / 6 - hp * M1 / 3 - h * sp.diff(M1, t)
        regular_R0 = a * hp**2 * n**2 / 9 + scalar_D * n + R00
        regular_R = R.subs(R0, regular_R0)
        lower = sp.Poly(sp.expand(delta(regular_R)), U)
        # These discrepancies vanish using a*h''=a*h'''=0.
        reduced_u2 = lower.coeff_monomial(U**2).subs(
            bppp, -4 * a * (hp**2 + h * hpp) / 3
        )
        zero(reduced_u2 - 10 * a * h * hpp * n / 3)
        target_u1 = (
            (sp.diff(M1, t, 2) - 4 * a * h * hp**2 / 9) * n
            + sp.diff(M0, t, 2) - 2 * h * scalar_D
        )
        zero(lower.coeff_monomial(U) - target_u1 + 2 * a * hppp * n**2 / 3)
        zero(
            lower.coeff_monomial(1)
            - sp.diff(scalar_D, t) * n - sp.diff(R00, t)
            - 2 * a * hp * hpp * n**2 / 9
        )
        M1prime = -bp * hp / 3 - b * hpp / 12
        differentiated = sp.diff(M1prime, t).subs(bpp, -4 * a * h * hp / 3)
        zero(differentiated - 4 * a * h * hp**2 / 9
             + 5 * bp * hpp / 12 + b * hppp / 12)

    def test_formal_branches_chart_derivation_and_coordinate_shear(self):
        t, n, U, x, y = sp.symbols("t n U x y")
        # First tuple is the coefficient specialization of the actual171
        # square-root fixture, not a rerun of its full inverse checker.
        # Second tuple is formal only: nonconstant D is allowed by the
        # coefficient equations, but is not claimed to obey actual return.
        examples = [
            (sp.Integer(2), sp.S.Zero, sp.S.Zero, sp.S.Zero, sp.S.Zero,
             sp.S.Zero, sp.S.Zero, t, sp.S.One),
            (sp.S.Zero, sp.S.One, sp.S.Zero, t**2, t**4 / 6,
             -t / 6, t**6 / 54, t, 1 + 5 * t * n / 9),
        ]
        for a, b, c, h, k, M1, M0, R00, value in examples:
            zero(sp.diff(k, t, 2) - 2 * h)
            hp = sp.diff(h, t)
            scalar_D = sp.diff(c, t, 3) / 6 - hp * M1 / 3 - h * sp.diff(M1, t)
            R0 = a * hp**2 * n**2 / 9 + scalar_D * n + R00
            m = -2 * a * hp * n**2 / 3 + M1 * n + M0
            rho, q, F, P, R = integrated_R(t, n, U, a, b, c, h, m, R0)
            self.assertNotEqual(q, 0)
            delta = lambda G: sp.diff(G, t) - sp.diff(F, U) * sp.diff(G, n)
            zero(sp.diff(R, U) - delta(P))
            zero(delta(R) - value)
            Y = y + t * x
            Z = 3 * t * y**2 + sp.diff(k, t) * y + n
            Z += (3 * t**2 * y + k) * x + t**3 * x**2
            W = R.subs(U, y) + P.subs(U, y) * x + rho * x**2
            chart_T = lambda G: (
                sp.diff(G, t) - x * sp.diff(G, y)
                - (3 * y**2 + 2 * h * y) * sp.diff(G, n)
            )
            for G in (x, Y, Z):
                zero(chart_T(G))
            zero(chart_T(W) - value)

        # a=0, b=1, h=t³ satisfies the upper gates with this M1, but
        # violates b*h'''+5b'*h''=0. The missing U¹ term detects it.
        h, M1, M0 = t**3, -t**2 / 4, sp.S.Zero
        scalar_D = -sp.diff(h, t) * M1 / 3 - h * sp.diff(M1, t)
        R0 = scalar_D * n + t
        m = M1 * n + M0
        _, _, F, P, R = integrated_R(
            t, n, U, sp.S.Zero, sp.S.One, sp.S.Zero, h, m, R0
        )
        residual = sp.Poly(sp.expand(sp.diff(R, t) - sp.diff(F, U) * sp.diff(R, n)), U)
        for j in range(2, 7):
            zero(residual.coeff_monomial(U**j))
        zero(sp.expand(residual.coeff_monomial(U)).coeff(n) + sp.Rational(1, 2))
        self.assertEqual(sp.diff(h, t, 3), 6)

        # Independent polynomial coordinate-map control. Invariance of I
        # requires the separate field/lift proof, not this inverse identity.
        X, Y, Z, W, I, a, lam = sp.symbols("X Y Z W I a lam")
        A0, A1, A2, Q0, Q1, Q2 = sp.symbols("A0 A1 A2 Q0 Q1 Q2")
        A = A0 + A1 * X + A2 * Y
        Q = Q0 + Q1 * X * Y + Q2 * Y**3
        correction = a * (X - lam)**2 * Z**2 + A * Z + Q
        forward = (X, Y, Z, W - correction)
        inverse = (X, Y, Z, I + correction)
        forward_map = dict(zip((X, Y, Z, I), forward))
        inverse_map = dict(zip((X, Y, Z, W), inverse))
        for recovered, original in zip(inverse, (X, Y, Z, W)):
            zero(recovered.subs(forward_map, simultaneous=True) - original)
        for recovered, original in zip(forward, (X, Y, Z, I)):
            zero(recovered.subs(inverse_map, simultaneous=True) - original)


if __name__ == "__main__":
    unittest.main()
