"""Exact actual-frame controls for the two mixed-cubic lowering gates.

These examples distinguish affine repair of the first gate, failure of the
second gate for a nonprimitive relation, and covariance under actual bad-slot
shears. The completion example is a coordinate despite lacking a constant ambient
directional derivative. Every asserted frame has polynomial inverse controls.
No example here refutes the stronger primitive mixed-relation conjecture or
cancellation, and finite tests do not prove a universal coordinate criterion.
The fourth method checks three sharpness controls for the all-degree invariant
suspension criterion: a missing global slice, an invariant coefficient w, and
a coefficient w that is not E-affine. Their plane noncoordinate obstructions
are explicit zero divisors or nilpotents, not a coordinate-testing algorithm.
No prior checker or solver is imported. Root owns runtime execution.
"""

import unittest

import sympy as sp


class ThreeGoodMixedCubicGateChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def assert_matrix_equal(self, left, right):
        self.assertEqual(left.shape, right.shape)
        for value in left-right:
            self.assert_zero(value)

    @staticmethod
    def cubic_frame(a, b, v, u):
        half = sp.Rational(1, 2)
        return sp.Matrix([u, v+a*u, a-half*v**3+b*u,
                          b+3*half*a*v**2+3*half*a**2*v*u+half*a**3*u**2])

    @staticmethod
    def cubic_inverse(X, Y, Z, W):
        half = sp.Rational(1, 2)
        a = Z-X*W+half*Y**3
        v = Y-a*X
        b = W-3*half*a*v**2-3*half*a**2*v*X-half*a**3*X**2
        return sp.Matrix([a, b, v, X])

    def test_translated_cubic_affine_repair_and_coordinate_inverse(self):
        a, b, v, u, shift = sp.symbols("a b v u shift")
        X, Y, Z, W, Inew = sp.symbols("X Y Z W Inew")
        adapted, original = (a, b, v, u), (X, Y, Z, W)
        frame = self.cubic_frame(a, b, v, u)
        frame[0] += shift
        inverse = self.cubic_inverse(X-shift, Y, Z, W)
        forward_sub, inverse_sub = dict(zip(original, frame)), dict(zip(adapted, inverse))
        self.assert_matrix_equal(inverse.subs(forward_sub, simultaneous=True), sp.Matrix(adapted))
        self.assert_matrix_equal(frame.subs(inverse_sub, simultaneous=True), sp.Matrix(original))
        self.assert_zero(frame.jacobian(adapted).det()+1)
        speeds = sp.Matrix([sp.diff(value, u) for value in frame[:3]])
        self.assert_matrix_equal(speeds, sp.Matrix([1, a, b]))
        self.assertEqual(sp.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(b)).det(), 1)
        q = sp.diff(frame[3], u, 2)
        L, F3 = X, Y**3/2
        self.assertEqual(sp.gcd(L, F3), 1)
        H = L*W-F3
        actual_H = sp.expand(H.subs(forward_sub, simultaneous=True))
        sigma = sp.diff(actual_H, u, 2)
        self.assert_zero(sigma-shift*a**3)
        self.assert_zero(actual_H-(frame[2]-a+shift*frame[3]))
        rho = -shift
        corrected = sp.expand(actual_H+rho*frame[3])
        self.assert_zero(sigma+rho*q)
        self.assert_zero(corrected-(frame[2]-a))
        self.assert_zero(sp.diff(corrected, u)-b)
        self.assert_zero(corrected-frame[2]+a)
        for value in (*tuple(speeds), q, sigma, sp.diff(corrected, u)):
            self.assert_zero(sp.diff(value, v))  # Intrinsic N=partial_v.
        products = [speeds[i]*speeds[j] for i in range(3) for j in range(i, 3)]
        monomials = (1, a, b, a**2, a*b, b**2, a**3)
        matrix = sp.Matrix([[sp.Poly(value, a, b).coeff_monomial(monomial)
                             for value in products+[sigma.subs(shift, 1)]]
                            for monomial in monomials])
        self.assertEqual(matrix[:, :6].rank(), 6)
        self.assertEqual(matrix.rank(), 7)
        # The raw obstruction is genuine at shift=1, but rho=-shift repairs it.
        invariant = (X-shift)*W-Y**3/2-Z
        self.assert_zero(invariant.subs(forward_sub, simultaneous=True)+a)
        self.assertEqual(sp.diff(invariant, Z), -1)
        coordinate_frame = sp.Matrix([X, Y, W, invariant])
        coordinate_inverse = sp.Matrix([X, Y, (X-shift)*W-Y**3/2-Inew, W])
        self.assert_matrix_equal(coordinate_inverse.subs(
            dict(zip((X, Y, W, Inew), coordinate_frame)), simultaneous=True), sp.Matrix(original))
        self.assert_matrix_equal(coordinate_frame.subs(
            dict(zip(original, coordinate_inverse)), simultaneous=True), sp.Matrix([X, Y, W, Inew]))

    def test_nonprimitive_fixed_relation_second_gate_failure(self):
        a, b, c, u, rho = sp.symbols("a b c u rho")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, original = (a, b, c, u), (X, Y, Z, W)
        frame = sp.Matrix([u, a+b*u, c+a*u, b+u**2/2])
        inv_b = W-X**2/2
        inv_a = Y-inv_b*X
        inverse = sp.Matrix([inv_a, inv_b, Z-inv_a*X, X])
        forward_sub = dict(zip(original, frame))
        self.assert_matrix_equal(inverse.subs(forward_sub, simultaneous=True), sp.Matrix(adapted))
        self.assert_matrix_equal(frame.subs(dict(zip(adapted, inverse)), simultaneous=True),
                                 sp.Matrix(original))
        self.assert_zero(frame.jacobian(adapted).det()-1)
        speeds = sp.Matrix([sp.diff(value, u) for value in frame[:3]])
        self.assert_matrix_equal(speeds, sp.Matrix([1, b, a]))
        self.assertEqual(sp.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(b)).det(), -1)
        self.assertEqual(sp.diff(frame[3], u, 2), 1)
        L, F3 = Y, Y*X**2/2
        self.assertEqual(sp.gcd(L, F3), Y)  # The primitive-relation premise FAILS.
        H = L*W-F3
        actual_H = sp.expand(H.subs(forward_sub, simultaneous=True))
        self.assert_zero(actual_H-b*frame[1])
        self.assert_zero(sp.diff(actual_H, u, 2))
        G2 = rho*X**2/2
        P0 = sp.expand((H+rho*W-G2).subs(forward_sub, simultaneous=True))
        self.assert_zero(sp.diff(P0, u, 2))
        self.assert_zero(P0-b*(frame[1]+rho))
        second_speed = sp.diff(P0, u)
        self.assert_zero(second_speed-b**2)
        matrix = sp.Matrix([[sp.Poly(value, a, b).coeff_monomial(monomial)
                             for value in list(speeds)+[second_speed]]
                            for monomial in (1, a, b, b**2)])
        self.assertEqual(matrix[:, :3].rank(), 3)
        self.assertEqual(matrix.rank(), 4)
        # A different L succeeds, so this is not a failure of existence of a
        # successful relation, and W itself admits a fixed-good quadratic shear.
        alternative = X*(W-X**2/2)-Y
        self.assert_zero(alternative.subs(forward_sub, simultaneous=True)+a)

    def test_bad_shear_covariance_and_coordinate_without_constant_direction(self):
        a, b, v, u, kx, ky, kz, constant = sp.symbols("a b v u kx ky kz constant")
        X, Y, Z, W, Dnew, Inew = sp.symbols("X Y Z W Dnew Inew")
        original = (X, Y, Z, W)
        baseline = self.cubic_frame(a, b, v, u)
        K2, K1 = Z**2+X*Y, kx*X+ky*Y+kz*Z
        shear = K2+K1+constant
        frame = baseline.copy()
        frame[3] += shear.subs(dict(zip(original, baseline)), simultaneous=True)
        F3new = Y**3/2+X*K2
        Hnew = X*W-F3new
        corrected = Hnew-X*K1
        invariant = corrected-Z-constant*X
        forward_sub = dict(zip(original, frame))
        self.assert_zero(invariant.subs(forward_sub, simultaneous=True)+a)
        self.assert_zero(sp.diff(corrected.subs(forward_sub, simultaneous=True), u)-(b+constant))
        self.assert_zero(sp.diff(Hnew.subs(forward_sub, simultaneous=True), u, 2)
                         - 2*(kx+ky*a+kz*b))
        self.assert_zero(sp.diff(frame[3], u, 2)-(a**3+2*(b**2+a)))
        # The bad-slot shear and its inverse are polynomial with goods fixed.
        self.assert_zero((W+shear).subs(W, W-shear)-W)
        self.assert_zero((W-shear).subs(W, W+shear)-W)

        # A separate specialization W_new=W_old+Z^2: the invariant is still
        # a coordinate, but no nonzero constant ambient derivative is constant.
        I = X*W-X*Z**2-Y**3/2-Z
        dx, dy, dz, dw = sp.symbols("dx dy dz dw")
        directional = sum(coefficient*sp.diff(I, variable)
                          for coefficient, variable in zip((dx, dy, dz, dw), original))
        direction_matrix = sp.Matrix([
            [sp.Poly(sp.diff(I, variable), *original).coeff_monomial(monomial)
             for variable in original] for monomial in (W, Y**2, X*Z, X)])
        self.assertNotEqual(direction_matrix.det(), 0)
        self.assert_zero(directional.subs({dx: 0, dy: 0, dz: 0, dw: 0}))
        residue = I.subs(X, 0)
        self.assertEqual(sp.diff(residue, Z), -1)
        coordinate_frame = sp.Matrix([X, Y, W-Z**2, I])
        inv_Z = X*Dnew-Y**3/2-Inew
        coordinate_inverse = sp.Matrix([X, Y, inv_Z, Dnew+inv_Z**2])
        new_variables = (X, Y, Dnew, Inew)
        self.assert_matrix_equal(coordinate_inverse.subs(
            dict(zip(new_variables, coordinate_frame)), simultaneous=True), sp.Matrix(original))
        self.assert_matrix_equal(coordinate_frame.subs(
            dict(zip(original, coordinate_inverse)), simultaneous=True), sp.Matrix(new_variables))

    def test_invariant_suspension_hypothesis_sharpness_controls(self):
        w, y, t, z, s, r = sp.symbols("w y t z s r")
        variables = (w, y, t, z)

        def act(field, value):
            return sp.expand(sum(coefficient*sp.diff(value, variable)
                                 for coefficient, variable in zip(field, variables)))

        # (a) E=t*partial_w+z*partial_y is an LND and w is a local slice,
        # but its image ideal is (t,z), a proper ideal. Hence E has no slice.
        field_a = sp.Matrix([t, z, 0, 0])
        g_a, invariant_a = y*t, w*z-y*t
        self.assert_zero(act(field_a, invariant_a))
        self.assertEqual(act(field_a, w), t)
        self.assertNotEqual(act(field_a, w), 0)
        self.assert_zero(act(field_a, act(field_a, w)))
        generator_images = sp.Matrix([act(field_a, value) for value in variables])
        self.assert_matrix_equal(generator_images, sp.Matrix([t, z, 0, 0]))
        self.assert_matrix_equal(generator_images.subs({t: 0, z: 0}), sp.zeros(4, 1))
        # Every image has the form t*f_w+z*f_y. Evaluation above certifies
        # properness of their generated ideal, not just failure of one slice.
        flow_a = sp.Matrix([w+s*t, y+s*z, t, z])
        self.assert_matrix_equal(flow_a.diff(s).subs(s, 0), field_a)
        self.assert_zero(invariant_a.subs(dict(zip(variables, flow_a)), simultaneous=True)
                         - invariant_a)
        self.assertEqual(sp.reduced(y, [g_a], y, t)[1], y)
        self.assertEqual(sp.reduced(t, [g_a], y, t)[1], t)
        self.assertEqual(sp.reduced(y*t, [g_a], y, t)[1], 0)
        # The nonzero classes of y and t multiply to zero: this zero fiber
        # is reducible and cannot be the affine-line fiber of a coordinate.

        # (b) E=partial_t has the global slice t, but Ew=0.
        field_b = sp.Matrix([0, 0, 1, 0])
        g_b, invariant_b = y**2, w*z-y**2
        self.assertEqual(act(field_b, t), 1)
        self.assert_zero(act(field_b, invariant_b))
        self.assert_zero(act(field_b, w))
        self.assertEqual(sp.reduced(y, [g_b], y, t)[1], y)
        self.assertEqual(sp.reduced(y**2, [g_b], y, t)[1], 0)
        # The zero fiber has a nonzero nilpotent, so g_b is not a coordinate.

        # (c) The triangular LND has a slice and moves w, but E^2w is nonzero.
        field_c = sp.Matrix([2*y, z, 1, 0])
        self.assertEqual(act(field_c, t), 1)
        self.assert_zero(act(field_c, invariant_b))
        self.assertEqual(act(field_c, w), 2*y)
        self.assertEqual(act(field_c, act(field_c, w)), 2*z)
        self.assertNotEqual(act(field_c, act(field_c, w)), 0)
        self.assert_zero(act(field_c, act(field_c, act(field_c, w))))
        flow_c = sp.Matrix([w+2*y*s+z*s**2, y+z*s, t+s, z])
        self.assert_matrix_equal(flow_c.diff(s).subs(s, 0), field_c)
        self.assert_zero(flow_c.jacobian(variables).det()-1)
        self.assert_zero(invariant_b.subs(dict(zip(variables, flow_c)), simultaneous=True)
                         - invariant_b)
        flow_r = flow_c.subs(s, r)
        self.assert_matrix_equal(flow_c.subs(dict(zip(variables, flow_r)), simultaneous=True),
                                 flow_c.subs(s, s+r))
        flow_inverse = flow_c.subs(s, -s)
        self.assert_matrix_equal(flow_c.subs(dict(zip(variables, flow_inverse)), simultaneous=True),
                                 sp.Matrix(variables))
        self.assert_matrix_equal(flow_inverse.subs(dict(zip(variables, flow_c)), simultaneous=True),
                                 sp.Matrix(variables))


if __name__ == "__main__":
    unittest.main(verbosity=2)
