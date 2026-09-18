"""Independent finite algebra controls for the three bounded pass204 notes.

The two explicit frames are actual polynomial examples. The pivot jets and
transport model are formal controls, not a realized radical-pivot frame.
Neither these identities nor the representative leading-degree controls prove
the universal field, LND, kernel, or all-polynomial-parameter arguments. Those
remain written proofs. No earlier checker, proof, or solver code is imported.
"""

import unittest

import sympy as sp


class ActualFrameReplicaControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def test_two_root_actual_frame_slice_inverse_and_leading_coefficients(self):
        x, y, z, g, u, v = sp.symbols("x y z g u v")
        a, b, c = 1+2*sp.I*g, g**2, g*(1+sp.I*g)

        def E(expression):
            return sp.expand(a*sp.diff(expression,x)+b*sp.diff(expression,y))

        us = (1-2*sp.I*g)*x-4*y
        vs = a*y-b*x
        xi, yi = a*u+4*v, b*u+(1-2*sp.I*g)*v
        self.zero(E(us)-1)
        self.zero(E(vs))
        self.zero(xi.xreplace({u:us,v:vs})-x)
        self.zero(yi.xreplace({u:us,v:vs})-y)
        self.zero(us.xreplace({x:xi,y:yi})-u)
        self.zero(vs.xreplace({x:xi,y:yi})-v)

        j = -z**2/2+x*g-sp.I*y
        Zf = z+x*j
        Wf = g+x*y*(y-x)/2+z*j+x*j**2/2
        X,Y,Z,W,J0 = sp.symbols("X Y Z W J0")
        I = Z**2-X**2*Y*(X-Y)-2*X*W
        J = (-I-2*sp.I*Y)/2
        # Forward then inverse, with the recovered parameter checked first.
        self.zero(J.xreplace({X:x,Y:y,Z:Zf,W:Wf})-j)
        self.zero(Zf-x*j-z)
        self.zero(Wf-Zf*j+x*j**2/2-x*y*(y-x)/2-g)
        # Inverse then forward. J0 is kept independent to avoid nested expansion.
        zi = Z-X*J0
        gi = W-Z*J0+X*J0**2/2-X*Y*(Y-X)/2
        recovered_j = -zi**2/2+X*gi-sp.I*Y
        self.zero(recovered_j-J)
        self.zero(zi+X*J0-Z)
        self.zero(gi+X*Y*(Y-X)/2+zi*J0+X*J0**2/2-W)
        # Setting J0=J in these identities proves the reverse composition.

        self.zero(E(j)-c)
        self.zero(c**2-b*(a-b))
        e, h = E(E(Zf))/2, E(E(Wf))/2
        correct_h = -a*(c*z**2+a*vs)/2
        self.zero(e-a*c)
        self.zero(h-correct_h)
        self.zero(E(E(E(Zf))))
        self.zero(E(E(E(Wf))))
        for leading in [a,b,e,h]:
            self.assertNotEqual(sp.expand(leading),0)
        # The rejected guess omitted a^2 on the invariant v coefficient.
        wrong_h = -a*c*z**2/2-vs/2
        self.zero(h-wrong_h+(a**2-1)*vs/2)
        self.assertNotEqual(sp.expand(h-wrong_h),0)
        t,q = b/a,c/a
        rho = -v/2-q*z**2/2
        self.zero(q**2-t*(1-t))
        self.zero(sp.diff(rho,v)+sp.Rational(1,2))
        self.zero(h.xreplace({x:xi,y:yi})/a**2-rho)
        self.zero(e**2-a**2*b*(a-b))

    def test_radical_pivot_potentials_affine_gate_and_formal_transport(self):
        U,V,w,rho = sp.symbols("U V w rho")
        kt,kr,ktt,ktr,krr = sp.symbols("kt kr ktt ktr krr")
        kttt,kttr,ktrr,krrr = sp.symbols("kttt kttr ktrr krrr")
        n,nt,nr,ntt,ntr,nrr = sp.symbols("n nt nr ntt ntr nrr")
        ell,ellt,ellr,m = sp.symbols("ell ellt ellr m")
        f = V**2+kt*U+kr*V+n
        R = sp.diff(f,V)
        g3 = ktt*U**2/2+ktr*U*V+krr*V**2/2+nt*U+nr*V
        g4 = (kttt*U**3/6+kttr*U**2*V/2+ktrr*U*V**2/2
              +krrr*V**3/6+ntt*U**2/2+ntr*U*V+nrr*V**2/2)
        fr = ktr*U+krr*V+nr
        B,C = ktt*U+ktr*V+nt, 2*w+fr
        first = R*w+g3-ell
        fourth = w**2+fr*w+g4-ellt*U-ellr*V-m
        self.zero(sp.diff(first,U)-B)
        self.zero(sp.diff(first,V)-C)
        self.zero(sp.diff(first,w)-R)
        g3t = kttt*U**2/2+kttr*U*V+ktrr*V**2/2+ntt*U+ntr*V
        g3r = kttr*U**2/2+ktrr*U*V+krrr*V**2/2+ntr*U+nrr*V
        self.zero(sp.diff(fourth,U)-(ktr*w+g3t-ellt))
        self.zero(sp.diff(fourth,V)-(krr*w+g3r-ellr))
        self.zero(sp.diff(fourth,w)-C)
        self.zero(sp.Poly(fourth,w).coeff_monomial(w**2)-1)
        self.zero(sp.diff(fourth-w**2,w)-C+2*w)

        theta = -kr/2
        self.zero(R.subs(V,theta))
        self.zero(B.subs({V:theta,ktt:0,nt:-ktr*theta}))
        yt,yp,yv,wt,wp,wv,cc = sp.symbols("yt yp yv wt wp wv cc")
        reduced = sp.Matrix([[yt,yp,yv],[0,cc,0],[wt,wp,wv]])
        self.zero(reduced.det()-cc*(yt*wv-yv*wt))

        # A formal affine-line transport with NX nonzero and N^2 X nonzero.
        # It illustrates the cancellation mechanism, not an actual frame claim.
        u,v,a,t,alpha,beta,w0,k = sp.symbols("u v a t alpha beta w0 k")
        X = v**3+a*u
        y = alpha*v+beta
        wline = -ktr*y/2+w0
        zline = 2*rho*wline+theta**2+kt*y+kr*theta+n
        sigma = 2*rho*theta+k
        entries = [X,y+t*X,zline+sigma*X+rho**2*X**2,
                   wline+theta*X+rho*X**2]

        def E(expression):
            return sp.diff(expression,u)

        def N(expression):
            return sp.diff(expression,v)

        def P(expression):
            return sp.expand(a*N(expression)-N(X)*E(expression))

        self.zero(N(X)-3*v**2)
        self.zero(N(N(X))-6*v)
        self.zero(P(X))
        self.zero(P(entries[1])-a*alpha)
        for expression in entries:
            self.zero(P(P(expression)))
            self.zero(E(P(expression))-P(E(expression)))
        self.zero(P(v)-a)
        self.zero(P(u)+3*v**2)

    def test_counterexample_actual_frame_inverse_and_transport(self):
        u,v,g,w = sp.symbols("u v g w")
        X,Y,Z,W = sp.symbols("X Y Z W")
        forward = {X:u,Y:v+g*u,Z:g+u**2,W:w+(g+u**2)**4}
        inverse = {u:X,g:Z-X**2,v:Y-X*(Z-X**2),w:W-Z**4}
        for source,expression in inverse.items():
            self.zero(expression.xreplace(forward)-source)
        for target,expression in forward.items():
            self.zero(expression.xreplace(inverse)-target)

        def E(expression):
            return sp.expand(sp.diff(expression,X)+(Z-X**2)*sp.diff(expression,Y)
                             +2*X*sp.diff(expression,Z)+8*X*Z**3*sp.diff(expression,W))

        for target,expression in forward.items():
            self.zero(E(target).xreplace(forward)-sp.diff(expression,u))
        self.assertEqual([sp.Poly(e,u).degree() for e in forward.values()],[1,1,2,8])
        self.assertEqual([sp.Poly(e,u).LC() for e in forward.values()],[1,g,1,1])
        self.zero(E(E(X)))
        self.zero(E(E(Y)))
        self.zero(E(Z-X**2))
        self.zero(E(Y-X*(Z-X**2)))
        self.zero(E(W-Z**4))

    def test_replica_inverse_and_leading_coefficient_controls(self):
        X,Y,Z,W,j = sp.symbols("X Y Z W j")
        H = 2*X*W-Z**2
        Zj,Wj = Z-X*j,W-Z*j+X*j**2/2
        self.zero(2*X*Wj-Zj**2-H)
        # H is preserved, so a parameter J(X,Y,H) has the same value in both frames.
        self.zero(Zj+X*j-Z)
        self.zero(Wj+Zj*j+X*j**2/2-W)
        self.zero((Z+X*j)-X*j-Z)
        self.zero((W+Z*j+X*j**2/2)-(Z+X*j)*j+X*j**2/2-W)
        self.zero(X*sp.diff(H,Z)+Z*sp.diff(H,W))

        def E(expression):
            return sp.diff(expression,X)+(Z-X**2)*sp.diff(expression,Y)+2*X*sp.diff(expression,Z)+8*X*Z**3*sp.diff(expression,W)

        j0,jx,jy,c0,p0,px,py,q0,qx,qy = sp.symbols("j0 jx jy c0 p0 px py q0 qx qy")
        leading_j = j0+jx*X+jy*Y
        P,Q = p0+px*X+py*Y,q0+qx*X+qy*Y
        # Representative positive H-degrees support, but do not prove, the all-degree argument.
        for degree in [1,2,3]:
            parameter = leading_j*H**degree+c0
            expression = W-Z*parameter+X*parameter**2/2-P*(Z-X*parameter)-Q
            coefficient = 2**(2*degree-1)*X**(2*degree+1)*leading_j**2
            self.zero(sp.Poly(expression,W).coeff_monomial(W**(2*degree))-coefficient)
            self.zero(sp.Poly(E(expression),W).coeff_monomial(W**(2*degree))
                      -sp.diff(coefficient,X)-(Z-X**2)*sp.diff(coefficient,Y))
        mm = sp.Symbol("mm",integer=True,positive=True)
        kk = sp.Symbol("kk",integer=True,nonnegative=True)
        self.assertTrue((2*mm+1+2*kk).is_positive)
        Pval,Px,Py,Qx,Qy = sp.symbols("Pval Px Py Qx Qy")
        possible_rhs = 2*X*Pval+(Px+(Z-X**2)*Py)*Z+Qx+(Z-X**2)*Qy
        self.zero(sp.Poly(8*X*Z**3-possible_rhs,Z).coeff_monomial(Z**3)-8*X)
        lam = sp.Symbol("lam")
        parameter = lam*H
        expression = W-Z*parameter+X*parameter**2/2-P*(Z-X*parameter)-Q
        self.zero(sp.Poly(E(expression),W).coeff_monomial(W**2)-6*lam**2*X**2)
        self.zero(E(Z-X*X))


if __name__ == "__main__":
    unittest.main()
