"""Exact quartic-presentation controls for pass52.

The saturation examples are coefficient models, not constructions
of actual unresolved-cylinder obstruction points. The universal
complete-intersection and generation conclusions remain proofs.
"""

import unittest
import sympy as sp


class QuarticFiberGateChecks(unittest.TestCase):
    def test_generic_eliminations_recover_the_complete_conic(self):
        a, b, aa, ab, bb = sp.symbols("a b Qaa Qab Qbb")
        u, v = sp.symbols("U V")
        relations = (b*v-aa, a*v+b*u+ab, a*u-bb)
        conic = a**2*aa+a*b*ab+b**2*bb

        a_chart = {u: bb/a, v: -(b*bb+a*ab)/a**2}
        values = [sp.cancel(expr.subs(a_chart, simultaneous=True))
                  for expr in relations]
        self.assertEqual(values[1:], [0, 0])
        self.assertEqual(sp.cancel(values[0]+conic/a**2), 0)

        b_chart = {v: aa/b, u: -(a*aa+b*ab)/b**2}
        values = [sp.cancel(expr.subs(b_chart, simultaneous=True))
                  for expr in relations]
        self.assertEqual(values[:2], [0, 0])
        self.assertEqual(sp.cancel(values[2]+conic/b**2), 0)

        z, w, epsilon = sp.symbols("Z W epsilon")
        c, d, e, f, g, h, q1, q2, q3 = sp.symbols(
            "c d e f g h q1 q2 q3")
        qaa = epsilon*z**2-2*f*z+2*c*w-q1
        qab = 2*epsilon*z*w-2*g*z+2*d*w-q2
        qbb = epsilon*w**2-2*h*z+2*e*w-q3
        b1 = a**2*c+a*b*d+b**2*e
        b2 = a**2*f+a*b*g+b**2*h
        q = a**2*q1+a*b*q2+b**2*q3
        self.assertEqual(sp.expand(
            a**2*qaa+a*b*qab+b**2*qbb
            -(epsilon*(a*z+b*w)**2-2*b2*z+2*b1*w-q)), 0)

    def test_independent_saturations_and_full_scheme_fibers(self):
        a, b, z, w, u, v, aux = sp.symbols("a b Z W U V aux")
        variables = (a, b, u, v, z, w)

        def saturated(generators, denominator):
            basis = sp.groebner(
                list(generators)+[1-aux*denominator],
                aux, *variables, domain=sp.QQ, order="lex")
            return [p.as_expr() for p in basis.polys
                    if not p.as_expr().has(aux)]

        def same_ideal(first, second):
            one = sp.groebner(first, *variables, domain=sp.QQ)
            two = sp.groebner(second, *variables, domain=sp.QQ)
            self.assertTrue(all(one.reduce(expr)[1] == 0
                                for expr in second))
            self.assertTrue(all(two.reduce(expr)[1] == 0
                                for expr in first))

        # B1=a^(n+1), B2=b^(n+1), epsilon=1, Q=0.
        # These are bounded formal conic data, not full-frame models.
        for n in (1, 2):
            qaa = z**2+2*a**(n-1)*w
            qab = 2*z*w
            qbb = w**2-2*b**(n-1)*z
            relations = [b*v-qaa, a*v+b*u+qab, a*u-qbb]
            same_ideal(saturated(relations, a), relations)
            same_ideal(saturated(relations, b), relations)

            residuals = [sp.expand(expr.subs({a: 0, b: 0}))
                         for expr in relations]
            self.assertFalse(any(expr.has(u, v) for expr in residuals))
            fiber = sp.groebner(residuals, z, w, domain=sp.QQ)
            if n == 1:
                self.assertEqual(
                    [p.as_expr() for p in fiber.polys], [z, w])
            else:
                self.assertEqual(
                    [p.as_expr() for p in fiber.polys], [z**2, z*w, w**2])
                self.assertNotEqual(fiber.reduce(z)[1], 0)
                self.assertNotEqual(fiber.reduce(w)[1], 0)
                for expr in (z**2, z*w, w**2):
                    self.assertEqual(fiber.reduce(expr)[1], 0)
                # The nilpotents survive in the length-three coefficient
                # algebra; U,V are entirely free on this closed fiber.


if __name__ == "__main__":
    unittest.main()

