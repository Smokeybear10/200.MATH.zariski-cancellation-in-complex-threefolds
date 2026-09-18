"""Exact finite controls for the polynomial-curve exclusion119.

These checks do not establish the all-degree formal-series argument,
the invariant-kernel intersection, or an actual global coordinate frame.
No solver or other checker internals are imported.
"""

import unittest

import sympy as sp


class CubicPolynomialCurveChecks(unittest.TestCase):
    def zero(self, expression):
        entries = expression if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.simplify(entry), 0)

    def test_indicial_and_infinitesimal_identities(self):
        x = sp.Symbol("x", positive=True)
        r = sp.Symbol("r", real=True)
        h_leading = 3*(r+1)/(4*x)
        g_leading = -r/x**2
        indicial = sp.diff(h_leading, x)+h_leading**2+x*g_leading*h_leading-g_leading
        self.zero(indicial+(3*r-1)*(r-3)/(16*x**2))

        # Quotient differentiation at F=x^3 in direction x^r.
        base, perturbation = x**3, x**r
        gamma0 = base-x*sp.diff(base, x)
        gamma1 = perturbation-x*sp.diff(perturbation, x)
        g0 = sp.diff(base, x, 2)/gamma0
        dg = sp.simplify((sp.diff(perturbation, x, 2)*gamma0
                          -sp.diff(base, x, 2)*gamma1)/gamma0**2)
        tau0 = -sp.diff(g0, x)-2*x*g0**2
        dtau = sp.simplify(-sp.diff(dg, x)-4*x*g0*dg)
        h0 = -(3*x*g0+sp.diff(tau0, x)/tau0)/4
        dh = sp.simplify(-(3*x*dg+sp.diff(dtau/tau0, x))/4)
        dresidual = sp.simplify(sp.diff(dh, x)+2*h0*dh+x*(dg*h0+g0*dh)-dg)
        A = -(r-1)*(r-3)/2
        B = (r-1)*(r-3)*(r**2-20*r+123)/192
        multiplier = sp.prod(r-j for j in (1, 3, 5, 7, 9))/192
        self.zero(dg-A*x**(r-5))
        self.zero(dtau-A*(17-r)*x**(r-6))
        self.zero(dh-B*x**(r-4))
        self.zero(dresidual-multiplier*x**(r-5))
        self.zero((r-1)*B+2*A-multiplier)

    def test_ramified_frame_and_root_divisor_controls(self):
        s, t, u, rho, v, y2, x1 = sp.symbols("s t u rho v y2 x1")
        for a, H in ((s**2-1, t**2+s*t), (s**3-1, s*t-1)):
            with self.subTest(a=a, H=H):
                def Dw(value):
                    return sp.cancel(sp.diff(value, t)/sp.diff(H, t))

                def Dx(value):
                    return sp.cancel((sp.diff(value, s)-sp.diff(H, s)*Dw(value))
                                     /sp.diff(a, s))

                self.zero(Dx(a)-1)
                self.zero(Dx(H))
                self.zero(Dw(H)-1)
                self.zero(Dw(a))
                for probe in (s, t, s/(s+t), H**2+a*t):
                    self.zero(Dx(Dw(probe))-Dw(Dx(probe)))

                f = 2*a**3+3*a
                b = sp.Matrix([a, H, f])
                bx, bw = b.applyfunc(Dx), b.applyfunc(Dw)
                frame = b.row_join(bx).row_join(bw)
                self.zero(frame.det()+4*a**3)
                self.zero(frame.inv()*bx.applyfunc(Dx)
                          -sp.Matrix([-3/a**2, 3/a, 3*H/a**2]))
                self.zero(bx.applyfunc(Dw))
                self.zero(bw.applyfunc(Dw))
                g = -3/a**2
                self.zero(-Dx(g)-2*a*g**2+24/a**3)

                original = b*(u+rho)+bx*v+bw*y2
                X = original[2]-3*original[0]
                self.zero(X-(6*a**2*original[0]-4*a**3*u-4*a**3*rho))
                self.zero(sp.diff(X, u)-2*a**3)

                # Finite polynomial T and a root s0=1; no kernel theorem here.
                T = s**3+2*s+5
                radial = T/a**3+7*H
                reconstructed = sp.cancel(6*a**2*x1-4*a**3*u-4*a**3*radial)
                h0 = -4*T.subs(s, 1)
                self.zero(reconstructed.subs(s, 1)-h0)
                self.assertEqual(sp.rem(reconstructed-h0, s-1, s), 0)

    def test_fractional_exponent_and_nonlinear_remainder_controls(self):
        s = sp.Symbol("s", positive=True)

        def residual(a, f):
            def delta(value):
                return sp.cancel(sp.diff(value, s)/sp.diff(a, s))

            gamma = f-a*delta(f)
            g = sp.cancel(delta(delta(f))/gamma)
            tau = sp.cancel(-delta(g)-2*a*g**2)
            h = sp.cancel(-(3*a*g+delta(tau)/tau)/4)
            return sp.cancel(delta(h)+h**2+a*g*h-g)

        # Monomial controls include the second indicial root r=1/3.
        # Degree normalization in the proof is essential to exclude that root.
        for n, m in ((2, 3), (2, 5), (2, 6), (3, 1)):
            r = sp.Rational(m, n)
            self.zero(residual(s**n, s**m)+(3*r-1)*(r-3)/(16*s**(2*n)))

        # Exact finite nonlinear expansions around a^3 with a=s^2.
        for d in (0, 1, 3, 4, 5):
            r = sp.Rational(d, 2)
            expected = sp.prod(r-j for j in (1, 3, 5, 7, 9))/192
            value = residual(s**2, s**6+s**d)
            self.zero(sp.limit(value/s**(d-10), s, sp.oo)-expected)
            self.assertNotEqual(value, 0)
        self.zero(residual(s**2, 7*s**6+3*s**2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
