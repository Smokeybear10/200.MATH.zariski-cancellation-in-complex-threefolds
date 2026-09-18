"""Finite raw identities for293; no field-theoretic certification.

The exact cubic extension contradiction is a written argument, not a
consequence of these tests. No project proof or checker is imported.
"""

import unittest

import sympy as s


class ConstantFirstLineControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_actual_translation_and_parameter_sign(self):
        t, n, P, Xs, alpha, d, k, k1 = s.symbols("t n P Xs alpha d k k1")
        y = alpha * P + d
        z = 2 * t * y + P**2 + k1 * P + n
        X = Xs - alpha
        Y = y + P * X + t * X**2
        Z = z + (2 * t * P + k) * X + t**2 * X**2
        ys, ps, ks = d + alpha**2 * t, P - 2 * alpha * t, k + 2 * alpha * t**2
        ns = n - alpha * k + 3 * alpha**2 * t**2 + 2 * alpha * t * k1
        zs = 2 * t * ys + ps**2 + (k1 + 4 * alpha * t) * ps + ns
        self.assert_zero(Y - (ys + ps * Xs + t * Xs**2))
        self.assert_zero(Z - (zs + (2 * t * ps + ks) * Xs + t**2 * Xs**2))

    def test_complete_constant_first_gradient_ledger(self):
        t, n, U, P = s.symbols("t n U P")
        beta, b0 = s.symbols("beta b0")
        k, c, p, q, d, v1, v0 = [s.Function(name)(t) for name in ("k", "c", "p", "q", "d", "v1", "v0")]
        b = beta * t + b0
        k1, k2, k3, k4 = [s.diff(k, t, j) for j in range(1, 5)]
        aa = (2 * P + k1) * U + k2 * P**2 / 2
        cc = U**2 + k2 * P * U + k3 * P**3 / 6
        raw = (v1 * n + v0 - (beta * P + p) * aa - b * cc
               + (beta * n + s.diff(c, t)) * U + s.diff(c, t, 2) * P**2 / 2
               + (s.diff(p, t) * n + s.diff(q, t)) * P)
        qu = s.expand(((2 * P + k1) * s.diff(raw, n) - s.diff(raw, P)).subs(U, d))
        qp = s.expand(((2 * U + k2 * P) * s.diff(raw, n) - s.diff(raw, t)).subs(U, d))
        f2 = 4 * s.diff(p, t) + b * k3 + 3 * beta * k2
        f1 = 6 * beta * d + p * k2 + s.diff(p, t) * k1 - s.diff(c, t, 2) + 2 * v1
        self.assert_zero(2 * qu.coeff(P, 2) - f2)
        self.assert_zero(qu.coeff(P, 1) - f1)
        self.assert_zero(6 * qp.coeff(P, 3) - (b * k4 + 4 * beta * k3))
        self.assert_zero(2 * qp.coeff(P, 2) - (p * k3 + 3 * k2 * s.diff(p, t) - s.diff(c, t, 3)))
        self.assert_zero(qp.coeff(P, 1) - (d * f2 - s.diff(p, t, 2) * n + k2 * v1 - s.diff(q, t, 2)))
        self.assert_zero(qp.coeff(P, 0) - (d * f1 - 3 * beta * d**2 - s.diff(v1, t) * n - s.diff(v0, t)))
        self.assert_zero(qu.coeff(P, 0) - (k1 * v1 + (b * k2 + 2 * p + 2 * beta * k1) * d
                                           - s.diff(p, t) * n - s.diff(q, t)))
        differentiated = s.diff(f1, t).subs({s.diff(p, t, 2): 0, s.diff(v1, t): 0,
                                             s.diff(c, t, 3): p * k3 + 3 * k2 * s.diff(p, t)},
                                            simultaneous=True)
        self.assert_zero(differentiated - (6 * beta * s.diff(d, t) - s.diff(p, t) * k2))

    def test_exact_cubic_after_first_potential_elimination(self):
        t, z, P, b, beta, d, k1, k2, p, pp, q1, c1, c2, v1, v0 = s.symbols(
            "t z P b beta d k1 k2 p pp q1 c1 c2 v1 v0")
        k3 = (-4 * pp - 3 * beta * k2) / b
        n = z - 2 * t * d - P**2 - k1 * P
        aa = (2 * P + k1) * d + k2 * P**2 / 2
        cc = d**2 + k2 * P * d + k3 * P**3 / 6
        w = (v1 * n + v0 - (beta * P + p) * aa - b * cc
             + (beta * n + c1) * d + c2 * P**2 / 2 + (pp * n + q1) * P)
        polynomial = s.Poly(s.expand(w), P)
        self.assertEqual(polynomial.degree(), 3)
        self.assert_zero(polynomial.coeff_monomial(P**3) + pp / 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
