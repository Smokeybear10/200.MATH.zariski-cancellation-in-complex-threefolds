"""Finite exact controls for the common-factor quadratic-graph exclusion186.

These independent polynomial/jet computations do not construct an actual
1122 frame.  The actual chart, exact coefficient field, full graph ideal,
and evaluated-unit cofactor are written-proof inputs, not test conclusions.
Constant translations below really are polynomial automorphisms.  Formal
coefficient jets are not being promoted to actual frames or field elements.
No older checker, proof implementation, or solver internals are imported.
"""

import unittest

import sympy as sp


def jet_dt(expression, t, chains):
    """Differentiate independent coefficient jets, fixing rho and U,V."""
    result = sp.diff(expression, t)
    for chain in chains:
        result += sum(
            sp.diff(expression, left) * right
            for left, right in zip(chain, chain[1:])
        )
    return sp.expand(result)


class CommonFactorQuadraticControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_eliminant_and_quadratic_model_coefficients(self):
        U, V, t = sp.symbols("U V t")
        k01, k20, k11, k02, k30, k21, k12, k03 = sp.symbols(
            "k01 k20 k11 k02 k30 k21 k12 k03"
        )
        n10, n01, n20, n11, n02 = sp.symbols("n10 n01 n20 n11 n02")
        ell, ell_t, ell_rho, m = sp.symbols("ell ell_t ell_rho m")
        # Literal divided Taylor forms, with mutually independent jets.
        K2 = (k20 * U**2 + 2 * k11 * U * V + k02 * V**2) / 2
        K3 = (
            k30 * U**3 + 3 * k21 * U**2 * V
            + 3 * k12 * U * V**2 + k03 * V**3
        ) / 6
        N2 = (n20 * U**2 + 2 * n11 * U * V + n02 * V**2) / 2
        S = 4 * t * U**3 + K2 + n10 * U + n01 * V
        T = U**4 + K3 + N2
        R = k01 - U
        A1 = sp.diff(S, V)
        H = sp.expand(R * (T - ell_t * U - ell_rho * V - m)
                      + A1 * (ell - S))
        top = sum(
            coefficient * U**i * V**j
            for (i, j), coefficient in sp.Poly(H, U, V).terms()
            if i + j == 5
        )
        self.zero(top + U**5)
        self.zero(H.coeff(V, 3) - R * k03 / 6 + k02**2 / 2)

        r, rp, rpp, h = sp.symbols("r rp rpp h")
        staged = H.subs(
            {k01: r, k11: rp, k21: rpp, k02: 0, k12: 0, k03: 0,
             n02: h}, simultaneous=True
        ).expand()
        self.zero(staged.coeff(V, 2) - (r - U) * h / 2)
        linear = (
            (r - U) * (rpp * U**2 / 2 + n11 * U - ell_rho)
            - (rp * U + n01)**2
        )
        self.zero(staged.coeff(V, 1) - linear)
        self.zero(staged.coeff(V, 0).coeff(U, 4)
                  - (r - k30 / 6 - 4 * t * rp))

        p2 = sp.symbols("p2", nonzero=True)
        p1, p0, omega, aU, aV, a0 = sp.symbols("p1 p0 omega aU aV a0")
        P = p2 * U**2 + p1 * U + p0
        G = V - P
        unrestricted_model = sp.expand(omega * G + (aU * U + aV * V + a0) * G**2)
        self.zero(unrestricted_model.coeff(U, 5) - aU * p2**2)
        self.zero(unrestricted_model.coeff(U, 4).coeff(V, 1) - aV * p2**2)
        model = sp.expand(omega * G + h * (r - U) * G**2 / 2)
        self.zero(model.coeff(V, 2) - h * (r - U) / 2)
        self.zero(model.coeff(V, 1) - (omega - h * (r - U) * P))
        self.zero(model.coeff(V, 0).coeff(U, 4)
                  - (h * r * p2**2 / 2 - h * p2 * p1))
        prior = {
            rpp: -2 * h * p2,
            n11: -h * p1 - rp**2,
            ell_rho: h * p0 + r * rp**2 + 2 * rp * n01,
            omega: -(n01 + r * rp)**2,
        }
        self.zero((linear - model.coeff(V, 1)).subs(prior, simultaneous=True))

        # Known nonzero r'' is the only denominator in these identities.
        r2 = sp.symbols("r2", nonzero=True)
        r3, rho, kappa3, sprime = sp.symbols("r3 rho kappa3 sprime")
        h0 = r2**2 / 8
        hprime = r2 * r3 / 4
        leading_p2 = -4 / r2
        leading_p1 = -(hprime * rho + sprime + rp**2) / h0
        self.zero(h0 * leading_p2**2 - 2)
        self.zero(r2 + 2 * h0 * leading_p2)
        fourth_gap = sp.expand(
            (r3 * rho + kappa3) / 6 + 4 * t * rp
            - h0 * leading_p2 * leading_p1
        )
        self.zero(fourth_gap.coeff(rho, 1) + sp.Rational(5, 6) * r3)
        lam = sp.symbols("lam", nonzero=True)
        mu = sp.symbols("mu")
        self.zero(lam * fourth_gap.subs(
            {r2: lam, r3: 0, rp: lam * t + mu,
             sprime: lam * kappa3 / 24 - mu * (lam * t + mu)},
            simultaneous=True,
        ))

        # Low-graph leading-factor control, including p1=0 and p0=0.
        # The universal divisibility contradiction is supplied by the note.
        self.zero(top.subs(V, p1 * U) + U**5)
        self.assertNotEqual(top.subs(V, p1 * U), 0)

    def test_actual_translation_and_normalized_first_potential(self):
        X, Y, Z, W, t, rho, y, theta, z, w = sp.symbols(
            "X Y Z W t rho y theta z w"
        )
        mu, nu = sp.symbols("mu nu")
        lam = sp.symbols("lam", nonzero=True)
        forward = (X + mu, Y - nu, Z, W)
        inverse = (X - mu, Y + nu, Z, W)
        variables = (X, Y, Z, W)
        for direct, reverse in ((forward, inverse), (inverse, forward)):
            substitution = dict(zip(variables, reverse))
            for expression, variable in zip(direct, variables):
                self.zero(expression.subs(substitution, simultaneous=True) - variable)

        K = sp.symbols("K0:5")
        N = sp.symbols("N0:3")
        q = -t * rho + t**4
        r1 = mu * t + nu
        old_r = lam * t**2 / 2 + r1
        old_k = old_r * rho + K[0]
        sigma = sp.diff(q, t) * y + sp.diff(q, rho) * theta + old_k
        new_k = old_k + sp.diff(q, t) * r1 + 2 * mu * rho * sp.diff(q, rho) - 2 * mu * q
        self.zero(new_k - (old_k - r1 * rho + 4 * r1 * t**3 - 2 * mu * t**4))
        self.zero(sp.diff(new_k, rho) - lam * t**2 / 2)
        new_y, new_theta = y - r1, theta - 2 * mu * rho
        new_sigma, new_z = sigma - 2 * mu * q, z - mu * sigma + mu**2 * q
        new_w = w - mu * theta + mu**2 * rho
        self.zero(new_sigma - (sp.diff(q, t) * new_y + sp.diff(q, rho) * new_theta + new_k))
        self.zero(y + t * X - nu - (new_y + t * (X + mu)))
        self.zero(z + sigma * X + q * X**2
                  - (new_z + new_sigma * (X + mu) + q * (X + mu)**2))
        self.zero(w + theta * X + rho * X**2
                  - (new_w + new_theta * (X + mu) + rho * (X + mu)**2))

        U, V, s0, p0, p0_rho = sp.symbols("U V s0 p0 p0_rho")
        dt = lambda expression: jet_dt(expression, t, (K, N))
        r, h = lam * t**2 / 2, lam**2 / 8
        s = lam * K[2] / 24 + s0
        k = r * rho + K[0]
        n = h * rho**2 / 2 + s * rho + N[0]
        p2, p1 = -4 / lam, -K[3] / (3 * lam) - 8 * t**2
        P = p2 * U**2 + p1 * U + p0
        S = (4 * t * U**3 + dt(dt(k)) * U**2 / 2
             + sp.diff(dt(k), rho) * U * V
             + dt(n) * U + sp.diff(n, rho) * V)
        alpha = K[2] / 3 - t * K[3] / 3 - 8 * lam * t**3 - 4 * s0 / lam
        B = r * alpha + lam * t * p0 - lam**2 * t**2 * rho + s * p1 + N[1]
        ell = r * B + (h * rho + s) * p0
        on_graph = sp.expand(S.subs(V, P))
        self.zero(on_graph.coeff(U, 3))
        self.zero(lam * (on_graph.coeff(U, 2) - alpha))
        self.zero(lam * ((r - U) * (alpha * U + B) + on_graph - ell))

        # Formal chain rule permits p0 to depend on rho before its equation.
        ell_rho = sp.diff(ell, rho) + p0_rho * sp.diff(ell, p0)
        D = h * rho + s + r * lam * t
        required = h * p0 + r * (lam * t)**2 + 2 * lam * t * (h * rho + s)
        self.zero(lam * (ell_rho - required - D * (p0_rho - 2 * lam * t)))
        self.assertEqual(sp.Poly(D, rho).degree(), 1)
        self.zero(sp.Poly(D, rho).LC() - h)
        # Nonzero omega=-D^2 and coefficient-field primitive subtraction
        # are proof inputs; these identities do not establish them by sampling.

    def test_final_rho_squared_linear_coefficient(self):
        U, V, t, rho = sp.symbols("U V t rho")
        lam = sp.symbols("lam", nonzero=True)
        K = sp.symbols("K0:4")
        N = sp.symbols("N0:3")
        sj = sp.symbols("s0:3")
        Bj = sp.symbols("B0:2")
        Pj = sp.symbols("P0:2")
        alpha, p1, m = sp.symbols("alpha p1 m")
        chains = (K, N, sj, Bj, Pj)
        dt = lambda expression: jet_dt(expression, t, chains)
        r, h = lam * t**2 / 2, lam**2 / 8
        k = r * rho + K[0]
        n = h * rho**2 / 2 + sj[0] * rho + N[0]
        # Literal Taylor coefficients are differentiated independently here.
        T = (
            U**4 + dt(dt(dt(k))) * U**3 / 6
            + sp.diff(dt(dt(k)), rho) * U**2 * V / 2
            + sp.diff(dt(k), rho, 2) * U * V**2 / 2
            + sp.diff(k, rho, 3) * V**3 / 6
            + dt(dt(n)) * U**2 / 2
            + sp.diff(dt(n), rho) * U * V
            + sp.diff(n, rho, 2) * V**2 / 2
        )
        explicit_T = (
            U**4 + K[3] * U**3 / 6 + lam * U**2 * V / 2
            + (sj[2] * rho + N[2]) * U**2 / 2
            + sj[1] * U * V + h * V**2 / 2
        )
        self.zero(T - explicit_T)
        P = -4 * U**2 / lam + p1 * U + Pj[0] + 2 * lam * t * rho
        w = alpha * U + lam**2 * t**2 * rho + Bj[0]
        ell = r * (lam**2 * t**2 * rho + Bj[0]) + (h * rho + sj[0]) * (2 * lam * t * rho + Pj[0])
        A1 = lam * t * U + h * rho + sj[0]
        terms = (
            A1 * w,
            T.subs(V, P),
            -dt(ell) * U,
            -sp.diff(ell, rho) * P,
        )
        coefficient = lambda expression: sp.expand(expression).coeff(U, 1).coeff(rho, 2)
        self.zero(sp.expand(ell).coeff(rho, 2) - lam**3 * t / 4)
        self.zero(sp.expand(dt(ell)).coeff(rho, 2) - lam**3 / 4)
        for index, term in enumerate(terms):
            expected = -lam**3 / 4 if index == 2 else 0
            self.zero(coefficient(term) - expected)
        potential = sp.expand(sum(terms))
        self.zero(coefficient(potential - m) + lam**3 / 4)
        linear = sp.Poly(potential.coeff(U, 1), rho)
        self.assertEqual(linear.degree(), 2)
        self.zero(linear.LC() + lam**3 / 4)
        # K,N,s,B,P jets remain arbitrary.  No hidden equation on their lower
        # coefficients is used, and no finite control proves transcendence.


if __name__ == "__main__":
    unittest.main()
