"""Finite independent algebra controls for both actual normalizations202.

The six methods reconstruct raw lower coefficients, exact rational bases,
Wronskians, polynomial inverse orders and coefficient translations.  They do
not prove completeness in a finite differential field, actual realization,
preservation of an entire initial kernel, recognition, or cancellation.
No prior checker, proof solver or implementation is imported.
Root owns canonical execution after complete saved-source review.
"""

import unittest

import sympy as sp


class TwoRootNormalizationControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def jets(self, r):
        k, s, n = sp.symbols("k0:6"), sp.symbols("s0:4"), sp.symbols("n0:4")
        chains = list(zip(k, k[1:])) + list(zip(s, s[1:])) + list(zip(n, n[1:]))

        def dr(expression):
            return sp.diff(expression, r) + sum(
                sp.diff(expression, slot)*successor for slot, successor in chains)

        def dt(expression):
            return sp.factor((1+r**2)**2*dr(expression)/(2*r))

        return k, s, n, dr, dt

    def lower(self, q, R, nu, k0, s0, n0, dt):
        """Coefficient arrays derived from the literal V-square equations."""
        Rp, Rpp = dt(R), dt(dt(R))
        vp, vpp = dt(nu), dt(dt(nu))
        Delta = sp.factor(R*Rpp/2-Rp**2)
        d = dt(dt(dt(q)))/6
        b1, b0 = sp.factor(R*vp-2*Rp*nu), sp.factor(R*dt(s0)-2*Rp*s0)
        c2 = sp.factor(R*vpp/4-Rp*vp/2-nu*Rpp/2)
        c1 = sp.factor(R*dt(dt(s0))/2-Rp*dt(s0)
                       -(nu*dt(dt(k0))+s0*Rpp)/2)
        c0 = sp.factor(R*dt(dt(n0))/2-Rp*dt(n0)-s0*dt(dt(k0))/2)
        a2 = sp.factor(b1**2/(2*Delta*R)-nu*c2/Delta-nu**2/R)
        a1 = sp.factor(b1*b0/(Delta*R)-nu*c1/Delta-2*nu*s0/R)
        a0 = sp.factor(b0**2/(2*Delta*R)-nu*c0/Delta-s0**2/R)
        C2, C1, C0 = -R*a2-nu**2, -R*a1-2*nu*s0, -R*a0-s0**2
        return {
            "Delta": Delta,
            "U3": sp.factor(R*dt(dt(dt(k0)))/6-Rp*dt(dt(k0))/2
                            -d*s0-Delta*b0/(R*nu)),
            "U3rho": sp.factor(R*dt(Rpp)/6-Rp*Rpp/2-d*nu-Delta*b1/(R*nu)),
            "B3": sp.factor(-R*dt(a2/3)+Rp*a2/3-nu*vp/2-b1*C2/(R*nu)),
            "B2": sp.factor(-R*dt(a1/2)+Rp*a1/2-nu*dt(s0)-s0*vp/2
                            -(b1*C1+b0*C2)/(R*nu)),
            "B1": sp.factor(-R*dt(a0)+Rp*a0-nu*dt(n0)-s0*dt(s0)
                            -(b1*C0+b0*C1)/(R*nu)),
            "L3": sp.factor(a2/3),
        }

    def inverse_pairs(self, slots, pairs):
        Z = slots[2]
        for forward, inverse in pairs:
            for outer, inner in ((forward, inverse), (inverse, forward)):
                replacement = dict(zip(slots, inner))
                for expression, coordinate in zip(outer, slots):
                    self.zero(expression.subs(replacement, simultaneous=True)-coordinate)
            for index in (0, 1, 3):
                self.zero(sp.diff(inverse[index], Z))
            self.zero(sp.diff(inverse[2], Z)-1)

    def test_monomial_raw_gates_fifth_order_and_last_coefficient(self):
        r, C = sp.symbols("r C")
        O = 1+r**2
        q, R, nu = r/O, O/r, -O**3/r**3
        k, s, n, dr, dt = self.jets(r)
        raw = self.lower(q, R, nu, k[0], s[0], n[0], dt)
        U = (r*O**3*k[3]+6*r**2*O**2*k[2]+6*r*O**2*k[1]
             +3*r*O*s[1]+3*(1-r**2)*s[0])
        V = (O**5*k[3]+6*r*O**4*k[2]+6*O**4*k[1]
             +r**2*O**3*s[3]+6*r*O**2*s[2]
             -6*O*(3*r**2-1)*s[1]+24*r*(r**2-1)*s[0])
        self.zero(raw["Delta"]-1/(8*q**6))
        self.zero(raw["U3"]-O**4*U/(48*r**5))
        self.zero(raw["U3rho"])
        self.zero(raw["B3"])
        self.zero(raw["B2"]+O**2*V/(4*r**4))
        s1 = (r**2-1)*s[0]/(r*O)-(O**2*k[3]+6*r*O*k[2]+6*O*k[1])/3
        s2 = sp.factor(dr(s1).subs(s[1], s1))
        s3 = sp.factor(dr(s2).subs(s[1], s1))
        eliminated = raw["B2"].subs({s[1]: s1, s[2]: s2, s[3]: s3},
                                     simultaneous=True)
        fifth = r*O*k[5]+5*(3*r**2+1)*k[4]+60*r*k[3]+60*k[2]
        self.zero(eliminated-O**6*fifth/(12*r**3))
        last = self.lower(q, R, nu, 0, C*R, n[0], dt)["B1"]
        self.zero(last+O*(O**4*(r*n[3]+3*n[2])+12*C**2*r*(r**2-1))/(2*r**3))

    def test_monomial_bases_primitives_and_bare_third_potential(self):
        r, C = sp.symbols("r C")
        O = 1+r**2
        t, q, R, nu = r**2/O, r/O, O/r, -O**3/r**3
        basis = [sp.S.One, t, R, t*R, t**2*R]
        for h in basis:
            self.zero(r*O*sp.diff(h, r, 5)+5*(3*r**2+1)*sp.diff(h, r, 4)
                      +60*r*sp.diff(h, r, 3)+60*sp.diff(h, r, 2))
        matrix = sp.Matrix([[sp.factor(sp.diff(h, r, i)) for h in basis]
                            for i in range(5)])
        self.zero(matrix.det(method="domain-ge")+288/(r**5*O**5))
        particular = -C**2*r*(2*r**2+3)/(2*O)
        self.zero(O**4*(r*sp.diff(particular, r, 3)+3*sp.diff(particular, r, 2))
                  +12*C**2*r*(r**2-1))
        for h in (sp.S.One, r, 1/r):
            self.zero(r*sp.diff(h, r, 3)+3*sp.diff(h, r, 2))
        dt = lambda expression: sp.factor(O**2*sp.diff(expression, r)/(2*r))
        bare = self.lower(q, R, nu, 0, 0, 0, dt)
        self.zero(bare["L3"]+1/(2*q**5))
        for name in ("U3", "U3rho", "B3", "B2", "B1"):
            self.zero(bare[name])
        ell0 = sp.Function("ell0")(r)
        self.zero(-R*dt(ell0)+dt(R)*ell0+R**2*dt(ell0/R))
        # Exact-field completeness is the written state-vector argument,
        # not a conclusion supplied by these rational basis identities.

    def test_monomial_actual_maps_columns_and_X_translation(self):
        X, Y, Z, W = slots = sp.symbols("X Y Z W")
        c, a, C, K0, K1, p0, p1, p2 = sp.symbols("c a C K0 K1 p0 p1 p2")
        N0, Np, Nm, constant = sp.symbols("N0 Nplus Nminus constant")
        P2 = p0*X**2+p1*X*Y+p2*Y**2
        pairs = [
            ((X,Y,Z,W/c),(X,Y,Z,c*W)),
            ((X,Y,Z-K0*X-K1*Y,W+P2),(X,Y,Z+K0*X+K1*Y,W-P2)),
            ((X+a,Y,Z,W+a*(Y**2-sp.Rational(3,2)*(X+a)*Y)),
             (X-a,Y,Z,W-a*(Y**2-sp.Rational(3,2)*X*Y))),
            ((X,Y,Z-N0,W+Nm*X+(Np-Nm)*Y),
             (X,Y,Z+N0,W-Nm*X-(Np-Nm)*Y)),
            ((X,Y,Z,W-constant),(X,Y,Z,W+constant)),
        ]
        self.inverse_pairs(slots, pairs)
        r, rho, y, theta, w, n0, x = sp.symbols("r rho y theta w n0 x")
        O = 1+r**2
        t, q, R, nu = r**2/O, r/O, O/r, -O**3/r**3
        dt = lambda expression: sp.factor(O**2*sp.diff(expression, r)/(2*r))
        self.zero((c*q)/c-q)
        self.zero(c**2*(-1/(c**2*q**3))-nu)
        Q = dt(dt(q))/2
        P = p0+p1*t+p2*t**2
        k0 = K0+K1*t+R*P
        self.zero(dt(k0-R*P)-K1)
        self.zero(R*rho+k0-K0-K1*t-R*(rho+P))
        n = nu*rho**2/2+C*R*rho+n0
        z = Q*y**2+dt(R)*rho*y+R*theta+n
        sigma = dt(q)*y+R*rho
        Pa = a*(t**2-sp.Rational(3,2)*t)
        yn, rn = y-a*t, rho+Pa
        tn = theta-2*a*rho+a*(2*t-sp.Rational(3,2))*yn
        zn = z-a*sigma+a**2*q
        wn = w-a*theta+a**2*rho+a*yn**2
        self.zero(sigma-2*a*q-dt(q)*yn-R*rn)
        self.zero(w+theta*(x-a)+rho*(x-a)**2
                  +a*((yn+t*x)**2-sp.Rational(3,2)*x*(yn+t*x))
                  -(wn+tn*x+rn*x**2))
        nnew = zn-Q*yn**2-dt(R)*rn*yn-R*tn
        correction = (C*a*r**3+3*C*a*r+a**2*r**3)/(2*O)
        self.zero(nnew-(nu*rn**2/2+(C-a)*R*rn+n0+correction))
        particular = -C**2*r*(2*r**2+3)/(2*O)
        self.zero(particular+correction.subs(a,C))
        self.zero(N0+Np*r+Nm/r-N0-R*(Nm+(Np-Nm)*t))

    def test_reciprocal_raw_system_and_last_coefficient(self):
        r = sp.symbols("r")
        O = 1+r**2
        q, R, nu = r/O, r, -r*O
        k, s, n, dr, dt = self.jets(r)
        raw = self.lower(q, R, nu, k[0], s[0], n[0], dt)
        U = (r**3*O**2*k[3]+6*r**2*(r**2-1)*O*k[2]
             +6*r*(r**2-1)**2*k[1]+3*r*(r**2-3)*s[1]+3*(5-r**2)*s[0])
        V = (r**2*(r**2-3)*s[3]-6*r*s[2]+6*s[1]
             +r**2*(r**2-3)*O*k[3]+6*r*(r**4-4*r**2-1)*k[2]
             +6*(r**4-6*r**2+1)*k[1])
        self.zero(raw["Delta"]-(r**2-3)*O**3/(8*r**2))
        self.zero(raw["U3"]-O**4*U/(48*r**5))
        self.zero(raw["U3rho"])
        self.zero(raw["B3"])
        self.zero(raw["B2"]+O**4*V/(4*(r**2-3)**2))
        last = self.lower(q,R,nu,0,0,n[0],dt)["B1"]
        self.zero(last+r*O**3*(r*(r**2-3)*O*n[3]
                              +3*(r**4-6*r**2+1)*n[2])/(2*(r**2-3)**2))
        f = 1/r
        d = dt(dt(dt(q)))/6
        D = dt(d)*f/4+d*dt(f)
        self.zero(d+(r**2-1)*O**4/(16*r**5))
        self.zero(D+(r**2-3)**2*O**5/(128*r**8))
        self.zero(dt(dt(f))**2/(8*f**3*D)-nu)

    def test_reciprocal_six_state_basis_and_final_three_modes(self):
        r = sp.symbols("r")
        O = 1+r**2
        t, q, R, nu = r**2/O, r/O, r, -r*O
        pairs = [(sp.S.One,sp.S.Zero),(t,sp.S.Zero),(R,nu),
                 (R*t,nu*t),(R*t**2,nu*t**2),(1/r,O/r)]
        for k, s in pairs:
            U = (r**3*O**2*sp.diff(k,r,3)+6*r**2*(r**2-1)*O*sp.diff(k,r,2)
                 +6*r*(r**2-1)**2*sp.diff(k,r)
                 +3*r*(r**2-3)*sp.diff(s,r)+3*(5-r**2)*s)
            V = (r**2*(r**2-3)*sp.diff(s,r,3)-6*r*sp.diff(s,r,2)+6*sp.diff(s,r)
                 +r**2*(r**2-3)*O*sp.diff(k,r,3)
                 +6*r*(r**4-4*r**2-1)*sp.diff(k,r,2)
                 +6*(r**4-6*r**2+1)*sp.diff(k,r))
            self.zero(U)
            self.zero(V)
        matrix = sp.Matrix.hstack(*[
            sp.Matrix([sp.factor(sp.diff(k,r,i)) for i in range(3)]
                      +[sp.factor(sp.diff(s,r,i)) for i in range(3)])
            for k,s in pairs
        ])
        self.zero(matrix.det(method="domain-ge")+64*r**4*(r**2-3)/O**6)
        dt = lambda expression: sp.factor(O**2*sp.diff(expression,r)/(2*r))
        self.zero(2*dt(q)-(1/r-R))
        self.zero(2*dt(R)-(O/r-nu))
        basis = [sp.S.One, r, r*t]
        for h in basis:
            self.zero(r*(r**2-3)*O*sp.diff(h,r,3)
                      +3*(r**4-6*r**2+1)*sp.diff(h,r,2))
        matrix = sp.Matrix([[sp.factor(sp.diff(h,r,i)) for h in basis]
                            for i in range(3)])
        self.zero(matrix.det(method="domain-ge")+2*r*(r**2-3)/O**3)
        bare = self.lower(q,R,nu,0,0,0,dt)
        self.zero(bare["L3"]+r*O**2/2)
        for name in ("U3","U3rho","B3","B2","B1"):
            self.zero(bare[name])

    def test_reciprocal_actual_involution_translations_and_inverse_orders(self):
        X,Y,Z,W = slots = sp.symbols("X Y Z W")
        c,lam,K0,K1,p0,p1,p2,N0,N1,N2,C = sp.symbols(
            "c lam K0 K1 p0 p1 p2 N0 N1 N2 C")
        P2 = p0*X**2+p1*X*Y+p2*Y**2
        self.inverse_pairs(slots, [
            ((X,X-Y,Z,W),(X,X-Y,Z,W)),
            ((X,Y,Z,W/c),(X,Y,Z,c*W)),
            ((X,Y+lam,Z,W),(X,Y-lam,Z,W)),
            ((X,Y,Z-K0*X-K1*Y,W+P2),(X,Y,Z+K0*X+K1*Y,W-P2)),
            ((X,Y,Z-N0,W+N1*X+N2*Y),(X,Y,Z+N0,W-N1*X-N2*Y)),
            ((X,Y,Z,W-C),(X,Y,Z,W+C)),
        ])
        F = Z**2-X**2*Y*(X-Y)
        self.zero(F.subs(Y,X-Y)-F)
        r,rho,y,theta,n0,rn = sp.symbols("r rho y theta n0 rhonew")
        O = 1+r**2
        t,q,R,nu = r**2/O,r/O,r,-r*O
        dt = lambda expression: sp.factor(O**2*sp.diff(expression,r)/(2*r))
        self.zero(c*q/((1-t)-1)+c*q/t)
        self.zero((c*q/t)/c-q/t)
        self.zero(c**2*(-r*O/c**2)-nu)
        Q = dt(dt(q))/2
        P = p0+p1*t+p2*t**2
        k0 = K0+K1*t+R*P+lam*dt(q)
        s0 = nu*P+lam*dt(R)
        k = R*rho+k0
        n = nu*rho**2/2+s0*rho+n0
        z = Q*y**2+dt(k)*y+R*theta+n
        yn = y+lam
        k1 = k-lam*dt(q)
        n1 = nu*rho**2/2+(s0-lam*dt(R))*rho+n0-lam*dt(k0)+lam**2*Q
        self.zero(z-Q*yn**2-dt(k1)*yn-R*theta-n1)
        self.zero(k1-K0-K1*t-R*(rho+P))
        self.zero(z-K1*yn-Q*yn**2-dt(R)*(rho+P)*yn
                  -R*(theta+dt(P)*yn)-n1)
        self.zero(sp.Poly(sp.expand(n1.subs(rho,rn-P)),rn).coeff_monomial(rn))
        z_with_modes = (Q*y**2+dt(R)*rho*y+R*theta+nu*rho**2/2
                        +N0+R*(N1+N2*t))
        theta_final = theta+N1+N2*t
        self.zero(z_with_modes-N0-Q*y**2-dt(R)*rho*y
                  -R*theta_final-nu*rho**2/2)
        ell0 = sp.Function("ell0")(r)
        self.zero(-R*dt(ell0)+dt(R)*ell0+R**2*dt(ell0/R))
        self.zero((-R*dt(ell0)+dt(R)*ell0).subs(ell0,C*R).doit())


if __name__ == "__main__":
    unittest.main()
