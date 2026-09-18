"""Finite exact-algebra controls for the fourth potential in pass296.

The coefficient functions k(t,s), n(t,s), ell(t,s), and h0(t,s) remain
arbitrary. Mixed derivatives commute formally. These checks reconstruct
the literal potentials, not sampled coefficient polynomials or a solver's
output. A separate generic point-jet calculation retains every moving
intercept derivative and displays, rather than discards, the level residual.

Scope: symbolic identities, formal polynomial degree bounds, and the algebra
used in the written minor-ideal argument. Passing does not establish actual
chart entry, a finite coefficient field, whole-line return, an LND theorem,
the universal unit-ideal conclusion, a Bezout bound, or recognition. No other
saved proof or checker is imported. Root owns the sole canonical execution
after a complete saved-source read; the author does not execute this file.
"""

import unittest

import sympy as sp


def reduced(expression):
    """Exact rational reduction; coefficient functions stay symbolic."""
    return sp.cancel(sp.expand(expression))


def determinant(first, second, third):
    """Determinant of three covector rows in the order (dt, ds, dv)."""
    return first.dot(second.cross(third))


def polynomial_primitive(expression, variable):
    """Integrate only the displayed formal polynomial variable, from zero."""
    polynomial = sp.Poly(sp.expand(expression), variable)
    return sp.Add(*(
        coefficient * variable ** (power[0] + 1) / (power[0] + 1)
        for power, coefficient in polynomial.terms()
    ))


def point_jets():
    """Independent point values, with only H_U=B-gamma*lambda imposed."""
    X, m, gamma, lam, hu, hp, hv = sp.symbols("X m gamma lam hu hp hv")
    # No symbol is specialized to zero; m is inverted in the rational field.
    yt, ys, yv, pt, ps, pv, vt, vs, vv = sp.symbols(
        "yt ys yv pt ps pv vt vs vv"
    )
    dt = sp.Matrix([1, 0, 0])
    ds = sp.Matrix([0, 1, 0])
    dv = sp.Matrix([0, 0, 1])
    dy = sp.Matrix([yt, ys, yv])
    dp = sp.Matrix([pt, ps, pv])
    dtheta = sp.Matrix([vt, vs, vv])
    D = gamma / m
    B = hu + gamma * lam
    beta = B / m
    gt = -(hp + lam * B) / m
    gs = -hv / m - lam**2
    dg = -D * dy - beta * dp - lam * dtheta + gt * dt + gs * ds
    Arow = dy + X * dp + X**2 * dt
    Brow = gamma * dp + m * dtheta + B * dt + m * lam * ds
    Brow += X * (gamma * dt + m * ds)
    Crow = dg + X * dtheta + X**2 * ds
    return locals()


class PrincipalFourthPotentialControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t, cls.s, cls.U, cls.P, cls.V = sp.symbols("t s U P V")
        t, s, U, P, V = cls.t, cls.s, cls.U, cls.P, cls.V
        cls.k, cls.n, cls.ell, cls.h0 = (
            sp.Function(name)(t, s) for name in ("k", "n", "ell", "h0")
        )
        k, n, ell, h0 = cls.k, cls.n, cls.ell, cls.h0

        def taylor(function, degree):
            return sp.Add(*(
                sp.diff(function, t, i, s, degree - i)
                * P**i * V**(degree - i)
                / (sp.factorial(i) * sp.factorial(degree - i))
                for i in range(degree + 1)
            ))

        cls.m = m = sp.diff(k, s)
        cls.F = F = taylor(k, 2) + taylor(n, 1)
        cls.gamma = gamma = 2 * P + sp.diff(k, t)
        cls.g = g = (ell - gamma * U - F) / m
        cls.B = B = 2 * U + sp.diff(F, P)
        cls.lam = lam = sp.diff(F, V) / m
        cls.D = gamma / m
        cls.beta = B / m
        cls.H = H = reduced(
            U**2 + sp.diff(F, P) * U + sp.diff(F, V) * g
            + taylor(k, 3) + taylor(n, 2)
            - sp.diff(ell, t) * P - sp.diff(ell, s) * V
        )
        cls.gradient = tuple(sp.diff(H, variable) for variable in (U, P, V))
        hu, hp, hv = cls.gradient
        cls.R = tuple(map(reduced, (
            hp - cls.D * hv + lam * hu,
            sp.diff(H, t) - sp.diff(h0, t) - cls.beta * hv + lam * hp,
            sp.diff(H, s) - sp.diff(h0, s),
        )))

    def assert_zero(self, expression):
        self.assertEqual(reduced(expression), 0)

    def test_raw_generic_potentials_closedness_and_correction(self):
        t, s, U, P, V = self.t, self.s, self.U, self.P, self.V
        m, F, g, H = self.m, self.F, self.g, self.H
        hu, hp, hv = self.gradient
        RU, RP, RV = self.R
        self.assert_zero(hu - (self.B - self.gamma * self.lam))
        self.assert_zero(hp + m * sp.diff(g, t) + self.lam * self.B)
        self.assert_zero(hv + m * sp.diff(g, s) + m * self.lam**2)
        self.assert_zero(sp.diff(F, V, t) - sp.diff(F, P, s))
        for first, second, a, b in (
            (RU, RP, P, U), (RU, RV, V, U), (RP, RV, V, P)
        ):
            self.assert_zero(sp.diff(first, a) - sp.diff(second, b))
        self.assert_zero(
            sp.diff(RU, U)
            - sp.diff(self.k, t, 2)
            + 2 * self.D * sp.diff(m, t) - self.D**2 * sp.diff(m, s)
        )

        # Negative control: omitting lambda*d_formal(H) is not closed.
        alpha_u = hp - self.D * hv
        alpha_p = sp.diff(H, t) - sp.diff(self.h0, t) - self.beta * hv
        alpha_v = sp.diff(H, s) - sp.diff(self.h0, s) - self.lam * hv
        wrong_up = reduced(sp.diff(alpha_u, P) - sp.diff(alpha_p, U))
        wrong_uv = reduced(sp.diff(alpha_u, V) - sp.diff(alpha_v, U))
        self.assert_zero(wrong_up + sp.diff(m, t) * hu / m)
        self.assert_zero(wrong_uv + sp.diff(m, s) * hu / m)
        self.assertNotEqual(wrong_up, 0)
        self.assertNotEqual(wrong_uv, 0)

    def test_generic_path_primitive_and_monic_division(self):
        U, P, V = self.U, self.P, self.V
        RU, RP, RV = self.R
        Q = reduced(
            polynomial_primitive(RU, U)
            + polynomial_primitive(RP.subs(U, 0), P)
            + polynomial_primitive(RV.subs({U: 0, P: 0}), V)
        )
        self.assert_zero(Q.subs({U: 0, P: 0, V: 0}))
        for variable, component in zip((U, P, V), self.R):
            self.assert_zero(sp.diff(Q, variable) - component)
            self.assertLessEqual(sp.Poly(component, U, P, V).total_degree(), 3)
        self.assertLessEqual(sp.Poly(self.H, U, P, V).total_degree(), 3)
        self.assertLessEqual(sp.Poly(Q, U, P, V).total_degree(), 4)
        self.assertLessEqual(sp.Poly(Q, U).degree(), 2)
        e = reduced(sp.diff(RU, U) / 2)
        self.assert_zero(sp.diff(e, V))
        self.assertLessEqual(sp.Poly(e, P).degree(), 2)
        q0 = sp.symbols("q0")
        remainder = reduced(Q - q0 - e * (self.H - self.h0))
        polynomial = sp.Poly(remainder, U)
        self.assertLessEqual(polynomial.degree(), 1)
        R1, R0 = polynomial.coeff_monomial(U), polynomial.coeff_monomial(1)
        self.assertLessEqual(sp.Poly(R1, P, V).total_degree(), 4)
        self.assertLessEqual(sp.Poly(R0, P, V).total_degree(), 5)
        self.assert_zero(Q - q0 - e * (self.H - self.h0) - R1 * U - R0)

    def test_independent_point_rows_all_jacobian_coefficients(self):
        j = point_jets()
        X, m, lam = j["X"], j["m"], j["lam"]
        hu, hp, hv, D, beta = (j[key] for key in ("hu", "hp", "hv", "D", "beta"))
        dy, dp, dtheta, dt, ds = (j[key] for key in ("dy", "dp", "dtheta", "dt", "ds"))
        Arow, Brow, Crow = (j[key] for key in ("Arow", "Brow", "Crow"))
        row_residual = Crow + D * Arow - (X - lam) * Brow / m
        row_residual += (hu * (dp + X * dt) + hp * dt + hv * ds) / m
        for entry in row_residual:
            self.assert_zero(entry)

        yt, ys, yv = dy
        pt, ps, pv = dp
        vt, vs, vv = dtheta
        J = reduced(determinant(Arow, Brow, Crow))
        coefficients = sp.Poly(J, X)
        self.assertLessEqual(coefficients.degree(), 2)
        tangent = hu * yv + hp * pv + hv * vv
        J1 = hu * ((pt + vs + lam) * yv - yt * pv - ys * vv)
        J1 += hp * (yv + (vs + lam) * pv - ps * vv)
        J1 += hv * (pt * vv - pv * vt - beta * pv - D * yv)
        KU = determinant(dy, dp, dtheta) + (beta * ys - lam * yt) * pv
        KU += (lam * pt - beta * ps) * yv
        KP = yv * (vs + D * ps + lam) - ys * (vv + D * pv)
        KV = yt * (vv + D * pv) - yv * (vt + D * pt + beta)
        self.assert_zero(coefficients.coeff_monomial(X**2) - tangent)
        self.assert_zero(coefficients.coeff_monomial(X) - J1)
        self.assert_zero(coefficients.coeff_monomial(1) - hu * KU - hp * KP - hv * KV)

        # These are H_t-h0_t and H_s-h0_s after the actual level's
        # t/s derivatives; its v derivative is not silently imposed.
        level_t = -hu * yt - hp * pt - hv * vt
        level_s = -hu * ys - hp * ps - hv * vs
        reduced_J1 = (hp - D * hv) * yv
        reduced_J1 += (level_t - beta * hv) * pv + (level_s - lam * hv) * vv
        self.assert_zero(J1 - reduced_J1 - (pt + vs + lam) * tangent)
        corrected_dv = (hp - D * hv + lam * hu) * yv
        corrected_dv += (level_t - beta * hv + lam * hp) * pv + level_s * vv
        self.assert_zero(J1 - corrected_dv - (pt + vs) * tangent)

    def test_wedge_minor_algebra_and_missing_calibration_control(self):
        j = point_jets()
        X, m, lam = j["X"], j["m"], j["lam"]
        hu, hp, hv, D, beta = (j[key] for key in ("hu", "hp", "hv", "D", "beta"))
        dy, dp, dtheta, dt, ds, dv = (
            j[key] for key in ("dy", "dp", "dtheta", "dt", "ds", "dv")
        )
        Bbar = dtheta + D * dp + beta * dt + lam * ds
        RH = hu * dp + hp * dt + hv * ds
        qu = hp - D * hv + lam * hu
        qp = -hu * dy[0] - hp * dp[0] - hv * dtheta[0] - beta * hv + lam * hp
        qv = -hu * dy[1] - hp * dp[1] - hv * dtheta[1]
        RQ = qu * dp + qp * dt + qv * ds
        tangent = hu * dy[2] + hp * dp[2] + hv * dtheta[2]
        syzygy = hu * dy + hv * Bbar + RQ - lam * RH
        for entry in syzygy - tangent * dv:
            self.assert_zero(entry)
        J0 = -determinant(dy, Bbar, RH)
        self.assert_zero(
            hu * J0 - determinant(RH, RQ, Bbar)
            + tangent * determinant(RH, dv, Bbar)
        )
        self.assert_zero(
            hv * J0 + determinant(RH, RQ, dy)
            - tangent * determinant(RH, dv, dy)
        )
        rhs = ((X + lam) * hu - qu) * (dp + X * dt)
        rhs += ((X + lam) * hp - qp) * dt + ((X + lam) * hv - qv) * ds
        all_X = hu * j["Arow"] + hv * j["Brow"] / m - rhs
        for entry in all_X - tangent * dv:
            self.assert_zero(entry)

        minor_up = hu * qp - hp * qu
        self.assert_zero(hp**2 - hu * (qp - lam * hp) - D * hp * hv + minor_up)
        cu, cp, cv = sp.symbols("cu cp cv")
        bezout = cu * hu + cp * hp + cv * hv
        side = cu * hu + cv * hv
        self.assert_zero(bezout**2 - cp**2 * hp**2 - side * (bezout + cp * hp))

        # A formal curve can have a unit first gradient and dependent
        # gradients if the calibrated scalar is omitted. This fixture is
        # not claimed to satisfy the actual chart or fourth-potential gates.
        u, p, v, parameter = sp.symbols("u p v parameter")
        first = u**2 + p
        second = first**2
        substitution = {u: parameter, p: -parameter**2, v: 0}
        hgrad = [sp.diff(first, variable).subs(substitution) for variable in (u, p, v)]
        qgrad = [sp.diff(second, variable).subs(substitution) for variable in (u, p, v)]
        self.assertEqual(hgrad[1], 1)
        for a, b in ((0, 1), (0, 2), (1, 2)):
            self.assert_zero(hgrad[a] * qgrad[b] - hgrad[b] * qgrad[a])


if __name__ == "__main__":
    unittest.main()
