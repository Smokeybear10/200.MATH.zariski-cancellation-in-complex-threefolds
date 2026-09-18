"""Independent exact controls for the pass76 written arguments.

These finite and symbolic identities do not prove cancellation, the
published geometric input, or an all-degree classification theorem.
No solver, earlier checker, or research-note implementation is imported.
"""

import unittest

import sympy as sp


def action(coefficients, coordinates, expression):
    return sp.expand(sum(v * sp.diff(expression, x)
                         for v, x in zip(coefficients, coordinates)))


def substitute(expressions, coordinates, values):
    mapping = dict(zip(coordinates, values))
    return [sp.expand(e.subs(mapping, simultaneous=True)) for e in expressions]


def constant_kernel(expressions, variables, parameters):
    rows = []
    for expression in expressions:
        for coefficient in sp.Poly(sp.expand(expression), *variables).coeffs():
            rows.append([sp.diff(coefficient, p) for p in parameters])
    return sp.Matrix(rows).nullspace()


class NiceFrontierChecks(unittest.TestCase):
    def test_two_invariant_jacobian_and_actual_gauge_inverse(self):
        a, U, V, S = sp.symbols("a U V S")
        k = a * U + U**2
        examples = [
            (U, 1, 0, 1, 1 + 2 * V),
            (1, U, 1, 0, 1 - 2 * V),
            (a, a**2 + 1, -a + k * (a**2 + 1), 1 - k * a, 1),
            (0, 1, k, 1, 1),
            (1, 0, 1, k, 1),
        ]
        for u, v, r, s, expected in examples:
            u, v, r, s = map(sp.sympify, (u, v, r, s))
            self.assertEqual(sp.expand(r * u + s * v), 1)
            output = sp.Matrix([
                s**2 * U + 2 * s * u * V + u**2 * S,
                -s * r * U + (s * v - r * u) * V + u * v * S,
                r**2 * U - 2 * r * v * V + v**2 * S,
            ])
            direct = sp.expand(output.jacobian([U, V, S]).det())
            formula = 1 + 2 * U * (v * sp.diff(s, U) + u * sp.diff(r, U))
            formula += 2 * V * (v * sp.diff(u, U) - u * sp.diff(v, U))
            self.assertEqual(sp.expand(direct - formula), 0)
            self.assertEqual(sp.expand(direct - expected), 0)
            self.assertEqual(sp.expand(output[0] * output[2] - output[1]**2),
                             U * S - V**2)

        variables = [a, U, V, S]
        forward = [a, U, V - k * U, S - 2 * k * V + k**2 * U]
        inverse = [a, U, V + k * U, S + 2 * k * V + k**2 * U]
        self.assertEqual(substitute(forward, variables, inverse), variables)
        self.assertEqual(substitute(inverse, variables, forward), variables)
        self.assertEqual([sp.diff(x, S) for x in forward], [0, 0, 0, 1])

    def test_pencil_arbitrary_two_jet_and_positive_frames(self):
        s, b, c = sp.symbols("s b c")
        F, G, H = sp.symbols("F G H")
        r = sp.Function("r")(s, b, c)
        coordinates = [s, b, c]
        speeds = [1, -F, -G * b + s * (2 * H - G * F)]
        second = action(speeds, coordinates, action(speeds, coordinates, r))
        expected = (sp.diff(r, s, 2) - 2 * F * sp.diff(r, s, b)
                    + F**2 * sp.diff(r, b, 2) + 2 * H * sp.diff(r, c))
        self.assertEqual(sp.simplify((second - expected).subs({s: 0, b: 0, c: 0})), 0)

        a, B, C, lam = sp.symbols("a B C lam")
        polynomial = a**4 + a
        old = [a, s, B, C]
        new = [a, s, b, c]
        forward = [a, s, B - s * polynomial, C - lam * B**2 / 2]
        inverse = [a, s, b + s * polynomial,
                   c + lam * (b + s * polynomial)**2 / 2]
        self.assertEqual(substitute(forward, old, inverse), new)
        self.assertEqual(substitute(inverse, new, forward), old)
        f = sp.diff(polynomial, a)
        T = [1, 0, s * f, s * lam * f * B]
        self.assertEqual([action(T, old, x) for x in forward], [1, 0, 0, 0])
        self.assertEqual([sp.diff(x, s, 2) for x in forward], [0, 0, 0, 0])
        self.assertEqual(action([0, 0, 1, lam * B], old, B), 1)

        # The f=0 boundary has its own actual inverse, not a division by f.
        G0 = a**3 + a
        forward0 = [a, s, B, C - s * G0 * B]
        inverse0 = [a, s, b, c + s * G0 * b]
        self.assertEqual(substitute(forward0, old, inverse0), new)
        self.assertEqual(substitute(inverse0, new, forward0), old)
        self.assertEqual([sp.diff(x, s, 2) for x in forward0], [0, 0, 0, 0])

    def test_leading_divisor_and_constant_apex_controls(self):
        x, y, z, w = sp.symbols("x y z w")
        variables = [x, y, z, w]
        direction = sp.symbols("d0:4")
        q = x * z - y**2
        a = q + w
        examples = [
            (sp.Matrix([1, a, a**2, -a**2 * x + 2 * a * y - z]),
             q, -x * q**2, [sp.Matrix([0, 0, 0, 1])]),
            (sp.Matrix([1, 0, y, (z - y * x)**2]),
             y, x**2 * y**2,
             [sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 0, 1, 0]),
              sp.Matrix([0, 0, 0, 1])]),
        ]
        for P, factor, leading_expected, expected_kernel in examples:
            J = P.jacobian(variables)
            self.assertEqual((J * P).applyfunc(sp.expand), sp.zeros(4, 1))
            self.assertEqual((J**3).applyfunc(sp.expand), sp.zeros(4))
            self.assertNotEqual((J**2).applyfunc(sp.expand), sp.zeros(4))
            self.assertEqual(J.rank(), 2)
            self.assertEqual(J.row_join(P).rank(), 3)
            self.assertEqual(sp.expand(factor.subs(dict(zip(variables, P)),
                                                  simultaneous=True)), 0)
            degree = max(sp.Poly(p, *variables).total_degree() for p in P)
            leading = [sum(coefficient * sp.prod(v**e for v, e in zip(variables, powers))
                           for powers, coefficient in sp.Poly(p, *variables).terms()
                           if sum(powers) == degree) for p in P]
            self.assertEqual([sp.expand(p) for p in leading],
                             [0, 0, 0, sp.expand(leading_expected)])
            good = constant_kernel(J**2 * sp.Matrix(direction), variables, direction)
            apex = constant_kernel([sum(d * sp.diff(factor, v)
                                        for d, v in zip(direction, variables))],
                                   variables, direction)
            self.assertEqual(good, expected_kernel)
            self.assertEqual(apex, expected_kernel)

    def test_nonunit_first_speed_primitive_slice(self):
        a, y, z, w = sp.symbols("a y z w")
        I, V, S = sp.symbols("I V S")
        old = [a, y, z, w]
        invariant = a * y - z
        h = 1 + a * invariant
        E = [0, a, a**2, h]
        Q = [0, 0, 0, -a]  # [partial_z,E] in the original frame.
        forward = [a, invariant, a * w - h * y, w - invariant * y]
        new = [a, I, V, S]
        inverse = [a, a * S - V, a * (a * S - V) - I,
                   (1 + a * I) * S - I * V]
        self.assertEqual(substitute(forward, old, inverse), new)
        self.assertEqual(substitute(inverse, new, forward), old)
        self.assertEqual([action(E, old, p) for p in E], [0, 0, 0, 0])
        self.assertEqual([action(E, old, p) for p in forward], [0, 0, 0, 1])
        self.assertEqual([action(Q, old, p) for p in forward[:3]], [0, 0, -a**2])
        self.assertEqual(sp.cancel(action(Q, old, forward[2]) / (-a**2)), 1)
        # Original E remains nonvanishing even on a=0, where Q vanishes.
        self.assertEqual([sp.sympify(p).subs(a, 0) for p in E], [0, 0, 0, 1])

    def test_variable_direction_commuting_slice_family(self):
        a, s, b, c, I, V = sp.symbols("a s b c I V")
        ta, ts, tb, tc = sp.symbols("ta ts tb tc")
        variables = [a, s, b, c]
        invariant = a * b - c
        h = invariant**2 + a
        E = [0, 1, h, a * h]
        T = [ta, ts, tb, tc]
        Q = [action(T, variables, sp.sympify(p)) for p in E]
        expected = [0, 0, 2 * ta * h * invariant, 2 * ta * a * h * invariant]
        self.assertEqual([action(E, variables, p) for p in Q],
                         [sp.expand(p) for p in expected])
        forward = [a, invariant, b - s * h, s]
        inverse = [a, s, V + s * (I**2 + a), a * (V + s * (I**2 + a)) - I]
        adapted = [a, I, V, s]
        self.assertEqual(substitute(forward, variables, inverse), adapted)
        self.assertEqual(substitute(inverse, adapted, forward), variables)
        self.assertEqual([action(E, variables, p) for p in forward], [0, 0, 0, 1])
        good_Q = [p.subs(ta, 0) for p in Q]
        values = [action(good_Q, variables, p) for p in forward[:3]]
        self.assertEqual(substitute(values, variables, inverse),
                         [0, 0, sp.expand(2 * I * (tb * a - tc))])

    def test_weighted_pencil_obstruction_coefficients(self):
        a, s, b, c = sp.symbols("a s b c")
        hb = sp.Function("h")(b)
        ubc = sp.Function("u")(b, c)
        coordinates = [s, b, c]
        R = s * hb + ubc  # The preceding zero-order identities impose this form.
        for ell, n in [(1, 3), (2, 3)]:
            F, G = a**n, a**ell
            K = a**(ell + 1) + a**(ell + 2)
            H = sp.Rational(n, n + ell) * a**(n + ell)
            M = 2 * H - G * F
            speed = [1, -F, -G * b - K + s * M]
            second = action(speed, coordinates, action(speed, coordinates, R))
            power = min(n, 2 * ell)
            expected = -2 * sp.diff(hb, b) if n < 2 * ell else b**2 * sp.diff(ubc, c, 2)
            self.assertEqual(sp.expand(second).coeff(a, power), expected)

        p, q, u = [sp.Function(name)(b) for name in ("p", "q", "v")]
        for ell in [1, 2]:
            n = 2 * ell
            F, G = a**n, a**ell
            K = a**(ell + 1) + a**(ell + 2)
            H = sp.Rational(2, 3) * a**(3 * ell)
            M = 2 * H - G * F
            speed = [1, -F, -G * b - K + s * M]
            resonant = s * hb + p * c**2 / 2 + q * c + u
            second = action(speed, coordinates, action(speed, coordinates, resonant))
            self.assertEqual(second.coeff(a, 2 * ell), b**2 * p - 2 * sp.diff(hb, b))
            self.assertEqual(second.coeff(a, 3 * ell).coeff(c),
                             2 * b * sp.diff(p, b) + sp.Rational(4, 3) * p)
            reduced = s + q * c + u
            reduced_second = action(speed, coordinates, action(speed, coordinates, reduced))
            self.assertEqual(sp.expand(reduced_second.coeff(s) + 2 * F * M * sp.diff(q, b)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
