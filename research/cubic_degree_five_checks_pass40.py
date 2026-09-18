"""Exact rescaling/unit controls; no claimed degree-five residual example."""

import unittest

import sympy as s


a, b, c, d, t = s.symbols("a b c d t")
X = s.Matrix([a, b, c, d])


def clean(value):
    if isinstance(value, s.MatrixBase):
        return value.applyfunc(lambda item: s.cancel(s.expand(item)))
    return s.cancel(s.expand(value))


def act(field, value):
    if isinstance(value, s.MatrixBase):
        return clean(value.jacobian(X) * field)
    return clean(sum(field[i] * s.diff(value, X[i]) for i in range(4)))


def bracket(left, right):
    return clean(act(left, right) - act(right, left))


def adjoint(left, right, order):
    for _ in range(order):
        right = bracket(left, right)
    return right


class CubicDegreeFiveChecks(unittest.TestCase):
    def assert_zero(self, value):
        value = clean(value)
        self.assertEqual(value, s.zeros(*value.shape) if isinstance(value, s.MatrixBase) else 0)

    def test_invariant_rescaling_including_nonzero_higher_corrections(self):
        E = s.Matrix([0, a, b, 1])
        g = 2 * a * c - b**2
        f = 1 / g
        self.assert_zero(act(E, g))
        self.assert_zero(act(E, d) - 1)
        corrections = []
        for index in range(4):
            T = s.eye(4)[:, index]
            for order in range(1, 5):
                previous = adjoint(E, T, order - 1)
                correction = order * f**(order - 1) * act(previous, f) * E
                expected = f**order * adjoint(E, T, order) - correction
                self.assert_zero(adjoint(f * E, T, order) - expected)
                if index == 0:
                    corrections.append(clean(correction))
        self.assertNotEqual(corrections[2], s.zeros(4, 1))
        self.assert_zero(corrections[3])

    def test_generator_niceness_does_not_check_the_inverted_unit(self):
        Z = s.Matrix([a / d, 0, 0, 1])
        self.assert_zero(act(Z, act(Z, X)))
        inverse = 1 / d
        for order in range(1, 7):
            inverse = act(Z, inverse)
            self.assert_zero(inverse - (-1)**order * s.factorial(order) / d**(order + 1))
            self.assertNotEqual(inverse, 0)
        flow = X + t * Z
        self.assert_zero(flow[3] - d - t)
        self.assertNotEqual(s.diff(flow[3], t), 0)

    def test_slice_unit_gate_and_nonunit_cleared_field_control(self):
        E = s.Matrix([0, 1, 0, 0])
        delta = E / a
        Z = s.Matrix([0, c / a, 0, 1])
        sigma = a * b - c * d
        self.assert_zero(act(E, b) - 1)
        self.assert_zero(bracket(delta, Z))
        self.assert_zero(act(Z, act(Z, X)))
        self.assert_zero(act(Z, a))
        self.assert_zero(act(Z, 1 / a))
        self.assert_zero(act(delta, sigma) - 1)
        self.assert_zero(act(Z, sigma))
        W = clean(a * Z)
        self.assertEqual(W, s.Matrix([0, c, 0, a]))
        self.assert_zero(bracket(E, W))
        self.assert_zero(act(W, act(W, X)))
        self.assert_zero(act(W, d) - a)
        self.assertEqual(s.gcd(W[1], W[3]), 1)
        # Every derivative lies in (a,c), although the original E has a slice.
        self.assert_zero(W.subs({a: 0, c: 0}))
        self.assertNotEqual(E.subs({a: 0, c: 0}), s.zeros(4, 1))

    def test_actual_localized_section_and_two_sided_inverse(self):
        aa, cc, ss, dd = s.symbols("aa cc ss dd")
        forward = s.Matrix([a, c, a * b - c * d, d])
        inverse = s.Matrix([aa, (ss + cc * dd) / aa, cc, dd])
        self.assert_zero(forward.subs(dict(zip(X, inverse)), simultaneous=True) - s.Matrix([aa, cc, ss, dd]))
        self.assert_zero(inverse.subs(dict(zip((aa, cc, ss, dd), forward)), simultaneous=True) - X)
        Z = s.Matrix([0, c / a, 0, 1])
        delta = s.Matrix([0, 1 / a, 0, 0])
        self.assert_zero(act(Z, forward) - s.Matrix([0, 0, 0, 1]))
        self.assert_zero(act(delta, forward) - s.Matrix([0, 0, 1, 0]))
        numerator, denominator = s.fraction(inverse[1])
        self.assertEqual(denominator, aa)
        self.assertNotEqual(numerator.subs(aa, 0), 0)

    def test_exact_denominator_clearing_formula(self):
        gg, pp, qq, lam = s.symbols("gg pp qq lam", nonzero=True)
        sigma = qq / (lam * gg**2)
        tau = pp / gg - lam * sigma**2 / 2
        # Coefficients in the fixed constant directions (T_c,T_d,T_e).
        rational = s.Matrix([sigma**2 / 12 + tau / (3 * lam), sigma / 3, 1])
        polynomial = s.Matrix([gg**3 * pp / (3 * lam) - qq**2 / (12 * lam**2), gg**2 * qq / (3 * lam), gg**4])
        self.assert_zero(gg**4 * rational - polynomial)
        self.assert_zero(polynomial[2] * lam - lam * gg**4)
        for coefficient in polynomial:
            self.assertTrue(s.Poly(coefficient, gg, pp, qq).is_multivariate)


if __name__ == "__main__":
    unittest.main(verbosity=2)
