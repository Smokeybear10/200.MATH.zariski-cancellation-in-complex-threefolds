"""Independent exact coefficient controls for primitive graph descent134.

These three methods check formal identities in equations6--11 and14--16 of
the written proof, including a varying-slope negative control, a rational
coefficient specialization and explicit constant-coefficient normalization.
Formal coefficient arrays are not asserted to be actual polynomial frames.
In particular h=1/T is nonrealizable under all the actual hypotheses once
the proof's constant-coefficient conclusion is imposed. The tests do not
prove constant-field descent, generalized Luroth, the rational-pencil kernel
lemma, or universal correction passage.
No solver or previous checker is imported, and no rational parameter is
assumed to be a polynomial invariant generator.
"""

import unittest

import sympy as s


def zero(expr):
    return s.cancel(s.expand(expr)) == 0


class PrimitiveGraphDescentControls(unittest.TestCase):
    def test_graph_jacobian_and_four_forced_coefficients(self):
        gamma, delta = s.symbols("gamma delta", nonzero=True)
        gu, gt, gr, yt, yr, yv = s.symbols("gu gt gr yt yr yv")
        # Independent implicit-graph first jets. The coefficient derivatives
        # gt,gr are distinct from the total derivatives of G(y,z).
        zt, zr = (-gt-gu*yt)/delta, (-gr-gu*yr)/delta
        M = s.Matrix([[yt, yr], [zt, zr]])
        pv = s.Matrix([yv, -gu*yv/delta])
        direct_jacobian = -(s.Matrix([[gu, delta]])*M.adjugate()*pv)[0]
        self.assertTrue(zero(direct_jacobian-yv*(gu*gr/delta-gt)))

        y, h2, h3, ell_t, ell_tt = s.symbols("y h2 h3 ell_t ell_tt")
        delta_t, delta_r, m, m_t, m_r = s.symbols("delta_t delta_r m m_t m_r")
        z_on_graph = (m-gamma*y**3-h2*y**2/2-ell_t*y)/delta
        G_u = 3*gamma*y**2+h2*y+ell_t
        G_r = delta_t*y+delta_r*z_on_graph-m_r
        G_t = h3*y**2/2+ell_tt*y+delta_t*z_on_graph-m_t
        factor = s.expand(G_u*G_r/delta-G_t)
        self.assertTrue(zero(factor.coeff(y, 5)+3*gamma**2*delta_r/delta**2))
        after_r = s.expand(factor.subs(delta_r, 0))
        self.assertTrue(zero(after_r.coeff(y, 3)-4*gamma*delta_t/delta))
        constant_slope = s.expand(after_r.subs(delta_t, 0))
        self.assertTrue(zero(constant_slope.coeff(y, 2)+3*gamma*m_r/delta+h3/2))
        self.assertTrue(zero(constant_slope.coeff(y, 1)+h2*m_r/delta+ell_tt))
        forced = s.expand(constant_slope.subs({m_r: -delta*h3/(6*gamma),
                                              ell_tt: h2*h3/(6*gamma)}))
        self.assertTrue(zero(forced-m_t-h3*ell_t/(6*gamma)))
        self.assertEqual(s.diff(forced, y), 0)

        # Consistent formal varying-delta data: delta=1+rho,
        # ell=(1+rho)^2/2, h=m=0. The factor is nonconstant in y,
        # so these data cannot satisfy the normalized unit-Jacobian premise.
        rho = s.symbols("rho")
        negative = factor.subs({gamma: 1, delta: 1+rho, delta_r: 1,
                               delta_t: 0, h2: 0, h3: 0, ell_t: 0,
                               ell_tt: 0, m: 0, m_t: 0, m_r: 0})
        self.assertTrue(zero(negative+3*y**5/(1+rho)**2))
        self.assertNotEqual(s.cancel(s.diff(negative, y)), 0)

    def test_exact_elimination_weight_three_and_rational_coefficients(self):
        gamma, delta = s.symbols("gamma delta", nonzero=True)
        tau, rho, y, h, h1, h2, lam = s.symbols("tau rho y h h1 h2 lam")
        ell0, ell1, m0 = s.symbols("ell0 ell1 m0")
        X, Y, Z, U0 = s.symbols("X Y Z U0")
        wprime = U0-(3*gamma*tau**2*y+h)*X-gamma*tau**3*X**2
        rho_solution = (wprime-3*gamma*tau*y**2-h1*y-ell0)/delta
        graph = gamma*y**3+h2*y**2/2+ell1*y+delta*(Z-rho*X)+delta*lam*rho-m0
        eliminated = s.expand(graph.subs(rho, rho_solution).subs(y, Y-tau*X))

        A2 = h2/2-3*gamma*tau*lam
        D2 = -tau*h2+h1+3*gamma*tau**2*lam
        E2 = tau**2*h2/2-tau*h1+h-gamma*tau**3*lam
        B1 = ell1-lam*h1
        C1 = -tau*ell1+lam*tau*h1-lam*h+ell0
        C0 = m0+lam*ell0
        F = (delta*Z+(lam-X)*U0+gamma*Y**3+A2*Y**2+D2*X*Y
             +E2*X**2+B1*Y+C1*X-C0)
        self.assertTrue(zero(eliminated-F))
        self.assertEqual(s.expand(eliminated).coeff(X, 3), 0)
        self.assertEqual(s.diff(F, Z), delta)
        self.assertTrue(zero(s.diff(F, U0)-lam+X))
        self.assertTrue(zero(F.subs(Z, -F.subs(Z, 0)/delta)))

        def top_weight(polynomial):
            poly = s.Poly(polynomial, X, Y, Z, U0, domain=s.EX)
            weights = (1, 1, 1, 2)
            degree = max(sum(i*j for i, j in zip(monomial, weights))
                         for monomial, _ in poly.terms())
            top = sum(coefficient*X**monomial[0]*Y**monomial[1]
                      *Z**monomial[2]*U0**monomial[3]
                      for monomial, coefficient in poly.terms()
                      if sum(i*j for i, j in zip(monomial, weights)) == degree)
            return degree, s.expand(top)

        degree, top = top_weight(F)
        self.assertEqual(degree, 3)
        self.assertTrue(zero(top+X*U0-gamma*Y**3))
        kappa, W = s.symbols("kappa W")
        original_relation = s.expand(F.subs(U0, W-kappa*Z))
        original_poly = s.Poly(original_relation, X, Y, Z, W, domain=s.EX)
        original_top = sum(coefficient*X**monomial[0]*Y**monomial[1]*Z**monomial[2]*W**monomial[3]
                           for monomial, coefficient in original_poly.terms()
                           if monomial[0]+monomial[1]+monomial[2]+2*monomial[3] == 3)
        self.assertTrue(zero(original_top+X*W-gamma*Y**3))

        # Formal rational coefficients in the exact field C(T), not a
        # claim that T is polynomial in some actual invariant ring.
        T = s.symbols("T")
        h_fun = 1/T
        lambda_fun = s.diff(h_fun, T, 3)/6
        ell_fun = -1/(15*T**5)
        self.assertTrue(zero(s.diff(ell_fun, T)-s.diff(h_fun, T, 2)**2/12))
        specialization = {gamma: 1, delta: 2, tau: T, h: h_fun,
                          h1: s.diff(h_fun, T), h2: s.diff(h_fun, T, 2),
                          lam: lambda_fun, ell0: ell_fun,
                          ell1: s.diff(ell_fun, T), m0: 1/(T-1)}
        rational_F = s.expand(F.subs(specialization, simultaneous=True))
        self.assertTrue(zero(s.Poly(rational_F, X, Y, Z, U0).coeff_monomial(Y**2)-4/T**3))
        self.assertEqual(s.fraction(s.cancel(4/T**3))[1], T**3)
        self.assertEqual(top_weight(rational_F), (3, -X*U0+Y**3))
        common_denominator = 15*T**9*(T-1)
        cleared = s.cancel(common_denominator*rational_F)
        self.assertEqual(s.fraction(cleared)[1], 1)
        s.Poly(cleared, T, X, Y, Z, U0, domain=s.QQ)
        self.assertTrue(zero(cleared/common_denominator-rational_F))
        self.assertTrue(zero(rational_F.subs(Z, -rational_F.subs(Z, 0)/2)))

    def test_mobius_top_normalization_and_explicit_affine_inverse(self):
        X, Y, Z, U0, T, I0 = s.symbols("X Y Z U0 T I0")
        gamma, delta, cI = s.symbols("gamma delta cI", nonzero=True)
        p1, p0, q1, q0 = s.symbols("p1 p0 q1 q0")
        i20, iY, iZ, iU, i0 = s.symbols("i20 iY iZ iU i0")
        Phi = X*U0-gamma*Y**3
        invariant_polynomial = cI*Phi+i20*X**2+iY*Y+iZ*Z+iU*U0+i0
        numerator, denominator = p1*I0+p0, q1*I0+q0
        parameter = numerator/denominator
        determinant = p1*q0-p0*q1
        self.assertTrue(zero(p1-parameter*q1-determinant/denominator))
        inverse_parameter = (p0-T*q0)/(T*q1-p1)
        self.assertTrue(zero(inverse_parameter.subs(T, parameter)-I0))
        self.assertTrue(zero(parameter.subs(I0, inverse_parameter)-T))

        coefficient_unit = -1/(cI*(p1-T*q1))
        pencil = coefficient_unit*(numerator-T*denominator)
        self.assertTrue(zero(s.diff(pencil, I0)+1/cI))
        self.assertTrue(zero(pencil+I0/cI-coefficient_unit*(p0-T*q0)))
        self.assertTrue(zero(pencil.subs(T, parameter)))
        actual_formal_polynomial = s.expand(pencil.subs(I0, invariant_polynomial))
        poly = s.Poly(actual_formal_polynomial, X, Y, Z, U0, domain=s.EX)
        original = s.Poly(invariant_polynomial, X, Y, Z, U0, domain=s.EX)
        for monomial, coefficient in poly.terms():
            if any(monomial):
                self.assertTrue(zero(coefficient+original.coeff_monomial(monomial)/cI))
                self.assertTrue(zero(s.diff(coefficient, T)))
        top = sum(coefficient*X**e[0]*Y**e[1]*Z**e[2]*U0**e[3]
                  for e, coefficient in poly.terms() if e[0]+e[1]+e[2]+2*e[3] == 3)
        self.assertTrue(zero(top+Phi))
        # Constant numerator and constant denominator are both legitimate.
        for entries in ((1, 2, 0, 3), (0, 2, 1, 3), (2, 1, 3, 4)):
            specialized = dict(zip((p1, p0, q1, q0), entries))
            with self.subTest(mobius=entries):
                self.assertNotEqual(determinant.subs(specialized), 0)
                self.assertTrue(zero(pencil.subs(specialized).subs(T, parameter.subs(specialized))))

        lam, A2, D2, E2, B1, C1 = s.symbols("lam A2 D2 E2 B1 C1")
        J = (delta*Z+(lam-X)*U0+gamma*Y**3+A2*Y**2+D2*X*Y
             +E2*X**2+B1*Y+C1*X)
        x0 = X-lam
        w1 = U0-E2*x0-D2*Y-2*E2*lam-C1
        F0 = gamma*Y**3+A2*Y**2+(B1+D2*lam)*Y+E2*lam**2+C1*lam
        self.assertTrue(zero(-J-x0*w1+F0+delta*Z))
        x_new, y_new, z_new, w_new = s.symbols("x_new y_new z_new w_new")
        forward = s.Matrix([x0, Y, Z, w1])
        inverse = s.Matrix([x_new+lam, y_new, z_new,
                            w_new+E2*x_new+D2*y_new+2*E2*lam+C1])
        old_vars, new_vars = (X, Y, Z, U0), (x_new, y_new, z_new, w_new)
        forward_after_inverse = forward.subs(dict(zip(old_vars, inverse)), simultaneous=True)
        inverse_after_forward = inverse.subs(dict(zip(new_vars, forward)), simultaneous=True)
        self.assertEqual([s.expand(f) for f in forward_after_inverse], list(new_vars))
        self.assertEqual([s.expand(f) for f in inverse_after_forward], list(old_vars))
        self.assertEqual(forward.jacobian(old_vars).det(), 1)
        # Constant delta gives a separate explicit coordinate completion.
        J0 = s.symbols("J0")
        recovered_Z = (J0-J.subs(Z, 0))/delta
        self.assertTrue(zero(J.subs(Z, recovered_Z)-J0))
        self.assertTrue(zero(recovered_Z.subs(J0, J)-Z))


if __name__ == "__main__":
    unittest.main()
