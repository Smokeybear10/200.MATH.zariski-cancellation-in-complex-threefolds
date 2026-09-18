"""Polynomial non-null speed controls, not original four-space frames."""

import unittest

import sympy as sp


class ScalarSpeedBoundaryChecks(unittest.TestCase):
    def test_both_nonnull_scalar_types_have_unimodular_polynomial_speeds(self):
        s, t, h = sp.symbols("s t h")
        T, W = s**2-1, s*t-1

        def zero(value):
            entries = value if isinstance(value, sp.MatrixBase) else [value]
            for entry in entries:
                self.assertEqual(sp.cancel(entry), 0)

        zero(T*W-s*(s**2*t-s-t)-1)
        controls = [
            (sp.Matrix([s, T*W, T**2*W**3]), h**3, 1, -3*h**4/4),
            (sp.Matrix([s, T**2*W**3, T*W]), 1/h, -1, -3/(4*h**4)),
        ]
        for b, D, sign, determinant in controls:
            with self.subTest(D=D):
                ratio = sp.cancel(b[1]/b[2])
                d1, d2 = sp.diff(D, h), sp.diff(D, h, 2)
                Q = sp.Matrix([
                    [-1, 0, 0],
                    [0, d2/2, (d1-h*d2)/2],
                    [0, (d1-h*d2)/2, D-h*d1+h**2*d2/2],
                ])
                n = sp.Matrix([0, 1, -h])
                zero(Q.diff(h)-sp.diff(D, h, 3)*n*n.T/2)
                zero(Q.det()-determinant)
                metric = Q.subs(h, ratio)
                zero(b[0]**2-D.subs(h, ratio)*b[2]**2-1)
                zero((b.T*metric*b)[0]+1)
                zero((n.subs(h, ratio).T*b)[0])
                zero(b.row_join(b.diff(s)).row_join(b.diff(t)).det()
                     -sign*2*s*T**2*W**3)
                for coordinate in (s, t):
                    zero((b.T*metric*b.diff(coordinate))[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
