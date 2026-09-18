"""Finite exact intrinsic controls for the mixed quartic family in pass105.

One method tests m=1,...,5.  Successive monic polynomial division builds
the truncated cubic independently of the proof's alpha recurrence.
These instances do not verify the all-m saturation or flatness proof,
and no original four-coordinate E-frame is asserted.
"""

from math import comb
import unittest

import sympy as sp


class MixedQuarticCubicChecks(unittest.TestCase):
    def test_mixed_quartic_cubic_preparation_controls(self):
        x, y, c, t, w = sp.symbols("x y c t w")
        h = y ** 3 - y ** 2
        initial = h - t
        quartic = initial + x * y ** 4

        def zero(value):
            self.assertEqual(sp.expand(value), 0)

        def trunc(value, power):
            return sp.rem(sp.expand(value), x ** power, x)

        # Coefficientwise Euclidean preparation, not the alpha fixed-point rule.
        prepared = initial
        unit_factor = sp.S.One
        for order in range(1, 6):
            error = sp.expand(quartic - unit_factor * prepared).coeff(x, order)
            quotient, remainder = sp.div(error, initial, y)
            self.assertLessEqual(sp.degree(remainder, y), 2)
            unit_factor = sp.expand(unit_factor + x ** order * quotient)
            prepared = sp.expand(prepared + x ** order * remainder)
            zero(trunc(quartic - unit_factor * prepared, order + 1))

        for m in range(1, 6):
            with self.subTest(m=m):
                gm = trunc(prepared, m)
                alpha = sp.expand(gm).coeff(y, 2)
                beta = sp.expand(gm).coeff(y, 1)
                gamma = sp.expand(gm).coeff(y, 0)
                q0 = 1 - x * alpha
                self.assertEqual(sp.Poly(gm, y).LC(), 1)
                self.assertEqual(sp.degree(gm, y), 3)

                # Compare independent division output with the formal equations.
                zero(trunc((alpha + 1 - x * alpha ** 2) * q0 ** 2
                           + x ** 2 * t, m))
                zero(trunc(beta * q0 ** 2 - x * t, m))
                zero(trunc(gamma * q0 + t, m))
                quotient, remainder = sp.div(quartic, gm, y)
                zero(quotient - (x * y + q0))
                correction, rem_x = sp.div(remainder, x ** m, x)
                zero(rem_x)
                self.assertLessEqual(sp.degree(correction, y), 2)
                zero(quotient.subs(x, 0) - 1)

                f = h + x * y ** 4 + x ** m * c
                u, rem_x = sp.div(sp.expand(gm.subs(t, f)), x ** m, x)
                zero(rem_x)
                sp.Poly(u, x, y, c)  # The lift is a polynomial, not a rational repair.

                def n(value):
                    return sp.expand(
                        -x ** m * sp.diff(value, y)
                        + (3 * y ** 2 - 2 * y + 4 * x * y ** 3)
                        * sp.diff(value, c)
                    )

                zero(n(x))
                zero(n(f))
                self.assertEqual(
                    sp.gcd(x ** m, 3 * y ** 2 - 2 * y + 4 * x * y ** 3), 1
                )
                nu = n(u)
                n2u = n(nu)
                n3u = n(n2u)
                zero(nu + 3 * y ** 2 + 2 * alpha.subs(t, f) * y
                     + beta.subs(t, f))
                zero(n2u - x ** m * (6 * y + 2 * alpha.subs(t, f)))
                zero(n3u + 6 * x ** (2 * m))
                self.assertNotEqual(n3u, 0)
                zero(n(n3u))
                c2 = n(n(c))
                c3 = n(c2)
                c4 = n(c3)
                zero(c2 + x ** m * (6 * y - 2 + 12 * x * y ** 2))
                zero(c3 - x ** (2 * m) * (6 + 24 * x * y))
                zero(c4 + 24 * x ** (3 * m + 1))
                self.assertNotEqual(c4, 0)
                zero(n(c4))

                # Exact recovery and the reverse identity modulo the cubic relation.
                recovered_c = -quotient.subs(t, f) * u - correction.subs(t, f)
                zero(recovered_c - c)
                zero(gm.subs(t, f) - x ** m * u)
                source_c = -quotient * w - correction
                zero(h + x * y ** 4 + x ** m * source_c - t
                     - quotient * (gm - x ** m * w))

                omitted = sp.expand(prepared).coeff(x, m)
                u_x0 = sp.expand(u.subs(x, 0))
                zero(u_x0 + c + omitted.subs(t, h))
                catalan_m = comb(2 * m, m) // (m + 1)
                zero(omitted.subs(t, 0) - (-1) ** (m + 1) * catalan_m * y ** 2)
                whole_u = sp.rem(u_x0, h, y)
                zero(whole_u + c - (-1) ** m * catalan_m * y ** 2)
                zero(sp.rem(whole_u, y ** 2, y) + c)
                zero(whole_u.subs(y, 1) + c - (-1) ** m * catalan_m)
                zero(sp.diff(whole_u.subs(y, 0), c) + 1)
                zero(sp.diff(whole_u.subs(y, 1), c) + 1)
                whole_nu = sp.rem(nu.subs(x, 0), h, y)
                zero(whole_nu + sp.diff(h, y))
                zero(sp.rem(whole_nu, y ** 2, y) - 2 * y)
                zero(whole_nu.subs(y, 1) + 1)

                if m == 1:
                    zero(u + c + y ** 4)
                if m == 2:
                    zero(u + c - y ** 4 * (y + 1) - x * c * (y + 1))

                # Finite samples only; the full module theorem is proved in the note.
                sample2 = 1 + f + (x + f ** 2) * y + (1 + x * f) * y ** 2
                zero(n(n(n(sample2))))
                sample3 = sample2 + (1 + f) * u
                zero(n(n(n(n(sample3)))))
                columns = [sp.expand(h ** j * y ** i)
                           for i in range(3) for j in range(3)]
                columns += [sp.expand(h ** j * u_x0) for j in range(3)]
                polys = [sp.Poly(value, y, c) for value in columns]
                monomials = sorted(set().union(*(poly.monoms() for poly in polys)))
                matrix = sp.Matrix([
                    [poly.coeff_monomial(mon) for poly in polys]
                    for mon in monomials
                ])
                self.assertEqual(matrix.rank(), 12)


if __name__ == "__main__":
    unittest.main(verbosity=2)

