"""Finite exact controls for the supplied speed-curve recognition proof.

The actual frames below have last E-degrees 2, 3, and 5, including a repeated
parameter divisor with nonunit alpha. These finitely many
examples do not prove the all-degree theorem. The independent nilpotent
quotient identities retain multiplicities but are not actual frame examples.
Wronskian controls verify explicit polynomial coordinate changes, while the
rank-two frame demonstrates failure of the rank-one selected-column bound.
The final actual rank-two frame has a unit speed row and shows that the
original last partial need not send the common intrinsic kernel into A.
No recognition theorem, arbitrary-frame entry, or novelty claim is tested.
No earlier checker or research solver is imported. Root owns execution.
"""

import unittest

import sympy as sp


class ThreeGoodSpeedCurveChecks(unittest.TestCase):
    @staticmethod
    def act(column, value, variables):
        return sp.expand(sum(coefficient * sp.diff(value, variable)
                             for coefficient, variable in zip(column, variables)))

    @classmethod
    def bracket(cls, left, right, variables):
        return sp.Matrix([cls.act(left, right[i], variables)
                          - cls.act(right, left[i], variables)
                          for i in range(len(variables))])

    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def assert_matrix_equal(self, left, right):
        self.assertEqual(left.shape, right.shape)
        for value in left - right:
            self.assert_zero(value)

    def assert_inverse_pair(self, frame, inverse, adapted, original):
        forward_sub = dict(zip(original, frame))
        inverse_sub = dict(zip(adapted, inverse))
        for value, target in zip(inverse, adapted):
            self.assert_zero(value.subs(forward_sub, simultaneous=True) - target)
        for value, target in zip(frame, original):
            self.assert_zero(value.subs(inverse_sub, simultaneous=True) - target)

    def test_actual_all_degree_last_coordinate_frames(self):
        a, b, c, u, time = sp.symbols("a b c u time")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, original = (a, b, c, u), (X, Y, Z, W)
        for ell, parameter_degree in ((2, 1), (3, 1), (5, 1), (2, 3)):
            with self.subTest(last_degree=ell, parameter_degree=parameter_degree):
                good = (u, b+a**parameter_degree*u, c+a**(2*parameter_degree)*u)
                frame = good + (a+good[1]**ell,)
                base_parameter = W-Y**ell
                p = base_parameter**parameter_degree
                inverse = (base_parameter, Y-p*X, Z-p**2*X, X)
                self.assert_inverse_pair(frame, inverse, adapted, original)
                forward_sub = dict(zip(original, frame))
                inverse_sub = dict(zip(adapted, inverse))
                self.assert_zero(sp.Matrix(frame).jacobian(adapted).det()+1)
                self.assertEqual(sp.Poly(frame[3], u).degree(), ell)

                E = sp.Matrix([sp.expand(sp.diff(value, u).subs(
                    inverse_sub, simultaneous=True)) for value in frame])
                self.assert_matrix_equal(E, sp.Matrix([1, p, p**2, ell*p*Y**(ell-1)]))
                T = sp.Matrix([0, 0, 0, 1])
                transported_T = sp.Matrix(inverse).jacobian(original)[:, 3].subs(
                    forward_sub, simultaneous=True)
                self.assert_matrix_equal(transported_T, sp.Matrix([
                    1, -parameter_degree*a**(parameter_degree-1)*u,
                    -2*parameter_degree*a**(2*parameter_degree-1)*u, 0]))
                Q = self.bracket(E, T, original)
                alpha = sp.diff(p, W)
                delta = sp.diff(E[3], W)
                self.assert_matrix_equal(Q, sp.Matrix([
                    0, -alpha, -2*p*alpha, -ell*alpha*Y**(ell-1)]))
                self.assert_matrix_equal(self.bracket(E, Q, original), sp.zeros(4, 1))
                f_prime = sp.Matrix([0, 1, 2*p])
                A0 = self.act(f_prime, p, original[:3])
                self.assert_zero(alpha-parameter_degree*base_parameter**(parameter_degree-1))
                self.assert_zero(A0+delta)
                for field in (E, Q):
                    self.assert_zero(self.act(field, p, original))
                    self.assert_zero(self.act(field, alpha, original))
                self.assertEqual(self.act(E, X, original), 1)  # Recognized actual slice.

                flow = sp.Matrix([X+time, Y+time*p, Z+time*p**2,
                                  base_parameter+(Y+time*p)**ell])
                for value, target in zip(flow, frame):
                    self.assert_zero(value.subs(forward_sub, simultaneous=True)
                                     - target.subs(u, u+time))
                flow_jacobian = flow.jacobian(original)
                self.assert_zero(flow_jacobian.det()-1)
                selected_column = sp.Matrix([
                    (-1)**(3+i) * flow_jacobian[:3, [j for j in range(4) if j != i]].det()
                    for i in range(4)])
                self.assert_matrix_equal(selected_column, T+time*Q)
                determinant_reduction = ((1+time*A0)*sp.diff(flow[3], W)
                                         - time*alpha*self.act(f_prime, flow[3], original[:3]))
                self.assert_zero(determinant_reduction-1)
                derivative_polynomial = sp.Poly(sp.diff(flow[3], W), time)
                for j in range(ell+1):
                    error = derivative_polynomial.coeff_monomial(time**j)-delta**j
                    self.assertEqual(sp.rem(error, alpha, W), 0)
                self.assertEqual(sp.rem(delta**(ell+1), alpha, W), 0)
                if parameter_degree == 3:
                    self.assert_zero(alpha-3*base_parameter**2)
                    self.assert_zero(delta-2*Y*alpha)
                    self.assertEqual(sp.rem(delta, base_parameter**2, W), 0)
                    self.assertNotEqual(sp.rem(delta, base_parameter**3, W), 0)
                    for x in original[:3]:
                        self.assert_zero(alpha*sp.diff(p, x, W)
                                         - sp.diff(alpha, W)*sp.diff(p, x))

                # Compute actual iterates independently, then check both scalar recursions.
                iterates = [W]
                for _ in range(ell+1):
                    iterates.append(self.act(E, iterates[-1], original))
                self.assertNotEqual(iterates[ell], 0)
                self.assertEqual(iterates[ell+1], 0)
                for k in range(1, ell+2):
                    previous_Q = self.act(Q, iterates[k-1], original)
                    self.assert_zero(sp.diff(iterates[k], W)+k*previous_Q)
                    self.assert_zero(self.act(Q, iterates[k], original)
                                     + alpha*self.act(f_prime, iterates[k], original[:3])
                                     - k*delta*previous_Q)
                self.assert_zero(self.act(Q, iterates[ell], original))
                self.assert_zero(self.act(Q, self.act(Q, W, original), original)
                                 - ell*(ell-1)*alpha**2*Y**(ell-2))

    def test_full_multiplicity_and_primitive_normal_controls(self):
        epsilon, time, parameter = sp.symbols("epsilon time parameter")
        for ell in (1, 2, 3, 5):
            with self.subTest(nilpotence_index=ell+1):
                alpha, delta = epsilon**(ell+1), epsilon
                inverse = sum(delta**j*time**j for j in range(ell+1))
                residual = sp.expand((1-time*delta)*inverse-1)
                self.assert_zero(residual+alpha*time**(ell+1))
                self.assertEqual(sp.rem(residual, alpha, epsilon), 0)
                self.assertNotEqual(sp.rem(delta**ell, alpha, epsilon), 0)
                d = sp.gcd(alpha, delta)
                self.assertEqual(d, epsilon)
                self.assertEqual(sp.rem(d**(ell+1), alpha, epsilon), 0)
        # The previous controls are quotient algebra, not supplied-frame realizations.
        f = sp.Matrix([1, parameter, parameter**2])
        normal = f.cross(f.diff(parameter))
        self.assert_matrix_equal(normal, sp.Matrix([parameter**2, -2*parameter, 1]))
        self.assertEqual(normal[2], 1)  # Exact Bezout certificate.
        self.assert_zero(normal.dot(f))
        self.assert_zero(normal.dot(f.diff(parameter)))
        self.assertEqual(max(sp.Poly(value, parameter).degree() for value in normal), 2)
        low_degree_f = sp.Matrix([1, parameter, 0])
        self.assert_matrix_equal(low_degree_f.cross(low_degree_f.diff(parameter)),
                                 sp.Matrix([0, 0, 1]))
        dependent_f = sp.Matrix([parameter, 2*parameter, 3*parameter])
        self.assert_matrix_equal(dependent_f.cross(dependent_f.diff(parameter)), sp.zeros(3, 1))
        self.assertEqual(sp.gcd_list(list(dependent_f)), parameter)
        # This dependent nonconstant row fails the unit-gcd hypothesis.
        x1, x2, x3 = sp.symbols("x1 x2 x3")
        xs = (x1, x2, x3)
        for degree in (1, 2, 4):
            p = (x1+x3)**degree
            coefficient_directions = (sp.Matrix([1, 0, -1]), sp.Matrix([0, 1, 0]))
            good_field = sp.Matrix([1, p, -1])
            for direction in coefficient_directions:
                self.assert_zero(self.act(direction, p, xs))
            self.assert_zero(self.act(good_field, p, xs))
            self.assert_zero(self.act(good_field, x1+x3, xs))
            # These are total degrees of nonzero summands, not monomial-support intervals.
            for k in range(3):
                summand = sp.expand(p**k*sp.diff(p, x1))
                actual_degree = sp.Poly(summand, *xs).total_degree()
                self.assertGreaterEqual(actual_degree, k*degree)
                self.assertLess(actual_degree, (k+1)*degree)

    def test_polynomial_wronskian_coordinate_controls(self):
        x1, x2, x3, z, v = sp.symbols("x1 x2 x3 z v")
        xs = (x1, x2, x3)
        H = x1**2+x2*x3+3*x2
        for m in (1, 2, 4):
            with self.subTest(parameter_degree=m):
                P = sp.expand(3*(z+H)**m+2)
                Pz = sp.diff(P, z)
                for x in xs:
                    self.assert_zero(Pz*sp.diff(P, x, z)-sp.diff(Pz, z)*sp.diff(P, x))
                polynomial = sp.Poly(P, z)
                leading = polynomial.coeff_monomial(z**m)
                recovered_H = sp.expand(polynomial.coeff_monomial(z**(m-1))/(m*leading))
                self.assertEqual(leading, 3)
                self.assertEqual(sp.denom(recovered_H), 1)
                for x in xs:
                    self.assert_zero(sp.diff(P, x)-sp.diff(recovered_H, x)*Pz)
                recovered_F = sp.expand(P.subs(z, v-recovered_H))
                for x in xs:
                    self.assertEqual(sp.diff(recovered_F, x), 0)
                self.assertEqual(sp.Poly(recovered_F, v).degree(), m)
                self.assert_zero(recovered_F.subs(v, z+recovered_H)-P)
                self.assert_inverse_pair(xs+(z+recovered_H,), xs+(v-recovered_H,),
                                         xs+(z,), xs+(v,))
                self.assert_zero(sp.Matrix(xs+(z+recovered_H,)).jacobian(xs+(z,)).det()-1)
        outside = x1*z**2+x2*z+x3
        failed_wronskian = (sp.diff(outside, z)*sp.diff(outside, x1, z)
                           - sp.diff(outside, z, 2)*sp.diff(outside, x1))
        self.assertNotEqual(sp.expand(failed_wronskian), 0)

    def test_actual_rank_two_selected_column_boundary(self):
        a, b, c, u, time = sp.symbols("a b c u time")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, original = (a, b, c, u), (X, Y, Z, W)
        good = (a+b*u, b+c*u, u)
        frame = good+(c+(good[0]*good[1])**2,)
        inv_c = W-(X*Y)**2
        inv_b = Y-inv_c*Z
        inverse = (X-inv_b*Z, inv_b, inv_c, Z)
        self.assert_inverse_pair(frame, inverse, adapted, original)
        self.assert_zero(sp.Matrix(frame).jacobian(adapted).det()+1)
        speeds = sp.Matrix([sp.diff(value, u) for value in good])
        self.assert_matrix_equal(speeds, sp.Matrix([b, c, 1]))
        self.assertEqual(speeds.jacobian(adapted).rank(), 2)
        T = sp.Matrix(inverse).jacobian(original)[:, 3].subs(
            dict(zip(original, frame)), simultaneous=True)
        self.assert_matrix_equal(T, sp.Matrix([u**2, -u, 1, 0]))
        E = sp.Matrix([0, 0, 0, 1])
        Q = self.bracket(E, T, adapted)
        second = self.bracket(E, Q, adapted)
        self.assert_matrix_equal(second, sp.Matrix([2, 0, 0, 0]))
        self.assert_matrix_equal(self.bracket(E, second, adapted), sp.zeros(4, 1))
        self.assert_matrix_equal(T.subs(u, u+time), T+time*Q+time**2*second/2)
        # This is a recognized translation frame, not a cancellation counterexample.
        # Its nonzero second adjoint directly exceeds the rank-one selected bound.

    def test_actual_rank_two_intrinsic_kernel_nonpreservation(self):
        a, b, c, u = sp.symbols("a b c u")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, original = (a, b, c, u), (X, Y, Z, W)
        actual_Y, actual_Z = b+a*u, c+a**2*u
        actual_W = a+actual_Y**2
        actual_X = u+actual_Y*actual_Z-a*actual_W
        frame = (actual_X, actual_Y, actual_Z, actual_W)
        inv_a = W-Y**2
        inv_u = X-Y*Z+inv_a*W
        inverse = (inv_a, Y-inv_a*inv_u, Z-inv_a**2*inv_u, inv_u)
        self.assert_inverse_pair(frame, inverse, adapted, original)
        self.assert_zero(sp.Matrix(frame).jacobian(adapted).det()+1)

        E = sp.Matrix([0, 0, 0, 1])
        h = c-a*b
        speeds = sp.Matrix([self.act(E, value, adapted) for value in frame[:3]])
        self.assert_matrix_equal(speeds, sp.Matrix([1+a*h, a, a**2]))
        self.assertEqual(speeds.jacobian(adapted).rank(), 2)
        self.assert_zero(speeds[0]-h*speeds[1]-1)  # Exact unit-ideal certificate.
        self.assert_zero(self.act(E, a, adapted))
        self.assert_zero(self.act(E, h, adapted))
        for speed in speeds:
            self.assert_zero(self.act(E, speed, adapted))

        T = sp.Matrix(inverse).jacobian(original)[:, 3].subs(
            dict(zip(original, frame)), simultaneous=True).applyfunc(sp.expand)
        Tu = a+actual_W
        expected_T = sp.Matrix([1, -u-a*Tu, -2*a*u-a**2*Tu, Tu])
        self.assert_matrix_equal(T, expected_T)
        for index, value in enumerate(frame):
            self.assert_zero(self.act(T, value, adapted)-int(index == 3))
        degree = max([sp.Poly(value, u).degree() for value in T[:3]]
                     + [sp.Poly(T[3], u).degree()-1])
        self.assertEqual(degree, 2)
        self.assertEqual(sp.Poly(T[3], u).degree(), 2)
        intrinsic_top = sp.Matrix([sp.Poly(value, u).coeff_monomial(u**degree)
                                   for value in T[:3]] + [0])
        N = sp.Matrix([0, -a**3, -a**4, 0])
        self.assert_matrix_equal(intrinsic_top, N)
        primitive_direction = sp.Matrix([0, 1, a, 0])
        self.assert_matrix_equal(N, -a**3*primitive_direction)
        for invariant in (a, h, *tuple(speeds)):
            self.assert_zero(self.act(N, invariant, adapted))
        self.assertEqual(self.act(primitive_direction, b, adapted), 1)
        self.assert_zero(self.act(primitive_direction, h, adapted))

        Th = self.act(T, h, adapted)
        self.assert_zero(Th+actual_Y)
        self.assertEqual(self.act(E, Th, adapted), -a)
        self.assertNotEqual(self.act(E, Th, adapted), 0)
        # h lies in C[a,h]=ker(N|C[a,b,c]), but T(h) does not lie in ker E.
        # This full polynomial inverse already recognizes the translation frame.
        # It is not a cancellation counterexample or a realization of a minimal profile.


if __name__ == "__main__":
    unittest.main(verbosity=2)
