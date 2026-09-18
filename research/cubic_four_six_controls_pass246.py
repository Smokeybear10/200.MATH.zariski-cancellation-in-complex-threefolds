"""Finite algebra controls for the written (4,6) exclusion in pass246.

This standalone suite must be read before a separately authorized run.
It imports no retained checker. Its examples do not certify universal
trace duality, the conductor theorem, the formal-branch argument,
birationality of an arbitrary parametrization, or any actual sliced frame.
Those assertions are proved with their exact hypotheses in the note.

The controls independently construct multiplication matrices by polynomial
remainders. They check bounded monogenic dual pairings, the required
Laurent coefficients, full symbolic quartic traces, and an explicit
nonbirational boundary where characteristic and minimal degrees differ.
"""

import unittest

import sympy as sp


def multiplication_matrix(element, relation, variable):
    """Multiply by element in the displayed monic polynomial quotient."""
    size = sp.Poly(relation, variable).degree()
    columns = []
    for power in range(size):
        remainder = sp.Poly(
            sp.rem(element * variable**power, relation, variable), variable
        )
        columns.append(
            sp.Matrix(
                [remainder.coeff_monomial(variable**row) for row in range(size)]
            )
        )
    return sp.Matrix.hstack(*columns)


def polynomial_part_and_tail(y_polynomial, x, degree, last_power):
    """Finite expansion of y**(degree/4), with y monic of degree four.

    The auxiliary w equals 1/x. Terms through w**last_power are returned.
    In particular, this is a finite Taylor calculation, not a test of the
    existence or uniqueness of the full inverse formal Laurent series.
    """
    w = sp.Dummy("inverse_x")
    unit = sp.expand(y_polynomial.subs(x, 1 / w) * w**4)
    truncated = sp.series(
        unit ** sp.Rational(degree, 4),
        w,
        0,
        degree + last_power + 1,
    ).removeO()
    expansion = sp.expand(truncated / w**degree)
    polynomial_part = sp.expand(
        sum(expansion.coeff(w, -power) * x**power for power in range(degree + 1))
    )
    tail = {power: expansion.coeff(w, power) for power in range(1, last_power + 1)}
    return polynomial_part, tail


class CubicFourSixControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def assert_zero_matrix(self, matrix):
        for entry in matrix:
            self.assert_zero(entry)

    def test_bounded_monogenic_trace_dual_pairings(self):
        """Three literal orders, not a universal conductor certification."""
        x, u, z = sp.symbols("x u z")
        examples = (
            (x**2, x**3 + x),
            (x**3, x**4 + x**2),
            (x**4 + x, x**3),
        )
        for y, psi in examples:
            with self.subTest(y=y, psi=psi):
                relation = y - u
                size = sp.degree(y, x)
                identity = sp.eye(size)
                mx = multiplication_matrix(x, relation, x)
                mp = multiplication_matrix(psi, relation, x)
                minimum = sp.expand(mp.charpoly(z).as_expr())
                derivative_p = sp.diff(minimum, z).subs(z, psi)
                derivative_x = sp.diff(y, x)
                dx = multiplication_matrix(derivative_x, relation, x)
                dp = multiplication_matrix(derivative_p, relation, x)

                # In these bounded examples the characteristic roots of psi
                # are distinct: its derivative matrix is invertible.
                self.assertNotEqual(sp.factor(dp.det()), 0)
                for generator, derivative in ((mx, dx), (mp, dp)):
                    inverse = derivative.inv()
                    pairing = sp.Matrix(
                        size,
                        size,
                        lambda i, j: sp.cancel(
                            sp.trace(generator ** (i + j) * inverse)
                        ),
                    )
                    for i in range(size):
                        for j in range(size):
                            if i + j < size - 1:
                                self.assert_zero(pairing[i, j])
                            elif i + j == size - 1:
                                self.assert_zero(pairing[i, j] - 1)
                            self.assertIsNotNone(pairing[i, j].as_poly(u))
                    expected_sign = (-1) ** (size * (size - 1) // 2)
                    self.assert_zero(pairing.det() - expected_sign)

                # Finite counterpart of G_psi/y': verify it is polynomial
                # here and that its multiples by the O-basis lie in C.
                conductor_candidate = sp.cancel(
                    derivative_p.subs(u, y) / derivative_x
                )
                self.assertIsNotNone(conductor_candidate.as_poly(x))
                mc = multiplication_matrix(conductor_candidate, relation, x)
                self.assert_zero_matrix(mc * dx - dp)
                unit_vector = identity[:, 0]
                c_basis = sp.Matrix.hstack(
                    *[mp**power * unit_vector for power in range(size)]
                )
                self.assertNotEqual(sp.factor(c_basis.det()), 0)
                inverse_basis = c_basis.inv()
                for power in range(size):
                    coordinates = inverse_basis * mc * mx**power * unit_vector
                    for entry in coordinates:
                        self.assertIsNotNone(sp.cancel(entry).as_poly(u))

    def test_polynomial_parts_and_the_forbidden_negative_coefficient(self):
        x, A, B, C, d, s, e = sp.symbols("x A B C d s e")
        general_y = x**4 + A * x**2 + B * x + C
        _, half_tail = polynomial_part_and_tail(general_y, x, 2, 1)
        _, three_half_tail = polynomial_part_and_tail(general_y, x, 6, 1)
        self.assert_zero(half_tail[1] - B / 2)
        self.assert_zero(
            three_half_tail[1] - sp.Rational(3, 16) * B * (4 * C - A**2)
        )

        h = x**2 + A / 2
        y = h**2 + B * x
        parts = {}
        tails = {}
        for degree in range(7):
            parts[degree], tails[degree] = polynomial_part_and_tail(
                y, x, degree, 1
            )
            self.assertEqual(sp.degree(parts[degree], x), degree)
            self.assert_zero(sp.Poly(parts[degree], x).LC() - 1)
        phi = h**3 + sp.Rational(3, 2) * B * x * h + sp.Rational(3, 8) * B**2
        self.assert_zero(parts[2] - h)
        self.assert_zero(parts[4] - y)
        self.assert_zero(parts[6] - phi)
        self.assert_zero(tails[6][1])
        self.assert_zero(tails[4][1])
        self.assert_zero(tails[2][1] - B / 2)

        # Polynomial minus its exact fractional-power expression has the
        # opposite tail sign. Substitution x(z)=z+lower terms cannot change
        # its z^-1 coefficient. The universal substitution proof is textual.
        first_negative_tail = -tails[6][1] - d * tails[4][1] - s * tails[2][1]
        self.assert_zero(first_negative_tail + s * B / 2)
        self.assertNotEqual(sp.expand(first_negative_tail), 0)

        # If B=0 the whole permitted polynomial family is even, including
        # the s*P2 term. It cannot generate L(x) along with the even y.
        even_psi = (parts[6] + d * parts[4] + s * parts[2] + e).subs(B, 0)
        even_y = y.subs(B, 0)
        self.assert_zero(even_y.subs(x, -x) - even_y)
        self.assert_zero(even_psi.subs(x, -x) - even_psi)

    def test_exact_quartic_companion_traces_and_missing_center(self):
        x, u, z, A, B, d, e = sp.symbols("x u z A B d e")
        h = x**2 + A / 2
        y = h**2 + B * x
        phi = h**3 + sp.Rational(3, 2) * B * x * h + sp.Rational(3, 8) * B**2
        relation = sp.expand(y - u)

        # Build every column from a remainder, not the printed recurrence
        # or a copied matrix of already-simplified trace coefficients.
        mphi = multiplication_matrix(phi, relation, x)
        trace1 = sp.expand(sp.trace(mphi))
        trace2 = sp.expand(sp.trace(mphi * mphi))
        trace3 = sp.expand(sp.trace(mphi * mphi * mphi))
        self.assert_zero(trace1)
        self.assert_zero(
            trace2 - 4 * u**3 - sp.Rational(3, 2) * A * B**2 * u
            - sp.Rational(3, 16) * B**4
        )
        self.assert_zero(trace3 - sp.Rational(3, 64) * B**6)

        shift = d * u + e
        mpsi = mphi + shift * sp.eye(4)
        t1 = sp.trace(mpsi)
        t2 = sp.trace(mpsi * mpsi)
        t3 = sp.trace(mpsi * mpsi * mpsi)
        e3 = sp.expand((t1**3 - 3 * t1 * t2 + 2 * t3) / 6)
        expected = 4 * shift**3 - shift * trace2 + B**6 / 64
        self.assert_zero(e3 - expected)
        characteristic = sp.Poly(mpsi.charpoly(z).as_expr(), z)
        self.assert_zero(characteristic.coeff_monomial(z) + e3)
        self.assert_zero(e3.coeff(u, 4) + 4 * d)
        self.assert_zero(e3.coeff(u, 3) - 4 * (d**3 - e))
        self.assert_zero(e3.subs({d: 0, e: 0}) - B**6 / 64)
        self.assertNotEqual(e3.subs({d: 0, e: 0}), 0)

    def test_nonbirational_boundary_has_repeated_characteristic_polynomial(self):
        x, u, z, A = sp.symbols("x u z A")
        h = x**2 + A / 2
        y = h**2
        psi = h**3
        relation = sp.expand(y - u)
        mpsi = multiplication_matrix(psi, relation, x)
        characteristic = sp.expand(mpsi.charpoly(z).as_expr())

        # The formal missing linear coefficient really can vanish when B=0.
        # It is the retained degree-four primitiveness assumption that fails.
        self.assert_zero(characteristic - (z**2 - u**3) ** 2)
        self.assert_zero_matrix(mpsi**2 - u**3 * sp.eye(4))
        self.assert_zero(sp.Poly(characteristic, z).coeff_monomial(z))
        derivative_matrix = multiplication_matrix(
            sp.diff(characteristic, z).subs(z, psi), relation, x
        )
        self.assert_zero_matrix(derivative_matrix)
        self.assert_zero(y.subs(x, -x) - y)
        self.assert_zero(psi.subs(x, -x) - psi)


if __name__ == "__main__":
    unittest.main()
