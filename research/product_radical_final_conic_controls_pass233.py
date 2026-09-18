"""Finite algebra controls for the D=0 product-radical conic proof233.

Standalone, with no imports of retained checkers, solvers or proof files.
Jacobian coefficients are reconstructed from the literal coordinate map.
The possible square-root mode is retained in independent r with t=r^2.
The endpoint uses every symbolic integration constant, not a sample grid.

Exact-field completeness, joint constants, actual chart hypotheses,
the nonvertex theorem and original-coordinate independence remain written
proof inputs. No finite test certifies those theorems or unrestricted
cancellation. The centered parameter is not an ambient coordinate.
Root alone may execute this saved file after its complete source read.
"""

import unittest

import sympy as sp


t, s, r, c = sp.symbols("t s r c", nonzero=True)
X, h = sp.symbols("X h")


def clean(expression):
    return sp.cancel(sp.expand(expression))


def literal_rows(tt, k, kt, n, A, B, C, E, F, G):
    y = A * h**2 + B * h + C
    w = E * h**2 + F * h + G
    z = w / (2 * s) + kt * y - h**2 / (8 * s**3 * tt**3) - sp.diff(k, s) * h / (2 * s * tt**2) + n
    return [y + tt * X,
            z + (s * y - h / (2 * s * tt) + k) * X + s * tt * X**2,
            w + (s**2 * y - h / tt) * X + s**2 * tt * X**2]


def coefficient_reader(rows, parameter):
    """Sparse coefficient extraction of the raw three-by-three determinant."""
    polys = [[sp.Poly(sp.diff(row, variable), X, h).as_dict()
              for variable in (parameter, s, h)] for row in rows]
    permutations = [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                    ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]
    cache = {}

    def coefficient(x_degree, h_degree):
        target = (x_degree, h_degree)
        if target not in cache:
            answer = 0
            for perm, sign in permutations:
                p0, p1, p2 = [polys[a][perm[a]] for a in range(3)]
                for (x0, h0), a0 in p0.items():
                    for (x1, h1), a1 in p1.items():
                        key = (x_degree - x0 - x1, h_degree - h0 - h1)
                        if key in p2:
                            answer += sign * a0 * a1 * p2[key]
            cache[target] = sp.factor(answer)
        return cache[target]
    return coefficient


def integrated_family(tt, b, d, e, gamma, j, n0, root=None, reduced_G=False, G_override=None):
    """Explicit primitives, retaining coefficient functions before later gates."""
    ds = lambda expression, order=1: sp.diff(expression, s, order)
    k = -1 / (8 * c * s * tt) + b * tt + d
    kt = 1 / (8 * c * s * tt**2) + b
    A, E = c / (s**2 * tt), e / tt
    B = 4 * c * ds(d) + 2 * tt * e + 1 / (2 * s**2 * tt)
    F = 4 * s**2 * e * ds(d) + 2 * s**2 * e**2 * tt / c - (s * ds(e) + e) / (2 * c * tt)
    C = 4 * s**2 * e * ds(d) * tt**2 + s**2 * e**2 * tt**3 / c - (s * ds(d, 2) + ds(d)) + 1 / (16 * c * s**2 * tt) + j * tt
    if root is not None:
        F += gamma / root
        C += 2 * gamma * root**3
    N2 = (-s * ds(b, 2) + ds(b) + j) / (8 * c * s) + ds(e) / (8 * c**2) + e / (16 * c**2 * s)
    n = s * e * (e - 4 * c * ds(b)) * tt / (8 * c**2) - N2 / tt + (s * ds(d, 2) + ds(d)) / (8 * c * s * tt**2) - 1 / (128 * c**2 * s**3 * tt**3) + n0
    G = (tt**3 * s**4 * e**3 / c**2 + 4 * tt**2 * s**4 * e**2 * ds(d) / c
         + tt * (s**2 * e * j / c - s**3 * e * ds(e) / (2 * c**2) - s**2 * e**2 / c**2)
         + 2 * s**3 * ds(b, 2) * ds(d) - 2 * s**2 * ds(b) * ds(d) + 2 * s**2 * ds(n0)
         - s**3 * ds(d) * ds(e) / c - s**2 * e * ds(d) / c)
    if reduced_G:
        G += (2 * s**2 * ds(e, 2) + 6 * s * ds(e) + e) / (16 * c**2 * tt)
    else:
        G += (2 * s**3 * ds(d) * ds(d, 2) + 2 * s**2 * ds(d)**2 + s**2 * ds(b, 3) / (4 * c)
              - s * ds(j) / (4 * c) - s**2 * ds(e, 2) / (4 * c**2) - s * ds(e) / (4 * c**2) + e / (16 * c**2)) / tt
        G += (s**2 * ds(d, 3) + 3 * s * ds(d, 2)) / (4 * c * tt**2)
    if root is not None:
        G += gamma * ((-2 * s**2 * ds(b) + 4 * s**2 * e / c) * root**3 + 2 * s**2 * ds(d) * root - 1 / (4 * c * root))
    if G_override is not None:
        G = G_override
    return dict(k=k, kt=kt, n=n, A=A, B=B, C=C, E=E, F=F, G=G)


class ProductRadicalFinalConicControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_D_zero_raw_leading_coefficients(self):
        alpha, b, d, e = [sp.Function(name)(s) for name in ("alpha", "b", "d", "e")]
        E, B, C, F, G, n = [sp.Function(name)(t, s) for name in ("E", "B", "C", "F", "G", "n")]
        A = alpha / t
        k = -1 / (8 * s**3 * alpha * t) + b * t + d
        self.zero(A / (8 * s**3 * t**4) + A**2 * sp.diff(k, t, 2) / 2)
        read = coefficient_reader(literal_rows(t, k, sp.diff(k, t), n, A, B, C, E, F, G), t)
        h5 = -alpha * (t * sp.diff(E, t) + E) * (2 * s**2 * alpha * sp.diff(b, s) - t * E) / (s**2 * t**3)
        self.zero(read(0, 5) - h5)
        X2h2 = 3 * (8 * s**4 * t * alpha**2 * sp.diff(d, s) + 4 * s**2 * t**3 * E * alpha
                       - 2 * s**2 * t * B * alpha + 2 * s * sp.diff(alpha, s) + 5 * alpha) / (8 * s**4 * t**4 * alpha)
        self.zero(read(2, 2) - X2h2)
        forced_E = 2 * s**2 * alpha * sp.diff(b, s) / t
        self.zero(t * sp.diff(forced_E, t) + forced_E)
        solved_B = 4 * s**2 * alpha * sp.diff(d, s) + 2 * t * e + (2 * s * sp.diff(alpha, s) + 5 * alpha) / (2 * s**2 * t * alpha)
        staged = coefficient_reader(literal_rows(t, k, sp.diff(k, t), n, A, solved_B, C, e / t, F, G), t)
        self.zero(staged(2, 2))
        self.zero(staged(1, 4) + 5 * (s * sp.diff(alpha, s) + 2 * alpha) / (8 * s**4 * t**6))
        self.zero(s * sp.diff(c / s**2, s) + 2 * c / s**2)
        k_final = -1 / (8 * c * s * t) + b * t + d
        h_root = -2 * s**2 * t * sp.diff(k_final, s)
        final_B = 4 * c * sp.diff(d, s) + 2 * t * e + 1 / (2 * s**2 * t)
        self.zero(2 * c * h_root / (s**2 * t) + final_B - 2 * t * (e - 2 * c * sp.diff(b, s)))

    def test_raw_F_C_n_equations_and_all_primitive_freedoms(self):
        b, d, e, gamma, j, n0 = [sp.Function(name)(s) for name in ("b", "d", "e", "gamma", "j", "n0")]
        F, C, n, G = [sp.Function(name)(t, s) for name in ("F", "C", "n", "G")]
        k = -1 / (8 * c * s * t) + b * t + d
        B = 4 * c * sp.diff(d, s) + 2 * t * e + 1 / (2 * s**2 * t)
        read = coefficient_reader(literal_rows(t, k, sp.diff(k, t), n, c / (s**2 * t), B, C, e / t, F, G), t)
        K = e - 2 * c * sp.diff(b, s)
        bracket = 8 * c * s**2 * t * e * sp.diff(d, s) - 4 * c * t**2 * sp.diff(F, t) - 2 * c * t * F + 12 * s**2 * t**2 * e**2 + s * sp.diff(e, s) + e
        U = (16 * c**2 * s * t**3 * sp.diff(n, t) + 8 * c * s**2 * t**3 * e * sp.diff(b, s)
             + 2 * c * s * t * sp.diff(b, s, 2) - 4 * c * t**3 * sp.diff(F, t) + 2 * c * t * sp.diff(C, t)
             - 2 * c * t * sp.diff(b, s) - 4 * c * C + 4 * s**2 * t**3 * e**2 + t * e)
        V = (64 * c**2 * s**3 * t**4 * sp.diff(n, t) + 32 * c * s**4 * t**4 * e * sp.diff(b, s)
             - 32 * c * s**4 * t**3 * e * sp.diff(d, s) + 8 * c * s**3 * t**2 * sp.diff(b, s, 2)
             + 8 * c * s**3 * t * sp.diff(d, s, 2) + 16 * c * s**2 * t**3 * F - 8 * c * s**2 * t**2 * sp.diff(b, s)
             - 8 * c * s**2 * t * C + 8 * c * s**2 * t * sp.diff(d, s) - 32 * s**4 * t**4 * e**2 + 4 * s**2 * t**2 * e - 1)
        self.zero(read(0, 4) + K * bracket / (4 * s**4 * t**4))
        self.zero(read(1, 3) - U / (4 * s**4 * t**5))
        self.zero(read(2, 1) - V / (16 * c * s**4 * t**4))

        family = integrated_family(r**2, b, d, e, gamma, j, n0, root=r)
        dt = lambda expression: sp.diff(expression, r) / (2 * r)
        Fp, Cp, np = family["F"], family["C"], family["n"]
        substitution = {F: Fp, sp.diff(F, t): dt(Fp), C: Cp, sp.diff(C, t): dt(Cp), n: np, sp.diff(n, t): dt(np)}
        for raw in (bracket, U, V):
            self.zero(raw.xreplace(substitution).subs(t, r**2))
        self.zero(dt(Cp) - Cp / r**2 - (4 * s**2 * r**2 * e * sp.diff(d, s)
                  + (s * sp.diff(d, s, 2) + sp.diff(d, s)) / r**2 + gamma * r
                  + 2 * s**2 * r**4 * e**2 / c - 1 / (8 * c * s**2 * r**4)))
        self.zero(dt(gamma / r) + gamma / (2 * r**3))
        self.zero(dt(j * r**2) - j)
        self.zero(dt(n0))

    def test_raw_G_solution_and_square_root_residual_gates(self):
        b, d, e, gamma, j, n0 = [sp.Function(name)(s) for name in ("b", "d", "e", "gamma", "j", "n0")]
        unknown_G = sp.Function("G")(r, s)
        family = integrated_family(r**2, b, d, e, gamma, j, n0, root=r, G_override=unknown_G)
        read = coefficient_reader(literal_rows(r**2, **family), r)
        solved_G = integrated_family(r**2, b, d, e, gamma, j, n0, root=r)["G"]
        replace = {unknown_G: solved_G, sp.diff(unknown_G, r): sp.diff(solved_G, r),
                   sp.diff(unknown_G, s): sp.diff(solved_G, s)}
        self.zero(sp.diff(read(2, 0), unknown_G) - 1 / (r * s**2))
        self.zero(read(2, 0).xreplace(replace))
        K = e - 2 * c * sp.diff(b, s)
        D = s * sp.diff(d, s, 3) + 3 * sp.diff(d, s, 2)
        E3 = 3 * s * sp.diff(e, s, 2) + 6 * sp.diff(e, s) - 2 * c * s * sp.diff(b, s, 3)
        I = sp.diff(j, s) - 8 * c * s**2 * sp.diff(d, s) * sp.diff(d, s, 2) - 8 * c * s * sp.diff(d, s)**2 - sp.diff(e, s) / (2 * c)
        expected12 = (-24 * c * s * K * gamma * r**7 - (2 * E3 + 6 * c * I) * r**2 + 10 * c * D) / (8 * c * r**9 * s**3)
        expected03 = (12 * c * s * K**2 * gamma * r**7 - 2 * c * K * sp.diff(gamma, s) * r**3 + K * (E3 + 2 * c * I) * r**2 - 4 * c * K * D) / (4 * c * r**9 * s**3)
        self.zero(read(1, 2).xreplace(replace) - expected12)
        self.zero(read(0, 3).xreplace(replace) - expected03)
        # The two surviving linear equations are independent since c!=0.
        self.zero(sp.Matrix([[2, 6 * c], [1, 2 * c]]).det() + 2 * c)

    def test_next_raw_coefficients_and_exact_b_n0_primitives(self):
        b, n0 = sp.Function("b")(s), sp.Function("n0")(s)
        d0, d1, d2, lam, mu, j0 = sp.symbols("d0 d1 d2 lam mu j0")
        d = d0 + d1 * s + d2 / s
        e = (2 * c * s * sp.diff(b, s) - 4 * c * b + lam * s + mu) / (3 * s)
        j = 4 * c * s**2 * sp.diff(d, s)**2 + e / (2 * c) + j0
        self.zero(s * sp.diff(d, s, 3) + 3 * sp.diff(d, s, 2))
        self.zero(3 * s * sp.diff(e, s, 2) + 6 * sp.diff(e, s) - 2 * c * s * sp.diff(b, s, 3))
        self.zero(sp.diff(j - 4 * c * s**2 * sp.diff(d, s)**2 - e / (2 * c), s))
        family = integrated_family(t, b, d, e, 0, j, n0, reduced_G=True)
        read = coefficient_reader(literal_rows(t, **family), t)
        N = s * sp.diff(b, s, 4) + 4 * sp.diff(b, s, 3) + 24 * c * t * (
            d1 * s**2 * sp.diff(b, s, 3) + 2 * d1 * s * sp.diff(b, s, 2) - 2 * d1 * sp.diff(b, s)
            - d2 * sp.diff(b, s, 3) + s * sp.diff(n0, s, 2) + 2 * sp.diff(n0, s))
        self.zero(read(1, 1) - N / (48 * c * s**2 * t**4))
        self.zero(read(0, 2) + (e - 2 * c * sp.diff(b, s)) * read(1, 1))
        self.zero(sp.diff(s**4 * sp.diff(b, s, 3), s) - s**3 * (s * sp.diff(b, s, 4) + 4 * sp.diff(b, s, 3)))
        b0, b1, b2, b3, n1, n2 = sp.symbols("b0 b1 b2 b3 n1 n2")
        bp = b0 + b1 * s + b2 * s**2 + b3 / s
        np = d1 * b1 * s - d2 * b3 / s**3 + n1 / s + n2
        replace = {b: bp, n0: np}
        replace.update({sp.diff(b, s, i): sp.diff(bp, s, i) for i in range(1, 5)})
        replace.update({sp.diff(n0, s, i): sp.diff(np, s, i) for i in range(1, 3)})
        self.zero(N.xreplace(replace))
        self.zero(sp.diff(s**2 * sp.diff(np, s), s) - 2 * d1 * b1 * s + 6 * d2 * b3 / s**3)

    def test_complete_symbolic_family_matches_centered_original_columns(self):
        b0, b1, b2, b3, d0, d1, d2, e0, e1, j0, n1, n2 = sp.symbols(
            "b0 b1 b2 b3 d0 d1 d2 e0 e1 j0 n1 n2"
        )
        b = b0 + b1 * s + b2 * s**2 + b3 / s
        d = d0 + d1 * s + d2 / s
        e = e0 + e1 / s - 2 * c * b3 / s**2
        j = 4 * c * s**2 * sp.diff(d, s)**2 + e / (2 * c) + j0
        n0 = d1 * b1 * s - d2 * b3 / s**3 + n1 / s + n2
        self.zero(3 * s * e - 2 * c * s * sp.diff(b, s) + 4 * c * b
                  - (3 * e0 + 2 * c * b1) * s - (3 * e1 + 4 * c * b0))
        family = integrated_family(t, b, d, e, 0, j, n0, reduced_G=True)
        Y, Z, W = literal_rows(t, **family)
        upsilon = sp.symbols("upsilon")
        h_center = s * t * upsilon - 2 * s**2 * t * sp.diff(d, s) - s**2 * t**2 * e / c - 1 / (4 * c)
        Y, Z, W = [entry.subs(h, h_center) for entry in (Y, Z, W)]
        Ybar = Y + 2 * d1
        expected_Ybar = t * (X + j0 + c * upsilon**2)
        self.zero(Ybar - expected_Ybar)
        Z1 = Z - (b0 + e1 / (2 * c)) * Ybar - d0 * X + 2 * b0 * d1 + 2 * b2 * d2 - n2
        W1 = W + 2 * b3 * Ybar + 2 * d2 * X - 2 * b1 * d2 - 6 * b3 * d1 + 2 * n1
        mathfrak_a, mathfrak_p = X + e0 / c, X + b1 + e0 / (2 * c)
        calV = s * expected_Ybar - upsilon / 2
        calT = s**2 * expected_Ybar - s * upsilon + 1 / (4 * c * t)
        self.zero(Z1 - mathfrak_p * calV - b2 * calT)
        self.zero(W1 - mathfrak_a * calT - (e1 / c) * calV)
        self.zero(expected_Ybar * calT - calV**2 - (X + j0) / (4 * c))

    def test_undivided_original_relation_is_nonzero(self):
        Y, Z, W, Ybar, Z1, W1, calV, calT = sp.symbols("Y Z W Ybar Z1 W1 calV calT")
        b0, b1, b2, b3, d0, d1, d2, e0, e1, j0, n1, n2 = sp.symbols(
            "b0 b1 b2 b3 d0 d1 d2 e0 e1 j0 n1 n2"
        )
        a, p = X + e0 / c, X + b1 + e0 / (2 * c)
        delta = p * a - b2 * e1 / c
        relation = delta * Ybar * (p * W1 - (e1 / c) * Z1) - (a * Z1 - b2 * W1)**2 - delta**2 * (X + j0) / (4 * c)
        linear_rows = {Z1: p * calV + b2 * calT, W1: a * calT + (e1 / c) * calV}
        self.zero((a * Z1 - b2 * W1).subs(linear_rows, simultaneous=True) - delta * calV)
        self.zero((p * W1 - (e1 / c) * Z1).subs(linear_rows, simultaneous=True) - delta * calT)
        self.zero(relation.subs(linear_rows, simultaneous=True)
                  - delta**2 * (Ybar * calT - calV**2 - (X + j0) / (4 * c)))
        original_rows = {Ybar: Y + 2 * d1,
                         Z1: Z - (b0 + e1 / (2 * c)) * (Y + 2 * d1) - d0 * X + 2 * b0 * d1 + 2 * b2 * d2 - n2,
                         W1: W + 2 * b3 * (Y + 2 * d1) + 2 * d2 * X - 2 * b1 * d2 - 6 * b3 * d1 + 2 * n1}
        original_relation = relation.subs(original_rows, simultaneous=True)
        self.zero(sp.Poly(original_relation, Z).coeff_monomial(Z**2) + a**2)
        self.assertEqual(sp.Poly(original_relation, Z).degree(), 2)
        self.assertEqual(sp.Poly(delta, X).degree(), 2)
        self.assertEqual(sp.Poly(delta, X).LC(), 1)


if __name__ == "__main__":
    unittest.main()
