"""Finite exact pass78 controls, not universal action or local-ring proofs.

The Euler method is a formal fraction-field matrix calculation. The conic
method is an actual retained nice sliced action with an explicit inverse.
The pole/socle method is weaker polynomial-plane data, not a full frame.
The final method tests three specified homogeneous binary triples only.
"""

import unittest

import sympy as sp


def derive(column, variables, expression):
    return sp.expand(sum(column[i] * sp.diff(expression, variable)
                         for i, variable in enumerate(variables)))


class NiceBinaryRamificationChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = expression if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(entry), 0)

    def assert_inverse(self, source, forward, target, inverse):
        for variable, expression in zip(source, inverse):
            self.assert_zero(expression.subs(dict(zip(target, forward)), simultaneous=True)
                             - variable)
        for variable, expression in zip(target, forward):
            self.assert_zero(expression.subs(dict(zip(source, inverse)), simultaneous=True)
                             - variable)

    def test_formal_two_by_two_euler_matrix(self):
        p, q, a, b, gamma = sp.symbols("p q a b gamma")
        radial = sp.Matrix([p, q])
        tau = sp.Matrix([a, b])
        row = sp.Matrix([[b, -a]])
        omega = p * b - q * a
        matrix = -gamma / omega * tau * row
        self.assert_zero(matrix ** 2)
        self.assert_zero(matrix * tau)
        self.assert_zero(matrix * radial + gamma * tau)
        self.assert_zero(sp.trace(matrix))
        self.assert_zero(matrix.det())
        self.assertNotEqual(sp.cancel(matrix[0, 0]), 0)
        basis = sp.Matrix.hstack(radial, tau)
        self.assert_zero(basis.det() - omega)
        normal = sp.Matrix([[0, 0], [-gamma, 0]])
        self.assert_zero(basis.inv() * matrix * basis - normal)
        self.assert_zero(row * matrix)
        # The opposite sign fails the specified radial identity.
        self.assertNotEqual(sp.cancel((-matrix * radial + gamma * tau)[0]), 0)
        # No entries here are asserted to be an actual velocity Jacobian.

    def test_actual_conic_wronskian_and_nonparallel_second_iterate(self):
        x, y, z, w = source = sp.symbols("x y z w")
        xx, aa, u, v = target = sp.symbols("xx aa u v")
        parameter = x * z - y ** 2 + w
        field = sp.Matrix([1, parameter, parameter ** 2,
                           -parameter ** 2 * x + 2 * parameter * y - z])
        partial_w = sp.Matrix([0, 0, 0, 1])
        forward = sp.Matrix([x, parameter, y - x * parameter, z - x * parameter ** 2])
        inverse = sp.Matrix([xx, u + xx * aa, v + xx * aa ** 2,
                             aa - xx * v + u ** 2 + 2 * xx * aa * u])
        self.assert_inverse(source, forward, target, inverse)
        self.assert_zero(sp.Matrix([derive(field, source, f) for f in forward])
                         - sp.Matrix([1, 0, 0, 0]))
        self.assert_zero(sp.Matrix([derive(field, source, f) for f in field]))

        derived = field.diff(w)
        next_bracket = derived.diff(w)
        second_iterate = sp.Matrix([derive(derived, source, f) for f in derived])
        self.assert_zero(second_iterate - sp.Matrix([0, 0, 0, 2]))
        self.assert_zero(derived.jacobian(source) * field - field.jacobian(source) * derived)
        jacobian = field.jacobian(source)
        self.assert_zero(jacobian ** 3)
        self.assert_zero(jacobian * derived)
        self.assert_zero(jacobian * next_bracket + second_iterate)
        full_columns = sp.Matrix.hstack(field, partial_w, derived, next_bracket)
        self.assert_zero(full_columns.det() - 2)
        transverse = sp.Matrix.hstack(field[:3, :], derived[:3, :], next_bracket[:3, :])
        self.assert_zero(full_columns.det() - transverse.det())
        t = sp.symbols("t")
        curve = sp.Matrix([1, t, t ** 2])
        self.assertEqual(sp.Matrix.hstack(curve, curve.diff(t), curve.diff(t, 2)).det(), 2)
        # A nonzero two-row minor disproves parallelism for this actual example.
        pair = sp.Matrix.hstack(derived, second_iterate)
        self.assert_zero(pair.extract([1, 3], [0, 1]).det() - 2)
        self.assert_zero(sp.Matrix([derive(derived, source, f) for f in second_iterate]))
        # Its vanishing third iterate is a property of this example only.
        p, q = sp.symbols("p q")
        binary = sp.Matrix([p ** 2, p * q, q ** 2])
        normal = binary.diff(p).cross(binary.diff(q))
        actual_normal = normal.subs({p: 1, q: parameter}, simultaneous=True)
        normal_invariant = sum(actual_normal[i] * source[i] for i in range(3))
        self.assert_zero(normal_invariant + 2 * field[3])
        self.assert_zero(derive(field, source, normal_invariant))
        self.assert_zero(derive(derived, source, normal_invariant))

    def test_ramified_plane_derivatives_genuine_pole_and_socle(self):
        u, v = variables = sp.symbols("u v")
        p, q, fourth = u, v ** 2 + u * v, 1 + v
        parameter_jacobian = sp.Matrix([p, q]).jacobian(variables)
        delta = parameter_jacobian.det()
        self.assert_zero(delta - u - 2 * v)
        inverse_jacobian = parameter_jacobian.inv()

        def partial_p(f):
            return sp.cancel(inverse_jacobian[0, 0] * sp.diff(f, u)
                             + inverse_jacobian[1, 0] * sp.diff(f, v))

        def partial_q(f):
            return sp.cancel(inverse_jacobian[0, 1] * sp.diff(f, u)
                             + inverse_jacobian[1, 1] * sp.diff(f, v))

        self.assert_zero(partial_p(p) - 1)
        self.assert_zero(partial_p(q))
        self.assert_zero(partial_q(p))
        self.assert_zero(partial_q(q) - 1)
        for f in variables:
            self.assert_zero(partial_p(partial_q(f)) - partial_q(partial_p(f)))
        self.assert_zero(partial_p(fourth) + v / delta)
        self.assert_zero(partial_q(fourth) - 1 / delta)
        self.assert_zero(v ** 2 + p * v - q)
        # This verifies the chain rule on weaker plane data, not a four-variable action.
        outputs = sp.Matrix([p ** 2, p * q, q ** 2, fourth])
        algebraic_partials = sp.Matrix([[partial_p(f), partial_q(f)] for f in outputs])
        self.assert_zero(algebraic_partials * parameter_jacobian - outputs.jacobian(variables))

        ideal = sp.groebner([p, q], u, v)

        def residue(f):
            return ideal.reduce(sp.expand(f))[1]

        self.assert_zero(residue(u))
        self.assert_zero(residue(v ** 2))
        self.assertEqual(residue(v), v)
        self.assert_zero(residue(fourth * (1 - v) - 1))
        self.assert_zero(residue(delta) - 2 * v)
        for degree in (2, 3):
            gamma = degree * fourth - p * partial_p(fourth) - q * partial_q(fourth)
            numerator = degree * fourth * delta - v ** 2
            self.assert_zero(gamma - numerator / delta)
            self.assert_zero(numerator.subs(u, -2 * v) + v ** 2)
            self.assertNotEqual(sp.expand(numerator.subs(u, -2 * v)), 0)
            self.assert_zero(residue(numerator) - 2 * degree * v)
            self.assertNotEqual(residue(numerator), 0)
            self.assert_zero(residue(u * numerator))
            self.assert_zero(residue(v * numerator))
            # Multiplication on basis (1,v) has image/socle Cv and kernel Cv.
            images = [sp.Poly(residue(numerator * basis), v) for basis in (1, v)]
            multiplication = sp.Matrix([[image.coeff_monomial(basis) for image in images]
                                        for basis in (1, v)])
            self.assert_zero(multiplication - sp.Matrix([[0, 0], [2 * degree, 0]]))
            self.assertEqual(multiplication.rank(), 1)
            self.assertEqual(multiplication.nullspace(), [sp.Matrix([0, 1])])
        # These finite identities do not prove the general Jacobian-socle theorem.

    def test_binary_minor_independence_and_cauchy_binet(self):
        p, q = sp.symbols("p q")
        triples = ((p ** 2, p * q, q ** 2),
                   (p ** 3, p ** 2 * q + p * q ** 2, q ** 3),
                   (p ** 4 + q ** 4, p ** 3 * q, q ** 4))
        rows = sp.Matrix(2, 3, sp.symbols("a0:6"))
        pairs = ((0, 1), (0, 2), (1, 2))
        alpha = sp.Matrix(sp.symbols("alpha0:3"))
        beta = sp.Matrix(sp.symbols("beta0:3"))
        epsilon = sp.symbols("epsilon")
        for forms in triples:
            degree = sp.Poly(forms[0], p, q).total_degree()
            with self.subTest(degree=degree):
                binary_jacobian = sp.Matrix(forms).jacobian((p, q))
                minors = [binary_jacobian.extract(list(pair), [0, 1]).det() for pair in pairs]
                normal = binary_jacobian[:, 0].cross(binary_jacobian[:, 1])
                self.assert_zero(normal - sp.Matrix([minors[2], -minors[1], minors[0]]))
                coefficient_matrix = sp.Matrix([
                    [sp.Poly(f, p, q).coeff_monomial(p ** j * q ** (2 * degree - 2 - j))
                     for f in minors] for j in range(2 * degree - 1)])
                self.assertEqual(coefficient_matrix.rank(), 3)
                pivot_rows = coefficient_matrix.T.rref()[1]
                unit_minor = coefficient_matrix.extract(list(pivot_rows), [0, 1, 2])
                self.assertNotEqual(unit_minor.det(), 0)
                self.assert_zero(unit_minor.inv() * unit_minor * (alpha + epsilon * beta)
                                 - alpha - epsilon * beta)
                # Extract degree 2e-2 over C[epsilon]/(epsilon²), retaining nilpotents.
                order = 2 * degree - 2
                formal_sum = (sum((alpha[i] + epsilon * beta[i]) * minors[i] for i in range(3))
                              + (1 + epsilon) * p ** (order + 1) + epsilon ** 2 * q ** order)
                formal_poly = sp.Poly(formal_sum, p, q)
                degree_coefficients = sp.Matrix([
                    sp.rem(formal_poly.coeff_monomial(p ** j * q ** (order - j)),
                           epsilon ** 2, epsilon) for j in range(order + 1)])
                self.assert_zero(degree_coefficients - coefficient_matrix * (alpha + epsilon * beta))
                selected = degree_coefficients.extract(list(pivot_rows), [0])
                self.assert_zero(unit_minor.inv() * selected - alpha - epsilon * beta)
                self.assert_zero(degree_coefficients.diff(epsilon) - coefficient_matrix * beta)
                cauchy_binet = sum(rows.extract([0, 1], list(pair)).det() * minors[i]
                                  for i, pair in enumerate(pairs))
                self.assert_zero((rows * binary_jacobian).det() - cauchy_binet)
        # Dependent forms need not have three independent Jacobian minors.
        dependent = sp.Matrix([p ** 2, p * q, p ** 2 + p * q]).jacobian((p, q))
        minors = [dependent.extract(list(pair), [0, 1]).det() for pair in pairs]
        self.assert_zero(minors[0] - minors[1])
        self.assert_zero(minors[0] + minors[2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
