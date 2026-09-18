"""Finite exact controls for common Gauss valuations and residue recovery145.

Two methods use actual inverse-verified families. A third uses both
active branches of the explicitly nonactual base-flip family. The fourth
checks Laurent integrality of actual129 invariant polynomials and a
deliberately noninjective ring specialization with algebraic residue.
Finite rational valuations and truncated algebraic Taylor jets do not
prove universal Gauss embedding, coefficient recovery, or activity of
every actual factor. In particular a valuation-zero rational expression
need not be constant, and a ring specialization need not extend to fields.
No previous checker or solver is imported.
"""

import unittest

import sympy as sp


class CommonGaussValuationControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def order_and_leading(self, expression, epsilon):
        expression = sp.cancel(expression)
        if expression == 0:
            return None, sp.S.Zero
        numerator, denominator = sp.fraction(expression)
        top = sp.Poly(numerator, epsilon)
        bottom = sp.Poly(denominator, epsilon)
        top_order = min(power[0] for power, coefficient in top.terms() if coefficient != 0)
        bottom_order = min(power[0] for power, coefficient in bottom.terms() if coefficient != 0)
        leading = sp.cancel(top.nth(top_order) / bottom.nth(bottom_order))
        return top_order - bottom_order, leading

    def delta(self, F, variable, speed, initial, time):
        return sp.expand(sum((coefficient * sp.binomial(degree, index)
                              * initial ** (degree - index) * speed**index
                              * time ** (index - 1)
                              for (degree,), coefficient in sp.Poly(F, variable).terms()
                              for index in range(1, degree + 1)), sp.S.Zero))

    def test_actual_sharp_family_has_full_invariant_residues(self):
        u, a, b, v, t, eps = sp.symbols("u a b v t eps")
        x, y_target, z_target, w_target, A = sp.symbols("x y_target z_target w_target A")
        for degree in (3, 4):
            with self.subTest(degree=degree):
                F = t**degree / 2 + t + 2
                divided = self.delta(F, t, a, v, u)
                frame = (v + a * u, a - F.subs(t, v) + (b + 1) * u,
                         a - F.subs(t, v) + (b + 2) * u, b + divided)
                X, Y, Z, W = frame
                recovered_u = sp.cancel(Z - Y)
                recovered_a = sp.cancel(2 * Y - Z - (Z - Y) * W + F.subs(t, X))
                recovered_v = sp.cancel(X - recovered_a * recovered_u)
                recovered_b = sp.cancel(W - self.delta(F, t, recovered_a, recovered_v, recovered_u))
                for recovered, expected in zip((recovered_u, recovered_a, recovered_b, recovered_v),
                                                (u, a, b, v)):
                    self.zero(recovered - expected)

                # Independent-A reverse composition has only the monic
                # recovery residual; no inverse is inferred from a Jacobian.
                inv_u = z_target - y_target
                inv_v = x - A * inv_u
                inv_b = w_target - self.delta(F, t, A, inv_v, inv_u)
                reverse = (inv_v + A * inv_u,
                           A - F.subs(t, inv_v) + (inv_b + 1) * inv_u,
                           A - F.subs(t, inv_v) + (inv_b + 2) * inv_u,
                           inv_b + self.delta(F, t, A, inv_v, inv_u))
                a_identity = A - (2 * y_target - z_target - inv_u * w_target + F.subs(t, x))
                for value, target, error in zip(reverse, (x, y_target, z_target, w_target),
                                                (0, a_identity, a_identity, 0)):
                    self.zero(value - target - error)

                y = a - F.subs(t, v) - (b + 1) * v / a
                z = a - F.subs(t, v) - (b + 2) * v / a
                tau, rho = (b + 1) / a, (b + 2) / a
                tau_hat, rho_hat = tau + y * eps, rho + z * eps
                a_hat = sp.cancel(1 / (rho_hat - tau_hat))
                b_hat = sp.cancel((2 * tau_hat - rho_hat) / (rho_hat - tau_hat))
                coefficient_poly = sp.Poly(F, t)
                f = [b + coefficient_poly.nth(1) * a]
                f.extend(coefficient_poly.nth(j + 1) * a for j in range(1, degree))
                fminus = a * (coefficient_poly.nth(0) - a)
                S = sum((eps**(-j) * value.subs({a: a_hat, b: b_hat}, simultaneous=True)
                         for j, value in enumerate(f)), sp.S.Zero)
                S += eps * fminus.subs(a, a_hat)
                time_at_infinity = (1 / eps - v) / a
                W_at_infinity = sp.cancel(W.subs(u, time_at_infinity))
                zeta = sp.cancel((W_at_infinity - S) / eps**2)
                order, residue = self.order_and_leading(zeta, eps)
                self.assertEqual(order, 0)
                self.zero(residue - a**2 * v)

                # These are actual polynomial target expressions for all
                # three source invariants, not just initial source formulas.
                actual_a = 2 * y_target - z_target - (z_target - y_target) * w_target + F.subs(t, x)
                target_at_infinity = {symbol: sp.cancel(value.subs(u, time_at_infinity))
                                      for symbol, value in zip((x, y_target, z_target, w_target), frame)}
                a_at_infinity = sp.cancel(actual_a.subs(target_at_infinity, simultaneous=True))
                u_at_infinity = sp.cancel(target_at_infinity[z_target] - target_at_infinity[y_target])
                v_at_infinity = sp.cancel(target_at_infinity[x] - a_at_infinity * u_at_infinity)
                b_at_infinity = sp.cancel(target_at_infinity[w_target]
                                          - self.delta(F, t, a_at_infinity, v_at_infinity, u_at_infinity))
                for evaluated, expected in ((a_at_infinity, a), (b_at_infinity, b), (v_at_infinity, v)):
                    self.zero(evaluated - expected)
                    order, residue = self.order_and_leading(evaluated, eps)
                    self.assertEqual(order, 0)
                    self.zero(residue - expected)
                self.zero(f[-1] / coefficient_poly.nth(degree) - a)
                self.zero(f[0] - coefficient_poly.nth(1) * a - b)
                # These exact formulas recover L=C(a,b) from its tail field.

    def test_actual_finite_covers_recover_the_missing_coefficient(self):
        u, a, b, v, eps = sp.symbols("u a b v eps")
        X, Y, Z, W = sp.symbols("X Y Z W")
        for n in (2, 3):
            with self.subTest(n=n):
                frame = (v + a**n * u, a + b * u, b + u, u)
                recovered_a = Y - (Z - W) * W
                inverse = (W, recovered_a, Z - W, X - recovered_a**n * W)
                for value, expected in zip(inverse, (u, a, b, v)):
                    self.zero(value.subs(dict(zip((X, Y, Z, W), frame)), simultaneous=True) - expected)
                for value, expected in zip(frame, (X, Y, Z, W)):
                    self.zero(value.subs(dict(zip((u, a, b, v), inverse)), simultaneous=True) - expected)

                tau, rho = b / a**n, 1 / a**n
                y, z = a - b * v / a**n, b - v / a**n
                fminus = a**n * (a - b**2)
                self.zero(tau / rho - b)
                self.zero(rho * fminus + (tau / rho)**2 - a)
                # The all-n extension degree is proved by Eisenstein in140;
                # these finite controls do not establish unboundedness.
                self.zero(a**n - 1 / rho)
                self.assertGreater(sp.degree(fminus, a), n)

                tau_hat, rho_hat = tau + y * eps, rho + z * eps
                b_hat = sp.cancel(tau_hat / rho_hat)
                # A finite exact algebraic Taylor jet with the chosen
                # constant term a. No rationality of the full root is assumed.
                a_hat = a * sum((sp.binomial(-sp.Rational(1, n), j)
                                * (z * eps / rho)**j for j in range(4)), sp.S.Zero)
                algebraic_error = sp.expand(a_hat**n * rho_hat - 1)
                for j in range(4):
                    self.zero(algebraic_error.coeff(eps, j))
                fminus_hat = (a_hat - b_hat**2) / rho_hat
                W_at_infinity = (1 / eps - v) / a**n
                first_remainder = sp.cancel(W_at_infinity - rho_hat / eps + b_hat)
                order, leading = self.order_and_leading(first_remainder, eps)
                self.assertEqual(order, 1)
                self.zero(leading - fminus)
                zeta = sp.cancel((first_remainder - eps * fminus_hat) / eps**2)
                order, leading = self.order_and_leading(zeta, eps)
                self.assertEqual(order, 0)
                expected = (-a ** (n + 1) * v / n
                            + a ** (2 * n) * ((2 + sp.Rational(1, n)) * a * b - 2 * b**3))
                self.zero(leading - expected)
                self.zero(sp.diff(leading, v) + a ** (n + 1) / n)

                target_values = [sp.cancel(f.subs(u, (1 / eps - v) / a**n)) for f in frame]
                for polynomial, expected in zip(inverse[1:], (a, b, v)):
                    evaluated = sp.cancel(polynomial.subs(
                        dict(zip((X, Y, Z, W), target_values)), simultaneous=True))
                    order, residue = self.order_and_leading(evaluated, eps)
                    self.assertEqual(order, 0)
                    self.zero(evaluated - expected)
                    self.zero(residue - expected)

    def test_formal_active_branches_share_only_the_sampled_valuations(self):
        eps, a, rho, zeta, intrinsic = sp.symbols("eps a rho zeta intrinsic")
        x, y, z, w = sp.symbols("x y z w")
        center = -rho**2 / eps + eps * a**2
        abstract_target = {x: 1 / eps, y: a / eps, z: rho / eps,
                           w: center + eps**2 * zeta}
        Q = z**2 + x * w
        samples = (x, y, z, w, Q, y**2 - x**2 * Q, y / z, x / Q)
        for sign in (1, -1):
            with self.subTest(sign=sign):
                initial_y, initial_z = -intrinsic / (2 * a), sign * a
                branch_target = {x: 1 / eps, y: initial_y + a / eps,
                                 z: initial_z + rho / eps,
                                 w: -rho**2 / eps - 2 * rho * initial_z}
                a_hat, rho_hat = a + initial_y * eps, rho + initial_z * eps
                zeta_hat = intrinsic - initial_y**2 * eps
                coefficient_map = {a: a_hat, rho: rho_hat, zeta: zeta_hat}
                for target in (x, y, z, w):
                    self.zero(abstract_target[target].subs(coefficient_map, simultaneous=True)
                              - branch_target[target])
                for target_expression in samples:
                    abstract_value = sp.cancel(target_expression.subs(abstract_target, simultaneous=True))
                    branch_value = sp.cancel(target_expression.subs(branch_target, simultaneous=True))
                    abstract_order, abstract_leading = self.order_and_leading(abstract_value, eps)
                    branch_order, branch_leading = self.order_and_leading(branch_value, eps)
                    self.assertEqual(branch_order, abstract_order)
                    self.zero(branch_leading - abstract_leading.subs(zeta, intrinsic))

                # Initial source z is an invariant coefficient, but target z
                # is not a global invariant polynomial: its X-degree is1.
                self.zero(initial_z - sign * a)
                self.assertEqual(self.order_and_leading(branch_target[z], eps)[0], -1)
                self.assertEqual(self.order_and_leading(sign * a, eps)[0], 0)
                # A zero valuation is not enough for rational expressions.
                rational_ratio = sp.cancel(branch_target[y] / branch_target[x])
                self.assertEqual(self.order_and_leading(rational_ratio, eps)[0], 0)
                self.zero(rational_ratio - a - initial_y * eps)
                self.assertNotEqual(sp.diff(rational_ratio, eps), 0)
                self.zero(branch_target[z]**2 + branch_target[x] * branch_target[w] - a**2)

    def test_actual_invariant_laurent_integrality_and_ring_only_specialization(self):
        u, a, b, v, eps, zeta, t = sp.symbols("u a b v eps zeta t")
        x, y, z, w = sp.symbols("x y z w")
        F = t**3 / 2
        frame = (u, v + a * u, a - v**3 / 2 + b * u,
                 b + self.delta(F, t, a, v, u))
        A = z - x * w + y**3 / 2
        V = y - A * x
        B = w - self.delta(F, t, A, V, x)
        inverse = (x, A, B, V)
        for value, expected in zip(inverse, (u, a, b, v)):
            self.zero(value.subs(dict(zip((x, y, z, w), frame)), simultaneous=True) - expected)
        for value, expected in zip(frame, (x, y, z, w)):
            self.zero(value.subs(dict(zip((u, a, b, v), inverse)), simultaneous=True) - expected)
        for value in frame[:3]:
            self.zero(sp.diff(value, u, 2))
        self.zero(sp.diff(frame[3], u, 2) - a**3)

        # Here f2=a^3/2, f1=0, f0=b, fminus=-a. Independently
        # substitute the actual inverse, before using the claimed integral forms.
        target = {x: 1 / eps, y: a / eps, z: b / eps,
                  w: a**3 / (2 * eps**2) + b - a * eps + eps**2 * zeta}
        integral_forms = (a - eps * zeta,
                          b + eps * (zeta**3 / 2 - a) + eps**2 * zeta,
                          zeta)
        for polynomial, integral, residue in zip((A, B, V), integral_forms, (a, b, zeta)):
            evaluated = sp.cancel(polynomial.subs(target, simultaneous=True))
            self.zero(evaluated - integral)
            self.zero(evaluated.subs(eps, 0) - residue)
            sp.Poly(evaluated, eps, zeta)  # No negative powers or zeta denominators.
            self.assertEqual(self.order_and_leading(evaluated, eps)[0], 0)

        # The selected Taylor map gives the actual frame at X=infinity.
        # These identities also verify the chosen signs in the finite center.
        selected_map = {a: a + v * eps, b: b + (a - v**3 / 2) * eps, zeta: v}
        for symbol, actual in zip((x, y, z, w), frame):
            self.zero(target[symbol].subs(selected_map, simultaneous=True) - actual.subs(u, 1 / eps))
        for integral, actual in zip(integral_forms, (a, b, v)):
            self.zero(integral.subs(selected_map, simultaneous=True) - actual)

        # Additional actual invariant expressions test closure under products.
        for polynomial, expected in ((A**2 + B * V, integral_forms[0]**2 + integral_forms[1] * zeta),
                                     (A * V**2 + B**2, integral_forms[0] * zeta**2 + integral_forms[1]**2)):
            evaluated = sp.cancel(polynomial.subs(target, simultaneous=True))
            self.zero(evaluated - expected)
            sp.Poly(evaluated, eps, zeta)

        # This is ONLY a ring-specialization boundary. It is not an inactive
        # factor of the actual cubic fixture, nor an actual coordinate frame.
        # The nonzero kernel prevents extension to a rational field embedding.
        kernel_element = zeta - a
        self.assertNotEqual(kernel_element, 0)
        self.assertEqual(kernel_element.subs(zeta, a), 0)
        self.assertEqual(self.order_and_leading(kernel_element, eps)[0], 0)
        for integral, residue in zip(integral_forms, (a, b, a)):
            specialized = sp.expand(integral.subs(zeta, a))
            sp.Poly(specialized, eps)
            self.zero(specialized.subs(eps, 0) - residue)


if __name__ == "__main__":
    unittest.main()
