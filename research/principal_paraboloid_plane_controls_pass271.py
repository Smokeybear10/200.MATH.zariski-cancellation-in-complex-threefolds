"""Finite algebra controls for the nonconstant-intercept plane reduction271.

All maps and gradients are reconstructed here from formal coefficient
functions, with every t,n derivative retained. These tests do not prove
actual field return, exact-field descent, the pure-top theorem, or
recognition. The final method also controls Root's subsequent constant-
sigma line coefficient observation, without claiming a saved endpoint.
No retained checker is imported. Root owns the sole canonical execution.
"""

import unittest

import sympy as sp


class PrincipalParaboloidPlaneControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    @staticmethod
    def formal_data():
        t, n, U, P = sp.symbols("t n U P")
        H, T, omega = (sp.Function(name)(t, n) for name in ("H", "T", "omega"))
        k = sp.Function("k")(t)
        gamma = 2 * P + sp.diff(k, t)
        B1 = 2 * U + sp.diff(k, t, 2) * P
        A = gamma * U + sp.diff(k, t, 2) * P**2 / 2
        C = U**2 + sp.diff(k, t, 2) * P * U + sp.diff(k, t, 3) * P**3 / 6
        g = T + sp.diff(H, t) * P - sp.diff(H, n) * A
        F = (
            -sp.diff(H, n, 2) * A**2 / 2
            + (sp.diff(H, n, t) * P + sp.diff(T, n)) * A
            + sp.diff(H, n) * C
            - sp.diff(H, t) * U
            - sp.diff(H, t, 2) * P**2 / 2
            - sp.diff(T, t) * P
        )
        W = omega - F
        return t, n, U, P, H, T, omega, k, gamma, B1, A, C, g, F, W

    def test_exact_parameter_change_and_second_potential(self):
        t, n, U, P, H, T, omega, k, gamma, B1, A, C, g, F, W = self.formal_data()
        Ht, Hn = sp.diff(H, t), sp.diff(H, n)
        nu, old_nt = 1 / Hn, -Ht / Hn
        ell = T / Hn
        old_second = gamma * U + sp.diff(k, t, 2) * P**2 / 2 + old_nt * P + nu * g
        self.assert_zero(old_second - ell)

        to_old = sp.Matrix([[1, 0], [Ht, Hn]])
        to_new = sp.Matrix([[1, 0], [-Ht / Hn, 1 / Hn]])
        for product in (to_old * to_new, to_new * to_old):
            for entry in product - sp.eye(2):
                self.assert_zero(entry)
        speed = sp.symbols("speed", nonzero=True)
        self.assert_zero(-speed**4 * to_old.det() + speed**4 * Hn)
        self.assertNotEqual(sp.cancel(-speed**4 * Hn + speed**4), 0)
        # Old partial_t fixes the old parameter H=s.
        self.assert_zero(Ht + old_nt * Hn)
        self.assert_zero(nu * Hn - 1)

    def test_literal_high_coefficients_and_quartic_potential(self):
        t, n, U, P, H, T, omega, k, gamma, B1, A, C, g, F, W = self.formal_data()
        X = sp.symbols("X")
        yt, yn, yv, pt, pn, pv, wt, wn, wv = sp.symbols(
            "yt yn yv pt pn pv wt wn wv"
        )
        gt = sp.diff(g, t) + sp.diff(g, U) * yt + sp.diff(g, P) * pt
        gn = sp.diff(g, n) + sp.diff(g, U) * yn + sp.diff(g, P) * pn
        gv = sp.diff(g, U) * yv + sp.diff(g, P) * pv
        literal = sp.Matrix([
            [yt + X * pt + X**2, yn + X * pn, yv + X * pv],
            [gamma * pt + B1 + X * gamma, gamma * pn + 1, gamma * pv],
            [wt + X * gt + X**2 * sp.diff(H, t),
             wn + X * gn + X**2 * sp.diff(H, n), wv + X * gv],
        ])
        coefficients = sp.Poly(sp.expand(literal.det()), X)
        self.assertLessEqual(coefficients.degree(), 4)
        self.assert_zero(coefficients.nth(4))
        self.assert_zero(coefficients.nth(3))
        expected = wv + sp.diff(F, U) * yv + sp.diff(F, P) * pv
        self.assert_zero(coefficients.nth(2) - expected)

        self.assert_zero(sp.diff(A, U) - gamma)
        self.assert_zero(sp.diff(A, P) - B1)
        self.assert_zero(sp.diff(C, P) - sp.diff(A, t))
        self.assert_zero(sp.diff(W, U) - sp.diff(g, P) + gamma * sp.diff(g, n))
        self.assert_zero(sp.diff(W, P) - sp.diff(g, t) + B1 * sp.diff(g, n))
        self.assertLessEqual(sp.Poly(sp.expand(W), U, P).total_degree(), 4)
        # Omitting the mixed H_nt term changes the primitive gradient.
        wrong_F = F - sp.diff(H, n, t) * P * A
        self.assertNotEqual(sp.cancel(sp.diff(F - wrong_F, U)), 0)

    def test_remaining_literal_coefficients_and_sextic_primitive(self):
        t, n, U, P, H, T, omega, k, gamma, B1, A, C, g, F, W = self.formal_data()
        yt, yn, yv, pt, pn, pv = sp.symbols("yt yn yv pt pn pv")
        a0 = sp.Matrix([[yt, yn, yv]])
        a1 = sp.Matrix([[pt, pn, pv]])
        b0 = gamma * a1 + sp.Matrix([[B1, 1, 0]])
        b1 = sp.Matrix([[gamma, 0, 0]])
        c0 = (
            sp.diff(W, U) * a0 + sp.diff(W, P) * a1
            + sp.Matrix([[sp.diff(W, t), sp.diff(W, n), 0]])
        )
        c1 = (
            sp.diff(g, U) * a0 + sp.diff(g, P) * a1
            + sp.Matrix([[sp.diff(g, t), sp.diff(g, n), 0]])
        )
        # Exact X and constant coefficients of the literal determinant.
        raw_X = (
            sp.Matrix.vstack(a1, b0, c0).det()
            + sp.Matrix.vstack(a0, b1, c0).det()
            + sp.Matrix.vstack(a0, b0, c1).det()
        )
        raw_constant = sp.Matrix.vstack(a0, b0, c0).det()
        QU = gamma * sp.diff(W, n) - sp.diff(W, P)
        QP = B1 * sp.diff(W, n) - sp.diff(W, t)
        self.assert_zero(raw_X - QU * yv - QP * pv)
        DU = (B1 * yn - yt) * pv + (pt - B1 * pn) * yv
        DP = (1 + gamma * pn) * yv - gamma * yn * pv
        self.assert_zero(raw_constant - QU * DU - QP * DP)
        self.assert_zero(sp.diff(QU, P) - sp.diff(QP, U))

        # Termwise polynomial integration, not an assumed primitive.
        Q = sum(
            coefficient * U**(i + 1) * P**j / (i + 1)
            for (i, j), coefficient in sp.Poly(sp.expand(QU), U, P).terms()
        )
        remaining = sp.cancel(sp.expand(QP - sp.diff(Q, P)))
        self.assert_zero(sp.diff(remaining, U))
        Q += sum(
            coefficient * P**(j + 1) / (j + 1)
            for (j,), coefficient in sp.Poly(remaining, P).terms()
        )
        self.assert_zero(sp.diff(Q, U) - QU)
        self.assert_zero(sp.diff(Q, P) - QP)
        self.assert_zero(Q.subs({U: 0, P: 0}))
        polynomial = sp.Poly(sp.expand(Q), U, P)
        self.assertLessEqual(polynomial.total_degree(), 6)
        top = sum(
            coefficient * U**i * P**j
            for (i, j), coefficient in polynomial.terms() if i + j == 6
        )
        expected_top = sp.diff(H, n, 3) * P**3 * (sp.diff(k, t, 2) * P + 4 * U)**3 / 48
        self.assert_zero(top - expected_top)
        # Exact factor multiplicities after a symbolic linear change.
        Z = sp.symbols("Z")
        split = sp.cancel(
            expected_top.subs(U, (Z - sp.diff(k, t, 2) * P) / 4)
        )
        self.assert_zero(split - sp.diff(H, n, 3) * P**3 * Z**3 / 48)
        self.assertEqual(sp.degree(split, P), 3)
        self.assertEqual(sp.degree(split, Z), 3)

    def test_unit_cofactor_fixtures_and_smoothness_negative(self):
        U, P, v, level, r0, r1 = sp.symbols("U P v level r0 r1")
        eta = sp.symbols("eta", nonzero=True)
        G = P - U**2
        R = r0 + r1 * U
        relation = level + eta * G + G**2 * R
        on_curve = {U: v, P: v**2}
        self.assert_zero(relation.subs(on_curve, simultaneous=True) - level)
        GU = sp.diff(relation, U).subs(on_curve, simultaneous=True)
        GP = sp.diff(relation, P).subs(on_curve, simultaneous=True)
        self.assert_zero(GU + 2 * eta * v)
        self.assert_zero(GP - eta)
        self.assert_zero(GP / eta - 1)
        self.assert_zero(sp.div(relation - level, G, P)[1])

        # The plane curve is smooth, but an arbitrary cofactor need not be a unit.
        bad_relation = G * U
        bad_U = sp.diff(bad_relation, U).subs(on_curve, simultaneous=True)
        bad_P = sp.diff(bad_relation, P).subs(on_curve, simultaneous=True)
        self.assert_zero(bad_U.subs(v, 0))
        self.assert_zero(bad_P.subs(v, 0))
        self.assert_zero(bad_P - v)
        self.assertNotEqual(bad_P, eta)

    def test_constant_sigma_line_coefficient_observation(self):
        t, n, U, P, H, T, omega, k, gamma, B1, A, C, g, F, W = self.formal_data()
        # Formal coefficient derivatives precede any substitution P=sigma(t,n).
        QU = gamma * sp.diff(W, n) - sp.diff(W, P)
        QP = B1 * sp.diff(W, n) - sp.diff(W, t)
        h2, h3 = sp.diff(H, n, 2), sp.diff(H, n, 3)
        first = gamma**3 * h3 / 2 - 3 * gamma * h2
        second = gamma**2 * h3 - 2 * h2
        self.assert_zero(sp.Poly(sp.expand(QU), U).nth(2) - first)
        self.assert_zero(sp.Poly(sp.expand(QP), U).nth(3) - second)
        self.assert_zero(2 * first - gamma * second + 4 * gamma * h2)
        self.assert_zero(second.subs(P, -sp.diff(k, t) / 2) + 2 * h2)
        # Nonzero gamma branch: the two equations require both h2,h3 zero.
        gamma0 = sp.symbols("gamma0", nonzero=True)
        j2, j3 = sp.symbols("j2 j3")
        equations = sp.Matrix([
            [sp.diff(gamma0**3 * j3 / 2 - 3 * gamma0 * j2, j2),
             sp.diff(gamma0**3 * j3 / 2 - 3 * gamma0 * j2, j3)],
            [sp.diff(gamma0**2 * j3 - 2 * j2, j2),
             sp.diff(gamma0**2 * j3 - 2 * j2, j3)],
        ])
        self.assert_zero(equations.det() + 2 * gamma0**3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
