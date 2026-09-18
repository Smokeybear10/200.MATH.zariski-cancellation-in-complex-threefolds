"""Independent finite exact-algebra controls for the three pass214 notes.

Formal jets and branch fixtures are not asserted to realize actual frames.
Only the explicitly constant-coefficient four-variable shears are ambient
maps here. These tests do not prove cofactor support, field return, algebraic
norm identities, universal branch expansions, or recognition/exclusion.
No retained checker or solver implementation is imported.
"""

import unittest

import sympy as s


class RankTwoHighDegreeControls(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(s.cancel(s.expand(value)), 0)

    def model(self):
        rho = s.symbols("rho", nonzero=True)
        U, V, w = s.symbols("U V w")
        j, h, K, krr, ht, hr, Kr, krrr = s.symbols("j h K krr ht hr Kr krrr")
        nt, nr, ntt, ntr, nrr, ell, lt, lr, m = s.symbols("nt nr ntt ntr nrr ell lt lr m")
        a = rho**-3
        R = 2 * a * V + j
        S = -V**3 / rho**4 + h * U**2 / 2 + K * U * V + krr * V**2 / 2 + nt * U + nr * V
        T = ell - S
        c = -3 * V**2 / rho**4 + K * U + krr * V + nr
        Q = V**4 / rho**5 + ht * U**3 / 6 + hr * U**2 * V / 2
        Q += Kr * U * V**2 / 2 + krrr * V**3 / 6
        Q += ntt * U**2 / 2 + ntr * U * V + nrr * V**2 / 2 - lt * U - lr * V - m
        H = a * T**2 + R * c * T + R**2 * Q
        St = ht * U**2 / 2 + hr * U * V + Kr * V**2 / 2 + ntt * U + ntr * V
        Sr = 4 * V**3 / rho**5 + hr * U**2 / 2 + Kr * U * V + krrr * V**2 / 2 + ntr * U + nrr * V
        Rt, Rr = K, -6 * V / rho**4 + krr
        return locals()

    def test_full_linear_center_coefficients(self):
        z = self.model()
        U, V, rho = z["U"], z["V"], z["rho"]
        a, R = z["a"], z["R"]
        # k_tt=0 also kills both derivatives of that coefficient.
        H = s.expand(z["H"].subs({z["h"]: 0, z["ht"]: 0, z["hr"]: 0}, simultaneous=True))
        b = z["nt"] - rho**3 * z["j"] * z["K"] / 2
        delta = 2 * z["ntt"] - rho**3 * z["K"]**2
        A = a * b**2 + delta * R**2 / 4
        phi = -V**3 / rho**4 + z["krr"] * V**2 / 2 + z["nr"] * V
        c0 = s.diff(phi, V)
        D = -2 * a * b * (z["ell"] - phi) - R * c0 * (z["K"] * V + z["nt"])
        D += R**2 * (z["Kr"] * V**2 / 2 + z["ntr"] * V - z["lt"])
        polynomial = s.Poly(H, U)
        self.zero(polynomial.coeff_monomial(U**2) - A)
        self.zero(polynomial.coeff_monomial(U) - D)
        self.assertEqual(polynomial.degree(), 2)
        self.zero(s.Poly(polynomial.coeff_monomial(1), V).coeff_monomial(V**6) + rho**-11)
        Vc = -rho**3 * z["j"] / 2
        self.zero(A.subs(V, Vc) - a * b**2)
        self.zero((z["ntt"] - rho**3 * z["K"]**2 / 2) - delta / 2)
        # Explicit polynomial Bezout remainder; the constant a*b^2 is nonzero
        # only after imposing the written nonzero center-slope hypothesis.
        self.zero(A - (delta * R / 4) * R - a * b**2)

        D4 = 2 * rho**-7 * (3 * z["K"] + rho * z["Kr"])
        br = z["ntr"] - s.Rational(3, 2) * rho**2 * z["j"] * z["K"]
        br -= rho**3 * z["krr"] * z["K"] / 2 + rho**3 * z["j"] * z["Kr"] / 2
        D3 = 4 * rho**-7 * (b + rho * br) + 2 * rho**3 * z["j"] * D4
        self.zero(s.Poly(s.expand(D), V).coeff_monomial(V**4) - D4)
        self.zero(s.Poly(s.expand(D), V).coeff_monomial(V**3) - D3)
        self.assertLessEqual(s.Poly(s.expand(D), V).degree(), 4)

        B, Br = s.symbols("B Br")
        normalized = {z["K"]: 0, z["Kr"]: 0, z["nt"]: B, z["ntt"]: 0, z["ntr"]: Br}
        H0 = s.expand(H.subs(normalized, simultaneous=True))
        self.zero(s.Poly(H0, U, V).coeff_monomial(U * V**3) - 4 * rho**-7 * (B + rho * Br))
        self.zero(s.Poly(H0, U, V).coeff_monomial(U**2) - rho**-3 * B**2)
        self.zero(s.Poly(H0, U, V).coeff_monomial(V**6) + rho**-11)

    def test_actual_constant_shears_and_center_slope(self):
        X, Y, Z, W, x0, y0, z0, w0 = s.symbols("X Y Z W x0 y0 z0 w0")
        alpha, beta, gamma = s.symbols("alpha beta gamma")
        forward = (X, Y, Z - gamma * Y, W + alpha * Y + beta * X)
        backward = (x0, y0, z0 + gamma * y0, w0 - alpha * y0 - beta * x0)
        for original, expression in zip((X, Y, Z, W), backward):
            self.zero(expression.subs(dict(zip((x0, y0, z0, w0), forward)), simultaneous=True) - original)
        for original, expression in zip((x0, y0, z0, w0), forward):
            self.zero(expression.subs(dict(zip((X, Y, Z, W), backward)), simultaneous=True) - original)
        self.assertEqual(tuple(s.diff(value, Z) for value in forward), (0, 0, 1, 0))
        scale = s.symbols("scale")
        scaled = {X: scale * X, Y: scale * Y, Z: scale**2 * Z, W: scale**2 * W}
        for expression, variable, degree in zip(forward, (X, Y, Z, W), (1, 1, 2, 2)):
            self.zero(s.Poly(s.expand(expression.subs(scaled, simultaneous=True)), scale).coeff_monomial(scale**degree) - variable)

        rho = s.symbols("rho", nonzero=True)
        t, y, theta, w, k, kt, j, K, n, nt = s.symbols("t y theta w k kt j K n nt")
        shift = alpha * t + beta
        z = -w / rho**2 + theta**2 / rho**3 + kt * y + j * theta + n
        sigma = -theta / rho**2 + k
        theta1, w1 = theta + shift, w + alpha * y
        k1 = k + shift / rho**2 - gamma * t
        kt1, j1 = kt + alpha / rho**2 - gamma, j - 2 * shift / rho**3
        n1 = n - j * shift + shift**2 / rho**3
        z1 = -w1 / rho**2 + theta1**2 / rho**3 + kt1 * y + j1 * theta1 + n1
        self.zero(z1 - z + gamma * y)
        self.zero(-theta1 / rho**2 + k1 - sigma + gamma * t)
        self.zero(w + theta * X + rho * X**2 + alpha * (y + t * X) + beta * X
                  - w1 - theta1 * X - rho * X**2)
        self.zero(z + sigma * X + X**2 / rho - gamma * (y + t * X)
                  - z1 - (-theta1 / rho**2 + k1) * X - X**2 / rho)
        K1 = K - 2 * alpha / rho**3
        nt1 = nt - K * shift - j * alpha + 2 * shift * alpha / rho**3
        self.zero(nt1 - rho**3 * j1 * K1 / 2 - (nt - rho**3 * j * K / 2))
        c, cstar = s.symbols("c cstar")
        values = {alpha: c / 2, beta: 0, gamma: cstar, kt: cstar - c / (2 * rho**2), K: c / rho**3}
        self.zero(kt1.subs(values, simultaneous=True))
        self.zero(K1.subs(values, simultaneous=True))
        self.zero(s.diff(cstar - c / (2 * rho**2), rho) - c / rho**3)
        self.zero(s.diff(rho**3 * (c / rho**3), rho))

    def test_weighted_sextic_and_four_branch_resultant(self):
        z = self.model()
        U, V, rho, h, hr = [z[name] for name in ("U", "V", "rho", "h", "hr")]
        scale = s.symbols("scale")
        weighted = lambda expression: s.Poly(
            s.expand(expression.subs({U: scale**6 * U, V: scale**4 * V}, simultaneous=True)), scale
        )
        polynomial = weighted(z["H"])
        self.assertEqual(polynomial.degree(), 26)
        self.zero(polynomial.coeff_monomial(scale**26) - 2 * z["ht"] * U**3 * V**2 / (3 * rho**6))
        expected_parts = (
            h**2 * U**4 / (4 * rho**3) - h * U**2 * V**3 / rho**7 + V**6 / rho**11,
            3 * h * U**2 * V**3 / rho**7 - 6 * V**6 / rho**11,
            2 * hr * U**2 * V**3 / rho**6 + 4 * V**6 / rho**11,
        )
        terms = (z["a"] * z["T"]**2, z["R"] * z["c"] * z["T"], z["R"]**2 * z["Q"])
        for term, expected in zip(terms, expected_parts):
            self.zero(weighted(term.subs(z["ht"], 0)).coeff_monomial(scale**24) - expected)
        expected = h**2 * U**4 / (4 * rho**3) + 2 * (h + rho * hr) * U**2 * V**3 / rho**7 - V**6 / rho**11
        self.zero(weighted(z["H"].subs(z["ht"], 0)).coeff_monomial(scale**24) - expected)

        # Exact finite leading-branch and resultant controls, not a test of the
        # existence/completeness of formal branches for arbitrary lower data.
        T, a6, b4, bta, Z0 = s.symbols("T a6 b4 bta Z0")
        branch_product = s.prod(Z0 - a6 * bta**6 * root**6 for root in (1, -1, s.I, -s.I))
        self.zero(branch_product - (Z0**2 - a6**2 * bta**12)**2)
        resultant = s.resultant(b4 * T**4 - V, U - a6 * T**6, T)
        self.zero(resultant - (b4**3 * U**2 - a6**2 * V**3)**2)
        A0 = h**2 / (4 * rho**3)
        cross, last = 2 * (h + rho * hr) / rho**7, -rho**-11
        self.zero(cross**2 - 4 * A0 * last - (4 * (h + rho * hr)**2 + h**2) / rho**14)

    def test_affine_second_cofactor_requires_both_potentials(self):
        z = self.model()
        U, V, w, R, a = [z[name] for name in ("U", "V", "w", "R", "a")]
        B = s.diff(z["S"], U)
        C = 2 * a * w + z["c"]
        Lt = z["lt"] - z["St"] - z["Rt"] * w
        Lr = z["lr"] - z["Sr"] - z["Rr"] * w
        first = R * w + z["S"] - z["ell"]
        second = a * w**2 + z["c"] * w + z["Q"]
        self.zero(s.diff(second, U) + Lt)
        self.zero(s.diff(second, V) + Lr)
        self.zero(s.diff(second, w) - C)
        self.zero(s.diff(z["H"], U) + R * (C * B + R * Lt)
                  - (2 * a * B - R * z["Rt"]) * first)
        self.zero(s.diff(z["H"], V) + R * (C**2 + R * Lr)
                  - 4 * a * R * second + R * z["Rr"] * first)

        r = s.symbols("r", nonzero=True)
        b, pt, pr, pv, wp, lt, lr = s.symbols("b pt pr pv wp lt lr")
        cc = -r * wp - b * pv  # Total V-derivative of the first potential.
        wt, wr = (lt - b * pt) / r, (lr - b * pr) / r
        determinant = s.Matrix([[pt, pr, pv], [b, cc, r], [wt, wr, wp]]).det()
        q1 = -r * (cc * b + r * lt)
        multiplier = pr + pv * pt + pv * wp
        residual = r**2 * determinant + multiplier * q1
        second_v = cc * wp - lt * pv - lr
        self.zero(residual - r * (r * pt - b * pv) * second_v)
        self.assertNotEqual(s.expand(r * (r * pt - b * pv) * second_v), 0)
        self.zero(residual.subs(lr, cc * wp - lt * pv))

    def test_graph_degree_and_euler_norm_arithmetic(self):
        V, U, rho = s.symbols("V U rho", nonzero=True)
        b, j, delta, p3, p4, a0 = s.symbols("b j delta p3 p4 a0", nonzero=True)
        R = 2 * V / rho**3 + j
        D = sum(coefficient * V**i for i, coefficient in enumerate(s.symbols("d0:5")))
        A = b**2 / rho**3 + delta * R**2 / 4
        for degree, leader in ((3, p3), (4, p4)):
            P = leader * V**degree + sum(coefficient * V**i for i, coefficient in enumerate(s.symbols("p0:" + str(degree))))
            q1 = s.Poly(s.expand(2 * A * P + D), V)
            self.zero(q1.coeff_monomial(V**(degree + 2)) - 2 * delta * leader / rho**6)
        qsmall = sum(coefficient * V**i for i, coefficient in enumerate(s.symbols("q0:3")))
        for degree, leader in ((3, p3), (4, p4)):
            P = leader * V**degree + sum(coefficient * V**i for i, coefficient in enumerate(s.symbols("p0:" + str(degree))))
            C = s.expand(a0 * P**2 - qsmall * P)
            self.zero(s.Poly(C, V).coeff_monomial(V**(2 * degree)) - a0 * leader**2)
            if degree == 4:
                self.assertEqual(s.Poly(C, V).degree(), 8)
            else:
                D3 = s.Poly(s.expand(qsmall - 2 * a0 * P), V).coeff_monomial(V**3)
                self.zero(D3 + 2 * a0 * p3)
                self.zero(D3**2 - 4 * a0 * s.Poly(C, V).coeff_monomial(V**6))

        c0, epsilon = s.symbols("c0 epsilon")
        J = sum(coefficient * V**i for i, coefficient in enumerate(s.symbols("j0:4")))
        G = (U - J)**2 - epsilon * R**2 * (V - c0)
        self.zero(s.discriminant(G, U) - 4 * epsilon * R**2 * (V - c0))
        Br, lam = s.symbols("Br lam")
        D3, A0, C6 = 4 * (b + rho * Br) / rho**7, b**2 / rho**3, -rho**-11
        self.zero(D3**2 - 4 * A0 * C6 - 4 * (4 * (b + rho * Br)**2 + b**2) / rho**14)
        self.zero((4 * (b + rho * Br)**2 + b**2).subs(Br, lam * b / rho)
                  - b**2 * (4 * (1 + lam)**2 + 1))
        n = s.symbols("n", positive=True, integer=True)
        for sign in (1, -1):
            exponent = -1 + sign * s.I / 2
            self.zero(4 * (1 + exponent)**2 + 1)
            self.zero(s.im(n * exponent) - sign * n / 2)
        # Bounded product-rule controls support, but do not prove, the field norm.
        for count in range(1, 5):
            factors = s.symbols("b0:" + str(count), nonzero=True)
            product = s.prod(factors)
            derivative = sum(s.diff(product, value) * lam * value / rho for value in factors)
            self.zero(rho * derivative - count * lam * product)
        t = s.symbols("t")
        unit = (1 + rho + t * rho**2) / (1 - rho + t**2 * rho**2)
        for order in range(-3, 4):
            rational = rho**order * unit
            logarithmic = s.cancel(rho * s.diff(rational, rho) / rational)
            self.zero(logarithmic.subs(rho, 0) - order)


if __name__ == "__main__":
    unittest.main()
