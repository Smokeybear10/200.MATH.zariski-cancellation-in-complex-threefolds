"""One exact actual-frame control for quadratic time and full acceleration span.

The construction is a polynomial conjugate of a known translation. Both
inverse orders are checked, so it is not only coefficient or localized data.
The finite identities do not prove recognition for arbitrary quadratic-time
frames, optimality of nonlinear coordinate changes, or cancellation.
"""

import unittest

import sympy as sp


class QuasiNiceFullAccelerationChecks(unittest.TestCase):
    def test_actual_inverse_flow_and_full_acceleration_span(self):
        u, v, z, w = sp.symbols("u v z w")
        X, Y, Z, W, time = sp.symbols("X Y Z W time")

        def forward(u0, v0, z0, w0):
            r0 = sp.expand(u0 + v0**2)
            y0 = sp.expand(v0 + r0**2)
            z1 = sp.expand(z0 + v0 * y0)
            w1 = sp.expand(w0 + v0**2 * y0)
            x0 = sp.expand(r0 + y0 * w1 - z1**2)
            return (x0, y0, z1, w1)

        def inverse(x0, y0, z0, w0):
            # Expanding at each triangular stage avoids spurious expression
            # swell without omitting either full composition.
            r0 = sp.expand(x0 - y0 * w0 + z0**2)
            v0 = sp.expand(y0 - r0**2)
            return (sp.expand(r0 - v0**2), v0,
                    sp.expand(z0 - v0 * y0), sp.expand(w0 - v0**2 * y0))

        source = (u, v, z, w)
        target = (X, Y, Z, W)
        frame = forward(*source)
        restored = inverse(*target)
        self.assertEqual(inverse(*frame), source)
        self.assertEqual(forward(*restored), target)
        self.assertEqual(sp.expand(sp.det(sp.Matrix(frame).jacobian(source))), 1)

        r = u + v**2
        acceleration_half = (w - 2 * v * z, sp.Integer(1), v, v**2)
        velocity = (1 + 2 * r * acceleration_half[0], 2 * r,
                    2 * v * r, 2 * v**2 * r)
        self.assertEqual(sp.expand(frame[1] * frame[3] - frame[2]**2
                                   - frame[1] * (w - 2 * v * z) + z**2), 0)
        shifted = forward(u + time, v, z, w)
        for i, value in enumerate(frame):
            with self.subTest(coordinate=i):
                self.assertEqual(sp.expand(sp.diff(value, u) - velocity[i]), 0)
                self.assertEqual(sp.expand(sp.diff(value, u, 2)
                                           - 2 * acceleration_half[i]), 0)
                self.assertNotEqual(sp.expand(sp.diff(value, u, 2)), 0)
                self.assertEqual(sp.diff(value, u, 3), 0)
                self.assertEqual(sp.expand(shifted[i] - value - time * velocity[i]
                                           - time**2 * acceleration_half[i]), 0)

        c1, c2, c3, c4 = sp.symbols("c1 c2 c3 c4")
        affine = sum(c * value for c, value in zip((c1, c2, c3, c4), frame))
        actual = sp.expand(sp.diff(affine, u, 2) / 2)
        expected = c1 * (w - 2 * v * z) + c2 + c3 * v + c4 * v**2
        self.assertEqual(sp.expand(actual - expected), 0)
        coefficients = sp.Poly(actual, w, z, v)
        self.assertEqual(coefficients.coeff_monomial(w), c1)
        self.assertEqual(coefficients.coeff_monomial(v), c3)
        self.assertEqual(coefficients.coeff_monomial(v**2), c4)
        self.assertEqual(coefficients.coeff_monomial(1), c2)
        self.assertEqual(sp.diff(r, u), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
