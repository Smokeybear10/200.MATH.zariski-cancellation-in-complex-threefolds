"""Independent finite controls for the height-two actual family in pass212.

The general polynomial inverse, all-degree ideal argument and unbounded
relation-weight theorem require their written proofs. These checks establish
exact identities for a symbolic function and finite monomial controls only.
No retained checker or research implementation is imported.
"""

import unittest

import sympy as s


class HeightTwoInitialFamilyControls(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(s.expand(value), 0)

    def test_actual_family_maps_degrees_and_flow(self):
        u, t, y, z = s.symbols("u t y z")
        X, Y, Z, W, lam = s.symbols("X Y Z W lam")
        f = s.Function("f")
        forward = (
            u,
            y + t * u,
            z + (3 * t**2 * y + f(t)) * u + t**3 * u**2,
            t - y**3 + (z - 3 * t * y**2) * u + f(t) * u**2,
        )
        self.zero(forward[3] - t - forward[0] * forward[2] + forward[1]**3)
        inverse_t = W - X * Z + Y**3
        inverse_y = Y - X * inverse_t
        inverse_z = Z - (3 * inverse_t**2 * inverse_y + f(inverse_t)) * X - inverse_t**3 * X**2
        backward = (X, inverse_t, inverse_y, inverse_z)

        # Check the staged inverse in both directions. Intermediate simplification
        # is important for a symbolic f: polynomial equality inside its argument
        # must be established before applying that arbitrary function.
        returned_t = s.expand(inverse_t.subs(dict(zip((X, Y, Z, W), forward)), simultaneous=True))
        self.zero(returned_t - t)
        returned_y = s.expand(forward[1] - forward[0] * returned_t)
        self.zero(returned_y - y)
        returned_z = forward[2] - (3 * returned_t**2 * returned_y + f(returned_t)) * forward[0]
        returned_z -= returned_t**3 * forward[0]**2
        self.zero(returned_z - z)
        self.zero(backward[0] - X)
        reconstructed_y = s.expand(backward[2] + backward[1] * backward[0])
        self.zero(reconstructed_y - Y)
        reconstructed_z = backward[3] + (3 * backward[1]**2 * backward[2] + f(backward[1])) * backward[0]
        reconstructed_z += backward[1]**3 * backward[0]**2
        reconstructed_z = s.expand(reconstructed_z)
        self.zero(reconstructed_z - Z)
        reconstructed_w = backward[1] + backward[0] * reconstructed_z - reconstructed_y**3
        self.zero(reconstructed_w - W)

        for expression, degree, leader in zip(forward, (1, 1, 2, 2), (1, t, t**3, f(t))):
            polynomial = s.Poly(expression, u)
            self.assertEqual(polynomial.degree(), degree)
            self.zero(polynomial.LC() - leader)
            self.zero(s.diff(expression, u, degree + 1))
            # The finite Taylor identity is the polynomial translation flow.
            taylor = sum(s.diff(expression, u, j) * lam**j / s.factorial(j) for j in range(degree + 1))
            self.zero(expression.subs(u, u + lam) - taylor)

    def test_literal_partials_and_common_intrinsic_slice(self):
        u, t, y, z = s.symbols("u t y z")
        f = s.Function("f")
        C = 6 * t * y + s.diff(f(t), t)
        variables = (u, t, y, z)
        tz_columns = (0, -u, u**2, 1 + C * u**2)
        tw_columns = (0, 1, -u, -C * u)
        apply = lambda columns, value: s.expand(sum(coefficient * s.diff(value, variable)
                                                    for coefficient, variable in zip(columns, variables)))
        forward = (
            u, y + t * u,
            z + (3 * t**2 * y + f(t)) * u + t**3 * u**2,
            t - y**3 + (z - 3 * t * y**2) * u + f(t) * u**2,
        )
        for index, expression in enumerate(forward):
            self.zero(apply(tz_columns, expression) - int(index == 2))
            self.zero(apply(tw_columns, expression) - int(index == 3))
        for variable in variables:
            self.zero(apply(tz_columns, apply(tw_columns, variable))
                      - apply(tw_columns, apply(tz_columns, variable)))
        self.assertEqual(max(s.degree(value, u) for value in tz_columns[1:]), 2)
        self.assertEqual(max(s.degree(value, u) for value in tw_columns[1:]), 1)

        D = lambda value: s.expand(s.diff(value, y) + C * s.diff(value, z))
        for variable, z_column, w_column in zip(variables, tz_columns, tw_columns):
            self.zero(s.expand(z_column).coeff(u, 2) - D(variable))
            self.zero(s.expand(w_column).coeff(u, 1) + D(variable))
        H = z - 3 * t * y**2 - s.diff(f(t), t) * y
        self.zero(D(H))
        self.zero(D(y) - 1)
        self.zero(D(t))
        h0 = s.symbols("h0")
        self.zero(H.subs(z, h0 + 3 * t * y**2 + s.diff(f(t), t) * y) - h0)
        self.zero((h0 + 3 * t * y**2 + s.diff(f(t), t) * y).subs(h0, H) - z)

    def test_base_full_ideal_and_bounded_monomial_independence(self):
        X, Y, Z, W, t, eta = s.symbols("X Y Z W t eta")
        generators = (X * Z - Y**3, X * W - Y * Z, Y**2 * W - Z**2)
        initial = {X: eta, Y: t * eta, Z: t**3 * eta**2, W: t**4 * eta**2}
        for generator in generators:
            self.zero(generator.subs(initial, simultaneous=True))
        F1, F2, F3 = generators
        self.zero(W * F1 - Z * F2 + Y * F3)
        self.zero(Y**2 * F2 - X * F3 - Z * F1)
        self.zero(Y**2 * W * F1 - X * Z * F3 - Z**2 * F1 + Y**3 * F3)
        weight_two = (X**2, X * Y, Y**2, Z, W)
        coefficient_columns = [s.Poly(s.expand(value.subs(initial, simultaneous=True) / eta**2), t)
                               for value in weight_two]
        matrix = s.Matrix([[value.coeff_monomial(t**row) for value in coefficient_columns]
                           for row in range(5)])
        self.assertEqual(matrix.det(), 1)

        # The written argument proves this for every weight. Check all normal
        # monomials of weight at most24, including overlaps between families.
        images = {}
        cap = 24
        for i in range(cap + 1):
            for j in range(cap + 1 - i):
                for k in range((cap - i - j) // 2 + 1):
                    for ell in range((cap - i - j - 2 * k) // 2 + 1):
                        if (i and k) or (i and ell) or (j >= 2 and ell):
                            continue
                        monomial = (i, j, k, ell)
                        key = (i + j + 2 * k + 2 * ell, j + 3 * k + 4 * ell)
                        self.assertNotIn(key, images)
                        images[key] = monomial

    def test_finite_second_relation_thresholds(self):
        X, Y, Z, W, t, eta = s.symbols("X Y Z W t eta")
        for n in range(4, 31):
            m, r = divmod(n, 3)
            threshold = (2 * n + 2) // 3
            self.assertEqual(2 * m + r, threshold)
            self.assertGreaterEqual(threshold - 2, 0)
            second = X**(threshold - 2) * W - Y**r * Z**m
            self.zero(second.subs({X: eta, Y: t * eta, Z: t**3 * eta**2,
                                   W: t**n * eta**2}, simultaneous=True))
            # Modulo F1, the W coefficient X^(threshold-2) is nonzero.
            self.assertNotEqual(s.diff(second, W).subs(X, 1), 0)
            for weight in range(threshold):
                intervals = [(n * j, n * j + (3 * (weight - 2 * j)) // 2)
                             for j in range(weight // 2 + 1)]
                for earlier, later in zip(intervals, intervals[1:]):
                    self.assertLess(earlier[1], later[0])
        # No weight-two relation for any monomial member in this finite range.
        for n in range(4, 31):
            self.assertEqual(len({0, 1, 2, 3, n}), 5)


if __name__ == "__main__":
    unittest.main()
