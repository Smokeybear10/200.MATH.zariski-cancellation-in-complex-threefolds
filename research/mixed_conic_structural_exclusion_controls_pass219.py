"""Finite exact-algebra controls for the mixed-conic exclusion219.

Standalone: no proof, other checker, or workspace data is imported.
The raw coordinate map is rebuilt from the complete lower formulas218.
The tests enumerate every cubic/quadratic Jacobian contribution, check
the differential identities used in exact-field integration, and check
the finite-constant map's structural factorization and cleared relation.

These controls do not prove the actual chart, scalar calibration, exact
constant-field statements, completeness of algebraic integration, or
polynomial-ring independence. Those remain written-proof gates. Formal
functions here stand for arbitrary jets, not a rational-field ansatz.
Execution is reserved to Root after complete saved-source review.
"""

import unittest

import sympy as sp


h, rho = sp.symbols("h rho", nonzero=True)
X, xi, s = sp.symbols("X xi s")
C = sp.symbols("C", nonzero=True)
g0, g1, g2, kappa = sp.symbols("g0 g1 g2 kappa")
f0, f1, lam, mu, nu, d0, N0, N2 = sp.symbols(
    "f0 f1 lam mu nu d0 N0 N2"
)


def clean(expr):
    return sp.factor(sp.cancel(expr))


def raw_centered_map(F, delta, n0):
    """Return raw and parameter-centered maps from the lower formulas218.

    The original capital X is never substituted or differentiated.
    The substitution for xi is only a change of the localized parameter.
    """
    G = g0 + g1 * h + g2 * h**2
    epsilon = sp.diff(delta, h)
    alpha = rho / C
    b = (sp.diff(G, h) * rho + 2 * h * delta * rho**2) / C
    c0 = delta - sp.diff(F, h, 2) / 3 + sp.diff(G, h) ** 2 / (4 * C) + kappa
    c = (
        2 * h * rho * epsilon
        + sp.diff(G, h, 2) / 2
        + h**2 * delta**2 * rho**3 / C
        + h * delta * sp.diff(G, h) * rho**2 / C
        + c0 * rho
    )
    n = (
        (delta * (h * sp.diff(F, h) - F) - h**2 * delta**2) * rho
        - C * (delta - sp.diff(F, h, 2) / 2 - c0) / rho
        + C * sp.diff(G, h, 2) / (2 * rho**2)
        + n0
    )
    k = C / rho + F * rho + G
    kt = sp.diff(k, h) / rho
    kr = sp.diff(k, rho) - h * sp.diff(k, h) / rho
    d = alpha * delta
    e = b * delta + epsilon
    f = clean(
        rho
        / (2 * h)
        * (
            kr * e
            + (2 * C * b / rho**3 - sp.diff(G, h) / rho**2) * c
            + b * sp.diff(n, rho)
            + sp.diff(n, h) / rho
        )
    )
    theta = alpha * xi**2 + b * xi + c
    w = d * xi**2 + e * xi + f
    y = h * theta + xi
    z = (
        -h**2 * w
        + xi**2 / rho
        + kt * xi
        + sp.diff(k, rho) * theta
        + n
    )
    sigma = h**2 * theta + 2 * h * xi + k
    raw = sp.Matrix(
        [
            y + h * rho * X,
            z + sigma * X + h**2 * rho * X**2,
            w + theta * X + rho * X**2,
        ]
    )
    centered = sp.Matrix(
        [clean(entry.subs(xi, s - b / (2 * alpha))) for entry in raw]
    )
    columns = [
        sp.Matrix([sp.expand(entry).coeff(s, j) for entry in centered])
        for j in range(3)
    ]
    return raw, centered, columns, b / (2 * alpha)


def jacobian_contributions(columns, degree):
    """Convolve all three derivative columns, without a leading-term shortcut."""
    result = []
    for i in range(3):
        for j in range(3):
            for k in (1, 2):
                if i + j + k - 1 == degree:
                    matrix = sp.Matrix.hstack(
                        columns[i].diff(h),
                        columns[j].diff(rho),
                        k * columns[k],
                    )
                    result.append(((i, j, k), clean(matrix.det())))
    return result


class MixedConicStructuralControls(unittest.TestCase):
    def zero(self, expr):
        self.assertEqual(clean(expr), 0)

    def vector_zero(self, vector):
        for entry in vector:
            self.zero(entry)

    def test_unrestricted_cubic_and_quadratic_jacobian_coefficients(self):
        F, delta, n0 = [sp.Function(name)(h) for name in ("F", "delta", "n0")]
        _, centered, columns, shift = raw_centered_map(F, delta, n0)
        self.zero(shift - (g1 + 2 * g2 * h) / 2 - h * delta * rho)
        self.vector_zero(
            centered - sum(
                (columns[j] * s**j for j in range(3)), sp.zeros(3, 1)
            )
        )
        direction = sp.Matrix(
            [h, F + h**2 * (X - delta), X + delta]
        )
        self.vector_zero(columns[2] - rho * direction / C)
        self.vector_zero(columns[1] - direction.diff(h))

        cubic = jacobian_contributions(columns, 3)
        quadratic = jacobian_contributions(columns, 2)
        self.assertEqual(
            [index for index, _ in cubic],
            [(0, 2, 2), (1, 1, 2), (1, 2, 1), (2, 0, 2), (2, 1, 1)],
        )
        self.assertEqual(
            [index for index, _ in quadratic],
            [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 1, 1), (2, 0, 1)],
        )
        J3 = sum(value for _, value in cubic)
        J2 = sum(value for _, value in quadratic)
        M = h * sp.diff(F, h) - F - 2 * h**2 * delta
        self.zero(
            J3
            - M
            * (6 * h * sp.diff(delta, h, 2) - sp.diff(F, h, 3)
               + 6 * sp.diff(delta, h))
            / (6 * C * h)
        )

        # Only the already isolated J3 derivative gate is imposed for J2.
        delta_h = (sp.diff(F, h, 2) - lam) / (6 * h)
        derivative_gate = {
            sp.diff(delta, h, j): sp.diff(delta_h, h, j - 1)
            for j in range(1, 4)
        }
        reduced_J2 = J2.subs(derivative_gate, simultaneous=True).doit()
        radial_constant = (
            -h**2 * sp.diff(F, h, 4)
            + 2 * h * sp.diff(F, h, 3)
            + 2 * lam
            - 2 * sp.diff(F, h, 2)
        )
        radial_linear = (
            3 * g1 * h**2 * sp.diff(F, h, 3)
            - 3 * g1 * h * sp.diff(F, h, 2)
            + 6 * g2 * h**3 * sp.diff(F, h, 3)
            - 6 * h**2 * sp.diff(n0, h, 2)
            + 6 * h * sp.diff(n0, h)
        )
        expected_J2 = -M * (C * radial_constant + rho * radial_linear) / (
            12 * C * h**3 * rho
        )
        self.zero(reduced_J2 - expected_J2)
        # The exact-field proof separates these distinct radial powers.
        self.zero(sp.diff(C * radial_constant + rho * radial_linear, rho)
                  - radial_linear)
        self.zero(sp.diff(radial_linear, rho))

    def test_exact_differential_identities_and_constant_form_substitution(self):
        # These derivative identities support, but do not replace, the
        # written joint-constant argument for algebraic solutions.
        F, delta = [sp.Function(name)(h) for name in ("F", "delta")]
        lambda_expression = sp.diff(F, h, 2) - 6 * h * sp.diff(delta, h)
        self.zero(
            sp.diff(lambda_expression, h)
            - sp.diff(F, h, 3)
            + 6 * sp.diff(delta, h)
            + 6 * h * sp.diff(delta, h, 2)
        )
        g = sp.Function("g")(h)
        euler = h**2 * sp.diff(g, h, 2) - 2 * h * sp.diff(g, h) + 2 * g
        mu_expression = (2 * g - h * sp.diff(g, h)) / h
        nu_expression = (h * sp.diff(g, h) - g) / h**2
        self.zero(sp.diff(mu_expression, h) + euler / h**2)
        self.zero(sp.diff(nu_expression, h) - euler / h**3)
        self.zero(g - h * mu_expression - h**2 * nu_expression)

        finite_F = f0 + f1 * h + lam * h**2 / 2 + mu * h**3 / 6 + nu * h**4 / 12
        finite_delta = d0 + mu * h / 6 + nu * h**2 / 12
        particular_n = (
            g1 * lam * h / 2
            + (g1 * nu / 2 + g2 * mu) * h**3 / 3
            + g2 * nu * h**4 / 4
        )
        finite_n = N0 + N2 * h**2 + particular_n
        self.zero(sp.diff(finite_F, h, 2) - lam - mu * h - nu * h**2)
        self.zero(sp.diff(finite_F, h, 2) - 6 * h * sp.diff(finite_delta, h) - lam)
        self.zero(
            h**2 * sp.diff(finite_F, h, 4)
            - 2 * h * sp.diff(finite_F, h, 3)
            + 2 * sp.diff(finite_F, h, 2) - 2 * lam
        )
        n_rhs = -g1 * lam / 2 + (g1 * nu / 2 + g2 * mu) * h**2 + 2 * g2 * nu * h**3
        self.zero(h * sp.diff(finite_n, h, 2) - sp.diff(finite_n, h) - n_rhs)
        self.zero(
            3 * g1 * h**2 * sp.diff(finite_F, h, 3)
            - 3 * g1 * h * sp.diff(finite_F, h, 2)
            + 6 * g2 * h**3 * sp.diff(finite_F, h, 3)
            - 6 * h**2 * sp.diff(finite_n, h, 2)
            + 6 * h * sp.diff(finite_n, h)
        )
        remainder = sp.Function("remainder")(h)
        N2_expression = sp.diff(remainder, h) / (2 * h)
        N0_expression = remainder - h**2 * N2_expression
        homogeneous = h * sp.diff(remainder, h, 2) - sp.diff(remainder, h)
        self.zero(sp.diff(N2_expression, h) - homogeneous / (2 * h**2))
        self.zero(sp.diff(N0_expression, h) + homogeneous / 2)

    def test_full_structural_factorization_and_nonzero_ambient_relation(self):
        F = f0 + f1 * h + lam * h**2 / 2 + mu * h**3 / 6 + nu * h**4 / 12
        delta = d0 + mu * h / 6 + nu * h**2 / 12
        n0 = (
            N0 + g1 * lam * h / 2 + N2 * h**2
            + (g1 * nu / 2 + g2 * mu) * h**3 / 3
            + g2 * nu * h**4 / 4
        )
        raw, centered, _, shift = raw_centered_map(F, delta, n0)
        T = X + kappa - lam / 3
        A = rho * (s**2 / C + T)
        B = h * A + s
        D = h**2 * A + 2 * h * s + C / rho
        v0 = sp.Matrix([0, f0, X + d0])
        v1 = sp.Matrix([1, f1, mu / 6])
        v2 = sp.Matrix([0, X + lam / 2 - d0, nu / 12])
        offset = sp.Matrix(
            [
                -g1 / 2,
                g0 * X + N0 - g1 * f1 / 2 + g2 * f0,
                g2 * X + N2 - g1 * mu / 4 - g2 * lam / 2,
            ]
        )
        self.vector_zero(centered - offset - v0 * A - v1 * B - v2 * D)
        self.vector_zero(centered.subs(s, xi + shift) - raw)
        self.zero(B**2 - A * D + C * T)
        determinant = sp.Matrix.hstack(v0, v1, v2).det()
        expected_det = (X + d0) * (X + lam / 2 - d0) - f0 * nu / 12
        self.zero(determinant - expected_det)
        self.assertEqual(sp.Poly(determinant, X).LC(), 1)

        # The following hats are actual triangular complex-coefficient
        # shears of independent ambient symbols, unlike A, B, D.
        Y, Z, W, H, ZH, WH = sp.symbols("Y Z W H ZH WH")
        forward = {
            H: Y + g1 / 2,
            ZH: Z - offset[1] - f1 * (Y + g1 / 2),
            WH: W - offset[2] - mu * (Y + g1 / 2) / 6,
        }
        inverse = {
            Y: H - g1 / 2,
            Z: ZH + offset[1] + f1 * H,
            W: WH + offset[2] + mu * H / 6,
        }
        for variable, expr in forward.items():
            self.zero(expr.subs(inverse, simultaneous=True) - variable)
        for variable, expr in inverse.items():
            self.zero(expr.subs(forward, simultaneous=True) - variable)
        p = X - d0 + lam / 2
        q = X + d0
        Delta = f0 * nu / 12 - p * q
        relation = (
            (nu * ZH / 12 - p * WH) * (f0 * WH - q * ZH)
            - Delta**2 * (H**2 + C * T)
        )
        # Uniformly nonzero, even when any of the other constants vanish.
        self.assertEqual(
            sp.Poly(relation, X, H, ZH, WH).coeff_monomial(X**4 * H**2), -1
        )
        self.zero(
            relation.subs(
                {H: B, ZH: f0 * A + p * D, WH: q * A + nu * D / 12},
                simultaneous=True,
            )
        )
        ambient_relation = relation.subs(forward, simultaneous=True)
        self.assertFalse(sp.Poly(ambient_relation, X, Y, Z, W).is_zero)
        # Both shear inverses return the displayed nonzero polynomial.
        self.zero(ambient_relation.subs(inverse, simultaneous=True) - relation)


if __name__ == "__main__":
    unittest.main()
