"""Three exact actual-frame controls for the pass126 cofactor bounds.

The first derives all four coordinate partials from an inverse Jacobian and
checks their brackets, filtration shifts, common intrinsic direction, height,
and the inverse-flow-Jacobian orientation. The second is a separate actual
rank-one speed family with a direct exterior-minor cancellation check.
The third checks the joint-curve determinant and commutator identities in an
actual frame with the original coordinate X as a slice. It is recognized and
does not realize an unresolved height profile such as (1, 2, 2, 2).
These polynomial examples do not certify the universal rank bounds, kernel
recognition, historical novelty, or arbitrary-frame entry. No prior checker
or research solver is imported. Execution is left to the canonical runner.
"""

import unittest

import sympy as sp


class ThreeGoodCofactorChecks(unittest.TestCase):
    @staticmethod
    def expanded(values):
        return tuple(sp.expand(value) for value in values)

    @staticmethod
    def act(column, value, variables):
        return sp.expand(sum(coefficient * sp.diff(value, variable)
                             for coefficient, variable in zip(column, variables)))

    @classmethod
    def bracket(cls, left, right, variables):
        return sp.Matrix([cls.act(left, value, variables)
                          - cls.act(right, coefficient, variables)
                          for value, coefficient in zip(right, left)])

    def test_full_partial_frame_shifts_and_flow_cofactors(self):
        a, b, c, u, time = sp.symbols("a b c u time")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted = (a, b, c, u)
        original = (X, Y, Z, W)
        good = (a, b + a**2 * u, c + b * u)
        frame = good + (u + good[2]**2,)
        inv_u = W - Z**2
        inv_b = Y - X**2 * inv_u
        inverse = (X, inv_b, Z - inv_b * inv_u, inv_u)
        forward_sub = dict(zip(original, frame))
        inverse_sub = dict(zip(adapted, inverse))
        self.assertEqual(self.expanded(value.subs(forward_sub, simultaneous=True)
                                       for value in inverse), adapted)
        self.assertEqual(self.expanded(value.subs(inverse_sub, simultaneous=True)
                                       for value in frame), original)

        jacobian = sp.Matrix(frame).jacobian(adapted)
        self.assertEqual(sp.expand(jacobian.det()), 1)
        partial_matrix = jacobian.inv().applyfunc(sp.cancel)
        inverse_jacobian = sp.Matrix(inverse).jacobian(original)
        recovered_partials = inverse_jacobian.subs(
            forward_sub, simultaneous=True).applyfunc(sp.expand)
        self.assertEqual((partial_matrix - recovered_partials).applyfunc(sp.expand),
                         sp.zeros(4))
        for coefficient in partial_matrix:
            self.assertEqual(sp.denom(coefficient), 1)
        partials = [partial_matrix[:, index] for index in range(4)]
        expected = [
            sp.Matrix([1, -2*a*u, 2*a*u**2, 0]),
            sp.Matrix([0, 1, -u, 0]),
            sp.Matrix([0, 2*a**2*(c+b*u),
                       1-2*a**2*(c+b*u)*u+2*b*(c+b*u), -2*(c+b*u)]),
            sp.Matrix([0, -a**2, a**2*u-b, 1]),
        ]
        for index, column in enumerate(partials):
            self.assertEqual((column - expected[index]).applyfunc(sp.expand), sp.zeros(4, 1))
            self.assertEqual(self.expanded(self.act(column, value, adapted) for value in frame),
                             tuple(int(index == row) for row in range(4)))
        for i in range(4):
            for j in range(i):
                self.assertEqual(self.bracket(partials[i], partials[j], adapted), sp.zeros(4, 1))

        shifts = []
        E = sp.Matrix([0, 0, 0, 1])
        expected_shifts = (2, 1, 2, 1)
        top_coefficients = (2*a, sp.Integer(-1), -2*a**2*b, a**2)
        for index, column in enumerate(partials):
            shift = max([sp.Poly(value, u).degree() for value in column[:3]]
                        + [sp.Poly(column[3], u).degree() - 1])
            shifts.append(shift)
            self.assertEqual(shift, expected_shifts[index])
            intrinsic_top = sp.Matrix([sp.Poly(value, u).coeff_monomial(u**shift)
                                       for value in column[:3]])
            self.assertEqual(intrinsic_top, sp.Matrix([0, 0, top_coefficients[index]]))
            iterated = column
            for order in range(1, shift + 2):
                iterated = self.bracket(E, iterated, adapted)
                self.assertEqual(iterated, column.diff(u, order).applyfunc(sp.expand))
                if order == shift:
                    self.assertNotEqual(iterated, sp.zeros(4, 1))
                if order == shift + 1:
                    self.assertEqual(iterated, sp.zeros(4, 1))
        self.assertEqual(tuple(shifts), expected_shifts)
        self.assertEqual(sum(shift + 1 for shift in shifts), 10)
        speeds = sp.Matrix([sp.diff(value, u) for value in good])
        acceleration = sp.expand(sp.diff(frame[3], u, 2))
        self.assertEqual(speeds, sp.Matrix([0, a**2, b]))
        self.assertEqual(acceleration, 2*b**2)
        self.assertEqual(speeds.jacobian(adapted).rank(), 2)
        for multiplier in top_coefficients:
            for value in tuple(speeds) + (acceleration,):
                self.assertEqual(sp.expand(multiplier * sp.diff(value, c)), 0)

        # Compute the original-frame flow first, then differentiate that flow.
        flow = sp.Matrix([sp.expand(value.subs(u, u+time).subs(
            inverse_sub, simultaneous=True)) for value in frame])
        original_flow_jacobian = flow.jacobian(original)
        flow_jacobian = original_flow_jacobian.subs(
            forward_sub, simultaneous=True).applyfunc(sp.expand)
        self.assertEqual(sp.expand(flow_jacobian.det()), 1)
        inverse_flow_jacobian = flow_jacobian.adjugate().applyfunc(sp.expand)
        conjugated_adapted = partial_matrix.subs(u, u+time).applyfunc(sp.expand)
        conjugated_original = (jacobian * conjugated_adapted).applyfunc(sp.expand)
        self.assertEqual(conjugated_original, inverse_flow_jacobian)
        self.assertEqual((flow_jacobian * conjugated_original).applyfunc(sp.expand), sp.eye(4))
        for index, theorem_bound in enumerate((3, 3, 3, 2)):
            degree = max(sp.Poly(value, time).degree()
                         for value in conjugated_original[:, index])
            self.assertEqual(degree, expected_shifts[index])
            self.assertLessEqual(degree, theorem_bound)

    def test_actual_rank_one_family_exterior_minor_cancellation(self):
        a, b, c, u, time = sp.symbols("a b c u time")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted = (a, b, c, u)
        original = (X, Y, Z, W)
        f, g = a**2 + a, a**3 + 2
        frame = (u, b + f*u, c + g*u, a + u**2)
        inv_a = W - X**2
        inverse = (inv_a, Y - f.subs(a, inv_a)*X,
                   Z - g.subs(a, inv_a)*X, X)
        self.assertEqual(self.expanded(value.subs(dict(zip(original, frame)), simultaneous=True)
                                       for value in inverse), adapted)
        self.assertEqual(self.expanded(value.subs(dict(zip(adapted, inverse)), simultaneous=True)
                                       for value in frame), original)
        jacobian = sp.Matrix(frame).jacobian(adapted)
        self.assertEqual(sp.expand(jacobian.det()), -1)
        bad_partial = jacobian.inv()[:, 3].applyfunc(sp.expand)
        expected_partial = sp.Matrix([1, -u*sp.diff(f, a), -u*sp.diff(g, a), 0])
        self.assertEqual((bad_partial - expected_partial).applyfunc(sp.expand), sp.zeros(4, 1))
        top = sp.Matrix([0, -sp.diff(f, a), -sp.diff(g, a), 0])
        self.assertEqual((bad_partial.subs(u, u+time) - bad_partial
                          - time * top).applyfunc(sp.expand), sp.zeros(4, 1))

        speeds = sp.Matrix([sp.diff(value, u) for value in frame[:3]])
        self.assertEqual(speeds, sp.Matrix([1, f, g]))
        update_rows = speeds.jacobian(adapted)
        self.assertEqual(update_rows.rank(), 1)
        good_rows = sp.Matrix(frame[:3]).jacobian(adapted)
        wedge_rows = good_rows + time*update_rows
        # These four minors are the coordinates of the actual good-row wedge.
        # The two nonconstant speed differentials are both multiples of da.
        first_order_nonzero = False
        for omitted in range(4):
            minor = sp.expand(wedge_rows[:, [j for j in range(4) if j != omitted]].det())
            polynomial = sp.Poly(minor, time)
            self.assertEqual(polynomial.coeff_monomial(time**2), 0)
            self.assertEqual(polynomial.coeff_monomial(time**3), 0)
            self.assertLessEqual(polynomial.degree(), 1)
            first_order_nonzero |= polynomial.coeff_monomial(time) != 0
        self.assertTrue(first_order_nonzero)

    def test_joint_curve_determinant_and_commutator_identities(self):
        a, b, c, u, time, parameter = sp.symbols("a b c u time parameter")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted = (a, b, c, u)
        original = (X, Y, Z, W)
        good = (u, b + a*u, c + a**2*u)
        frame = good + (a + good[1]**2,)
        p = W - Y**2
        inverse = (p, Y-p*X, Z-p**2*X, X)
        forward_sub = dict(zip(original, frame))
        inverse_sub = dict(zip(adapted, inverse))
        self.assertEqual(self.expanded(value.subs(forward_sub, simultaneous=True)
                                       for value in inverse), adapted)
        self.assertEqual(self.expanded(value.subs(inverse_sub, simultaneous=True)
                                       for value in frame), original)
        self.assertEqual(sp.expand(sp.Matrix(frame).jacobian(adapted).det()), -1)

        E = sp.Matrix([sp.expand(sp.diff(value, u).subs(inverse_sub, simultaneous=True))
                       for value in frame])
        f_parameter = sp.Matrix([1, parameter, parameter**2])
        q_parameter = 2*parameter**2
        f = f_parameter.subs(parameter, p)
        c0 = E[3]
        q = self.act(E, c0, original)
        self.assertEqual((E[:3, :] - f).applyfunc(sp.expand), sp.zeros(3, 1))
        self.assertEqual(sp.expand(c0 - 2*p*Y), 0)
        self.assertEqual(sp.expand(q - q_parameter.subs(parameter, p)), 0)
        self.assertEqual(self.act(E, p, original), 0)
        for value in tuple(f) + (q,):
            self.assertEqual(self.act(E, value, original), 0)
        # X is an actual original-coordinate slice, not just a rational slice.
        self.assertEqual(self.act(E, X, original), 1)

        flow = sp.Matrix([sp.expand(value.subs(u, u+time).subs(
            inverse_sub, simultaneous=True)) for value in frame])
        expected_flow = sp.Matrix(original) + time*E + sp.Matrix([0, 0, 0, time**2*q/2])
        self.assertEqual((flow - expected_flow).applyfunc(sp.expand), sp.zeros(4, 1))
        self.assertEqual(sp.expand(flow.jacobian(original).det()), 1)

        alpha = sp.diff(p, W)
        delta = sp.diff(c0, W)
        f_prime = f_parameter.diff(parameter).subs(parameter, p)
        q_prime = sp.diff(q_parameter, parameter).subs(parameter, p)
        C0 = self.act(f_prime, c0, original[:3])
        self.assertEqual(alpha, 1)
        self.assertEqual(delta, 2*Y)
        self.assertEqual(sp.expand(C0 - (2*p-4*Y**2)), 0)
        self.assertEqual(sp.expand(delta**2-alpha*(q_prime/2-C0)), 0)

        bad_partial = sp.Matrix([0, 0, 0, 1])
        Q = self.bracket(E, bad_partial, original).applyfunc(sp.expand)
        expected_Q = sp.Matrix([-alpha*value for value in f_prime] + [-delta])
        self.assertEqual((Q - expected_Q).applyfunc(sp.expand), sp.zeros(4, 1))
        self.assertEqual(self.act(Q, p, original), 0)
        self.assertEqual(self.act(Q, alpha, original), 0)
        self.assertEqual(sp.expand(self.act(Q, c0, original)+q_prime*alpha/2), 0)
        self.assertEqual(self.bracket(E, Q, original), sp.zeros(4, 1))
        self.assertEqual(sp.expand(self.act(E, delta, original)-q_prime*alpha/2), 0)
        for value in original[:3]:
            self.assertEqual(self.act(Q, self.act(Q, value, original), original), 0)
        self.assertEqual(self.act(Q, self.act(Q, W, original), original), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
