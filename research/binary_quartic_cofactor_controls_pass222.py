"""Finite exact-algebra controls for the two saved quartic notes222.

Standalone: no retained checker, solver, proof, or workspace data is imported.
Formal potential residuals are kept until their explicit substitutions.
Degree fixtures are formal plane algebra, not actual translation frames.
They distinguish a strict degree contradiction from equality or unsaturated
top factors; they do not establish any geometric realization.

Actual field return, scalar calibration, selected-factor simplicity, LND
and Wang results, and all universal degree conclusions remain written-proof
inputs. No223/224 calculation or claim is included. Root alone may execute
this saved checker after its complete source review.
"""

from math import factorial
import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, X, y = sp.symbols("U V X y")


def clean(expr):
    return sp.cancel(sp.expand(expr))


def taylor(expr, order):
    return sum(
        sp.diff(expr, t, i, rho, order - i)
        * U**i * V**(order - i)
        / (factorial(i) * factorial(order - i))
        for i in range(order + 1)
    )


class BinaryQuarticCofactorControls(unittest.TestCase):
    def zero(self, expr):
        self.assertEqual(clean(expr), 0)

    def test_arbitrary_q_formal_gradients_with_prior_residuals(self):
        q, k, n, ell, m = [sp.Function(name)(t, rho) for name in ("q", "k", "n", "ell", "m")]
        f = taylor(q, 2) + taylor(k, 1) + n
        return_poly = sp.diff(f, V)
        c = sp.diff(f, rho)
        A2 = sp.diff(q, rho, 2) / 2
        S = taylor(q, 3) + taylor(k, 2) + taylor(n, 1)
        Q = taylor(q, 4) + taylor(k, 3) + taylor(n, 2) - sp.diff(ell, t) * U - sp.diff(ell, rho) * V - m
        for left, right in [
            (sp.diff(S, U), sp.diff(f, t)),
            (sp.diff(S, V), c),
            (sp.diff(return_poly, U), sp.diff(q, t, rho)),
            (sp.diff(return_poly, V), 2 * A2),
            (sp.diff(c, U), sp.diff(return_poly, t)),
            (sp.diff(c, V), sp.diff(return_poly, rho)),
            (sp.diff(Q, U), sp.diff(S, t) - sp.diff(ell, t)),
            (sp.diff(Q, V), sp.diff(S, rho) - sp.diff(ell, rho)),
        ]:
            self.zero(left - right)

        # Chain-rule jets are independent symbols, with only the identities
        # just reconstructed imposed. T means ell-S, not its evaluation.
        A, R, c0, T, Q0, w = sp.symbols("A R c0 T Q0 w")
        RU, Rt, Rr, ft, Lt, Lr = sp.symbols("RU Rt Rr ft Lt Lr")
        e3, e4 = sp.symbols("e3 e4")
        H = A * T**2 + R * c0 * T + R**2 * Q0
        HU = (
            sp.diff(H, R) * RU + sp.diff(H, c0) * Rt
            - sp.diff(H, T) * ft + sp.diff(H, Q0) * (-Lt - Rt * w)
        )
        HV = (
            sp.diff(H, R) * 2 * A + sp.diff(H, c0) * Rr
            - sp.diff(H, T) * c0 + sp.diff(H, Q0) * (-Lr - Rr * w)
        )
        B1, C1 = ft + RU * w, c0 + 2 * A * w
        expected_U = -R * (C1 * B1 + R * Lt)
        expected_V = -R * (C1**2 + R * Lr)
        # e3=T-Rw and e4=A w^2+c w+Q. No prior relation is hidden.
        substitution = {T: R * w + e3, Q0: -A * w**2 - c0 * w + e4}
        residual_U = e3 * (-2 * A * ft + RU * c0 + R * Rt) + 2 * R * RU * e4
        residual_V = R * Rr * e3 + 4 * A * R * e4
        self.zero(HU.subs(substitution, simultaneous=True) - expected_U - residual_U)
        self.zero(HV.subs(substitution, simultaneous=True) - expected_V - residual_V)
        self.zero((HU.subs(substitution, simultaneous=True) - expected_U).subs({e3: 0, e4: 0}))
        self.zero((HV.subs(substitution, simultaneous=True) - expected_V).subs({e3: 0, e4: 0}))
        self.zero(H.subs(substitution, simultaneous=True) - (R * C1 * e3 + A * e3**2 + R**2 * e4))

    def test_undivided_wedge_identity_and_differential_residual(self):
        R, B, C, Lt, Lr = sp.symbols("R B C Lt Lr")
        yt, yr, yv, vt, vr, vv, wt, wr, wv = sp.symbols("yt yr yv vt vr vv wt wr wv")
        dy = sp.Matrix([[yt, yr, yv]])
        dvartheta = sp.Matrix([[vt, vr, vv]])
        dw = sp.Matrix([[wt, wr, wv]])
        middle = R * dvartheta + sp.Matrix([[B, C, 0]])
        J = sp.Matrix.vstack(dy, middle, dw).det()
        DU = R * (yv * vr - yr * vv) + C * yv
        DV = R * (yt * vv - yv * vt) - B * yv
        HU, HV = -R * (C * B + R * Lt), -R * (C**2 + R * Lr)
        scaled_dw = -B * dy - C * dvartheta + sp.Matrix([[Lt, Lr, 0]])
        differential_residual = R * dw - scaled_dw
        residual_wedge = sp.Matrix.vstack(dy, middle, differential_residual).det()
        # All entries here are polynomials, including at formal R=0.
        self.zero(R**3 * J - DU * HU - DV * HV - R**2 * residual_wedge)
        self.zero(R**2 * sp.Matrix.vstack(dy, middle, scaled_dw).det() - DU * HU - DV * HV)
        a_minor = yv * vr - yr * vv
        b_minor = yt * vv - yv * vt
        explicit_RJ = (
            -(R * Lt + B * C) * a_minor
            -(R * Lr + C**2) * b_minor + yv * (B * Lr - C * Lt)
        )
        self.zero(sp.Matrix.vstack(dy, middle, scaled_dw).det() - explicit_RJ)

    def test_all_six_raw_quadratic_ratio_coefficients_and_collapse(self):
        alpha = sp.symbols("alpha", nonzero=True)
        beta, gamma = sp.symbols("beta gamma")
        q = (alpha * t**2 + beta * t + gamma) / rho
        names = ("kap", "zeta", "lam", "omega", "theta", "k")
        funcs = {name: sp.Function(name)(t, rho) for name in names}
        jets = {name: sp.symbols(name) for name in names}
        dt = {name: sp.symbols(name + "_t") for name in names}
        dr = {name: sp.symbols(name + "_r") for name in names}
        replace = {}
        for name in names:
            replace[funcs[name]] = jets[name]
            replace[sp.diff(funcs[name], t)] = dt[name]
            replace[sp.diff(funcs[name], rho)] = dr[name]
        capital_y = y + t * X
        capital_z = (
            alpha * y**2 / rho + funcs["kap"] * y + funcs["zeta"]
            + (sp.diff(q, t) * y + sp.diff(q, rho) * funcs["theta"] + funcs["k"]) * X
            + q * X**2
        )
        capital_w = funcs["lam"] * y + funcs["omega"] + funcs["theta"] * X + rho * X**2
        raw_jacobian = sp.Matrix([capital_y, capital_z, capital_w]).jacobian([t, rho, y]).det()
        raw_jacobian = raw_jacobian.xreplace(replace)
        H, eta = sp.symbols("H eta")
        qr, qtr, qrr = sp.diff(q, rho), sp.diff(q, t, rho), sp.diff(q, rho, 2)
        # These two substitutions only introduce the displayed definitions.
        raw_jacobian = raw_jacobian.subs(dt["k"], H + jets["kap"] - qtr * jets["theta"] - qr * dt["theta"])
        raw_jacobian = raw_jacobian.subs(dt["theta"], jets["lam"] - eta)
        Zr = sp.diff(capital_z, rho).xreplace(replace)
        Wr = sp.diff(capital_w, rho).xreplace(replace)
        first_factor = dt["kap"] * y + dt["zeta"] + H * X
        second_factor = eta * X - dt["lam"] * y - dt["omega"]
        self.zero(raw_jacobian - first_factor * Wr - Zr * second_factor)
        poly = sp.Poly(sp.expand(raw_jacobian), X, y)
        raw_coefficients = [
            (y**3, alpha * dt["lam"] / rho**2),
            (X * y**2, -alpha * eta / rho**2 - qtr * dt["lam"]),
            (X**2 * y, dt["kap"] - qr * dt["lam"] + qtr * eta),
            (y**2, dt["kap"] * dr["lam"] - dr["kap"] * dt["lam"] + alpha * dt["omega"] / rho**2),
            (X**3, H + qr * eta),
            (X**2, dt["zeta"] + H * dr["theta"] - qr * dt["omega"]
             + (qrr * jets["theta"] + qr * dr["theta"] + dr["k"]) * eta),
        ]
        for monomial, expected in raw_coefficients:
            self.zero(poly.coeff_monomial(monomial) - expected)
        gates = [dt["lam"], eta, dt["kap"], dt["omega"], H, dt["zeta"]]
        surviving_rows = [alpha * dt["lam"] / rho**2, -alpha * eta / rho**2,
                          dt["kap"], alpha * dt["omega"] / rho**2, H, dt["zeta"]]
        prior = {}
        for (monomial, _), gate, surviving in zip(raw_coefficients, gates, surviving_rows):
            self.zero(poly.coeff_monomial(monomial).subs(prior) - surviving)
            prior[gate] = 0
        first_five = dict.fromkeys(gates[:5], 0)
        self.zero(raw_jacobian.subs(first_five) - dt["zeta"] * Wr)
        self.zero(raw_jacobian.subs(prior))

    def test_saturated_degree_controls_and_equality_boundaries(self):
        v = sp.symbols("v")
        for g in (1, 2, 3):
            with self.subTest(saturated_degree=g):
                relation = U**g - V**(g - 1)
                cofactor = sp.prod(V - j * U for j in range(1, 7 - g))
                eliminant = sp.expand(relation * cofactor)
                evaluation = {U: v**(g - 1), V: v**g}
                self.zero(relation.subs(evaluation, simultaneous=True))
                self.assertEqual(sp.Poly(eliminant, U, V).total_degree(), 6)
                q1 = sp.expand(cofactor.subs(evaluation, simultaneous=True))
                self.assertEqual(sp.Poly(q1, v).degree(), (6 - g) * g)
                self.assertEqual((6 - g) * g > 3 * g, g < 3)
                # Other leading factors do not vanish on the leading vector.
                self.zero(cofactor.subs({U: 0, V: 1}, simultaneous=True) - 1)

        # Formal equality at g=m=3 is NOT an actual frame: it only shows
        # that the scalar degree/divisibility comparison is not strict.
        cubic_relation = U**3 - V**2
        cubic_cofactor = V**3
        evaluation = {U: v**2, V: v**3}
        self.zero(cubic_relation.subs(evaluation, simultaneous=True))
        self.zero(cubic_cofactor.subs(evaluation, simultaneous=True) - (v**3)**3)
        self.assertEqual(sp.Poly(cubic_relation * cubic_cofactor, U, V).total_degree(), 6)
        self.assertEqual(sp.Poly((v**3)**3, v).degree(), 9)

        # Without saturation, the top cofactor can lose evaluated degree.
        # Here g=2,m=4, and deg(q1)=6 rather than the invalid prediction8.
        quadratic_relation = U**2 - V
        unsaturated_cofactor = U**2 * V**2
        evaluation = {U: v, V: v**2}
        self.zero(quadratic_relation.subs(evaluation, simultaneous=True))
        q1 = sp.expand(unsaturated_cofactor.subs(evaluation, simultaneous=True))
        self.assertEqual(sp.Poly(q1, v).degree(), 6)
        self.zero(q1 - (v**2)**3)
        self.assertEqual(sp.Poly(quadratic_relation * unsaturated_cofactor, U, V).total_degree(), 6)

    def test_zero_linear_term_cubic_and_actual_pair_transport(self):
        A, B = sp.symbols("A B", nonzero=True)
        q = (A * t**3 + B * t**2) / rho
        h = t / rho
        theta, nu, kr = sp.symbols("theta nu kr")
        self.zero(taylor(q, 2).subs({U: h, V: 1}, simultaneous=True) - A * h**3)
        self.zero(taylor(q, 3).subs({U: h, V: 1}, simultaneous=True))
        line_return = (sp.diff(taylor(q, 2), V) + kr).subs({U: h * theta + nu, V: theta}, simultaneous=True)
        self.zero(sp.expand(line_return).coeff(theta) + A * t**3 / rho**3)

        a, b, c, d, e, f = sp.symbols("a b c d e f")
        det = a * d - b * c
        XX, YY, XP, YP = sp.symbols("XX YY XP YP")
        forward = {XP: a * XX + b * YY, YP: c * XX + d * YY}
        inverse = {XX: (d * XP - b * YP) / det, YY: (-c * XP + a * YP) / det}
        for variable, expr in forward.items():
            self.zero(expr.subs(inverse, simultaneous=True) - variable)
        for variable, expr in inverse.items():
            self.zero(expr.subs(forward, simultaneous=True) - variable)
        original = (a * XX + b * YY) * (c * XX + d * YY)**2 * (e * XX + f * YY)
        normalized = XP * YP**2 * ((e * d - f * c) * XP + (f * a - e * b) * YP) / det
        self.zero(original.subs(inverse, simultaneous=True) - normalized)
        l, m = a + b * t, c + d * t
        yp, vp = det * y / l, theta / l - 2 * rho * b * y / l**2
        self.zero(yp - (m / l) * vp / (rho / l**2)
                  + (l * m * theta - rho * (b * m + d * l) * y) / (rho * l))
        self.zero(l**2 * theta - 2 * rho * l * b * y - l**3 * vp)
        self.zero(sp.Matrix([yp, vp]).jacobian([y, theta]).det() - det / l**2)


if __name__ == "__main__":
    unittest.main()
