"""Four standalone exact algebra controls for working proof 314.

No earlier code is imported. These tests do not prove field integration,
formal factorization preservation, full initial-kernel transport, or a
recognition theorem. The actual source states those separate boundaries.
"""

import unittest

import sympy as sp


class VariableCouplingHodographControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_complete_cubic_part_and_both_linear_divisors(self):
        P, V, m, mt, ms, ktt, kttt, mtt, mts, mss = sp.symbols(
            "P V m mt ms ktt kttt mtt mts mss")
        F2 = ktt*P**2/2+mt*P*V+ms*V**2/2
        linear = mt*P+ms*V
        H3 = kttt*P**3/6+mtt*P**2*V/2+mts*P*V**2/2+mss*V**3/6
        cubic = sp.Poly(sp.expand(H3-linear*F2/m), P, V)
        self.assert_zero(cubic.coeff_monomial(V**3)-(mss/6-ms**2/(2*m)))
        direction = kttt-3*mtt*mt/ms+3*mts*mt**2/ms**2-mss*mt**3/ms**3
        self.assert_zero(cubic.as_expr().subs(V, -mt*P/ms)-P**3*direction/6)
        self.assert_zero(cubic.as_expr().subs({V: 0, mt: 0})-kttt*P**3/6)

    def test_inverse_derivatives_and_fixed_direction_cancellation(self):
        hr, hrr, hrrr, ht, htr = sp.symbols("hr hrr hrrr ht htr")
        m = 1/hr
        ms = -hrr/hr**3
        mss = (hrr*sp.diff(ms, hr)+hrrr*sp.diff(ms, hrr))/hr
        self.assert_zero(m*mss-3*ms**2+hrrr/hr**5)
        mt = -(htr*hr-hrr*ht)/hr**3
        old_direction = -mt/ms
        r1 = (old_direction-ht)/hr
        self.assert_zero(r1+htr/hrr)
        self.assert_zero(htr+hrr*r1)
        # Neither expression has divided by mt, which may vanish.
        self.assert_zero((r1+htr/hrr).subs(htr, hrr*ht/hr))

    def test_completed_square_third_derivative_coefficients(self):
        t, r = sp.symbols("t r")
        h = sp.Function("h")(t)
        ell = sp.Function("ell")(t)
        d = sp.Function("d")(t)
        H = (r+ell)**2/(2*h)+d
        A = sp.diff(H, r, 2)
        tr = sp.diff(H, t, r)
        residual = (sp.diff(H, t, 3)-3*tr*sp.diff(H, t, t, r)/A
                    +3*tr**2*sp.diff(A, t)/A**2)
        polynomial = sp.Poly(sp.expand(residual), r)
        self.assertLessEqual(polynomial.degree(), 2)
        h3, ell3, d3 = sp.diff(h, t, 3), sp.diff(ell, t, 3), sp.diff(d, t, 3)
        self.assert_zero(polynomial.coeff_monomial(r**2)+h3/(2*h**2))
        self.assert_zero(polynomial.coeff_monomial(r)-(ell3/h-ell*h3/h**2))
        self.assert_zero(polynomial.coeff_monomial(1)-(d3+ell*ell3/h-ell**2*h3/(2*h**2)))

    def test_full_actual_inverse_and_intrinsic_transport(self):
        X, Y, Z, W, Xs, Ys, Zs, Ws = sp.symbols("X Y Z W Xs Ys Zs Ws")
        l2, l1, l0, d2, d1, d0 = sp.symbols("l2 l1 l0 d2 d1 d0")
        shift = l2/2
        forward = {Xs: X+shift,
                   Ys: Y-l1*(X+shift)/2,
                   Zs: Z+l0*(X+shift)}
        forward[Ws] = W-d2*forward[Zs]-d1*forward[Ys]-d0*(X+shift)**2
        inverse = {X: Xs-shift, Y: Ys+l1*Xs/2, Z: Zs-l0*Xs,
                   W: Ws+d2*Zs+d1*Ys+d0*Xs**2}
        for new, expression in forward.items():
            self.assert_zero(expression.subs(inverse, simultaneous=True)-new)
        for old, expression in inverse.items():
            self.assert_zero(expression.subs(forward, simultaneous=True)-old)

        t, s, y, sigma, theta, k, kt, m, n, w = sp.symbols(
            "t s y sigma theta k kt m n w")
        z = 2*t*y+sigma**2+kt*sigma+m*theta+n
        full = {Y: y+sigma*X+t*X**2,
                Z: z+(2*t*sigma+k)*X+t**2*X**2,
                W: w+theta*X+s*X**2}
        Yfull = (full[Y].subs(X, Xs-shift)-l1*Xs/2).expand()
        Zfull = (full[Z].subs(X, Xs-shift)+l0*Xs).expand()
        Wfull = (full[W].subs(X, Xs-shift)-d2*Zfull-d1*Yfull-d0*Xs**2).expand()
        ell_poly = l2*t**2+l1*t+l0
        d_poly = d2*t**2+d1*t+d0
        ell_prime = sp.diff(ell_poly, t)
        sigma_new = sigma-2*shift*t-l1/2
        k_new = k+ell_poly
        theta_new = theta-2*shift*s-d2*(2*t*sigma_new+k_new)-d1*sigma_new
        y_new = y-shift*sigma+shift**2*t
        self.assert_zero(sp.Poly(Yfull, Xs).coeff_monomial(1)-y_new)
        self.assert_zero(sp.Poly(Yfull, Xs).coeff_monomial(Xs)-sigma_new)
        self.assert_zero(sp.Poly(Yfull, Xs).coeff_monomial(Xs**2)-t)
        self.assert_zero(sp.Poly(Zfull, Xs).coeff_monomial(Xs)-(2*t*sigma_new+k_new))
        self.assert_zero(sp.Poly(Wfull, Xs).coeff_monomial(Xs)-theta_new)
        self.assert_zero(sp.Poly(Wfull, Xs).coeff_monomial(Xs**2)-(s-d_poly))
        kt_new = kt+ell_prime+m*sp.diff(d_poly, t)
        n_new = (n-shift*k-shift**2*t**2+kt*ell_prime/2+ell_prime**2/4
                 +m*(d2*k_new+2*shift*s))
        self.assert_zero(sp.Poly(Zfull, Xs).coeff_monomial(1)
                         -(2*t*y_new+sigma_new**2+kt_new*sigma_new+m*theta_new+n_new))


if __name__ == "__main__":
    unittest.main(verbosity=2)
