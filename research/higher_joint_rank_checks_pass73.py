"""Three bounded exact controls for the full six-dimensional transfer.

The companion and derivative tables are formal algebra with two separate
defect directions. The polynomial coordinate maps have actual inverses.
None of these controls constructs an original moving full-frame action
or computationally establishes the written recognition theorem.
"""

import unittest

import sympy as sp


class HigherJointRankChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_jordan_partitions_and_full_two_row_images(self):
        def partitions(total, largest):
            if total == 0:
                yield ()
            else:
                for first in range(min(total, largest), 0, -1):
                    for tail in partitions(total - first, first):
                        yield (first,) + tail

        def jordan(parts):
            matrix = sp.zeros(sum(parts))
            offset = 0
            for size in parts:
                for row in range(offset, offset + size - 1):
                    matrix[row, row + 1] = 1
                offset += size
            return matrix

        all_parts = tuple(partitions(6, 6))
        self.assertEqual(len(all_parts), 11)
        for m in (4, 5):
            candidates = tuple(part for part in all_parts if part[0] == m)
            self.assertEqual(candidates, ((4, 2), (4, 1, 1)) if m == 4 else ((5, 1),))
            actual_rank_candidates = []
            for part in candidates:
                matrix = jordan(part)
                self.assert_zero(matrix**m)
                self.assertEqual((matrix**(m - 1)).rank(), 1)
                self.assertEqual((matrix**(m - 2)).rank(), 2)
                if m == 5:
                    self.assertEqual((matrix**2).rank(), 3)
                if matrix.rank() >= 4:
                    actual_rank_candidates.append(part)
            self.assertEqual(actual_rank_candidates, [(4, 2)] if m == 4 else [(5, 1)])

        sigma, tau, mu1, nu1, nu2 = sp.symbols("sigma tau mu1 nu1 nu2")
        mu2 = sp.Symbol("mu2", nonzero=True)
        e0, e1, v00, v01 = sp.symbols("e0 e1 v00 v01")
        c, e = sp.Matrix([1, 0, 0, 0]), sp.Matrix([e0, e1, 1, 0])
        v0 = sp.Matrix([v00, v01, mu1, mu2])
        ell, mu = sp.Matrix([1, 0]), sp.Matrix([mu1, mu2])
        nu = nu1 * ell + nu2 * mu
        for m in (4, 5):
            top = c.col_join((m - 1) * ell)
            previous = (c * sigma + e).col_join((m - 2) * (ell * sigma + mu))
            first = previous - sigma * top
            self.assert_zero(first - e.col_join((m - 2) * mu - sigma * ell))
            full_pair = sp.Matrix.hstack(top, first)
            self.assertEqual(full_pair.shape, (6, 2))
            self.assertEqual(full_pair.rank(), 2)
            layer = ell * (sp.Rational(m - 1, m - 2) * tau
                           - sigma**2 / (2 * (m - 2))) + mu * sigma + nu
            # The two auxiliary rows, not a scalar contraction, give
            # the differential of the entire preceding bad pair.
            for parameter in (sigma, tau):
                column = (c * sp.diff(tau, parameter) + e * sp.diff(sigma, parameter)).col_join(
                    (m - 2) * layer.diff(parameter))
                self.assert_zero(column - top * sp.diff(tau, parameter)
                                 - first * sp.diff(sigma, parameter))
            if m == 5:
                second_velocity = (c * tau + e * sigma + v0).col_join(2 * layer)
                second = second_velocity - tau * top - sigma * first
                expected_bottom = 2 * layer - 4 * tau * ell - sigma * (3 * mu - sigma * ell)
                self.assert_zero(second - v0.col_join(expected_bottom))
                full_triple = sp.Matrix.hstack(top, first, second)
                self.assertEqual(full_triple.shape, (6, 3))
                self.assert_zero(full_triple.extract([0, 2, 3], [0, 1, 2]).det() - mu2)
                self.assertEqual(full_triple.rank(), 3)
                dual = sp.Matrix.hstack(c, e, v0, sp.Matrix([0, 1, 0, 0])).inv()[3, :]
                self.assert_zero(dual * full_triple[:4, :])

    def test_two_independent_defect_coefficient_cancellations(self):
        sigma, u0, nu1, nu2 = sp.symbols("sigma u0 nu1 nu2")
        # Free coefficient directions. In particular DL and DM are
        # never identified or replaced by a single defect line.
        C, E0, DL, DM = (sp.eye(4)[:, index] for index in range(4))
        self.assertEqual(sp.Matrix.hstack(DL, DM).rank(), 2)
        tau = u0 + sigma**2 / 2
        for m in (4, 5):
            Jc = sp.Rational(m - 1, 2) * DL
            Je = C / (m - 1) - sigma * DL / 2 + sp.Rational(m - 2, 2) * DM
            Jv = (C * sigma / ((m - 1) * (m - 2)) + E0 / (m - 2)
                  - sp.Rational(m - 1, 2 * (m - 2)) * u0 * DL
                  - sigma * DM / 2 + sp.Rational(m - 3, 2) * (nu1 * DL + nu2 * DM))
            bad_layer = (DL * (sp.Rational(m - 1, m - 2) * tau
                              - sigma**2 / (2 * (m - 2)))
                         + DM * sigma + nu1 * DL + nu2 * DM)
            self.assert_zero(Jc * tau + Je * sigma + Jv
                             - sp.Rational(m - 3, 2) * bad_layer - (C * sigma + E0) / (m - 2))
            beta = (sigma - (m - 3) * nu2) / (m - 2)
            gamma = ((sigma**2 - (m - 3) * nu2 * sigma) / ((m - 1) * (m - 2))
                     + u0 / (m - 2) - sp.Rational(m - 3, m - 1) * nu1)
            bracket = -Jv - beta * Je - gamma * Jc + sp.diff(beta, sigma) * E0 + sp.diff(gamma, sigma) * C
            self.assert_zero(bracket)
            self.assert_zero(sp.diff(beta, sigma, m - 1))
            self.assert_zero(sp.diff(gamma, sigma, m - 1))
            s_u0 = sp.diff(gamma, sigma, m - 2)
            self.assert_zero(s_u0 - (sp.Rational(1, 3) if m == 4 else 0))
            second_iterate = s_u0 * sp.diff(gamma, u0) * C
            self.assert_zero(second_iterate - (C / 6 if m == 4 else sp.zeros(4, 1)))
            self.assert_zero(s_u0 * second_iterate.diff(u0))

    def test_actual_coordinate_changes_and_polynomial_clearing(self):
        q1, q2, X, Y = sp.symbols("q1 q2 X Y")
        a0, b, z, w = sp.symbols("a0 b z w")
        a, B, Z, W = sp.symbols("a B Z W")
        e0, e1, v00, v01, mu1 = sp.symbols("e0 e1 v00 v01 mu1")
        mu2 = sp.Symbol("mu2", nonzero=True)
        c, e = sp.Matrix([1, 0, 0, 0]), sp.Matrix([e0, e1, 1, 0])
        v0, c2 = sp.Matrix([v00, v01, mu1, mu2]), sp.Matrix([0, 1, 0, 0])
        constant_basis = sp.Matrix.hstack(c, e, v0, c2)
        original, dual = sp.Matrix([q1, q2, X, Y]), sp.Matrix([a0, b, z, w])
        dual_map, original_inverse = constant_basis.inv() * original, constant_basis * dual
        self.assert_zero(dual_map.subs(dict(zip(original, original_inverse)), simultaneous=True) - dual)
        self.assert_zero(original_inverse.subs(dict(zip(dual, dual_map)), simultaneous=True) - original)
        self.assert_zero(dual_map[1] - X + mu1 * Y / mu2)
        self.assert_zero(dual_map[2] - Y / mu2)
        self.assert_zero(original_inverse.jacobian(dual)[:, 0] - c)
        self.assert_zero(original_inverse.jacobian(dual)[:, 3] - c2)

        sigma, u0, nu1, nu2, g = sp.symbols("sigma u0 nu1 nu2 g")
        new = sp.Matrix([a, B, Z, W])
        for m in (4, 5):
            beta = (sigma - (m - 3) * nu2) / (m - 2)
            gamma = ((sigma**2 - (m - 3) * nu2 * sigma) / ((m - 1) * (m - 2))
                     + u0 / (m - 2) - sp.Rational(m - 3, m - 1) * nu1)
            correction = -z**2 / 12 + nu2 * b / 3 if m == 4 else -nu2 * b / 2
            forward = sp.Matrix([a0 + correction, b, z, w])
            inverse = sp.Matrix([a - correction.subs({b: B, z: Z}), B, Z, W])
            self.assert_zero(forward.subs(dict(zip(dual, inverse)), simultaneous=True) - new)
            self.assert_zero(inverse.subs(dict(zip(new, forward)), simultaneous=True) - dual)
            jacobian = forward.jacobian(dual)
            transported = inverse.jacobian(new).subs(dict(zip(new, forward)), simultaneous=True)
            self.assert_zero(jacobian * transported - sp.eye(4))
            self.assert_zero(transported * jacobian - sp.eye(4))
            self.assertEqual(jacobian.det(), 1)
            self.assert_zero(transported[:, 0] - sp.eye(4)[:, 0])
            self.assert_zero(transported[:, 3] - sp.eye(4)[:, 3])
            kappa = (jacobian * sp.Matrix([gamma, beta, 1, 0]))[0]
            if m == 4:
                expected = sigma**2 / 6 + u0 / 2 - nu1 / 3 - z / 6 - nu2**2 / 6
                self.assert_zero(kappa - expected)
                self.assert_zero(sp.diff(kappa, z) + sp.diff(kappa, u0) / 3)
                delta_kappa = sp.diff(kappa, sigma) + (sigma + nu2) * sp.diff(kappa, z)
                self.assert_zero(delta_kappa - beta / 3)
                Ez = g * (sigma + nu2)
                Eb = g * (sigma**2 / 2 + 3 * u0 / 2 + nu1)
                N = (Ez - 2 * nu2 * g) / 2
                U = Eb - g * (z / 2 + 2 * nu1 + nu2**2 / 2)
                self.assert_zero(N - g * beta)
                self.assert_zero(U - 3 * g * kappa)
                self.assert_zero(g * sp.diff(N, sigma) - g**2 / 2)
                self.assert_zero(g * (sp.diff(U, sigma) + (sigma + nu2) * sp.diff(U, z)) - g * N)
                self.assert_zero(transported[:, 1] - sp.eye(4)[:, 1] + nu2 * sp.eye(4)[:, 0] / 3)
            else:
                self.assert_zero(kappa - gamma + nu2 * beta / 2)
                self.assert_zero(sp.diff(kappa, sigma) - beta / 2)
                E2z = g**2 * (sigma + nu2)
                E2b = g**2 * (sigma**2 / 2 + 4 * u0 / 3 + nu1)
                n = (E2z - 3 * nu2 * g**2) / 3
                Q = (g**2 * E2b / 4 - 3 * n**2 / 8 - 3 * nu2 * g**2 * n / 2
                     - (nu2**2 / 2 + 3 * nu1 / 4) * g**4)
                self.assert_zero(n - g**2 * beta)
                self.assert_zero(Q - g**4 * kappa)
                self.assert_zero(g * sp.diff(n, sigma) - g**3 / 3)
                self.assert_zero(g * sp.diff(Q, sigma) - g**3 * n / 2)
                self.assert_zero(transported[:, 1] - sp.eye(4)[:, 1] - nu2 * sp.eye(4)[:, 0] / 2)


if __name__ == "__main__":
    unittest.main()
