"""Two bounded controls for the separate pass69 shear and vertical lemmas.

The shear is an actual polynomial coordinate inverse. Its velocity and
adjoint tables are formal consequences of the stated frame identities,
not a constructed full-frame action. The n-parametric coefficient checks
do not replace the written Laurent-ring LND restriction/specialization.
"""

import unittest

import sympy as sp


class CubicShearVerticalChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_actual_shear_and_formal_full_coefficient_bounds(self):
        q1, q2, x, y = sp.symbols("q1 q2 x y")
        Q1, Q2, X, Y = sp.symbols("Q1 Q2 X Y")
        G, g = sp.symbols("G g", nonzero=True)
        old = sp.Matrix([q1, q2, x, y])
        new = sp.Matrix([Q1, Q2, X, Y])
        forward = sp.Matrix([q1 - x * y / (2 * G) + y**3 / (12 * G**3), q2, x, y])
        inverse = sp.Matrix([Q1 + X * Y / (2 * G) - Y**3 / (12 * G**3), Q2, X, Y])
        self.assert_zero(forward.subs(dict(zip(old, inverse)), simultaneous=True) - new)
        self.assert_zero(inverse.subs(dict(zip(new, forward)), simultaneous=True) - old)
        jacobian = forward.jacobian(old)
        transported = inverse.jacobian(new).subs(dict(zip(new, forward)), simultaneous=True)
        self.assert_zero(jacobian * transported - sp.eye(4))
        self.assert_zero(transported * jacobian - sp.eye(4))
        self.assertEqual(jacobian.det(), 1)
        basis = sp.eye(4)
        self.assert_zero(transported[:, 0] - basis[:, 0])
        self.assert_zero(transported[:, 1] - basis[:, 1])
        self.assert_zero(transported[:, 2] - basis[:, 2] - y * basis[:, 0] / (2 * G))
        self.assert_zero(transported[:, 3] - basis[:, 3]
                         - (x / (2 * G) - y**2 / (4 * G**3)) * basis[:, 0])

        # Formal coefficient tables retain the original, stronger relation
        # V_X=-g W_1. They do not assume normalized nilpotence descends.
        W1 = sp.Matrix(sp.symbols("w0:4"))
        VX = -g * W1
        VY = sp.Matrix(sp.symbols("v0:4"))
        WX = sp.Matrix(sp.symbols("wx0:4"))
        WY = sp.Matrix(sp.symbols("wy0:4"))
        P = sp.Symbol("P")
        zero = sp.zeros(4, 1)
        good = {0: basis[:, 0], 1: W1}
        bad_x = {0: basis[:, 2], 1: WX, 2: VX}
        bad_y = {0: basis[:, 3], 1: WY, 2: VY}
        e_x = {0: x, 1: P, 2: g**2}
        e_y = {0: y, 1: g * G}

        def ad_product(order, coefficients):
            return sum((sp.binomial(order, j) * coefficients.get(j, 0)
                        * good.get(order - j, zero) for j in range(order + 1)), zero)

        e_y_squared = {0: y**2, 1: 2 * y * g * G, 2: 2 * g**2 * G**2}
        x_multiplier = {j: entry / (2 * G) for j, entry in e_y.items()}
        y_multiplier = {j: e_x.get(j, 0) / (2 * G)
                        - e_y_squared.get(j, 0) / (4 * G**3) for j in range(3)}

        def new_bad(order, original, multiplier):
            return original.get(order, zero) + ad_product(order, multiplier)

        self.assert_zero(new_bad(2, bad_x, x_multiplier))
        self.assert_zero(new_bad(3, bad_x, x_multiplier))
        self.assert_zero(y_multiplier[2])
        self.assert_zero(new_bad(3, bad_y, y_multiplier))
        self.assert_zero(new_bad(2, bad_y, y_multiplier)
                         - VY - (P / G - y * g / G**2) * W1)

        def e_product(order):
            return sum(sp.binomial(order, j) * e_x.get(j, 0)
                       * e_y.get(order - j, 0) for j in range(order + 1))

        self.assert_zero(e_product(4))
        e_y_cubed_3 = 6 * (g * G)**3
        self.assert_zero(g**3 - e_product(3) / (2 * G) + e_y_cubed_3 / (12 * G**3))

    def test_n_parametric_dilation_and_vertical_divisibility_boundary(self):
        s, z, coefficient = sp.symbols("s z coefficient")
        n = sp.Symbol("n", integer=True, positive=True)
        j = sp.Symbol("j", integer=True, nonnegative=True)
        # On A, T_z=z^(n-1) Phi T Phi^-1. On s there is one
        # additional z because Phi^-1(s)=zs. The permitted ranges
        # j<=n-1 and j<=n give nonnegative exponents, respectively.
        self.assertEqual(sp.powsimp(
            z**(n - 1) * coefficient * s**j / z**j
            - coefficient * s**j * z**(n - 1 - j), force=True), 0)
        self.assertEqual(sp.powsimp(
            z**(n - 1) * z * coefficient * s**j / z**j
            - coefficient * s**j * z**(n - j), force=True), 0)
        horizontal = coefficient * s**(n - 1) * z**0
        vertical = coefficient * s**n * z**0
        self.assertEqual(sp.diff(horizontal, z), 0)
        self.assertEqual(sp.diff(vertical, z), 0)
        self.assertEqual(sp.simplify(sp.diff(coefficient * s**n, s, 1)
                                     - n * coefficient * s**(n - 1)), 0)

        # A formal vertical field D(s)=h s^n/n! has a nonzero
        # derivative of every positive power when h is fixed and nonzero.
        # This is a non-LND boundary control, not the universal proof that
        # a specialized LND must annihilate an element dividing its image.
        h = sp.Symbol("h", nonzero=True)
        power = sp.Symbol("d", integer=True, positive=True)
        image = h * s**n * sp.diff(s**power, s) / sp.factorial(n)
        expected = power * h * s**(power + n - 1) / sp.factorial(n)
        self.assertEqual(sp.simplify(image - expected), 0)
        self.assertEqual(sp.simplify((h * s**n / sp.factorial(n)) / s
                                     - h * s**(n - 1) / sp.factorial(n)), 0)


if __name__ == "__main__":
    unittest.main()
