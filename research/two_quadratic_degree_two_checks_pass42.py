"""Finite controls for the degree-two tangent-plane and image arguments.

The actual model is the already known unimodular-pair cylinder. New tests
target the common-plane and bad-speed image deductions, not a new example.
No project solver or proof module is imported. Universal claims remain
in the written argument and cited recognition inputs.
"""

import unittest

import sympy as sp


def clean(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda item: sp.cancel(sp.expand(item)))
    return sp.cancel(sp.expand(value))


def act(field, value, variables):
    return clean(sum(coefficient * sp.diff(value, variable)
                     for coefficient, variable in zip(field, variables)))


def bracket(left, right, variables):
    return clean(right.jacobian(variables) * left - left.jacobian(variables) * right)


class TwoQuadraticDegreeTwoChecks(unittest.TestCase):
    def setUp(self):
        self.u, self.v, self.a, self.c = sp.symbols("u v a c")
        self.variables = (self.u, self.v, self.a, self.c)
        u, v, a, c = self.variables
        self.f, self.g = u, u*v-1
        self.E = sp.Matrix([0, 0, self.f, self.g])
        self.physical = sp.Matrix([u+a**2/2, v+c**2/2, a, c])
        self.partials = [sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 0, 0]),
                         sp.Matrix([-a, 0, 1, 0]), sp.Matrix([0, -c, 0, 1])]
        self.W = [bracket(self.E, partial, self.variables) for partial in self.partials]
        self.V = [bracket(self.E, self.W[index], self.variables) for index in (2, 3)]
        self.h = sp.Matrix([self.f**2, self.g**2, 0, 0])

    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_actual_common_tangent_plane_and_all_annihilations(self):
        fields = [self.E, *self.W[:2], *self.V]
        top = sp.Matrix.hstack(*self.V)
        self.assertEqual(top.rank(), 2)
        self.assertEqual(sp.Matrix.hstack(*fields).rank(), 2)
        self.assertEqual(self.h.jacobian(self.variables).rank(), 2)
        self.assertEqual(sp.Matrix([self.f, self.g]).jacobian(self.variables).rank(), 2)
        for index, field in enumerate(fields):
            with self.subTest(field=index):
                self.assertZero(self.h.jacobian(self.variables)*field)
                self.assertZero(act(field, self.f, self.variables))
                self.assertZero(act(field, self.g, self.variables))
        for left in fields:
            for right in fields:
                self.assertZero(bracket(left, right, self.variables))

    def test_actual_conjugate_columns_and_top_coefficients(self):
        time = sp.symbols("time")
        first = self.physical.applyfunc(lambda x: act(self.E, x, self.variables))
        flow = self.physical+time*first+time**2*self.h/2
        columns = []
        for index in range(4):
            column = self.partials[index]+time*self.W[index]
            if index >= 2:
                column += time**2*self.V[index-2]/2
            columns.append(column)
        self.assertZero(flow.jacobian(self.variables)*sp.Matrix.hstack(*columns)-sp.eye(4))
        self.assertZero(first.applyfunc(lambda x: act(self.E, x, self.variables))-self.h)
        self.assertZero(self.h.applyfunc(lambda x: act(self.E, x, self.variables)))
        self.assertEqual(sp.degree(flow[2], time), 1)
        self.assertEqual(sp.degree(flow[3], time), 1)

    def test_slice_quotient_restrictions_have_exact_rank_one(self):
        u, v, a, c = self.variables
        r, s = self.g*a-self.f*c, v*a-c
        self.assertZero(act(self.E, s, self.variables)-1)
        self.assertZero(act(self.E, r, self.variables))
        self.assertZero(self.f*s-r-a)
        self.assertZero(self.g*s-v*r-c)
        invariants = sp.Matrix([u, v, r])
        restricted = invariants.jacobian(self.variables)*sp.Matrix.hstack(*self.W[:2], *self.V)
        self.assertEqual(restricted.rank(), 1)
        self.assertZero(restricted[:2, :])
        self.assertNotEqual(restricted[2, 0], 0)
        self.assertZero(invariants.jacobian(self.variables)*self.E)

    def test_unrestricted_second_bracket_identity_and_invariant_specialization(self):
        # This identity is differentiated with fully symbolic coefficients.
        # No local nilpotence or invariance is assumed for this first control.
        x = sp.symbols("x0:4")
        P = sp.Matrix([sp.Function("p"+str(i))(*x) for i in range(4)])
        J = P.jacobian(x)
        F = P[2:4, :]
        EF = F.jacobian(x)*P
        for index in (2, 3):
            partial = sp.eye(4)[:, index]
            second = bracket(P, bracket(P, partial, x), x)
            self.assertZero(second[2:4, :]
                            - 2*F.jacobian(x)*J[:, index]
                            + EF.diff(x[index]))
        first = self.physical.applyfunc(lambda value: act(self.E, value, self.variables))
        frame = sp.Matrix.hstack(*self.partials)
        physical_jacobian = first.jacobian(self.variables)*frame
        speed_jacobian = sp.Matrix([self.f, self.g]).jacobian(self.variables)*frame
        physical_tops = self.physical.jacobian(self.variables)*sp.Matrix.hstack(*self.V)
        self.assertZero(physical_tops[2:4, :]-2*speed_jacobian*physical_jacobian[:, 2:4])

    def test_bad_speed_image_and_material_rank_hypothesis(self):
        F = sp.Matrix([self.f, self.g])
        projected = sp.Matrix.hstack(*self.V)[2:4, :]
        self.assertEqual(projected.row_join(F).rank(), projected.rank())
        u = self.u
        positive = sp.Matrix([u**2, 3*u**2])
        self.assertZero(positive.diff(u)*(u/2)-positive)
        self.assertZero(positive[0]*positive[1].diff(u)-positive[1]*positive[0].diff(u))
        self.assertZero(3*positive[0]-positive[1])
        # Rank-one Jacobian alone does not imply the image condition or a
        # constant projective direction. The dependent-defect example uses
        # this same polynomial pair after replacing u by u+v.
        negative = sp.Matrix([u, u**2+1])
        derivative = negative.diff(u)
        self.assertEqual(derivative.rank(), 1)
        self.assertEqual(derivative.row_join(negative).rank(), 2)
        self.assertNotEqual(clean(negative[0]*derivative[1]-negative[1]*derivative[0]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
