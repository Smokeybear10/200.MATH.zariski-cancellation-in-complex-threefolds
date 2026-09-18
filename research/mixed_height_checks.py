#!/usr/bin/env python3
"""Independent exact controls for the mixed-height arguments.

The nonzero-top tests certify the reduction identities, not an example
satisfying every nonzero-k mixed-frame hypothesis. The genuine mixed-frame
example has zero top constants. No research module is imported.
"""

import unittest

import sympy as sp


a, b, c, d = X = sp.symbols("a b c d")
t = sp.symbols("t")


def apply(field, value, coordinates=X):
    return sp.expand(sum(coefficient * sp.diff(value, variable)
                         for coefficient, variable in zip(field, coordinates)))


def iterate(field, value, order):
    for _ in range(order):
        value = sp.factor(apply(field, value))
    return value


def bracket(left, right):
    return sp.Matrix([apply(left, q) - apply(right, p)
                      for p, q in zip(left, right)])


def partial(index):
    return sp.eye(4)[:, index]


def mixed_field():
    f = a + b*d
    return sp.Matrix((-d*f, f, 1, 0))


def zero_top_field():
    primitive = sp.Matrix((1, a, b+a*a/2, c+a*b+a**3/6))
    invariant = d-a*c-b*b/2+a*a*b/2-a**4/24
    return invariant*primitive, primitive, invariant


def primitive_power_law_field():
    # Physical names here are (a,b,c,d), with b the curved coordinate,
    # c the slice, and a the bad coordinate. This is the (a,d,z,w)
    # notation of the written note, renamed to use this checker's X.
    invariant = b-a*a/2
    return sp.Matrix((invariant, a*invariant, 1, 0)), invariant


def primitive_cubic_time_field():
    invariant = c-a*b+a**3/6
    primitive = sp.Matrix((1, a, b+a*a/2, 0))
    return invariant*primitive+partial(3), primitive, invariant


class MixedHeightTests(unittest.TestCase):
    def assertMatrixZero(self, matrix):
        self.assertTrue(all(sp.expand(entry) == 0 for entry in matrix), matrix)

    def test_formal_brackets_give_actual_commutation(self):
        # Formal basis A, B0, V. These are bracket identities, not an E example.
        s, k = sp.symbols("s k", nonzero=True)
        aa, bb, vv = (sp.eye(3)[:, index] for index in range(3))
        ad_matrix = sp.Matrix.hstack(-2*k*vv, -aa/4+k*s*vv/2, sp.zeros(3, 1))

        def ad_e(vector):
            return vector.diff(s) + ad_matrix*vector

        self.assertMatrixZero(ad_e(4*bb+s*aa))
        self.assertMatrixZero(ad_e(ad_e(bb+s*aa/4)))
        self.assertMatrixZero(ad_e(ad_e(aa)))
        self.assertMatrixZero(ad_e(ad_e(bb))-k*vv)

    def test_triangular_top_identity_fixes_the_derived_slice(self):
        # Here b plays x4. The affine top identity is genuine, but one good
        # double bracket fails, so this is not a full nonzero-k branch example.
        field = sp.Matrix((b/4+c**4/32, c**3/6, 1, 0))
        top = sp.Matrix([iterate(field, coordinate, 4) for coordinate in X])
        highest = sp.Matrix([iterate(field, coordinate, 5) for coordinate in X])
        s = iterate(field, b, 3)
        self.assertEqual(top, sp.Matrix((c, 1, 0, 0)))
        self.assertEqual(highest, partial(0))
        self.assertEqual(s, c)
        constant = top-s*highest
        reduction = 4*constant+s*highest
        self.assertEqual(reduction, sp.Matrix((c, 4, 0, 0)))
        self.assertMatrixZero(bracket(field, reduction))
        self.assertEqual(apply(reduction, b), 4)
        self.assertEqual(apply(reduction, s), iterate(field, apply(reduction, b), 3))
        self.assertEqual(apply(reduction, s), 0)
        self.assertMatrixZero(sp.Matrix([apply(reduction, q) for q in reduction]))
        self.assertMatrixZero(bracket(field, bracket(field, partial(1))))
        self.assertNotEqual(bracket(field, bracket(field, partial(2))), sp.zeros(4, 1))

    def test_burgers_high_a_degree_cannot_cancel(self):
        # Representative degree controls, not a replacement for the general proof.
        leading = b*b+c
        for degree in (2, 3, 6):
            s = leading*a**degree+(b+d)*a+1
            residual = sp.Poly(sp.expand(4*sp.diff(s, b)+s*sp.diff(s, a)), a)
            self.assertEqual(residual.degree(), 2*degree-1)
            self.assertEqual(sp.expand(residual.LC()-degree*leading**2), 0)

    def test_burgers_affine_a_coefficient_has_nonzero_top_b_degree(self):
        for degree in (0, 1, 4):
            r = b**degree+c
            s = r*a+b*b+d
            residual = sp.expand(4*sp.diff(s, b)+s*sp.diff(s, a))
            coefficient = residual.coeff(a, 1)
            self.assertEqual(sp.expand(coefficient-(4*sp.diff(r, b)+r*r)), 0)
            self.assertEqual(sp.degree(coefficient, b), 2*degree)
            self.assertNotEqual(coefficient, 0)

    def test_rational_burgers_solution_is_a_negative_control(self):
        s = 4*a/b
        self.assertEqual(sp.cancel(4*sp.diff(s, b)+s*sp.diff(s, a)), 0)
        self.assertNotEqual(sp.diff(s, a), 0)
        with self.assertRaises(sp.PolynomialError):
            sp.Poly(s, a, b)
        # The proposed polynomial shear degenerates for this rational solution.
        self.assertEqual(sp.cancel(a-b*s/4), 0)

    def test_shear_inverse_and_retained_good_partial(self):
        s = c*c+d
        q = a-b*s/4
        target = sp.symbols("Q B C D")
        qq, bb, cc, dd = target
        forward = sp.Matrix((q, b, c, d))
        inverse = sp.Matrix((qq+bb*(cc*cc+dd)/4, bb, cc, dd))
        self.assertMatrixZero(forward.subs(dict(zip(X, inverse)), simultaneous=True)-sp.Matrix(target))
        self.assertMatrixZero(inverse.subs(dict(zip(target, forward)), simultaneous=True)-sp.Matrix(X))
        self.assertEqual(forward.jacobian(X).det(), 1)
        self.assertEqual(sp.Matrix([apply(partial(0), f) for f in forward]), partial(0))
        reduction = sp.Matrix((s, 4, 0, 0))
        self.assertEqual(sp.Matrix([apply(reduction, f) for f in forward]), 4*partial(1))

    def test_coordinate_slice_alone_does_not_imply_local_nilpotence(self):
        field = sp.Matrix((a, 4, 0, 0))
        self.assertEqual(apply(field, b/4), 1)
        for order in range(1, 9):
            self.assertEqual(iterate(field, a, order), a)

    def test_genuine_mixed_control_and_non_nilpotent_middle_coefficient(self):
        field = mixed_field()
        first = [bracket(field, partial(index)) for index in range(4)]
        for index in range(3):
            self.assertMatrixZero(bracket(field, first[index]))
        top = bracket(field, first[3])
        self.assertMatrixZero(top-sp.Matrix((2*d*(a+b*d), -2*(a+b*d), 0, 0)))
        self.assertMatrixZero(bracket(field, top))
        for vector in first[:3]:
            self.assertMatrixZero(bracket(vector, top))
        # A good partial itself need not commute with the bad top field.
        self.assertNotEqual(bracket(partial(0), top), sp.zeros(4, 1))
        self.assertEqual(first[3], sp.Matrix((a+2*b*d, -b, 0, 0)))
        for order in range(1, 9):
            self.assertEqual(iterate(first[3], b, order), (-1)**order*b)

    def test_genuine_mixed_determinant_and_inverse_jacobian_orientation(self):
        field = mixed_field()
        jacobian = field.jacobian(X)
        top = bracket(field, bracket(field, partial(3)))
        defect = top*partial(3).T
        matrix = sp.eye(4)-t*jacobian+t*t*defect/2
        flow = sp.Matrix(X)+t*field
        self.assertMatrixZero(sp.Matrix([apply(field, f) for f in field]))
        self.assertEqual(sp.expand(matrix.det()), 1)
        self.assertMatrixZero(flow.jacobian(X)*matrix-sp.eye(4))
        self.assertMatrixZero(matrix*flow.jacobian(X)-sp.eye(4))
        self.assertMatrixZero(jacobian.applyfunc(lambda f: apply(field, f))-jacobian**2+defect)

    def test_actual_degree_1112_frame_and_rank_two(self):
        # Adapted variables: F=a+bd, U=b-cF, D=d, S=c.
        ff, uu, dd, ss = adapted = sp.symbols("F U D S")
        old_b = uu+ss*ff
        old_a = ff-dd*old_b
        frame = sp.Matrix((old_a-ss, old_b, ss, dd))
        coefficient_columns = frame.jacobian(adapted).inv()
        degrees = []
        for index in range(4):
            vector = coefficient_columns[:, index]
            degrees.append(max(sp.degree(sp.expand(value), ss)-(row == 3)
                               for row, value in enumerate(vector) if value != 0))
        self.assertEqual(degrees, [1, 1, 1, 2])
        field = mixed_field()
        frame_partials = (partial(0), partial(1), partial(0)+partial(2))
        family = [field]+[bracket(field, vector) for vector in frame_partials]
        family.append(bracket(field, bracket(field, partial(3))))
        self.assertEqual(sp.Matrix.hstack(*family).rank(), 2)

    def test_zero_top_nonslice_control_has_mixed_brackets(self):
        field, primitive, invariant = zero_top_field()
        self.assertEqual(apply(primitive, invariant), 0)
        for index in (0, 1, 3):
            self.assertMatrixZero(bracket(field, bracket(field, partial(index))))
        top = bracket(field, bracket(field, partial(2)))
        self.assertMatrixZero(top-2*field)
        self.assertMatrixZero(bracket(field, top))
        # The coefficient ideal is exactly (invariant), so there is no slice.
        self.assertEqual(field[0], invariant)
        self.assertTrue(all(sp.cancel(value/invariant).is_polynomial(*X) for value in field))
        self.assertEqual(sp.Poly(invariant, X).total_degree(), 4)

    def test_zero_top_higher_iterate_need_not_be_nice(self):
        field, _, invariant = zero_top_field()
        third_bad = iterate(field, c, 3)
        fourth = sp.Matrix([iterate(field, coordinate, 4) for coordinate in X])
        fifth = sp.Matrix([apply(field, value) for value in fourth])
        self.assertEqual(sp.expand(third_bad-2*invariant**3), 0)
        self.assertMatrixZero(fourth-sp.Matrix((0, 0, 0, 6*invariant**4)))
        self.assertMatrixZero(fifth)
        self.assertEqual(sp.expand(apply(fourth, fourth[3])-144*invariant**7), 0)
        self.assertNotEqual(apply(fourth, fourth[3]), 0)
        parameter = sp.symbols("u")
        p = sp.Matrix((0, 0, 0, 6*parameter**4))
        ell = 2*parameter**3
        self.assertMatrixZero(3*ell*p.diff(parameter)-4*sp.diff(ell, parameter)*p)

    def test_primitive_slice_power_law_is_not_excluded_by_freeness(self):
        field, invariant = primitive_power_law_field()
        self.assertEqual(apply(field, invariant), 0)
        self.assertEqual(apply(field, c), 1)
        for index in (1, 2, 3):
            self.assertMatrixZero(bracket(field, bracket(field, partial(index))))
        bad_top = bracket(field, bracket(field, partial(0)))
        self.assertMatrixZero(bad_top-sp.Matrix((2*invariant, 2*a*invariant, 0, 0)))
        self.assertMatrixZero(bracket(field, bad_top))
        highest = sp.Matrix([iterate(field, coordinate, 2) for coordinate in X])
        self.assertMatrixZero(highest-invariant**2*partial(1))
        self.assertMatrixZero(sp.Matrix([apply(field, value) for value in highest]))
        self.assertEqual(sp.expand(apply(highest, highest[1])-2*invariant**3), 0)

    def test_primitive_power_law_kernel_coordinates_and_exact_height(self):
        field, invariant = primitive_power_law_field()
        u = a-c*invariant
        forward = sp.Matrix((invariant, u, d, c))
        gg, uu, ww, ss = adapted = sp.symbols("G U W S")
        inverse = sp.Matrix((uu+ss*gg, gg+(uu+ss*gg)**2/2, ss, ww))
        self.assertMatrixZero(forward.subs(dict(zip(X, inverse)), simultaneous=True)-sp.Matrix(adapted))
        self.assertMatrixZero(inverse.subs(dict(zip(adapted, forward)), simultaneous=True)-sp.Matrix(X))
        self.assertEqual(sp.Matrix([apply(field, value) for value in forward]), partial(3))
        # Frame (b-c-d,c,d,a), not the physical frame containing the slice.
        frame = sp.Matrix((inverse[1]-ss-ww, ss, ww, inverse[0]))
        frame_partials = frame.jacobian(adapted).inv()
        degrees = []
        for index in range(4):
            vector = frame_partials[:, index]
            degrees.append(max(sp.degree(sp.expand(value), ss)-(row == 3)
                               for row, value in enumerate(vector) if value != 0))
        self.assertEqual(degrees, [1, 1, 1, 2])

    def test_m2_shear_is_polynomial_and_turns_the_control_nice(self):
        field, invariant = primitive_power_law_field()
        # c_top=e_b, lambda=1, x4=a, so y_b=b-a^2/2.
        forward = sp.Matrix((a, b-a*a/2, c, d))
        aa, bb, cc, dd = target = sp.symbols("A B C D")
        inverse = sp.Matrix((aa, bb+aa*aa/2, cc, dd))
        self.assertMatrixZero(forward.subs(dict(zip(X, inverse)), simultaneous=True)-sp.Matrix(target))
        self.assertMatrixZero(inverse.subs(dict(zip(target, forward)), simultaneous=True)-sp.Matrix(X))
        transformed = sp.Matrix([apply(field, value) for value in forward])
        transformed = transformed.subs(dict(zip(X, inverse)), simultaneous=True)
        self.assertEqual(transformed, sp.Matrix((bb, 0, 1, 0)))
        for value in transformed:
            self.assertEqual(apply(transformed, value, target), 0)
        new_bad = partial(0)+a*partial(1)
        self.assertMatrixZero(bracket(field, bracket(field, new_bad)))
        for index in (1, 2, 3):
            self.assertEqual(sp.Matrix([apply(partial(index), value) for value in forward]), partial(index))

    def test_uniform_m2_shear_bracket_cancellation(self):
        # Algebraic coefficient identity, distinct from an example of E.
        lam, gg = sp.symbols("lambda g", nonzero=True)
        vv = sp.Matrix(sp.symbols("v1:5"))
        ad_e_a = -lam*vv/(2*gg)
        self.assertMatrixZero(vv+2*gg/lam*ad_e_a)
        # E(g)=0 and E(x4)=lambda*g imply E^2(x4^2)=2lambda^2*g^2.
        zz = sp.symbols("z")
        first = lam*gg*sp.diff(zz**2, zz)
        second = lam*gg*sp.diff(first, zz)
        self.assertEqual(second, 2*lam**2*gg**2)

    def test_general_rational_burgers_normal_form(self):
        r = sp.symbols("r", nonzero=True)
        alpha, beta, gamma = c*c+1, d+c, c*d+1
        numerator = alpha*a+beta
        denominator = alpha*b/r+gamma
        sigma = numerator/denominator
        residual = r*sp.diff(sigma, b)+sigma*sp.diff(sigma, a)
        self.assertEqual(sp.cancel(residual), 0)
        self.assertEqual(sp.diff(denominator, a), 0)
        self.assertEqual(sp.diff(numerator, b), 0)
        self.assertEqual(sp.diff(numerator, a)-r*sp.diff(denominator, b), 0)
        field = sp.Matrix((numerator, r*denominator, 0, 0))
        self.assertEqual(sp.cancel(apply(field, sigma)), 0)
        self.assertEqual(sp.expand(apply(field, denominator)-alpha*denominator), 0)
        self.assertEqual(sp.expand(apply(field, numerator)-alpha*numerator), 0)

    def test_positive_weight_rational_burgers_control_has_fixed_locus(self):
        # A model of the positive-weight contradiction, not a full mixed frame.
        r = sp.Integer(3)
        euler = sp.Matrix((a, b, 0, 0))
        sigma = r*a/b
        for n in (1, 2, 4):
            field = sp.Matrix((b**(n+1), 0, 0, 0))
            invariant = r*b**n
            self.assertEqual(apply(field, invariant), 0)
            self.assertEqual(sp.cancel(apply(field, sigma)-invariant), 0)
            self.assertMatrixZero(bracket(euler, field)-n*field)
            self.assertMatrixZero(field.subs({a: 0, b: 0}))
            reduced = field/invariant
            commuting = sp.Matrix((sigma, r, 0, 0))
            self.assertTrue(all(sp.cancel(value) == 0 for value in bracket(reduced, commuting)))

    def test_invariant_plane_denominator_clearing_is_exact(self):
        # R=C[c,d], N=c^2*d+1, D=c, sigma=N/D reduced.
        numerator, denominator = c*c*d+1, c
        sigma = numerator/denominator
        self.assertEqual(sp.gcd(numerator, denominator), 1)
        field = partial(3)
        invariant = c
        rational = field/invariant
        self.assertEqual(apply(field, denominator), 0)
        self.assertEqual(apply(field, numerator), invariant*denominator)
        self.assertEqual(sp.cancel(apply(field, sigma)-invariant), 0)
        self.assertEqual(sp.cancel(apply(rational, numerator)), denominator)
        # The reduced denominator of delta(d) divides g and is E-invariant.
        clearing = sp.denom(sp.cancel(rational[3]))
        self.assertEqual(clearing, c)
        self.assertEqual(apply(field, clearing), 0)
        self.assertEqual(clearing*rational, field)
        self.assertEqual(apply(clearing*rational, c), 0)
        self.assertEqual(iterate(clearing*rational, d, 2), 0)

    def test_commutation_of_rescale_does_not_alone_transfer_to_original(self):
        original = sp.Matrix((b, 0, 0, 0))
        rational = original/b
        translation = partial(1)
        self.assertMatrixZero(bracket(rational, translation))
        self.assertNotEqual(bracket(original, translation), sp.zeros(4, 1))
        # Missing hypothesis: the original derivative ideal is (b), no slice.
        self.assertEqual(sp.gcd_list(list(original)), b)

    def test_primitive_cubic_time_control_and_nonzero_rescaled_defect(self):
        field, primitive, invariant = primitive_cubic_time_field()
        self.assertEqual(apply(field, invariant), 0)
        self.assertEqual(apply(field, d), 1)
        for index in (0, 2, 3):
            self.assertMatrixZero(bracket(field, bracket(field, partial(index))))
        top = bracket(field, bracket(field, partial(1)))
        self.assertMatrixZero(top-2*invariant*primitive)
        self.assertMatrixZero(bracket(field, top))
        highest = sp.Matrix([iterate(field, coordinate, 3) for coordinate in X])
        self.assertMatrixZero(highest-2*invariant**3*partial(2))
        self.assertMatrixZero(sp.Matrix([apply(field, value) for value in highest]))
        self.assertEqual(sp.expand(iterate(field, b, 2)-invariant**2), 0)
        rational = field/invariant
        rescaled_top = bracket(rational, bracket(rational, partial(1)))
        expected = -2*partial(3)/invariant**2
        self.assertTrue(all(sp.cancel(value) == 0 for value in rescaled_top-expected))
        self.assertNotEqual(expected, sp.zeros(4, 1))
        self.assertTrue(all(sp.cancel(value) == 0 for value in bracket(rational, rescaled_top)))

    def test_cubic_time_rational_reduction_gives_actual_coordinate_ring(self):
        field, _, invariant = primitive_cubic_time_field()
        rational = field/invariant
        sigma = sp.cancel(apply(field, b)/invariant)
        self.assertEqual(sigma, a)
        commuting = sp.Matrix((0, 2, 2*a, 0))
        self.assertTrue(all(sp.cancel(value) == 0 for value in bracket(rational, commuting)))
        self.assertMatrixZero(bracket(field, commuting))
        self.assertEqual(apply(commuting, sigma), 0)
        self.assertEqual(apply(commuting, invariant), 0)
        # Kernel of commuting is C[a,c-ab,d], an actual coordinate three-ring.
        forward = sp.Matrix((a, b, c-a*b, d))
        aa, bb, cc, dd = target = sp.symbols("A B C D")
        inverse = sp.Matrix((aa, bb, cc+aa*bb, dd))
        self.assertMatrixZero(forward.subs(dict(zip(X, inverse)), simultaneous=True)-sp.Matrix(target))
        self.assertMatrixZero(inverse.subs(dict(zip(target, forward)), simultaneous=True)-sp.Matrix(X))
        self.assertEqual(sp.Matrix([apply(commuting, value) for value in forward]), 2*partial(1))
        # The good highest constant direction 2*d/dc survives.
        self.assertEqual(sp.Matrix([apply(2*partial(2), value) for value in forward]), 2*partial(2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
