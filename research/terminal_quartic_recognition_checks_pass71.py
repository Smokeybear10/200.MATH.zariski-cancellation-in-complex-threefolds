"""Bounded exact controls for the separate pass71 written arguments.

Coefficient tables live in an explicitly larger polynomial ring. They are
not a realization of the original four-coordinate adjoint frame. Actual
polynomial shear inverses are distinguished from those formal tables.
Finite degree cases do not prove Wang's theorem or the universal leading
coefficient argument, and no source theorem is computationally certified.
"""

import unittest

import sympy as sp


class TerminalQuarticRecognitionChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_one_power_polynomial_field_and_parabolic_shear(self):
        a, b, z, w, g, n, u, v, p = sp.symbols("a b z w g n u v p")
        nu1, nu2 = sp.symbols("nu1 nu2")
        c0 = 2 * nu1 + nu2**2 / 2
        coordinates = (a, b, z, w, g, n, u, v, p)
        # This nine-variable coefficient model is deliberately not B=C^[4].
        e_values = (v + g * b / 3, u + g * (z / 2 + c0),
                    2 * n + 2 * nu2 * g, p, 0, g**2 / 2,
                    g * n, g * u / 3, 0)
        t_values = (u / 3, n, g, 0, 0, 0, 0, 0, 0)

        def derivation(values, expression):
            return sum(value * sp.diff(expression, coordinate)
                       for coordinate, value in zip(coordinates, values))

        def e(expression):
            return derivation(e_values, expression)

        def t(expression):
            return derivation(t_values, expression)

        def delta(expression):
            return e(expression) / g

        def s(expression):
            return t(expression) / g

        for coordinate in coordinates:
            self.assert_zero(e(t(coordinate)) - t(e(coordinate)))
            self.assert_zero(t(t(coordinate)))
            self.assert_zero(g * s(coordinate) - t(coordinate))
        self.assert_zero((e(z) - 2 * nu2 * g) / 2 - n)
        self.assert_zero(e(b) - g * (z / 2 + c0) - u)
        self.assert_zero(e(a) - g * b / 3 - v)

        beta = n / g
        h = u / g - beta**2
        i = v / g - 2 * beta**3 / 9 - 2 * h * beta / 3
        self.assert_zero(delta(beta) - sp.Rational(1, 2))
        self.assert_zero(delta(u / (3 * g)) - beta / 3)
        for invariant in (g, h, i, p):
            self.assert_zero(e(invariant))
            self.assert_zero(t(invariant))
        h_cleared = -n**2 + g * u
        i_cleared = 4 * n**3 / 9 - 2 * g * u * n / 3 + g**2 * v
        self.assert_zero(g**2 * h - h_cleared)
        self.assert_zero(g**3 * i - i_cleared)
        quotient = (-12 * u**2 * n**2 + 72 * v * n**3
                    + g * (16 * u**3 - 108 * u * n * v)
                    + 81 * g**2 * v**2)
        self.assert_zero(81 * i_cleared**2 + 16 * h_cleared**3 - g**2 * quotient)
        self.assert_zero(e(quotient))
        self.assert_zero(t(quotient))

        # The coordinate map itself is an actual polynomial automorphism.
        a0, b0, z0, w0 = sp.symbols("a0 b0 z0 w0")
        old = sp.Matrix([a0, b0, z0, w0])
        new = sp.Matrix([a, b, z, w])
        forward = sp.Matrix([a0 - z0**2 / 12 + nu2 * b0 / 3, b0, z0, w0])
        inverse = sp.Matrix([a + z**2 / 12 - nu2 * b / 3, b, z, w])
        self.assert_zero(forward.subs(dict(zip(old, inverse)), simultaneous=True) - new)
        self.assert_zero(inverse.subs(dict(zip(new, forward)), simultaneous=True) - old)
        jacobian = forward.jacobian(old)
        transported = inverse.jacobian(new).subs(dict(zip(new, forward)), simultaneous=True)
        self.assert_zero(jacobian * transported - sp.eye(4))
        self.assert_zero(transported * jacobian - sp.eye(4))
        self.assertEqual(jacobian.det(), 1)
        self.assert_zero(transported[:, 0] - sp.eye(4)[:, 0])
        self.assert_zero(transported[:, 3] - sp.eye(4)[:, 3])
        self.assert_zero(transported[:, 1] - sp.eye(4)[:, 1] + nu2 * sp.eye(4)[:, 0] / 3)
        self.assert_zero(transported[:, 2] - sp.eye(4)[:, 2] - z0 * sp.eye(4)[:, 0] / 6)

    def test_weighted_leading_coefficient_including_zero_and_one(self):
        w, time = sp.symbols("w time")
        p, g = sp.symbols("p g", nonzero=True)
        n, u = sp.symbols("n u")
        aa, bb, cc = sp.symbols("aa bb cc", nonzero=True)
        # These are coefficient-identity controls, not asserted zero relations.
        cases = (
            (0, 0, cc),
            (0, bb, cc * w + 7),
            (aa, 0, cc),
            (aa, bb * w + 3, cc * w**2 + 5 * w + 7),
            (aa * w**2 + w + 1, bb * w**3 + 2, cc * w**4 + 3),
            (aa * w**2 + 1, bb, cc * w + 2),
            (aa, bb * w**4 + 1, cc),
            (aa, bb, cc * w**4 + 1),
        )
        observed_degrees = []
        for case in cases:
            with self.subTest(coefficients=case):
                polynomials = tuple(sp.sympify(entry) for entry in case)
                weighted = [sp.degree(poly, w) + offset if poly != 0 else None
                            for poly, offset in zip(polynomials, (2, 1, 0))]
                degree = max(value for value in weighted if value is not None)
                observed_degrees.append(degree)
                starred = [sp.Poly(poly, w).LC() if weight == degree else 0
                           for poly, weight in zip(polynomials, weighted)]
                flow_factors = (u + time * g * n + time**2 * g**3 / 4,
                                n + time * g**2 / 2, g)
                flow = sum(poly.subs(w, w + time * p) * factor
                           for poly, factor in zip(polynomials, flow_factors))
                coefficient = sp.Poly(sp.expand(flow), time).coeff_monomial(time**degree)
                expected = sum(star * p**(degree - offset) * factor
                               for star, offset, factor in zip(starred, (2, 1, 0),
                                                               (g**3 / 4, g**2 / 2, g))
                               if star != 0)
                self.assert_zero(coefficient - expected)
                normalized = starred[0] * g**2 / 4 + starred[1] * p * g / 2 + starred[2] * p**2
                self.assert_zero(coefficient / (g * p**(degree - 2)) - normalized)
                self.assertNotEqual(sp.expand(normalized), 0)
        self.assertIn(0, observed_degrees)
        self.assertIn(1, observed_degrees)

    def test_two_endpoint_shears_and_good_partial_cancellation(self):
        a, b, z, w = sp.symbols("a b z w")
        ap, bp, zp, wp = sp.symbols("ap bp zp wp")
        lam, g = sp.symbols("lam g", nonzero=True)
        alpha, gamma, invariant, u0, chi = sp.symbols("alpha gamma invariant u0 chi")
        old = sp.Matrix([a, b, z, w])
        new = sp.Matrix([ap, bp, zp, wp])
        f = w / (2 * lam)
        beta = f + invariant
        h = alpha * invariant + gamma - invariant**2
        kappa = (beta**2 + h) / 3
        linear = (2 * f + alpha) / 3
        remainder = (-f**2 - alpha * f + gamma) / 3
        self.assert_zero(kappa - linear * beta - remainder)
        self.assert_zero(lam * sp.diff(beta, w) - sp.Rational(1, 2))
        self.assert_zero(lam * sp.diff(kappa, w) - beta / 3)

        def inverse_and_transport(forward, inverse):
            self.assert_zero(forward.subs(dict(zip(old, inverse)), simultaneous=True) - new)
            self.assert_zero(inverse.subs(dict(zip(new, forward)), simultaneous=True) - old)
            jacobian = forward.jacobian(old)
            transported = inverse.jacobian(new).subs(dict(zip(new, forward)), simultaneous=True)
            self.assert_zero(jacobian * transported - sp.eye(4))
            self.assert_zero(transported * jacobian - sp.eye(4))
            self.assertEqual(jacobian.det(), 1)
            return jacobian, transported

        # The two maps are genuine polynomial automorphisms over the
        # displayed constant field. Their S/E tables are formal input.
        forward = sp.Matrix([a - linear * b - remainder * z, b - f * z, z, w])
        fp = f.subs(w, wp)
        lp = linear.subs(w, wp)
        rp = remainder.subs(w, wp)
        inverse = sp.Matrix([ap + lp * bp + (lp * fp + rp) * zp, bp + fp * zp, zp, wp])
        jacobian, transported = inverse_and_transport(forward, inverse)
        self.assert_zero(jacobian * sp.Matrix([kappa, beta, 1, 0])
                         - sp.Matrix([0, invariant, 1, 0]))
        self.assert_zero(transported[:, 1] - sp.eye(4)[:, 1] - linear * sp.eye(4)[:, 0])

        e_linear = lam * g * sp.diff(linear, w)
        ee_linear = lam * g * sp.diff(e_linear, w)
        self.assert_zero(e_linear - g / 3)
        self.assert_zero(ee_linear)
        wa = sp.Matrix(sp.symbols("wa0:4"))
        vb = -sp.Rational(2, 3) * g * wa
        # The original identity g W_a=-3 V_b/2 is a stated hypothesis.
        self.assert_zero(g * wa + sp.Rational(3, 2) * vb)
        self.assert_zero(vb + ee_linear * sp.eye(4)[:, 0] + 2 * e_linear * wa)

        beta0 = f + u0
        primitive = w**2 / (12 * lam**2) + u0 * w / (3 * lam)
        kappa0 = primitive + chi
        self.assert_zero(lam * sp.diff(primitive, w) - beta0 / 3)
        forward0 = sp.Matrix([a - primitive * z, b - beta0 * z, z, w])
        inverse0 = sp.Matrix([ap + primitive.subs(w, wp) * zp,
                              bp + beta0.subs(w, wp) * zp, zp, wp])
        jacobian0, transported0 = inverse_and_transport(forward0, inverse0)
        self.assert_zero(jacobian0 * sp.Matrix([kappa0, beta0, 1, 0])
                         - sp.Matrix([chi, 0, 1, 0]))
        self.assert_zero(transported0[:, 0] - sp.eye(4)[:, 0])


if __name__ == "__main__":
    unittest.main()
