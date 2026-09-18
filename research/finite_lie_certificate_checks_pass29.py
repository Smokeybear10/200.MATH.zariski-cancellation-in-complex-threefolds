"""Exact finite certificates for the premises of the pass-29 Lie criterion.

This verifies polynomial identities in a declared free four-variable ring.
The cancellation consequence depends on the separately written, cited proof.
No universal existence, novelty, human review or formal proof is certified.
Only unittest and SymPy are imported; no solver or earlier checker is used.
"""

import unittest

import sympy as sp


def checked_polynomial(expression, coordinates):
    if isinstance(expression, bool) or not isinstance(expression, (int, sp.Expr)):
        raise ValueError("Expected an exact polynomial, not text or executable input")
    expression = sp.sympify(expression)
    if (expression.is_commutative is not True or expression.atoms(sp.Float)
            or not expression.free_symbols.issubset(coordinates)):
        raise ValueError("Inexact coefficient or undeclared variable")
    try:
        return sp.Poly(expression, *coordinates, domain=sp.QQ).as_expr()
    except (sp.PolynomialError, sp.CoercionFailed) as error:
        raise ValueError("Expected a rational-coefficient polynomial") from error


def rational_row(row, width):
    if not isinstance(row, (tuple, list)) or len(row) != width:
        raise ValueError("Incorrect constant coefficient row length")
    result = []
    for value in row:
        if isinstance(value, bool) or not isinstance(value, (int, sp.Expr)):
            raise ValueError("Coefficient must be an exact rational constant")
        value = sp.sympify(value)
        if value.is_Rational is not True:
            raise ValueError("Coefficient must be an exact rational constant")
        result.append(value)
    return tuple(result)


def evaluate(field, expression, coordinates):
    return sp.expand(sum(value*sp.diff(expression, variable)
                         for value, variable in zip(field, coordinates)))


def bracket(left, right, coordinates):
    return tuple(evaluate(left, value, coordinates)
                 -evaluate(right, other, coordinates)
                 for value, other in zip(right, left))


def combination(row, fields):
    return tuple(sp.expand(sum(c*f[index] for c, f in zip(row, fields)))
                 for index in range(4))


def verify_certificate(coordinates, delta, fields, generators, table,
                       slice_polynomial, nilpotence_orders):
    """Return checked premises, or reject this candidate with ValueError.

    The fields need only span a finite bracket-closed space, not be LNDs or
    linearly independent. All scalars in their relations are rational constants.
    A rejection is not proof that no other certificate exists.
    """
    if (not isinstance(coordinates, tuple) or len(coordinates) != 4
            or not all(isinstance(v, sp.Symbol) and v.is_commutative is True
                       for v in coordinates)
            or len(set(coordinates)) != 4):
        raise ValueError("Declare exactly four distinct polynomial variables")
    if not isinstance(fields, (tuple, list)) or not 1 <= len(fields) <= 64:
        raise ValueError("Supply a bounded nonempty finite spanning list")

    def vector(values):
        if not isinstance(values, (tuple, list)) or len(values) != 4:
            raise ValueError("A vector field must have four coefficients")
        return tuple(checked_polynomial(v, coordinates) for v in values)

    delta = vector(delta)
    fields = tuple(vector(f) for f in fields)
    width = len(fields)
    if not isinstance(generators, (tuple, list)) or len(generators) != 5:
        raise ValueError("Require delta and all four coordinate translations")
    generators = tuple(rational_row(row, width) for row in generators)
    units = tuple(tuple(sp.Integer(i == j) for j in range(4)) for i in range(4))
    for target, row in zip((delta,)+units, generators):
        if any(sp.expand(a-b) != 0 for a, b in zip(target, combination(row, fields))):
            raise ValueError("A required generator is not represented")

    expected_pairs = {(i, j) for i in range(width) for j in range(i+1, width)}
    if (not isinstance(table, dict)
            or not all(isinstance(pair, tuple) and len(pair) == 2
                       and all(type(index) is int for index in pair)
                       for pair in table)
            or set(table) != expected_pairs):
        raise ValueError("Require every unordered pair in the bracket table")
    for (i, j), row in table.items():
        row = rational_row(row, width)
        actual = bracket(fields[i], fields[j], coordinates)
        if any(sp.expand(a-b) != 0 for a, b in zip(actual, combination(row, fields))):
            raise ValueError("Invalid bracket-closure identity")

    if not isinstance(nilpotence_orders, (tuple, list)) or len(nilpotence_orders) != 4:
        raise ValueError("Require one local-nilpotence bound per coordinate")
    for variable, order in zip(coordinates, nilpotence_orders):
        if type(order) is not int or not 1 <= order <= 128:
            raise ValueError("Nilpotence bounds must be bounded positive integers")
        iterate = variable
        for _ in range(order):
            iterate = evaluate(delta, iterate, coordinates)
        if iterate != 0:
            raise ValueError("A declared generator nilpotence identity fails")

    slice_polynomial = checked_polynomial(slice_polynomial, coordinates)
    if evaluate(delta, slice_polynomial, coordinates) != 1:
        raise ValueError("The proposed polynomial is not a slice")
    return {
        "premise_identities_verified": True,
        "ambient_dimension": 4,
        "finite_closure_dimension_upper_bound": width,
        "delta_local_nilpotence_verified": True,
        "polynomial_slice_verified": True,
        "recognition_consequence": "kernel is C^[3], conditional on the cited pass-29 theorem",
        "universal_cancellation_verified": False,
        "proof_assistant_verified": False,
    }


def nonsolvable_fixture():
    """Explicit data from the independently known nonlinear coordinate inverse."""
    x, y, z, w = sp.symbols("x y z w")
    u = x+y**2
    fields = (
        (1, 0, 0, 0), (-2*y, 1, 0, 0),
        (-2*y*u, u, 0, 0), (y, 0, 0, 0),
        (x+3*y**2, -y, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
    )
    def row(*entries):
        values = [0]*7
        for index, coefficient in entries:
            values[index] = coefficient
        return tuple(values)
    table = {(i, j): row() for i in range(7) for j in range(i+1, 7)}
    table.update({
        (0, 2): row((1, 1)), (0, 4): row((0, 1)),
        (1, 3): row((0, 1)), (1, 4): row((1, -1)),
        (2, 3): row((4, 1)), (2, 4): row((2, -2)),
        (3, 4): row((3, 2)),
    })
    return {
        "coordinates": (x, y, z, w),
        "delta": (1+4*y*u, -2*u, 0, 0), "fields": fields,
        "generators": (row((0, 1), (2, -2)), row((0, 1)),
                       row((1, 1), (3, 2)), row((5, 1)), row((6, 1))),
        "table": table, "slice_polynomial": u, "nilpotence_orders": (5, 3, 1, 1),
    }


class FiniteLieCertificateChecks(unittest.TestCase):
    def test_complete_nonsolvable_certificate(self):
        result = verify_certificate(**nonsolvable_fixture())
        self.assertTrue(result["premise_identities_verified"])
        self.assertEqual(result["finite_closure_dimension_upper_bound"], 7)
        self.assertFalse(result["universal_cancellation_verified"])
        self.assertFalse(result["proof_assistant_verified"])

    def test_independent_abelian_translation_certificate(self):
        variables = sp.symbols("a b c d")
        fields = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
        result = verify_certificate(
            variables, fields[0], fields, (fields[0],)+fields,
            {(i, j): (0, 0, 0, 0) for i in range(4) for j in range(i+1, 4)},
            variables[0], (2, 1, 1, 1))
        self.assertTrue(result["polynomial_slice_verified"])

    def test_missing_or_wrong_translation_rejected(self):
        fixture = nonsolvable_fixture()
        fixture["generators"] = fixture["generators"][:-1]
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)
        fixture = nonsolvable_fixture()
        fixture["generators"] = fixture["generators"][:2]+((0,)*7,)+fixture["generators"][3:]
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)

    def test_polynomial_instead_of_constant_relation_rejected(self):
        fixture = nonsolvable_fixture()
        fixture["table"][(0, 2)] = (0, fixture["coordinates"][0], 0, 0, 0, 0, 0)
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)

    def test_incomplete_and_false_bracket_tables_rejected(self):
        fixture = nonsolvable_fixture()
        del fixture["table"][(0, 1)]
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)
        for converted in (lambda index: float(index), lambda index: bool(index)):
            fixture = nonsolvable_fixture()
            fixture["table"] = {tuple(converted(index) for index in pair): row
                                for pair, row in fixture["table"].items()}
            with self.assertRaises(ValueError):
                verify_certificate(**fixture)
        fixture = nonsolvable_fixture()
        fixture["table"][(2, 3)] = (0,)*7
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)

    def test_inadequate_nilpotence_bounds_rejected(self):
        fixture = nonsolvable_fixture()
        fixture["nilpotence_orders"] = (4, 3, 1, 1)
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)
        for orders in ((0, 3, 1, 1), (True, 3, 1, 1), (129, 3, 1, 1)):
            fixture["nilpotence_orders"] = orders
            with self.assertRaises(ValueError):
                verify_certificate(**fixture)

    def test_wrong_slice_rejected(self):
        fixture = nonsolvable_fixture()
        fixture["slice_polynomial"] = fixture["coordinates"][0]
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)

    def test_slice_with_finite_closure_but_nonlnd_rejected(self):
        x, y, z, w = sp.symbols("x y z w")
        fields = ((1, y, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0),
                  (0, 0, 1, 0), (0, 0, 0, 1))
        rows = tuple(tuple(int(i == j) for j in range(5)) for i in range(5))
        table = {(i, j): (0,)*5 for i in range(5) for j in range(i+1, 5)}
        table[(0, 2)] = (0, 0, -1, 0, 0)
        self.assertEqual(evaluate(fields[0], x, (x, y, z, w)), 1)
        with self.assertRaisesRegex(ValueError, "nilpotence"):
            verify_certificate((x, y, z, w), fields[0], fields, rows, table,
                               x, (2, 8, 1, 1))

    def test_malformed_inexact_and_nonpolynomial_data_rejected(self):
        fixture = nonsolvable_fixture()
        coords = fixture["coordinates"]
        for expression in (sp.Float("0.1")*coords[0], 1/coords[0],
                           sp.Symbol("undeclared"), "__import__('os')", True,
                           sp.Eq(coords[0], 0), sp.Eq(1, 0, evaluate=False),
                           sp.Symbol("noncommutative", commutative=False)):
            with self.assertRaises(ValueError):
                checked_polynomial(expression, coords)
        fixture["coordinates"] = (coords[0], coords[0], coords[2], coords[3])
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)
        fixture = nonsolvable_fixture()
        fixture["delta"] = fixture["delta"][:3]
        with self.assertRaises(ValueError):
            verify_certificate(**fixture)

    def test_spanning_fields_need_not_all_be_lnds(self):
        fixture = nonsolvable_fixture()
        x, y, z, w = fixture["coordinates"]
        semisimple = fixture["fields"][4]
        current = y
        for order in range(1, 7):
            current = evaluate(semisimple, current, fixture["coordinates"])
            self.assertEqual(current, (-1)**order*y)
        self.assertTrue(verify_certificate(**fixture)["premise_identities_verified"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
