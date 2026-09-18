"""Exact finite controls for the actual rational-entry boundary in proof266.

These checks do not prove the curve-pencil theorem, divisibility lemma for
every LND, or the universal polynomial-entry recognition criterion.
No retained checker or solver is imported.
"""

import unittest

import sympy as sp


class CurveFieldEntryControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    @staticmethod
    def data():
        X, Y, Z, W = sp.symbols("X Y Z W")
        I = X * W - Y**2
        J = W + 2 * I * Y + I**2 * X
        values = [2 * Y + 2 * I * X, W - I**2 * X, 0, -2 * I * W - 2 * I**2 * Y]

        def D(expression):
            return sp.expand(sum(value * sp.diff(expression, variable)
                                 for value, variable in zip(values, [X, Y, Z, W])))

        def E(expression):
            return sp.expand(D(expression) + sp.diff(expression, Z))

        return (X, Y, Z, W), I, J, values, D, E

    def test_invariants_and_exact_local_nilpotence_on_generators(self):
        (X, Y, Z, W), I, J, values, D, E = self.data()
        self.assert_zero(D(I))
        self.assert_zero(D(J))
        self.assert_zero(E(I))
        self.assert_zero(E(Z) - 1)
        for variable, second in zip([X, Y, W], [2 * J, -2 * I * J, 2 * I**2 * J]):
            self.assert_zero(D(D(variable)) - second)
            self.assertNotEqual(sp.expand(second), 0)
            self.assert_zero(D(D(D(variable))))
        for variable in [X, Y, Z, W]:
            self.assert_zero(D(sp.diff(variable, Z)) - sp.diff(D(variable), Z))

    def test_explicit_invariant_coordinate_map_and_both_inverses(self):
        variables, I, J, values, D, E = self.data()
        X, Y, Z, W = variables
        def step(coordinates, sign):
            x, y, z, w = coordinates
            return [
                sp.expand(x + sign * z * (2 * y + 2 * I * x) + z**2 * J),
                sp.expand(y + sign * z * (w - I**2 * x) - z**2 * I * J),
                z,
                sp.expand(w + sign * z * (-2 * I * w - 2 * I**2 * y)
                          + z**2 * I**2 * J),
            ]

        forward = step(variables, -1)
        backward = step(variables, 1)
        for index in [0, 1, 3]:
            self.assert_zero(E(forward[index]))
        # Preserve I and J first, so the finite inverse calculation can
        # use their already-proved invariant values without huge expansion.
        for image in [forward, backward]:
            x, y, z, w = image
            self.assert_zero(x * w - y**2 - I)
            self.assert_zero(w + 2 * I * y + I**2 * x - J)
        # Each image preserves I and J, so keeping those original expressions
        # in step now computes the literal inverse composition exactly.
        for image, sign in [(forward, 1), (backward, -1)]:
            for variable, restored in zip(variables, step(image, sign)):
                self.assert_zero(restored - variable)

    def test_rational_entry_and_no_polynomial_W_shear(self):
        (X, Y, Z, W), I, J, values, D, E = self.data()
        self.assert_zero(X * W - I - Y**2)
        parameter = sp.symbols("parameter")
        self.assertEqual(sp.rem(parameter + Y**2, X, X), parameter + Y**2)
        pX, pY, pZ = sp.symbols("pX pY pZ")
        derivative = values[3] - values[0] * pX - values[1] * pY - pZ
        coefficient = sp.Poly(sp.expand(derivative), W).nth(2)
        self.assert_zero(coefficient - (X**3 * pY - 2 * X**2 * Y - 2 * X))
        # Dividing the necessary zero coefficient by X and then setting X=0
        # leaves -2, independent of every possible polynomial derivative P_Y.
        divided = sp.cancel(coefficient / X)
        self.assertEqual(divided.subs(X, 0), -2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
