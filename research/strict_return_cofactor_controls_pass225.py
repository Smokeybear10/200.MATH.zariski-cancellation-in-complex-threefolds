"""Finite exact-algebra controls for the strict return-cofactor note225.

This standalone file imports no retained checker, solver, or proof source.
The cancellation checks are polynomial syzygies with residuals retained.
The root check is an explicit unit-ideal certificate, not a grid of roots.
Formal boundary fixtures are not actual globally sliced polynomial frames.

Actual field return, simplicity of the selected component, nonzero R and
q1, the actual unit Jacobian, and the characteristic-zero divisor/descent
arguments remain written-proof inputs. These tests do not prove sector
classification, arbitrary frame entry, or cancellation. Root alone may
execute the saved file after a complete source read.
"""

import unittest

import sympy as sp


def clean(expression):
    return sp.cancel(sp.expand(expression))


class StrictReturnCofactorControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_raw_wedge_residual_and_polynomial_cancellations(self):
        R, B, C, Lt, Lr = sp.symbols("R B C Lt Lr")
        yt, yr, yv, vt, vr, vv, wt, wr, wv = sp.symbols(
            "yt yr yv vt vr vv wt wr wv"
        )
        dy = sp.Matrix([[yt, yr, yv]])
        dtheta = sp.Matrix([[vt, vr, vv]])
        dw = sp.Matrix([[wt, wr, wv]])
        middle = R * dtheta + sp.Matrix([[B, C, 0]])
        J = sp.Matrix.vstack(dy, middle, dw).det()
        DU = R * (yv * vr - yr * vv) + C * yv
        DV = R * (yt * vv - yv * vt) - B * yv
        HU, HV = -R * (C * B + R * Lt), -R * (C**2 + R * Lr)
        potential_residual = R * dw + B * dy + C * dtheta - sp.Matrix([[Lt, Lr, 0]])
        wedge_residual = R**3 * J - DU * HU - DV * HV
        self.zero(wedge_residual - R**2 * sp.Matrix.vstack(dy, middle, potential_residual).det())

        # Impose only dt and d-rho rows. The entire remaining error is the
        # dv row, not a derivative taken after specializing an algebraic root.
        first_two_rows = {Lt: R * wt + B * yt + C * vt,
                          Lr: R * wr + B * yr + C * vr}
        dv_residual = R * wv + B * yv + C * vv
        transverse_minor = yt * (R * vr + C) - yr * (R * vt + B)
        self.zero(wedge_residual.subs(first_two_rows, simultaneous=True)
                  - R**2 * transverse_minor * dv_residual)

        # Independent derivative values retain every input residual. In the
        # written proof q1 and R are nonzero polynomials in a domain; only
        # then may their displayed common factors be cancelled.
        q1, W0, J0, gu, gv, hu, hv, du, dv = sp.symbols(
            "q1 W0 J0 gu gv hu hv du dv"
        )
        product_error = W0 * q1 - R**3
        factor_U, factor_V = hu - q1 * gu, hv - q1 * gv
        raw_wedge = R**3 * J0 - du * hu - dv * hv
        raw_V_gradient = hv + R * (C**2 + R * Lr)
        cancelled_wedge = W0 * J0 - du * gu - dv * gv
        cancelled_gradient = W0 * (C**2 + R * Lr) + R**2 * gv
        self.zero(q1 * cancelled_wedge
                  - (raw_wedge + du * factor_U + dv * factor_V + J0 * product_error))
        self.zero(R * cancelled_gradient
                  - (W0 * raw_V_gradient - W0 * factor_V - product_error * gv))

    def test_root_ideal_certificate_with_both_units_retained(self):
        # These are independent values at a geometric root of R. No root
        # multiplicity, yv or B nonvanishing assumption is introduced.
        W0, J0, B, C, yv, vv, gu, gv = sp.symbols("W0 J0 B C yv vv gu gv")
        iw, ij = sp.symbols("inverse_W0 inverse_J0")
        DU, DV = C * yv, -B * yv
        gradient_at_root = W0 * C**2
        derivative_at_root = B * yv + C * vv
        wedge_at_root = W0 * J0 - DU * gu - DV * gv
        linear_form = yv * gu + vv * gv
        self.zero(wedge_at_root - gv * derivative_at_root - (W0 * J0 - C * linear_form))

        # This polynomial identity avoids dividing by W0 or extracting a
        # square root of C^2 inside the symbolic computation.
        root_certificate = (
            W0 * (W0 * J0 + C * linear_form)
            * (wedge_at_root - gv * derivative_at_root)
            + linear_form**2 * gradient_at_root
        )
        self.zero(root_certificate - W0**3 * J0**2)

        # Adjoining inverse equations for the two nonzero root values makes
        # the contradiction an explicit identity expressing 1 in the ideal.
        aw, aj = iw * W0, ij * J0
        unit_certificate = (
            iw**3 * ij**2 * root_certificate
            - (aw - 1) * (aw**2 + aw + 1) * aj**2
            - (aj - 1) * (aj + 1)
        )
        self.zero(unit_certificate - 1)

    def test_nonunit_jacobian_and_coarse_degree_negative_controls(self):
        # Formal identity model only. Every gradient, differential and
        # wedge identity used by225 holds, but J=v is nonzero and NOT a
        # unit. Thus W0=1 can fail to vanish at the root of R=v.
        t, rho, v, U, V = sp.symbols("t rho v U V")
        y, theta, w = v, sp.S.Zero, v - rho
        R, B, C, Lt, Lr = v, -v, sp.S.Zero, sp.S.Zero, -v
        relation, cofactor = V, U**3
        eliminant = relation * cofactor
        point = {U: y, V: theta}
        q1, W0 = cofactor.subs(point, simultaneous=True), sp.S.One
        gu = sp.diff(relation, U).subs(point, simultaneous=True)
        gv = sp.diff(relation, V).subs(point, simultaneous=True)
        hu = sp.diff(eliminant, U).subs(point, simultaneous=True)
        hv = sp.diff(eliminant, V).subs(point, simultaneous=True)
        self.zero(relation.subs(point, simultaneous=True))
        self.zero(hu - q1 * gu)
        self.zero(hv - q1 * gv)
        self.zero(hu + R * (C * B + R * Lt))
        self.zero(hv + R * (C**2 + R * Lr))
        variables = (t, rho, v)
        dy = sp.Matrix([[sp.diff(y, s) for s in variables]])
        dtheta = sp.Matrix([[sp.diff(theta, s) for s in variables]])
        dw = sp.Matrix([[sp.diff(w, s) for s in variables]])
        for entry in R * dw + B * dy + C * dtheta - sp.Matrix([[Lt, Lr, 0]]):
            self.zero(entry)
        middle = R * dtheta + sp.Matrix([[B, C, 0]])
        J = sp.Matrix.vstack(dy, middle, dw).det()
        DU = R * (dy[2] * dtheta[1] - dy[1] * dtheta[2]) + C * dy[2]
        DV = R * (dy[0] * dtheta[2] - dy[2] * dtheta[0]) - B * dy[2]
        self.zero(J - v)
        self.zero(R**3 * J - DU * hu - DV * hv)
        self.zero(W0 * J - DU * gu - DV * gv)
        self.zero(W0 * (C**2 + R * Lr) + R**2 * gv)
        self.zero(W0 * q1 - R**3)
        self.assertEqual(sp.Poly(J, v).degree(), 1)
        self.assertEqual(W0.subs(v, 0), 1)

        # Coarse q1|R^3 and the sextic saturated degree alone also permit
        # equality. This is the formal cusp, not an actual frame or a model
        # claimed to satisfy the full gradients with a unit Jacobian.
        relation, cofactor = U**3 - V**2, V**3
        point = {U: v**2, V: v**3}
        q1 = cofactor.subs(point, simultaneous=True)
        R = v**3
        self.zero(relation.subs(point, simultaneous=True))
        self.zero(q1 - R**3)
        self.assertEqual(sp.Poly(relation * cofactor, U, V).total_degree(), 6)
        self.assertEqual(sp.Poly(q1, v).degree(), 9)
        self.assertEqual(sp.rem(R**3, q1, v), 0)
        self.assertNotEqual(sp.rem(R**3 / v, q1, v), 0)

        # Finite divisor sanity checks include constant, simple and repeated
        # roots. They do not prove squarefree-divisor descent in general.
        for return_poly in (sp.S.One, v - 2, (v - 2)**3, (v - 2)**2 * (v + 1)):
            with self.subTest(return_polynomial=return_poly):
                Rpoly = sp.Poly(return_poly, v)
                radical = Rpoly.exquo(sp.gcd(Rpoly, Rpoly.diff())).monic()
                allowed = sp.cancel(return_poly**3 / radical.as_expr())
                self.zero(allowed * radical.as_expr() - return_poly**3)
                self.assertEqual(sp.Poly(allowed, v).degree(), 3 * Rpoly.degree() - radical.degree())
                if Rpoly.degree() > 0:
                    self.assertLess(sp.Poly(allowed, v).degree(), 3 * Rpoly.degree())


if __name__ == "__main__":
    unittest.main()
