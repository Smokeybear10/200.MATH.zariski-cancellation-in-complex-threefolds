"""Exact identity controls for the fixed-bad-pair repair obstruction.

These tests do not construct a full adjoint frame.  The second method
uses actual polynomial functions and their true local Jacobian inverse.
"""

import unittest

import sympy as S


class FaithfulFrameRankChecks(unittest.TestCase):
    def test_hessian_and_exact_pole_module(self):
        a, f, g, v, X, Y, T = S.symbols("a f g v X Y T")
        C = S.Function("C")
        h = 2 * f**2 * C(g / f)
        vec = S.Matrix([X, Y])
        quadratic = (vec.T * S.hessian(h, [f, g]) * vec)[0] / 4
        transformed = quadratic.subs(
            {g: f * v, Y: T + v * X}, simultaneous=True
        ).doit()
        expected = (
            C(v) * X**2
            + S.diff(C(v), v) * X * T
            + S.diff(C(v), v, 2) * T**2 / 2
        )
        self.assertEqual(S.simplify(transformed - expected), 0)

        C2 = S.Function("C2")
        acceleration = 2 * a**2 * C2(a, v)
        self.assertEqual(
            S.expand(a * S.diff(acceleration, a) - 2 * acceleration),
            2 * a**3 * S.diff(C2(a, v), a),
        )

        m1, m2, k, n = S.symbols("m1 m2 k n")
        z = (T**2 - v) / a
        q = X * T / a - v * (T**2 - v) / a**2
        self.assertEqual(
            S.expand(m1 * z + m2 * q)
            - S.expand(
                (a * m1 - v * m2) * (T**2 - v) / a**2
                + m2 * X * T / a
            ),
            0,
        )
        self.assertEqual(
            S.simplify(
                (m1 * z + m2 * q).subs({m1: a * k + v * n, m2: a * n})
                - (k * (T**2 - v) + n * X * T)
            ),
            0,
        )
        k1, k2, n1, n2 = S.symbols("k1 k2 n1 n2")
        M = S.Matrix([[a * k1 + v * n1, a * n1],
                      [a * k2 + v * n2, a * n2]])
        self.assertEqual(S.expand(M.det() - a**2 * (k1 * n2 - n1 * k2)), 0)

    def test_actual_local_jacobian_and_nonzero_good_adjoint(self):
        a, t, z, s, c = S.symbols("a t z s c")
        v = t**2 - a * z
        X = a * s + t * z
        Y = v * X + t
        q = t * s + z**2
        Q1 = z + c * a + X**2
        Q2 = q + Y**2

        self.assertEqual(S.expand(S.diff(Q1, s, 2) - 2 * a**2), 0)
        self.assertEqual(S.expand(S.diff(Q2, s, 2) - 2 * a**2 * v**2), 0)
        self.assertEqual(S.diff(Q1, s, 3), 0)
        self.assertEqual(S.diff(Q2, s, 3), 0)
        base_v = S.symbols("base_v")
        h = S.Matrix([2 * a**2, 2 * a**2 * base_v**2])
        self.assertEqual(h.jacobian([a, base_v]).det(), 16 * a**3 * base_v)

        actual_jacobian = S.Matrix([Q1, Q2, X, Y]).jacobian([a, t, z, s])
        line_jacobian = actual_jacobian.subs({a: 0, t: 1, z: 0})
        expected = S.Matrix([[c, 0, 1, 0],
                             [2 * s, s + 2, 2, 1],
                             [s, 0, 1, 0],
                             [s, 1, 1, 0]])
        self.assertEqual(line_jacobian, expected)
        self.assertEqual(S.factor(line_jacobian.det()), s - c)

        true_dual = line_jacobian.inv()[:, 0]
        claimed_dual = S.Matrix([1 / (c - s), 0, -s / (c - s), 0])
        self.assertEqual((true_dual - claimed_dual).applyfunc(S.simplify), S.zeros(4, 1))
        self.assertEqual(
            (line_jacobian * true_dual).applyfunc(S.simplify),
            S.Matrix([1, 0, 0, 0]),
        )
        second_adjoint = true_dual.diff(s, 2)
        claimed_second = 2 * S.Matrix([1, 0, -c, 0]) / (c - s)**3
        self.assertEqual(
            (second_adjoint - claimed_second).applyfunc(S.simplify), S.zeros(4, 1)
        )
        self.assertEqual(line_jacobian.subs({c: 1, s: 0}).det(), -1)
        self.assertEqual(
            second_adjoint.subs({c: 1, s: 0}), S.Matrix([2, 0, -2, 0])
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
