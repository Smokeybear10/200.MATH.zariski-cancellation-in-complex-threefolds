"""Exact actual-frame control for failure of middle-adjoint kernel stability.

The parameter shift is held constant by all derivations. For each nonzero
complex shift the good-speed row is a unit, the bad coordinate has E-degree
two, and the selected original partial has filtration degree two. Both
polynomial inverse orders are checked, so the fields are not coefficient-only
data. The nonzero identity N(Q(h)) disproves the proposed stability shortcut
for this family, which is already a translation in its adapted coordinates.
This does not establish a cancellation counterexample, a minimal partial
profile, or a classification of arbitrary frames. A separate finite control
checks good-only degree preservation, the actual removable acceleration, and
one polynomial outside the quadratic speed span. That last polynomial is not
asserted to occur as an acceleration in any actual frame. No prior checker is
imported. Execution is left to Root's canonical runner.
"""

import unittest

import sympy as sp


class ThreeGoodUnitRankTwoBoundaryChecks(unittest.TestCase):
    @staticmethod
    def act(field, value, variables):
        return sp.expand(sum(coefficient*sp.diff(value, variable)
                             for coefficient, variable in zip(field, variables)))

    @classmethod
    def bracket(cls, left, right, variables):
        return sp.Matrix([cls.act(left, right[i], variables)
                          - cls.act(right, left[i], variables)
                          for i in range(len(variables))])

    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def assert_matrix_equal(self, left, right):
        self.assertEqual(left.shape, right.shape)
        for value in left-right:
            self.assert_zero(value)

    def test_shift_family_actual_inverse_and_quotient_nonpreservation(self):
        a, b, c, u, shift, H = sp.symbols("a b c u shift H")
        Y, Z, W, V = sp.symbols("Y Z W V")
        adapted, original = (a, b, c, u), (Y, Z, W, V)
        h = c-2*a*b
        k = a*(a+2*shift)
        actual_Y = b+(a+shift)*u
        actual_Z = c+a**2*u
        actual_W = a+b**2-h*u
        actual_V = u+actual_Y**2
        frame = sp.Matrix([actual_Y, actual_Z, actual_W, actual_V])

        inv_u = V-Y**2
        inv_old_y = Y-shift*inv_u
        inv_a = inv_u*Z-inv_old_y**2+W
        inv_b = Y-(inv_a+shift)*inv_u
        inv_c = Z-inv_a**2*inv_u
        inverse = sp.Matrix([inv_a, inv_b, inv_c, inv_u])
        forward_sub = dict(zip(original, frame))
        inverse_sub = dict(zip(adapted, inverse))
        self.assert_matrix_equal(inverse.subs(forward_sub, simultaneous=True),
                                 sp.Matrix(adapted))
        self.assert_matrix_equal(frame.subs(inverse_sub, simultaneous=True),
                                 sp.Matrix(original))
        self.assert_zero(frame.jacobian(adapted).det()-1)

        E = sp.Matrix([0, 0, 0, 1])
        speeds = sp.Matrix([self.act(E, value, adapted) for value in frame[:3]])
        self.assert_matrix_equal(speeds, sp.Matrix([a+shift, a**2, -h]))
        self.assertEqual(speeds.jacobian(adapted).rank(), 2)
        for value in (a, h, *tuple(speeds)):
            self.assert_zero(self.act(E, value, adapted))
        self.assertEqual(self.act(E, u, adapted), 1)
        acceleration = self.act(E, self.act(E, actual_V, adapted), adapted)
        self.assert_zero(acceleration-2*(a+shift)**2)
        self.assert_zero(self.act(E, acceleration, adapted))
        self.assertEqual(sp.Poly(actual_V, u).degree(), 2)

        base_speeds = sp.Matrix([a+shift, a**2, -H])
        omega = sp.Matrix.hstack(base_speeds, base_speeds.diff(a),
                                 base_speeds.diff(H)).det()
        self.assert_zero(omega+k)
        unit_certificate = speeds[1]-(a-shift)*speeds[0]
        self.assert_zero(unit_certificate-shift**2)
        # This is a unit certificate after a nonzero complex specialization,
        # not a claim that shift**2 is a unit in C[shift,a,b,c,u].
        for value in (1, 2, -1):
            self.assertEqual(sp.expand(unit_certificate.subs(shift, value)), value**2)
        self.assert_matrix_equal(speeds.subs({a: 0, c: 0, shift: 0}, simultaneous=True),
                                 sp.zeros(3, 1))
        coefficient_rows = sp.Matrix([
            [sp.Poly(value, a, H).coeff_monomial(monomial)
             for monomial in (a, a**2, H)] for value in base_speeds])
        self.assertEqual(coefficient_rows.det(), -1)

        # The last original partial holds Y,Z,W fixed and differentiates V.
        T = inverse.jacobian(original)[:, 3].subs(
            forward_sub, simultaneous=True).applyfunc(sp.expand)
        Ta = c+2*shift*b+k*u
        expected_T = sp.Matrix([Ta, -1*shift-a-u*Ta, -a**2-2*a*u*Ta, 1])
        self.assert_matrix_equal(T, expected_T)
        for index, value in enumerate(frame):
            self.assert_zero(self.act(T, value, adapted)-int(index == 3))
        self.assert_zero(T[0].subs(shift, 1)-(c+2*b+a*(a+2)*u))
        degree = max([sp.Poly(value, u).degree() for value in T[:3]]
                     + [sp.Poly(T[3], u).degree()-1])
        self.assertEqual(degree, 2)

        Q = self.bracket(E, T, adapted)
        expected_Q = sp.Matrix([k, -c-2*shift*b-2*k*u,
                                -2*a*c-4*a*shift*b-4*a*k*u, 0])
        self.assert_matrix_equal(Q, expected_Q)
        top = sp.Matrix([sp.Poly(value, u).coeff_monomial(u**degree)
                         for value in T[:3]]+[0])
        primitive = sp.Matrix([0, 1, 2*a, 0])
        N = -k*primitive
        self.assert_matrix_equal(top, N)
        self.assert_matrix_equal(self.bracket(E, Q, adapted), 2*N)
        self.assert_matrix_equal(self.bracket(E, 2*N, adapted), sp.zeros(4, 1))
        for value in (a, h, *tuple(speeds)):
            self.assert_zero(self.act(N, value, adapted))
        self.assert_zero(self.act(primitive, h, adapted))
        self.assertEqual(self.act(primitive, b, adapted), 1)
        # The triangular pair c=h+2ab, h=c-2ab identifies the primitive kernel.
        self.assert_zero(h.subs(c, H+2*a*b)-H)
        self.assert_zero((H+2*a*b).subs(H, h)-c)

        Qh = self.act(Q, h, adapted)
        self.assert_zero(self.act(Q, a, adapted)-k)
        self.assert_zero(Qh+2*b*k)
        self.assert_zero(self.act(E, Qh, adapted))
        self.assert_zero(self.act(N, Qh, adapted)-2*k**2)
        self.assertNotEqual(sp.expand(self.act(N, Qh, adapted)), 0)
        self.assert_zero(self.act(primitive, Qh, adapted)+2*k)
        D1 = Q.subs(u, 0)
        self.assert_zero(self.act(self.bracket(primitive, D1, adapted), h, adapted)
                         + 2*k)
        self.assert_zero(self.act(Q, a, adapted)-a*(a+2*shift))
        self.assertNotEqual(sp.expand(self.act(Q, a, adapted)), 0)
        self.assert_zero(self.act(N, self.act(N, actual_W, adapted), adapted)-2*k**2)
        self.assert_zero(self.act(N, self.act(N, actual_V, adapted), adapted)-2*k**2)
        # Thus Q(h) lies in A but not in S=ker(N|A), even for shift=1,
        # with a unit good-speed row and a genuinely quadratic last coordinate.

    def test_good_only_degrees_and_quadratic_shear_span_controls(self):
        a, b, c, u, H = sp.symbols("a b c u H")
        Y, Z, W, V, Unew = sp.symbols("Y Z W V Unew")
        good_variables = (Y, Z, W)
        h = c-2*a*b
        good_frame = (b+(a+1)*u, c+a**2*u, a+b**2-h*u)
        speeds = (a+1, a**2, -h)
        good_sub = dict(zip(good_variables, good_frame))
        speed_sub = dict(zip(good_variables, speeds))
        samples = (
            Y+2*Z-W+1,
            Y**2+Z*W+Z-3,
            Y**3+Y*Z*W+W**2+2,
            (Y+Z)**2*W**2+Z**4+Y*W+5,
        )
        # These four evaluations illustrate the homogeneous-leading argument;
        # they do not prove its assertion for every polynomial F.
        for expected_degree, sample in enumerate(samples, start=1):
            with self.subTest(total_degree=expected_degree):
                polynomial = sp.Poly(sample, *good_variables)
                self.assertEqual(polynomial.total_degree(), expected_degree)
                leading_form = sum(
                    coefficient*sp.prod(variable**power for variable, power
                                        in zip(good_variables, powers))
                    for powers, coefficient in polynomial.terms()
                    if sum(powers) == expected_degree)
                pulled = sp.Poly(sp.expand(sample.subs(good_sub, simultaneous=True)), u)
                self.assertEqual(pulled.degree(), expected_degree)
                leading_value = sp.expand(leading_form.subs(speed_sub, simultaneous=True))
                self.assertNotEqual(leading_value, 0)
                self.assert_zero(pulled.coeff_monomial(u**expected_degree)-leading_value)

        actual_V = u+good_frame[0]**2
        acceleration = sp.diff(actual_V, u, 2)
        self.assert_zero(acceleration-2*speeds[0]**2)
        self.assert_zero(actual_V-good_frame[0]**2-u)
        self.assertEqual(sp.diff(actual_V-good_frame[0]**2, u), 1)
        # Both orders of the fixed-good triangular coordinate shear.
        reduced = V-Y**2
        recovered = Unew+Y**2
        self.assert_zero(recovered.subs(Unew, reduced)-V)
        self.assert_zero(reduced.subs(V, recovered)-Unew)

        base_speeds = (a+1, a**2, -H)
        products = [sp.expand(base_speeds[i]*base_speeds[j])
                    for i in range(3) for j in range(i, 3)]
        unrealized_acceleration = a**5
        polynomials = [sp.Poly(value, a, H)
                       for value in products+[unrealized_acceleration]]
        monomials = sorted(set().union(*(set(poly.monoms()) for poly in polynomials)))
        coefficients = sp.Matrix([
            [poly.coeff_monomial(powers) for poly in polynomials]
            for powers in monomials])
        quadratic_span = coefficients[:, :6]
        self.assertEqual(quadratic_span.rank(), 6)
        self.assertEqual(coefficients.rank(), 7)
        realized_q = sp.Poly(2*(a+1)**2, a, H)
        realized_vector = sp.Matrix([realized_q.coeff_monomial(powers)
                                     for powers in monomials])
        self.assert_matrix_equal(realized_vector, 2*quadratic_span[:, 0])
        self.assertEqual(quadratic_span.row_join(realized_vector).rank(), 6)
        # a**5 is only a nonmembership control in C[a,H]. Nothing here
        # constructs an actual last coordinate with that acceleration or
        # asserts minimality of any full coordinate frame.


if __name__ == "__main__":
    unittest.main(verbosity=2)
