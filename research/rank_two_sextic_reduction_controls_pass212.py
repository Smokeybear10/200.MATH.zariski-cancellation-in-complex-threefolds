"""Independent finite identities for the rank-two sextic reduction212.

These controls do not certify actual realization, field return, conductor
bounds, immersion, the all-degree cone lemma, or branch recognition. Formal
coefficient jets and cone fixtures are not asserted to be actual four-frames.
No retained checker or solver implementation is imported.
"""

import unittest

import sympy as s


class RankTwoSexticControls(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(s.cancel(s.expand(value)), 0)

    def model(self):
        rho = s.symbols("rho", nonzero=True)
        U, V, w = s.symbols("U V w")
        kr, ktt, ktr, krr, kttt, kttr, ktrr, krrr = s.symbols(
            "kr ktt ktr krr kttt kttr ktrr krrr"
        )
        nt, nr, ntt, ntr, nrr, ell, lt, lr, m = s.symbols(
            "nt nr ntt ntr nrr ell lt lr m"
        )
        A = rho**-3
        R = 2 * A * V + kr
        S = -V**3 / rho**4 + ktt * U**2 / 2 + ktr * U * V
        S += krr * V**2 / 2 + nt * U + nr * V
        T = ell - S
        c = -3 * V**2 / rho**4 + ktr * U + krr * V + nr
        Q = V**4 / rho**5 + kttt * U**3 / 6 + kttr * U**2 * V / 2
        Q += ktrr * U * V**2 / 2 + krrr * V**3 / 6
        Q += ntt * U**2 / 2 + ntr * U * V + nrr * V**2 / 2 - lt * U - lr * V - m
        St = kttt * U**2 / 2 + kttr * U * V + ktrr * V**2 / 2 + ntt * U + ntr * V
        Sr = 4 * V**3 / rho**5 + kttr * U**2 / 2 + ktrr * U * V
        Sr += krrr * V**2 / 2 + ntr * U + nrr * V
        Rt, Rr = ktr, -6 * V / rho**4 + krr
        H = A * T**2 + R * c * T + R**2 * Q
        return locals()

    def test_sextic_center_and_finite_degree_list(self):
        z = self.model()
        U, V, rho = z["U"], z["V"], z["rho"]
        H, R, S, T, c, Q, A = [z[name] for name in ("H", "R", "S", "T", "c", "Q", "A")]
        scale = s.symbols("scale")
        top = lambda expression: s.Poly(
            s.expand(expression.subs({U: scale * U, V: scale * V}, simultaneous=True)), scale
        ).coeff_monomial(scale**6)
        for expression, coefficient in zip((A * T**2, R * c * T, R**2 * Q), (1, -6, 4)):
            self.zero(top(expression) - coefficient * V**6 / rho**11)
        self.zero(top(H) + V**6 / rho**11)
        polynomial = s.Poly(s.expand(H), U, V)
        self.assertEqual(polynomial.total_degree(), 6)
        self.assertEqual(polynomial.degree(U), 4)
        coefficients_u = s.Poly(s.expand(H), U)
        self.zero(coefficients_u.coeff_monomial(U**4) - z["ktt"]**2 / (4 * rho**3))
        for power, bound in ((3, 2), (2, 3), (1, 4), (0, 6)):
            self.assertLessEqual(s.Poly(coefficients_u.coeff_monomial(U**power), V).degree(), bound)
        # Vanishing k_tt entails vanishing both displayed derivatives of it.
        dropped = s.expand(H.subs({z["ktt"]: 0, z["kttt"]: 0, z["kttr"]: 0}, simultaneous=True))
        self.assertLessEqual(s.Poly(dropped, U).degree(), 2)

        Vc = -rho**3 * z["kr"] / 2
        p = S.subs(V, Vc) - z["ell"]
        D = (V**2 + V * Vc + Vc**2) / (2 * rho)
        D -= rho**3 * z["krr"] * (V + Vc) / 4
        D -= rho**3 * (z["ktr"] * U + z["nr"]) / 2
        self.zero(R.subs(V, Vc))
        self.zero(S - z["ell"] - p + R * D)
        self.assertLessEqual(s.Poly(s.expand(D), U, V).total_degree(), 2)
        self.assertLessEqual(s.Poly(s.expand(p), U).degree(), 2)
        self.zero(H.subs(V, Vc) - A * p**2)

        # Enumerate only the finite integer consequences of the proved bounds.
        pairs = [(d, e) for d in range(2, 7) for e in range(1, min(d, 5))
                 if e == 1 or s.igcd(d, e) != 1 or (d - 1) * (e - 1) <= e]
        expected = [(d, 1) for d in range(2, 7)] + [(3, 2), (4, 2), (6, 2), (6, 3), (6, 4)]
        self.assertEqual(sorted(pairs), sorted(expected))
        forced_zero_ktt = [pair for pair in pairs if pair[0] > 2 * pair[1]]
        self.assertEqual(sorted(forced_zero_ktt), [(3, 1), (4, 1), (5, 1), (6, 1), (6, 2)])

    def test_undivided_potential_gradients_and_wedge(self):
        z = self.model()
        U, V, w = z["U"], z["V"], z["w"]
        A, R, S, T, c, Q, H = [z[name] for name in ("A", "R", "S", "T", "c", "Q", "H")]
        B = s.diff(S, U)
        C = 2 * A * w + c
        Lt = z["lt"] - z["St"] - z["Rt"] * w
        Lr = z["lr"] - z["Sr"] - z["Rr"] * w
        first = R * w + S - z["ell"]
        second = A * w**2 + c * w + Q
        self.zero(s.diff(S, V) - c)
        self.zero(s.diff(c, U) - z["Rt"])
        self.zero(s.diff(c, V) - z["Rr"])
        self.zero(s.diff(Q, U) - z["St"] + z["lt"])
        self.zero(s.diff(Q, V) - z["Sr"] + z["lr"])
        for derivative, expected in zip((s.diff(first, U), s.diff(first, V), s.diff(first, w)), (B, C, R)):
            self.zero(derivative - expected)
        for derivative, expected in zip((s.diff(second, U), s.diff(second, V), s.diff(second, w)), (-Lt, -Lr, C)):
            self.zero(derivative - expected)

        # Exact prior-potential remainders, before setting either potential to zero.
        self.zero(H - R**2 * second + first * (A * (T + R * w) + R * c))
        self.zero(s.diff(H, U) + R * (C * B + R * Lt)
                  - (2 * A * B - R * z["Rt"]) * first)
        self.zero(s.diff(H, V) + R * (C**2 + R * Lr)
                  - 4 * A * R * second + R * z["Rr"] * first)

        # Independent evaluated jets, imposing precisely the three derivatives
        # of the first potential. This checks the calibration algebra, not its
        # actual nonzero value or coefficient-field interpretation.
        r = s.symbols("r", nonzero=True)
        b, cc, lt, lr = s.symbols("b cc lt lr")
        yt, yr, yv, vt, vr, vv = s.symbols("yt yr yv vt vr vv")
        wt = (-b * yt - cc * vt + lt) / r
        wr = (-b * yr - cc * vr + lr) / r
        wv = (-b * yv - cc * vv) / r
        J = s.Matrix([[yt, yr, yv], [r * vt + b, r * vr + cc, r * vv], [wt, wr, wv]]).det()
        DU = r * (yv * vr - yr * vv) + cc * yv
        DV = r * (yt * vv - yv * vt) - b * yv
        HU, HV = -r * (cc * b + r * lt), -r * (cc**2 + r * lr)
        self.zero(r**3 * J - DU * HU - DV * HV)

    def test_cone_shear_and_opposite_pair_power_sums(self):
        P, Q, S = s.symbols("P Q S")
        H = s.Function("H")(P)  # In the proof H is an arbitrary polynomial.
        forward = (P, Q - P * H, S - 2 * Q * H + P * H**2)
        backward = (P, Q + P * H, S + 2 * Q * H + P * H**2)
        for map1, map2 in ((forward, backward), (backward, forward)):
            substitution = dict(zip((P, Q, S), map1))
            for variable, expression in zip((P, Q, S), map2):
                self.zero(expression.subs(substitution, simultaneous=True) - variable)
        self.zero(forward[0] * forward[2] - forward[1]**2 - (P * S - Q**2))
        a, b, h = s.symbols("a b h")
        self.zero(a * (b - a * h) - (a * b - a**2 * h))
        self.zero((b - a * h)**2 - (b**2 - 2 * a * b * h + a**2 * h**2))

        x, sigma, c = s.symbols("x sigma c")
        pi = (sigma**2 + 2 * c) / 2
        companion = s.Matrix([[0, -pi], [1, sigma]])
        sums = [s.Integer(2), sigma]
        for j in range(2, 17):
            sums.append(s.expand(sigma * sums[-1] - pi * sums[-2]))
        power = s.eye(2)
        for j, value in enumerate(sums):
            self.zero(s.trace(power) - value)
            power = (power * companion).applyfunc(s.expand)
            leading = s.expand(value).coeff(sigma, j)
            expected = s.expand(((1 + s.I) / 2)**j + ((1 - s.I) / 2)**j)
            self.zero(leading - expected)
            self.assertEqual(leading == 0, j % 4 == 2)
        A4, A3, A2, A1, A0 = s.symbols("A4 A3 A2 A1 A0")
        actual = A4 * sums[4] + A3 * sums[3] + A2 * sums[2] + A1 * sums[1] + A0 * sums[0]
        displayed = -A4 * sigma**4 / 2 - A3 * sigma**3 / 2 - 2 * A4 * c * sigma**2
        displayed += (A1 - 3 * A3 * c) * sigma + 2 * A4 * c**2 - 2 * A2 * c + 2 * A0
        self.zero(actual - displayed)
        self.zero((sigma**2 - 4 * pi) + 4 * ((sigma / 2)**2 + c))

        # Finite cancellation controls for the omitted leading residue class.
        beta = s.symbols("beta", nonzero=True)
        for n in (2, 6, 10, 14):
            aa = x**2 + c
            exponent = (n - 2) // 4
            remainder = beta * x**n - aa * beta * (aa**2)**exponent
            self.assertLess(s.Poly(s.expand(remainder), x).degree(), n)

    def test_repeated_center_fiber_and_cubic_collision(self):
        rho, kappa = s.symbols("rho kappa", nonzero=True)
        U, V, U0, Vc, w = s.symbols("U V U0 Vc w")
        d20, d11, d02, d10, d01, d00 = s.symbols("d20 d11 d02 d10 d01 d00")
        D = d20 * U**2 + d11 * U * V + d02 * V**2 + d10 * U + d01 * V + d00
        R = 2 * (V - Vc) / rho**3
        potential = R * (w - D) + kappa * (U - U0)**2
        B = -R * s.diff(D, U) + 2 * kappa * (U - U0)
        C = 2 * (w - D) / rho**3 - R * s.diff(D, V)
        self.zero(s.diff(potential, U) - B)
        self.zero(s.diff(potential, V) - C)
        self.zero(s.diff(potential, w) - R)
        self.zero(R * (-(w - D) / kappa) - (U - U0)**2 + potential / kappa)
        vertex = {U: U0, V: Vc, w: D.subs({U: U0, V: Vc}, simultaneous=True)}
        for entry in (B, C, R):
            self.zero(entry.subs(vertex, simultaneous=True))

        b1 = s.symbols("b1", nonzero=True)
        multiplication_y = s.Matrix([[U0, 0], [b1, U0]])
        self.zero((U * s.eye(2) - multiplication_y).det() - (U - U0)**2)
        self.zero((rho**-3 * kappa**2 * (U - U0)**4)
                  - (U - U0)**2 * (rho**-3 * kappa**2 * (U - U0)**2))
        x, A, B0, root = s.symbols("x A B0 root")
        theta, y = x**2, A * x**3 + B0 * x
        relation = U**2 - V * (A * V + B0)**2
        self.zero(relation.subs({U: y, V: theta}, simultaneous=True))
        self.zero(theta - theta.subs(x, -x))
        self.zero(y - y.subs(x, -x) - 2 * x * (A * x**2 + B0))
        for point in (root, -root):
            self.zero(y.subs({x: point, B0: -A * root**2}, simultaneous=True))
            self.zero(theta.subs(x, point) - root**2)
        self.zero(s.diff(theta, x).subs(x, 0))
        self.zero(s.diff(y, x).subs({x: 0, B0: 0}, simultaneous=True))


if __name__ == "__main__":
    unittest.main()
