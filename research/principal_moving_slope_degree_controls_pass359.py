"""Standalone finite exact controls for retained 353, 354, and 357 identities.

The checks rebuild normalized support from literal potentials, not retained
checker imports. They do not certify whole-ring return, field constants,
universal degree-case exhaustion, projective geometry, or recognition.
Coefficient-field transformations are never declared ambient maps here.
"""

import unittest

import sympy as sp


def integrate_formal(expression, variable):
    return sp.Add(*(
        coefficient * variable**(powers[0]+1)/(powers[0]+1)
        for powers, coefficient in sp.Poly(sp.expand(expression), variable).terms()
    ))


def top_part(expression, variables, degree):
    return sp.Add(*(
        coefficient * sp.prod(z**power for z, power in zip(variables, powers))
        for powers, coefficient in sp.Poly(sp.expand(expression), *variables).terms()
        if sum(powers) == degree
    ))


def normalized_support(x, p, q, b, bp, kappa, A, C, ess, rhos):
    r11, r20, r10, r01, r00 = rhos
    return (-2*b*p**2*x + bp*p**2*q/2 + kappa*p**3
            + b*x*q + (A-2*C)*x*p - ess*q**2/2
            + r11*p*q + r20*p**2 + r10*p + r01*q + r00)


class MovingSlopeDegreeControls(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_normalized_support_and_equal_degree_shear(self):
        t, s, U, P, V, x, p, q, q0 = sp.symbols("t s U P V x p q q0")
        B = sp.Function("B")(t)
        f = sp.Function("f")(t)
        ell = sp.Function("ell")(t, s)
        h = sp.Function("h")(t, s)
        n = B*s+f
        u = sp.diff(n, t)
        b, bp = sp.diff(B, t), sp.diff(B, t, 2)
        wf = ell-2*P*U-u*P-B*V
        H = (U**2+u*U+B*wf+sp.diff(n, t, 2)*P**2/2+b*P*V
             - sp.diff(ell, t)*P-sp.diff(ell, s)*V)
        HU, HP, HV = [sp.diff(H, z) for z in (U, P, V)]
        QU = HP-2*P*HV+B*HU
        QP = sp.diff(H, t)-sp.diff(h, t)-(2*U+u)*HV+B*HP
        QV = sp.diff(H, s)-sp.diff(h, s)
        Q = (integrate_formal(QU, U)+integrate_formal(QP.subs(U, 0), P)
             + integrate_formal(QV.subs({U: 0, P: 0}), V))
        for variable, gradient in zip((U, P, V), (QU, QP, QV)):
            self.assertZero(sp.diff(Q, variable)-gradient)

        A = sp.diff(n, t, 2)/2-B**2
        C = sp.diff(ell, s)+B**2
        T = sp.diff(ell, t)
        ess = sp.diff(ell, s, 2)
        old_P = p+C/b
        old_V = q-A*old_P/b-A*C/b**2+T/b
        old_U = x-u/2+B*old_P
        phi = sp.expand((Q-q0).subs({U: old_U, P: old_P, V: old_V}, simultaneous=True))
        poly = sp.Poly(phi, x, p, q)
        kappa = sp.diff(n, t, 3)/6-2*B*b-A*bp/(2*b)
        r11 = (A*ess+C*bp)/b-sp.diff(ell, t, s)
        r20 = (-A**2*ess+4*A*B*b**2-4*A*C*bp
               + 2*A*b*sp.diff(ell, t, s)-8*B*C*b**2
               + C*b*sp.diff(n, t, 3)+T*b*bp-b**2*sp.diff(ell, t, 2))/(2*b**2)
        for monomial, value in ((p*q, r11), (p**2, r20)):
            self.assertZero(poly.coeff_monomial(monomial)-value)
        rhos = (r11, r20, poly.coeff_monomial(p),
                poly.coeff_monomial(q), poly.coeff_monomial(1))
        self.assertZero(phi-normalized_support(x, p, q, b, bp, kappa, A, C, ess, rhos))
        self.assertEqual(poly.total_degree(), 3)
        self.assertZero(poly.coeff_monomial(x*p**2)+2*b)
        self.assertZero(poly.coeff_monomial(x*q)-b)

        # Test the shear on independent coefficient symbols, retaining all lower terms.
        bb, bbt, lam, kap, aa, cc, ee, delta = sp.symbols("bb bbt lam kap aa cc ee delta")
        rhos0 = sp.symbols("r11 r20 r10 r01 r00")
        x1, q1 = sp.symbols("x1 q1")
        original = normalized_support(x, p, q, bb, bbt, kap, aa, cc, ee, rhos0)
        inverse = {x: x1+lam*p, q: q1-2*lam*x1/bb-lam**2*p/bb}
        self.assertZero((x**2+bb*p*q).subs(inverse, simultaneous=True)-(x1**2+bb*p*q1))
        transformed = sp.expand(original.subs(inverse, simultaneous=True))
        reduced = sp.rem(transformed, x1**2+bb*p*q1-delta, x1)
        K = -2*bb-bbt*lam/bb
        Gamma = kap-2*bb*lam-bbt*lam**2/(2*bb)
        self.assertZero(top_part(reduced, (x1, p, q1), 3)
                        - (K*p**2*x1+bbt*p**2*q1/2+Gamma*p**3))
        resonance = {lam: -2*bb**2/bbt, kap: -2*bb**3/bbt}
        self.assertZero(K.subs(resonance, simultaneous=True))
        self.assertZero(Gamma.subs(resonance, simultaneous=True))
        wrong_inverse = {x: x1+lam*p, q: q1-2*lam*x1/bb+lam**2*p/bb}
        wrong = (x**2+bb*p*q).subs(wrong_inverse, simultaneous=True)-(x1**2+bb*p*q1)
        self.assertZero(wrong-2*lam**2*p**2)
        self.assertNotEqual(sp.cancel(wrong), 0)

    def test_generic_357_odd_identity_and_nonzero_top(self):
        p, w, alpha, delta, d, b, bp = sp.symbols("p w alpha delta d b bp")
        e2, e1, e0, f1, f0 = sp.symbols("e2 e1 e0 f1 f0")
        A, C, kappa = sp.symbols("A C kappa")
        rhos = sp.symbols("r11 r20 r10 r01 r00")
        r11, r20, r10, r01, r00 = rhos
        E = e2*p**2+e1*p+e0
        F = f1*p+f0
        u = p/alpha+delta
        x = E+w*F
        qe = (d-E**2-u*F**2)/(b*p)
        qo = -2*E*F/(b*p)
        q = qe+w*qo
        phi = normalized_support(x, p, q, b, bp, kappa, A, C, 0, rhos)
        reduced = sp.rem(sp.expand(phi), w**2-u, w)
        odd = sp.Poly(reduced, w).coeff_monomial(w)
        N = (d-3*E**2-u*F**2-bp*p**2*E/b-2*b*p**3
             + (A-2*C)*p**2-2*r11*p*E/b-2*r01*E/b)
        self.assertZero(odd-F*N/p)
        top = sp.Poly(sp.expand(N), p).coeff_monomial(p**4)
        self.assertZero(top+3*e2**2+bp*e2/b)
        self.assertZero(top.subs(e2, -bp/(2*b))+bp**2/(4*b**2))
        self.assertNotEqual(sp.cancel(top.subs(e2, -bp/(2*b))), 0)
        # Both allowed nonzero odd modes are retained, with no division by f0 or f1.
        self.assertZero((odd-F*N/p).subs(f1, 0))
        self.assertZero((odd-F*N/p).subs(f0, 0))
        self.assertZero(sp.rem(sp.expand(x**2+b*p*q-d), w**2-u, w))
        # Missing one E^2 contribution from b*x*q is a false cancellation.
        wrong_N = N+E**2
        self.assertNotEqual(sp.cancel(odd-F*wrong_N/p), 0)
        # F=0 is the purely even boundary, not an admissible whole-line return.
        self.assertZero(odd.subs({f0: 0, f1: 0}))
        self.assertZero(q.subs({f0: 0, f1: 0})-(d-E**2)/(b*p))

    def test_353_all_X_monic_specialization_polynomial(self):
        X, P, t, s, B, b, alpha = sp.symbols("X P t s B b alpha")
        j, k0, v2, v1, v0, n, nt, ell = sp.symbols("j k0 v2 v1 v0 n nt ell")
        v3 = -alpha**2/b
        y = alpha*P**2+j*P+k0
        theta = v3*P**3+v2*P**2+v1*P+v0
        Y = y+P*X+t*X**2
        Z = 2*t*y+P**2+theta+n+(2*t*P+s)*X+t**2*X**2
        W = ell-2*P*y-nt*P-B*theta+theta*X+s*X**2
        KX = X-B+2*b/alpha
        TX = sp.expand(W-KX*Z)
        self.assertZero(sp.Poly(TX, P).coeff_monomial(P**3))
        self.assertLessEqual(sp.Poly(TX, P).degree(), 2)
        T2 = sp.Poly(TX, P).coeff_monomial(P**2)
        self.assertZero(T2-(-2*j-2*b*v2/alpha-KX*(1+2*t*alpha)))
        combination = sp.expand(alpha*TX-T2*Y)
        linear = sp.Poly(combination, P).coeff_monomial(P)
        target = -alpha*(2*k0+nt)-2*b*v1+(2*j+2*b*v2/alpha+KX)*(j+X)
        self.assertZero(linear-target)
        self.assertLessEqual(sp.Poly(combination, P).degree(), 1)
        self.assertEqual(sp.Poly(linear, X).degree(), 2)
        self.assertEqual(sp.Poly(linear, X).LC(), 1)
        self.assertZero(sp.Poly(Y, P).coeff_monomial(P**2)-alpha)
        self.assertZero(sp.Poly(Z, P).coeff_monomial(P**3)+alpha**2/b)
        # The missing 2b/alpha term leaves an exact nonzero cubic.
        wrong = sp.expand(W-(X-B)*Z)
        self.assertZero(sp.Poly(wrong, P).coeff_monomial(P**3)+2*alpha)
        self.assertNotEqual(sp.Poly(wrong, P).coeff_monomial(P**3), 0)

    def test_353_two_exact_B_f_families_and_fixed_s_derivatives(self):
        T, s = sp.symbols("T s")
        j, B0, beta, kappa, rho, f1, f0, pole = sp.symbols("j B0 beta kappa rho f1 f0 pole")
        families = (
            (beta*T+B0,
             2*beta*j*T**3+(2*B0*j-j**2-beta*kappa)*T**2+f1*T+f0),
            (B0+pole/T,
             (-j**2+2*B0*j)*T**2-pole*rho/T+f1*T+f0),
        )
        s_curve = kappa*T-2*j*T**2+rho
        c = kappa-4*T*j
        for B, f in families:
            b = sp.diff(B, T)
            bp = sp.diff(B, T, 2)
            a = j-B
            n = B*s+f
            # Differentiate at fixed original s before applying its transported identity.
            ntt = sp.diff(n, T, 2).subs(s, s_curve)
            nttt = sp.diff(n, T, 3).subs(s, s_curve)
            self.assertZero(b*c+a**2+ntt/2-B**2)
            self.assertZero(nttt/6-2*B*b-2*b*a+bp*c/2)
            coefficient_identity = (j**2-(2*B+4*T*b+T**2*bp)*j
                                    +(b+T*bp/2)*kappa+bp*rho/2+sp.diff(f, T, 2)/2)
            self.assertZero(coefficient_identity)
            self.assertZero(coefficient_identity.subs(j, 0))
            self.assertZero(coefficient_identity.subs(rho, 0))
            wrong_ntt = sp.diff(n.subs(s, s_curve), T, 2)
            self.assertZero(wrong_ntt-ntt-(2*b*c-4*B*j))
            self.assertNotEqual(sp.cancel(wrong_ntt-ntt), 0)

        B, f = families[1]
        b, bp = sp.diff(B, T), sp.diff(B, T, 2)
        self.assertZero(2*B+4*T*b+T**2*bp-2*B0)
        self.assertZero(b+T*bp/2)
        self.assertZero(bp/2-pole/T**3)
        wrong_f = f+2*pole*rho/T
        wrong_identity = (j**2-(2*B+4*T*b+T**2*bp)*j
                          +(b+T*bp/2)*kappa+bp*rho/2+sp.diff(wrong_f, T, 2)/2)
        self.assertZero(wrong_identity-2*pole*rho/T**3)
        self.assertNotEqual(sp.cancel(wrong_identity), 0)


if __name__ == "__main__":
    unittest.main()
