"""One exact finite-control method for the whole-fiber actions100.

Checks a symbolic weighted cubic and explicit derivations on the two
Artin coefficient rings C[g]/g^2 and C[g]/(g^2(g-1)), including both
orders of a polynomial fiber-coordinate change with beta=c^2. These
quotient-ring controls are not original polynomial C4 frames. They do
not certify the actual volume, whole-fiber presentation, normalization,
or universal geometric hypotheses of the written proof. No older
checker or solver is imported; subtests do not add unittest methods.
"""

import unittest

import sympy as S


class QuadraticWholeFiberChecks(unittest.TestCase):
    def test_weighted_coefficient_and_nilpotent_fiber_actions(self):
        c, x, y = S.symbols("c x y")
        gamma, lam = S.symbols("gamma lam", nonzero=True)
        beta = S.Function("beta")(c)

        def weighted(expr, gamma_value=gamma):
            return S.expand(gamma_value * x * S.diff(expr, y)
                            + lam * y * S.diff(expr, c))

        first = weighted(beta * y)
        second = weighted(first)
        third = weighted(second)
        self.assertEqual(S.expand(first - gamma * beta * x
                                  - lam * S.diff(beta, c) * y**2), 0)
        self.assertEqual(S.expand(second
                                  - 3 * gamma * lam * S.diff(beta, c) * x * y
                                  - lam**2 * S.diff(beta, c, 2) * y**3), 0)
        expected = (3 * gamma**2 * lam * S.diff(beta, c) * x**2
                    + 6 * gamma * lam**2 * S.diff(beta, c, 2) * x * y**2
                    + lam**3 * S.diff(beta, c, 3) * y**4)
        self.assertEqual(S.expand(third - expected), 0)
        self.assertEqual(S.Poly(third, x, y).coeff_monomial(x**2),
                         3 * gamma**2 * lam * S.diff(beta, c))

        b0, b1, b2 = S.symbols("b0 b1 b2")
        for coefficient, gamma_value, answer in (
            (b0, gamma, 0),
            (c, gamma, 3 * gamma**2 * lam * x**2),
            (b0 + b1 * c + b2 * c**2, 0, 0),
            (c**3, 0, 6 * lam**3 * y**4),
        ):
            value = coefficient * y
            for _ in range(3):
                value = weighted(value, gamma_value)
            self.assertEqual(S.expand(value - answer), 0)

        g, sigma, Z = S.symbols("g sigma Z")
        q, kappa, delta = S.symbols("q kappa delta", nonzero=True)
        eta1, eta2 = S.symbols("eta1 eta2")
        for profile, modulus in (("double", g**2),
                                 ("double_and_simple", g**2 * (g - 1))):
            with self.subTest(profile=profile):
                def red(expr):
                    return S.expand(S.rem(S.expand(expr), modulus, g))

                if profile == "double":
                    e1, e2, epsilon = S.S.Zero, S.S.One, g
                else:
                    e1, e2, epsilon = g**2, 1 - g**2, g - g**2
                for relation in (e1**2 - e1, e2**2 - e2, e1 * e2,
                                 e1 + e2 - 1, epsilon**2, e1 * epsilon):
                    self.assertEqual(red(relation), 0)
                self.assertNotEqual(red(epsilon), 0)

                eta = eta2 * e2 + eta1 * e1
                speed = kappa * epsilon + delta * e1
                coefficient = b0 + b1 * c + b2 * c**2
                h = red(eta + epsilon * coefficient)
                hc = S.diff(h, c)
                u = sigma + h
                z = red(c + q * sigma * h + q * sigma**2 / 2)

                def E(expr):
                    return red(S.diff(expr, sigma))

                def N(expr):
                    return red(speed * S.diff(expr, c))

                def T(expr):
                    return red((1 - q * sigma * hc) * S.diff(expr, c))

                self.assertEqual(red(hc**2), 0)
                self.assertEqual(red(speed * hc), 0)
                self.assertEqual(N(h), 0)
                self.assertEqual(N(N(c)), 0)
                self.assertNotEqual(N(c), 0)
                self.assertEqual(N(u), 0)
                self.assertEqual(N(z), red(speed))
                self.assertEqual(E(u), 1)
                self.assertEqual(red(E(z) - q * u), 0)
                self.assertEqual(E(E(z)), q)
                self.assertEqual(E(E(E(z))), 0)
                self.assertEqual(T(z), 1)
                self.assertEqual(red(T(u) - hc), 0)
                self.assertEqual(T(sigma), 0)
                for generator in (g, sigma, c):
                    self.assertEqual(red(N(T(generator)) - T(N(generator))), 0)
                    self.assertEqual(red(E(N(generator)) - N(E(generator))), 0)
                    self.assertEqual(red(E(T(generator)) - T(E(generator))
                                         + q * hc * S.diff(generator, c)), 0)
                self.assertEqual(T(T(T(c))), 0)
                self.assertEqual(T(T(T(u))), 0)
                # Nonconstant beta leaves a nonzero nilpotent commutator.
                self.assertNotEqual(red(E(T(c)).subs({b0: 0, b1: 0, b2: 1})), 0)
                self.assertEqual(red(E(T(c)).subs({b1: 0, b2: 0})), 0)

                # An actual automorphism over the stated Artin coefficient
                # ring, not a lift to an original polynomial C4 frame.
                h_square = red(eta + epsilon * c**2)
                z_forward = red(c + q * sigma * h_square + q * sigma**2 / 2)
                centered_Z = Z - q * sigma * eta - q * sigma**2 / 2
                c_backward = red(centered_Z - q * sigma * epsilon * centered_Z**2)
                forward = (g, sigma, z_forward)
                backward = (g, sigma, c_backward)
                self.assertEqual(
                    tuple(red(expr.subs(dict(zip((g, sigma, Z), forward)),
                                        simultaneous=True)) for expr in backward),
                    (g, sigma, c),
                )
                self.assertEqual(
                    tuple(red(expr.subs(dict(zip((g, sigma, c), backward)),
                                        simultaneous=True)) for expr in forward),
                    (g, sigma, Z),
                )
                transported_c = red(S.diff(c_backward, Z).subs(Z, z_forward))
                self.assertEqual(red(transported_c
                                     - (1 - 2 * q * sigma * epsilon * c)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
