"""Finite exact raw-map controls for292.

No project proof or solver is imported. Passing these identities does
not prove the curve-pencil lemma, actual field return, monic division
descent, or cancellation.
"""

import unittest

import sympy as s


class MovingLinePencilControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_raw_constant_gradient_compatibility(self):
        t, n, U, P = s.symbols("t n U P")
        beta, b0 = s.symbols("beta b0")
        a, d, r, k, c, p, q, v1, v0 = [s.Function(name)(t)
                                      for name in ("a", "d", "r", "k", "c", "p", "q", "v1", "v0")]
        b = beta * t + b0
        k1, k2, k3 = [s.diff(k, t, j) for j in range(1, 4)]
        aa = (2 * P + k1) * U + k2 * P**2 / 2
        cc = U**2 + k2 * P * U + k3 * P**3 / 6
        omega = -3 * beta * r * n**2 / 2 + v1 * n + v0
        raw = (omega - (beta * P + p) * aa - b * cc
               + (beta * n + s.diff(c, t)) * U + s.diff(c, t, 2) * P**2 / 2
               + (s.diff(p, t) * n + s.diff(q, t)) * P)
        qu = (2 * P + k1) * s.diff(raw, n) - s.diff(raw, P)
        qp = (2 * U + k2 * P) * s.diff(raw, n) - s.diff(raw, t)
        constant = s.expand((qp + a * qu).subs(U, a * P + r * n + d)).coeff(P, 0)
        v1_value = (-3 * beta * d - beta * a * k1 - k1 * s.diff(p, t) / 2
                    - a * b * k2 / 2 - a * p - p * k2 / 2 + s.diff(c, t, 2) / 2)
        # Protect v1': it is the independent compatibility unknown.
        v1_prime_symbol = s.Dummy("v1_prime")
        constant = constant.xreplace({s.diff(v1, t): v1_prime_symbol})
        constant = constant.xreplace({v1: v1_value})
        constant = s.expand(constant.xreplace({v1_prime_symbol: s.diff(v1, t)}))
        self.assert_zero(constant.coeff(n, 2) - 3 * beta * (s.diff(r, t) / 2 - r**2))
        self.assert_zero(constant.coeff(n, 1)
                         - (-6 * beta * d * r - 3 * beta * k1 * a * r - a * s.diff(p, t) - s.diff(v1, t)))

    def test_complex_coefficient_gates(self):
        t = s.symbols("t")
        beta, b0 = s.symbols("beta b0")
        a, d, k, c, p, v1 = [s.Function(name)(t) for name in ("a", "d", "k", "c", "p", "v1")]
        b = beta * t + b0
        k1, k2, k3 = [s.diff(k, t, j) for j in range(1, 4)]
        pp = s.diff(p, t)
        ap = -(4 * a + k2) / (2 * t)
        pp_value = -(b * k3 + 3 * beta * (4 * a + k2)) / 4
        v1p = 3 * beta * d / t + 3 * beta * k1 * a / (2 * t) - a * pp
        c2 = 2 * v1 + 6 * beta * d + 2 * beta * a * k1 + k1 * pp + a * b * k2 + 2 * a * p + p * k2
        D = beta * k1 - 2 * p - b * k2 - 2 * t * pp
        E1 = -b * k1 + 2 * beta * k - 2 * t * p
        L0 = s.diff(c, t) - p * k1 - 2 * t * v1
        C1 = 2 * t * a + k1
        residuals = [s.diff(D, t), s.diff(E1, t) - D, s.diff(L0, t) + a * D,
                     s.diff(C1, t) + 2 * a, s.diff(k - t * C1, t)]
        for expression in residuals:
            expression = expression.subs({s.diff(p, t, 2): -3 * beta * ap,
                                           s.diff(v1, t): v1p,
                                           s.diff(c, t, 2): c2,
                                           s.diff(a, t): ap}, simultaneous=True)
            self.assert_zero(expression.subs(pp, pp_value))

    def test_full_actual_pencil_and_quadratic_relation(self):
        t, Y, P, X = s.symbols("t Y P X")
        beta, b0, a, d, k, k1, k2, k3, p, pp, q, qp, c, cp, cpp, v1, v0 = s.symbols(
            "beta b0 a d k k1 k2 k3 p pp q qp c cp cpp v1 v0")
        b = beta * t + b0
        y = Y - P * X - t * X**2
        n = -2 * t * y + 2 * t * (a * P + d)
        aa = (2 * P + k1) * y + k2 * P**2 / 2
        cc = y**2 + k2 * P * y + k3 * P**3 / 6
        omega = 3 * beta * n**2 / (4 * t) + v1 * n + v0
        z = 2 * t * y + P**2 + k1 * P + n
        Z = z + (2 * t * P + k) * X + t**2 * X**2
        theta = p * n + q + (beta * n + cp) * P - b * aa
        w = omega - (beta * P + p) * aa - b * cc + (beta * n + cp) * y + cpp * P**2 / 2 + (pp * n + qp) * P
        W = w + theta * X + (b * n + c) * X**2
        D = beta * k1 - 2 * p - b * k2 - 2 * t * pp
        E1 = -b * k1 + 2 * beta * k - 2 * t * p
        E0 = E1 - D * t
        L0 = cp - p * k1 - 2 * t * v1
        corrected = W + b0 * Y**2 + 2 * beta * Y * Z - E0 * X * Y
        lam = D * (P + t * X) + L0
        self.assert_zero(s.diff(corrected, Y) - lam)
        self.assert_zero(s.diff(Z, Y))
        C1, C0 = 2 * t * a + k1, 2 * t * d
        wc = k - t * C1
        uc = (D * C1 - 2 * L0) / D**2
        vc = C0 + L0**2 / D**2 - C1 * L0 / D
        self.assert_zero(Z - (wc * X + lam**2 / D**2 + uc * lam + vc))


if __name__ == "__main__":
    unittest.main(verbosity=2)
