"""Finite symbolic controls for the three pass208 working arguments.

Checks of identities, jets and inverse maps are not proofs of time-degree
rigidity, field constants, conductor geometry, actual-field descent, or the
global unit-speed conclusion. The I-only parameter is handled through an
exact invariant argument, not by testing a list of polynomial degrees.
No earlier checker or solver implementation is imported.
"""

import unittest

import sympy as s


def put(expression, substitutions):
    return expression.subs(substitutions, simultaneous=True)


class RadicalBranchControls208(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_general_I_only_replica_inverse_and_leading_root_identities(self):
        X, Y, Z, W, j = s.symbols("X Y Z W j")
        xi, eta, r, T = s.symbols("xi eta r T")
        I = W**2 + X * Y - X**2 * Z
        forward = {X: xi, W: eta + xi * j, Z: T + j**2,
                   Y: 2 * r + xi * T - 2 * eta * j}
        xhat = W - X * j
        rhat = (Y + 2 * W * j - X * j**2 - X * Z) / 2
        That = Z - j**2
        self.assertZero(put(I, forward) - eta**2 - 2 * r * xi)
        inverse = {xi: X, eta: xhat, r: rhat, T: That}
        for coordinate, formula in inverse.items():
            self.assertZero(put(formula, forward) - coordinate)
        for coordinate, formula in forward.items():
            self.assertZero(put(formula, inverse) - coordinate)
        self.assertZero(xhat**2 + 2 * rhat * X - I)
        # Both argument identities make the same j=P(I) valid in both orders
        # for every polynomial P. No test claims the degree-rigidity theorem.
        delta = lambda expression: X * s.diff(expression, W) - 2 * W * s.diff(expression, Y)
        self.assertZero(delta(I))
        P = s.Function("P")
        self.assertZero(delta(P(I)))
        # Independent formal E-jets under E(a)=E(g)=0 and e=g^2,h=a*g.
        a, g, EX, EW, EZ = s.symbols("a g EX EW EZ")
        formal_E = lambda expression: (a * s.diff(expression, X)
                                      + EW * s.diff(expression, W)
                                      + EZ * s.diff(expression, Z)
                                      + 2 * a * g * s.diff(expression, EW)
                                      + 2 * g**2 * s.diff(expression, EZ))
        d = EW - 2 * g * X
        c = a * EZ - g * EW
        self.assertZero(formal_E(d))
        self.assertZero(formal_E(c))
        self.assertZero(formal_E(a * W - g * X**2) - a * d)
        self.assertZero(formal_E(a * Z - g * W) - c)

    def test_cusp_and_node_local_jet_signs(self):
        x, U, V, H = s.symbols("x U V H")
        B, C, Lt, Lr, ktt, ktr, krr = s.symbols("B C Lt Lr ktt ktr krr")
        a2, a3, a4, b2, b3, b4, w1, w2, w3 = s.symbols("a2 a3 a4 b2 b3 b4 w1 w2 w3")
        q20, q11, q02 = s.symbols("q20 q11 q02")
        third = B * U + C * V + 2 * V * H + ktt * U**2 / 2 + ktr * U * V + krr * V**2 / 2
        fourth = -Lt * U - Lr * V + C * H + H**2 + ktr * U * H + krr * V * H + q20 * U**2 + q11 * U * V + q02 * V**2
        jet = {U: a2 * x**2 + a3 * x**3 + a4 * x**4,
               V: b2 * x**2 + b3 * x**3 + b4 * x**4,
               H: w1 * x + w2 * x**2 + w3 * x**3}
        pjet, kjet = s.expand(put(third, jet)), s.expand(put(fourth, jet))
        self.assertZero(kjet.coeff(x, 1) - C * w1)
        self.assertZero(pjet.coeff(x, 2).subs(C, 0) - B * a2)
        self.assertZero(put(pjet.coeff(x, 3), {C: 0, a2: 0}) - B * a3 - 2 * b2 * w1)
        self.assertZero(put(kjet.coeff(x, 2), {C: 0, a2: 0}) - w1**2 + Lr * b2)
        yc_r, yc_t, Sr, ell_r, w0, wt, wr = s.symbols("yc_r yc_t Sr ell_r w0 wt wr")
        actual_Lr = ell_r - Sr - krr * w0
        center_derivative = B * yc_r + Sr + (-2 * w0) * (-krr / 2) - ell_r
        self.assertZero(center_derivative - B * yc_r + actual_Lr)
        cusp_J = s.Matrix([[yc_t, yc_r, 0], [B, 0, 0], [wt, wr, w1]]).det()
        self.assertZero(cusp_J + B * yc_r * w1)
        self.assertZero(b2 * cusp_J + w1**3 - w1 * (w1**2 - b2 * B * yc_r))
        self.assertZero(s.Rational(1, 2)**3 - s.Rational(1, 8))  # normalized207 cusp
        yc, ystar = s.symbols("yc ystar")
        star = -b2 / b3
        self.assertZero((yc + a3 * x**3).subs(x, star) - yc + a3 * b2**3 / b3**3)
        p = ktt * (U - yc) * (U - ystar) / 2
        substitutions = {ystar: yc - a3 * b2**3 / b3**3, ktt: 2 * B * b3**3 / (a3 * b2**3)}
        self.assertZero(put(s.diff(p, U).subs(U, yc), substitutions) - B)

        c, node, y0, A2, A3, r0, r1, kr, BD = s.symbols("c node y0 A2 A3 r0 r1 kr BD")
        y = y0 + A2 * x**2 + A3 * x * (x**2 + c)
        R = (x**2 + c) * (r1 * x + r0)
        theta = (R - kr) / 2
        for root in (node, -node):
            base = {c: -node**2, x: root}
            self.assertZero(put(s.diff(y, x), base) - 2 * root * (A2 + A3 * root))
            self.assertZero(put(s.diff(theta, x), base) - root * (r0 + r1 * root))
        Cplus = -2 * BD * (A2 + A3 * node) / (r0 + r1 * node)
        Cminus = -2 * BD * (A2 - A3 * node) / (r0 - r1 * node)
        self.assertZero((r0**2 - r1**2 * node**2) * (Cplus + Cminus) + 4 * BD * (A2 * r0 - A3 * r1 * node**2))
        r0_value = -c * A3 * r1 / A2
        xstar = c * A3 / A2
        self.assertZero(-r0_value / r1 - xstar)
        self.assertZero((A2 * r1 - A3 * r0_value) - r1 * (A2**2 + c * A3**2) / A2)
        self.assertZero(xstar**2 + c - c * (A2**2 + c * A3**2) / A2**2)
        self.assertZero(y.subs(x, xstar) - (y0 - A2 * c) - c * (A2**2 + c * A3**2)**2 / A2**3)

    def test_actual_k_normalization_and_conic_coefficient_gates(self):
        X, Y, Z, W, XP, YP, ZP, WP = s.symbols("X Y Z W XP YP ZP WP")
        shift, alpha, beta, A1, A2, A3, A4, A5 = s.symbols("shift alpha beta A1 A2 A3 A4 A5")
        forward = {XP: X + shift, YP: Y, ZP: Z - A3 * Y - A5 * (X + shift), WP: W + alpha * Y + beta * (X + shift)}
        inverse = {X: XP - shift, Y: YP, Z: ZP + A3 * YP + A5 * XP, W: WP - alpha * YP - beta * XP}
        for coordinate, expression in forward.items():
            self.assertZero(put(expression, inverse) - coordinate)
        for coordinate, expression in inverse.items():
            self.assertZero(put(expression, forward) - coordinate)
        for coordinate, expression in forward.items():
            self.assertZero(s.diff(expression, Z) - (1 if coordinate == ZP else 0))
        t, rho, y, z, w, theta = s.symbols("t rho y z w theta")
        k = A1 * t * rho + A2 * rho**2 / 2 + A3 * t + A4 * rho + A5
        sigma = 2 * rho * theta + k
        chart = {X: XP - shift, Y: y + t * (XP - shift),
                 Z: z + sigma * (XP - shift) + rho**2 * (XP - shift)**2,
                 W: w + theta * (XP - shift) + rho * (XP - shift)**2}
        new_Z, new_W = s.expand(put(forward[ZP], chart)), s.expand(put(forward[WP], chart))
        self.assertZero(new_Z.coeff(XP, 2) - rho**2)
        self.assertZero(new_W.coeff(XP, 2) - rho)
        knew = new_Z.coeff(XP, 1) - 2 * rho * new_W.coeff(XP, 1)
        self.assertZero(knew - (k + 2 * shift * rho**2 - 2 * alpha * t * rho - 2 * beta * rho - A3 * t - A5))
        self.assertZero(put(knew, {shift: -A2 / 4, alpha: A1 / 2, beta: A4 / 2}))

        v, b, lam, nrr, D, K, p2, p1, p0, a1, a0 = s.symbols("v b lam nrr D K p2 p1 p0 a1 a0")
        theta_v = p2 * v**2 + p1 * v + p0
        xi = a1 * v + a0
        eta = b * theta_v + xi
        conic = s.expand(eta**2 + 2 * lam * theta_v * eta + nrr * theta_v**2 / 2 - D * theta_v - K)
        self.assertZero(conic.coeff(v, 4) - p2**2 * (b**2 + 2 * lam * b + nrr / 2))
        self.assertZero(conic.coeff(v, 3).subs(nrr, -2 * b**2 - 4 * lam * b) - 2 * p2 * a1 * (b + lam))
        self.assertZero(put(conic, {b: -lam, nrr: 2 * lam**2}) - xi**2 + D * theta_v + K)
        U, V, nt, nr, ntt, ntr, ell, ellt, ellr, m = s.symbols("U V nt nr ntt ntr ell ellt ellr m")
        S, R = nt * U + nr * V, 2 * V
        Q = ntt * U**2 / 2 + ntr * U * V + nrr * V**2 / 2 - ellt * U - ellr * V - m
        eliminant = s.Poly((ell - S)**2 + R * nr * (ell - S) + R**2 * Q, U, V)
        top = sum(coef * U**i * V**j for (i, j), coef in eliminant.terms() if i + j == 4)
        self.assertZero(top - 2 * ntt * U**2 * V**2 - 4 * ntr * U * V**3 - 2 * nrr * V**4)
        c4, c3, c2, c1, c0, xv = s.symbols("c4 c3 c2 c1 c0 xv")
        even, odd = c4 * V**2 + c2 * V + c0, c3 * V + c1
        graph = (U - even)**2 - V * odd**2
        parametrization = {U: c4 * xv**4 + c3 * xv**3 + c2 * xv**2 + c1 * xv + c0, V: xv**2}
        self.assertZero(put(graph, parametrization))
        graph_poly = s.Poly(graph, U, V)
        self.assertZero(sum(coef * U**i * V**j for (i, j), coef in graph_poly.terms() if i + j == 4) - c4**2 * V**4)
        # This is a polynomial model for the top-term calculation, not a test
        # of birationality or the universal selected-cofactor argument.

    def test_scalar_jacobian_with_independent_coefficient_jets(self):
        x, rho, lam, D, K, ell, nr, n, gamma = s.symbols("x rho lam D K ell nr n gamma")
        lamr, Dr, Kt, Kr = s.symbols("lamr Dr Kt Kr")
        variables = (x, rho, lam, D, K, ell, nr, n)
        columns = ((0, 0, 0, gamma * lamr, Kt, gamma * lam, 0, gamma),
                   (0, 1, lamr, Dr, Kr, D, 2 * lam**2, nr),
                   (1, 0, 0, 0, 0, 0, 0, 0))
        derivative = lambda expression, column: sum(s.diff(expression, variable) * value for variable, value in zip(variables, columns[column]))
        row = lambda expression: s.Matrix([[derivative(expression, column) for column in range(3)]])
        theta = (x**2 - K) / D
        w = x - lam * theta - nr / 2
        y = (ell - 2 * theta * x + 2 * lam * theta**2) / gamma
        z = 2 * rho * w + theta**2 + n
        dt, dr, dx = s.Matrix([[1, 0, 0]]), s.Matrix([[0, 1, 0]]), s.Matrix([[0, 0, 1]])
        omega = 2 * theta * row(theta) + gamma * dt + 2 * (x - lam * theta) * dr
        identities = (row(w) - dx + lam * row(theta) + (theta * lamr + lam**2) * dr,
                      gamma * row(y) + 2 * theta * row(w) - lam * omega - (D - 2 * lam * x) * dr + 2 * x * row(theta),
                      D * row(theta) - 2 * x * dx + (Kt + gamma * lamr * theta) * dt + (Kr + Dr * theta) * dr,
                      row(z) - 2 * rho * row(w) - omega)
        for identity in identities:
            for entry in identity:
                self.assertZero(entry)
        J = s.cancel(s.Matrix.vstack(row(y), row(z), row(w)).det())
        wedge = s.Matrix.vstack(row(y), omega, row(w)).det()
        self.assertZero(J - wedge)
        cleared = s.Poly(s.cancel(gamma * D**3 * J), x)
        self.assertZero(cleared.coeff_monomial(x**4) - 10 * gamma * D * lamr)
        self.assertZero(cleared.coeff_monomial(x**2).subs(lamr, 0) - 6 * D**2 * Kt)
        self.assertZero(put(cleared.coeff_monomial(x**3), {lamr: 0, Kt: 0}) + 2 * gamma * D * Dr)
        self.assertZero(put(cleared.coeff_monomial(x), {lamr: 0, Kt: 0, Dr: 0}) - 4 * gamma * D**3 * lam + 2 * gamma * D**2 * Kr)
        self.assertZero(put(J, {lamr: 0, Kt: 0, Dr: 0, Kr: 2 * lam * D}) + D)

    def test_full_quartic_normalized_inverse_and_affine_return(self):
        X, Y, Z, W, U, V, Z0, W0, x, t, rho = s.symbols("X Y Z W U V Z0 W0 x t rho")
        lam, delta, gamma, kappa, n1, n2, ell0 = s.symbols("lam delta gamma kappa n1 n2 ell0")
        # gamma, delta and lam are the nonzero complex constants in the proof.
        theta0 = (x**2 - kappa) / delta
        theta = theta0 - 2 * lam * rho
        w = x - lam * theta - lam**2 * rho - n1 / 2
        n = gamma * t + lam**2 * rho**2 + n1 * rho + n2
        ell = gamma * lam * t + delta * rho + ell0
        y = (ell - 2 * theta * x + 2 * lam * theta**2) / gamma
        z = 2 * rho * w + theta**2 + n
        actual = {X: U + lam, Y: y + t * (U + lam),
                  Z: z + 2 * rho * theta * (U + lam) + rho**2 * (U + lam)**2,
                  W: w + theta * (U + lam) + rho * (U + lam)**2}
        affine = {U: X - lam, V: gamma * Y - 2 * lam * Z - ell0 + 2 * lam * n2,
                  Z0: Z - n2, W0: W + n1 / 2}
        back = {X: U + lam, Y: (V + 2 * lam * Z0 + ell0) / gamma, Z: Z0 + n2, W: W0 - n1 / 2}
        for coordinate, expression in affine.items():
            self.assertZero(put(expression, back) - coordinate)
        for coordinate, expression in back.items():
            self.assertZero(put(expression, affine) - coordinate)
        j = theta0 + rho * U
        T = gamma * t - 4 * lam * rho * theta0 + 4 * lam**2 * rho**2
        normalized = {U: U, W0: x + U * j, Z0: T + 2 * rho * x + j**2 - 2 * lam * rho**2 * U,
                      V: delta * rho - 2 * x * theta0 + T * U - 2 * lam * rho**2 * U**2}
        for coordinate in (U, V, Z0, W0):
            self.assertZero(put(affine[coordinate], actual) - normalized[coordinate])
        I = W0**2 + U * V - U**2 * Z0
        J = (I - kappa) / delta
        xhat = W0 - U * J
        rhohat = (V - U * Z0 + 2 * W0 * J - U * J**2) / delta
        That = Z0 - 2 * rhohat * xhat - J**2 + 2 * lam * rhohat**2 * U
        that = (That + 4 * lam * rhohat * (xhat**2 - kappa) / delta - 4 * lam**2 * rhohat**2) / gamma
        self.assertZero(put(J, normalized) - j)
        xback = s.expand(normalized[W0] - U * j)
        rhoback = s.cancel((normalized[V] - U * normalized[Z0] + 2 * normalized[W0] * j - U * j**2) / delta)
        Tback = s.cancel(normalized[Z0] - 2 * rhoback * xback - j**2 + 2 * lam * rhoback**2 * U)
        tback = (Tback + 4 * lam * rhoback * (xback**2 - kappa) / delta - 4 * lam**2 * rhoback**2) / gamma
        for result, expected in ((xback, x), (rhoback, rho), (Tback, T), (tback, t)):
            self.assertZero(result - expected)
        self.assertZero(delta * (J - rhohat * U) - xhat**2 + kappa)
        # The verified identity reconstructs theta0=J-rhohat*U and j=J.
        reverse = {W0: xhat + U * J,
                   Z0: That + 2 * rhohat * xhat + J**2 - 2 * lam * rhohat**2 * U,
                   V: delta * rhohat - 2 * xhat * (J - rhohat * U) + That * U - 2 * lam * rhohat**2 * U**2}
        for coordinate, expression in reverse.items():
            self.assertZero(expression - coordinate)
        self.assertZero(gamma * that - 4 * lam * rhohat * (xhat**2 - kappa) / delta + 4 * lam**2 * rhohat**2 - That)
        ordered_normal = [normalized[coordinate] for coordinate in (U, V, Z0, W0)]
        self.assertZero(s.Matrix(ordered_normal).jacobian((U, x, t, rho)).det() + gamma * delta)
        self.assertZero(s.Matrix([affine[c] for c in (U, V, Z0, W0)]).jacobian((X, Y, Z, W)).det() - gamma)
        self.assertZero(s.Matrix([actual[c] for c in (X, Y, Z, W)]).jacobian((U, x, t, rho)).det() + delta)


if __name__ == "__main__":
    unittest.main()
