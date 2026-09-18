"""Finite exact controls for the constant-speed binary-cubic argument134.

The first method checks independent formal Jacobian coefficients, not an
integrable or realizable arbitrary matrix. The second checks the formal
double-root consequences and the resulting nonunit determinant factor;
it supplies no actual double-root polynomial automorphism. The third is
an actual inverse-verified pure-cube family with arbitrary constant cubic
coefficients. These examples do not prove the generic-component argument,
the finite-field descent, the embedded-line lemma, correction passage,
or the universal rigidity theorem. No previous checker is imported.
"""

import unittest

import sympy as s


def zero(expr):
    return s.expand(expr) == 0


class BinaryCubicRigidityControls(unittest.TestCase):
    def test_formal_block_coefficients_and_integrated_potentials(self):
        t, r, u, v = s.symbols("t r u v")
        y, z, yv, zv = s.symbols("y z yv zv")
        c30, c21, c12, c03 = s.symbols("c30 c21 c12 c03")
        m11, m12, m21, m22 = s.symbols("m11 m12 m21 m22")
        kt, kr, ktt, ktr, krr, lt, lr = s.symbols("kt kr ktt ktr krr lt lr")
        k0, ell0, m0, j0 = s.symbols("k0 ell0 m0 j0", nonzero=True)
        M = s.Matrix([[m11, m12], [m21, m22]])
        p, pv = s.Matrix([y, z]), s.Matrix([yv, zv])
        C = c30*t**3 + c21*t**2*r + c12*t*r**2 + c03*r**3
        gradC = s.Matrix([s.diff(C, t), s.diff(C, r)])
        hessC = s.hessian(C, (t, r))
        gradCp = gradC.subs({t: y, r: z}, simultaneous=True)
        gradk, hessk = s.Matrix([kt, kr]), s.Matrix([[ktt, ktr], [ktr, krr]])
        gradell = s.Matrix([lt, lr])

        # The coefficient tensor of C and Hessian of k are symmetric;
        # M itself is entirely independent and is not assumed symmetric.
        third_contraction = s.Matrix([
            (p.T*hessC.diff(t)*p)[0]/2,
            (p.T*hessC.diff(r)*p)[0]/2,
        ])
        self.assertTrue(all(zero(x) for x in third_contraction-gradCp))
        self.assertEqual(M+M.adjugate(), s.trace(M)*s.eye(2))
        A = M+u*s.eye(2)
        self.assertEqual(A.adjugate(), M.adjugate()+u*s.eye(2))

        dw, dd = s.symbols("dw dd")
        wt, wr, dt, dr = s.symbols("wt wr dt dr")
        gradw_raw, gradd_raw = s.Matrix([wt, wr]), s.Matrix([dt, dr])
        bottom = gradw_raw+u*gradd_raw+u**2*gradC
        block = A.row_join(pv).col_join(bottom.T.row_join(s.Matrix([[dw+u*dd]])))
        block_formula = A.det()*(dw+u*dd)-(bottom.T*A.adjugate()*pv)[0]
        self.assertTrue(zero(block.det()-block_formula))
        self.assertTrue(zero(s.expand(block_formula).coeff(u, 3)-dd+gradC.dot(pv)))
        self.assertTrue(zero(s.expand(A.det()/j0).coeff(u, 2)-1/j0))

        B = hessC*p+gradk
        nu = gradCp+hessk*p+gradell
        gradd = M.T*gradC+B
        gradw = M.T*B+nu
        dv, wv = gradC.dot(pv), B.dot(pv)
        integrated = (A.det()*(wv+u*dv)
                      -((gradw+u*gradd+u**2*gradC).T*A.adjugate()*pv)[0])
        targets = [-(nu.T*M.adjugate()*pv)[0], -nu.dot(pv), 0, 0]
        for power, target in enumerate(targets):
            with self.subTest(coefficient=power):
                self.assertTrue(zero(s.expand(integrated).coeff(u, power)-target))

        d = gradC.dot(p)+k0
        w = (p.T*hessC*p)[0]/2+gradk.dot(p)+ell0
        G = C.subs({t: y, r: z}, simultaneous=True)+(p.T*hessk*p)[0]/2+gradell.dot(p)-m0
        jet = {y: y+yv*v, z: z+zv*v}
        for potential, derivative in ((d, dv), (w, wv), (G, nu.dot(pv))):
            self.assertTrue(zero(s.diff(potential.subs(jet, simultaneous=True), v).subs(v, 0)-derivative))

    def test_formal_double_root_line_and_nonunit_jacobian_factor(self):
        U, V, f, gamma = s.symbols("U V f gamma", nonzero=True)
        ktt, ktr, krr, lt, lr, m = s.symbols("ktt ktr krr lt lr m")
        G = gamma*U**2*V+ktt*U**2/2+ktr*U*V+krr*V**2/2+lt*U+lr*V-m
        on_line = s.Poly(G.subs(U, f), V)
        self.assertEqual(on_line.coeff_monomial(V**2), krr/2)
        self.assertTrue(zero(on_line.coeff_monomial(V)-gamma*f**2-ktr*f-lr))
        normal_derivative = s.diff(G, U).subs(U, f)
        self.assertTrue(zero(s.diff(normal_derivative, V)-2*gamma*f-ktr))

        constrained = s.expand(G.subs({krr: 0, ktr: -2*gamma*f,
                                       lr: gamma*f**2, m: ktt*f**2/2+lt*f}))
        R = gamma*(U-f)*V+ktt*(U+f)/2+lt
        self.assertTrue(zero(constrained-(U-f)*R))
        self.assertTrue(zero(R.subs(U, f)-ktt*f-lt))
        self.assertEqual(s.diff(R.subs(U, f), V), 0)
        # Commuting derivatives give (k_tr)_r=(k_rr)_t=0.
        rr = s.symbols("rr")
        ff = s.Function("f")(rr)
        self.assertEqual(s.diff(-2*gamma*ff, rr), -2*gamma*s.diff(ff, rr))

        u, y = s.symbols("u y")
        t0, t1, t2 = s.symbols("t0 t1 t2")
        tu = t0+t1*y+t2*y**2
        zu, zy, zz, zw, wu, wy, wz, ww = s.symbols("zu zy zz zw wu wy wz ww")
        J = s.Matrix([[1, 0, 0, 0], [tu, 1+u*s.diff(tu, y), 0, 0],
                      [zu, zy, zz, zw], [wu, wy, wz, ww]])
        factor = 1+u*s.diff(tu, y)
        self.assertTrue(zero(J.det()-factor*(zz*ww-zw*wz)))
        self.assertEqual(s.Poly(factor, u).degree(), 1)
        self.assertEqual(s.expand(factor.subs({u: -1, y: 0, t1: 1})), 0)
        self.assertTrue(zero(J.det().subs({u: -1, y: 0, t1: 1})))

    def test_actual_pure_cube_family_inverse_and_normalized_coefficients(self):
        u, a, b, v = s.symbols("u a b v")
        X, Y, Z, W, A, B, V = s.symbols("X Y Z W A B V")
        gamma, beta, alpha, epsilon = s.symbols("gamma beta alpha epsilon")

        def F(x):
            return gamma*x**3+beta*x**2+alpha*x+epsilon

        def Fprime(x):
            return 3*gamma*x**2+2*beta*x+alpha

        def Delta(aa, vv, xx):
            return aa*Fprime(vv)+aa**2*(3*gamma*vv+beta)*xx+gamma*aa**3*xx**2

        frame = s.Matrix([u, v+a*u, a-F(v)+b*u, b+Delta(a, v, u)])
        back_a = Z-X*W+F(Y)
        original_to_base = dict(zip((X, Y, Z, W), frame))
        recovered_a = s.expand(back_a.subs(original_to_base, simultaneous=True))
        recovered_u = frame[0]
        recovered_v = s.expand(frame[1]-recovered_a*recovered_u)
        recovered_b = s.expand(frame[3]-Delta(recovered_a, recovered_v, recovered_u))
        self.assertEqual([recovered_u, recovered_a, recovered_b, recovered_v], [u, a, b, v])

        # Independent placeholders prove the reverse order without imposing
        # a hidden relation among the original X,Y,Z,W coordinates.
        reverse = [X, V+A*X, A-F(V)+B*X, B+Delta(A, V, X)]
        reverse = [s.expand(f.subs(B, W-Delta(A, V, X))) for f in reverse]
        reverse = [s.expand(f.subs(V, Y-A*X)) for f in reverse]
        self.assertEqual(reverse, [X, Y, A+X*W-F(Y), W])
        self.assertEqual([s.expand(f.subs(A, back_a)) for f in reverse], [X, Y, Z, W])
        self.assertTrue(zero(frame.jacobian((u, a, b, v)).det()-1))
        self.assertEqual([s.diff(f, u) for f in frame[:3]], [1, a, b])
        self.assertTrue(all(zero(s.diff(f, u, 2)) for f in frame[:3]))
        self.assertTrue(zero(s.diff(frame[3], u, 2)-2*gamma*a**3))
        self.assertEqual(s.diff(frame[3], u, 3), 0)

        def T(f):
            return s.expand(-u*s.diff(f, a)+(1+u*Fprime(v))*s.diff(f, b)+u**2*s.diff(f, v))

        self.assertEqual([T(f) for f in frame], [0, 0, 0, 1])
        self.assertEqual([s.expand(T(f)).coeff(u, 2) for f in (a, b, v)], [0, 0, 1])
        p = s.Matrix([v, a-F(v)])
        pv = p.diff(v)
        M = p.jacobian((a, b))
        C = gamma*a**3
        gradC = s.Matrix([s.diff(C, a), s.diff(C, b)])
        hessC = s.hessian(C, (a, b))
        k, ell, m = beta*a**2, b+alpha*a, a-epsilon
        gradk = s.Matrix([s.diff(k, a), s.diff(k, b)])
        d_actual = s.expand(frame[3]).coeff(u, 1)
        w_actual = frame[3].subs(u, 0)
        self.assertTrue(zero(d_actual-gradC.dot(p)-k))
        self.assertTrue(zero(w_actual-(p.T*hessC*p)[0]/2-gradk.dot(p)-ell))
        G = F(Y)+Z-a
        self.assertTrue(zero(G.subs({Y: p[0], Z: p[1]}, simultaneous=True)))
        gradG = s.Matrix([Fprime(v), 1])
        self.assertTrue(zero(-(gradG.T*M.adjugate()*pv)[0]-1))
        integrated_m = gamma*p[0]**3+beta*p[0]**2+alpha*p[0]+p[1]
        self.assertTrue(zero(integrated_m-m))
        self.assertTrue(zero(s.Matrix(frame[1:]).jacobian((a, b, v)).det()-1))


if __name__ == "__main__":
    unittest.main()
