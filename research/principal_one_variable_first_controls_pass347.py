"""Standalone exact finite controls for 344, 345, and 346.

Only symbolic polynomial and differential-jet identities are checked.
These tests do not certify the universal selected-degree classification,
constant-field integration, exact K-return, local nilpotence, or recognition.
No earlier checker is imported. The author has not executed, imported, or
compiled this saved source; the root agent owns its canonical execution.

Coefficient divisions have declared symbolic nonzero denominators. The g=0
case is treated separately from formulas that divide by g. A final field-only
boundary control explicitly inverts a nonconstant polynomial. Generic jets
are independent until an explicitly displayed identity is substituted.
"""

import unittest

import sympy as sp


class OneVariableFirstPotentialControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.factor(sp.expand(expression)), 0)

    def test_general_nonlinear_second_cubic_restriction(self):
        U, P = sp.symbols("U P")
        alpha, Hr = sp.symbols("alpha Hr", nonzero=True)
        beta, Hrr, Htr, Htt, Ht, Lr, Lt, gp = sp.symbols(
            "beta Hrr Htr Htt Ht Lr Lt gp"
        )
        g = -alpha**2
        phi = (
            Hrr * (U**2 + g * P**2)**2 / 2
            + Htr * (U**2 + g * P**2) * P + Htt * P**2 / 2
            + 2 * (1 + g * Hr) * U * P + Ht * U
            + Hr * gp * P**3 / 3 - Lr * (U**2 + g * P**2) - Lt * P
        )
        centered = sp.expand((U**2 + g * P**2).subs(U, alpha * P + beta))
        self.zero(centered - (2 * alpha * beta * P + beta**2))
        restricted = sp.Poly(sp.expand(phi.subs(U, alpha * P + beta)), P)
        self.assertLessEqual(restricted.degree(), 3)
        self.zero(restricted.coeff_monomial(P**3) - Hr * gp / 3)
        self.assertNotEqual(restricted.coeff_monomial(P**3), 0)
        self.zero(restricted.coeff_monomial(P**4))
        # This is formal substitution only: no derivative of a moving root
        # alpha or beta is introduced in the coefficient comparison.

    def test_variable_c_top_normal_derivative_and_zero_g_boundary(self):
        U, P, r = sp.symbols("U P r")
        c, cp, g = sp.symbols("c cp g", nonzero=True)
        cpp, d1, d2, gp, Lr, Lt, beta = sp.symbols("cpp d1 d2 gp Lr Lt beta")
        J = 1 + g * c
        phi = (
            cp * P * U**2 + (g * cp + c * gp / 3) * P**3
            + (cpp * r + d2) * P**2 / 2 + 2 * J * U * P
            + (cp * r + d1) * U - Lr * (U**2 + g * P**2) - Lt * P
        )
        top = sum(coef * U**ij[0] * P**ij[1]
                  for ij, coef in sp.Poly(phi, U, P).terms() if sum(ij) == 3)
        self.zero(top - P * (cp * U**2 + (g * cp + c * gp / 3) * P**2))
        lam, z = sp.symbols("lam z")
        self.zero(sp.discriminant(cp * z**2 + lam, z) + 4 * cp * lam)
        self.zero(top.subs(gp, -3 * g * cp / c) - cp * P * U**2)

        identities = {
            gp: -3 * g * cp / c,
            beta: -J / cp,
            Lr: (cpp * r + d2) / (2 * g),
            Lt: -J**2 / cp,
        }
        restricted = sp.Poly(sp.expand(
            phi.subs(U, beta).subs(identities, simultaneous=True)
        ), P)
        for power in (1, 2, 3):
            self.zero(restricted.coeff_monomial(P**power))
        normal = sp.diff(phi, U).subs(U, beta)
        normal_value = cp * r + d1 - 2 * beta * Lr
        self.zero((normal - normal_value).subs(identities, simultaneous=True))
        self.zero(sp.Poly(sp.expand(normal), P).coeff_monomial(P)
                  - 2 * (cp * beta + J))

        # Separate g=0 control. Do not substitute into identities containing
        # 1/g: the coefficient equations are rebuilt before that division.
        zero_g_phi = phi.subs({g: 0, gp: 0}, simultaneous=True)
        zero_g_line = sp.Poly(sp.expand(zero_g_phi.subs(U, -1 / cp)), P)
        self.zero(zero_g_line.coeff_monomial(P**2) - (cpp * r + d2) / 2)
        self.zero(zero_g_line.coeff_monomial(P) + 1 / cp + Lt)
        final_zero_g = zero_g_line.as_expr().subs(
            {cpp: 0, d2: 0, Lt: -1 / cp}, simultaneous=True
        )
        self.assertLessEqual(sp.Poly(sp.expand(final_zero_g), P).degree(), 0)

    def test_literal_scalar_energy_and_quadratic_field_coefficient(self):
        t, r, P = sp.symbols("t r P")
        c, cp, g = sp.symbols("c cp g", nonzero=True)
        beta, betap, p, f, J, Jt, cpp, d1, d2 = sp.symbols(
            "beta betap p f J Jt cpp d1 d2"
        )
        Lval, Lr, Lt = sp.symbols("Lval Lr Lt")
        y = beta - p
        z = 2 * t * beta + J * P**2 + (cp * r + d1) * P + c * beta**2 - Lval + f - 2 * t * p
        w = r - 2 * beta * P

        def dt(expr):
            jet = ((beta, betap), (p, g), (f, 2 * p), (J, Jt),
                   (cp, cpp), (d1, d2), (c, cp), (Lval, Lt))
            return sp.diff(expr, t) + sum(sp.diff(expr, v) * dv for v, dv in jet)

        def dr(expr):
            return sp.diff(expr, r) + sp.diff(expr, Lval) * Lr

        rows = [sp.Matrix([dt(expr), dr(expr), sp.diff(expr, P)]) for expr in (y, z, w)]
        scalar = sp.expand(rows[0].dot(rows[1].cross(rows[2])))
        expected = (betap - g) * (-2 * (beta * cp + J) * P + 2 * beta * Lr - cp * r - d1)
        self.zero(scalar - expected)
        self.zero((scalar - (betap - g) * (2 * beta * Lr - cp * r - d1)).subs(beta, -J / cp))
        self.zero(scalar.subs({g: 0, betap: 0}, simultaneous=True))

        A, B, energy, gp = sp.symbols("A B energy gp")
        Jexact = 1 + g * c

        def exact_dt(expr):
            return sp.diff(expr, c) * cp + sp.diff(expr, cp) * A * g + sp.diff(expr, g) * gp

        gp_value = -3 * g * cp / c
        conserved_C = g * c**3
        conserved_energy = cp**2 + A * g * c
        self.zero(exact_dt(conserved_C).subs(gp, gp_value))
        self.zero(exact_dt(conserved_energy).subs(gp, gp_value))
        self.zero(exact_dt(Jexact).subs(gp, gp_value) + 2 * g * cp)
        exact_betap = exact_dt(-Jexact / cp).subs(gp, gp_value)
        self.zero(exact_betap - g - g * (conserved_energy + A) / cp**2)
        # Compatibility of L_t in F with L_r=(A*r+B)/2 forces the exact
        # derivative constants. This formal ledger retains both coefficients.
        At, Bt = sp.symbols("At Bt")
        compatibility = At * r / 2 + Bt / 2
        self.zero(sp.diff(compatibility, r) - At / 2)
        self.zero(compatibility.subs(r, 0) - Bt / 2)

        wvar, e = sp.symbols("wvar e")
        integrated_z = z.subs(Lval, A * r**2 / 4 + B * r / 2 + e)
        eliminated = sp.Poly(sp.expand(integrated_z.subs(r, wvar + 2 * beta * P)), P)
        quadratic = eliminated.coeff_monomial(P**2)
        self.zero(quadratic - (J + 2 * beta * cp - A * beta**2))
        q2 = quadratic.subs({beta: -Jexact / cp, J: Jexact}, simultaneous=True)
        self.zero(q2 + Jexact * (conserved_energy + A) / cp**2)
        self.zero(w.subs(r, wvar + 2 * beta * P) - wvar)
        self.zero((wvar + 2 * beta * P).subs(wvar, w) - r)

        a2, a1, a0, zvar = sp.symbols("a2 a1 a0 zvar")
        polynomial = a2 * P**2 + a1 * P + a0 - zvar
        disc = sp.discriminant(polynomial, P)
        self.zero(disc - (a1**2 - 4 * a2 * (a0 - zvar)))
        self.assertEqual(sp.Poly(disc, zvar).degree(), 1)
        self.zero(sp.diff(disc, zvar) - 4 * a2)
        self.assertEqual(sp.Poly(polynomial.subs(a2, 0), P).degree(), 1)
        # Actual nonvanishing of a2, and both K-field inclusions, remain
        # hypotheses/deductions of the written proof, not sampled tests.

    def test_constant_c_normal_derivatives_and_odd_module_identities(self):
        U, P, beta = sp.symbols("U P beta")
        c = sp.symbols("c", nonzero=True)
        g, gp, Lr, Lt, d1, d2 = sp.symbols("g gp Lr Lt d1 d2")
        phi = (-Lr * U**2 + 2 * (1 + c * g) * U * P + d1 * U
               + (d2 / 2 - g * Lr) * P**2 + c * gp * P**3 / 3 - Lt * P)
        normal_line = sp.diff(phi, P).subs(P, beta)
        self.zero(sp.diff(normal_line, U) - 2 * (1 + c * g))
        self.zero(sp.diff(phi, U) - (-2 * Lr * U + 2 * (1 + c * g) * P + d1))
        A3, A2, A1, A0 = sp.symbols("A3 A2 A1 A0")
        graph = A3 * P**3 + A2 * P**2 + A1 * P + A0
        normal_graph = sp.Poly(sp.expand(sp.diff(phi, U).subs(U, graph)), P)
        self.zero(normal_graph.coeff_monomial(P**3) + 2 * Lr * A3)
        self.zero(normal_graph.coeff_monomial(P).subs(Lr, 0) - 2 * (1 + c * g))
        self.zero(sp.Poly(phi, U, P).coeff_monomial(P**3) - c * gp / 3)

        z, u = sp.symbols("z u")
        a, A = sp.symbols("a A", nonzero=True)
        b0, B, E0, E2 = sp.symbols("b0 B E0 E2")
        sigma = a * z**2 + b0
        x = E0 + E2 * z**2 + z * (A * z**2 + B)
        odd = x - E0 - E2 * (sigma - b0) / a
        self.zero(odd - z * (A * z**2 + B))
        self.zero(odd**2 - (u * (A * u + B)**2).subs(u, z**2))
        self.assertEqual(sp.Poly(A * u + B, u).degree(), 1)
        self.assertEqual(sp.Poly((A * u + B).subs(B, 0), u).degree(), 1)
        f0, f1, g0, g1 = sp.symbols("f0 f1 g0 g1")
        R = A * z**2 + B
        product = (f0 + z * R * f1) * (g0 + z * R * g1)
        self.zero(product - (f0 * g0 + z**2 * R**2 * f1 * g1
                              + z * R * (f0 * g1 + f1 * g0)))
        # A=0, B!=0 is a real boundary: the odd coefficient becomes a unit.
        # The degree-(3,2) exclusion cannot be asserted after dropping A!=0.
        Bunit = sp.symbols("Bunit", nonzero=True)
        self.zero(odd.subs({A: 0, B: Bunit}, simultaneous=True) / Bunit - z)
        # Inverting the nonconstant coefficient also recovers z in the field,
        # illustrating why the theorem needs polynomial-ring, not field, return.
        self.zero(sp.cancel(odd / (A * z**2 + B)) - z)


if __name__ == "__main__":
    unittest.main()
