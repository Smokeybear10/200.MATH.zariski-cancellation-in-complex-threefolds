"""Finite exact controls for the intrinsic Catalan family in pass104.

One unittest method checks m=1,...,5.  These symbolic instances do not
prove the all-m polynomial-divisibility, saturation, or presentation
theorems.  The family is intrinsic A=C[x,y,c], not an original E-frame.
No previous checker or solver is imported.
"""

from math import comb
import unittest

import sympy as sp


class CatalanHiddenParameterChecks(unittest.TestCase):
    def test_finite_catalan_recovery_and_residues(self):
        x, y, c, t = sp.symbols("x y c t")

        def catalan(j):
            return comb(2 * j, j) // (j + 1)

        def zero(value):
            self.assertEqual(sp.expand(value), 0)

        for m in range(1, 6):
            with self.subTest(m=m):
                p = sp.Add(*[
                    (-1) ** j * catalan(j) * x ** j * t ** (j + 1)
                    for j in range(m)
                ])
                residual, remainder = sp.div(t - p - x * p ** 2, x ** m, x)
                zero(remainder)
                zero(residual.subs(t, 0))
                zero(residual.subs(x, 0) - (-1) ** m * catalan(m) * t ** (m + 1))

                f = y ** 2 + x * y ** 4 + x ** m * c
                p_actual = sp.expand(p.subs(t, f))
                u, remainder = sp.div(y ** 2 - p_actual, x ** m, x)
                zero(remainder)
                self.assertTrue(sp.Poly(u, x, y, c).is_multivariate)
                r_actual = sp.expand(residual.subs(t, f))

                def n(value):
                    return sp.expand(
                        -x ** m * sp.diff(value, y)
                        + (2 * y + 4 * x * y ** 3) * sp.diff(value, c)
                    )

                zero(n(x))
                zero(n(f))
                self.assertEqual(sp.gcd(x ** m, 2 * y + 4 * x * y ** 3), 1)
                zero(n(u) + 2 * y)
                zero(n(n(u)) - 2 * x ** m)
                zero(n(n(n(u))))

                c2 = n(n(c))
                c3 = n(c2)
                c4 = n(c3)
                zero(c2 + 2 * x ** m + 12 * x ** (m + 1) * y ** 2)
                zero(c3 - 24 * x ** (2 * m + 1) * y)
                zero(c4 + 24 * x ** (3 * m + 1))
                self.assertNotEqual(c4, 0)
                zero(n(c4))

                # Exact polynomial recovery and the relative conic relation.
                zero(c - (r_actual - (1 + 2 * x * p_actual) * u
                          - x ** (m + 1) * u ** 2))
                zero(y ** 2 - x ** m * u - p_actual)
                zero(2 * n(n(u)) * u - n(u) ** 2 + 4 * p_actual)

                u_at_x0 = sp.expand(u.subs(x, 0))
                zero(u_at_x0 + c - (-1) ** m * catalan(m) * y ** (2 * m + 2))
                whole_fiber_u = sp.rem(u_at_x0, y ** 2, y)
                zero(whole_fiber_u + c)
                whole_fiber_nu = sp.rem(n(u).subs(x, 0), y ** 2, y)
                zero(whole_fiber_nu + 2 * y)
                self.assertNotEqual(whole_fiber_nu, 0)
                zero(sp.rem(whole_fiber_nu ** 2, y ** 2, y))

                jacobian = sp.Matrix([x, y, u]).jacobian([x, y, c]).det()
                zero(jacobian + sp.diff(p, t).subs(t, f))
                if m == 1:
                    zero(jacobian + 1)
                    zero(u + c + y ** 4)
                    self.assertEqual(sp.total_degree(n(y), x, y), 1)
                else:
                    self.assertGreater(sp.Poly(jacobian, x, y, c).total_degree(), 0)
                    self.assertGreaterEqual(sp.total_degree(n(y), x, y), 2)

                # A finite sample of the module formula, not its saturation proof.
                sample = f ** 2 + x + (1 + x * f) * y + (f + x ** 2) * u
                zero(n(n(n(sample))))

                # Independent coefficient-matrix check of three finite parity rows.
                columns = [y ** (2 * j) for j in range(3)]
                columns += [y ** (2 * j + 1) for j in range(3)]
                columns += [sp.expand(u_at_x0 * y ** (2 * j)) for j in range(3)]
                polynomials = [sp.Poly(value, y, c) for value in columns]
                monomials = sorted(set().union(*(p0.monoms() for p0 in polynomials)))
                matrix = sp.Matrix([
                    [p0.coeff_monomial(mon) for p0 in polynomials]
                    for mon in monomials
                ])
                self.assertEqual(matrix.rank(), 9)


if __name__ == "__main__":
    unittest.main(verbosity=2)

