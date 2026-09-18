"""Finite exact controls for the conditional weight-four cusp gate164.

The formal ansatz does not supply an invariant. Critical-point jets check
the displayed Hessian algebra, not the global slice obstruction itself.
Polynomial inverse identities are independent of any generic coefficient
specialization. The last method separates abstract algebraic coefficient
controls from actual ratio data and tests the need for regular k. No old
checker, solver, or proof dependency is imported.
"""

import unittest

import sympy as sp


def cubic_polynomial(X, Y, coefficients):
    return sum(coefficient*X**i*Y**j for coefficient, (i, j) in zip(
        coefficients, ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1),
                       (0, 2), (3, 0), (2, 1), (1, 2), (0, 3))
    ))


class CuspWeightFourControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_full_ansatz_cubic_time_and_rho_constraints(self):
        X, y, theta, z, sigma, w = sp.symbols("X y theta z sigma w")
        tau, rho, k, kt, r, n, k0 = sp.symbols("tau rho k kt r n k0")
        mu, nu, alpha, beta, gamma = sp.symbols("mu nu alpha beta gamma")
        delta, epsilon, zeta = sp.symbols("delta epsilon zeta")
        coefficients = sp.symbols("q0:10")
        Y = y+tau*X
        Z = z+sigma*X+tau**3*X**2
        W = w+theta*X+rho*X**2
        H = -y**3+(kt*y+r*theta+n)*X+k*X**2
        Q = cubic_polynomial(X, Y, coefficients)
        ansatz = sp.expand(
            (mu*X+nu*Y)*H+(alpha*X+beta*Y+gamma)*Z
            +(delta*X+epsilon*Y+zeta)*W+Q
        )
        Q3 = sum(coefficients[6+i]*tau**i for i in range(4))
        top = ansatz.coeff(X, 3)
        expected = ((mu+nu*tau)*k+(alpha+beta*tau)*tau**3
                    +(delta+epsilon*tau)*rho+Q3)
        self.zero(top-expected)
        self.assertEqual(sp.degree(ansatz, X), 3)
        # Intercept/coefficient jets can move in rho without changing this
        # extracted term. Only k_rho=r and rho_rho=1 survive at X^3.
        yr, tr, zr, sr, wr, ktr, rr, nr = sp.symbols("yr tr zr sr wr ktr rr nr")
        rho_jet = sp.diff(ansatz, rho)+sum(
            velocity*sp.diff(ansatz, coordinate)
            for coordinate, velocity in ((y, yr), (theta, tr), (z, zr),
                (sigma, sr), (w, wr), (k, r), (kt, ktr), (r, rr), (n, nr))
        )
        self.zero(sp.expand(rho_jet).coeff(X, 3)-(mu+nu*tau)*r-delta-epsilon*tau)

        c1 = sp.Symbol("c1", nonzero=True)
        c0 = sp.Symbol("c0")
        denominator = c1*tau+c0
        cleared = sp.expand(mu+nu*tau+(delta+epsilon*tau)*denominator)
        self.zero(cleared.coeff(tau, 2)-epsilon*c1)
        self.zero(cleared.coeff(tau, 1)-nu-delta*c1-epsilon*c0)
        self.zero(cleared.coeff(tau, 0)-mu-delta*c0)
        self.zero(cleared.subs({epsilon: 0, mu: -delta*c0, nu: -delta*c1}))
        # After dividing by the nonzero constant delta, the k0 condition is
        # a polynomial numerator identity. No field algebraicity is inferred.
        normalized_numerator = (
            (-c0-c1*tau)*(rho+denominator*k0)
            +denominator*((alpha+beta*tau)*tau**3+rho+Q3)
        )
        necessary = -denominator*k0+(alpha+beta*tau)*tau**3+Q3
        self.zero(normalized_numerator-denominator*necessary)
        self.assertLessEqual(sp.degree((alpha+beta*tau)*tau**3+Q3, tau), 4)

    def test_critical_hessian_and_both_polynomial_inverse_branches(self):
        X, Y, Z, W, x, I, J1, J = sp.symbols("X Y Z W x I J1 J")
        c0, alpha, zeta = sp.symbols("c0 alpha zeta")
        c1, ell = sp.symbols("c1 ell", nonzero=True)
        kappa = sp.Symbol("kappa", nonzero=True)
        coefficients = sp.symbols("q0:10")
        Q = cubic_polynomial(X, Y, coefficients)
        P = (c0*X+c1*Y)*Y**3+Q
        beta = ell-c1*zeta
        gamma0 = kappa+alpha*zeta+c0*zeta**2
        CZ = -c0*X**2-c1*X*Y+alpha*X+beta*Y+gamma0
        candidate = CZ*Z+(X+zeta)*W+P
        critical_X, critical_Y = -zeta, -kappa/ell
        self.zero(CZ.subs(X, critical_X)-ell*Y-kappa)
        self.zero(ell*CZ.subs({X: critical_X, Y: critical_Y}))
        self.zero(sp.diff(candidate, W).subs(X, critical_X))

        # The Hessian determinant ell^2 is AT X=-zeta, not the unrestricted
        # determinant in the original variables. Its upper block is arbitrary.
        hessian = sp.hessian(candidate, (X, Y, Z, W)).subs(X, -zeta)
        self.zero(hessian[1, 2]-ell)
        self.assertEqual(hessian[0, 3], 1)
        self.assertEqual(hessian[1, 3], 0)
        self.assertEqual(hessian[2:4, 2:4], sp.zeros(2))
        M11, M12, M22, CX = sp.symbols("M11 M12 M22 CX")
        block = sp.Matrix([[M11, M12, CX, 1], [M12, M22, ell, 0],
                           [CX, ell, 0, 0], [1, 0, 0, 0]])
        self.zero(block.det()-ell**2)
        PX, PY = sp.symbols("PX PY")
        critical_Z = -PY/ell
        critical_W = -CX*critical_Z-PX
        self.zero(ell*(ell*critical_Z+PY))
        self.zero(ell*(CX*critical_Z+critical_W+PX))
        # At zero gradient, the product rule for E(I) has Hess(I)*E as
        # its first jet; the derivative-of-E term multiplies zero gradient.
        e = sp.Matrix(sp.symbols("e0:4"))
        e_jets = sp.Matrix(4, 4, sp.symbols("ej0:16"))
        self.assertEqual(block*e+e_jets.T*sp.zeros(4, 1), block*e)

        # The surviving ell=0 branch has an explicit whole-ring inverse.
        D = -c0*X-c1*Y+alpha+c0*zeta
        CZ0 = CZ.subs(ell, 0)
        self.zero(CZ0-(X+zeta)*D-kappa)
        invariant = CZ0*Z+(X+zeta)*W+P
        companion = W+D*Z
        inverse_Z = (I-(X+zeta)*J-P)/kappa
        inverse_W = J-D*inverse_Z
        to_targets = {Z: inverse_Z, W: inverse_W}
        self.zero(kappa*(invariant.xreplace(to_targets)-I))
        self.zero(kappa*(companion.xreplace(to_targets)-J))
        self.zero(kappa*(inverse_Z.xreplace({I: invariant, J: companion})-Z))
        self.zero(kappa*(inverse_W.xreplace({I: invariant, J: companion})-W))

        # kappa=0 is a separate polynomial-shear identity. It is excluded
        # under the actual invariant hypotheses by the written normality
        # argument, not by a finite computation or a division by kappa.
        shifted_P = sp.expand(P.subs(X, x-zeta))
        pY = sp.expand(P.subs(X, -zeta))
        quotient, remainder = sp.div(shifted_P-pY, x, x)
        self.zero(remainder)
        self.zero(shifted_P-x*quotient-pY)
        self.assertEqual(sp.degree(pY, Y), 4)
        self.zero(sp.Poly(pY, Y).LC()-c1)
        D_shifted = D.subs(X, x-zeta)
        shear_J1 = W+D_shifted*Z+quotient
        inverse_shear_W = J1-quotient-D_shifted*Z
        self.zero(shear_J1.subs(W, inverse_shear_W)-J1)
        self.zero(inverse_shear_W.subs(J1, shear_J1)-W)
        kappa_zero_I = ((X+zeta)*(W+D*Z)+P).subs(X, x-zeta)
        self.zero(kappa_zero_I-x*shear_J1-pY)

    def test_specialization_coefficient_field_and_regularity_boundary(self):
        # Abstract polynomial ring C[z,h], NOT a supplied actual cusp frame.
        # tau=z^2, rho=z+z^2 h are independent, eta=z is algebraic over
        # C(tau), and k=h is regular. The coefficient-field argument in the
        # note is not replaced by these two-generator arithmetic identities.
        z, h = sp.symbols("z h")
        tau, rho, chi, k, eta = z**2, z+z**2*h, z**2, h, z
        self.zero(rho-chi*k-eta)
        ratio_jacobian = sp.Matrix([tau, rho]).jacobian((z, h)).det()
        self.zero(ratio_jacobian-2*z**3)
        self.assertNotEqual(ratio_jacobian, 0)

        def d_rho(expression):
            return sp.diff(expression, h)/z**2

        def d_tau(expression):
            return (sp.diff(expression, z)/(2*z)
                    -(1+2*z*h)*sp.diff(expression, h)/(2*z**3))

        self.zero(z**2*d_rho(tau))
        self.zero(z**2*(d_rho(rho)-1))
        self.zero(2*z**3*(d_tau(tau)-1))
        self.zero(2*z**3*d_tau(rho))
        self.zero(z**2*(d_rho(k)-1/chi))
        self.zero(z**2*d_rho(eta))
        self.zero(2*z*d_tau(eta)-1)
        self.zero(eta**2-tau)

        T, V = sp.symbols("T V")
        Q = V**2-T
        redundant_Q = T**3*Q
        self.zero(Q.xreplace({T: tau, V: eta}))
        self.zero(redundant_Q.xreplace({T: tau, V: eta}))
        self.assertEqual(redundant_Q.subs(T, 0), 0)
        common_order = min(e[0] for e, c in sp.Poly(redundant_Q, T).terms())
        self.assertEqual(common_order, 3)
        normalized = sum(c*T**(e[0]-common_order)
                         for e, c in sp.Poly(redundant_Q, T).terms())
        self.zero(normalized-Q)
        q0 = normalized.subs(T, 0)
        self.assertEqual(q0, V**2)
        self.zero(q0.subs(V, rho)-chi*(1+z*h)**2)
        self.zero(tau.subs(z, 0))
        self.zero(rho.subs(z, 0))
        # The repeated root of q0 and the repeated divisor g=z^2 are kept;
        # this example gives no universal reducedness or multiplicity bound.

        # This rational involution fixes both base ratios but changes eta.
        # The standard nonsquare/field-degree argument remains a written
        # argument, not a general theorem inferred from a finite test grid.
        deck = {z: -z, h: h+2/z}
        self.zero(z*(tau.xreplace(deck)-tau))
        self.zero(z*(rho.xreplace(deck)-rho))
        self.zero(eta.xreplace(deck)+eta)
        self.assertNotEqual(eta.xreplace(deck), eta)
        for coordinate in (z, h):
            self.zero(z*(coordinate.xreplace(deck).xreplace(deck)-coordinate))

        # Actual163 ratio data, without rerunning its earlier inverse tests:
        # a=1, g=t, rho=t*q, k=q, eta=0, and Q(T,V)=V.
        t, q = sp.symbols("t q")
        actual_a, actual_b, actual_d, actual_k = sp.S.One, t, t*q, q
        actual_chi = actual_b/actual_a
        actual_rho = actual_d/actual_a**2
        self.zero(actual_rho-actual_chi*actual_k)
        self.zero(actual_rho.subs(t, 0))
        quotient, remainder = sp.div(actual_rho, actual_a*actual_chi, t)
        self.zero(quotient-q)
        self.zero(remainder)

        # Removing regularity invalidates contraction: in C[t,q], let
        # rho=q, chi=g=t, eta=0 and k=q/t. The field equations still hold,
        # but Q(0,rho)=q is not in the polynomial ideal (t).
        nonregular_k = q/t
        self.zero(t*(q-t*nonregular_k))
        self.zero(t*sp.diff(nonregular_k, q)-1)
        quotient, remainder = sp.div(q, t, t)
        self.zero(quotient)
        self.assertEqual(remainder, q)
        self.assertNotEqual(remainder, 0)
        # This last field-only boundary violates k in S_a and is expressly
        # not an actual quartic chart or a counterexample to the164 theorem.


if __name__ == "__main__":
    unittest.main()
