"""Finite exact controls for all-degree leading normalization.

Actual divided-difference frames with minimal bad degrees m=2,3,4 supply both
polynomial inverse orders, c_m=[u^m]W=E^mW/m!, and sharp/strict weighted
multiplicity controls. Separate elementary coordinate maps verify the two
invertible normalization operations.

The fourth method checks an actual Nagata-type polynomial automorphism and
its inverse, then matches it with separately specified formal Taylor data.
That coefficient data is not called an actual dense frame without an E-action.
The fifth method independently extracts the full-constant formal tails and
Laurent cancellations, and checks the final discriminant algebra only. It
does not prove the all-degree classification or the odd-valuation argument.

Synthetic leading maps are explicitly NOT actual coordinate realizations.
Their finite monomial signatures distinguish a rational leading coefficient
from an algebraic one; a rational non-pure-power binary form also shows that
weighted degree and rationality alone are not the one-point-at-infinity step.
No finite test proves invariant growth, generic first-tail primitivity, or
the universal normalization theorem. No earlier checker or solver is imported.
"""

import math
import unittest

import sympy as sp


class LeadingNormalizationControls(unittest.TestCase):
    def zero(self, expression):
        numerator = sp.fraction(sp.together(expression))[0]
        self.assertEqual(sp.expand(numerator), 0)

    def zeros(self, expressions):
        for expression in expressions:
            self.zero(expression)

    @staticmethod
    def weighted_top(expression, variables, weights):
        terms = sp.Poly(expression, *variables).terms()
        degree = max(sum(i*w for i, w in zip(monomial, weights))
                     for monomial, _ in terms)
        top = sum(coefficient*sp.prod(x**i for x, i in zip(variables, monomial))
                  for monomial, coefficient in terms
                  if sum(i*w for i, w in zip(monomial, weights)) == degree)
        return degree, sp.expand(top)

    def test_actual_inverse_factorials_and_weighted_multiplicity(self):
        u, a, b, v = sp.symbols("u a b v")
        X, Y, Z, W, A = sp.symbols("X Y Z W A")
        original = (X, Y, Z, W)
        gamma = sp.Rational(1, 2)
        for m in (2, 3, 4):
            with self.subTest(bad_degree=m):
                F = lambda t: gamma*t**(m+1)+t+2
                delta = lambda aa, vv, uu: aa+gamma*sum(
                    math.comb(m+1, j)*vv**(m+1-j)*aa**j*uu**(j-1)
                    for j in range(1, m+2))
                forward = (u, v+a*u, a-F(v)+b*u, b+delta(a, v, u))
                xf, yf, zf, wf = forward
                ai = sp.expand(zf-xf*wf+F(yf))
                vi = sp.expand(yf-ai*xf)
                bi = sp.expand(wf-delta(ai, vi, xf))
                self.zeros((xf-u, ai-a, vi-v, bi-b))

                # Independent A records the only reverse residual. Substituting
                # A=Z-XW+F(Y) then gives the full inverse, without denominators.
                a_inverse = Z-X*W+F(Y)
                vv, bb = Y-A*X, W-delta(A, Y-A*X, X)
                reverse = (X, vv+A*X, A-F(vv)+bb*X, bb+delta(A, vv, X))
                self.zeros((reverse[0]-X, reverse[1]-Y,
                            reverse[2]-Z-(A-a_inverse), reverse[3]-W))
                self.zero(sp.Matrix(forward).jacobian((u, a, b, v)).det()-1)
                self.zeros(sp.diff(f, u, 2) for f in forward[:3])
                cm = sp.Poly(wf, u).coeff_monomial(u**m)
                self.zeros((cm-gamma*a**(m+1),
                            sp.diff(wf, u, m)-math.factorial(m)*cm,
                            sp.diff(cm, v)))
                self.assertNotEqual(sp.expand(sp.diff(wf, u, m)-cm), 0)
                self.assertEqual(sp.Poly(wf, u).degree(), m)
                self.assertEqual(sp.Poly(cm, a, b).total_degree(), m+1)
                # Speeds (1,a,b) are dense. A degree-m good shear has leading
                # coefficient of total (a,b)-degree <=m, so cannot cancel cm.
                # Higher-degree good shears have that higher E-degree. Thus
                # these actual examples really have minimum mu=m.
                speeds = sp.Matrix([1, a, b])
                self.zero(sp.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(b)).det()-1)
                Tvalues = (0, -u, 1+u*sp.diff(F(v), v), u*u)
                for coordinate, expected in zip(forward, (0, 0, 0, 1)):
                    self.zero(sum(sp.diff(coordinate, x)*value
                                  for x, value in zip((u, a, b, v), Tvalues))-expected)

                phi = X*W-gamma*Y**(m+1)
                v_inverse = Y-X*a_inverse
                weights = (1, 1, 1, m)
                self.zero(sp.gcd(phi, X)-1)
                for k in (1, 2, 3):
                    sharp = v_inverse**k
                    strict = a_inverse**k
                    sharp_weight, sharp_top = self.weighted_top(sharp, original, weights)
                    strict_weight, strict_top = self.weighted_top(strict, original, weights)
                    self.assertEqual(sharp_weight, (m+2)*k)
                    self.assertEqual(strict_weight, (m+1)*k)
                    self.zeros((sharp_top-X**k*phi**k, strict_top-(-phi)**k))
                    # phi does not divide X, so the displayed multiplicity is
                    # exactly k. Actual T=partial_W lowers source weight by m.
                    d_sharp = sp.diff(sharp, W, k)
                    d_strict = sp.diff(strict, W, k)
                    self.zeros((d_sharp-math.factorial(k)*X**(2*k),
                                d_strict-(-1)**k*math.factorial(k)*X**k))
                    evaluated_sharp = d_sharp.subs(dict(zip(original, forward)),
                                                   simultaneous=True)
                    evaluated_strict = d_strict.subs(dict(zip(original, forward)),
                                                     simultaneous=True)
                    self.assertEqual(sp.Poly(evaluated_sharp, u).degree(), sharp_weight-m*k)
                    self.assertEqual(sp.Poly(evaluated_strict, u).degree(), strict_weight-m*k)
                    self.assertEqual(sharp_weight-(m+2)*k, 0)
                    self.assertLess(strict_weight-(m+2)*k, 0)
                    self.zero(sp.diff(v**k, v, k)-math.factorial(k))
                    self.zero(sp.diff(a**k, v, k))

    def test_elementary_normalization_has_both_inverse_orders(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        G1, G2, G3, H = sp.symbols("G1 G2 G3 H")
        gamma = sp.Rational(1, 2)
        for m in (2, 3, 4):
            with self.subTest(bad_degree=m):
                Q = lambda x, y, z: x**(m-1)*z+y**m
                changed = (X+Y, Y+Z, Z, W+Q(X, Y, Z))
                xx, yy, zz = G1-G2+G3, G2-G3, G3
                inverse = (xx, yy, zz, H-Q(xx, yy, zz))
                new_symbols = (G1, G2, G3, H)
                old_symbols = (X, Y, Z, W)
                self.zeros(f.subs(dict(zip(new_symbols, changed)), simultaneous=True)-x
                           for f, x in zip(inverse, old_symbols))
                self.zeros(f.subs(dict(zip(old_symbols, inverse)), simultaneous=True)-x
                           for f, x in zip(changed, new_symbols))
                self.zero(sp.Matrix(changed).jacobian(old_symbols).det()-1)
                before = xx*H-(gamma*yy**(m+1)+xx*Q(xx, yy, zz))
                self.zero(before.subs(dict(zip(new_symbols, changed)), simultaneous=True)
                          -(X*W-gamma*Y**(m+1)))
                degree, top = self.weighted_top(before, new_symbols, (1, 1, 1, m))
                self.assertEqual(degree, m+1)
                self.zero(top-before)
                self.zero(sp.gcd(xx, gamma*yy**(m+1))-1)
                # This map composes with the actual first-method fixtures.
                # A constant good inverse and a bad shear are polynomial maps,
                # not maps obtained by inverting the first good coordinate.

    def test_synthetic_algebraic_and_rational_leading_boundaries(self):
        X, Y, Z, W, lam, a, b, U, V = sp.symbols("X Y Z W lam a b U V")
        gamma = sp.Rational(1, 2)
        for m in (2, 3, 4):
            with self.subTest(bad_weight=m):
                # Exhaust the finite source monomial space of weight <=m+1.
                # Each leading image is a nonzero scalar times one monomial.
                exponents = []
                for l in range(2):
                    limit = m+1-m*l
                    for i in range(limit+1):
                        for j in range(limit-i+1):
                            for k in range(limit-i-j+1):
                                exponents.append((i, j, k, l))
                rational_signatures = [
                    (i+j+k+m*l, j+(m+1)*l, k) for i, j, k, l in exponents]
                algebraic_signatures = [
                    (i+j+k+m*l, 2*j+l, k) for i, j, k, l in exponents]
                self.assertEqual(len(set(rational_signatures)), len(exponents)-1)
                self.assertEqual(len(set(algebraic_signatures)), len(exponents))
                rational_map = {X: lam, Y: lam*a, Z: lam*b,
                                W: gamma*lam**m*a**(m+1)}
                algebraic_map = {X: lam, Y: lam*a*a, Z: lam*b, W: lam**m*a}
                self.zero((X*W-gamma*Y**(m+1)).subs(rational_map, simultaneous=True))
                algebraic_relation = W*W-X**(2*m-1)*Y
                self.zero(algebraic_relation.subs(algebraic_map, simultaneous=True))
                degree, _ = self.weighted_top(algebraic_relation, (X, Y, Z, W),
                                              (1, 1, 1, m))
                self.assertEqual(degree, 2*m)
                self.assertGreater(degree, m+1)
                # a -> -a fixes C(a^2,b), but not the proposed leading a.
                # T^2-tau is Eisenstein at tau in C(b)[tau][T], so the
                # associated coefficient field is genuinely quadratic.
                # This source-field example is NOT an actual four-frame.
                self.zeros(((a*a).subs(a, -a)-a*a, b.subs(a, -a)-b))
                self.assertNotEqual(a.subs(a, -a), a)

                # Rationality and the correct weight are still weaker than
                # the actual one-point-at-infinity/pure-power conclusion.
                non_power, power = U**m*V, gamma*(2*U-3*V)**(m+1)
                self.zero(sp.hessian(non_power, (U, V)).det()+m*m*U**(2*m-2))
                self.assertNotEqual(sp.expand(sp.hessian(non_power, (U, V)).det()), 0)
                self.zero(sp.hessian(power, (U, V)).det())
                rational_non_power = {X: lam, Y: lam*a, Z: lam*b,
                                      W: lam**m*a**m*b}
                self.zero((X*W-Y**m*Z).subs(rational_non_power, simultaneous=True))
                # No polynomial inverse is asserted for this last leading map.

    def test_nagata_inverse_and_independent_formal_tail_extraction(self):
        X, Y, Z, R, W, r, J = sp.symbols("X Y Z R W r J")
        kappa, a, alpha = sp.symbols("kappa a alpha", nonzero=True)
        # These are constant parameters. Division by alpha is division by a
        # nonzero complex constant, never localization at a source coordinate.
        H = X*W+kappa*R*R
        r_forward = R+X*H/alpha
        J_forward = W-2*kappa*R*H/alpha-kappa*X*H*H/alpha**2
        H_forward = sp.expand(X*J_forward+kappa*r_forward**2)
        self.zero(H_forward-H)
        self.zeros((r_forward-X*H_forward/alpha-R,
                    J_forward+2*kappa*r_forward*H_forward/alpha
                    -kappa*X*H_forward**2/alpha**2-W))

        H_inverse = X*J+kappa*r*r
        R_inverse = r-X*H_inverse/alpha
        W_inverse = J+2*kappa*r*H_inverse/alpha-kappa*X*H_inverse**2/alpha**2
        H_back = sp.expand(X*W_inverse+kappa*R_inverse**2)
        self.zero(H_back-H_inverse)
        self.zeros((R_inverse+X*H_back/alpha-r,
                    W_inverse-2*kappa*R_inverse*H_back/alpha
                    -kappa*X*H_back**2/alpha**2-J))
        self.zero(sp.Matrix([r_forward, J_forward]).jacobian((R, W)).det()-1)
        self.zeros(((Z-a*Y**2)+a*Y**2-Z, (R+a*Y**2)-a*Y**2-R))
        # X,Y are fixed. Together with R=Z-aY^2, these are actual two-sided
        # four-variable polynomial inverses for each allowed constant triple.

        tau, rho, U, V = sp.symbols("tau rho U V")
        fs = {3: -kappa*a*a*tau**4, 2: 2*kappa*a*tau*tau*rho,
              1: -kappa*rho*rho, 0: a*alpha*tau*tau}

        def homogeneous(f, degree):
            return sp.expand(sum(
                sp.diff(f, tau, i, rho, degree-i)*U**i*V**(degree-i)
                / (math.factorial(i)*math.factorial(degree-i))
                for i in range(degree+1)))

        f_minus = -alpha*rho
        first = -sum(homogeneous(fs[j], j+1) for j in range(4))
        phi = sp.expand(first-f_minus)
        psi = -sum(homogeneous(fs[j], j+2) for j in range(4))-homogeneous(f_minus, 1)
        self.zeros((phi-(kappa*(V-a*U*U)**2-2*a*alpha*tau*U+alpha*rho),
                    psi-alpha*(V-a*U*U)))
        # The following is a rational coefficient chart, not a separately
        # inverse-certified dense sliced frame. Its normalized parameter is
        # v=alpha*r, so N'=alpha^{-1}partial_r in this control.
        y = (kappa*r*r+alpha*rho)/(2*a*alpha*tau)
        z = a*y*y+r
        evaluate = lambda f: f.subs({U: y, V: z}, simultaneous=True)
        self.zeros((evaluate(first)-f_minus, evaluate(phi),
                    evaluate(psi)-alpha*r,
                    sp.diff(evaluate(psi), r)/alpha-1))
        W_chart = sum(
            X**j*sum(evaluate(homogeneous(fs[k], k-j)) for k in range(j, 4))
            for j in range(4))
        Y_chart, Z_chart = y+tau*X, z+rho*X
        R_chart = Z_chart-a*Y_chart**2
        H_chart = X*W_chart+kappa*R_chart**2
        self.zeros((H_chart-(kappa*r*r+a*alpha*tau*tau*X),
                    R_chart+X*H_chart/alpha-r))
        # This verifies extraction by the same polynomial r-coordinate of the
        # actual Nagata map, without inferring realizability of arbitrary jets.

    def test_general_constant_tails_laurent_cancellation_and_discriminant(self):
        tau, rho, U, V, eps, zeta = sp.symbols("tau rho U V eps zeta")
        kappa, a, alpha = sp.symbols("kappa a alpha", nonzero=True)
        c, b0, d0, l0, n0 = sp.symbols("c b0 d0 l0 n0")
        # All eight displayed parameters are constants. These are formal
        # coefficient data, not an independently realized dense E-frame.
        fs = {3: -kappa*a*a*tau**4}
        fs[2] = c*fs[3]-2*kappa*a*b0*tau**3+2*kappa*a*tau*tau*rho
        fs[1] = (c*fs[2]-kappa*(b0*b0+2*a*d0)*tau*tau
                 +2*kappa*b0*tau*rho-kappa*rho*rho)
        fs[0] = (c*fs[1]+a*alpha*tau*tau
                 -(2*kappa*b0*d0+l0)*tau+2*kappa*d0*rho)
        b = 2*a*c*tau+b0
        d = a*c*c*tau*tau+c*b0*tau-c*rho+d0
        ell = -2*a*alpha*tau+l0
        n = (alpha*rho-2*a*c*alpha*tau*tau
             +(c*l0-alpha*b0)*tau+n0)
        f_minus = -kappa*d*d-n

        def homogeneous(f, degree):
            return sp.expand(sum(
                sp.diff(f, tau, i, rho, degree-i)*U**i*V**(degree-i)
                / (math.factorial(i)*math.factorial(degree-i))
                for i in range(degree+1)))

        first = -sum(homogeneous(fs[j], j+1) for j in range(4))
        phi = sp.expand(first-f_minus)
        psi = sp.expand(-sum(homogeneous(fs[j], j+2) for j in range(4))
                        -homogeneous(f_minus, 1))
        residual = V-a*U*U-b*U-d
        expected_phi = kappa*residual**2+ell*U+n
        beta = alpha*d+c*f_minus
        self.zeros((phi-expected_phi, psi-c*phi-alpha*residual-beta,
                    psi.subs({U: 0, V: 0}),
                    beta-alpha*d+c*(kappa*d*d+n)))
        # This includes the c*Phi term, which is absent in the simplified
        # method above. Omitting it would give the wrong quartic coefficient.
        self.zeros((sp.Poly(phi, U, V).coeff_monomial(U**4)-kappa*a*a,
                    sp.Poly(psi, U, V).coeff_monomial(U**4)-c*kappa*a*a))

        # Construct the common formal Laurent source directly, without
        # substituting a putative parameterization of a selected component.
        X, Y, Z = 1/eps, tau/eps, rho/eps
        W = sum(fs[j]/eps**j for j in range(4))+f_minus*eps+zeta*eps**2
        x = X-c
        R0 = Z-a*Y*Y-b0*Y-d0
        H = sp.expand(x*W+kappa*R0*R0+l0*Y+n0)
        A = a*alpha*tau*tau
        B = c*A+alpha*b0*tau-alpha*rho
        expected_H = A/eps+B+(zeta-c*f_minus)*eps-c*zeta*eps**2
        # Compare cleared polynomial numerators, not generic rational gcds.
        self.assertEqual(sp.expand(eps**4*(H-expected_H)), 0)
        H_shifted = sp.Poly(sp.expand(eps**4*H), eps)
        self.zeros(H_shifted.coeff_monomial(eps**j) for j in range(3))
        self.zeros((H_shifted.coeff_monomial(eps**3)-A,
                    H_shifted.coeff_monomial(eps**4)-B))
        I = sp.expand(x*H+alpha*R0)
        expected_I = (zeta-c*f_minus-c*B-alpha*d0
                      +eps*(-2*c*zeta+c*c*f_minus)+eps**2*c*c*zeta)
        self.assertEqual(sp.expand(eps**5*(I-expected_I)), 0)
        I_shifted = sp.Poly(sp.expand(eps**5*I), eps)
        self.zeros(I_shifted.coeff_monomial(eps**j) for j in range(5))
        self.zero(I_shifted.coeff_monomial(eps**5)
                  -(zeta-c*f_minus-c*B-alpha*d0))
        self.zero(sp.diff(I_shifted.coeff_monomial(eps**5), zeta)-1)

        # Pure coefficient algebra for the final squared-discriminant gate.
        # If the preceding actual-coordinate argument supplies the quadratic
        # constraint, this identity yields a square equal to a linear-J
        # factor times s^2. The UFD odd-valuation contradiction is a written
        # universal argument, not inferred from these finite identities.
        s, t, J = sp.symbols("s t J")
        constraint = alpha*a*t*t-l0*s*t-J*s*s
        linear_factor = l0*l0+4*alpha*a*J
        difference = (2*alpha*a*t-l0*s)**2-linear_factor*s*s
        self.zero(difference-4*alpha*a*constraint)
        self.zero(difference.subs(J, (alpha*a*t*t-l0*s*t)/s**2))
        self.assertEqual(sp.Poly(linear_factor, J).degree(), 1)
        self.zero(sp.diff(linear_factor, J)-4*alpha*a)
        self.assertNotEqual(sp.diff(linear_factor, J), 0)


if __name__ == "__main__":
    unittest.main()
