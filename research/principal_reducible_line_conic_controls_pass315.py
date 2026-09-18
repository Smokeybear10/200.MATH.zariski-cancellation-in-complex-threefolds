"""Six standalone exact algebra controls for working proofs 313 and 315.

No solver or earlier checker is imported. These identities do not verify
the full initial-kernel input, exact constant fields, whole-ring return,
primitive-LND theorem, or published recognition endpoint. See the proofs.
"""

import unittest

import sympy as sp


class ReducibleLineConicControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def surface(self):
        names = "P V m p q kt ktt kttt nt ns ntt nts nss ell lt ls h0"
        values = sp.symbols(names)
        v = dict(zip(names.split(), values))
        P, V, m, p, q, kt, ktt, kttt, nt, ns, ntt, nts, nss, ell, lt, ls, h0 = values
        F = ktt*P**2/2+p*P*V+nt*P+ns*V
        A1 = sp.diff(F, P)-(2*P+kt)*(p*P+ns)/m
        A0 = ((p*P+ns)*(ell-F)/m+kttt*P**3/6+q*P**2*V/2
              +ntt*P**2/2+nts*P*V+nss*V**2/2-lt*P-ls*V-h0)
        return v, F, A1, A0

    def test_formal_discriminant_coefficients(self):
        v, _, A1, A0 = self.surface()
        P, V, m, p = (v[name] for name in ("P", "V", "m", "p"))
        delta = sp.Poly(sp.expand(A1**2-4*A0), P, V)
        self.assert_zero(delta.coeff_monomial(V**2)-(p**2-2*v["nss"]))
        self.assert_zero(delta.coeff_monomial(P**2*V)+2*v["q"])
        expected = 2*p*v["ktt"]-2*v["kt"]*p**2/m+4*p*v["ns"]/m-4*v["nts"]
        self.assert_zero(delta.coeff_monomial(P*V)-expected)
        # All possible V terms are retained; no evaluated substitution is used.
        self.assertLessEqual(delta.degree(V), 2)

    def test_exact_joint_constant_slopes_including_zero_c(self):
        m, c, kt, ktt, ns, nts, nss = sp.symbols("m c kt ktt ns nts nss")
        eta = (c*kt/2-ns)/m
        eta_t = c*sp.diff(eta, m)+ktt*sp.diff(eta, kt)+nts*sp.diff(eta, ns)
        eta_s = c*sp.diff(eta, kt)+nss*sp.diff(eta, ns)
        pv = 2*c*ktt-2*kt*c**2/m+4*c*ns/m-4*nts
        self.assert_zero(4*m*eta_t-pv)
        self.assert_zero(eta_s-(c**2/2-nss)/m)
        self.assert_zero((4*m*eta_t-pv).subs(c, 0))
        self.assert_zero(eta_s.subs(nss, c**2/2))

    def test_complete_actual_auxiliary_row(self):
        X, t, s, v, c, d, a, gamma, theta0 = sp.symbols("X t s v c d a gamma theta0")
        sigma, kt, k, n, j, w0, eta = sp.symbols("sigma kt k n j w0 eta")
        m = c*t+d
        ns = c*kt/2-m*eta
        theta = gamma*v+theta0
        y = j-c*theta/2
        z = 2*t*y+sigma**2+kt*sigma+m*theta+n
        D0 = (2*sigma+kt)/m
        lam = (c*sigma+ns)/m
        w = -D0*y-lam*theta+w0
        Y = y+sigma*X+t*X**2
        Z = z+(2*t*sigma+k)*X+t**2*X**2
        W = w+theta*X+s*X**2
        tau = a*gamma
        for coordinate, target in ((X, 0), (Y, -c*tau/2),
                                   (Z, d*tau), (W, (X+eta)*tau)):
            self.assert_zero(a*sp.diff(coordinate, v)-target)
        self.assert_zero((c*D0/2-lam)-eta)

    def test_both_actual_coordinate_frames_and_inverses(self):
        X, Y, Z, W, U, V, c, d, eta, tau = sp.symbols("X Y Z W U V c d eta tau")
        u1 = Z+2*d*Y/c
        v1 = W+2*(X+eta)*Y/c
        inverse1 = {Z: U-2*d*Y/c, W: V-2*(X+eta)*Y/c}
        self.assert_zero(u1.subs(inverse1)-U)
        self.assert_zero(v1.subs(inverse1)-V)
        self.assert_zero(inverse1[Z].subs({U: u1, V: v1})-Z)
        self.assert_zero(inverse1[W].subs({U: u1, V: v1})-W)

        def action(expression, cy, dz):
            return sp.expand(cy*sp.diff(expression, Y)+dz*sp.diff(expression, Z)
                             +(X+eta)*tau*sp.diff(expression, W))

        self.assert_zero(action(u1, -c*tau/2, d*tau))
        self.assert_zero(action(v1, -c*tau/2, d*tau))
        # The c=0 frame is defined separately; no specialization into 1/c.
        u2 = Y
        v2 = W-(X+eta)*Z/d
        inverse2 = {Y: U, W: V+(X+eta)*Z/d}
        self.assert_zero(u2.subs(inverse2)-U)
        self.assert_zero(v2.subs(inverse2)-V)
        self.assert_zero(inverse2[W].subs({U: u2, V: v2})-W)
        self.assert_zero(action(u2, 0, d*tau))
        self.assert_zero(action(v2, 0, d*tau))

    def test_conic_lower_coefficient_solves(self):
        v, _, A1, A0 = self.surface()
        P, V, m, p = (v[name] for name in ("P", "V", "m", "p"))
        bP, bV, b0 = sp.symbols("bP bV b0")
        mu = v["ktt"]-(v["kt"]*p+2*v["ns"])/m
        nu = v["nt"]-v["kt"]*v["ns"]/m
        B = bP*P+bV*V+b0
        residual = sp.Poly(sp.expand(A0-(A1-B)*B), P, V)
        C2 = v["ntt"]/2-(p*v["nt"]+v["ns"]*v["ktt"]/2)/m
        b0_solve = m*((mu-bP)*bP-C2)/(2*p)
        ls_solve = -v["ns"]**2/m-(p-2*bV)*b0-nu*bV
        self.assert_zero(residual.coeff_monomial(P**2).subs(b0, b0_solve))
        self.assert_zero(residual.coeff_monomial(V)-(ls_solve-v["ls"]))
        self.assert_zero(sp.diff(b0_solve, v["h0"]))
        self.assert_zero(sp.diff(ls_solve, v["h0"]))

    def test_conic_polynomial_support_and_factor_unit_solve(self):
        s, sigma, eta, m, p, q = sp.symbols("s sigma eta m p q")
        k10, k20, k30 = sp.symbols("k10 k20 k30")
        n0, n1, n2, nt0, nt1, nt2, ntt0, ntt1, ntt2 = sp.symbols(
            "n0 n1 n2 nt0 nt1 nt2 ntt0 ntt1 ntt2")
        kttt1 = sp.symbols("kttt1")
        kt = p*s+k10
        ktt = q*s+k20
        kttt = kttt1*s+k30
        ns = 2*n2*s+n1
        nt = nt2*s**2+nt1*s+nt0
        ntt = ntt2*s**2+ntt1*s+ntt0
        mu = ktt-(kt*p+2*ns)/m
        nu = nt-kt*ns/m
        bP = ktt/4-m*kttt/(12*p)
        bV = p/2-m*q/(4*p)
        C2 = ntt/2-(p*nt+ns*ktt/2)/m
        b0 = m*((mu-bP)*bP-C2)/(2*p)
        ls = -ns**2/m-(p-2*bV)*b0-nu*bV
        for expression, degree in ((mu, 1), (nu, 2), (bP, 1), (b0, 2), (ls, 2)):
            self.assertLessEqual(sp.Poly(sp.expand(expression), s).degree(), degree)
        self.assert_zero(p-2*bV-m*q/(2*p))
        theta = (eta+2*p*sigma**2/m-(mu-2*bP)*sigma-nu+2*b0)/(p-2*bV)
        factor_difference = -2*p*sigma**2/m+(p-2*bV)*theta+(mu-2*bP)*sigma+nu-2*b0
        self.assert_zero(factor_difference-eta)
        self.assertLessEqual(sp.Poly(sp.expand(theta), sigma).degree(), 2)
        self.assertLessEqual(sp.Poly(sp.expand(theta), eta).degree(), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
