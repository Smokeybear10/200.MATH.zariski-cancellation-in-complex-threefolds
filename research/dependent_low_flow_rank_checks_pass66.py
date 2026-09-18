"""Exact finite controls for the dependent degree-two joint-rank bound.

The Jordan and companion controls are linear algebra, not proposed actions.
The actual model is the already recorded pass42 rank-two leading boundary.
It checks new full companion accounting, not a new realization or a proof
of the universal recognition/source gates. The strengthened argument uses
no speed-rank or nonconstant-projective-speed hypothesis.
"""

import unittest

import sympy as sp


class DependentLowFlowRankChecks(unittest.TestCase):
    def same(self, left, right):
        difference = left - right
        if isinstance(difference, sp.MatrixBase):
            self.assertEqual(difference.applyfunc(sp.expand), sp.zeros(*difference.shape))
        else:
            self.assertEqual(sp.expand(difference), 0)

    @staticmethod
    def partitions(total, maximum):
        if total == 0:
            yield ()
        for first in range(min(total, maximum), 0, -1):
            for tail in DependentLowFlowRankChecks.partitions(total - first, first):
                yield (first,) + tail

    @staticmethod
    def jordan(parts):
        result = sp.zeros(sum(parts))
        offset = 0
        for size in parts:
            for i in range(size - 1):
                result[offset + i, offset + i + 1] = 1
            offset += size
        return result

    def test_five_dimensional_cube_zero_rank_alternatives(self):
        high_rank = []
        for parts in self.partitions(5, 3):
            M = self.jordan(parts)
            self.same(M**3, sp.zeros(5))
            self.assertLessEqual((M**2).rank(), 1)
            if M**2 == sp.zeros(5):
                self.assertLessEqual(M.rank(), 2)
            if M.rank() >= 3:
                high_rank.append(parts)
                self.assertEqual(M.rank(), 3)
                self.assertEqual((M**2).rank(), 1)
                self.assertEqual(len(M.nullspace()), 2)
                line = (M**2).columnspace()[0]
                relations = M.row_join(-line)
                preimage = sp.Matrix.hstack(*(vector[:5, :] for vector in relations.nullspace()))
                self.assertEqual(preimage.rank(), 3)
                self.assertEqual(M.row_join(preimage).rank(), 3)
        self.assertEqual(high_rank, [(3, 2)])

    def test_full_companions_and_horizontal_preimage_gate(self):
        e = sp.eye(5)
        N = self.jordan((3, 2))
        # Both changes are exact invertible basis changes. In each split,
        # the fifth diagonal entry is zero and the bottom good entries vanish.
        zero_bottom = sp.Matrix.hstack(e[:, 0], e[:, 3], e[:, 2], e[:, 4], e[:, 1])
        auxiliary = e[:, 1] + e[:, 4]
        nonzero_bottom = sp.Matrix.hstack(
            e[:, 0] - auxiliary,
            e[:, 1] - e[:, 2] + e[:, 3],
            e[:, 2],
            e[:, 4],
            auxiliary,
        )
        for change, expected_bottom_rank in ((zero_bottom, 0), (nonzero_bottom, 1)):
            self.assertIn(change.det(), (-1, 1))
            M = change.inv() * N * change
            J, d, ell = M[:4, :4], -2 * M[:4, 4], M[4:5, :4]
            self.same(M[4, 4], 0)
            self.same(ell[:, :2], sp.zeros(1, 2))
            self.assertNotEqual(d, sp.zeros(4, 1))
            self.assertNotEqual(ell, sp.zeros(1, 4))
            self.same(M**3, sp.zeros(5))
            self.assertEqual((M**2).rank(), 1)
            self.assertEqual((M**2)[:4, :4].rank(), 1)
            self.assertEqual((M**2)[4:5, :].rank(), expected_bottom_rank)

            time = sp.symbols("time")
            conjugated = sp.eye(4) - time * J + time**2 * d * ell / 2
            inverse = sp.eye(4) + time * J + time**2 * (M**2)[:4, :4]
            self.same(conjugated * inverse, sp.eye(4))
            self.same(inverse * conjugated, sp.eye(4))

            image_line = (M**2).columnspace()[0]
            full_relations = M.row_join(-image_line)
            full_preimage = sp.Matrix.hstack(
                *(vector[:5, :] for vector in full_relations.nullspace())
            )
            # M^{-1}(im M^2)=im M for the full (3,2) companion. Its
            # image has a nonzero auxiliary projection, so it cannot
            # equal any three-dimensional horizontal subspace.
            self.assertEqual(full_preimage.rank(), 3)
            self.assertEqual(M.row_join(full_preimage).rank(), 3)
            self.assertEqual(M[4:5, :].rank(), 1)
            # Solve M(x,0)=lambda*image_line, retaining the auxiliary row.
            relations = M[:, :4].row_join(-image_line)
            solutions = relations.nullspace()
            horizontal_preimage = sp.Matrix.hstack(*(vector[:4, :] for vector in solutions))
            self.assertEqual(horizontal_preimage.rank(), 2)
            horizontal_kernel = M[:, :4].nullspace()
            self.assertEqual(len(horizontal_kernel), 2 - expected_bottom_rank)

            # These are the exact good-column and auxiliary-column identities.
            for i in (0, 1):
                good_top = (-J[:, i]).col_join(sp.zeros(1, 1))
                self.same(M * good_top, -(M**2)[:, i])
            self.same(M * d.col_join(sp.zeros(1, 1)), -2 * (M**2)[:, 4])

    def test_actual_rank_two_boundary_and_its_weighted_companion(self):
        u, v, A, C = sp.symbols("u v A C")
        variables = (u, v, A, C)
        f, g = u + v, (u + v)**2 + 1
        physical = sp.Matrix([u + A**2 / 2, v + C**2 / 2, A, C])
        frame_jacobian = physical.jacobian(variables)
        partials = frame_jacobian.inv()
        velocity = sp.Matrix([0, 0, f, g])

        def bracket(left, right):
            return (right.jacobian(variables) * left - left.jacobian(variables) * right).applyfunc(sp.expand)

        middle = [bracket(velocity, partials[:, i]) for i in range(4)]
        defects = [bracket(velocity, middle[i]) for i in (2, 3)]
        primitive = sp.Matrix([0, 0, 1, 2 * f])
        self.same(defects[0], 2 * f * primitive)
        self.same(defects[1], 2 * g * primitive)
        for i in (0, 1):
            self.same(bracket(velocity, middle[i]), sp.zeros(4, 1))
        for defect in defects:
            self.same(bracket(velocity, defect), sp.zeros(4, 1))
        self.assertEqual(sp.Matrix.hstack(*defects).rank(), 1)
        self.assertEqual(sp.Matrix.hstack(velocity, middle[0], middle[1], *defects).rank(), 2)
        self.same((C - f * A).diff(A) * f + (C - f * A).diff(C) * g, 1)

        P = frame_jacobian * velocity
        J = P.jacobian(variables) * partials
        h = P.jacobian(variables) * velocity
        self.same(h, sp.Matrix([f**2, g**2, 0, 0]))
        self.same(h.jacobian(variables) * velocity, sp.zeros(4, 1))
        d = frame_jacobian * primitive
        ell = sp.Matrix([[0, 0, 2 * f, 2 * g]])
        M = J.row_join(-d / 2).col_join(ell.row_join(sp.zeros(1, 1)))
        self.same(M**3, sp.zeros(5))
        self.assertEqual(M.rank(), 3)
        self.assertEqual((M**2).rank(), 1)
        self.same((M**2)[:4, :4], h.jacobian(variables) * partials / 2)
        scalar_s = (ell * P)[0]
        self.same(M * P.col_join(sp.zeros(1, 1)), h.col_join(sp.Matrix([scalar_s])))

        # The actual q=2 boundary need not satisfy the proportional-H branch.
        H = h[:2, :]
        self.assertNotEqual(sp.factor(sp.Matrix.hstack(H, H.diff(u)).det()), 0)
        self.assertEqual((M**2).row_join(M * P.col_join(sp.zeros(1, 1))).rank(), 2)
        self.assertEqual(sp.Matrix.hstack(-J[:, 0], -J[:, 1], d).rank(), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
