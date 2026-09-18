"""Standalone finite exact controls for the arbitrary-top-plinth construction.

The written proof, not this suite, supplies the all-degree pole contraction,
the arbitrary-polynomial quantifier, and the inherited global minimum.
Only unittest and SymPy are imported. No solver or sibling checker is used.
"""

import unittest

import sympy as sp


x, lam, b, c, h, w, i = sp.symbols("x lam b c h w i")
par, k, a1, a2, a3 = sp.symbols("par k a1 a2 a3")
ff, ss = sp.symbols("ff ss")


def expand(expression):
    return sp.expand(expression)


def apply_bh(field, expression):
    return expand(field[0] * sp.diff(expression, b)
                  + field[1] * sp.diff(expression, h))


def apply_bc(field, expression):
    return expand(field[0] * sp.diff(expression, b)
                  + field[1] * sp.diff(expression, c))


def flow(p):
    invariant = p * b + x**2 * h**2
    new_h = h - 2 * lam * x * p * invariant**2
    new_b = (b + 4 * lam * x**3 * h * invariant**2
             - 4 * lam**2 * x**4 * p * invariant**4)
    return invariant, new_b, new_h


class MinimumTopStructureChecks(unittest.TestCase):
    def test_flow_is_reconstructed_from_the_nilpotent_field(self):
        F, W, H = flow(par)
        field = (2 * x**4 * h, -x**2 * par)
        self.assertEqual(apply_bh(field, F), 0)
        self.assertEqual(apply_bh(field, apply_bh(field, h)), 0)
        self.assertEqual(apply_bh(field, apply_bh(field, b)),
                         -2 * x**6 * par)
        self.assertEqual(apply_bh(field, apply_bh(
            field, apply_bh(field, b))), 0)
        time = 2 * lam * F**2 / x
        derived_b = (b + time * apply_bh(field, b)
                     + time**2 * apply_bh(field, apply_bh(field, b)) / 2)
        derived_h = h + time * apply_bh(field, h)
        self.assertEqual(sp.cancel(derived_b - W), 0)
        self.assertEqual(sp.cancel(derived_h - H), 0)
        self.assertEqual(expand(par * W + x**2 * H**2 - F), 0)
        determinant = (sp.diff(W, b) * sp.diff(H, h)
                       - sp.diff(W, h) * sp.diff(H, b))
        self.assertEqual(sp.factor(determinant), 1)

    def test_independent_plane_has_both_polynomial_inverse_compositions(self):
        F, W, H = flow(par)
        recovered_h = H + 2 * lam * x * par * F**2
        recovered_b = (W - 4 * lam * x**3 * H * F**2
                       - 4 * lam**2 * x**4 * par * F**4)
        # The invariant used in these substitutions is checked from the
        # actual transformed generators, not assumed unchanged.
        self.assertEqual(expand(par * W + x**2 * H**2), expand(F))
        self.assertEqual(expand(recovered_h), h)
        self.assertEqual(expand(recovered_b), b)
        Fstar = par * w + x**2 * i**2
        old_h = i + 2 * lam * x * par * Fstar**2
        old_b = (w - 4 * lam * x**3 * i * Fstar**2
                 - 4 * lam**2 * x**4 * par * Fstar**4)
        self.assertEqual(expand(par * old_b + x**2 * old_h**2), expand(Fstar))
        back_w = (old_b + 4 * lam * x**3 * old_h * Fstar**2
                  - 4 * lam**2 * x**4 * par * Fstar**4)
        back_i = old_h - 2 * lam * x * par * Fstar**2
        self.assertEqual(expand(back_w), w)
        self.assertEqual(expand(back_i), i)
        self.assertEqual(W.subs(lam, 0), b)
        self.assertEqual(H.subs(lam, 0), h)

    def test_forward_physical_quotient_has_an_explicit_polynomial_expansion(self):
        # p=1+x*k is a formal polynomial identity. Substitution k=k(x)
        # remains valid. No x differentiation is used in this identity.
        p = 1 + x * k
        F, W, H = flow(p)
        v = 1 + lam * x
        U = 4 * lam * h * F**2 - 4 * lam**2 * x * p * F**4
        difference_quotient = sp.cancel((1 - p**3) / x)
        C = (difference_quotient * b**2 - 2 * p**2 * x * b * h**2
             - p * x**3 * h**4)
        self.assertEqual(expand(x * C), expand(b**2 - p * F**2))
        self.assertEqual(expand(W - b), expand(x**3 * U))
        correction = (lam**2 * b**2 + 2 * lam * C
                      + v**2 * (2 * x * b * U + x**4 * U**2))
        sp.Poly(correction, x, lam, b, h, k)
        self.assertEqual(expand(H + v**2 * W**2 - (h + b**2)
                                - x**2 * correction), 0)
        # h+b²=x²c makes Z=c+correction globally polynomial.
        self.assertEqual(correction.subs(lam, 0), 0)
        reduced_numerator = sp.rem(
            expand((H + v**2 * W**2).subs(h, x**2 * c - b**2)),
            x**2, x)
        self.assertEqual(reduced_numerator, 0)

    def test_inverse_physical_quotient_has_an_explicit_polynomial_expansion(self):
        p = 1 + x * k
        Fstar = p * w + x**2 * i**2
        old_h = i + 2 * lam * x * p * Fstar**2
        V = -4 * lam * i * Fstar**2 - 4 * lam**2 * x * p * Fstar**4
        old_b = w + x**3 * V
        difference_quotient = sp.cancel((p**3 - 1) / x)
        C = (difference_quotient * w**2 + 2 * p**2 * x * w * i**2
             + p * x**3 * i**4)
        self.assertEqual(expand(x * C), expand(p * Fstar**2 - w**2))
        correction = -lam**2 * w**2 + 2 * lam * C + 2 * x * w * V + x**4 * V**2
        sp.Poly(correction, x, lam, w, i, k)
        v = 1 + lam * x
        self.assertEqual(expand(old_h + old_b**2 - (i + v**2 * w**2)
                                - x**2 * correction), 0)
        # i+v²w²=x²z makes the physical inverse c*=z+correction.
        self.assertEqual(correction.subs(lam, 0), 0)
        physical_i_mod_x2 = -w**2 - 2 * lam * x * w**2
        inverse_numerator_mod_x2 = sp.rem(
            expand((old_h + old_b**2).subs(i, physical_i_mod_x2)),
            x**2, x)
        self.assertEqual(inverse_numerator_mod_x2, 0)

    def test_canonical_intertwining_and_actual_degree_one_top(self):
        F, W, H = flow(par)
        Lbh = (2 * x**4 * h, -x**2 * par)
        vertical = (x**2 - 4 * lam * x * par * F * Lbh[0],
                    -4 * lam * x * par * F * Lbh[1])
        self.assertEqual(apply_bh(vertical, W), x**2)
        self.assertEqual(apply_bh(vertical, H), 0)
        # Differentiate the unreduced physical numerator independently.
        v = 1 + lam * x
        self.assertEqual(
            apply_bh(vertical, H + v**2 * W**2),
            expand(2 * v**2 * W * x**2))
        p = 1 - x
        h0 = x**2 * c - b**2
        actual_F = p * b + x**2 * h0**2
        actual_H = h0 - 2 * lam * x * p * actual_F**2
        derived = (sp.diff(actual_H, c), -sp.diff(actual_H, b))
        L = (2 * x**4 * h0, -p + 4 * x**2 * b * h0)
        expected = (x**2 - 4 * lam * x * p * actual_F * L[0],
                    2 * b - 4 * lam * x * p * actual_F * L[1])
        self.assertEqual(tuple(map(expand, derived)), tuple(map(expand, expected)))
        first = tuple(expand(sp.diff(value, lam)) for value in derived)
        self.assertNotEqual(first, (0, 0))
        self.assertEqual(tuple(sp.diff(value, lam) for value in first), (0, 0))
        self.assertEqual(sp.Poly(derived[0], lam).degree(), 1)
        self.assertEqual(sp.Poly(derived[1], lam).degree(), 1)

    def test_primitive_gcd_and_entire_fixed_ideal_include_repeated_roots(self):
        h0 = x**2 * c - b**2
        for p in (sp.Integer(1), 1 - x, (1 - x)**2, 1 - x**2):
            with self.subTest(p=p):
                F = p * b + x**2 * h0**2
                L = (2 * x**4 * h0, -p + 4 * x**2 * b * h0)
                self.assertEqual(sp.gcd(*L), 1)
                actual_ideal = sp.groebner(L, c, b, x)
                expected_ideal = sp.groebner((p, h0), c, b, x)
                self.assertEqual(tuple(actual_ideal), tuple(expected_ideal))
                top = tuple(-4 * x * p * F * value for value in L)
                actual_gcd = sp.gcd(*top)
                self.assertEqual(sp.cancel(actual_gcd / (-4 * x * p * F))
                                 .free_symbols, set())
                self.assertEqual(tuple(value.subs(x, 0) for value in L), (0, -1))
                if p != 1:
                    self.assertEqual(tuple(expand(value.subs(
                        {x: 1, c: b**2})) for value in L), (0, 0))

    def test_slope_corrected_slice_and_all_three_residue_controls(self):
        p = 1 + a1 * x + a2 * x**2 + a3 * x**3
        h0 = x**2 * c - b**2
        F = p * b + x**2 * h0**2
        g = 1 - 2 * a1 * x
        numerator = expand(h0 + g * F**2)
        S, remainder = sp.div(numerator, x**2, x)
        self.assertEqual(remainder, 0)
        L = (2 * x**4 * h0, -p + 4 * x**2 * b * h0)
        self.assertEqual(apply_bc(L, F), 0)
        self.assertEqual(apply_bc(L, S), -p)
        self.assertEqual(expand(S.subs(x, 0)),
                         expand(c + (2 * a2 - 3 * a1**2) * b**2 + 2 * b**5))
        # At a nonzero ordinary fiber, the displayed inverse is polynomial.
        alpha = sp.Integer(2)
        palpha = 1 - alpha
        galpha = 1 + 2 * alpha
        recovered_h = alpha**2 * ss - galpha * ff**2
        recovered_b = (ff - alpha**2 * recovered_h**2) / palpha
        recovered_c = (recovered_h + recovered_b**2) / alpha**2
        h_check = sp.factor(alpha**2 * recovered_c - recovered_b**2)
        F_check = sp.factor(palpha * recovered_b + alpha**2 * h_check**2)
        S_check = sp.factor((h_check + galpha * F_check**2) / alpha**2)
        self.assertEqual(F_check, ff)
        self.assertEqual(S_check, ss)
        # Root residue parity works also when the chosen p has a double root.
        for galpha in (sp.Integer(3), sp.Integer(5)):
            Froot = h**2
            Sroot = h + galpha * h**4
            functions = [expand(Froot**j) for j in range(5)]
            functions += [expand(Froot**j * Sroot) for j in range(5)]
            degree = max(sp.degree(value, h) for value in functions)
            matrix = sp.Matrix([[value.coeff(h, power) for value in functions]
                                for power in range(degree + 1)])
            self.assertEqual(matrix.rank(), 10)

    def test_constant_p_has_a_genuine_two_sided_relative_coordinate_inverse(self):
        h0 = x**2 * c - b**2
        F = b + x**2 * h0**2
        S = sp.cancel((h0 + F**2) / x**2)
        sp.Poly(S, x, b, c)
        reconstructed_h = x**2 * ss - ff**2
        reconstructed_b = ff - x**2 * reconstructed_h**2
        reconstructed_c = ss - reconstructed_h**2 * (ff + reconstructed_b)
        actual_h = sp.factor(x**2 * reconstructed_c - reconstructed_b**2)
        actual_F = sp.factor(reconstructed_b + x**2 * actual_h**2)
        actual_S = sp.factor((actual_h + actual_F**2) / x**2)
        self.assertEqual(actual_h, reconstructed_h)
        self.assertEqual(actual_F, ff)
        self.assertEqual(actual_S, ss)
        back_h = sp.factor(x**2 * S - F**2)
        back_b = sp.factor(F - x**2 * back_h**2)
        back_c = sp.factor(S - back_h**2 * (F + back_b))
        self.assertEqual(back_h, h0)
        self.assertEqual(back_b, b)
        self.assertEqual(back_c, c)
        L = (2 * x**4 * h0, -1 + 4 * x**2 * b * h0)
        self.assertEqual(apply_bc(L, S), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
