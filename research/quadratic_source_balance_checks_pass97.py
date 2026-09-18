"""Bounded exact arithmetic controls for the source-row balance in pass97.

One unittest method checks the two retained full-lattice column controls,
their failure of the new rank-four row balance, seven finite branch tables
of degrees one and two, weighted (2,1) projection cases, and a mixed-degree
cubic boundary. The arithmetic
identity behind the tables is sum_a e_ja * (n / N_j) = n, where
N_j = sum_a e_ja. If their uniform row vector has an integral common factor,
division by that factor remains in the supported lattice.

The weighted controls test sum_i d_i v_i against n/N_j only in the
specified saturated cases. They retain an unsaturated case and a valid
singleton example whose weighted vector is not primitive. Primitivity
of the unweighted sum of a lattice basis must not be transferred to a
weighted sum. These finite identities are separate from the universal
weighted ramification/residue-to-Thom argument.

These are standard-library integer calculations, not a proof that actual
Thom entries equal ramification-times-residue degrees. They do not construct
an original polynomial frame, certify geometric realizability, run an old
suite, or exclude every cubic case.
"""

import itertools
import math
import unittest


def weighted_rows(groups, vector):
    """Apply the disjoint-row ramification map T to an integer vector."""
    if len(vector) != sum(len(group) for group in groups):
        raise ValueError("The vector must have one entry per source label.")
    result = []
    offset = 0
    for group in groups:
        result.append(
            sum(e * vector[offset + a] for a, e in enumerate(group))
        )
        offset += len(group)
    return tuple(result)


def uniform_rows(groups, degree):
    """Return the proposed complete-source row totals n/N_j."""
    if not groups or any(not group or any(e <= 0 for e in group)
                         for group in groups):
        raise ValueError("Each branch group must have positive indices.")
    if any(degree % sum(group) for group in groups):
        raise ValueError("Every cover degree must divide the total degree.")
    return tuple(degree // sum(group)
                 for group in groups for _ in group)


def determinant2(first, second):
    return first[0] * second[1] - first[1] * second[0]


class QuadraticSourceBalanceChecks(unittest.TestCase):
    def test_full_lattice_controls_and_uniform_row_divisibility(self):
        # The (3,1) columns are a full basis of L = Z^2.
        triple_groups = ((1, 1),)
        triple_columns = ((2, 1), (1, 0))
        self.assertEqual(abs(determinant2(*triple_columns)), 1)
        self.assertEqual(
            tuple(weighted_rows(triple_groups, col)
                  for col in triple_columns),
            ((3,), (1,)),
        )
        triple_total = tuple(map(sum, zip(*triple_columns)))
        self.assertEqual(triple_total, (3, 1))
        self.assertEqual(uniform_rows(triple_groups, 4), (2, 2))
        self.assertNotEqual(triple_total, uniform_rows(triple_groups, 4))

        # For (2,2), x+y=2z identifies L with Z^2 via (x,z).
        # Its index-two image in the split (x,y)-plane is not the full basis.
        double_groups = ((1, 1), (2,))
        double_columns = ((1, 1, 1), (2, 0, 1))
        double_basis_coordinates = tuple((col[0], col[2])
                                         for col in double_columns)
        self.assertEqual(abs(determinant2(*double_basis_coordinates)), 1)
        self.assertEqual(
            tuple(weighted_rows(double_groups, col)
                  for col in double_columns),
            ((2, 2), (2, 2)),
        )
        double_total = tuple(map(sum, zip(*double_columns)))
        self.assertEqual(double_total, (3, 1, 2))
        self.assertEqual(uniform_rows(double_groups, 4), (2, 2, 2))
        self.assertNotEqual(double_total, uniform_rows(double_groups, 4))

        # All seven nonempty subsets of these three branch-group types.
        # Repetition of subtests does not create additional unittest methods.
        branch_types = ((1,), (2,), (1, 1))
        tables = tuple(
            groups
            for size in range(1, len(branch_types) + 1)
            for groups in itertools.combinations(branch_types, size)
        )
        self.assertEqual(len(tables), 7)
        for groups in tables:
            with self.subTest(total_degree=4, groups=groups):
                vector = uniform_rows(groups, 4)
                self.assertEqual(weighted_rows(groups, vector),
                                 (4,) * len(groups))
                content = math.gcd(*vector)
                self.assertGreater(content, 1)
                divided = tuple(value // content for value in vector)
                self.assertEqual(weighted_rows(groups, divided),
                                 (4 // content,) * len(groups))
                self.assertEqual(tuple(content * x for x in divided),
                                 vector)

        # Profile (2,1): the double and simple columns form a full basis.
        mixed_groups = ((1, 1),)
        mixed_columns = ((1, 1), (1, 0))
        self.assertEqual(abs(determinant2(*mixed_columns)), 1)
        self.assertEqual(
            tuple(weighted_rows(mixed_groups, col)
                  for col in mixed_columns),
            ((2,), (1,)),
        )
        # Positive degrees with 2*d_double+d_simple <= 4 are exhausted here.
        degree_pairs = tuple(
            (d_double, d_simple)
            for d_double in range(1, 3)
            for d_simple in range(1, 5)
            if 2 * d_double + d_simple <= 4
        )
        self.assertEqual(degree_pairs, ((1, 1), (1, 2)))
        # Saturation at n=3 fails the degree-two constant-field tower.
        self.assertEqual(2 * 1 + 1, 3)
        with self.assertRaises(ValueError):
            uniform_rows(mixed_groups, 3)
        # The remaining saturated case has weighted row totals (3,1).
        saturated_degrees = (1, 2)
        mixed_weighted = tuple(
            sum(degree * col[a]
                for degree, col in zip(saturated_degrees, mixed_columns))
            for a in range(2)
        )
        self.assertEqual(2 * saturated_degrees[0] + saturated_degrees[1], 4)
        self.assertEqual(mixed_weighted, (3, 1))
        self.assertEqual(weighted_rows(mixed_groups, mixed_weighted), (4,))
        self.assertNotEqual(mixed_weighted, uniform_rows(mixed_groups, 4))
        # The unsaturated n=4, degrees (1,1) case does not trigger balance.
        unsaturated_weight = 2 * 1 + 1
        self.assertLess(unsaturated_weight, 4)
        self.assertEqual(tuple(map(sum, zip(*mixed_columns))), (2, 1))

        # A singleton double column (1) is an integral basis. Its degree-two
        # projection has weighted vector (2), which need not be primitive.
        singleton_groups = ((2,),)
        singleton_column = (1,)
        self.assertEqual(math.gcd(*singleton_column), 1)
        self.assertEqual(weighted_rows(singleton_groups, singleton_column),
                         (2,))
        singleton_weighted = tuple(2 * x for x in singleton_column)
        self.assertEqual(singleton_weighted, (2,))
        self.assertEqual(singleton_weighted,
                         uniform_rows(singleton_groups, 4))
        self.assertEqual(weighted_rows(singleton_groups, singleton_weighted),
                         (4,))
        self.assertEqual(math.gcd(*singleton_weighted), 2)

        # A degree-six cover with branch degrees two and three has primitive
        # balanced vector (3,2). This divisibility test gives no exclusion.
        cubic_groups = ((2,), (3,))
        cubic_vector = uniform_rows(cubic_groups, 6)
        self.assertEqual(cubic_vector, (3, 2))
        self.assertEqual(weighted_rows(cubic_groups, cubic_vector), (6, 6))
        self.assertEqual(math.gcd(*cubic_vector), 1)
        # 2x=3y has exactly the integer solutions (x,y)=k(3,2).
        # Bezout 3-2=1 verifies that this displayed generator is primitive.
        self.assertEqual(cubic_vector[0] - cubic_vector[1], 1)

        with self.assertRaises(ValueError):
            uniform_rows(((3,),), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
