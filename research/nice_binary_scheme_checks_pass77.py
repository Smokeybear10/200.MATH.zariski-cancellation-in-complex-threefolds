"""Finite exact pass77 controls, not a classification or proof certificate.

Only unittest and SymPy are imported. The first method uses actual nice
polynomial actions with both adapted inverse orders, including a genuinely
nonreduced transverse quotient. The binary and bare conormal methods test
selected algebraic data, not their realization by the unresolved full frame.
The graph method separates actual nice controls from a nonnice graph action.
"""

import unittest

import sympy as sp


def derive(column, variables, expression):
    return sp.expand(sum(column[i] * sp.diff(expression, variable)
                         for i, variable in enumerate(variables)))


def bracket(left, right, variables):
    return sp.Matrix([derive(left, variables, entry) for entry in right]) - sp.Matrix(
        [derive(right, variables, entry) for entry in left])


class NiceBinarySchemeChecks(unittest.TestCase):
    def assert_zero(self, expression):
        if isinstance(expression, sp.MatrixBase):
            for entry in expression:
                self.assertEqual(sp.expand(entry), 0)
        else:
            self.assertEqual(sp.expand(expression), 0)

    def assert_inverse(self, source, forward, target, inverse):
        to_source = dict(zip(target, forward))
        to_target = dict(zip(source, inverse))
        for variable, expression in zip(source, inverse):
            self.assert_zero(expression.subs(to_source, simultaneous=True) - variable)
        for variable, expression in zip(target, forward):
            self.assert_zero(expression.subs(to_target, simultaneous=True) - variable)

    def test_actual_scheme_jets_reduced_and_nonreduced(self):
        a, b, c, w = source = sp.symbols("a b c w")
        aa, u, v, ww = target = sp.symbols("aa u v ww")
        partial_w = sp.Matrix([0, 0, 0, 1])
        for power in (1, 2):
            with self.subTest(power=power):
                speed = a ** power
                last_speed = sp.Integer(1) if power == 1 else 1 + a
                bezout_r = sp.Integer(1) if power == 1 else 1 - a
                bezout_t = sp.Integer(0) if power == 1 else sp.Integer(1)
                self.assert_zero(bezout_r * last_speed + bezout_t * speed - 1)
                invariant_u = last_speed * b - speed * w
                supplied_slice = bezout_t * b + bezout_r * w
                field = sp.Matrix([0, speed, invariant_u, last_speed])
                forward = sp.Matrix([a, invariant_u, c - invariant_u * supplied_slice,
                                     supplied_slice])
                inverse = sp.Matrix([aa,
                                     bezout_r.subs(a, aa) * u + aa ** power * ww,
                                     v + u * ww,
                                     -bezout_t * u + last_speed.subs(a, aa) * ww])
                self.assert_inverse(source, forward, target, inverse)
                self.assert_zero(sp.Matrix([derive(field, source, f) for f in forward])
                                 - partial_w)
                self.assert_zero(sp.Matrix([derive(field, source, f) for f in field]))
                derived = bracket(partial_w, field, source)
                self.assert_zero(derived - sp.Matrix([0, 0, -speed, 0]))
                self.assert_zero(bracket(field, derived, source))
                self.assert_zero(sp.Matrix([derive(derived, source, f) for f in field]))

                # Exact transverse ideal equals (a^power,b), without taking radicals.
                transverse = sp.groebner([speed, invariant_u], *source)
                quotient = sp.groebner([speed, b], *source)
                for f in (speed, b):
                    self.assert_zero(transverse.reduce(f)[1])
                for f in field[:3]:
                    self.assert_zero(quotient.reduce(f)[1])

                def reduce_entry(f):
                    return quotient.reduce(sp.expand(f))[1]

                jacobian = field.jacobian(source)
                self.assert_zero(jacobian ** 3)
                self.assert_zero(jacobian.applyfunc(lambda f: derive(field, source, f))
                                 + jacobian ** 2)
                reduced_jacobian = jacobian.applyfunc(reduce_entry)
                initial = reduced_jacobian.subs(w, 0)
                self.assert_zero((reduced_jacobian - initial + w * bezout_r * initial ** 2)
                                 .applyfunc(reduce_entry))
                reduced_derived_jet = derived.jacobian(source).applyfunc(reduce_entry)
                self.assert_zero((reduced_derived_jet + bezout_r * initial ** 2)
                                 .applyfunc(reduce_entry))
                self.assert_zero((reduced_derived_jet ** 2).applyfunc(reduce_entry))
                for i in range(4):
                    for j in range(i + 1, 4):
                        for k in range(4):
                            for ell in range(k + 1, 4):
                                minor = reduced_derived_jet.extract([i, j], [k, ell]).det()
                                self.assert_zero(reduce_entry(minor))

                # Invariant quotient coordinate V reduces to the original c.
                self.assert_zero(reduce_entry(forward[2] - c))
                self.assert_zero(reduce_entry(supplied_slice - bezout_r * w))
                self.assert_zero(reduce_entry(derive(field, source, c ** 2 * w)
                                              - last_speed * c ** 2))
                self.assert_zero(derive(derived, source, c * speed) + speed ** 2)
                self.assert_zero(derive(derived, source, forward[2]) + speed)

                if power == 2:
                    self.assertNotEqual(reduce_entry(a), 0)
                    self.assert_zero(reduce_entry(a ** 2))
                    self.assertEqual(reduced_derived_jet[2, 0], -2 * a)
                    self.assertNotEqual(reduced_derived_jet[2, 0], 0)
                    self.assertEqual(reduced_jacobian[3, 0], 1)
                    self.assertNotEqual(reduce_entry(last_speed), 1)
                    self.assert_zero(reduce_entry(last_speed * bezout_r - 1))
                    # A nonconstant polynomial unit exists in this quotient.
                    self.assert_zero(reduce_entry((1 + a * w) * (1 - a * w) - 1))
                    self.assertNotEqual(reduce_entry(sp.diff(1 + a * w, w)), 0)

    def test_representative_binary_ideal_power_bounds(self):
        u, v = sp.symbols("u v")
        triples = ((u ** 2, u * v, v ** 2),
                   (u ** 3, u ** 2 * v + u * v ** 2, v ** 3),
                   (u ** 4 + v ** 4, u ** 3 * v, v ** 4))
        for forms in triples:
            degree = sp.Poly(forms[0], u, v).total_degree()
            with self.subTest(degree=degree):
                self.assertEqual(sp.gcd(sp.gcd(forms[0], forms[1]), forms[2]), 1)
                for form in forms:
                    self.assertTrue(all(sum(monomial) == degree
                                        for monomial in sp.Poly(form, u, v).monoms()))
                ideal = sp.groebner(forms, u, v)
                # These monomials generate (u,v)^(2e-1).
                for exponent in range(2 * degree):
                    monomial = u ** exponent * v ** (2 * degree - 1 - exponent)
                    self.assert_zero(ideal.reduce(monomial)[1])
                self.assertEqual(ideal.reduce(sp.Integer(1))[1], 1)

        # The common-factor boundary fails the asserted high-power inclusion.
        invalid = sp.groebner([u ** 3, u ** 2 * v, u * v ** 2], u, v)
        self.assertNotEqual(invalid.reduce(v ** 5)[1], 0)

    def test_bare_conormal_inverse_is_not_a_full_frame(self):
        x, y, z, w = source = sp.symbols("x y z w")
        p, q, zz, ww = target = sp.symbols("p q zz ww")
        forward = sp.Matrix([x, y + x ** 2 * w, z, w])
        inverse = sp.Matrix([p, q - p ** 2 * ww, zz, ww])
        self.assert_inverse(source, forward, target, inverse)
        self.assertEqual(forward.jacobian(source).det(), 1)
        self.assert_zero(sp.diff(forward[0], w))
        self.assert_zero(sp.diff(forward[1], w) - forward[0] ** 2)
        parameter_ideal = sp.groebner(forward[:2], *source)
        stationary_ideal = sp.groebner([x, y], *source)
        for f in (x, y):
            self.assert_zero(parameter_ideal.reduce(f)[1])
        for f in forward[:2]:
            self.assert_zero(stationary_ideal.reduce(f)[1])
        self.assertEqual(parameter_ideal.reduce(sp.Integer(1))[1], 1)
        square = sp.groebner([x ** 2, x * y, y ** 2], *source)
        self.assert_zero(square.reduce(sp.diff(forward[1], w))[1])

    def test_graph_hessian_and_higher_degree_square_zero(self):
        x, y, z, w = source = sp.symbols("x y z w")
        t = sp.symbols("t")
        graph = x * z - y ** 2
        parameter = w + graph
        conic = sp.Matrix([1, t, t ** 2])
        self.assert_zero((conic.T * sp.hessian(graph, (x, y, z)) * conic)[0])
        for curve_degree in (3, 4):
            higher = sp.Matrix([1, t, t ** curve_degree])
            obstruction = (higher.T * sp.hessian(graph, (x, y, z)) * higher)[0]
            self.assert_zero(obstruction - 2 * (t ** curve_degree - t ** 2))
            self.assertNotEqual(sp.expand(obstruction), 0)

        for curve_degree in (2, 3):
            # Both are actual polynomial graph actions and have Ex=1.
            # Only the degree-two member is nice in these original coordinates.
            speeds = sp.Matrix([1, parameter, parameter ** curve_degree])
            fourth = -sum(speeds[i] * sp.diff(graph, variable)
                          for i, variable in enumerate((x, y, z)))
            field = speeds.col_join(sp.Matrix([fourth]))
            self.assert_zero(derive(field, source, parameter))
            self.assert_zero(derive(field, source, fourth)
                             + 2 * (parameter ** curve_degree - parameter ** 2))
            self.assert_zero(bracket(field, field.diff(w), source))
            if curve_degree == 2:
                self.assert_zero(field.jacobian(source) ** 3)
                self.assertNotEqual(field.jacobian(source) ** 2, sp.zeros(4))

        xx, yy, zz, aa = target = sp.symbols("xx yy zz aa")
        graph_forward = sp.Matrix([x, y, z, parameter])
        graph_inverse = sp.Matrix([xx, yy, zz, aa - xx * zz + yy ** 2])
        self.assert_inverse(source, graph_forward, target, graph_inverse)
        for curve_degree in (3, 5):
            field = sp.Matrix([1, w, w ** curve_degree, 0])
            self.assert_zero(field.jacobian(source) ** 2)
            forward = sp.Matrix([x, y - w * x, z - w ** curve_degree * x, w])
            inverse = sp.Matrix([xx, yy + aa * xx, zz + aa ** curve_degree * xx, aa])
            self.assert_inverse(source, forward, target, inverse)
            self.assert_zero(sp.Matrix([derive(field, source, f) for f in forward])
                             - sp.Matrix([1, 0, 0, 0]))
            self.assert_zero(field[0] ** (curve_degree - 1) * field[2]
                             - field[1] ** curve_degree)

    def test_stationary_two_shear_omission_coefficients(self):
        x, y, z, w = source = sp.symbols("x y z w")
        p, q, zz, ww = target = sp.symbols("p q zz ww")
        cx, cy, cz, cw, fp, fq = sp.symbols("cx cy cz cw fp fq")
        direction = sp.Matrix([cx, cy, cz, cw])
        for degree in (2, 3):
            with self.subTest(degree=degree):
                first = x + y ** degree * (w + z ** 2)
                second = y + first ** degree * (w + z ** 3)
                forward = sp.Matrix([first, second, z, w])
                inverse_y = q - p ** degree * (ww + zz ** 3)
                inverse_x = p - inverse_y ** degree * (ww + zz ** 2)
                inverse = sp.Matrix([inverse_x, inverse_y, zz, ww])
                self.assert_inverse(source, forward, target, inverse)

                # These exact generator relations give (p,q)=(x,y).
                self.assert_zero(first - x - y ** degree * (w + z ** 2))
                self.assert_zero(second - y - first ** degree * (w + z ** 3))
                stationary_power = sp.groebner(
                    [x ** i * y ** (degree - i) for i in range(degree + 1)], *source)
                for expression in forward[:2]:
                    self.assert_zero(stationary_power.reduce(sp.diff(expression, w))[1])
                self.assert_zero(sp.diff(first, w) - y ** degree)
                self.assert_zero(sp.diff(second, w) - first ** degree
                                 - degree * first ** (degree - 1)
                                 * (w + z ** 3) * y ** degree)

                # Exact constant-direction chain rule, expressed in inverse coordinates.
                cp_original = (cx + degree * cy * y ** (degree - 1) * (w + z ** 2)
                               + y ** degree * (cw + 2 * z * cz))
                cq_original = (cy + degree * first ** (degree - 1)
                               * (w + z ** 3) * cp_original
                               + first ** degree * (cw + 3 * z ** 2 * cz))
                self.assert_zero(derive(direction, source, first) - cp_original)
                self.assert_zero(derive(direction, source, second) - cq_original)
                cp = (cx + degree * cy * inverse_y ** (degree - 1) * (ww + zz ** 2)
                      + inverse_y ** degree * (cw + 2 * zz * cz))
                cq = (cy + degree * p ** (degree - 1) * (ww + zz ** 3) * cp
                      + p ** degree * (cw + 3 * zz ** 2 * cz))
                leading = (-p ** degree) ** (degree - 1) * (
                    degree * cy - p ** degree * (cw + 2 * zz * cz))
                self.assert_zero(sp.Poly(cp, ww).coeff_monomial(ww ** degree) - leading)
                # fp,fq are formal coefficients independent of z,w, not a finite F search.
                combined = sp.Poly(fp * cp + fq * cq, ww)
                self.assert_zero(combined.coeff_monomial(ww ** (degree + 1))
                                 - degree * p ** (degree - 1) * fq * leading)
                reduced = sp.expand((fp * cp + fq * cq).subs({cy: 0, cz: 0, cw: 0}))
                self.assert_zero(sp.Poly(reduced, ww).coeff_monomial(ww)
                                 - degree * p ** (degree - 1) * fq * cx)
                self.assert_zero(cp.subs({cy: 0, cz: 0, cw: 0}) - cx)

                # Formal chain rule assuming Ep=Eq=0 and E²z=E²w=0.
                # Inert velocity symbols encode those assumptions, not an action realization.
                vz, vw = sp.symbols("vz vw")
                formal_field = sp.Matrix([0, 0, vz, vw])
                second_y = derive(formal_field, target,
                                  derive(formal_field, target, inverse_y))
                self.assert_zero(second_y + 6 * p ** degree * zz * vz ** 2)
                second_x = derive(formal_field, target,
                                  derive(formal_field, target, inverse_x)).subs(vz, 0)
                remaining_factor = ((degree - 1) * p ** degree * (ww + zz ** 2)
                                    - 2 * inverse_y)
                self.assert_zero(second_x + degree * p ** degree * inverse_y ** (degree - 2)
                                 * vw ** 2 * remaining_factor)
                self.assertEqual(sp.Poly(remaining_factor, q).coeff_monomial(q), -2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
