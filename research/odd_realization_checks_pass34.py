"""Finite exact controls for the conditional integral plinth isolation proof.

The written proof supplies the actual-quotient hypotheses, integral Thom
diagram, absence of normalization cycles, and all-component quantifier.
These tests do not instantiate the unknown hypersurface embedding.
"""

import unittest

import sympy as sp


def maximal_minor_gcd(matrix):
    """For an r by r+1 matrix, compute its full-rank lattice index."""
    rows, columns = matrix.shape
    if columns != rows + 1:
        raise ValueError("This bounded control expects one extra column")
    determinants = []
    for omitted in range(columns):
        kept = [column for column in range(columns) if column != omitted]
        determinants.append(matrix[:, kept].det())
    return abs(sp.gcd_list(determinants))


class OddRealizationChecks(unittest.TestCase):
    def test_unchanged_pairing_edges_land_on_opposite_node_branches(self):
        roots = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)
        edges = ((0, 2), (0, 3), (1, 2))
        self.assertEqual(tuple(root**2 for root in roots), (1, 1, -1, -1))
        for left, right in edges:
            self.assertEqual(roots[left]**2, 1)
            self.assertEqual(roots[right]**2, -1)
            self.assertNotEqual(2 * roots[left], 0)
            self.assertNotEqual(2 * roots[right], 0)
        theta = sp.Matrix([[1, 1, 0, 0], [0, 0, 1, 1]])
        incidence = sp.zeros(4, 3)
        for column, edge in enumerate(edges):
            for row in edge:
                incidence[row, column] = 1
        self.assertEqual(theta * incidence, sp.ones(2, 3))

    def test_node_columns_are_a_full_integer_basis_not_just_rationally_independent(self):
        b, c, e = sp.symbols("b c e", integer=True)
        incidence = sp.Matrix([[1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 0]])
        target = sp.Matrix([c + e - b, b, c, e])
        self.assertEqual(incidence * sp.Matrix([c - b, e, b]), target)
        self.assertEqual(abs(incidence[[1, 2, 3], :].det()), 1)
        equation = sp.Matrix([[1, 1, -1, -1]])
        self.assertEqual(equation * incidence, sp.zeros(1, 3))
        # Both quotient maps are the same primitive integer functional.
        theta = sp.Matrix([[1, 1, 0, 0], [0, 0, 1, 1]])
        self.assertEqual(sp.Matrix([[1, -1]]) * theta, equation)
        self.assertEqual(sp.gcd_list(list(equation)), 1)

    def test_doubled_branch_blocks_have_the_claimed_integral_cokernel(self):
        for branches in range(1, 6):
            with self.subTest(branches=branches):
                image_and_diagonal = (2 * sp.eye(branches)).row_join(
                    sp.ones(branches, 1))
                self.assertEqual(maximal_minor_gcd(image_and_diagonal),
                                 2**(branches - 1))
                mod_two = image_and_diagonal.applyfunc(lambda value: value % 2)
                self.assertEqual(mod_two.rank(), 1)
                # All columns except the diagonal vanish modulo two, so
                # its rational rank here is also exactly its F_2 rank.
                self.assertEqual(mod_two[:, :branches], sp.zeros(branches))
                self.assertEqual(mod_two[:, branches], sp.ones(branches, 1))

    def test_unrelated_blocks_do_not_remove_torsion_but_an_extra_cycle_can(self):
        # Two doubled branches at one point, plus an independent puncture
        # at another point, have separate sphere columns.
        matrix = sp.Matrix([[2, 0, 0, 1, 0],
                            [0, 2, 0, 1, 0],
                            [0, 0, 1, 0, 1]])
        base_mod_two = matrix.applyfunc(lambda value: value % 2)
        self.assertEqual(base_mod_two.rank(), 2)
        obstruction = sp.Matrix([[1, -1, 0]])
        self.assertEqual((obstruction * matrix).applyfunc(lambda value: value % 2),
                         sp.zeros(1, 5))
        # This is an abstract negative control, not an actual curve cover:
        # an unaccounted non-puncture cycle could destroy the obstruction.
        extra_cycle = sp.Matrix([1, 0, 0])
        self.assertEqual(obstruction * extra_cycle, sp.ones(1, 1))
        enlarged_mod_two = matrix.row_join(extra_cycle).applyfunc(
            lambda value: value % 2)
        self.assertEqual(enlarged_mod_two.rank(), 3)

    def test_a_doubled_fixed_fiber_alone_has_an_actual_primitive_ambient_control(self):
        x, u, t = sp.symbols("x u t")
        invariant = x * t - u**2

        def derivation(expression):
            return sp.expand(x * sp.diff(expression, u)
                             + 2 * u * sp.diff(expression, t))

        self.assertEqual(derivation(x), 0)
        self.assertEqual(derivation(invariant), 0)
        self.assertEqual(derivation(derivation(u)), 0)
        self.assertEqual(derivation(derivation(derivation(t))), 0)
        self.assertEqual(sp.gcd(x, 2 * u), 1)
        self.assertEqual(invariant.subs(x, 0), -u**2)
        self.assertEqual(tuple(value.subs({x: 0, u: 0}) for value in (x, 2 * u)),
                         (0, 0))
        # A transverse disc t=0 has fiber algebra C[x,u]/(x,u^2),
        # with the explicit length-two basis 1,u.
        fiber = sp.groebner((x, invariant.subs(t, 0)), x, u)
        self.assertEqual(tuple(fiber), (x, u**2))
        self.assertEqual(fiber.reduce(u**2)[1], 0)
        self.assertEqual(fiber.reduce(u)[1], u)
        self.assertEqual(fiber.reduce(sp.Integer(1))[1], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
