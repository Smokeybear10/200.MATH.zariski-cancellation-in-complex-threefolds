"""Finite rational-base transfer controls for the cubic exclusion.

The two polynomial base maps include a generically degree-two map.
These identities do not prove constant fields, the all-degree obstruction,
kernel intersections, or existence/nonexistence of a global actual frame.
"""

import unittest

import sympy as sp


class CubicPullbackTransferChecks(unittest.TestCase):
    def zero(self, value):
        entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(sp.cancel(entry), 0)

    def test_birational_and_degree_two_rational_base_transfer(self):
        s, t, u, rho, y1, y2, a, c = sp.symbols("s t u rho y1 y2 a c")
        f = a*s**3+c*s
        for p in (s*t-1, t**2+s*t):
            with self.subTest(base_map=p):
                pt, ps = sp.diff(p, t), sp.diff(p, s)

                def Dp(value):
                    return sp.diff(value, t)/pt

                def Ds(value):
                    return sp.diff(value, s)-ps*sp.diff(value, t)/pt

                self.zero(Dp(s))
                self.zero(Dp(p)-1)
                self.zero(Ds(s)-1)
                self.zero(Ds(p))
                for coordinate in (s, t):
                    self.zero(Ds(Dp(coordinate))-Dp(Ds(coordinate)))

                b = sp.Matrix([s, p, f])
                old_frame = b.row_join(b.diff(s)).row_join(b.diff(t))
                new_bs = b.applyfunc(Ds)
                new_bp = b.applyfunc(Dp)
                new_frame = b.row_join(new_bs).row_join(new_bp)
                self.zero(new_bs-sp.Matrix([1, 0, sp.diff(f, s)]))
                self.zero(new_bp-sp.Matrix([0, 1, 0]))
                self.zero(old_frame.det()-pt*new_frame.det())

                new_y2 = ps*y1+pt*y2
                old_good = b*(u+rho)+b.diff(s)*y1+b.diff(t)*y2
                new_good = b*(u+rho)+new_bs*y1+new_bp*new_y2
                self.zero(old_good-new_good)
                linear_coordinate = old_good[2]-c*old_good[0]
                self.zero(linear_coordinate-3*a*s**2*old_good[0]
                          +2*a*s**3*u+2*a*s**3*rho)

        # If s^3 rho=T(s)+c0 s^3 p, the residue is a complex scalar.
        T0, T1, T2, T3, c0, x1 = sp.symbols("T0 T1 T2 T3 c0 x1")
        T = T0+T1*s+T2*s**2+T3*s**3
        p = t**2+s*t
        X = 3*a*s**2*x1-2*a*s**3*u-2*a*(T+c0*s**3*p)
        self.zero(X.subs(s, 0)+2*a*T0)
        self.assertEqual(sp.rem(X+2*a*T0, s, s), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
