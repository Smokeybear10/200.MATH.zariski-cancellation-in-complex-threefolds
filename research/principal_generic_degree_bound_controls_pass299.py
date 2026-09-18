"""Finite controls for299, not a universal degree or cancellation proof.

Checks the Hilbert-polynomial identity and abstract boundary examples.
Imports no solver, earlier checker, or project proof.
"""

import unittest

import sympy as s


class GenericDegreeBoundControls(unittest.TestCase):
    def test_hilbert_polynomial_identity(self):
        n, a, b = s.symbols("n a b")

        def four_variable_monomials(q):
            return (q + 3) * (q + 2) * (q + 1) / 6

        dimension = (four_variable_monomials(n)
                     - four_variable_monomials(n - a)
                     - four_variable_monomials(n - b)
                     + four_variable_monomials(n - a - b))
        expected = a * b * n + a * b * (4 - a - b) / 2
        self.assertEqual(s.expand(dimension - expected), 0)
        self.assertEqual(s.expand(expected.subs({a: 3, b: 4})), 12 * n - 18)

    def test_abstract_degree_twelve_embedding(self):
        U, P, V, v = s.symbols("U P V v")
        f, g = P - U**3, V - P**4
        evaluation = {U: v, P: v**3, V: v**12}
        self.assertEqual(s.expand(f.subs(evaluation)), 0)
        self.assertEqual(s.expand(g.subs(evaluation)), 0)
        self.assertEqual(s.Poly(f, U, P, V).total_degree(), 3)
        self.assertEqual(s.Poly(g, U, P, V).total_degree(), 4)
        self.assertEqual(s.Poly(evaluation[V], v).degree(), 12)
        matrix = s.Matrix([[s.diff(f, z) for z in (U, P, V)],
                           [s.diff(g, z) for z in (U, P, V)]])
        self.assertEqual(matrix[:, 1:3].det(), 1)
        # A nonconstant common factor can evaluate to a unit.
        D = 1 + g
        F, G = D * f, D * g
        self.assertEqual(s.expand(D.subs(evaluation)), 1)
        reduced = s.Matrix([[s.diff(F, z) for z in (P, V)],
                            [s.diff(G, z) for z in (P, V)]])
        self.assertEqual(s.expand(reduced.det().subs(evaluation)), 1)

    def test_shared_surface_boundary_rejects_degree_inference(self):
        U, P, V, v = s.symbols("U P V v")
        f, g = V, V**2
        evaluation = {U: v, P: v**13, V: 0}
        self.assertEqual(f.subs(evaluation), 0)
        self.assertEqual(g.subs(evaluation), 0)
        matrix = s.Matrix([[s.diff(f, z) for z in (U, P, V)],
                           [s.diff(g, z) for z in (U, P, V)]])
        for columns in ((0, 1), (0, 2), (1, 2)):
            self.assertEqual(matrix[:, list(columns)].det().subs(evaluation), 0)
        self.assertEqual(s.Poly(evaluation[P], v).degree(), 13)


if __name__ == "__main__":
    unittest.main(verbosity=2)
