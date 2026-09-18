"""Finite exact-algebra controls for the conditional quartic-conic exclusion241.

The raw eliminant is rebuilt from q=rho**2-t**4 and independent lower jets.
The graph factorization, its actual cofactor hypothesis, the UFD implication,
and the inherited 237/238 geometric reduction remain written proof inputs.
No finite fixture certifies them or an unrestricted cancellation claim.
No retained source, checker, or solver module is imported.
"""

import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, zeta = sp.symbols("U V zeta")
A = sp.Symbol("A", nonzero=True)
B, C, epsilon = sp.symbols("B C epsilon")
K = {(i, j): sp.Symbol(f"k{i}{j}") for i in range(5) for j in range(5-i)}
N = {(i, j): sp.Symbol(f"n{i}{j}") for i in range(4) for j in range(4-i)}
ell, ellt, ellr, m = sp.symbols("ell ellt ellr m")


def clean(expression):
    return sp.cancel(sp.expand(expression))


def coefficient_partial(expression, direction):
    result = sp.diff(expression, (t, rho)[direction])
    for table in (K, N):
        for (i, j), symbol in table.items():
            derivative = sp.diff(expression, symbol)
            if derivative == 0:
                continue
            target = (i+(direction == 0), j+(direction == 1))
            if target not in table:
                raise ValueError("Derivative exceeds the finite jet table")
            result += derivative*table[target]
    return sp.expand(result)


def lower_taylor(table, degree):
    return sum(table[i, degree-i]*U**i*V**(degree-i)
               / (sp.factorial(i)*sp.factorial(degree-i)) for i in range(degree+1))


def raw_centered_eliminant():
    """Literal q Taylor substitution and all four lower potentials."""
    eps = sp.Symbol("eps")
    q = rho**2-t**4
    shifted_q = sp.expand(q.subs({t: t+eps*U, rho: rho+eps*V}, simultaneous=True))
    f = shifted_q.coeff(eps, 2)+lower_taylor(K, 1)+N[0, 0]
    S = shifted_q.coeff(eps, 3)+lower_taylor(K, 2)+lower_taylor(N, 1)
    Q = shifted_q.coeff(eps, 4)+lower_taylor(K, 3)+lower_taylor(N, 2) \
        - ellt*U-ellr*V-m
    R, beta, T = sp.diff(f, V), coefficient_partial(f, 1), ell-S
    H = T**2+R*beta*T+R**2*Q
    centered = sp.Poly(sp.expand(H.subs(V, zeta-K[0, 1]/2)), U, zeta)
    return f, S, Q, R, beta, T, centered


class RepeatedRootQuarticConicControls241(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_six_coefficients_from_the_literal_complete_eliminant(self):
        f, S, Q, R, beta, T, raw = raw_centered_eliminant()
        kappa, c = K[0, 1], K[0, 2]
        self.assertZero(R-2*V-kappa)
        self.assertZero(beta-K[1, 1]*U-c*V-N[0, 1])
        self.assertZero(beta-sp.diff(S, V))
        p = S.subs(V, -kappa/2)-ell
        self.assertZero(p+4*t*U**3-K[2, 0]*U**2/2
                        -(N[1, 0]-kappa*K[1, 1]/2)*U-kappa**2*c/8
                        +kappa*N[0, 1]/2+ell)
        self.assertZero(raw.as_expr().subs(zeta, 0)-p**2)
        self.assertZero(sp.Poly(raw.as_expr(), zeta).coeff_monomial(zeta))
        top = sum(coefficient*U**powers[0]*zeta**powers[1]
                  for powers, coefficient in raw.terms() if sum(powers) == 6)
        self.assertZero(top-16*t**2*U**6+4*U**4*zeta**2)
        expected = {
            (0, 5): 2*K[0, 3]/3,
            (1, 4): 2*K[1, 2],
            (0, 4): 2*N[0, 2]-3*c**2/4-kappa*K[0, 3],
            (2, 3): 2*K[2, 1],
            (1, 3): 4*N[1, 1]-2*c*K[1, 1]-2*kappa*K[1, 2],
            (3, 2): 2*K[3, 0]/3+4*c*t,
        }
        for powers, coefficient in expected.items():
            self.assertZero(raw.coeff_monomial(U**powers[0]*zeta**powers[1])-coefficient)

    def test_graph_center_division_and_the_required_A_squared_denominator(self):
        l1, l0, m1 = sp.symbols("l1 l0 m1")
        P = A*U**2+B*U+C
        linear = l1*U+l0
        M = linear**2+m1*zeta-4*zeta**2/A**2
        model = sp.Poly(sp.expand((zeta-P)**2*M+2*epsilon*zeta*(zeta-P)), U, zeta)
        self.assertZero(model.as_expr().subs(zeta, 0)-(P*linear)**2)
        self.assertZero(sp.Poly(model.as_expr(), zeta).coeff_monomial(zeta)
                        - P*(P*m1-2*linear**2-2*epsilon))
        expected = {(0, 5): 0, (1, 4): 0, (0, 4): -4/A**2,
                    (2, 3): 8/A, (1, 3): 8*B/A**2, (3, 2): -8*B/A}
        for powers, coefficient in expected.items():
            self.assertZero(model.coeff_monomial(U**powers[0]*zeta**powers[1])-coefficient)

        l1sol, l0sol, m1sol = -4*t/A, -2*t*B/A**2, 32*t**2/A**3
        linearsol = l1sol*U+l0sol
        epssol = (C*m1sol-2*l0sol**2)/2
        self.assertZero(P*m1sol-2*linearsol**2-2*epssol)
        self.assertZero(sp.Poly(P*linearsol, U).coeff_monomial(U**3)+4*t)
        self.assertZero(sp.Poly(P*linearsol, U).coeff_monomial(U**2)+6*t*B/A)
        Bcenter = -A*K[2, 0]/(12*t)
        self.assertZero(sp.Poly(P*linearsol, U).coeff_monomial(U**2).subs(B, Bcenter)-K[2, 0]/2)
        leading_M = l1sol**2*U**2-4*zeta**2/A**2
        self.assertZero(leading_M-(16*t**2*U**2-4*zeta**2)/A**2)

        # A repeated P is permitted by the written UFD argument. This fixture
        # checks divisibility arithmetic, not that universal implication itself.
        root = sp.Symbol("root")
        repeated_P = A*(U-root)**2
        repeated_p = repeated_P*(l1sol*U+l0)
        quotient, remainder = sp.div(repeated_p, repeated_P, U)
        self.assertZero(quotient-l1sol*U-l0)
        self.assertZero(remainder)
        self.assertZero(sp.rem(repeated_p**2, repeated_P**2, U))
        self.assertZero(sp.discriminant(repeated_P, U))

        # The discarded denominator is a genuine error, masked by setting A=1.
        actual = model.coeff_monomial(U*zeta**3)
        wrong = 8*B/A
        self.assertZero(actual-wrong-8*B*(1-A)/A**2)
        self.assertNotEqual(clean(actual-wrong), 0)
        self.assertZero((actual-wrong).subs(A, 1))

    def test_differentiated_jet_gates_and_exact_incompatibility(self):
        _, _, _, _, _, _, raw = raw_centered_eliminant()
        c, Djet, Dtjet = K[0, 2], K[2, 1], K[3, 1]
        zeros = {K[0, 3]: 0, K[1, 2]: 0, K[2, 2]: 0}
        self.assertEqual(coefficient_partial(c, 0), K[1, 2])
        self.assertEqual(coefficient_partial(c, 1), K[0, 3])
        self.assertEqual(coefficient_partial(Djet, 1), coefficient_partial(K[1, 2], 0))
        self.assertZero(coefficient_partial(4/Djet, 1).subs(zeros))
        self.assertZero((raw.coeff_monomial(zeta**4)+4/A**2).subs(
            {**zeros, N[0, 2]: 3*c**2/8-2/A**2}, simultaneous=True))
        self.assertZero((raw.coeff_monomial(U**2*zeta**3)-8/A).subs(Djet, 4/A))

        Bcenter = -A*K[2, 0]/(12*t)
        Bhigh = -A*K[3, 0]/12-A*c*t/2
        self.assertZero(raw.coeff_monomial(U**3*zeta**2)+8*Bhigh/A)
        relation = K[3, 0]-K[2, 0]/t+6*c*t
        self.assertZero(Bhigh-Bcenter+A*relation/12)
        first_derivative = coefficient_partial(relation, 1).subs(zeros)
        self.assertZero(first_derivative-Dtjet+Djet/t)

        # A_rho=0 was established above. Only now may this rho derivative
        # treat the independent symbol A as fixed.
        fifth_row = 4*N[1, 1]-2*c*K[1, 1]+2*K[2, 0]/(3*A*t)
        self.assertZero(8*Bcenter/A**2+2*K[2, 0]/(3*A*t))
        fifth_derivative = coefficient_partial(fifth_row, 1).subs(zeros)
        self.assertZero(fifth_derivative-4*N[1, 2]-2*Djet/(3*A*t))
        nrr = 3*c**2/8-Djet**2/8
        self.assertZero(nrr-(3*c**2/8-2/A**2).subs(A, 4/Djet))
        nrr_t = coefficient_partial(nrr, 0).subs(zeros)
        self.assertZero(4*nrr_t+Djet*Dtjet)
        second_derivative = fifth_derivative.subs(N[1, 2], nrr_t).subs(A, 4/Djet)
        self.assertZero(second_derivative+Djet*(Dtjet-Djet/(6*t)))

        D = sp.Symbol("D", nonzero=True)
        Dt = sp.Symbol("Dt")
        first = first_derivative.subs({Djet: D, Dtjet: Dt}, simultaneous=True)
        second = clean((-second_derivative/Djet).subs({Djet: D, Dtjet: Dt}, simultaneous=True))
        self.assertZero(first-Dt+D/t)
        self.assertZero(second-Dt+D/(6*t))
        self.assertZero(second-first-5*D/(6*t))
        incompatible = sp.resultant(t*first, 6*t*second, Dt)
        self.assertZero(incompatible-5*t*D)
        self.assertZero(incompatible/(5*t*D)-1)
        self.assertNotEqual(incompatible, 0)


if __name__ == "__main__":
    unittest.main()
