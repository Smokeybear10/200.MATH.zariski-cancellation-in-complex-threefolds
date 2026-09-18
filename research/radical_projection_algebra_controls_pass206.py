"""Finite exact-algebra controls for the three working pass206 notes.

These standalone symbolic checks do not certify an initial-kernel theorem,
field contraction, integral closure, the universal semigroup argument, LND
properties, or recognition. The cusp/node fixtures are formal plane rings,
not actual globally sliced fourfold frames. No earlier checker is imported.
"""

import math
import unittest

import sympy as s


def zero(expression):
    return s.cancel(s.expand(expression)) == 0


def put(expression, substitutions):
    return expression.subs(substitutions, simultaneous=True)


class RadicalProjectionAlgebra206(unittest.TestCase):
    def assertZero(self, expression):
        self.assertTrue(zero(expression), str(expression))

    def test_weighted_normal_forms_and_actual_inverse_formulas(self):
        X, Y, Z, W, U, V, scale = s.symbols("X Y Z W U V scale")
        alpha, beta, c, gamma, root = s.symbols("alpha beta c gamma root")
        cprime = c - alpha**2 / 4
        rank_one = Z**2 + alpha * X**2 * Z + beta * X**2 * W + c * X**4
        # beta is nonzero in the stated rank-one normalization.
        one_forward = {U: Z + alpha * X**2 / 2, V: -beta * W - cprime * X**2}
        one_inverse = {Z: U - alpha * X**2 / 2, W: -(V + cprime * X**2) / beta}
        self.assertZero(rank_one - put(U**2 - X**2 * V, one_forward))
        for target, formula in one_forward.items():
            self.assertZero(put(formula, one_inverse) - target)
        for source, formula in one_inverse.items():
            self.assertZero(put(formula, one_forward) - source)
        # gamma is independent and nonzero in the inverse rational formulas.
        rank_two = Z * W + alpha * X**2 * Z + beta * X**2 * W + (alpha * beta - gamma) * X**4
        two_forward = {U: Z + beta * X**2, V: (W + alpha * X**2) / gamma}
        two_inverse = {Z: U - beta * X**2, W: gamma * V - alpha * X**2}
        self.assertZero(rank_two - gamma * put(U * V - X**4, two_forward))
        for target, formula in two_forward.items():
            self.assertZero(put(formula, two_inverse) - target)
        for source, formula in two_inverse.items():
            self.assertZero(put(formula, two_forward) - source)
        weight_scale = {X: scale * X, Y: scale * Y, Z: scale**2 * Z, W: scale**2 * W}
        for equation in (rank_one, rank_two):
            self.assertZero(put(equation, weight_scale) - scale**4 * equation)
        for formula in (*one_forward.values(), *two_forward.values()):
            self.assertZero(put(formula, weight_scale) - scale**2 * formula)
        # Degenerate coefficients give literal factorizations, not new frames.
        self.assertZero(put(rank_one, {beta: 0, c: alpha**2 / 4 - root**2})
                        - (Z + (alpha / 2 - root) * X**2) * (Z + (alpha / 2 + root) * X**2))
        self.assertZero(rank_two.subs(gamma, 0) - (Z + beta * X**2) * (W + alpha * X**2))
        T, Q, P, rho = s.symbols("T Q P rho")
        for equation, ratio in ((Z**2 - X**2 * W, Q**2 - P), (Z * W - X**4, Q * P - 1)):
            self.assertZero(put(equation, {Y: T * X, Z: Q * X**2, W: P * X**2}) - X**4 * ratio)
        self.assertZero(s.diff(rho**2, rho, 2) - 2)
        self.assertZero(s.diff(1 / rho, rho, 2) - 2 / rho**3)

    def test_undivided_eliminant_gradients_and_calibrated_wedge(self):
        U, V, w = s.symbols("U V w")
        k = {(i, j): s.Symbol(f"k{i}{j}") for i in range(4) for j in range(4 - i)}
        n = {(i, j): s.Symbol(f"n{i}{j}") for i in range(3) for j in range(3 - i)}
        ell, ell_t, ell_r, m = s.symbols("ell ell_t ell_r m")

        def coefficient_derivative(expression, direction):
            result = 0
            for jets, order in ((k, 3), (n, 2)):
                for (i, j), value in jets.items():
                    if i + j < order:
                        following = jets[i + (direction == 0), j + (direction == 1)]
                        result += s.diff(expression, value) * following
            return result + s.diff(expression, ell) * (ell_t if direction == 0 else ell_r)

        def homogeneous(jets, order):
            return sum(jets[i, order - i] * U**i * V**(order - i)
                       / (s.factorial(i) * s.factorial(order - i)) for i in range(order + 1))

        f = V**2 + k[1, 0] * U + k[0, 1] * V + n[0, 0]
        R = s.diff(f, V)
        S = homogeneous(k, 2) + homogeneous(n, 1)
        b = coefficient_derivative(f, 1)
        Q = homogeneous(k, 3) + homogeneous(n, 2) - ell_t * U - ell_r * V - m
        T = ell - S
        third = R * w - T
        fourth = w**2 + b * w + Q
        H = T**2 + R * b * T + R**2 * Q
        self.assertZero(b - s.diff(S, V))
        self.assertZero(H - R**2 * fourth + third * (T + R * w + R * b))
        B, C = s.diff(S, U), 2 * w + b
        Rt, Rr = coefficient_derivative(R, 0), coefficient_derivative(R, 1)
        Lt = ell_t - coefficient_derivative(S, 0) - Rt * w
        Lr = ell_r - coefficient_derivative(S, 1) - Rr * w
        for variable, expected in ((U, B), (V, C), (w, R)):
            self.assertZero(s.diff(third, variable) - expected)
        for variable, expected in ((U, -Lt), (V, -Lr), (w, C)):
            self.assertZero(s.diff(fourth, variable) - expected)
        # These are polynomial residual identities before either potential is zero.
        self.assertZero(s.diff(H, U) + R * (C * B + R * Lt) - (2 * B - R * Rt) * third)
        self.assertZero(s.diff(H, V) + R * (C**2 + R * Lr) - 4 * R * fourth + R * Rr * third)
        Hpoly = s.Poly(s.expand(H), U, V)
        top_five = sum(coef * U**i * V**j for (i, j), coef in Hpoly.terms() if i + j == 5)
        self.assertEqual(Hpoly.total_degree(), 5)
        self.assertZero(top_five - 4 * V**2 * homogeneous(k, 3))
        self.assertZero(s.expand(H).coeff(U, 4) - k[2, 0]**2 / 4)
        third_jets_zero = {value: 0 for (i, j), value in k.items() if i + j == 3}
        Hdrop = s.Poly(put(H, third_jets_zero), U, V)
        top_four = sum(coef * U**i * V**j for (i, j), coef in Hdrop.terms() if i + j == 4)
        expected_four = homogeneous(k, 2)**2 - 2 * V * (k[1, 1] * U + k[0, 2] * V) * homogeneous(k, 2) + 4 * V**2 * homogeneous(n, 2)
        self.assertZero(top_four - expected_four)
        self.assertLessEqual(s.Poly(put(H, {k[2, 0]: 0, k[3, 0]: 0, k[2, 1]: 0}), U).degree(), 2)
        center_v = -k[0, 1] / 2
        center = S.subs(V, center_v) - ell
        division = -k[1, 1] * U / 2 - k[0, 2] * (V + center_v) / 4 - n[0, 1] / 2
        self.assertZero(S - ell - center + R * division)
        self.assertZero(H.subs(V, center_v) - center**2)

        # Independent differential rows, with all prior-potential errors retained.
        rr, bb, cc, lt, lr, rt, rp, p3, p4 = s.symbols("rr bb cc lt lr rt rp p3 p4")
        yt, yr, yv, vt, vr, vv, wt, wr, wv = s.symbols("yt yr yv vt vr vv wt wr wv")
        yrow = s.Matrix([[yt, yr, yv]])
        vrow = s.Matrix([[vt, vr, vv]])
        wrow = s.Matrix([[wt, wr, wv]])
        middle = rr * vrow + s.Matrix([[bb, cc, 0]])
        constrained_w = -bb * yrow - cc * vrow + s.Matrix([[lt, lr, 0]])
        differential_error = rr * wrow - constrained_w
        det = lambda row3: s.Matrix.vstack(yrow, middle, row3).det()
        Jraw, Jnumerator = det(wrow), det(constrained_w)
        error_det = det(differential_error)
        self.assertZero(rr * Jraw - Jnumerator - error_det)
        DU = rr * (yv * vr - yr * vv) + cc * yv
        DV = rr * (yt * vv - yv * vt) - bb * yv
        HU = -rr * (cc * bb + rr * lt)
        HV = -rr * (cc**2 + rr * lr)
        self.assertZero(DU * HU + DV * HV - rr**2 * Jnumerator)
        full_HU = HU + (2 * bb - rr * rt) * p3
        full_HV = HV + 4 * rr * p4 - rr * rp * p3
        expected_error = DU * (2 * bb - rr * rt) * p3 + DV * (4 * rr * p4 - rr * rp * p3) - rr**2 * error_det
        self.assertZero(DU * full_HU + DV * full_HV - rr**3 * Jraw - expected_error)
        # Setting p3=p4=0 and differential_error=0 yields the calibrated R^3 J identity.

    def test_finite_coprime_semigroup_and_conductor_budget(self):
        allowed = set()
        for d in range(2, 6):
            for e in range(2, 5):
                if math.gcd(d, e) != 1:
                    continue

                def belongs(value):
                    return any(value >= j * e and (value - j * e) % d == 0 for j in range(d))

                ceiling = d * e + d + e
                gaps = [value for value in range(ceiling) if not belongs(value)]
                conductor = max(gaps) + 1
                residues = [(j * e) % d for j in range(d)]
                self.assertEqual(sorted(residues), list(range(d)))
                self.assertEqual(len(gaps), (d - 1) * (e - 1) // 2)
                self.assertEqual(len(gaps), sum((j * e - residues[j]) // d for j in range(d)))
                self.assertEqual(max(gaps), d * e - d - e)
                self.assertEqual(conductor, (d - 1) * (e - 1))
                self.assertTrue(all(belongs(value) for value in range(conductor, ceiling)))
                # Finite consistency check for the required degrees of R*v^n.
                if conductor <= e:
                    allowed.add((d, e))
                    self.assertTrue(all(belongs(value) for value in range(e, ceiling)))
                else:
                    self.assertTrue(any(value >= e for value in gaps))
        self.assertEqual(allowed, {(2, 3), (3, 2)})
        # This enumerates only the degree window of the saved proof, not all pairs.
        noncoprime = {(d, e) for d in range(2, 6) for e in range(2, 5) if math.gcd(d, e) > 1}
        self.assertEqual(noncoprime, {(2, 2), (2, 4), (3, 3), (4, 2), (4, 4)})

    def test_cubic_normalization_even_odd_and_formal_defect_fixtures(self):
        v, x, U, V, z, c = s.symbols("v x U V z c")
        a, b, c0, d, e, f1, g0 = s.symbols("a b c0 d e f1 g0")
        F, G = s.symbols("F G")
        shift = b / (2 * a)
        quadratic = a * v**2 + b * v + c0
        cubic = d * v**3 + e * v**2 + f1 * v + g0
        c2 = e - 3 * d * shift
        c1 = (f1 - 2 * e * shift + 3 * d * shift**2) / d
        constant = -d * shift**3 + e * shift**2 - f1 * shift + g0
        forward = {U: F / a + shift**2 - c0 / a, V: (G - c2 * (F / a + shift**2 - c0 / a) - constant) / d}
        inverse = {F: a * (U - shift**2) + c0, G: d * V + c2 * U + constant}
        for target, expression in forward.items():
            self.assertZero(put(expression, inverse) - target)
        for source, expression in inverse.items():
            self.assertZero(put(expression, forward) - source)
        parameter_sub = {F: quadratic.subs(v, x - shift), G: cubic.subs(v, x - shift)}
        self.assertZero(put(forward[U], parameter_sub) - x**2)
        self.assertZero(put(forward[V], parameter_sub) - x**3 - c1 * x)

        plane = {U: x**2, V: x * (x**2 + c)}
        relation = V**2 - U * (U + c)**2
        self.assertZero(put(relation, plane))
        for power in range(7):
            representative = (U + c) * U**(power // 2) if power % 2 == 0 else V * U**(power // 2)
            self.assertZero((x**2 + c) * x**power - put(representative, plane))
        Ac = s.symbols("A0:4")
        Bc = s.symbols("B0:4")
        even = sum(Ac[i] * z**i for i in range(4))
        odd = sum(Bc[i] * z**i for i in range(4))
        aq, ar = s.div(even, z + c, z)
        bq, br = s.div(odd, z + c, z)
        self.assertZero(ar - even.subs(z, -c))
        self.assertZero(br - odd.subs(z, -c))
        h = even.subs(z, x**2) + x * odd.subs(z, x**2)
        self.assertZero(h - (x**2 + c) * (aq.subs(z, x**2) + x * bq.subs(z, x**2)) - ar - x * br)
        # Membership of h uses br=0; membership of x*h additionally uses ar=0.
        self.assertZero(x * h - x**2 * odd.subs(z, x**2) - x * even.subs(z, x**2))
        self.assertEqual(s.rem(s.Integer(1), z + c, z), 1)  # missing odd class x
        self.assertZero(relation.subs(c, 0) - (V**2 - U**3))
        node_local = s.expand(relation.subs(U, z - c))
        self.assertZero(node_local - (V**2 + c * z**2 - z**3))
        # Purely formal nodal boundary: it meets the module/conductor identities,
        # but no Taylor-potential or scalar-Jacobian claim is made for it.
        y, theta, w = x * (x**2 - 1), (x**2 - 1) / 2, x
        R = 2 * theta
        self.assertZero(R * w - y)
        self.assertZero(w**2 - 2 * theta - 1)
        self.assertZero(y**2 - 4 * theta**2 * (2 * theta + 1))
        self.assertEqual((y.subs(x, 1), theta.subs(x, 1)), (y.subs(x, -1), theta.subs(x, -1)))
        self.assertNotEqual(w.subs(x, 1), w.subs(x, -1))


if __name__ == "__main__":
    unittest.main()
