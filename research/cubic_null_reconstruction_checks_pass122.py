"""One conditional row/absorption check for the null reconstruction122.

All scalar speed-relation residuals are retained in the certificates.
The test does not prove global invariant-kernel contraction, the
finite-place residue lemma, or an original-coordinate contradiction.
"""

import unittest

import sympy as sp


class NullReconstructionChecks(unittest.TestCase):
    def test_original_coordinate_row_and_polynomial_absorption(self):
        h, Y, P, g = sp.symbols("h Y P g")
        x1, x2, x3, u = sp.symbols("x1 x2 x3 u")
        a3 = sp.Symbol("a3", nonzero=True)
        a2, a1, a0 = sp.symbols("a2 a1 a0")
        D = a3*h**3+a2*h**2+a1*h+a0

        def zero(value):
            entries = value if isinstance(value, sp.MatrixBase) else [value]
            for entry in entries:
                self.assertEqual(sp.cancel(entry), 0)

        speed = sp.Matrix([-(1+D*Y**2)/(2*Y), h*Y, Y])
        relative_v = (x2-h*x3)/Y
        twice_R = (2*Y**2*x1+sp.diff(D, h)*Y**2*x2
                   +(1+(D-h*sp.diff(D, h))*Y**2)*x3)
        relative_R = twice_R/2
        orbit_coefficient = (x3-relative_R)/Y
        reconstructed = (speed*orbit_coefficient+speed.diff(h)*relative_v
                         +speed.diff(Y)*relative_R)
        zero(reconstructed-sp.Matrix([x1, x2, x3]))
        zero(Y**2*relative_v-(Y*x2-h*Y*x3))

        # A polynomial residual, not an imposed zero substitution.
        F = 2*g*Y**2+a3*P**3+a2*P**2*Y+a1*P*Y**2+a0*Y**3+Y
        polynomial_row = (2*Y**2*x1+(3*a3*P**2+2*a2*P*Y+a1*Y**2)*x2
                          +(3+4*g*Y+a2*P**2+2*a1*P*Y+3*a0*Y**2)*x3)
        zero(Y*(twice_R.subs(h, P/Y)-polynomial_row)+2*F*x3)
        zero(polynomial_row.subs({P: 0, Y: 0})-3*x3)
        E_row = sum(sp.diff(polynomial_row, x)*b
                    for x, b in zip((x1, x2, x3), (g, P, Y)))
        zero(E_row-3*F)
        invariant_U = Y*x2-P*x3
        zero(sum(sp.diff(invariant_U, x)*b
                 for x, b in zip((x1, x2, x3), (g, P, Y))))

        K0 = (-1-2*g*Y-a2*P**2-a1*P*Y-a0*Y**2)/a3
        zero(a3*(P**3-Y*K0)-F)
        zero(K0.subs({P: 0, Y: 0})+1/a3)
        a, B0, R = sp.symbols("a B0 R")
        rho = a*Y+B0/Y
        third_coordinate = Y*(u+rho)+R
        zero(third_coordinate-Y*u-R-B0-a*Y**2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
