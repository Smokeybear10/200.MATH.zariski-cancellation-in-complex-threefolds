"""Independent exact controls for the selected rank-two Su braid cell.

Source scope is proved separately in su-cell-recursion-pass37.md. These finite
identities do not establish the character-variety identification by themselves.
Only unittest and SymPy are imported; there are no project/solver imports.
"""

import unittest

import sympy as sp


a, b, c, d, r, q, t, k = sp.symbols("a b c d r q t k")
zero = sp.Integer(0)


def crossing(value):
    return sp.Matrix([[0, 1], [1, value]])


def cancel_matrix(matrix):
    return matrix.applyfunc(sp.cancel)


def prefixes(values):
    current = sp.eye(2)
    result = [current]
    for value in values:
        current = cancel_matrix(crossing(value) * current)
        result.append(current)
    return result


def raw_from_normalized(aa, bb, cc, dd, rr, qq):
    return (
        aa,
        rr,
        (qq - 1) / rr,
        -rr / qq,
        qq**2 * (bb - aa) - qq * (qq - 1) / rr,
        zero,
        qq**2 * (cc - bb),
        zero,
        qq**2 * (dd - cc),
        zero,
    )


def prime_parameters_from_matrices(values):
    """Recover every Appendix A parameter from its previous actual matrix.

    For a lower-left nonzero matrix, M=H(A/C)*s*b', with
    diag(b')=(C,-det(M)/C). For an upper matrix, use (A.0.3).
    This routine does not call the claimed coordinate parametrization.
    """
    matrix = sp.eye(2)
    recovered = []
    for value in values:
        aa, bb, cc, dd = list(matrix)
        if sp.cancel(cc) == 0:
            prime = (dd * value + bb) / aa
        else:
            prime = -(cc**2 / matrix.det()) * (value + aa / cc)
        recovered.append(sp.cancel(prime))
        matrix = cancel_matrix(crossing(value) * matrix)
    return tuple(recovered)


class SuCellChecks(unittest.TestCase):
    def assert_expr_equal(self, actual, expected):
        self.assertEqual(sp.cancel(actual - expected), 0)

    def assert_matrix_equal(self, actual, expected):
        self.assertEqual(cancel_matrix(actual - expected), sp.zeros(*actual.shape))

    def assert_tuple_equal(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for got, want in zip(actual, expected):
            self.assert_expr_equal(got, want)

    def test_all_prefix_matrices_and_exact_walk(self):
        values = raw_from_normalized(a, b, c, d, r, q)
        upper = q * a + (q - 1) / r
        expected = [
            sp.eye(2),
            sp.Matrix([[0, 1], [1, a]]),
            sp.Matrix([[1, a], [r, 1 + r * a]]),
            sp.Matrix([[r, 1 + r * a], [q, upper]]),
            sp.Matrix([[q, upper], [0, 1 / q]]),
            sp.Matrix([[0, 1 / q], [q, q * b]]),
            sp.Matrix([[q, q * b], [0, 1 / q]]),
            sp.Matrix([[0, 1 / q], [q, q * c]]),
            sp.Matrix([[q, q * c], [0, 1 / q]]),
            sp.Matrix([[0, 1 / q], [q, q * d]]),
            sp.Matrix([[q, q * d], [0, 1 / q]]),
        ]
        actual = prefixes(values)
        for got, want in zip(actual, expected):
            self.assert_matrix_equal(got, want)
        self.assert_tuple_equal(
            [matrix[1, 0] for matrix in actual],
            [0, 1, r, q, 0, q, 0, q, 0, q, 0],
        )
        for index, matrix in enumerate(actual):
            self.assert_expr_equal(matrix.det(), (-1) ** index)

    def test_appendix_a_parameters_and_two_sided_raw_inverse(self):
        values = raw_from_normalized(a, b, c, d, r, q)
        recovered = prime_parameters_from_matrices(values)
        self.assert_tuple_equal(
            recovered, [a, r, -r * q, 0, b, 0, c, 0, d, 0]
        )

        # Start independently with freely chosen RAW up coefficients.
        aa, bb, cc, dd = sp.symbols("raw_a raw_b raw_c raw_d")
        raw_values = (aa, r, (q - 1) / r, -r / q, bb, zero, cc, zero, dd, zero)
        normalized = prime_parameters_from_matrices(raw_values)
        reconstructed = raw_from_normalized(
            normalized[0], normalized[4], normalized[6], normalized[8],
            normalized[1], -normalized[2] / normalized[1],
        )
        self.assert_tuple_equal(reconstructed, raw_values)
        self.assert_tuple_equal(
            [normalized[index] for index in (0, 4, 6, 8)],
            [
                aa,
                aa + (q - 1) / (r * q) + bb / q**2,
                aa + (q - 1) / (r * q) + (bb + cc) / q**2,
                aa + (q - 1) / (r * q) + (bb + cc + dd) / q**2,
            ],
        )

    def test_source_stay_monodromy_matches_actual_product(self):
        stay2, stay3 = sp.symbols("stay2 stay3")
        switch = sp.Matrix([[0, 1], [1, 0]])
        # Eight crossings follow position 2; seven follow position 3.
        factor2 = sp.diag(-1 / stay2, stay2)
        factor3 = switch * sp.diag(-1 / stay3, stay3) * switch
        diagonal = cancel_matrix((factor2 * factor3).subs(
            {stay2: r, stay3: -r * q}, simultaneous=True
        ))
        actual = prefixes(raw_from_normalized(a, b, c, d, r, q))[-1]
        self.assert_matrix_equal(diagonal, sp.diag(actual[0, 0], actual[1, 1]))
        kappa = sp.symbols("kappa", nonzero=True)
        self.assert_matrix_equal(
            sp.diag(kappa, 1 / kappa) *
            diagonal.subs(q, 1 / kappa),
            sp.eye(2),
        )

    def test_unipotent_absorption_and_simultaneous_normalized_translation(self):
        h_minus_t = sp.Matrix([[1, -t], [0, 1]])
        self.assert_matrix_equal(crossing(a) * h_minus_t, crossing(a - t))
        values = raw_from_normalized(a, b, c, d, r, q)
        acted_raw = (values[0] - t,) + values[1:]
        # Full product control is independent of the parameter recovery.
        self.assert_matrix_equal(
            prefixes(values)[-1] * h_minus_t,
            prefixes(acted_raw)[-1],
        )
        recovered = prime_parameters_from_matrices(acted_raw)
        self.assert_tuple_equal(
            recovered, [a - t, r, -r * q, 0, b - t, 0, c - t, 0, d - t, 0]
        )
        self.assert_tuple_equal(
            acted_raw, raw_from_normalized(a - t, b - t, c - t, d - t, r, q)
        )

    def test_torus_push_and_weights_at_every_crossing(self):
        t1, t2 = sp.symbols("t1 t2", nonzero=True)
        torus_inverse = sp.diag(1 / t1, 1 / t2)
        switched_inverse = sp.diag(1 / t2, 1 / t1)
        self.assert_matrix_equal(
            crossing(a) * torus_inverse,
            switched_inverse * crossing((t1 / t2) * a),
        )
        values = raw_from_normalized(a, b, c, d, r, q)
        acted = tuple(
            sp.cancel(value * (k if index % 2 == 0 else 1 / k))
            for index, value in enumerate(values)
        )
        self.assert_tuple_equal(
            acted, raw_from_normalized(k * a, k * b, k * c, k * d, r / k, q)
        )
        recovered = prime_parameters_from_matrices(acted)
        self.assert_tuple_equal(
            recovered, [k * a, r / k, -r * q / k, 0,
                        k * b, 0, k * c, 0, k * d, 0]
        )
        diagonal_inverse = sp.diag(1 / k, 1)
        self.assert_matrix_equal(
            prefixes(values)[-1] * diagonal_inverse,
            diagonal_inverse * prefixes(acted)[-1],
        )

    def test_affine_quotient_and_cylinder_maps_in_both_directions(self):
        u, v, w, sigma = sp.symbols("u v w sigma")
        quotient_and_slice = (b - a, c - a, d - a, -a)
        inverse = (-sigma, u - sigma, v - sigma, w - sigma)
        forward_variables = (a, b, c, d)
        target_variables = (u, v, w, sigma)
        self.assert_tuple_equal(
            [value.subs(dict(zip(target_variables, quotient_and_slice)),
                        simultaneous=True) for value in inverse],
            forward_variables,
        )
        self.assert_tuple_equal(
            [value.subs(dict(zip(forward_variables, inverse)),
                        simultaneous=True) for value in quotient_and_slice],
            target_variables,
        )
        infinitesimal = [
            -sum(sp.diff(value, variable) for variable in forward_variables)
            for value in quotient_and_slice
        ]
        self.assert_tuple_equal(infinitesimal, [0, 0, 0, 1])
        acted = [value.subs(
            {a: a - t, b: b - t, c: c - t, d: d - t},
            simultaneous=True,
        ) for value in quotient_and_slice]
        self.assert_tuple_equal(
            acted, [b - a, c - a, d - a, -a + t]
        )

    def test_full_projective_borel_normal_form_and_global_invariants(self):
        # The normalizing sequence is U(t=a), followed by T(k=r).
        values = raw_from_normalized(a, b, c, d, r, q)
        after_u = (values[0] - a,) + values[1:]
        after_t = tuple(
            sp.cancel(value * (r if index % 2 == 0 else 1 / r))
            for index, value in enumerate(after_u)
        )
        invariants = (r * (b - a), r * (c - a), r * (d - a))
        self.assert_tuple_equal(
            after_t, raw_from_normalized(0, *invariants, sp.Integer(1), q)
        )
        for value in invariants:
            self.assert_expr_equal(
                value.subs({a: a - t, b: b - t, c: c - t, d: d - t},
                           simultaneous=True),
                value,
            )
            self.assert_expr_equal(
                value.subs({a: k * a, b: k * b, c: k * c, d: k * d, r: r / k},
                           simultaneous=True),
                value,
            )
        # Opposite normalizations use (a,r) and the three invariants.
        i1, i2, i3 = sp.symbols("i1 i2 i3")
        recovered = (a, a + i1 / r, a + i2 / r, a + i3 / r, r)
        self.assert_tuple_equal(
            [value.subs({i1: invariants[0], i2: invariants[1], i3: invariants[2]},
                        simultaneous=True) for value in recovered],
            [a, b, c, d, r],
        )

    def test_explicit_generic_diagonal_parameters_and_restricted_cell(self):
        primes = list(map(sp.Integer, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]))
        entries = primes + [1 / sp.prod(primes)]
        pairs = list(zip(entries[::2], entries[1::2]))
        diagonal_product = sp.eye(2)
        for first, second in pairs:
            self.assertNotEqual(first, second)
            diagonal_product *= sp.diag(first, second)
        self.assertEqual(diagonal_product.det(), 1)
        for mask in range(64):
            one_per_pair = sp.prod(pair[(mask >> index) & 1]
                                   for index, pair in enumerate(pairs))
            self.assertNotEqual(one_per_pair, 1)
        switch = sp.Matrix([[0, 1], [1, 0]])
        source_d0 = sp.eye(2)
        for first, second in pairs[:5]:
            source_d0 *= switch * sp.diag(first, second) * switch
        source_d0 *= sp.diag(*pairs[5])
        actual = prefixes(raw_from_normalized(a, b, c, d, r, 1 / source_d0[0, 0]))[-1]
        self.assert_matrix_equal(
            source_d0 * sp.diag(actual[0, 0], actual[1, 1]),
            sp.eye(2),
        )
        self.assertNotEqual(source_d0[0, 0], 1)


if __name__ == "__main__":
    unittest.main()

