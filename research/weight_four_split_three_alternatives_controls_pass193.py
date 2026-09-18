"""Finite exact controls for the split nonzero-R reduction in pass193.

These are independent symbolic coefficient identities, not actual split-frame
fixtures. They do not prove primitive-LND descent, a field equality, the
one-point-at-infinity argument, or the exhaustive geometric classification.
The two quadratic alternatives remain unresolved by the referenced note.
No earlier checker or proof/solver implementation is imported.
"""

import unittest

import sympy as sp


class SplitThreeAlternativesControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_general_q_constant_projection_determinant_jets(self):
        # Differentiate independent first-order coefficient polynomials before
        # evaluating their jets. This is not a realization of an actual frame.
        t, y, X, theta = sp.symbols("t y X theta")
        R, Rt, Ry, A, At, Ay = sp.symbols("R Rt Ry A At Ay")
        K, Kt, Ky, rho, rhot, rhoy = sp.symbols(
            "K Kt Ky rho rhot rhoy"
        )
        alpha, alphat, alphay = sp.symbols("alpha alphat alphay")
        beta, betat, betay, g, gt, gy = sp.symbols(
            "beta betat betay g gt gy"
        )
        q, qp, qp_new, c = sp.symbols("q qp qp_new c")
        r_field = R + Rt * t + Ry * y
        a_field = A + At * t + Ay * y
        k_field = K + Kt * t + Ky * y
        rho_field = rho + rhot * t + rhoy * y
        alpha_field = alpha + alphat * t + alphay * y
        beta_field = beta + betat * t + betay * y
        g_field = g + gt * t + gy * y
        outputs = sp.Matrix(
            [
                y + t * X,
                r_field * theta + a_field + k_field * X
                + (q + qp * t) * X**2,
                alpha_field * theta**2 + beta_field * theta + g_field
                + theta * X + rho_field * X**2,
            ]
        )
        rows = outputs.jacobian((t, y, theta)).subs({t: 0, y: 0})
        expected_rows = sp.Matrix(
            [
                [X, 1, 0],
                [Rt * theta + At + Kt * X + qp * X**2,
                 Ry * theta + Ay + Ky * X, R],
                [alphat * theta**2 + betat * theta + gt + rhot * X**2,
                 alphay * theta**2 + betay * theta + gy + rhoy * X**2,
                 2 * alpha * theta + beta + X],
            ]
        )
        self.assertEqual(rows, expected_rows)
        determinant = sp.expand(rows.det())
        wt = alphat * theta**2 + betat * theta + gt
        wy = alphay * theta**2 + betay * theta + gy
        collected = (
            (2 * alpha * theta + beta + X)
            * (-Rt * theta - At + X * (Ry * theta + Ay - Kt)
               + X**2 * (Ky - qp))
            + R * (wt - X * wy + rhot * X**2 - rhoy * X**3)
        )
        self.zero(determinant - collected)
        coefficient = sp.Poly(determinant, X, theta)
        time_zero = coefficient.coeff_monomial(theta**2)
        time_one = coefficient.coeff_monomial(X * theta**2)
        self.zero(time_zero - (R * alphat - 2 * alpha * Rt))
        self.zero(time_one - (2 * alpha * Ry - R * alphay))
        proportional_jets = {
            alpha: c * R**2, alphat: 2 * c * R * Rt,
            alphay: 2 * c * R * Ry,
        }
        self.zero(time_zero.subs(proportional_jets, simultaneous=True))
        self.zero(time_one.subs(proportional_jets, simultaneous=True))
        quotient = alpha_field / r_field**2
        self.zero(sp.diff(quotient, t).subs({t: 0, y: 0}) - time_zero / R**3)
        self.zero(sp.diff(quotient, y).subs({t: 0, y: 0}) + time_one / R**3)
        self.zero(
            determinant.subs(qp, qp_new) - determinant
            + (qp_new - qp) * X**2 * (2 * alpha * theta + beta + X)
        )

    def test_split_affine_multiplier_and_leading_rho_slots(self):
        t, rho = sp.symbols("t rho")
        a, b, c0, c1, c2, c3 = sp.symbols("a b c0 c1 c2 c3")
        q = -t**3 - 1 / t
        multiplier = a + b * t
        cubic = c0 + c1 * t + c2 * t**2 + c3 * t**3
        self.zero(multiplier * q + b * t**4 + a * t**3 + b + a / t)
        cleared = sp.Poly(sp.expand(t * (multiplier * q + cubic)), t)
        self.zero(cleared.coeff_monomial(1) + a)
        self.zero(cleared.coeff_monomial(t**5) + b)
        self.assertEqual(cleared.degree(), 5)
        # In a vanishing polynomial identity these two separate slots force
        # a=b=0. This includes, without division, either vanishing coefficient.
        self.zero(cleared.as_expr().subs({a: 0, b: 0}) - t * cubic)
        self.zero(sp.limit(t * multiplier * q, t, 0) + a)
        self.zero(sp.expand((multiplier * q).subs(a, 0)).coeff(t, 4) + b)

        B00, B10, B11, C00, C10, C11 = sp.symbols(
            "B00 B10 B11 C00 C10 C11"
        )
        B_linear = B10 + B11 * t
        C_linear = C10 + C11 * t
        top_three = B_linear * rho - C_linear * q
        self.zero(sp.diff(top_three, rho) - B_linear)
        # When only the C linear part survives, the same affine-multiplier
        # slots apply. If both are constant, B00 is nonzero in the proof.
        self.zero(top_three.subs({B10: 0, B11: 0}) + C_linear * q)
        top_two = B00 * rho - C00 * q
        self.zero(sp.diff(top_two, rho) - B00)

    def test_literal_eliminant_top_and_vanishing_C4_delta(self):
        U, V, t = sp.symbols("U V t")
        R, R1, R2, d, d1, d2, e = sp.symbols("R R1 R2 d d1 d2 e")
        k2, k3, nt, nr, ntt, ntr, nrr = sp.symbols(
            "k2 k3 nt nr ntt ntr nrr"
        )
        ell, ellt, ellr, m = sp.symbols("ell ellt ellr m")
        S = d * U**3 + k2 * U**2 / 2 + R1 * U * V + nt * U + nr * V
        T = (e * U**4 + k3 * U**3 / 6 + R2 * U**2 * V / 2
             + ntt * U**2 / 2 + ntr * U * V + nrr * V**2 / 2)
        H = sp.expand(R * (T - ellt * U - ellr * V - m)
                      + (R1 * U + nr) * (ell - S))
        polynomial = sp.Poly(H, U, V)
        C4 = e * R - d * R1
        Delta = R * R2 / 2 - R1**2
        C3 = R * k3 / 6 - R1 * k2 / 2 - d * nr
        top_four = sum(coef * U**powers[0] * V**powers[1]
                       for powers, coef in polynomial.terms() if sum(powers) == 4)
        self.zero(top_four - C4 * U**4)
        self.zero(polynomial.coeff_monomial(U**2 * V) - Delta)
        self.zero(polynomial.coeff_monomial(U**3) - C3)
        self.zero(polynomial.coeff_monomial(U * V) - (R * ntr - 2 * R1 * nr))
        self.zero(polynomial.coeff_monomial(V**2) - R * nrr / 2)
        self.assertEqual(polynomial.degree(V), 2)

        logarithmic_slope = d1 / (4 * d)
        slope_derivative = d2 / (4 * d) - d1**2 / (4 * d**2)
        drop = {e: d1 / 4, R1: R * logarithmic_slope,
                R2: R * (logarithmic_slope**2 + slope_derivative)}
        self.zero(C4.subs(drop, simultaneous=True))
        delta_drop = R**2 * (4 * d * d2 - 5 * d1**2) / (32 * d**2)
        self.zero(Delta.subs(drop, simultaneous=True) - delta_drop)
        dropped = sp.Poly(H.subs(drop, simultaneous=True), U, V)
        self.assertLessEqual(dropped.total_degree(), 3)
        top_three = sum(coef * U**powers[0] * V**powers[1]
                        for powers, coef in dropped.terms() if sum(powers) == 3)
        self.zero(top_three - U**2 * (C3.subs(drop, simultaneous=True) * U
                                      + delta_drop * V))
        d_split = t**-4 - 1
        split_jets = {d: d_split, d1: sp.diff(d_split, t),
                      d2: sp.diff(d_split, t, 2)}
        self.zero((4 * d * d2 - 5 * d1**2).subs(split_jets) + 80 / t**6)
        self.zero(delta_drop.subs(split_jets) + 5 * R**2 / (2 * t**6 * d_split**2))
        # The displayed numerator is nonzero in the coefficient field for
        # R!=0. This is not a pointwise assertion at poles or at zeros of d.
        f0, f1, f2 = sp.symbols("f0 f1 f2")
        reciprocal_jets = {R: 1 / f0, R1: -f1 / f0**2,
                           R2: 2 * f1**2 / f0**3 - f2 / f0**2}
        self.zero(Delta.subs(reciprocal_jets, simultaneous=True) + f2 / (2 * f0**3))


if __name__ == "__main__":
    unittest.main()
