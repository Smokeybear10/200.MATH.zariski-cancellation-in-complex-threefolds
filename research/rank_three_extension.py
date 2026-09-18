"""Bounded exact slice search for a specified Freudenburg extension.

No finite unsuccessful search asserts nonexistence of an arbitrary slice.
The only coefficients used are rational numbers. This module is exploratory,
not imported by the standalone identity checker.
"""

import argparse
import json
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix

x, y, z, w = VARIABLES = sp.symbols("x y z w")
f = x*z-y**2
g = z*f**2+2*x**2*y*f+x**5
r = -x**3-f*y
DELTA = tuple(sp.expand(sp.det(sp.Matrix([
    [sp.diff(f, q) for q in VARIABLES[:3]],
    [sp.diff(g, q) for q in VARIABLES[:3]],
    [sp.diff(v, q) for q in VARIABLES[:3]],
]))) for v in VARIABLES[:3])


def monomials_at_most(bound, variables=4):
    if variables == 1:
        return [(i,) for i in range(bound+1)]
    return [(i,)+tail for i in range(bound+1)
            for tail in monomials_at_most(bound-i, variables-1)]


def derivative(poly, images):
    return sp.expand(sum(sp.diff(poly, v)*dv for v, dv in zip(VARIABLES, images)))


def search(bound, a):
    """Solve D(s)=1 among ALL total-degree <= bound polynomials over Q."""
    start = time.monotonic()
    inputs = monomials_at_most(bound)
    images = (*DELTA, sp.expand(a))
    terms = [sp.Poly(q, *VARIABLES).terms() for q in images]
    columns = []
    outputs = {(0, 0, 0, 0)}
    for monomial in inputs:
        col = {}
        for j, exponent in enumerate(monomial):
            if not exponent:
                continue
            for powers, coefficient in terms[j]:
                out = tuple(monomial[k]+powers[k]-(k == j) for k in range(4))
                col[out] = col.get(out, 0)+exponent*coefficient
        col = {q: c for q, c in col.items() if c}
        columns.append(col)
        outputs.update(col)
    ordered_outputs = sorted(outputs)
    row_ids = {q: i for i, q in enumerate(ordered_outputs)}
    rows = {}
    for j, col in enumerate(columns):
        for q, c in col.items():
            rows.setdefault(row_ids[q], {})[j] = sp.QQ.convert(c)
    rhs_column = len(inputs)
    rows.setdefault(row_ids[(0,0,0,0)], {})[rhs_column] = sp.QQ.one
    matrix = DomainMatrix(rows, (len(outputs), len(inputs)+1), sp.QQ)
    reduced, pivots = matrix.rref()
    answer = {
        "a": str(a), "total_degree_bound": bound,
        "unknown_coefficients": len(inputs), "equations": len(outputs),
        "augmented_rank": len(pivots), "arithmetic": "QQ",
        "bounded_slice_exists": rhs_column not in pivots,
        "elapsed_seconds": round(time.monotonic()-start, 3),
        "unbounded_nonexistence_proved": False,
    }
    if rhs_column not in pivots:
        data = reduced.to_dod()
        solution = sum(sp.sympify(data.get(i, {}).get(rhs_column, 0))*
                       sp.prod(v**e for v, e in zip(VARIABLES, inputs[pivot]))
                       for i, pivot in enumerate(pivots))
        if derivative(solution, images) != 1:
            raise AssertionError("RREF output failed direct polynomial verification")
        answer["slice"] = str(sp.expand(solution))
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--degree", type=int, default=6)
    parser.add_argument("--a", choices=("1", "1+x", "1+x^2", "1+y", "1+f"), default="1+x")
    args = parser.parse_args()
    choices = {"1": sp.Integer(1), "1+x": 1+x, "1+x^2": 1+x*x,
               "1+y": 1+y, "1+f": 1+f}
    if args.degree < 1:
        parser.error("Degree must be positive")
    print(json.dumps(search(args.degree, choices[args.a]), indent=2))
