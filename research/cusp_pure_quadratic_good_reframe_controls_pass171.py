"""Finite controls for the pure quadratic cusp good-coordinate reframe.

The coefficient jets and X-chart controls are formal identities, not
asserted realizations of arbitrary data.  The triangular coordinate map
has a genuine two-sided polynomial inverse over the constant field.  The
written actual-frame argument must supply the hypotheses that make its
new coordinate E-affine and permit the retained three-good theorem.
The negative control violates pure degree at most two; it is not an
actual counterexample.  No older checker is imported or executed here.
"""

import unittest

import sympy as sp


class PureQuadraticGoodReframeControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_literal_potential_forces_constant_coefficients_and_third_jet(self):
        U, V = sp.symbols("U V")
        r, rt, rr = sp.symbols("r rt rr")
        ktt, kttt, kttr, ktrr, krrr = sp.symbols("ktt kttt kttr ktrr krrr")
        nt, nr, ntt, ntr, nrr = sp.symbols("nt nr ntt ntr nrr")
        ell, ellt, ellr = sp.symbols("ell ellt ellr")
        f = U**3+ktt*U**2/2+rt*U*V+rr*V**2/2+nt*U+nr*V
        H3k = kttt*U**3/6+kttr*U**2*V/2+ktrr*U*V**2/2+krrr*V**3/6
        H2n = ntt*U**2/2+ntr*U*V+nrr*V**2/2
        Phi = (rt*U+rr*V+nr)*(ell-f)/r+H3k+H2n-ellt*U-ellr*V
        polynomial = sp.Poly(sp.expand(Phi), U, V)
        self.zero(polynomial.coeff_monomial(U**4)+rt/r)
        self.zero(polynomial.coeff_monomial(U**3*V)+rr/r)

        # If total degree is at most two, these two quartic coefficients
        # vanish.  All derivatives of rt=rr=0 then vanish as well.
        constant_r = Phi.xreplace({rt: 0, rr: 0, kttr: 0, ktrr: 0, krrr: 0})
        reduced = sp.Poly(sp.expand(constant_r), U, V)
        self.zero(reduced.coeff_monomial(V**2)-nrr/2)
        self.zero(reduced.coeff_monomial(U*V)-ntr)
        s = sp.symbols("s")
        constant_rs = constant_r.xreplace({nr: s, nrr: 0, ntr: 0})
        self.zero(sp.Poly(sp.expand(constant_rs), U, V).coeff_monomial(U**3)
                  -(kttt/6-s/r))
        pure = sp.Poly(sp.expand(constant_rs.subs(kttt, 6*s/r)), U, V)
        self.assertLessEqual(pure.total_degree(), 2)
        self.zero(pure.coeff_monomial(V)+s**2/r+ellr)
        self.zero(pure.coeff_monomial(U**2)-(ntt/2-s*ktt/(2*r)))

        # The exact-constant integration is a written-proof step.  This
        # arithmetic independently checks its explicit polynomial form.
        t, J, L, N = sp.symbols("t J L N")
        k0 = (s*t**3-J*t**2-L*t-N)/r
        Bfun = s*t**3-r*k0
        self.zero(sp.diff(k0, t, 3)-6*s/r)
        self.zero(Bfun-(J*t**2+L*t+N))
        self.zero(sp.diff(Bfun, t, 2)/2-J)
        self.zero(sp.diff(Bfun, t)-2*J*t-L)

    def test_chart_cancellation_with_independent_theta(self):
        x, y, z, w, t, rho, theta = sp.symbols("x y z w t rho theta")
        r, s, J, L, N, a, n0 = sp.symbols("r s J L N a n0")
        k0 = (s*t**3-J*t**2-L*t-N)/r
        k = r*rho+k0
        sigma = 3*t**2*y+k
        Y = y+t*x
        Z = z+sigma*x+t**3*x**2
        W = w+theta*x+rho*x**2
        cusp = x*Z-Y**3
        self.zero(cusp-(-y**3+(z-3*t*y**2)*x+k*x**2))
        Q2 = J*Y**2+L*x*Y+N*x**2
        Vnew = r**2*W+s*Z-r*cusp-Q2
        expected_constant = r**2*w+s*z+r*y**3-J*y**2
        expected_linear = (r**2*theta+s*sigma-r*(z-3*t*y**2)
                           -(2*J*t+L)*y)
        self.zero(Vnew-expected_constant-expected_linear*x)
        self.zero(sp.Poly(sp.expand(Vnew), x).coeff_monomial(x**2))
        self.zero(a**2*sp.diff(Vnew, x, 2))
        # E=a*d/dX here, with a invariant.  No inverse formula divides by a.
        # Inserting the additional159 z identity cancels theta completely.
        z_identity = 3*t*y**2+sp.diff(k0, t)*y+r*theta+s*rho+n0
        self.zero(expected_linear.subs(z, z_identity)-(s*k0-r*n0))
        self.zero(sp.diff(expected_linear.subs(z, z_identity), theta))

    def test_polynomial_inverse_and_impure_cubic_boundary(self):
        X, Y, Z, W, V = sp.symbols("X Y Z W V")
        r, s, J, L, N = sp.symbols("r s J L N")
        Q2 = J*Y**2+L*X*Y+N*X**2
        Vforward = r**2*W+(s-r*X)*Z+r*Y**3-Q2
        Wback = (V-(s-r*X)*Z-r*Y**3+Q2)/r**2
        self.zero(Vforward.subs(W, Wback)-V)
        self.zero(Wback.subs(V, Vforward)-W)
        # Inverting the nonzero complex scalar r is polynomial over C.
        self.zero(sp.diff(Vforward, W)-r**2)
        target = sp.Matrix([X, Y, Z, Vforward])
        self.zero(target.jacobian((X, Y, Z, W)).det()-r**2)

        # Formal failure fixture: add a genuine cubic discrepancy to Bfun.
        # It violates the necessary U^3 potential equation.  This is only
        # a boundary for this reframe, not a no-completion theorem.
        x, y, z, w, t, rho, theta, defect, a = sp.symbols(
            "x y z w t rho theta defect a"
        )
        k0_bad = (s*t**3-J*t**2-L*t-N-defect*t**3)/r
        k_bad = r*rho+k0_bad
        Yf = y+t*x
        Zf = z+(3*t**2*y+k_bad)*x+t**3*x**2
        Wf = w+theta*x+rho*x**2
        Vbad = (r**2*Wf+s*Zf-r*(x*Zf-Yf**3)
                -(J*Yf**2+L*x*Yf+N*x**2))
        self.zero(sp.Poly(sp.expand(Vbad), x).coeff_monomial(x**2)-defect*t**3)
        self.zero(a**2*sp.diff(Vbad, x, 2)-2*a**2*defect*t**3)
        self.zero(sp.diff(k0_bad, t, 3)/6-s/r+defect/r)
        self.assertNotEqual(sp.expand(defect*t**3), 0)


if __name__ == "__main__":
    unittest.main()
