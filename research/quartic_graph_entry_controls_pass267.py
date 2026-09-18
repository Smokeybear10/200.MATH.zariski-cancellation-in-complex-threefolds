"""Independent finite identities for the genuine quartic-graph endpoint267.

These controls rebuild the old potentials, actual shear, scalar and full-X
determinants, and polynomial substitution. They do not prove constant-field
integration, actual chart entry, the curve-pole lemma, or cancellation.
No retained checker or solver module is imported.
"""

import unittest

import sympy as sp


class QuarticGraphEntryControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_old_potentials_and_actual_shear_cancel_every_lambda_term(self):
        t, lam, y, z, X = sp.symbols("t lam y z X")
        alpha, beta, gamma = sp.symbols("alpha beta gamma")
        q, r, k0, n0 = (sp.Function(name)(t) for name in ("q", "r", "k0", "n0"))
        ell = sp.Function("ell")(t, lam)
        e = alpha * t + beta
        m, nu = 1 / e, gamma / e**2
        k, n = m * lam + k0, nu * lam + n0
        d = sp.diff(r, t, 2)
        f = (sp.diff(q, t, 2) - d * m) * y**2 / 2 + sp.diff(k, t) * y + n
        old_potential = (
            (sp.diff(q, t, 3) - sp.diff(r, t, 3) * m - 3 * d * sp.diff(m, t))
            * y**3 / 6
            + (sp.diff(k, t, 2) - d * nu) * y**2 / 2
            + sp.diff(n, t) * y
        )
        theta = (z - f) / m
        w = (ell - old_potential - sp.diff(f, lam) * theta) / m
        R = r - e * q
        Lambda = gamma * q - e * k0
        K = gamma * k0 - e * n0
        S = e * ell + gamma**2 * m**2 * lam
        B = sp.diff(R, t, 3) * y**3 / 6 + sp.diff(Lambda, t, 2) * y**2 / 2 + sp.diff(K, t) * y + gamma * n0
        C1 = sp.diff(R, t, 2) * y**2 / 2 + sp.diff(Lambda, t) * y + K
        C2 = sp.diff(R, t) * y + Lambda
        self.assert_zero(w - (alpha * y - gamma) * z - S - B)
        self.assert_zero(sp.diff(B, y) - sp.diff(C1, t))
        Y = y + t * X
        Z = z + (sp.diff(q, t) * y + k) * X + q * X**2
        W = w + theta * X + (sp.diff(r, t) * y + lam) * X**2 + r * X**3
        actual_J = W - (alpha * Y + beta * X - gamma) * Z
        claimed_J = S + B + C1 * X + C2 * X**2 + R * X**3
        self.assert_zero(actual_J - claimed_J)
        self.assert_zero(sp.diff(claimed_J - S, lam))
        quartic_top = (sp.diff(q, t, 4) - m * sp.diff(r, t, 4) - 4 * sp.diff(q, t, 3) * sp.diff(m, t) / m) / 24
        self.assert_zero(e * quartic_top + sp.diff(R, t, 4) / 24)

    def test_literal_scalar_and_first_X_determinants(self):
        t, S, y, X = sp.symbols("t S y X")
        z, H = (sp.Function(name)(t, S, y) for name in ("z", "H"))
        H = sp.Function("H")(t, S)
        m, q, k0, R, Lambda, K, b0 = (sp.Function(name)(t) for name in ("m", "q", "k0", "R", "Lambda", "K", "b0"))
        B = sp.diff(R, t, 3) * y**3 / 6 + sp.diff(Lambda, t, 2) * y**2 / 2 + sp.diff(K, t) * y + b0
        C1 = sp.diff(R, t, 2) * y**2 / 2 + sp.diff(Lambda, t) * y + K
        Y = y + t * X
        Z = z + (sp.diff(q, t) * y + k0 + m * H) * X + q * X**2
        J = S + B + C1 * X + (sp.diff(R, t) * y + Lambda) * X**2 + R * X**3
        # Expand the literal Y row of the determinant, not a supplied formula.
        raw = sum(
            sp.diff(Y, variable) * sp.Matrix([Z, J]).jacobian(
                [other for other in (t, S, y) if other != variable]
            ).det() * (-1)**index
            for index, variable in enumerate((t, S, y))
        )
        coefficients = sp.Poly(sp.expand(raw), X)
        scalar = sp.diff(z, t) - sp.diff(B, t) * sp.diff(z, S)
        first = (m * sp.diff(H, t) + sp.diff(m, t) * H
                 - m * sp.diff(B, t) * sp.diff(H, S) - sp.diff(z, y)
                 + sp.diff(q, t, 2) * y + sp.diff(k0, t))
        self.assert_zero(coefficients.nth(0) - scalar)
        self.assert_zero(coefficients.nth(1) - first)
        # The omitted coefficient derivative m' H is generally nonzero.
        self.assertNotEqual(sp.diff(m, t) * H, 0)

    def test_high_degree_gates_retain_the_full_coordinate_coefficient(self):
        t, S, y = sp.symbols("t S y")
        zc = [sp.Function(f"z{i}")(t, S) for i in range(5)]
        bc = [sp.Function(f"b{i}")(t) for i in range(4)]
        z = sum(zc[i] * y**i for i in range(5))
        B = sum(bc[i] * y**i for i in range(4))
        scalar = sp.Poly(sp.expand(sp.diff(z, t) - sp.diff(B, t) * sp.diff(z, S)), y)
        self.assert_zero(scalar.nth(7) + sp.diff(bc[3], t) * sp.diff(zc[4], S))
        self.assert_zero(scalar.nth(6).subs(sp.diff(zc[4], S), 0) + sp.diff(bc[3], t) * sp.diff(zc[3], S))
        self.assert_zero(scalar.nth(5).subs({sp.diff(zc[4], S): 0, sp.diff(zc[3], S): 0}) + sp.diff(bc[3], t) * sp.diff(zc[2], S))
        top_fixed = {sp.diff(zc[i], S): 0 for i in (2, 3, 4)}
        self.assert_zero(scalar.nth(4).subs(top_fixed) - sp.diff(zc[4], t) + sp.diff(bc[3], t) * sp.diff(zc[1], S))
        self.assert_zero(scalar.nth(3).subs(top_fixed) - sp.diff(zc[3], t) + sp.diff(bc[3], t) * sp.diff(zc[0], S) + sp.diff(bc[2], t) * sp.diff(zc[1], S))
        H = sp.Function("H")(t, S)
        m, q, k0 = (sp.Function(name)(t) for name in ("m", "q", "k0"))
        first = m * sp.diff(H, t) + sp.diff(m, t) * H - m * sp.diff(B, t) * sp.diff(H, S) - sp.diff(z, y) + sp.diff(q, t, 2) * y + sp.diff(k0, t)
        self.assert_zero(sp.Poly(sp.expand(first), y).nth(3) + m * sp.diff(bc[3], t) * sp.diff(H, S) + 4 * zc[4])
        self.assertNotEqual(sp.cancel(1 / S**2 - 4), 0)

    def test_actual_inverse_and_polynomial_entry_substitution(self):
        X, Y, Z, W, J, S, y, t = sp.symbols("X Y Z W J S y t")
        alpha, beta, gamma = sp.symbols("alpha beta gamma")
        multiplier = alpha * Y + beta * X - gamma
        forward, inverse = W - multiplier * Z, J + multiplier * Z
        self.assert_zero(forward.subs(W, inverse) - J)
        self.assert_zero(inverse.subs(J, forward) - W)
        z4, z3, z2, a1, a0, b1, b0, h1, h0, m, qp, q, k0 = sp.symbols("z4 z3 z2 a1 a0 b1 b0 h1 h0 m qp q k0")
        z = z4 * y**4 + z3 * y**3 + z2 * y**2 + (a1 * S + b1) * y + a0 * S + b0
        H = h1 * S + h0
        # Arbitrary cubic field-coefficient correction models the proved form.
        pc = sp.symbols("p0:10")
        monomials = [1, X, Y, X**2, X * Y, Y**2, X**3, X**2 * Y, X * Y**2, Y**3]
        correction = sum(c * term for c, term in zip(pc, monomials))
        old_Z = z + (qp * y + k0 + m * H) * X + q * X**2
        entry = sp.expand(old_Z.subs({y: Y - t * X, S: J - correction}, simultaneous=True))
        self.assertFalse(entry.has(y, S, W))
        self.assertEqual(sp.Poly(entry, X, Y, J).degree(J), 1)
        recovered = entry.subs(J, S + correction).subs(Y, y + t * X)
        self.assert_zero(recovered - old_Z)


if __name__ == "__main__":
    unittest.main(verbosity=2)
