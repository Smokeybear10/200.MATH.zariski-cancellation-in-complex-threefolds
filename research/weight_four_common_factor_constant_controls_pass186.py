"""Bounded exact controls for the common-factor constant-y exclusion186.

The coefficient jets and Taylor charts here are formal. These finite identities
do not supply an actual inverse, the full initial kernel, the exact coefficient
field, transcendence, kernel contraction, or Wang's classification. Those are
written inputs or arguments in the companion proof. No earlier checker is
imported. This file is authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


class WeightFourCommonFactorConstantControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_quartic_chart_and_staged_theta_rigidity(self):
        t, y, X, theta = sp.symbols("t y X theta")
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
        Y = y + t * X
        W = w + theta * X + rho * X**2
        Z = R * theta + A + K * X + t**4 * X**2 - t * W
        raw = sp.Matrix([[dt(f), dy(f), sp.diff(f, theta)] for f in (Y, Z, W)])
        reduced = raw.copy()
        reduced[1, :] = raw[1, :] + t * raw[2, :]
        expected_middle = [
            Rt * theta + At - w + (Kt - theta) * X + (4*t**3 - rho) * X**2,
            Ry * theta + Ay + Ky * X,
            R,
        ]
        for actual, expected in zip(reduced[1, :], expected_middle):
            self.zero(actual - expected)
        determinant = sp.expand(raw.det())
        self.zero(determinant - reduced.det())
        literal = (
            (sp.diff(w, theta) + X)
            * (w - Rt * theta - At
               + X * ((Ry + 1) * theta + Ay - Kt)
               + X**2 * (Ky + rho - 4*t**3))
            + R * (dt(w) - X*dy(w) + rhot*X**2 - rhoy*X**3)
        )
        self.zero(determinant - literal)

        # Independently isolate the new quartic term from the literal rows.
        split_rows = sp.Matrix([
            [dt(f), dy(f), sp.diff(f, theta)] for f in (Y, Z-t**4*X**2, W)])
        self.zero(determinant - split_rows.det()
                  + 4*t**3*X**2*(sp.diff(w, theta) + X))
        self.zero(determinant.coeff(X, 0).coeff(theta, 3) - 2*alpha**2)

        # Alpha=0 is a field inference in the proof. Its partials also vanish.
        affine = sp.expand(determinant.subs(
            {alpha: 0, alphat: 0, alphay: 0}, simultaneous=True))
        self.zero(affine.coeff(X, 2).coeff(theta, 1) - (Ry + 1))
        x_theta = affine.coeff(X, 1).coeff(theta, 1)
        self.zero(x_theta - (beta - Rt + beta*(Ry + 1) - R*betay))
        preceding = sp.expand(x_theta.subs(Ry, -1))
        self.zero(preceding - (beta - Rt - R*betay))
        theta_only = affine.coeff(X, 0).coeff(theta, 1)
        self.zero(theta_only - (beta*(beta - Rt) + R*betat))
        self.zero(theta_only - beta*preceding - R*(betat + beta*betay))

        rprime, rsecond, d, dprime = sp.symbols("r_prime r_second d d_prime")
        forced_beta = rprime + d/R
        forced_t = (sp.diff(forced_beta, R)*rprime
                    + sp.diff(forced_beta, rprime)*rsecond
                    + sp.diff(forced_beta, d)*dprime)
        forced_y = -sp.diff(forced_beta, R)
        burgers = sp.expand(forced_t + forced_beta*forced_y)
        self.zero(burgers - (rsecond + dprime/R + d**2/R**3))
        self.zero(R**3*burgers - (rsecond*R**3 + dprime*R**2 + d**2))
        # Coefficient vanishing additionally needs the written transcendence
        # of R over ker(partial_y); it is not asserted from these jets.

    def test_original_derivation_local_kernel_and_time_leading_obstruction(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        mu, nu = sp.symbols("mu nu")
        F = (X + mu)*Z + (Y - nu)*W

        def T(expression):
            return (nu - Y)*sp.diff(expression, Z) + (X + mu)*sp.diff(expression, W)

        for value in (X, Y, F):
            self.zero(T(value))
        self.zero(T(Z) - (nu - Y))
        self.zero(T(W) - (X + mu))
        self.zero(T(T(Z)))
        self.zero(T(T(W)))

        t, y, theta, rho, g, A, K = sp.symbols("t y theta rho g A K")
        a = sp.Symbol("a", nonzero=True)
        R = mu*t + nu - y
        chart_y = y + t*X
        chart_w = mu*theta + g + theta*X + rho*X**2
        chart_z = R*theta + A + K*X + t**4*X**2 - t*chart_w
        self.zero(sp.diff(chart_z, theta) - (nu - chart_y))
        self.zero(sp.diff(chart_w, theta) - (X + mu))
        chart_F = (X + mu)*chart_z + (chart_y - nu)*chart_w
        self.zero(sp.diff(chart_F, theta))
        for value in (X, chart_y, chart_z, chart_w):
            self.zero(a*sp.diff(sp.diff(value, theta), X)
                      - sp.diff(a*sp.diff(value, X), theta))
        # The preceding calculation uses a in L and holds X,theta independent.
        # Original-ring restriction is justified by the exact component values.

        p = sp.Symbol("p", nonzero=True)
        q0, F0, W0 = sp.symbols("q0 F0 W0")
        local_Z = (F0 + q0*W0)/p
        self.zero(p*local_Z - q0*W0 - F0)
        self.zero(p*sp.diff(local_Z, W0) - q0)
        self.zero(p*sp.diff(W0, W0) - p)
        # Removing the p denominator requires the written mod-p contraction
        # argument. These local formulas alone do not prove the full kernel.

        u, x0, y0, z0, w0, z1, w1 = sp.symbols("u x0 y0 z0 w0 z1 w1")
        time_X = x0 + a*u
        time_Y = y0 + a*t*u
        time_Z = z0 + z1*u + a**2*(-t*rho + t**4)*u**2
        time_W = w0 + w1*u + a**2*rho*u**2
        time_F = sp.expand((time_X + mu)*time_Z + (time_Y - nu)*time_W)
        self.assertEqual(sp.degree(time_F, u), 3)
        self.zero(time_F.coeff(u, 3) - a**3*t**4)
        c = sp.Symbol("c", nonzero=True)
        q30, q21, q12, q03 = sp.symbols("q30 q21 q12 q03")
        Q3 = q30*X**3 + q21*X**2*Y + q12*X*Y**2 + q03*Y**3
        time_Q3 = sp.expand(Q3.subs({X: time_X, Y: time_Y}, simultaneous=True))
        obstruction = c*t**4 + q30 + q21*t + q12*t**2 + q03*t**3
        self.zero(sp.expand(c*time_F + time_Q3).coeff(u, 3) - a**3*obstruction)
        self.assertEqual(sp.degree(obstruction, t), 4)
        self.assertEqual(sp.expand(obstruction).coeff(t, 4), c)
        # The written proof, not this finite coefficient check, supplies
        # transcendental t and Wang's invariant cF+Q(X,Y).
        for degree in (1, 2, 4, 5):
            cs = sp.symbols(f"q{degree}_0:{degree+1}")
            homogeneous = sum(cs[i]*X**(degree-i)*Y**i for i in range(degree+1))
            time_form = sp.expand(homogeneous.subs(
                {X: time_X, Y: time_Y}, simultaneous=True))
            self.zero(time_form.coeff(u, degree)
                      - a**degree*sum(cs[i]*t**i for i in range(degree+1)))


if __name__ == "__main__":
    unittest.main()
