"""Finite exact-algebra controls for the held pass306 factor-selection proof.

This standalone source rebuilds the raw surface from arbitrary coefficient
functions. It imports no retained research code and contains no solver calls.
These identities do not verify the actual chart, the whole-line return, the
unit-minor theorem, exact differential constants, or a universal recognition
claim. All variables and inverted coefficients below are formal field data.

Authoring protocol: do not execute, import or compile this saved source before
Root has fully read it and performs the sole canonical execution.
"""

import unittest

import sympy as sp


def zero(expression):
    """Normalize an exact rational identity without numeric tolerances."""
    return sp.cancel(sp.expand(expression))


def raw_surface():
    """Literal Taylor construction, with arbitrary lower functions retained."""
    t, s, U, P, V = sp.symbols("t s U P V")
    m = sp.Function("m")(t)
    k = s * m + sp.Function("k0")(t)
    n = sp.Function("n")(t, s)
    ell = sp.Function("ell")(t, s)
    h0 = sp.Function("h0")(t, s)
    b0 = sp.Function("b0")(t, s)

    def taylor(function, degree):
        return sum(
            sp.diff(function, t, degree - i, s, i)
            * P ** (degree - i) * V ** i
            / (sp.factorial(degree - i) * sp.factorial(i))
            for i in range(degree + 1)
        )

    F = taylor(k, 2) + taylor(n, 1)
    gamma = 2 * P + sp.diff(k, t)
    D = gamma / m
    lam = sp.diff(F, V) / m
    g = (ell - gamma * U - F) / m
    H0 = (
        U**2 + sp.diff(F, P) * U + sp.diff(F, V) * g
        + taylor(k, 3) + taylor(n, 2)
        - sp.diff(ell, t) * P - sp.diff(ell, s) * V - h0
    )
    Hpoly = sp.Poly(sp.expand(H0), U)
    A1 = Hpoly.coeff_monomial(U)
    A0 = Hpoly.coeff_monomial(1)
    p, q, j = (sp.diff(m, t, order) for order in (1, 2, 3))
    bp = sp.diff(k, t, 2) / 4 - m * sp.diff(k, t, 3) / (12 * p)
    bv = p / 2 - m * q / (4 * p)
    B = bp * P + bv * V + b0
    A = A1 - B
    return {
        "t": t, "s": s, "U": U, "P": P, "V": V,
        "m": m, "k": k, "n": n, "ell": ell, "h0": h0,
        "b0": b0, "F": F, "D": D, "lam": lam, "H0": H0,
        "A1": A1, "A0": A0, "p": p, "q": q, "j": j,
        "bp": bp, "bv": bv, "A": A, "B": B,
    }


class SelectedConicFactorControls(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(zero(expression), 0)

    def test_raw_cubic_and_lower_factorization_coefficients(self):
        data = raw_surface()
        t, s, P, V = (data[name] for name in ("t", "s", "P", "V"))
        m, p, q, k, n = (
            data[name] for name in ("m", "p", "q", "k", "n")
        )
        A0, A, B, bp, bv = (
            data[name] for name in ("A0", "A", "B", "bp", "bv")
        )
        av = sp.diff(A, V)
        raw = sp.Poly(sp.expand(A0), P, V)
        residual = sp.Poly(sp.expand(A0 - A * B), P, V)
        u = sp.diff(k, t, 2) - (
            sp.diff(k, t) * p + 2 * sp.diff(n, s)
        ) / m
        self.assertZero(
            raw.coeff_monomial(P**3)
            - sp.diff(k, t, 3) / 6 + p * sp.diff(k, t, 2) / (2 * m)
        )
        self.assertZero(
            raw.coeff_monomial(P**2 * V) - q / 2 + p**2 / m
        )
        for monomial in (P**3, P**2 * V, P * V**2, V**3):
            self.assertZero(residual.coeff_monomial(monomial))
        self.assertZero(av - (p - bv))
        self.assertZero(av - bv - m * q / (2 * p))
        self.assertZero(
            residual.coeff_monomial(V**2) - sp.diff(n, s, 2) / 2 + av * bv
        )
        expected_pv = (
            sp.diff(n, t, s) - 2 * p * sp.diff(n, s) / m
            - u * bv - (av - bv) * bp
        )
        self.assertZero(residual.coeff_monomial(P * V) - expected_pv)

        # Dropping either product contribution changes the raw PV coefficient.
        wrong_raw_pv = sp.diff(n, t, s) - p * sp.diff(n, s) / m
        self.assertNotEqual(zero(raw.coeff_monomial(P * V) - wrong_raw_pv), 0)
        self.assertZero(
            sp.diff(u, s)
            - (q - p**2 / m - 2 * sp.diff(n, s, 2) / m)
        )

    def test_differentiated_raw_pv_compatibility(self):
        data = raw_surface()
        t, s, P, V = (data[name] for name in ("t", "s", "P", "V"))
        m, p, q, j, n = (
            data[name] for name in ("m", "p", "q", "j", "n")
        )
        av = sp.diff(data["A"], V)
        bv = data["bv"]
        f = 2 * av * bv
        self.assertZero(f - p**2 / 2 + m**2 * q**2 / (8 * p**2))

        # Start from the actual polynomial product residual, not a copied ODE.
        raw_pv = sp.Poly(
            sp.expand(data["A0"] - data["A"] * data["B"]), P, V
        ).coeff_monomial(P * V)
        differentiated = sp.diff(raw_pv, s).subs(
            {
                sp.diff(n, t, s, 2): sp.diff(f, t),
                sp.diff(n, s, 2): f,
            },
            simultaneous=True,
        )
        target = -5 * m**2 * q * (2 * p * j - 3 * q**2) / (48 * p**3)
        self.assertZero(differentiated - target)
        self.assertZero(sp.diff(data["bp"], s) - q / 4 + m * j / (12 * p))

        # If u_s misses -p^2/m, the residual changes even on the correct ODE.
        wrong = differentiated - bv * p**2 / m
        ode = {j: 3 * q**2 / (2 * p)}
        self.assertZero(differentiated.subs(ode, simultaneous=True))
        self.assertNotEqual(zero(wrong.subs(ode, simultaneous=True)), 0)

    def test_quadratic_selected_gradient_and_contradiction(self):
        data = raw_surface()
        s, U, P, V = (data[name] for name in ("s", "U", "P", "V"))
        m, p, q, j, n = (
            data[name] for name in ("m", "p", "q", "j", "n")
        )
        A, B, D, lam = (data[name] for name in ("A", "B", "D", "lam"))
        av = sp.diff(A, V)

        # Impose the formal factorization, then differentiate before restriction.
        factored = (U + A) * (U + B)
        QU = sp.diff(factored, P) - D * sp.diff(factored, V) \
            + lam * sp.diff(factored, U)
        QV = sp.diff(factored, s)
        restricted = (QV - av * QU).subs(U, -A)
        bracket = sp.diff(A, s) - av * (sp.diff(A, P) - D * av + lam)
        self.assertZero(restricted - (B - A) * bracket)
        bracket_poly = sp.Poly(sp.expand(bracket), P, V)
        self.assertLessEqual(bracket_poly.total_degree(), 1)
        self.assertZero(bracket_poly.coeff_monomial(V))
        raw_slope = bracket_poly.coeff_monomial(P)
        expected = (
            (p**2 - 2 * sp.diff(n, s, 2)) / m + 2 * q
            + m * j / (12 * p) + m * q**2 / (8 * p**2)
        )
        self.assertZero(raw_slope - expected)
        f = 2 * av * data["bv"]
        slope = raw_slope.subs(sp.diff(n, s, 2), f)
        self.assertZero(
            slope - (2 * m * p * j + 9 * m * q**2 + 48 * p**2 * q)
            / (24 * p**2)
        )
        self.assertZero(
            slope.subs(j, 3 * q**2 / (2 * p))
            - q * (m * q + 4 * p**2) / (2 * p**2)
        )

        # Uniform point-jet contradiction, retaining m and p as nonzero units.
        M, pp = sp.symbols("M pp", nonzero=True)
        qq = -4 * pp**2 / M
        jj = 3 * qq**2 / (2 * pp)
        self.assertZero(M * jj + 9 * pp * qq + 12 * pp**3 / M)
        self.assertNotEqual(zero(-12 * pp**3 / M), 0)

        # Finite cofactor fixture: a repeated plane factor loses gradient units.
        eta, x = sp.symbols("eta x", nonzero=True)
        G = V - P**2
        good = eta * G
        bad = G**2
        on_curve = {P: x, V: x**2}
        self.assertEqual(sp.diff(good, V).subs(on_curve), eta)
        self.assertEqual(sp.diff(bad, V).subs(on_curve), 0)
        self.assertEqual(sp.diff(bad, P).subs(on_curve), 0)

    def test_reciprocal_family_and_nonzero_constant_field_boundaries(self):
        t, s, tau, d = sp.symbols("t s tau d")
        c = sp.symbols("c", nonzero=True)
        T = t - tau
        m = d + c / T
        p, q, j = (sp.diff(m, t, order) for order in (1, 2, 3))
        self.assertZero(2 * p * j - 3 * q**2)
        r = q / (2 * p)
        self.assertZero(sp.diff(r, t) - r**2)
        self.assertZero(t + 1 / r - tau)
        self.assertZero(T**2 * p + c)
        self.assertZero(m + T * p - d)
        self.assertZero(p / 2 - m * q / (4 * p) - d / (2 * T))

        # A nonconstant s-coefficient solves the t-ODE but fails m_s=0.
        cs = sp.Function("c")(s)
        false_joint_constant_family = d + cs / T
        p1, q1, j1 = (
            sp.diff(false_joint_constant_family, t, order)
            for order in (1, 2, 3)
        )
        self.assertZero(2 * p1 * j1 - 3 * q1**2)
        self.assertNotEqual(zero(sp.diff(false_joint_constant_family, s)), 0)

        # If m_tt=0, compatibility alone vanishes but the conic V-slope vanishes.
        linear_m = t + d
        linear_p = sp.diff(linear_m, t)
        linear_q = sp.diff(linear_m, t, 2)
        self.assertEqual(linear_q, 0)
        self.assertZero(linear_m * linear_q / (2 * linear_p))
        self.assertZero(
            2 * linear_p * sp.diff(linear_m, t, 3) - 3 * linear_q**2
        )


if __name__ == "__main__":
    unittest.main()
