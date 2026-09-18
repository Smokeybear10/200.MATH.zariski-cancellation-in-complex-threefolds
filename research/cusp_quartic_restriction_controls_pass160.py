"""Independent finite exact controls for the nongraph cusp restriction160.

The first two methods use formal coefficient jets and necessary equations.
They do not realize an actual four-coordinate cusp frame, prove the generic
degree exhaustion, or replace the finite-field constant argument in the note.
The third method is an actual plane automorphism over its coefficient field,
not a descent of that map to the original four-variable polynomial ring.

Read alongside cusp-nongraph-quartic-restriction-pass160-working.md. No solver
or previous checker is imported. All rational identities below are cleared
by explicitly known nonzero coefficient denominators before comparison.
"""

import unittest

import sympy as sp


class CuspQuarticRestrictionControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_potential_and_nested_square_coefficients(self):
        U, V = sp.symbols("U V")
        r, r1 = sp.symbols("r r1", nonzero=True)
        r2, r3, K2, K3 = sp.symbols("r2 r3 K2 K3")
        nt, nr, ntt, nr1 = sp.symbols("nt nr ntt nr1")
        N = sp.symbols("N", nonzero=True)
        N1, ell, ellt, ellr = sp.symbols("N1 ell ellt ellr")

        # r = k_rho, r_rho = 0. These are independent commuting coefficient
        # jets, not assigned polynomial source coordinates or a unit Jacobian.
        f = U**3 + K2 * U**2 / 2 + r1 * U * V + nt * U + nr * V
        H3k_H2n = (
            K3 * U**3 / 6 + r2 * U**2 * V / 2
            + ntt * U**2 / 2 + nr1 * U * V + N * V**2 / 2
        )
        phi = sp.expand(
            sp.diff(f, V) * (ell - f) / r
            + H3k_H2n - ellt * U - ellr * V
        )
        delta = r2 / 2 - r1**2 / r
        b1 = nr1 - 2 * r1 * nr / r
        b0 = -nr**2 / r - ellr
        B = delta * U**2 + b1 * U + b0
        C = phi.subs(V, 0)
        c4 = -r1 / r
        c3 = K3 / 6 - r1 * K2 / (2 * r) - nr / r

        self.assertEqual(sp.Poly(phi, V).degree(), 2)
        self.assertEqual(sp.Poly(phi, U, V).total_degree(), 4)
        self.assert_zero(phi.coeff(V, 2) - N / 2)
        self.assert_zero(r * (phi.coeff(V, 1) - B))
        self.assert_zero(r * (C.coeff(U, 4) - c4))
        self.assert_zero(r * (C.coeff(U, 3) - c3))
        self.assert_zero(r * (phi - N * V**2 / 2 - B * V - C))

        # Completion of the V-square is literal, without treating any of its
        # field coefficients as constants for the coefficient derivations.
        square_residual = sp.expand(C - B**2 / (2 * N))
        self.assert_zero(
            2 * N * r**2
            * (square_residual.coeff(U, 4) - c4 + delta**2 / (2 * N))
        )
        self.assert_zero(
            N * r**2
            * (square_residual.coeff(U, 3) - c3 + delta * b1 / N)
        )
        N_forced = -r * delta**2 / (2 * r1)
        self.assert_zero(r**2 * (2 * N_forced * c4 - delta**2))

        # Differentiate the extracted cubic identity independently in rho.
        # k_tt,rho=r'', k_ttt,rho=r''', n_rho,rho=N, and
        # n_tau,rho,rho=N'. The first square identity makes N_rho=0.
        cubic_equation = c3 - delta * b1 / N
        rho_derivative = (
            r2 * sp.diff(cubic_equation, K2)
            + r3 * sp.diff(cubic_equation, K3)
            + N * sp.diff(cubic_equation, nr)
            + N1 * sp.diff(cubic_equation, nr1)
        )
        expected = (
            r3 / 6 - r1 * r2 / (2 * r) - N / r
            - delta * (N1 - 2 * r1 * N / r) / N
        )
        self.assert_zero(N * r**2 * (rho_derivative - expected))
        # These U^4/U^3 identities do not impose the remaining U^2 identity
        # or the required nonzero affine coefficient of the completed square.

    def test_rational_jet_ode_reciprocal_and_fifth_power(self):
        r, r1 = sp.symbols("r r1", nonzero=True)
        r2, r3, N, N1 = sp.symbols("r2 r3 N N1")

        def dt(expression):
            return (
                r1 * sp.diff(expression, r)
                + r2 * sp.diff(expression, r1)
                + r3 * sp.diff(expression, r2)
            )

        delta = r2 / 2 - r1**2 / r
        N_forced = -r * delta**2 / (2 * r1)
        N_derivative = dt(N_forced)
        # The rho equation is first multiplied by N. Its substitution uses
        # direct jet differentiation of N, independently of a logarithm rule.
        compatibility = (
            N * (r3 / 6 - r1 * r2 / (2 * r) - N / r)
            - delta * (N1 - 2 * r1 * N / r)
        )
        substituted = compatibility.subs(
            {N: N_forced, N1: N_derivative}, simultaneous=True
        )
        ode = (
            4 * r1 * r3 - 12 * r1**2 * r2 / r
            + 12 * r1**4 / r**2 - 3 * r2**2
        )
        self.assert_zero(
            r**3 * (48 * r1**2 * substituted - 5 * r * delta**2 * ode)
        )
        residual = (
            r3 / 6 - r1 * r2 / (2 * r) + delta**2 / (2 * r1)
            - 2 * dt(delta) + delta * r2 / r1 + delta * r1 / r
        )
        self.assert_zero(r**2 * (24 * r1 * residual + 5 * ode))

        chi = 1 / r
        chi1, chi2 = dt(chi), dt(dt(chi))
        chi3 = dt(chi2)
        reciprocal_ode = 4 * chi1 * chi3 - 3 * chi2**2
        self.assert_zero(r**6 * reciprocal_ode - r**2 * ode)
        self.assert_zero(r**3 * (2 * chi**2 * delta + chi2))

        # A fourth-root adjunction is algebraic, not a rational-generator
        # assumption. Only its derivative identity is checked here. The joint
        # constant-field and integration claims require the written proof.
        h0, h1, h2 = sp.symbols("h0 h1 h2")
        root_chi1 = h0**4
        root_chi2 = 4 * h0**3 * h1
        root_chi3 = 12 * h0**2 * h1**2 + 4 * h0**3 * h2
        self.assert_zero(
            4 * root_chi1 * root_chi3 - 3 * root_chi2**2 - 16 * h0**7 * h2
        )

        tau, C0, C2 = sp.symbols("tau C0 C2")
        C1 = sp.symbols("C1", nonzero=True)
        s = tau - C2
        family = C0 + C1 * s**5
        q1, q2, q3 = [sp.diff(family, tau, j) for j in (1, 2, 3)]
        self.assert_zero(4 * q1 * q3 - 3 * q2**2)
        self.assertNotEqual(sp.expand(q1), 0)
        self.assertNotEqual(sp.expand(q2), 0)

        # If r=1/chi, these are the numerators of r',r'',r''' with
        # denominators chi^2,chi^3,chi^4. This avoids rational gcd expansion.
        R1 = -q1
        R2 = 2 * q1**2 - family * q2
        R3 = -6 * q1**3 + 6 * family * q1 * q2 - family**2 * q3
        ode_numerator = (
            4 * R1 * R3 - 12 * R1**2 * R2 + 12 * R1**4 - 3 * R2**2
        )
        self.assert_zero(ode_numerator)
        # N=chi''^2/(8 chi^3 chi')=10 C1 s^2/chi^3.
        self.assert_zero(q2**2 - 8 * q1 * 10 * C1 * s**2)
        self.assert_zero(ode_numerator.subs(C0, 0))
        self.assert_zero((q2**2 - 80 * q1 * C1 * s**2).subs(C0, 0))

        A = sp.symbols("A", nonzero=True)
        B = sp.symbols("B")
        linear_chi = A * tau + B
        linear_q1 = sp.diff(linear_chi, tau)
        linear_q2 = sp.diff(linear_chi, tau, 2)
        self.assert_zero(
            4 * linear_q1 * sp.diff(linear_chi, tau, 3) - 3 * linear_q2**2
        )
        self.assertNotEqual(linear_q1, 0)
        self.assertEqual(linear_q2, 0)
        # Delta=-chi''/(2 chi^2) therefore vanishes: an ODE solution need
        # not satisfy the nongraph quartic premise Delta != 0.
        self.assert_zero(-linear_q2)

    def test_abstract_two_four_embedding_and_degree_lowering_inverse(self):
        U, V, t, R, S = sp.symbols("U V t R S")
        A, C, q2 = sp.symbols("A C q2", nonzero=True)
        B, q1, q0 = sp.symbols("B q1 q0")

        def Q(argument):
            return q2 * argument**2 + q1 * argument + q0

        y = A * t**2 + B
        theta = Q(y) + C * t
        self.assertEqual(sp.Poly(y, t).degree(), 2)
        self.assertEqual(sp.Poly(theta, t).degree(), 4)
        self.assert_zero(theta - Q(y) - C * t)

        parameter = (V - Q(U)) / C
        relation_coordinate = U - A * parameter**2 - B
        inverse_U = R + A * S**2 + B
        inverse_V = Q(inverse_U) + C * S
        forward = {U: inverse_U, V: inverse_V}
        backward = {R: relation_coordinate, S: parameter}
        self.assert_zero(C**2 * (
            relation_coordinate.subs(forward, simultaneous=True) - R
        ))
        self.assert_zero(C * (parameter.subs(forward, simultaneous=True) - S))
        self.assert_zero(C**2 * (
            inverse_U.subs(backward, simultaneous=True) - U
        ))
        self.assert_zero(C**4 * (
            inverse_V.subs(backward, simultaneous=True) - V
        ))
        jacobian = sp.Matrix([relation_coordinate, parameter]).jacobian([U, V])
        self.assert_zero(C * jacobian.det() - 1)

        G = (V - Q(U))**2 - C**2 * (U - B) / A
        self.assert_zero(A * G.subs({U: y, V: theta}, simultaneous=True))
        self.assert_zero(A * G + C**2 * relation_coordinate)
        self.assertEqual(sp.Poly(G, U, V).total_degree(), 4)
        self.assert_zero(sp.expand(G).coeff(U, 4) - q2**2)
        self.assert_zero(
            A * (sp.diff(G, U) + sp.diff(Q(U), U) * sp.diff(G, V)) + C**2
        )
        # The inverse sends the curve R=0 to (y,theta), and its other
        # coordinate restricts to t. This is a plane embedding over the
        # coefficient field only, with no assigned cusp coefficient partials.
        self.assert_zero(inverse_U.subs({R: 0, S: t}, simultaneous=True) - y)
        self.assert_zero(inverse_V.subs({R: 0, S: t}, simultaneous=True) - theta)


if __name__ == "__main__":
    unittest.main()
