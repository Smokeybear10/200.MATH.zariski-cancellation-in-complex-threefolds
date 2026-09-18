"""Finite intrinsic and formal label controls, not an original-frame test."""

import unittest

import sympy as sp


class QuadraticTripleBranchControl(unittest.TestCase):
    def test_intrinsic_triple_fiber_and_three_to_two_labels(self):
        x, y, c, t, Y, s, w, zeta, theta = sp.symbols("x y c t Y s w zeta theta")

        def n(poly):
            return sp.expand(x * sp.diff(poly, y) - 3 * y**2 * sp.diff(poly, c))

        z = c * x + y**3
        self.assertEqual(n(z), 0)
        self.assertEqual(n(n(n(y))), 0)
        self.assertEqual(n(n(n(x))), 0)
        self.assertEqual(n(n(n(n(c)))), 0)
        self.assertEqual(sp.gcd(x, -3 * y**2), 1)
        self.assertEqual(z.subs(x, 0), y**3)
        self.assertEqual(
            sp.Matrix([x, z]).jacobian([x, y]).subs({x: 0, y: 0}),
            sp.Matrix([[1, 0], [c, 0]]),
        )

        # Exact normalized base cusp and its full cubic pullback.
        base_X, base_Z = sp.symbols("base_X base_Z")
        self.assertEqual(
            (base_X**3 - base_Z**4).subs({base_X: t**4, base_Z: t**3}), 0
        )
        pulled = sp.expand(z.subs(x, t**4) - t**3)
        self.assertEqual(sp.expand(pulled - (y**3 - t**3 * (1 - c * t))), 0)
        self.assertEqual(
            sp.expand(sp.discriminant(pulled, y) + 27 * t**6 * (1 - c * t)**2), 0
        )

        # After y=(1-ct)^(1/3)Y, the formal curve is Y^3=t^3.
        # Only exact polynomial identities are tested, not infinite series.
        cubic = Y**3 - t**3
        numerator = t**2 - 2 * t * Y - 2 * Y**2
        self.assertEqual(
            sp.rem(sp.expand(numerator**2 - 9 * t**4), cubic, Y), 0
        )
        H = s * numerator / 3
        rem = sp.rem(sp.expand(H**2 - t**4 * (1 + t)), cubic, Y)
        self.assertEqual(sp.expand(rem - t**4 * (s**2 - 1 - t)), 0)
        self.assertEqual(sp.expand(H.subs(Y, t)), -s * t**2)
        for root in (zeta, zeta**2):
            label = sp.expand(H.subs(Y, root * t) - s * t**2)
            self.assertEqual(sp.rem(label, zeta**2 + zeta + 1, zeta), 0)

        # Source normalization, with two distinct points glued over t=0.
        source_t = w**2 - 1
        source_H = source_t**2 * w
        self.assertEqual(
            sp.expand(source_H**2 - source_t**4 * (1 + source_t)), 0
        )
        self.assertEqual(source_t.subs(w, -1), 0)
        self.assertEqual(source_t.subs(w, 1), 0)
        self.assertEqual(source_H.subs(w, -1), 0)
        self.assertEqual(source_H.subs(w, 1), 0)
        self.assertEqual(
            [sp.diff(source_t, w).subs(w, r) for r in (-1, 1)], [-2, 2]
        )

        # Conductor descent for the original (3,4) cusp.
        for exponent, monomial in zip((6, 7, 8), (base_Z**2, base_X * base_Z, base_X**2)):
            self.assertEqual(
                monomial.subs({base_X: t**4, base_Z: t**3}), t**exponent
            )
        self.assertEqual(
            (base_X**4 + base_X**2 * base_Z**3).subs(
                {base_X: t**4, base_Z: t**3}
            ),
            t**16 + t**17,
        )
        normalized_X = source_t**4
        normalized_Z = source_t**3
        normalized_K = source_t**8 * w
        self.assertEqual(
            sp.expand(normalized_K**2 - normalized_X**4 - normalized_X**2 * normalized_Z**3),
            0,
        )

        # Denominator-cleared formal N(Y)=0, not rationality of K on E.
        derivative_numerator = t**4 * theta**3 - t * y**3
        reduced = sp.rem(derivative_numerator, theta**3 - (1 - c * t), theta)
        reduced = sp.rem(reduced, pulled, y)
        self.assertEqual(sp.expand(reduced), 0)
        rational_c = (t**3 - y**3) / t**4
        self.assertEqual(sp.cancel(t**4 * sp.diff(rational_c, y)), -3 * y**2)
        self.assertEqual(sp.degree(1 + t, t), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
