"""Finite exact-algebra controls for the separate notes228,229 and230.

No retained checker, solver, or proof file is imported. The q derivatives
are rebuilt in the exact quadratic coefficient field q^2=t*rho. Formal
coefficient jets and all six functions in the constant-return map remain
free until a displayed identity explicitly uses a relation.

Original-ring local nilpotence, primitive-gcd invariance, coefficient-ring
membership, the published UFD/nice-field theorems, actual field return and
transcendence are written-proof inputs, not conclusions of these tests.
Neither parameter changes nor individual field factors are asserted to
be original polynomial coordinates. No conic or later source is tested.
Root alone may execute this file after a full saved-source read.
"""

from math import factorial
import unittest

import sympy as sp


t, rho, q = sp.symbols("t rho q", nonzero=True)
U, V, X, y, theta = sp.symbols("U V X y theta")


def field_reduce(expression):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    modulus = q**2 - t * rho
    numerator = sp.rem(numerator, modulus, q)
    denominator = sp.rem(denominator, modulus, q)
    if denominator == 0:
        raise ValueError("Zero denominator in the quadratic coefficient field")
    return sp.cancel(numerator / denominator)


def Dt(expression):
    return field_reduce(sp.diff(expression, t) + q * sp.diff(expression, q) / (2 * t))


def Dr(expression):
    return field_reduce(sp.diff(expression, rho) + q * sp.diff(expression, q) / (2 * rho))


def qjet(i, j):
    result = q
    for _ in range(i):
        result = Dt(result)
    for _ in range(j):
        result = Dr(result)
    return result


def Hj(order):
    return sum(qjet(i, order - i) * U**i * V**(order - i)
               / (factorial(i) * factorial(order - i))
               for i in range(order + 1))


class ProductRadicalLowerDegreeControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def field_zero(self, expression):
        self.assertEqual(field_reduce(expression), 0)

    def test_constant_first_leading_potentials_and_squared_slope(self):
        eta, kr, ktt, ktr, krr, nt, nr = sp.symbols("eta kr ktt ktr krr nt nr")
        H2, H3 = Hj(2), Hj(3)
        R = (sp.diff(H2, V) + kr).subs({U: eta, V: theta}, simultaneous=True)
        S = (H3 + ktt * U**2 / 2 + ktr * U * V + krr * V**2 / 2 + nt * U + nr * V)
        S = S.subs({U: eta, V: theta}, simultaneous=True)
        return_slope = sp.expand(R).coeff(theta)
        cubic_S = sp.expand(S).coeff(theta, 3)
        self.field_zero(return_slope - qjet(0, 2))
        self.field_zero(cubic_S - qjet(0, 3) / 6)
        w_quadratic = -cubic_S / return_slope
        self.field_zero(w_quadratic - 1 / (4 * rho))
        self.field_zero(Dr(q) * w_quadratic + qjet(0, 2) / 2)

        delta, lam, omega, kap, zeta, sigma0 = sp.symbols("delta lam omega kap zeta sigma0")
        capital_y = eta + t * X
        capital_z = kap * theta + zeta + (Dr(q) * theta + sigma0) * X + q * X**2
        capital_w = theta**2 / (4 * rho) + lam * theta + omega + theta * X + rho * X**2
        self.zero(delta * sp.diff(capital_y, theta))
        self.field_zero(delta * sp.diff(capital_z, theta) - delta * (Dr(q) * X + kap))
        self.zero(delta**2 * sp.diff(capital_z, theta, 2))
        self.zero(delta**2 * sp.diff(capital_w, theta, 2) - delta**2 / (2 * rho))
        self.zero(delta**3 * sp.diff(capital_w, theta, 3))

        c0, c1, c2, d = sp.symbols("c0 c1 c2 d")
        self.field_zero((delta**2 * Dr(q)**2 - d * t / 2).subs(delta**2, 2 * d * rho))
        slope_relation = sp.Poly((c1 + c2 * t)**2 - d * t / 2, t)
        F2, F1, F0 = (slope_relation.coeff_monomial(t**j) for j in (2, 1, 0))
        self.zero(F2 - c2**2)
        self.zero(F1 - (2 * c1 * c2 - d / 2))
        self.zero(F0 - c1**2)
        # Algebraic consequence of all coefficients vanishing is d^2=0.
        # The nonzero complex d and the UFD derivation input are not tested.
        self.zero(16 * F0 * F2 - 16 * c1 * c2 * F1 + 4 * F1**2 - d**2)

    def test_zero_return_radial_potentials_and_fixed_formal_partial(self):
        p = rho / t
        c, kt, kr, ktt, ktr, krr, n0, nt, nr, k0, w = sp.symbols(
            "c kt kr ktt ktr krr n0 nt nr k0 w"
        )
        line = {U: y, V: p * y + c}
        H2, H3, H4 = Hj(2), Hj(3), Hj(4)
        self.field_zero(H2.subs(line, simultaneous=True) + q * c**2 / (8 * rho**2))
        self.field_zero(H3.subs(line, simultaneous=True)
                        - q * c**2 * y / (8 * t * rho**2) - q * c**3 / (16 * rho**3))
        self.field_zero(H4.subs(line, simultaneous=True)
                        + q * c**2 * y**2 / (8 * t**2 * rho**2)
                        + q * c**3 * y / (8 * t * rho**3) + 5 * q * c**4 / (128 * rho**4))
        self.field_zero(Dt(p) + p * Dr(p))
        S = H3 + ktt * U**2 / 2 + ktr * U * V + krr * V**2 / 2 + nt * U + nr * V
        S_line = sp.Poly(sp.expand(S.subs(line, simultaneous=True)), y)
        self.field_zero(S_line.coeff_monomial(y**2) - (ktt + 2 * p * ktr + p**2 * krr) / 2)
        self.field_zero(S_line.coeff_monomial(y)
                        - (c * (ktr + p * krr) + nt + p * nr + q * c**2 / (8 * t * rho**2)))
        self.field_zero(S_line.coeff_monomial(1)
                        - (c**2 * krr / 2 + c * nr + q * c**3 / (16 * rho**3)))

        c_actual = 4 * rho**2 * kr / q
        actual_line = {U: y, V: p * y + c_actual}
        R = sp.diff(H2, V) + kr
        self.field_zero(R.subs(actual_line, simultaneous=True))
        # Differentiate with U,V fixed BEFORE substituting the line.
        C1 = (Dr(H2) + ktr * U + krr * V + nr).subs(actual_line, simultaneous=True) + Dr(Dr(q)) * w
        K = kt + p * kr
        Kr = ktr + kr / t + p * krr
        Omega = c_actual * krr + nr + 3 * q * c_actual**2 / (16 * rho**3)
        self.field_zero(C1 + q * w / (4 * rho**2) - Kr * y - Omega)
        f_line = (H2 + kt * U + kr * V + n0).subs(actual_line, simultaneous=True)
        self.field_zero(f_line - K * y - n0 - 2 * rho**2 * kr**2 / q)
        sigma = Dt(q) * y + Dr(q) * (p * y + c_actual) + k0
        self.field_zero(sigma - q * y / t - 2 * rho * kr - k0)

    def test_zero_return_scalar_wedge_and_common_nice_row(self):
        p, C, yt, yr, yv, wt, wr, wv = sp.symbols("p C yt yr yv wt wr wv")
        dy = sp.Matrix([[yt, yr, yv]])
        dw = sp.Matrix([[wt, wr, wv]])
        middle = sp.Matrix([[-p * C, C, 0]])
        J = sp.Matrix.vstack(dy, middle, dw).det()
        self.zero(J - C * ((yt + p * yr) * wv - yv * (wt + p * wr)))

        Kr, Omega, C0 = sp.symbols("Kr Omega C0")
        lam, omega = 4 * rho**2 * Kr / q, 4 * rho**2 * (Omega - C0) / q
        self.field_zero(-q * (lam * y + omega) / (4 * rho**2) + Kr * y + Omega - C0)
        tau, s, kap, zeta, lam, omega, c, sigma0 = sp.symbols("tau s kap zeta lam omega c sigma0")
        capital_y = y + t * X
        capital_z = kap * y + zeta + (s * y + sigma0) * X + q * X**2
        capital_w = lam * y + omega + (s**2 * y + c) * X + rho * X**2
        for expression, expected in ((capital_y, tau), (capital_z, tau * (s * X + kap)),
                                     (capital_w, tau * (s**2 * X + lam))):
            self.zero(tau * sp.diff(expression, y) - expected)
            self.zero(tau**2 * sp.diff(expression, y, 2))

        # Uniform leading-row control: epsilon marks a drop of X-degree.
        # The written proof supplies arbitrary-degree completeness and the
        # transcendence of s; this identity is not a finite-degree search.
        eps, ld, md, nd, lower_l, lower_m, lower_n = sp.symbols(
            "eps ld md nd lower_l lower_m lower_n"
        )
        scaled_row = ((ld + eps * lower_l)
                      + (md + eps * lower_m) * (s + eps * kap)
                      + (nd + eps * lower_n) * (s**2 + eps * lam))
        self.zero(sp.expand(scaled_row).coeff(eps, 0) - (ld + md * s + nd * s**2))
        self.assertEqual(sp.Poly(ld + md * s + nd * s**2, s).all_coeffs(), [nd, md, ld])
        # If s is complex instead, a constant-coefficient fixed row exists.
        s0, kappa0 = sp.symbols("s0 kappa0")
        self.zero((-s0 * X - kappa0) + (s0 * X + kappa0))

    def test_constant_return_field_change_and_full_six_function_jacobian(self):
        old_s = q / t
        radial = lambda expression: Dt(expression) + (rho / t) * Dr(expression)
        Ds = lambda expression: 2 * q * Dr(expression)
        for expression, expected_t, expected_s in ((t, 1, 0), (old_s, 0, 1),
                                                    (rho, rho / t, 2 * q), (q, old_s, t)):
            self.field_zero(radial(expression) - expected_t)
            self.field_zero(Ds(expression) - expected_s)
        s = sp.symbols("s", nonzero=True)
        y0, y1 = sp.Function("y0")(t, s), sp.Function("y1")(t, s)
        parameter_map = sp.Matrix([t, s**2 * t, (y - y0) / y1])
        self.zero(parameter_map.jacobian([t, s, y]).det() - 2 * s * t / y1)

        A, lam, omega, c, k, f0 = [sp.Function(name)(t, s)
                                  for name in ("A", "lam", "omega", "c", "k", "f0")]
        w = A * y**2 + lam * y + omega
        capital_y = y + t * X
        capital_w = w + (s**2 * y + c) * X + s**2 * t * X**2
        capital_z = w / (2 * s) + sp.diff(k, t) * y + f0 + (s * y + c / (2 * s) + k) * X + s * t * X**2
        raw_J = sp.Matrix([capital_y, capital_z, capital_w]).jacobian([t, s, y]).det()
        U0 = capital_z - capital_w / (2 * s)
        T = lambda expression: sp.diff(expression, t) - X * sp.diff(expression, y)
        self.zero(U0 - (sp.diff(k, t) * y + f0 + k * X + s * X * capital_y / 2))
        TU = sp.diff(k, t, 2) * y + sp.diff(f0, t)
        Ws = sp.diff(A, s) * y**2 + sp.diff(lam, s) * y + sp.diff(omega, s) + (2 * s * y + sp.diff(c, s)) * X + 2 * s * t * X**2
        TW = sp.diff(A, t) * y**2 + sp.diff(lam, t) * y + sp.diff(omega, t) + (sp.diff(c, t) - lam - 2 * A * y) * X
        corrected_Us = (-A * y**2 / (2 * s**2)
                        + (sp.diff(k, t, s) - lam / (2 * s**2)) * y
                        + sp.diff(f0, s) - omega / (2 * s**2)
                        + (sp.diff(k, s) - c / (2 * s**2)) * X)
        self.zero(T(U0) - TU)
        self.zero(sp.diff(capital_w, s) - Ws)
        self.zero(T(capital_w) - TW)
        self.zero(sp.diff(U0, s) - capital_w / (2 * s**2) - corrected_Us)
        self.zero(raw_J - TU * Ws + corrected_Us * TW)
        self.zero(sp.Poly(sp.expand(raw_J), X, y).coeff_monomial(X * y**3) + A**2 / s**2)


if __name__ == "__main__":
    unittest.main()
