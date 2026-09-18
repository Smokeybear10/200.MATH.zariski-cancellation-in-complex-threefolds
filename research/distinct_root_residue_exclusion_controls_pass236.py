"""Standalone finite algebra controls for the written pass236 proof.

Source-only authorship. This module does not import any retained proof,
solver, or checker. A canonical run is separately owned and recorded.

These identities do not establish the actual-chart theorem, finite-field
constant statements, polynomial-return arguments, primitive LND division,
the cited UFD/nice-derivation theorems, or the exhaustive reduction235.
In particular a formal quotient below becomes the actual w only when the
written third-potential remainder vanishes.
"""

import functools
import unittest

import sympy as sp


t, rho, q = sp.symbols("t rho q", nonzero=True)
lam, mu = sp.symbols("lam mu")
U, V = sp.symbols("U V")
X, y, theta = sp.symbols("X y theta")
kt, kr, ktt, ktr, krr, nt, nr = sp.symbols(
    "k_t k_r k_tt k_tr k_rr n_t n_r"
)
k, n, ell = sp.symbols("k n ell")
qt = (rho - 4 * mu * t**3) / (2 * q)
qr = t / (2 * q)


def field_normal(expr):
    """Use the quadratic relation, keeping t,q algebraically independent."""
    return sp.cancel(expr.subs(rho, (q**2 + lam + mu * t**4) / t))


def dt(expr):
    """Extended derivative with rho fixed, before relation reduction."""
    return field_normal(sp.diff(expr, t) + qt * sp.diff(expr, q))


def dr(expr):
    """Extended derivative with t fixed, before relation reduction."""
    return field_normal(sp.diff(expr, rho) + qr * sp.diff(expr, q))


@functools.lru_cache(maxsize=None)
def taylor_coefficients():
    """Derive H_1,...,H_4 by repeated coefficient differentiation."""
    result = []
    current = q
    for degree in range(1, 5):
        current = field_normal(
            (U * dt(current) + V * dr(current)) / degree
        )
        result.append(current)
    return tuple(result)


def lower_second():
    return kt * U + kr * V + n


def lower_third():
    return ktt * U**2 / 2 + ktr * U * V + krr * V**2 / 2 + nt * U + nr * V


def evaluate(poly, first, second):
    return sp.cancel(poly.subs({U: first, V: second}, simultaneous=True))


def chart_swap(values):
    """Literal good-slot interchange, leaving actual Z,W unchanged."""
    t0, r0, q0, y0, z0, w0, sig0, th0 = values
    return (
        1 / t0,
        r0 / t0**2,
        q0 / t0**2,
        -y0 / t0,
        z0 - sig0 * y0 / t0 + q0 * y0**2 / t0**2,
        w0 - th0 * y0 / t0 + r0 * y0**2 / t0**2,
        sig0 / t0 - 2 * q0 * y0 / t0**2,
        th0 / t0 - 2 * r0 * y0 / t0**2,
    )


class DistinctRootResidueExclusionControls236(unittest.TestCase):
    def assert_zero(self, expr):
        self.assertEqual(sp.cancel(expr), 0)

    def assert_field_zero(self, expr):
        self.assertEqual(field_normal(expr), 0)

    def test_quadratic_field_derivatives_and_zero_return(self):
        relation = q**2 - t * rho + lam + mu * t**4
        self.assert_field_zero(dt(relation))
        self.assert_field_zero(dr(relation))
        self.assert_field_zero(dt(dr(q)) - dr(dt(q)))
        qtr = (q**2 - lam + 3 * mu * t**4) / (4 * q**3)
        qrr = -t**2 / (4 * q**3)
        qrrr = 3 * t**3 / (8 * q**5)
        for actual, expected in (
            (dt(q), qt),
            (dr(q), qr),
            (dt(dr(q)), qtr),
            (dr(dr(q)), qrr),
            (dr(dr(dr(q))), qrrr),
        ):
            self.assert_field_zero(actual - expected)

        H1, H2, H3, _ = taylor_coefficients()
        p0 = (q**2 - lam + 3 * mu * t**4) / t**2
        self.assert_zero(qtr + qrr * p0)
        for actual, expected in (
            (evaluate(H1, 1, p0), q / t),
            (evaluate(H2, 1, p0), -(lam + 3 * mu * t**4) / (2 * q * t**2)),
            (evaluate(H3, 1, p0), (lam - mu * t**4) / (2 * q * t**3)),
        ):
            self.assert_field_zero(actual - expected)

        intercept = -kr / qrr
        third = evaluate(H3 + lower_third(), y, p0 * y + intercept) - ell
        third_poly = sp.Poly(third, y)
        self.assertEqual(third_poly.degree(), 3)
        self.assert_field_zero(
            third_poly.coeff_monomial(y**3)
            - (lam - mu * t**4) / (2 * q * t**3)
        )
        # The nonzero-residue premise is proved using transcendence of t.
        numerator = sp.Poly(lam - mu * t**4, t)
        self.assertEqual(numerator.coeff_monomial(1), lam)
        self.assertEqual(numerator.coeff_monomial(t**4), -mu)
        # When y,theta are scalar, this retained coefficient makes the
        # fourth potential a genuine quadratic equation in w.
        self.assert_zero(qrr / 2 + t**2 / (8 * q**3))

    def test_single_residue_square_paths_and_actual_nice_row(self):
        alpha = sp.symbols("alpha", nonzero=True)
        epsilon, offset = sp.symbols("epsilon offset")
        tau = sp.symbols("tau", nonzero=True)
        H = taylor_coefficients()
        single = {lam: alpha**2, mu: 0}
        base_rho = (q**2 + alpha**2) / t
        qtr = (q**2 - alpha**2) / (4 * q**3)
        qrr = -t**2 / (4 * q**3)

        for sign in (1, -1):
            with self.subTest(sign=sign):
                slope = (q + sign * sp.I * alpha) / t
                p = slope**2
                squared_path = (t + epsilon) * (base_rho + p * epsilon) - alpha**2
                self.assert_zero(squared_path - (q + slope * epsilon) ** 2)
                self.assert_zero(base_rho - t * slope**2 + 2 * sign * sp.I * alpha * slope)
                for degree, Hj in enumerate(H, start=1):
                    value = evaluate(Hj.subs(single), 1, p)
                    self.assert_zero(value - (slope if degree == 1 else 0))
                r_lead = qtr + qrr * p
                self.assert_zero(r_lead + sign * sp.I * alpha / (2 * q**2))

                projected_theta = p * y + offset
                return_poly = qtr * y + qrr * projected_theta + kr
                third_numerator = ell - evaluate(
                    H[2].subs(single) + lower_third(), y, projected_theta
                )
                self.assertLessEqual(sp.Poly(third_numerator, y).degree(), 2)
                w_fit, remainder = sp.div(third_numerator, return_poly, y)
                self.assertLessEqual(sp.Poly(w_fit, y).degree(), 1)
                self.assert_zero(sp.diff(remainder, y))
                self.assert_zero(third_numerator - return_poly * w_fit - remainder)

                z_fit = sp.cancel(
                    qr * w_fit + evaluate(H[1].subs(single) + lower_second(), y, projected_theta)
                )
                sig_fit = sp.cancel(
                    base_rho * y / (2 * q) + qr * projected_theta + k
                )
                self.assertLessEqual(sp.Poly(z_fit, y).degree(), 1)
                self.assert_zero(sp.diff(sig_fit, y) - slope)
                kappa = sp.diff(z_fit, y)
                lambda1 = sp.diff(w_fit, y)
                columns = (
                    y + t * X,
                    z_fit + sig_fit * X + q * X**2,
                    w_fit + projected_theta * X + base_rho * X**2,
                )
                expected = (
                    tau,
                    tau * (slope * X + kappa),
                    tau * (p * X + lambda1),
                )
                for column, derivative in zip(columns, expected):
                    self.assert_zero(tau * sp.diff(column, y) - derivative)
                    self.assert_zero(tau**2 * sp.diff(column, y, 2))

        # Uniform top-of-X certificate. The tails represent arbitrary
        # strictly lower orders after clearing a common degree.
        T, s, lc, mc, nc, lt, mt, ntail, kap, vel = sp.symbols(
            "T s lc mc nc lt mt ntail kap vel"
        )
        scaled_row = (lc + T * lt) + (s + kap * T) * (mc + T * mt) + (
            s**2 + vel * T
        ) * (nc + T * ntail)
        top = sp.expand(scaled_row).coeff(T, 0)
        self.assertEqual(sp.Poly(top, s).all_coeffs(), [nc, mc, lc])

    def test_constant_first_line_and_uniform_square_obstruction(self):
        delta, speed = sp.symbols("delta speed", nonzero=True)
        y0, lambda1, omega, kappa, zeta = sp.symbols("y0 lambda1 omega kappa zeta")
        _, H2, H3, _ = taylor_coefficients()
        qtr = (q**2 - lam + 3 * mu * t**4) / (4 * q**3)
        qrr = -t**2 / (4 * q**3)
        return_poly = qtr * y0 + qrr * theta + kr
        third_numerator = ell - evaluate(H3 + lower_third(), y0, theta)
        w_fit, remainder = sp.div(third_numerator, return_poly, theta)
        self.assert_zero(sp.diff(remainder, theta))
        self.assert_zero(third_numerator - return_poly * w_fit - remainder)
        self.assertEqual(sp.Poly(w_fit, theta).degree(), 2)
        w2 = t / (4 * q**2)
        self.assert_field_zero(sp.Poly(w_fit, theta).coeff_monomial(theta**2) - w2)
        z_fit = sp.cancel(qr * w_fit + evaluate(H2 + lower_second(), y0, theta))
        self.assertLessEqual(sp.Poly(z_fit, theta).degree(), 1)

        w_generic = w2 * theta**2 + lambda1 * theta + omega
        sigma = field_normal(qt) * y0 + qr * theta + k
        Z = kappa * theta + zeta + sigma * X + q * X**2
        W = w_generic + theta * X + rho * X**2
        DZ = delta * sp.diff(Z, theta)
        D2W = delta**2 * sp.diff(W, theta, 2)
        self.assert_zero(DZ - delta * (qr * X + kappa))
        self.assert_zero(delta**2 * sp.diff(Z, theta, 2))
        self.assert_zero(D2W - delta**2 * t / (2 * q**2))
        self.assert_zero(delta**3 * sp.diff(W, theta, 3))
        self.assert_zero(speed * sp.diff(D2W, X))
        self.assert_zero(sp.diff(DZ, X) - delta * qr)

        d, c1, c2 = sp.symbols("d c1 c2")
        self.assert_zero((2 * d * q**2 / t) * qr**2 - d * t / 2)
        obstruction = sp.Poly((c1 + c2 * t) ** 2 - d * t / 2, t)
        A, B, C = (obstruction.coeff_monomial(t**j) for j in (0, 1, 2))
        self.assertEqual((A, B, C), (c1**2, 2 * c1 * c2 - d / 2, c2**2))
        # These three coefficient equations force d^2=0. The actual
        # theorem separately supplies d != 0 in characteristic zero.
        self.assert_zero(d**2 - 16 * A * C + 2 * B * (4 * c1 * c2 + d))

    def test_actual_good_swap_and_full_chart_both_orders(self):
        Y, Z, W = sp.symbols("Y Z W")
        F = Z**2 - X * Y * W + lam * X**4 + mu * Y**4
        swapped_F = F.subs({X: Y, Y: X, lam: mu, mu: lam}, simultaneous=True)
        self.assert_zero(swapped_F - F)
        original = (X, Y, Z, W)
        for entry in original:
            once = entry.subs({X: Y, Y: X}, simultaneous=True)
            twice = once.subs({X: Y, Y: X}, simultaneous=True)
            self.assert_zero(twice - entry)

        z0, w0, sig0, th0 = sp.symbols("z0 w0 sig0 th0")
        values = (t, rho, q, y, z0, w0, sig0, th0)
        once = chart_swap(values)
        twice = chart_swap(once)
        for actual, expected in zip(twice, values):
            self.assert_zero(actual - expected)
        ts, rs, qs, ys, zs, ws, sigs, ths = once
        newX = y + t * X
        self.assert_zero(ys + ts * newX - X)
        self.assert_zero(zs + sigs * newX + qs * newX**2 - (z0 + sig0 * X + q * X**2))
        self.assert_zero(ws + ths * newX + rs * newX**2 - (w0 + th0 * X + rho * X**2))
        self.assert_zero(
            qs**2 - ts * rs + mu + lam * ts**4
            - (q**2 - t * rho + lam + mu * t**4) / t**4
        )
        # Literal partial_Z is unchanged by this actual good-slot swap.
        self.assertEqual([sp.diff(entry, Z) for entry in (Y, X, Z, W)], [0, 0, 1, 0])


if __name__ == "__main__":
    unittest.main()
