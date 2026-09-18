"""Finite exact controls for the base-dependent nonlinear-intercept exclusion150.

The generic jets test original-coordinate chain rules and necessary matrix
identities. They are not claimed to arise from a nilpotent speed map or an
actual dense frame. The degree controls use three explicit polynomial
coefficient families; the all-degree determinant reduction and divisor
argument remain written proofs. No rank-one classification is asserted.
The fourth method includes a genuine polynomial frame whose rational
coefficient speed q/p is NOT in the specified polynomial coefficient ring.
Known coefficient denominators are cleared before polynomial expansion;
there is no critical-root inversion, solver import, earlier-checker import,
or numerical search.
"""

import unittest

import sympy as sp


class NonlinearInterceptRankTwoControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_original_chain_rule_and_reverse_determinant(self):
        a, ap, z, Rp, Hp, Hx = sp.symbols("a ap z Rp Hp Hx")
        fp, fq, gp, gq, hp, hq = sp.symbols("fp fq gp gq hp hq")
        coefficient_matrix = sp.Matrix([[fp, fq], [gp, gq], [hp, hq]])
        source_matrix = sp.Matrix([
            [-Rp, 1, 0],
            [-(ap*z-Hp)*Rp-Hx, ap*z-Hp, a],
        ])
        original = coefficient_matrix*source_matrix
        reverse = source_matrix*coefficient_matrix
        L1, L2 = gp-Rp*fp, gq-Rp*fq
        expected_reverse = sp.Matrix([
            [L1, L2],
            [(ap*z-Hp)*L1-Hx*fp+a*hp,
             (ap*z-Hp)*L2-Hx*fq+a*hq],
        ])
        for entry in reverse-expected_reverse:
            self.zero(entry)
        self.zero(sp.trace(original)-sp.trace(reverse))
        self.zero(sp.trace(reverse)-L1-(ap*z-Hp)*L2+Hx*fq-a*hq)

        Jfg, Jfh, Jgh = fp*gq-fq*gp, fp*hq-fq*hp, gp*hq-gq*hp
        self.zero(reverse.det()-Hx*Jfg-a*Jgh+a*Rp*Jfh)

        # Independently differentiate a genuinely base-dependent polynomial
        # source pair. This is a chain-rule control, not a nilpotent frame.
        x, y, p = sp.symbols("x y p")
        R = x**2+x
        a_poly = p**2+p
        H = p*x**3+x**2+p**2*x
        source_p = y-R
        source_q = a_poly.subs(p, source_p)*z-H.subs(p, source_p)
        independent = sp.Matrix([source_p, source_q]).jacobian((x, y, z))
        direct_formula = sp.Matrix([
            [-sp.diff(R, x), 1, 0],
            [-(sp.diff(a_poly, p)*z-sp.diff(H, p))*sp.diff(R, x)-sp.diff(H, x),
             sp.diff(a_poly, p)*z-sp.diff(H, p), a_poly],
        ]).subs(p, source_p)
        for entry in independent-direct_formula:
            self.zero(entry)

    def test_determinant_reduction_one_form_and_reduced_trace(self):
        a, ap, A, Ap, B, Bp, C, Cp = sp.symbols("a ap A Ap B Bp C Cp")
        x, q, R, Rp = sp.symbols("x q R Rp")
        fp, fq, gp, gq, hp, hq = sp.symbols("fp fq gp gq hp hq")
        Jfg, Jfh, Jgh = fp*gq-fq*gp, fp*hq-fq*hp, gp*hq-gq*hp
        Hx = A*Rp+B
        determinant = Hx*Jfg+a*Jgh-a*Rp*Jfh
        self.zero(determinant-Rp*(A*Jfg-a*Jfh)-(B*Jfg+a*Jgh))

        # These are the numerators of a*dh=B*df+A*dg.
        hp_num, hq_num = B*fp+A*gp, B*fq+A*gq
        self.zero(fp*hq_num-fq*hp_num-A*Jfg)
        self.zero(gp*hq_num-gq*hp_num+B*Jfg)
        self.zero(
            Hx*Jfg+(gp*hq_num-gq*hp_num)-Rp*(fp*hq_num-fq*hp_num)
        )

        H, H_p = A*R+B*x+C, Ap*R+Bp*x+Cp
        I = ap*(q+H)-a*H_p
        U = ap*A-a*Ap
        self.zero(I-U*R-(ap*B-a*Bp)*x-(ap*q+ap*C-a*Cp))
        L1, L2 = gp-Rp*fp, gq-Rp*fq
        full_trace_times_a = a*L1+I*L2-a*Hx*fq+a**2*hq
        reduced_trace_times_a = a*L1+(I+a*A)*L2
        self.zero(
            full_trace_times_a-reduced_trace_times_a
            -a*(a*hq-B*fq-A*gq)
        )
        substituted_trace = a*L1+I*L2-a*Hx*fq+a*hq_num
        self.zero(substituted_trace-reduced_trace_times_a)

        # The rank-two gate needs Jfg!=0. These identities do not divide by
        # Jfg or claim its nonvanishing for arbitrary formal specializations.
        self.zero(Jfg.subs({fq: 0, gq: 0}, simultaneous=True))

    def test_multiple_root_and_unique_highest_degree_controls(self):
        p, q, x = sp.symbols("p q x")
        fp, fq, gp, gq = sp.symbols("fp fq gp gq")
        a = p**2*(1+p)
        A = 1+p+p**2
        B = p+p**3
        C = p**2-1
        ap = sp.diff(a, p)
        U = sp.expand(ap*A-a*sp.diff(A, p))
        self.zero(a.subs(p, 0))
        self.assertEqual(sp.Poly(a, p).coeff_monomial(p**2), 1)
        self.assertEqual(A.subs(p, 0), 1)
        self.zero(U.subs(p, 0))
        self.assertEqual(sp.Poly(U, p).coeff_monomial(p), 2)

        for n in (2, 3, 5):
            with self.subTest(R_degree=n):
                R = x**n+x
                Rp = sp.diff(R, x)
                H = A*R+B*x+C
                I = ap*(q+H)-a*sp.diff(H, p)
                self.assertEqual(sp.degree(H.subs(p, 0), x), n)
                self.zero(sp.diff(H, x)-A*Rp-B)
                self.zero(
                    I-U*R-(ap*B-a*sp.diff(B, p))*x
                    -(ap*q+ap*C-a*sp.diff(C, p))
                )

                # The necessary h_q numerator from the determinant is used
                # explicitly; arbitrary jets are not called a realization.
                full_after_one_form = (
                    a*(gp-Rp*fp)+I*(gq-Rp*fq)
                    -a*sp.diff(H, x)*fq+a*(B*fq+A*gq)
                )
                reduced = sp.expand(a*(gp-Rp*fp)+(I+a*A)*(gq-Rp*fq))
                self.zero(full_after_one_form-reduced)
                self.assertEqual(sp.degree(reduced, x), 2*n-1)
                self.zero(sp.Poly(reduced, x).LC()+n*U*fq)

                fq_zero = sp.expand(reduced.subs(fq, 0))
                self.assertEqual(sp.degree(fq_zero, x), n)
                self.zero(sp.Poly(fq_zero, x).LC()-U*gq)
                both_q_zero = sp.expand(fq_zero.subs(gq, 0))
                self.zero(both_q_zero-a*(gp-Rp*fp))

    def test_zero_U_branches_and_rational_coefficient_boundary(self):
        p, q, x = sp.symbols("p q x")
        fp, fq, gp, gq, v, w, kappa = sp.symbols("fp fq gp gq v w kappa")
        Jfg = fp*gq-fq*gp
        # V=0: two functions annihilated by the same nonzero coefficient
        # derivation cannot have a nonzero coefficient Jacobian.
        Df, Dg = fp+kappa*fq, gp+kappa*gq
        self.zero(Jfg-Df*gq+fq*Dg)
        for n in (3, 5):
            Rp = sp.diff(x**n+x, x)
            trace = sp.expand(gp-Rp*fp+(v*x+w)*(gq-Rp*fq))
            self.assertEqual(sp.degree(trace, x), n)
            self.zero(sp.Poly(trace, x).LC()+n*v*fq)
            fq_zero = sp.expand(trace.subs(fq, 0))
            self.assertEqual(sp.degree(fq_zero, x), n-1)
            self.zero(sp.Poly(fq_zero, x).LC()+n*fp)

        r, s, lam, cfun = sp.symbols("r s lam cfun")
        Rp = r*x+s
        quadratic_trace = sp.expand(
            gp-Rp*fp+(lam*Rp+kappa)*(gq-Rp*fq)
        )
        self.zero(sp.Poly(quadratic_trace, x).coeff_monomial(x**2)+lam*r**2*fq)
        self.zero(
            quadratic_trace.subs(fq, 0)
            -(gp+kappa*gq)-Rp*(lam*gq-fp)
        )
        self.zero(quadratic_trace.subs(
            {fq: 0, fp: lam*cfun, gq: cfun, gp: -kappa*cfun},
            simultaneous=True,
        ))

        # Generic rational exceptional family. a,D,C are independent
        # coefficient jets, and the derivative below holds q fixed.
        a, ap, D, Dp, C, Cp, k, c, f0, g0, h0 = sp.symbols(
            "a ap D Dp C Cp k c f0 g0 h0"
        )

        def dp(expression):
            return (sp.diff(expression, p)+ap*sp.diff(expression, a)
                    +Dp*sp.diff(expression, D)+Cp*sp.diff(expression, C))

        f = f0-c*D/r
        g = g0+c*(q+C)/a-c*k*p-c*s*D/r
        h = h0+k*g-c*D**2/(2*r)
        gp_num = c*r*(a*Cp-ap*(q+C))-c*k*a**2*r-c*s*Dp*a**2
        hp_num = k*gp_num-c*D*Dp*a**2
        self.zero(r*dp(f)+c*Dp)
        self.zero(a*sp.diff(g, q)-c)
        self.zero(a**2*r*dp(g)-gp_num)
        self.zero(a*sp.diff(h, q)-k*c)
        self.zero(a**2*r*dp(h)-hp_num)
        self.zero(a**2*dp(sp.diff(g, q))+c*ap)
        self.zero(a**2*(sp.diff(dp(g), q)-dp(sp.diff(g, q))))

        # Trace and determinant numerators for H=k*a*R+a*D*x+C.
        I_plus_aA = ap*(q+C)-a*Cp-a**2*Dp*x+k*a**2
        self.zero(gp_num+c*a**2*Rp*Dp+c*r*I_plus_aA)
        Jnum = (-c*Dp)*c  # a*r*Jfg
        self.zero(Jnum+c**2*Dp)
        Jgh_num, Jfh_num = c**2*D*Dp, k*Jnum
        self.zero(c*(k*gp_num-hp_num)-a**2*Jgh_num)
        Hx = a*(k*Rp+D)
        self.zero(Hx*Jnum+a*Jgh_num-a*Rp*Jfh_num)

        # The polynomial obstruction is (a*c(p))'=0. This identity is
        # checked on a finite coefficient family; its universal degree
        # contradiction for nonzero polynomial c(p) is in the proof.
        c0, c1, c2 = sp.symbols("c0 c1 c2")
        a_poly = p**2*(1+p)
        c_poly = c0+c1*p+c2*p**2
        product_derivative = sp.expand(sp.diff(a_poly*c_poly, p))
        self.zero(
            product_derivative-a_poly*sp.diff(c_poly, p)
            -sp.diff(a_poly, p)*c_poly
        )
        self.zero(sp.Poly(product_derivative, p).LC()-5*c2)

        # Actual retained-type line family. Its ambient polynomial speed
        # q/p is excluded by the polynomial-coefficient membership premise.
        y, z, u = sp.symbols("y z u")
        P = y-x**2/2
        source_q = P*z-P**2*x
        speeds = sp.Matrix([-P, z-P*x, -P**2/2])
        self.zero(source_q-P*speeds[1])
        self.assertEqual(sp.Poly(q, p).nth(0), q)
        self.assertNotEqual(q, 0)  # q is not divisible by p in C[p,q].
        jac = speeds.jacobian((x, y, z))
        for entry in jac**3:
            self.zero(entry)
        self.assertNotEqual(sp.expand((jac**2)[0, 0]), 0)
        self.zero(jac[:2, [1, 2]].det()+1)

        forward = (x+u*speeds[0], y+u*speeds[1], z+u*speeds[2], u)
        X, Y, Z, W = sp.symbols("X Y Z W")
        recovered_p = Y-X**2/2-W*Z
        recovered_x = X+W*recovered_p
        inverse = (
            recovered_x,
            recovered_p+recovered_x**2/2,
            Z+W*recovered_p**2/2,
            W,
        )
        source, target = (x, y, z, u), (X, Y, Z, W)
        for expression, identity in zip(inverse, source):
            self.zero(expression.subs(dict(zip(target, forward)), simultaneous=True)-identity)
        for expression, identity in zip(forward, target):
            self.zero(expression.subs(dict(zip(source, inverse)), simultaneous=True)-identity)
        for expression in forward[:3]:
            self.zero(sp.diff(expression, u, 2))
        self.zero(forward[3]-u)


if __name__ == "__main__":
    unittest.main()
