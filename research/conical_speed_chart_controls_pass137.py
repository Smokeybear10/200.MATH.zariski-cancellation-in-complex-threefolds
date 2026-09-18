"""Exact controls for the speed-based conical chart in137.

The first two methods use independent formal jets, not assumed realizable
as actual polynomial coordinates or to have a unit determinant. They check
the selected cofactor without dividing by sigma_xi. No universal descent
or field theorem is certified by these finite symbolic identities.

The third method is different: both polynomial inverse orders are verified
for an actual resonant, rank-two conical action with no slice. Its derivative
ideal is the proper principal ideal (xi), so it does not satisfy the sliced
nonexistence theorem and is not a cancellation counterexample.
No earlier checker or solver is imported.
"""

import unittest

import sympy as sp


def jet_matrix(X, r1, yj, zj, wj, dj, sigma_tau, sigma_xi):
    """Rows Y,Z,W; columns tau,xi,v; entries are formal jets."""
    yt, yi, yv = yj
    zt, zi, zv = zj
    wt, wi, wv = wj
    dt, di, dv = dj
    return sp.Matrix([
        [yt+X, yi, yv],
        [zt+r1*X, zi, zv],
        [wt+dt*X+sigma_tau*X**2/2,
         wi+di*X+sigma_xi*X**2/2, wv+dv*X],
    ])


class ConicalSpeedChartControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_general_wedge_and_tangency_without_acceleration_independence(self):
        X, r1, st, si = sp.symbols("X r1 st si")
        yt, yi, yv, zt, zi, zv = sp.symbols("yt yi yv zt zi zv")
        wt, wi, wv, dt, di, dv = sp.symbols("wt wi wv dt di dv")
        yj, zj = (yt, yi, yv), (zt, zi, zv)
        matrix = jet_matrix(X, r1, yj, zj, (wt, wi, wv), (dt, di, dv), st, si)
        polynomial = sp.Poly(sp.expand(matrix.det()), X)
        tangent_defect = r1*yv-zv
        targets = {
            0: sp.Matrix([yj, zj, (wt, wi, wv)]).det(),
            1: (sp.Matrix([yj, zj, (dt, di, dv)]).det()
                + (zi-r1*yi)*wv+tangent_defect*wi),
            2: (si*(yv*zt-yt*zv)+st*(yi*zv-yv*zi))/2
               + (zi-r1*yi)*dv+tangent_defect*di,
            3: si*tangent_defect/2,
            4: 0,
        }
        for power, target in targets.items():
            self.assert_zero(polynomial.coeff_monomial(X**power)-target)

        # These are adjugate numerators for the selected original partial d/dW.
        Ttau_num = matrix.minor_submatrix(2, 0).det()
        Txi_num = -matrix.minor_submatrix(2, 1).det()
        Tv_num = matrix.minor_submatrix(2, 2).det()
        self.assert_zero(Ttau_num-(yi*zv-yv*zi))
        self.assert_zero(Txi_num-(yv*zt-yt*zv+X*tangent_defect))
        self.assert_zero(Tv_num-(yt*zi-yi*zt+X*(zi-r1*yi)))
        self.assert_zero(sp.Poly(sp.expand(Txi_num), X).coeff_monomial(X)-tangent_defect)

        # With sigma_xi=0, the cubic determinant term says nothing about tangency.
        # The selected speed-cofactor coefficient still detects the same defect.
        self.assert_zero(targets[3].subs(si, 0))
        self.assert_zero(sp.diff(Txi_num.subs(si, 0), X)-tangent_defect)
        self.assertEqual(tangent_defect.subs({r1: 1, yv: 1, zv: 0}), 1)

    def test_tangent_chain_rule_and_kappa_reparameterization(self):
        X, y, r1, r, kt, ki = sp.symbols("X y r1 r kt ki")
        yt, yi, yv = sp.symbols("yt yi yv")
        wt, wi, wy, dt, di, dy, st, si = sp.symbols("wt wi wy dt di dy st si")
        alpha = r*y+kt
        matrix = jet_matrix(
            X, r1, (yt, yi, yv), (alpha+r1*yt, ki+r1*yi, r1*yv),
            (wt+wy*yt, wi+wy*yi, wy*yv),
            (dt+dy*yt, di+dy*yi, dy*yv), st, si,
        )
        c0 = alpha*wi-ki*wt
        c1 = ki*wy-ki*dt+alpha*di
        c2 = ki*dy+(alpha*si-ki*st)/2
        self.assert_zero(matrix.det()-yv*(c0+c1*X+c2*X**2))
        Txi_num = sp.Poly(sp.expand(-matrix.minor_submatrix(2, 1).det()), X)
        Tv_num = sp.Poly(sp.expand(matrix.minor_submatrix(2, 2).det()), X)
        self.assert_zero(Txi_num.coeff_monomial(X))
        self.assert_zero(Tv_num.coeff_monomial(X)-ki)

        correction = {dy: (st-alpha*si/ki)/2, wy: dt-alpha*di/ki}
        self.assert_zero(c1.subs(correction))
        self.assert_zero(c2.subs(correction))
        self.assert_zero(matrix.det().subs(correction)-yv*c0)
        # sigma_xi may be zero: all denominators are the separately proved k_xi.
        self.assert_zero(correction[dy].subs(si, 0)-st/2)
        ell = sp.Symbol("ell")
        d_integrated = -r*si*y**2/(4*ki)+(st-kt*si/ki)*y/2+ell
        self.assert_zero(sp.diff(d_integrated, y)-correction[dy])

        # Partial_tau(new)=partial_tau(old)-k_tau/k_xi*partial_xi.
        sigma_tau_new, sigma_kappa = st-kt*si/ki, si/ki
        d_tau_new, d_kappa = dt-kt*di/ki, di/ki
        w_tau_new, w_kappa = wt-kt*wi/ki, wi/ki
        self.assert_zero(correction[dy]-(sigma_tau_new-r*y*sigma_kappa)/2)
        self.assert_zero(correction[wy]-(d_tau_new-r*y*d_kappa))
        self.assert_zero(c0+ki*(w_tau_new-r*y*w_kappa))
        # J0=k_xi gives D(w)=-1/y_v, with the original chart factor retained.
        self.assert_zero((yv*c0-ki)+ki*(yv*(w_tau_new-r*y*w_kappa)+1))

    def test_actual_resonant_rank_two_boundary_without_slice(self):
        x, tau, xi, v = sp.symbols("x tau xi v")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted = (x, tau, xi, v)
        forward = sp.Matrix([
            x,
            2*v+tau*x,
            4*tau*v+xi+tau**2*x,
            -tau/2+v*x+tau*x**2/2,
        ])
        inverse_tau = X*Y-2*W
        inverse_v = (Y-inverse_tau*X)/2
        inverse_xi = Z-2*inverse_tau*Y+inverse_tau**2*X
        inverse = sp.Matrix([X, inverse_tau, inverse_xi, inverse_v])
        originals = (X, Y, Z, W)
        for value, expected in zip(inverse, adapted):
            self.assert_zero(value.subs(dict(zip(originals, forward)), simultaneous=True)-expected)
        for value, expected in zip(forward, originals):
            self.assert_zero(value.subs(dict(zip(adapted, inverse)), simultaneous=True)-expected)
        self.assert_zero(forward.jacobian(adapted).det()-1)

        E = lambda f: sp.expand(xi*sp.diff(f, x))
        speeds = sp.Matrix([E(f) for f in forward[:3]])
        self.assertEqual(speeds, sp.Matrix([xi, xi*tau, xi*tau**2]))
        for f in forward[:3]:
            self.assert_zero(E(E(f)))
        self.assert_zero(E(E(forward[3]))-xi**2*tau)
        self.assert_zero(E(E(E(forward[3]))))
        self.assert_zero(speeds[0]*speeds[2]-speeds[1]**2)
        self.assert_zero(sp.Matrix([speeds[0], speeds[1]]).jacobian([xi, tau]).det()-xi)
        self.assert_zero(xi*sp.diff(xi**2*tau, xi)-2*xi**2*tau)

        # E(B) generates exactly (xi): every image is divisible by xi and E(x)=xi.
        # xi is an actual coordinate, hence this ideal is proper and no slice exists.
        self.assert_zero(E(forward[0])-xi)
        for f in forward:
            self.assert_zero(E(f).subs(xi, 0))
            self.assert_zero(sp.rem(E(f), xi, xi))
        invariant = forward[3]-forward[0]*forward[1]/2
        self.assert_zero(invariant+tau/2)
        self.assert_zero(E(invariant))

        # The same exact original partial has the expected coefficient normalization.
        T_adapted = sp.Matrix([
            sp.expand(sp.diff(f, W).subs(dict(zip(originals, forward)), simultaneous=True))
            for f in inverse
        ])
        self.assertEqual(T_adapted, sp.Matrix([0, -2, 8*v, x]))
        self.assertEqual(T_adapted.diff(x), sp.Matrix([0, 0, 0, 1]))
        self.assert_zero(sp.diff(xi, v))
        self.assert_zero(sp.diff(T_adapted[2], v)-8)
        for j, f in enumerate(forward):
            transported = sum(T_adapted[i]*sp.diff(f, adapted[i]) for i in range(4))
            self.assert_zero(transported-(1 if j == 3 else 0))


if __name__ == "__main__":
    unittest.main()
