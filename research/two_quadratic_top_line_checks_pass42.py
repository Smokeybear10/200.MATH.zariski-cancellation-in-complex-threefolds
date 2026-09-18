"""Finite exact controls for the full-companion top-line reduction.

Only the boundary example is asserted to realize the two-quadratic
rank-two frame. Jordan matrices and rotating coefficient data are
formal controls, not constructed higher-flow actions. No solver imports.
"""

import unittest

import sympy as sp


def act(field, polynomial, variables):
    return sp.expand(sum(v * sp.diff(polynomial, x)
                         for v, x in zip(field, variables)))


def bracket(left, right, variables):
    return sp.Matrix([act(left, p, variables) - act(right, q, variables)
                      for p, q in zip(right, left)])


def clean(matrix):
    return matrix.applyfunc(sp.cancel)


def partitions(total, largest=None):
    if total == 0:
        yield ()
        return
    if largest is None:
        largest = total
    for first in range(min(total, largest), 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def jordan(sizes):
    blocks = []
    for size in sizes:
        block = sp.zeros(size)
        for i in range(size - 1):
            block[i, i + 1] = 1
        blocks.append(block)
    return sp.diag(*blocks)


class TwoQuadraticTopLineChecks(unittest.TestCase):
    def test_full_image_line_and_constant_top_jordan_boundaries(self):
        admitted = []
        for sizes in partitions(6):
            m = sizes[0] - 1
            if m < 3:
                continue
            admitted.append(sizes)
            matrix = jordan(sizes)
            previous = matrix ** (m - 1)
            highest = matrix ** m
            self.assertEqual(highest.rank(), 1)
            self.assertEqual(previous.rank() - highest.rank(), 1)
            self.assertEqual(matrix * highest, sp.zeros(6))
            self.assertEqual(previous.row_join(highest).rank(),
                             previous.rank())
        self.assertEqual(admitted, [(6,), (5, 1), (4, 2), (4, 1, 1)])

        boundary = jordan((3, 3))
        self.assertEqual(boundary ** 3, sp.zeros(6))
        self.assertEqual((boundary ** 2).rank(), 2)
        for m in (4, 5, 6):
            for sizes in partitions(6):
                if sizes[0] == m:
                    self.assertEqual((jordan(sizes) ** (m - 1)).rank(), 1)

    def test_actual_degree_two_boundary_and_full_velocity_rows(self):
        # Actual polynomial inverse: b=u+a^2/2, d=v+c^2/2.
        u, v, a, c = variables = sp.symbols("u v a c")
        b, d = sp.symbols("b d")
        physical = sp.Matrix([u + a ** 2 / 2, v + c ** 2 / 2, a, c])
        inverse = {u: b - a ** 2 / 2, v: d - c ** 2 / 2}
        self.assertEqual(physical.subs(inverse), sp.Matrix([b, d, a, c]))
        self.assertEqual(sp.expand((b - a ** 2 / 2).subs(b, physical[0])), u)
        self.assertEqual(sp.expand((d - c ** 2 / 2).subs(d, physical[1])), v)
        partials = [sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 0, 0]),
                    sp.Matrix([-a, 0, 1, 0]), sp.Matrix([0, -c, 0, 1])]
        for i, partial in enumerate(partials):
            self.assertEqual(sp.Matrix([act(partial, p, variables)
                                        for p in physical]), sp.eye(4)[:, i])
        f, g = u, u * v - 1
        field = sp.Matrix([0, 0, f, g])
        velocity = sp.Matrix([act(field, p, variables) for p in physical])
        jacobian = sp.Matrix(4, 4, lambda i, j:
                             act(partials[j], velocity[i], variables))
        first = [bracket(field, t, variables) for t in partials]
        second = [bracket(field, t, variables) for t in first]
        self.assertEqual(second[0], sp.zeros(4, 1))
        self.assertEqual(second[1], sp.zeros(4, 1))
        for t in second[2:]:
            self.assertEqual(bracket(field, t, variables), sp.zeros(4, 1))
        defects = sp.Matrix(4, 2, lambda i, j:
                            act(second[j + 2], physical[i], variables))
        selector = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1]])
        matrix = jacobian.row_join(-defects / 2).col_join(
            selector.row_join(sp.zeros(2)))
        layers = [physical, velocity]
        for _ in range(3):
            layers.append(sp.Matrix([act(field, p, variables)
                                     for p in layers[-1]]))
        self.assertEqual(layers[2], sp.Matrix([f ** 2, g ** 2, 0, 0]).applyfunc(sp.expand))
        self.assertEqual(layers[3], sp.zeros(4, 1))
        for j in (1, 2, 3):
            expected = layers[j].col_join((j - 1) * selector * layers[j - 1])
            actual = sp.factorial(j - 1) * matrix ** (j - 1) * velocity.col_join(sp.zeros(2, 1))
            self.assertEqual(clean(actual - expected), sp.zeros(6, 1))
            derivative = sp.Matrix(4, 4, lambda i, k:
                                   act(partials[k], layers[j][i], variables))
            self.assertEqual(clean((matrix ** j)[:4, :4] * sp.factorial(j)
                                   - derivative), sp.zeros(4))
        self.assertEqual(clean(matrix ** 3), sp.zeros(6))
        point = {u: 2, v: 3, a: 5, c: 7}
        self.assertEqual(defects.subs(point).rank(), 2)
        self.assertEqual(matrix.subs(point).rank(), 4)
        self.assertEqual((matrix.subs(point) ** 2).rank(), 2)
        self.assertEqual(act(field, v * a - c, variables), 1)

    def test_formal_rotation_identities_do_not_supply_a_nilpotent_companion(self):
        # The two old top identities alone permit rotation. This is NOT an action.
        a = sp.symbols("a")
        m = 3
        top = sp.Matrix([a, a ** 2, 0, 0])
        lower = sp.Matrix([1, a])
        defects = sp.Matrix([[0, 0], [0, 0], [1, 0], [0, 1]])
        selected = sp.Matrix.hstack(top[:2, :], top.diff(a)[:2, :])
        image = sp.Matrix.hstack((m - 1) * defects * lower / 2,
                                m * defects * lower.diff(a) / 2)
        jacobian = clean(image * selected.inv()).row_join(sp.zeros(4, 2))
        self.assertEqual(clean(jacobian * top - (m - 1) * defects * lower / 2),
                         sp.zeros(4, 1))
        self.assertEqual(clean(jacobian * top.diff(a) - m * defects * lower.diff(a) / 2),
                         sp.zeros(4, 1))
        rotation = sp.det(sp.Matrix.hstack(lower, lower.diff(a)))
        self.assertEqual(rotation, 1)
        for i, expected in [(0, m * (m - 1) * defects[:, 1] / 2),
                            (1, -m * (m - 1) * defects[:, 0] / 2)]:
            correction = (m - 1) * lower[i] * top.diff(a) - m * sp.diff(lower[i], a) * top
            self.assertEqual(clean(jacobian * correction - expected), sp.zeros(4, 1))
        selector = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1]])
        companion = jacobian.row_join(-defects / 2).col_join(
            selector.row_join(sp.zeros(2)))
        t = sp.symbols("t")
        self.assertNotEqual(sp.factor((sp.eye(6) - t * companion).det()), 1)

    def test_power_law_differentials_and_repeated_factor_orders(self):
        a, b = sp.symbols("a b")
        base = (a - 1) ** 2 * (b + 2) ** 3
        for m in (3, 4, 5):
            q = base ** m
            lower = [2 * base ** (m - 1), -3 * base ** (m - 1)]
            for value in lower:
                for variable in (a, b):
                    residual = m * q * sp.diff(value, variable)
                    residual -= (m - 1) * value * sp.diff(q, variable)
                    self.assertEqual(sp.factor(residual), 0)
                ratio = sp.cancel(value ** m / q ** (m - 1))
                self.assertFalse(ratio.free_symbols)
            for multiplicity in range(1, 5 * m + 1):
                needed = sp.Rational((m - 1) * multiplicity, m)
                self.assertEqual(needed.q == 1, multiplicity % m == 0)
            self.assertNotEqual(sp.Rational((m - 1) * (m + 1), m).q, 1)

    def test_rescaled_adjoint_formula_on_actual_polynomial_derivations(self):
        # This control tests rescaling only, not the rank-two frame premise.
        x, y, z, s = variables = sp.symbols("x y z s")
        g = x + 1
        delta = sp.Matrix([0, x, y, 1])
        field = g * delta
        self.assertEqual(act(field, g, variables), 0)
        for i in range(4):
            partial = sp.eye(4)[:, i]
            first = bracket(field, partial, variables)
            second = bracket(field, first, variables)
            third = bracket(field, second, variables)
            rescaled_second = bracket(delta, bracket(delta, partial, variables), variables)
            expected_second = second / g ** 2 + 2 * act(first, g, variables) * field / g ** 3
            self.assertEqual(clean(rescaled_second - expected_second), sp.zeros(4, 1))
            rescaled_third = bracket(delta, rescaled_second, variables)
            expected_third = third / g ** 3 + 3 * act(second, g, variables) * field / g ** 4
            self.assertEqual(clean(rescaled_third - expected_third), sp.zeros(4, 1))

        # Exact rank-update controls, not an asserted full-frame realization.
        alpha, beta, G, omega, theta = sp.symbols("alpha beta G omega theta")
        old_pair = sp.eye(4)[:, :2]
        charts = [
            (sp.Matrix([alpha, beta]),
             sp.Matrix([[omega, (-G / 2 - alpha * omega) / beta]])),
            (sp.Matrix([alpha, 0]), sp.Matrix([[-G / (2 * alpha), omega]])),
        ]
        for coefficients, row in charts:
            self.assertEqual(sp.cancel((row * coefficients)[0] + G / 2), 0)
            update = sp.eye(2) + 2 * coefficients * row / G
            self.assertEqual(clean(update ** 2 - update), sp.zeros(2))
            self.assertEqual(sp.cancel(sp.trace(update)), 1)
            self.assertEqual(sp.cancel(update.det()), 0)
            self.assertEqual(clean(update * coefficients), sp.zeros(2, 1))
            new_pair = clean(old_pair * update / G ** 2)
            self.assertEqual(new_pair.rank(), 1)
            field_column = old_pair * coefficients
            self.assertEqual(field_column.row_join(new_pair).rank(), 2)
        independent_pair = sp.eye(4)[:, 1:3]
        independent_field = sp.eye(4)[:, 0]
        new_independent = independent_pair / G ** 2
        new_independent += 2 * independent_field * sp.Matrix([[omega, theta]]) / G ** 3
        self.assertEqual(sp.cancel(new_independent[1:3, :].det()), G ** -4)
        self.assertEqual(independent_field.row_join(new_independent).rank(), 3)


if __name__ == "__main__":
    unittest.main()
