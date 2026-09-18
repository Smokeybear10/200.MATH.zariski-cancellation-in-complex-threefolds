"""One finite symbolic control method for degree-module rigidity102.

Checks the conic/matrix identities, first base-adic coefficient maps on
whole and mixed Artin fibers, and sample weighted comparisons. It does
not prove finite freeness, actual flatness, degree-module saturation,
a canonical original frame, or the universal theorem in the note.
"""

import unittest

import sympy as S


class QuadraticDegreeModuleChecks(unittest.TestCase):
    def test_conic_first_coefficients_and_weight_comparison(self):
        a, b, theta, B1, B2, G, w = S.symbols("a b theta B1 B2 G w")
        r = a*G + b*w
        p = a*B1 + b*B2
        NG = theta*b*r + B1
        Nw = -theta*a*r + B2

        def N(expr):
            return S.expand(NG*S.diff(expr, G) + Nw*S.diff(expr, w))

        self.assertEqual(S.expand(N(r)-p), 0)
        self.assertEqual(N(N(r)), 0)
        self.assertEqual(S.expand(N(NG)-theta*b*p), 0)
        self.assertEqual(S.expand(N(Nw)+theta*a*p), 0)
        self.assertEqual(N(N(NG)), 0)
        self.assertEqual(N(N(Nw)), 0)
        conic = theta*r**2 - 2*B2*G + 2*B1*w
        self.assertEqual(N(conic), 0)

        matrix = S.Matrix(((0, B1, B2),
                           (0, theta*a*b, -theta*a**2),
                           (0, theta*b**2, -theta*a*b)))
        self.assertEqual((matrix**3).applyfunc(S.expand), S.zeros(3))
        self.assertEqual((matrix*S.Matrix((0, a, b))).applyfunc(S.expand),
                         S.Matrix((p, 0, 0)))
        self.assertNotEqual(S.expand(matrix**2)[0, 1], 0)

        # A primitive pair need not be unimodular; theta need not be a unit.
        s, t, c, g, eta = S.symbols("s t c g eta")
        nonunit_case = {a: s, b: t, theta: s, B1: s**2, B2: t**2}
        self.assertEqual(S.gcd(s, t), 1)
        self.assertEqual(s.subs({s: 0, t: 0}), 0)
        self.assertEqual(t.subs({s: 0, t: 0}), 0)
        self.assertEqual(S.expand(N(conic).subs(nonunit_case)), 0)
        self.assertEqual((matrix.subs(nonunit_case)**3).applyfunc(S.expand),
                         S.zeros(3))

        b10, b11, b20, b21, q10, q11 = S.symbols(
            "b10 b11 b20 b21 q10 q11")
        unknowns = (b10, b11, b20, b21, q10, q11)
        first_B1 = s*b10 + t*b11
        first_B2 = s*b20 + t*b21
        first_Q = s*q10 + t*q11
        u10, u11, v10, v11, z10, z11 = S.symbols(
            "u10 u11 v10 v11 z10 z11")
        first_quadratic = (s*u10+t*u11, s*v10+t*v11, s*z10+t*z11)

        for mixed in (False, True):
            for beta, expected_rank in ((c, 6), (c**2, 6), (S.Integer(2), 4)):
                with self.subTest(mixed=mixed, beta=str(beta)):
                    modulus = g**2*(g-1) if mixed else g**2
                    epsilon = g-g**2 if mixed else g
                    w_fiber = eta*g**2 + epsilon*beta if mixed else epsilon*beta
                    raw = (first_quadratic[0]*g**2
                           + 2*first_quadratic[1]*g*w_fiber
                           + first_quadratic[2]*w_fiber**2
                           - 2*first_B2*g + 2*first_B1*w_fiber - first_Q)
                    whole = S.rem(S.expand(raw), modulus, g)
                    double = S.expand(S.rem(whole, g**2, g))
                    expected = -2*first_B2*g + 2*first_B1*g*beta - first_Q
                    self.assertEqual(S.expand(double-expected), 0)
                    coefficients = S.Poly(double, s, t, g, c).coeffs()
                    coefficient_matrix = S.Matrix(
                        [[S.diff(value, symbol) for symbol in unknowns]
                         for value in coefficients])
                    self.assertEqual(coefficient_matrix.rank(), expected_rank)
                    if expected_rank == 6:
                        self.assertEqual(len(coefficient_matrix.nullspace()), 0)
                    else:
                        # Constant beta loses independence, so this argument
                        # must not claim six forced zero coefficients.
                        self.assertEqual(len(coefficient_matrix.nullspace()), 2)

        x, y = S.symbols("x y")
        lam, b0 = S.symbols("lam b0", nonzero=True)
        k20, k11, k02, ell1, ell2, j1, j2 = S.symbols(
            "k20 k11 k02 ell1 ell2 j1 j2")
        base_square = k20*s**2 + k11*s*t + k02*t**2
        base_first_a2 = ell1*s + ell2*t
        base_first_ab = j1*s + j2*t
        for beta in (c, c**2):
            with self.subTest(weight_beta=str(beta)):
                rhs = base_square - base_first_a2*y - base_first_ab*beta*y
                weighted_rhs = S.expand(rhs.subs({s: x, t: b0*y**2}))
                terms = S.Poly(weighted_rhs, x, y).terms()
                self.assertTrue(all(2*i+j >= 3 for (i, j), value in terms
                                    if value != 0))
                degree_two = sum(value*x**i*y**j for (i, j), value in terms
                                 if 2*i+j == 2)
                self.assertEqual(degree_two, 0)
                lhs = lam*S.diff(beta, c)*y**2
                self.assertNotEqual(lhs, 0)
                self.assertEqual(S.Poly(lhs, x, y).monoms(), [(0, 2)])


if __name__ == "__main__":
    unittest.main(verbosity=2)

