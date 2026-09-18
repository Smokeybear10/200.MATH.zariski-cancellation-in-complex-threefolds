"""One binary-normal parameter control, not an actual four-coordinate action."""

import unittest

import sympy as S


class BinaryNormalUnitChecks(unittest.TestCase):
    def zero(self, expression):
        entries = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(S.expand(entry), 0)

    def test_cubic_ramification_and_explicit_unit_normal(self):
        xi, eta, s, t = S.symbols("xi eta s t")
        H = S.Matrix([xi**3, xi**2 * eta, eta**3])
        N0 = S.Matrix([2 * eta**3, -3 * xi * eta**2, xi**3])
        raw = H.diff(xi).cross(H.diff(eta))
        self.zero(raw - 3 * xi * N0)
        self.assertEqual(S.Poly(S.gcd_list(list(raw)), xi, eta, domain=S.QQ).monic().as_expr(), xi)
        self.assertEqual(S.Poly(S.gcd_list(list(N0)), xi, eta, domain=S.QQ).monic().as_expr(), 1)
        for column in (H, H.diff(xi), H.diff(eta)):
            self.zero(N0.dot(column))

        p, r = s, s * t - 1
        replacement = {xi: p, eta: r}
        b = H.subs(replacement, simultaneous=True)
        N = N0.subs(replacement, simultaneous=True)
        self.zero(t * p - r - 1)
        self.zero(S.Matrix([p, r]).jacobian([s, t]).det() - s)
        U = t**5 * p**2 - 5 * t**4 * p * r + 10 * t**3 * r**2
        V = -10 * t**2 * p**2 + 5 * t * p * r - r**2
        self.zero(U * p**3 + V * r**3 - (t * p - r)**5)
        self.zero(S.Matrix([U, 0, V]).dot(b) - 1)
        self.zero(S.Matrix([V / 2, 0, U]).dot(N) - 1)

        parameter_cross = b.diff(s).cross(b.diff(t))
        self.zero(parameter_cross - 3 * s**2 * N)
        self.assertEqual(S.Poly(S.gcd_list(list(parameter_cross)), s, t, domain=S.QQ).monic().as_expr(), s**2)
        self.zero(S.Matrix.hstack(b, b.diff(s), b.diff(t)).det())
        self.zero(b[:2, :].jacobian([s, t]).det() - 3 * s**5)
        self.assertEqual(b.jacobian([s, t]).rank(), 2)
        for column in (b, b.diff(s), b.diff(t)):
            self.zero(N.dot(column))
        self.zero(parameter_cross.subs(s, 0))
        self.zero(N.subs(s, 0) - S.Matrix([-2, 0, 0]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
