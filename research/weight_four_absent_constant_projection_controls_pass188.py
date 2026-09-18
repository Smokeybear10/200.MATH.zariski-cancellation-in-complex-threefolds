"""Finite controls for the absent-variable constant-projection exclusion188.

The charts and coefficient jets below are formal. Actual polynomiality and
local nilpotence of P, invariant primitive division, exact coefficient fields,
kernel contraction and Wang's theorem belong to the written proof. Invariant
Delta is explicitly imposed in the iterate control, not inferred from a test.
The unit-ideal inverse is a genuine polynomial identity over constant
coefficients; it is kept separate from the nonunit-ideal kernel argument.
No earlier checker is imported. Authored source-only; Root owns execution.
"""

import unittest

import sympy as sp


class AbsentConstantProjectionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_determinant_and_constant_ratio_jets(self):
        X, t, y, theta = sp.symbols("X t y theta")
        R, A, K, rho, alpha, beta, g = sp.symbols("R A K rho alpha beta g")
        Rt, At, Kt, rhot, alphat, betat, gt = sp.symbols(
            "R_t A_t K_t rho_t alpha_t beta_t g_t")
        Ry, Ay, Ky, rhoy, alphay, betay, gy = sp.symbols(
            "R_y A_y K_y rho_y alpha_y beta_y g_y")
        coefficients = (R, A, K, rho, alpha, beta, g)
        t_jets = (Rt, At, Kt, rhot, alphat, betat, gt)
        y_jets = (Ry, Ay, Ky, rhoy, alphay, betay, gy)

        def dt(expression):
            return sp.diff(expression, t) + sum(
                sp.diff(expression, c) * dc
                for c, dc in zip(coefficients, t_jets))

        def dy(expression):
            return sp.diff(expression, y) + sum(
                sp.diff(expression, c) * dc
                for c, dc in zip(coefficients, y_jets))

        w = alpha * theta**2 + beta * theta + g
        chart = (y + t*X, R*theta + A + K*X + t**4*X**2,
                 w + theta*X + rho*X**2)
        rows = sp.Matrix([[dt(f), dy(f), sp.diff(f, theta)] for f in chart])
        determinant = sp.expand(rows.det())
        literal = (
            (2*alpha*theta + beta + X)
            * (-Rt*theta - At
               + X*(Ry*theta + Ay - Kt)
               + X**2*(Ky - 4*t**3))
            + R*(dt(w) - X*dy(w) + rhot*X**2 - rhoy*X**3)
        )
        self.zero(determinant - literal)
        theta_square = determinant.coeff(X, 0).coeff(theta, 2)
        x_theta_square = determinant.coeff(X, 1).coeff(theta, 2)
        self.zero(theta_square - (R*alphat - 2*alpha*Rt))
        self.zero(x_theta_square - (2*alpha*Ry - R*alphay))
        self.zero(R**3 * dt(alpha/R**2) - theta_square)
        self.zero(R**3 * dy(alpha/R**2) + x_theta_square)

        c = sp.symbols("c")
        constant_ratio = {alpha: c*R**2, alphat: 2*c*R*Rt,
                          alphay: 2*c*R*Ry}
        self.zero(theta_square.subs(constant_ratio, simultaneous=True))
        self.zero(x_theta_square.subs(constant_ratio, simultaneous=True))
        # The implication that this ratio lies in C uses the exact joint
        # constant field proved in the note. The c=0 specialization is allowed.

    def test_iterates_with_explicit_invariant_primitive_factor(self):
        X, theta = sp.symbols("X theta")
        a, gamma, R, Delta = sp.symbols("a gamma R Delta", nonzero=True)
        t, y, rho, A, K, beta, g, c = sp.symbols("t y rho A K beta g c")
        alpha = c*R**2
        Z = R*theta + A + K*X + t**4*X**2
        W = alpha*theta**2 + beta*theta + g + theta*X + rho*X**2
        rate = a*gamma
        P = lambda expression: rate*sp.diff(expression, theta)
        D = lambda expression: P(expression)/Delta
        E = lambda expression: a*sp.diff(expression, X)

        # Delta and all displayed field coefficients are independent of X
        # and theta here. These are the proved invariance hypotheses, not
        # conclusions supplied by this formal chart.
        self.zero(P(Delta))
        self.zero(E(Delta))
        self.zero(P(X))
        self.zero(P(y + t*X))
        self.zero(P(Z) - rate*R)
        self.zero(P(P(Z)))
        self.zero(P(P(P(W))))
        self.zero(P(P(W)) - 2*c*P(Z)**2)
        self.zero(Delta**2*D(D(W)) - P(P(W)))
        self.zero(Delta**2*(D(D(W)) - 2*c*D(Z)**2))
        for expression in (X, y + t*X, Z, W):
            self.zero(Delta*(E(D(expression)) - D(E(expression))))

        # A noninvariant divisor changes the second-iterate identity.
        # This rational negative control is not a candidate primitive LND.
        d0 = sp.symbols("d0")
        bad_delta = theta + d0
        bad_D = lambda expression: sp.diff(expression, theta)/bad_delta
        residual = bad_D(bad_D(theta**2)) - 2*bad_D(theta)**2
        self.zero(sp.cancel(bad_delta**3*residual) + 2*theta)
        self.assertNotEqual(sp.cancel(residual), 0)

    def test_affine_unit_inverse_and_time_leading_obstructions(self):
        X, Y, Z, W, T, F = sp.symbols("X Y Z W T F")
        B, C, lam, mu = sp.symbols("B C lam mu")
        direct_T, direct_F = lam*Z + mu*W, B*W - C*Z
        inverse_Z, inverse_W = B*T - mu*F, C*T + lam*F
        bezout = lam*B + mu*C
        self.zero(inverse_Z.subs({T: direct_T, F: direct_F}, simultaneous=True)
                  - bezout*Z)
        self.zero(inverse_W.subs({T: direct_T, F: direct_F}, simultaneous=True)
                  - bezout*W)
        self.zero(direct_T.subs({Z: inverse_Z, W: inverse_W}, simultaneous=True)
                  - bezout*T)
        self.zero(direct_F.subs({Z: inverse_Z, W: inverse_W}, simultaneous=True)
                  - bezout*F)

        b0, bx, by, c0, cx, cy = sp.symbols("b0 bx by c0 cx cy")
        l0, m0 = sp.symbols("l0 m0", nonzero=True)
        affine_B = b0 + bx*X + by*Y
        affine_C = c0 + cx*X + cy*Y
        cases = (
            {B: affine_B, C: (1-l0*affine_B)/m0, lam: l0, mu: m0},
            {B: 1/l0, C: affine_C, lam: l0, mu: 0},
        )
        for parameters in cases:
            self.zero(bezout.subs(parameters, simultaneous=True) - 1)
            fwd = (direct_T.subs(parameters, simultaneous=True),
                   direct_F.subs(parameters, simultaneous=True))
            inv = (inverse_Z.subs(parameters, simultaneous=True),
                   inverse_W.subs(parameters, simultaneous=True))
            self.zero(inv[0].subs({T: fwd[0], F: fwd[1]}, simultaneous=True) - Z)
            self.zero(inv[1].subs({T: fwd[0], F: fwd[1]}, simultaneous=True) - W)
            self.zero(fwd[0].subs({Z: inv[0], W: inv[1]}, simultaneous=True) - T)
            self.zero(fwd[1].subs({Z: inv[0], W: inv[1]}, simultaneous=True) - F)

        # Primitive gcd is not a unit ideal. This nonunit control has no
        # constant Bezout companion; the written proof uses contraction.
        nonunit_F = X*W - Y*Z
        self.zero(X*sp.diff(nonunit_F, Z) + Y*sp.diff(nonunit_F, W))
        self.zero(bezout.subs({B: X, C: Y}, simultaneous=True).subs({X: 0, Y: 0}))
        for coordinate in (X, Y, Z, W):
            self.zero(sp.diff(nonunit_F, coordinate).subs(
                {X: 0, Y: 0, Z: 0, W: 0}, simultaneous=True))

        u, t, rho = sp.symbols("u t rho")
        a = sp.symbols("a", nonzero=True)
        x0, y0, z0, w0, z1, w1 = sp.symbols("x0 y0 z0 w0 z1 w1")
        time_X, time_Y = x0 + a*u, y0 + a*t*u
        time_Z = z0 + z1*u + a**2*t**4*u**2
        time_W = w0 + w1*u + a**2*rho*u**2
        time_B = affine_B.subs({X: time_X, Y: time_Y}, simultaneous=True)
        time_C = affine_C.subs({X: time_X, Y: time_Y}, simultaneous=True)
        time_F = sp.expand(time_B*time_W - time_C*time_Z)
        self.zero(time_F.coeff(u, 3)
                  - a**3*((bx+by*t)*rho - (cx+cy*t)*t**4))
        self.zero(time_F.coeff(u, 3).coeff(rho, 1) - a**3*(bx+by*t))
        constant_B = sp.expand(time_F.subs({bx: 0, by: 0}, simultaneous=True))
        self.zero(constant_B.coeff(u, 3) + a**3*(cx+cy*t)*t**4)
        both_constant = sp.expand(constant_B.subs({cx: 0, cy: 0}, simultaneous=True))
        self.zero(both_constant.coeff(u, 2) - a**2*(b0*rho-c0*t**4))
        self.zero(both_constant.coeff(u, 2).coeff(rho, 1) - a**2*b0)

        eta = sp.symbols("eta", nonzero=True)
        q0, q1, q2, q3 = sp.symbols("q0 q1 q2 q3")
        affine_obstruction = 2*eta*(bx+by*t)*t**4 + q0+q1*t+q2*t**2+q3*t**3
        constant_obstruction = 2*eta*b0*t**4 + q0+q1*t+q2*t**2
        self.zero(sp.expand(affine_obstruction).coeff(t, 5) - 2*eta*by)
        self.zero(sp.expand(affine_obstruction).coeff(t, 4) - 2*eta*bx)
        self.zero(sp.expand(constant_obstruction).coeff(t, 4) - 2*eta*b0)
        # Nonzero leading parts, transcendental t,rho, primitive LND
        # construction and Wang's alternatives remain written-proof steps.


if __name__ == "__main__":
    unittest.main()
