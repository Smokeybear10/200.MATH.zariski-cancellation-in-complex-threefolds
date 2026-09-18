"""Bounded exact controls for the quadratic extra-factor exclusion169.

All coefficient jets and polynomial pairs below are formal controls, not
actual four-coordinate cusp frames.  The written proof, not these finite
checks, supplies coefficient-field polynomiality, exact constants, the
universal residue-field lemma and its actual-field-return contradiction.
No old solver or checker is imported.  Root executes after source review.
"""

import unittest

import sympy as sp


class QuadraticExtraFactorControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_potential_graph_coefficients_and_reciprocal_ode(self):
        U, V, rho = sp.symbols("U V rho")
        r, rt, rtt, rttt = sp.symbols("r rt rtt rttt")
        kap, kapt, kaptt = sp.symbols("kap kapt kaptt")
        s, st, stt, n0t, n0tt, k0tt, k0ttt = sp.symbols(
            "s st stt n0t n0tt k0tt k0ttt"
        )
        ec = sp.symbols("ec:4")
        ect = sp.symbols("ect:4")
        ell = sum(ec[i]*rho**i for i in range(4))
        ellt = sum(ect[i]*rho**i for i in range(4))
        nr = 2*kap*rho+s
        nt = kapt*rho**2+st*rho+n0t
        ntt = kaptt*rho**2+stt*rho+n0tt
        ntr = 2*kapt*rho+st
        ktt = rtt*rho+k0tt
        kttt = rttt*rho+k0ttt
        f = U**3+ktt*U**2/2+(rt*U+nr)*V+nt*U
        # Literal H3(k)+H2(n), with factorials kept independent of f.
        H3k = kttt*U**3/6+rtt*U**2*V/2
        H2n = ntt*U**2/2+ntr*U*V+kap*V**2
        Phi = (rt*U+nr)*(ell-f)/r+H3k+H2n-ellt*U-sp.diff(ell, rho)*V
        coefficients = sp.Poly(sp.expand(Phi), U, V)
        Delta = rtt/2-rt**2/r
        self.zero(coefficients.coeff_monomial(U**4)+rt/r)
        self.zero(coefficients.coeff_monomial(V**2)-kap)
        self.zero(coefficients.coeff_monomial(U**2*V)-Delta)
        self.zero(coefficients.coeff_monomial(U*V)-(ntr-2*rt*nr/r))
        self.zero(coefficients.coeff_monomial(V)+nr**2/r+sp.diff(ell, rho))
        C2 = ntt/2-rt*nt/r-nr*ktt/(2*r)
        self.zero(coefficients.coeff_monomial(U**2)-C2)
        self.zero(sp.Poly(C2, rho).coeff_monomial(rho**2)
                  -(kaptt/2-rt*kapt/r-kap*rtt/r))

        p2, alpha, b, d2, e, d, lam = sp.symbols("p2 alpha b d2 e d lam")
        p2t, alphat, bt, d2t, et, dt = sp.symbols("p2t alphat bt d2t et dt")
        p1 = alpha*rho+b
        p0 = d2*rho**2+e*rho+d
        P = p2*U**2+p1*U+p0
        graph_potential = lam*(V-P)+kap*(V-P)**2
        factor_coefficients = sp.Poly(sp.expand(graph_potential), U, V)
        self.zero(factor_coefficients.coeff_monomial(U**2)
                  -(kap*(p1**2+2*p2*p0)-lam*p2))
        self.zero(factor_coefficients.coeff_monomial(V)-(lam-2*kap*p0))
        Pt = p2t*U**2+(alphat*rho+bt)*U+d2t*rho**2+et*rho+dt
        S = (Pt+sp.diff(P, U)*sp.diff(P, rho)
             +((rt*U+nr)*sp.diff(P, U)+3*U**2+ktt*U+rt*P+nt)/r)
        Scoeff = sp.Poly(sp.expand(S), U)
        self.zero(Scoeff.coeff_monomial(U**2)
                  -(p2t+2*alpha*p2+3*rt*p2/r+3/r))
        self.zero(sp.Poly(Scoeff.coeff_monomial(U), rho).coeff_monomial(rho)
                  -(alphat+alpha**2+2*rt*alpha/r+4*kap*p2/r+rtt/r+4*p2*d2))

        # Independent reciprocal jets.  No fifth-power form is inserted.
        F0, F1, F2, F3 = sp.symbols("F0 F1 F2 F3")

        def Dt(expression):
            return (sp.diff(expression, F0)*F1+sp.diff(expression, F1)*F2
                    +sp.diff(expression, F2)*F3)

        R = 1/F0
        R1, R2 = Dt(R), Dt(Dt(R))
        delta = R2/2-R1**2/R
        p = 4*F0*F1/F2
        K = F2**2/(16*F1*F0**3)
        a = F1/F0+F2/F1-2*F3/F2
        self.zero(p-2*R1/(R*delta))
        self.zero(K+R*delta**2/(4*R1))
        self.zero(a-(2*R1/R-Dt(K)/K))
        self.zero(K*p**2+R1/R)
        self.zero(-2*K*p-delta)
        ode = 4*F1*F3-3*F2**2
        self.zero(Dt(p)+2*a*p+3*R1*p/R+3/R+5*F0*ode/F2**2)
        q = F2/F1
        self.zero(4*Dt(q)+q**2-ode/F1**2)
        # This identity explains the root-free integration in the proof.
        self.zero(Dt(1/q)-sp.Rational(1, 4)+ode/(4*F2**2))

    def test_fifth_power_polynomiality_leaders_and_ratio(self):
        zeta, C0, C1, rho, y, tau = sp.symbols("zeta C0 C1 rho y tau")
        F = C0+C1*zeta**5
        r = 1/F
        kap = 5*C1*zeta**2/F**3
        p2 = zeta*F
        D = sp.diff(F, zeta)/F
        alpha = D-2/zeta
        rt, rtt = sp.diff(r, zeta), sp.diff(r, zeta, 2)
        self.zero(4*sp.diff(F, zeta)*sp.diff(F, zeta, 3)
                  -3*sp.diff(F, zeta, 2)**2)
        self.zero(sp.diff(F, zeta, 2)/sp.diff(F, zeta)-4/zeta)
        self.zero(sp.diff(sp.diff(F, zeta)/zeta**4, zeta))
        self.zero(sp.diff(D, zeta)-(4*D/zeta-D**2))
        d2_from_S = -(sp.diff(alpha, zeta)+alpha**2+2*rt*alpha/r
                      +4*kap*p2/r+rtt/r)/(4*p2)
        d2 = -sp.diff(F, zeta)/(zeta**2*F**2)-sp.Rational(3, 2)/(zeta**3*F)
        self.zero(d2_from_S-d2)
        B = sp.diff(kap, zeta, 2)/2-(rt/r)*sp.diff(kap, zeta)-kap*rtt/r
        shared = 1/zeta**2-6*D/zeta+D**2
        self.zero(B/kap-shared)
        self.zero(alpha**2+2*p2*d2-shared)
        lambda2 = (kap*(alpha**2+2*p2*d2)-B)/p2
        self.zero(lambda2)
        ell3 = (2*kap*d2-4*kap**2/r)/3
        z2 = r*d2+kap
        w3 = (ell3-2*kap*d2)/r
        self.zero(z2+sp.Rational(3, 2)/(zeta**3*F**2))
        self.zero(w3-10*C1/(zeta*F**3))
        self.zero(w3+4*kap*z2/(3*r**2))
        self.zero(w3**2/z2**3+sp.Rational(800, 27)*C1**2*zeta**7)
        # The C0=0 case is retained, rather than excluded by a denominator.
        self.zero(d2.subs(C0, 0)+sp.Rational(13, 2)/(C1*zeta**8))
        self.zero(w3.subs(C0, 0)-10/(C1**2*zeta**16))

        # Independently keep every coefficient slot abstract for extraction,
        # avoiding expansion of fifth-power rational denominators here.
        R0, R1, R2, K0, K1, P2, A1, D2, L3 = sp.symbols(
            "R0 R1 R2 K0 K1 P2 A1 D2 L3"
        )
        b, e, d, s, n0, st, n0t, k0t, k0tt = sp.symbols(
            "b e d s n0 st n0t k0t k0tt"
        )
        E0, E1, E2 = sp.symbols("E0 E1 E2")
        P = P2*y**2+(A1*rho+b)*y+D2*rho**2+e*rho+d
        n = K0*rho**2+s*rho+n0
        nt = K1*rho**2+st*rho+n0t
        nr = 2*K0*rho+s
        ell = L3*rho**3+E2*rho**2+E1*rho+E0
        projected_z = 3*tau*y**2+(R1*rho+k0t)*y+R0*P+n
        projected_w = (ell-y**3-(R2*rho+k0tt)*y**2/2
                       -nt*y-(R1*y+nr)*P)/R0
        zpoly = sp.Poly(projected_z, rho)
        wpoly = sp.Poly(projected_w, rho)
        self.assertEqual(zpoly.degree(), 2)
        self.assertEqual(wpoly.degree(), 3)
        self.zero(zpoly.LC()-(R0*D2+K0))
        self.zero(wpoly.LC()-(L3-2*K0*D2)/R0)

    def test_finite_weighted_residue_controls_and_cancellation_boundary(self):
        R, Z, W, a, b, gamma = sp.symbols("R Z W a b gamma")
        z = a*R**2+R+1
        w = b*R**3-2*R+3
        # Several finite highest-weight spaces, not a substitute for the
        # written universal no-cancellation or exact residue-field lemma.
        for degree in (6, 7, 9, 12):
            pairs = [(i, j) for j in range(degree//3+1)
                     for i in range(degree//2+1) if 2*i+3*j == degree]
            coefficients = sp.symbols(f"c{degree}_:{len(pairs)}")
            H = sum(c*Z**i*W**j for c, (i, j) in zip(coefficients, pairs))
            evaluated = sp.Poly(H.xreplace({Z: z, W: w}), R)
            self.assertEqual(evaluated.degree(), degree)
            leading = sum(c*a**i*b**j for c, (i, j) in zip(coefficients, pairs))
            self.zero(evaluated.LC()-leading)
            i0, j0 = pairs[0]
            residue_polynomial = sum(
                c*gamma**((j-j0)//2) for c, (i, j) in zip(coefficients, pairs)
            )
            self.zero(leading/(a**i0*b**j0)
                      -residue_polynomial.subs(gamma, b**2/a**3))
            self.assertNotEqual(residue_polynomial, 0)

        # A monomial finite control for the seventh-power residue; these
        # arithmetic identities alone do not establish an exact field index.
        zeta = sp.symbols("zeta")
        zm = zeta**3*R**2
        wm = zeta**8*R**3
        self.zero(wm**2/zm**3-zeta**7)
        self.zero(zm**8/wm**3-R**7)

        # Deliberate failure of the transcendence premise.  Hidden lower
        # terms now recover a new residue despite the leading ratio being 1.
        t = sp.symbols("t")
        z_bad, w_bad = R**2, R**3+t
        numerator = sp.Poly(w_bad**2-z_bad**3, R)
        denominator = sp.Poly(w_bad, R)
        self.assertEqual(numerator.degree(), 3)
        self.assertEqual(denominator.degree(), 3)
        self.zero(numerator.LC()/denominator.LC()-2*t)
        self.zero(sp.Poly(w_bad, R).LC()**2/sp.Poly(z_bad, R).LC()**3-1)


if __name__ == "__main__":
    unittest.main()
