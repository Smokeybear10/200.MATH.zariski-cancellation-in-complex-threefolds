"""Independent finite controls for the unified constant-y split exclusion176.

The formal theta chart checks the literal determinant, each X coefficient,
and the explicitly staged prior-relation substitutions.  The displayed T0
is a polynomial locally nilpotent derivation; its commutation with E is
checked in a formal coefficient chart, not a newly supplied dense frame.
Kernel localization identities and finite monomial signatures support the
written coefficient proof, without replacing its universal argument.

The arbitrary-Q Hessian calculation uses independent second jets and a
separate higher-degree polynomial fixture.  No test proves the coefficient
field gates, Wang's theorem, existence of an invariant correction, or
recognition of a fourfold.  No earlier checker is imported.  Root executes
only after complete saved-source review.
"""

import unittest

import sympy as sp


class SplitConstantProjectionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_theta_determinant_and_staged_rigidity(self):
        x, t, y, v = sp.symbols("x t y v")
        R, A, K, rho, alpha, beta, g = [
            sp.Function(name)(t, y)
            for name in ("R", "A", "K", "rho", "alpha", "beta", "g")
        ]
        w = alpha * v**2 + beta * v + g
        Y = y + t * x
        W = w + v * x + rho * x**2
        Z = R * v + A - t * w + (K - t * v) * x - t * rho * x**2
        self.zero(Z + t * W - (R * v + A + K * x))
        literal = sp.Matrix([Y, Z, W]).jacobian((t, y, v))
        reduced = literal.copy()
        reduced[1, :] = literal[1, :] + t * literal[2, :]
        expected = sp.Matrix([
            [x, 1, 0],
            [sp.diff(R, t) * v + sp.diff(A, t) - w
             + (sp.diff(K, t) - v) * x - rho * x**2,
             sp.diff(R, y) * v + sp.diff(A, y) + sp.diff(K, y) * x, R],
            [sp.diff(w, t) + sp.diff(rho, t) * x**2,
             sp.diff(w, y) + sp.diff(rho, y) * x**2, sp.diff(w, v) + x],
        ])
        for entry in reduced - expected:
            self.zero(entry)
        J = sp.expand(literal.det())
        self.zero(J - reduced.det())
        B0 = w - sp.diff(R, t) * v - sp.diff(A, t)
        B1 = (sp.diff(R, y) + 1) * v + sp.diff(A, y) - sp.diff(K, t)
        B2 = sp.diff(K, y) + rho
        coefficients = [
            B0 * sp.diff(w, v) + R * sp.diff(w, t),
            B0 + B1 * sp.diff(w, v) - R * sp.diff(w, y),
            B1 + B2 * sp.diff(w, v) + R * sp.diff(rho, t),
            B2 - R * sp.diff(rho, y),
        ]
        self.zero(J - sum(coefficient * x**i for i, coefficient in enumerate(coefficients)))
        self.zero(sp.expand(coefficients[0]).coeff(v, 3) - 2 * alpha**2)

        # First impose alpha=0, including its coefficient derivatives.
        # Only then impose the prior X^2*v consequence R_y=-1.
        alpha_zero = {alpha: 0, sp.diff(alpha, t): 0, sp.diff(alpha, y): 0}
        after_alpha = [
            sp.expand(coefficient.subs(alpha_zero, simultaneous=True))
            for coefficient in coefficients
        ]
        self.zero(after_alpha[2].coeff(v) - sp.diff(R, y) - 1)
        linear_v = after_alpha[1].coeff(v).subs(sp.diff(R, y), -1)
        constant_v = after_alpha[0].coeff(v)
        self.zero(linear_v - (beta - sp.diff(R, t) - R * sp.diff(beta, y)))
        self.zero(constant_v - (beta**2 - beta * sp.diff(R, t) + R * sp.diff(beta, t)))
        self.zero(constant_v - beta * linear_v
                  - R * (sp.diff(beta, t) + beta * sp.diff(beta, y)))

        # Independent first/second jets for R=r(t)-y and beta=r_t+d/R.
        # Dt(R)=r1 and Dy(R)=-1.  Clearing powers of the nonzero R is
        # legitimate in this field calculation, not an integral-unit claim.
        R0 = sp.Symbol("R0", nonzero=True)
        r1, r2, d, d1 = sp.symbols("r1 r2 d d1")
        beta_jet = r1 + d / R0
        Dt_beta = r1 * sp.diff(beta_jet, R0) + r2 * sp.diff(beta_jet, r1) + d1 * sp.diff(beta_jet, d)
        Dy_beta = -sp.diff(beta_jet, R0)
        self.zero(beta_jet - r1 - R0 * Dy_beta)
        self.zero(R0**3 * (Dt_beta + beta_jet * Dy_beta)
                  - (r2 * R0**3 + d1 * R0**2 + d**2))
        # Coefficient comparison itself needs the written transcendence proof.
        numerator = sp.Poly(r2 * R0**3 + d1 * R0**2 + d**2, R0)
        self.assertEqual((numerator.nth(3), numerator.nth(2), numerator.nth(0)), (r2, d1, d**2))
        mu, nu = sp.symbols("mu nu")
        R_final, beta_final = mu * t + nu - y, mu
        for expression in (
            sp.diff(R_final, y) + 1,
            beta_final - sp.diff(R_final, t) - R_final * sp.diff(beta_final, y),
            sp.diff(beta_final, t) + beta_final * sp.diff(beta_final, y),
        ):
            self.zero(expression)
            self.zero(expression.subs(mu, 0))

    def test_unified_polynomial_derivation_kernel_and_formal_commutation(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        mu, nu = sp.symbols("mu nu")  # zero mu is explicitly allowed.
        p, q, F0 = sp.symbols("p q F0")
        pp, qq = X + mu, nu - Y
        T = lambda expression: qq * sp.diff(expression, Z) + pp * sp.diff(expression, W)
        F = pp * Z - qq * W
        for coordinate, expected in zip((X, Y, Z, W), (0, 0, qq, pp)):
            self.zero(T(coordinate) - expected)
            self.zero(T(T(coordinate)))
            self.zero(T(coordinate).subs({X: -mu, Y: nu}, simultaneous=True))
        self.zero(T(F))
        self.zero(F - (X * Z + Y * W + mu * Z - nu * W))
        inverse_x, inverse_y = p - mu, nu - q
        self.zero(pp.subs({X: inverse_x, Y: inverse_y}, simultaneous=True) - p)
        self.zero(qq.subs({X: inverse_x, Y: inverse_y}, simultaneous=True) - q)
        self.zero(inverse_x.subs({p: pp, q: qq}, simultaneous=True) - X)
        self.zero(inverse_y.subs({p: pp, q: qq}, simultaneous=True) - Y)

        # Localized coordinate identities, not an inverse in the original
        # polynomial ring after dividing by its nonunit p.
        kernel_form = p * Z - q * W
        inverse_z = (F0 + q * W) / p
        self.zero(kernel_form.subs(Z, inverse_z) - F0)
        self.zero(inverse_z.subs(F0, kernel_form) - Z)
        self.zero(kernel_form.subs(p, 0) + q * W)
        # Finite signatures illustrating the written injectivity modulo p.
        signatures = set()
        for i in range(4):
            for degree in range(4):
                image = (q**i * F0**degree).subs(F0, -q * W)
                self.zero(image - (-1)**degree * q**(i + degree) * W**degree)
                self.assertNotIn((i + degree, degree), signatures)
                signatures.add((i + degree, degree))

        x, t, y, v = sp.symbols("x t y v")
        speed, rho, A, K, g = [
            sp.Function(name)(t, y) for name in ("speed", "rho", "A", "K", "g")
        ]
        R = mu * t + nu - y
        w = mu * v + g
        images = (
            x, y + t * x,
            R * v + A - t * w + (K - t * v) * x - t * rho * x**2,
            w + v * x + rho * x**2,
        )
        expected = (0, 0, nu - images[1], images[0] + mu)
        for image, value in zip(images, expected):
            self.zero(sp.diff(image, v) - value)
            commutator = speed * sp.diff(sp.diff(image, v), x)
            commutator -= sp.diff(speed * sp.diff(image, x), v)
            self.zero(commutator)
            self.zero((sp.diff(image, v) - value).subs(mu, 0))
        # Kernel invariant matching is literal, independent of whether the
        # arbitrary formal coefficients satisfy the remaining actual gates.
        transported_F = (x + mu) * images[2] + (images[1] - nu) * images[3]
        self.zero(sp.diff(transported_F, v))

    def test_arbitrary_Q_critical_hessian_and_vector_jet(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        c = sp.Symbol("c", nonzero=True)
        alpha, beta = sp.symbols("alpha beta")
        qxx, qxy, qyy = sp.symbols("qxx qxy qyy")
        generic_hessian = sp.Matrix([
            [qxx, qxy, c, 0], [qxy, qyy, 0, c],
            [c, 0, 0, 0], [0, c, 0, 0],
        ])
        self.zero(generic_hessian.det() - c**4)

        # Higher-degree Q is independent of the generic second-jet identity.
        coefficients = sp.symbols("q0 q1 q2 q3 q4 q5 q6 q7 q8")
        monomials = (1, X, Y, X**2, X * Y, Y**2, X**3 * Y**2, X * Y**5, X**7)
        Q = sum(a * b for a, b in zip(coefficients, monomials))
        invariant_candidate = c * (X * Z + Y * W) + alpha * Z + beta * W + Q
        base_point = {X: -alpha / c, Y: -beta / c}
        critical = {
            **base_point,
            Z: -sp.diff(Q, X).subs(base_point, simultaneous=True) / c,
            W: -sp.diff(Q, Y).subs(base_point, simultaneous=True) / c,
        }
        for coordinate in (X, Y, Z, W):
            self.zero(sp.diff(invariant_candidate, coordinate).subs(critical, simultaneous=True))
        specialized_hessian = generic_hessian.subs({
            qxx: sp.diff(Q, X, 2),
            qxy: sp.diff(Q, X, Y),
            qyy: sp.diff(Q, Y, 2),
        }, simultaneous=True)
        for entry in sp.hessian(invariant_candidate, (X, Y, Z, W)) - specialized_hessian:
            self.zero(entry)

        # Product rule at the critical point with arbitrary vector-field jets.
        # Derivatives of the vector field multiply the zero gradient.
        local = sp.Matrix(sp.symbols("dx dy dz dw"))
        values = sp.Matrix(sp.symbols("e0:4"))
        first_jet = sp.Matrix(4, 4, sp.symbols("j0:16"))
        vector_field = values + first_jet * local
        quadratic_jet = (local.T * generic_hessian * local)[0] / 2
        Lie_jet = sum(vector_field[i] * sp.diff(quadratic_jet, local[i]) for i in range(4))
        origin = dict.fromkeys(tuple(local), 0)
        differentiated = sp.Matrix([
            sp.diff(Lie_jet, coordinate).subs(origin, simultaneous=True)
            for coordinate in local
        ])
        for entry in differentiated - generic_hessian * values:
            self.zero(entry)
        # Nonsliced boundary: a nonzero LND fixes the split polynomial but
        # vanishes on a plane, so there is no contradiction at its critical point.
        split = X * Z + Y * W
        T_split = lambda f: -Y * sp.diff(f, Z) + X * sp.diff(f, W)
        self.zero(T_split(split))
        for coordinate in (X, Y, Z, W):
            self.zero(T_split(T_split(coordinate)))
            self.zero(T_split(coordinate).subs({X: 0, Y: 0}))


if __name__ == "__main__":
    unittest.main()
