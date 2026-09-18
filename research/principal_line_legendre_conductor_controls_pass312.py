"""Standalone exact identity controls for working proofs 310 and 312.

These six tests do not prove constant-field return, normalization, conductor
membership for all elements, or the universal exclusion. Those arguments
are in the written proofs. No earlier checker or solver is imported.
"""

import unittest

import sympy as sp


class LegendreConductorControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_full_original_map_after_legendre_change(self):
        X, t, r, omega, eta, xi = sp.symbols("X t r omega eta xi")
        f, f1, g, g1, g2, e, e1 = sp.symbols("f f1 g g1 g2 e e1")
        s = -2*r*t**2 - f1*t - g1
        n = -r**2*t**2 + (f-r*f1)*t + g-r*g1
        ell = 2*r**3*t**2 + r**2*f1*t + e
        nt_old = 2*r**2*t + f
        sigma = omega + r*t
        y = r*omega + (eta-f)/2
        theta = (eta*xi - (4*r*t+f1)*sigma + 4*r**2*t**2
                 + 2*r*f1*t + e1-r**2*g2)
        z = 2*t*y + sigma**2 + theta + n
        w = ell - 2*sigma*y - nt_old*sigma - r*theta
        Y = y + sigma*X + t*X**2
        Z = z + (2*t*sigma+s)*X + t**2*X**2
        W = w + theta*X + s*X**2
        S = omega+t*X
        T = t+xi
        d = e+r*g-r**2*g1
        c = e1+g-r*g1-r**2*g2
        target_y = (X+r)*S + (eta-f)/2
        target_z = S**2-f1*S-g1*X+c+eta*T
        target_w = (X-r)*Z-(X+r)*S**2-eta*S-g*X+d
        self.assert_zero(Y-target_y)
        self.assert_zero(Z-target_z)
        self.assert_zero(W-target_w)
        self.assert_zero(W-((X-r)*Z+(X+r)*S**2-(2*Y+f)*S-g*X+d))

    def test_exterior_row_without_suppressing_coefficient_derivatives(self):
        X, t, r, S = sp.symbols("X t r S")
        f = sp.Function("f")(r)
        g = sp.Function("g")(r)
        d = sp.Function("d")(r)
        eta = sp.Function("eta")(t, r)
        T = sp.Function("T")(t, r)
        Y = (X+r)*S+(eta-f)/2
        Z = S**2-sp.diff(f, r)*S-sp.diff(g, r)*X+sp.diff(d, r)+eta*T
        W = (X-r)*Z-(X+r)*S**2-eta*S-g*X+d
        for variable, target in ((t, 0), (r, -eta*T), (S, -eta)):
            row = sp.diff(W, variable)-(X-r)*sp.diff(Z, variable)
            row += 2*S*sp.diff(Y, variable)
            self.assert_zero(row-target)

    def test_full_scalar_coefficients_and_constant_sheet(self):
        X, S, omega, t, r = sp.symbols("X S omega t r")
        eta, et, er, T, Tt, Tr = sp.symbols("eta et er T Tt Tr")
        c1, f1, f2, g2 = sp.symbols("c1 f1 f2 g2")
        rows = sp.Matrix([
            [et/2, er/2+S-f1/2, X+r],
            [et*T+eta*Tt, er*T+eta*Tr+c1-f2*S-g2*X, 2*S-f1],
            [0, -eta*T, -eta],
        ])
        determinant = sp.expand(rows.det())
        fixed_omega = sp.Poly(determinant.subs(S, omega+t*X), X, omega)
        self.assertLessEqual(fixed_omega.total_degree(), 1)
        q = 2*T+f2/2
        self.assert_zero(fixed_omega.coeff_monomial(omega)-eta*(et*q+eta*Tt))
        x_coefficient = fixed_omega.coeff_monomial(X)
        x_coefficient = x_coefficient.subs({g2: 2*T**2-2*t*q,
                                          Tt: q/(2*(T-t))})
        self.assert_zero(x_coefficient+eta**2*q/2)
        sheet = {T: -f2/4, Tt: 0, g2: f2**2/8}
        expected = -eta*et*(eta*Tr+c1+2*T*f1+2*r*T**2)/2
        self.assert_zero(determinant.subs(sheet)-expected.subs(sheet))
        self.assert_zero((T**2-g2/2-t*q).subs(sheet))

    def test_normalization_relations_and_genuine_denominator(self):
        X, Y, Z, S, V, eta, r = sp.symbols("X Y Z S V eta r")
        f, f1, g, g1, c, d, T = sp.symbols("f f1 g g1 c d T")
        AX = f1+2*T*(X+r)
        BXY = 2*T*Y+T*f-g1*X+c
        D = (X+r)*AX-(2*Y+f)
        E0 = -(X+r)*BXY-g*X+d
        eta_from_y = 2*Y-2*(X+r)*S+f
        z_full = S**2-f1*S-g1*X+c+eta*T
        self.assert_zero(z_full.subs(eta, eta_from_y)-(S**2-AX*S+BXY))
        w_full = (X-r)*Z+(X+r)*S**2-(2*Y+f)*S-g*X+d
        self.assert_zero((w_full-2*X*Z).subs(Z, S**2-AX*S+BXY)-(D*S+E0))
        numerator = (V-E0)**2-AX*D*(V-E0)+BXY*D**2
        self.assert_zero(numerator.subs(V, D*S+E0)-D**2*(S**2-AX*S+BXY))
        self.assertEqual(sp.Poly(D, Y).degree(), 1)
        self.assertEqual(sp.Poly(D, Y).coeff_monomial(Y), -2)
        y_on_divisor = ((X+r)*AX-f)/2
        residue = sp.expand(numerator.subs(Y, y_on_divisor))
        self.assertEqual(sp.Poly(residue, V).coeff_monomial(V**2), 1)
        self.assertEqual(sp.Poly(D**2, Y).degree(), 2)

    def test_rank_two_multiplication_and_conductor_coefficients(self):
        S, A, B, Z, D, p, q, h, k = sp.symbols("S A B Z D p q h k")
        relation = S**2-A*S-Z+B

        def remainder(expression):
            return sp.rem(sp.Poly(expression, S), sp.Poly(relation, S)).as_expr()

        product = remainder((p+q*S)*(h+k*S))
        expected = p*h+q*k*(Z-B)+(p*k+q*h+q*k*A)*S
        self.assert_zero(product-expected)
        # Membership in R means the S coefficient is divisible by D.
        # Once q=D*k, membership of (p+q*S)*S forces D to divide p.
        multiplied_s = sp.Poly(remainder((p+D*k*S)*S), S)
        self.assert_zero(multiplied_s.coeff_monomial(S)-(p+D*k*A))
        self.assert_zero(multiplied_s.coeff_monomial(1)-D*k*(Z-B))
        # D*N multiplies all of N into R, with no denominator required.
        for coefficient in sp.Poly(remainder(D*(p+q*S)*(h+k*S)), S).all_coeffs():
            self.assert_zero(coefficient.subs(D, 0))
        # The missing integral generator S itself is not in R when D is nonunit.
        self.assertEqual(sp.Poly(S, S).coeff_monomial(S).subs(D, 0), 1)

    def test_conductor_derivative_is_incompatible_with_invariance(self):
        X, S, eta, r, f1, T, t, a, omega, xi = sp.symbols(
            "X S eta r f1 T t a omega xi")
        D = (X+r)*(f1+2*T*(X+r)-2*S)-eta
        ED = a*sp.diff(D, X)+a*t*sp.diff(D, S)
        expected = a*(f1-2*S+(4*T-2*t)*(X+r))
        self.assert_zero(ED-expected)
        self.assert_zero(sp.Poly(ED, S).coeff_monomial(S)+2*a)
        full_x = sp.Poly(ED.subs(S, omega+t*X), X)
        self.assert_zero(full_x.coeff_monomial(X)-4*a*(T-t))
        self.assert_zero(full_x.coeff_monomial(X).subs(T, t+xi)-4*a*xi)
        # If a and a*t are polynomials in eta, this displayed derivation
        # is explicitly locally nilpotent on the three polynomial generators.
        ap = eta**2+1
        bp = eta**3-eta

        def deriv(expression):
            return sp.expand(ap*sp.diff(expression, X)+bp*sp.diff(expression, S))

        for generator in (X, S, eta):
            self.assert_zero(deriv(deriv(generator)))
        sample = X**2*S**2+eta*X*S
        for _ in range(5):
            sample = deriv(sample)
        self.assert_zero(sample)


if __name__ == "__main__":
    unittest.main(verbosity=2)
