"""Independent finite controls for the candidate cusp quartic exclusion161.

No solver or earlier checker is imported. Formal quotient-gradient jets
check the even determinant identity. Exact rational functions check the
highest-rho coefficient mismatch for the full fifth-power family.
A separate direct Jacobian tests a formal specialized chart, explicitly
NOT an actual constant-J frame. None of these tests proves global
coordinate descent, cancellation, or every step of the universal proof.
"""

import unittest

import sympy as sp


class CuspQuarticExclusionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def test_even_determinant_from_independent_gradient_jets(self):
        U, T = sp.symbols("U T")
        A, lam, r = sp.symbols("A lam r", nonzero=True)
        B, At, Ar, Bt, Br = sp.symbols("B At Ar Bt Br")
        rp, ktt, nt, nr = sp.symbols("rp ktt nt nr")
        q = sp.symbols("q0:3")
        qt = sp.symbols("qt0:3")
        qr = sp.symbols("qr0:3")
        Q = sum(q[i] * U**i for i in range(3))
        Qt = sum(qt[i] * U**i for i in range(3))
        Qr = sum(qr[i] * U**i for i in range(3))
        Qu = sp.diff(Q, U)
        y = A * T**2 + B
        yT, yt, yr = 2*A*T, At*T**2+Bt, Ar*T**2+Br
        at = {U: y}
        thetaT = Qu.xreplace(at)*yT+1
        thetat = Qt.xreplace(at)+Qu.xreplace(at)*yt
        thetar = Qr.xreplace(at)+Qu.xreplace(at)*yr
        A1 = rp*y+nr
        B1 = 3*y**2+ktt*y+rp*(Q.xreplace(at)+T)+nt
        CU = (thetar+A1/r)*yT-yr*thetaT
        CV = yt*thetaT-(thetat+B1/r)*yT
        # The nested relation imposes kappa=-A*lambda. Its evaluated
        # gradient is (lambda-2*kappa*T*Q_U, 2*kappa*T).
        kappa = -A*lam
        gradU = lam-2*kappa*T*Qu.xreplace(at)
        gradV = 2*kappa*T
        determinant = sp.expand(CU*gradU+CV*gradV)
        even = sp.expand((determinant+determinant.subs(T, -T))/2)
        S = Qt+Qu*Qr+Qu*(rp*U+nr)/r+(3*U**2+ktt*U+rp*Q+nt)/r
        expected_even = -lam*Br+lam*T**2*(-Ar+4*A**2*S.xreplace(at))
        self.zero(even-expected_even)
        self.zero(determinant.subs(T, 0)+lam*Br)

        # Once kappa_rho=0, A=-kappa/lambda has this exact derivative.
        lr = sp.Symbol("lambda_rho")
        kap = sp.Symbol("kappa", nonzero=True)
        derivative_A = kap*lr/lam**2
        self.zero(derivative_A/(4*(-kap/lam)**2)-lr/(4*kap))

    def test_exact_fifth_power_top_coefficient_mismatch(self):
        z = sp.Symbol("z", nonzero=True)
        c0 = sp.Symbol("c0")
        c1 = sp.Symbol("c1", nonzero=True)
        f = c0+c1*z**5
        r = 1/f
        N = 10*c1*z**2/f**3
        rp = sp.diff(r, z)
        delta = sp.diff(r, z, 2)/2-rp**2/r
        b = sp.diff(N, z)-2*rp*N/r
        c = sp.diff(N, z, 2)/4-(rp*sp.diff(N, z)+N*sp.diff(r, z, 2))/(2*r)
        h = sp.cancel((2*N*c-b**2)/(2*delta))
        ell3 = sp.cancel(-(h+N**2/r)/3)
        p = sp.cancel(-b/N)
        q = sp.cancel(-h/N)
        lam3 = sp.cancel(
            rp*ell3/r-N*sp.diff(N, z)/(2*r)-sp.diff(ell3, z)-b*h/N
        )
        s2 = sp.cancel(
            sp.diff(q, z)+2*p*q+p*N/r+rp*q/r+sp.diff(N, z)/(2*r)
        )
        expected = {
            h: 5*c1*(3*c0+13*c1*z**5)/(z*f**5),
            ell3: -5*c1*(c0+11*c1*z**5)/(z*f**5),
            p: (-2*c0+3*c1*z**5)/(z*f),
            q: -(3*c0+13*c1*z**5)/(2*z**3*f**2),
            lam3: -35*c1/(z**2*f**4),
            s2: sp.Rational(21, 2)/(z**4*f),
        }
        for actual, target in expected.items():
            self.zero(actual-target)
        mismatch = sp.cancel(s2-3*lam3/(2*N))
        self.zero(mismatch-sp.Rational(63, 4)/(z**4*f))
        self.assertNotEqual(mismatch, 0)
        # Zero c0 is allowed. c1=0 is excluded by the nongraph proof
        # and is never substituted into a division by delta or N.
        self.zero(mismatch.subs(c0, 0)-sp.Rational(63, 4)/(c1*z**9))

    def test_direct_jacobian_of_a_formal_nested_chart_fails(self):
        tau, rho, T = sp.symbols("tau rho T", nonzero=True)
        U, V = sp.symbols("U V")
        r = tau**-5
        k = r*rho
        n = 5*tau**-13*rho**2
        ell = -55*tau**-21*rho**3
        f = (
            U**3+sp.diff(k, tau, 2)*U**2/2
            +sp.diff(r, tau)*U*V+sp.diff(n, tau)*U+sp.diff(n, rho)*V
        )
        g3 = (
            sp.diff(k, tau, 3)*U**3/6
            +sp.diff(r, tau, 2)*U**2*V/2
            +sp.diff(n, tau, 2)*U**2/2
            +sp.diff(n, tau, rho)*U*V+sp.diff(n, rho, 2)*V**2/2
        )
        phi = sp.cancel(
            sp.diff(f, V)*(ell-f)/r+g3-sp.diff(ell, tau)*U-sp.diff(ell, rho)*V
        )
        N = sp.diff(n, rho, 2)
        Q = tau**6*U**2+3*rho*U/tau-sp.Rational(13, 2)*rho**2/tau**8
        lam = -35*rho**3/tau**22
        nu = phi.subs({U: 0, V: 0})-N*Q.subs(U, 0)**2/2
        self.zero(phi-(N*(V-Q)**2/2+lam*U+nu))

        # B=rho is just a convenient generic intercept, not a proven
        # actual choice. The selected relation holds with m=nu+lambda*B.
        A = -N/(2*lam)
        y = A*T**2+rho
        theta = Q.subs(U, y)+T
        z0 = 3*tau*y**2+sp.diff(k, tau)*y+r*theta+n
        w = (ell-f.xreplace({U: y, V: theta}))/r
        self.zero(phi.xreplace({U: y, V: theta})-(nu+lam*rho))
        original_matrix = sp.Matrix([y, z0, w]).jacobian((tau, rho, T))
        determinant = sp.cancel(original_matrix.det())
        expected_T2 = -45/(rho*tau**13)
        self.zero(sp.expand(determinant).coeff(T, 2)-expected_T2)
        self.assertNotEqual(expected_T2, 0)
        self.assertGreater(sp.degree(determinant, T), 0)


if __name__ == "__main__":
    unittest.main()
