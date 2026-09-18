"""Finite monic-preparation checks, not an actual-frame classification.

One method tests e=1..4 for a perturbation with odd and quartic terms.
The note proves arbitrary Q, every e, flatness and the entire filtration.
"""

import unittest

import sympy as sp


class TriangularWholeDoubleChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_finite_preparation_and_hidden_parameter(self):
        x, y, z, T = sp.symbols("x y z T")
        Q = y**4+y**3+y+1
        P = y**2+x*Q
        for e in range(1, 5):
            with self.subTest(e=e):
                F, V = y**2-T, sp.Integer(1)
                for k in range(1, e):
                    defect = sp.Poly(sp.expand(P-T-V*F), x)
                    for power in range(k):
                        self.assert_zero(defect.coeff_monomial(x**power))
                    Dk = defect.coeff_monomial(x**k)
                    quotient, remainder = sp.div(Dk, y**2-T, y)
                    self.assertLess(sp.degree(remainder, y), 2)
                    F = sp.expand(F+x**k*remainder)
                    V = sp.expand(V+x**k*quotient)
                remainder_numerator = sp.expand(P-T-V*F)
                R, residual = sp.div(remainder_numerator, x**e, x)
                self.assert_zero(residual)
                self.assert_zero(P-T-V*F-x**e*R)
                self.assertEqual(sp.degree(F, y), 2)
                self.assert_zero(sp.Poly(F, y).LC()-1)
                self.assert_zero(F.subs(x, 0)-(y**2-T))
                self.assert_zero(V.subs(x, 0)-1)
                if e >= 2:
                    self.assertNotEqual(sp.expand(V), 1)
                geometric_inverse = sum((1-V)**j for j in range(e))
                self.assert_zero(sp.rem(sp.expand(V*geometric_inverse-1), x**e, x))

                f = P+x**e*z
                Fhat, Vhat, Rhat = [sp.expand(g.subs(T, f)) for g in (F, V, R)]
                U, residual = sp.div(Fhat, x**e, x)
                self.assert_zero(residual)
                self.assert_zero(z+Vhat*U+Rhat)
                alpha = sp.Poly(F, y).coeff_monomial(y)

                def deriv(expression):
                    return sp.expand(-x**e*sp.diff(expression, y)
                                     + sp.diff(P, y)*sp.diff(expression, z))

                self.assert_zero(deriv(f))
                self.assert_zero(deriv(U)+2*y+alpha.subs(T, f))
                self.assert_zero(deriv(deriv(U))-2*x**e)
                self.assert_zero(deriv(deriv(deriv(U))))
                nz = z
                for _ in range(4):
                    nz = deriv(nz)
                self.assert_zero(nz+24*x**(3*e+1))
                self.assertNotEqual(nz, 0)
                self.assert_zero(deriv(nz))
                self.assert_zero(U.subs(x, 0)+z+R.subs({x: 0, T: y**2}, simultaneous=True))
                whole = sp.groebner([x, y**2], x, y, z)
                self.assert_zero(whole.reduce(sp.expand(deriv(U)))[1]+2*y)
                reduced_U = sp.expand(U.subs({x: 0, y: 0}))
                self.assert_zero(sp.diff(reduced_U, z)+1)

                # Finite leading-term controls for the proved all-n formula.
                generic_U = F/x**e
                for n in range(7):
                    j = n//2
                    basis_top = generic_U**j if n % 2 == 0 else y*generic_U**j
                    image = (-x**e)**n*sp.diff(basis_top, y, n)
                    expected = (-1)**n*sp.factorial(n)*x**(e*((n+1)//2))
                    self.assert_zero(image-expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
