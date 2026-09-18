"""Finite exact checks for the two different repair paths of pass 34.

Only unittest and SymPy are imported. These controls do not prove the
universal normalized-centralizer classification or find an unknown quotient.
"""

import unittest

import sympy as sp


x, lam, b, c, h, t, u = sp.symbols("x lam b c h t u")


def expand(expression):
    return sp.expand(expression)


def jacobian_field_h(potential):
    """Exact physical Jacobian coefficients kept in independent b,h symbols.

    The substitution h=x²c-b² is injective. Its chain rule avoids expanding
    high powers while still checking both physical coefficient polynomials.
    """
    h_derivative = sp.diff(potential, h)
    return (expand(x**2 * h_derivative),
            expand(-sp.diff(potential, b) + 2 * b * h_derivative))


def apply(field, expression):
    return expand(field[0] * sp.diff(expression, b)
                  + field[1] * sp.diff(expression, c))


def auxiliary_flow(p, parameter=lam):
    invariant = p * b + x**2 * h**2
    new_h = h - 2 * parameter * x * p * invariant**2
    new_b = (b + 4 * parameter * x**3 * h * invariant**2
             - 4 * parameter**2 * x**4 * p * invariant**4)
    return invariant, new_b, new_h


def lambda_jet(expression):
    return sp.rem(expand(expression), lam**2, lam)


class PlinthRepairChecks(unittest.TestCase):
    def test_parameter_bridge_has_uniform_polynomial_inverse_identities(self):
        p = 1 - (1 - t) * x
        F, W, H = auxiliary_flow(p)
        self.assertEqual(p.subs(x, 0), 1)
        self.assertEqual(expand(p * W + x**2 * H**2 - F), 0)
        recovered_h = H + 2 * lam * x * p * F**2
        recovered_b = (W - 4 * lam * x**3 * H * F**2
                       - 4 * lam**2 * x**4 * p * F**4)
        self.assertEqual(expand(recovered_h), h)
        self.assertEqual(expand(recovered_b), b)
        # The reverse-time maps are independently checked on the same
        # independent coordinate plane, uniformly in the path parameter.
        inverse_h = h + 2 * lam * x * p * F**2
        inverse_b = (b - 4 * lam * x**3 * h * F**2
                     - 4 * lam**2 * x**4 * p * F**4)
        self.assertEqual(expand(p * inverse_b + x**2 * inverse_h**2 - F), 0)
        self.assertEqual(expand(inverse_h - 2 * lam * x * p * F**2), h)
        self.assertEqual(expand(inverse_b + 4 * lam * x**3 * inverse_h * F**2
                                - 4 * lam**2 * x**4 * p * F**4), b)
        # Both canonical physical numerator congruences use only p(0)=1.
        self.assertEqual(sp.rem(expand(
            (H + (1 + lam * x)**2 * W**2).subs(h, x**2 * c - b**2)),
            x**2, x), 0)

    def test_actual_first_jet_of_bridge_has_a_nonadditive_parameter_term(self):
        p = 1 - x
        r = p + t * (1 - p)
        Fr = r * b + x**2 * h**2
        inverse_r_b = b - 4 * lam * x**3 * h * Fr**2
        inverse_r_h = h + 2 * lam * x * r * Fr**2
        Fp_after_inverse = lambda_jet(
            p * inverse_r_b + x**2 * inverse_r_h**2)
        # Compose U_p with U_r^-1 in the actual quotient modulo lambda².
        bridge_b = lambda_jet(
            inverse_r_b + 4 * lam * x**3 * inverse_r_h * Fp_after_inverse**2)
        first = expand(bridge_b.coeff(lam, 1))
        Fp = p * b + x**2 * h**2
        expected = 4 * x**3 * h * (Fp**2 - Fr**2)
        self.assertEqual(first, expand(expected))
        self.assertEqual(first.coeff(t, 2), -4 * x**3 * h * (1 - p)**2 * b**2)
        additive_defect = expand(first.subs(t, t + u) - first
                                 - first.subs(t, u))
        self.assertEqual(additive_defect,
                         -8 * x**3 * h * (1 - p)**2 * b**2 * t * u)
        self.assertNotEqual(additive_defect, 0)
        self.assertEqual(first.subs(t, 0), 0)

    def test_scaling_identity_on_an_actual_centralizer_and_required_q1_premise(self):
        D0 = (x**2, 2 * b)
        E = (sp.Integer(0), 4 * x * b)
        pencil = (x**2, 2 * b + 4 * lam * x * b)
        K = lam * (b**3 + x * b) + lam**4 * x**2
        forward = (b, c + K)
        inverse = {b: b, c: c - K}
        for actual, variable in zip(forward, (b, c)):
            self.assertEqual(expand(actual.subs(inverse, simultaneous=True)), variable)
        conjugated = tuple(expand(apply(pencil, value).subs(
            inverse, simultaneous=True)) for value in forward)
        conjugated_E = tuple(expand(apply(E, value).subs(
            inverse, simultaneous=True)) for value in forward)
        self.assertEqual(conjugated_E, E)
        D1 = (sp.Integer(0), 4 * x * b + x**2 * (3 * b**2 + x))
        self.assertEqual(conjugated,
                         tuple(expand(v0 + lam * v1) for v0, v1 in zip(D0, D1)))
        scaled_K = K.subs(lam, t * lam)
        scaled_actual = (x**2, expand(2 * b + 4 * lam * x * b
                                     + x**2 * sp.diff(scaled_K, b)))
        identity_rhs = tuple(expand(v0 + t * lam * v1 + (1 - t) * lam * ee)
                             for v0, v1, ee in zip(D0, D1, E))
        self.assertEqual(scaled_actual, identity_rhs)
        # Centralizing E alone does not guarantee q1 if the original
        # degree-one premise is omitted.
        higher_K = lam**2 * b**2
        higher_pencil_c = 2 * b + 4 * lam * x * b + x**2 * sp.diff(higher_K, b)
        self.assertEqual(sp.Poly(higher_pencil_c, lam).degree(), 2)

    def test_p_family_conjugated_E_has_exact_fourth_coefficient(self):
        p = 1 - x
        h0 = h
        F = p * b + x**2 * h0**2
        W = (b + 4 * lam * x**3 * h0 * F**2
             - 4 * lam**2 * x**4 * p * F**4)
        L = (2 * x**4 * h0, -p + 4 * x**2 * b * h0)
        actual = jacobian_field_h(-2 * x * W**2)
        self.assertEqual(tuple(sp.Poly(value, lam).degree() for value in actual), (4, 4))
        expected_fourth = tuple(expand(-256 * x**9 * p**2 * F**7 * value)
                                for value in L)
        fourth = tuple(expand(sp.Poly(value, lam).nth(4)) for value in actual)
        self.assertEqual(fourth, expected_fourth)
        self.assertNotEqual(fourth, (0, 0))
        self.assertEqual(tuple(value.subs(lam, 0) for value in actual),
                         (0, 4 * x * b))

    def test_full_scaled_hamiltonian_has_degree_five_only_off_the_endpoints(self):
        p = 1 - x
        h0 = h
        F = p * b + x**2 * h0**2
        W = (b + 4 * lam * x**3 * h0 * F**2
             - 4 * lam**2 * x**4 * p * F**4)
        H = h0 - 2 * lam * x * p * F**2
        L = (2 * x**4 * h0, -p + 4 * x**2 * b * h0)
        D1 = tuple(-4 * x * p * F * value for value in L)
        C = jacobian_field_h(-2 * x * W**2)
        # These are the actual images of h,b under phi_t^-1.
        image_b = W.subs(lam, t * lam)
        image_h = (H + 2 * lam * x * W**2).subs(lam, t * lam)
        actual = jacobian_field_h(image_h - 2 * lam * x * image_b**2)
        expected = tuple(expand(v0 + t * lam * v1
                                + (1 - t) * lam * cc.subs(lam, t * lam))
                         for v0, v1, cc in zip((x**2, 2 * b), D1, C))
        self.assertEqual(actual, expected)
        self.assertEqual(tuple(sp.Poly(value, lam).degree() for value in actual), (5, 5))
        for tau in (sp.Integer(2), sp.Integer(-1), sp.Rational(1, 2)):
            self.assertEqual(tuple(sp.Poly(value.subs(t, tau), lam).degree()
                                   for value in actual), (5, 5))
        for tau in (sp.Integer(0), sp.Integer(1)):
            self.assertEqual(max(sp.Poly(value.subs(t, tau), lam).degree()
                                 for value in actual), 1)
        for value, cc in zip(actual, C):
            self.assertEqual(expand(sp.Poly(value, lam).nth(5)),
                             expand((1 - t) * t**4 * sp.Poly(cc, lam).nth(4)))

    def test_repair_endpoint_and_exact_fiberwise_plinth_degree_behavior(self):
        p_t = 1 - (1 - t) * x
        h0 = x**2 * c - b**2
        F = p_t * b + x**2 * h0**2
        g = 1 + 2 * (1 - t) * x
        numerator = expand(h0 + g * F**2)
        S, remainder = sp.div(numerator, x**2, x)
        self.assertEqual(remainder, 0)
        L = (2 * x**4 * h0, -p_t + 4 * x**2 * b * h0)
        self.assertEqual(apply(L, S), expand(-p_t))
        self.assertEqual(apply(tuple(value.subs(t, 1) for value in L),
                               S.subs(t, 1)), -1)
        self.assertEqual(sp.degree(p_t.subs(t, 1), x), 0)
        for tau in (sp.Integer(0), sp.Integer(2), sp.Integer(-1)):
            self.assertEqual(sp.degree(p_t.subs(t, tau), x), 1)
        self.assertEqual(sp.cancel(p_t.subs(x, 1 / (1 - t))), 0)
        double_root_path = 1 + (1 - t) * ((1 - x)**2 - 1)
        self.assertEqual(sp.degree(double_root_path.subs(t, 0), x), 2)
        self.assertEqual(sp.degree(double_root_path.subs(t, 2), x), 2)
        self.assertEqual(sp.degree(double_root_path.subs(t, 1), x), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
