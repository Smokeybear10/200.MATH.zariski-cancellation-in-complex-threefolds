"""Exact determinant coefficients, not an action or recognition checker."""

import unittest

import sympy as S


class ConstantAccelerationVolumeChecks(unittest.TestCase):
    def test_formal_volume_coefficients_and_critical_specialization(self):
        u, q, r1, r2, rv = S.symbols("u q r1 r2 rv")
        b = S.Matrix(S.symbols("b0:3"))
        p = S.Matrix(S.symbols("p0:3"))
        w = S.Matrix(S.symbols("w0:3"))
        a1 = S.Matrix(S.symbols("a10:13"))
        a2 = S.Matrix(S.symbols("a20:23"))
        av = S.Matrix(S.symbols("v0:3"))
        top = S.Matrix.hstack(b, u * p + a1, u * w + a2, av)
        full = top.col_join(S.Matrix([[q * u, r1, r2, rv]]))
        determinant = S.Poly(S.expand(full.det(method="domain-ge")), u)
        omega = S.Matrix.hstack(b, p, w).det()
        normal = p.cross(w)
        self.assertEqual(determinant.degree(), 3)
        self.assertEqual(S.expand(determinant.nth(3) + q * normal.dot(av)), 0)
        self.assertEqual(S.expand(normal.dot(b) - omega), 0)
        critical = S.expand(determinant.as_expr().subs(dict.fromkeys(av, 0)))
        expected = rv * S.Matrix.hstack(b, u * p + a1, u * w + a2).det()
        self.assertEqual(S.expand(critical - expected), 0)
        self.assertEqual(S.expand(S.Poly(critical, u).nth(2) - rv * omega), 0)

        # Column order (u,s1,s2,v) has opposite orientation to
        # ds1 wedge ds2 wedge dv wedge du in the global volume proof.
        orientation = S.Matrix([[0, 1, 0, 0], [0, 0, 1, 0],
                                [0, 0, 0, 1], [1, 0, 0, 0]]).det()
        self.assertEqual(orientation, -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
