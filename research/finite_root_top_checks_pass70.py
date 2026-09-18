"""Exact finite-root controls, not full-frame realizations.

The actual sliced triangular examples for m=3,4 fail the required
adjoint profile. Constant-field and nonnormal-ring controls deliberately
change hypotheses. Written separability, constants and normality
arguments are not claimed proved by finite symbolic tests.
"""

import unittest

import sympy as sp


class FiniteRootTopChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_extended_original_partials_and_actual_flow_chain_rule(self):
        g, b, x, s, time = sp.symbols("g b x s time")
        root_coordinates = sp.Matrix([g, b, x, s])
        a, root_symbol = sp.symbols("a root_symbol")
        zero = sp.zeros(4, 1)
        for order in (3, 4):
            with self.subTest(order=order):
                original_coordinates = sp.Matrix([g**order, b, x, s])
                # Columns are the extensions of the ORIGINAL (a,b,x,s)
                # partials. The first is not the root-coordinate partial.
                partials = sp.diag(1 / (order * g**(order - 1)), 1, 1, 1)

                def apply(field, polynomial):
                    return sp.cancel(sum(field[i] * sp.diff(polynomial, variable)
                                         for i, variable in enumerate(root_coordinates)))

                def bracket(first, second):
                    return sp.Matrix([apply(first, second[i]) - apply(second, first[i])
                                      for i in range(4)])

                def original_jacobian(functions):
                    return sp.Matrix([[apply(partials[:, j], entry) for j in range(4)]
                                      for entry in functions])

                self.assert_zero(original_jacobian(original_coordinates) - sp.eye(4))
                for i in range(4):
                    for j in range(4):
                        self.assert_zero(bracket(partials[:, i], partials[:, j]))
                self.assert_zero(order * g**(order - 1) * apply(partials[:, 0], g) - 1)
                self.assertNotEqual(apply(partials[:, 0], g), 1)

                # Verify the algebraic differential formula before eliminating
                # a, so root-coordinate differentiation cannot replace T_a.
                rational = (a + b * s) / (x + 1) + root_symbol
                chain = (sp.diff(rational, a) + sp.diff(rational, root_symbol)
                         / (order * root_symbol**(order - 1)))
                embedding = {a: g**order, root_symbol: g}
                self.assert_zero(apply(partials[:, 0], rational.subs(embedding))
                                 - chain.subs(embedding))

                action = sp.Matrix([
                    0, 0, g**order * s**(order - 1) / sp.factorial(order - 1), 1,
                ])
                delta = action / g
                self.assert_zero(apply(action, s) - 1)
                self.assert_zero(apply(action, g))
                self.assert_zero(apply(delta, g))

                original_heights, normalized_heights = [], []
                conjugated_columns = []
                for j in range(4):
                    for field, heights in ((action, original_heights),
                                           (delta, normalized_heights)):
                        current = partials[:, j]
                        degree = 0
                        conjugated = zero.copy()
                        for k in range(order + 2):
                            if current != zero:
                                degree = k
                            if field == delta:
                                conjugated += time**k / sp.factorial(k) * sp.Matrix([
                                    apply(current, entry) for entry in original_coordinates
                                ])
                            current = bracket(field, current)
                        self.assert_zero(current)
                        heights.append(degree)
                        if field == delta:
                            conjugated_columns.append(conjugated)
                self.assertEqual(original_heights, [order, 0, 0, order - 1])
                self.assertEqual(normalized_heights, [order, 0, 0, order - 1])

                iterate = original_coordinates
                divided_iterate = original_coordinates
                for _ in range(order):
                    iterate = sp.Matrix([apply(action, entry) for entry in iterate])
                    divided_iterate = sp.Matrix([apply(delta, entry) for entry in divided_iterate])
                self.assert_zero(iterate - sp.Matrix([0, 0, g**order, 0]))
                self.assert_zero(divided_iterate - sp.Matrix([0, 0, 1, 0]))

                flow = sp.Matrix([
                    g, b,
                    x + g**order * ((s + time / g)**order - s**order) / sp.factorial(order),
                    s + time / g,
                ])
                inverse_flow = flow.subs(time, -time)
                self.assert_zero(flow.subs(dict(zip(root_coordinates, inverse_flow)),
                                          simultaneous=True) - root_coordinates)
                self.assert_zero(inverse_flow.subs(dict(zip(root_coordinates, flow)),
                                                  simultaneous=True) - root_coordinates)
                for i, entry in enumerate(flow):
                    self.assert_zero(sp.diff(entry, time)
                                     - delta[i].subs(dict(zip(root_coordinates, flow)),
                                                     simultaneous=True))
                original_flow = sp.Matrix([g**order, flow[1], flow[2], flow[3]])
                jacobian = original_jacobian(original_flow)
                conjugated = sp.Matrix.hstack(*conjugated_columns)
                self.assert_zero(jacobian * conjugated - sp.eye(4))
                self.assert_zero(conjugated * jacobian - sp.eye(4))
                self.assertEqual(sp.cancel(jacobian.det()), 1)
                inverse_jacobian = original_jacobian(
                    sp.Matrix([g**order, inverse_flow[1], inverse_flow[2], inverse_flow[3]])
                ).subs(dict(zip(root_coordinates, flow)), simultaneous=True)
                self.assert_zero(jacobian * inverse_jacobian - sp.eye(4))
                self.assert_zero(inverse_jacobian * jacobian - sp.eye(4))

    def test_constant_field_and_polynomial_root_descent_boundaries(self):
        a, root, g, omega = sp.symbols("a root g omega")
        u, v, t = sp.symbols("u v t")
        scale = sp.Symbol("scale", nonzero=True)
        for order in (3, 4):
            with self.subTest(order=order):
                minimum = sp.Poly(root**order - a, root, domain=sp.QQ.frac_field(a))
                self.assertTrue(minimum.is_irreducible)
                root_derivative = 1 / (order * g**(order - 1))
                self.assert_zero(sp.diff(minimum.as_expr(), root).subs(root, g)
                                 * root_derivative + sp.diff(minimum.as_expr(), a))
                # A nonconstant root is not a new differential constant.
                self.assertNotEqual(root_derivative, 0)
                cyclotomic = sp.cyclotomic_poly(order, omega)
                self.assert_zero(sp.rem((omega * g)**order - g**order, cyclotomic, omega))
                self.assertNotEqual(sp.rem((omega * g)**(order - 1) - g**(order - 1),
                                           cyclotomic, omega), 0)

                # Repeated factors are retained, not replaced by reduced
                # divisors in the actual root-recovery identity.
                polynomial_root = (u + v**2)**2 * v**3
                top = polynomial_root**order
                preceding = scale * polynomial_root**(order - 1)
                recovered = sp.cancel(scale * top / preceding)
                self.assert_zero(recovered - polynomial_root)
                self.assert_zero(recovered**order - top)

                # The same fraction-and-integrality data alone do not give
                # membership in the nonnormal cusp C[t^2,t^3].
                cusp_top, cusp_preceding = t**order, t**(order - 1)
                self.assert_zero(cusp_top / cusp_preceding - t)
                self.assert_zero(t**order - cusp_top)
                F = sp.Function("F")
                self.assert_zero(sp.diff(F(t**2, t**3), t).subs(t, 0))
                self.assertEqual(sp.diff(t, t).subs(t, 0), 1)

        # Over Q, adjoining a root of a constant polynomial produces an
        # algebraic constant. Over C these roots were already in the base.
        constant_root = sp.Symbol("constant_root")
        constant_minimum = sp.Poly(constant_root**2 - 2, constant_root, domain=sp.QQ)
        self.assertTrue(constant_minimum.is_irreducible)
        for original_variable in (a, u, v, t):
            self.assert_zero(sp.diff(constant_minimum.as_expr(), original_variable))
        self.assertEqual(constant_minimum.degree(), 2)

        # A selected fourth root may generate only a quadratic extension.
        # Differentiate its quartic relation without assuming it is minimal.
        quartic = sp.Poly(root**4 - a**2, root, domain=sp.QQ.frac_field(a))
        quadratic = sp.Poly(root**2 - a, root, domain=sp.QQ.frac_field(a))
        self.assertFalse(quartic.is_irreducible)
        self.assertTrue(quadratic.is_irreducible)
        from_quartic = (sp.diff(a**2, a) / (4 * g**3)).subs(a, g**2)
        self.assert_zero(from_quartic - 1 / (2 * g))


if __name__ == "__main__":
    unittest.main()
