"""Finite exact-algebra controls for the saved distinct-root reduction235.

These checks independently reconstruct Taylor coefficients in the quadratic
field q**2 = t*rho - a - b*t**4, its full leading sextic, and bounded formal
degree/characteristic-polynomial fixtures.  They do not prove actual return,
the calibrated Jacobian, cofactor divisibility, the general plane-degree
lemma, existence/nonexistence of actual frames, or a cancellation theorem.
The degree fixtures are formal polynomial pairs, not asserted actual charts.
No retained proof, checker, or solver module is imported.
"""

import unittest

import sympy as sp


t, rho, q = sp.symbols("t rho q", nonzero=True)
a, b = sp.symbols("a b")
U, V, Z, v, W = sp.symbols("U V Z v W")


def clean(expression):
    return sp.cancel(sp.expand(expression))


def field_reduce(expression):
    """Use the relation only after applying coefficient derivatives."""
    return clean(expression.subs(rho, (q**2 + a + b*t**4)/t))


def dt(expression):
    return sp.diff(expression, t) + (rho - 4*b*t**3)*sp.diff(expression, q)/(2*q)


def dr(expression):
    return sp.diff(expression, rho) + t*sp.diff(expression, q)/(2*q)


def square_root_jets():
    """Solve the four coefficient equations of a square, not a jet table."""
    eps = sp.Symbol("eps")
    radicand = (t + eps*U)*(rho + eps*V) - a - b*(t + eps*U)**4
    increments = [None] + [sp.expand(radicand).coeff(eps, j) for j in range(1, 5)]
    jets = [q]
    for j in range(1, 5):
        cross = sum(jets[i]*jets[j-i] for i in range(1, j))
        jets.append(sp.factor((increments[j] - cross)/(2*q)))
    return increments, jets


def multiplication_characteristic(rpoly, ppoly):
    """Multiplication by r on the displayed finite-free monic quotient."""
    degree = sp.degree(ppoly, v)
    columns = []
    for j in range(degree):
        remainder = sp.Poly(sp.rem(rpoly*v**j, ppoly - W, v), v)
        columns.append([remainder.coeff_monomial(v**i) for i in range(degree)])
    matrix = sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))
    return sp.expand(matrix.charpoly(U).as_expr())


class DistinctRootResidueSexticControls235(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_quadratic_field_taylor_recursion_and_extended_derivatives(self):
        relation = q**2 - t*rho + a + b*t**4
        self.assertZero(dt(relation))
        self.assertZero(dr(relation))
        for fixture in (q, t*rho/q + q**3, (t + rho)/(q*t)):
            self.assertZero(dt(dr(fixture)) - dr(dt(fixture)))
        self.assertZero(dr(dr(q)) + t**2/(4*q**3))

        increments, jets = square_root_jets()
        expected_increments = [
            (rho - 4*b*t**3)*U + t*V, U*V - 6*b*t**2*U**2,
            -4*b*t*U**3, -b*U**4,
        ]
        for actual, expected in zip(increments[1:], expected_increments):
            self.assertZero(actual - expected)
        derivative_jet = q
        for j in range(1, 5):
            derivative_jet = sp.factor((U*dt(derivative_jet) + V*dr(derivative_jet))/j)
            self.assertZero(field_reduce(derivative_jet - jets[j]))
            self.assertZero(2*q*jets[j] + sum(jets[i]*jets[j-i] for i in range(1, j))
                            - increments[j])
        D1, D2, D3, D4 = increments[1:]
        displayed = [D2/(2*q) - D1**2/(8*q**3),
                     D3/(2*q) - D1*D2/(4*q**3) + D1**3/(16*q**5),
                     D4/(2*q) - (2*D1*D3 + D2**2)/(8*q**3)
                     + 3*D1**2*D2/(16*q**5) - 5*D1**4/(128*q**7)]
        for actual, expected in zip(jets[2:], displayed):
            self.assertZero(actual - expected)
        R1 = sp.diff(jets[2], V)
        C2 = dr(jets[2])
        self.assertZero(R1 - U/(2*q) + t*D1/(4*q**3))
        self.assertZero(C2 + t*D2/(4*q**3) + D1*U/(4*q**3)
                        - 3*t*D1**2/(16*q**5))
        # Coefficient differentiation is not formal differentiation in V.
        self.assertNotEqual(field_reduce(C2 - R1), 0)

    def test_full_sextic_factorization_and_all_residue_degeneracies(self):
        _, jets = square_root_jets()
        R1, C2 = sp.diff(jets[2], V), dr(jets[2])
        H6 = field_reduce(dr(dr(q))*jets[3]**2/2 - R1*C2*jets[3] + R1**2*jets[4])
        Z0 = t**2*V + (a - 3*b*t**4 - q**2)*U
        bracket = Z0**4 + 8*q**2*(a + b*t**4)*U**2*Z0**2 \
            + 16*q**4*(a - b*t**4)**2*U**4
        self.assertZero(H6 + U**2*bracket/(512*q**9*t**4))
        self.assertEqual(sp.Poly(H6, U, V).total_degree(), 6)
        self.assertZero(sp.Poly(H6, U, V).coeff_monomial(U**2*V**4) + t**4/(512*q**9))
        depressed = clean((-512*q**9*t**4*H6/U**2).subs(
            V, (Z - (a - 3*b*t**4 - q**2)*U)/t**2))
        self.assertZero(depressed - Z**4 - 8*q**2*(a + b*t**4)*U**2*Z**2
                        - 16*q**4*(a - b*t**4)**2*U**4)
        self.assertEqual(sp.Poly(depressed, Z).coeff_monomial(Z**3), 0)
        self.assertEqual(sp.Poly(depressed, Z).coeff_monomial(Z), 0)

        alpha, beta = sp.symbols("alpha beta", nonzero=True)
        four_lines = sp.prod(Z + 2*sp.I*q*(ee*alpha + dd*beta*t**2)*U
                             for ee in (-1, 1) for dd in (-1, 1))
        self.assertZero(four_lines - depressed.subs({a: alpha**2, b: beta**2}))
        # Count repeated finite directions over the generic coefficient field.
        quartic = sp.expand(four_lines.subs(U, 1))
        cases = [(quartic, 1),
                 (quartic.subs(beta, 0), Z**2 + 4*q**2*alpha**2),
                 (quartic.subs(alpha, 0), Z**2 + 4*q**2*beta**2*t**4),
                 (quartic.subs({alpha: 0, beta: 0}), Z**3)]
        for polynomial, expected_gcd in cases:
            common = sp.Poly(polynomial, Z).gcd(sp.Poly(sp.diff(polynomial, Z), Z)).monic()
            self.assertZero(common.as_expr() - expected_gcd)
        # U=0 is the additional direction at infinity, always exactly double.
        at_infinity = sp.Poly(H6.subs(V, 1), U)
        self.assertEqual(min(monomial[0] for monomial, coeff in at_infinity.terms() if coeff != 0), 2)
        pure = H6.subs({a: 0, b: 0})
        self.assertZero(pure + U**2*((q**2/t)*U - t*V)**4/(512*q**9))
        # A special numerical t fiber can merge generic lines; it is not a field identity.
        special = sp.expand(quartic.subs({alpha: 1, beta: 1, t: 1}))
        self.assertZero(special - Z**2*(Z**2 + 16*q**2))
        self.assertEqual(sp.Poly(special, Z).gcd(sp.Poly(sp.diff(special, Z), Z)).degree(), 1)

    def test_formal_cofactor_degree_fixtures_and_pure_case_boundary(self):
        evaluate = lambda expression, y, theta: sp.expand(expression.subs({U: y, V: theta}, simultaneous=True))
        # A selected double top line and a quadratic parametrization force degree eight.
        G = V**2 - U
        Q1 = U**2*(U - V)**2 + U**3 + V + 1
        self.assertZero(evaluate(G, v**2, v))
        self.assertEqual(sp.Poly(G*Q1, U, V).total_degree(), 6)
        q1 = evaluate(Q1, v**2, v)
        R = evaluate(U + 2*V + 3, v**2, v)
        self.assertEqual(sp.degree(q1, v), 8)
        self.assertEqual(sp.degree(R**3, v), 6)
        self.assertNotEqual(sp.rem(R**3, q1, v), 0)
        self.assertLessEqual(sp.degree(evaluate(U**3 + V + 1, v**2, v), v), 6)

        # A simple selected top line yields degree five against a cubic bound.
        Qsimple = U**2*(U - V)*(U - 2*V)*(U - 3*V)
        self.assertEqual(sp.degree(evaluate(Qsimple, v, 1), v), 5)
        self.assertEqual(sp.degree(evaluate(U + V, v, 1)**3, v), 3)
        # A double line need not violate this bound: this is not an actual frame.
        Qdouble = U*V*(U - V)*(U - 2*V)*(U - 3*V) + 1
        self.assertEqual(sp.Poly(U*Qdouble, U, V).total_degree(), 6)
        self.assertEqual(evaluate(Qdouble, 0, v), 1)
        # The pure-residue (2,4) top is outside the at-most-two argument.
        Gpure, Qpure = V**4 - U, U**2
        self.assertZero(evaluate(Gpure, v**4, v))
        self.assertEqual(sp.Poly(Gpure*Qpure, U, V).total_degree(), 6)
        self.assertEqual(sp.degree(evaluate(Qpure, v**4, v), v), 8)
        self.assertEqual(sp.degree(evaluate(U - V, v**4, v)**3, v), 12)

    def test_finite_free_characteristic_polynomials_and_birational_boundary(self):
        eta, kappa, nu = sp.symbols("eta kappa nu")
        fixtures = [(v, v**2 + eta*v + nu),
                    (v**2 + eta*v, v**3 + kappa*v + nu),
                    (v**3 + eta*v, v**4 + kappa*v**2 + nu),
                    (v**2 + v, v**5 + v**2)]
        for rpoly, ppoly in fixtures:
            i, d = sp.degree(rpoly, v), sp.degree(ppoly, v)
            self.assertEqual(sp.gcd(i, d), 1)  # These particular pairs are birational.
            characteristic = multiplication_characteristic(rpoly, ppoly)
            self.assertZero(characteristic - sp.resultant(ppoly - W, U - rpoly, v))
            self.assertZero(characteristic.subs({U: rpoly, W: ppoly}, simultaneous=True))
            polynomial = sp.Poly(characteristic, U, W)
            self.assertEqual(polynomial.total_degree(), d)
            top = sum(coeff*U**powers[0]*W**powers[1] for powers, coeff in polynomial.terms()
                      if sum(powers) == d)
            self.assertZero(top - U**d)
            in_U = sp.Poly(characteristic, U)
            for j in range(1, d + 1):
                coefficient = in_U.coeff_monomial(U**(d-j))
                if coefficient != 0:
                    self.assertLessEqual(sp.degree(coefficient, W), i*j//d)
                self.assertLess(i*j//d, j)
        # Without field equality, the rank-d characteristic polynomial can repeat
        # the minimal relation: finite-free rank alone does not prove equation (17).
        repeated = multiplication_characteristic(v**2, v**4)
        self.assertZero(repeated - (U**2 - W)**2)
        self.assertZero((U**2 - W).subs({U: v**2, W: v**4}, simultaneous=True))
        self.assertEqual(sp.Poly(U**2 - W, U, W).total_degree(), 2)
        self.assertEqual(sp.degree(v**4, v), 4)


if __name__ == "__main__":
    unittest.main()
