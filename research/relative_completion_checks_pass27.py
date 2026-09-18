"""Exact finite controls for relative-completion-pass27.md.

Imports only unittest and SymPy. The published global slice-existence
theorem is not inferred from these finite polynomial controls.
"""

import unittest
import sympy as sp


u, v, z, p, f, s, phat = sp.symbols("u v z p f s phat")


def act(field, expression, variables=(u, v)):
    return sp.expand(sum(c * sp.diff(expression, x)
                         for c, x in zip(field, variables)))


def bracket(left, right, variables=(u, v)):
    return tuple(sp.expand(act(left, c, variables)
                           - act(right, b, variables))
                 for b, c in zip(left, right))


def determinant(left, right):
    return sp.expand(left[0] * right[1] - left[1] * right[0])


def finite_integral(field, value, slice_value, variables, bound=30):
    result = sp.Integer(0)
    derivative = sp.expand(value)
    for j in range(bound):
        if derivative == 0:
            return sp.expand(result)
        result += (-1) ** j * slice_value ** (j + 1) * derivative / sp.factorial(j + 1)
        derivative = act(field, derivative, variables)
    raise AssertionError("The declared finite nilpotence bound was exceeded")


class RelativeCompletionChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.P = u + v ** 2
        cls.F = v + cls.P ** 3
        cls.V = (sp.diff(cls.F, v), -sp.diff(cls.F, u))
        cls.Wbase = (-2 * v, sp.Integer(1))
        cls.q = cls.P ** 3 * cls.F + cls.F ** 2 + z * cls.P ** 2
        cls.W0 = tuple(sp.expand(w + cls.q * d)
                       for w, d in zip(cls.Wbase, cls.V))
        cls.g = cls.P ** 3 * cls.F + z * cls.P ** 2
        cls.W = tuple(sp.expand(w - cls.g * d)
                      for w, d in zip(cls.W0, cls.V))

    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_unrestricted_bracket_divergence_identity(self):
        a, b, c, e = (sp.Function(name)(u, v) for name in ("a", "b", "c", "e"))
        V, W = (a, b), (c, e)
        J = a * e - b * c
        divV, divW = sp.diff(a, u) + sp.diff(b, v), sp.diff(c, u) + sp.diff(e, v)
        commutator = bracket(V, W)
        self.zero(commutator[0] - divW * a + sp.diff(J, v) + c * divV)
        self.zero(commutator[1] - divW * b - sp.diff(J, u) + e * divV)

    def test_nonlinear_actual_coordinate_inverse(self):
        inverse_v = f - p ** 3
        inverse_u = p - inverse_v ** 2
        substitution = {u: inverse_u, v: inverse_v}
        self.zero(self.P.subs(substitution, simultaneous=True) - p)
        self.zero(self.F.subs(substitution, simultaneous=True) - f)
        self.zero(inverse_u.subs({p: self.P, f: self.F}, simultaneous=True) - u)
        self.zero(inverse_v.subs({p: self.P, f: self.F}, simultaneous=True) - v)

    def test_volume_and_unit_coefficient_identity(self):
        self.zero(sp.diff(self.V[0], u) + sp.diff(self.V[1], v))
        self.zero(determinant(self.V, self.Wbase) - 1)
        self.zero(act(self.V, self.P) - 1)
        self.zero(act(self.V, self.F))

    def test_chosen_bezout_complement_really_fails_commutation(self):
        h = sp.expand(sp.diff(self.W0[0], u) + sp.diff(self.W0[1], v))
        self.zero(h - (3 * self.P ** 2 * self.F + 2 * z * self.P))
        self.zero(determinant(self.V, self.W0) - 1)
        self.assertNotEqual(h, 0)
        for entry, coefficient in zip(bracket(self.V, self.W0), self.V):
            self.zero(entry - h * coefficient)

    def test_finite_right_inverse_on_polynomial_values(self):
        field = (sp.Integer(1), sp.Integer(0))
        for degree in range(8):
            h = (f ** 2 + z) * p ** degree + f * p
            g = finite_integral(field, h, p, (p, f))
            self.zero(act(field, g, (p, f)) - h)
            self.zero(g.subs(p, 0))

    def test_slice_integral_keeps_invariant_ambiguity(self):
        h = 3 * p ** 2 * f + 2 * z * p
        g = finite_integral((sp.Integer(1), sp.Integer(0)), h, p, (p, f))
        self.zero(g - (p ** 3 * f + z * p ** 2))
        self.zero((p ** 3 * f + f ** 2 + z * p ** 2) - g - f ** 2)

    def test_correction_preserves_determinant_and_commutes(self):
        self.zero(determinant(self.V, self.W) - 1)
        for entry in bracket(self.V, self.W):
            self.zero(entry)
        self.zero(act(self.W, self.P) - self.F ** 2)
        self.zero(act(self.W, self.F) - 1)

    def test_corrected_dual_coordinates_are_actual(self):
        corrected_P = self.P - self.F ** 3 / 3
        self.zero(act(self.V, corrected_P) - 1)
        self.zero(act(self.W, corrected_P))
        old_p = phat + f ** 3 / 3
        old_v = f - old_p ** 3
        old_u = old_p - old_v ** 2
        substitution = {u: old_u, v: old_v}
        self.zero(corrected_P.subs(substitution, simultaneous=True) - phat)
        self.zero(self.F.subs(substitution, simultaneous=True) - f)

    def test_corrected_complement_nilpotence_on_original_generators(self):
        field = (f ** 2, sp.Integer(1))
        old_v, old_u = f - p ** 3, p - (f - p ** 3) ** 2
        for expression, bound in ((old_v, 10), (old_u, 19)):
            derivative = expression
            for _ in range(bound):
                derivative = act(field, derivative, (p, f))
            self.zero(derivative)

    def test_primitive_does_not_mean_unit_image_ideal(self):
        self.assertEqual(sp.gcd(z, u), 1)
        self.assertEqual(z.subs({z: 0, u: 0}), 0)
        self.assertEqual(u.subs({z: 0, u: 0}), 0)
        basis = sp.groebner([z, u], z, u, v)
        self.assertEqual(basis.reduce(sp.Integer(1))[1], 1)

    def test_quotient_can_be_free_without_ambient_freeness(self):
        field = (s - 1, u)
        self.assertEqual(field[0].subs({s: 1, u: 0}), 0)
        self.assertEqual(field[1].subs({s: 1, u: 0}), 0)
        self.zero(act(field, -u).subs(s, 0) - 1)
        self.zero(act(field, s))


if __name__ == "__main__":
    unittest.main(verbosity=2)
