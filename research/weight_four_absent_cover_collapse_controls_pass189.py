"""Necessary exact-algebra controls for absent zero-R cover collapse189.

The formal coefficient jets check the integral and coefficient recurrences.
They do not prove the actual function-field equality, a curve pole-degree
bound, rationality of K, or an integer-valued valuation theorem. The last
method includes formal covers that satisfy the displayed Euler equations but
do not supply the actual field return required by the written proof.
No older checker, proof implementation, or solver internals are imported.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


def coefficient_dt(expression, chains, extra=()):
    result = 0
    for chain in chains:
        result += sum(sp.diff(expression, left) * right
                      for left, right in zip(chain, chain[1:]))
    result += sum(sp.diff(expression, left) * right for left, right in extra)
    return sp.expand(result)


class AbsentCoverCollapseControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_integral_and_unrestricted_top_coefficient_gates(self):
        U, n = sp.symbols("U n")
        a, b, c = (sp.symbols(f"{name}0:4") for name in ("a", "b", "c"))
        d0 = sp.symbols("d0", nonzero=True)
        d = (d0, *sp.symbols("d1:3"))
        h = sp.symbols("h0:3")
        M, Mt, Mn, Mtt, Mtn, Mnn = sp.symbols("M Mt Mn Mtt Mtn Mnn")
        W0, W0t, W0n = sp.symbols("W0 W0t W0n")
        chains = (a, b, c, d, h)
        dt = lambda expression: coefficient_dt(
            expression, chains, ((M, Mt), (Mt, Mtt), (Mn, Mtn), (W0, W0t))
        )

        def dn(expression):
            return (sp.diff(expression, n) + sp.diff(expression, M) * Mn
                    + sp.diff(expression, Mt) * Mtn
                    + sp.diff(expression, Mn) * Mnn
                    + sp.diff(expression, W0) * W0n)

        rho = a[0] * n**2 + b[0] * n + c[0]
        eta = sp.diff(rho, n)
        F = d[0] * U**3 + h[0] * U**2
        FU = sp.diff(F, U)
        P = dt(rho) * U - eta * F + M
        integral = (
            a[0] * F**2 - dt(eta) * U * F
            - eta * (d[1] * U**4 / 4 + h[1] * U**3 / 3)
            + dt(dt(rho)) * U**2 / 2 + Mt * U - Mn * F + W0
        )
        self.zero(sp.diff(integral, U) - (dt(P) - FU * dn(P)))
        expanded = sp.expand(integral)
        scalar_equation = sp.expand(dt(integral) - FU * dn(integral))
        self.zero(scalar_equation.coeff(U, 8))
        self.zero(scalar_equation.coeff(U, 7))
        gate6 = sp.Rational(7, 2) * d[0] * (a[0] * d[1] + 2 * d[0] * a[1])
        gate5 = (12 * a[1] * d[0] * h[0] + 3 * a[0] * d[1] * h[0]
                 + 4 * a[0] * d[0] * h[1] + 3 * d[0]**2 * Mnn)
        self.zero(scalar_equation.coeff(U, 6) - gate6)
        self.zero(scalar_equation.coeff(U, 5) - gate5)
        gate2 = (dt(dt(dt(rho))) / 2 - h[1] * Mn
                 - 3 * h[0] * Mtn - 3 * d[0] * W0n)
        self.zero(scalar_equation.coeff(U, 2) - gate2)
        for power in (2, 5, 6, 8):
            Wj = expanded.coeff(U, power)
            Wjm2 = expanded.coeff(U, power - 2)
            Wjm1 = expanded.coeff(U, power - 1)
            self.zero(scalar_equation.coeff(U, power)
                      - dt(Wj) + 3 * d[0] * dn(Wjm2) + 2 * h[0] * dn(Wjm1))
        mu = a[0] * h[0] * d[1] / d[0]**2 - 4 * a[0] * h[1] / (3 * d[0])
        prior = {a[1]: -a[0] * d[1] / (2 * d[0]), Mnn: mu}
        self.zero(d[0]**2 * gate5.subs(prior, simultaneous=True))
        self.zero(gate6.subs(a[1], -a[0] * d[1] / (2 * d[0])))
        # These polynomial identities do not prove that a scalar equation
        # holds for an actual frame, or identify the constants of a field.

    def test_u2_primitive_and_linear_cover_u4_gate(self):
        U, n, t = sp.symbols("U n t")
        a, b, c = (sp.symbols(f"{name}0:4") for name in ("a", "b", "c"))
        d0 = sp.symbols("d0", nonzero=True)
        d = (d0, *sp.symbols("d1:3"))
        h = sp.symbols("h0:3")
        mu = sp.symbols("mu0:3")
        M1 = sp.symbols("M1_0:3")
        M0 = sp.symbols("M0_0:3")
        W00 = sp.symbols("W00")
        chains = (a, b, c, d, h, mu, M1, M0)
        dt = lambda expression: coefficient_dt(expression, chains)
        rho = a[0] * n**2 + b[0] * n + c[0]
        eta = sp.diff(rho, n)
        F = d[0] * U**3 + h[0] * U**2
        M = mu[0] * n**2 / 2 + M1[0] * n + M0[0]
        W0 = (
            a[3] * n**3 / (18 * d[0])
            + (b[3] / 2 - h[1] * mu[0] - 3 * h[0] * mu[1]) * n**2 / (6 * d[0])
            + (c[3] / 2 - h[1] * M1[0] - 3 * h[0] * M1[1]) * n / (3 * d[0])
            + W00
        )
        W = sp.expand(
            a[0] * F**2 - dt(eta) * U * F
            - eta * (d[1] * U**4 / 4 + h[1] * U**3 / 3)
            + dt(dt(rho)) * U**2 / 2 + dt(M) * U - sp.diff(M, n) * F + W0
        )
        W1, W2 = W.coeff(U, 1), W.coeff(U, 2)
        residual2 = dt(W2) - 3 * d[0] * sp.diff(W0, n) - 2 * h[0] * sp.diff(W1, n)
        self.zero(d[0] * residual2)
        self.zero(sp.expand(W0).coeff(n, 3) - a[3] / (18 * d[0]))
        self.zero(sp.expand(W - W0).coeff(n, 3))
        # The written proof uses these primitives and actual field return to
        # conclude L=K(n). No such field assertion is a finite test outcome.

        linear_substitution = {value: 0 for value in (*a, *mu)}
        linear_W = sp.expand(W.subs(linear_substitution, simultaneous=True))
        self.zero(linear_W.coeff(n, 2) - b[3] / (12 * d[0]))
        self.zero(sp.expand((W - W0).subs(linear_substitution, simultaneous=True)).coeff(n, 2))
        self.zero(linear_W.coeff(U, 4) + b[1] * d[0] + b[0] * d[1] / 4)
        self.zero(sp.diff(linear_W.coeff(U, 3), n))
        residual4 = (
            dt(linear_W.coeff(U, 4))
            - 3 * d[0] * sp.diff(linear_W.coeff(U, 2), n)
            - 2 * h[0] * sp.diff(linear_W.coeff(U, 3), n)
        )
        self.zero(residual4 + (10 * d[0] * b[2] + 5 * d[1] * b[1] + d[2] * b[0]) / 4)
        self.zero(residual4.subs({d[0]: 4 * t, d[1]: 4, d[2]: 0}, simultaneous=True)
                  + 5 * (2 * t * b[2] + b[1]))

    def test_euler_exponents_and_valuation_arithmetic_only(self):
        t = sp.symbols("t", nonzero=True)
        a = sp.symbols("a", nonzero=True)

        def da(expression):
            return sp.diff(expression, t) - a * sp.diff(expression, a) / (2 * t)

        a3 = da(da(da(a)))
        self.zero(t**3 * a3 + sp.Rational(15, 8) * a)
        gamma_a = a3 / (72 * t)
        self.zero(t**4 * gamma_a + sp.Rational(5, 192) * a)
        self.zero(da(gamma_a) + 9 * gamma_a / (2 * t))
        self.zero(da(a**2 * t))
        self.zero(gamma_a**2 * t**9 - sp.Rational(25, 36864) * a**2 * t)

        j = sp.symbols("j", nonzero=True)

        def dj(expression):
            return sp.diff(expression, t) - j * sp.diff(expression, j) / (2 * t)

        b3 = dj(dj(j))
        self.zero(t**2 * b3 - sp.Rational(3, 4) * j)
        gamma_j = b3 / (48 * t)
        self.zero(t**3 * gamma_j - j / 64)
        self.zero(dj(gamma_j) + 7 * gamma_j / (2 * t))
        self.zero(dj(j**2 * t))
        self.zero(gamma_j**2 * t**7 - j**2 * t / 4096)
        for exponent in (9, 7):
            forced_order = sp.Rational(-2, exponent)
            self.assertFalse(forced_order.is_integer)
            self.assertEqual(forced_order.q, exponent)
            self.zero(2 + exponent * forced_order)
        # This checks the arithmetic once a uniformizer gamma is justified.
        # It does not establish K=C(gamma), the pole-pencil inequality, or a DVR.

        v = sp.symbols("v", nonzero=True)
        formal_t, formal_a, formal_b = v**2, 1 / v, 2 * v
        formal_dt = lambda expression: sp.diff(expression, v) / (2 * v)
        self.zero(2 * formal_t * formal_dt(formal_a) + formal_a)
        self.zero(2 * formal_t * formal_dt(formal_dt(formal_b)) + formal_dt(formal_b))
        ga = gamma_a.subs({t: formal_t, a: formal_a}, simultaneous=True)
        gj = gamma_j.subs({t: formal_t, j: formal_dt(formal_b)}, simultaneous=True)
        self.zero(v**9 * ga + sp.Rational(5, 192))
        self.zero(v**7 * gj - sp.Rational(1, 64))
        # At v=infinity the formal orders are ord(t)=-2 and ord(gamma)=9
        # or 7, not 1. Hence these formal Euler examples have no
        # arithmetic contradiction; actual field return is indispensable.
        for order in (9, 7):
            self.assertEqual(2 * order + order * (-2), 0)


if __name__ == "__main__":
    unittest.main()
