"""Finite exact algebra controls for the two normalized two-root branches.

These independent symbolic identities support the saved pass203 arguments.
They do not prove actual field return, finite-field ODE completeness,
irreducibility, normality, or the recognition theorem. In particular a scalar
Jacobian is not treated as proof that a formal chart is an actual frame.
No proof, solver, or earlier checker module is imported.
"""

import unittest

import sympy as sp


class TwoRootBranchControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def raw_potentials(self, r, rho, U, V, g, R, nu, ell3):
        """Build the literal coefficient potentials, before evaluating U,V."""
        g0, g1, g2, g3 = g
        omega = 1 + r**2
        q = r / omega

        def dr(expression):
            return sp.diff(expression, r) + sum(
                sp.diff(expression, old) * new
                for old, new in zip(g[:-1], g[1:])
            )

        def dt(expression):
            return sp.cancel(omega**2 * dr(expression) / (2 * r))

        k = R * rho
        n = nu * rho**2 / 2
        ell = ell3 * rho**3 + R * g0
        qt, qtt = dt(q), dt(dt(q))
        qttt, qtttt = dt(qtt), dt(dt(qtt))
        kt, ktt = dt(k), dt(dt(k))
        S = (qttt * U**3 / 6 + ktt * U**2 / 2
             + dt(R) * U * V + dt(n) * U + sp.diff(n, rho) * V)
        T = (qtttt * U**4 / 24 + dt(ktt) * U**3 / 6
             + dt(dt(R)) * U**2 * V / 2 + dt(dt(n)) * U**2 / 2
             + dt(sp.diff(n, rho)) * U * V
             + sp.diff(n, rho, 2) * V**2 / 2)
        m = sp.Symbol("m")
        H = (R * (T - dt(ell) * U - sp.diff(ell, rho) * V - m)
             + (dt(R) * U + sp.diff(n, rho)) * (ell - S))
        return dt, dr, qt, qtt, kt, n, ell, S, H

    def test_monomial_literal_potentials_scalar_and_ode(self):
        r, rho, U, V, y, z, X = sp.symbols("r rho U V y z X")
        g = sp.symbols("g0:4")
        g0, g1, g2, g3 = g
        omega = 1 + r**2
        t, q, s = r**2 / omega, r / omega, (1 - r**2) / omega
        R, nu = 1 / q, -1 / q**3
        dt, _, qt, qtt, kt, n, ell, S, H = self.raw_potentials(
            r, rho, U, V, g, R, nu, -1 / (2 * q**5)
        )
        P = (U**2 + 4 * s * rho * U + 4 * rho**2) / (8 * q**2)
        B1 = -dt(g0) / q**2
        remainder = sp.cancel(H - R * nu * (V - P)**2 / 2 - B1 * U)
        self.zero(sp.diff(remainder, U))
        self.zero(sp.diff(remainder, V))
        theta = P.subs(U, y) + q * z
        self.zero(qtt * y**2 / 2 + kt * y + R * theta + n - z)
        w = g0 + z * (rho + s * y / 2) / q
        self.zero((ell - S.subs({U: y, V: theta})) / R - w)

        # Literal determinant with unrestricted y and coefficient derivatives.
        yt, yp, yz = sp.symbols("yt yp yz")
        h = (rho + s * y / 2) / q
        entries = [y, z, g0 + z * h]
        derivatives = [
            lambda e: dt(e) + yt * sp.diff(e, y),
            lambda e: sp.diff(e, rho) + yp * sp.diff(e, y),
            lambda e: sp.diff(e, z) + yz * sp.diff(e, y),
        ]
        J = sp.Matrix([[D(e) for D in derivatives] for e in entries]).det()
        expected = dt(g0) * yp - z * ((y + 2 * s * rho) * yp / (4 * q**3) + yt / q)
        self.zero(J - expected)
        A, At, B, Bt, Bp = sp.symbols("A At B Bt Bp")
        projected = sp.expand(expected.subs({y: A*z**2+B, yt: At*z**2+Bt, yp: Bp}))
        self.zero(projected.coeff(z, 3) + A*Bp/(4*q**3) + At/q)
        self.zero(projected.coeff(z, 1) + (B+2*s*rho)*Bp/(4*q**3) + Bt/q)
        self.zero(projected.coeff(z, 0) - dt(g0)*Bp)

        # Independent t-jets, not the r-jets used to construct the potentials.
        G1, G2, G3 = sp.symbols("G1 G2 G3")
        a = 4*q**2*G2/G1
        Da = dt(a) + sp.diff(a, G1)*G2 + sp.diff(a, G2)*G3
        self.zero(4*q**2*Da+a**2+2*s*a - 8*q**2/G1*(2*q**2*G3+3*s*G2))
        basis = [sp.Integer(1), t, q]
        for e in basis:
            self.zero(2*q**2*dt(dt(dt(e)))+3*s*dt(dt(e)))
        wronskian = sp.Matrix([basis, [dt(e) for e in basis], [dt(dt(e)) for e in basis]]).det()
        self.zero(wronskian + 1/(4*q**3))
        alpha, beta, gamma, delta = sp.symbols("alpha beta gamma delta")
        solved_g = alpha*t+beta*q+gamma
        solved_a = 4*q**2*dt(dt(solved_g))/dt(solved_g)
        solved_b = delta/dt(solved_g)
        self.zero(solved_a+beta/(q*dt(solved_g)))
        self.zero(4*q**2*dt(solved_b)+solved_a*solved_b)

        Yf = y + t*X
        Zf = z + (qt*y + R*rho)*X + q*X**2
        Wf = w + theta*X + rho*X**2
        self.zero(Zf**2-X**2*Yf*(X-Yf)-2*X*Wf - (z**2-2*X*g0))
        Y, Z, W, C = sp.symbols("Y Z W C")
        graph_polynomial = Z**2-X**2*Y*(X-Y)-2*X*(W-C)
        self.zero(sp.diff(graph_polynomial, W) + 2*X)
        self.zero(graph_polynomial.subs(X, 0) - Z**2)

    def test_monomial_actual_automorphism_both_orders_and_chart(self):
        X, Y, Z, W, zv, Gv = sp.symbols("X Y Z W zv Gv")
        alpha, gamma, delta = sp.symbols("alpha gamma delta")
        beta = sp.Symbol("beta", nonzero=True)
        I = Z**2-X**2*Y*(X-Y)-2*X*(W-gamma)
        J = (2*delta-I-2*alpha*Y)/(2*beta)
        zs = Z-X*J
        Gs = W-gamma-Z*J+X*J**2/2-X*Y*(Y-X)/2
        Ji = (2*delta-zv**2+2*X*Gv-2*alpha*Y)/(2*beta)
        Zi = zv+X*Ji
        Wi = Gv+gamma+X*Y*(Y-X)/2+zv*Ji+X*Ji**2/2
        # Both orders are polynomial identities; beta is the allowed C* scalar.
        self.zero(Zi.xreplace({zv: zs, Gv: Gs})-Z)
        self.zero(Wi.xreplace({zv: zs, Gv: Gs})-W)
        self.zero(zs.xreplace({Z: Zi, W: Wi})-zv)
        self.zero(Gs.xreplace({Z: Zi, W: Wi})-Gv)
        self.zero(X*sp.diff(J, Z)+Z*sp.diff(J, W))

        r, y, z = sp.symbols("r y z")
        omega = 1+r**2
        t, q, s = r**2/omega, r/omega, (1-r**2)/omega
        H0 = (2*delta-z**2-2*alpha*y)/(2*beta)
        G = alpha*t+beta*q
        forward = {
            Y: y+t*X,
            Z: z+H0*X+q*X**2,
            W: gamma+G+z*H0+((H0**2+y**2)/2+q*z)*X+(q*H0-s*y/2)*X**2,
        }
        self.zero(I.xreplace(forward)-(z**2-2*G*X))
        self.zero(J.xreplace(forward)-(H0+q*X))
        self.zero(zs.xreplace(forward)-z)
        self.zero(Gs.xreplace(forward)-G)
        self.zero(y**2-s*y*X-q**2*X**2-(y+t*X)*(y+t*X-X))

    def test_reciprocal_literal_potentials_scalar_and_ode(self):
        r, rho, U, V, y, xi = sp.symbols("r rho U V y xi")
        g = sp.symbols("g0:4")
        g0, g1, g2, g3 = g
        omega = 1+r**2
        R, nu = r, -r*omega
        _, dr, _, qtt, kt, n, ell, S, H = self.raw_potentials(
            r, rho, U, V, g, R, nu, -r*omega**2/2
        )
        P = ((r**2-3)*omega**2*U**2/(8*r**4)
             - rho*(r**2-1)*omega*U/(2*r**2)+omega*rho**2/2)
        B1 = -r*omega**2*g1/2
        remainder = sp.cancel(H-R*nu*(V-P)**2/2-B1*U)
        self.zero(sp.diff(remainder, U))
        self.zero(sp.diff(remainder, V))
        C, eps = omega/r, -omega**2/(2*r**3)
        h = C*rho+eps*y
        z = xi+h*y
        w = h*z-h**2*y/2+g0
        theta = P.subs(U, y)+xi/r
        self.zero(qtt*y**2/2+kt*y+R*theta+n-z)
        self.zero((ell-S.subs({U: y, V: theta}))/R-w)

        yr, yp, yx = sp.symbols("yr yp yx")
        derivatives = [
            lambda e: dr(e)+yr*sp.diff(e, y),
            lambda e: sp.diff(e, rho)+yp*sp.diff(e, y),
            lambda e: sp.diff(e, xi)+yx*sp.diff(e, y),
        ]
        J = sp.Matrix([[D(e) for D in derivatives] for e in [y, z, w]]).det()
        expected = g1*yp+xi*((sp.diff(C,r)*rho+sp.diff(eps,r)*y)*yp-C*yr)-y*g1*C*yx
        self.zero(J-expected)
        AA, Ar, BB, Br, Bp = sp.symbols("AA Ar BB Br Bp")
        projected = sp.expand(expected.subs({y: AA*xi**2+BB, yr: Ar*xi**2+Br, yp: Bp, yx: 2*AA*xi}))
        self.zero(projected.coeff(xi,3)-(sp.diff(eps,r)*AA*Bp-C*Ar-2*g1*C*AA**2))
        self.zero(projected.coeff(xi,1)-((sp.diff(C,r)*rho+sp.diff(eps,r)*BB)*Bp-C*Br-2*g1*C*AA*BB))
        self.zero(projected.coeff(xi,0)-g1*Bp)
        A = -1/(r*omega*g1)
        a = 2*r**2*(r*g2+3*g1)/((r**2-3)*g1)
        self.zero(sp.diff(eps,r)*A*a-C*dr(A)-2*g1*C*A**2)
        residual = (sp.diff(C,r)+sp.diff(eps,r)*a)*a-C*dr(a)-2*g1*C*A*a
        ode = r**2*(r**2-3)*g3+6*r*(r**2-4)*g2+6*(r**2-6)*g1
        self.zero(residual+2*omega*ode/((r**2-3)**2*g1))

    def test_reciprocal_basis_parameter_and_field_relation_controls(self):
        r, rho, xi, h, y, z, H, Svar, p = sp.symbols("r rho xi h y z H Svar p")
        alpha, gamma, delta = sp.symbols("alpha gamma delta")
        beta = sp.Symbol("beta", nonzero=True)
        omega = 1+r**2
        basis = [sp.Integer(1), r**-2, omega/r**3]
        for e in basis:
            self.zero(r**2*(r**2-3)*sp.diff(e,r,3)+6*r*(r**2-4)*sp.diff(e,r,2)+6*(r**2-6)*sp.diff(e,r))
        wronskian = sp.Matrix([[sp.diff(e,r,j) for e in basis] for j in range(3)]).det()
        self.zero(wronskian-2*(r**2-3)/r**8)
        g = alpha/r**2+beta*omega/r**3+gamma
        D = 2*alpha*r+beta*r**2+3*beta
        A, a = r**3/(omega*D), 2*beta*r**2/D
        C, eps = omega/r, -omega**2/(2*r**3)
        self.zero(sp.diff(g,r)+D/r**4)
        self.zero(A+1/(r*omega*sp.diff(g,r)))
        self.zero(a-2*r**2*(r*sp.diff(g,r,2)+3*sp.diff(g,r))/((r**2-3)*sp.diff(g,r)))
        b = delta*A
        self.zero(sp.diff(eps,r)*a*b-C*sp.diff(b,r)-2*sp.diff(g,r)*C*A*b)
        T = g-gamma
        projected_y = A*xi**2+a*rho+b
        projected_h = C*rho+eps*projected_y
        self.zero(beta*projected_h-(T+alpha)*projected_y+(xi**2+delta)/2)
        self.zero(beta*(C/a+eps)-(T+alpha))
        self.zero(beta*C*A/a-sp.Rational(1,2))
        self.zero(T.subs(r,1/p)-(beta*p**3+alpha*p**2+beta*p))

        # Polynomial identities and degree/primitive slots, not irreducibility tests.
        cubic = beta*H**3+alpha*H**2+beta*H-Svar
        self.zero(cubic.subs({H:p, Svar:T.subs(r,1/p)}))
        self.assertEqual(sp.Poly(cubic,H).degree(), 3)
        self.zero(sp.Poly(cubic,H).LC()-beta)
        self.zero(sp.diff(cubic,Svar)+1)
        graph_w = z*h-y*h**2/2
        graph_polynomial = y*H**2-2*z*H+2*Svar
        self.zero(graph_polynomial.subs({H:h, Svar:graph_w}))
        self.assertEqual(sp.Poly(graph_polynomial,H).degree(), 2)
        self.zero(sp.diff(graph_polynomial,Svar)-2)


if __name__ == "__main__":
    unittest.main()
