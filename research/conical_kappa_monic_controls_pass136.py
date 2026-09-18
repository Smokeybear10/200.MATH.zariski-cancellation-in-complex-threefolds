"""Finite symbolic controls for kappa-polynomiality and monic pencils in136.

All coefficient functions below are formal. The differential tests do not
construct an actual localized coordinate frame or prove a finite-field
integration theorem. The polynomiality propagation example deliberately
fails a remaining coefficient equation. The pencil tests distinguish the
exact field C(p/q) from a selected component over a larger algebraic field;
they do not prove rationality or coefficient descent in the actual problem.
No earlier checker, search, or solver is imported.
"""

import unittest

import sympy as sp


def primitive_at_zero(polynomial, variable):
    """Polynomial integration, with zero constant; coefficients may be rational."""
    terms = sp.Poly(sp.expand(polynomial), variable)
    return sp.Add(*(coefficient*variable**(power[0]+1)/(power[0]+1)
                    for power, coefficient in terms.terms()))


def coefficient_targets(tau, kappa, r, sigma, ell, m):
    """Independent handwritten coefficients of (d_tau-r*y*d_kappa)w."""
    return {
        5: -r**3*sp.diff(sigma, kappa, 3)/16,
        4: 5*r*(2*sp.diff(r, tau)*sp.diff(sigma, kappa, 2)
                + 3*r*sp.diff(sigma, tau, kappa, kappa))/48,
        3: (-sp.diff(r, tau, 2)*sp.diff(sigma, kappa)/12
            - sp.diff(r, tau)*sp.diff(sigma, tau, kappa)/3
            - r*sp.diff(sigma, tau, tau, kappa)/2
            + r**2*sp.diff(ell, kappa, 2)/2),
        2: (sp.diff(sigma, tau, 3)/4
            - sp.diff(r, tau)*sp.diff(ell, kappa)/2
            - 3*r*sp.diff(ell, tau, kappa)/2),
        1: sp.diff(ell, tau, 2)-r*sp.diff(m, kappa),
        0: sp.diff(m, tau),
    }


class ConicalKappaMonicControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_integrated_graph_and_all_six_Dw_coefficients(self):
        tau, kappa, y = sp.symbols("tau kappa y")
        r = sp.Function("r")(tau)
        sigma = sp.Function("sigma")(tau, kappa)
        ell = sp.Function("ell")(tau, kappa)
        m = sp.Function("m")(tau, kappa)
        D = lambda f: sp.diff(f, tau)-r*y*sp.diff(f, kappa)
        d = -r*sp.diff(sigma, kappa)*y**2/4 + sp.diff(sigma, tau)*y/2 + ell
        w = (r**2*sp.diff(sigma, kappa, 2)*y**4/16
             - (sp.diff(r, tau)*sp.diff(sigma, kappa)/12
                + r*sp.diff(sigma, tau, kappa)/4)*y**3
             + (sp.diff(sigma, tau, 2)/4-r*sp.diff(ell, kappa)/2)*y**2
             + sp.diff(ell, tau)*y + m)
        self.assert_zero(sp.diff(d, y)-D(sigma)/2)
        self.assert_zero(sp.diff(w, y)-D(d))
        self.assert_zero(primitive_at_zero(D(d), y)+m-w)
        computed = sp.Poly(sp.expand(D(w)), y)
        self.assertEqual(computed.degree(), 5)
        for power, target in coefficient_targets(tau, kappa, r, sigma, ell, m).items():
            self.assert_zero(computed.coeff_monomial(y**power)-target)

        # Constant residual -1/y_v requires each positive-degree coefficient to vanish.
        yv = sp.Symbol("yv")
        self.assert_zero(sp.Poly(sp.expand(D(w)+1/yv), y).coeff_monomial(1)
                         - sp.diff(m, tau)-1/yv)

    def test_finite_polynomial_primitives_do_not_solve_all_compatibility(self):
        tau, kappa = sp.symbols("tau kappa")
        r = tau
        sigma = (tau+1)*kappa**2 + kappa/tau + tau**2
        self.assert_zero(sp.diff(sigma, kappa, 3))
        # The y^3 coefficient prescribes an affine polynomial ell_{kappa,kappa}.
        ell_kk = (sp.diff(r, tau, 2)*sp.diff(sigma, kappa)/(6*r**2)
                  + 2*sp.diff(r, tau)*sp.diff(sigma, tau, kappa)/(3*r**2)
                  + sp.diff(sigma, tau, tau, kappa)/r)
        self.assertLessEqual(sp.Poly(ell_kk, kappa).degree(), 1)
        ell = (primitive_at_zero(primitive_at_zero(ell_kk, kappa), kappa)
               + (tau+1)*kappa + tau**2)
        m_k = sp.diff(ell, tau, 2)/r
        m = primitive_at_zero(m_k, kappa) + 1/(tau+1)
        self.assertEqual(sp.Poly(sigma, kappa).degree(), 2)
        self.assertEqual(sp.Poly(ell, kappa).degree(), 3)
        self.assertEqual(sp.Poly(m, kappa).degree(), 4)
        self.assert_zero(sp.diff(ell, kappa, 2)-ell_kk)
        self.assert_zero(sp.diff(m, kappa)-m_k)
        self.assert_zero(sp.diff(ell, kappa, 4))
        self.assert_zero(sp.diff(m, kappa, 5))
        targets = coefficient_targets(tau, kappa, r, sigma, ell, m)
        for power in (5, 3, 1):
            self.assert_zero(targets[power])
        # This remaining obstruction is nonzero. The formal family is NOT a solution.
        self.assert_zero(targets[4] - (25*tau**2+10*tau)/24)
        self.assertNotEqual(sp.cancel(targets[4]), 0)

    def test_monic_coefficient_separation_and_exact_field_boundary(self):
        X, Y, Z, W, T = sp.symbols("X Y Z W T")
        cp, cq = sp.symbols("cp cq")
        forbidden = (W**3, W**2, X*W, Y*W, Z*W)
        p_coeffs, q_coeffs = sp.symbols("p0:5"), sp.symbols("q0:5")
        p_good, q_good = X**2*Y+Z, Y+1
        p = cp*W+p_good+sum(c*f for c, f in zip(p_coeffs, forbidden))
        q = cq*W+q_good+sum(c*f for c, f in zip(q_coeffs, forbidden))
        pencil = sp.Poly(p-T*q, W, X, Y, Z)
        for monomial, pi, qi in zip(forbidden, p_coeffs, q_coeffs):
            coefficient = pencil.coeff_monomial(monomial)
            self.assert_zero(coefficient-(pi-T*qi))
            # If this coefficient vanishes over C(T), its two constant coefficients vanish.
            self.assertEqual(sp.Poly(coefficient, T).coeff_monomial(1), pi)
            self.assertEqual(sp.Poly(coefficient, T).coeff_monomial(T), -qi)

        specialization = dict.fromkeys(p_coeffs+q_coeffs, 0)
        p_linear, q_linear = p.subs(specialization), q.subs(specialization)
        G = (T*q_good-p_good)/(cp-T*cq)
        self.assert_zero(p_linear-T*q_linear-(cp-T*cq)*(W-G))
        self.assert_zero(sp.diff(W-G, W)-1)

        # Both numerator and denominator can be nonconstant. No polynomial generator
        # for the rational field is assumed in this exact monic pencil example.
        p0, q0 = W+X**2*Y+Z, Y+1
        exact_relation = p0-T*q0
        self.assert_zero(exact_relation.subs(T, p0/q0))
        self.assert_zero(sp.diff(exact_relation, W)-1)
        U = sp.Symbol("U")
        inverse_W = U-X**2*Y-Z
        self.assert_zero(p0.subs(W, inverse_W)-U)
        self.assert_zero(inverse_W.subs(U, p0)-W)

        # A selected component over C(lambda), lambda^2=T, is a different field.
        # One must not apply its degree-one conclusion to the squared numerator/denominator.
        lam = sp.Symbol("lam")
        squared_pencil = X**2-T*Y**2
        selected = X-lam*Y
        self.assert_zero(squared_pencil.subs(T, lam**2)-selected*(X+lam*Y))
        self.assert_zero(sp.resultant(selected, lam**2-T, lam)-squared_pencil)
        self.assertEqual(sp.Poly(squared_pencil, X, Y).total_degree(), 2)
        self.assertEqual(sp.Poly(selected, X, Y).total_degree(), 1)
        self.assert_zero(squared_pencil.subs(T, X**2/Y**2))
        self.assert_zero(selected.subs(lam, X/Y))
        self.assertNotEqual(sp.cancel(X**2/Y**2-X/Y), 0)


if __name__ == "__main__":
    unittest.main()
