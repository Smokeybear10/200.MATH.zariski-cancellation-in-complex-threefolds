"""Finite exact controls for the formal inverse-branch family of pass141.

Three fixed polynomials, including two nonmonomial examples, test polynomial
divided differences, both Jacobians, the selected rational derivation,
independently recovered Taylor tails and algebraic-branch reconstruction.
These tuples are deliberately NOT polynomial coordinate frames: their
original Jacobian is the nonunit F'(k), although the relative Jacobian is 1.
The reconstruction is rational after adjoining a root, not a polynomial
inverse. Finite arithmetic here does not prove the all-degree field-degree,
irreducibility, squarefreeness or shear-minimum statements of the proof.
No solver or previous checker is imported.
"""

import unittest

import sympy as sp


class FormalInverseBranchControls(unittest.TestCase):
    def setUp(self):
        self.X, self.k, self.rho, self.v = sp.symbols("X k rho v")
        self.t, self.U, self.V = sp.symbols("t U V")
        self.samples = (
            self.t**2 / 2,
            self.t**3 + self.t + 2,
            self.t**4 + self.t**2 + 3 * self.t - 1,
        )

    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def divided_difference(self, polynomial, base, step, parameter):
        """Binomial polynomial, with no division by the parameter."""
        result = sp.S.Zero
        for (degree,), coefficient in sp.Poly(polynomial, self.t).terms():
            for i in range(1, degree + 1):
                result += (
                    coefficient * sp.binomial(degree, i)
                    * base ** (degree - i) * step**i * parameter ** (i - 1)
                )
        return sp.expand(result)

    def fixture(self, polynomial):
        X, k, rho, v = self.X, self.k, self.rho, self.v
        tau = polynomial.subs(self.t, k)
        slope = sp.diff(tau, k)
        Y, Z = v + tau * X, k + rho * X
        W = self.divided_difference(polynomial, k, rho, X)

        def dt(expression):
            return sp.cancel(sp.diff(expression, k) / slope)

        def selected(expression):
            return sp.cancel(
                -X * sp.diff(expression, k) / slope
                + sp.diff(expression, rho) / slope
                + X**2 * sp.diff(expression, v)
            )

        def homogeneous(expression, order, first, second):
            result = sp.S.Zero
            for i in range(order + 1):
                term = sp.diff(expression, rho, order - i)
                for _ in range(i):
                    term = dt(term)
                result += term * first**i * second ** (order - i) / (
                    sp.factorial(i) * sp.factorial(order - i)
                )
            return sp.cancel(result)

        return tau, slope, Y, Z, W, dt, selected, homogeneous

    def test_polynomial_tuple_and_distinct_jacobians(self):
        X, k, rho, v = self.X, self.k, self.rho, self.v
        for polynomial in self.samples:
            with self.subTest(F=polynomial):
                tau, slope, Y, Z, W, dt, selected, _ = self.fixture(polynomial)
                degree = sp.degree(polynomial, self.t)
                leading = sp.Poly(polynomial, self.t).LC()
                self.zero(X * W - polynomial.subs(self.t, Z) + tau)
                self.assertEqual(sp.degree(W, X), degree - 1)
                self.zero(sp.Poly(W, X).LC() - leading * rho**degree)
                self.zero(W.subs(X, 0) - slope * rho)
                self.assertTrue(all(power[0] >= 0 for power, _ in sp.Poly(W, X).terms()))
                for value, target in zip((X, Y, Z, W), (0, 0, 0, 1)):
                    self.zero(selected(value) - target)
                self.zero(selected(rho) - 1 / slope)
                self.assertGreater(sp.degree(slope, k), 0)
                self.assertGreater(sp.degree(sp.denom(sp.cancel(selected(rho))), k), 0)
                self.zero(dt(tau) - 1)
                self.zero(dt(rho))

                relative = sp.Matrix([
                    [dt(value), sp.diff(value, rho), sp.diff(value, v)]
                    for value in (Y, Z, W)
                ])
                original = sp.Matrix((X, Y, Z, W)).jacobian((X, k, rho, v))
                self.zero(relative.det() - 1)
                self.zero(original.det() - slope)
                self.zero(original.det() - slope * relative.det())
                self.zero(selected(v) - X**2)
                self.zero(selected(k).coeff(X, 2))
                self.zero(selected(rho).coeff(X, 2))
                # The good-speed rank is two; this is not an inverse certificate.
                speed_jacobian = sp.Matrix((tau, rho)).jacobian((k, rho))
                self.zero(speed_jacobian.det() - slope)

    def test_independent_peeling_tails_and_residual_factor(self):
        X, k, rho, v, U, V = self.X, self.k, self.rho, self.v, self.U, self.V
        for polynomial in self.samples:
            with self.subTest(F=polynomial):
                tau, slope, Y, Z, W, dt, selected, H = self.fixture(polynomial)
                degree = int(sp.degree(polynomial, self.t))
                remaining = W
                coefficients = {}
                # Descending recovery, rather than inserting the proposed f_j.
                for j in range(degree - 1, -1, -1):
                    fj = sp.expand(remaining).coeff(X, j)
                    self.zero(sp.diff(fj, v))
                    coefficients[j] = fj
                    positive_part = sum(
                        (X ** (j - h) * H(fj, h, v, k) for h in range(j + 1)),
                        sp.S.Zero,
                    )
                    remaining = sp.cancel(remaining - positive_part)
                    expected = sp.Poly(polynomial, self.t).nth(j + 1) * rho ** (j + 1)
                    self.zero(fj - expected)
                self.zero(remaining)

                S = sum((
                    X**j * sum((H(fj, h, v, k) / X**h for h in range(j + 2)), sp.S.Zero)
                    for j, fj in coefficients.items()
                ), sp.S.Zero)
                self.zero(S - (polynomial.subs(self.t, Z) - polynomial.subs(self.t, 0)) / X)
                tail = sp.cancel(W - S)
                R1 = -sum((H(fj, j + 1, U, V) for j, fj in coefficients.items()), sp.S.Zero)
                fm1 = sp.cancel(R1.subs({U: v, V: k}, simultaneous=True))
                Phi = sp.cancel(R1 - fm1)
                Psi = -sum((H(fj, j + 2, U, V) for j, fj in coefficients.items()), sp.S.Zero)
                Psi = sp.cancel(Psi - H(fm1, 1, U, V))
                self.zero(R1 - polynomial.subs(self.t, 0) + polynomial.subs(self.t, V))
                self.zero(fm1 - polynomial.subs(self.t, 0) + tau)
                self.zero(tail - fm1 / X)
                self.zero(selected(tail) - 1)
                self.zero(H(fm1, 2, U, V))
                theta_fm1 = fm1 + H(fm1, 1, v, k) / X
                corrected_tail = sp.cancel(tail - theta_fm1 / X)
                self.zero(corrected_tail - v / X**2)
                self.zero(selected(corrected_tail) - 1)
                self.zero(Phi - tau + polynomial.subs(self.t, V))
                self.zero(Psi - U)
                self.zero(sp.diff(Psi, U) - dt(Phi))
                self.zero(sp.diff(Psi, V) - sp.diff(Phi, rho))

                quotient, remainder = sp.div(
                    polynomial.subs(self.t, V) - tau, V - k, V
                )
                self.zero(remainder)
                residual = -quotient
                self.zero(Phi - (V - k) * residual)
                self.zero(residual.subs(V, k) + slope)
                self.assertEqual(sp.degree(Phi, V), degree)
                self.assertEqual(sp.degree(residual, V), degree - 1)
                # A finite squarefreeness check, not the all-degree argument.
                finite_gcd = sp.gcd(
                    sp.Poly(Phi, V, domain=sp.QQ.frac_field(k)),
                    sp.Poly(sp.diff(Phi, V), V, domain=sp.QQ.frac_field(k)),
                )
                self.assertEqual(finite_gcd.degree(), 0)

    def test_algebraic_branch_reconstruction_and_finite_taylor_root(self):
        X, k, rho, v = self.X, self.k, self.rho, self.v
        x, y, z, w, branch, epsilon = sp.symbols("x y z w branch epsilon")
        for polynomial in self.samples:
            with self.subTest(F=polynomial):
                tau, slope, Y, Z, W, dt, selected, _ = self.fixture(polynomial)
                Q = polynomial.subs(self.t, z) - x * w
                root_residual = polynomial.subs(self.t, branch) - Q
                reconstruction = {
                    X: x, k: branch, rho: (z - branch) / x, v: y - x * Q,
                }
                reconstructed_forward = [
                    sp.cancel(value.subs(reconstruction, simultaneous=True))
                    for value in (X, Y, Z, W)
                ]
                # These vanish only after imposing F(branch)=Q. They are not
                # identities claiming a rational or polynomial inverse over M.
                for value, target, residual in zip(
                    reconstructed_forward,
                    (x, y, z, w),
                    (0, x * root_residual, 0, -root_residual / x),
                ):
                    self.zero(value - target - residual)
                forward = {x: X, y: Y, z: Z, w: W, branch: k}
                for value, target in zip(reconstruction.values(), (X, k, rho, v)):
                    self.zero(value.subs(forward, simultaneous=True) - target)
                self.zero(Q.subs(forward, simultaneous=True) - tau)
                self.assertEqual(sp.degree(root_residual, branch), sp.degree(polynomial, self.t))

                # Taylor-root identity modulo epsilon^4, not an infinite-series
                # proof. The nonmonomial cases genuinely use rational dt(k).
                theta_coefficients = [k]
                derivative = k
                for order in range(1, 4):
                    derivative = dt(derivative)
                    theta_coefficients.append(derivative * v**order / sp.factorial(order))
                # Truncated convolution avoids expanding unused high orders.
                powers = [sp.S.One, sp.S.Zero, sp.S.Zero, sp.S.Zero]
                root_coefficients = [sp.S.Zero] * 4
                for exponent in range(int(sp.degree(polynomial, self.t)) + 1):
                    coefficient = sp.Poly(polynomial, self.t).nth(exponent)
                    for order in range(4):
                        root_coefficients[order] += coefficient * powers[order]
                    powers = [sp.cancel(sum((
                        powers[i] * theta_coefficients[order - i]
                        for i in range(order + 1)
                    ), sp.S.Zero)) for order in range(4)]
                for order in range(4):
                    self.zero(root_coefficients[order] - (tau, v, 0, 0)[order])
                self.zero(selected(tau + v / X))
                self.zero(selected(rho + k / X))


if __name__ == "__main__":
    unittest.main()
