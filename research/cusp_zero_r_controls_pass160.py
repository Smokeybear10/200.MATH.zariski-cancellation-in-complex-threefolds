"""Finite exact controls for the zero-r cusp generic reduction160.

The first two methods use independent coefficient jets, not claimed actual
frames or arbitrary solutions of the constant-Jacobian constraints. The
last method verifies one actual polynomial inverse in both orders.
These tests do not certify universal recognition or integral descent.
"""

import unittest

import sympy as sp


class ZeroRCuspControls(unittest.TestCase):
    def test_reduced_determinant_and_polynomial_primitive(self):
        U, X = sp.symbols("U X")
        s, yt, yr, yv = sp.symbols("s yt yr yv", nonzero=True)
        jets = {
            (j, i, k): sp.Symbol(f"p{j}_{i}_{k}")
            for j in range(4)
            for i in range(3)
            for k in range(3 - i)
        }
        h, ht, hr = sp.symbols("h ht hr")

        def coeff_derivative(expr, axis):
            ans = sp.S.Zero
            for (j, i, k), symbol in jets.items():
                target = (j, i + (axis == 0), k + (axis == 1))
                if target in jets:
                    ans += sp.diff(expr, symbol) * jets[target]
            return sp.expand(ans)

        P = sum(jets[j, 0, 0] * U**j for j in range(4))
        Pt = coeff_derivative(P, 0)
        Pr = coeff_derivative(P, 1)
        Pu = sp.diff(P, U)
        Q = sp.integrate(sp.expand(Pt + Pu * Pr), U)
        R = Q + h
        Ru = sp.diff(R, U)
        Rt = coeff_derivative(R, 0) + ht
        Rr = coeff_derivative(R, 1) + hr
        self.assertEqual(sp.expand(Ru - Pt - Pu * Pr), 0)
        self.assertLessEqual(sp.degree(Q, U), 6)
        self.assertEqual(Q.subs(U, 0), 0)

        # Direct determinant of the reduced differential rows. Partial
        # derivatives of y are independent; no division by yv is used.
        matrix = sp.Matrix([
            [X + yt, yr, yv],
            [-s * Pu, s, 0],
            [
                Rt + Ru * yt + X * (Pt + Pu * yt),
                Rr + Ru * yr + X * (Pr + Pu * yr) + X**2,
                Ru * yv + X * Pu * yv,
            ],
        ])
        determinant = sp.expand(matrix.det())
        expected_constant = sp.expand(-s * (Rt + Pu * Rr) * yv)
        self.assertEqual(sp.expand(determinant - expected_constant), 0)
        self.assertEqual(sp.Poly(determinant, X).degree(), 0)

        # Before imposing the primitive equation, recover its sign from
        # a fresh matrix with unrelated first jets of w.
        wt, wr, wv = sp.symbols("wt wr wv")
        raw = sp.Matrix([
            [X + yt, yr, yv],
            [-s * Pu, s, 0],
            [
                wt + X * (Pt + Pu * yt),
                wr + X * (Pr + Pu * yr) + X**2,
                wv + X * Pu * yv,
            ],
        ])
        raw_det = sp.Poly(sp.expand(raw.det()), X)
        self.assertEqual(
            sp.expand(raw_det.coeff_monomial(X)
                      - s * (wv - (Pt + Pu * Pr) * yv)), 0
        )
        self.assertEqual(raw_det.coeff_monomial(X**2), 0)

    def test_highest_coefficient_constraint(self):
        U = sp.Symbol("U")
        p = sp.symbols("p0:4")
        pt = sp.symbols("pt0:4")
        pr = sp.symbols("pr0:4")
        prr = sp.symbols("prr0:4")
        ptr = sp.symbols("ptr0:4")
        ptt = sp.symbols("ptt0:4")
        h_t, h_r = sp.symbols("h_t h_r")
        P = sum(p[i] * U**i for i in range(4))
        Pt = sum(pt[i] * U**i for i in range(4))
        Pr = sum(pr[i] * U**i for i in range(4))
        Q = sp.integrate(sp.expand(Pt + sp.diff(P, U) * Pr), U)
        Qr = sp.expand(sum(
            sp.diff(Q, p[i]) * pr[i]
            + sp.diff(Q, pt[i]) * ptr[i]
            + sp.diff(Q, pr[i]) * prr[i]
            for i in range(4)
        ))
        Qt = sp.expand(sum(
            sp.diff(Q, p[i]) * pt[i]
            + sp.diff(Q, pt[i]) * ptt[i]
            + sp.diff(Q, pr[i]) * ptr[i]
            for i in range(4)
        ))
        obstruction = sp.Poly(
            sp.expand(Qt + h_t + sp.diff(P, U) * (Qr + h_r)), U
        )
        self.assertEqual(
            sp.expand(sp.Poly(Q, U).coeff_monomial(U**6)
                      - p[3] * pr[3] / 2), 0
        )
        self.assertEqual(
            sp.expand(obstruction.coeff_monomial(U**8)
                      - sp.Rational(3, 2) * p[3]
                      * (pr[3]**2 + p[3] * prr[3])), 0
        )
        # A vanishing top coefficient is a necessary condition only.
        self.assertEqual(
            obstruction.coeff_monomial(U**8).subs({pr[3]: 0, prr[3]: 0}),
            0
        )

    def test_actual_cusp_boundary_both_inverse_orders(self):
        x, t, p, v = sp.symbols("x t p v")
        X, Y, Z, W = sp.symbols("X Y Z W")
        forward = (
            x,
            v + t * x,
            p + 3 * t * v**2 + 3 * t**2 * v * x + t**3 * x**2,
            t - v**3 * x + p * x**2,
        )
        H = X * Z - Y**3
        inv_t = W - X * H
        inv_v = Y - X * inv_t
        inv_p = (
            Z - 3 * inv_t * inv_v**2
            - 3 * inv_t**2 * inv_v * X - inv_t**3 * X**2
        )
        inverse = (X, inv_t, inv_p, inv_v)
        source = (x, t, p, v)
        target = (X, Y, Z, W)
        for value, want in zip(inverse, source):
            self.assertEqual(sp.expand(value.xreplace(dict(zip(target, forward)))
                                       - want), 0)
        for value, want in zip(forward, target):
            self.assertEqual(sp.expand(value.xreplace(dict(zip(source, inverse)))
                                       - want), 0)
        self.assertEqual(tuple(sp.degree(f, x) for f in forward), (1, 1, 2, 2))
        self.assertEqual(tuple(sp.Poly(f, x).LC() for f in forward),
                         (1, t, t**3, p))
        self.assertEqual(
            sp.expand(sp.Matrix(forward[1:]).jacobian((t, p, v)).det()), -1
        )
        self.assertEqual(sp.diff(inv_t, Z), -X**2)
        self.assertEqual(sp.diff(inv_v, Z), X**3)
        self.assertEqual(
            sp.expand((X * Z - Y**3).xreplace(dict(zip(target, forward)))
                      - (p * x - v**3)), 0
        )


if __name__ == "__main__":
    unittest.main()
