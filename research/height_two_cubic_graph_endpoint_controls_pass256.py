"""Finite algebra controls for the conditional height-two graph proofs255/256.

This standalone source reconstructs scalar coefficients, reciprocal coordinate
transport, and the general-nu invariant from the literal polynomial maps.
It does not certify constant-field integration, the generic curve pole lemma,
actual chart entry, or the published recognition theorem. No retained proof,
solver, or checker is imported. Root owns the single canonical execution.
"""

import unittest

import sympy as sp


class HeightTwoCubicGraphEndpointControls(unittest.TestCase):
    def equal(self, left, right=0):
        self.assertEqual(sp.cancel(sp.expand(left - right)), 0)

    @staticmethod
    def coefficient(expression, variable, power):
        return sp.Poly(sp.expand(expression), variable).coeff_monomial(
            variable**power
        )

    def test_literal_scalar_coefficient_gates(self):
        t, lam, y = sp.symbols("t lam y")
        q, rho, k, nu, n0, mu, ell0 = [
            sp.Function(name)(t)
            for name in ("q", "rho", "k", "nu", "n0", "mu", "ell0")
        ]
        n = sp.Function("n")(t, lam)
        ell = sp.Function("ell")(t, lam)

        def projected_map(n_value, ell_value):
            speed = sp.diff(n_value, lam)
            z = sp.diff(q, t, 2) * y**2 / 2 + sp.diff(k, t) * y + n_value
            w = (
                -sp.diff(q, t, 3) * y**3 / 6
                + (speed * sp.diff(rho, t, 2) - sp.diff(k, t, 2)) * y**2 / 2
                - sp.diff(n_value, t) * y
                + ell_value
            ) / speed
            jac = sp.Matrix([y, z, w]).jacobian([t, lam, y]).det()
            self.equal(
                jac,
                sp.diff(z, t) * sp.diff(w, lam)
                - sp.diff(z, lam) * sp.diff(w, t),
            )
            return sp.expand(jac)

        raw = projected_map(n, ell)
        self.equal(
            self.coefficient(raw, y, 5),
            sp.diff(q, t, 3) ** 2 * sp.diff(n, lam, 2)
            / (12 * sp.diff(n, lam) ** 2),
        )
        self.assertLessEqual(sp.Poly(raw, y).degree(), 5)

        affine_n = projected_map(nu * lam + n0, ell)
        for degree in (5, 4):
            self.equal(self.coefficient(affine_n, y, degree))
        self.equal(
            self.coefficient(affine_n, y, 3),
            (sp.diff(q, t, 4) * nu - 4 * sp.diff(q, t, 3) * sp.diff(nu, t))
            / (6 * nu),
        )
        self.equal(
            self.coefficient(affine_n, y, 2),
            (
                sp.diff(q, t, 3) * sp.diff(ell, lam)
                - nu**2 * sp.diff(rho, t, 3)
                + nu * sp.diff(k, t, 3)
                - 3 * sp.diff(k, t, 2) * sp.diff(nu, t)
            ) / (2 * nu),
        )

        affine_both = projected_map(nu * lam + n0, mu * lam + ell0)
        self.equal(
            self.coefficient(affine_both, y, 1),
            (nu * sp.diff(nu, t, 2) - 2 * sp.diff(nu, t) ** 2) * lam / nu
            + sp.diff(n0, t, 2) - 2 * sp.diff(nu, t) * sp.diff(n0, t) / nu
            + sp.diff(k, t, 2) * mu / nu,
        )
        self.equal(
            self.coefficient(affine_both, y, 0),
            (2 * mu * sp.diff(nu, t) / nu - sp.diff(mu, t)) * lam
            + (mu * sp.diff(n0, t) + ell0 * sp.diff(nu, t)) / nu
            - sp.diff(ell0, t),
        )
        # Differential equivalences, not a test proof of exact-field completeness.
        self.equal(
            sp.diff(1 / nu, t, 2),
            (2 * sp.diff(nu, t) ** 2 - nu * sp.diff(nu, t, 2)) / nu**3,
        )
        self.equal(
            sp.diff(sp.diff(q, t, 3) / nu**4, t),
            (sp.diff(q, t, 4) * nu - 4 * sp.diff(q, t, 3) * sp.diff(nu, t))
            / nu**5,
        )
        # A coefficient-field scalar need not be complex or lambda-constant.
        special = {q: t**3, rho: t**4 / 4, k: 0, nu: 1, n0: 0,
                   mu: t, ell0: 0}
        scalar_fixture = affine_both.subs(special, simultaneous=True).doit()
        self.equal(scalar_fixture, -lam)

    def test_reciprocal_primitives_and_actual_coordinate_inverse(self):
        t = sp.symbols("t")
        alpha, beta, chi, c = sp.symbols("alpha beta chi c", nonzero=True)
        d = alpha * t + beta
        self.equal(sp.diff(1 / d, t, 3), -6 * alpha**3 / d**4)
        self.equal(sp.diff(-chi / (6 * alpha**3 * d), t, 3), chi / d**4)
        self.equal(sp.diff(chi * t**3 / (6 * beta**4), t, 3), chi / beta**4)

        X, Y, Z, W, Xs, Ys, Zs, Ws = sp.symbols("X Y Z W Xs Ys Zs Ws")
        r0, r1, r2 = sp.symbols("r0 r1 r2")

        def quadratic(xx, yy):
            return r2 * yy**2 + r1 * xx * yy + r0 * xx**2

        forward = (
            alpha * Y + beta * X,
            X,
            (Z - quadratic(X, Y)) / c,
            W,
        )
        backward = (
            Ys,
            (Xs - beta * Ys) / alpha,
            c * Zs + quadratic(Ys, (Xs - beta * Ys) / alpha),
            Ws,
        )
        for actual, expected in zip(
            forward, (Xs, Ys, Zs, Ws)
        ):
            self.equal(actual.subs(dict(zip((X, Y, Z, W), backward)), simultaneous=True), expected)
        for actual, expected in zip(backward, (X, Y, Z, W)):
            self.equal(actual.subs(dict(zip((Xs, Ys, Zs, Ws), forward)), simultaneous=True), expected)
        self.equal(sp.Matrix(forward).jacobian([X, Y, Z, W]).det(), -alpha / c)

        lam, v = sp.symbols("lam v")
        moving_y = sp.Function("moving_y")(t, lam, v)
        parameters = (d * X + alpha * moving_y, 1 / d, lam / d, v / c)
        parameter_det = sp.Matrix(parameters).jacobian([X, t, lam, v]).det()
        self.equal(parameter_det, -alpha / (c * d**2))
        self.equal((-alpha / c) / parameter_det, d**2)
        # Omitting the selected-parameter rescaling loses the required factor c.
        wrong_parameters = parameters[:-1] + (v,)
        wrong_det = sp.Matrix(wrong_parameters).jacobian([X, t, lam, v]).det()
        self.equal((-alpha / c) / wrong_det, d**2 / c)
        self.assertNotEqual(sp.cancel(d**2 / c - d**2), 0)
        # The constant-denominator branch has coordinate factor 1/c and v=cv*.
        self.equal((1 / c) * c, 1)

    def test_full_reciprocal_projected_transport(self):
        t, lam, y, w, Xs = sp.symbols("t lam y w Xs")
        alpha, beta, c = sp.symbols("alpha beta c", nonzero=True)
        k, rho, n0 = [sp.Function(name)(t) for name in ("k", "rho", "n0")]
        r0, r1, r2 = sp.symbols("r0 r1 r2")
        d = alpha * t + beta
        q0 = c / d
        q2 = r2 * t**2 + r1 * t + r0
        n = lam / d + n0
        q = q0 + q2
        z = sp.diff(q, t, 2) * y**2 / 2 + sp.diff(k, t) * y + n
        ys = -alpha * y / d
        old_x = Xs / d + ys
        old_y = y + t * old_x
        old_z = z + (sp.diff(q, t) * y + k) * old_x + q * old_x**2
        old_w = w + (sp.diff(rho, t) * y + lam) * old_x + rho * old_x**2
        zstar = (old_z - r2 * old_y**2 - r1 * old_x * old_y - r0 * old_x**2) / c

        ts, ls = 1 / d, lam / d
        rhos, ks, ns = rho / d**2, k / (c * d), (ls + n0) / c
        star_derivative = lambda function: -d**2 * sp.diff(function, t) / alpha
        rhos_prime = star_derivative(rhos)
        ks_prime = star_derivative(ks)
        zs = 3 * ts * ys**2 + ks_prime * ys + ns
        ws = w + (sp.diff(rho, t) * y + lam) * ys + rho * ys**2

        self.equal(alpha * old_y + beta * old_x, Xs)
        self.equal(old_x, ys + ts * Xs)
        self.equal(zstar, zs + (3 * ts**2 * ys + ks) * Xs + ts**3 * Xs**2)
        self.equal(old_w, ws + (rhos_prime * ys + ls) * Xs + rhos * Xs**2)
        self.equal(rhos_prime, -sp.diff(rho, t) / alpha + 2 * rho / d)
        self.equal(ks_prime, (k - d * sp.diff(k, t) / alpha) / c)
        # At fixed t*, d/dlambda* = d*d/dlambda; nu* is 1/c, not 1.
        self.equal(d * sp.diff(ns, lam), 1 / c)
        self.assertNotEqual(sp.cancel(1 / c - 1), 0)

    def test_general_nu_endpoint_and_both_actual_inverse_orders(self):
        t, lam, y, X = sp.symbols("t lam y X")
        nu = sp.symbols("nu", nonzero=True)
        mu, A2, A1, c1, c2, c3 = sp.symbols("mu A2 A1 c1 c2 c3")
        k, C = sp.Function("k")(t), sp.Function("C")(t)
        rho = (k + mu * t**3 + A2 * t**2 + c1 * t + c3) / nu
        n0 = -mu * k - A1 * t - c2
        ell0 = C + mu * n0
        n, ell = nu * lam + n0, nu * mu * lam + ell0
        z = 3 * t * y**2 + sp.diff(k, t) * y + n
        w = (
            ell - y**3 + (nu * sp.diff(rho, t, 2) - sp.diff(k, t, 2)) * y**2 / 2
            - sp.diff(n0, t) * y
        ) / nu
        self.equal(mu, (nu * sp.diff(rho, t, 3) - sp.diff(k, t, 3)) / 6)
        self.equal(sp.diff(n0, t, 2) + mu * sp.diff(k, t, 2))
        self.equal(nu * w, mu * z - y**3 + A2 * y**2 + A1 * y + C)
        self.equal(sp.Matrix([y, z, w]).jacobian([t, lam, y]).det(), -sp.diff(C, t))

        Y = y + t * X
        Z = z + (3 * t**2 * y + k) * X + t**3 * X**2
        W = w + (sp.diff(rho, t) * y + lam) * X + rho * X**2
        invariant = nu * W - mu * Z - X * Z + Y**3 - A2 * Y**2 - A1 * Y - c1 * X * Y - c2 * X - c3 * X**2
        self.equal(invariant, C)
        self.equal(sp.Matrix([Y, Z, W]).jacobian([t, lam, y]).det(), -sp.diff(C, t))

        xx, yy, zz, ww, ii = sp.symbols("xx yy zz ww ii")
        correction = -mu * zz - xx * zz + yy**3 - A2 * yy**2 - A1 * yy - c1 * xx * yy - c2 * xx - c3 * xx**2
        actual_i = nu * ww + correction
        actual_w = (ii - correction) / nu
        self.equal(actual_i.subs(ww, actual_w), ii)
        self.equal(actual_w.subs(ii, actual_i), ww)

        # Deliberately dropping nu in either original W or lambda is detected.
        self.equal(invariant - nu * W + W - C, (1 - nu) * W)
        self.assertNotEqual(sp.cancel(actual_i.subs(ww, ii - correction) - ii), 0)
        zfree = sp.symbols("zfree")
        correct_lambda = (zfree - 3 * t * y**2 - sp.diff(k, t) * y - n0) / nu
        wrong_lambda = nu * correct_lambda
        self.equal(
            z.subs(lam, wrong_lambda) - zfree,
            (nu - 1) * (zfree - 3 * t * y**2 - sp.diff(k, t) * y - n0),
        )
        self.assertNotEqual(sp.cancel(z.subs(lam, wrong_lambda) - zfree), 0)


if __name__ == "__main__":
    unittest.main()
