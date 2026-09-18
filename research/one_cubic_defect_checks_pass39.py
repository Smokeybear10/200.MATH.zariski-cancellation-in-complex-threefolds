"""Exact controls for the bounded one-cubic-partial proof, not a proof of it."""

import unittest

import sympy as s


a, b, c, d, t = s.symbols("a b c d t")
X = s.Matrix([a, b, c, d])
g = a + b + c - d**3 / 6
P = s.Matrix([1, 0, g * d**2 / 2 - 1, g])


def clean(value):
    return value.applyfunc(s.expand) if isinstance(value, s.MatrixBase) else s.expand(value)


def act(field, value):
    if isinstance(value, s.MatrixBase):
        return clean(value.jacobian(X) * field)
    return clean(sum(field[i] * s.diff(value, X[i]) for i in range(4)))


def bracket(left, right):
    return clean(act(left, right) - act(right, left))


def iterate(field, value, count):
    for _ in range(count):
        value = act(field, value)
    return value


class OneCubicDefectChecks(unittest.TestCase):
    def assert_zero(self, value):
        value = clean(value)
        self.assertEqual(value, s.zeros(*value.shape) if isinstance(value, s.MatrixBase) else 0)

    def test_actual_slice_and_two_sided_coordinate_inverse(self):
        aa, bb, gg, rr = s.symbols("aa bb gg rr")
        r = d - a * g
        forward = s.Matrix([a, b, g, r])
        inverse = s.Matrix([aa, bb, gg - aa - bb + (rr + aa * gg)**3 / 6, rr + aa * gg])
        self.assert_zero(forward.subs(dict(zip(X, inverse)), simultaneous=True) - s.Matrix([aa, bb, gg, rr]))
        self.assert_zero(inverse.subs(dict(zip((aa, bb, gg, rr), forward)), simultaneous=True) - X)
        self.assert_zero(act(P, forward) - s.Matrix([1, 0, 0, 0]))
        self.assert_zero(forward.jacobian(X).det() - 1)

    def test_exact_actual_partial_profile(self):
        for index, expected_height in enumerate((1, 1, 1, 3)):
            field = s.eye(4)[:, index]
            for _ in range(expected_height):
                field = bracket(P, field)
            self.assertNotEqual(field, s.zeros(4, 1))
            self.assert_zero(bracket(P, field))
        self.assert_zero(iterate(P, X, 3) - s.Matrix([0, 0, g**3, 0]))
        self.assert_zero(iterate(P, X, 4))

    def test_flow_and_both_jacobian_inverse_orders(self):
        flow = s.Matrix([a + t, b, c + ((d + t * g)**3 - d**3) / 6 - t, d + t * g])
        self.assert_zero(s.diff(flow, t) - P.subs(dict(zip(X, flow)), simultaneous=True))
        self.assert_zero(flow.jacobian(X).det() - 1)
        u = bracket(P, bracket(P, s.eye(4)[:, 3]))
        v = bracket(P, u)
        C = s.eye(4) - t * P.jacobian(X) + (t**2 * u / 2 + t**3 * v / 6) * s.eye(4)[3, :]
        self.assert_zero(flow.jacobian(X) * C - s.eye(4))
        self.assert_zero(C * flow.jacobian(X) - s.eye(4))

    def test_six_dimensional_companion_and_iterate_blocks(self):
        u = bracket(P, bracket(P, s.eye(4)[:, 3]))
        v = bracket(P, u)
        M = P.jacobian(X).row_join(-u / 2).row_join(-v / 6)
        M = M.col_join(s.Matrix([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]))
        power = s.eye(6)
        for order in range(1, 7):
            power = clean(power * M)
            self.assert_zero(power[:4, :4] - iterate(P, X, order).jacobian(X) / s.factorial(order))
        self.assert_zero(power)
        self.assert_zero((s.eye(6) - t * M).det() - 1)

    def test_changed_top_coefficient_factors(self):
        h = iterate(P, X, 3)
        ell = P[3]
        u = bracket(P, bracket(P, s.eye(4)[:, 3]))
        v = bracket(P, u)
        J = P.jacobian(X)
        self.assert_zero(J * h - ell * v / 3)
        self.assert_zero(J * h.jacobian(X) - v * s.Matrix([ell]).jacobian(X))
        self.assertEqual(h.jacobian(X).rank(), 1)
        self.assert_zero(ell * act(s.eye(4)[:, 0], h) - 3 * act(s.eye(4)[:, 0], ell) * h)

    def test_middle_non_lnd_and_highest_lnd(self):
        u = bracket(P, bracket(P, s.eye(4)[:, 3]))
        v = bracket(P, u)
        self.assert_zero(act(u, d) - 2 * g * d)
        self.assert_zero(act(u, g) + g**2)
        value = g
        for order in range(1, 7):
            value = act(u, value)
            self.assert_zero(value - (-1)**order * s.factorial(order) * g**(order + 1))
            self.assertNotEqual(value, 0)
        self.assert_zero(act(v, g))
        self.assert_zero(act(v, d) - 3 * g**2)
        self.assert_zero(iterate(v, X, 4))
        top_field = s.Matrix([0, 0, g**3, 0])
        self.assert_zero(act(top_field, g) - g**3)
        self.assertNotEqual(act(top_field, top_field), s.zeros(4, 1))

    def test_actual_cubic_shear_and_repaired_partial(self):
        shear = s.Matrix([a, b, c - d**3 / 6, d])
        inverse = s.Matrix([a, b, c + d**3 / 6, d])
        self.assert_zero(shear.subs(dict(zip(X, inverse)), simultaneous=True) - X)
        self.assert_zero(inverse.subs(dict(zip(X, shear)), simultaneous=True) - X)
        new_bad = s.eye(4)[:, 3] + d**2 * s.eye(4)[:, 2] / 2
        self.assert_zero(act(new_bad, shear) - s.eye(4)[:, 3])
        self.assert_zero(bracket(P, bracket(P, bracket(P, new_bad))))
        transformed = act(P, shear).subs(dict(zip(X, inverse)), simultaneous=True)
        self.assert_zero(transformed - s.Matrix([1, 0, -1, a + b + c]))

    def test_cubic_and_quadratic_leibniz_coefficients(self):
        q, z, gg, lam = s.symbols("q z gg lam", nonzero=True)
        f3 = q**2 / (2 * lam**3)
        flow3 = f3.subs(q, q + t * lam * gg)
        self.assert_zero(s.diff(flow3, t, 3))
        self.assert_zero(3 * s.diff(flow3, t, 2).subs(t, 0) - 3 * gg**2 / lam)
        f4 = q / (3 * lam**2)
        flow4 = f4.subs(q, q + t * z + t**2 * lam * gg / 2)
        self.assert_zero(s.diff(flow4, t, 3))
        self.assert_zero(3 * s.diff(flow4, t, 2).subs(t, 0) - gg / lam)


if __name__ == "__main__":
    unittest.main(verbosity=2)
