"""One actual-frame control for frame-filtration-generation-pass49.md.

The example disproves bounded degree of an arbitrary supplied slice's
projected coordinate generators, not bounded-degree generation of the ring.
"""

import unittest

import sympy as sp


class FrameFiltrationGenerationChecks(unittest.TestCase):
    def test_actual_frame_and_unbounded_supplied_slice_projection(self):
        u, v, a, c, r, s = sp.symbols("u v a c r s")
        variables = (u, v, a, c)
        g = u * v - 1
        physical = sp.Matrix([u + a**2 / 2, v + c**2 / 2, a, c])
        E = sp.Matrix([0, 0, u, g])

        def clean(value):
            return sp.cancel(sp.expand(value))

        def act(field, value):
            return clean(sum(entry * sp.diff(value, coordinate)
                             for entry, coordinate in zip(field, variables)))

        def bracket(left, right):
            return sp.Matrix([act(left, right[i]) - act(right, left[i])
                              for i in range(4)])

        partials = physical.jacobian(variables).inv()
        W = [bracket(E, partials[:, i]) for i in range(4)]
        V = [bracket(E, W[i]) for i in (2, 3)]
        for i in (0, 1):
            self.assertEqual(bracket(E, W[i]), sp.zeros(4, 1))
        for top in V:
            self.assertEqual(bracket(E, top), sp.zeros(4, 1))
        bad = sp.Matrix([[act(top, coordinate) for top in V]
                         for coordinate in physical[2:]])
        self.assertEqual(clean(bad.det() - 4 * u**2 * g), 0)
        for coordinate in physical:
            self.assertEqual(act(E, act(E, act(E, coordinate))), 0)

        s0 = v * a - c
        r0 = g * a - u * c
        self.assertEqual(act(E, s0), 1)
        self.assertEqual(act(E, r0), 0)
        self.assertEqual(act(W[0], r0), 1)

        for n in (2, 3, 5):
            with self.subTest(n=n):
                s_n = s0 + r0**n
                inverse = {
                    a: u * (s - r**n) - r,
                    c: g * (s - r**n) - v * r,
                }
                self.assertEqual(act(E, s_n), 1)
                self.assertEqual(clean(s_n.subs(inverse, simultaneous=True) - s), 0)
                self.assertEqual(clean(r0.subs(inverse, simultaneous=True) - r), 0)
                for coordinate in (a, c):
                    self.assertEqual(clean(inverse[coordinate].subs(
                        {r: r0, s: s_n}, simultaneous=True
                    ) - coordinate), 0)

                expected = [
                    u + (r + u * r**n)**2 / 2,
                    v + (v * r + g * r**n)**2 / 2,
                    -r - u * r**n,
                    -v * r - g * r**n,
                ]
                for i, coordinate in enumerate(physical):
                    projected = (
                        coordinate - s_n * act(E, coordinate)
                        + s_n**2 * act(E, act(E, coordinate)) / 2
                    )
                    actual = clean(projected.subs(inverse, simultaneous=True))
                    self.assertEqual(clean(actual - expected[i]), 0)
                    self.assertEqual(sp.degree(actual, r),
                                     2 * n if i < 2 else n)
                    self.assertEqual(sp.diff(actual, s), 0)
                self.assertEqual(
                    sp.Poly(expected[0], r).LC(), u**2 / 2
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
