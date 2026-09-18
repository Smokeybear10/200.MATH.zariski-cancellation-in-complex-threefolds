"""Exact classifier for vertical extensions of one Freudenburg derivation.

For a rational polynomial a(x,y,z), this module classifies whether

    Delta + a*d/dw

has a polynomial slice, using the working all-coefficient theorem proved in
``arbitrary-coefficients-pass.md``.  It does not classify arbitrary locally
nilpotent derivations on four-space and does not settle Zariski cancellation.

Positive answers contain a directly verified primitive and slice.  Negative
answers use the theorem that a slice exists exactly when
``a = c + Delta(H)`` with ``c != 0``; a failed finite image calculation is a
complete homogeneous linear-algebra decision, not a bounded slice ansatz.
If the optional work limit is exceeded, the result is ``unknown``.

Run with the repository's SymPy environment, for example:

    /opt/anaconda3/bin/python research/full_coefficient_classifier.py '1+2*f*r'
    /opt/anaconda3/bin/python research/full_coefficient_classifier.py --self-test
"""

from __future__ import annotations

import argparse
import ast
import json
from math import comb
import sys
import time
import unittest

import sympy as sp
from sympy.polys.matrices import DomainMatrix


x, y, z, w = sp.symbols("x y z w")
f = x*z-y**2
g = z*f**2+2*x**2*y*f+x**5
r = -x**3-f*y


def jacobian_derivation_image(value: sp.Expr) -> sp.Expr:
    """Return Jac(f,g,value), expanded over QQ[x,y,z]."""
    matrix = sp.Matrix([
        [sp.diff(f, variable) for variable in (x, y, z)],
        [sp.diff(g, variable) for variable in (x, y, z)],
        [sp.diff(value, variable) for variable in (x, y, z)],
    ])
    return sp.expand(matrix.det())


DELTA_IMAGES = tuple(jacobian_derivation_image(variable)
                     for variable in (x, y, z))


def delta(value: sp.Expr) -> sp.Expr:
    return sp.expand(sum(sp.diff(value, variable)*image
                         for variable, image in zip((x, y, z), DELTA_IMAGES)))


def exact_degree_exponents(degree: int) -> list[tuple[int, int, int]]:
    return [(i, j, degree-i-j)
            for i in range(degree+1)
            for j in range(degree-i+1)]


def monomial(exponents: tuple[int, int, int]) -> sp.Expr:
    return x**exponents[0]*y**exponents[1]*z**exponents[2]


def homogeneous_parts(value: sp.Expr) -> dict[int, sp.Expr]:
    parts: dict[int, sp.Expr] = {}
    for exponents, coefficient in sp.Poly(value, x, y, z, domain=sp.QQ).terms():
        degree = sum(exponents)
        parts[degree] = parts.get(degree, sp.Integer(0)) + coefficient*monomial(exponents)
    return {degree: sp.expand(part) for degree, part in parts.items() if part != 0}


def solve_homogeneous_image(target: sp.Expr, output_degree: int) -> dict:
    """Decide target in Delta(R[output_degree-4]) and return one preimage."""
    input_degree = output_degree-4
    inputs = exact_degree_exponents(input_degree)
    outputs = exact_degree_exponents(output_degree)
    row_id = {powers: index for index, powers in enumerate(outputs)}
    rows: dict[int, dict[int, object]] = {}

    for column, powers in enumerate(inputs):
        image = sp.Poly(delta(monomial(powers)), x, y, z, domain=sp.QQ)
        for out_powers, coefficient in image.terms():
            if coefficient:
                rows.setdefault(row_id[out_powers], {})[column] = sp.QQ.convert(coefficient)

    rhs_column = len(inputs)
    for powers, coefficient in sp.Poly(target, x, y, z, domain=sp.QQ).terms():
        if coefficient:
            rows.setdefault(row_id[powers], {})[rhs_column] = sp.QQ.convert(coefficient)

    matrix = DomainMatrix(rows, (len(outputs), len(inputs)+1), sp.QQ)
    reduced, pivots = matrix.rref()
    stats = {
        "output_degree": output_degree,
        "input_degree": input_degree,
        "unknowns": len(inputs),
        "equations": len(outputs),
        "dense_cell_estimate": len(inputs)*len(outputs),
        "augmented_rank": len(pivots),
    }
    if rhs_column in pivots:
        stats["in_image"] = False
        return {"in_image": False, "stats": stats}

    # Set every free variable to zero.  In RREF, row i has pivot pivots[i].
    data = reduced.to_dod()
    coefficients = [sp.Rational(0) for _ in inputs]
    for row, pivot in enumerate(pivots):
        if pivot < rhs_column:
            coefficients[pivot] = sp.Rational(data.get(row, {}).get(rhs_column, 0))
    primitive = sp.expand(sum(coefficient*monomial(powers)
                              for coefficient, powers in zip(coefficients, inputs)))
    if sp.expand(delta(primitive)-target) != 0:
        raise AssertionError("RREF preimage failed direct Delta verification")
    stats["in_image"] = True
    return {"in_image": True, "primitive": primitive, "stats": stats}


def parse_coefficient(source: str) -> sp.Expr:
    """Parse arithmetic without evaluating calls, attributes, or arbitrary code."""
    names = {
        "x": x, "y": y, "z": z,
        "f": f, "g": g, "r": r,
        "X": x, "Y": y, "Z": z,
        "F": f, "G": g, "R": r,
    }

    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return sp.Integer(node.value)
        if isinstance(node, ast.Name) and node.id in names:
            return names[node.id]
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = visit(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp):
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Add):
                return left+right
            if isinstance(node.op, ast.Sub):
                return left-right
            if isinstance(node.op, ast.Mult):
                return left*right
            if isinstance(node.op, ast.Div):
                if right == 0:
                    raise ValueError("Division by zero is not allowed")
                return left/right
            if (isinstance(node.op, ast.Pow)
                    and isinstance(right, sp.Integer) and right >= 0):
                return left**right
        raise ValueError(
            "Use rational arithmetic, x/y/z or f/g/r, and nonnegative integer powers")

    try:
        result = visit(ast.parse(source, mode="eval").body)
    except SyntaxError as error:
        raise ValueError("Invalid coefficient expression") from error
    return checked_coefficient(result)


def checked_coefficient(value: sp.Expr | str) -> sp.Expr:
    if isinstance(value, str):
        return parse_coefficient(value)
    value = sp.sympify(value)
    if value.has(sp.Float) or value.free_symbols - {x, y, z}:
        raise ValueError("coefficient must use only x,y,z (or the aliases f,g,r)")
    try:
        return sp.Poly(value, x, y, z, domain=sp.QQ).as_expr()
    except (sp.PolynomialError, sp.polys.polyerrors.CoercionFailed) as error:
        raise ValueError("coefficient must lie in QQ[x,y,z]") from error


def classify(coefficient: sp.Expr | str, work_limit: int | None = 2_000_000) -> dict:
    """Return an exact theorem-backed classification or an explicit unknown."""
    started = time.monotonic()
    a = checked_coefficient(coefficient)
    result = {
        "coefficient": str(a),
        "scope": "vertical extension of the fixed Freudenburg Delta on QQ[x,y,z]",
        "theorem_dependency": (
            "working all-coefficient theorem in research/arbitrary-coefficients-pass.md; "
            "internally audited, external priority/review pending"),
        "general_zariski_cancellation_solved": False,
    }

    fixed_line = sp.expand(a.subs({x: 0, y: 0}))
    result["fixed_line_restriction"] = str(fixed_line)
    if z in fixed_line.free_symbols:
        result.update({
            "status": "does_not_exist",
            "decision": "fixed_point",
            "reason": (
                "Over an algebraic closure the nonconstant fixed-line restriction "
                "has a zero, at which the full derivation vanishes."),
            "elapsed_seconds": round(time.monotonic()-started, 6),
        })
        return result

    c = sp.Rational(fixed_line)
    result["constant_c"] = str(c)
    if c == 0:
        result.update({
            "status": "does_not_exist",
            "decision": "fixed_point",
            "reason": "The full derivation vanishes on the fixed line x=y=0.",
            "elapsed_seconds": round(time.monotonic()-started, 6),
        })
        return result

    target = sp.expand(a-c)
    parts = homogeneous_parts(target)
    required_work = sum(
        comb(degree+2, 2)*comb(degree-2, 2)
        for degree in parts if degree >= 4)
    result["dense_cell_estimate"] = required_work
    result["work_limit"] = work_limit
    if work_limit is not None and required_work > work_limit:
        result.update({
            "status": "unknown",
            "decision": "work_limit",
            "reason": (
                "The complete homogeneous image calculation was not run; "
                "no negative conclusion is inferred from the work limit."),
            "elapsed_seconds": round(time.monotonic()-started, 6),
        })
        return result

    component_stats = []
    primitive = sp.Integer(0)
    for degree in sorted(parts):
        if degree < 4:
            result.update({
                "status": "does_not_exist",
                "decision": "exact_homogeneous_image",
                "failed_output_degree": degree,
                "reason": (
                    "Delta raises ordinary homogeneous degree by four, so this "
                    "nonzero component cannot be in Delta(QQ[x,y,z])."),
                "component_stats": component_stats,
                "elapsed_seconds": round(time.monotonic()-started, 6),
            })
            return result
        solved = solve_homogeneous_image(parts[degree], degree)
        component_stats.append(solved["stats"])
        if not solved["in_image"]:
            result.update({
                "status": "does_not_exist",
                "decision": "exact_homogeneous_image",
                "failed_output_degree": degree,
                "reason": (
                    "The displayed homogeneous component is outside the exact "
                    "finite-dimensional image of Delta.  The working theorem then "
                    "excludes every polynomial slice degree."),
                "component_stats": component_stats,
                "elapsed_seconds": round(time.monotonic()-started, 6),
            })
            return result
        primitive += solved["primitive"]

    primitive = sp.expand(primitive)
    residual = sp.expand(delta(primitive)-target)
    if residual != 0:
        raise AssertionError("assembled primitive failed direct verification")
    slice_polynomial = sp.expand((w-primitive)/c)
    slice_residual = sp.expand(
        sum(sp.diff(slice_polynomial, variable)*image
            for variable, image in zip((x, y, z), DELTA_IMAGES))
        + a*sp.diff(slice_polynomial, w)-1)
    if slice_residual != 0:
        raise AssertionError("constructed slice failed direct verification")

    result.update({
        "status": "exists",
        "decision": "exact_primitive",
        "primitive_H": str(primitive),
        "slice": str(slice_polynomial),
        "primitive_verification_residual": str(residual),
        "slice_verification_residual": str(slice_residual),
        "component_stats": component_stats,
        "elapsed_seconds": round(time.monotonic()-started, 6),
    })
    return result


class ClassifierTests(unittest.TestCase):
    def assert_status(self, coefficient, status, **kwargs):
        answer = classify(coefficient, **kwargs)
        self.assertEqual(answer["status"], status, answer)
        return answer

    def test_constant_slice(self):
        answer = self.assert_status(sp.Integer(1), "exists")
        self.assertEqual(sp.sympify(answer["slice"], locals={"w": w}), w)

    def test_zero_and_negative_constants(self):
        self.assert_status(sp.Integer(0), "does_not_exist")
        answer = self.assert_status(sp.Integer(-2), "exists")
        self.assertEqual(sp.sympify(answer["slice"], locals={"w": w}), -w/2)

    def test_all_generator_images_and_product(self):
        for primitive in (x, y, z, x*y):
            answer = self.assert_status(1+delta(primitive), "exists")
            self.assertEqual(sp.expand(delta(sp.sympify(
                answer["primitive_H"], locals={"x": x, "y": y, "z": z}))
                -delta(primitive)), 0)

    def test_every_monomial_through_degree_four_is_nonslice(self):
        # Delta raises homogeneous degree by four and kills degree-zero inputs.
        # Monomials supported only on z are independently caught by fixed points.
        for degree in range(1, 5):
            for powers in exact_degree_exponents(degree):
                self.assert_status(1+monomial(powers), "does_not_exist")

    def test_requested_negative_examples(self):
        S = x*x*y+f*z
        for coefficient in (1+S, 1+y, 1+f, 1+3*g*x-2*f**3):
            self.assert_status(coefficient, "does_not_exist")

    def test_fixed_line_obstruction(self):
        answer = self.assert_status(1+z, "does_not_exist")
        self.assertEqual(answer["decision"], "fixed_point")

    def test_work_limit_is_unknown(self):
        answer = self.assert_status(1+delta(x**5), "unknown", work_limit=1)
        self.assertEqual(answer["decision"], "work_limit")

    def test_parser_aliases_and_direct_verification(self):
        answer = self.assert_status("1+2*f*r", "exists")
        self.assertEqual(answer["slice_verification_residual"], "0")

    def test_parser_rejects_unsafe_and_nonpolynomial_input(self):
        for source in (
                "__import__('os').system('true')", "sin(x)", "u+x",
                "1/x", "x**-1", "0.5+x"):
            with self.subTest(source=source):
                with self.assertRaises(ValueError):
                    parse_coefficient(source)


def main() -> int:
    parser = argparse.ArgumentParser(description=(
        "Classify Delta+a*d/dw for the fixed Freudenburg Delta. Negative "
        "answers rely on the working all-coefficient theorem, not on a bounded "
        "slice search; this does not address arbitrary LNDs on affine four-space."))
    parser.add_argument("coefficient", nargs="?",
                        help="rational expression in x,y,z; aliases f,g,r are available")
    parser.add_argument("--work-limit", type=int, default=2_000_000,
                        help="maximum dense matrix-cell estimate; 0 means unlimited")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ClassifierTests)
        outcome = unittest.TextTestRunner(verbosity=2).run(suite)
        print(json.dumps({
            "tests_run": outcome.testsRun,
            "successful": outcome.wasSuccessful(),
            "sympy": sp.__version__,
            "scope": "exact classifier mechanics and theorem-backed examples",
            "formal_proof_assistant_verification": False,
            "novelty_established": False,
        }, indent=2))
        return 0 if outcome.wasSuccessful() else 1

    if args.coefficient is None:
        parser.error("provide a coefficient or use --self-test")
    if args.work_limit < 0:
        parser.error("--work-limit must be nonnegative")
    limit = None if args.work_limit == 0 else args.work_limit
    try:
        answer = classify(args.coefficient, work_limit=limit)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(answer, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
