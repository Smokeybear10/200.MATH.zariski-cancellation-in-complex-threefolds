"""Finite pass108 row, Artin, and conic identities, in exactly two methods.

These symbolic controls do not establish purity, all-degree generation,
Hartogs coefficient contraction, local integrality of a divided quartic,
or existence of an original constant-acceleration frame. The examples of
gcd rows are formal coefficient examples, not realizable actual frames.
"""

import unittest

import sympy as sp


class MixedPureQuarticChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_quartic_row_and_mixed_artin_coefficients(self):
        G, r, c, d, k, ell = sp.symbols("G r c d k ell")

        def deriv(expression):
            return sp.expand(r * sp.diff(expression, G)
                             + d * sp.diff(expression, r))

        image = G**2
        for _ in range(4):
            image = deriv(image)
        self.assert_zero(image - 6 * d**2)
        self.assert_zero(deriv(image))

        row = sp.Matrix([[6 * d**2, k, ell]])
        generic_kernel = sp.Matrix([
            [k, ell], [-6 * d**2, 0], [0, -6 * d**2]
        ])
        self.assertEqual(row * generic_kernel, sp.zeros(1, 2))
        self.assertEqual(generic_kernel.rank(), 2)

        x, y = sp.symbols("x y")
        base_P = x + y
        # Nonreduced parameter pairs, followed by an explicitly forbidden
        # unit-A0 coefficient pattern. No example is an actual frame.
        cases = [
            (x**2, x**2 * y**3, 6 * x**2, y**3, 0),
            (x**2, y**3, 6 * x**4, y**3, 0),
            (x**2, x**4, sp.Integer(6), sp.Integer(1), 6),
        ]
        for b, L, expected_A, expected_B, slope_constant in cases:
            with self.subTest(b=b, L=L):
                self.assertEqual(sp.gcd(base_P, L), 1)
                D = sp.gcd(6 * b**2, L)
                A0 = sp.cancel(6 * b**2 / D)
                B0 = sp.cancel(L / D)
                self.assert_zero(A0 - expected_A)
                self.assert_zero(B0 - expected_B)
                self.assertEqual(sp.gcd(A0, B0), 1)
                self.assert_zero(6 * (b * base_P)**2 * B0
                                 - base_P**2 * L * A0)
                V3 = B0 * G**2 - A0 * c
                for component in (0, 1):
                    slope = sp.diff(V3.subs(G, component), c)
                    self.assert_zero(slope + A0)
                self.assertEqual(A0.subs({x: 0, y: 0}), slope_constant)

        modulus = G**3 - G**2

        def reduce_artin(expression):
            return sp.rem(sp.expand(expression), modulus, G)

        nilpotent, simple = G - G**2, G**2
        self.assert_zero(reduce_artin(nilpotent**2))
        self.assert_zero(reduce_artin(simple**2 - simple))
        self.assert_zero(reduce_artin(nilpotent * simple))
        # Coefficient vectors in 1,G,G^2,c retain the whole nilpotent fiber.
        monomials = [1, G, G**2, c]

        def vector(expression):
            poly = sp.Poly(reduce_artin(expression), G, c)
            return sp.Matrix([poly.coeff_monomial(term) for term in monomials])

        pure_piece = sp.Matrix.hstack(*(vector(term) for term in monomials))
        self.assertEqual(pure_piece, sp.eye(4))
        for lam, rho, expected_rank in ((1, 1, 2), (1, 2, 3)):
            speed = lam * nilpotent + rho * simple
            self.assert_zero(speed - lam * G - (rho - lam) * G**2)
            rank = sp.Matrix.hstack(vector(1), vector(G), vector(speed)).rank()
            self.assertEqual(rank, expected_rank)
        # This is only the one-way speed test, not a converse for W3.

    def test_sharp_conic_and_divided_quartic_identities(self):
        a, b, G, H, eps, B1, B2 = sp.symbols("a b G H eps B1 B2")
        r = a * G + b * H
        Q = eps * r**2 - 2 * B2 * G + 2 * B1 * H
        sharp_rhs = 2 * B1 * H + 2 * eps * a * b * G * H + eps * b**2 * H**2
        self.assert_zero(Q + 2 * B2 * G - eps * a**2 * G**2 - sharp_rhs)

        x, y, H1, H2 = sp.symbols("x y H1 H2")
        decomposition = (
            x * (2 * B1 * H1 + 2 * eps * a * b * G * H1)
            + y * (2 * B1 * H2 + 2 * eps * a * b * G * H2)
            + eps * b**2 * (
                x**2 * H1**2 + 2 * x * y * H1 * H2 + y**2 * H2**2)
        )
        self.assert_zero(sharp_rhs.subs(H, x * H1 + y * H2) - decomposition)
        self.assert_zero((sharp_rhs.subs(H, x * H1 + y * H2)
                          - decomposition).subs({a: x**2, b: y**3}))

        # Normalized smooth-a formulas. U is a rational expression here;
        # the actual proof, not this check, must establish U in A_R.
        beta, delta, zeta, qcoef = sp.symbols("beta delta zeta qcoef")
        B2n = a * beta + b**2 * delta
        Qn = a * zeta + b**2 * qcoef
        P = a**2 + b * B2n
        NG = eps * b * r + a
        NH = -eps * a * r + B2n

        def deriv(expression):
            return sp.cancel(NG * sp.diff(expression, G)
                             + NH * sp.diff(expression, H))

        self.assert_zero(deriv(r) - P)
        self.assert_zero(deriv(NG) - eps * b * P)
        self.assert_zero(deriv(NH) + eps * a * P)
        conic = eps * r**2 - 2 * B2n * G + 2 * a * H - Qn
        self.assert_zero(deriv(conic))
        U = (eps * H**2 - 2 * delta * G - qcoef) / a
        proposed_H_rhs = (zeta + 2 * beta * G - eps * a * G**2
                          - 2 * eps * b * G * H - b**2 * U)
        self.assert_zero(a * (2 * H - proposed_H_rhs) - conic)
        value = U
        iterates = []
        for _ in range(5):
            value = deriv(value)
            iterates.append(value)
        self.assert_zero(iterates[2] + 6 * eps**2 * P * NH)
        self.assert_zero(iterates[3] - 6 * eps**3 * a * P**2)
        self.assert_zero(iterates[4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
