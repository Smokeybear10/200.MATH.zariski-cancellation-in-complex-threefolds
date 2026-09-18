"""Finite controls for the polynomial moving-parameter repair.

These controls do not realize the full two-quadratic frame. The final
non-LND example has an actual first partial but lacks the required
second partial and highest-flow package. No solver is imported.
"""

import unittest

import sympy as sp


VARIABLES = sp.symbols("s t u z")
s, t, u, z = VARIABLES


def act(field, value):
    return sp.expand(sum(c * sp.diff(value, x)
                         for c, x in zip(field, VARIABLES)))


def bracket(left, right):
    return sp.Matrix([act(left, r) - act(right, l)
                      for l, r in zip(left, right)])


def divergence(field):
    return sp.expand(sum(sp.diff(c, x)
                         for c, x in zip(field, VARIABLES)))


def control(m):
    E = sp.Matrix([1, 0, 0, 0])
    U = sp.Matrix([0, 1, 0, 0])
    T = sp.Matrix([0, s, 0, 1])
    g, h = u*z, u
    H = sp.Matrix([0, 0, u, -z])
    Y = sp.Matrix([0, -g*s + h*t, u, -z])
    v = g**(m-1)*s - g**(m-2)*h*t
    repair = (g**(m-2)*Y + v*U).applyfunc(sp.expand)
    return E, U, T, g, h, H, Y, v, repair


class MovingCommutingRepairChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(value.applyfunc(sp.expand),
                             sp.zeros(*value.shape))
        else:
            self.assertEqual(sp.expand(value), 0)

    def test_first_partial_has_an_actual_two_sided_coordinate_frame(self):
        S, Q, V, Z = sp.symbols("S Q V Z")
        forward = sp.Matrix([s, t-s*z, u, z])
        inverse = sp.Matrix([S, Q+S*Z, V, Z])
        new = (S, Q, V, Z)
        self.assertZero(inverse.subs(dict(zip(new, forward)),
                                     simultaneous=True)-sp.Matrix(VARIABLES))
        self.assertZero(forward.subs(dict(zip(VARIABLES, inverse)),
                                     simultaneous=True)-sp.Matrix(new))
        E, U, T, g, h, H, Y, v, repair = control(3)
        self.assertZero(sp.Matrix([act(T, f) for f in forward])
                        - sp.Matrix([0, 0, 0, 1]))
        self.assertZero(bracket(E, T)-U)
        self.assertZero(bracket(E, U))
        self.assertZero(act(T, g)-h)
        self.assertZero(act(E, g))
        self.assertZero(act(U, g))
        self.assertZero(divergence(T))

    def test_derived_preslice_brackets_and_divergence_cancel_exactly(self):
        for m in (3, 4, 5):
            E, U, T, g, h, H, Y, v, repair = control(m)
            alpha = sp.Rational(m-1, 2)
            V = -g*U/alpha
            self.assertZero(bracket(E, Y)+g*U)
            self.assertZero(bracket(Y, U)+h*U)
            self.assertZero(bracket(Y, V)+h*V)
            self.assertZero(act(Y, g))
            self.assertZero(divergence(Y)-h)
            self.assertNotEqual(h, 0)
            self.assertZero(act(E, v)-g**(m-1))
            self.assertZero(act(U, v)+g**(m-2)*h)
            self.assertZero(repair-g**(m-2)*H)
            self.assertZero(bracket(E, repair))
            self.assertZero(bracket(U, repair))
            self.assertZero(bracket(V, repair))
            self.assertZero(act(repair, g))
            self.assertZero(divergence(repair))

    def test_nonzero_iterates_match_the_written_all_order_obstruction(self):
        # The all-n conclusion uses H(g)=0 and H(u)=u in the note.
        # These bounded iterations independently test that recurrence.
        for m in (3, 4, 5):
            E, U, T, g, h, H, Y, v, repair = control(m)
            self.assertZero(act(H, g))
            self.assertZero(act(H, u)-u)
            self.assertZero(act(H, z)+z)
            value_u, value_z = u, z
            for n in range(1, 8):
                value_u, value_z = act(repair, value_u), act(repair, value_z)
                self.assertZero(value_u-g**(n*(m-2))*u)
                self.assertZero(value_z-(-1)**n*g**(n*(m-2))*z)
                self.assertNotEqual(value_u, 0)
                self.assertNotEqual(value_z, 0)


if __name__ == "__main__":
    unittest.main()
