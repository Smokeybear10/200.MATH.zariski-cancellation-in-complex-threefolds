"""Finite exact controls for the actual universal weight-four chart184.

Independent symmetric coefficient jets model commuting partial derivatives.
They do not assert that arbitrary jets realize an actual sliced frame.  Raw
determinants and potential residuals are checked before imposing their prior
relations; in particular no division by the projected polynomial R occurs.
The algebraic square-root example is a coefficient-field boundary, not an
actual four-coordinate inverse.  Its nonzero q_rhorho makes the w^2 term
indispensable.  The two quintics are not asserted irreducible or smooth.

The actual chart, calibrated scalar determinant, full field return, and
normalization claims remain written proofs.  No earlier checker or proof
internal is imported.  Root owns canonical execution after source review.
Authoring entails no execution, import, compilation, or universal certificate.
"""

import unittest

import sympy as sp


def jets(prefix, order):
    return {(i, j): sp.Symbol(f"{prefix}{i}{j}")
            for i in range(order + 1) for j in range(order + 1 - i)}


def directional(coefficients, degree, U, V, dt=0, dr=0):
    return sum(coefficients[i + dt, degree - i + dr] * U**i * V**(degree - i)
               / (sp.factorial(i) * sp.factorial(degree - i))
               for i in range(degree + 1))


class WeightFourChartControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_raw_high_coefficients_and_two_row_reductions(self):
        X, y, theta, w = sp.symbols("X y theta w")
        yt, yr, yv, tt, tr, tv = sp.symbols("yt yr yv theta_t theta_r theta_v")
        zt, zr, zv, wt, wr, wv = sp.symbols("zt zr zv wt wr wv")
        st, sr, sv = sp.symbols("sigma_t sigma_r sigma_v")
        q, k, n = jets("q", 3), jets("k", 2), jets("n", 1)
        raw = sp.Matrix([
            [X + yt, yr, yv],
            [q[1, 0] * X**2 + st * X + zt,
             q[0, 1] * X**2 + sr * X + zr, sv * X + zv],
            [tt * X + wt, X**2 + tr * X + wr, tv * X + wv],
        ])
        raw_det = sp.expand(raw.det())
        self.zero(raw_det.coeff(X, 4) - (q[0, 1] * tv - sv + q[1, 0] * yv))
        self.assertLessEqual(sp.degree(raw_det, X), 4)
        sigma_prior = {
            st: q[2, 0] * y + q[1, 1] * theta + k[1, 0] + q[1, 0] * yt + q[0, 1] * tt,
            sr: q[1, 1] * y + q[0, 2] * theta + k[0, 1] + q[1, 0] * yr + q[0, 1] * tr,
            sv: q[1, 0] * yv + q[0, 1] * tv,
        }
        staged = raw.subs(sigma_prior, simultaneous=True)
        fU = q[2, 0] * y + q[1, 1] * theta + k[1, 0]
        fV = q[1, 1] * y + q[0, 2] * theta + k[0, 1]
        row9 = staged.copy()
        row9[1, :] = staged[1, :] - q[0, 1] * staged[2, :] - q[1, 0] * X * staged[0, :]
        expected_row9 = [zt - q[0, 1] * wt + X * fU,
                         zr - q[0, 1] * wr + X * fV, zv - q[0, 1] * wv]
        for actual, expected in zip(row9[1, :], expected_row9):
            self.zero(actual - expected)
        staged_det = sp.expand(staged.det())
        self.zero(staged_det.coeff(X, 4))
        self.zero(staged_det.coeff(X, 3) - (-zv + q[0, 1] * wv + fU * yv + fV * tv))
        self.zero(row9.det() - staged_det)

        f_t = directional(q, 2, y, theta, dt=1) + directional(k, 1, y, theta, dt=1) + n[1, 0]
        f_r = directional(q, 2, y, theta, dr=1) + directional(k, 1, y, theta, dr=1) + n[0, 1]
        # Differentiating z-q_r*w=f includes w*d(q_r).  Omitting it is
        # precisely the error the next row identity is designed to detect.
        z_prior = {
            zt: q[0, 1] * wt + q[1, 1] * w + f_t + fU * yt + fV * tt,
            zr: q[0, 1] * wr + q[0, 2] * w + f_r + fU * yr + fV * tr,
            zv: q[0, 1] * wv + fU * yv + fV * tv,
        }
        B1, C1 = f_t + q[1, 1] * w, f_r + q[0, 2] * w
        row12 = row9.subs(z_prior, simultaneous=True)
        row12[1, :] = row12[1, :] - fU * row12[0, :]
        expected_row12 = [fV * tt + B1, fV * (tr + X) + C1, fV * tv]
        for actual, expected in zip(row12[1, :], expected_row12):
            self.zero(actual - expected)
        self.zero(sp.expand(row12.det()).coeff(X, 3))
        self.zero(row12.det() - staged_det.subs(z_prior, simultaneous=True))

    def test_remaining_wedges_and_algebraic_coefficient_term(self):
        X, U, V, w = sp.symbols("X U V w")
        yt, yr, yv, tt, tr, tv, wt, wr, wv = sp.symbols("yt yr yv theta_t theta_r theta_v wt wr wv")
        R, B1, C1, Lt, Lr = sp.symbols("R B1 C1 Lambda_t Lambda_r")
        dy, dtheta, dw = sp.Matrix([[yt, yr, yv]]), sp.Matrix([[tt, tr, tv]]), sp.Matrix([[wt, wr, wv]])
        dt, dr = sp.Matrix([[1, 0, 0]]), sp.Matrix([[0, 1, 0]])
        rows = sp.Matrix.vstack(dy + X * dt,
                                R * (dtheta + X * dr) + B1 * dt + C1 * dr,
                                dw + X * dtheta + X**2 * dr)
        determinant = sp.expand(rows.det())
        self.zero(determinant.coeff(X, 3))
        self.zero(determinant.coeff(X, 2) - (R * wv + B1 * yv + C1 * tv))
        self.zero(determinant.coeff(X, 0)
                  - sp.Matrix.vstack(dy, R * dtheta + B1 * dt + C1 * dr, dw).det())
        prior_error = R * dw + B1 * dy + C1 * dtheta - Lt * dt - Lr * dr
        # Exact X residual before imposing d(Rw+g3)=d ell.  The two
        # determinants vanish when that relation holds; no R inversion.
        expected_linear = -Lt * yv - Lr * tv + C1 * wv
        self.zero(determinant.coeff(X, 1) - expected_linear
                  - sp.Matrix.vstack(dy, dr, prior_error).det()
                  - sp.Matrix.vstack(dt, dtheta, prior_error).det())

        q, k, n = jets("q", 4), jets("k", 3), jets("n", 2)
        ell_t, ell_r = sp.symbols("ell_t ell_r")
        f = directional(q, 2, U, V) + directional(k, 1, U, V) + n[0, 0]
        f_t = directional(q, 2, U, V, dt=1) + directional(k, 1, U, V, dt=1) + n[1, 0]
        f_r = directional(q, 2, U, V, dr=1) + directional(k, 1, U, V, dr=1) + n[0, 1]
        g3 = directional(q, 3, U, V) + directional(k, 2, U, V) + directional(n, 1, U, V)
        g3_t = directional(q, 3, U, V, dt=1) + directional(k, 2, U, V, dt=1) + directional(n, 1, U, V, dt=1)
        g3_r = directional(q, 3, U, V, dr=1) + directional(k, 2, U, V, dr=1) + directional(n, 1, U, V, dr=1)
        g4 = directional(q, 4, U, V) + directional(k, 3, U, V) + directional(n, 2, U, V)
        R = sp.diff(f, V)
        Rt, Rr = sp.diff(f_t, V), sp.diff(f_r, V)
        B1, C1 = f_t + q[1, 1] * w, f_r + q[0, 2] * w
        for actual, expected in ((sp.diff(g3, U), f_t), (sp.diff(g3, V), f_r),
                                 (sp.diff(g4, U), g3_t), (sp.diff(g4, V), g3_r),
                                 (sp.diff(f_r, U), Rt), (sp.diff(f_r, V), Rr)):
            self.zero(actual - expected)
        third = R * w + g3
        self.zero(sp.diff(third, U) * yv + sp.diff(third, V) * tv + sp.diff(third, w) * wv
                  - (B1 * yv + C1 * tv + R * wv))
        Lt, Lr = ell_t - g3_t - Rt * w, ell_r - g3_r - Rr * w
        fourth = q[0, 2] * w**2 / 2 + f_r * w + g4 - ell_t * U - ell_r * V
        fourth_v = sp.diff(fourth, U) * yv + sp.diff(fourth, V) * tv + sp.diff(fourth, w) * wv
        self.zero(fourth_v - (-Lt * yv - Lr * tv + C1 * wv))
        without_square = fourth - q[0, 2] * w**2 / 2
        deleted_v = (sp.diff(without_square, U) * yv + sp.diff(without_square, V) * tv
                     + sp.diff(without_square, w) * wv)
        self.zero(fourth_v - deleted_v - q[0, 2] * w * wv)

        # Algebraic q^2=rho is allowed.  In C(q), the coefficient partial
        # d/drho is (1/(2q))*d/dq, not zero and not a rational-q restriction.
        Q = sp.Symbol("Q", nonzero=True)
        qjets = [Q]
        for _ in range(4):
            qjets.append(sp.diff(qjets[-1], Q) / (2 * Q))
        expected_jets = [Q, 1 / (2 * Q), -1 / (4 * Q**3), 3 / (8 * Q**5), -15 / (16 * Q**7)]
        for actual, expected in zip(qjets, expected_jets):
            self.zero(actual - expected)
        self.zero(sp.diff(Q**2, Q) / (2 * Q) - 1)
        self.zero((fourth_v - deleted_v).subs(q[0, 2], qjets[2]) + w * wv / (4 * Q**3))
        self.assertNotEqual(qjets[2], 0)

    def test_two_literal_quintics_and_elimination_residual(self):
        t, rho, U, V, w, m = sp.symbols("t rho U V w m")
        k, n, ell = [sp.Function(name)(t, rho) for name in ("k", "n", "ell")]

        def H(expression, degree):
            return sum(sp.diff(expression, t, i, rho, degree - i) * U**i * V**(degree - i)
                       / (sp.factorial(i) * sp.factorial(degree - i))
                       for i in range(degree + 1))

        for q, expected_top in ((-t**2 * rho, -U**4 * V), (-t * rho + t**4, -U**5)):
            f = H(q, 2) + H(k, 1) + n
            R, f_r = sp.diff(f, V), sp.diff(f, rho)
            g3, g4 = H(q, 3) + H(k, 2) + H(n, 1), H(q, 4) + H(k, 3) + H(n, 2)
            self.zero(sp.diff(q, rho, 2))
            tail = g4 - sp.diff(ell, t) * U - sp.diff(ell, rho) * V - m
            eliminant = sp.expand(R * tail + f_r * (ell - g3))
            third_residual, fourth_residual = R * w + g3 - ell, f_r * w + tail
            self.zero(eliminant - (R * fourth_residual - f_r * third_residual))
            polynomial = sp.Poly(eliminant, U, V)
            self.assertEqual(polynomial.total_degree(), 5)
            top = sum(coefficient * U**powers[0] * V**powers[1]
                      for powers, coefficient in polynomial.terms() if sum(powers) == 5)
            self.zero(top - expected_top)
            if q == -t**2 * rho:
                self.zero(f - (-rho * U**2 - 2 * t * U * V + H(k, 1) + n))
                self.zero(R - (sp.diff(k, rho) - 2 * t * U))
                self.zero(g3 - (-U**2 * V + H(k, 2) + H(n, 1)))
                self.zero(f_r - (-U**2 + H(sp.diff(k, rho), 1) + sp.diff(n, rho)))
                self.zero(g4 - (H(k, 3) + H(n, 2)))
            else:
                self.zero(f - (6 * t**2 * U**2 - U * V + H(k, 1) + n))
                self.zero(R - (sp.diff(k, rho) - U))
                self.zero(g3 - (4 * t * U**3 + H(k, 2) + H(n, 1)))
                self.zero(f_r - (H(sp.diff(k, rho), 1) + sp.diff(n, rho)))
                self.zero(g4 - (U**4 + H(k, 3) + H(n, 2)))
        # Neither total degree five nor elimination proves that the actual
        # selected prime is the whole quintic or that the plane is embedded.


if __name__ == "__main__":
    unittest.main()
