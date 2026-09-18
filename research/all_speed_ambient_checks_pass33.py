"""Finite exact controls for the all-speed ambient obstruction.

The unknown hypersurface presentation is not supplied by this suite.
Rational branch matrices support, but do not prove, the written
topological quotient argument. Only unittest and SymPy are imported.
"""

import unittest

import sympy as sp


u, x, y, z = sp.symbols("u x y z")
d = u**4 - 1
root_values = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)


def field(F, G):
    return sp.Matrix([sp.diff(F, v) for v in (x, y, z)]).cross(
        sp.Matrix([sp.diff(G, v) for v in (x, y, z)]))


def apply(coefficients, polynomial):
    return sp.expand(sum(a * sp.diff(polynomial, v)
                         for a, v in zip(coefficients, (x, y, z))))


def branch_matrix(groups):
    matrix = sp.zeros(len(groups), sum(len(group) for group in groups))
    column = 0
    for row, indices in enumerate(groups):
        for index in indices:
            matrix[row, column] = index
            column += 1
    return matrix


class AllSpeedAmbientChecks(unittest.TestCase):
    def test_weighted_branch_kernel_and_diagonal_preimage_dimensions(self):
        patterns = (
            ((1,),),
            ((2, 3, 5),),
            ((1, 1), (1, 1)),
            ((2, 4, 1), (3,)),
            ((1, 2), (3,), (2, 7, 4)),
        )
        for groups in patterns:
            theta = branch_matrix(groups)
            r, q = theta.shape
            self.assertEqual(theta.rank(), r)
            diagonal = sp.ones(r, 1)
            augmented = theta.row_join(-diagonal)
            solutions = augmented.nullspace()
            self.assertEqual(len(solutions), q - r + 1)
            projected = sp.Matrix.hstack(*(vector[:q, :] for vector in solutions))
            self.assertEqual(projected.rank(), q - r + 1)
            for vector in solutions:
                self.assertEqual(theta * vector[:q, :] - vector[q] * diagonal,
                                 sp.zeros(r, 1))

    def test_selected_component_lower_bound_with_other_branches(self):
        for selected_branches in range(1, 4):
            for selected_points in range(selected_branches, selected_branches + 4):
                for other_branches in range(4):
                    for excess in range(3):
                        other_points = other_branches + excess
                        total_components = (selected_points + other_points
                                            - selected_branches - other_branches + 1)
                        bound = selected_points - selected_branches + 1
                        self.assertGreaterEqual(total_components, bound)
                        self.assertEqual(total_components - bound, excess)
        # A genuine product quotient has one fiber component even if its
        # artificially enlarged exceptional divisor has several branches.
        for branches in range(1, 6):
            theta = branch_matrix(tuple((1,) for _ in range(branches)))
            self.assertEqual(theta.cols - theta.rows + 1, 1)

    def test_actual_conductor_and_extra_root_component_counts(self):
        polynomials = (d, d**2, d * (u - 2), d * (u - 2)**3 * (u - 3))
        for polynomial in polynomials:
            roots = sp.roots(polynomial, u)
            self.assertEqual(sum(roots.values()), sp.degree(polynomial, u))
            self.assertTrue(set(root_values).issubset(roots))
            n = len(roots) - 4
            normalized_line_count = len(roots) + 2  # split at 1 and i
            glued_component_count = normalized_line_count - 3
            self.assertEqual(glued_component_count, 3 + n)
            self.assertEqual(glued_component_count, len(roots) - 1)
            self.assertLess(glued_component_count, len(roots))  # smooth-base bound
            self.assertEqual(glued_component_count, len(roots) - 2 + 1)
        # The degree-two nodal map has two base branches, not four.
        for r in root_values:
            self.assertIn(sp.simplify(r**2), (1, -1))
        self.assertEqual(branch_matrix(((1, 1), (1, 1))).cols - 2 + 1, 3)

    def test_rank_one_linear_pullback_cannot_give_rank_two_node(self):
        a, b, c, k, q11, q12, q22 = sp.symbols("a b c k q11 q12 q22")
        linear = sp.Matrix([[a, b, c], [k * a, k * b, k * c]])
        quadratic = sp.Matrix([[q11, q12], [q12, q22]])
        pulled = linear.T * quadratic * linear
        for i in range(3):
            for j in range(i + 1, 3):
                for r in range(3):
                    for s in range(r + 1, 3):
                        self.assertEqual(sp.expand(pulled.extract([i, j], [r, s]).det()), 0)
        ordinary_node = sp.hessian(x * y, (x, y, z))
        self.assertEqual(ordinary_node.rank(), 2)
        cubic_pullback = sp.expand((a * x + b * y)**3 + (c * y + k * z)**3)
        self.assertTrue(all(sum(powers) == 3
                            for powers, coefficient in sp.Poly(cubic_pullback, x, y, z).terms()
                            if coefficient != 0))

    def test_even_hamiltonian_action_and_ambient_divergence_identities(self):
        G = d * u
        p = sp.expand(d * sp.diff(G, u))
        self.assertEqual(p, sp.expand(d * (5 * u**4 - 1)))
        self.assertEqual(sp.expand(p.subs(u, -u) - p), 0)
        self.assertNotEqual(p, 0)
        for r in root_values:
            self.assertEqual(sp.simplify(G.subs(u, r)), 0)
            self.assertEqual(sp.simplify(p.subs(u, r)), 0)
        A = (u - 1) * (u - sp.I)
        relation = A * z - y * (y - 1)
        image = p * A * sp.diff(relation, y) + p * (2 * y - 1) * sp.diff(relation, z)
        self.assertEqual(sp.expand(image), 0)
        # These are ordinary polynomial controls, not an unknown embedding.
        F = x * y * z + x**2 - y + z**3
        lifted_G = x**2 * z + y**3 - x
        K = field(F, lifted_G)
        self.assertEqual(apply(K, F), 0)
        self.assertEqual(apply(K, lifted_G), 0)
        self.assertEqual(sp.expand(sum(sp.diff(a, v)
                                       for a, v in zip(K, (x, y, z)))), 0)

    def test_exact_odd_replica_subspace_including_zero_speed(self):
        t = sp.symbols("t")
        for constant in (0, 1, -2):
            for Q in (sp.Integer(1), t, t**3 - 2 * t + 3):
                H = constant + (t**2 - 1) * Q
                multiplier = sp.expand(u * H.subs(t, u**2))
                self.assertEqual(sp.expand(multiplier + multiplier.subs(u, -u)), 0)
                self.assertEqual(sp.rem(multiplier, d, u), constant * u)
        # Surface invariants need not lift to ambient invariants: du is
        # in T but not in S; multiplying the primitive u by it is not odd.
        extra_surface_invariant = d * u
        self.assertNotEqual(sp.expand(extra_surface_invariant.subs(u, -u)
                                      - extra_surface_invariant), 0)
        forbidden_replica = d * u**2
        self.assertEqual(sp.rem(forbidden_replica, d, u), 0)
        self.assertNotEqual(sp.expand(forbidden_replica
                                      + forbidden_replica.subs(u, -u)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
