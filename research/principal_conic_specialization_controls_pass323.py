"""Bounded exact algebra controls for the reciprocal-conic exclusion323.

The four methods reconstruct the generic specialization, the centered
quadratic/cubic algebra, and the literal conic leading coefficients.
Negative controls retain genuine polynomial generation when a needed
nonvanishing or constant-leading-coefficient hypothesis is removed.

This file does not prove actual chart entry, field return, preservation
of the original ring, or the universal generation lemma. Those are
written proof inputs. It imports no solver and no retained checker.
The author has not executed, imported, or compiled this saved source.
"""

import unittest

import sympy as sp


def zero(expression):
    """Exact rational simplification, with no numerical sampling."""
    return sp.cancel(sp.together(sp.expand(expression))) == 0


class ConicSpecializationControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertTrue(zero(expression), str(expression))

    def test_generic_linear_combination_and_specialized_degrees(self):
        x, z = sp.symbols("x z")
        f2, f1, g1, lam, mu = sp.symbols("f2 f1 g1 lam mu")
        g2, h3 = sp.symbols("g2 h3", nonzero=True)
        f0, g0, h2, h1, h0 = [sp.Function(name) for name in
                              ("f0", "g0", "h2", "h1", "h0")]
        first = f2*z**2 + (f1 + lam*x)*z + f0(x)
        second = g2*z**2 + (g1 + mu*x)*z + g0(x)
        third = h3*z**3 + h2(x)*z**2 + h1(x)*z + h0(x)
        slope = g2*lam - f2*mu
        constant_slope = g2*f1 - f2*g1
        self.assert_zero(
            g2*first - f2*second
            - (slope*x + constant_slope)*z - g2*f0(x) + f2*g0(x)
        )

        # Work in the generic coefficient field with slope inverted.
        # The separate negative controls below treat slope=0.
        root = -constant_slope/slope
        first_at, second_at, third_at = [
            expression.subs(x, root) for expression in (first, second, third)
        ]
        self.assert_zero(
            first_at - f2*second_at/g2 - f0(root) + f2*g0(root)/g2
        )
        self.assertEqual(sp.Poly(second_at, z).degree(), 2)
        self.assertEqual(sp.Poly(third_at, z).degree(), 3)
        self.assert_zero(sp.Poly(second_at, z).LC() - g2)
        self.assert_zero(sp.Poly(third_at, z).LC() - h3)

        # No division by the first quadratic coefficient is used.
        self.assert_zero(first_at.subs(f2, 0) - f0(-f1/lam))
        self.assert_zero(root.subs(f2, 0) + f1/lam)

    def test_quadratic_cubic_centering_and_parity_module(self):
        z, xi, q = sp.symbols("z xi q")
        a, c3 = sp.symbols("a c3", nonzero=True)
        b, c, c2, c1, c0 = sp.symbols("b c c2 c1 c0")
        quadratic = a*z**2 + b*z + c
        cubic = c3*z**3 + c2*z**2 + c1*z + c0
        shift = xi - b/(2*a)
        centered_quadratic = sp.expand(quadratic.subs(z, shift))
        centered_cubic = sp.expand(cubic.subs(z, shift))
        self.assert_zero(
            (centered_quadratic - c + b**2/(4*a))/a - xi**2
        )
        even_part = (
            centered_cubic.coeff(xi, 2)*xi**2
            + centered_cubic.coeff(xi, 0)
        )
        odd_slope = c1 - c2*b/a + 3*c3*b**2/(4*a**2)
        odd_generator = centered_cubic - even_part
        self.assert_zero(odd_generator - xi*(c3*xi**2 + odd_slope))
        self.assert_zero(
            odd_generator**2 - xi**2*(c3*xi**2 + odd_slope)**2
        )

        # Multiplication in K[q] + xi*(c3*q+odd_slope)*K[q],
        # modulo xi^2=q, keeps precisely the same odd factor.
        u0, u1, v0, v1 = sp.symbols("u0 u1 v0 v1")
        factor = c3*q + odd_slope
        product = (u0 + xi*factor*u1)*(v0 + xi*factor*v1)
        module_form = (
            u0*v0 + q*factor**2*u1*v1
            + xi*factor*(u0*v1 + u1*v0)
        )
        self.assert_zero(sp.rem(product - module_form, xi**2 - q, xi))
        quotient, remainder = sp.div(1, factor, q)
        self.assert_zero(quotient)
        self.assert_zero(remainder - 1)
        self.assertEqual(sp.Poly(factor, q).degree(), 1)

    def test_literal_conic_potentials_and_nonzero_leaders(self):
        t, tau, d = sp.symbols("t tau d")
        c = sp.symbols("c", nonzero=True)
        x, sigma = sp.symbols("x sigma")
        eta, beta, chi, bp, b0 = sp.symbols("eta beta chi bp b0")
        k, kt, ktt, nt, ns, n, ell, s = sp.symbols(
            "k kt ktt nt ns n ell s"
        )
        duration = t - tau
        coupling = d + c/duration
        p = sp.diff(coupling, t)
        delta = coupling*sp.diff(coupling, t, 2)/(2*p)
        bv = (p - delta)/2
        theta = (eta + 2*p*sigma**2/coupling + beta*sigma + chi)/delta
        y = -bp*sigma - bv*theta - b0
        z = 2*t*y + sigma**2 + kt*sigma + coupling*theta + n
        lower = ktt*sigma**2/2 + p*sigma*theta + nt*sigma + ns*theta
        w = (ell - (2*sigma + kt)*y - lower)/coupling
        actual_y = y + sigma*x + t*x**2
        actual_z = z + (2*t*sigma + k)*x + t**2*x**2
        actual_w = w + theta*x + s*x**2
        theta2 = sp.expand(theta).coeff(sigma, 2)
        y2 = sp.expand(actual_y).coeff(sigma, 2)
        z2 = sp.expand(actual_z).coeff(sigma, 2)
        w3 = sp.expand(actual_w).coeff(sigma, 3)
        denominator = c + d*duration
        self.assert_zero(theta2 - 2*c*duration/denominator**2)
        self.assert_zero(y2 + d*c/denominator**2)
        self.assert_zero(z2 - (1 - 2*t*d*c/denominator**2 + 2*c/denominator))
        self.assert_zero(w3 - 2*c/denominator**2)
        self.assert_zero(w3 + (2*y2 + p*theta2)/coupling)
        self.assert_zero(
            sp.expand(actual_y).coeff(sigma, 1)
            - sp.expand(y).coeff(sigma, 1) - x
        )
        self.assert_zero(
            sp.expand(actual_z).coeff(sigma, 1)
            - sp.expand(z).coeff(sigma, 1) - 2*t*x
        )
        transverse_slope = sp.cancel(z2 - 2*t*y2)
        self.assert_zero(transverse_slope - (3*c + d*duration)/denominator)
        # Extract polynomial support before simplifying coefficient fractions.
        # The nonzero leading coefficients were checked separately above.
        self.assertEqual(sp.Poly(sp.expand(actual_z), sigma).degree(), 2)
        self.assertEqual(sp.Poly(sp.expand(actual_w), sigma).degree(), 3)

        # Test the exact leading polynomials in the transcendental T.
        independent_t = sp.symbols("T")
        z_numerator = sp.cancel(
            (z2*denominator**2).subs(t, independent_t + tau)
        )
        self.assert_zero(sp.Poly(z_numerator, independent_t).coeff_monomial(
            independent_t**2
        ) - d**2)
        self.assert_zero(z2.subs(d, 0) - 3)
        self.assert_zero(y2.subs(d, 0))
        self.assert_zero(w3.subs(d, 0) - 2/c)
        self.assert_zero(transverse_slope.subs(d, 0) - 3)

    def test_missing_hypotheses_allow_actual_polynomial_generation(self):
        x, z = sp.symbols("x z")
        # Both quadratics have the same nonzero moving linear slope.
        # Their constant difference coefficient is 1, so there is no
        # cancellation fiber: r=1*1-1*1=0, yet z=first-second.
        first = z**2 + (x + 1)*z
        second = z**2 + x*z
        third = z**3
        self.assert_zero(first - second - z)
        self.assertEqual(sp.Poly(first, z).degree(), 2)
        self.assertEqual(sp.Poly(second, z).degree(), 2)
        self.assertEqual(sp.Poly(third, z).degree(), 3)
        self.assertEqual(1*1 - 1*1, 0)
        self.assert_zero(sp.expand(first - second).coeff(z, 1) - 1)

        # Keeping r=1 but allowing the cubic leader to depend on x also
        # defeats the conclusion: z=third-first*second, while at x=0
        # the third generator drops from cubic degree to degree one.
        first = x*z
        second = z**2
        third = x*z**3 + z
        self.assert_zero(third - first*second - z)
        self.assertEqual(sp.Poly(third, z).degree(), 3)
        self.assertEqual(sp.Poly(third.subs(x, 0), z).degree(), 1)
        self.assert_zero(first.subs(x, 0))


if __name__ == "__main__":
    unittest.main()
