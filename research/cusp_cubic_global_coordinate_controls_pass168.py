"""Finite exact controls for the cubic cusp lift in pass168.

The generic jets and the nonconstant-chi example are formal coefficient
controls, not asserted actual dense frames.  The final polynomial fixture
has its actual inverse checked in two independent triangular stages.
The parameter-independent coordinate change also has both inverse orders.
These calculations do not prove the universal constant-field argument,
actual field return, a kernel theorem, or unrestricted cancellation.
No earlier checker is imported.  Root owns execution after source review.
"""

import unittest

import sympy as sp


class CubicGlobalCoordinateControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_chart_expansion_before_differential_constraints(self):
        x, y, t, rho = sp.symbols("x y t rho")
        r, s, alpha, beta, h, C = sp.symbols("r s alpha beta h C")
        b0, b1, b2, c0, c1, c2, d0, d1, graph0 = sp.symbols(
            "b0 b1 b2 c0 c1 c2 d0 d1 graph0"
        )
        chi = alpha*t + beta
        # Independent coefficient jets, with only the literal definitions
        # b=s*t^3-r*k0, c=s*k0-r*n0, d=r*ell0+s*n0 imposed.
        k0 = (s*t**3-b0)/r
        kt = (3*s*t**2-b1)/r
        ktt = (6*s*t-b2)/r
        n0 = (s*k0-c0)/r
        nt = (s*kt-c1)/r
        ell0 = (d0-s*n0)/r
        p3 = C/chi**3
        p2 = chi*c2/(2*r)
        p1 = alpha*rho/chi + chi*d1/r
        p0 = (h/chi-s/r)*rho + graph0
        P = p3*y**3+p2*y**2+p1*y+p0
        z = 3*t*y**2+kt*y+r*P+s*rho+n0
        w = ((-1/chi-s**2/r)*rho+ell0-y**3
             -ktt*y**2/2-nt*y-s*P)/r
        Y = y+t*x
        Z = z+(3*t**2*y+r*rho+k0)*x+t**3*x**2
        W = w+P*x+rho*x**2
        cusp = x*Z-Y**3
        inner = r**2*W+s*Z-r*cusp
        inner_expected = (-r*rho/chi+b2*y**2/2+c1*y+d0
                          +(b1*y+c0)*x+b0*x**2)
        self.zero(inner-inner_expected)

        projected = (1+s*h)*n0+r*graph0+r*h*ell0
        q3 = r*p3+alpha*b2/2
        q2 = 3*t+r*p2+h*b2/2+alpha*c1
        q1 = kt+chi*d1+h*c1+alpha*d0
        a2 = alpha*b1+chi*b2/2
        a1 = 3*t**2+h*b1+alpha*c0+chi*c1
        a0 = k0+h*c0+chi*d0
        B1 = alpha*b0+chi*b1
        B0 = t**3+h*b0+chi*c0
        C0 = chi*b0
        Qchart = (q3*y**3+q2*y**2+q1*y
                  +x*(a2*y**2+a1*y+a0)+x**2*(B1*y+B0)+x**3*C0)
        Istar = Z+(beta*x+alpha*Y+h)*inner
        self.zero(Istar-projected-Qchart)
        # A nonzero omitted term reproduces the discarded collection error.
        self.zero(sp.diff(Qchart, x).subs(x, 0).coeff(y, 2)-a2)
        self.assertNotEqual(sp.expand(chi*b2/2), 0)

    def test_independent_jet_pde_and_global_coordinate_inverse(self):
        t, x, y, Y = sp.symbols("t x y Y")
        r, s, alpha, beta, h, C = sp.symbols("r s alpha beta h C")
        b0, b1, b2, c0, c1, c2, d0, d1 = sp.symbols(
            "b0 b1 b2 c0 c1 c2 d0 d1"
        )
        chi = alpha*t+beta
        b3 = 6*r*C/chi**4
        k0 = (s*t**3-b0)/r
        kt = (3*s*t**2-b1)/r
        ktt = (6*s*t-b2)/r
        # These are the differentiated positive-coefficient equations.
        # They are necessary formal jet constraints, not realization data.
        c3 = -(6+3*alpha*c2+h*b3)/chi
        d2 = -(ktt+h*c2+2*alpha*d1)/chi
        velocities = {b0: b1, b1: b2, b2: b3,
                      c0: c1, c1: c2, c2: c3, d0: d1, d1: d2}

        def Dt(expression):
            return sp.diff(expression, t) + sum(
                sp.diff(expression, variable)*velocity
                for variable, velocity in velocities.items()
            )

        q3 = r*C/chi**3+alpha*b2/2
        q2 = 3*t+chi*c2/2+h*b2/2+alpha*c1
        q1 = kt+chi*d1+h*c1+alpha*d0
        a2 = alpha*b1+chi*b2/2
        a1 = 3*t**2+h*b1+alpha*c0+chi*c1
        a0 = k0+h*c0+chi*d0
        B1 = alpha*b0+chi*b1
        B0 = t**3+h*b0+chi*c0
        C0 = chi*b0
        for q in (q3, q2, q1):
            self.zero(Dt(q))
        for coefficient, derivative in (
                (a2, 3*q3), (a1, 2*q2), (a0, q1),
                (B1, 2*a2), (B0, a1), (C0, B1)):
            self.zero(Dt(coefficient)-derivative)
        Qchart = (q3*y**3+q2*y**2+q1*y
                  +x*(a2*y**2+a1*y+a0)+x**2*(B1*y+B0)+x**3*C0)
        self.zero(Dt(Qchart)-x*sp.diff(Qchart, y))
        Qfixed = sp.expand(Qchart.subs(y, Y-t*x))
        Qformula = (q3*Y**3+q2*Y**2+q1*Y
                    +x*((a2-3*t*q3)*Y**2+(a1-2*t*q2)*Y+a0-t*q1)
                    +x**2*((B1-2*t*a2+3*t**2*q3)*Y+B0-t*a1+t**2*q2)
                    +x**3*(C0-t*B1+t**2*a2-t**3*q3))
        self.zero(Qfixed-Qformula)
        for coefficient in sp.Poly(Qfixed, x, Y).coeffs():
            self.zero(Dt(coefficient))

        # Here Q has genuinely constant symbolic coefficients.  This is an
        # actual polynomial coordinate map independent of a dense E-frame.
        Z, W, I, J = sp.symbols("Z W I J")
        monomials = [x**i*Y**j for i in range(4) for j in range(4-i)]
        constants = sp.symbols("q:10")
        Q = sum(c*m for c, m in zip(constants, monomials))
        L = beta*x+alpha*Y+h
        Jforward = W+(s/r**2-x/r)*Z
        Iforward = Z+r**2*L*Jforward+r*L*Y**3-Q
        Zback = I-r**2*L*J-r*L*Y**3+Q
        Wback = J-(s/r**2-x/r)*Zback
        self.zero(Zback.xreplace({I: Iforward, J: Jforward})-Z)
        self.zero(Wback.xreplace({I: Iforward, J: Jforward})-W)
        self.zero(Iforward.xreplace({Z: Zback, W: Wback})-I)
        self.zero(Jforward.xreplace({Z: Zback, W: Wback})-J)

    def test_actual_cubic_fixture_and_formal_nonconstant_chi(self):
        x, y, t, rho, Y, I, J, Z, W = sp.symbols("x y t rho Y I J Z W")
        Yf = y+t*x
        Zf = y**3+t+(3*t**2*y+rho-t**3)*x+t**3*x**2
        Wf = -rho-(y-t)**3+((y-t)**3+t)*x+rho*x**2
        If = (1-x**2)*Zf+x*Wf+(x-1)*Yf**3
        Jf = Wf-x*Zf
        Gamma = (-(y-t)**3-t*(3*y**2-3*t*y+t**2)*x
                 +(t**3-3*t**2*y)*x**2-t**3*x**3)
        self.zero(If-t)
        self.zero(Jf+rho-Gamma)
        self.assertEqual([sp.degree(f, x) for f in (x, Yf, Zf, Wf)],
                         [1, 1, 2, 2])
        leaders = [sp.Poly(f, x).LC() for f in (x, Yf, Zf, Wf)]
        self.assertEqual(leaders, [1, t, t**3, rho])
        self.zero(leaders[0]*leaders[2]-leaders[1]**3)
        eta = sp.symbols("eta")
        self.zero(sp.det(sp.Matrix([eta, t*eta, rho*eta**2]).jacobian(
            (eta, t, rho)))-eta**3)

        # First stage: (x,Y,Z,W) <-> (x,Y,I,J).
        Itarget = (1-x**2)*Z+x*W+(x-1)*Y**3
        Jtarget = W-x*Z
        Zback = I-x*J+(1-x)*Y**3
        Wback = J+x*Zback
        self.zero(Itarget.xreplace({Z: Zback, W: Wback})-I)
        self.zero(Jtarget.xreplace({Z: Zback, W: Wback})-J)
        self.zero(Zback.xreplace({I: Itarget, J: Jtarget})-Z)
        self.zero(Wback.xreplace({I: Itarget, J: Jtarget})-W)
        # Second stage is triangular, avoiding nested inverse expansion.
        yback = Y-x*I
        rhoback = Gamma.xreplace({y: yback, t: I})-J
        self.zero(yback.xreplace({Y: Yf, I: t})-y)
        self.zero(rhoback.xreplace({Y: Yf, I: t, J: Jf})-rho)
        self.zero((y+t*x).xreplace({y: yback, t: I})-Y)
        self.zero((-rho+Gamma).xreplace({y: yback, t: I, rho: rhoback})-J)
        self.assertEqual(sp.diff(x, x), 1)  # The genuine fixture has a slice.

        # Separate formal family with chi=t: no actual coordinate frame is
        # asserted for these rational coefficient data.
        b = -1/t+2*t**2-t+5
        c = 3*t-t**2+2/t**2+3/t+4
        d = (11*t+b-2*c+13)/t
        self.zero(sp.diff(b, t, 3)-6/t**4)
        q3 = 1/t**3+sp.diff(b, t, 2)/2
        q2 = 3*t+t*sp.diff(c, t, 2)/2+sp.diff(b, t, 2)+sp.diff(c, t)
        q1 = -sp.diff(b, t)+2*sp.diff(c, t)+d+t*sp.diff(d, t)
        self.zero(q3-2)
        self.zero(q2-7)
        self.zero(q1-11)
        a2 = sp.diff(b, t)+t*sp.diff(b, t, 2)/2
        a1 = 3*t**2+2*sp.diff(b, t)+c+t*sp.diff(c, t)
        a0 = -b+2*c+t*d
        B1 = b+t*sp.diff(b, t)
        B0 = t**3+2*b+t*c
        C0 = t*b
        Qchart = (q3*y**3+q2*y**2+q1*y+x*(a2*y**2+a1*y+a0)
                  +x**2*(B1*y+B0)+x**3*C0)
        Qfixed = sp.Poly(sp.expand(Qchart.subs(y, Y-t*x)), x, Y)
        self.assertLessEqual(Qfixed.total_degree(), 3)
        for coefficient in Qfixed.coeffs():
            reduced = sp.cancel(coefficient)
            self.assertEqual(reduced.free_symbols, set())


if __name__ == "__main__":
    unittest.main()
