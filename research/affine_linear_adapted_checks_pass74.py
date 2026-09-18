"""Exact actual affine-action controls for the separate degree-bound proof.

Finite examples verify projection/inverse identities, not the universal
affine-linear argument or a sharp degree bound. No research modules are
imported. The second method retains the fixed-point and non-LND boundaries.
"""

import unittest

import sympy as sp


class AffineLinearAdaptedChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_actual_flows_projections_and_supplied_slice_inverses(self):
        x = sp.Matrix(sp.symbols("x0:4"))
        U1, U2, U3, S, time, other_time = sp.symbols("U1 U2 U3 S time other_time")
        target = sp.Matrix([U1, U2, U3, S])
        jordan = sp.zeros(4)
        for row in range(1, 4):
            jordan[row, row - 1] = 1
        split = sp.zeros(4)
        split[1, 0], split[3, 2] = 1, 1
        change = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0],
                            [0, 0, 1, 1], [0, 0, 0, 1]])
        shift = sp.Matrix([2, -1, 3, 1])
        cases = ((jordan, sp.eye(4), sp.zeros(4, 1)),
                 (split, change, shift))

        for original_N, linear_change, translation in cases:
            with self.subTest(matrix=original_N):
                inverse_change = linear_change.inv()
                N = linear_change * original_N * inverse_change
                p = linear_change[:, 0] - N * translation
                ell = inverse_change[0, :]
                velocity = N * x + p
                self.assert_zero(N**4)
                self.assert_zero(ell * N)
                self.assert_zero((ell * p)[0] - 1)
                self.assertGreater(N.row_join(p).rank(), N.rank())

                def act(expression):
                    return sum(value * sp.diff(expression, variable)
                               for variable, value in zip(x, velocity))

                def flow(point, parameter):
                    return sum((parameter**power / sp.factorial(power) * N**power * point
                                + parameter**(power + 1) / sp.factorial(power + 1) * N**power * p
                                for power in range(4)), sp.zeros(4, 1))

                w = (ell * x)[0]
                self.assert_zero(act(w) - 1)
                self.assert_zero(flow(flow(x, other_time), time) - flow(x, time + other_time))
                self.assert_zero(flow(x, 0) - x)
                self.assert_zero(flow(x, time).diff(time)
                                 - N * flow(x, time) - p)
                self.assert_zero((ell * flow(x, time))[0] - w - time)
                projection = flow(x, -w).applyfunc(sp.expand)
                self.assert_zero(ell * projection)
                self.assert_zero(projection.applyfunc(act))
                self.assert_zero(flow(projection, w) - x)
                self.assert_zero(projection.subs(dict(zip(x, flow(x, time))), simultaneous=True) - projection)
                self.assertLessEqual(max(sp.Poly(entry, *x).total_degree() for entry in projection), 4)

                invariants = (inverse_change * projection)[1:, :]
                section = linear_change * sp.Matrix([0, U1, U2, U3])
                self.assert_zero(ell * section)
                # This is a genuinely supplied polynomial slice, not
                # merely the linear slice chosen for the construction.
                supplied = sp.expand(w + invariants[0]**2 + invariants[1])
                self.assert_zero(act(supplied) - 1)
                h = sp.expand(supplied.subs(dict(zip(x, section)), simultaneous=True))
                self.assert_zero(h - U1**2 - U2)
                self.assert_zero(supplied - w - h.subs({U1: invariants[0], U2: invariants[1],
                                                       U3: invariants[2]}, simultaneous=True))
                degree_slice = sp.Poly(supplied, *x).total_degree()
                self.assertLessEqual(sp.Poly(h, U1, U2, U3).total_degree(), degree_slice)
                forward = invariants.col_join(sp.Matrix([supplied]))
                inverse = flow(section, S - h).applyfunc(sp.expand)
                self.assert_zero(forward.subs(dict(zip(x, inverse)), simultaneous=True) - target)
                self.assert_zero(inverse.subs(dict(zip(target, forward)), simultaneous=True) - x)
                self.assert_zero(forward.applyfunc(act) - sp.Matrix([0, 0, 0, 1]))
                self.assertLessEqual(max(sp.Poly(entry, *x).total_degree() for entry in forward),
                                     max(4, degree_slice))
                self.assertLessEqual(max(sp.Poly(entry, *target).total_degree() for entry in inverse),
                                     4 * degree_slice)
                current = x
                for _ in range(5):
                    current = current.applyfunc(act)
                self.assert_zero(current)
                if original_N == jordan:
                    self.assert_zero((N**3 * p) - sp.Matrix([0, 0, 0, 1]))
                    self.assertEqual(sp.degree(flow(x, time)[3], time), 4)

    def test_fixed_point_and_non_nilpotent_boundaries(self):
        x = sp.Matrix(sp.symbols("x0:4"))
        N = sp.zeros(4)
        N[1, 0], N[3, 2] = 1, 1
        q = sp.Matrix([1, 2, 3, 4])
        p = N * q
        velocity = N * x + p
        self.assert_zero(N**2)
        self.assert_zero(velocity.subs(dict(zip(x, -q)), simultaneous=True))
        linear = sp.Matrix([sp.symbols("l0:4")])
        equations = list(linear * N) + [(linear * p)[0] - 1]
        self.assertEqual(sp.linsolve(equations, tuple(linear)), sp.EmptySet)
        # At this actual zero of the vector field, every polynomial
        # derivative vanishes. A displayed probe is only a finite check.
        probe = x[0]**3 * x[1] + x[2] * x[3]**2 + x[1]
        derivative = sum(value * sp.diff(probe, variable) for variable, value in zip(x, velocity))
        self.assert_zero(derivative.subs(dict(zip(x, -q)), simultaneous=True))

        # A linear slice alone does not force local nilpotence.
        bad_N = sp.diag(1, 0, 0, 0)
        bad_p = sp.Matrix([0, 1, 0, 0])
        bad_velocity = bad_N * x + bad_p

        def bad_act(expression):
            return sum(value * sp.diff(expression, variable) for variable, value in zip(x, bad_velocity))

        self.assert_zero(bad_act(x[1]) - 1)
        self.assert_zero(bad_act(x[0]) - x[0])
        self.assertNotEqual(x[0], 0)
        self.assertGreater(bad_N.row_join(bad_p).rank(), bad_N.rank())
        self.assertNotEqual(bad_N**4, sp.zeros(4))


if __name__ == "__main__":
    unittest.main()
