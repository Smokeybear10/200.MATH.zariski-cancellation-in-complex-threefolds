"""Finite exact controls for reciprocal split rigidity180 and construction182.

Formal coefficient charts are not asserted to be actual dense frames.  The
negative fixture satisfies the differential equations and has nonzero scalar
Jacobian, but its projected-field degree is eight by the written pencil lemma.
The tests verify its equation and primitive coefficient data, not a universal
irreducibility or field-degree theorem.

The final original-coordinate maps really are polynomial automorphisms;
generic I-return identities alone are not treated as realization evidence.
No speed or Ny is set to one in a recognition argument.  No earlier checker
or solver internal is imported.  Root alone performs canonical execution
after full saved-source review.  No novelty or universal proof is claimed.
"""

import unittest

import sympy as sp


class SplitReciprocalGraphControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_pencil_derivatives_and_proper_field_boundary(self):
        t, rho, y = sp.symbols("t rho y")
        d = sp.Symbol("d", nonzero=True)
        T, k, n, ell, B = [sp.Function(name)(t) for name in ("T", "k", "n", "ell", "B")]
        A1, h = d**2 / T, T - t
        w0 = (B - sp.diff(k, t, 3) * y**3 / 6
              - sp.diff(n, t, 2) * y**2 / 2 + sp.diff(ell, t) * y) / d
        w = A1 * rho / d + w0
        theta = (y * w - sp.diff(k, t, 2) * y**2 / 2 - sp.diff(n, t) * y + ell) / d
        z = sp.diff(k, t) * y - y * theta + d * rho + n - t * w
        g3 = (3 * sp.diff(k, t, 2) + T * sp.diff(k, t, 3)) / (6 * d)
        g2 = (2 * sp.diff(n, t) + T * sp.diff(n, t, 2)) / (2 * d)
        g1 = sp.diff(k, t) - ell / d - T * sp.diff(ell, t) / d
        g0 = n - T * B / d
        g = g3 * y**3 + g2 * y**2 + g1 * y + g0
        self.zero(d * T * (z + y**2 * w / d - h * w - g))

        ode_k = T * sp.diff(k, t, 4) + 4 * sp.diff(k, t, 3)
        ode_n = T * sp.diff(n, t, 3) + 3 * sp.diff(n, t, 2)
        ode_ell = T * sp.diff(ell, t, 2) - d * sp.diff(k, t, 2) + 2 * sp.diff(ell, t)
        # Raw derivative errors identify the exact prior ODE needed.
        self.zero(6 * d * sp.diff(g3, t) - sp.diff(h, t) * sp.diff(k, t, 3) - ode_k)
        self.zero(2 * d * sp.diff(g2, t) - sp.diff(h, t) * sp.diff(n, t, 2) - ode_n)
        self.zero(d * sp.diff(g1, t) + sp.diff(h, t) * sp.diff(ell, t) + ode_ell)
        prior = {
            sp.diff(k, t, 4): -4 * sp.diff(k, t, 3) / T,
            sp.diff(n, t, 3): -3 * sp.diff(n, t, 2) / T,
            sp.diff(ell, t, 2): (d * sp.diff(k, t, 2) - 2 * sp.diff(ell, t)) / T,
        }
        for residual in (
            6 * d * sp.diff(g3, t) - sp.diff(h, t) * sp.diff(k, t, 3),
            2 * d * sp.diff(g2, t) - sp.diff(h, t) * sp.diff(n, t, 2),
            d * sp.diff(g1, t) + sp.diff(h, t) * sp.diff(ell, t),
        ):
            self.zero(T * residual.subs(prior, simultaneous=True))

        # Formal/nonactual negative fixture.  All three ODEs hold, but h is
        # nonconstant and the actual projected-field equality is absent.
        kn = t**-5
        en = sp.Rational(10, 3) * t**-6
        An, Tn, hn = 2 / t, t / 2, -t / 2
        mn = 2 * rho / t
        self.zero(t**9 * (sp.diff(kn, t, 4) + 4 * An * sp.diff(kn, t, 3)))
        self.zero(t**8 * (sp.diff(en, t, 2) - An * (sp.diff(kn, t, 2) - 2 * sp.diff(en, t))))
        self.zero(sp.diff(sp.S.Zero, t, 3) + 3 * An * sp.diff(sp.S.Zero, t, 2))
        wn = mn - sp.diff(kn, t, 3) * y**3 / 6 + sp.diff(en, t) * y
        vn = y * wn - sp.diff(kn, t, 2) * y**2 / 2 + en
        zn = sp.diff(kn, t) * y - y * vn + rho - t * wn
        Jn = sp.Matrix([y, zn, wn]).jacobian((t, rho, y)).det()
        self.zero(t**12 * (Jn + 2 * rho / t**2))
        self.assertNotEqual(-2 * rho / t**2, 0)
        gn3 = (3 * sp.diff(kn, t, 2) + Tn * sp.diff(kn, t, 3)) / 6
        gn1 = sp.diff(kn, t) - en - Tn * sp.diff(en, t)
        self.zero(t**7 * gn3 + sp.Rational(5, 2))
        self.zero(t**6 * gn1 - sp.Rational(5, 3))
        gn = gn3 * y**3 + gn1 * y
        self.zero(t**8 * (zn + y**2 * wn - hn * wn - gn))

        # With f=h=-t/2 the coefficient field C(y)(t) is already generated
        # by f.  Its relation with g has total degree eight, not one.
        S, V = sp.symbols("S V")
        relation = 768 * S**7 * V - 20 * y * S - 15 * y**3
        self.zero(t**8 * relation.subs({S: hn, V: gn}, simultaneous=True))
        self.zero(t + 2 * hn)
        self.assertEqual(sp.Poly(relation, S, V).total_degree(), 8)
        self.assertEqual(sp.degree(relation, V), 1)
        self.zero(sp.diff(relation, V) - 768 * S**7)
        self.zero(relation.subs({S: 0, V: 0}) + 15 * y**3)
        self.assertNotEqual(-15 * y**3, 0)
        # The V-leading coefficient is a power of S, and the constant
        # coefficient is nonzero at S=0.  Primitivity plus the written
        # irreducibility/pencil proof supplies the exact field-index claim.

    def test_euler_forms_actual_normalization_and_invariant_coordinate(self):
        X, Y, Z, W = sp.symbols("X Y Z W")
        nu = sp.Symbol("nu")
        d = sp.Symbol("d", nonzero=True)
        original = (X, Y, Z, W)
        forward = (X, Y + nu * X, Z - nu * W, W)
        inverse = (X, Y - nu * X, Z + nu * W, W)
        for expression, target in zip(forward, original):
            self.zero(expression.subs(dict(zip(original, inverse)), simultaneous=True) - target)
        for expression, target in zip(inverse, original):
            self.zero(expression.subs(dict(zip(original, forward)), simultaneous=True) - target)
        self.zero(forward[0] * forward[2] + forward[1] * forward[3] - (X * Z + Y * W))
        for expression, target in zip(inverse, (0, 0, 1, 0)):
            self.zero(sp.diff(expression, Z) - target)

        x, t_old, y, rho, z, w, theta, sigma = sp.symbols("x t_old y rho z w theta sigma")
        old_Y = y + t_old * x
        old_Z = z + sigma * x - t_old * rho * x**2
        old_W = w + theta * x + rho * x**2
        self.zero(old_Y + nu * x - (y + (t_old + nu) * x))
        self.zero(old_Z - nu * old_W
                  - (z - nu * w + (sigma - nu * theta) * x - (t_old + nu) * rho * x**2))
        self.zero(z - nu * w + (t_old + nu) * w - (z + t_old * w))
        t = sp.Symbol("t", nonzero=True)
        self.zero((d**2 / (t_old + nu)).subs(t_old, t - nu) - d**2 / t)

        k2, k1, k0, q, n1, n00, p, ell0, e = sp.symbols("k2 k1 k0 q n1 n00 p ell0 e")
        k = k2 * t**2 + k1 * t + k0 + q / t
        n = n1 * t + n00 + p / t
        ell = d * k2 * t + ell0 + e / t + d * q / t**2
        self.zero(t**5 * (sp.diff(k, t, 4) + 4 * sp.diff(k, t, 3) / t))
        self.zero(t**4 * (sp.diff(n, t, 3) + 3 * sp.diff(n, t, 2) / t))
        self.zero(t**4 * (sp.diff(ell, t, 2) - d * sp.diff(k, t, 2) / t + 2 * sp.diff(ell, t) / t))
        self.zero(t**4 * sp.diff(k, t, 3) + 6 * q)
        self.zero(t**3 * sp.diff(n, t, 2) - 2 * p)
        self.zero(sp.diff(k - q / t, t, 3))
        self.zero(sp.diff(n - p / t, t, 2))
        self.zero(t**2 * sp.diff(ell - d * k2 * t - d * q / t**2, t) + e)

        F3 = k2 * Y**3 + k1 * X * Y**2 + k0 * X**2 * Y + q * X**3
        F2 = n1 * Y**2 + n00 * X * Y + p * X**2
        F1 = (d * k1 - ell0) * Y + (d * k0 - e) * X
        F = F3 + F2 + F1
        U = -X**2 * Z + (d - X * Y) * W
        J = (d + X * Y) * Z + Y**2 * W
        I = J - F
        B0 = sp.Symbol("B0")  # arbitrary coefficient value; no t derivative here.
        m = d**2 * rho / t + B0
        chart_w = (m - sp.diff(k, t, 3) * y**3 / 6
                   - sp.diff(n, t, 2) * y**2 / 2 + sp.diff(ell, t) * y) / d
        chart_theta = (y * chart_w - sp.diff(k, t, 2) * y**2 / 2
                       - sp.diff(n, t) * y + ell) / d
        chart_z = sp.diff(k, t) * y - y * chart_theta + d * rho + n - t * chart_w
        chart_Y = y + t * x
        chart_Z = chart_z + (-t * chart_theta - rho * y + k) * x - t * rho * x**2
        chart_W = chart_w + chart_theta * x + rho * x**2
        chart_J = (d + x * chart_Y) * chart_Z + chart_Y**2 * chart_W
        J_coefficients = [
            d**2 * rho - t * m + d * n + (d * sp.diff(k, t) - ell - t * sp.diff(ell, t)) * y
            + (3 * sp.diff(k, t, 2) + t * sp.diff(k, t, 3)) * y**3 / 6
            + (2 * sp.diff(n, t) + t * sp.diff(n, t, 2)) * y**2 / 2,
            d * k - t * ell + (sp.diff(k, t) + t * sp.diff(k, t, 2) / 2) * y**2
            + (n + t * sp.diff(n, t)) * y,
            (k + t * sp.diff(k, t)) * y + t * n,
            t * k,
        ]
        self.zero(d**2 * t**4 * (chart_J - sum(value * x**i for i, value in enumerate(J_coefficients))))
        chart_F = F.subs({X: x, Y: chart_Y}, simultaneous=True)
        self.zero(d**2 * t**4 * (chart_J - chart_F - (d * n - t * B0)))

        # Actual matrix map: both inverse orders, with only a complex-unit
        # denominator d^2.  No inverse of original X or Y is introduced.
        self.zero((d - X * Y) * J - Y**2 * U - d**2 * Z)
        self.zero((d + X * Y) * U + X**2 * J - d**2 * W)
        x1, y1, u1, i1 = sp.symbols("x1 y1 u1 i1")
        target_F = F.subs({X: x1, Y: y1}, simultaneous=True)
        target_J = i1 + target_F
        inv_Z = ((d - x1 * y1) * target_J - y1**2 * u1) / d**2
        inv_W = ((d + x1 * y1) * u1 + x1**2 * target_J) / d**2
        self.zero(-x1**2 * inv_Z + (d - x1 * y1) * inv_W - u1)
        self.zero((d + x1 * y1) * inv_Z + y1**2 * inv_W - target_F - i1)
        self.zero(I - (d * Z + Y * (X * Z + Y * W) - F))


if __name__ == "__main__":
    unittest.main()
