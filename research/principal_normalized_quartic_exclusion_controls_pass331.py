"""Exact algebra controls for the three degree-pattern exclusions in330.

The written proofs supply whole polynomial-ring return, the degree list,
and parity-module arguments. This suite checks their explicit identities;
it is not a formal certificate for those universal arguments or cancellation.
No other saved checker is imported.
"""

import unittest

import sympy as sp


class NormalizedQuarticControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    @staticmethod
    def primitive(u, p, rr, tr, tt, ht, lr, lt):
        return rr*u**4/2 + tr*u**2*p + tt*p**2/2 + 2*u*p + ht*u - lr*u**2 - lt*p

    def test_pair_12_specialization_retains_exact_quadratic_and_cubic(self):
        u, x, t, s, ell = sp.symbols("u x t s ell")
        a, b = sp.symbols("a b", nonzero=True)
        c, d2, d1, d0 = sp.symbols("c d2 d1 d0")
        sigma = a*u**2 + b*u + c
        theta = d2*u**2 + d1*u + d0
        yy = u + sigma*x + t*x**2
        zz = 2*t*u + sigma**2 + theta + (2*t*sigma+s)*x + t**2*x**2
        ww = ell - 2*sigma*u + theta*x + s*x**2
        invariant = yy**2 + x*ww - x**2*zz
        self.assert_zero(invariant-u**2-ell*x)
        x0 = -1/b
        y0, z0, w0 = (sp.expand(f.subs(x, x0)) for f in (yy, zz, ww))
        self.assert_zero(sp.Poly(y0, u).coeff_monomial(u))
        self.assert_zero(sp.Poly(y0, u).coeff_monomial(u**2) + a/b)
        self.assert_zero(sp.Poly(w0, u).coeff_monomial(u**3) + 2*a)
        self.assert_zero(z0 - (y0**2 + x0*w0-u**2-ell*x0)/x0**2)
        self.assert_zero(y0 - (-a/b)*u**2 - y0.subs(u, 0))

    def test_pair_12_zero_linear_coefficient_still_fails_fourth_level(self):
        u, a, c = sp.symbols("u a c")
        rr, tr, tt, ht, lr, lt = sp.symbols("rr tr tt ht lr lt")
        q = self.primitive(u, a*u**2+c, rr, tr, tt, ht, lr, lt)
        odd = sp.expand((q-q.subs(u, -u))/2)
        self.assert_zero(odd - (2*a*u**3 + (2*c+ht)*u))
        self.assert_zero(sp.Poly(q, u).coeff_monomial(u**3) - 2*a)

    def test_pair_14_successive_leading_coefficients(self):
        u = sp.symbols("u")
        a4, a3, a2, a1, a0 = sp.symbols("a4 a3 a2 a1 a0")
        rr, tr, tt, ht, lr, lt = sp.symbols("rr tr tt ht lr lt")
        p = a4*u**4+a3*u**3+a2*u**2+a1*u+a0
        q = sp.expand(self.primitive(u, p, rr, tr, tt, ht, lr, lt))
        self.assert_zero(sp.Poly(q, u).coeff_monomial(u**8) - tt*a4**2/2)
        q1 = q.subs(tt, 0)
        self.assert_zero(sp.Poly(q1, u).coeff_monomial(u**6) - tr*a4)
        q2 = q1.subs(tr, 0)
        self.assert_zero(sp.Poly(q2, u).coeff_monomial(u**5) - 2*a4)

    def test_pair_24_parity_and_final_cubic_obstruction(self):
        v, u = sp.symbols("v u")
        a, h, aa, bb, dd, cc = sp.symbols("a h aa bb dd cc")
        rr, tr, tt, ht, lr, lt = sp.symbols("rr tr tt ht lr lt")
        y = a*v**2+h
        even_p = aa*u**2+bb*u+dd
        sigma = even_p.subs(u, y)+cc*v
        q = sp.expand(self.primitive(y, sigma, rr, tr, tt, ht, lr, lt))
        odd = sp.expand((q-q.subs(v, -v))/2)
        bracket = (tr+tt*aa)*u**2 + (tt*bb+2)*u + tt*dd-lt
        self.assert_zero(odd-cc*v*bracket.subs(u, y))
        # If tt=0, the odd bracket retains coefficient 2 at u.
        self.assert_zero(sp.Poly(bracket.subs(tt, 0), u).coeff_monomial(u)-2)
        even = self.primitive(u, even_p, rr, tr, tt, ht, lr, lt) + tt*cc**2*(u-h)/(2*a)
        self.assert_zero((q+q.subs(v, -v))/2 - even.subs(u, y))
        reduced = even.subs({tr: -tt*aa, lt: tt*dd, bb: -2/tt}, simultaneous=True)
        selected_p = aa*u**2-2*u/tt+dd
        expected = rr*u**4/2-tt*selected_p**2/2+ht*u-lr*u**2+tt*cc**2*(u-h)/(2*a)
        self.assert_zero(reduced-expected)
        self.assert_zero(sp.Poly(sp.expand(reduced), u).coeff_monomial(u**3)-2*aa)


if __name__ == "__main__":
    unittest.main(verbosity=2)
