"""Standalone finite exact-algebra controls for pass317.

These controls rebuild the literal surface with arbitrary coefficient functions,
then its necessary lower family and both original-map determinants. They do not
prove algebraic-field integration completeness, actual entry, whole-ring return,
factor-unit hypotheses, or an unrestricted recognition/cancellation theorem.

No retained solver or checker is imported. This source is handed off unexecuted;
the parent owns its full preread and sole canonical execution.
"""

import unittest

import sympy as sp


class VariableCouplingLineControls(unittest.TestCase):
    def setUp(self):
        self.t, self.r = sp.symbols("t r", nonzero=True)
        self.U, self.P, self.V = sp.symbols("U P V")
        self.X, self.p, self.eps = sp.symbols("X p eps")
        self.h = sp.Function("h")(self.t)
        self.hp = sp.diff(self.h, self.t)
        self.hpp = sp.diff(self.h, self.t, 2)
        self.disc = 2 * self.h * self.hpp - self.hp**2
        self.m = self.h / self.r
        self.q0, self.q1, self.j0, self.j1, self.c = sp.symbols(
            "q0 q1 j0 j1 c"
        )
        self.q = self.q1 * self.t + self.q0
        self.j = self.j1 * self.t + self.j0

    def reduce(self, expr):
        # h is the full generic complex quadratic, including its degenerations.
        expr = sp.sympify(expr).doit()
        expr = expr.xreplace(
            {sp.diff(self.h, self.t, order): 0 for order in range(3, 9)}
        )
        return sp.cancel(expr)

    def zero(self, expr):
        self.assertEqual(sp.factor(self.reduce(expr)), 0)

    def old_t(self, expr):
        # This is fixed old s, not fixed r=k.
        return self.reduce(
            sp.diff(expr, self.t)
            + self.r * self.hp * sp.diff(expr, self.r) / (2 * self.h)
        )

    def old_s(self, expr):
        return self.reduce(self.h * sp.diff(expr, self.r) / self.r)

    def raw(self, n, ell):
        """Literal Taylor surface, before selecting a surface factor or level."""
        U, P, V, r = self.U, self.P, self.V, self.r
        kt = self.old_t(r)
        ktt = self.old_t(kt)
        kts = self.old_t(self.m)
        kss = self.old_s(self.m)
        f = (
            ktt * P**2 / 2
            + kts * P * V
            + kss * V**2 / 2
            + self.old_t(n) * P
            + self.old_s(n) * V
        )
        g = (ell - (2 * P + kt) * U - f) / self.m
        h3 = (
            self.old_t(ktt) * P**3 / 6
            + self.old_s(ktt) * P**2 * V / 2
            + self.old_t(kss) * P * V**2 / 2
            + self.old_s(kss) * V**3 / 6
        )
        n2 = (
            self.old_t(self.old_t(n)) * P**2 / 2
            + self.old_t(self.old_s(n)) * P * V
            + self.old_s(self.old_s(n)) * V**2 / 2
        )
        surface = self.reduce(
            U**2
            + sp.diff(f, P) * U
            + sp.diff(f, V) * g
            + h3
            + n2
            - self.old_t(ell) * P
            - self.old_s(ell) * V
        )
        a1 = self.reduce(sp.diff(surface, U).subs(U, 0))
        a0 = self.reduce(surface.subs(U, 0))
        return f, self.reduce(g), surface, a1, a0

    def coefficient(self, expr, i, j):
        return sp.Poly(self.reduce(expr), self.P, self.V).coeff_monomial(
            self.P**i * self.V**j
        )

    def homogeneous(self, expr, degree):
        poly = sp.Poly(self.reduce(expr), self.P, self.V)
        return sum(
            coefficient * self.P**i * self.V**j
            for (i, j), coefficient in poly.terms()
            if i + j == degree
        )

    def affine_linear_part(self):
        return (
            self.r * self.disc * self.P / (8 * self.h**2)
            + self.hp * self.V / (4 * self.r)
        )

    def family(self, integration_coefficient=None):
        h, r = self.h, self.r
        n = r**2 * self.hp**2 / (16 * h**2) + h * self.q / r + self.j
        alpha = self.hp**2 * self.disc / (128 * h**4)
        beta = self.hp * self.j1 / (4 * h)
        gamma = self.hp * self.q1 / 4 + self.q * self.hp**2 / (8 * h)
        delta = h**2 * self.q**2 / 2
        e = self.c * h if integration_coefficient is None else integration_coefficient
        ell = -alpha * r**3 - beta * r - gamma + e / r + delta / r**3
        b0 = (
            r**2 * self.hp * self.disc / (32 * h**3)
            + self.j1 / 2
            + self.q * self.hp / (4 * r)
        )
        return n, ell, self.affine_linear_part() + b0

    def actual_coordinates(self, y, sigma, theta, z, w):
        t, r, X, h = self.t, self.r, self.X, self.h
        return (
            y + sigma * X + t * X**2,
            z + (2 * t * sigma + r) * X + t**2 * X**2,
            w + theta * X + r**2 * X**2 / (2 * h),
        )

    def determinant(self, coordinates):
        return self.reduce(
            sp.det(
                sp.Matrix(
                    [
                        [sp.diff(coordinate, variable) for variable in (self.t, self.r, self.p)]
                        for coordinate in coordinates
                    ]
                )
            )
        )

    def test_generic_cubic_and_quadratic_factor_necessity(self):
        t, r, P, V, h = self.t, self.r, self.P, self.V, self.h
        n = sp.Function("n")(t, r)
        ell = sp.Function("ell")(t, r)
        b0 = sp.Symbol("b0")
        _, _, _, a1, a0 = self.raw(n, ell)
        b1 = self.affine_linear_part()
        self.zero(
            self.homogeneous(a1, 2)
            - (-self.hp * P**2 / h + 2 * h * P * V / r**2)
        )
        self.zero(self.homogeneous(a0, 3) - self.homogeneous(a1, 2) * b1)
        residual = a0 - (a1 - b1 - b0) * (b1 + b0)
        vv = h**2 * (r * sp.diff(n, r, 2) + 2 * sp.diff(n, r)) / (2 * r**3)
        vv -= 3 * self.hp**2 / (16 * r**2)
        self.zero(self.coefficient(residual, 0, 2) - vv)
        self.zero(sp.diff(self.coefficient(residual, 1, 1), b0) + 2 * h / r**2)

        f, j = sp.Function("f")(t), sp.Function("j")(t)
        n_partial = r**2 * self.hp**2 / (16 * h**2) + f / r + j
        self.zero(vv.subs(n, n_partial))
        _, _, _, a1, a0 = self.raw(n_partial, ell)
        b0_solution = (
            r**2 * self.hp * self.disc / (32 * h**3)
            + sp.diff(j, t) / 2
            + f * self.hp / (4 * r * h)
        )
        b = b1 + b0_solution
        residual = a0 - (a1 - b) * b
        self.zero(self.coefficient(residual, 0, 2))
        self.zero(self.coefficient(residual, 1, 1))
        self.zero(
            self.coefficient(residual, 2, 0)
            - sp.diff(j, t, 2) / 2
            - h * sp.diff(f / h, t, 2) / (2 * r)
        )
        # Negative control: old fixed-s differentiation is not fixed-r differentiation.
        self.zero(self.old_t(r) - r * self.hp / (2 * h))
        self.assertNotEqual(self.reduce(self.old_t(r) - sp.diff(r, t)), 0)

    def test_linear_necessity_and_complete_factor_orientation(self):
        t, r, h, P, V = self.t, self.r, self.h, self.P, self.V
        n, ell_family, b = self.family()
        ell = sp.Function("ell")(t, r)
        _, _, _, a1, a0 = self.raw(n, ell)
        residual = a0 - (a1 - b) * b
        alpha = self.hp**2 * self.disc / (128 * h**4)
        beta = self.hp * self.j1 / (4 * h)
        gamma = self.hp * self.q1 / 4 + self.q * self.hp**2 / (8 * h)
        delta = h**2 * self.q**2 / 2
        expected_v = -h / r**2 * (
            sp.diff(r * ell, r)
            + 4 * alpha * r**3
            + 2 * beta * r
            + gamma
            + 2 * delta / r**3
        )
        self.zero(self.coefficient(residual, 0, 1) - expected_v)
        e = sp.Function("e")(t)
        _, ell_partial, _ = self.family(e)
        self.zero(expected_v.subs(ell, ell_partial))
        self.zero(
            self.coefficient(residual, 1, 0).subs(ell, ell_partial)
            + h * sp.diff(e / h, t) / r
        )

        _, _, surface, a1, a0 = self.raw(n, ell_family)
        residual = self.reduce(a0 - (a1 - b) * b)
        for monomial, coefficient in sp.Poly(residual, P, V).terms():
            if sum(monomial):
                self.zero(coefficient)
        level = residual.subs({P: 0, V: 0})
        self.zero(surface - level - (self.U + a1 - b) * (self.U + b))

        S, T = sp.symbols("S T")
        substitution = {P: S - r * self.hp / (4 * h), V: T - self.q}
        translated_b = r * self.disc * S / (8 * h**2) + self.hp * T / (4 * r) + self.j1 / 2
        psi = S * (2 * h * T / r**2 - self.hp * S / h) + self.m * self.q1
        self.zero(b.subs(substitution, simultaneous=True) - translated_b)
        self.zero((a1 - 2 * b).subs(substitution, simultaneous=True) - psi)
        for restriction in ({S: 0}, {T: r**2 * self.hp * S / (2 * h**2)}):
            self.zero(psi.subs(restriction) - self.m * self.q1)
        # Without q1 != 0 these branches have zero factor difference, not a unit.
        self.zero(psi.subs({S: 0, self.q1: 0}))
        # Both formal factor orientations are retained; they differ by m*q1.
        self.zero((-b - self.m * self.q1) - (-b) + self.m * self.q1)

    def test_literal_maps_and_both_complete_determinants(self):
        t, r, p, X, h, eps = self.t, self.r, self.p, self.X, self.h, self.eps
        n, ell, b = self.family()
        _, raw_w, _, _, _ = self.raw(n, ell)
        for direction in (0, 1):
            S = sp.Integer(0) if direction == 0 else p
            T = p if direction == 0 else r**2 * self.hp * p / (2 * h**2)
            sigma = S - r * self.hp / (4 * h)
            theta = T - self.q
            y = -b.subs({self.P: sigma, self.V: theta}, simultaneous=True) - eps * self.m * self.q1
            z_raw = 2 * t * y + sigma**2 + self.old_t(r) * sigma + self.m * theta + n
            w_raw = raw_w.subs({self.U: y, self.P: sigma, self.V: theta}, simultaneous=True)
            if direction == 0:
                expected_y = -self.hp * p / (4 * r) - self.j1 / 2 - eps * self.m * self.q1
                expected_z = 2 * t * expected_y + self.m * p + self.j
                expected_w = self.c + h * p**2 / (2 * r**2)
                expected_j = eps * self.q1**2 * h**2 / r**5 * (
                    (2 * eps - 1) * X * r**2 + 2 * eps * p * h
                )
            else:
                expected_y = -r * self.hpp * p / (4 * h) - self.j1 / 2 - eps * self.m * self.q1
                expected_z = 2 * t * expected_y + p**2 + r * self.hp * p / (2 * h) + self.j
                expected_w = self.c + (2 * eps - 1) * p * self.q1 + p**2 * r**2 * self.hpp / (4 * h**2)
                expected_j = eps * self.q1**2 / (2 * r**3) * (
                    -8 * eps * X * p * r * h
                    + (1 - 2 * eps) * X * r**2 * self.hp
                    + (8 * eps**2 - 4 * eps) * self.q1 * h**2
                    + p * r**2 * self.hpp
                )
            self.zero(y - expected_y)
            self.zero(z_raw - expected_z)
            self.zero(w_raw - expected_w)
            coordinates = self.actual_coordinates(
                self.reduce(y), sigma, theta, self.reduce(z_raw), self.reduce(w_raw)
            )
            determinant = self.determinant(coordinates)
            self.zero(determinant - expected_j)
            self.zero(determinant.subs(eps, 0))
            x_coefficient = sp.Poly(self.reduce(determinant.subs(eps, 1)), X).coeff_monomial(X)
            if direction == 0:
                self.zero(x_coefficient - self.q1**2 * h**2 / r**3)
            else:
                self.zero(sp.diff(x_coefficient, p) + 4 * self.q1**2 * h / r**2)
            self.assertNotEqual(self.reduce(x_coefficient), 0)

    def test_constant_h_and_full_parameter_jacobian_boundaries(self):
        t, r, p, X, eps = self.t, self.r, self.p, self.X, self.eps
        h0 = sp.Symbol("h0", nonzero=True)
        # Independently written constant-h maps. Neither direction disappears.
        y = -self.j1 / 2 - eps * h0 * self.q1 / r
        for direction in (0, 1):
            sigma = sp.Integer(0) if direction == 0 else p
            theta = p - self.q if direction == 0 else -self.q
            z = 2 * t * y + (h0 * p / r if direction == 0 else p**2) + self.j
            w = self.c + (h0 * p**2 / (2 * r**2) if direction == 0 else (2 * eps - 1) * p * self.q1)
            coordinates = (
                y + sigma * X + t * X**2,
                z + (2 * t * sigma + r) * X + t**2 * X**2,
                w + theta * X + r**2 * X**2 / (2 * h0),
            )
            determinant = self.determinant(coordinates)
            self.zero(determinant.subs(eps, 0))
            expected_x = (
                self.q1**2 * h0**2 / r**3
                if direction == 0
                else -4 * p * self.q1**2 * h0 / r**2
            )
            actual_x = sp.Poly(self.reduce(determinant.subs(eps, 1)), X).coeff_monomial(X)
            self.zero(actual_x - expected_x)
            self.assertNotEqual(self.reduce(actual_x), 0)
            # A zero q1 erases the obstruction only by violating the factor-unit gate.
            self.zero(determinant.subs(self.q1, 0))

        slope = sp.Function("slope")(t, r)
        intercept = sp.Function("intercept")(t, r)
        inverse_parameters = (t, r**2 / (2 * self.h), (p - intercept) / slope)
        matrix = sp.Matrix(
            [[sp.diff(value, variable) for variable in (t, r, p)] for value in inverse_parameters]
        )
        self.zero(matrix.det() - r / (self.h * slope))
        # The variable affine intercept contributes derivatives but no determinant factor.
        self.assertNotEqual(self.reduce(matrix.det() - r / self.h), 0)


if __name__ == "__main__":
    unittest.main()
