#!/usr/bin/env python3
"""Independent exact controls for coordinate-plane and normalizer claims.

No research module is imported. These are finite symbolic controls, not
formal verification of Rentschler or the general cancellation conjecture.
The uniform linear-plane proof is in linear-plane-obstruction-pass.md.
"""

import unittest

import sympy as sp


X = x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4")
A = a, b, c, s = sp.symbols("a b c s")
sigma = x4 - x1*x2
E = sp.Matrix((2*sigma, 3*sigma**2, 4*sigma**3,
               1 + 2*x2*sigma + 3*x1*sigma**2))
forward = sp.Matrix((a+s**2, b+s**3, c+s**4,
                     s+(a+s**2)*(b+s**3)))
inverse = sp.Matrix((x1-sigma**2, x2-sigma**3,
                     x3-sigma**4, sigma))


def apply(field, value, coordinates=X):
    return sp.expand(sum(q*sp.diff(value, z)
                         for q, z in zip(field, coordinates)))


def bracket(left, right, coordinates=X):
    return sp.Matrix([apply(left, q, coordinates)-apply(right, p, coordinates)
                      for p, q in zip(left, right)])


def degree(field, value, coordinates):
    if value == 0:
        raise ValueError("Degree of zero is excluded from this test helper")
    for order in range(40):
        value = apply(field, value, coordinates)
        if value == 0:
            return order
    raise AssertionError("Test example did not terminate within its bound")


class ProjectivePlaneTests(unittest.TestCase):
    def assertZero(self, value):
        entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
        self.assertTrue(all(sp.cancel(entry) == 0 for entry in entries), value)

    def test_inverse_after_forward(self):
        self.assertZero(inverse.subs(dict(zip(X, forward)), simultaneous=True)
                        - sp.Matrix(A))

    def test_forward_after_inverse(self):
        self.assertZero(forward.subs(dict(zip(A, inverse)), simultaneous=True)
                        - sp.Matrix(X))

    def test_coordinate_jacobian(self):
        self.assertEqual(sp.expand(forward.jacobian(A).det()), 1)

    def test_slice_and_kernel_generators(self):
        self.assertZero(sp.Matrix([apply(E, value) for value in inverse])
                        - sp.Matrix((0, 0, 0, 1)))

    def test_pushforward_of_translation(self):
        self.assertZero(E.subs(dict(zip(X, forward)), simultaneous=True)
                        - forward.diff(s))

    def test_flow_time_degrees(self):
        self.assertEqual([sp.degree(value, s) for value in forward], [2, 3, 4, 5])
        self.assertZero(forward.diff(s, 6))
        self.assertEqual(forward.diff(s, 5)[3], 120)

    def test_constant_commuting_translation(self):
        self.assertZero(bracket(E, sp.eye(4)[:, 2]))

    def test_first_three_coefficient_separation(self):
        d1, d2, d3 = sp.symbols("d1 d2 d3")
        expression = sp.Poly(2*s*d1+3*s**2*d2+4*s**3*d3, s)
        self.assertEqual([expression.coeff_monomial(s**i) for i in (1, 2, 3)],
                         [2*d1, 3*d2, 4*d3])

    def test_general_plane_images_on_slice_divisor(self):
        alpha, beta, gamma, u0, v0, l1, l2, l3 = sp.symbols(
            "alpha beta gamma u0 v0 l1 l2 l3")
        U = x4+alpha*x1+beta*x2+gamma*x3+u0
        V = l1*x1+l2*x2+l3*x3+v0
        self.assertEqual(sp.expand(apply(E, U).subs(x4, x1*x2)), 1)
        self.assertEqual(sp.expand(apply(E, V).subs(x4, x1*x2)), 0)
        self.assertZero(apply(E, V).subs(x4, s+x1*x2)
                        - (2*l1*s+3*l2*s**2+4*l3*s**3))

    def test_uniform_plane_jacobian_minors(self):
        alpha, beta, gamma, l1, l2, l3 = sp.symbols("alpha beta gamma l1 l2 l3")
        jac = sp.Matrix((x1*x2+alpha*x1+beta*x2+gamma*x3,
                         l1*x1+l2*x2+l3*x3)).jacobian((x1, x2, x3))
        minors = [sp.expand(jac[:, list(pair)].det())
                  for pair in ((0, 1), (0, 2), (1, 2))]
        self.assertZero(sp.Matrix(minors)-sp.Matrix((
            (x2+alpha)*l2-(x1+beta)*l1,
            (x2+alpha)*l3-gamma*l1, (x1+beta)*l3-gamma*l2)))

    def test_uniform_rank_failure_forces_zero_linear_form(self):
        alpha, beta, gamma, l1, l2, l3 = sp.symbols("alpha beta gamma l1 l2 l3")
        minors = ((x2+alpha)*l2-(x1+beta)*l1,
                  (x2+alpha)*l3-gamma*l1, (x1+beta)*l3-gamma*l2)
        coefficients = [coefficient for minor in minors
                        for coefficient in sp.Poly(minor, x1, x2, x3).coeffs()]
        self.assertEqual(sp.linsolve(coefficients, (l1, l2, l3)),
                         sp.FiniteSet((0, 0, 0)))

    def test_nonlinear_plane_succeeds(self):
        self.assertEqual(apply(E, inverse[0]), 0)
        self.assertEqual(apply(E, sigma), 1)
        self.assertGreater(sp.Poly(inverse[0], *X).total_degree(), 1)

    def test_quasi_extension_noninvariant_multiplier(self):
        x, y, u, w = coords = sp.symbols("x y u w")
        field = sp.Matrix((u, 2*x*u, 1, 0))
        self.assertEqual(apply(field, u, coords), 1)
        self.assertEqual(apply(field, y-x*x, coords), 0)
        self.assertEqual(apply(field, x, coords), u)
        self.assertEqual(apply(field, y, coords), 2*x*u)

    def test_quasi_extension_degree_descent(self):
        x, y, u, w = coords = sp.symbols("x y u w")
        field = sp.Matrix((u, 2*x*u, 1, 0))
        plane = sp.Matrix((1, 2*x, 0, 0))
        for value in (x, y, x*y, x**3+y**2):
            image = apply(plane, value, coords)
            self.assertEqual(degree(field, image, coords),
                             degree(field, value, coords)-degree(field, u, coords)-1)

    def test_primitive_row_need_not_be_lnd_or_unimodular(self):
        x, y = coords = sp.symbols("x y")
        euler = sp.Matrix((x, y))
        self.assertEqual(sp.gcd(x, y), 1)
        self.assertEqual(euler.subs({x: 0, y: 0}), sp.zeros(2, 1))
        self.assertEqual(apply(euler, x, coords), x)

    def test_rational_normalizer_divisor_is_removed(self):
        s0, x, y, z = coords = sp.symbols("s0 x y z")
        translation = sp.Matrix((1, 0, 0, 0))
        primitive = sp.Matrix((0, 1, 0, 0))
        field = s0*primitive
        self.assertZero(bracket(translation, field, coords)-field/s0)
        self.assertZero(bracket(translation, primitive, coords))

    def test_slice_normalizer_requires_local_nilpotence(self):
        s0, x = coords = sp.symbols("s0 x")
        translation = sp.Matrix((1, 0))
        scaling = sp.Matrix((s0, 0))
        self.assertZero(bracket(scaling, translation, coords)+translation)
        self.assertEqual(apply(scaling, s0, coords), s0)

    def test_unimodular_control_commutes_and_is_nice(self):
        aa, bb, z, w = coords = sp.symbols("aa bb z w")
        v = aa-bb*z
        field, nice = sp.Matrix((bb*v, 0, v, 1)), sp.Matrix((z, 1, 0, 0))
        self.assertZero(bracket(field, nice, coords))
        self.assertZero(sp.Matrix([apply(field, entry, coords) for entry in field]))
        self.assertZero(sp.Matrix([apply(nice, entry, coords) for entry in nice]))
        self.assertEqual(apply(field, w, coords), 1)

    def test_unimodular_displayed_plane_not_projectable(self):
        aa, bb, z, w = sp.symbols("aa bb z w")
        v = aa-bb*z
        self.assertEqual(sp.diff(v, aa), 1)
        self.assertEqual(sp.Matrix((z, 1)).subs(z, 0), sp.Matrix((0, 1)))

    def test_nonunimodular_coordinate_matrix_inverse(self):
        x, y, aa, bb, v = sp.symbols("x y aa bb v")
        matrix = sp.Matrix(((1, v), (v, 1+v*v)))
        inv = sp.Matrix(((1+v*v, -v), (-v, 1)))
        self.assertZero(matrix*inv-sp.eye(2))
        Q, U = matrix*sp.Matrix((x, y))
        S, T = matrix*sp.Matrix((aa, bb))
        self.assertZero(U*S-Q*T-(y*aa-x*bb))

    def test_nonunimodular_commutation_and_slice(self):
        x, y, aa, bb, v = coords = sp.symbols("x y aa bb v")
        Q, U, S, T = x+v*y, v*x+(1+v*v)*y, aa+v*bb, v*aa+(1+v*v)*bb
        field = sp.Matrix((U*(v*x+(v*v-1)*y), -U*(x+v*y),
                           1+v*v+U*(v*aa+(v*v-1)*bb), -v-U*(aa+v*bb), U))
        nice = sp.Matrix((0, 0, x, y, 0))
        self.assertZero(bracket(field, nice, coords))
        self.assertZero(apply(field, y*aa-x*bb-v, coords))
        self.assertZero(sp.Matrix([apply(field, f, coords) for f in (Q, U, S, T)])
                        - sp.Matrix((0, 0, 1, 0)))

    def test_nonunimodular_plane_failure(self):
        x, y, v = sp.symbols("x y v")
        ratio = -v+y/(x+v*y)
        self.assertZero(sp.diff(ratio, v)+1+y*y/(x+v*y)**2)
        self.assertNotEqual(sp.cancel(sp.diff(ratio, v)), 0)

    def test_nonunimodular_missing_line_fixed(self):
        x, y, v = sp.symbols("x y v")
        U = v*x+(1+v*v)*y
        induced = sp.Matrix((U*(v*x+(v*v-1)*y), -U*(x+v*y), U))
        self.assertEqual(induced.subs({x: 0, y: 0}), sp.zeros(3, 1))

    def test_two_commuting_coordinate_slices(self):
        s0, x, y, z = coords = sp.symbols("s0 x y z")
        field, other = sp.Matrix((1, 0, 0, 0)), sp.Matrix((1, 0, x, 0))
        self.assertZero(bracket(field, other, coords))
        self.assertEqual(apply(field, s0, coords), 1)
        self.assertEqual(apply(other, s0, coords), 1)
        self.assertEqual(apply(other, y-s0*x, coords), 0)

    def test_quotient_action_has_fixed_divisor(self):
        x, y, z = coords = sp.symbols("x y z")
        quotient = sp.Matrix((0, x, 0))
        self.assertEqual(quotient.subs(x, 0), sp.zeros(3, 1))
        self.assertEqual(apply(quotient, y, coords), x)


if __name__ == "__main__":
    unittest.main(verbosity=2)
