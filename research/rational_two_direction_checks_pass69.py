"""Exact controls for rational-two-direction-recognition-pass69.md.

The classification is a written proof, not a finite search theorem here.
These methods check its differential identities and two genuine polynomial
sliced actions. The radial rational symmetry is deliberately not an LND on
the localization containing its coefficient. No full moving frame is claimed.
"""

import unittest

import sympy as sp


class RationalTwoDirectionChecks(unittest.TestCase):
    def setUp(self):
        self.u, self.v, self.a, self.b = sp.symbols("u v a b")
        self.variables = sp.Matrix([self.u, self.v, self.a, self.b])

    def apply(self, field, polynomial):
        return sp.cancel(sum(
            field[i] * sp.diff(polynomial, variable)
            for i, variable in enumerate(self.variables)
        ))

    def bracket(self, first, second):
        return sp.Matrix([
            self.apply(first, entry) - self.apply(second, first[i])
            for i, entry in enumerate(second)
        ])

    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_classification_differential_and_leading_coefficient_identities(self):
        u, v, a, b = self.variables
        numerator = sp.Function("N")(a, b)
        denominator = sp.Function("D")(a, b)
        beta = numerator / denominator
        symmetry = sp.Matrix([0, 0, beta, 1])
        cleared = (
            denominator**2 * sp.diff(numerator, b)
            - numerator * denominator * sp.diff(denominator, b)
            + numerator * denominator * sp.diff(numerator, a)
            - numerator**2 * sp.diff(denominator, a)
        )
        self.assert_zero(denominator**3 * self.apply(symmetry, beta) - cleared)

        p, q = sp.Function("p")(b), sp.Function("q")(b)
        affine_beta = p * a + q
        affine_symmetry = sp.Matrix([0, 0, affine_beta, 1])
        self.assert_zero(
            self.apply(affine_symmetry, affine_beta)
            - a * (sp.diff(p, b) + p**2) - sp.diff(q, b) - p * q
        )
        center_a = sp.Function("A")(u, v)
        center_b = sp.Function("B")(u, v)
        radial_p = 1 / (b + center_b)
        radial_q = center_a / (b + center_b)
        self.assert_zero(sp.diff(radial_p, b) + radial_p**2)
        self.assert_zero(sp.diff(radial_q, b) + radial_p * radial_q)
        self.assert_zero(sp.diff(1 / radial_p, b) - 1)
        self.assert_zero(sp.diff(radial_q / radial_p, b))

        # Only the symbolic leading term is checked; no finite degree cutoff
        # is used to prove the classification's degree comparison.
        degree = sp.Symbol("n", integer=True, positive=True)
        leading = sp.Symbol("c", nonzero=True) * a**degree
        self.assertEqual(sp.simplify(
            leading * sp.diff(leading, a)
            - degree * sp.Symbol("c", nonzero=True)**2 * a**(2 * degree - 1)
        ), 0)

    def test_actual_parallel_action_with_nonzero_kappa(self):
        u, v, a, b = self.variables
        action = sp.Matrix([v, 0, b, 1])
        beta = u / v
        symmetry = sp.Matrix([0, 0, beta, 1])
        good_partial = sp.Matrix([0, 0, 1, 0])
        self.assert_zero(self.bracket(action, symmetry))
        self.assert_zero(self.apply(symmetry, beta))
        self.assert_zero(self.apply(action, beta) - 1)
        self.assert_zero(self.bracket(action, self.bracket(action, good_partial)))
        self.assert_zero(self.apply(action, b) - 1)
        self.assert_zero(self.apply(action, v))
        self.assert_zero(self.apply(symmetry, v))
        for variable in self.variables:
            self.assert_zero(self.apply(action, self.apply(action, self.apply(action, variable))))
            self.assert_zero(self.apply(symmetry, self.apply(symmetry, variable)))

        # This is a triangular polynomial coordinate inverse, not an abstract
        # inference from a rational slice or the symmetry's denominator.
        invariants = sp.Matrix([v, u - v * b, a - b**2 / 2])
        for invariant in invariants:
            self.assert_zero(self.apply(action, invariant))
        V, I, J, S = sp.symbols("V I J S")
        forward = sp.Matrix([*invariants, b])
        inverse = sp.Matrix([I + V * S, V, J + S**2 / 2, S])
        old_to_new = dict(zip(self.variables, inverse))
        new_to_old = dict(zip([V, I, J, S], forward))
        self.assert_zero(forward.subs(old_to_new, simultaneous=True) - sp.Matrix([V, I, J, S]))
        self.assert_zero(inverse.subs(new_to_old, simultaneous=True) - self.variables)

    def test_actual_radial_compatibility_without_local_nilpotence(self):
        u, v, a, b = self.variables
        center_a, center_b = u**2 + v, u * v + v**2
        shifted_a, shifted_b = a + center_a, b + center_b
        beta = shifted_a / shifted_b
        symmetry = sp.Matrix([0, 0, beta, 1])
        action = sp.Matrix([1, 0, -2 * u, -v])
        delta = action / v
        good_partial = sp.Matrix([0, 0, 1, 0])
        self.assert_zero(self.apply(action, u) - 1)
        self.assert_zero(self.apply(action, v))
        self.assert_zero(self.apply(symmetry, beta))
        self.assert_zero(self.apply(delta, beta))
        self.assert_zero(self.bracket(delta, symmetry))
        self.assert_zero(self.bracket(action, self.bracket(action, good_partial)))
        for variable in self.variables:
            self.assert_zero(self.apply(action, self.apply(action, self.apply(action, variable))))
            self.assert_zero(self.apply(symmetry, self.apply(symmetry, variable)))
        self.assert_zero(self.apply(action, shifted_a))
        self.assert_zero(self.apply(action, shifted_b))
        self.assert_zero(shifted_b * self.apply(symmetry, shifted_a) - shifted_a)
        self.assert_zero(shifted_b * self.apply(symmetry, shifted_b) - shifted_b)

        # Exact recurrence for arbitrary n >= 0 proves the moving denominator
        # has infinitely many nonzero iterates. The field is not an LND on
        # B[(b+B)^-1], despite killing all coordinate second iterates.
        n = sp.Symbol("n", integer=True, nonnegative=True)
        term = (-1)**n * sp.factorial(n) * shifted_b**(-n - 1)
        next_term = (-1)**(n + 1) * sp.factorial(n + 1) * shifted_b**(-n - 2)
        self.assertEqual(sp.simplify(sp.diff(term, b) - next_term), 0)

        U, V, A, B = sp.symbols("U V A B")
        forward = sp.Matrix([u, v, shifted_a, shifted_b])
        inverse = sp.Matrix([U, V, A - U**2 - V, B - U * V - V**2])
        self.assert_zero(forward.subs(dict(zip(self.variables, inverse)), simultaneous=True)
                         - sp.Matrix([U, V, A, B]))
        self.assert_zero(inverse.subs(dict(zip([U, V, A, B], forward)), simultaneous=True)
                         - self.variables)


if __name__ == "__main__":
    unittest.main()
