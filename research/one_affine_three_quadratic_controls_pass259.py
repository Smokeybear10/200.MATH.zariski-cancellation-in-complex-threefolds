"""Finite exact-algebra controls for the supplied 1222 frontier in pass259.

This standalone source imports no retained solver or checker.  Its examples
and identities do not prove the common invariant-field theorem, the universal
localization/return argument, or recognition of an arbitrary actual frame.
In particular, a nonzero determinant is not a unit-determinant certificate.

Source-only handoff: the author has not executed, imported, or compiled this
saved file.  Root owns the sole canonical execution after full source review.
"""

import unittest

import sympy as sp


class OneAffineThreeQuadraticControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def assert_vector_zero(self, vector):
        for entry in vector:
            self.assert_zero(entry)

    @staticmethod
    def higher_shift_frame():
        u, t, y, z = sp.symbols("u t y z")
        X, Y, Z, W = sp.symbols("X Y Z W")
        forward = sp.Matrix(
            [
                u,
                y + t * u**2,
                z + t**2 * u**2,
                t + u**2 * (z + t**2 * u**2) - (y + t * u**2) ** 2,
            ]
        )
        invariant = W - X**2 * Z + Y**2
        inverse = sp.Matrix(
            [
                X,
                invariant,
                Y - invariant * X**2,
                Z - invariant**2 * X**2,
            ]
        )
        return (u, t, y, z), (X, Y, Z, W), forward, inverse

    def test_higher_shift_actual_inverse_and_leaders(self):
        source, target, forward, inverse = self.higher_shift_frame()
        u, t, y, z = source
        X, Y, Z, W = target
        forward_substitution = dict(zip(target, forward))
        inverse_substitution = dict(zip(source, inverse))
        self.assert_vector_zero(
            inverse.subs(forward_substitution, simultaneous=True)
            - sp.Matrix(source)
        )
        self.assert_vector_zero(
            forward.subs(inverse_substitution, simultaneous=True)
            - sp.Matrix(target)
        )
        self.assert_zero(forward.jacobian(source).det() - 1)
        self.assert_zero(forward[3] - (t - y**2 + (z - 2 * t * y) * u**2))
        self.assertEqual([sp.degree(entry, u) for entry in forward], [1, 2, 2, 2])
        leaders = [sp.Poly(entry, u).LC() for entry in forward]
        self.assert_vector_zero(sp.Matrix(leaders) - sp.Matrix([1, t, t**2, z - 2*t*y]))

        # Literal initial relation only.  This check does not establish that
        # the principal ideal is the full initial kernel; that is written input.
        tau = sp.symbols("tau")
        initial = dict(zip(target, [tau, t*tau**2, t**2*tau**2, (z-2*t*y)*tau**2]))
        self.assert_zero((X**2 * Z - Y**2).subs(initial, simultaneous=True))

    def test_higher_shift_literal_partials_and_exact_top_vectors(self):
        source, target, forward, inverse = self.higher_shift_frame()
        u, t, y, z = source
        substitution = dict(zip(target, forward))
        # In this explicit automorphism, A=C[t,y,z] and T_i(u)=0.
        # Thus the maximum on these three generators is the exact shift.
        intrinsic = (t, y, z)
        N = sp.Matrix([0, 1, 2*t])
        expected_tops = (-2*t*N, N, -N)
        expected_shifts = (4, 4, 2)
        tops = []
        for variable, shift, expected in zip(
            target[1:], expected_shifts, expected_tops
        ):
            pulled = sp.Matrix(
                [
                    sp.expand(
                        sp.diff(entry, variable).subs(substitution, simultaneous=True)
                    )
                    for entry in inverse
                ]
            )
            self.assert_zero(pulled[0])
            self.assertEqual(max(sp.degree(entry, u) for entry in pulled[1:]), shift)
            top = sp.Matrix([sp.expand(entry).coeff(u, shift) for entry in pulled[1:]])
            self.assert_vector_zero(top - expected)
            tops.append(top)
        for i in range(3):
            for j in range(i + 1, 3):
                bracket = tops[j].jacobian(intrinsic) * tops[i]
                bracket -= tops[i].jacobian(intrinsic) * tops[j]
                self.assert_vector_zero(bracket)
        self.assert_zero((N.T * sp.Matrix([sp.diff(t, v) for v in intrinsic]))[0])

    def test_parameter_jacobian_factor_and_failed_return_negative(self):
        t, r, s, alpha, beta = sp.symbols("t r s alpha beta")
        Q = sp.Matrix([sp.Function(f"Q{i}")(t) for i in range(3)])
        S = sp.Matrix([sp.Function(f"S{i}")(t) for i in range(3)])
        T = sp.Matrix([sp.Function(f"T{i}")(t) for i in range(3)])
        # Differentiate the full parametrization, rather than inputting its
        # determinant coefficients as a purported independent reconstruction.
        parameter_map = T + S.diff(t)*r + Q.diff(t, 2)*r**2/2 + Q.diff(t)*s
        actual_matrix = parameter_map.jacobian((t, r, s))
        Q1, Q2, Q3, S1, S2, T1 = (
            sp.Matrix(sp.symbols(f"{name}_0:3"))
            for name in ("q1", "q2", "q3", "s1", "s2", "t1")
        )
        jet_substitution = {}
        for functions, order, jets in (
            (Q, 1, Q1), (Q, 2, Q2), (Q, 3, Q3),
            (S, 1, S1), (S, 2, S2), (T, 1, T1),
        ):
            jet_substitution.update(
                {sp.diff(functions[i], t, order): jets[i] for i in range(3)}
            )
        actual_matrix = actual_matrix.xreplace(jet_substitution)
        expected_matrix = sp.Matrix.hstack(
            T1 + S2*r + Q3*r**2/2 + Q2*s, S1 + Q2*r, Q1
        )
        self.assert_vector_zero(actual_matrix - expected_matrix)
        jacobian = sp.expand(actual_matrix.det())
        self.assert_zero(jacobian.coeff(s, 1) - sp.Matrix.hstack(Q2, S1, Q1).det())
        self.assert_zero(
            jacobian.subs({r: 0, s: 0}) - sp.Matrix.hstack(T1, S1, Q1).det()
        )
        self.assertEqual(sp.degree(jacobian, s), 1)

        dependent_second = alpha*S1 + beta*Q1
        relation = dict(zip(Q2, dependent_second))
        reduced_matrix = actual_matrix.subs(relation, simultaneous=True)
        reduced_det = reduced_matrix.det()
        expected_factorization = (1 + alpha*r) * sp.Matrix.hstack(
            reduced_matrix[:, 0], S1, Q1
        ).det()
        self.assert_zero(reduced_det - expected_factorization)
        # If alpha is nonzero this factor has positive r-degree.  The proof
        # needs invertibility in F[r,s], not merely nonzero determinant in K.
        self.assertEqual(sp.degree(1 + alpha*r, r), 1)
        self.assertEqual((1 + alpha*r).subs(alpha, 0), 1)

        # Nonlinear Q and nonzero J are compatible without inverse ring return.
        negative_Q = sp.Matrix([t, t**2/2, 0])
        negative_S = sp.Matrix([0, t, 0])
        negative_T = sp.Matrix([0, 0, t])
        negative = (
            negative_T + negative_S.diff(t)*r
            + negative_Q.diff(t, 2)*r**2/2 + negative_Q.diff(t)*s
        )
        self.assert_vector_zero(negative - sp.Matrix([s, r + r**2/2 + t*s, t]))
        bad_det = sp.expand(negative.jacobian((t, r, s)).det())
        self.assert_zero(bad_det + 1 + r)
        self.assertNotEqual(bad_det, 0)
        self.assertEqual(sp.Poly(bad_det, r, s).total_degree(), 1)
        self.assert_vector_zero(negative.subs(r, -2-r) - negative)
        self.assert_zero((r+1)**2 - (1 + 2*(negative[1] - negative[2]*negative[0])))
        self.assert_zero(bad_det.subs(r, -1))
        # The displayed nontrivial involution fixes all p_i.  In particular
        # neither inverse-field nor inverse-polynomial-ring return holds.

    def test_actual_all_shift_one_jordan_frame(self):
        x, p1, p2, p3 = sp.symbols("x p1 p2 p3")
        X, Y1, Y2, Y3 = sp.symbols("X Y1 Y2 Y3")
        p = sp.Matrix([p1, p2, p3])
        Y = sp.Matrix([Y1, Y2, Y3])
        jordan = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
        change = sp.Matrix([[1, 0, 0], [1, 1, 1], [1, 2, 4]])
        B = change * jordan * change.inv()
        sigma, q = B*p, B**2*p
        forward_Y = p + x*sigma + x**2*q
        inverse_p = (sp.eye(3) - X*B)*Y
        forward = sp.Matrix([x, *forward_Y])
        inverse = sp.Matrix([X, *inverse_p])
        source, target = (x, p1, p2, p3), (X, Y1, Y2, Y3)
        self.assert_vector_zero(
            inverse.subs(dict(zip(target, forward)), simultaneous=True) - sp.Matrix(source)
        )
        self.assert_vector_zero(
            forward.subs(dict(zip(source, inverse)), simultaneous=True) - sp.Matrix(target)
        )
        self.assert_vector_zero(B**3)
        self.assertEqual(B.rank(), 2)
        self.assertEqual((B**2).rank(), 1)
        self.assert_zero(forward.jacobian(source).det() - 1)
        self.assertEqual([sp.degree(entry, x) for entry in forward], [1, 2, 2, 2])
        self.assert_vector_zero(q - sp.ones(3, 1)*(p1-2*p2+p3)/2)
        for entry in q:
            self.assertNotEqual(sp.Poly(entry, p1, p2, p3).total_degree(), 0)
        self.assert_vector_zero(q.jacobian(p) - sigma.jacobian(p)**2)
        self.assert_vector_zero(
            forward_Y.jacobian(p)*(sp.eye(3) - x*B) - sp.eye(3)
        )
        tops = []
        for j, variable in enumerate(target[1:]):
            column = inverse_p.diff(variable)
            self.assertEqual(max(sp.degree(entry, X) for entry in column), 1)
            top = sp.Matrix([sp.expand(entry).coeff(X, 1) for entry in column])
            self.assert_vector_zero(top + B[:, j])
            tops.append(top)
        for i in range(3):
            for j in range(i+1, 3):
                self.assertEqual(sp.Matrix.hstack(tops[i], tops[j]).rank(), 2)
        # Here a=EX=1.  This actual family validates the all-one shift pattern;
        # it is not evidence that the nonunit-speed recognition proof is formal.


if __name__ == "__main__":
    unittest.main()
