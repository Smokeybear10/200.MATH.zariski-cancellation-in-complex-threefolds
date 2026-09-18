"""Independent finite integer-lattice controls, not a topology formalization."""

import unittest

import sympy as sp


def subsets(items, size):
    if size == 0:
        yield ()
    elif len(items) >= size:
        for tail in subsets(items[1:], size - 1):
            yield (items[0],) + tail
        yield from subsets(items[1:], size)


def branch_matrix(groups):
    matrix = sp.zeros(len(groups), sum(map(len, groups)))
    column = 0
    for row, indices in enumerate(groups):
        for index in indices:
            matrix[row, column] = index
            column += 1
    return matrix


def quotient_order(groups):
    matrix = branch_matrix(groups).row_join(sp.ones(len(groups), 1))
    # The gcd of maximal minors is the index of this full-rank lattice.
    minors = [abs(matrix[:, columns].det())
              for columns in subsets(tuple(range(matrix.cols)), matrix.rows)]
    return int(sp.gcd_list(minors))


def predicted_order(groups):
    gcds = [int(sp.gcd_list(group)) for group in groups]
    return int(sp.prod(gcds) // sp.ilcm(*([1] + gcds)))


class IntegralRamificationChecks(unittest.TestCase):
    def test_weighted_groups_against_maximal_minor_lattice_index(self):
        examples = (
            ((2, 3), (6, 10)),
            ((4, 8), (6, 9)),
            ((6, 12), (10,), (15, 30)),
            ((1, 1), (1, 1)),
            ((2, 4), (3, 9), (5, 10)),
            ((4,), (6,), (8,), (12,)),
        )
        for groups in examples:
            with self.subTest(groups=groups):
                self.assertEqual(quotient_order(groups), predicted_order(groups))

    def test_pairwise_coprimality_criterion_on_single_point_branches(self):
        for first in range(1, 8):
            for second in range(1, 8):
                for third in range(1, 6):
                    values = (first, second, third)
                    coprime = all(sp.gcd(values[i], values[j]) == 1
                                  for i in range(3) for j in range(i))
                    self.assertEqual(quotient_order(tuple((v,) for v in values)) == 1,
                                     coprime)
                    ell = sp.ilcm(*values)
                    column = sp.Matrix([ell // value for value in values])
                    self.assertEqual(sp.diag(*values) * column, ell * sp.ones(3, 1))
                    self.assertEqual(sp.gcd_list(list(column)), 1)
                    if coprime:
                        self.assertEqual(ell, sp.prod(values))

    def test_common_index_obstruction_and_one_branch_boundary(self):
        for index in range(1, 9):
            for branches in range(1, 6):
                self.assertEqual(quotient_order(((index,),) * branches),
                                 index ** (branches - 1))
        for group in ((2,), (12,), (6, 9), (4, 10, 14)):
            self.assertEqual(quotient_order((group,)), 1)

    def test_node_is_unobstructed_but_two_double_branches_are_not(self):
        self.assertEqual(quotient_order(((1, 1), (1, 1))), 1)
        self.assertEqual(quotient_order(((2,), (2,))), 2)
        self.assertEqual(quotient_order(((2,), (3,))), 1)
        self.assertEqual(quotient_order(((2, 3), (2,))), 1)
        self.assertEqual(quotient_order(((6,), (2,))), 2)
        # Actual established crossing-plinth control: degrees 5 and 2,
        # with a length-ten transverse fiber and primitive source column.
        self.assertEqual(quotient_order(((5,), (2,))), 1)
        self.assertEqual(sp.diag(5, 2) * sp.Matrix([2, 5]), sp.Matrix([10, 10]))
        x, y = sp.symbols("x y")
        f = x - y**2
        h = f**2 + 2 * x**2 * y * f + x**5
        self.assertEqual(tuple(sp.groebner((f, h), x, y)), (x - y**2, y**10))


if __name__ == "__main__":
    unittest.main(verbosity=2)
