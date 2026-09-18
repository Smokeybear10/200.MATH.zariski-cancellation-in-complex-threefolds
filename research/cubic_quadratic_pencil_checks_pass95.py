"""Finite leading-frame and Artin controls, not a verifier of the general proof.

The polynomial fields below live on a normal associated-graded three-ring.
Neither the fields nor the Artin ideals are asserted to lift to the original
four-coordinate action. Exactly one unittest method is provided.
"""

import itertools
import unittest

import sympy as S


class CubicQuadraticPencilControls(unittest.TestCase):
    def test_sharp_normal_frame_and_artin_lengths(self):
        xi, eta, c = S.symbols("xi eta c")
        p, q = S.symbols("p q")
        variables = (xi, eta, c)

        for exponent in (3, 4):
            with self.subTest(normal_frame_degree=exponent):
                matrix = S.Matrix([[1, 0], [c**exponent, 1]])
                inverse = S.Matrix([[1, 0], [-c**exponent, 1]])
                self.assertEqual(matrix * inverse, S.eye(2))
                self.assertEqual(inverse * matrix, S.eye(2))
                self.assertEqual(matrix.det(), 1)
                leading_p, leading_q = xi, eta + c**exponent * xi
                backward = {xi: p, eta: q - c**exponent * p}
                self.assertEqual(leading_p.subs(backward, simultaneous=True), p)
                self.assertEqual(
                    S.expand(leading_q.subs(backward, simultaneous=True) - q), 0
                )
                self.assertEqual(
                    S.expand((q - c**exponent * p).subs(
                        {p: leading_p, q: leading_q}, simultaneous=True
                    ) - eta), 0
                )

                def field(value):
                    return S.expand(
                        xi**2 * S.diff(value, c)
                        - exponent * c**(exponent - 1) * xi**3
                        * S.diff(value, eta)
                    )

                self.assertEqual(field(leading_p), 0)
                self.assertEqual(field(leading_q), 0)
                self.assertEqual(field(c), xi**2)
                self.assertEqual(field(field(c)), 0)
                first, second = leading_p**2, leading_p * leading_q
                for coordinate in variables:
                    jacobian = S.Matrix([
                        [S.diff(value, variable) for variable in variables]
                        for value in (first, second, coordinate)
                    ]).det()
                    self.assertEqual(S.expand(jacobian - 2 * field(coordinate)), 0)

                iterate = eta
                values = []
                for _ in range(4):
                    iterate = field(iterate)
                    values.append(iterate)
                if exponent == 3:
                    self.assertEqual(values[2], -6 * xi**7)
                    self.assertEqual(values[3], 0)
                else:
                    # This is still a polynomial LND, but fails the actual
                    # fourth-derivative constraint on the original normal eta.
                    self.assertEqual(values[3], -24 * xi**9)
                    self.assertNotEqual(values[3], 0)

        x, y = S.symbols("x y")
        cases = (
            ((x**2 + y**3, x*y), 5, [5, 4, 2, 1, 0]),
            ((x**2, x*y + y**3), 6, [6, 5, 3, 2, 1, 0]),
        )
        for generators, length, expected_ranks in cases:
            with self.subTest(artin_length=length):
                groebner = S.groebner(generators, x, y, order="lex", domain=S.QQ)
                leading = [poly.LM(order=groebner.order).exponents
                           for poly in groebner.polys]
                pure_bounds = [
                    min(monomial[index] for monomial in leading
                        if monomial[index] > 0
                        and all(monomial[j] == 0 for j in range(2) if j != index))
                    for index in range(2)
                ]
                standard = [
                    exponent
                    for exponent in itertools.product(*(range(b) for b in pure_bounds))
                    if not any(all(a >= b for a, b in zip(exponent, divisor))
                               for divisor in leading)
                ]
                expected = {(1, 0)} | {(0, power) for power in range(length - 1)}
                self.assertEqual(set(standard), expected)
                self.assertEqual(len(standard), length)

                basis = [x**i * y**j for i, j in standard]

                def residue_vector(value):
                    remainder = groebner.reduce(S.expand(value))[1]
                    polynomial = S.Poly(remainder, x, y, domain=S.QQ)
                    self.assertTrue(set(polynomial.monoms()) <= set(standard)
                                    or polynomial.is_zero)
                    return S.Matrix([polynomial.coeff_monomial(monomial)
                                     for monomial in basis])

                multiplication_x = S.Matrix.hstack(
                    *(residue_vector(x * monomial) for monomial in basis)
                )
                multiplication_y = S.Matrix.hstack(
                    *(residue_vector(y * monomial) for monomial in basis)
                )
                self.assertEqual(multiplication_x * multiplication_y,
                                 multiplication_y * multiplication_x)
                self.assertEqual(residue_vector(y**(length - 1)), S.zeros(length, 1))
                self.assertNotEqual(residue_vector(y**(length - 2)),
                                    S.zeros(length, 1))

                current = S.eye(length)
                ranks = [length]
                for _ in range(length):
                    next_space = S.Matrix.hstack(multiplication_x * current,
                                                multiplication_y * current)
                    columns = next_space.columnspace()
                    ranks.append(len(columns))
                    if not columns:
                        break
                    current = S.Matrix.hstack(*columns)
                self.assertEqual(ranks, expected_ranks)
                # These exact ranks retain the nonhomogeneous ideal powers,
                # not just the total degrees of a chosen standard basis.


if __name__ == "__main__":
    unittest.main(verbosity=2)
