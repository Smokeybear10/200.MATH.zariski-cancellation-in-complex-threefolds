"""Exact finite controls for the formal-chart boundary in audit260.

These checks rebuild the formulas independently using SymPy. They do not
verify the universal chain lemma, field-extension degree, etale geometry,
or any cancellation theorem. The degree-two field argument is written in
the accompanying mathematical note. No retained checker is imported.
"""

import unittest

import sympy as sp


class FormalFieldReturnControls(unittest.TestCase):
    def assert_zero(self, value):
        self.assertEqual(sp.cancel(sp.expand(value)), 0)

    def test_tail_gradients_and_whole_line_parameter(self):
        tau, rho, v, U, V = sp.symbols("tau rho v U V")
        phi = (V - U**2) ** 2 - 2 * tau * U + rho
        psi = V - U**2
        y = (v**2 + rho) / (2 * tau)
        z = v + y**2
        self.assert_zero(phi.subs({U: y, V: z}, simultaneous=True))
        self.assert_zero(psi.subs({U: y, V: z}, simultaneous=True) - v)
        self.assert_zero(sp.diff(phi, tau) - sp.diff(psi, U))
        self.assert_zero(sp.diff(phi, rho) - sp.diff(psi, V))
        self.assertEqual(sp.Poly(phi, U, V).total_degree(), 4)
        self.assertEqual(sp.Poly(psi, U, V).total_degree(), 2)
        # Altering the rho coefficient is detected by the second gradient.
        self.assertNotEqual(sp.diff(phi + rho, rho) - sp.diff(psi, V), 0)

    def test_actual_nagata_map_has_both_polynomial_inverses(self):
        X, Y, R, W, I, J = sp.symbols("X Y R W I J")
        H = X * W + R**2
        image_I = R + X * H
        image_J = W - 2 * R * H - X * H**2
        delta = X * J + I**2
        inverse_R = I - X * delta
        inverse_W = J + 2 * I * delta - X * delta**2
        forward = {I: image_I, J: image_J}
        backward = {R: inverse_R, W: inverse_W}
        self.assert_zero(inverse_R.subs(forward, simultaneous=True) - R)
        self.assert_zero(inverse_W.subs(forward, simultaneous=True) - W)
        self.assert_zero(image_I.subs(backward, simultaneous=True) - I)
        self.assert_zero(image_J.subs(backward, simultaneous=True) - J)
        full_map = sp.Matrix([X, Y, image_I, image_J])
        self.assert_zero(full_map.jacobian([X, Y, R, W]).det() - 1)
        # The sign in the last inverse term is essential.
        wrong_W = J + 2 * I * delta + X * delta**2
        self.assertNotEqual(
            sp.expand(wrong_W.subs(forward, simultaneous=True) - W), 0
        )

    def test_formal_chart_has_unit_jacobian_and_square_return(self):
        X, tau, rho, v = sp.symbols("X tau rho v")
        y = (v**2 + rho) / (2 * tau)
        Y = y + tau * X
        R = v - v**2 * X - tau**2 * X**2
        Z = R + Y**2
        quotient, remainder = sp.div(
            sp.Poly(v**2 - R**2, X), sp.Poly(X, X)
        )
        self.assertEqual(remainder.as_expr(), 0)
        W = tau**2 + quotient.as_expr()
        self.assertEqual(sp.Poly(W, X).degree(), 3)
        self.assert_zero(Z - (v + y**2 + rho * X))
        H = X * W + R**2
        I = R + X * H
        J = W - 2 * R * H - X * H**2
        self.assert_zero(H - (v**2 + tau**2 * X))
        self.assert_zero(I - v)
        self.assert_zero(J - tau**2)
        determinant = sp.Matrix([Y, Z, W]).jacobian([tau, rho, v]).det()
        self.assert_zero(determinant - 1)

    def test_deck_involution_obstructs_derivation_descent(self):
        X, Y, v, tau, rho, J = sp.symbols("X Y v tau rho J")
        rho_expression = 2 * tau * (Y - tau * X) - v**2

        def E(expression):
            return sp.diff(expression, X) + tau * sp.diff(expression, Y)

        self.assert_zero(E(rho_expression))
        self.assert_zero(E(tau))
        self.assert_zero(E(v))
        self.assert_zero(E(X) - 1)
        self.assert_zero(E(Y) - tau)
        recovered_Y = (v**2 + rho_expression) / (2 * tau) + tau * X
        self.assert_zero(recovered_Y - Y)
        self.assert_zero((tau**2).subs(tau, -tau) - tau**2)
        self.assert_zero(E(Y).subs(tau, -tau) + E(Y))
        self.assertNotEqual(sp.expand(E(Y).subs(tau, -tau) - E(Y)), 0)
        # After tau inversion the cover derivative has the explicit inverse.
        self.assert_zero(sp.diff(tau**2 - J, tau) / (2 * tau) - 1)
        # These identities do not replace the symbolic field-degree proof.
        self.assertNotEqual(sp.diff(tau**2 - J, tau).subs(tau, 0), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
