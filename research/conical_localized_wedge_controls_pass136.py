"""Exact finite controls for the localized conical wedge calculation in136.

We expand the Jacobian-shaped matrix of Y=y+tau*X,
Z=z+rho(tau)*X, W=w+d*X+sigma*X**2/2 at fixed X. Independent
jets are formal coefficient data, not asserted actual polynomial coordinates.
In particular, unit Jacobian, a slice, and a realizable rank-two action are
not conclusions of these tests. No previous checker or solver is imported.

The tests retain the chart factor y_v: j_v=y_v*j_y. The conditional
normalization N'(v)=1 gives j_v=k_sigma, not j_y=k_sigma unless y_v=1.
The final finite polynomial substitution detects precisely this distinction;
it is not asserted to meet the complete original-frame hypotheses.
"""

import unittest

import sympy as sp


def wedge_matrix(X, rho_prime, y_jets, z_jets, w_jets, d_jets):
    """Rows Y,Z,W; columns tau,sigma,v; no division by its determinant."""
    yt, ys, yv = y_jets
    zt, zs, zv = z_jets
    wt, ws, wv = w_jets
    dt, ds, dv = d_jets
    return sp.Matrix([
        [yt + X, ys, yv],
        [zt + rho_prime*X, zs, zv],
        [wt + dt*X, ws + ds*X + X**2/2, wv + dv*X],
    ])


class ConicalLocalizedWedgeControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_full_independent_jet_expansion_and_selected_cofactor(self):
        X, r1 = sp.symbols("X r1")
        yt, ys, yv, zt, zs, zv = sp.symbols("yt ys yv zt zs zv")
        wt, ws, wv, dt, ds, dv = sp.symbols("wt ws wv dt ds dv")
        y_jets, z_jets = (yt, ys, yv), (zt, zs, zv)
        matrix = wedge_matrix(X, r1, y_jets, z_jets,
                              (wt, ws, wv), (dt, ds, dv))
        determinant = sp.Poly(sp.expand(matrix.det()), X)
        targets = {
            0: sp.Matrix([y_jets, z_jets, (wt, ws, wv)]).det(),
            1: (sp.Matrix([y_jets, z_jets, (dt, ds, dv)]).det()
                + (zs-r1*ys)*wv + (r1*yv-zv)*ws),
            2: (yv*zt-yt*zv)/2 + (zs-r1*ys)*dv + (r1*yv-zv)*ds,
            3: (r1*yv-zv)/2,
            4: 0,
        }
        for power, target in targets.items():
            self.assert_zero(determinant.coeff_monomial(X**power) - target)
        self.assertEqual(determinant.degree(), 3)

        # The two X-updates in the first rows share one column: the X^4 term vanishes.
        selected_v_numerator = matrix.minor_submatrix(2, 2).det()
        self.assert_zero(selected_v_numerator
                         - (yt*zs-ys*zt) - X*(zs-r1*ys))

    def test_tangent_chain_rule_and_conditional_normalization(self):
        X, y, r1, r2 = sp.symbols("X y r1 r2")
        kt, ks = sp.symbols("kt ks")
        yt, ys, yv = sp.symbols("yt ys yv")
        wt, ws, wy, dt, ds, dy = sp.symbols("wt ws wy dt ds dy")
        tangent = r2*y + kt
        # These are original v-chart jets reconstructed from partials at fixed y.
        matrix = wedge_matrix(
            X, r1, (yt, ys, yv),
            (tangent+r1*yt, ks+r1*ys, r1*yv),
            (wt+wy*yt, ws+wy*ys, wy*yv),
            (dt+dy*yt, ds+dy*ys, dy*yv),
        )
        c0 = tangent*ws - ks*wt
        c1 = tangent*ds + ks*(wy-dt)
        c2 = tangent/2 + ks*dy
        self.assert_zero(matrix.det() - yv*(c0 + c1*X + c2*X**2))
        selected_v_numerator = sp.Poly(sp.expand(matrix.minor_submatrix(2, 2).det()), X)
        self.assert_zero(selected_v_numerator.coeff_monomial(X) - ks)

        # In the coefficient field ks != 0, these are the proposed X^2/X^1 equations.
        correction = {dy: -tangent/(2*ks), wy: dt-tangent*ds/ks}
        self.assert_zero(c2.subs(correction))
        self.assert_zero(c1.subs(correction))
        self.assert_zero(matrix.det().subs(correction) - yv*c0)
        # Normalizing the selected top coefficient to one means j0=ks.
        self.assert_zero((yv*c0-ks) - ks*(yv*(tangent*ws/ks-wt)-1))

        # The y-chart must first be justified. With y_v=z_v=0, use independent
        # original w_v,d_v, not the now-invalid chain expressions wy*y_v,dy*y_v.
        original_wv, original_dv = sp.symbols("original_wv original_dv")
        degenerate = wedge_matrix(
            X, r1, (yt, ys, 0), (tangent+r1*yt, ks+r1*ys, 0),
            (wt, ws, original_wv), (dt, ds, original_dv),
        )
        D0 = yt*ks - ys*tangent
        self.assert_zero(degenerate.det() - (D0+ks*X)*(original_wv+original_dv*X))
        polynomial = sp.Poly(sp.expand(degenerate.det()), X)
        self.assert_zero(polynomial.coeff_monomial(X**2) - ks*original_dv)
        self.assert_zero(polynomial.coeff_monomial(X).subs(original_dv, 0)
                         - ks*original_wv)
        self.assert_zero(degenerate.det().subs({original_dv: 0, original_wv: 0}))

    def test_nontrivial_y_derivative_factor_is_retained(self):
        # Here y_v=2, rho=tau^2, k=sigma. This checks a formal polynomial
        # substitution with determinant one, not the complete rank-two frame premise.
        tau, sigma, v, X, y = sp.symbols("tau sigma v X y")
        Y = 2*v + tau*X
        Z = 4*tau*v + sigma + tau**2*X
        W = -tau/2 - 2*v**2*X + sigma*X**2/2
        v_chart = sp.Matrix([Y, Z, W]).jacobian([tau, sigma, v])
        self.assert_zero(v_chart.det() - 1)
        selected_v_numerator = v_chart.minor_submatrix(2, 2).det()
        self.assert_zero(selected_v_numerator - X)

        Y_y = y + tau*X
        Z_y = 2*tau*y + sigma + tau**2*X
        W_y = -tau/2 - y**2*X/2 + sigma*X**2/2
        y_chart = sp.Matrix([Y_y, Z_y, W_y]).jacobian([tau, sigma, y])
        self.assert_zero(y_chart.det() - sp.Rational(1, 2))
        self.assert_zero(v_chart.det() - 2*y_chart.det())
        self.assertNotEqual(sp.expand(y_chart.det()-1), 0)


if __name__ == "__main__":
    unittest.main()
