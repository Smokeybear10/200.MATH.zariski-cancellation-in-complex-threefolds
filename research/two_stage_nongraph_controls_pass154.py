"""Finite exact controls for the fixed-axis two-stage candidate154.

The first method checks genuine polynomial coordinate maps and both inverse
orders for three complex outer polynomials of degrees 2,3,4, with every lower
coefficient nonzero. Divided differences are constructed as polynomials;
the original coordinate x is never inverted, including at x=0.

The remaining methods concern separately specified formal coefficient charts
and finite coefficient identities. They do NOT supply an actual dense sliced
frame. No finite check proves canonical coefficient return, Gauss descent,
the universal odd-valuation argument, or exhaustion at any minimum degree.
No earlier checker, solver, or search implementation is imported.
"""

import math
import unittest

import sympy as sp


class TwoStageNongraphControls(unittest.TestCase):
    def zero(self, expression):
        # Denominators below are only powers of named nonzero constant alpha,
        # or Laurent powers of eps that are explicitly cleared before use.
        # No generic rational gcd or source-coordinate localization is used.
        self.assertEqual(sp.expand(expression), 0)

    def zeros(self, expressions):
        for expression in expressions:
            self.zero(expression)

    @staticmethod
    def outer(t, degree):
        return sum((j+1)*t**j for j in range(degree+1))

    @staticmethod
    def divided_shift(t, step, x, degree):
        # (B(t+x*step)-B(t))/x, constructed without division by x.
        return sum((j+1)*math.comb(j, k)*t**(j-k)*x**(k-1)*step**k
                   for j in range(1, degree+1) for k in range(1, j+1))

    def test_generalized_nagata_polynomial_inverse_orders(self):
        x, Y, Z, R, W, r, J, h = sp.symbols("x Y Z R W r J h")
        alpha = sp.symbols("alpha", nonzero=True)
        a, b0, d0, l0, n0 = sp.symbols("a b0 d0 l0 n0")
        L0 = l0*Y+n0
        A0 = a*Y*Y+b0*Y+d0
        self.zeros(((Z-A0)+A0-Z, (R+A0)-A0-R))
        for q in (2, 3, 4):
            with self.subTest(outer_degree=q):
                B = lambda t: self.outer(t, q)
                dd = lambda t, step: self.divided_shift(t, step, x, q)
                shift = sp.expand(dd(R, h))
                self.assertTrue(all(power[0] >= 0
                                    for power, _ in sp.Poly(shift, x).terms()))
                self.zero(x*shift-(B(R+x*h)-B(R)))
                self.zero(dd(R, h)+dd(R+x*h, -h))

                H = x*W+B(R)+L0
                rf = R+x*H/alpha
                Jf = W-dd(R, H/alpha)
                Hf = sp.expand(x*Jf+B(rf)+L0)
                self.zero(Hf-H)
                # Apply the negative-flow inverse to the actual forward map.
                self.zeros((rf-x*Hf/alpha-R,
                            Jf-dd(rf, -Hf/alpha)-W))

                Hi = x*J+B(r)+L0
                Ri = r-x*Hi/alpha
                Wi = J-dd(r, -Hi/alpha)
                Hback = sp.expand(x*Wi+B(Ri)+L0)
                self.zero(Hback-Hi)
                # Apply the forward flow to the independent inverse variables.
                self.zeros((Ri+x*Hback/alpha-r,
                            Wi-dd(Ri, Hback/alpha)-J))

                # These polynomial formulas remain defined at the divisor x=0.
                self.zeros((rf.subs(x, 0)-R,
                            Jf.subs(x, 0)
                            -(W-sp.diff(B(R), R)*(B(R)+L0)/alpha)))
                Delta = lambda f: x*sp.diff(f, R)-sp.diff(B(R), R)*sp.diff(f, W)
                self.zero(Delta(H))
                iterate = W
                for _ in range(q):
                    iterate = sp.expand(Delta(iterate))
                self.zero(iterate+x**(q-1)*sp.diff(B(R), R, q))
                self.assertNotEqual(iterate, 0)
                self.zero(Delta(iterate))
                # Together with R=Z-A0(Y), this is an actual four-coordinate
                # automorphism. No E-action or dense three-good profile is
                # inferred from that fact alone.

    def test_independent_taylor_tails_and_exact_laurent_integrality(self):
        U, V, tau, rho, eps, zeta = sp.symbols("U V tau rho eps zeta")
        a, alpha = sp.symbols("a alpha", nonzero=True)
        b0, d0, l0, n0 = sp.symbols("b0 d0 l0 n0")
        A0 = lambda t: a*t*t+b0*t+d0

        def homogeneous_taylor(f, degree):
            return sp.expand(sum(
                sp.diff(f, tau, i, rho, degree-i)*U**i*V**(degree-i)
                /(math.factorial(i)*math.factorial(degree-i))
                for i in range(degree+1)))

        for q in (2, 3, 4):
            with self.subTest(outer_degree=q):
                B = lambda t: self.outer(t, q)
                d, m = 2*q, 2*q-1
                C = sp.expand(B(V-A0(U))+l0*U+n0)
                pieces = {k: sp.Integer(0) for k in range(d+1)}
                for (i, j), coefficient in sp.Poly(C, U, V).terms():
                    pieces[i+j] += coefficient*U**i*V**j
                self.zero(sum(pieces.values())-C)
                to_coefficients = {U: tau, V: rho}
                fs = {j: -pieces[j+1].subs(to_coefficients, simultaneous=True)
                      for j in range(1, m+1)}
                fs[0] = -pieces[1].subs(to_coefficients, simultaneous=True)+a*alpha*tau*tau
                f_minus = -pieces[0]-alpha*rho+alpha*b0*tau
                first = -sum(homogeneous_taylor(fs[j], j+1) for j in range(m+1))
                phi = sp.expand(first-f_minus)
                psi = sp.expand(-sum(homogeneous_taylor(fs[j], j+2)
                                     for j in range(m+1))-homogeneous_taylor(f_minus, 1))
                self.zeros((phi-C-alpha*(rho-tau*sp.diff(A0(U), U)),
                            psi-alpha*(V-a*U*U-b0*U),
                            sp.diff(psi, U)-sp.diff(phi, tau),
                            sp.diff(psi, V)-sp.diff(phi, rho)))
                gamma = -(q+1)*(-a)**q
                self.zero(fs[m]-gamma*tau**d)
                self.assertEqual(sp.Poly(phi, U, V).total_degree(), d)
                self.zero(sp.Poly(phi, U, V).coeff_monomial(U**d)+gamma)

                # This is the common formal Laurent source, not a four-frame
                # or a choice of a realized component. All coefficient
                # derivatives above were taken before these substitutions.
                x, Y, Z = 1/eps, tau/eps, rho/eps
                W = sum(fs[j]/eps**j for j in range(m+1))+f_minus*eps+eps**2*zeta
                R0 = Z-A0(Y)
                H = sp.expand(x*W+B(R0)+l0*Y+n0)
                expected_H = a*alpha*tau*tau/eps+alpha*b0*tau-alpha*rho+eps*zeta
                self.zero(eps**d*(H-expected_H))
                Hshift = sp.Poly(sp.expand(eps**d*H), eps)
                self.zeros(Hshift.coeff_monomial(eps**j) for j in range(d-1))
                self.zero(Hshift.coeff_monomial(eps**(d-1))-a*alpha*tau*tau)
                I = sp.expand(x*H+alpha*R0)
                self.zero(I-zeta+alpha*d0)
                self.assertEqual(sp.Poly(I, eps).degree(), 0)
                self.zero(R0+x*H/alpha-(zeta/alpha-d0))
                # Inferring EI=0 requires the selected actual Gauss theorem.
                # The finite formal identities themselves do not provide it.

    def test_centered_gradient_signs_and_higher_inner_degree_obstruction(self):
        U, V, R = sp.symbols("U V R")
        alpha, kappa = sp.symbols("alpha kappa", nonzero=True)
        c, beta, ell, n, b1 = sp.symbols("c beta ell n b1")
        a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3")
        at = sp.symbols("at0:4")
        ar = sp.symbols("ar0:4")
        kt, kr, bt, br, lt, lr, nt, nr = sp.symbols("kt kr bt br lt lr nt nr")
        A = a0+a1*U+a2*U**2+a3*U**3
        At = sum(at[i]*U**i for i in range(4))
        Ar = sum(ar[i]*U**i for i in range(4))
        residual = V-A
        B = lambda t: kappa*t**3+b1*t  # centered: no quadratic or constant term
        phi = B(residual)+ell*U+n
        psi = alpha*residual+beta+c*phi
        parameters = (kappa, b1, a0, a1, a2, a3, ell, n)
        tau_jets = (kt, bt, *at, lt, nt)
        rho_jets = (kr, br, *ar, lr, nr)
        phi_tau = sum(sp.diff(phi, p)*jet for p, jet in zip(parameters, tau_jets))
        phi_rho = sum(sp.diff(phi, p)*jet for p, jet in zip(parameters, rho_jets))
        tau_residual = sp.expand((phi_tau-sp.diff(psi, U)).subs(V, R+A))
        rho_residual = sp.expand((phi_rho-sp.diff(psi, V)).subs(V, R+A))
        Bprime = sp.diff(B(R), R)
        expected_tau = kt*R**3+bt*R+Bprime*(c*sp.diff(A, U)-At)+lt*U+nt+alpha*sp.diff(A, U)-c*ell
        expected_rho = kr*R**3+br*R+Bprime*(-Ar-c)+lr*U+nr-alpha
        self.zeros((tau_residual-expected_tau, rho_residual-expected_rho))
        self.zeros((sp.Poly(tau_residual, R).coeff_monomial(R**3)-kt,
                    sp.Poly(rho_residual, R).coeff_monomial(R**3)-kr,
                    sp.Poly(tau_residual, R).coeff_monomial(R**2)
                    -3*kappa*(c*sp.diff(A, U)-At),
                    sp.Poly(rho_residual, R).coeff_monomial(R**2)+3*kappa*(Ar+c)))

        leading = sp.symbols("leading", nonzero=True)
        for inner_degree in (3, 4, 5):
            inner = leading*U**inner_degree+sum((j+1)*U**j for j in range(inner_degree))
            # Once the centered positive-R coefficients are zero, the
            # remaining tau identity is this polynomial in the fixed U.
            reduced = lt*U+nt-c*ell+alpha*sp.diff(inner, U)
            self.assertEqual(sp.Poly(reduced, U).degree(), inner_degree-1)
            self.zero(sp.Poly(reduced, U).coeff_monomial(U**(inner_degree-1))
                      -alpha*inner_degree*leading)
            self.assertNotEqual(alpha*inner_degree*leading, 0)

        a, s, t, J, l0 = sp.symbols("a s t J l0")
        quadratic_constraint = alpha*a*t*t-l0*s*t-J*s*s
        square_difference = (2*alpha*a*t-l0*s)**2-(l0*l0+4*alpha*a*J)*s*s
        self.zero(square_difference-4*alpha*a*quadratic_constraint)
        # This is only the final discriminant algebra. Its prime-coordinate
        # interpretation and odd valuation require the actual proof premises.


if __name__ == "__main__":
    unittest.main()
