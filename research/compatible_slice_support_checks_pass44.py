"""Finite exact controls for the faithfully flat compatibility-cokernel lemma.

The written proof, not these examples, establishes flat contraction,
prime avoidance, principal annihilators, and all height-one quantifiers.
"""

import unittest

import sympy as sp


x, y, t, s, u, v = sp.symbols("x y t s u v")


class CompatibleSliceSupportChecks(unittest.TestCase):
    def test_coprime_noncomaximal_subtraction(self):
        p, q = x**2, y**3 + x
        self.assertEqual(sp.gcd(p, q), 1)
        base_ideal = sp.groebner([p, q], x, y)
        self.assertEqual(base_ideal.reduce(sp.Integer(1))[1], 1)
        primitive = t**3 + x*y*t
        alpha, beta = x*y + y**2, x**3 - y
        a, b = p*primitive + alpha, q*primitive + beta
        D = lambda f: sp.expand(x*sp.diff(f, t))
        f = D(primitive)
        self.assertEqual(sp.expand(D(a) - p*f), 0)
        self.assertEqual(sp.expand(D(b) - q*f), 0)
        c = sp.expand(q*a - p*b)
        self.assertEqual(D(c), 0)
        self.assertEqual(sp.expand(c - (q*alpha - p*beta)), 0)
        recovered = sp.cancel((a - alpha)/p)
        self.assertEqual(sp.expand(recovered - primitive), 0)
        self.assertEqual(sp.expand((b - beta) - q*recovered), 0)
        self.assertEqual(sp.expand(D(recovered) - f), 0)

    def test_repeated_divisor_annihilator_and_coprimality_boundary(self):
        # For D=x**e d/dt, its image is precisely x**e R[t].
        # A polynomial lies in that image exactly when division by x**e
        # leaves a polynomial, since termwise integration is available.
        for exponent in range(1, 5):
            for order in range(exponent + 1):
                with self.subTest(exponent=exponent, order=order):
                    f = x**order*(1 + y*t) + x**(order + 1)*t**2
                    annihilator = x**max(exponent-order, 0)
                    integral = sp.integrate(
                        sp.cancel(annihilator*f/x**exponent), t
                    )
                    self.assertTrue(integral.is_polynomial(x, y, t))
                    self.assertEqual(
                        sp.expand(x**exponent*sp.diff(integral, t)
                                  - annihilator*f), 0
                    )
                    if order < exponent:
                        insufficient = sp.cancel(
                            annihilator*f/x**(exponent + 1)
                        )
                        self.assertFalse(insufficient.is_polynomial(x, y, t))
                    test_multiplier = (x+y)*(1+y**2)
                    coeff_gcd = sp.gcd_list(
                        sp.Poly(sp.expand(test_multiplier*f), t).all_coeffs()
                    )
                    actual_required = sp.cancel(
                        x**exponent/sp.gcd(x**exponent, coeff_gcd)
                    )
                    self.assertEqual(sp.expand(actual_required-annihilator), 0)
        # Noncoprime annihilators do not imply zero: [1] modulo x R[t].
        self.assertEqual(sp.gcd(x, x*y), x)
        self.assertEqual(x*sp.diff(t, t), x)
        self.assertEqual(x*sp.diff(y*t, t), x*y)
        self.assertFalse((1/x).is_polynomial(x, y, t))

    def test_actual_localized_compatible_slice(self):
        E = lambda f: sp.diff(f, s)
        U = lambda f: x*sp.diff(f, t) + y*sp.diff(f, s)
        for coordinate in (x, y, t, s):
            self.assertEqual(sp.expand(E(U(coordinate))-U(E(coordinate))), 0)
        local_slice = s-y*t/x
        self.assertEqual(E(local_slice), 1)
        self.assertEqual(sp.cancel(U(local_slice)), 0)
        self.assertFalse(local_slice.is_polynomial(x, y, t, s))
        self.assertEqual(U(s), y)
        # D(f) is divisible by x for every polynomial f, but -y is not.
        self.assertNotEqual((-y).subs(x, 0), 0)
        self.assertEqual(sp.cancel(x*sp.diff(y*t, t)), x*y)
        # The obstruction survives on the divisor x=0, rather than only
        # at the intersection of the two coprime curves x=0 and y=0.
        self.assertEqual(sp.gcd(x, y), 1)
        self.assertNotEqual(sp.rem(y, x, x), 0)

    def test_nonfaithful_sl2_contraction_countercontrol(self):
        relation = x*v-y*u-1
        D = lambda f: sp.expand(x*sp.diff(f, u)+y*sp.diff(f, v))
        self.assertEqual(D(relation), 0)
        self.assertEqual(D(u), x)
        self.assertEqual(D(v), y)
        quotient_ideal = sp.groebner([relation, x, y], x, y, u, v)
        self.assertEqual(quotient_ideal.reduce(sp.Integer(1))[1], 0)
        base_ideal = sp.groebner([x, y], x, y)
        self.assertEqual(base_ideal.reduce(sp.Integer(1))[1], 1)
        self.assertEqual(sp.gcd(x, y), 1)
        solved_v = (1+y*u)/x
        self.assertEqual(sp.cancel(relation.subs(v, solved_v)), 0)
        self.assertEqual(sp.cancel(D(u/x)), 1)
        # At x=0 the exact relation makes y invertible, explaining why
        # the map to the invariant plane cannot be faithfully flat.
        self.assertEqual(sp.expand(relation.subs(x, 0)), -y*u-1)
        self.assertEqual(sp.expand(y*(-u) - 1 - relation.subs(x, 0)), 0)


if __name__ == "__main__":
    unittest.main()
