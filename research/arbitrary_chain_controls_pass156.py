"""Finite recurrence controls for the arbitrary-chain obstruction156.

Short chains of lengths 3,4,5, including mixed degrees, check the top-two
coefficient induction and the critical-fiber degree/Jacobian recurrences.
The fiber is reconstructed backwards as univariate polynomials; its U
derivatives are computed independently forwards. Full nested U,V expressions
of product degree are deliberately not expanded.

Coefficient jets are formal tangent variables before numerical coefficient
specialization, not a claim that a C-derivation differentiates complex
constants nontrivially. No chain here is an actual dense four-frame. The
length-two boundary satisfies the formal gradient identity and explicitly
has no claimed actual realization. Finite tests do not prove the universal
obstruction, AMS extraction, coordinate entry, or cancellation.
No previous checker or solver is imported.
"""

import math
import unittest

import sympy as sp


class ArbitraryChainControls(unittest.TestCase):
    CHAINS = ((2, 2, 2), (3, 2, 3), (2, 3, 2, 2), (3, 2, 2, 3, 2))

    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    @staticmethod
    def stage(index, degree, t):
        return t**degree+sum((index+j)*t**j for j in range(degree))

    def test_top_two_coefficients_and_first_residual_degree_gate(self):
        H, K, R, pr, lam, nu = sp.symbols("H K R pr lam nu")
        for degrees in self.CHAINS:
            with self.subTest(degrees=degrees):
                n, r, q = len(degrees), degrees[0], degrees[1]
                A = lambda i, t: self.stage(i, degrees[i-1], t)
                A2 = A(2, R)
                bq = sp.Poly(A2, R).LC()
                P_at = pr*(H+A2)**r+(H+A2)**(r-1)+1

                if n == 3:
                    F = A(3, H)+lam*R+nu
                    first_product = sp.expand((sp.diff(F, R)
                                               -sp.diff(A2, R)*sp.diff(F, H))*P_at)
                    degree = q*(r+1)-1
                    self.assertEqual(sp.Poly(first_product, R).degree(), degree)
                    self.zero(sp.Poly(first_product, R).LC()
                              +q*bq**(r+1)*pr*sp.diff(A(3, H), H))
                    self.assertGreater(degree, q*r)
                    self.assertGreater(degree, q*r-1)
                    continue

                Z = {2: H, 3: K}
                previous_degree, previous_top, previous_next = 1, sp.Integer(1), sp.Integer(0)
                leading_pairs = {3: (previous_top, previous_next)}
                # One additional formal recurrence Z_n exercises the genuine
                # top-two induction step even for the short n=5 control.
                # The final F below still uses only Z_(n-1), Z_(n-2).
                for i in range(4, n+1):
                    Z[i] = sp.expand(Z[i-2]-A(i, Z[i-1]))
                    degree = math.prod(degrees[3:i])
                    poly = sp.Poly(Z[i], K)
                    if i == 4:
                        Ai = sp.Poly(A(i, K), K)
                        expected_top = -Ai.LC()
                        expected_next = -Ai.coeff_monomial(K**(degrees[i-1]-1))
                    else:
                        leading = sp.Poly(A(i, K), K).LC()
                        expected_top = -leading*previous_top**degrees[i-1]
                        expected_next = (-leading*degrees[i-1]
                                         *previous_top**(degrees[i-1]-1)*previous_next)
                        self.assertGreaterEqual(previous_degree, 2)
                    self.assertEqual(poly.degree(), degree)
                    self.zero(poly.LC()-expected_top)
                    self.zero(poly.coeff_monomial(K**(degree-1))-expected_next)
                    self.zero(sp.diff(poly.LC(), H))
                    self.zero(sp.diff(poly.coeff_monomial(K**(degree-1)), H))
                    previous_degree, previous_top, previous_next = degree, expected_top, expected_next
                    leading_pairs[i] = (expected_top, expected_next)

                Ftilde = sp.expand(A(n, Z[n-1])+lam*Z[n-2]+nu)
                Gtilde = Z[n-1]
                E0 = math.prod(degrees[3:n-1])
                D = degrees[-1]*E0
                poly = sp.Poly(Ftilde, K)
                if n == 4:
                    outer = sp.Poly(A(n, K), K)
                    expected_top = outer.LC()
                    expected_next = outer.coeff_monomial(K**(D-1))
                else:
                    leading = sp.Poly(A(n, K), K).LC()
                    prior_top, prior_next = leading_pairs[n-1]
                    expected_top = leading*prior_top**degrees[-1]
                    expected_next = (leading*degrees[-1]
                                     *prior_top**(degrees[-1]-1)*prior_next)
                self.assertEqual(poly.degree(), D)
                self.zero(poly.LC()-expected_top)
                self.zero(poly.coeff_monomial(K**(D-1))-expected_next)
                self.zero(sp.diff(poly.LC(), H))
                self.zero(sp.diff(poly.coeff_monomial(K**(D-1)), H))
                self.assertEqual(sp.Poly(Gtilde, K).degree(), E0)

                F = sp.expand(Ftilde.subs(K, R-A(3, H)))
                G = sp.expand(Gtilde.subs(K, R-A(3, H)))
                FH = sp.diff(F, H)
                self.assertEqual(sp.Poly(FH, R).degree(), D-1)
                self.zero(sp.Poly(FH, R).coeff_monomial(R**(D-1))
                          +D*expected_top*sp.diff(A(3, H), H))
                first_product = sp.expand((sp.diff(F, R)-sp.diff(A2, R)*FH)*P_at)
                degree = D+q*(r+1)-2
                self.assertEqual(sp.Poly(first_product, R).degree(), degree)
                self.zero(sp.Poly(first_product, R).LC()
                          -D*q*expected_top*bq**(r+1)*sp.diff(A(3, H), H)*pr)
                self.assertGreater(degree, D+q-1)
                self.assertGreater(degree, E0+q*r-1)
                self.assertLessEqual(sp.Poly(sp.diff(G, H), R).degree(), E0)
                self.assertLessEqual(sp.Poly(sp.diff(G, R), R).degree(), E0-1)

    def test_critical_fiber_inverse_derivatives_and_coefficient_jet_bounds(self):
        T, z, eps, left, right, left_jet, right_jet = sp.symbols(
            "T z eps left right left_jet right_jet")
        c, alpha, lam, lam_d, nu_d, outer_d0 = sp.symbols(
            "c alpha lam lam_d nu_d outer_d0")
        for degrees in self.CHAINS:
            with self.subTest(degrees=degrees):
                n, r = len(degrees), degrees[0]
                A = lambda i, t: self.stage(i, degrees[i-1], t)
                # Choose a concrete critical point of the final polynomial.
                # Its derivative identity is formed before this evaluation.
                outer = z**degrees[-1]+z*z+n
                self.zero(sp.diff(outer, z).subs(z, 0))

                P = {n-1: sp.Integer(0), n-2: T}
                for i in range(n-1, 1, -1):
                    P[i-2] = sp.expand(P[i]+A(i, P[i-1]))
                h = {i: math.prod(degrees[i+1:n-1]) for i in range(n-1)}
                for i in range(n-1):
                    self.assertEqual(sp.Poly(P[i], T).degree(), h[i])
                V_fiber = sp.expand(P[1]+A(1, P[0]))
                M = r*h[0]
                self.assertEqual(sp.Poly(V_fiber, T).degree(), M)
                self.assertGreaterEqual(M, 4)

                # Independent forward recurrence for the ORIGINAL U derivative,
                # evaluated on the already constructed coordinate fiber.
                Uder = {0: sp.Integer(1), 1: -sp.diff(A(1, z), z).subs(z, P[0])}
                for i in range(2, n):
                    Uder[i] = sp.expand(Uder[i-2]
                                        -sp.diff(A(i, z), z).subs(z, P[i-1])*Uder[i-1])
                epsilon0 = (-1)**(n-2)
                self.zero(Uder[n-1]+epsilon0*sp.diff(V_fiber, T))
                self.assertEqual(sp.Poly(Uder[n-1], T).degree(), M-1)

                derivative_polynomials = {}
                for i in range(1, n-1):
                    jets = list(sp.symbols(f"jet{i}_0:{degrees[i-1]+1}"))
                    if i == 1:
                        jets[-1] = sp.Integer(0)  # precisely the first top-jet gate
                    derivative_polynomials[i] = sum(jets[j]*z**j for j in range(degrees[i-1]+1))
                    # Independent dual-number coefficient extraction verifies
                    # the derivative recurrence BEFORE fiber specialization.
                    stage_jet = (left+eps*left_jet-A(i, right+eps*right_jet)
                                 -eps*derivative_polynomials[i].subs(z, right+eps*right_jet))
                    first_order = sp.expand(stage_jet).coeff(eps, 1)
                    expected = (left_jet-derivative_polynomials[i].subs(z, right)
                                -sp.diff(A(i, z), z).subs(z, right)*right_jet)
                    self.zero(first_order-expected)

                Q = {0: -c,
                     1: sp.expand(c*sp.diff(A(1, z), z).subs(z, P[0])
                                  -derivative_polynomials[1].subs(z, P[0]))}
                self.assertLessEqual(sp.Poly(Q[1], T).degree(), M-h[0])
                for i in range(2, n-1):
                    Q[i] = sp.expand(Q[i-2]-derivative_polynomials[i].subs(z, P[i-1])
                                     -sp.diff(A(i, z), z).subs(z, P[i-1])*Q[i-1])
                    self.assertLessEqual(sp.Poly(Q[i], T).degree(), M-h[i-1])
                    self.assertEqual((degrees[i-1]-1)*h[i-1]+M-h[i-2], M-h[i-1])
                    self.assertEqual(degrees[i-1]*h[i-1], h[i-2])
                    self.assertLess(h[i-2]+h[i-1], 2*h[0])
                self.assertLessEqual(sp.Poly(Q[n-2], T).degree(), M-degrees[-2])
                self.assertLessEqual(M-degrees[-2], M-2)
                lhs = outer_d0+lam_d*T+lam*Q[n-2]+nu_d
                rhs = alpha*Uder[n-1]
                self.assertLessEqual(sp.Poly(lhs, T).degree(), max(1, M-2))
                self.assertEqual(sp.Poly(rhs, T).degree(), M-1)
                self.assertEqual(sp.Poly(sp.expand(lhs-rhs), T).degree(), M-1)
                # No equality of these incompatible sides is asserted. This
                # checks finite degree bounds, not the universal theorem.

    def test_length_two_formal_boundary_has_no_critical_degree_gap(self):
        U, V, T, tau, rho = sp.symbols("U V T tau rho")
        K = V-U*U
        phi = K*K-2*tau*U+rho
        psi = K
        self.zero(sp.diff(phi, tau)-sp.diff(psi, U))
        self.zero(sp.diff(phi, rho)-sp.diff(psi, V))
        # A2'(0)=0 and its fiber has U=T,V=T^2. Here n=2, M=2:
        # the surviving lambda_delta*T term and the right side both have
        # degree M-1=1, so the n>=3 contradiction is genuinely unavailable.
        K_U_fiber = sp.diff(K, U).subs({U: T, V: T*T}, simultaneous=True)
        self.zero(K_U_fiber+2*T)
        lhs, rhs = -2*T, K_U_fiber
        self.zero(lhs-rhs)
        self.assertEqual(sp.Poly(lhs, T).degree(), 1)
        self.assertEqual(sp.Poly(rhs, T).degree(), 1)
        self.assertEqual(sp.Poly(T*T, T).degree(), 2)
        # This is a FORMAL differential-field boundary only. The separate154
        # actual-coordinate exclusion is not contradicted by it.


if __name__ == "__main__":
    unittest.main()
