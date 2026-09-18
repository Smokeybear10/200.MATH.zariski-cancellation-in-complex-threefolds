"""Finite elimination identities for300, not a recognition proof.

No solver, saved checker, or project proof is imported.
"""

import unittest

import sympy as s


class PlaneDegreeRefinementControls(unittest.TestCase):
    def test_eliminant_expansion_and_ideal_membership(self):
        U, A1, A0, e, L1, L0 = s.symbols("U A1 A0 e L1 L0")
        H = U**2 + A1 * U + A0
        Q = e * U**2 + L1 * U + L0
        r, z = L1 - e * A1, L0 - e * A0
        R = z**2 - A1 * r * z + A0 * r**2
        expanded = (L0**2 - A1 * L1 * L0 + A0 * L1**2
                    + e * (A1**2 - 2 * A0) * L0
                    - e * A0 * A1 * L1 + e**2 * A0**2)
        self.assertEqual(s.expand(R - expanded), 0)
        self.assertEqual(s.expand(R - r**2 * H
                                 + (r * U + A1 * r - z) * (Q - e * H)), 0)
        self.assertEqual(s.expand(s.resultant(H, Q, U) - R), 0)

    def test_reducible_surface_gradient_chain_rule(self):
        U, P, V = s.symbols("U P V")
        A, B = P**2 + V, P + 1
        H = (U + A) * (U + B)
        Q = P**2 * U**2 + (P**3 + V) * U + V**4 - P
        q = s.expand(Q.subs(U, -A))
        self.assertLessEqual(s.Poly(q, P, V).total_degree(), 6)
        for z in (P, V):
            minor = s.diff(H, U) * s.diff(Q, z) - s.diff(H, z) * s.diff(Q, U)
            self.assertEqual(s.expand(minor.subs(U, -A) - (B - A) * s.diff(q, z)), 0)

    def test_constant_factor_difference_substitution_bound(self):
        U, P, V, eta = s.symbols("U P V eta")
        A, B = P + 2 * V, P + 2 * V + eta
        Q = P**2 * U**2 + (P**3 + V**3) * U + V**4 - P
        self.assertEqual(s.expand(B - A), eta)
        self.assertEqual(s.Poly(A * B, P, V).total_degree(), 2)
        self.assertLessEqual(s.Poly(Q.subs(U, -A), P, V).total_degree(), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
