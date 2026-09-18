"""Finite exact controls for the two-recovery construction144.

Every sampled tuple is an actual polynomial automorphism by independently
checked staged inverse identities. Most samples intentionally fail the
three-good differential profile. The all-polynomial exclusion is proved
in the companion note, not inferred from this finite grid or a Jacobian.
No prior checker is imported. Do not execute before source review.
"""

import unittest

import sympy as sp


class TwoRecoveryCouplingControls(unittest.TestCase):
    def setUp(self):
        self.u, self.y, self.a, self.b, self.v = sp.symbols("u y a b v")
        self.A, self.z, self.w = sp.symbols("A z w")

    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def delta(self, F, speed, initial_y):
        result = sp.S.Zero
        for (degree,), coefficient in sp.Poly(F, self.y).terms():
            for index in range(1, degree + 1):
                result += (coefficient * sp.binomial(degree, index)
                           * initial_y ** (degree - index) * speed**index
                           * self.u ** (index - 1))
        return sp.expand(result)

    def action(self, expression, P):
        return sp.diff(expression, self.u) + P * sp.diff(expression, self.y)

    def actual_frame_and_inverse(self, H, Psi, F, P):
        u, y, a, b, v, A, z, w = (
            self.u, self.y, self.a, self.b, self.v, self.A, self.z, self.w)
        mid = a + b * H
        last = b + Psi.subs(A, mid)
        good = mid - F + u * last

        # The separate change from invariants to (u,y,a,b) is invertible.
        original_y = v + P * u
        recovered_v = y - P * u
        self.zero(original_y.subs(v, recovered_v) - y)
        self.zero(recovered_v.subs(y, original_y) - v)

        # Forward then inverse, simplifying each independent shear identity.
        recovered_A = sp.cancel(good + F - u * last)
        recovered_b = sp.cancel(last - Psi.subs(A, recovered_A))
        recovered_a = sp.cancel(recovered_A - recovered_b * H)
        self.zero(recovered_A - mid)
        self.zero(recovered_b - b)
        self.zero(recovered_a - a)

        # Reverse order in independent target variables z,w. No root equation
        # or extra coefficient compatibility is assumed in this inverse.
        inverse_A = z + F - u * w
        inverse_b = w - Psi.subs(A, inverse_A)
        inverse_a = inverse_A - inverse_b * H
        returned_A = sp.cancel(inverse_a + inverse_b * H)
        returned_W = sp.cancel(inverse_b + Psi.subs(A, returned_A))
        returned_Z = sp.cancel(returned_A - F + u * returned_W)
        self.zero(returned_A - inverse_A)
        self.zero(returned_W - w)
        self.zero(returned_Z - z)
        self.zero(sp.Matrix((good, last)).jacobian((a, b)).det() - 1)
        return sp.expand(good), sp.expand(last)

    def test_actual_coupled_automorphisms_fail_the_good_profile(self):
        u, y, a, A = self.u, self.y, self.a, self.A
        Psi = A**2 + u * y * A + y**3
        for P in (a, a**2 + a + 1):
            for F in (y**2 + y, y**3 + y + 2):
                for H in (sp.S.One, u + y):
                    with self.subTest(P=P, F=F, H=H):
                        good, last = self.actual_frame_and_inverse(H, Psi, F, P)
                        self.zero(self.action(self.action(u, P), P))
                        self.zero(self.action(self.action(y, P), P))
                        defect = sp.expand(self.action(self.action(good, P), P))
                        self.assertNotEqual(defect, 0)
                        # The failure is differential, not a failed inverse.
                        self.assertGreaterEqual(sp.Poly(last, u, y, a, self.b).total_degree(), 2)

    def test_zero_coupling_has_exact_all_degree_survivors(self):
        u, y, a, v, A, b = self.u, self.y, self.a, self.v, self.A, self.b
        for P in (a, a**2 + a + 1):
            for F in (y**3 / 2 + y + 2, y**4 + y**2 - y):
                with self.subTest(P=P, F=F):
                    PA = P.subs(a, A)
                    initial = y - PA * u
                    invariant_addition = A * initial + initial**2
                    Psi = self.delta(F, PA, initial) + invariant_addition
                    good, last = self.actual_frame_and_inverse(sp.S.Zero, Psi, F, P)
                    self.zero(self.action(self.action(good, P), P))
                    original_y = v + P * u
                    G = a * v + v**2
                    self.zero(good.subs(y, original_y) - a
                              + F.subs(y, v) - u * (b + G))
                    last_in_invariants = sp.expand(last.subs(y, original_y))
                    self.zero(last_in_invariants - b - G - self.delta(F, P, v))
                    self.assertEqual(sp.degree(last_in_invariants, u), sp.degree(F, y) - 1)
                    initial_G = Psi.subs({u: 0, A: a}, simultaneous=True) - P * sp.diff(F, y)
                    self.zero(initial_G - a * y - y**2)

    def test_coefficient_separation_and_hypothesis_boundaries(self):
        u, y, a, A = self.u, self.y, self.a, self.A
        M = sp.Function("M")(u, y)
        R = sp.Function("R")(u, y)
        P = a**2 + a + 1
        expanded_action = sp.expand(self.action(self.action(a * M + R, P), P))
        expected = (a * sp.diff(M, u, 2) + 2 * a * P * sp.diff(M, u, y)
                    + a * P**2 * sp.diff(M, y, 2) + sp.diff(R, u, 2)
                    + 2 * P * sp.diff(R, u, y) + P**2 * sp.diff(R, y, 2))
        self.zero(expanded_action - expected)
        coefficients = sp.Poly(expanded_action, a)
        self.zero(coefficients.nth(5) - sp.diff(M, y, 2))
        self.zero(coefficients.nth(4).subs(sp.diff(M, y, 2), 0) - sp.diff(R, y, 2))

        gamma, kappa, q1, q0, f1, f0 = sp.symbols("gamma kappa q1 q0 f1 f0", nonzero=True)
        reduced_M = 1 + kappa * u - q1 * u**2 + gamma * u * y
        reduced_R = u * (q1 * y + q0) - gamma * y**2 - f1 * y - f0
        self.zero(self.action(self.action(a * reduced_M + reduced_R, a), a))
        for H in (sp.S.One, u + y):
            defect = self.action(self.action(H * reduced_M + u, a), a)
            self.assertNotEqual(sp.expand(defect), 0)

        # Removing nonconstancy of P permits a nonzero invariant H.
        F = y**3 + y
        constant_speed = sp.Integer(2)
        H = y - constant_speed * u
        Psi = self.delta(F, constant_speed, H)
        good, _ = self.actual_frame_and_inverse(H, Psi, F, constant_speed)
        self.zero(self.action(self.action(good, constant_speed), constant_speed))

        # Removing nonlinearity of F permits H=1 even at dense speed rank2.
        affine_F = 3 * y + 1
        good, _ = self.actual_frame_and_inverse(sp.S.One, sp.S.Zero, affine_F, P)
        self.zero(self.action(self.action(good, P), P))
        third_speed = self.b - 3 * P
        self.zero(sp.Matrix((P, third_speed)).jacobian((a, self.b)).det() - sp.diff(P, a))


if __name__ == "__main__":
    unittest.main()

