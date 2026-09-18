"""Finite exact-algebra controls for the two working pass205 proofs.

These standalone controls check Bezout coordinate identities, actual commuting
pair boundary fixtures, and undivided universal-chart identities at q=rho**2
and q=1/rho.  They do not prove the coprime-dependent/comaximal lemma, the
actual field-return or product-unit gates, general coefficient-field descent,
local nilpotence for arbitrary charts, or either published recognition theorem.
The rational chart fixtures below are symbolic identities, not actual frames.
No earlier proof or checker is imported.  The author has not executed this file.
"""

import unittest

import sympy as sp


class NiceCommutingZeroRControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_bezout_coordinate_inverses_and_nonunit_content(self):
        F, G, p, q, V, T, H, s = sp.symbols("F G p q V T H s")
        defect = p * F + q * G - 1
        H_forward = G * V - F * T
        s_forward = p * V + q * T
        V_inverse = F * s + q * H
        T_inverse = G * s - p * H

        # Both inverse orders retain, rather than assume, the Bezout defect.
        forward_pair = {H: H_forward, s: s_forward}
        inverse_pair = {V: V_inverse, T: T_inverse}
        self.assert_zero(
            V_inverse.subs(forward_pair, simultaneous=True) - V - defect * V
        )
        self.assert_zero(
            T_inverse.subs(forward_pair, simultaneous=True) - T - defect * T
        )
        self.assert_zero(
            H_forward.subs(inverse_pair, simultaneous=True) - H - defect * H
        )
        self.assert_zero(
            s_forward.subs(inverse_pair, simultaneous=True) - s - defect * s
        )

        X, U = sp.symbols("X U")
        fixture = {F: U, G: U**2 + 1, p: -U, q: 1}
        self.assert_zero(defect.subs(fixture))
        h0 = H_forward.subs(fixture)
        s0 = s_forward.subs(fixture)

        def D(expression):
            return U * sp.diff(expression, V) + (U**2 + 1) * sp.diff(expression, T)

        def P(expression):
            return U * D(expression)

        self.assert_zero(D(h0))
        self.assert_zero(D(s0) - 1)
        self.assert_zero(P(U))
        for coordinate in (X, U, V, T):
            self.assert_zero(D(D(coordinate)))
            self.assert_zero(P(P(coordinate)))
            self.assert_zero(sp.diff(P(coordinate), X))
        self.assert_zero(P(V) - U**2)
        self.assert_zero(P(T) - U * (U**2 + 1))
        # Content U is allowed; primitivity is obtained only after division.
        self.assert_zero(sp.gcd(P(V), P(T)) - U)

    def test_actual_pair_component_boundary_and_nonunit_fixture(self):
        u, v, c, w0 = sp.symbols("u v c w0")
        X, Y, Z, W, tau = sp.symbols("X Y Z W tau")
        old = (u, v, c, w0)
        new = (X, Y, Z, W)
        inverse_c = Z - X**2
        inverse_v = Y - X * inverse_c

        for nonunit in (False, True):
            with self.subTest(nonunit_content=nonunit):
                forward_w = w0 + u**2 if nonunit else w0 + u * v + u**2
                forward = (u, v + c * u, c + u**2, forward_w)
                inverse_w = W - X**2 if nonunit else W - X * inverse_v - X**2
                inverse = (X, inverse_v, inverse_c, inverse_w)
                to_old = dict(zip(new, forward))
                to_new = dict(zip(old, inverse))
                for coordinate, expression in zip(old, inverse):
                    self.assert_zero(expression.subs(to_old, simultaneous=True) - coordinate)
                for coordinate, expression in zip(new, forward):
                    self.assert_zero(expression.subs(to_new, simultaneous=True) - coordinate)
                self.assertEqual([sp.degree(expression, u) for expression in forward], [1, 1, 2, 2])

                def E(expression):
                    return sp.diff(expression, u)

                def P(expression):
                    return (c if nonunit else 1) * sp.diff(expression, v)

                components = [P(expression) for expression in forward]
                expected = [0, c, 0, 0] if nonunit else [0, 1, 0, u]
                for expression, component, target in zip(forward, components, expected):
                    self.assert_zero(component - target)
                    self.assert_zero(P(component))
                    self.assert_zero(E(P(expression)) - P(E(expression)))
                self.assert_zero(E(E(forward[0])))
                self.assert_zero(E(E(forward[1])))
                self.assert_zero(E(components[3]) - (0 if nonunit else 1))
                if nonunit:
                    for component in components:
                        self.assert_zero(E(component))
                    self.assert_zero(components[1] - c)

                # Only relation identities are tested, not fullness/height.
                leading = {X: tau, Y: c * tau, Z: tau**2, W: tau**2}
                self.assert_zero((Z - X**2).subs(leading, simultaneous=True))
                self.assert_zero((W - X**2).subs(leading, simultaneous=True))

    def test_t_independent_universal_potentials_and_zero_r_stages(self):
        t, rho, X, y, theta, w = sp.symbols("t rho X y theta w")
        yt, yr, yv = sp.symbols("yt yr yv")
        ht, hr, hv = sp.symbols("thetat thetar thetav")
        wt, wr, wv = sp.symbols("wt wr wv")
        ell_t, ell_r, C0 = sp.symbols("ell_t ell_r C0")
        k = {(i, j): sp.Symbol(f"k_{i}_{j}") for i in range(4) for j in range(4 - i)}
        n = {(i, j): sp.Symbol(f"n_{i}_{j}") for i in range(3) for j in range(3 - i)}
        projected = ((yt, yr, yv), (ht, hr, hv), (wt, wr, wv))

        def coefficient_derivative(expression, axis):
            result = sp.diff(expression, (t, rho)[axis])
            for jets in (k, n):
                for (i, j), symbol in jets.items():
                    next_index = (i + 1, j) if axis == 0 else (i, j + 1)
                    if next_index in jets:
                        result += sp.diff(expression, symbol) * jets[next_index]
            return result

        def total(expression, column):
            result = coefficient_derivative(expression, column) if column < 2 else 0
            for variable, derivatives in zip((y, theta, w), projected):
                result += sp.diff(expression, variable) * derivatives[column]
            return result

        for q_value in (rho**2, 1 / rho):
            with self.subTest(q=q_value):
                q1, q2, q3, q4 = [sp.diff(q_value, rho, order) for order in range(1, 5)]
                self.assertNotEqual(q2, 0)
                f = q2 * theta**2 / 2 + k[1, 0] * y + k[0, 1] * theta + n[0, 0]
                sigma = q1 * theta + k[0, 0]
                z = q1 * w + f
                R = sp.diff(f, theta)
                B = coefficient_derivative(f, 0)
                C = q2 * w + coefficient_derivative(f, 1)
                g3 = (
                    q3 * theta**3 / 6
                    + k[2, 0] * y**2 / 2 + k[1, 1] * y * theta
                    + k[0, 2] * theta**2 / 2 + n[1, 0] * y + n[0, 1] * theta
                )
                g4 = (
                    q4 * theta**4 / 24
                    + k[3, 0] * y**3 / 6 + k[2, 1] * y**2 * theta / 2
                    + k[1, 2] * y * theta**2 / 2 + k[0, 3] * theta**3 / 6
                    + n[2, 0] * y**2 / 2 + n[1, 1] * y * theta
                    + n[0, 2] * theta**2 / 2
                )
                self.assert_zero(sp.diff(g3, y) - coefficient_derivative(f, 0))
                self.assert_zero(sp.diff(g3, theta) - coefficient_derivative(f, 1))
                self.assert_zero(sp.diff(g4, y) - coefficient_derivative(g3, 0))
                self.assert_zero(sp.diff(g4, theta) - coefficient_derivative(g3, 1))

                # Independent literal rows, before imposing either lower potential.
                coordinates = (y + t * X, z + sigma * X + q_value * X**2, w + theta * X + rho * X**2)
                raw = sp.Matrix([[total(entry, column) for column in range(3)] for entry in coordinates])
                determinant = sp.Poly(sp.expand(raw.det()), X)
                for power in (3, 4, 5):
                    self.assert_zero(determinant.nth(power))
                third = R * w + g3
                self.assert_zero(determinant.nth(2) - total(third, 2))
                fourth = q2 * w**2 / 2 + coefficient_derivative(f, 1) * w + g4 - ell_t * y - ell_r * theta

                # Differentiate with ell_t,ell_r fixed, then substitute their
                # total derivatives.  The prior third-potential residual stays.
                fourth_v = total(fourth, 2).subs(
                    {ell_t: total(third, 0), ell_r: total(third, 1)}, simultaneous=True
                )
                self.assert_zero(
                    determinant.nth(1) - fourth_v - (yt + hr) * total(third, 2)
                )
                without_square = fourth - q2 * w**2 / 2
                self.assert_zero(total(fourth, 2) - total(without_square, 2) - q2 * w * wv)
                self.assertNotEqual(sp.cancel(q2 * w * wv), 0)

                # Exact R=0 and B=0 coefficient stages, without dividing R.
                stage = {k[0, 1]: -q2 * theta, k[2, 0]: 0, n[1, 0]: -k[1, 1] * theta}
                self.assert_zero(R.subs(stage, simultaneous=True))
                self.assert_zero(B.subs(stage, simultaneous=True))
                C_stage = C.subs(stage, simultaneous=True)
                self.assert_zero(
                    determinant.nth(0).subs(stage, simultaneous=True)
                    - C_stage * (yt * wv - yv * wt)
                )
                w_affine = (
                    -k[1, 1] * y / q2
                    + (C0 - q3 * theta**2 / 2 - k[0, 2] * theta - n[0, 1]) / q2
                )
                self.assert_zero(C_stage.subs(w, w_affine) - C0)
                z_affine = z.subs(stage, simultaneous=True).subs(w, w_affine)
                self.assert_zero(sp.diff(w_affine, y, 2))
                self.assert_zero(sp.diff(z_affine, y, 2))
                self.assert_zero(sp.diff(fourth, w, 2) - q2)
                if q_value == 1 / rho:
                    self.assertNotEqual(q3, 0)
                    self.assertNotEqual(q4, 0)


if __name__ == "__main__":
    unittest.main()
