"""Finite exact controls for the pass-32 divergence-class reduction.

No unknown hypersurface presentation is supplied or discovered here.
The four-dimensional source quotient is not a computation of theta's rank.
Only unittest and SymPy are imported, with no project solver.
"""

import unittest

import sympy as sp


u = sp.symbols("u")
d = u**4 - 1
roots = (sp.Integer(1), sp.I, sp.Integer(-1), -sp.I)
pairs = ((sp.Integer(1), sp.I),
         (sp.Integer(1), -sp.I),
         (sp.Integer(-1), sp.I))
X, Y, Z = sp.symbols("X Y Z")


def reduce_derivative(q):
    """Return G in d*C[u], remainder of degree < 3, with q=G'+remainder."""
    remainder = sp.Poly(q, u, domain=sp.QQ_I)
    potential = sp.Integer(0)
    while not remainder.is_zero and remainder.degree() >= 3:
        degree = remainder.degree()
        term = remainder.LC() * d * u**(degree - 3) / sp.Integer(degree + 1)
        potential += term
        remainder = sp.Poly(remainder.as_expr() - sp.diff(term, u),
                            u, domain=sp.QQ_I)
    return sp.expand(potential), remainder.as_expr()


def periods(q):
    primitive = sp.integrate(q, u)
    return sp.Matrix([sp.expand(primitive.subs(u, right)
                               - primitive.subs(u, left))
                      for left, right in pairs])


def derive(poly, variables, coefficients):
    return sp.expand(sum(c * sp.diff(poly, v)
                         for v, c in zip(variables, coefficients)))


def divergence(variables, coefficients):
    return sp.expand(sum(sp.diff(c, v)
                         for v, c in zip(variables, coefficients)))


def hamiltonian(F, G):
    return tuple(sp.expand(c) for c in
                 sp.Matrix([sp.diff(F, v) for v in (X, Y, Z)]).cross(
                     sp.Matrix([sp.diff(G, v) for v in (X, Y, Z)])))


def diagonal_projection(poly):
    result = sp.Integer(0)
    for powers, coefficient in sp.Poly(poly, X, Y, Z).terms():
        if powers[0] == powers[1] == powers[2]:
            result += coefficient * (X * Y * Z)**powers[0]
    return sp.expand(result)


class DivergenceTorsionChecks(unittest.TestCase):
    def test_unique_three_term_derivative_remainder(self):
        examples = [u**degree for degree in range(15)]
        examples += [u**17 / 3 - 2 * u**10 + (1 + sp.I) * u**7 - 5 * u + 2,
                     sp.diff(d * (u**8 - sp.I * u**2 + 3), u)]
        for q in examples:
            potential, remainder = reduce_derivative(q)
            self.assertEqual(sp.expand(q - sp.diff(potential, u) - remainder), 0)
            self.assertEqual(sp.rem(potential, d, u), 0)
            self.assertTrue(remainder == 0 or sp.degree(remainder, u) <= 2)
        self.assertEqual(reduce_derivative(u**3), (d / 4, 0))
        self.assertEqual(reduce_derivative(u**4)[1], sp.Rational(1, 5))
        for q in (sp.Integer(1), u, u**2):
            self.assertEqual(reduce_derivative(q), (0, q))

    def test_primitive_differences_give_exact_remainder_coordinates(self):
        matrix = sp.Matrix.hstack(*(periods(u**j) for j in range(3)))
        self.assertEqual(sp.simplify(matrix.det()), -8 * sp.I / 3)
        q = 3 * u**13 - u**8 / 7 + (2 - sp.I) * u**2 + 4 * u - 2
        potential, remainder = reduce_derivative(q)
        self.assertEqual(periods(sp.diff(potential, u)), sp.zeros(3, 1))
        coefficients = sp.Matrix([sp.expand(remainder).coeff(u, j)
                                  for j in range(3)])
        self.assertEqual(sp.simplify(periods(q) - matrix * coefficients),
                         sp.zeros(3, 1))
        # Zero residues alone are weaker than having a descending primitive.
        self.assertNotEqual(periods(sp.Integer(1)), sp.zeros(3, 1))

    def test_original_scaled_pairs_and_residue_coordinate(self):
        c = sp.Rational(3, 2)
        q = u**7 - 2 * u**2 + sp.I
        p = sp.expand(c * u + d * q)
        residues = {r: sp.simplify(-p.subs(u, r) / sp.diff(d, u).subs(u, r))
                    for r in roots}
        for r in roots:
            self.assertEqual(sp.simplify(p.subs(u, r) / r), c)
            self.assertEqual(residues[r], -c / (4 * r**2))
        for left, right in pairs:
            self.assertEqual(sp.simplify(residues[left] + residues[right]), 0)
        G = d * (u**5 - 2 * u + 1)
        p_hamiltonian = sp.expand(d * sp.diff(G, u))
        for r in roots:
            self.assertEqual(p_hamiltonian.subs(u, r), 0)
        self.assertEqual(periods(sp.diff(G, u)), sp.zeros(3, 1))

    def test_polynomial_hamiltonian_and_change_of_potential_lift(self):
        F = X * Y * Z + X**3 + Y**2 - Z + 1
        G = X * Z + Y**3 - 2 * X
        Q = X * Y - Z**2 + 3
        field = hamiltonian(F, G)
        self.assertEqual(derive(F, (X, Y, Z), field), 0)
        self.assertEqual(divergence((X, Y, Z), field), 0)
        changed = hamiltonian(F, G + F * Q)
        correction = hamiltonian(F, Q)
        self.assertEqual(tuple(sp.expand(new - old - F * extra)
                               for new, old, extra in zip(changed, field, correction)),
                         (0, 0, 0))
        # The sign convention is fixed by F=X, omega_F=dY wedge dZ.
        coordinate_field = hamiltonian(X, G)
        self.assertEqual(coordinate_field[0], 0)
        self.assertEqual(-coordinate_field[2], -sp.diff(G, Y))
        self.assertEqual(coordinate_field[1], -sp.diff(G, Z))

    def test_genuine_nodal_cylinder_allows_nonzero_residues(self):
        F = Y**2 - X**2 * (X + 1)
        substitution = {X: u**2 - 1, Y: u * (u**2 - 1)}
        self.assertEqual(sp.expand(F.subs(substitution)), 0)
        canonical_factor = sp.cancel(sp.diff(u**2 - 1, u)
                                     / sp.diff(F, Y).subs(substitution))
        self.assertEqual(canonical_factor, 1 / (u**2 - 1))
        self.assertEqual(derive(F, (X, Y, Z), (0, 0, 1)), 0)
        self.assertEqual(divergence((X, Y, Z), (0, 0, 1)), 0)
        one_form_factor = -canonical_factor
        self.assertEqual(sp.limit((u - 1) * one_form_factor, u, 1),
                         sp.Rational(-1, 2))
        self.assertEqual(sp.limit((u + 1) * one_form_factor, u, -1),
                         sp.Rational(1, 2))

    def test_local_volume_integration_is_exact_but_need_not_polynomial(self):
        xi, eta, t = sp.symbols("xi eta t")
        volume_coefficient = 1 + xi + eta * t + t
        h = xi**2 * t + eta + t**3
        numerator = sp.integrate(volume_coefficient * h, t)
        k = sp.cancel(numerator / volume_coefficient)
        self.assertEqual(sp.cancel(sp.diff(volume_coefficient * k, t)
                                   / volume_coefficient - h), 0)
        self.assertEqual(derive(xi * eta, (xi, eta, t), (0, 0, k)), 0)
        self.assertEqual(volume_coefficient.subs({xi: 0, eta: 0, t: 0}), 1)
        self.assertNotEqual(sp.denom(k), 1)

    def test_smooth_global_quotient_retains_diagonal_monomials(self):
        F = X * Y * Z - 1
        generators = ((X, 0, -Z), (0, Y, -Z))
        for field in generators:
            self.assertEqual(derive(F, (X, Y, Z), field), 0)
            self.assertEqual(divergence((X, Y, Z), field), 0)
        # Bounded monomial controls support the all-degree weight proof.
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    monomial = X**i * Y**j * Z**k
                    if i == j == k:
                        self.assertEqual(diagonal_projection(monomial), monomial)
                    else:
                        field, weight = ((generators[0], i - k) if i != k
                                         else (generators[1], j - k))
                        multiple = tuple(monomial * c / sp.Integer(weight)
                                         for c in field)
                        self.assertEqual(divergence((X, Y, Z), multiple), monomial)
        a = X**3 * Y + Y**2 * Z**5 + X * Y * Z
        b = X**2 * Z + (X * Y * Z)**2 + 3 * Y
        field = tuple(sp.expand(a * left + b * right)
                      for left, right in zip(*generators))
        self.assertEqual(diagonal_projection(divergence((X, Y, Z), field)), 0)
        self.assertEqual(diagonal_projection(sp.Integer(1)), 1)
        q = 1 + 2 * X * Y * Z - (X * Y * Z)**3
        self.assertEqual(diagonal_projection(F * q), sp.expand(F * q))
        self.assertNotEqual(sp.expand(F * q), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
