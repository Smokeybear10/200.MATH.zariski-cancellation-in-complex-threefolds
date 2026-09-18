"""Finite exact controls for the written all-tower exhaustion lemma.

Only unittest and SymPy are used. These checks do not verify an unknown
ambient realization or replace the universal saturation proof.
"""

import unittest
import sympy as sp


class IsolatedNodeControls(unittest.TestCase):
    def test_nodal_norm_lifts_and_singular_locus(self):
        u, s, d, v, r, a = sp.symbols("u s d v r a")
        f = v**2 - d**2 * (d + 1)
        for b in (sp.Integer(1), s + 2, s**2 - s + 3):
            remainder = sp.rem(s * b**2, s**2 - (d + 1), s)
            even = sp.expand(remainder).coeff(s, 0)
            odd = sp.expand(remainder).coeff(s, 1)
            lift = sp.expand(d**2 * even + d * v * odd)
            physical = lift.subs({d: u**4 - 1, v: (u**4 - 1) * u**2})
            self.assertEqual(sp.expand(physical - ((u**4 - 1) * u * b.subs(s, u**2))**2), 0)
            self.assertTrue(all(sum(powers) >= 2 for powers, _ in sp.Poly(lift, d, v).terms()))
            for k in range(1, 5):
                relation = f**k * a - r**2 + lift
                for variable in (d, v, r, a):
                    self.assertEqual(sp.diff(relation, variable).subs({d: 0, v: 0, r: 0}), 0)
                self.assertEqual(relation.subs({d: 0, v: 0}), -r**2)

    def test_exact_derivative_orders_and_exhaustion_endpoint(self):
        f, r, a, beta, K = sp.symbols("f r a beta K")
        for k in range(1, 6):
            for ell in range(1, k + 1):
                er = f**k * beta
                ea = 2 * r * f**(k - ell) * beta
                relation = f**ell * a - r**2 + K
                derivative = sp.diff(relation, r) * er + sp.diff(relation, a) * ea
                self.assertEqual(sp.expand(derivative), 0)
                self.assertEqual(ea.subs(f, 0), 2 * r * beta if ell == k else 0)
            # The negative exponent when ell > k is a genuine uncancelled pole.
            self.assertEqual(sp.cancel((2 * r * beta / f) * f), 2 * r * beta)

    def test_residual_transcendence_derivative_control(self):
        s, d, r, a = sp.symbols("s d r a")
        relation = r**2 - d**2 * s
        for degree in range(1, 6):
            polynomial = (1 + r) * a**degree + (d + s * r) * a**(degree - 1)
            derivative = sp.rem(2 * r * sp.diff(polynomial, a), relation, r)
            self.assertNotEqual(sp.expand(derivative), 0)
            leading = sp.Poly(derivative, a).LC()
            self.assertEqual(sp.expand(leading - 2 * degree * (r + d**2 * s)), 0)
        # The radicand has odd s-adic order: these finite examples are nonsquares.
        for b in (sp.Integer(1), 1 + s, s**2 * (s + 2)):
            polynomial = sp.Poly(s * b**2, s)
            order = min(monomial[0] for monomial, coefficient in polynomial.terms() if coefficient != 0)
            self.assertEqual(order % 2, 1)

    def test_saturation_requires_residue_injection(self):
        f, r, t = sp.symbols("f r t")
        # A=C[f,r] embeds in B=C[f,t] by r=f*t, and A_f=B_f.
        self.assertEqual(sp.cancel((r / f).subs(r, f * t)), t)
        self.assertEqual((f * t).subs(f, 0), 0)
        # r is nonzero modulo f in the abstract A, but its image dies in B/fB.
        self.assertEqual(sp.rem(r, f, f), r)
        self.assertEqual(sp.rem((f * t), f, f), 0)
        # Hence reducing any polynomial in f,r at f=0 gives no t-dependence.
        for degree in range(1, 6):
            candidate = sum((f + r)**j for j in range(degree + 1))
            self.assertEqual(candidate.subs(r, f * t).subs(f, 0), 1)
        # D=f*d/dt differentiates r to f^2: it is not a minimal local slice.
        self.assertEqual(f * sp.diff(f * t, t), f**2)
        self.assertEqual(f * sp.diff(t, t), f)

    def test_other_factor_is_unit_on_every_tested_thickening(self):
        f, q = sp.symbols("f q")
        kappa = sp.Integer(5)
        beta = kappa + f * q
        for n in range(1, 7):
            inverse = sum((-f * q / kappa)**j for j in range(n)) / kappa
            error = sp.expand(beta * inverse - 1)
            self.assertEqual(sp.rem(error, f**n, f), 0)
            self.assertEqual(sp.expand(error + (-f * q / kappa)**n), 0)


if __name__ == "__main__":
    unittest.main()
