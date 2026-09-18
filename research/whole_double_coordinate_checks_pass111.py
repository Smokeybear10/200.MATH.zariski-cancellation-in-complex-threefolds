"""Finite intrinsic whole-double coordinate controls, not original E-frames.

One method checks e=1..4. The all-e kernel/flatness and actual divisor
noncollapse failure are written proofs, not conclusions of these samples.
"""

import unittest

import sympy as sp


class WholeDoubleCoordinateChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_coordinate_degree_and_residue_controls(self):
        x, y, t, X, G0, c0, eps, C = sp.symbols("x y t X G0 c0 eps C")
        G, c = y+x*t, t+(y+x*t)**2
        inverse = {x: X, y: G0-X*(c0-G0**2), t: c0-G0**2}
        forward = {X: x, G0: G, c0: c}
        for expression, target in ((x, X), (G, G0), (c, c0)):
            self.assert_zero(expression.subs(inverse, simultaneous=True)-target)
        for expression, target in ((X, x), (inverse[y], y), (inverse[t], t)):
            self.assert_zero(expression.subs(forward, simultaneous=True)-target)
        self.assert_zero(sp.Matrix([x, G, c]).jacobian([x, y, t]).det()-1)
        self.assert_zero((G-y)/x-t)
        self.assert_zero(sp.rem(sp.expand(G**2-y**2), x, x))

        artin = sp.groebner([eps**2], eps, C)
        residues = [sp.Integer(1), eps, C]
        monomials = [sp.Integer(1), eps, C]
        residue_matrix = sp.Matrix([
            [sp.Poly(artin.reduce(f)[1], eps, C).coeff_monomial(m)
             for f in residues] for m in monomials
        ])
        self.assertEqual(residue_matrix.det(), 1)
        self.assert_zero(artin.reduce(eps**2)[1])

        for e in range(1, 5):
            with self.subTest(e=e):
                f = y**2+x**e*t

                def deriv(expression):
                    return sp.expand(-x**e*sp.diff(expression, y)
                                     + 2*y*sp.diff(expression, t))

                def iterate(expression, n):
                    for _ in range(n):
                        expression = deriv(expression)
                    return expression

                self.assert_zero(deriv(f))
                self.assert_zero(deriv(G)+x**e-2*x*y)
                self.assert_zero(iterate(G, 2)+2*x**(e+1))
                self.assert_zero(iterate(G, 3))
                self.assert_zero(iterate(c, 4)-24*x**(2*e+2))
                self.assertNotEqual(iterate(c, 4), 0)
                self.assert_zero(iterate(c, 5))
                self.assert_zero(iterate(t, 3))
                self.assert_zero(deriv(t)-2*y)
                self.assertEqual(sp.gcd(x**e, 2*y), 1)
                whole = sp.groebner([x, f], x, y, t)
                expected = sp.groebner([x, G**2], x, y, t)
                for relation in (x, G**2):
                    self.assert_zero(whole.reduce(sp.expand(relation))[1])
                for relation in (x, f):
                    self.assert_zero(expected.reduce(sp.expand(relation))[1])
                self.assert_zero(whole.reduce(c)[1]-t)
                self.assert_zero(whole.reduce(deriv(c))[1]-2*y)
                self.assert_zero(whole.reduce(deriv(G))[1])
                self.assert_zero(f.subs(x, 0)-y**2)
                self.assert_zero(G.subs(x, 0)-y)
                normal_square = sp.groebner([x**2, x*y, y**2], x, y, t)
                normal_image = normal_square.reduce(deriv(y))[1]
                self.assertEqual(normal_image, -x if e == 1 else 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
