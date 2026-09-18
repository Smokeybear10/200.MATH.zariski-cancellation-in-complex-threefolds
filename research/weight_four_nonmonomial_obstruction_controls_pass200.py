"""Finite exact algebra controls for the two normalized nonmonomial branches.

The written pass199 normalization and pass200 graph/projection proofs supply
the actual hypotheses.  These independent symbolic identities do not prove
actual realization, full initial kernels, field return, exact-field ODE
completeness, irreducibility, or geometric exclusion.  No older checker or
proof/solver implementation is imported.  Root owns canonical execution.
"""

import unittest

import sympy as sp


class NonmonomialObstructionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def polynomial_zero(self, expression, *variables):
        # Simplify coefficients separately; avoid one expanded rational numerator.
        for coefficient in sp.Poly(sp.expand(expression), *variables).coeffs():
            self.zero(coefficient)

    def test_literal_potentials_square_and_short_projected_entries(self):
        q, rho, U, V, m, xi = sp.symbols("q rho U V m xi")
        g = sp.Function("g")(q)
        dt = lambda value: sp.factor(sp.diff(value, q) / (2 * q))
        R = 1 / (q * (q + 1))
        nu = 1 / (q**3 * (q + 1)**3 * (3 * q - 1))
        L3 = -(q**2 + 4*q - 1) / (2*q**5*(q+1)**5*(3*q-1)**3)
        k, n, ell = R*rho, nu*rho**2/2, L3*rho**3 + R*g
        Q = dt(dt(q)) / 2
        d, e4 = dt(dt(dt(q))) / 6, dt(dt(dt(dt(q)))) / 24
        self.zero(Q + 1 / (8*q**3))
        self.zero(d - 1 / (16*q**5))
        self.zero(e4 + 5 / (128*q**7))

        S = (d*U**3 + dt(dt(k))*U**2/2 + dt(R)*U*V
             + dt(n)*U + sp.diff(n, rho)*V)
        T = (e4*U**4 + dt(dt(dt(k)))*U**3/6
             + dt(dt(R))*U**2*V/2 + dt(dt(n))*U**2/2
             + dt(sp.diff(n, rho))*U*V + nu*V**2/2)
        H = (R*(T - dt(ell)*U - sp.diff(ell, rho)*V - m)
             + (dt(R)*U + nu*rho)*(ell-S))
        p2 = -(q+1)*(3*q-1)/(8*q**2)
        p1 = (9*q**2+4*q-1)/(2*q**2*(q+1)*(3*q-1))
        p0 = -(3*q**2+6*q-1)/(2*q**2*(q+1)**2*(3*q-1)**2)
        P = p2*U**2 + p1*rho*U + p0*rho**2
        A2 = R*nu/2
        B0 = -R*m + nu*rho*R*g + (nu*L3 - R*nu*p0**2/2)*rho**4
        completed = A2*(V-P)**2 - R**2*sp.diff(g, q)*U/(2*q) + B0
        self.polynomial_zero(H-completed, U, V, rho)

        # xi = R*zeta.  This scaling is important in the projection branch.
        theta = P + xi/R
        z_raw = Q*U**2 + dt(k)*U + R*theta + n
        w_raw = (ell-S.subs(V, theta))/R
        D = q*(q+1)*(3*q-1)
        h = U/(2*q) - rho/D
        z_short = xi-sp.Rational(3, 2)*h**2
        w_short = (h+U)*z_short+h**3/2+g
        self.polynomial_zero(z_raw-z_short, U, rho, xi)
        self.polynomial_zero(w_raw-w_short, U, rho, xi)
        e = q/(3*q-1)
        self.zero(q*nu/R**3-e)
        # The y coefficient comes from H=A2*zeta^2+B1*y+B0.
        self.zero(-A2 / (R**2*(-R**2*sp.diff(g, q)/(2*q)))
                  - e/sp.diff(g, q))

    def test_graph_scalar_and_cubic_degree_controls(self):
        q, rho, y = sp.symbols("q rho y")
        xi = sp.Function("xi")(q, rho)
        D = q*(q+1)*(3*q-1)
        h = y/(2*q)-rho/D
        z = xi-sp.Rational(3, 2)*h**2
        omega = h*xi-h**3
        raw = sp.Matrix([y, z, omega]).jacobian([q, rho, y]).det()
        expected = xi*(-sp.diff(xi, q)/D
                       + y*sp.diff(xi, rho)/(2*q**2)
                       - rho*sp.diff(D, q)*sp.diff(xi, rho)/D**2)
        self.polynomial_zero(raw-expected, y)
        self.zero(sp.Poly(sp.expand(expected), y).coeff_monomial(y)
                  - xi*sp.diff(xi, rho)/(2*q**2))
        self.zero(expected.subs(sp.diff(xi, rho), 0)
                  + xi*sp.diff(xi, q)/D)
        self.zero(expected.subs({xi: 0, sp.diff(xi, rho): 0,
                                sp.diff(xi, q): 0}, simultaneous=True))

        # Formal independent variables for the written generic degree argument.
        h0, z0, x0, S, H = sp.symbols("h0 z0 xi0 S H")
        forward_z = x0-sp.Rational(3, 2)*h0**2
        inverse_xi = z0+sp.Rational(3, 2)*h0**2
        self.zero(forward_z.subs(x0, inverse_xi)-z0)
        self.zero(inverse_xi.subs(z0, forward_z)-x0)
        omega0 = z0*h0+h0**3/2
        cubic = H**3+2*z0*H-2*S
        self.zero(cubic.subs({H: h0, S: omega0}, simultaneous=True))
        self.assertEqual(sp.Poly(cubic, H).degree(), 3)
        self.assertEqual(sp.Poly(cubic, S).coeff_monomial(S), -2)
        # These coefficients support, but do not replace, the written Gauss proof.

    def test_projection_raw_jets_scalar_coefficients_and_ode(self):
        q, rho, xi = sp.symbols("q rho xi")
        Y, Yq, Yr, Yx, Gq = sp.symbols("Y Yq Yr Yxi Gq")
        D = q*(q+1)*(3*q-1)
        h = Y/(2*q)-rho/D
        hq = Yq/(2*q)-Y/(2*q**2)+rho*sp.diff(D, q)/D**2
        hr, hx = Yr/(2*q)-1/D, Yx/(2*q)
        dy = sp.Matrix([[Yq, Yr, Yx]])
        dh = sp.Matrix([[hq, hr, hx]])
        dxi = sp.Matrix([[0, 0, 1]])
        dz = dxi-3*h*dh
        domega = h*dxi+(xi-3*h**2)*dh+sp.Matrix([[Gq, 0, 0]])
        raw = dy.col_join(dz).col_join(domega).det()
        expected = (Gq*Yr
                    + xi*((-Y/(2*q**2)+rho*sp.diff(D, q)/D**2)*Yr+Yq/D)
                    - 3*h*Gq*Yx/D)
        self.polynomial_zero(raw-expected, Y, Yq, Yr, Yx, xi, rho)

        g = sp.Function("g")(q)
        offset = sp.Function("offset")(q, rho)
        e = q/(3*q-1)
        A = e/sp.diff(g, q)
        replacements = {
            Y: A*xi**2+offset, Yq: sp.diff(A, q)*xi**2+sp.diff(offset, q),
            Yr: sp.diff(offset, rho), Yx: 2*A*xi, Gq: sp.diff(g, q),
        }
        specialized = expected.subs(replacements, simultaneous=True)
        c3 = (-A*sp.diff(offset, rho)/(2*q**2)+sp.diff(A, q)/D
              - 3*sp.diff(g, q)*A**2/(q*D))
        c1 = ((-offset/(2*q**2)+rho*sp.diff(D, q)/D**2)*sp.diff(offset, rho)
              + sp.diff(offset, q)/D-3*e*offset/(q*D)+6*e*rho/D**2)
        c0 = sp.diff(g, q)*sp.diff(offset, rho)
        self.polynomial_zero(specialized-c3*xi**3-c1*xi-c0, xi)
        a = -2*(q*(3*q-1)*sp.diff(g, q, 2)+(3*q+1)*sp.diff(g, q)) / (
            (q+1)*(3*q-1)**2*sp.diff(g, q))
        self.zero(a - 2*q**2/D*(sp.diff(A, q)/A-3*e/q))
        riccati = (-a**2/(2*q**2)+sp.diff(D, q)*a/D**2+sp.diff(a, q)/D
                   -3*e*a/(q*D)+6*e/D**2)
        ode = (3*q-1)*sp.diff(g, q, 3)+9*sp.diff(g, q, 2)
        self.zero(riccati+2*ode/((q+1)**2*(3*q-1)**3*sp.diff(g, q)))
        beta_extracted = (3*q-1)**3*sp.diff(g, q, 2)/18
        alpha_extracted = sp.diff(g, q)+(3*q-1)*sp.diff(g, q, 2)/6
        gamma_extracted = g-alpha_extracted*q-beta_extracted/(3*q-1)
        self.zero(sp.diff(beta_extracted, q)-(3*q-1)**2*ode/18)
        self.zero(sp.diff(alpha_extracted, q)-ode/6)
        self.zero(sp.diff(gamma_extracted, q)+(6*q-1)*ode/18)

    def test_projection_solutions_parameter_quartic_and_primitive_slots(self):
        q, rho, y, h, xi, z, w, H = sp.symbols("q rho y h xi z w H")
        alpha, beta, gamma, delta = sp.symbols("alpha beta gamma delta")
        D = q*(q+1)*(3*q-1)
        e = q/(3*q-1)
        g = alpha*q+beta/(3*q-1)+gamma
        den = alpha*(3*q-1)**2-3*beta
        A = q*(3*q-1)/den
        a = -2*(9*alpha*q**2-alpha+3*beta)/((q+1)*(3*q-1)*den)
        b = delta*A
        T = g-gamma
        self.zero((3*q-1)*sp.diff(g, q, 3)+9*sp.diff(g, q, 2))
        self.zero(A-e/sp.diff(g, q))
        self.zero(a-2*q**2/D*(sp.diff(A, q)/A-3*e/q))
        self.zero(sp.diff(b, q)-(a*D/(2*q**2)+3*e/q)*b)
        # Each one-constant boundary is included, with the other constant nonzero.
        for replacement in ({alpha: 0}, {beta: 0}):
            self.zero((A-e/sp.diff(g, q)).subs(replacement))
            self.zero((sp.diff(b, q)-sp.diff(A, q)*b/A).subs(replacement))
        self.zero((1-a*D/(2*q))/A-6*alpha)
        self.zero(-a*D/A-6*T-2*alpha)

        parameter = xi**2+delta+(6*T+2*alpha)*h-6*alpha*y
        cover_equation = y-A*(xi**2+delta)-a*rho
        self.polynomial_zero(
            cover_equation.subs(rho, D*(y/(2*q)-h))+A*parameter, y, xi, h)
        T0 = sp.symbols("T0")
        independent_parameter = xi**2+delta+(6*T0+2*alpha)*h-6*alpha*y
        quartic = (3*H**4+12*z*H**2
                   -(24*(w-y*z-gamma)+8*alpha)*H
                   +24*alpha*y-4*z**2-4*delta)
        eliminated = independent_parameter.subs({
            xi: z+sp.Rational(3, 2)*h**2,
            T0: w-y*z-h*z-h**3/2-gamma,
        }, simultaneous=True)
        self.polynomial_zero(4*eliminated+quartic.subs(H, h), h, y, z, w)
        self.assertEqual(sp.Poly(quartic, H).degree(), 4)
        self.assertEqual(sp.Poly(quartic, H).LC(), 3)
        self.assertEqual(sp.Poly(quartic, w).coeff_monomial(w), -24*H)
        constant_mod_H = quartic.subs({H: 0, w: 0})
        self.zero(constant_mod_H-(24*alpha*y-4*z**2-4*delta))
        self.assertEqual(sp.Poly(constant_mod_H, z).coeff_monomial(z**2), -4)
        # The universal primitive/irreducibility and actual-field conclusions
        # remain written arguments, not assertions established by this suite.


if __name__ == "__main__":
    unittest.main()
