"""Finite local algebra controls for the simple-return-root note231.

Standalone: no retained checker, solver, or proof file is imported.
Root-value identities and local Taylor coefficients are computed before
specializing their stated relations. The simple-root/unit-J hypotheses
remain visible. Boundary fixtures are formal algebra, not actual frames.

The actual chart, selected component and nonzero cofactor, scalar
calibration, local-ring order rules and descent are written-proof inputs.
No smoothness, normality, conic exclusion or unrestricted recognition is
certified by these controls. Root alone may execute this source after a
complete saved-source read.
"""

import unittest

import sympy as sp


def clean(expression):
    return sp.cancel(sp.expand(expression))


class SimpleReturnRootControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_root_determinant_and_affine_return_differential(self):
        R, B, C = sp.symbols("R B C")
        yt, yr, yv, vt, vr, vv, wt, wr, wv = sp.symbols(
            "yt yr yv vt vr vv wt wr wv"
        )
        dy = sp.Matrix([[yt, yr, yv]])
        dtheta = sp.Matrix([[vt, vr, vv]])
        dw = sp.Matrix([[wt, wr, wv]])
        middle = R * dtheta + sp.Matrix([[B, C, 0]])
        J = sp.Matrix.vstack(dy, middle, dw).det()
        at_root = J.subs({R: 0, C: 0})
        self.zero(at_root - B * (yv * wr - yr * wv))
        self.zero(at_root.subs(yv, 0) + B * yr * wv)
        dv_potential = R * wv + B * yv + C * vv
        self.zero(dv_potential.subs({R: 0, C: 0}) - B * yv)
        Lr = sp.symbols("Lr")
        rho_potential = R * wr + B * yr + C * vr - Lr
        self.zero(rho_potential.subs({R: 0, C: 0}) - (B * yr - Lr))

        r1, qt_r, qr_r, gu, gv = sp.symbols("r1 qt_r qr_r gu gv")
        return_derivative_error = r1 - qt_r * yv - qr_r * vv
        curve_derivative = gu * yv + gv * vv
        # With yv=0, both exact derivative identities force r1*gv=0.
        # Thus simple return r1!=0 forces gv=0, even if no plane gradient
        # was assumed nonzero in advance. No moving root is differentiated.
        self.zero(r1 * gv - qr_r * curve_derivative
                  - gv * return_derivative_error - yv * (qt_r * gv - qr_r * gu))

    def test_local_order_conflict_and_hypothesis_boundaries(self):
        eps = sp.symbols("eps")
        r1, r2, r3, c0, c1, c2, l0, l1, l2 = sp.symbols(
            "r1 r2 r3 c0 c1 c2 l0 l1 l2"
        )
        q2, q3, q4, g0, g1, g2 = sp.symbols("q2 q3 q4 g0 g1 g2")
        R = r1 * eps + r2 * eps**2 + r3 * eps**3
        C = c0 + c1 * eps + c2 * eps**2
        Lr = l0 + l1 * eps + l2 * eps**2
        q1 = q2 * eps**2 + q3 * eps**3 + q4 * eps**4
        Gv = g0 + g1 * eps + g2 * eps**2
        HV = -R * (C**2 + R * Lr)
        difference = sp.expand(HV - q1 * Gv)
        self.zero(difference.coeff(eps, 1) + r1 * c0**2)

        # Root-value reasoning supplies c0=g0=0. All higher local jets
        # stay arbitrary, including the possibility Gv identically zero.
        staged = sp.expand(difference.subs({c0: 0, g0: 0}))
        self.zero(staged.coeff(eps, 0))
        self.zero(staged.coeff(eps, 1))
        second_coefficient = staged.coeff(eps, 2)
        self.zero(second_coefficient + r1**2 * l0)
        self.zero(sp.expand((q1 * Gv).subs(g0, 0)).coeff(eps, 2))
        self.zero(sp.expand(HV.subs(c0, 0)).coeff(eps, 2) + r1**2 * l0)

        # l0=B*yr and J0=-B*yr*wv imply J0+l0*wv=0.
        # The coefficient mismatch therefore gives a polynomial unit-ideal
        # certificate, not a sample of particular nonzero numerical jets.
        J0, wv, ir, ij = sp.symbols("J0 wv inverse_r1 inverse_J0")
        determinant_error = J0 + l0 * wv
        consequence = wv * second_coefficient + r1**2 * determinant_error
        self.zero(consequence - r1**2 * J0)
        ar, aj = ir * r1, ij * J0
        certificate = ir**2 * ij * consequence - (ar - 1) * (ar + 1) * aj - (aj - 1)
        self.zero(certificate - 1)

        # Multiple-root order boundary only: the two terms inside the
        # bracket can now cancel. This is NOT a full actual chart fixture.
        double_R, vanishing_C, unit_Lr = eps**2, eps, -sp.S.One
        self.zero(-double_R * (vanishing_C**2 + double_R * unit_Lr))
        self.assertEqual(sp.Poly(double_R, eps).degree(), 2)

        # A stronger formal negative control without unit J: all used
        # gradients, full differential rows and the wedge are compatible
        # with simple R=v and ord(q1)=3 when J=v. It is not an actual frame.
        t, rho, v, U, V = sp.symbols("t rho v U V")
        y, theta, w = v, sp.S.Zero, v - rho
        R, B, C, Lt, Lr = v, -v, sp.S.Zero, sp.S.Zero, -v
        G, Q1 = V, U**3
        H = G * Q1
        point = {U: y, V: theta}
        q1 = Q1.subs(point, simultaneous=True)
        hu = sp.diff(H, U).subs(point, simultaneous=True)
        hv = sp.diff(H, V).subs(point, simultaneous=True)
        self.zero(hu + R * (C * B + R * Lt))
        self.zero(hv + R * (C**2 + R * Lr))
        variables = (t, rho, v)
        dy = sp.Matrix([[sp.diff(y, z) for z in variables]])
        dtheta = sp.Matrix([[sp.diff(theta, z) for z in variables]])
        dw = sp.Matrix([[sp.diff(w, z) for z in variables]])
        for entry in R * dw + B * dy + C * dtheta - sp.Matrix([[Lt, Lr, 0]]):
            self.zero(entry)
        J = sp.Matrix.vstack(dy, R * dtheta + sp.Matrix([[B, C, 0]]), dw).det()
        self.zero(J - v)
        self.zero(R**3 * J - v * hv)
        self.zero(q1 - v**3)
        self.assertEqual(sp.diff(R, v).subs(v, 0), 1)
        self.assertEqual(J.subs(v, 0), 0)

    def test_product_radical_conic_and_noncritical_root_identities(self):
        t, s = sp.symbols("t s", nonzero=True)
        ks, A2, A1, A0, chi, U, V = sp.symbols("ks A2 A1 A0 chi U V")
        P = lambda z: A2 * z**2 + A1 * z + A0
        y, theta = P(chi), s**2 * P(chi) + chi
        q, rho = s * t, s**2 * t
        R = (rho * y - t * theta) / (4 * q * rho) + ks / (2 * s * t)
        self.zero(R - (2 * s**2 * ks - chi) / (4 * s**3 * t))
        root = 2 * s**2 * ks
        self.zero(R.subs(chi, root))
        self.zero(sp.diff(R, chi) + 1 / (4 * s**3 * t))
        G = U - P(V - s**2 * U)
        GU, GV = sp.diff(G, U), sp.diff(G, V)
        self.zero(G.subs({U: y, V: theta}, simultaneous=True))
        self.zero(GU + s**2 * GV - 1)

        R0, B, C, Lt, Lr, eta = sp.symbols("R0 B C Lt Lr eta")
        HU, HV = -R0 * (C * B + R0 * Lt), -R0 * (C**2 + R0 * Lr)
        self.zero(HU + s**2 * HV
                  + R0 * (C * (B + s**2 * C) + R0 * (Lt + s**2 * Lr)))
        slope = 2 * A2 * root + A1
        self.zero(sp.diff(P(chi), chi).subs(chi, root) - slope)
        self.zero(GV.subs({U: y, V: theta}, simultaneous=True).subs(chi, root) + slope)

        # At R=0 with q1=eta*R, the divided gradient equations give
        # eta+C(B+s^2 C)=0 and C^2-eta*P'(root)=0.
        Bbar = B + s**2 * C
        combination_error = eta + C * Bbar
        V_gradient_error = C**2 - eta * slope
        dv_normalized = Bbar * slope + C
        self.zero(C * dv_normalized - V_gradient_error - slope * combination_error)
        self.zero((eta - C * Bbar) * combination_error
                  + Bbar**2 * V_gradient_error + eta * Bbar**2 * slope - eta**2)
        # Setting C=0 leaves eta; setting slope=0 forces eta^2 through the
        # displayed identity. Nonzero eta is a written cofactor input.
        self.zero(combination_error.subs(C, 0) - eta)


if __name__ == "__main__":
    unittest.main()
