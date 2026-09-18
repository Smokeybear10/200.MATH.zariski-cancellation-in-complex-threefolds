"""Finite independent coefficient controls for the three-stage obstruction155.

Four generic coefficient-jet families of stage degrees (r,q,k)>=2 check the
full derivative identity and both successive highest R coefficients. The
parameter derivatives are independent symbols; they are not obtained from
the proof's reduced identity. The formal plane inverse is also checked.

A separate rational differential-field example has k=1 and satisfies both
gradient identities. It confirms why the outer-degree hypothesis matters.
Neither method supplies an actual dense sliced four-coordinate frame.
Finite symbolic controls are not proofs of the universal degree argument,
canonical tail return, or exhaustive placement of an embedded line.
No previous checker, solver, or search implementation is imported.
"""

import unittest

import sympy as sp


class ThreeStageGradientControls(unittest.TestCase):
    def zero(self, expression):
        # The first method is polynomial. The boundary has only monomial
        # powers of the named coefficient-field parameter tau in denominators.
        self.assertEqual(sp.expand(expression), 0)

    def zeros(self, expressions):
        for expression in expressions:
            self.zero(expression)

    def test_independent_parameter_jets_and_successive_top_coefficients(self):
        U, V, R, H = sp.symbols("U V R H")
        alpha, lam = sp.symbols("alpha lam", nonzero=True)
        beta, c, n, lam_d, n_d = sp.symbols("beta c n lam_d n_d")
        for r, q, k in ((2, 2, 2), (3, 2, 2), (2, 3, 2), (2, 2, 3)):
            with self.subTest(inner=r, middle=q, outer=k):
                aa, bb, cc = (sp.symbols(f"a0:{r+1}"),
                              sp.symbols(f"b0:{q+1}"),
                              sp.symbols(f"c0:{k+1}"))
                ad, bd, cd = (sp.symbols(f"ad0:{r+1}"),
                              sp.symbols(f"bd0:{q+1}"),
                              sp.symbols(f"cd0:{k+1}"))
                # These independent generators are nonzero in their rational
                # function field. No centering or zero lower coefficient is
                # imposed; every coefficient keeps its independent jet.
                A = lambda t: sum(aa[j]*t**j for j in range(r+1))
                B = lambda t: sum(bb[j]*t**j for j in range(q+1))
                C = lambda t: sum(cc[j]*t**j for j in range(k+1))
                Ad = sum(ad[j]*U**j for j in range(r+1))
                Bd = sum(bd[j]*R**j for j in range(q+1))
                Cd = sum(cd[j]*H**j for j in range(k+1))
                Ruv = V-A(U)
                Huv = U-B(Ruv)
                Ui, Vi = H+B(R), R+A(H+B(R))
                forward_substitution = {R: Ruv, H: Huv}
                inverse_substitution = {U: Ui, V: Vi}
                self.zeros((Ui.subs(forward_substitution, simultaneous=True)-U,
                            Vi.subs(forward_substitution, simultaneous=True)-V,
                            Ruv.subs(inverse_substitution, simultaneous=True)-R,
                            Huv.subs(inverse_substitution, simultaneous=True)-H))
                # This inverse belongs to the formal plane over the coefficient
                # field, not to an asserted actual original four-ring change.

                phi = C(Huv)+lam*Ruv+n
                psi = alpha*Huv+beta+c*phi
                parameters = (*aa, *bb, *cc, lam, n)
                jets = (*ad, *bd, *cd, lam_d, n_d)
                delta_phi = sum(sp.diff(phi, p)*jet for p, jet in zip(parameters, jets))
                original_residual = delta_phi-sp.diff(psi, U)
                # First replace V, which restores the independent middle R;
                # only then replace U, which restores the outer residual H.
                residual = sp.expand(original_residual.subs(V, R+A(U))
                                     .subs(U, H+B(R)))
                Aprime = sp.diff(A(U), U)
                Bprime = sp.diff(B(R), R)
                Cprime = sp.diff(C(H), H)
                P = c*Aprime-Ad
                P_at = P.subs(U, H+B(R))
                A_at = Aprime.subs(U, H+B(R))
                expected = (Cd-Cprime*(Bd+Bprime*P_at+c)
                            +lam_d*R+lam*P_at+n_d-alpha*(1+Bprime*A_at))
                self.zero(residual-expected)

                # The generic highest degree comes from the top jet of A.
                # Its elimination is a necessary consequence of residual=0,
                # not an assertion that these unrestricted jets satisfy it.
                pr = sp.Poly(P, U).coeff_monomial(U**r)
                self.zero(pr+ad[r])
                high_degree = q*(r+1)-1
                first_coefficient = sp.Poly(residual, R).coeff_monomial(R**high_degree)
                self.assertEqual(sp.Poly(residual, R).degree(), high_degree)
                self.zero(first_coefficient+q*bb[q]**(r+1)*pr*Cprime)
                self.assertGreater(high_degree, q*r)
                self.assertGreater(high_degree, q*r-1)

                # Impose precisely p_r=0 by setting the independent top jet
                # ad_r to zero. Every other jet remains independent.
                reduced = sp.expand(residual.subs(ad[r], 0))
                P_reduced = sp.expand(P.subs(ad[r], 0))
                pnext = sp.Poly(P_reduced, U).coeff_monomial(U**(r-1))
                self.zero(pnext-(c*r*aa[r]-ad[r-1]))
                next_degree = q*r-1
                second_coefficient = sp.Poly(reduced, R).coeff_monomial(R**next_degree)
                self.assertEqual(sp.Poly(reduced, R).degree(), next_degree)
                self.zero(second_coefficient
                          +q*bb[q]**r*(pnext*Cprime+alpha*r*aa[r]))
                self.assertGreater(next_degree, q)
                self.assertGreater(next_degree, q*(r-1))

                obstruction = -pnext*Cprime-alpha*r*aa[r]
                self.assertEqual(sp.Poly(obstruction, H).degree(), k-1)
                self.zero(sp.Poly(obstruction, H).coeff_monomial(H**(k-1))
                          +pnext*k*cc[k])
                # The zero-pnext branch still has a nonzero scalar residual.
                zero_branch = sp.expand(obstruction.subs(ad[r-1], c*r*aa[r]))
                self.zero(zero_branch+alpha*r*aa[r])
                self.assertNotEqual(zero_branch, 0)

    def test_degree_one_outer_stage_formal_boundary(self):
        U, V, R, H, tau, rho = sp.symbols("U V R H tau rho")
        # Coefficient field C(tau,rho), delta=partial_tau. Inverting tau
        # here is permitted in that FORMAL field, not in an original B.
        A = lambda t: t*t+sp.Rational(1, 2)
        B = lambda t: (t*t-sp.Rational(1, 4))/(2*tau)
        C = lambda t: -2*tau*t
        Ruv = V-A(U)
        Huv = U-B(Ruv)
        alpha, beta, c, lam, n = 2*tau, -rho, 1, 1, rho+sp.Rational(1, 2)
        phi = C(Huv)+lam*Ruv+n
        psi = alpha*Huv+beta+c*phi
        self.zeros((phi-((V-U*U)**2-2*tau*U+rho),
                    psi-(V-U*U),
                    sp.diff(phi, tau)-sp.diff(psi, U),
                    sp.diff(phi, rho)-sp.diff(psi, V)))
        self.assertEqual(sp.Poly(A(U), U).degree(), 2)
        self.assertEqual(sp.Poly(B(R), R).degree(), 2)
        self.assertEqual(sp.Poly(C(H), H).degree(), 1)
        self.zero(sp.Poly(B(R), R).coeff_monomial(R))
        P = c*sp.diff(A(U), U)-sp.diff(A(U), tau)
        self.zero(P-2*U)
        pnext = sp.Poly(P, U).coeff_monomial(U)
        # The second top-coefficient equation really holds: C' is now a
        # nonzero coefficient-field constant, rather than positive H-degree.
        self.zero(-pnext*sp.diff(C(H), H)-alpha*2)
        self.assertNotEqual(pnext, 0)
        self.assertEqual(sp.Poly(sp.diff(C(H), H), H).degree(), 0)
        # No actual dense frame is asserted. This boundary only shows that
        # the differential-field obstruction cannot drop its k>=2 premise.


if __name__ == "__main__":
    unittest.main()
