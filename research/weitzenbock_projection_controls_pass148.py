"""Exact formal controls for fixed projected-plane obstructions148.

These are necessary-condition and coefficient-field calculations, not
actual completed four-coordinate frames. The critical-point proof uses
an algebraic root over C(r,q); the finite identities below do not replace
that universal argument or classify arbitrary nonlinear coordinate
placements. Rational speed examples explicitly retain their invariant
denominators. The final method checks finite divisor-leading coefficients
for a variable-H model; it does not prove the universal valuation lemma.
No previous checker or solver is imported.
"""

import unittest

import sympy as sp


class WeitzenbockProjectionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_generic_critical_polynomial_and_minor_identities(self):
        A, Ar, q, t, X, alpha, beta = sp.symbols("A Ar q t X alpha beta")
        fr, fq, gr, gq = sp.symbols("fr fq gr gq")
        J = fr*gq - fq*gr
        for d in (2, 3):
            with self.subTest(degree=d):
                H, Hp = t**d, d*t**(d-1)
                rows = sp.Matrix([[alpha + X*fr, X*fq, 1],
                                  [-Ar*(q+H)/A**2 + beta + X*gr,
                                   1/A + X*gq, Hp/A]])
                C = Ar*(q+H) + alpha*A*Hp - beta*A**2
                D = A*gq - Hp*fq
                critical = sp.expand(C*D + A**2*gr - A*Hp*fr)
                self.zero(fq*critical - (fq*C + A*fr)*D + A**2*J)
                self.assertEqual(sp.degree(critical, t), 2*d - 1)
                self.zero(sp.Poly(critical, t).LC() + d*Ar*fq)
                first_branch = sp.expand(critical.subs(fq, 0))
                self.assertEqual(sp.degree(first_branch, t), d)
                self.zero(sp.Poly(first_branch, t).LC() - Ar*A*gq)

                evaluated = rows.subs(X, -1/D)
                residual = evaluated.row(1) - Hp/A*evaluated.row(0)
                for entry, expected in zip(residual, (-critical/(A**2*D), 0, 0)):
                    self.zero(entry - expected)
                # At a root of critical with D nonzero, all minors vanish.
                # The exact Bezout identity above supplies the nonzero-D gate
                # when fq!=0; when fq=0, D=A*gq is a nonzero coefficient.
                minors = [evaluated[:, [i, j]].det() for i, j in ((0, 1), (0, 2), (1, 2))]
                for minor, expected in zip(minors, (-fq*critical/(A**2*D**2),
                                                    critical/(A**2*D), 0)):
                    self.zero(minor - expected)

    def test_polynomial_and_rational_speed_examples_in_both_branches(self):
        r, q, t, z, X, alpha, beta = sp.symbols("r q t z X alpha beta")
        speed_pairs = ((r, q), (q, r), (1/r, q/r), (q/r, r))
        for a in (r, r**2 + 1):
            for d in (2, 3):
                H, Hp = t**d, d*t**(d-1)
                for f, g in speed_pairs:
                    with self.subTest(a=a, degree=d, f=f, g=g):
                        ar = sp.diff(a, r)
                        fr, fq, gr, gq = sp.diff(f, r), sp.diff(f, q), sp.diff(g, r), sp.diff(g, q)
                        J = sp.cancel(fr*gq - fq*gr)
                        self.assertNotEqual(J, 0)
                        D = sp.cancel(a*gq - Hp*fq)
                        C = ar*(q+H) + alpha*a*Hp - beta*a**2
                        critical = sp.cancel(C*D + a**2*gr - a*Hp*fr)
                        self.assertEqual(sp.degree(critical, t), d if fq == 0 else 2*d - 1)
                        self.assertNotEqual(D, 0)
                        self.zero(fq*critical - (fq*C + a*fr)*D + a**2*J)

                        # Independently differentiate the original placement
                        # (r,t,z), then compare its rational change to (r,q,t).
                        source_q = a*z - H
                        original_goods = sp.Matrix([t + alpha*r + X*f.subs(q, source_q),
                                                    z + beta*r + X*g.subs(q, source_q)])
                        original_rows = original_goods.jacobian((r, t, z))
                        coefficient_rows = sp.Matrix([
                            [alpha + X*fr, X*fq, 1],
                            [-ar*(q+H)/a**2 + beta + X*gr, 1/a + X*gq, Hp/a],
                        ])
                        change = sp.Matrix([[1, 0, 0], [ar*z, -Hp, a], [0, 1, 0]])
                        self.zero(change.det() + a)
                        composed_rows = coefficient_rows.subs(q, source_q)*change
                        for entry in original_rows - composed_rows:
                            self.zero(entry)

                        evaluated = coefficient_rows.subs(X, -1/D)
                        residual = evaluated.row(1) - Hp/a*evaluated.row(0)
                        self.zero(residual[0] + critical/(a**2*D))
                        self.zero(residual[1])
                        self.zero(residual[2])
                        # These denominator examples lie in invariant
                        # localizations. No actual completion is asserted.
                        for speed in (f, g):
                            numerator, denominator = sp.fraction(sp.cancel(speed))
                            self.zero(denominator*speed - numerator)
                            self.zero(sp.diff(denominator, t))
                            self.zero(sp.diff(denominator, z))

    def test_planes_containing_coefficient_coordinate_have_distinct_failures(self):
        r, q, t, z, T, b, c = sp.symbols("r q t z T b c")
        for d in (2, 3):
            with self.subTest(degree=d):
                a, H = r**2 + 1, t**d
                projected = b*t + c*(q+H)/a
                self.assertEqual(sp.degree(projected, t), d)
                self.zero(sp.Poly(projected, t).LC() - c/a)
                # For c!=0 this is a degree-d polynomial in the generic
                # line parameter; the written field-degree argument, not
                # a finite test, proves L[projected] is proper in L[t].
                defining_polynomial = a*T - a*b*t - c*(q+H)
                self.zero(defining_polynomial.subs(T, projected))
                self.assertEqual(sp.degree(defining_polynomial, t), d)

                # The plane span(r,t) instead collapses over the surviving
                # divisor r=0 when a(r)=r^2. It is not a whole-line failure
                # over the generic coefficient field.
                ramified_a = r**2
                source_q = ramified_a*z - H
                self.zero(source_q.subs(r, 0) + t**d)
                residue_relation = T**d + q
                self.zero(residue_relation.subs({T: t, q: -t**d}, simultaneous=True))
                self.assertEqual(sp.degree(residue_relation, T), d)
                invariant_denominator = q + 1
                self.assertNotEqual(invariant_denominator, 0)
                self.assertNotEqual(invariant_denominator.subs(q, -t**d), 0)
                # Thus this chosen invariant localization does not remove
                # the generic divisor, while both projected residues are
                # algebraic over C(q). No actual dense frame is claimed.

    def test_variable_H_multiple_root_divisor_leading_controls(self):
        r, q, t, X, alpha, beta = sp.symbols("r q t X alpha beta")
        a = r**2 * (1+r)
        ar = sp.diff(a, r)
        lower_constant_g = r**-3 + r**-1

        def order_and_leading(expression):
            numerator, denominator = sp.fraction(sp.cancel(expression))
            top, bottom = sp.Poly(numerator, r), sp.Poly(denominator, r)
            ntop = min(monomial[0] for monomial, coefficient in top.terms() if coefficient != 0)
            nbottom = min(monomial[0] for monomial, coefficient in bottom.terms() if coefficient != 0)
            return ntop-nbottom, sp.cancel(top.nth(ntop)/bottom.nth(nbottom))

        for d in (2, 3):
            with self.subTest(residue_degree=d):
                P, Pprime = t**d, d*t**(d-1)
                H = P + r*t**7 + r**2*t**9
                Hr, Ht = sp.diff(H, r), sp.diff(H, t)
                I = ar*(q+H) - a*Hr + alpha*a*Ht - beta*a**2
                self.zero(H.subs(r, 0) - P)
                self.assertEqual(sp.degree(H, t), 9)

                def data(f, g):
                    fr, fq = sp.diff(f, r), sp.diff(f, q)
                    gr, gq = sp.diff(g, r), sp.diff(g, q)
                    D = a*gq - Ht*fq
                    F = I*D + a**2*gr - a*Ht*fr
                    J = fr*gq - fq*gr
                    return fr, fq, gr, gq, D, F, J

                # e=2 and the first q-dependent coefficient of g has m=0.
                # The four rows cover n<m+e, n>m+e, and both tie types.
                cases = (
                    (r*q, 2, -Pprime*(3*q+2*P), 2*d-1),
                    (r**3*q, 3, 2*P, d),
                    (r**2*q, 3, -Pprime*(4*q+2*P)+2*P, 2*d-1),
                    (r**2, 3, -2*Pprime+2*P, d),
                )
                for f, expected_order, expected_leading, expected_degree in cases:
                    g = q + lower_constant_g
                    fr, fq, gr, gq, D, F, J = data(f, g)
                    self.assertNotEqual(sp.cancel(J), 0)
                    # Retain the ORIGINAL g and J in the coprimality identity.
                    self.zero(fq*F - (fq*I + a*fr)*D + a**2*J)
                    observable = sp.expand(F - F.subs(t, 0))
                    order, leading = order_and_leading(observable)
                    self.assertEqual(order, expected_order)
                    self.zero(leading - expected_leading)
                    self.assertEqual(sp.degree(leading, t), expected_degree)
                    F_without_constant_g = data(f, q)[5]
                    self.zero(F-F_without_constant_g-a**2*sp.diff(lower_constant_g, r))
                    self.zero(sp.diff(F-F_without_constant_g, t))
                    self.zero(observable - (F_without_constant_g-F_without_constant_g.subs(t, 0)))

                # Independently retain H_r/a in the fixed-q differential row.
                f, g = r*q, q+lower_constant_g
                fr, fq, gr, gq, D, F, J = data(f, g)
                rows = sp.Matrix([[alpha+X*fr, X*fq, 1],
                                  [beta+Hr/a-ar*(q+H)/a**2+X*gr,
                                   1/a+X*gq, Ht/a]])
                evaluated = rows.subs(X, -1/D)
                difference = evaluated.row(1)-Ht/a*evaluated.row(0)
                for actual, expected in zip(difference, (-F/(a**2*D), 0, 0)):
                    self.zero(actual-expected)
                self.assertNotEqual(sp.cancel(J-data(f, q)[6]), 0)

                # If g_q=0 its entire contribution is t-constant. This is
                # not permission to change the original determinant J.
                fr, fq, gr, gq, D, F, J = data(r*q, r**-3)
                self.zero(gq)
                self.assertNotEqual(sp.cancel(J), 0)
                self.zero(F + Ht*(I*fq+a*fr) - a**2*gr)
                order, leading = order_and_leading(F-F.subs(t, 0))
                self.assertEqual(order, 2)
                self.zero(leading + Pprime*(3*q+2*P))


if __name__ == "__main__":
    unittest.main()
