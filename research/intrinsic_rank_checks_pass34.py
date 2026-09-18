"""Finite exact controls for the geometric generic class-group calculation.

Only unittest and SymPy are imported. The written proof, not this suite,
establishes the geometric hypotheses, the complete divisor relations,
and the quantifier over every invariant-plane coordinate. In particular,
none of these controls proves a universal intrinsic LND rank bound.
"""

import unittest

import sympy as sp


class IntrinsicRankChecks(unittest.TestCase):
    def test_canonical_jacobian_and_minimal_slice_identities(self):
        x, y, z = sp.symbols("x y z")
        f = x * z - y**2
        r = x**3 + y * f
        h = z * f**2 + 2 * x**2 * y * f + x**5

        def derivative(expression):
            return sp.expand(sp.Matrix([
                [sp.diff(f, variable) for variable in (x, y, z)],
                [sp.diff(h, variable) for variable in (x, y, z)],
                [sp.diff(expression, variable) for variable in (x, y, z)],
            ]).det())

        expected = (-2 * f * r, 6 * x**2 * r - h,
                    2 * x * (5 * y * r + f**2))
        for variable, image in zip((x, y, z), expected):
            self.assertEqual(sp.expand(derivative(variable) - image), 0)
        self.assertEqual(derivative(f), 0)
        self.assertEqual(derivative(h), 0)
        self.assertEqual(sp.expand(derivative(r) + f * h), 0)
        self.assertEqual(sp.expand(x * h - r**2 - f**3), 0)
        self.assertEqual(sp.gcd_list([derivative(v) for v in (x, y, z)]), 1)

    def test_f_boundary_chart_and_degree_five_cover(self):
        x, y, z, H, U = sp.symbols("x y z H U")
        f = x * z - y**2
        r = x**3 + y * f
        h = z * f**2 + 2 * x**2 * y * f + x**5
        chart = {z: y**2 / x}
        self.assertEqual(sp.cancel(f.subs(chart)), 0)
        self.assertEqual(sp.cancel(r.subs(chart)), x**3)
        self.assertEqual(sp.cancel(h.subs(chart)), x**5)
        self.assertEqual(sp.cancel((-2 * f * r).subs(chart)), 0)
        self.assertEqual(sp.cancel((6 * x**2 * r - h).subs(chart)), 5 * x**5)
        relation = sp.Poly(U**5 - H, U, domain=sp.QQ.frac_field(H))
        self.assertEqual(relation.degree(), 5)
        self.assertEqual(sp.gcd(relation, relation.diff()).as_expr(), 1)
        # Monic division gives the five displayed residue-basis candidates.
        # Irreducibility over C(H) is the written Eisenstein/cover argument.
        for degree in range(5):
            self.assertEqual(sp.rem(U**degree, relation.as_expr(), U), U**degree)
        self.assertEqual(sp.rem(U**5, relation.as_expr(), U), H)

    def test_h_boundary_rational_inverse_and_degree_two_cover(self):
        x, y, z, F, R, X = sp.symbols("x y z F R X")
        f = x * z - y**2
        r = x**3 + y * f
        h = z * f**2 + 2 * x**2 * y * f + x**5
        old_y = (R - X**3) / F
        old_z = (F + old_y**2) / X
        chart = {x: X, y: old_y, z: old_z}
        self.assertEqual(sp.cancel(f.subs(chart, simultaneous=True)), F)
        self.assertEqual(sp.cancel(r.subs(chart, simultaneous=True)), R)
        self.assertEqual(sp.cancel(h.subs(chart, simultaneous=True)),
                         (R**2 + F**3) / X)
        dx = sp.cancel((-2 * f * r).subs(chart, simultaneous=True))
        dr = sp.cancel((-f * h).subs(chart, simultaneous=True))
        self.assertEqual(dx, -2 * F * R)
        relation = sp.Poly(R**2 + F**3, R, domain=sp.QQ.frac_field(F))
        self.assertEqual(relation.degree(), 2)
        self.assertEqual(sp.gcd(relation, relation.diff()).as_expr(), 1)
        self.assertEqual(sp.cancel(dr * X / relation.as_expr()), -F)
        self.assertEqual(sp.rem(R**2, relation.as_expr(), R), -F**3)
        # The odd F-valuation of -F^3 excludes a square in C(F).
        self.assertEqual(sp.Poly(-F**3, F).terms(), [((3,), -1)])

    def test_boundary_block_relations_have_no_integral_torsion(self):
        for block_sizes in ((5, 2), (2,), (2, 3, 5), (5, 5, 2)):
            with self.subTest(block_sizes=block_sizes):
                size = sum(block_sizes)
                relations = []
                complements = []
                offset = 0
                for block_size in block_sizes:
                    relation = sp.zeros(size, 1)
                    for index in range(offset, offset + block_size):
                        relation[index] = 1
                    relations.append(relation)
                    # The sum vector together with all but the final
                    # basis vector is an integral basis of this block.
                    for index in range(offset, offset + block_size - 1):
                        complements.append(sp.eye(size)[:, index])
                    offset += block_size
                complete_basis = sp.Matrix.hstack(*(relations + complements))
                self.assertEqual(abs(complete_basis.det()), 1)
                relation_matrix = sp.Matrix.hstack(*relations)
                self.assertEqual(relation_matrix.rank(), len(block_sizes))
                self.assertEqual(len(complements),
                                 sum(degree - 1 for degree in block_sizes))
                if block_sizes == (5, 2):
                    self.assertEqual(len(complements), 5)

    def test_nonlinear_plane_coordinates_and_unbounded_rank_formula(self):
        f, h, a, b = sp.symbols("f h a b")
        for exponent in range(1, 7):
            with self.subTest(exponent=exponent):
                forward = (f + h**exponent, h)
                inverse = {f: a - b**exponent, h: b}
                self.assertEqual(tuple(sp.expand(expression.subs(
                    inverse, simultaneous=True)) for expression in forward), (a, b))
                self.assertEqual(sp.expand((a - b**exponent).subs(
                    {a: forward[0], b: forward[1]}, simultaneous=True)), f)
                determinant = sp.Matrix(forward).jacobian((f, h)).det()
                self.assertEqual(determinant, 1)
                horizontal_f = sp.Poly(a - b**exponent, b,
                                       domain=sp.QQ.frac_field(a))
                horizontal_h = sp.Poly(b, b, domain=sp.QQ.frac_field(a))
                self.assertEqual(horizontal_f.degree(), exponent)
                self.assertEqual(horizontal_h.degree(), 1)
                self.assertEqual(sp.gcd(horizontal_f, horizontal_f.diff()).as_expr(), 1)
                self.assertEqual(sp.gcd(horizontal_f, horizontal_h).as_expr(), 1)
                relation_rank = horizontal_f.degree() * (5 - 1) + (2 - 1)
                self.assertEqual(relation_rank, 4 * exponent + 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
