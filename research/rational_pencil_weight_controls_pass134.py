"""Finite exact rational-pencil controls for the algebra lemma134.

Both numerator and denominator may be nonconstant invariants. Coefficients
in C(T) have weight zero, and selected components after algebraic extension
are kept separate from a generator over exactly C(T). The written Gauss and
localization proof, not these finite tests, establishes the universal kernel
statement. No polynomial Luroth generator or previous solver is imported.
"""

import unittest

import sympy as s


def weight(expr, variables, weights, parameter):
    polynomial = s.Poly(expr, *variables, domain=s.QQ.frac_field(parameter))
    return max(sum(e*w for e, w in zip(monomial, weights)) for monomial in polynomial.monoms())


class RationalPencilWeightControls(unittest.TestCase):
    def test_nonconstant_numerator_denominator_and_base_locus(self):
        x, y, z, u, T = s.symbols("x y z u T")
        variables, weights = (x, y, z, u), (3, 2, 1, 1)
        p, q = x, y
        F = p-T*q
        self.assertEqual(s.gcd(p, q), 1)
        self.assertEqual(s.diff(p, u), 0)
        self.assertEqual(s.diff(q, u), 0)
        self.assertEqual(s.cancel(F.subs(T, p/q)), 0)
        self.assertEqual(s.Poly(F, T).primitive()[0], 1)
        self.assertEqual(weight(p, variables, weights, T), 3)
        self.assertEqual(weight(q, variables, weights, T), 2)
        self.assertEqual(weight(F, variables, weights, T), 3)
        coefficient_unit = (T**2+1)/(T-1)
        self.assertEqual(weight(coefficient_unit*F, variables, weights, T), 3)
        self.assertEqual(s.cancel((coefficient_unit*F)/coefficient_unit-F), 0)

        # The generic line retains the pencil's base point x=y=0.
        # Dividing by q first does not license adding an equation y=0.
        self.assertEqual(F.subs({x: 0, y: 0}), 0)
        self.assertEqual(s.gcd(F, q), 1)
        self.assertEqual(s.expand(F.subs(x, T*y)), 0)
        self.assertEqual(q.subs(x, T*y), y)
        for quotient, remainder in ((x+z, 0), (x*y+T, y*z+T*u),
                                    (z**2+T*x, y**2+u), (T**2+y, y)):
            candidate = s.expand(F*quotient+remainder)
            actual_quotient, actual_remainder = s.div(candidate, F, x)
            with self.subTest(remainder=str(remainder)):
                self.assertEqual(s.expand(actual_remainder-remainder), 0)
                self.assertEqual(s.expand(actual_quotient-quotient), 0)
                self.assertEqual(s.expand(candidate.subs(x, T*y)-remainder), 0)
                # A finite saturation check: multiplying by q preserves
                # the zero/nonzero remainder because the quotient is a domain.
                _, multiplied_remainder = s.div(y*candidate, F, x)
                self.assertEqual(s.expand(multiplied_remainder-y*remainder), 0)

    def test_selected_component_after_extension_does_not_bound_old_pencil(self):
        x, y, z, u, T, lam = s.symbols("x y z u T lam")
        p, q = x**2, y**2
        F = p-T*q
        component = x-lam*y
        self.assertEqual(s.gcd(p, q), 1)
        self.assertEqual(s.cancel(F.subs(T, p/q)), 0)
        self.assertEqual(s.cancel(component.subs(lam, x/y)), 0)
        self.assertEqual(s.expand(F.subs(T, lam**2)-component*(x+lam*y)), 0)
        self.assertEqual(s.resultant(lam**2-T, component, lam), F)
        self.assertEqual(s.diff(p/q, u), 0)
        self.assertEqual(s.diff(x/y, u), 0)
        ordinary = (1, 1, 1, 1)
        self.assertEqual(weight(F, (x, y, z, u), ordinary, T), 2)
        self.assertEqual(weight(p, (x, y, z, u), ordinary, T), 2)
        self.assertEqual(weight(q, (x, y, z, u), ordinary, T), 2)
        self.assertEqual(weight(component, (x, y, z, u), ordinary, lam), 1)


if __name__ == "__main__":
    unittest.main()
