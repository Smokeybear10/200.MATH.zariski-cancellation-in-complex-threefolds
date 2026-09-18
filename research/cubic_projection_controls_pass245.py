"""Finite exact-algebra controls for the separate proofs 240, 243 and 245.

This file reconstructs polynomial identities, a bounded companion-matrix
trace calculation, and specified parity/conductor fixtures. It does not
prove the universal field, irreducibility, scalar-Jacobian, whole-return,
or actual-frame hypotheses used in those written proofs. In particular,
the final formal (3,6) fixture is not an actual sliced four-ring.

Standalone source: no retained proof, solver, or checker is imported.
Execution is reserved to Root after complete source review.
"""

import unittest

import sympy as sp


def parity_parts(expr, x, u):
    """Return even part and coefficient of x, as polynomials in u=x^2."""
    even = sp.S.Zero
    odd = sp.S.Zero
    for (degree,), coefficient in sp.Poly(sp.expand(expr), x).terms():
        if degree % 2:
            odd += coefficient * u ** ((degree - 1) // 2)
        else:
            even += coefficient * u ** (degree // 2)
    return sp.expand(even), sp.expand(odd)


def order_at(expr, x, point):
    shifted = sp.Poly(sp.expand(expr.subs(x, x + point)), x)
    return min(degree for (degree,), coefficient in shifted.terms()
               if coefficient != 0)


class CubicProjectionControls(unittest.TestCase):
    def assert_zero(self, expr):
        numerator, _ = sp.cancel(expr).as_numer_denom()
        self.assertEqual(sp.expand(numerator), 0)

    def test_companion_trace_and_nonzero_linear_coefficient(self):
        U = sp.symbols("U")
        a = sp.symbols("a", nonzero=True)
        b, c, d, gamma = sp.symbols("b c d gamma")
        # Direct multiplication by v modulo a*v^3+b*v^2+c*v+d-U.
        companion = sp.Matrix([
            [0, 0, (U - d) / a],
            [1, 0, -c / a],
            [0, 1, -b / a],
        ])
        identity = sp.eye(3)
        annihilator = (
            a * companion**3 + b * companion**2 + c * companion
            + (d - U) * identity
        )
        for entry in annihilator:
            self.assert_zero(entry)

        # Matrix powers are reconstructed, not supplied as Newton sums.
        powers = [identity]
        for _ in range(10):
            powers.append((powers[-1] * companion).applyfunc(sp.expand))
        traces = [sp.expand(matrix.trace()) for matrix in powers]
        self.assert_zero(traces[0] - 3)
        self.assert_zero(traces[1] + b / a)
        self.assert_zero(traces[2] - b**2 / a**2 + 2 * c / a)
        for j in range(3, 11):
            self.assert_zero(
                traces[j] - (U - d) * traces[j - 3] / a
                + b * traces[j - 1] / a + c * traces[j - 2] / a
            )
        for j, trace in enumerate(traces):
            self.assertLessEqual(sp.Poly(trace, U).degree(), j // 3)
        for k in range(4):
            self.assert_zero(
                sp.Poly(traces[3 * k], U).coeff_monomial(U**k)
                - 3 / a**k
            )

        # psi=gamma*y^2+r(v), with all six coefficients of r independent.
        coefficients = sp.symbols("r0:6")
        tr_r = sp.expand(sum(coefficients[j] * traces[j]
                             for j in range(6)))
        tr_r_squared = sp.expand(sum(
            coefficients[i] * coefficients[j] * traces[i + j]
            for i in range(6) for j in range(6)
        ))
        self.assertLessEqual(sp.Poly(tr_r, U).degree(), 1)
        self.assertLessEqual(sp.Poly(tr_r_squared, U).degree(), 3)
        trace_psi = 3 * gamma * U**2 + tr_r
        trace_psi_squared = (
            3 * gamma**2 * U**4 + 2 * gamma * U**2 * tr_r
            + tr_r_squared
        )
        e2 = sp.expand((trace_psi**2 - trace_psi_squared) / 2)
        self.assert_zero(
            e2 - 3 * gamma**2 * U**4 - 2 * gamma * U**2 * tr_r
            - (tr_r**2 - tr_r_squared) / 2
        )
        self.assert_zero(sp.Poly(e2, U).coeff_monomial(U**4)
                         - 3 * gamma**2)
        self.assertEqual(sp.Poly(e2, U).degree(), 4)
        # This bounded j<=10 calculation supports, not replaces, the
        # all-j induction and primitive-generator argument in proof243.

    def test_all_three_center_and_evaluated_gradient_identities(self):
        x, U, V = sp.symbols("x U V")
        a2 = sp.symbols("a2", nonzero=True)
        b2, kappa, s = sp.symbols("b2 kappa s")
        u = (U - b2) / a2
        y = a2 * x**2 + b2
        formal_return = 2 * V + kappa
        center = {V: -kappa / 2}

        def evaluate(expr, return_poly):
            theta = (return_poly - kappa) / 2
            return expr.subs({U: y, V: theta}, simultaneous=True)

        # Pair (2,3): independent linear center factors and affine lift.
        A1, A0, Q1, Q0, lU, lV, l0 = sp.symbols(
            "A1 A0 Q1 Q0 lU lV l0"
        )
        A = A1 * u + A0
        Q = Q1 * u + Q0
        Ax, Qx = A.subs(U, y), Q.subs(U, y)
        R = (x + s) * Ax
        p = (u - s**2) * A * Q
        w_tilde = -(x - s) * Qx
        G = (formal_return - s * A)**2 - u * A**2
        lift = lU * U + lV * V + l0
        cofactor = -(u - s**2) * Q**2 + formal_return * lift
        H = G * cofactor
        bx = -(x - s) * Qx**2 + Ax * evaluate(lift, R)
        self.assert_zero(evaluate(G, R))
        self.assert_zero(R * w_tilde + p.subs(U, y))
        self.assert_zero(G.subs(center) * cofactor.subs(center) - p**2)
        self.assert_zero(evaluate(cofactor, R) - (x + s) * bx)
        self.assert_zero(evaluate(sp.diff(G, V), R) - 4 * x * Ax)
        self.assert_zero(evaluate(sp.diff(H, V), R) - R * 4 * x * bx)
        self.assertEqual(sp.Poly(G, U, V).total_degree(), 3)
        self.assertEqual(sp.Poly(cofactor, U, V).total_degree(), 3)

        # Pair (2,4): the quadratic quotient and its parity norm.
        A4, B4, C4, q1, q0, gamma = sp.symbols(
            "A4 B4 C4 q1 q0 gamma"
        )
        Q = q1 * u + q0
        Qx = Q.subs(U, y)
        norm = (A4 * u + C4)**2 - B4**2 * u
        Wplus = A4 * x**2 + B4 * x + C4
        Wminus = A4 * x**2 - B4 * x + C4
        R = -Wminus * Qx
        p = norm * Q
        G = (formal_return + Q * (A4 * u + C4))**2 \
            - B4**2 * u * Q**2
        cofactor = norm + gamma * formal_return
        H = G * cofactor
        L1 = Wplus - gamma * Qx
        self.assert_zero(R * Wplus + p.subs(U, y))
        self.assert_zero(evaluate(G, R))
        self.assert_zero(G.subs(center) * cofactor.subs(center) - p**2)
        self.assert_zero(evaluate(cofactor, R) - Wminus * L1)
        self.assert_zero(evaluate(sp.diff(G, V), R) - 4 * B4 * x * Qx)
        self.assert_zero(
            evaluate(sp.diff(H, V), R) + R * 4 * B4 * x * L1
        )
        self.assertEqual(sp.Poly(G, U, V).total_degree(), 4)
        self.assertEqual(sp.Poly(cofactor, U, V).total_degree(), 2)

        # Pair (2,5): retain both the nonvertex and vertex parameters.
        h2, h1, h0 = sp.symbols("h2 h1 h0")
        scale = sp.symbols("scale", nonzero=True)
        A = h2 * u**2 + h1 * u + h0
        Ax = A.subs(U, y)
        R = -(x + s) * Ax / scale
        p = (u - s**2) * A
        G = (scale * formal_return + s * A)**2 - u * A**2
        cofactor = -(u - s**2)
        H = G * cofactor
        self.assert_zero(R * scale * (x - s) + p.subs(U, y))
        self.assert_zero(evaluate(G, R))
        self.assert_zero(G.subs(center) * cofactor.subs(center) - p**2)
        self.assert_zero(evaluate(cofactor, R) - (s**2 - x**2))
        self.assert_zero(evaluate(sp.diff(G, V), R)
                         + 4 * scale * x * Ax)
        self.assert_zero(
            evaluate(sp.diff(H, V), R)
            + R * 4 * scale**2 * x * (x - s)
        )
        self.assertEqual(sp.Poly(G, U, V).total_degree(), 5)
        self.assertEqual(sp.Poly(cofactor, U, V).total_degree(), 1)
        # These identities do not assert q1|R or the actual determinant
        # for freely chosen constants. Those are written-proof inputs.

    def test_parity_conductor_and_overlapping_center_fixtures(self):
        x, u = sp.symbols("x u")
        A, Q, s = u + 1, u + 2, sp.Integer(3)
        Ax, Qx = A.subs(u, x**2), Q.subs(u, x**2)
        generator = x * Ax
        R = (x + s) * Ax
        w_tilde = -(x - s) * Qx

        def in_plane(expr):
            _, odd = parity_parts(expr, x, u)
            return sp.rem(odd, A, u) == 0

        self.assertTrue(in_plane(R))
        self.assertTrue(in_plane(x * R))
        conductor_element = Ax * (2 + x + 3 * x**2 + x**3)
        self.assertTrue(in_plane(conductor_element))
        self.assertTrue(in_plane(x * conductor_element))
        self.assertTrue(in_plane(1 + x**2))
        self.assertFalse(in_plane(x))
        # Q-A=1 returns x from the actual module generators in this fixture.
        self.assert_zero(x - (s * Qx - w_tilde - generator))
        self.assertEqual(sp.gcd(A, Q), 1)
        # A shared odd factor is a negative module-return control.
        bad_Q = A * (u + 2)
        self.assertEqual(sp.gcd(A, bad_Q), A)
        self.assertEqual(sp.rem(1, sp.gcd(A, bad_Q), u), 1)

        # The d=3 center divisibility has overlapping roots at +/-1.
        overlap_A, overlap_Q = u - 1, u + 2
        overlap_R = (x + 1) * overlap_A.subs(u, x**2)
        overlap_p = ((u - 1) * overlap_A * overlap_Q).subs(u, x**2)
        self.assertEqual(sp.rem(overlap_p, overlap_R, x), 0)
        self.assertEqual(order_at(overlap_R, x, -1), 2)
        self.assertEqual(order_at(overlap_p, x, -1), 2)
        self.assertEqual(order_at(overlap_p, x, 1), 2)
        # At the coincident vertex, even parity raises order 3 to order 4.
        vertex_R = x**3
        vertex_p = x**4 * (x**2 + 2)
        self.assertEqual(sp.rem(vertex_p, vertex_R, x), 0)
        self.assertEqual(order_at(vertex_R, x, 0), 3)
        self.assertEqual(order_at(vertex_p, x, 0), 4)
        self.assertEqual(order_at(sp.diff(x**2, x), x, 0), 1)

        # The d=4 norm overlap C=0: both quadratics share a simple zero.
        wplus, wminus = x**2 + x, x**2 - x
        norm = u * (u - 1)
        even_p = (norm * (u + 2)).subs(u, x**2)
        self.assertEqual(sp.gcd(wplus, wminus), x)
        self.assertEqual(order_at(wplus, x, 0), 1)
        self.assertEqual(order_at(wminus, x, 0), 1)
        self.assertEqual(order_at(even_p, x, 0), 2)
        self.assertEqual(sp.rem(even_p, wplus, x), 0)
        self.assertEqual(sp.rem(even_p, wminus, x), 0)
        self.assertEqual(sp.rem(even_p, norm.subs(u, x**2), x), 0)
        # Finite fixtures do not replace the all-root parity/conductor proof.

    def test_formal_three_six_countercontrol_and_missing_center_identity(self):
        x, U, V = sp.symbols("x U V")
        y = x**3
        P = x**4 + x**2
        theta = (x**6 + x**4 + x**2) / 2
        R = 2 * theta
        w_tilde = y - x
        p = -U**3 + U
        self.assert_zero(R * w_tilde + p.subs(U, y))
        self.assert_zero(R * x - y * P - y)
        self.assert_zero(R * x**2 - P**2 + y**2)
        self.assert_zero(x - y + w_tilde)
        self.assert_zero(x**2 - P + y**2 - y * w_tilde)
        self.assert_zero(P**3 - 3 * y**2 * P - y**2 - y**4)
        G0 = -(2 * V - U**2)**3 + 3 * U**2 * (2 * V - U**2) \
            + U**2 + U**4
        self.assert_zero(G0.subs({U: y, V: theta}, simultaneous=True))
        self.assert_zero(G0.subs(V, 0) - p**2)
        self.assertEqual(sp.Poly(G0, U, V).total_degree(), 6)
        top = sum(coefficient * U**i * V**j
                  for (i, j), coefficient in sp.Poly(G0, U, V).terms()
                  if i + j == 6)
        self.assert_zero(top - U**6)
        linear = sp.expand(G0).coeff(V, 1)
        self.assert_zero(linear + 6 * U**4 - 6 * U**2)
        self.assertNotEqual(linear, 0)
        self.assert_zero(sp.expand(-linear / 8).coeff(U, 4)
                         - sp.Rational(3, 4))
        # G0 meets the weaker algebraic return fixtures but explicitly
        # violates [V]H=0. It is not a counterexample to proof243.


if __name__ == "__main__":
    unittest.main()
