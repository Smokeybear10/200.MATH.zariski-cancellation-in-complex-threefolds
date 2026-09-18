"""Bounded exact algebra for the polynomial-radical centered eliminant239.

All lower jets remain symbolic.  These controls rebuild the Taylor potentials,
check the complete centered polynomial, and distinguish several invalid
shortcuts.  They do not prove the actual chart, LND or field-return assertions,
normality, a cofactor theorem, recognition, or nonrealizability.  The last
nodal fixture is expressly NOT an actual Taylor chart.  No 237/238 endpoint,
retained checker, proof file, or solver module is imported or certified.
"""

import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, eta, w, v = sp.symbols("U V eta w v")
K = {(i, j): sp.Symbol(f"k{i}{j}") for i in range(4) for j in range(4-i)}
N = {(i, j): sp.Symbol(f"n{i}{j}") for i in range(3) for j in range(3-i)}
L = {(i, j): sp.Symbol(f"ell{i}{j}") for i in range(2) for j in range(2-i)}
m = sp.Symbol("m")


def clean(expression):
    return sp.cancel(sp.expand(expression))


def coefficient_partial(expression, direction):
    """The original coefficient partial, fixing formal U,V,eta and w."""
    result = sp.diff(expression, (t, rho)[direction])
    for table in (K, N, L):
        for (i, j), symbol in table.items():
            derivative = sp.diff(expression, symbol)
            if derivative == 0:
                continue
            target = (i + (direction == 0), j + (direction == 1))
            if target not in table:
                raise ValueError("The finite jet table is too short for this derivative")
            result += derivative*table[target]
    return sp.expand(result)


def divided_jet(table, degree):
    return sum(table[i, degree-i]*U**i*V**(degree-i)
               / (sp.factorial(i)*sp.factorial(degree-i)) for i in range(degree+1))


def raw_potentials(g):
    """Rebuild q jets by a literal two-variable substitution."""
    eps = sp.Symbol("eps")
    q = rho**2 - g
    shifted = sp.expand(q.subs({t: t+eps*U, rho: rho+eps*V}, simultaneous=True))
    qjets = [shifted.coeff(eps, degree) for degree in range(5)]
    f = qjets[2] + divided_jet(K, 1) + N[0, 0]
    S = qjets[3] + divided_jet(K, 2) + divided_jet(N, 1)
    Q = qjets[4] + divided_jet(K, 3) + divided_jet(N, 2) \
        - L[1, 0]*U - L[0, 1]*V - m
    R = sp.diff(f, V)
    beta = coefficient_partial(f, 1)
    T = L[0, 0] - S
    H = sp.expand(T**2 + R*beta*T + R**2*Q)
    return q, qjets, f, S, Q, R, beta, T, H


def centered_components(g):
    """The displayed center data, separately entered for comparison."""
    kappa, c = K[0, 1], K[0, 2]
    B = K[1, 1]*U + N[0, 1] - kappa*c/2
    p = -sp.diff(g, t, 3)*U**3/6 + K[2, 0]*U**2/2 \
        + (N[1, 0]-kappa*K[1, 1]/2)*U \
        + kappa**2*c/8 - kappa*N[0, 1]/2 - L[0, 0]
    Q0 = -sp.diff(g, t, 4)*U**4/24 + K[3, 0]*U**3/6 \
        + (N[2, 0]/2-kappa*K[2, 1]/4)*U**2 \
        + (kappa**2*K[1, 2]/8-kappa*N[1, 1]/2-L[1, 0])*U \
        - kappa**3*K[0, 3]/48 + kappa**2*N[0, 2]/8 + kappa*L[0, 1]/2 - m
    Q1 = K[2, 1]*U**2/2 + (N[1, 1]-kappa*K[1, 2]/2)*U \
        + kappa**2*K[0, 3]/8 - kappa*N[0, 2]/2 - L[0, 1]
    Q2 = (K[1, 2]*U+N[0, 2])/2 - kappa*K[0, 3]/4
    Q3 = K[0, 3]/6
    return kappa, c, B, p, (Q0, Q1, Q2, Q3)


def homogeneous_part(expression, degree):
    polynomial = sp.Poly(sp.expand(expression), U, V)
    return sum(coefficient*U**powers[0]*V**powers[1]
               for powers, coefficient in polynomial.terms() if sum(powers) == degree)


class PolynomialRadicalCenterControls239(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_raw_taylor_potentials_and_centered_coefficient_chain_rules(self):
        for g in (t**3, t**4):
            q, jets, f, S, Q, R, beta, T, H = raw_potentials(g)
            self.assertZero(sp.diff(q, rho, 2)-2)
            self.assertZero(jets[1] + sp.diff(g, t)*U - 2*rho*V)
            self.assertZero(jets[2] - V**2 + sp.diff(g, t, 2)*U**2/2)
            self.assertZero(jets[3] + sp.diff(g, t, 3)*U**3/6)
            self.assertZero(jets[4] + sp.diff(g, t, 4)*U**4/24)
            self.assertZero(R - 2*V - K[0, 1])
            self.assertZero(beta - K[1, 1]*U - K[0, 2]*V - N[0, 1])
            self.assertZero(sp.diff(S, U)-coefficient_partial(f, 0))
            self.assertZero(sp.diff(S, V)-coefficient_partial(f, 1))
            self.assertZero(sp.diff(Q, U)-coefficient_partial(S, 0)+L[1, 0])
            self.assertZero(sp.diff(Q, V)-coefficient_partial(S, 1)+L[0, 1])
            self.assertNotEqual(clean(beta-R), 0)

            centered_S = S.subs(V, eta-K[0, 1]/2)
            centered_beta = beta.subs(V, eta-K[0, 1]/2)
            for direction, shift_derivative in ((0, K[1, 1]), (1, K[0, 2])):
                original_then_shift = coefficient_partial(S, direction).subs(V, eta-K[0, 1]/2)
                centered_then_differentiate = coefficient_partial(centered_S, direction)
                self.assertZero(centered_then_differentiate-original_then_shift
                                + shift_derivative*centered_beta/2)
                # Omitting the coefficient-dependent shift is generically wrong.
                self.assertNotEqual(clean(centered_then_differentiate-original_then_shift), 0)

    def test_complete_center_division_and_every_eliminant_coefficient(self):
        for g in (t**3, t**4):
            q, jets, f, S, Q, R, beta, T, H = raw_potentials(g)
            kappa, c, B, p, qparts = centered_components(g)
            Q0, Q1, Q2, Q3 = qparts
            shift = {V: eta-kappa/2}
            self.assertZero(R.subs(shift)-2*eta)
            self.assertZero(S.subs(V, -kappa/2)-L[0, 0]-p)
            self.assertEqual(sp.degree(p, U), 3)
            self.assertZero(S.subs(shift)-L[0, 0]-p-B*eta-c*eta**2/2)
            self.assertZero(beta.subs(shift)-B-c*eta)
            self.assertZero(Q.subs(shift)-sum(qparts[j]*eta**j for j in range(4)))

            D = -K[1, 1]*U/2-N[0, 1]/2-c*V/4+c*kappa/8
            self.assertZero(D+B/2+c*R/8)
            self.assertZero(S-L[0, 0]-p+R*D)
            self.assertLessEqual(sp.Poly(D, U, V).total_degree(), 1)
            coefficients = [p**2, 0, 4*Q0-B**2-c*p,
                            4*Q1-2*c*B, 4*Q2-3*c**2/4, 4*Q3]
            centered_H = sp.Poly(sp.expand(H.subs(shift)), eta)
            self.assertEqual(centered_H.degree(), 5)
            for power, coefficient in enumerate(coefficients):
                self.assertZero(centered_H.coeff_monomial(eta**power)-coefficient)
            self.assertZero(H.subs(V, -kappa/2)-p**2)
            # Without the monic w² term the center vanishes, losing p² entirely.
            missing_monic = R*beta*T+R**2*Q
            self.assertZero(missing_monic.subs(V, -kappa/2))
            self.assertNotEqual(clean((H-missing_monic).subs(V, -kappa/2)), 0)

    def test_full_top_parts_and_the_old_quadratic_center_boundary(self):
        for g in (t**3, t**4):
            q, jets, f, S, Q, R, beta, T, H = raw_potentials(g)
            kappa, c, B, p, qparts = centered_components(g)
            g3, g4 = sp.diff(g, t, 3), sp.diff(g, t, 4)
            top6 = g3**2*U**6/36-g4*U**4*V**2/6
            top5 = (-kappa*g4*U**4*V-g3*K[2, 0]*U**5
                    +(c*g3+4*K[3, 0])*U**3*V**2+12*K[2, 1]*U**2*V**3
                    +12*K[1, 2]*U*V**4+4*K[0, 3]*V**5)/6
            self.assertZero(homogeneous_part(H, 6)-top6)
            self.assertZero(homogeneous_part(H, 5)-top5)
            self.assertEqual(sp.Poly(H, U, V).total_degree(), 6)
            self.assertEqual(sp.degree(H, U), 6)
            self.assertEqual(sp.degree(H, V), 5)  # Generic independent k03 is retained.
            self.assertZero(sp.Poly(H, U).coeff_monomial(U**6)-g3**2/36)
            self.assertZero(sp.Poly(H, V).coeff_monomial(V**5)-2*K[0, 3]/3)
            expected = U**6 if g == t**3 else 4*U**4*(4*t**2*U**2-V**2)
            self.assertZero(top6-expected)
            old_quadratic_center = p+g3*U**3/6
            self.assertEqual(sp.degree(old_quadratic_center, U), 2)
            self.assertNotEqual(clean(S.subs(V, -kappa/2)-L[0, 0]-old_quadratic_center), 0)

        # Setting g=0 really does recover the older degree-five/two-center boundary.
        _, _, _, S0, _, _, _, _, H0 = raw_potentials(sp.Integer(0))
        self.assertEqual(sp.Poly(H0, U, V).total_degree(), 5)
        self.assertEqual(sp.degree(S0.subs(V, -K[0, 1]/2)-L[0, 0], U), 2)
        self.assertZero(homogeneous_part(H0, 5)-4*V**2*divided_jet(K, 3))

    def test_undivided_potential_identity_and_nonactual_normality_countercontrol(self):
        for g in (t**3, t**4):
            q, jets, f, S, Q, R, beta, T, H = raw_potentials(g)
            first = R*w+S-L[0, 0]
            fourth = w**2+beta*w+Q
            self.assertZero(R**2*fourth-H-first*(R*w+T+R*beta))
            # The exact identity is polynomial even at the formal divisor R=0.
            self.assertZero((R**2*fourth-H).subs(V, -K[0, 1]/2)
                            + (S.subs(V, -K[0, 1]/2)-L[0, 0])**2)

        # A cubic center and a monic module relation alone do not force normality.
        # This nodal fixture deliberately violates the actual Taylor degree bounds.
        rr = v**2-1
        y, theta = v*rr, rr/2
        correction = U*(2*V)*(2*V+1)
        wfixture = -v+correction.subs({U: y, V: theta}, simultaneous=True)
        pfixture = U-U**3
        self.assertZero(rr*wfixture+pfixture.subs(U, y))
        self.assertZero(wfixture**2-2*correction.subs({U: y, V: theta}, simultaneous=True)*wfixture
                        + (correction**2-(2*V+1)).subs({U: y, V: theta}, simultaneous=True))
        self.assertZero(correction.subs({U: y, V: theta}, simultaneous=True)-wfixture-v)
        self.assertEqual(y.subs(v, 1), y.subs(v, -1))
        self.assertEqual(theta.subs(v, 1), theta.subs(v, -1))
        self.assertNotEqual(wfixture.subs(v, 1), wfixture.subs(v, -1))
        self.assertEqual(sp.Poly(pfixture, U).degree(), 3)
        self.assertEqual(sp.Poly(-2*correction, U, V).total_degree(), 3)
        self.assertEqual(sp.Poly(correction**2-(2*V+1), U, V).total_degree(), 6)
        # Actual beta has degree at most one and actual Q at most four.


if __name__ == "__main__":
    unittest.main()
