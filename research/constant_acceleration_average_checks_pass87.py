"""Finite actual-coordinate controls, not a universal linearization test."""

import unittest

import sympy as S


def act(vector, polynomial, coordinates):
    return S.expand(sum(v * S.diff(polynomial, t)
                        for v, t in zip(vector, coordinates)))


class ConstantAccelerationAverageChecks(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(S.expand(expression), 0)

    def test_actual_constant_acceleration_and_nonnilpotent_average(self):
        u, x, y, c = canonical = S.symbols("u x y c")
        Z, A, B, C = original = S.symbols("Z A B C")
        z = x + u**2
        a = (1 + z**2) * u - z * y
        b = -z * u + y
        forward = S.Matrix([z, a, b, c])
        inverse = S.Matrix([
            A + Z * B,
            Z - (A + Z * B)**2,
            Z * A + (1 + Z**2) * B,
            C,
        ])
        to_original = dict(zip(canonical, inverse))
        to_canonical = dict(zip(original, forward))
        for actual, target in zip(forward, original):
            self.zero(actual.subs(to_original, simultaneous=True) - target)
        for actual, target in zip(inverse, canonical):
            self.zero(actual.subs(to_canonical, simultaneous=True) - target)
        self.zero(forward.jacobian(canonical).det() + 1)
        self.zero(inverse.jacobian(original).det() + 1)

        # E is the actual translation in u before this polynomial frame change.
        E = S.Matrix([1, 0, 0, 0])
        self.zero(act(E, z, canonical) - 2 * u)
        self.zero(S.diff(z, u, 2) - 2)
        self.zero(S.diff(z, u, 3))
        for f, degree in zip(forward, [2, 5, 3, 0]):
            self.assertEqual(S.Poly(f, u).degree(), degree)
            self.zero(S.diff(f, u, degree + 1))
        E_original = forward.diff(u).subs(to_original, simultaneous=True)
        self.zero(act(E_original, inverse[0], original) - 1)
        self.zero(act(E_original, Z, original) - 2 * inverse[0])

        # T is the true original partial d/dZ, obtained from the inverse.
        T = inverse.diff(Z).subs(to_canonical, simultaneous=True)
        expected_T = S.Matrix([
            -z * u + y,
            1 - 2 * u * (-z * u + y),
            (1 - z**2) * u + z * y,
            0,
        ])
        for actual, target in zip(T, expected_T):
            self.zero(actual - target)
        for f, target in zip(forward, [1, 0, 0, 0]):
            self.zero(act(T, f, canonical) - target)
        for f in canonical:
            for _ in range(3):
                f = act(T, f, canonical)
            self.zero(f)

        # Conjugate the actual derivation by u -> -u, with x,y,c fixed.
        signs = [-1, 1, 1, 1]
        conjugate_T = S.Matrix([
            sign * coefficient.subs(u, -u)
            for sign, coefficient in zip(signs, T)
        ])
        V = (T + conjugate_T) / 2
        expected_V = S.Matrix([-z * u, 1 + 2 * z * u**2, z * y, 0])
        for actual, target, sign in zip(V, expected_V, signs):
            self.zero(actual - target)
            self.zero(sign * actual.subs(u, -u) - actual)
        self.zero(act(V, z, canonical) - 1)
        self.zero(V[0] + z * u)
        self.assertNotEqual(S.expand(V[0]), 0)

        # The all-n non-LND proof is in the note; these are six exact cases.
        t = S.symbols("t")
        P = S.Integer(1)
        iterate = y
        for n in range(1, 7):
            P = S.diff(P, t) + t * P
            iterate = act(V, iterate, canonical)
            self.zero(iterate - P.subs(t, z) * y)
            self.assertEqual(S.Poly(P, t).degree(), n)
            self.assertEqual(S.Poly(P, t).LC(), 1)
        self.zero(V[1].subs(u, 0) - 1)
        self.zero(V[2].subs(u, 0) - x * y)

        # A different equivariant actual LND still exists in this control.
        other = S.Matrix([0, 1, 0, 0])
        self.zero(act(other, z, canonical) - 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
