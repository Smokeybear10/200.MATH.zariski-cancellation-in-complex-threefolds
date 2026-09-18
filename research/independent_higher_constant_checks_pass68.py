"""Exact formal coefficient controls for the independent constant-top proof.

Two methods check the universal velocity/commutator coefficients and the
m=4,5,6 nilpotence split. The supplied frame, full companion-image theorem,
and actual polynomial-coordinate generation are hypotheses of the written
proof, not conclusions of these formal calculations. No new action or
classification theorem is computationally certified here.
"""

import unittest
import sympy as sp


class IndependentHigherConstantChecks(unittest.TestCase):
    def assert_zero(self, expression):
        if isinstance(expression, sp.MatrixBase):
            for entry in expression:
                self.assertEqual(sp.factor(entry), 0)
        else:
            self.assertEqual(sp.factor(expression), 0)

    def test_symbolic_full_velocity_and_commuting_coefficients(self):
        m = sp.symbols("m", integer=True, positive=True)
        sigma, q, nu1, nu2, lam = sp.symbols("sigma q nu1 nu2 lam")
        tau = q + sigma**2 / 2
        # Formal coefficient basis (c, d, V*ell, V*mu). These are not
        # specified Jacobian columns of a realized polynomial action.
        c, d, vell, vmu = [sp.eye(4)[:, i] for i in range(4)]
        jc = (m - 1) * vell / 2
        jd = c / (m - 1) - sigma * vell / 2 + (m - 2) * vmu / 2
        lower_ell = (m - 1) * tau / (m - 2) - sigma**2 / (2 * (m - 2)) + nu1
        lower_mu = sigma + nu2

        # Recover Je independently from the full upper velocity identity,
        # including both auxiliary-row contributions in L*h_(m-3).
        je_from_velocity = (
            (sigma * c + d) / (m - 2) - tau * jc - sigma * jd
            + (m - 3) * (lower_ell * vell + lower_mu * vmu) / 2
        )
        je_claimed = (
            sigma * c / ((m - 1) * (m - 2)) + d / (m - 2)
            - (m - 1) * q * vell / (2 * (m - 2)) - sigma * vmu / 2
            + (m - 3) * (nu1 * vell + nu2 * vmu) / 2
        )
        self.assert_zero(je_from_velocity - je_claimed)

        b0 = -(m - 3) * nu2 / (m - 2)
        beta = sigma / (m - 2) + b0
        gamma = (
            sigma**2 / ((m - 1) * (m - 2)) + b0 * sigma / (m - 1)
            + q / (m - 2) - (m - 3) * nu1 / (m - 1)
        )
        # E acts as d/dsigma on this coefficient ring because Eq=0.
        commutator = (
            -je_from_velocity - beta * jd - gamma * jc
            + sp.diff(beta, sigma) * d + sp.diff(gamma, sigma) * c
        )
        self.assert_zero(commutator)

        # Separate collinear bad-layer branch mu=lam*ell. This uses the
        # two-direction formula, not the independent-mu correction.
        jd_collinear = c / (m - 1) + (-sigma + (m - 2) * lam) * vell / 2
        beta_collinear = (sigma - (m - 2) * lam) / (m - 1)
        self.assert_zero(-jd_collinear - beta_collinear * jc
                         + sp.diff(beta_collinear, sigma) * c)

    def test_full_lower_layer_and_degree_four_five_six_split(self):
        sigma, q, nu1, nu2, dsigma, dq = sp.symbols("sigma q nu1 nu2 dsigma dq")
        # A constant linear-algebra control with independent bad projections.
        # It does not claim existence of E with these formal layer data.
        c = sp.Matrix([1, 0, 0, 0])
        d = sp.Matrix([0, 1, 1, 0])
        e = sp.Matrix([0, 0, 0, 1])
        ell, mu = sp.Matrix([1, 0]), sp.Matrix([0, 1])
        z_row = sp.Matrix([[0, 0, 0, 1]])
        self.assertEqual(sp.Matrix.hstack(c, d, e).rank(), 3)
        self.assertEqual((z_row * c)[0], 0)
        self.assertEqual((z_row * d)[0], 0)
        self.assertEqual((z_row * e)[0], 1)

        for degree in (4, 5, 6):
            with self.subTest(degree=degree):
                m = sp.Integer(degree)
                tau = q + sigma**2 / 2
                self.assert_zero(sp.diff(tau, sigma) - sigma)
                lower = (
                    ell * ((m - 1) * tau / (m - 2) - sigma**2 / (2 * (m - 2)))
                    + mu * sigma + nu1 * ell + nu2 * mu
                )
                self.assert_zero(lower.diff(sigma) - (ell * sigma + mu))
                ordinary_lower = lower.diff(sigma) * dsigma + lower.diff(q) * dq
                full_rows = (
                    (m - 1) * ell * (sigma * dsigma + dq)
                    + ((m - 2) * mu - sigma * ell) * dsigma
                ) / (m - 2)
                self.assert_zero(ordinary_lower - full_rows)

                b0 = -(m - 3) * nu2 / (m - 2)
                beta = sigma / (m - 2) + b0
                gamma = (sigma**2 / ((m - 1) * (m - 2))
                         + b0 * sigma / (m - 1) + q / (m - 2)
                         - (m - 3) * nu1 / (m - 1))
                first = e + beta * d + gamma * c
                self.assert_zero(first.diff(sigma, degree - 1))
                zq = sp.Rational(1, 3) if degree == 4 else sp.Integer(0)
                self.assert_zero(first.diff(sigma, degree - 2) - zq * c)
                self.assert_zero(sp.diff(beta, q) * zq)
                second = first.diff(q) * zq
                expected_second = c / 6 if degree == 4 else sp.zeros(4, 1)
                self.assert_zero(second - expected_second)
                self.assert_zero(second.diff(q) * zq)
                self.assertEqual((z_row * first)[0], 1)


if __name__ == "__main__":
    unittest.main()
