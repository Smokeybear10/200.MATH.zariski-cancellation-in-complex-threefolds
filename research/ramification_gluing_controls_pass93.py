"""Finite integer-lattice and curve-ring controls, not action realization."""

from itertools import product
from math import gcd, lcm
import unittest


def determinant(matrix):
    """Exact determinant of the small square integer matrices used below."""
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("A square matrix is required")
    if size == 0:
        return 1
    return sum(
        (-1) ** col * matrix[0][col]
        * determinant([row[:col] + row[col + 1:] for row in matrix[1:]])
        for col in range(size)
    )


def image(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def support_compatible(columns, point_labels):
    """A column must meet at most one actual point of the source curve."""
    return all(
        len({point_labels[j] for j, value in enumerate(col) if value}) <= 1
        for col in columns
    )


def basis_index(columns, cross=False):
    """Index in the stated whole lattice; reject columns outside it."""
    if cross:
        if any(len(v) != 3 or v[0] + v[1] != 2 * v[2] for v in columns):
            raise ValueError("Not in x+y=2z")
        coordinates = [(v[0], v[2]) for v in columns]
        for original, (x, z) in zip(columns, coordinates):
            if original != (x, 2 * z - x, z):
                raise ValueError("The integral lattice inverse failed")
    else:
        coordinates = columns
    matrix = [list(row) for row in zip(*coordinates)]
    return abs(determinant(matrix))


# A polynomial is an ascending tuple of integer coefficients.
def poly(coefficients):
    values = list(coefficients)
    while values and values[-1] == 0:
        values.pop()
    return tuple(values)


ZERO, ONE = (), (1,)
VARIABLE = (0, 1)


def add(left, right):
    return poly(
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(max(len(left), len(right)))
    )


def scale(value, factor):
    return poly(factor * item for item in value)


def multiply(left, right):
    if not left or not right:
        return ZERO
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return poly(result)


def power(value, exponent):
    if exponent < 0:
        raise ValueError("Nonnegative exponent required")
    result = ONE
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def compose(value, argument):
    result = ZERO
    for coefficient in reversed(value):
        result = add(multiply(result, argument), (coefficient,))
    return result


def evaluate(value, argument):
    result = 0
    for coefficient in reversed(value):
        result = result * argument + coefficient
    return result


def derivative(value):
    return poly(i * value[i] for i in range(1, len(value)))


def constant(value):
    return value[0] if value else 0


def cn_basis_product(n, j, k):
    """Structure constants over Z[t], for e0=1 and ej=t*w**j."""
    result = [ZERO] * n
    if j == 0 or k == 0:
        result[j + k] = ONE
        return result
    quotient, remainder = divmod(j + k, n)
    coefficient = multiply(
        power(VARIABLE, 2 if remainder == 0 else 1),
        power((1, 1), quotient),
    )
    result[remainder] = coefficient
    return result


def cn_multiply(left, right):
    n = len(left)
    result = [ZERO] * n
    for j, k in product(range(n), repeat=2):
        factor = multiply(left[j], right[k])
        for index, coefficient in enumerate(cn_basis_product(n, j, k)):
            result[index] = add(result[index], multiply(factor, coefficient))
    return result


class RamificationGluingControls(unittest.TestCase):
    def test_full_lattices_weighted_columns_and_actual_point_support(self):
        cases = [
            ("four_one", ((1, 1),), ((3, 1), (1, 0)), (4, 1), ((1, 1),), False),
            ("five_one", ((1, 1),), ((4, 1), (1, 0)), (5, 1), ((1, 1),), False),
            ("four_one_one", ((1, 1, 1),), ((2, 1, 1), (1, 0, 0), (0, 1, 0)),
             (4, 1, 1), ((1, 1, 1),), False),
            ("four_two", ((1, 1, 0), (0, 0, 2)), ((1, 3, 2), (1, 1, 1)),
             (4, 2), ((1, 1), (2,)), True),
        ]
        for name, matrix, columns, multiplicities, branch_indices, cross in cases:
            with self.subTest(profile=name):
                rows, normalization_points = len(matrix), len(matrix[0])
                self.assertEqual(len(columns), normalization_points - rows + 1)
                self.assertEqual(basis_index(columns, cross), 1)
                for col, multiplicity in zip(columns, multiplicities):
                    self.assertTrue(all(value >= 0 for value in col))
                    self.assertEqual(image(matrix, col), (multiplicity,) * rows)
                branch_gcds = [gcd(*indices) for indices in branch_indices]
                self.assertEqual(gcd(*multiplicities), lcm(*branch_gcds))
                self.assertTrue(all(sum(indices) in (2, 3) for indices in branch_indices))
                self.assertTrue(support_compatible(columns, [0] * normalization_points))

        # Same positive multiplicities (4,1), but index two, not a whole basis.
        index_two = ((2, 2), (1, 0))
        self.assertEqual([image(((1, 1),), col)[0] for col in index_two], [4, 1])
        self.assertEqual(basis_index(index_two), 2)
        self.assertNotEqual(basis_index(index_two), 1)

        # A full basis with the right multiplicities still fails unglued support.
        full_but_unglued = ((3, 1), (1, 0))
        self.assertEqual(basis_index(full_but_unglued), 1)
        self.assertFalse(support_compatible(full_but_unglued, ["plus", "minus"]))
        self.assertFalse(support_compatible(
            ((1, 3, 2), (1, 1, 1)), ["plus", "minus", "axis_origin"]
        ))
        with self.assertRaises(ValueError):
            basis_index(((1, 1, 0), (0, 0, 1)), cross=True)

    def test_finite_curve_multiplication_and_nonreduced_glued_fibers(self):
        w = VARIABLE
        for n in (2, 3):
            with self.subTest(curve=f"C_{n}"):
                t_of_w = add(power(w, n), (-1,))
                embedded_basis = [ONE] + [
                    multiply(t_of_w, power(w, j)) for j in range(1, n)
                ]
                module_basis = [
                    [ONE if i == j else ZERO for i in range(n)] for j in range(n)
                ]
                for j, k in product(range(n), repeat=2):
                    coefficients = cn_basis_product(n, j, k)
                    embedded_product = ZERO
                    for coefficient, basis_element in zip(coefficients, embedded_basis):
                        embedded_product = add(embedded_product, multiply(
                            compose(coefficient, t_of_w), basis_element
                        ))
                    self.assertEqual(
                        embedded_product, multiply(embedded_basis[j], embedded_basis[k])
                    )
                    if j and k:
                        self.assertTrue(all(constant(a) == 0 for a in coefficients))
                    else:
                        self.assertEqual(coefficients, module_basis[j + k])

                for i, j, k in product(range(n), repeat=3):
                    self.assertEqual(
                        cn_multiply(cn_multiply(module_basis[i], module_basis[j]), module_basis[k]),
                        cn_multiply(module_basis[i], cn_multiply(module_basis[j], module_basis[k])),
                    )
                # The reduced normalization fiber is w**n=1. All ej, j>0,
                # contain its defining polynomial. Its roots are unramified:
                # w*(dt/dw)=n*(t+1), which is the nonzero constant n there.
                self.assertEqual(multiply(w, derivative(t_of_w)), scale(power(w, n), n))
                for j in range(1, n):
                    self.assertEqual(embedded_basis[j], multiply(t_of_w, power(w, j)))
                # In the actual finite fiber, the n-1 nonconstant module-basis
                # classes remain independent, while all their products vanish.
                self.assertEqual(len(module_basis), n)
                self.assertEqual(sum(constant(a) for a in module_basis[0]), 1)

        # C_cross: pairs of polynomials with f(1)=f(-1)=g(0).
        # Finite G-module generators are 1, beta=(t*w,0), alpha=(0,a).
        zero_pair, unit_pair = (ZERO, ZERO), (ONE, ONE)
        pair_add = lambda p, q: (add(p[0], q[0]), add(p[1], q[1]))
        pair_mul = lambda p, q: (multiply(p[0], q[0]), multiply(p[1], q[1]))
        a = VARIABLE
        t = (add(power(w, 2), (-1,)), ZERO)
        s = (ZERO, power(a, 2))
        beta = (multiply(t[0], w), ZERO)
        alpha = (ZERO, a)
        glued = lambda p: evaluate(p[0], 1) == evaluate(p[0], -1) == evaluate(p[1], 0)
        for generator in (unit_pair, t, s, beta, alpha):
            self.assertTrue(glued(generator))
        self.assertEqual(pair_mul(t, s), zero_pair)
        self.assertEqual(pair_mul(alpha, alpha), s)
        self.assertEqual(pair_mul(alpha, beta), zero_pair)
        self.assertEqual(pair_mul(t, alpha), zero_pair)
        self.assertEqual(pair_mul(s, beta), zero_pair)
        self.assertEqual(
            pair_mul(beta, beta),
            pair_mul(pair_mul(t, t), pair_add(t, unit_pair)),
        )
        for left, right in product((unit_pair, beta, alpha), repeat=2):
            self.assertTrue(glued(pair_mul(left, right)))
        # beta^2=t^2(t+1), alpha^2=s, alpha*beta=0 imply a
        # square-zero radical in the three-dimensional fiber t=s=0.
        self.assertEqual(derivative(s[1]), (0, 2))
        self.assertEqual(evaluate(derivative(t[0]), 1), 2)
        self.assertEqual(evaluate(derivative(t[0]), -1), -2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
