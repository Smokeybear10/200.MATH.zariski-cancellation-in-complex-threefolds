"""Finite exact controls for the pass-30 all-action surface proof.

These tests do not classify unknown automorphisms, prove the source
theorems, or decide whether the surface has three algebra generators.
They use only unittest and SymPy, with no project solver imports.
"""

import unittest

import sympy as sp


u, y, z, t, c = sp.symbols("u y z t c")
A = (u - 1) * (u - sp.I)
d = u**4 - 1
relation = A * z - y * (y - 1)
roots = (sp.Integer(1), sp.I, sp.Integer(-1), -sp.I)
pairs = (((roots[0], 0), (roots[1], 0)),
         ((roots[0], 1), (roots[3], None)),
         ((roots[2], None), (roots[1], 1)))


def zero(expr):
    return sp.expand(expr) == 0


def delta(expr, coefficient=sp.Integer(1)):
    return sp.expand(coefficient * (A * sp.diff(expr, y)
                                   + (2 * y - 1) * sp.diff(expr, z)))


def flow(expr, coefficient):
    return sp.expand(expr.subs(
        {y: y + A * coefficient,
         z: z + (2 * y - 1) * coefficient + A * coefficient**2},
        simultaneous=True))


def branch(expr, root, epsilon):
    if epsilon is None:
        a = sp.expand(A.subs(u, root))
        yy = root * a * t
        zz = sp.expand(yy * (yy - 1) / a)
    else:
        yy = sp.Integer(epsilon)
        zz = root * (2 * epsilon - 1) * t
    return sp.expand(expr.subs({u: root, y: yy, z: zz}, simultaneous=True))


def root_values(expr):
    return tuple(sp.expand(expr.subs(u, r)) for r in roots)


def belongs_to_M(expr):
    values = tuple(sp.expand(expr.subs(u, r) / r) for r in roots)
    return all(zero(v - values[0]) for v in values)


class AllNoninvariantSurfaceChecks(unittest.TestCase):
    def test_normalization_derivation_and_actual_six_line_speeds(self):
        p = c * u + d * (u**3 + (2 - sp.I) * u + 1)
        self.assertTrue(zero(delta(relation, p)))
        self.assertTrue(zero(delta(delta(y, p), p)))
        self.assertTrue(zero(delta(delta(delta(z, p), p), p)))
        for pair in pairs:
            speeds = []
            for root, epsilon in pair:
                if epsilon is None:
                    param = y / (root * A.subs(u, root))
                else:
                    param = z / (root * (2 * epsilon - 1))
                speeds.append(branch(delta(param, p), root, epsilon))
            self.assertTrue(zero(speeds[0] - c))
            self.assertTrue(zero(speeds[1] - c))

    def test_exact_remainder_classifier_and_negative_controls(self):
        for p in (u, d, 7 * u + d * (u**7 - 3 * u**2 + sp.I),
                  sp.Integer(0)):
            self.assertTrue(belongs_to_M(p))
            rem = sp.rem(p, d, u)
            self.assertTrue(zero(rem - sp.expand(p.subs(u, 1)) * u))
        for p in (sp.Integer(1), u**2, u**3, 1 + d * u):
            self.assertFalse(belongs_to_M(p))
        matrix = sp.Matrix([[sp.expand(r**k / r - roots[0]**k / roots[0])
                             for k in range(4)] for r in roots[1:]])
        self.assertEqual(matrix.rank(), 3)
        self.assertEqual(matrix.nullspace(), [sp.Matrix([0, 1, 0, 0])])

    def test_actual_flow_inverse_composition_and_gluing(self):
        p = u + d * (u**2 + 1)
        q = -2 * u + d * (u + sp.I)
        self.assertTrue(zero(flow(relation, p) - relation))
        for f in (u, y, z):
            self.assertTrue(zero(flow(flow(f, p), -p) - f))
            self.assertTrue(zero(flow(flow(f, p), q) - flow(f, p + q)))
        for pair in pairs:
            for root, epsilon in pair:
                if epsilon is None:
                    param = y / (root * A.subs(u, root))
                else:
                    param = z / (root * (2 * epsilon - 1))
                self.assertTrue(zero(branch(flow(param, p), root, epsilon)
                                     - t - 1))

    def test_all_affine_root_maps_and_minus_case_pairing_failure(self):
        possible = []
        target_roots = set(roots)
        for first in roots:
            for second in roots:
                if first == second:
                    continue
                alpha = sp.simplify((second - first) / (sp.I - 1))
                beta = sp.simplify(first - alpha)
                images = {sp.simplify(alpha * r + beta) for r in roots}
                if images == target_roots:
                    possible.append((alpha, beta))
        self.assertEqual(set(possible), {(r, sp.Integer(0)) for r in roots})
        retaining_split = [(a, b) for a, b in possible
                           if {sp.simplify(a + b), sp.simplify(a * sp.I + b)}
                           == {sp.Integer(1), sp.I}]
        self.assertEqual(retaining_split, [(sp.Integer(1), sp.Integer(0))])
        original_pairs = {frozenset(pair) for pair in pairs}
        swapped_first = frozenset(((roots[0], 1), (roots[1], 1)))
        self.assertNotIn(swapped_first, original_pairs)
        # Both branches are required to kill a possible leading pole.
        residue_matrix = sp.Matrix([[0, 1], [1, 1]])
        self.assertEqual(residue_matrix.det(), -1)

    def test_fractional_module_inverse_and_exact_order_four(self):
        self.assertTrue(zero(u * ((1 - d) * u**3) + d**2 - 1))
        for k in range(8):
            self.assertTrue(zero(sp.rem(u**(k + 4) - u**k, d, u)))
            values = root_values(u**k)
            constant_on_four = all(zero(v - values[0]) for v in values)
            constant_on_pairs = all(zero(left[0]**k - right[0]**k)
                                    for left, right in pairs)
            self.assertEqual(constant_on_four, k % 4 == 0)
            self.assertEqual(constant_on_pairs, k % 4 == 0)
            self.assertEqual(sp.gcd(u**k, d), 1)
        # These are normalization residue controls. Nonprincipality of
        # the actual modules also uses B* = C*, proved in the note.

    def test_two_actual_velocities_have_no_common_zero(self):
        self.assertTrue(zero((2 * y - 1)**2 - 4 * A * z - 1
                             + 4 * relation))
        self.assertTrue(zero(u * u**3 - d - 1))
        normal_combination = sp.expand(
            u**3 * ((2 * y - 1) * delta(z, u) - 4 * z * delta(y, u))
            - ((2 * y - 1) * delta(z, d) - 4 * z * delta(y, d)))
        self.assertTrue(zero(normal_combination - 1 + 4 * relation))
        for pair in pairs:
            for root, epsilon in pair:
                self.assertTrue(zero(branch(delta(y, d), root, epsilon)))
                self.assertTrue(zero(branch(delta(z, d), root, epsilon)))
        self.assertEqual(root_values(u), roots)
        # The original u velocity vanishes on u=0, off the conductor.
        self.assertTrue(zero(delta(y, u).subs(u, 0)))
        self.assertTrue(zero(delta(z, u).subs(u, 0)))
        self.assertEqual(d.subs(u, 0), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
