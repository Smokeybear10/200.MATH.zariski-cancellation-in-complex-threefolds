#!/usr/bin/env python3
"""Exact algebraic controls for the affine-quadratic-pencil written proof.

No solver imports. These checks do not formalize Euler characteristic or
certify every polynomial slice. Run with /opt/anaconda3/bin/python.
"""

import unittest

import sympy as sp


x, y, z, w = variables = sp.symbols("x y z w")
F, U, V, W = target = sp.symbols("F U V W")
v = sp.Matrix([y, z, w])
identity = sp.eye(3)
half = sp.Rational(1, 2)


def clean(value):
    return sp.cancel(sp.expand(value))


def substitute(expression, source, values):
    return clean(expression.subs(dict(zip(source, values)), simultaneous=True))


class QuadraticPencilTests(unittest.TestCase):
    def assert_matrix_zero(self, matrix):
        self.assertTrue(all(clean(entry) == 0 for entry in matrix))

    def assert_inverse(self, forward, inverse):
        for expression, expected in zip(forward, target):
            self.assertEqual(substitute(expression, variables, inverse), expected)
        for expression, expected in zip(inverse, variables):
            self.assertEqual(substitute(expression, target, forward), expected)

    def test_generic_rank_one_specialization_obstruction(self):
        alpha, q, r, s, t = sp.symbols("alpha q r s t")
        A = sp.diag(alpha, 0, 0)
        B = sp.Matrix([[q, r, s], [r, 0, 0], [s, 0, 0]])
        self.assertEqual(sp.expand((A+t*B).det()), 0)

    def test_nilpotent_square_root_index_three(self):
        A0 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        L = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
        A1 = A0*L
        S = identity + x*L/2 - x**2*L**2/8
        Sinv = identity - x*L/2 + 3*x**2*L**2/8
        self.assert_matrix_zero(L**3)
        self.assertNotEqual(L**2, sp.zeros(3))
        self.assert_matrix_zero(A1-A1.T)
        self.assert_matrix_zero(S*Sinv-identity)
        self.assert_matrix_zero(S**2-identity-x*L)
        self.assert_matrix_zero(S.T*A0*S-A0-x*A1)
        self.assertEqual((A0+x*A1).det(), -1)

    def test_generic_truncated_square_root_coefficient_identities(self):
        t = sp.symbols("t")
        square_root = 1+t/2-t**2/8
        inverse_root = 1-t/2+3*t**2/8
        self.assertEqual(sp.rem(square_root**2-(1+t), t**3, t), 0)
        self.assertEqual(sp.rem(square_root*inverse_root-1, t**3, t), 0)

    def test_positive_cubic_inverse(self):
        forward = (x+2*y*z+x*z**2+w**2, y+x*z/2, z, w)
        xi = F-2*U*V-W**2
        inverse = (xi, U-xi*V/2, V, W)
        self.assert_inverse(forward, inverse)
        self.assertEqual(sp.Matrix(forward).jacobian(variables).det(), 1)

    def test_positive_cubic_slice_and_local_nilpotence(self):
        polynomial = x+2*y*z+x*z**2+w**2

        def derivation(value):
            return sp.expand(sp.diff(value, x)-z*sp.diff(value, y)/2)

        self.assertEqual(derivation(polynomial), 1)
        for generator in variables:
            self.assertEqual(derivation(derivation(generator)), 0)

    def test_positive_cubic_has_no_constant_slice_direction(self):
        polynomial = x+2*y*z+x*z**2+w**2
        directions = sp.symbols("a:4")
        derivative = sum(a*sp.diff(polynomial, variable)
                         for a, variable in zip(directions, variables))
        equations = sp.Poly(derivative-1, variables).coeffs()
        self.assertEqual(sp.linsolve(equations, directions), sp.EmptySet)

    def test_full_matrix_inverse_with_nonzero_linear_term(self):
        A0 = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        L = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
        A = A0*(identity+x*L)
        b = sp.Matrix([1, x, 0])
        c = clean(3*x+2+(b.T*A.inv()*b)[0]/4)
        polynomial = clean((v.T*A*v)[0]+(b.T*v)[0]+c)
        S = identity+x*L/2-x**2*L**2/8
        Sinv = identity-x*L/2+3*x**2*L**2/8
        u = (S*(v+A.inv()*b/2)).applyfunc(clean)
        forward = (polynomial, *u)
        ut = sp.Matrix([U, V, W])
        xi = clean((F-(ut.T*A0*ut)[0]-2)/3)
        vi = (Sinv*ut-A.inv()*b/2).applyfunc(
            lambda expression: substitute(expression, (x,), (xi,)))
        inverse = (xi, *vi)
        for expression in (*forward, *inverse):
            self.assertEqual(sp.denom(clean(expression)).free_symbols, set())
        self.assert_inverse(forward, inverse)
        self.assertEqual(clean(polynomial-(u.T*A0*u)[0]-3*x-2), 0)

    def test_three_nonsingular_negative_controls(self):
        examples = (
            x+y+x*y*z+w**2,
            x*y**2+y+z**2+w**2,
            x+y**2+2*x*y*z+w**2,
        )
        for polynomial in examples:
            gradient = [sp.diff(polynomial, variable) for variable in variables]
            self.assertEqual(list(sp.groebner(gradient, *variables)), [1])

    def test_negative_control_determinants_and_center_values(self):
        examples = (
            (x+y+x*y*z+w**2, -x**2/4, x),
            (x*y**2+y+z**2+w**2, x, -1/(4*x)),
            (x+y**2+2*x*y*z+w**2, -x**2, x),
        )
        for polynomial, determinant, center_value in examples:
            A = sp.hessian(polynomial, (y, z, w))/2
            b = sp.Matrix([sp.diff(polynomial, variable).subs({y: 0, z: 0, w: 0})
                           for variable in (y, z, w)])
            c = polynomial.subs({y: 0, z: 0, w: 0})
            self.assertEqual(clean(A.det()-determinant), 0)
            self.assertEqual(clean(c-(b.T*A.inv()*b)[0]/4-center_value), 0)

    def test_special_fiber_rank_and_radical_linear_controls(self):
        examples = (
            (x+y+x*y*z+w**2, 1, True),
            (x*y**2+y+z**2+w**2, 2, True),
            (x+y**2+2*x*y*z+w**2, 2, False),
        )
        for polynomial, rank, radical_linear in examples:
            A = (sp.hessian(polynomial, (y, z, w))/2).subs(x, 0)
            b = sp.Matrix([sp.diff(polynomial, variable).subs(
                {x: 0, y: 0, z: 0, w: 0}) for variable in (y, z, w)])
            self.assertEqual(A.rank(), rank)
            self.assertEqual(A.row_join(b).rank() > rank, radical_linear)

    def test_critical_point_free_assumption_cannot_be_removed(self):
        polynomial = y**2+z**2+w**2+x**2
        self.assertEqual((sp.hessian(polynomial, (y, z, w))/2).det(), 1)
        self.assertEqual(tuple(sp.diff(polynomial, variable).subs(
            {x: 0, y: 0, z: 0, w: 0}) for variable in variables), (0, 0, 0, 0))

    def test_singular_pencil_moving_kernel_completion(self):
        A = sp.Matrix([[0, 0, x], [0, 0, -1], [x, -1, 0]])
        n = sp.Matrix([1, x, 0])
        M = sp.Matrix([[1, 0, 0], [x, 1, 0], [0, 0, 1]])
        self.assertEqual(A.det(), 0)
        self.assertEqual(A.rank(), 2)
        self.assert_matrix_zero(A*n)
        self.assertEqual(M.det(), 1)
        self.assert_matrix_zero(M.T*A*M-sp.Matrix(
            [[0, 0, 0], [0, 0, -1], [0, -1, 0]]))
        # There is no nonzero constant vector in the kernels at both 0 and 1.
        self.assertEqual(A.subs(x, 0).col_join(A.subs(x, 1)).rank(), 3)

    def test_singular_pencil_linear_radical_positive_inverse(self):
        forward = (y+2*(x*y-z)*w, x, z-x*y, w)
        yi = F+2*V*W
        inverse = (U, yi, V+U*yi, W)
        self.assert_inverse(forward, inverse)

    def test_singular_pencil_zero_radical_coefficient_control(self):
        forward = (x+2*(x*y-z)*w, y, z-x*y, w)
        xi = F+2*V*W
        inverse = (xi, U, V+xi*U, W)
        self.assert_inverse(forward, inverse)

    def test_nonaffine_family_smoothness_controls(self):
        for m in range(2, 6):
            polynomial = x+x**m*y*z+w**2
            gradient = [sp.diff(polynomial, variable) for variable in variables]
            self.assertEqual(list(sp.groebner(gradient, *variables)), [1])

    def test_nonaffine_family_open_inverse(self):
        lam, U0, V0, W0 = sp.symbols("lam U0 V0 W0")
        xi = lam-U0*V0-W0**2
        for m in range(2, 6):
            polynomial = x+x**m*y*z+w**2
            yi = U0/xi**m
            self.assertEqual(clean(polynomial.subs(
                {x: xi, y: yi, z: V0, w: W0}, simultaneous=True)-lam), 0)
            self.assertEqual(clean(xi**m*yi-U0), 0)
            # Reverse direction uses the equation F=lam to recover x.
            reverse_x = lam-x**m*y*z-w**2
            self.assertEqual(sp.expand(reverse_x-x-(lam-polynomial)), 0)

    def test_nonaffine_rank_one_exception_is_real(self):
        for m in range(2, 6):
            polynomial = x+x**m*y*z+w**2
            A = sp.hessian(polynomial, (y, z, w))/2
            self.assertEqual(A.subs(x, 0).rank(), 1)
            self.assertEqual(sp.expand(A.det()+x**(2*m)/4), 0)
            self.assertEqual(sp.diff(A, x).subs(x, 0), sp.zeros(3))
            # Rank rises through higher powers of x, despite a vanishing
            # derivative on the radical. This is not an affine pencil.
            self.assertEqual(A.rank(), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
