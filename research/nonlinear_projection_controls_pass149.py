"""Finite exact controls for two nonlinear projected placements149.

These are formal necessary-condition calculations, not completed actual
four-coordinate frames. The source-coordinate shears have both inverse
orders checked, but no inverse is inferred for a shifted four-variable pair.
The proof's algebraic-root and whole-line arguments remain written proofs.
All critical-row checks use polynomial numerators before expansion: neither
an unknown critical denominator nor a large rational gcd is introduced.
No previous checker or solver is imported.
"""

import unittest

import sympy as sp


class NonlinearProjectionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def affine_numerator(self, row, variable, numerator, denominator):
        """Return denominator*row(numerator/denominator), without division."""
        for entry in row:
            self.zero(sp.diff(entry, variable, 2))
        return row.applyfunc(
            lambda entry: sp.expand(
                denominator*entry.subs(variable, 0)
                + numerator*sp.diff(entry, variable)
            )
        )

    def test_first_lane_cleared_rows_parity_and_degree_controls(self):
        p, q, t, z, X, rp = sp.symbols("p q t z X rp")
        fp, fq, gp, gq = sp.symbols("fp fq gp gq")
        J = fp*gq-fq*gp
        B = p+2*t*rp
        delta = B*gq-2*t*fq
        critical = z*delta+B*gp-2*t*fp
        self.zero(fq*critical-(fq*z+fp)*delta+B*J)

        # These are p times the independent absolute differential rows.
        p_rows = sp.Matrix([
            [-rp*z+p*X*fp, rp+p*X*fq, p+2*t*rp],
            [-z+p*X*gp, 1+p*X*gq, 2*t],
        ])
        transformed_first = sp.Matrix([[X*(fp-rp*gp), X*(fq-rp*gq), 1]])
        for entry in p_rows.row(0)-rp*p_rows.row(1)-p*transformed_first:
            self.zero(entry)
        cleared_difference = p_rows.row(1)-2*t*transformed_first
        at_critical = self.affine_numerator(cleared_difference, X, -1, delta)
        for entry, target in zip(at_critical, (-critical, 0, 0)):
            self.zero(entry-target)

        for n in (2, 3):
            with self.subTest(shear_degree=n):
                # R(z)=z^n+2z. Everything below is already polynomial.
                zn = q+t**2
                b_num = p**n+4*t*p**(n-1)+2*n*t*zn**(n-1)
                delta_num = b_num*gq-2*t*fq*p**(n-1)
                f_num = sp.expand(zn*delta_num+p*b_num*gp-2*t*fp*p**n)
                self.zero(
                    f_num+f_num.subs(t, -t)
                    -2*p**n*((q+t**2)*gq+p*gp)
                )
                self.assertEqual(sp.degree(f_num, t), 2*n+1)
                self.zero(sp.Poly(f_num, t).LC()-2*n*gq)
                if n == 3:
                    branch = sp.expand(f_num.subs(gq, 0))
                    self.assertEqual(sp.degree(branch, t), 5)
                    self.zero(sp.Poly(branch, t).LC()-6*p*gp)

                # Differentiate a finite polynomial speed specialization in
                # original (p,t,z), independently of the generic row identity.
                R = z**n+2*z
                source_q = p*z-t**2
                goods = sp.Matrix([t+R+X*p, z+X*source_q])
                original_rows = goods.jacobian((p, t, z))
                coefficient_rows = p_rows.subs(
                    {rp: sp.diff(R, z), fp: 1, fq: 0, gp: 0, gq: 1},
                    simultaneous=True,
                )
                change = sp.Matrix([[1, 0, 0], [z, -2*t, p], [0, 1, 0]])
                self.zero(change.det()+p)
                for entry in coefficient_rows*change-p*original_rows:
                    self.zero(entry)

    def test_second_lane_cleared_rows_and_all_parity_degree_cases(self):
        p, q, t, z, X, B, T, c = sp.symbols("p q t z X B T c")
        fp, fq, gp, gq, d0, d1 = sp.symbols("fp fq gp gq d0 d1")
        J = fp*gq-fq*gp
        delta = p*B*gq-2*t*fq
        critical = (z*B+2*t)*delta+B*(p*B*gp-2*t*fp)
        self.zero(
            fq*critical-(fq*(z*B+2*t)+B*fp)*delta+p*B**2*J
        )
        raw_first = sp.Matrix([[1+X*fp, X*fq, B]])
        second_scaled = sp.Matrix([[-z+p*X*gp, 1+p*X*gq, 2*t]])
        cleared_difference = B*second_scaled-2*t*raw_first
        at_critical = self.affine_numerator(cleared_difference, X, -B, delta)
        for entry, target in zip(at_critical, (-critical, 0, 0)):
            self.zero(entry-target)
        self.zero(critical.subs(B, 0)+4*t**2*fq)

        A = (q+T)*gq+p*gp
        # C_num=p*C, so no symbolic reciprocal p is expanded.
        C_num = p**2*gq-(q+T)*fq-p*fp
        for k in (0, 1, 2, 3):
            with self.subTest(D0_degree=k):
                D0 = d0 if k == 0 else d0+d1*T**k
                bt = c+t*D0.subs(T, t**2)
                a_t, cn_t = A.subs(T, t**2), C_num.subs(T, t**2)
                p_f = sp.expand(
                    p*bt**2*a_t+2*t*bt*cn_t-4*p*t**2*fq
                )
                odd_equation = sp.expand(p*D0*A+C_num)
                even_part = sp.expand(
                    p*(c**2+T*D0**2)*A+2*T*D0*C_num-4*p*T*fq
                )
                reduced_even = sp.expand(p*(c**2*A-T*D0**2*A-4*T*fq))
                self.zero(
                    p_f-p_f.subs(t, -t)
                    -4*c*t*odd_equation.subs(T, t**2)
                )
                self.zero(p_f+p_f.subs(t, -t)-2*even_part.subs(T, t**2))
                self.zero(even_part-reduced_even-2*T*D0*odd_equation)

                if k >= 2:
                    self.zero(sp.Poly(odd_equation, T).LC()-p*d1*gq)
                    gq_zero = sp.expand(odd_equation.subs(gq, 0))
                    self.assertEqual(sp.degree(gq_zero, T), k)
                    self.zero(sp.Poly(gq_zero, T).LC()-p**2*d1*gp)
                elif k == 1:
                    self.zero(sp.Poly(odd_equation, T).coeff_monomial(T**2)-p*d1*gq)
                    after_forcing_gq_zero = sp.expand(reduced_even.subs(gq, 0))
                    self.assertEqual(sp.degree(after_forcing_gq_zero, T), 3)
                    self.zero(sp.Poly(after_forcing_gq_zero, T).LC()+p**2*gp*d1**2)
                else:
                    self.zero(sp.Poly(reduced_even, T).coeff_monomial(T**2)+p*d0**2*gq)
                    self.zero(sp.Poly(odd_equation.subs(gq, 0), T).coeff_monomial(T)+fq)

        # D0=0 is the affine boundary, treated separately in the proof.
        self.zero(sp.Poly(C_num, T).coeff_monomial(T)+fq)
        reduced_affine = p*c**2*A
        self.zero(sp.Poly(reduced_affine, T).coeff_monomial(T)-p*c**2*gq)
        self.zero(J.subs({fq: 0, fp: p*gq, gq: 0}, simultaneous=True))

        # Whole-line finite controls are not a substitute for the module proof.
        O = 1+T
        self.zero((t*O.subs(T, t**2))**2-(T*O**2).subs(T, t**2))
        self.assertEqual(sp.rem(sp.Integer(1), O, T), 1)
        R = 2*t+t**2+t**4
        self.zero(R-(T+T**2).subs(T, t**2)-2*t)

    def test_exceptional_divisor_and_actual_intercept_shear_inverses(self):
        p, q, t, z, X = sp.symbols("p q t z X")
        c, d, e, alpha, beta, gamma = sp.symbols("c d e alpha beta gamma")
        R = c*z**2+d*z+e
        source_q = p*z-t**2
        f = 2*c*alpha*q+d*alpha*p+gamma
        g = alpha*p+beta
        source_goods = sp.Matrix([
            t+R+X*f.subs(q, source_q), z+X*g
        ])
        rows = source_goods.jacobian((p, t, z))
        reduced = sp.Matrix.vstack(rows.row(0)-sp.diff(R, z)*rows.row(1), rows.row(1))
        expected = sp.Matrix([
            [0, 1-4*c*alpha*t*X, 2*c*alpha*p*X],
            [alpha*X, 0, 1],
        ])
        for entry in reduced-expected:
            self.zero(entry)
        minors = [reduced[:, [i, j]].det() for i, j in ((0, 1), (0, 2), (1, 2))]
        for minor, target in zip(
            minors,
            (-alpha*X*(1-4*c*alpha*t*X), -2*c*alpha**2*p*X**2, 1-4*c*alpha*t*X),
        ):
            self.zero(minor-target)
        at_divisor = self.affine_numerator(reduced.subs(p, 0), X, 1, 4*c*alpha*t)
        for entry in at_divisor.row(0):
            self.zero(entry)
        self.assertEqual(at_divisor[1, 0], alpha)
        self.assertNotEqual(1-t**2, 0)  # h=q+1 survives generic p=0.

        rp = sp.diff(R, z)
        B = p+2*t*rp
        delta = B*sp.diff(g, q)-2*t*sp.diff(f, q)
        critical = z*delta+B*sp.diff(g, p)-2*t*sp.diff(f, p)
        self.zero(critical-p*alpha)

        # These are only the three-coordinate intercept automorphisms.
        # They are not inverses of a shifted four-coordinate frame.
        A, Y, Z = sp.symbols("A Y Z")
        source = (p, t, z)
        target = (A, Y, Z)
        for n in (2, 3):
            forward = (p, t+z**n+z, z)
            inverse = (A, Y-Z**n-Z, Z)
            for expression, identity in zip(inverse, source):
                self.zero(expression.subs(dict(zip(target, forward)), simultaneous=True)-identity)
            for expression, identity in zip(forward, target):
                self.zero(expression.subs(dict(zip(source, inverse)), simultaneous=True)-identity)
        for n in (2, 4):
            forward = (p+t+t**n, z, t)
            inverse = (A-Z-Z**n, Z, Y)
            for expression, identity in zip(inverse, source):
                self.zero(expression.subs(dict(zip(target, forward)), simultaneous=True)-identity)
            for expression, identity in zip(forward, target):
                self.zero(expression.subs(dict(zip(source, inverse)), simultaneous=True)-identity)


if __name__ == "__main__":
    unittest.main()
