"""Finite exact-algebra controls for the binary-quartic sextic220.

Standalone: no proof, solver, retained checker, or workspace data is imported.
The unrestricted four-slope identity and the literal coefficient derivatives
are symbolic identities, not finite-grid tests. The multiplicity fixtures
cover each root partition, with and without a root at infinity.

These controls do not prove actual-chart existence, nonzero return, exact
field return, normalization, the plane-degree theorem, ambient recognition,
arbitrary entry, or cancellation. The written proof supplies those gates.
Only Root may execute this saved source after complete source review.
"""

from itertools import combinations
from math import factorial
import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, z = sp.symbols("U V z")
PAIRS = tuple(combinations(range(4), 2))


def clean(expr):
    return sp.cancel(sp.expand(expr))


def scaled_sextic(jets):
    """Build the scaled polynomial directly from the derivative expression."""
    s0, s1, s2, s3, s4 = jets
    p3 = s3 * z**3 / 6 - s2 * z**2 / 2 + s1 * z - s0
    p4 = s4 * z**4 / 24 - s3 * z**3 / 6 + s2 * z**2 / 2 - s1 * z + s0
    r2 = 2 * s0 - s1 * z
    h2_rho = -s2 * z**2 / 2 + 2 * s1 * z - 3 * s0
    return sp.expand(s0 * p3**2 - r2 * h2_rho * p3 + r2**2 * p4)


def polynomial_sextic(poly):
    return scaled_sextic([sp.diff(poly, t, j) for j in range(5)])


def pair_forms(factors):
    return [
        factors[i] * factors[j] * V
        - rho * sp.diff(factors[i] * factors[j], t) * U
        for i, j in PAIRS
    ]


class BinaryQuarticPairFactorControls(unittest.TestCase):
    def zero(self, expr):
        self.assertEqual(clean(expr), 0)

    def test_literal_universal_top_and_homogeneous_scaling(self):
        sf = sp.Function("s")(t)
        q = sf / rho

        def taylor(order):
            return sum(
                sp.diff(q, t, i, rho, order - i)
                * U**i * V**(order - i)
                / (factorial(i) * factorial(order - i))
                for i in range(order + 1)
            )

        h2, h3, h4 = [taylor(j) for j in (2, 3, 4)]
        r2 = sp.diff(h2, V)
        # The negative sign is the leading term of ell-S, not an ansatz.
        raw_top = (
            sp.diff(q, rho, 2) * h3**2 / 2
            - r2 * sp.diff(h2, rho) * h3
            + r2**2 * h4
        )
        jets = sp.symbols("s0:5")
        replacement = {sp.diff(sf, t, j): jets[j] for j in range(5)}
        raw_top = raw_top.xreplace(replacement)
        expected = V**6 * scaled_sextic(jets).subs(z, rho * U / V) / rho**11
        self.zero(raw_top - expected)
        top_poly = sp.Poly(sp.expand(raw_top), U, V)
        self.assertEqual(top_poly.total_degree(), 6)
        self.assertTrue(all(sum(monomial) == 6 for monomial, _ in top_poly.terms()))
        self.zero(sp.diff(q, rho, 2) / 2 - sf / rho**3)
        self.zero(r2 - (-sp.diff(sf, t) * rho * U + 2 * sf * V) / rho**3)
        # Affine degree can drop while the homogeneous sextic stays nonzero.
        self.zero(polynomial_sextic(sp.Integer(1)) + 1)
        self.zero(raw_top.subs(dict(zip(jets, [1, 0, 0, 0, 0]))) + V**6 / rho**11)

    def test_unrestricted_six_pair_identity_and_affine_derivative_bridge(self):
        slopes = sp.symbols("u0:4")
        elementary = [sp.Integer(1)] + [
            sum(sp.prod(slopes[i] for i in indices) for indices in combinations(range(4), j))
            for j in range(1, 5)
        ]
        # s^(j)/(j! s)=e_j is used only after its affine-factor check below.
        normalized = scaled_sextic(
            [factorial(j) * elementary[j] for j in range(5)]
        )
        product = sp.prod(1 - (slopes[i] + slopes[j]) * z for i, j in PAIRS)
        self.zero(normalized + product)
        self.assertEqual(sp.Poly(normalized, z).degree(), 6)
        self.assertEqual(normalized.subs(z, 0), -1)

        # Reconstruct one generic pair-root cancellation without dividing by
        # any specialized pair sum or asserting that all sums are nonzero.
        p, a, b = sp.symbols("p a b")
        e_at_pair = [1, (1 + a) / z, (p + a + b) / z**2,
                     (p * a + b) / z**3, p * b / z**4]
        self.zero(scaled_sextic([factorial(j) * e_at_pair[j] for j in range(5)]))
        self.zero(p * (1 - a)**2 * (p + (a - p - b - 1) + (1 - a + b)))

        intercepts = sp.symbols("a0:4")
        gradients = sp.symbols("b0:4")
        factors = [intercepts[i] + gradients[i] * t for i in range(4)]
        poly = sp.prod(factors)
        for order in range(5):
            product_rule = sum(
                sp.prod(gradients[i] if i in chosen else factors[i] for i in range(4))
                for chosen in combinations(range(4), order)
            )
            self.zero(sp.diff(poly, t, order) / factorial(order) - product_rule)
        self.zero(sp.prod(factors[i] * factors[j] for i, j in PAIRS) - poly**3)
        for (i, j), form in zip(PAIRS, pair_forms(factors)):
            self.zero(
                form - factors[i] * factors[j]
                * (V - rho * (gradients[i] / factors[i] + gradients[j] / factors[j]) * U)
            )

    def test_all_root_partitions_and_projective_infinity(self):
        fixtures = [
            ("1111-finite", [t, t - 1, t - 2, t - 3], [1, 1, 1, 1, 1, 1]),
            ("211-finite", [t, t, t - 1, t - 2], [1, 1, 2, 2]),
            ("22-finite", [t, t, t - 1, t - 1], [1, 1, 4]),
            ("31-finite", [t, t, t, t - 1], [3, 3]),
            ("4-finite", [t, t, t, t], [6]),
            ("1111-infinity", [1, t, t - 1, t - 2], [1, 1, 1, 1, 1, 1]),
            ("211-infinity", [1, 1, t, t - 1], [1, 1, 2, 2]),
            ("22-infinity", [1, 1, t, t], [1, 1, 4]),
            ("31-infinity", [1, 1, 1, t], [3, 3]),
            ("4-infinity", [1, 1, 1, 1], [6]),
        ]
        for name, given_factors, multiplicities in fixtures:
            with self.subTest(partition=name):
                factors = list(map(sp.sympify, given_factors))
                poly = sp.prod(factors)
                forms = pair_forms(factors)
                homogeneous = -sp.prod(forms)
                self.zero(V**6 * polynomial_sextic(poly).subs(z, rho * U / V) - homogeneous)
                self.assertEqual(sp.Poly(sp.expand(homogeneous), U, V).total_degree(), 6)
                self.assertTrue(all(sp.expand(form).coeff(V) != 0 for form in forms))

                # Group normalized factors over Q(t,rho), not at sampled t.
                groups = []
                for i, j in PAIRS:
                    pair = factors[i] * factors[j]
                    slope = clean(sp.diff(pair, t) / pair)
                    for group in groups:
                        if clean(slope - group[0]) == 0:
                            group[1] += 1
                            break
                    else:
                        groups.append([slope, 1])
                actual = sorted(group[1] for group in groups)
                self.assertEqual(actual, multiplicities)
                self.assertEqual(sum(actual), 6)
                self.assertEqual(all(m == 1 for m in actual), name.startswith("1111"))
                for left, right in combinations(groups, 2):
                    self.assertNotEqual(clean(left[0] - right[0]), 0)
                # This checks the listed maximum multiplicity only, not the
                # written theorem identifying it as a projected-degree bound.
                expected_max = {"1111": 1, "211": 2, "22": 4, "31": 3, "4": 6}
                self.assertEqual(max(actual), expected_max[name.split("-")[0]])

        self.zero(-sp.prod(pair_forms([1, 1, 1, 1])) + V**6)
        self.zero(-sp.prod(pair_forms([1, 1, 1, t])) + V**3 * (t * V - rho * U)**3)

    def test_affineness_and_transcendental_parameter_negative_controls(self):
        # Non-affine factors invalidate s^(j)/(j!s)=e_j. This is formal
        # algebra outside the proof's complex-coefficient linear factors.
        bad_s = 1 + t**2
        wrong_pair_product = -(bad_s - 2 * t * z)**3
        residual = polynomial_sextic(bad_s) - wrong_pair_product
        self.zero(residual - z**2 * (2 * t * z - bad_s) * (z**2 - 4 * t * z + 2 * bad_s))
        self.zero(residual.subs(t, 0) + z**4 + 2 * z**2)
        self.assertNotEqual(clean(residual), 0)
        self.assertNotEqual(sp.diff(bad_s, t, 2), 0)

        # Four distinct projective roots have six distinct pair factors over
        # C(t,rho). A special value of t can merge them and is not a field
        # extension preserving the required transcendental parameter.
        factors = [t - 1, t + 1, t - 2, t + 2]
        left, right = factors[0] * factors[1], factors[2] * factors[3]
        slope_difference = clean(sp.diff(left, t) / left - sp.diff(right, t) / right)
        self.zero(slope_difference + 6 * t / ((t**2 - 1) * (t**2 - 4)))
        self.assertNotEqual(slope_difference, 0)
        self.zero(slope_difference.subs(t, 0))
        form_left = left * V - rho * sp.diff(left, t) * U
        form_right = right * V - rho * sp.diff(right, t) * U
        proportionality_minor = (
            sp.expand(form_left).coeff(U) * sp.expand(form_right).coeff(V)
            - sp.expand(form_right).coeff(U) * sp.expand(form_left).coeff(V)
        )
        self.zero(proportionality_minor - 6 * rho * t)
        self.assertNotEqual(clean(proportionality_minor), 0)
        self.zero(form_right.subs(t, 0) - 4 * form_left.subs(t, 0))


if __name__ == "__main__":
    unittest.main()
