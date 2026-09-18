"""Finite exact-algebra controls for the product-radical pruning note227.

Standalone: no proof, solver, or retained checker is imported. Algebraic
coefficient derivatives are computed in the quotient field q^2=t*rho,
without selecting an analytic square root or making L rational.

The full initial-kernel hypotheses, actual field return and scalar
calibration, module freeness and completeness of the degree proof remain
written inputs. The plane parametrizations below are formal fixtures,
not actual globally sliced frames. In particular the (4,3) fixture
satisfies the strict cofactor bound but fails the conductor inclusion.
No ambient coordinate, recognition or unrestricted theorem is tested.
Root alone may execute this source after a complete saved-source read.
"""

from math import factorial
import unittest

import sympy as sp


t, rho, q = sp.symbols("t rho q", nonzero=True)
U, V, v = sp.symbols("U V v")
field_relation = q**2 - t * rho


def reduce_field(expression):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    numerator = sp.rem(numerator, field_relation, q)
    denominator = sp.rem(denominator, field_relation, q)
    if denominator == 0:
        raise ValueError("Zero denominator in the algebraic coefficient field")
    return sp.cancel(numerator / denominator)


def Dt(expression):
    return reduce_field(sp.diff(expression, t) + q * sp.diff(expression, q) / (2 * t))


def Dr(expression):
    return reduce_field(sp.diff(expression, rho) + q * sp.diff(expression, q) / (2 * rho))


def qjet(i, j):
    result = q
    for _ in range(i):
        result = Dt(result)
    for _ in range(j):
        result = Dr(result)
    return result


def q_taylor(order):
    return sum(qjet(i, order - i) * U**i * V**(order - i)
               / (factorial(i) * factorial(order - i))
               for i in range(order + 1))


def generic_lower(prefix, degree):
    return sum(sp.Symbol(f"{prefix}_{i}_{j}") * U**i * V**j
               for i in range(degree + 1) for j in range(degree + 1 - i))


class ProductRadicalSexticControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def field_zero(self, expression):
        self.assertEqual(reduce_field(expression), 0)

    def test_quadratic_field_derivatives_and_raw_taylor_jets(self):
        self.field_zero(Dt(field_relation))
        self.field_zero(Dr(field_relation))
        for generator in (t, rho, q):
            self.field_zero(Dt(Dr(generator)) - Dr(Dt(generator)))
        half = sp.Rational(1, 2)
        for order in range(5):
            for i in range(order + 1):
                j = order - i
                falling_i = sp.prod(half - a for a in range(i))
                falling_j = sp.prod(half - a for a in range(j))
                self.field_zero(qjet(i, j) - q * falling_i * falling_j / (t**i * rho**j))
        Xi = rho * U - t * V
        H2, H3, H4 = (q_taylor(j) for j in (2, 3, 4))
        self.field_zero(H2 + Xi**2 / (8 * q**3))
        self.field_zero(H3 - Xi**2 * (rho * U + t * V) / (16 * q**5))
        self.field_zero(H4 + Xi**2 * (5 * rho**2 * U**2 + 6 * t * rho * U * V + 5 * t**2 * V**2) / (128 * q**7))
        self.field_zero(sp.diff(H2, V) - Xi / (4 * q * rho))
        self.field_zero(Dr(H2) + Xi * (rho * U + 3 * t * V) / (16 * rho * q**3))
        self.field_zero(Dr(Dr(q)) + q / (4 * rho**2))
        # Treating q as an independent constant under coefficient partials
        # is a wrong-field negative control, not an alternative convention.
        self.assertNotEqual(reduce_field(sp.diff(q, t) - Dt(q)), 0)

    def test_full_lower_potential_eliminant_has_the_exact_sextic(self):
        # Each lower Taylor jet is independent; no lower potential is set
        # to zero to obtain the leading sextic.
        kj = {(i, j): sp.Symbol(f"k_{i}_{j}") for i in range(4) for j in range(4 - i)}
        nj = {(i, j): sp.Symbol(f"n_{i}_{j}") for i in range(3) for j in range(3 - i)}
        ell, ell_t, ell_r, m = sp.symbols("ell ell_t ell_r m")

        def jet_taylor(jets, order):
            return sum(jets[i, order - i] * U**i * V**(order - i)
                       / (factorial(i) * factorial(order - i))
                       for i in range(order + 1))

        H2, H3, H4 = (q_taylor(j) for j in (2, 3, 4))
        f = H2 + jet_taylor(kj, 1) + nj[0, 0]
        Rformal = sp.diff(f, V)
        c = Dr(H2) + kj[1, 1] * U + kj[0, 2] * V + nj[0, 1]
        S = H3 + jet_taylor(kj, 2) + jet_taylor(nj, 1)
        T0 = ell - S
        Q = H4 + jet_taylor(kj, 3) + jet_taylor(nj, 2) - ell_t * U - ell_r * V - m
        eliminant = Dr(Dr(q)) * T0**2 / 2 + Rformal * c * T0 + Rformal**2 * Q
        poly = sp.Poly(eliminant, U, V)
        self.assertEqual(poly.total_degree(), 6)
        H6 = sum(coefficient * U**i * V**j for (i, j), coefficient in poly.terms() if i + j == 6)
        Xi = rho * U - t * V
        expected = -U**2 * Xi**4 / (512 * q**9)
        self.field_zero(H6 - expected)
        self.field_zero(Rformal - Xi / (4 * q * rho) - kj[0, 1])
        for lower_symbol in set(kj.values()) | set(nj.values()) | {ell, ell_t, ell_r, m}:
            self.zero(sp.diff(H6, lower_symbol))
        bracket = (-(rho * U + t * V)**2
                   + 2 * (rho * U + 3 * t * V) * (rho * U + t * V)
                   - (5 * rho**2 * U**2 + 6 * t * rho * U * V + 5 * t**2 * V**2))
        self.zero(bracket + 4 * rho**2 * U**2)
        self.field_zero(H6.subs({U: 1, V: 0}, simultaneous=True) + rho**4 / (512 * q**9))

    def test_formal_degree_gates_with_generic_lower_cofactor_terms(self):
        Xi = rho * U - t * V
        kr = sp.symbols("kr")
        Rformal = Xi / (4 * q * rho) + kr
        # U-top conic: the Xi^4 top evaluates in degree eight; every
        # ordinary-degree-at-most-three lower term has degree at most six.
        point = {U: v, V: v**2}
        cofactor = Xi**4 + generic_lower("conic", 3)
        self.assertEqual(sp.Poly(cofactor.subs(point, simultaneous=True), v).degree(), 8)
        self.assertEqual(sp.Poly(generic_lower("conic", 3).subs(point, simultaneous=True), v).degree(), 6)
        self.assertEqual(sp.Poly(Rformal.subs(point, simultaneous=True), v).degree(), 2)
        self.assertGreater(8, 3 * 2)

        for d in (1, 2):
            with self.subTest(cubic_transverse_degree=d):
                point = {U: v**3, V: (rho * v**3 - v**d) / t}
                self.zero(Xi.subs(point, simultaneous=True) - v**d)
                cofactor = U**2 * Xi + generic_lower("cubic", 2)
                self.assertEqual(sp.Poly(cofactor.subs(point, simultaneous=True), v).degree(), 6 + d)
                self.assertEqual(sp.Poly(Rformal.subs(point, simultaneous=True), v).degree(), d)
                self.assertGreater(6 + d, 3 * d)

        for d in (1, 2, 3):
            with self.subTest(quartic_transverse_degree=d):
                point = {U: v**4, V: (rho * v**4 - v**d) / t}
                cofactor = U**2 + generic_lower("quartic", 1)
                self.assertEqual(sp.Poly(cofactor.subs(point, simultaneous=True), v).degree(), 8)
                self.assertEqual(sp.Poly(Rformal.subs(point, simultaneous=True), v).degree(), d)
                self.assertEqual(8 <= 3 * d, d == 3)

    def test_degree_five_gap_and_missing_conductor_boundary(self):
        # The four basis-index residues are exhaustive once the written
        # monic rank-four module theorem is supplied. No test proves it.
        self.assertEqual({3 * j % 4 for j in range(4)}, {0, 1, 2, 3})
        for j in range(4):
            possible_i = sp.Rational(5 - 3 * j, 4)
            self.assertFalse(possible_i.is_integer and possible_i >= 0)
        A, B = sp.symbols("A B")
        relation = B**4 - A**3
        for power in range(8):
            quotient, remainder = sp.div(B**power, relation, B)
            self.zero(B**power - quotient * relation - remainder)
            self.zero(remainder - A**(3 * (power // 4)) * B**(power % 4))
            self.zero(remainder.subs({A: v**4, B: v**3}, simultaneous=True) - v**(3 * power))

        # Formal (4,3) boundary: coarse AND strict cofactor bounds hold.
        # Its return has degree3, but R*v^2 has forbidden degree5 in
        # C=L[v^4,v^3]. Thus this fixture lacks R*L[v] subset C.
        Xi = rho * U - t * V
        G, Q1 = Xi**4 - U**3, U**2
        point = {U: v**4, V: (rho * v**4 - v**3) / t}
        self.zero(G.subs(point, simultaneous=True))
        q1 = sp.expand(Q1.subs(point, simultaneous=True))
        R = v**3
        self.assertEqual(sp.Poly(G * Q1, U, V).total_degree(), 6)
        self.assertEqual(sp.Poly(q1, v).degree(), 8)
        self.zero(R**3 / v - q1)
        self.assertEqual(sp.Poly(R * v**2, v).degree(), 5)
        self.assertEqual(sp.Poly(v**6, v).degree(), 6)


if __name__ == "__main__":
    unittest.main()
