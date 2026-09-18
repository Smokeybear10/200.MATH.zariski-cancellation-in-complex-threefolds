"""Independent exact controls for the pass-21 bridge obstructions.

Only SymPy and the standard library are imported. These finite controls do
not prove the written all-parameter module arguments, rank classification,
K-theory claims, novelty, or unrestricted cancellation.
"""

import unittest

import sympy as sp


x, y, z, r, h, t = sp.symbols("x y z r h t")
a, q, c, f = sp.symbols("a q c f")
X, rho, sigma = sp.symbols("X rho sigma")
u = sp.symbols("u")


def forward(xx, rr, tt):
    local = q * xx / 2 - a * tt
    new_r = rr + h * local
    new_x = xx + local * (rr + new_r)
    new_s = (
        tt - q * rr * tt - q**2 * xx * h * tt / 2
        + a * h * q * tt**2 / 2 + c * xx * rr / 2
        + c * q * xx**2 * h / 8
    )
    return new_x, new_r, new_s


def inverse(xx, rr, ss):
    local = a * ss - q * xx / 2
    old_r = rr + h * local
    old_x = xx + local * (old_r + rr)
    old_t = ss + q * ss * (old_r + rr) / 2 - c * xx * (old_r + rr) / 4
    return old_x, old_r, old_t


def relation_reduce(value):
    """Reduction in Q[a,c,h,x,r,t,...][q]/(q^2-ac)."""
    return sp.rem(sp.Poly(sp.expand(value), q), sp.Poly(q**2 - a*c, q)).as_expr().expand()


def jet(value, modulus):
    return sp.rem(sp.Poly(sp.expand(value), f), sp.Poly(f**modulus, f)).as_expr().expand()


def physical_base(n):
    ff = x*z - y**2
    rr = x**3 + y*ff**n
    hh = z*ff**(2*n) + 2*x**2*y*ff**n + x**5
    grad_f = sp.Matrix([sp.diff(ff, v) for v in (x, y, z)])
    grad_h = sp.Matrix([sp.diff(hh, v) for v in (x, y, z)])
    coefficients = [-sp.expand(v) for v in grad_f.cross(grad_h)]

    def derivative(value):
        return sp.expand(sum(b * sp.diff(value, v) for b, v in zip(coefficients, (x, y, z))))

    return ff, rr, hh, coefficients, derivative


class PrimitiveBridgeChecks(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.expand(value), 0)

    def test_universal_invariants_and_slice(self):
        fx, fr, fs = forward(x, r, t)

        def E(value):
            return 2*a*r*sp.diff(value, x) + a*h*sp.diff(value, r) + (1+q*r)*sp.diff(value, t)

        for value, target in ((fx, 0), (fr, 0), (fs, 1)):
            self.assertZero(relation_reduce(E(value) - target))
        # The relation really matters. Dropping ac=q^2 is a negative control.
        self.assertNotEqual(sp.expand(E(fs)-1), 0)
        self.assertEqual(sp.Poly(fs, t).degree(), 2)

    def test_universal_two_sided_inverse(self):
        fx, fr, fs = forward(x, r, t)
        gx, gr, gt = inverse(X, rho, sigma)
        for expression, target in zip((gx, gr, gt), (x, r, t)):
            self.assertZero(relation_reduce(expression.subs({X: fx, rho: fr, sigma: fs}, simultaneous=True)-target))
        for expression, target in zip((fx, fr, fs), (X, rho, sigma)):
            self.assertZero(relation_reduce(expression.subs({x: gx, r: gr, t: gt}, simultaneous=True)-target))

    def test_universal_polynomiality_and_surface_levels(self):
        fx, fr, fs = forward(x, r, t)
        gx, gr, gt = inverse(X, rho, sigma)
        for expression in (fx, fr, fs, gx, gr, gt):
            # Polynomial with rational coefficients, without inverting a or h.
            sp.Poly(expression, x, r, t, X, rho, sigma, h, a, q, c, domain=sp.QQ)
        self.assertZero(fx*h - fr**2 - (x*h-r**2))
        self.assertZero(gx*h - gr**2 - (X*h-rho**2))

    def test_physical_derivation_sign_primitivity_and_fixed_point(self):
        for n in (2, 3):
            with self.subTest(n=n):
                ff, rr, hh, coefficients, D = physical_base(n)
                self.assertZero(x*hh - rr**2 - ff**(2*n+1))
                for value, target in ((ff, 0), (hh, 0), (rr, ff**n*hh), (x, 2*ff**n*rr)):
                    self.assertZero(D(value)-target)
                self.assertEqual(sp.gcd_list(coefficients), 1)
                self.assertTrue(all(v.subs({x: 0, y: 0, z: 0}) == 0 for v in coefficients))
                self.assertZero(D(D(x))-2*ff**(2*n)*hh)

    def test_second_image_residue_independence(self):
        # Finite degree controls for the proof's disjoint 0,3,1 residue classes.
        columns = [u**(5*j+e) for e in (0, 3, 1) for j in range(9)]
        degree = max(sp.degree(v, u) for v in columns)
        matrix = sp.Matrix([[sp.expand(v).coeff(u, i) for v in columns] for i in range(degree+1)])
        self.assertEqual(matrix.rank(), len(columns))

    def test_valuation_window_and_minimum_degree_obstruction(self):
        for n in range(2, 11):
            for ell in range((n+1)//2, n):
                for J in (sp.Integer(1), 1+h, h**2+f):
                    qq = f**ell*J
                    cc = sp.cancel(qq**2/f**n)
                    sp.Poly(cc, f, h)
                    self.assertNotEqual(jet(qq, n), 0)
                    self.assertNotEqual(jet(f**(n+ell)*h*J, 2*n), 0)
                    self.assertZero((f**(n-ell)).subs(f, 0))
        # A permitted boundary has a gauge primitive; do not overclaim obstruction.
        D = lambda value: 2*f**3*r*sp.diff(value, x) + f**3*h*sp.diff(value, r)
        qq = f**3*(1+h)
        self.assertZero(D(qq*x/(2*f**3))-qq*r)
        # Outside 2 ell >= n, the displayed inverse need not be polynomial.
        self.assertEqual(sp.denom(sp.cancel((f**1)**2/f**3)), f)

    def test_forward_curve_jets_with_nonconstant_invariants(self):
        for n, ell in ((2, 1), (3, 2), (4, 2), (5, 3)):
            for J in (sp.Integer(1), h, 1+h+f):
                qq = f**ell*J
                qu = qq.subs(h, u**5)
                curve_x = u + qu*u**4
                curve_r = u**3 + qu*u**6/2
                ptilde = jet(X**2-sp.Rational(5, 2)*qq.subs(h, X**5)*X**5, n)
                with self.subTest(n=n, ell=ell, J=J):
                    self.assertZero(jet(curve_r-curve_x*ptilde.subs(X, curve_x), n))
                    self.assertZero(jet(u**5-curve_x*ptilde.subs(X, curve_x)**2, n))
                    self.assertZero(jet(qq*sp.diff(qq, h), n))

    def test_inverse_curve_jets_recompute_invariant_h(self):
        # Do not silently reuse q(f,X^5) where q(f,h_new) is required.
        for n, ell in ((2, 1), (4, 2), (5, 3)):
            qq = f**ell*(1+h+f)
            ptilde = jet(X**2-sp.Rational(5, 2)*qq.subs(h, X**5)*X**5, n)
            hh = jet(X*ptilde**2, n)
            rr = jet(X*ptilde, n)
            q_new = jet(qq.subs(h, hh), n)
            old_x = jet(X-q_new*X*rr, n)
            old_r = jet(rr-q_new*X*hh/2, n)
            self.assertZero(jet(old_r-old_x**3, n))
            self.assertZero(jet(hh-old_x**5, n))
            self.assertZero(jet(old_x-(X-qq.subs(h, X**5)*X**4), n))

    def test_physical_second_denominator_cancellation(self):
        Y, P = sp.symbols("Y P")
        rr = X*P + Y*a
        numerator = h-2*P*Y*a-X*P**2
        relation = X*h-rr**2-a**2*f
        self.assertZero(X*numerator-a**2*(Y**2+f)-relation)
        # Recover, rather than assume, the two lowest-order repair coefficients.
        coefficient = sp.symbols("coefficient")
        fx, fr, _ = forward(x, r, t)
        for power_h, power_x in ((0, 5), (1, 10)):
            substitution = {a: f**2, q: f*h**power_h, c: h**(2*power_h)}
            curve_x = jet(fx.subs(substitution).subs({x: u, r: u**3, h: u**5, t: 0}), 2)
            curve_r = jet(fr.subs(substitution).subs({x: u, r: u**3, h: u**5, t: 0}), 2)
            candidate = X**2+coefficient*f*X**power_x
            defect = jet(curve_r-curve_x*candidate.subs(X, curve_x), 2)
            equations = sp.Poly(defect, f, u).coeffs()
            self.assertEqual(sp.solve(equations, coefficient), {coefficient: -sp.Rational(5, 2)})

    def test_primitive_triangular_control(self):
        ss = t+y**3/2+x*y**4/8-x*y*t-x**2*y**2*t/2+x**3*t**2/2
        for m in (2, 3, 4, 7):
            D = lambda value: x**2*sp.diff(value, y)+y**m*sp.diff(value, z)
            invariant = (m+1)*x**2*z-y**(m+1)
            self.assertZero(D(invariant))
            self.assertZero(D(ss)+(1+x*y)*sp.diff(ss, t)-1)
            self.assertEqual(sp.gcd(x**2, y**m), 1)
            ideal = sp.groebner([x**2, y**m], x, y, z)
            self.assertEqual(ideal.reduce(invariant)[1], 0)
            self.assertEqual(ideal.reduce(x*y)[1], x*y)

    def test_nonlinear_translation_and_no_constant_centralizer(self):
        uu, vv, ww, zz = sp.symbols("u v w zeta")
        ss = zz-ww**2
        coefficients = [2*ss, 4*uu*ss, 8*uu*vv*ss, 1+16*uu*vv*ww*ss]
        coordinates = (uu, vv, ww, zz)
        E = lambda value: sp.expand(sum(b*sp.diff(value, v) for b, v in zip(coefficients, coordinates)))
        aa, bb, cc = uu-ss**2, vv-uu**2, ww-vv**2
        for value, target in ((ss, 1), (aa, 0), (bb, 0), (cc, 0)):
            self.assertZero(E(value)-target)
        self.assertEqual(sp.det(sp.Matrix([aa, bb, cc, ss]).jacobian(coordinates)).expand(), 1)
        lam = sp.symbols("l0:4")
        rows = []
        for b in coefficients:
            bracket = sum(v*sp.diff(b, w) for v, w in zip(lam, coordinates))
            rows.extend(sp.Poly(bracket, *coordinates).coeffs())
        matrix, rhs = sp.linear_eq_to_matrix(rows, lam)
        self.assertEqual(matrix.rank(), 4)
        self.assertTrue(all(v == 0 for v in rhs))

    def test_finite_center_transport_and_jacobian_obstruction(self):
        T = sp.symbols("T")
        V = 1+x
        self.assertZero(x**2+(1-x)*V-1)
        self.assertZero(sp.rem(V*(1-x)-1, x**2, x))
        source = h+T**2
        target = h+V**2*T**2
        shifted_h = h+(V**2-1)*T**2
        self.assertZero(source.subs(h, shifted_h)-target)
        self.assertZero(target.subs(h, h-(V**2-1)*T**2)-source)
        # Arbitrary polynomial corrections in h and T vanish from the jet.
        H = h**2+x*T+h*T
        L = h*T**2+T+x*h
        determinant = sp.Matrix([x, h+x**2*H, V*T+x**2*L]).jacobian((x, h, T)).det()
        self.assertZero(sp.rem(sp.expand(determinant), x**2, x)-(1+x))
        self.assertEqual(sp.Poly(1+x, x).degree(), 1)

    def test_singular_degree_stage(self):
        F, G, T, xx = sp.symbols("F G T xx")
        relation = xx*G-F**3-T**2
        self.assertTrue(all(sp.diff(relation, v).subs({F: 0, G: 0, T: 0, xx: 0}) == 0 for v in (F, G, T, xx)))
        ff, rr, hh, _, D = physical_base(1)
        self.assertZero(relation.subs({F: ff, G: hh, T: rr, xx: x}, simultaneous=True))
        self.assertZero(D(rr)-ff*hh)

    def test_conductor_pair_interpolation(self):
        wi, wj, bi, bj = sp.symbols("wi wj bi bj")
        c1 = (bi-bj)/(wi-wj)
        c0 = bi-wi*c1
        self.assertEqual(sp.cancel(c0+wi*c1-bi), 0)
        self.assertEqual(sp.cancel(c0+wj*c1-bj), 0)
        # Each pairwise diagonal contributes one independent gluing ratio.
        diagonal = sp.Matrix([[1,0,0], [1,0,0], [0,1,0], [0,1,0], [0,0,1], [0,0,1]])
        self.assertEqual(diagonal.rank(), 3)
        self.assertEqual(6-diagonal.rank(), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
