"""Exact actual-coordinate controls, not a universal moving-branch proof."""

import unittest

import sympy as sp


class MovingFrameDivisibilityChecks(unittest.TestCase):
    def setUp(self):
        self.a, self.s, self.z, self.w = sp.symbols("a s z w")
        self.base = (self.a, self.s, self.z, self.w)
        self.x = sp.symbols("x1:5")
        a, s, z, w = self.base
        self.g = a**2 + 1
        self.h = 2 * a
        self.E = sp.Matrix([0, 1, 0, -self.g])
        good = a - z * w / 3 + w**4 / 24
        self.physical = sp.Matrix([good + s, good - s, z - w**3 / 6, w])
        x1, x2, x3, x4 = self.x
        self.inverse = sp.Matrix([
            (x1 + x2) / 2 + x3 * x4 / 3 + x4**4 / 72,
            (x1 - x2) / 2,
            x3 + x4**3 / 6,
            x4,
        ])
        self.partials = self.physical.jacobian(self.base).inv()

    def act(self, field, polynomial):
        return sp.expand(sum(
            field[i] * sp.diff(polynomial, variable)
            for i, variable in enumerate(self.base)
        ))

    def bracket(self, left, right):
        return sp.Matrix([
            self.act(left, right[i]) - self.act(right, left[i])
            for i in range(4)
        ]).applyfunc(sp.expand)

    def same(self, left, right):
        difference = left - right
        if isinstance(difference, sp.MatrixBase):
            self.assertEqual(
                difference.applyfunc(sp.expand),
                sp.zeros(*difference.shape),
            )
        else:
            self.assertEqual(sp.expand(difference), 0)

    def test_actual_inverse_and_all_four_exact_adjoint_columns(self):
        a, s, z, w = self.base
        g, h = self.g, self.h
        self.same(
            self.inverse.subs(dict(zip(self.x, self.physical)), simultaneous=True),
            sp.Matrix(self.base),
        )
        self.same(
            self.physical.subs(dict(zip(self.base, self.inverse)), simultaneous=True),
            sp.Matrix(self.x),
        )
        self.same(self.physical.jacobian(self.base).det(), -2)
        expected = sp.Matrix([
            [sp.Rational(1, 2), sp.Rational(1, 2), w / 3, z / 3],
            [sp.Rational(1, 2), -sp.Rational(1, 2), 0, 0],
            [0, 0, 1, w**2 / 2],
            [0, 0, 0, 1],
        ])
        self.same(self.partials, expected)
        for i in range(4):
            for j in range(i):
                self.same(
                    self.bracket(self.partials[:, i], self.partials[:, j]),
                    sp.zeros(4, 1),
                )
        first = [
            sp.Matrix([0, 0, 0, h / 2]),
            sp.Matrix([0, 0, 0, h / 2]),
            sp.Matrix([-g / 3, 0, 0, w * h / 3]),
            sp.Matrix([0, 0, -g * w, z * h / 3]),
        ]
        second = [
            sp.zeros(4, 1),
            sp.zeros(4, 1),
            sp.Matrix([0, 0, 0, -2 * g * h / 3]),
            sp.Matrix([0, 0, g**2, 0]),
        ]
        for i in range(4):
            actual_first = self.bracket(self.E, self.partials[:, i])
            actual_second = self.bracket(self.E, actual_first)
            self.same(actual_first, first[i])
            self.same(actual_second, second[i])
            self.same(self.bracket(self.E, actual_second), sp.zeros(4, 1))
            self.assertNotEqual(
                first[i] if i < 2 else second[i], sp.zeros(4, 1)
            )
        self.same(self.bracket(second[2], second[3]), sp.zeros(4, 1))
        self.assertEqual(sp.Matrix.hstack(self.E, second[2], second[3]).rank(), 3)
        # A z-dependent speed violates exactly the fourth bound in this family.
        broad_g = a**2 + z + 1
        broad_E = sp.Matrix([0, 1, 0, -broad_g])
        broad_W4 = self.bracket(broad_E, self.partials[:, 3])
        broad_V4 = self.bracket(broad_E, broad_W4)
        broad_third = self.bracket(broad_E, broad_V4)
        self.same(broad_V4, sp.Matrix([0, 0, broad_g**2, -2*broad_g*w]))
        self.same(broad_third, sp.Matrix([0, 0, 0, 3*broad_g**2]))
        self.assertNotEqual(broad_third, sp.zeros(4, 1))
        broad_T = self.partials[:, 0] + self.partials[:, 1]
        broad_U = self.bracket(broad_E, broad_T)
        broad_W3 = self.bracket(broad_E, self.partials[:, 2])
        broad_Y = broad_g*broad_T + 3*broad_W3
        broad_repair = broad_g**2*broad_Y - broad_g**2*w*broad_U
        self.same(broad_repair, broad_third)

    def test_canonical_layers_failed_divisibility_and_zero_repair(self):
        a, s, z, w = self.base
        g, h = self.g, self.h
        layers = {0: self.physical}
        for order in range(1, 6):
            layers[order] = layers[order - 1].applyfunc(
                lambda polynomial: self.act(self.E, polynomial)
            )
        self.same(layers[2], sp.Matrix([g**2*w**2/2, g**2*w**2/2, -g**2*w, 0]))
        self.same(layers[3], sp.Matrix([-g**3*w, -g**3*w, g**3, 0]))
        self.same(layers[4], sp.Matrix([g**4, g**4, 0, 0]))
        self.same(layers[5], sp.zeros(4, 1))
        T = self.partials[:, 0] + self.partials[:, 1]
        S = self.partials[:, 2]
        U = self.bracket(self.E, T)
        W = self.bracket(self.E, S)
        V = self.bracket(self.E, W)
        self.same(self.act(T, g), h)
        self.same(g * U + sp.Rational(3, 2) * V, sp.zeros(4, 1))
        self.same(self.act(W, g), -g * h / 3)
        self.same(self.act(S, g), w * h / 3)
        self.assertNotEqual(sp.rem(self.act(S, g), g, a), 0)
        v = layers[2][2]
        self.same(self.act(self.E, v), g**3)
        self.same(self.act(U, v), -g**2*h)
        normalizer = g*T + 3*W
        self.same(normalizer, sp.Matrix([0, 0, 0, w*h]))
        self.same(g**2*normalizer + v*U, sp.zeros(4, 1))
        omitted = self.partials[:, 0] - self.partials[:, 1]
        self.same(omitted, sp.Matrix([0, 1, 0, 0]))
        self.same(self.act(omitted, g), 0)
        self.same(self.bracket(self.E, omitted), sp.zeros(4, 1))
        r = sp.symbols("r")
        invariant = w + g*s
        self.same(self.act(self.E, invariant), 0)
        self.same(invariant.subs(w, r-g*s), r)
        self.same((r-g*s).subs(r, invariant), w)
        self.same(self.act(self.E, s), 1)
        self.assertNotEqual(layers[2][2], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
