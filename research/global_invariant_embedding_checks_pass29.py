"""Finite illustrative controls for global-invariant-embedding-pass29.md.

These controls verify known displayed algebras, explicit normalizations and
Hamiltonian examples. They do not test the unknown polynomial p(u), prove
Abhyankar--Moh or Bhatwadekar--Dutta, or certify the universal geometric
nonembedding theorem. Only unittest and SymPy are imported.
"""

import unittest
import sympy as sp


u, D, E, X, Y, Z, Q = sp.symbols("u D E X Y Z Q")
ii = sp.I


def trunc(poly, variable, order):
    return sp.expand(sum(coefficient * variable**exponent[0]
                         for exponent, coefficient
                         in sp.Poly(sp.expand(poly), variable).terms()
                         if exponent[0] < order))


def jet_product(left, right, variable, order):
    return trunc(left * right, variable, order)


def jet_power(base, exponent, variable, order):
    result = sp.Integer(1)
    for _ in range(exponent):
        result = jet_product(result, base, variable, order)
    return result


def act(field, polynomial):
    return sp.expand(field[0] * sp.diff(polynomial, X)
                     + field[1] * sp.diff(polynomial, Y))


def hamiltonian(polynomial):
    return (sp.diff(polynomial, Y), -sp.diff(polynomial, X))


def lowest_total_degree(polynomial, variables):
    terms = sp.Poly(sp.expand(polynomial), *variables).terms()
    if not terms or sp.Poly(polynomial, *variables).is_zero:
        raise ValueError("The zero polynomial has no finite initial degree.")
    return min(sum(exponent) for exponent, coefficient in terms)


def homogeneous_quotient_dimension(relations, variables, degree):
    gb = sp.groebner(relations, *variables, order="grlex")
    leading = [polynomial.LM(order="grlex").exponents
               for polynomial in gb.polys]
    monomials = [(a, b, degree - a - b)
                 for a in range(degree + 1)
                 for b in range(degree - a + 1)]
    return sum(not any(all(exponent >= divisor for exponent, divisor
                           in zip(monomial, lead))
                       for lead in leading)
               for monomial in monomials)


class GlobalInvariantEmbeddingChecks(unittest.TestCase):
    def test_quartic_plane_base_has_exact_finite_birational_normalization(self):
        """This is C[d,e], not the unknown plane base of the universal proof."""
        d = u**4 - 1
        e = u * d
        phi = E**4 - D**4 * (D + 1)
        self.assertEqual(sp.expand(phi.subs({D: d, E: e}, simultaneous=True)), 0)
        self.assertEqual(sp.cancel(e / d), u)
        self.assertEqual(sp.expand(u**4 - d - 1), 0)
        self.assertEqual(sp.Poly(phi, E).degree(), 4)
        self.assertEqual(sp.Poly(phi, E).LC(), 1)
        for root in (sp.Integer(1), ii, sp.Integer(-1), -ii):
            self.assertEqual(sp.expand(d.subs(u, root)), 0)
            self.assertEqual(sp.expand(e.subs(u, root)), 0)
        # The degree-four relation remains irreducible over C(D):
        # D+1 has valuation one, so it is not a square in C(D).
        factors = sp.factor_list(phi, extension=ii)[1]
        self.assertEqual(len(factors), 1)
        self.assertEqual(factors[0][1], 1)

    def test_actual_four_distinct_formal_branches_and_initial_factors(self):
        order = 9
        root_series = sum(sp.binomial(sp.Rational(1, 4), k) * D**k
                          for k in range(order))
        self.assertEqual(jet_power(root_series, 4, D, order), D + 1)
        branches = []
        product = sp.Integer(1)
        for root in (sp.Integer(1), ii, sp.Integer(-1), -ii):
            branch = trunc(root * D * root_series, D, order)
            branches.append(branch)
            self.assertEqual(branch.subs(D, 0), 0)
            self.assertEqual(sp.diff(branch, D).subs(D, 0), root)
            self.assertEqual(
                trunc(jet_power(branch, 4, D, order) - D**4 * (D + 1),
                      D, order), 0)
            product = jet_product(product, E - branch, D, order)
        self.assertEqual(product, sp.expand(E**4 - D**4 * (D + 1)))
        self.assertEqual(len(set(branch.coeff(D, 1) for branch in branches)), 4)
        initial = (E - D) * (E + D) * (E - ii * D) * (E + ii * D)
        self.assertEqual(sp.expand(initial), E**4 - D**4)
        self.assertEqual(lowest_total_degree(E**4 - D**4 * (D + 1), (D, E)), 4)

    def test_quadratic_hilbert_counts_distinguish_node_and_quartic_pullback(self):
        variables = (X, Y, Z)
        node_relation = X * Y
        quartic_initial = Y**4 - X**4
        expected_node = {1: 3, 2: 5, 3: 7, 4: 9}
        expected_quartic = {1: 3, 2: 6, 3: 10, 4: 14}
        for degree in range(1, 5):
            self.assertEqual(
                homogeneous_quotient_dimension((node_relation,), variables, degree),
                expected_node[degree])
            self.assertEqual(
                homogeneous_quotient_dimension((quartic_initial,), variables, degree),
                expected_quartic[degree])
        self.assertEqual(sp.binomial(4, 2), 6)
        self.assertEqual(sp.binomial(4, 2) - 1, 5)

    def test_global_polynomial_pullback_and_forbidden_denominator_cancellation(self):
        phi = E**4 - D**4 * (D + 1)
        for polynomial in (X + D*Y + Y**2, X**2 + D*Y**3,
                           D*X + Y**5):
            pullback = sp.expand(phi.subs(E, polynomial))
            self.assertGreaterEqual(lowest_total_degree(pullback, (D, X, Y)), 4)
            # All derivatives of total order at most three vanish at the origin.
            for a in range(4):
                for b in range(4 - a):
                    for c in range(4 - a - b):
                        derivative = sp.diff(pullback, D, a, X, b, Y, c)
                        self.assertEqual(derivative.subs({D: 0, X: 0, Y: 0}), 0)
        global_equation = sp.expand(phi.subs(E, D*X))
        canceled_equation = sp.cancel(global_equation / D**4)
        self.assertEqual(global_equation, sp.expand(D**4 * (X**4 - D - 1)))
        self.assertEqual(canceled_equation, X**4 - D - 1)
        self.assertEqual(global_equation.subs({D: 0, X: 0}), 0)
        self.assertEqual(canceled_equation.subs({D: 0, X: 0}), -1)
        self.assertEqual(lowest_total_degree(global_equation, (D, X)), 4)
        self.assertEqual(lowest_total_degree(canceled_equation, (D, X)), 0)

    def test_squarefree_parallel_line_hamiltonian_in_nonlinear_coordinates(self):
        q = X + Y**2
        companion = Y + q**2
        polynomial = q**4 - (D + 1)
        field = hamiltonian(polynomial)
        self.assertEqual(act(field, q), 0)
        self.assertEqual(act(field, companion), sp.expand(-4 * q**3))
        self.assertEqual(act(field, polynomial), 0)
        for variable in (X, Y):
            value = variable
            for _ in range(3):
                value = act(field, value)
            self.assertEqual(value, 0)
        inverse = {X: Q - (Z - Q**2)**2, Y: Z - Q**2}
        self.assertEqual(sp.expand(q.subs(inverse, simultaneous=True)), Q)
        self.assertEqual(sp.expand(companion.subs(inverse, simultaneous=True)), Z)
        divisor = sp.Poly(sp.gcd(field[0], field[1]), X, Y).monic().as_expr()
        self.assertEqual(sp.expand(divisor), sp.expand(q**3))
        primitive = tuple(sp.cancel(coefficient / divisor) for coefficient in field)
        self.assertEqual(primitive, (8*Y, -4))
        self.assertEqual(act(field, divisor), 0)
        self.assertEqual(act(primitive, q), 0)
        self.assertEqual(act(primitive, polynomial), 0)
        for root in (sp.Integer(1), ii, sp.Integer(-1), -ii):
            self.assertNotEqual(4 * root**3, 0)

    def test_nonsquarefree_zero_fiber_is_not_a_product_of_reduced_lines(self):
        polynomial = (Q**2 - 1)**2
        reduced_equation = Q**2 - 1
        gcd = sp.Poly(sp.gcd(polynomial, sp.diff(polynomial, Q)), Q).monic().as_expr()
        self.assertEqual(gcd, reduced_equation)
        self.assertNotEqual(sp.rem(reduced_equation, polynomial, Q), 0)
        self.assertEqual(sp.rem(reduced_equation**2, polynomial, Q), 0)
        self.assertEqual(sp.rem(sp.diff(polynomial, Q), reduced_equation, Q), 0)
        for root in (sp.Integer(1), sp.Integer(-1)):
            self.assertEqual(sp.diff(polynomial, Q).subs(Q, root), 0)
        # Degree four but only two reduced components: the proof must reject it.
        self.assertEqual(sp.degree(polynomial, Q), 4)
        self.assertEqual(sp.degree(reduced_equation, Q), 2)

    def test_intersecting_affine_lines_do_not_imply_an_lnd_hamiltonian(self):
        polynomial = X * Y
        field = hamiltonian(polynomial)
        self.assertEqual(field, (X, -Y))
        self.assertEqual(act(field, polynomial), 0)
        for variable, eigenvalue in ((X, 1), (Y, -1)):
            value = variable
            for exponent in range(1, 7):
                value = act(field, value)
                self.assertEqual(value, eigenvalue**exponent * variable)
                self.assertNotEqual(value, 0)
        # The two component ideals sum to the maximal ideal, not the unit ideal.
        gb = sp.groebner((X, Y), X, Y)
        self.assertEqual(gb.reduce(sp.Integer(1))[1], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
