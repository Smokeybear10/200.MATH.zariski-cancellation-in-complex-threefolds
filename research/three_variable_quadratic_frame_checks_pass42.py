"""Six exact controls for the three-variable quadratic-frame theorem.

These check universal finite matrix identities and actual polynomial
actions. They do not machine-prove the published recognition theorems.
The projective-column control is explicitly separate from an actual
last iterate of a derivation.
"""

import unittest

import sympy as sp


def clean(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda item: sp.cancel(sp.expand(item)))
    return sp.cancel(sp.expand(value))


def act(field, value, variables):
    return clean(sum(coefficient*sp.diff(value, variable)
                     for coefficient, variable in zip(field, variables)))


def bracket(left, right, variables):
    return clean(sp.Matrix([
        act(left, right[index], variables)-act(right, left[index], variables)
        for index in range(len(variables))
    ]))


def substitute(value, variables, images):
    return clean(value.subs(dict(zip(variables, images)), simultaneous=True))


def coefficient(matrix, variable, degree):
    return matrix.applyfunc(lambda item: sp.Poly(sp.expand(item), variable)
                            .coeff_monomial(variable**degree))


class ThreeVariableQuadraticFrameChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_generic_rank_one_adjugate_update(self):
        entries = sp.symbols("a0:9")
        matrix = sp.Matrix(3, 3, entries)
        column = sp.Matrix(sp.symbols("v0:3"))
        row = sp.Matrix(sp.symbols("h0:3")).T
        q = sp.symbols("q")
        updated = matrix+q*column*row
        self.assertZero(updated.adjugate()*column-matrix.adjugate()*column)
        self.assertZero(updated.det()-matrix.det()-q*(row*matrix.adjugate()*column)[0])
        time = sp.symbols("time")
        J = sp.Matrix(3, 3, sp.symbols("j0:9"))
        inverse_flow = sp.eye(3)-time*J+time**2*column*row/2
        image = clean(inverse_flow.adjugate()*column)
        self.assertTrue(all(sp.degree(value, time) <= 2 for value in image))
        self.assertZero(image-(sp.eye(3)-time*J).adjugate()*column)

    def test_exact_high_flow_coefficients_in_both_top_degrees(self):
        time = sp.symbols("time")
        J = sp.Matrix(3, 3, sp.symbols("j0:9"))
        v = sp.Matrix(sp.symbols("v0:3"))
        h = sp.Matrix(sp.symbols("h0:3"))
        last = sp.Matrix(sp.symbols("H0:3"))
        before = sp.Matrix(sp.symbols("L0:3"))
        S = v*h.T
        inverse_flow = sp.eye(3)-time*J+time**2*S/2
        for degree in (2, 3):
            with self.subTest(degree=degree):
                if degree == 2:
                    flow_derivative = v+time*last
                    previous = v
                else:
                    flow_derivative = v+time*before+time**2*last/2
                    previous = before
                product = inverse_flow*flow_derivative
                high = coefficient(product, time, degree+1)
                next_high = coefficient(product, time, degree)
                self.assertZero(high-S*last/(2*sp.factorial(degree-1)))
                self.assertZero(next_high+J*last/sp.factorial(degree-1)
                                - S*previous/(2*sp.factorial(degree-2)))
                self.assertZero(sp.factorial(degree-1)*next_high
                                + J*last-sp.Rational(degree-1, 2)*S*previous)

    def test_high_adjugate_coefficient_uses_three_by_three_minors(self):
        time = sp.symbols("time")
        J = sp.Matrix(3, 3, sp.symbols("j0:9"))
        middle = sp.Matrix(3, 3, sp.symbols("k0:9"))
        top = sp.Matrix(3, 3, sp.symbols("h0:9"))
        for degree in (2, 3):
            with self.subTest(degree=degree):
                jacobian = sp.eye(3)+time*J+time**degree*top/sp.factorial(degree)
                if degree == 3:
                    jacobian += time**2*middle/2
                highest = coefficient(jacobian.adjugate(), time, 2*degree)
                self.assertZero(highest-top.adjugate()/sp.factorial(degree)**2)
        u = sp.Matrix(sp.symbols("u0:3"))
        v = sp.Matrix(sp.symbols("v0:3"))
        self.assertZero((u*v.T).adjugate())
        rank_two = sp.diag(1, 1, 0)
        self.assertNotEqual(rank_two.adjugate(), sp.zeros(3))

    def test_actual_exact_profile_with_unsliced_three_variable_base(self):
        y1, y2, y3, t = sp.symbols("y1 y2 y3 t")
        k1, k2, k3, s = sp.symbols("k1 k2 k3 s")
        ys = (y1, y2, y3)
        variables = ys+(t,)
        y = sp.Matrix(ys)
        k = sp.Matrix([k1, k2, k3])
        nilpotent = sp.Matrix([[-1, -3, -1], [1, 1, 1], [0, 2, 0]])
        self.assertZero(nilpotent**3)
        self.assertNotEqual(nilpotent**2, sp.zeros(3))
        base = nilpotent*y
        self.assertZero(base.subs({y1: 0, y2: 0, y3: 0}))
        # The base has a fixed point, so its image ideal cannot contain 1.
        action = base.col_join(sp.Matrix([1]))
        self.assertZero(act(action, t, variables)-1)
        pt = sp.Matrix([0, 0, 0, 1])
        self.assertZero(bracket(action, pt, variables))
        for index in range(3):
            partial = sp.eye(4)[:, index]
            second = bracket(action, bracket(action, partial, variables), variables)
            self.assertNotEqual(second, sp.zeros(4, 1))
            self.assertZero(bracket(action, second, variables))
        first_top = nilpotent**2*sp.eye(3)[:, 0]
        self.assertZero(bracket(base, first_top, ys))
        self.assertNotEqual(clean(sp.Matrix.hstack(base, first_top)[0:2, :].det()), 0)
        minus_flow = sp.eye(3)-t*nilpotent+t**2*nilpotent**2/2
        plus_flow = sp.eye(3)+s*nilpotent+s**2*nilpotent**2/2
        invariants = minus_flow*y
        forward = invariants.col_join(sp.Matrix([t]))
        inverse = (plus_flow*k).col_join(sp.Matrix([s]))
        targets = (k1, k2, k3, s)
        self.assertZero(substitute(forward, variables, inverse)-sp.Matrix(targets))
        self.assertZero(substitute(inverse, targets, forward)-sp.Matrix(variables))
        self.assertZero(sp.Matrix([act(action, value, variables) for value in invariants]))
        self.assertZero(forward.jacobian(variables).det()-1)
        for index in range(3):
            transformed_column = substitute(forward.jacobian(variables)[:, index],
                                            variables, inverse)
            self.assertEqual(max(sp.degree(value, s) for value in transformed_column
                                 if value != 0), 2)
        transformed_t = substitute(forward.jacobian(variables)[:, 3], variables, inverse)
        self.assertEqual(max(sp.degree(value, s) for value in transformed_t if value != 0), 0)

    def test_actual_zero_quadratic_top_branch_and_cubic_coordinate_flow(self):
        x, y, z, time = sp.symbols("x y z time")
        variables = (x, y, z)
        points = sp.Matrix(variables)
        field = sp.Matrix([1, x, y+x**2/2])
        for index in range(3):
            partial = sp.eye(3)[:, index]
            self.assertZero(bracket(field, bracket(field, partial, variables), variables))
        second = sp.Matrix([act(field, value, variables) for value in field])
        third = sp.Matrix([act(field, value, variables) for value in second])
        self.assertZero(third-sp.Matrix([0, 0, 2]))
        self.assertZero(sp.Matrix([act(field, value, variables) for value in third]))
        flow = points+time*field+time**2*second/2+time**3*third/6
        J = field.jacobian(variables)
        inverse_jacobian = sp.eye(3)-time*J
        self.assertZero(inverse_jacobian*flow.jacobian(variables)-sp.eye(3))
        self.assertZero(flow.jacobian(variables)*inverse_jacobian-sp.eye(3))
        self.assertZero(inverse_jacobian.adjugate()*field-flow.diff(time))
        self.assertZero(bracket(field, third, variables))
        self.assertZero(third.jacobian(variables)*third)
        self.assertZero(act(field, y-x**2/2, variables))

    def test_projective_constancy_requires_the_nonzero_eigenvector_identity(self):
        x, y, z = sp.symbols("x y z")
        variables = (x, y, z)
        polynomial = x+2*y+3*z
        constant_direction = sp.Matrix([1, -1, 2])
        top = polynomial**2*constant_direction
        self.assertEqual(top.jacobian(variables).rank(), 1)
        self.assertZero(top.jacobian(variables)*top-10*polynomial*top)
        for component in top:
            for variable in variables:
                self.assertZero(sp.diff(component/top[0], variable))
        h = sp.Matrix([1, 1, 0])
        self.assertZero((h.T*top)[0])
        self.assertZero((h.T*constant_direction)[0])
        # A rank-one Jacobian alone does not make the image a fixed line.
        # Neither this control nor the positive column is asserted to be
        # an actual highest D-iterate from the theorem.
        curved = sp.Matrix([x, x**2, 0])
        self.assertEqual(curved.jacobian(variables).rank(), 1)
        image = curved.jacobian(variables)*curved
        self.assertNotEqual(clean(sp.Matrix.hstack(curved, image)[0:2, :].det()), 0)
        self.assertNotEqual(sp.diff(curved[1]/curved[0], x), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
