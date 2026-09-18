"""Finite exact controls for the actual split-cubic chart175.

Independent coefficient functions verify the determinant integrations and
the exact potential residual before its preceding relation is imposed.
Only the retained157 fixture and its retained158 constant translation
are asserted actual, with both polynomial inverse stages checked.
The zero-R determinant controls are formal contradiction arithmetic.
No finite method proves universal recognition or that two potentials
generate the full evaluation ideal. No old checker is imported or run.
Root must source-review this file before canonical execution.
"""

import unittest

import sympy as sp


def zero(expression):
    assert sp.expand(expression) == 0, sp.expand(expression)


def chart(t, rho, X, y, z, w, sigma, theta):
    return (
        y + t * X,
        z + sigma * X - t * rho * X**2,
        w + theta * X + rho * X**2,
    )


def jacobian(entries, variables):
    return sp.Matrix([[sp.diff(G, v) for v in variables] for G in entries]).det()


def homogeneous_jet(G, degree, t, rho, U, V):
    return sum(
        sp.diff(G, t, i, rho, degree - i) * U**i * V**(degree - i)
        / (sp.factorial(i) * sp.factorial(degree - i))
        for i in range(degree + 1)
    )


class SplitCubicGenericChartControls(unittest.TestCase):
    def test_literal_top_two_integrations(self):
        t, rho, v, X = sp.symbols("t rho v X")
        y, z, w, sigma, theta = [
            sp.Function(name)(t, rho, v)
            for name in ("y", "z", "w", "sigma", "theta")
        ]
        direct = sp.Poly(sp.expand(jacobian(
            chart(t, rho, X, y, z, w, sigma, theta), (t, rho, v)
        )), X)
        self.assertLessEqual(direct.degree(), 4)
        zero(direct.coeff_monomial(X**4) + sp.diff(sigma, v)
             + t * sp.diff(theta, v) + rho * sp.diff(y, v))

        k = sp.Function("k")(t, rho)
        sigma1 = -t * theta - rho * y + k
        integrated = sp.Poly(sp.expand(jacobian(
            chart(t, rho, X, y, z, w, sigma1, theta), (t, rho, v)
        )), X)
        zero(integrated.coeff_monomial(X**4))
        expected3 = (
            -sp.diff(z, v) - t * sp.diff(w, v)
            + (sp.diff(k, t) - theta) * sp.diff(y, v)
            + (sp.diff(k, rho) - y) * sp.diff(theta, v)
        )
        zero(integrated.coeff_monomial(X**3) - expected3)
        primitive3 = -z - t * w + sp.diff(k, t) * y + sp.diff(k, rho) * theta - y * theta
        zero(expected3 - sp.diff(primitive3, v))

    def test_denominator_free_potentials_and_prior_relation_residual(self):
        t, rho, v, X, U, V = sp.symbols("t rho v X U V")
        y, w, theta = [
            sp.Function(name)(t, rho, v) for name in ("y", "w", "theta")
        ]
        k, n, ell = [sp.Function(name)(t, rho) for name in ("k", "n", "ell")]
        r = sp.diff(k, rho)
        R = r - y
        z = sp.diff(k, t) * y + r * theta - y * theta + n - t * w
        sigma = -t * theta - rho * y + k
        Y, Z, W = chart(t, rho, X, y, z, w, sigma, theta)
        zero(X * Z + Y * W - y * w
             - (sp.diff(k, t) * y + r * theta + n) * X - k * X**2)

        f = homogeneous_jet(k, 2, t, rho, U, V) + homogeneous_jet(n, 1, t, rho, U, V)
        g3 = homogeneous_jet(k, 3, t, rho, U, V) + homogeneous_jet(n, 2, t, rho, U, V)
        zero(sp.diff(g3, U) - sp.diff(f, t))
        zero(sp.diff(g3, V) - sp.diff(f, rho))
        evaluate = lambda G: G.subs({U: y, V: theta}, simultaneous=True)
        A = evaluate(sp.diff(f, V))
        B = evaluate(sp.diff(f, U)) - w
        variables = (t, rho, v)
        dy = sp.Matrix([[sp.diff(y, q) for q in variables]])
        dtheta = sp.Matrix([[sp.diff(theta, q) for q in variables]])
        dw = sp.Matrix([[sp.diff(w, q) for q in variables]])
        dt, drho = sp.Matrix([[1, 0, 0]]), sp.Matrix([[0, 1, 0]])
        dY = dy + X * dt
        middle = R * (dtheta + X * drho) + B * dt + A * drho
        last = dw + X * (dtheta + X * drho)
        literal_rows = sp.Matrix([[sp.diff(G, q) for q in variables] for G in (Y, Z, W)])
        reconstructed_middle = (
            literal_rows[1, :] + t * literal_rows[2, :]
            + (rho * X - sp.diff(k, t) + theta) * literal_rows[0, :]
        )
        for actual, expected in zip(reconstructed_middle, middle):
            zero(actual - expected)
        reduced = sp.Matrix.vstack(dY, middle, last)
        zero(literal_rows.det() - reduced.det())
        coefficients = sp.Poly(sp.expand(reduced.det()), X)
        self.assertLessEqual(coefficients.degree(), 2)

        C = R * w + evaluate(f) - ell
        psi = A * w + evaluate(g3) - sp.diff(ell, t) * y - sp.diff(ell, rho) * theta
        zero(coefficients.coeff_monomial(X**2) - sp.diff(C, v))
        # Exact residual without setting C or any derivative of C to zero.
        # It vanishes under the previously established identity C=0.
        residual = (
            (sp.diff(y, t) + sp.diff(theta, rho)) * sp.diff(C, v)
            - sp.diff(y, v) * sp.diff(C, t)
            - sp.diff(theta, v) * sp.diff(C, rho)
        )
        zero(coefficients.coeff_monomial(X) - sp.diff(psi, v) - residual)
        zero(coefficients.coeff_monomial(1)
             - sp.Matrix.vstack(dy, R * dtheta + B * dt + A * drho, dw).det())

    def test_retained_actual_fixture_and_translated_nonzero_k(self):
        u, a, b, c = sp.symbols("u a b c")
        X, Y, Z, W, Z0, W0 = sp.symbols("X Y Z W Z0 W0")
        forward0 = (u, a + b * u, c - b * u, b + u)
        inverse0 = (X, Y - (W0 - X) * X, W0 - X, Z0 + (W0 - X) * X)
        f0 = dict(zip((X, Y, Z0, W0), forward0))
        i0 = dict(zip((u, a, b, c), inverse0))
        for recovered, original in zip(inverse0, (u, a, b, c)):
            zero(recovered.subs(f0, simultaneous=True) - original)
        for recovered, original in zip(forward0, (X, Y, Z0, W0)):
            zero(recovered.subs(i0, simultaneous=True) - original)

        H0, H = X * Z0 + Y * W0, X * Z + Y * W
        forward1 = (X, Y, Z0 + Y * H0, W0 - X * H0)
        inverse1 = (X, Y, Z - Y * H, W + X * H)
        f1 = dict(zip((X, Y, Z, W), forward1))
        i1 = dict(zip((X, Y, Z0, W0), inverse1))
        for recovered, original in zip(inverse1, (X, Y, Z0, W0)):
            zero(recovered.subs(f1, simultaneous=True) - original)
        for recovered, original in zip(forward1, (X, Y, Z, W)):
            zero(recovered.subs(i1, simultaneous=True) - original)
        actual = [G.subs(f0, simultaneous=True) for G in forward1]
        self.assertEqual([sp.Poly(sp.expand(G), u).degree() for G in actual], [1, 1, 2, 2])
        p = c + a + b**2
        zero(sp.expand(actual[0] * actual[2] + actual[1] * actual[3]) - a * b - u * p)

        # Top selected partial comes from the actual staged inverse.
        b_back = W + X * H - X
        a_back = Y - X * b_back
        c_back = Z - Y * H + X * b_back
        actual_map = dict(zip((X, Y, Z, W), actual))
        for G, expected_top in zip((a_back, b_back, c_back), (-1, 0, 1)):
            pulled = sp.diff(G, Z).subs(actual_map, simultaneous=True)
            zero(sp.Poly(sp.expand(pulled), u).coeff_monomial(u**3) - expected_top)

        t, rho, v, shift = sp.symbols("t rho v shift")
        y, w, theta = -v, t, 1 + t * v
        z = -rho - y - t**2 + t * y**2
        sigma = -t * theta - rho * y
        old_chart = chart(t, rho, X, y, z, w, sigma, theta)
        normalized_source = {u: X, a: -v, b: t, c: -rho + v - t**2}
        for actual_entry, chart_entry in zip(actual[1:], old_chart):
            zero(actual_entry.subs(normalized_source, simultaneous=True) - chart_entry)
        zero(jacobian(old_chart, (t, rho, v)) + 1)
        zero((-y) * w - theta + 1)  # ell=-1
        zero(-w + t)  # psi=m=-t
        shifted_chart = tuple(G.subs(X, X - shift) for G in old_chart)
        y_new = y - shift * t
        theta_new = theta - 2 * shift * rho
        sigma_new = sigma + 2 * shift * t * rho
        k_new = sp.expand(sigma_new + t * theta_new + rho * y_new)
        zero(k_new + shift * t * rho)
        self.assertNotEqual(k_new, 0)
        zero(jacobian(shifted_chart, (t, rho, v)) + 1)
        new_H = X * shifted_chart[1] + shifted_chart[0] * shifted_chart[2]
        zero(sp.Poly(sp.expand(new_H), X).coeff_monomial(X**2) - k_new)

    def test_zero_R_determinant_degree_obstruction(self):
        t, rho, v = sp.symbols("t rho v")
        y, A = sp.Function("y")(t, rho), sp.Function("A")(t, rho)
        w = sp.Function("w")(t, rho, v)
        z = A - t * w
        determinant = jacobian((y, z, w), (t, rho, v))
        expected = sp.diff(w, v) * (
            sp.diff(y, t) * sp.diff(A, rho)
            - sp.diff(y, rho) * sp.diff(A, t) + sp.diff(y, rho) * w
        )
        zero(determinant - expected)
        # Formal arithmetic only: these tuples are not actual split frames.
        # The universal proof uses nonzero y_rho and degree 2*deg(w)-1.
        for degree in (1, 2, 3):
            yy, AA = t + rho, t * rho
            ww = v**degree + t * v**(degree - 1) + rho
            value = jacobian((yy, AA - t * ww, ww), (t, rho, v))
            polynomial = sp.Poly(sp.expand(value), v)
            self.assertEqual(polynomial.degree(), 2 * degree - 1)
            zero(polynomial.LC() - degree)


if __name__ == "__main__":
    unittest.main()
