"""Actual polynomial cubic frame, not a formal commutator-only model."""

import unittest

import sympy as sp


class ConstantCubicNonomissionChecks(unittest.TestCase):
    def same(self, left, right):
        difference = left - right
        if isinstance(difference, sp.MatrixBase):
            self.assertEqual(
                difference.applyfunc(lambda entry: sp.expand(entry).doit()),
                sp.zeros(*difference.shape),
            )
        else:
            self.assertEqual(sp.expand(difference).doit(), 0)

    @staticmethod
    def forward(t, y, z, s, g):
        X = y + s**2 / 2
        Y = z + g * s
        return sp.Matrix([(t + s * X - s**3 / 6) / 2, s + Y**2 / 2, X, Y])

    def test_symbolic_polynomial_family_and_all_actual_adjoint_columns(self):
        t, y, z, s = sp.symbols("t y z s")
        variables = (t, y, z, s)
        g = sp.Function("G")(t)
        gp = sp.diff(g, t)
        x = self.forward(t, y, z, s, g)
        Y = z + g * s
        jacobian = x.jacobian(variables)
        self.same(jacobian.det(), sp.Rational(1, 2))
        partials = sp.Matrix.hstack(
            sp.Matrix([2, 0, -2 * s * gp, 0]),
            sp.Matrix([-y, -s, -g + s * y * gp, 1]),
            sp.Matrix([-s, 1, s**2 * gp, 0]),
            sp.Matrix([y * Y, s * Y, 1 + g * Y - s * y * Y * gp, -Y]),
        )
        self.same(jacobian * partials, sp.eye(4))
        self.same(partials * jacobian, sp.eye(4))
        middle = partials.diff(s)
        self.same(middle[:, 0], sp.Matrix([0, 0, -2 * gp, 0]))
        self.same(middle[:, 1], sp.Matrix([0, -1, y * gp, 0]))
        self.same(middle[:, 2], sp.Matrix([-1, 0, 2 * s * gp, 0]))
        self.same(
            middle[:, 3],
            sp.Matrix([y * g, z + 2 * g * s, g**2 - y * (z + 2 * g * s) * gp, -g]),
        )
        self.same(partials[:, :2].diff(s, 2), sp.zeros(4, 2))
        defects = partials[:, 2:].diff(s, 2)
        self.same(
            defects,
            sp.Matrix.hstack(sp.Matrix([0, 0, 2 * gp, 0]), sp.Matrix([0, 2 * g, -2 * y * g * gp, 0])),
        )
        self.same(defects.diff(s), sp.zeros(4, 2))
        self.same(defects[1:3, :].det(), -4 * g * gp)
        self.same(x.diff(s, 2), sp.Matrix([s, g**2, 1, 0]))
        self.same(x.diff(s, 3), sp.Matrix([1, 0, 0, 0]))
        self.same(x.diff(s, 4), sp.zeros(4, 1))
        self.same(middle[:, 0], -defects[:, 0])
        self.same(2 * g * middle[:, 1], -defects[:, 1])
        N = middle[:, 2] + partials[:, 0] / 2
        self.same(N, s * defects[:, 0] / 2)

    def test_both_actual_inverse_orders_and_exact_nonomission_coefficients(self):
        t, y, z, s, Q1, Q2, X, Y = sp.symbols("t y z s Q1 Q2 X Y")
        g = t**2 + t + 1
        forward = self.forward(t, y, z, s, g)
        inverse_s = Q2 - Y**2 / 2
        inverse_t = 2 * Q1 - inverse_s * X + inverse_s**3 / 6
        inverse_y = X - inverse_s**2 / 2
        inverse_z = Y - (inverse_t**2 + inverse_t + 1) * inverse_s
        inverse = sp.Matrix([inverse_t, inverse_y, inverse_z, inverse_s])
        substitutions = dict(zip((Q1, Q2, X, Y), forward))
        self.same(inverse.subs(substitutions, simultaneous=True), sp.Matrix([t, y, z, s]))
        self.same(
            forward.subs(dict(zip((t, y, z, s), inverse)), simultaneous=True),
            sp.Matrix([Q1, Q2, X, Y]),
        )

        alpha, beta, gamma, delta = sp.symbols("alpha beta gamma delta")
        Y_old = z + g * s
        relation = 2 * alpha - beta * y - gamma * s + delta * y * Y_old
        polynomial = sp.Poly(sp.expand(relation), y, z, s)
        self.same(polynomial.coeff_monomial(y * z), delta)
        without_delta = sp.Poly(sp.expand(relation.subs(delta, 0)), y, z, s)
        self.same(without_delta.coeff_monomial(y), -beta)
        self.same(without_delta.coeff_monomial(s), -gamma)
        self.same(without_delta.coeff_monomial(1), 2 * alpha)

        # A constant good combination preserves k[t,s] only on beta=0.
        self.same(sp.diff(2 * alpha - beta * y, y), -beta)
        self.same((2 - y) / 2, 1 - y / 2)
        self.same((2 + y) / 2, 1 + y / 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
