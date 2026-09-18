"""Exact controls for the explicit inverse-verified common-factor frame187.

Unlike formal coefficient examples, this source tests an actual polynomial
map by staged inverse identities in both orders. The written proof supplies
the full initial-kernel dimension/Gauss argument. These finite controls do
not assert a new recognition theorem, a globally minimal time profile, or
unrestricted cancellation. No older checker or solver internals are imported.
Authored source-only; Root owns canonical execution.
"""

import unittest

import sympy as sp


def source_polynomials(x, y, t, rho):
    w = t - y**4
    theta = y * w - 4 * t * y**3
    z0 = -t * w + 6 * t**2 * y**2 - y * theta
    sigma0 = 4 * t**3 * y - t * theta
    q = -t * rho + t**4
    Y = y + t * x
    Z0 = z0 + sigma0 * x + t**4 * x**2
    W0 = w + theta * x
    Z = z0 + rho + (sigma0 - rho * y) * x + q * x**2
    W = W0 + rho * x**2
    gamma = (1 + x * Y) * Z0 + Y**2 * W0
    return Y, Z, W, gamma, w, theta, sigma0 - rho * y, q, Z0, W0


class CommonFactorActualFrameControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_actual_polynomial_inverse_in_both_orders(self):
        X, Y, Z, W, I, J = sp.symbols("X Y Z W I J")
        invariant = (1 - X * Y) * W - X**2 * Z + Y**4
        companion = (1 + X * Y) * Z + Y**2 * W
        inverse_Z = (1 - X * Y) * J - Y**2 * (I - Y**4)
        inverse_W = (1 + X * Y) * (I - Y**4) + X**2 * J
        linear = sp.Matrix([[-X**2, 1 - X * Y], [1 + X * Y, Y**2]])
        self.zero(linear.det() + 1)
        to_original = {I: invariant, J: companion}
        self.zero(inverse_Z.subs(to_original, simultaneous=True) - Z)
        self.zero(inverse_W.subs(to_original, simultaneous=True) - W)
        to_pair = {Z: inverse_Z, W: inverse_W}
        self.zero(invariant.subs(to_pair, simultaneous=True) - I)
        self.zero(companion.subs(to_pair, simultaneous=True) - J)

        x, y, t, rho = sp.symbols("x y t rho")
        sy, sz, sw, gamma, w, theta, sigma, q, zzero, wzero = source_polynomials(x, y, t, rho)
        self.zero(sz - (zzero + rho * (1 - x * sy)))
        self.zero(sw - (wzero + rho * x**2))
        actual = {X: x, Y: sy, Z: sz, W: sw}
        returned_I = sp.expand(invariant.subs(actual, simultaneous=True))
        returned_J = sp.expand(companion.subs(actual, simultaneous=True))
        self.zero(returned_I - t)
        self.zero(returned_J - rho - gamma)
        self.zero(sp.diff(returned_J, rho) - 1)

        # Inverse after forward: simplify recovered t,y before Gamma.
        # This avoids unnecessary nested expansions of a known triangular map.
        recovered_t = returned_I
        recovered_y = sp.expand(sy - recovered_t * x)
        recovered_gamma = source_polynomials(x, recovered_y, recovered_t, 0)[3]
        self.zero(recovered_y - y)
        self.zero(returned_J - recovered_gamma - rho)

        # Forward after inverse in the intermediate actual coordinates
        # (X,Y,I,J). The first block verified both original Z,W inverse orders.
        inverse_y = Y - I * X
        inverse_gamma = source_polynomials(X, inverse_y, I, 0)[3]
        inverse_rho = J - inverse_gamma
        forward_y = inverse_y + I * X
        forward_i = I
        forward_j = inverse_rho + inverse_gamma
        self.zero(forward_y - Y)
        self.zero(forward_i - I)
        self.zero(forward_j - J)
        restored_Z = (1 - X * forward_y) * forward_j - forward_y**2 * (forward_i - forward_y**4)
        restored_W = (1 + X * forward_y) * (forward_i - forward_y**4) + X**2 * forward_j
        self.zero(restored_Z - inverse_Z)
        self.zero(restored_W - inverse_W)

        # Verify that the same linear inverse reproduces the literal forward
        # source Z,W, rather than assuming the map is their abstract completion.
        source_pair = {X: x, Y: sy, I: t, J: rho + gamma}
        self.zero(inverse_Z.subs(source_pair, simultaneous=True) - sz)
        self.zero(inverse_W.subs(source_pair, simultaneous=True) - sw)

    def test_exact_time_degrees_and_full_initial_kernel_controls(self):
        x, y, t, rho = sp.symbols("x y t rho")
        sy, sz, sw, gamma, w, theta, sigma, q, zzero, wzero = source_polynomials(x, y, t, rho)
        forward = (x, sy, sz, sw)
        expected_first = (1, t, sigma + 2 * q * x, theta + 2 * rho * x)
        for coordinate, expected in zip(forward, expected_first):
            self.zero(sp.diff(coordinate, x) - expected)
        self.assertEqual(tuple(sp.degree(f, x) for f in forward), (1, 1, 2, 2))
        self.zero(sp.diff(sz, x, 2) - 2 * q)
        self.zero(sp.diff(sw, x, 2) - 2 * rho)
        for coordinate in forward:
            self.zero(sp.diff(coordinate, x, 3))
        source_I = (1 - x * sy) * sw - x**2 * sz + sy**4
        self.zero(source_I - t)
        self.zero(sp.diff(source_I, x))
        self.zero(sp.diff(x, x) - 1)

        # Recover the actual selected partial from the inverse, not a
        # merely nilpotent candidate. The Gamma identity keeps this small.
        gamma_drift = sp.diff(gamma, t) - x * sp.diff(gamma, y)
        self.zero(gamma_drift - (5 * y**4 + 12 * t * y**2 - 2 * t))
        partial_rho = 1 + x * sy + x**2 * gamma_drift
        self.zero(partial_rho - (1 + x * y + x**2 * (5 * y**4 + 12 * t * y**2 - t)))

        def selected_partial(expression):
            return (x**3 * sp.diff(expression, y) - x**2 * sp.diff(expression, t)
                    + partial_rho * sp.diff(expression, rho))

        for coordinate, expected in zip(forward, (0, 0, 1, 0)):
            self.zero(selected_partial(coordinate) - expected)
        for coefficient, expected in zip((x**3, -x**2, partial_rho), (1, 0, 0)):
            self.zero(sp.expand(coefficient).coeff(x, 3) - expected)
        self.assertEqual(sp.degree(theta, y), 5)
        self.zero(sp.expand(theta).coeff(y, 5) + 1)

        A, B, C, D, tau = sp.symbols("A B C D tau")
        initial_relation = A**2 * C + A * B * D - B**4
        leading = (tau, t * tau, q * tau**2, rho * tau**2)
        self.zero(initial_relation.subs(dict(zip((A, B, C, D), leading)), simultaneous=True))
        # Exact recovery identities, with denominators confined to the
        # fraction field. Independence is justified in the written proof.
        self.zero(leading[1] - t * leading[0])
        self.zero(leading[3] - rho * leading[0]**2)
        independent_triple = sp.Matrix((leading[0], leading[1], leading[3]))
        self.zero(independent_triple.jacobian((tau, t, rho)).det() - tau**3)
        self.assertEqual(sp.Poly(initial_relation, C).degree(), 1)
        self.zero(sp.Poly(initial_relation, C).LC() - A**2)
        constant_coefficient = initial_relation.subs(C, 0)
        self.zero(constant_coefficient.subs(A, 0) + B**4)
        self.assertEqual(sp.gcd(A**2, constant_coefficient), 1)
        # Gauss's lemma and the height-one prime argument, not finite checks,
        # establish that this relation generates the entire initial kernel.


if __name__ == "__main__":
    unittest.main()
