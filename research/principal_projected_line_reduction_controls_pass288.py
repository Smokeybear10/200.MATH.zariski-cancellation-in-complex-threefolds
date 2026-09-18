"""Independent finite coefficient controls for288.

These tests reconstruct formal gradients from the raw potential. They do
not certify exact-field integration, actual polynomial entry, or any
recognition theorem. No other project source or checker is imported.
"""

import unittest

import sympy as s


class ProjectedLineReductionControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_raw_five_coefficient_ledger(self):
        t, n, U, P, a, d = s.symbols("t n U P a d")
        b, c, k = [s.Function(name)(t) for name in ("b", "c", "k")]
        T, omega = s.Function("T")(t, n), s.Function("omega")(t, n)
        k1, k2, k3, k4 = [s.diff(k, t, j) for j in range(1, 5)]
        bp, bpp = s.diff(b, t), s.diff(b, t, 2)
        u, tn, ttn = s.diff(T, n, 2), s.diff(T, n), s.diff(T, t, n)
        on = s.diff(omega, n)
        aa = (2 * P + k1) * U + k2 * P**2 / 2
        cc = U**2 + k2 * P * U + k3 * P**3 / 6
        raw = (omega - (bp * P + tn) * aa - b * cc
               + (bp * n + s.diff(c, t)) * U
               + (bpp * n + s.diff(c, t, 2)) * P**2 / 2 + s.diff(T, t) * P)
        qu = s.expand(((2 * P + k1) * s.diff(raw, n) - s.diff(raw, P)).subs(U, a * P + d))
        qp = s.expand(((2 * U + k2 * P) * s.diff(raw, n) - s.diff(raw, t)).subs(U, a * P + d))
        f3 = bpp - (4 * a + k2) * u
        j3 = (-24 * a**2 * u - 18 * a * u * k2 - 3 * u * k2**2
              + 18 * a * bpp + b * k4 + 4 * bp * k3 + 6 * bpp * k2) / 6
        f2 = (-8 * a * u * k1 + 12 * a * bp - 8 * d * u - u * k1 * k2
              + 4 * ttn + b * k3 + 3 * bp * k2 + bpp * k1) / 2
        f1 = (2 * a * tn - a * u * k1**2 + a * b * k2 + 2 * a * bp * k1
              - 4 * d * u * k1 + 6 * d * bp + tn * k2 + ttn * k1
              - bpp * n - s.diff(c, t, 2) + 2 * on)
        j1 = (-4 * a * d * u * k1 + 6 * a * d * bp + a * tn * k2 + a * ttn * k1
              - a * bpp * n - a * s.diff(c, t, 2) + 2 * a * on
              - 4 * d**2 * u - d * u * k1 * k2 + 4 * d * ttn
              + d * b * k3 + 3 * d * bp * k2 + d * bpp * k1
              - s.diff(T, t, 2) + k2 * on)
        for actual, expected in ((qu.coeff(P, 3), f3), (qp.coeff(P, 3), j3),
                                 (qu.coeff(P, 2), f2), (qu.coeff(P, 1), f1),
                                 (qp.coeff(P, 1), j1)):
            self.assert_zero(actual - expected)

    def test_scalar_elimination_coefficients(self):
        t, n, U, P = s.symbols("t n U P")
        b, c, k, a, r, u, p, q, d0 = [s.Function(name)(t)
                                      for name in ("b", "c", "k", "a", "r", "u", "p", "q", "d0")]
        omega = s.Function("omega")(t, n)
        T, d = u * n**2 / 2 + p * n + q, r * n + d0
        k1, k2, k3, k4 = [s.diff(k, t, j) for j in range(1, 5)]
        ell = 4 * a + k2
        aa = (2 * P + k1) * U + k2 * P**2 / 2
        cc = U**2 + k2 * P * U + k3 * P**3 / 6
        raw = (omega - (s.diff(b, t) * P + s.diff(T, n)) * aa - b * cc
               + (s.diff(b, t) * n + s.diff(c, t)) * U
               + (s.diff(b, t, 2) * n + s.diff(c, t, 2)) * P**2 / 2 + s.diff(T, t) * P)
        qu = s.expand(((2 * P + k1) * s.diff(raw, n) - s.diff(raw, P)).subs(U, a * P + d))
        qp = s.expand(((2 * U + k2 * P) * s.diff(raw, n) - s.diff(raw, t)).subs(U, a * P + d))
        on = s.diff(omega, n)
        on_value = -qu.coeff(P, 1).subs(on, 0) / 2
        eliminated = s.expand(qp.coeff(P, 1).subs(on, on_value))
        p1 = u * (a * k1 + 2 * d0) - (b * k3 + 3 * ell * s.diff(b, t)) / 4
        substitutions = {
            s.diff(p, t, 2): s.diff(p1, t),
            s.diff(p, t): p1,
            s.diff(u, t, 2): 2 * s.diff(r, t) * u + 4 * r**2 * u,
        }
        eliminated = eliminated.subs(substitutions, simultaneous=True).doit()
        eliminated = eliminated.subs({s.diff(u, t): 2 * r * u,
                                      s.diff(a, t): r * ell,
                                      s.diff(b, t, 2): u * ell,
                                      k4: (-4 * s.diff(b, t) * k3 - 3 * u * ell**2) / b},
                                     simultaneous=True)
        eliminated = s.expand(eliminated)
        self.assert_zero(eliminated.coeff(n, 2) - u * (2 * r**2 - s.diff(r, t)))
        self.assert_zero(eliminated.coeff(n, 1)
                         - 2 * u * (2 * r * d0 + a * k1 * r - s.diff(d0, t) - a**2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
