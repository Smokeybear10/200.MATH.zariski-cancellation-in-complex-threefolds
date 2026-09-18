"""Four bounded algebraic controls for the quadratic sign involution.

Coefficient symbols in the first method stand for elements fixed by the
sign map and by the slice derivative. The second method is only a
nonreduced coefficient-ideal example, not an actual-frame realization.
The reflection method gives a concrete polynomial map and triangular inverse.
An additional method checks the intrinsic quadratic-parameter shift and
the complete transformed coefficients, without proving their geometric use.
These checks do not prove universal generation, ideal contraction,
actual-frame entry, surface cancellation, the linear-plane theorem,
or recognition of the unknown threefold. No solver or older checker is
imported.
"""

import unittest

import sympy as sp


class QuadraticInvolutionChecks(unittest.TestCase):
    def test_conjugation_and_even_odd_coordinate_formulas(self):
        u, v, r, U, P, eta, alpha, q = sp.symbols("u v r U P eta alpha q")
        k0, k1, k2, k3, k4 = sp.symbols("k0 k1 k2 k3 k4")
        square = 2 * P * U - eta

        def normal(value):
            return sp.expand(sp.rem(sp.expand(value), r**2 - square, r))

        def sigma(value):
            return sp.expand(value.subs(r, -r))

        def translate(value, amount):
            return sp.expand(value.subs(u, u + amount * r))

        def shifted(value):
            # Ring composition: apply sigma first, then exp(2 alpha r E).
            return translate(sigma(value), 2 * alpha)

        b = sp.symbols("b1:4")
        d = sp.symbols("d1:4")
        e = sp.symbols("e1:4")
        f = sp.symbols("f1:4")
        good = [b[i] * u + d[i] * U + e[i] * r + f[i] for i in range(3)]
        bad = q * u**2 / 2 + k4 * U**2 + k3 * r * U + k2 * U + k1 * r + k0
        values = [u, r, U, P, eta, u + alpha * r, *good, bad]
        for value in values:
            self.assertEqual(sp.expand(shifted(shifted(value)) - value), 0)
            conjugated = translate(sigma(translate(value, -alpha)), alpha)
            self.assertEqual(sp.expand(shifted(value) - conjugated), 0)
        self.assertEqual(shifted(u), u + 2 * alpha * r)
        self.assertEqual(shifted(r), -r)
        self.assertEqual(shifted(u + alpha * r), u + alpha * r)
        self.assertEqual(shifted(r**2 - square), r**2 - square)

        for i, value in enumerate(good):
            in_v = normal(value.subs(u, v - alpha * r))
            even = normal((in_v + sigma(in_v)) / 2)
            odd = normal((in_v - sigma(in_v)) / 2)
            self.assertEqual(sp.expand(even - b[i] * v - d[i] * U - f[i]), 0)
            self.assertEqual(sp.expand(odd - (e[i] - alpha * b[i]) * r), 0)

        bad_in_v = normal(bad.subs(u, v - alpha * r))
        expected_even = (q * v**2 / 2 + k4 * U**2 + k2 * U + k0
                         + q * alpha**2 * square / 2)
        expected_odd = r * (k3 * U + k1 - q * alpha * v)
        self.assertEqual(normal((bad_in_v + sigma(bad_in_v)) / 2 - expected_even), 0)
        self.assertEqual(normal((bad_in_v - sigma(bad_in_v)) / 2 - expected_odd), 0)
        self.assertEqual(normal(bad_in_v - expected_even - expected_odd), 0)

    def test_nonreduced_radical_does_not_mean_membership(self):
        s, U = sp.symbols("s U")
        polynomial = 1 + s * U
        inverse = 1 - s * U
        self.assertEqual(sp.rem(s**2, s**2, s), 0)
        self.assertEqual(sp.rem(s, s**2, s), s)
        self.assertNotEqual(sp.rem(s, s**2, s), 0)
        self.assertEqual(sp.rem(sp.expand(polynomial * inverse - 1), s**2, s), 0)
        # Bezout certificate for (s^2, 1+sU); s is radical but not in (s^2).
        self.assertEqual(sp.expand(polynomial * inverse + s**2 * U**2), 1)
        self.assertNotEqual(sp.expand(polynomial * inverse), 1)

    def test_zero_good_odd_column_triangular_reflection(self):
        x1, x2, x3, z, R = sp.symbols("x1 x2 x3 z R")
        F = x1**2 + x2 * x3 + x3**3
        k1 = sp.Integer(3)
        r = (z - F / 2) / k1
        recovered_z = k1 * R + F / 2

        def reflection(value):
            return sp.expand(value.subs(z, F - z))

        self.assertEqual(sp.expand(r.subs(z, recovered_z) - R), 0)
        self.assertEqual(sp.expand(recovered_z.subs(R, r) - z), 0)
        for value in (x1, x2, x3, z, r):
            self.assertEqual(sp.expand(reflection(reflection(value)) - value), 0)
        for value in (x1, x2, x3):
            self.assertEqual(reflection(value), value)
        self.assertEqual(sp.expand(reflection(r) + r), 0)
        self.assertEqual(sp.expand(z - reflection(z) - 2 * k1 * r), 0)
        self.assertEqual(sp.expand(reflection(z).subs(z, recovered_z)
                                   - recovered_z.subs(R, -R)), 0)
        jacobian = sp.Matrix([x1, x2, x3, r]).jacobian([x1, x2, x3, z])
        self.assertEqual(jacobian.det(), 1 / k1)

    def test_intrinsic_shift_and_all_transformed_coefficients(self):
        U, r, V, R, P, eta, a = sp.symbols("U r V R P eta a")
        b, d, e, f, u, q = sp.symbols("b d e f u q")
        k0, k1, k2, k3, k4 = sp.symbols("k0 k1 k2 k3 k4")
        shifted_U = U + a * r + a**2 * P / 2
        shifted_r = r + a * P
        inverse = {U: V - a * R + a**2 * P / 2, r: R - a * P}
        forward = {V: shifted_U, R: shifted_r}
        self.assertEqual(sp.expand(shifted_U.subs(inverse, simultaneous=True) - V), 0)
        self.assertEqual(sp.expand(shifted_r.subs(inverse, simultaneous=True) - R), 0)
        self.assertEqual(sp.expand(inverse[U].subs(forward, simultaneous=True) - U), 0)
        self.assertEqual(sp.expand(inverse[r].subs(forward, simultaneous=True) - r), 0)
        self.assertEqual(sp.expand(shifted_r**2 - 2 * P * shifted_U
                                   - (r**2 - 2 * P * U)), 0)

        def N(value):
            return sp.expand(r * sp.diff(value, U) + P * sp.diff(value, r))

        self.assertEqual(N(shifted_U), shifted_r)
        self.assertEqual(N(shifted_r), P)

        def normal(value):
            return sp.expand(sp.rem(sp.expand(value), R**2 - 2 * P * V + eta, R))

        good = b * u + d * U + e * r + f
        ep = e - a * d
        fp = f - a * P * e + a**2 * P * d / 2
        self.assertEqual(normal(good.subs(inverse, simultaneous=True)
                                - (b * u + d * V + ep * R + fp)), 0)
        self.assertEqual(ep.subs(e, a * d), 0)

        kp4 = k4
        kp3 = k3 - 2 * a * k4
        kp2 = k2 - 3 * a * P * k3 + 3 * a**2 * P * k4
        kp1 = k1 - a * k2 + 3 * a**2 * P * k3 / 2 - a**3 * P * k4
        kp0 = (k0 - a * P * k1 + a**2 * P * k2 / 2
               + (a * eta - a**3 * P**2 / 2) * k3
               + (a**4 * P**2 / 4 - a**2 * eta) * k4)
        bad = q * u**2 / 2 + k4 * U**2 + k3 * r * U + k2 * U + k1 * r + k0
        bad_prime = q * u**2 / 2 + kp4 * V**2 + kp3 * R * V + kp2 * V + kp1 * R + kp0
        self.assertEqual(normal(bad.subs(inverse, simultaneous=True) - bad_prime), 0)
        recovered_bad = bad_prime.subs(forward, simultaneous=True)
        self.assertEqual(sp.expand(sp.rem(sp.expand(recovered_bad - bad),
                                          r**2 - 2 * P * U + eta, r)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
