"""Exact coefficient and factor controls for the cusp chart159.

Independent formal coefficient jets check the original determinant's X4/X3
coefficients, the integrated row subtraction and X2 potential, and the X1/X0
potential and quotient-gradient identities. Generic jets are NOT declared
actual polynomial frames or constant-Jacobian solutions. Known powers of
r=k_rho are cleared before the lower determinant is expanded.

Separate formal plane examples guard the selected-factor and degree-drop
scope: a cofactor can restrict to a nonzero constant without being constant
as a polynomial. Those examples are not asserted to satisfy the full cusp
coefficient system. A separate fourth method has an explicit two-sided
polynomial inverse and is a genuine cusp (1,1,2,2) frame with coordinate
slice X. It has no extra factor and is already a polynomial translation.
Finite identities do not prove the universal chart, generic-field descent,
correction existence, or cancellation. No previous checker is imported.
"""

import math
import unittest

import sympy as sp


class CuspGenericChartControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    @staticmethod
    def total_degree(expression, variables):
        return sp.Poly(sp.expand(expression), *variables).total_degree()

    @staticmethod
    def homogeneous(expression, U, V, degree):
        scale = sp.symbols("scale")
        return sp.expand(expression.xreplace({U: scale*U, V: scale*V})).coeff(scale, degree)

    @staticmethod
    def potential_data():
        U, V = sp.symbols("U V")
        r = sp.symbols("r", nonzero=True)
        ell, ellt, ellp = sp.symbols("ell ellt ellp")
        ktt, ktp, kpp, kttt, kttp, ktpp, kppp = sp.symbols(
            "ktt ktp kpp kttt kttp ktpp kppp")
        nt, np, ntt, ntp, npp = sp.symbols("nt np ntt ntp npp")
        half, sixth = sp.Rational(1, 2), sp.Rational(1, 6)
        f = U**3+half*ktt*U*U+ktp*U*V+half*kpp*V*V+nt*U+np*V
        ft = half*kttt*U*U+kttp*U*V+half*ktpp*V*V+ntt*U+ntp*V
        fp = half*kttp*U*U+ktpp*U*V+half*kppp*V*V+ntp*U+npp*V
        g3 = (sixth*kttt*U**3+half*kttp*U*U*V+half*ktpp*U*V*V
              +sixth*kppp*V**3+half*ntt*U*U+ntp*U*V+half*npp*V*V)
        A, B = sp.diff(f, V), sp.diff(f, U)
        omega = (ell-f)/r
        phi = A*omega+g3-ellt*U-ellp*V
        # These are commuting parameter jets through order3 for k and order2
        # for n, not a derivation acting nontrivially on complex constants.
        return dict(U=U, V=V, r=r, ell=ell, ellt=ellt, ellp=ellp,
                    ktt=ktt, ktp=ktp, kpp=kpp, kttt=kttt, kttp=kttp,
                    ktpp=ktpp, kppp=kppp, nt=nt, np=np, ntt=ntt, ntp=ntp,
                    npp=npp, f=f, ft=ft, fp=fp, g3=g3, A=A, B=B,
                    omega=omega, phi=phi)

    def test_original_determinant_top_coefficients_and_integrated_rows(self):
        X, tau, y, theta, k, n = sp.symbols("X tau y theta k n")
        yt, yp, yv, zt, zp, zv = sp.symbols("yt yp yv zt zp zv")
        st, sp_, sv = sp.symbols("st sp sv")
        tt, tp, tv, wt, wp, wv = sp.symbols("tt tp tv wt wp wv")
        kt, r, ktt, ktp, kpp, nt, np = sp.symbols("kt r ktt ktp kpp nt np")
        original = sp.Matrix(((X+yt, yp, yv),
                              (3*tau*tau*X*X+st*X+zt, sp_*X+zp, sv*X+zv),
                              (tt*X+wt, X*X+tp*X+wp, tv*X+wv)))
        determinant = sp.Poly(sp.expand(original.det()), X)
        self.assertLessEqual(determinant.degree(), 4)
        self.zero(determinant.coeff_monomial(X**4)-(3*tau*tau*yv-sv))
        cofactor = original.adjugate()[2, 1]
        numerator = -((X+yt)*(X*X+tp*X+wp)-yp*(tt*X+wt))
        self.zero(cofactor-numerator)
        self.zero(sp.expand(cofactor).coeff(X, 3)+1)
        # The actual proof supplies a constant determinant J0 and then compares
        # this -1 coefficient to Nv/a^3. No determinant division is made here.

        sigma_jets = {st: 6*tau*y+3*tau*tau*yt+kt,
                      sp_: 3*tau*tau*yp+r, sv: 3*tau*tau*yv}
        after_sigma = sp.Poly(sp.expand(determinant.as_expr().xreplace(sigma_jets)), X)
        self.zero(after_sigma.coeff_monomial(X**4))
        expected3 = (6*tau*y+kt)*yv+r*tv-zv
        self.zero(after_sigma.coeff_monomial(X**3)-expected3)

        A = ktp*y+kpp*theta+np
        B = 3*y*y+ktt*y+ktp*theta+nt
        z_jets = {zt: (6*tau*y+kt)*yt+r*tt+B,
                  zp: (6*tau*y+kt)*yp+r*tp+A,
                  zv: (6*tau*y+kt)*yv+r*tv}
        integrated = original.xreplace({**sigma_jets, **z_jets})
        reduced = integrated.copy()
        factor = 3*tau*tau*X+6*tau*y+kt
        reduced[1, :] = integrated[1, :]-factor*integrated[0, :]
        expected_row = sp.Matrix([[r*tt+B, r*(tp+X)+A, r*tv]])
        for entry in reduced[1, :]-expected_row:
            self.zero(entry)
        reduced_det = sp.Poly(sp.expand(reduced.det()), X)
        self.zero(reduced_det.as_expr()-integrated.det())
        self.assertLessEqual(reduced_det.degree(), 2)
        self.zero(reduced_det.coeff_monomial(X**2)-(r*wv+B*yv+A*tv))

        U, V, w = sp.symbols("U V w")
        f = U**3+ktt*U*U/2+ktp*U*V+kpp*V*V/2+nt*U+np*V
        evaluated = {U: y, V: theta}
        self.zero(sp.diff(f, U).xreplace(evaluated)-B)
        self.zero(sp.diff(f, V).xreplace(evaluated)-A)
        # Total v differentiation of r*w+f(y,theta) is precisely that X2
        # coefficient. This identity also holds when r=0; no division was used.
        potential_v = r*wv+sp.diff(f, U).xreplace(evaluated)*yv+sp.diff(f, V).xreplace(evaluated)*tv
        self.zero(reduced_det.coeff_monomial(X**2)-potential_v)
        self.zero((reduced_det.coeff_monomial(X**2)-potential_v).subs(r, 0))

        sigma = 3*tau*tau*y+k
        z = 3*tau*y*y+kt*y+r*theta+n
        Ychart, Zchart = y+tau*X, z+sigma*X+tau**3*X*X
        self.zero(X*Zchart-Ychart**3-(-y**3+(kt*y+r*theta+n)*X+k*X*X))

    def test_exact_quartic_potential_and_constant_quotient_gradient(self):
        d = self.potential_data()
        U, V, r = d["U"], d["V"], d["r"]
        f, A, B, omega, phi = (d[name] for name in ("f", "A", "B", "omega", "phi"))
        self.zero(sp.diff(d["g3"], U)-d["ft"])
        self.zero(sp.diff(d["g3"], V)-d["fp"])
        self.zero(sp.diff(A, U)-d["ktp"])
        self.zero(sp.diff(A, V)-d["kpp"])
        expectedU = d["ft"]-d["ellt"]+d["ktp"]*omega-A*B/r
        expectedV = d["fp"]-d["ellp"]+d["kpp"]*omega-A*A/r
        phiU, phiV = sp.diff(phi, U), sp.diff(phi, V)
        self.zero(r*(phiU-expectedU))
        self.zero(r*(phiV-expectedV))
        self.assertEqual(self.total_degree(phi, (U, V)), 4)
        self.zero(r*self.homogeneous(phi, U, V, 4)
                  +(d["ktp"]*U+d["kpp"]*V)*U**3)

        X, y, theta = sp.symbols("X y theta")
        yt, yp, yv, tt, tp, tv = sp.symbols("yt yp yv tt tp tv")
        at = {U: y, V: theta}
        Ae, Be, we = (p.xreplace(at) for p in (A, B, omega))
        # Coefficient derivatives hold formal U,V fixed, then the full chain
        # rule adds their moving y,theta terms. The r derivatives are ktp,kpp.
        wt = (d["ellt"]-d["ft"].xreplace(at)-d["ktp"]*we-Be*yt-Ae*tt)/r
        wp = (d["ellp"]-d["fp"].xreplace(at)-d["kpp"]*we-Be*yp-Ae*tp)/r
        wv = -(Be*yv+Ae*tv)/r
        reduced = sp.Matrix(((X+yt, yp, yv),
                             (r*tt+Be, r*(tp+X)+Ae, r*tv),
                             (wt+X*tt, wp+X*tp+X*X, wv+X*tv)))
        # Clear the certified nonzero coefficient denominator in the last
        # row BEFORE taking its determinant, then expand a polynomial matrix.
        cleared = reduced.copy()
        for j in range(3):
            cleared[2, j] = sp.expand(r*r*reduced[2, j])
        det_numerator = sp.Poly(sp.expand(cleared.det()), X)
        self.assertLessEqual(det_numerator.degree(), 1)
        expected1 = phiU.xreplace(at)*yv+phiV.xreplace(at)*tv
        self.zero(det_numerator.coeff_monomial(X)-r*r*expected1)
        CU = (tp+Ae/r)*yv-yp*tv
        CV = yt*tv-(tt+Be/r)*yv
        expected0 = CU*phiU.xreplace(at)+CV*phiV.xreplace(at)
        self.zero(det_numerator.coeff_monomial(1)-r*r*expected0)
        # No claim that expected1 vanishes or expected0 is a unit for arbitrary
        # jets. Those are additional actual-frame conditions in the written proof.

    def test_degree_drops_and_formal_extra_factor_boundaries(self):
        d = self.potential_data()
        U, V, r, phi = d["U"], d["V"], d["r"], d["phi"]
        vanish_mixed = {d[name]: 0 for name in ("ktp", "kpp", "kttp", "ktpp", "kppp")}
        cubic = sp.expand(phi.xreplace(vanish_mixed))
        self.assertEqual(self.total_degree(cubic, (U, V)), 3)
        self.zero(self.homogeneous(cubic, U, V, 3)
                  -(d["kttt"]/6-d["np"]/r)*U**3)
        # The written differentiated coefficient identity also forces npp=0
        # when the cubic coefficient vanishes. Include that consequence here;
        # this substitution is not a numerical proof of the derivative argument.
        quadratic = sp.expand(cubic.xreplace({d["np"]: r*d["kttt"]/6, d["npp"]: 0}))
        self.assertEqual(self.total_degree(quadratic, (U, V)), 2)
        expected2 = (d["ntt"]/2-d["kttt"]*d["ktt"]/12)*U*U+d["ntp"]*U*V
        self.zero(self.homogeneous(quadratic, U, V, 2)-expected2)

        v = sp.symbols("v")
        # These factor/gradient examples are FORMAL PLANE polynomials only,
        # not solutions to the full coefficient-derivative system above.
        G = U
        for K, degree in ((sp.Integer(1), 2), (U, 3), (U*U+V, 4)):
            relation = G+G*G*K
            cofactor = 1+G*K
            selected = {U: 0, V: v}
            self.zero(relation-G*cofactor)
            self.assertEqual(self.total_degree(relation, (U, V)), degree)
            self.zero(relation.xreplace(selected))
            self.zero(cofactor.xreplace(selected)-1)
            self.assertGreater(self.total_degree(cofactor, (U, V)), 0)
            self.zero(sp.diff(relation, U).xreplace(selected)-1)
            self.zero(sp.diff(relation, V).xreplace(selected))
            self.zero(self.homogeneous(relation, U, V, degree)-U**degree)

        G = U*U+U+V+1
        relation, cofactor = 3*G+2*G*G, 3+2*G
        selected = {U: v, V: -v*v-v-1}
        self.zero(G.xreplace(selected))
        self.zero(relation-G*cofactor)
        self.zero(cofactor.xreplace(selected)-3)
        self.zero(sp.diff(relation, V).xreplace(selected)-3)
        self.assertEqual(self.total_degree(G, (U, V)), 2)
        self.assertEqual(self.total_degree(relation, (U, V)), 4)
        self.zero(self.homogeneous(relation, U, V, 4)-2*U**4)
        self.assertGreater(self.total_degree(cofactor, (U, V)), 0)
        # Selected quotient parameter U=v and unit gradient do not imply that
        # the nonconstant cofactor is constant in L[U,V].

    def test_actual_cusp_boundary_inverse_and_selected_normalization(self):
        x, tau, rho, v = base = sp.symbols("x tau rho v")
        X, Y, Z, W = original = sp.symbols("X Y Z W")
        theta = -v**3-tau
        z0 = 3*tau*v*v+theta+rho
        sigma = 3*tau*tau*v+rho
        forward = (x, v+tau*x, z0+sigma*x+tau**3*x*x,
                   tau+theta*x+rho*x*x)
        H = X*Z-Y**3
        inv_tau = (1+X)*W-X*H
        inv_v = Y-X*inv_tau
        inv_rho = (Z+W-H-3*inv_tau*inv_v**2
                   -3*inv_tau**2*inv_v*X-inv_tau**3*X*X)
        inverse = (X, inv_tau, inv_rho, inv_v)
        to_base = dict(zip(original, forward))
        to_original = dict(zip(base, inverse))
        for variable, expression in zip(base, inverse):
            self.zero(expression.xreplace(to_base)-variable)
        for variable, expression in zip(original, forward):
            self.zero(expression.xreplace(to_original)-variable)
        # These cleared identities are independent checks of the reverse
        # reconstruction. No division by X, or deletion of X=0, is used.
        self.zero(inv_rho*X-H-inv_v**3-X*(W-H))
        self.zero(inv_tau-((1+X)*W-X*H))
        H_actual = sp.expand(H.xreplace(to_base))
        self.zero(H_actual-(-v**3+(theta+rho)*x+rho*x*x))
        self.zero(forward[3]-H_actual-(tau+v**3-rho*x))

        weights = (1, 1, 2, 2)
        self.assertEqual(tuple(sp.Poly(f, x).degree() for f in forward), weights)
        self.zero(sp.diff(x, x)-1)
        leading = tuple(sp.Poly(f, x).LC() for f in forward)
        self.assertEqual(leading, (1, tau, tau**3, rho))
        for f, d, lc in zip(forward, weights, leading):
            self.zero(sp.diff(f, x, d)-math.factorial(d)*lc)
            self.zero(sp.diff(f, x, d+1))
        self.zero(sp.Matrix(forward).jacobian(base).det()+1)
        relative = sp.Matrix(forward[1:]).jacobian((tau, rho, v))
        self.zero(relative.det()+1)

        # Differentiate the ACTUAL inverse, then transport to the source.
        coefficients = tuple(sp.expand(sp.diff(f, Z).xreplace(to_base)) for f in inverse)
        expected = (0, -x*x, 1-x+3*v*v*x*x, x**3)
        for coefficient, target in zip(coefficients, expected):
            self.zero(coefficient-target)
        T = lambda f: sp.expand(sum(c*sp.diff(f, q) for q, c in zip(base, coefficients)))
        for j, f in enumerate(forward):
            self.zero(T(f)-int(j == 2))
        self.zero(T(x))
        self.assertEqual(max(sp.Poly(f, x).degree() for f in coefficients[1:]), 3)
        top = tuple(f.coeff(x, 3) for f in coefficients[1:])
        self.assertEqual(top, (0, 0, 1))
        self.zero(sp.diff(v, v)-1)
        for lc in leading:
            self.zero(sp.diff(lc, v))
        for f in inverse:
            self.zero(sp.diff(f, Z, 4))

        eta, U, V = sp.symbols("eta U V")
        initials = tuple(lc*eta**d for lc, d in zip(leading, weights))
        self.zero(H.xreplace(dict(zip(original, initials))))
        triple = sp.Matrix((initials[0], initials[1], initials[3]))
        self.assertNotEqual(sp.expand(triple.jacobian((tau, rho, eta)).det()), 0)
        # XZ-Y³ is primitive linear in Z, hence irreducible. Triple rank3
        # proves the full initial kernel is exactly (XZ-Y³).

        # Exact k=n=rho, ell=0 specializes the coefficient system:
        # f=U³+V, Phi=-f, m=tau, and the selected curve is a cubic graph.
        f, phi = U**3+V, -U**3-V
        selected = {U: v, V: theta}
        self.zero(tau+f.xreplace(selected))  # r*w+f=ell, r=1
        self.zero(phi.xreplace(selected)-tau)
        self.zero(sp.diff(phi.xreplace(selected), v))
        self.assertEqual(self.total_degree(phi, (U, V)), 3)
        self.zero(phi-tau-(-(U**3+V+tau)))
        CU = sp.Integer(1)
        CV = 1-3*v*v
        self.zero(CU*sp.diff(phi, U).xreplace(selected)
                  +CV*sp.diff(phi, V).xreplace(selected)+1)
        self.assertEqual(sp.Poly(H_actual, x).degree(), 2)
        self.zero(sp.diff(H_actual, x, 2)-2*rho)
        self.assertNotEqual(rho, 0)
        # The cusp polynomial itself is not invariant. The actual invariant
        # tau is the polynomial (1+X)W-XH of original weighted degree four.
        max_weight = max(sum(i*d for i, d in zip(powers, weights))
                         for powers, coefficient in sp.Poly(inv_tau, *original).terms())
        self.assertEqual(max_weight, 4)
        self.zero(sp.diff(inv_tau.xreplace(to_base), x))


if __name__ == "__main__":
    unittest.main()
