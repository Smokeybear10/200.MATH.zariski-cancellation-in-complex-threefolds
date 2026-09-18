"""Formal coefficient controls for the actual cubic graph proof.

Arbitrary rational scalar functions are represented by symbolic functions.
This does not assert that these formal graphs generate an actual frame;
the written proof separately establishes the graph and determinant gates.
"""

import unittest

import sympy as sp


class ConstantCubicGraphChecks(unittest.TestCase):
    def same(self, left, right):
        self.assertEqual(sp.simplify(sp.expand(left - right).doit()), 0)

    def test_three_exact_determinant_coefficients_and_coordinate_slice(self):
        t, f, X, Y = sp.symbols("t f X Y")
        F, U, G, k, ell, m, n = [
            sp.Function(name)(t) for name in ("F", "U", "G", "k", "ell", "m", "n")
        ]
        gp = sp.diff(G, t)
        a = sp.diff(F, t) / (2 * gp)
        C = sp.diff(U, t) / (2 * gp)
        d = a * G - F
        b = U - C * G
        x, y = X - f**2 / 2, Y - G * f
        Q1 = (
            f**3 / 6 - F * f**2 / 2
            + (x / 2 - a * y + k) * f
            + d * x - sp.diff(a, t) * y**2 / (2 * gp)
            + sp.diff(k, t) * y / gp + m
        )
        Q2 = (
            U * f**2 / 2 + (C * y + ell) * f
            + b * x + sp.diff(C, t) * y**2 / (2 * gp)
            + sp.diff(ell, t) * y / gp + n
        )

        def determinant(second):
            return sp.expand(sp.diff(Q1, t) * sp.diff(second, f) - sp.diff(Q1, f) * sp.diff(second, t))

        self.same(determinant(Q2).coeff(X, 2), -sp.diff(b, t) / 2)

        b0, kappa, a2, ell0, n0 = sp.symbols("b0 kappa a2 ell0 n0")
        U0 = b0 + kappa * G**2
        substitution = {sp.diff(U, t, order): sp.diff(U0, t, order) for order in range(4)}
        reduced_Q2 = (
            b0 * X + kappa * Y**2 / 2 + sp.diff(ell, t) * Y / gp
            + (ell - G * sp.diff(ell, t) / gp) * f + n
        )
        self.same(Q2.subs(substitution).doit(), reduced_Q2)
        self.same(
            determinant(reduced_Q2).coeff(X, 1).coeff(Y, 1),
            -sp.diff(sp.diff(ell, t) / gp, t) / 2,
        )

        ell_value = a2 * G + ell0
        ell_substitution = {
            sp.diff(ell, t, order): sp.diff(ell_value, t, order) for order in range(3)
        }
        final_Q2 = b0 * X + kappa * Y**2 / 2 + a2 * Y + ell0 * f + n
        self.same(reduced_Q2.subs(ell_substitution).doit(), final_Q2)
        final_det = determinant(final_Q2)
        self.same(final_det, ell0 * sp.diff(Q1, t) - sp.diff(n, t) * sp.diff(Q1, f))
        self.same(final_det.coeff(X, 1), ell0 * sp.diff(d, t) - sp.diff(n, t) / 2)

        # Under the written constant-determinant argument, n=2*ell0*d+n0.
        n_value = 2 * ell0 * d + n0
        normalized = final_Q2.subs(n, n_value)
        self.same(
            normalized - b0 * X - kappa * Y**2 / 2 - a2 * Y - n0,
            ell0 * (f + 2 * d),
        )
        self.same(sp.diff(f + 2 * d, f), 1)
        # ell0=0 would kill the entire second base row, not yield a unit determinant.
        zero_case = normalized.subs(ell0, 0)
        self.same(sp.diff(zero_case, t), 0)
        self.same(sp.diff(zero_case, f), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
