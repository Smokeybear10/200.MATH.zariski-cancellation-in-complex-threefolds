"""Bounded exact controls for vanishing-p degree-one integrability.

No project modules or solver internals are imported. The universal recognition
and all-order quantifiers are proved in vanishing-plinth-integrability-pass38.md.
"""

import unittest

import sympy as sp


x, lam, b, c, T, w, z = sp.symbols("x lam b c T w z")
h = x**2 * c - b**2
two_thirds = sp.Rational(2, 3)


def mod_x_polynomial(value, modulus):
    return sp.expand(sp.rem(sp.expand(value), modulus, x))


def compose_mod(polynomial, value, modulus):
    """Horner substitution in T, reducing after each multiplication."""
    coefficients = sp.Poly(polynomial, T).all_coeffs()
    result = sp.Integer(0)
    for coefficient in coefficients:
        result = mod_x_polynomial(result * value + coefficient, modulus)
    return result


def finite_curve_inverse(Q, G, modulus):
    """Reconstruct both-sided inverse in the finite coefficient ring."""
    error = lam * compose_mod(G, Q, modulus)
    inverse = T
    for _ in range(sp.degree(modulus, x)):
        inverse = mod_x_polynomial(
            T - compose_mod(error, inverse, modulus), modulus
        )
    return error, inverse


def correction_from_inverse(Q, inverse, modulus):
    numerator = mod_x_polynomial(
        Q - compose_mod(Q, inverse, modulus), modulus
    )
    quotient, remainder = sp.div(numerator, lam, lam)
    if sp.expand(remainder) != 0:
        raise AssertionError("The correction numerator is not divisible by lambda")
    return mod_x_polynomial(quotient, modulus)


def closed_family(e):
    p = x**e
    time = two_thirds * lam * x
    n = e + 2
    geometric_sum = sum((-time)**j for j in range(n))
    coefficient_b = sp.expand(1 - time * geometric_sum)
    coefficient_h = (-two_thirds * lam)**n * x**2
    W = sp.expand(coefficient_b * b + coefficient_h * h)
    K = sp.expand(time * p * b + (1 + time) * h)
    numerator = sp.expand(K + (1 + lam * x)**2 * W**2)
    Z, remainder = sp.div(numerator, x**2, x)
    if sp.expand(remainder) != 0:
        raise AssertionError("The forward physical coordinate has an x-pole")
    return p, time, coefficient_b, coefficient_h, W, K, sp.expand(Z)


class VanishingPlinthIntegrabilityChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def assert_mod_zero(self, expression, modulus):
        self.assert_zero(mod_x_polynomial(expression, modulus))

    def test_exact_polynomial_parity_equation(self):
        coefficients = sp.symbols("h0:7")
        H = sum(coefficient * T**index
                for index, coefficient in enumerate(coefficients))
        equation = sp.Poly(H + 2 * T * sp.diff(H, T) - 2 * T, T)
        constraints = [equation.coeff_monomial(T**index)
                       for index in range(1, 7)]
        solutions = sp.solve(constraints, coefficients[1:], dict=True)
        self.assertEqual(
            solutions,
            [{coefficients[1]: two_thirds,
              **{coefficient: sp.Integer(0) for coefficient in coefficients[2:]}}],
        )
        q0, q1 = sp.symbols("q0 q1", nonzero=True)
        Q0 = q0 + q1 * T
        G1 = two_thirds * T / q1
        H_linear = sp.expand(G1.subs(T, Q0))
        self.assert_zero(
            H_linear + 2 * T * sp.diff(H_linear, T) - 2 * T
            - two_thirds * q0 / q1
        )

    def test_primitive_boundary_and_zeroth_order_obstructions(self):
        alpha = sp.symbols("alpha")
        for e in (1, 2, 4):
            primitive_F = x**e * b + h
            self.assertEqual(
                sp.gcd(sp.diff(primitive_F, c), -sp.diff(primitive_F, b)), 1
            )
            constant_boundary_F = x**e * b + 2 + x * h
            for coefficient in (
                sp.diff(constant_boundary_F, c),
                -sp.diff(constant_boundary_F, b),
            ):
                self.assert_mod_zero(coefficient, x)
        for Q0 in (T, T + T**2, 1 + T**3):
            F0 = Q0.subs(T, -b**2)
            for G0 in (T, T + T**2):
                boundary = sp.expand(G0.subs(T, F0) + 2 * alpha * b)
                self.assert_zero(
                    (boundary - boundary.subs(b, -b)) / 2 - 2 * alpha * b
                )
                even = sp.expand((boundary + boundary.subs(b, -b)) / 2)
                self.assertGreater(sp.degree(even, b), 0)

    def test_finite_normal_displacement_including_e_one(self):
        # Nonlinear data deliberately need not satisfy the final parity gate.
        Q = T + T**2 + x * T
        G = x * (T + T**2 / 2) + x**2 * T
        g1 = 1 + T
        Q0 = T + T**2
        expected_first = sp.expand(
            b - x * lam * b * sp.diff(Q0, T).subs(T, -b**2)
            * g1.subs(T, Q0.subs(T, -b**2))
        )
        for e in (1, 2):
            modulus = x**(e + 2)
            p = x**e * (1 + x)
            error, inverse = finite_curve_inverse(Q, G, modulus)
            self.assert_mod_zero(
                inverse + compose_mod(error, inverse, modulus) - T, modulus
            )
            self.assert_mod_zero(
                compose_mod(inverse, T + error, modulus) - T, modulus
            )
            F = mod_x_polynomial(p * b + Q.subs(T, h), modulus)
            K = mod_x_polynomial(h + lam * compose_mod(G, F, modulus), modulus)
            phi_h = mod_x_polynomial(h + compose_mod(error, h, modulus), modulus)
            displacement = lam * p * b * compose_mod(sp.diff(G, T),
                                                      Q.subs(T, h), modulus)
            self.assert_mod_zero(K - phi_h - displacement, modulus)
            inverse_at_K = compose_mod(inverse, K, modulus)
            self.assert_mod_zero(inverse_at_K - h - displacement, modulus)

            U = correction_from_inverse(Q, inverse, modulus)
            numerator = mod_x_polynomial(
                F - compose_mod(Q, K, modulus)
                + lam * compose_mod(U, K, modulus), modulus
            )
            divided_x, remainder = sp.div(numerator, x**e, x)
            self.assert_zero(remainder)
            actual_first = mod_x_polynomial(divided_x * (1 - x), x**2)
            self.assert_zero(actual_first - expected_first)

    def test_repeated_root_crt_and_full_overlap(self):
        e = 2
        u = (x - 1)**2
        p = x**e * u
        marked = x**(e + 2)
        complete_modulus = marked * u
        Q = T + x * T**2
        G = two_thirds * x * (1 - x) * T
        _, marked_inverse = finite_curve_inverse(Q, G, marked)
        _, other_inverse = finite_curve_inverse(Q, G, u)
        U_marked = correction_from_inverse(Q, marked_inverse, marked)
        U_other = correction_from_inverse(Q, other_inverse, u)
        idempotent_marked = u * sp.invert(u, marked, x)
        idempotent_other = marked * sp.invert(marked, u, x)
        self.assert_mod_zero(idempotent_marked - 1, marked)
        self.assert_mod_zero(idempotent_marked, u)
        self.assert_mod_zero(idempotent_other, marked)
        self.assert_mod_zero(idempotent_other - 1, u)
        U = mod_x_polynomial(
            U_marked * idempotent_marked + U_other * idempotent_other,
            complete_modulus,
        )
        self.assert_mod_zero(U - U_marked, marked)
        self.assert_mod_zero(U - U_other, u)
        F = mod_x_polynomial(p * b + Q.subs(T, h), complete_modulus)
        K = mod_x_polynomial(
            h + lam * compose_mod(G, F, complete_modulus), complete_modulus
        )
        numerator = mod_x_polynomial(
            F - compose_mod(Q, K, complete_modulus)
            + lam * compose_mod(U, K, complete_modulus),
            complete_modulus,
        )
        divided_p, remainder = sp.div(numerator, p, x)
        self.assert_zero(remainder)
        W_jet = mod_x_polynomial(divided_p, x**2)
        self.assert_zero(W_jet - b + two_thirds * x * lam * b)
        self.assert_mod_zero(K + (1 + lam * x)**2 * W_jet**2, x**2)

    def test_closed_family_global_forward_and_inverse_divisibility(self):
        independent_h, independent_I = sp.symbols("independent_h independent_I")
        for e in range(1, 6):
            p, time, Bn, Cn, W, K, Z = closed_family(e)
            matrix = sp.Matrix([[Bn, Cn], [time * p, 1 + time]])
            inverse_matrix = sp.Matrix([[1 + time, -Cn], [-time * p, Bn]])
            self.assertEqual(
                (matrix * inverse_matrix).applyfunc(sp.expand), sp.eye(2)
            )
            self.assertEqual(
                (inverse_matrix * matrix).applyfunc(sp.expand), sp.eye(2)
            )
            I = x**2 * z - (1 + lam * x)**2 * w**2
            inverse_b = sp.expand((1 + time) * w - Cn * I)
            inverse_h = sp.expand(-time * p * w + Bn * I)
            inverse_c, remainder = sp.div(inverse_h + inverse_b**2, x**2, x)
            self.assert_zero(remainder)
            self.assert_mod_zero(W - b + two_thirds * x * lam * b, x**2)
            self.assert_zero(x**2 * Z - (1 + lam * x)**2 * W**2 - K)

            # Both compositions are checked in the independent (b,h) plane;
            # the two physical x^2 divisibility checks recover c and z.
            forward_bh = matrix * sp.Matrix([b, independent_h])
            back_bh = inverse_matrix * forward_bh
            self.assertEqual(
                back_bh.applyfunc(sp.expand), sp.Matrix([b, independent_h])
            )
            backward_bh = inverse_matrix * sp.Matrix([w, independent_I])
            back_wI = matrix * backward_bh
            self.assertEqual(
                back_wI.applyfunc(sp.expand), sp.Matrix([w, independent_I])
            )
            self.assert_zero(inverse_c.subs(lam, 0) - z)

    def test_actual_physical_action_and_normalization(self):
        for e in (1, 2, 4):
            p, time, Bn, Cn, W, K, Z = closed_family(e)
            F = p * b + h
            Lb, Lc = sp.diff(F, c), -sp.diff(F, b)
            D_b = x**2 + lam * two_thirds * x * Lb
            D_c = 2 * b + lam * two_thirds * x * Lc

            def action(value):
                return sp.expand(D_b * sp.diff(value, b)
                                 + D_c * sp.diff(value, c))

            self.assert_zero(action(W) - x**2)
            self.assert_zero(action(K))
            self.assert_zero(action(F) - x**2 * p)
            self.assert_zero(action(Z) - 2 * (1 + lam * x)**2 * W)
            self.assert_zero(W.subs(lam, 0) - b)
            self.assert_zero(Z.subs(lam, 0) - c)
            self.assert_zero(Lb.subs({x: 0, b: 0}))
            self.assert_zero(Lc.subs({x: 0, b: 0}))
            self.assertNotEqual(sp.expand(two_thirds * x * Lc), 0)

    def test_every_prescribed_p_example_and_forced_top_jet(self):
        u = (x - 1)**2 * (x + 2)**3
        radical_u = (x - 1) * (x + 2)
        g = sp.expand(two_thirds * x * radical_u / radical_u.subs(x, 0))
        for e in (1, 3):
            p = x**e * u
            F = p * b + h
            Lb, Lc = sp.diff(F, c), -sp.diff(F, b)
            self.assertEqual(sp.gcd(Lb, Lc), 1)
            self.assert_zero(sp.rem(g, x * radical_u, x))
            self.assert_zero(sp.Poly(g, x).coeff_monomial(x) - two_thirds)
            self.assert_mod_zero(g * Lb, x**2)
            self.assert_mod_zero(g * Lc - sp.Rational(4, 3) * x * b, x**2)
            self.assert_zero(Lb.subs({x: 0, b: 0}))
            self.assert_zero(Lc.subs({x: 0, b: 0}))

    def test_wrong_slope_and_nonlinear_boundary_cannot_be_odd_repaired(self):
        arbitrary_correction = lam**2 + (1 + lam) * T + T**3
        cases = [(T, T), (T + T**2, two_thirds * T),
                 (2 + 3 * T, sp.Rational(2, 9) * T + T**2 / 2)]
        for Q0, G1 in cases:
            H = sp.expand(G1.subs(T, Q0))
            even_obstruction = sp.expand(H + 2 * T * sp.diff(H, T) - 2 * T)
            self.assertGreater(sp.degree(even_obstruction, T), 0)
            boundary = even_obstruction.subs(T, -b**2)
            with_correction = boundary + 2 * b * arbitrary_correction.subs(T, -b**2)
            self.assert_zero(
                (with_correction + with_correction.subs(b, -b)) / 2 - boundary
            )


if __name__ == "__main__":
    unittest.main()

