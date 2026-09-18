"""Standalone exact controls for the fixed surface's four generators.

No prior checker, solver, or research module is imported. The finite
recognition/Nakayama argument is proved in nodal-elimination-pass23.md.
"""

import unittest

import sympy as sp


u, y, z, t = sp.symbols("u y z t")
i = sp.I
A = (u - 1) * (u - i)
b = (1 - i) * (u + 1) * (u + i) / 4
a = -i * A * (u + (1 + i) / 2) / 2
q = -u * b**2
r = i * u * A / 8
d = u**4 - 1
e = u * d
g = a + b * y
h = q * z + r * y
relation = A * z - y * (y - 1)
uy = (
    (-1 + i) * u**4 / 4 + sp.Rational(3, 2) * u**3
    - 9 * (1 + i) * u**2 / 4 + 4 * i * u + 2 - 2 * i
)
uz = (
    i * u**4 / 8 + (-3 + 3 * i) * u**3 / 8
    - sp.Rational(9, 8) * u**2 - (1 + i) * u - i
)
branches = [
    (sp.Integer(1), 0, 0), (i, 0, 0),
    (sp.Integer(1), 1, 1), (-i, None, 1),
    (sp.Integer(-1), None, 2), (i, 1, 2),
]
tags = [sp.Integer(0), sp.Integer(1), i]
signs = [sp.Integer(1), sp.Integer(-1), sp.Integer(-1)]


def line_substitution(root, epsilon):
    if epsilon is None:
        ar = A.subs(u, root)
        yy = root * ar * t
        zz = root**2 * ar * t**2 - root * t
    else:
        yy = sp.Integer(epsilon)
        zz = root * (2 * epsilon - 1) * t
    return {u: root, y: yy, z: zz}


class FourGeneratorChecks(unittest.TestCase):
    def test_six_original_branch_restrictions(self):
        for root, epsilon, pair in branches:
            with self.subTest(root=root, epsilon=epsilon):
                sub = line_substitution(root, epsilon)
                self.assertEqual(sp.expand(relation.subs(sub)), 0)
                self.assertEqual(sp.simplify(g.subs(sub) - tags[pair]), 0)
                self.assertEqual(sp.simplify(h.subs(sub) - signs[pair] * t), 0)
                self.assertEqual(sp.expand(d.subs(sub)), 0)
                self.assertEqual(sp.expand(e.subs(sub)), 0)

    def test_two_polynomial_bezout_identities(self):
        self.assertEqual(sp.expand(b * uy - u * A * r - 1), 0)
        self.assertEqual(sp.expand(A * uz - u * q - 1), 0)
        self.assertEqual(sp.degree(uy, u), 4)
        self.assertEqual(sp.degree(uz, u), 4)
        for first, second in [(b, A * r), (A, q)]:
            ff = sp.Poly(first, u, extension=i)
            gg = sp.Poly(second, u, extension=i)
            self.assertEqual(sp.gcd(ff, gg).degree(), 0)

    def test_polynomial_recovery_before_quotient(self):
        v = g - a
        yy = uy * v - u * (A * h + u * v * (v - b))
        # These are identities in C[u,y,z], not sampled surface points.
        self.assertEqual(sp.expand(yy - y - u**2 * b**2 * relation), 0)
        zz_using_y = uz * y * (y - 1) - u * (h - r * y)
        self.assertEqual(sp.expand(zz_using_y - z + uz * relation), 0)
        # Replacing y by its recovery changes z by a multiple of the relation.
        error_y = u**2 * b**2 * relation
        zz = uz * yy * (yy - 1) - u * (h - r * yy)
        error_z = -uz * relation + error_y * (uz * (yy + y - 1) + u * r)
        self.assertEqual(sp.expand(zz - z - error_z), 0)

    def test_finiteness_and_off_conductor_recovery(self):
        self.assertEqual(sp.expand(u**4 - d - 1), 0)
        self.assertEqual(sp.expand(e - u * d), 0)
        self.assertEqual(sp.cancel(e / d - u), 0)
        self.assertEqual(sp.degree(u**4 - sp.Symbol("D") - 1, u), 4)
        self.assertEqual(sp.LC(sp.Poly(u**4 - sp.Symbol("D") - 1, u)), 1)

    def test_conductor_points_and_local_coordinates(self):
        self.assertEqual(len(set(tags)), 3)
        for pair in range(3):
            self.assertNotEqual(signs[pair], 0)
        for root, epsilon, pair in branches:
            if epsilon is None:
                self.assertNotEqual(sp.simplify(A.subs(u, root)), 0)
                self.assertNotEqual(sp.simplify(r.subs(u, root)), 0)
            else:
                self.assertNotEqual(2 * epsilon - 1, 0)
                self.assertNotEqual(sp.simplify(q.subs(u, root)), 0)

    def test_full_pinched_cotangent_determinants(self):
        normal_hj, normal_hk = sp.symbols("normal_hj normal_hk")
        for pair in range(3):
            uj = branches[2 * pair][0]
            uk = branches[2 * pair + 1][0]
            matrix = sp.Matrix([
                [4 * uj**3, 4 * uk**3, 0],
                [4 * uj**4, 4 * uk**4, 0],
                [normal_hj, normal_hk, signs[pair]],
            ])
            expected = signs[pair] * 16 * uj**3 * uk**3 * (uk - uj)
            self.assertEqual(sp.expand(matrix.det() - expected), 0)
            self.assertNotEqual(sp.simplify(expected), 0)
            self.assertEqual(
                sp.expand(sp.diff(e, u).subs(u, uj) - 4 * uj**4), 0
            )

    def test_full_conductor_quotient_and_base_relation(self):
        gg = sp.Symbol("G")
        idempotents = []
        for index, tag in enumerate(tags):
            polynomial = sp.Integer(1)
            for other_index, other_tag in enumerate(tags):
                if other_index != index:
                    polynomial *= (gg - other_tag) / (tag - other_tag)
            idempotents.append(sp.expand(polynomial))
        self.assertEqual(sp.simplify(sum(idempotents) - 1), 0)
        for first, polynomial in enumerate(idempotents):
            for second, tag in enumerate(tags):
                self.assertEqual(
                    sp.simplify(polynomial.subs(gg, tag)),
                    sp.Integer(first == second),
                )
        common_parameter_sign = sum(
            signs[index] * polynomial
            for index, polynomial in enumerate(idempotents)
        )
        for pair, tag in enumerate(tags):
            self.assertEqual(
                sp.simplify(
                    signs[pair] * t * common_parameter_sign.subs(gg, tag) - t
                ),
                0,
            )
        self.assertEqual(sp.expand(e**4 - d**4 * (d + 1)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
