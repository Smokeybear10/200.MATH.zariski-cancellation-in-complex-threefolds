"""Finite determinant/saturation controls for the pass51 cubic theorem.

These are exact coefficient models, not asserted unresolved-frame
realizations. Universal exactness, source inputs and the actual fiber
dimension remain written proofs.
"""

import unittest
import sympy as sp


class CubicGenerationObstructionChecks(unittest.TestCase):
    def test_universal_syzygies_and_residual_degree(self):
        a, b, aa, ab, ba, bb = sp.symbols("a b A11 A12 A21 A22")
        f, g = a*aa+b*ab, a*ba+b*bb
        delta = aa*bb-ab*ba
        matrix = sp.Matrix([[bb, -ba], [-ab, aa], [-a, -b]])
        self.assertEqual((sp.Matrix([[f, g, delta]])*matrix).applyfunc(sp.expand),
                         sp.zeros(1, 2))
        self.assertEqual(sp.expand(matrix.extract([0, 1], [0, 1]).det()),
                         delta)
        self.assertEqual(sp.expand(
            matrix.extract([0, 2], [0, 1]).det()+g), 0)
        self.assertEqual(sp.expand(
            matrix.extract([1, 2], [0, 1]).det()-f), 0)

        z, w, t, epsilon = sp.symbols("Z W T epsilon")
        ca, cb, da, db, ea, eb, fa, fb, qa, qb, ha, hb = sp.symbols(
            "ca cb da db ea eb fa fb qa qb ha hb")
        entries = (
            -epsilon*z**2+2*ea*z-2*ca*w+qa,
            t-epsilon*z*w+2*eb*z-2*cb*w+qb,
            t+epsilon*z*w-2*fa*z+2*da*w-ha,
            epsilon*w**2-2*fb*z+2*db*w-hb,
        )
        determinant = sp.expand(entries[0]*entries[3]-entries[1]*entries[2])
        poly = sp.Poly(determinant, t)
        self.assertEqual(poly.degree(), 2)
        self.assertEqual(poly.coeff_monomial(t**2), -1)
        self.assertLessEqual(
            sp.Poly(poly.coeff_monomial(t), z, w).total_degree(), 1)
        self.assertLessEqual(
            sp.Poly(poly.coeff_monomial(1), z, w).total_degree(), 3)
        # The quartic cancellation is exact before any specialization.
        self.assertEqual(sp.Poly(determinant, z, w, t).coeff_monomial(
            z**2*w**2), 0)

    def test_exact_formal_saturations_and_scheme_fibers(self):
        a, b, z, w, t, aux = sp.symbols("a b Z W T aux")
        variables = (a, b, t, z, w)

        def saturation_at_a(generators):
            basis = sp.groebner(
                list(generators)+[1-aux*a], aux, *variables,
                order="lex", domain=sp.QQ)
            return [p.as_expr() for p in basis.polys
                    if not p.as_expr().has(aux)]

        def equal_ideals(first, second):
            basis_first = sp.groebner(first, *variables, domain=sp.QQ)
            basis_second = sp.groebner(second, *variables, domain=sp.QQ)
            self.assertTrue(all(basis_first.reduce(p)[1] == 0
                                for p in second))
            self.assertTrue(all(basis_second.reduce(p)[1] == 0
                                for p in first))

        r = a*z+b*w
        # Rank-one coefficient model: c=1, f=a, d=e=q=h=0.
        rank_one = [b*t-r*z-2*w, a*t+r*w-2*a*z]
        equal_ideals(saturation_at_a(rank_one), rank_one)
        self.assertEqual([sp.expand(p.subs({a: 0, b: 0}))
                          for p in rank_one], [-2*w, 0])

        # Rank-zero coefficient models: c=a^n, f=b^n and all
        # four other coefficient choices zero.
        for n in (1, 2):
            first = b*t-r*z-2*a**n*w
            second = a*t+r*w-2*b**n*z
            determinant = (
                -t**2+2*b**(n-1)*z**3-2*a**(n-1)*w**3
                +4*a**(n-1)*b**(n-1)*z*w)
            self.assertEqual(
                sp.expand(a*determinant -
                          ((w**2-2*b**(n-1)*z)*first
                           -(t-z*w)*second)), 0)
            self.assertEqual(
                sp.expand(b*determinant -
                          (-(t+z*w)*first
                           +(-z**2-2*a**(n-1)*w)*second)), 0)
            equal_ideals(saturation_at_a([first, second]),
                         [first, second, determinant])
            self.assertEqual(first.subs({a: 0, b: 0}), 0)
            self.assertEqual(second.subs({a: 0, b: 0}), 0)
            residual = sp.expand(determinant.subs({a: 0, b: 0}))
            self.assertEqual(sp.Poly(residual, t).LC(), -1)
            if n == 1:
                self.assertEqual(residual, -t**2+2*z**3-2*w**3+4*z*w)
            else:
                self.assertEqual(residual, -t**2)
                # The full scheme retains a nonzero nilpotent T.
                self.assertEqual(sp.rem(t**2, residual, t), 0)
                self.assertNotEqual(sp.rem(t, residual, t), 0)


if __name__ == "__main__":
    unittest.main()
