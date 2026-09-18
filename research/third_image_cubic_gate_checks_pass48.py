"""Exact finite cubic identities, not tests of the universal flatness/topology proof."""

import unittest

import sympy as sp


class ThirdImageCubicGateChecks(unittest.TestCase):
    def test_general_cubic_relations_and_derivatives(self):
        a, b, c, d, e, f, eps, q, h, z, w, t = sp.symbols(
            "a b c d e f eps q h z w t"
        )
        r = a * z + b * w
        b1, b2 = a * c + b * d, a * e + b * f
        p, bigq = a * b1 + b * b2, a * q + b * h
        dz, dw = eps * b * r + b1, -eps * a * r + b2
        dt = (
            eps * bigq
            + eps * (a * (e + 2 * d) + 3 * b * f) * z
            + eps * (-3 * a * c - b * (d + 2 * e)) * w
            + 2 * (c * f - d * e)
        )

        def deriv(value):
            value = sp.sympify(value)
            return sp.expand(
                sp.diff(value, z) * dz + sp.diff(value, w) * dw
                + sp.diff(value, t) * dt
            )

        conic = eps * r**2 - 2 * b2 * z + 2 * b1 * w - bigq
        g = eps * r * z - 2 * e * z + 2 * c * w - q
        hh = eps * r * w - 2 * f * z + 2 * d * w - h
        self.assertEqual(sp.expand(a * g + b * hh - conic), 0)
        self.assertEqual(deriv(conic), 0)
        self.assertEqual(deriv(r), sp.expand(p))
        self.assertEqual(deriv(deriv(deriv(g))), sp.expand(3 * eps**2 * b * p**2))
        self.assertEqual(deriv(deriv(deriv(hh))), sp.expand(-3 * eps**2 * a * p**2))
        self.assertEqual(deriv(deriv(deriv(t))), sp.expand(3 * eps**2 * p**2))
        self.assertEqual(deriv(deriv(deriv(deriv(t)))), 0)
        self.assertEqual(sp.expand(deriv(b * t - g) + eps * b * conic), 0)
        self.assertEqual(sp.expand(deriv(a * t + hh) + eps * a * conic), 0)
        self.assertEqual(dt.subs({a: 0, b: 0}), 2 * c * f - 2 * d * e)

    def test_unit_determinant_closed_equations_and_generic_elimination(self):
        a, b, z, w, t = sp.symbols("a b z w t")
        r = a * z + b * w
        bigq = a + 3 * b
        # Formal coefficient control: c=f=1, d=e=0, q=1, h=3.
        # It is not asserted to satisfy the actual divisor-cover hypotheses.
        conic = r**2 - 2 * b * z + 2 * a * w - bigq
        g, hh = r * z + 2 * w - 1, r * w - 2 * z - 3
        first, second = b * t - g, a * t + hh
        self.assertEqual(sp.expand(a * first - b * second + conic), 0)
        self.assertEqual(sp.cancel(second.subs(t, g / b) - conic / b), 0)
        self.assertEqual(sp.cancel(first.subs(t, -hh / a) + conic / a), 0)
        closed = [value.subs({a: 0, b: 0}) for value in (first, second)]
        groebner = sp.groebner(closed, z, w, t, domain=sp.QQ)
        self.assertEqual(groebner.reduce(z + sp.Rational(3, 2))[1], 0)
        self.assertEqual(groebner.reduce(w - sp.Rational(1, 2))[1], 0)
        self.assertEqual(groebner.reduce(t)[1], t)
        closed_matrix = sp.Matrix([[sp.diff(value, x) for x in (z, w)] for value in closed])
        self.assertEqual(closed_matrix.det(), -4)

    def test_rank_defects_and_missing_coefficient_premise(self):
        a, b, z, w, t = sp.symbols("a b z w t")
        r = a * z + b * w
        # Rank one leaves a plane in the cubic candidate's closed fiber.
        rank_one = [b * t - (r * z + 2 * w), a * t + r * w]
        reduced_one = [value.subs({a: 0, b: 0}) for value in rank_one]
        self.assertEqual(reduced_one, [-2 * w, 0])
        gb_one = sp.groebner(reduced_one, z, w, t)
        self.assertEqual(gb_one.reduce(z)[1], z)
        self.assertEqual(gb_one.reduce(t)[1], t)

        # c=a, f=b, d=e=0 has p=a^3+b^3 nonzero, but zero residue matrix.
        rank_zero = [b * t - (r * z + 2 * a * w), a * t + r * w - 2 * b * z]
        self.assertEqual([value.subs({a: 0, b: 0}) for value in rank_zero], [0, 0])
        self.assertNotEqual(sp.expand(a**3 + b**3), 0)

        # The prior weak control has B1=1, so the conic is not in (a,b)S.
        # It cannot enter the regular-sequence construction merely from flatness.
        weak_conic = r**2 + 2 * w - b
        self.assertEqual(weak_conic.subs({a: 0, b: 0}), 2 * w)
        self.assertNotEqual(weak_conic.subs({a: 0, b: 0}), 0)


if __name__ == "__main__":
    unittest.main()
