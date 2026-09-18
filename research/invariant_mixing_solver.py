#!/usr/bin/env python3
"""Generate exact certificates for one-variable invariant-row reduction.

Only the Python standard library is used. Polynomial coefficient arrays are
in ascending powers of the invariant parameter. The proof and conjugation
conventions are in extension-mixing-pass15.md, Sections 1 through 4.

Examples:
    python invariant_mixing_solver.py --a '["-1", "1"]' --b '["1", "1"]'
    python invariant_mixing_solver.py --batch '[{"a":[1],"b":[0,1]}]'

The output is one JSON value, including on invalid input. An error object has
exit status 2. Certificates use monic gcds, canonical rational strings, and
the zero polynomial ["0"]. No symbolic-computation package is imported.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
import json
import sys
from typing import Literal, Sequence


Polynomial = tuple[Fraction, ...]
ZERO: Polynomial = (Fraction(0),)


def _trim(coefficients: Sequence[Fraction]) -> Polynomial:
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result) if result else ZERO


def _zero(polynomial: Polynomial) -> bool:
    return polynomial == ZERO


def _scale(polynomial: Polynomial, scalar: Fraction) -> Polynomial:
    return _trim([scalar * coefficient for coefficient in polynomial])


def _subtract(left: Polynomial, right: Polynomial) -> Polynomial:
    length = max(len(left), len(right))
    return _trim([
        (left[index] if index < len(left) else Fraction(0))
        - (right[index] if index < len(right) else Fraction(0))
        for index in range(length)
    ])


def _multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    if _zero(left) or _zero(right):
        return ZERO
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            result[left_degree + right_degree] += (
                left_coefficient * right_coefficient
            )
    return _trim(result)


def _times_parameter(polynomial: Polynomial) -> Polynomial:
    return _trim((Fraction(0),) + polynomial)


def _divide(
    numerator: Polynomial, denominator: Polynomial
) -> tuple[Polynomial, Polynomial]:
    if _zero(denominator):
        raise ValueError("polynomial division by zero")
    if _zero(numerator) or len(numerator) < len(denominator):
        return ZERO, numerator
    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    remainder = numerator
    while not _zero(remainder) and len(remainder) >= len(denominator):
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[degree] += coefficient
        multiple = (Fraction(0),) * degree + _scale(denominator, coefficient)
        remainder = _subtract(remainder, multiple)
    return _trim(quotient), remainder


def _exact_divide(numerator: Polynomial, denominator: Polynomial) -> Polynomial:
    quotient, remainder = _divide(numerator, denominator)
    if not _zero(remainder):
        raise ArithmeticError("internal exact-division invariant failed")
    return quotient


def _monic_gcd(left: Polynomial, right: Polynomial) -> Polynomial:
    while not _zero(right):
        _, remainder = _divide(left, right)
        left, right = right, remainder
    if _zero(left):
        raise ValueError("the zero-zero coefficient pair is excluded")
    return _scale(left, Fraction(1) / left[-1])


def _strings(polynomial: Polynomial) -> list[str]:
    return [str(coefficient) for coefficient in polynomial]


@dataclass(frozen=True)
class Operation:
    kind: Literal["upper", "lower"]
    coefficient: Polynomial

    def as_json(self) -> dict[str, object]:
        return {"kind": self.kind, "coefficient": _strings(self.coefficient)}


@dataclass(frozen=True)
class Certificate:
    a: Polynomial
    b: Polynomial
    gcd: Polynomial
    normalized_a: Polynomial
    normalized_b: Polynomial
    branch: Literal["translation", "base"]
    constant: Fraction
    operations: tuple[Operation, ...]
    final_a: Polynomial
    final_b: Polynomial

    def as_json(self) -> dict[str, object]:
        return {
            "version": 1,
            "a": _strings(self.a),
            "b": _strings(self.b),
            "gcd": _strings(self.gcd),
            "normalized_a": _strings(self.normalized_a),
            "normalized_b": _strings(self.normalized_b),
            "branch": self.branch,
            "constant": str(self.constant),
            "operations": [operation.as_json() for operation in self.operations],
            "final_a": _strings(self.final_a),
            "final_b": _strings(self.final_b),
        }


def _translation_descent(
    a: Polynomial, b: Polynomial
) -> tuple[tuple[Operation, ...], Fraction]:
    """Reduce a primitive pair with b(0) nonzero to (0, b(0))."""
    if b[0] == 0:
        raise ArithmeticError("translation descent needs a nonzero b(0)")
    constant = b[0]
    operations: list[Operation] = []
    while len(b) > 1:
        previous_degree = len(b) - 1
        upper, a = _divide(a, b)
        if not _zero(upper):
            operations.append(Operation("upper", upper))
        if _zero(a):
            raise ArithmeticError("primitive Euclidean remainder vanished")
        lower, b = _divide(b, _times_parameter(a))
        if not _zero(lower):
            operations.append(Operation("lower", lower))
        if b[0] != constant or len(b) - 1 >= previous_degree:
            raise ArithmeticError("Euclidean degree-descent invariant failed")
    if not _zero(a):
        operations.append(Operation("upper", _scale(a, Fraction(1) / b[0])))
    return tuple(operations), constant


def _replay(
    a: Polynomial, b: Polynomial, operations: tuple[Operation, ...]
) -> tuple[Polynomial, Polynomial]:
    for operation in operations:
        if operation.kind == "upper":
            a = _subtract(a, _multiply(operation.coefficient, b))
        else:
            b = _subtract(
                b, _times_parameter(_multiply(operation.coefficient, a))
            )
    return a, b


def generate_certificate(a: Polynomial, b: Polynomial) -> Certificate:
    a, b = _trim(a), _trim(b)
    gcd = _monic_gcd(a, b)
    normalized_a = _exact_divide(a, gcd)
    normalized_b = _exact_divide(b, gcd)
    if normalized_b[0] != 0:
        branch: Literal["translation", "base"] = "translation"
        operations, constant = _translation_descent(normalized_a, normalized_b)
        final_a, final_b = ZERO, _scale(gcd, constant)
    else:
        branch = "base"
        divided_b = _trim(normalized_b[1:])
        auxiliary, constant = _translation_descent(divided_b, normalized_a)
        operations = tuple(
            Operation(
                "lower" if operation.kind == "upper" else "upper",
                operation.coefficient,
            )
            for operation in auxiliary
        )
        final_a, final_b = _scale(gcd, constant), ZERO
    if _replay(a, b, operations) != (final_a, final_b):
        raise ArithmeticError("internal final-row replay invariant failed")
    return Certificate(
        a=a, b=b, gcd=gcd,
        normalized_a=normalized_a, normalized_b=normalized_b,
        branch=branch, constant=constant, operations=operations,
        final_a=final_a, final_b=final_b,
    )


def _parse_polynomial(value: object, label: str) -> Polynomial:
    if not isinstance(value, list):
        raise ValueError(f"{label} must be a JSON coefficient array")
    coefficients: list[Fraction] = []
    for index, coefficient in enumerate(value):
        if isinstance(coefficient, bool) or not isinstance(
            coefficient, (int, str, Decimal)
        ):
            raise ValueError(f"{label}[{index}] must be a rational number or string")
        try:
            coefficients.append(Fraction(coefficient))
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            raise ValueError(f"invalid rational coefficient {label}[{index}]") from error
    return _trim(coefficients)


def _reject_nonfinite(value: str) -> object:
    raise ValueError(f"nonfinite JSON number {value} is not allowed")


def _read_json(value: str) -> object:
    return json.loads(value, parse_float=Decimal, parse_constant=_reject_nonfinite)


class _JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise ValueError(message)


def main(argv: Sequence[str] | None = None) -> int:
    parser = _JsonArgumentParser(add_help=False)
    parser.add_argument("--a")
    parser.add_argument("--b")
    parser.add_argument("--batch")
    parser.add_argument("--help", action="store_true")
    try:
        arguments = parser.parse_args(argv)
        if arguments.help:
            output: object = {
                "usage": "--a JSON_ARRAY --b JSON_ARRAY | --batch JSON_ARRAY",
                "coefficients": "ascending powers; rational strings are accepted",
                "schema_version": 1,
            }
        elif arguments.batch is not None:
            if arguments.a is not None or arguments.b is not None:
                raise ValueError("--batch cannot be combined with --a or --b")
            batch = _read_json(arguments.batch)
            if not isinstance(batch, list):
                raise ValueError("--batch must be a JSON array of coefficient pairs")
            certificates = []
            for index, item in enumerate(batch):
                if not isinstance(item, dict) or set(item) != {"a", "b"}:
                    raise ValueError(f"batch[{index}] must contain exactly a and b")
                a = _parse_polynomial(item["a"], f"batch[{index}].a")
                b = _parse_polynomial(item["b"], f"batch[{index}].b")
                certificates.append(generate_certificate(a, b).as_json())
            output = certificates
        else:
            if arguments.a is None or arguments.b is None:
                raise ValueError("supply both --a and --b, or supply --batch")
            a = _parse_polynomial(_read_json(arguments.a), "a")
            b = _parse_polynomial(_read_json(arguments.b), "b")
            output = generate_certificate(a, b).as_json()
        print(json.dumps(output, separators=(",", ":"), allow_nan=False))
        return 0
    except (ValueError, ArithmeticError) as error:
        print(json.dumps({"error": str(error)}, separators=(",", ":")))
        return 2


if __name__ == "__main__":
    sys.exit(main())
