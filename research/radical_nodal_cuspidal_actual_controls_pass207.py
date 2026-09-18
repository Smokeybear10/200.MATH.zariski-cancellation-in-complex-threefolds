"""Finite exact controls for the uniform actual radical family of pass207.

The parameter mu is symbolic, including its zero specialization. These
identities support the written actual inverse and derivation calculations;
they do not prove the full initial ideal, integral closure, all-degree
conductor theorem, or a recognition statement for arbitrary frames.
No previous checker or proof implementation is imported.
"""

import unittest

import sympy as s


def put(expression, substitutions):
    return expression.subs(substitutions, simultaneous=True)


def family(u, x, t, rho, mu):
    theta = (x**2 - mu) / 2
    j = theta + rho * u
    return (u, 2 * rho - x**3 + mu * x + t * u,
            t + 2 * rho * x + j**2, x + u * j)


def inverse(X, Y, Z, W, mu):
    J = (W**2 + X * Y - X**2 * Z - mu) / 2
    xhat = W - X * J
    rhohat = (Y - X * Z + 2 * W * J - X * J**2) / 2
    that = Z - 2 * rhohat * xhat - J**2
    return (X, xhat, that, rhohat), J


class RadicalActualControls207(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(s.cancel(s.expand(expression)), 0)

    def test_actual_inverse_both_orders_and_replica_invariant(self):
        u, x, t, rho, mu = s.symbols("u x t rho mu")
        X, Y, Z, W, h = s.symbols("X Y Z W h")
        target = (X, Y, Z, W)
        forward = family(u, x, t, rho, mu)
        source_map = dict(zip(target, forward))
        hats, J = inverse(X, Y, Z, W, mu)
        _, xhat, that, rhohat = hats
        theta = (x**2 - mu) / 2
        j = theta + rho * u
        self.assertZero(put(J, source_map) - j)
        # Staging uses the just-verified literal J image, avoiding nested powers.
        Xf, Yf, Zf, Wf = forward
        x_back = s.expand(Wf - Xf * j)
        rho_back = s.expand((Yf - Xf * Zf + 2 * Wf * j - Xf * j**2) / 2)
        t_back = Zf - 2 * rho_back * x_back - j**2
        for actual, expected in zip((Xf, x_back, t_back, rho_back), (u, x, t, rho)):
            self.assertZero(actual - expected)
        self.assertZero((xhat**2 - mu) / 2 + rhohat * X - J)
        # Thus the reconstructed theta is J-rhohat*X and reconstructed j is J.
        reverse = (X, 2 * rhohat - 2 * xhat * (J - rhohat * X) + that * X,
                   that + 2 * rhohat * xhat + J**2, xhat + X * J)
        for actual, expected in zip(reverse, target):
            self.assertZero(actual - expected)

        delta = lambda expression: X * s.diff(expression, W) - 2 * W * s.diff(expression, Y)
        I = W**2 + X * Y - X**2 * Z
        for invariant in (X, Z, I, J):
            self.assertZero(delta(invariant))
        self.assertZero(delta(delta(W)))
        self.assertZero(delta(delta(Y)) + 2 * X)
        self.assertZero(delta(delta(delta(Y))))
        minus = {X: X, Y: Y + 2 * W * h - X * h**2, Z: Z, W: W - X * h}
        plus = {X: X, Y: Y - 2 * W * h - X * h**2, Z: Z, W: W + X * h}
        for coordinate in target:
            self.assertZero(put(minus[coordinate], plus) - coordinate)
            self.assertZero(put(plus[coordinate], minus) - coordinate)
        for transformation in (minus, plus):
            self.assertZero(put(J, transformation) - J)
        # Since J itself is fixed, specializing h=J gives the actual replica.
        self.assertZero(minus[W].subs(h, J) - xhat)
        self.assertZero((minus[Y].subs(h, J) - X * Z) / 2 - rhohat)
        self.assertZero(s.diff(j, u) - rho)  # J is delta-invariant, not E-invariant.

    def test_literal_selected_partial_profile_and_jacobian_calibrations(self):
        u, x, t, rho, mu, v, tau = s.symbols("u x t rho mu v tau")
        X, Y, Z, W = s.symbols("X Y Z W")
        forward = family(u, x, t, rho, mu)
        source_map = dict(zip((X, Y, Z, W), forward))
        hats, J = inverse(X, Y, Z, W, mu)
        _, xhat, that, rhohat = hats
        theta, j = (x**2 - mu) / 2, (x**2 - mu) / 2 + rho * u
        J_Z = s.diff(J, Z)
        x_Z = s.diff(xhat, Z)
        rho_Z = s.diff(rhohat, Z)
        t_Z_chain = 1 - 2 * rho_Z * xhat - 2 * rhohat * x_Z - 2 * J * J_Z
        self.assertZero(s.diff(that, Z) - t_Z_chain)
        actual_x_Z = s.expand(put(x_Z, source_map))
        actual_rho_Z = s.expand(put(rho_Z, source_map))
        # The preceding inverse identities give xhat=x, rhohat=rho and J=j.
        actual_t_Z = s.expand(1 - 2 * actual_rho_Z * x - 2 * rho * actual_x_Z - 2 * j * put(J_Z, source_map))
        self.assertZero(actual_x_Z - u**3 / 2)
        self.assertZero(actual_rho_Z + u / 2 + x * u**2 / 2)
        self.assertZero(actual_t_Z - 1 - x * u - (x**2 + theta) * u**2)
        selected = lambda expression: (actual_x_Z * s.diff(expression, x)
                                      + actual_t_Z * s.diff(expression, t)
                                      + actual_rho_Z * s.diff(expression, rho))
        for coordinate, expected in zip(forward, (0, 0, 1, 0)):
            self.assertZero(selected(coordinate) - expected)
        for column, expected in ((actual_x_Z, s.Rational(1, 2)), (actual_t_Z, 0), (actual_rho_Z, 0)):
            self.assertLessEqual(s.Poly(column, u).degree(), 3)
            self.assertZero(column.coeff(u, 3) - expected)
        N = lambda expression: s.diff(expression, x) / 2
        self.assertZero(N(2 * x) - 1)

        degrees = tuple(s.Poly(expression, u).degree() for expression in forward)
        self.assertEqual(degrees, (1, 1, 2, 2))
        leaders = tuple(s.Poly(expression, u).LC() for expression in forward)
        for actual, expected in zip(leaders, (1, t, rho**2, rho)):
            self.assertZero(actual - expected)
            self.assertNotEqual(actual, 0)
            self.assertZero(N(actual))
        for expression, degree in zip(forward, degrees):
            self.assertZero(s.diff(expression, u, degree + 1))
        initial = tuple(coefficient * tau**degree for coefficient, degree in zip(leaders, degrees))
        self.assertZero(initial[0]**2 * initial[2] - initial[3]**2)
        for rational_expression, expected in ((initial[0], tau), (initial[1] / initial[0], t), (initial[3] / initial[0]**2, rho)):
            self.assertZero(rational_expression - expected)
        # These ratios support, but do not prove, the written full-kernel argument.
        self.assertZero(s.Matrix(forward).jacobian((u, x, t, rho)).det() + 2)
        self.assertZero(s.Matrix(forward[1:]).jacobian((t, rho, x)).det() + 2)
        normalized = [expression.subs(x, v / 2) for expression in forward[1:]]
        self.assertZero(s.Matrix(normalized).jacobian((t, rho, v)).det() + 1)

    def test_projected_inverse_potentials_and_actual_cusp_node_controls(self):
        x, t, rho, mu, U, V, A, B, a, z = s.symbols("x t rho mu U V A B a z")
        theta = (x**2 - mu) / 2
        y, zz, w = 2 * rho - x**3 + mu * x, t + 2 * rho * x + theta**2, x
        py, pz, pw = s.symbols("py pz pw")
        projected_map = {py: y, pz: zz, pw: w}
        rx = pw
        rr = (py + pw**3 - mu * pw) / 2
        rt = pz - 2 * rr * pw - ((pw**2 - mu) / 2)**2
        for expression, expected in ((rx, x), (rr, rho), (rt, t)):
            self.assertZero(put(expression, projected_map) - expected)
        inverse_map = {x: rx, rho: rr, t: rt}
        for expression, expected in ((y, py), (zz, pz), (w, pw)):
            self.assertZero(put(expression, inverse_map) - expected)
        u = s.Symbol("u")
        forward = family(u, x, t, rho, mu)
        sigma = s.expand(forward[2]).coeff(u, 1)
        self.assertZero(sigma - 2 * rho * theta)
        self.assertZero(s.expand(forward[3]).coeff(u, 1) - theta)
        R = 2 * theta
        self.assertZero(zz - 2 * rho * w - theta**2 - t)
        self.assertZero(R * w + y - 2 * rho)
        self.assertZero(w**2 - 2 * theta - mu)
        H = (U - 2 * rho)**2 - 4 * V**2 * (2 * V + mu)
        self.assertZero(put(H, {U: y, V: theta}))
        self.assertZero(H.subs(V, 0) - (U - 2 * rho)**2)
        yrow = s.Matrix([[s.diff(y, variable) for variable in (t, rho, x)]])
        vrow = s.Matrix([[s.diff(theta, variable) for variable in (t, rho, x)]])
        wrow = s.Matrix([[0, 0, 1]])
        self.assertZero(s.Matrix.vstack(yrow, R * vrow + s.Matrix([[1, 2 * x, 0]]), wrow).det() + 2)
        yv, vv = s.diff(y, x) / 2, s.diff(theta, x) / 2
        DU = R * (yv * s.diff(theta, rho) - s.diff(y, rho) * vv) + 2 * x * yv
        DV = R * (s.diff(y, t) * vv - yv * s.diff(theta, t)) - yv
        HU, HV = put(s.diff(H, U), {U: y, V: theta}), put(s.diff(H, V), {U: y, V: theta})
        self.assertZero(DU * HU + DV * HV + R**3)

        plane = {A: x**2, B: x**3 - mu * x}
        self.assertZero(2 * theta + mu - plane[A])
        self.assertZero(2 * rho - y - plane[B])
        cubic = B**2 - A * (A - mu)**2
        self.assertZero(put(cubic, plane))
        self.assertZero(put(H, {U: 2 * rho - B, V: (A - mu) / 2}) - cubic)
        for power in range(6):
            representative = (A - mu) * A**(power // 2) if power % 2 == 0 else B * A**(power // 2)
            self.assertZero((x**2 - mu) * x**power - put(representative, plane))
        self.assertEqual(s.rem(s.Integer(1), z - mu, z), 1)  # finite missing-odd-class control
        self.assertZero(cubic.subs(mu, 0) - (B**2 - A**3))
        self.assertZero(cubic.subs(A, z + mu) - (B**2 - mu * z**2 - z**3))
        for expression, expected in ((y, 2 * rho), (theta, 0)):
            self.assertZero(put(expression, {mu: a**2, x: a}) - expected)
            self.assertZero(put(expression, {mu: a**2, x: -a}) - expected)
        self.assertZero(w.subs(x, a) - w.subs(x, -a) - 2 * a)
        # For nonzero a the node branches are distinct; mu=0 gives the cusp.
        # The original kernel A=C[x,t,rho] is polynomial in both cases.


if __name__ == "__main__":
    unittest.main()
