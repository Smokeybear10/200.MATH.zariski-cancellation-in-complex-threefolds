"""Four exact controls for the leading-plane repair obstruction.

The written annihilation/induction proof supplies the quantifiers over
all polynomial coefficients and all slices. Finite slice and iterate
checks below are not substitutes for those quantifiers.
"""

import unittest

import sympy as sp


def clean(expression):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(lambda item: sp.cancel(sp.expand(item)))
    return sp.cancel(sp.expand(expression))


def act(field, expression, variables):
    return clean(sum(value*sp.diff(expression, variable)
                     for value, variable in zip(field, variables)))


def bracket(left, right, variables):
    return clean(sp.Matrix([
        act(left, value, variables)-act(right, other, variables)
        for value, other in zip(right, left)
    ]))


class LeadingPlaneRepairChecks(unittest.TestCase):
    def setUp(self):
        self.u, self.v, self.a, self.c = sp.symbols("u v a c")
        u, v, a, c = self.variables = (self.u, self.v, self.a, self.c)
        self.g = u*v-1
        self.E = sp.Matrix([0, 0, u, self.g])
        self.s = v*a-c
        self.r = self.g*a-u*c
        self.physical = sp.Matrix([u+a**2/2, v+c**2/2, a, c])
        self.partials = self.physical.jacobian(self.variables).inv()
        self.W = [bracket(self.E, self.partials[:, i], self.variables)
                  for i in range(4)]
        self.V = [bracket(self.E, self.W[i], self.variables)
                  for i in range(4)]
        second = sp.Matrix([act(self.E, act(self.E, value, self.variables),
                                self.variables) for value in self.physical])
        self.H = clean(self.partials*second)
        self.L = bracket(self.E, self.H, self.variables)

    def assertZero(self, expression):
        if isinstance(expression, sp.MatrixBase):
            self.assertEqual(clean(expression), sp.zeros(*expression.shape))
        else:
            self.assertEqual(clean(expression), 0)

    def test_actual_inverse_profiles_ranks_and_highest_bracket(self):
        u, v, a, c = self.variables
        g, E = self.g, self.E
        self.assertZero(act(E, self.s, self.variables)-1)
        self.assertZero(act(E, self.r, self.variables))
        r, s = sp.symbols("r s")
        inverse = {a: u*s-r, c: g*s-v*r}
        self.assertZero(self.s.subs(inverse, simultaneous=True)-s)
        self.assertZero(self.r.subs(inverse, simultaneous=True)-r)
        self.assertZero(u*self.s-self.r-a)
        self.assertZero(g*self.s-v*self.r-c)
        self.assertZero(self.H-sp.Matrix([u**2, g**2, 0, 0]))
        self.assertZero(self.L-sp.Matrix([0, 0, -u**2, -u**2*v-u*g**2]))
        self.assertZero(self.L+(u*self.V[2]+g*self.V[3])/2)
        self.assertZero(bracket(E, self.L, self.variables))
        self.assertEqual(sp.Matrix.hstack(self.V[2], self.V[3]).rank(), 2)
        self.assertZero(sp.Matrix([u, g]).jacobian((u, v)).det()-u)
        for i in range(4):
            expected = 1 if i < 2 else 2
            field = self.partials[:, i]
            for unused in range(expected):
                field = bracket(E, field, self.variables)
            self.assertNotEqual(field, sp.zeros(4, 1))
            self.assertZero(bracket(E, field, self.variables))
        quotient_coordinates = sp.Matrix([u, v, self.r, self.s])
        transported = quotient_coordinates.jacobian(self.variables)*self.partials
        transported = transported.subs(inverse, simultaneous=True)
        for i in range(4):
            coefficients = transported[:, i]
            # The shifted filtration counts the slice coefficient with -1.
            height = max([sp.degree(value, s) for value in coefficients[:3]
                          if value != 0]
                         + [sp.degree(coefficients[3], s)-1]
                         + [-1])
            self.assertEqual(height, 1 if i < 2 else 2)

    def test_true_tangent_projection_for_distinct_polynomial_slices(self):
        u, v, a, c = self.variables
        for q in (0, self.r, u*v+self.r**2):
            with self.subTest(q=q):
                sigma = self.s+q
                self.assertZero(act(self.E, sigma, self.variables)-1)
                alpha = act(self.H, sigma, self.variables)-sigma*act(
                    self.L, sigma, self.variables)
                repaired = clean(self.H-sigma*self.L-alpha*self.E)
                self.assertZero(act(self.E, alpha, self.variables))
                self.assertZero(bracket(self.E, repaired, self.variables))
                self.assertZero(act(repaired, sigma, self.variables))
                self.assertZero(act(repaired, u, self.variables)-u**2)
                self.assertZero(act(repaired, v, self.variables)-self.g**2)

    def test_entire_module_annihilation_and_unit_derivative_ideal(self):
        u, v, a, c = self.variables
        generators = sp.Matrix.hstack(self.E, self.W[0], self.W[1],
                                      self.V[2], self.V[3])
        # This zero row identity is independent of every coefficient choice.
        self.assertZero(generators[:2, :])
        symbols = sp.Matrix(sp.symbols("k0:5"))
        repaired = self.H+generators*symbols
        self.assertZero(repaired[0]-u**2)
        self.assertZero(repaired[1]-self.g**2)
        self.assertZero(u**2*(v**2-2*v**2*self.g)
                        + self.g**2*(3+2*self.g)-1)
        self.assertEqual(sp.gcd(u**2, self.g**2), 1)
        nonconstant = sp.Matrix([a*c+u, v**3, self.s*self.r,
                                 u**2+c, self.s**2+a*v])
        repaired = clean(self.H+generators*nonconstant)
        current = u
        for n in range(1, 9):
            current = act(repaired, current, self.variables)
            self.assertZero(current-sp.factorial(n)*u**(n+1))

    def test_explicit_quotient_field_and_nonzero_iterates(self):
        u, v, a, c = self.variables
        alpha = act(self.H, self.s, self.variables)-self.s*act(
            self.L, self.s, self.variables)
        self.assertZero(alpha+self.g**2*self.r)
        repaired = clean(self.H-self.s*self.L-alpha*self.E)
        image = sp.Matrix([act(repaired, value, self.variables)
                           for value in (u, v, self.r, self.s)])
        expected = sp.Matrix([u**2, self.g**2, -u*self.g**2*self.r, 0])
        self.assertZero(image-expected)
        r = sp.symbols("r")
        quotient = sp.Matrix([u**2, self.g**2, -u*self.g**2*r])
        current = u
        for n in range(1, 11):
            current = act(quotient, current, (u, v, r))
            self.assertZero(current-sp.factorial(n)*u**(n+1))
            self.assertNotEqual(current, 0)


if __name__ == "__main__":
    unittest.main()
