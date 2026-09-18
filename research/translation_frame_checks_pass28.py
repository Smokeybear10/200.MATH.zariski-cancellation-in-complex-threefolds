"""Independent finite controls for translation-frame-pass28.md.

Only unittest and SymPy are imported. The universal center induction,
degree bound and cited group/strong-nilpotence inputs remain written proofs.
"""

import unittest
import sympy as sp


x, y, u, v, s = sp.symbols("x y u v s")


def act(field, value, variables):
    return sp.expand(sum(a * sp.diff(value, z)
                         for a, z in zip(field, variables)))


def bracket(left, right, variables):
    return tuple(sp.expand(act(left, a, variables) - act(right, b, variables))
                 for a, b in zip(right, left))


def independent(fields, variables):
    fields = [tuple(sp.expand(a) for a in field) for field in fields
              if any(a != 0 for a in field)]
    if not fields:
        return []
    keys = sorted({(index, monomial)
                   for field in fields
                   for index, value in enumerate(field)
                   for monomial in sp.Poly(value, *variables).monoms()})
    columns = []
    for field in fields:
        terms = [sp.Poly(value, *variables).as_dict() for value in field]
        columns.append([terms[index].get(monomial, 0) for index, monomial in keys])
    pivots = sp.Matrix.hstack(*(sp.Matrix(column) for column in columns)).rref()[1]
    return [fields[index] for index in pivots]


def word_layer(fields, generators, variables):
    return independent([bracket(a, b, variables)
                        for a in fields for b in generators], variables)


class TranslationFrameChecks(unittest.TestCase):
    def test_weight_recurrence_including_zero_and_linear_degree(self):
        for degree in range(5):
            for n in range(1, 6):
                weights = [1]
                for _ in range(n-1):
                    weights.append(degree * weights[-1] + 1)
                self.assertEqual(weights[-1], sum(degree**j for j in range(n)))
                self.assertTrue(all(a <= b for a, b in zip(weights, weights[1:])))
                self.assertEqual(weights[0], 1)
                for i in range(1, n):
                    self.assertEqual(degree * weights[i-1], weights[i]-1)

    def test_positive_nonlinear_field_and_actual_linear_frame(self):
        old = sp.symbols("x0:4")
        new = sp.symbols("z0:4")
        matrix = sp.Matrix([[1, 1, 0, 0], [0, 1, 1, 0],
                            [0, 0, 1, 1], [0, 0, 0, 1]])
        self.assertEqual(matrix.det(), 1)
        coords = matrix * sp.Matrix(old)
        inverse = matrix.inv() * sp.Matrix(new)
        for got, wanted in zip(coords.subs(dict(zip(old, inverse)),
                                           simultaneous=True), new):
            self.assertEqual(sp.expand(got-wanted), 0)
        triangular = sp.Matrix([1, new[0]**2, new[1], new[2]**2])
        physical = matrix.inv() * triangular.subs(dict(zip(new, coords)),
                                                   simultaneous=True)
        recovered = (matrix * physical).subs(dict(zip(old, inverse)),
                                             simultaneous=True)
        self.assertEqual(recovered.applyfunc(sp.expand), triangular)

    def test_positive_field_strictly_decreases_common_weight(self):
        variables = sp.symbols("z0:4")
        weights = (1, 3, 7, 15)
        field = (1, variables[0]**2, variables[1], variables[2]**2)
        for index, value in enumerate(field):
            for monomial in sp.Poly(value, *variables).monoms():
                self.assertLess(sum(a*b for a, b in zip(monomial, weights)),
                                weights[index])
        for index in range(4):
            self.assertGreaterEqual(weights[index], 1)

    def test_published_strong_product_condition_on_positive_field(self):
        variables = sp.symbols("z0:4")
        field = sp.Matrix([1, variables[0]**2, variables[1], variables[2]**2])
        jacobian = field.jacobian(variables)
        product = sp.eye(4)
        for stage in range(4):
            fresh = sp.symbols("p%d_0:4" % stage)
            product = (jacobian.subs(dict(zip(variables, fresh)),
                                    simultaneous=True) * product).applyfunc(sp.expand)
            if stage == 2:
                self.assertNotEqual(product, sp.zeros(4))
        self.assertEqual(product, sp.zeros(4))

    def test_actual_bad_frame_coordinate_inverse_in_both_directions(self):
        slice_value = x+y**2
        invariant = y+slice_value**2
        field = (1+4*y*(x+y**2), -2*(x+y**2))
        self.assertEqual(act(field, slice_value, (x, y)), 1)
        self.assertEqual(act(field, invariant, (x, y)), 0)
        old_y = s-u**2
        old_x = u-old_y**2
        inverse = {x: old_x, y: old_y}
        self.assertEqual(sp.expand(slice_value.subs(inverse, simultaneous=True)-u), 0)
        self.assertEqual(sp.expand(invariant.subs(inverse, simultaneous=True)-s), 0)
        forward = {u: slice_value, s: invariant}
        self.assertEqual(sp.expand(old_x.subs(forward, simultaneous=True)-x), 0)
        self.assertEqual(sp.expand(old_y.subs(forward, simultaneous=True)-y), 0)

    def test_complete_five_field_bracket_table_and_generation(self):
        basis = [(1, 0), (0, 1), (0, u), (v, 0), (u, -v)]
        expected = {
            (0, 2): (0, 1), (0, 4): (1, 0), (1, 3): (1, 0),
            (1, 4): (0, -1), (2, 3): (u, -v),
            (2, 4): (0, -2*u), (3, 4): (2*v, 0),
        }
        for i in range(5):
            for j in range(i+1, 5):
                self.assertEqual(bracket(basis[i], basis[j], (u, v)),
                                 expected.get((i, j), (0, 0)))
        self.assertEqual(len(independent(basis, (u, v))), 5)
        inputs = [(1, 0), (2*v, 1), (1, -2*u)]
        generated = independent(inputs, (u, v))
        for _ in range(5):
            generated = independent(generated+word_layer(generated, inputs, (u, v)),
                                    (u, v))
        self.assertEqual(len(generated), 5)

    def test_finite_closure_is_perfect_and_has_nonnilpotent_member(self):
        basis = [(1, 0), (0, 1), (0, u), (v, 0), (u, -v)]
        derived = independent([bracket(a, b, (u, v))
                               for a in basis for b in basis], (u, v))
        self.assertEqual(len(derived), 5)
        field = (1+4*y*(x+y**2), -2*(x+y**2))
        witness = bracket((0, 1), field, (x, y))
        self.assertEqual(witness, (4*x+12*y**2, -4*y))
        current = y
        for exponent in range(1, 7):
            current = act(witness, current, (x, y))
            self.assertEqual(current, (-4)**exponent*y)

    def test_no_affine_linear_first_coordinate_in_bad_frame(self):
        a, b, c = sp.symbols("a b c")
        field = (1+4*y*(x+y**2), -2*(x+y**2))
        image = act(field, a*x+b*y+c, (x, y))
        self.assertEqual(sp.Poly(image, x, y).coeff_monomial(y**3), 4*a)
        self.assertEqual(sp.Poly(image.subs(a, 0), x, y).coeff_monomial(y**2), -2*b)
        self.assertEqual(image.subs({a: 0, b: 0}), 0)

    def test_exact_word_layers_separate_positive_and_bad_frames(self):
        positive = [(1, 0), (0, 1), (0, x**2)]
        layer = independent(positive, (x, y))
        for length in range(2, 5):
            layer = word_layer(layer, positive, (x, y))
            if length == 3:
                self.assertNotEqual(layer, [])
        self.assertEqual(layer, [])  # W=1+2=3; all length-four words vanish.
        bad = [(1, 0), (2*v, 1), (1, -2*u)]
        layer = independent(bad, (u, v))
        for _ in range(2, 6):
            layer = word_layer(layer, bad, (u, v))
        self.assertNotEqual(layer, [])  # Original degree d=3, W=4.

    def test_bad_frame_fails_strong_jacobian_test_exactly(self):
        field = sp.Matrix([1+4*y*(x+y**2), -2*(x+y**2)])
        jacobian = field.jacobian((x, y))
        self.assertEqual(sp.expand(jacobian.det()), 8*(x+y**2))
        at_point = jacobian.subs({x: 1, y: 0})
        self.assertNotEqual(at_point**2, sp.zeros(2))
        self.assertNotEqual(at_point**4, sp.zeros(2))
        # The same block remains nonzero after adjoining two fixed variables.
        ambient = sp.diag(at_point, sp.zeros(2))
        self.assertNotEqual(ambient**4, sp.zeros(4))


if __name__ == "__main__":
    unittest.main(verbosity=2)
