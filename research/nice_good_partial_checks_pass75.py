"""One actual reused-action control for two good-partial shortcuts.

The field derived from a genuine good coordinate partial need not be
nice in that frame or fix the supplied E-slice. This example is already
polynomially conjugate to a translation; no new hard action is claimed.
"""

import unittest

import sympy as sp


class NiceGoodPartialChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_actual_partial_derived_field_and_both_failed_shortcuts(self):
        x, y, z, w, time = sp.symbols("x y z w time")
        variables = sp.Matrix([x, y, z, w])
        a = x*z-y**2+w
        P = sp.Matrix([1, a, a**2, -a**2*x+2*a*y-z])
        jacobian = P.jacobian(variables)
        Q = P.diff(w)

        def act(field, expression):
            return sp.expand(sum(value*sp.diff(expression, variable)
                                 for variable, value in zip(variables, field)))

        self.assert_zero(Q-sp.Matrix([0, 1, 2*a, -2*a*x+2*y]))
        self.assert_zero(P.applyfunc(lambda entry: act(P, entry)))
        self.assert_zero(P.applyfunc(lambda entry: act(Q, entry)))
        self.assert_zero(Q.applyfunc(lambda entry: act(P, entry)))
        self.assert_zero(Q.applyfunc(lambda entry: act(P, entry))
                         - P.applyfunc(lambda entry: act(Q, entry)))
        second_Q = Q.applyfunc(lambda entry: act(Q, entry))
        self.assert_zero(second_Q-sp.Matrix([0, 0, 0, 2]))
        self.assert_zero(second_Q.applyfunc(lambda entry: act(Q, entry)))
        self.assertEqual(act(Q, act(Q, w)), 2)
        self.assertEqual(P.row_join(Q).rank(), 2)

        # The field is obtained from an actual original good partial,
        # not a rationally normalized or arbitrarily chosen centralizer.
        self.assert_zero(-jacobian[:, 3]+Q)
        self.assert_zero(2*jacobian**2*sp.Matrix([0, 0, 0, 1]))
        self.assert_zero((jacobian**2)[1, :]-sp.Matrix([[-a**2, 2*a, -1, 0]]))
        self.assertNotEqual(Q[1], 0)

        S, A, Y, Z = sp.symbols("S A Y Z")
        target = sp.Matrix([S, A, Y, Z])
        invariant_Y, invariant_Z = y-x*a, z-x*a**2
        forward = sp.Matrix([x, a, invariant_Y, invariant_Z])
        inverse = sp.Matrix([S, Y+S*A, Z+S*A**2,
                             A-S*Z+Y**2+2*S*A*Y])
        self.assert_zero(forward.subs(dict(zip(variables, inverse)), simultaneous=True)-target)
        self.assert_zero(inverse.subs(dict(zip(target, forward)), simultaneous=True)-variables)
        self.assert_zero(forward.jacobian(variables)*P-sp.Matrix([1, 0, 0, 0]))
        self.assert_zero(forward.jacobian(variables)*Q-sp.Matrix([0, 0, 1, 2*a]))
        supplied_slice = x+invariant_Y
        self.assertEqual(act(P, supplied_slice), 1)
        self.assertEqual(act(Q, supplied_slice), 1)
        self.assertEqual(act(Q, x), 0)

        # Both are actual polynomial flows with two-sided polynomial inverses.
        for field, acceleration in ((P, sp.zeros(4, 1)), (Q, second_Q)):
            flow = variables+time*field+time**2*acceleration/2
            inverse_flow = variables-time*field+time**2*acceleration/2
            self.assert_zero(flow.subs(dict(zip(variables, inverse_flow)),
                                      simultaneous=True)-variables)
            self.assert_zero(inverse_flow.subs(dict(zip(variables, flow)),
                                              simultaneous=True)-variables)
            self.assert_zero(flow.diff(time)-field.subs(dict(zip(variables, flow)),
                                                        simultaneous=True))


if __name__ == "__main__":
    unittest.main(verbosity=2)
