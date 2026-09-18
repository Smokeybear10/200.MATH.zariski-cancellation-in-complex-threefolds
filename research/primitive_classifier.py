"""Exact finite classifiers for the specific Freudenburg derivation in this project.

Formal coefficients use Q[X,F,G]; actual primitives use Q[x,y,z].
The primitive theorem is Delta(R) intersect C = L(M), where
    L(P) = G*P + 2*(X*G-F**3)*P_X,
    M = (F,G-X**5)*C + X**2*Q[F,G].
The separate slice classifier is ONLY for D_a = Delta + a(x,f,g)*d/dw.
Its proof also needs the orbit and fiber obstructions in the research report.
Failure to find a primitive is not used as a generic no-slice implication.

Examples:
  /opt/anaconda3/bin/python research/primitive_classifier.py --self-test
  /opt/anaconda3/bin/python research/primitive_classifier.py '5*G*X**2-4*F**3*X'
  /opt/anaconda3/bin/python research/primitive_classifier.py --mode slice '1+3*G*X-2*F**3'
"""

from __future__ import annotations

import argparse
import ast
import json
import unittest

import sympy as sp


X, F, G = sp.symbols("X F G")
x, y, z, w = sp.symbols("x y z w")
f = x*z-y**2
g = z*f**2+2*x**2*y*f+x**5
r = -x**3-f*y
t_poly = 2*x**2*y+f*z
s_poly = x**2*y+f*z
ACTUAL = {X: x, F: f, G: g}

# Reconstruct the Jacobian independently of the formal operator L.
_grad_f = sp.Matrix([sp.diff(f, v) for v in (x, y, z)])
_grad_g = sp.Matrix([sp.diff(g, v) for v in (x, y, z)])
DELTA_IMAGES = tuple(sp.expand(v) for v in _grad_f.cross(_grad_g))


def parse_coefficient(source: str) -> sp.Expr:
    """Parse arithmetic without evaluating calls, attributes, or arbitrary code."""
    names = {"X": X, "F": F, "G": G, "x": X, "f": F, "g": G}

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
            if isinstance(node.op, ast.Pow) and isinstance(right, sp.Integer) and right >= 0:
                return left**right
        raise ValueError("Use rational arithmetic, X/F/G, and nonnegative integer powers")

    try:
        result = visit(ast.parse(source, mode="eval").body)
    except SyntaxError as error:
        raise ValueError("Invalid coefficient expression") from error
    return checked_coefficient(result)


def checked_coefficient(value: sp.Expr | str) -> sp.Expr:
    if isinstance(value, str):
        return parse_coefficient(value)
    value = sp.sympify(value)
    if value.has(sp.Float) or value.free_symbols - {X, F, G}:
        raise ValueError("Coefficients must be exact polynomials in Q[X,F,G]")
    try:
        return sp.Poly(value, X, F, G, domain=sp.QQ).as_expr()
    except (sp.PolynomialError, sp.polys.polyerrors.CoercionFailed) as error:
        raise ValueError("Coefficients must belong to Q[X,F,G]") from error


def operator_L(value: sp.Expr) -> sp.Expr:
    return sp.expand(G*value+2*(X*G-F**3)*sp.diff(value, X))


def delta(value: sp.Expr) -> sp.Expr:
    return sp.expand(sum(sp.diff(value, v)*dv
                         for v, dv in zip((x, y, z), DELTA_IMAGES)))


def actual(value: sp.Expr) -> sp.Expr:
    return sp.expand(value.subs(ACTUAL, simultaneous=True))


def inverse_L(coefficient: sp.Expr | str) -> tuple[sp.Expr, list[dict]]:
    """Return the unique rational P with L(P)=a and its genuine G poles."""
    a = checked_coefficient(coefficient)
    if a == 0:
        return sp.Integer(0), []
    poly = sp.Poly(a, X)
    degree = poly.degree()
    next_coefficient = sp.Integer(0)
    inverse_terms = []
    poles = []
    for j in range(degree, -1, -1):
        value = sp.cancel((poly.nth(j)+2*(j+1)*F**3*next_coefficient)/((2*j+1)*G))
        inverse_terms.append(value*X**j)
        denominator = sp.fraction(value)[1]
        order = int(sp.degree(denominator, G))
        if order > 0:
            poles.append({"x_degree": j, "g_pole_order": order, "coefficient": value})
        next_coefficient = value
    inverse = sp.expand(sum(inverse_terms))
    if sp.cancel(operator_L(inverse)-a) != 0:
        raise AssertionError("Inverse recursion failed its exact identity check")
    return inverse, poles


def canonical_decomposition(coefficient: sp.Expr | str) -> tuple[sp.Expr, sp.Expr]:
    """Return the unique A in Q[X,F], P in C with a=A+L(P)."""
    a = checked_coefficient(coefficient)
    remainder = sp.Integer(0)
    correction = sp.Integer(0)
    for (i, j, m), coefficient_value in sp.Poly(a, X, F, G, domain=sp.QQ).terms():
        value = coefficient_value
        while m > 0 and value != 0:
            correction += value*X**i*F**j*G**(m-1)/(2*i+1)
            value *= sp.Rational(2*i, 2*i+1)
            if value == 0:
                break
            i, j, m = i-1, j+3, m-1
        if value != 0:
            remainder += value*X**i*F**j
    remainder, correction = sp.expand(remainder), sp.expand(correction)
    if sp.expand(a-remainder-operator_L(correction)) != 0 or remainder.has(G):
        raise AssertionError("Canonical decomposition failed its exact identity check")
    return remainder, correction


def module_certificate(polynomial: sp.Expr) -> dict:
    """Decide P in M and, if true, construct P=F*P1+(G-X^5)*P2+X^2*Q."""
    polynomial = checked_coefficient(polynomial)
    residue = sp.expand(polynomial.subs({F: 0, G: X**5}, simultaneous=True))
    terms = sp.Poly(residue, X, domain=sp.QQ).terms()
    bad = [coefficient*X**degree[0] for degree, coefficient in terms
           if coefficient != 0 and degree[0] % 5 != 2]
    if bad:
        return {"member": False, "residue": residue, "forbidden_terms": bad}
    Q = sp.expand(sum(coefficient*G**((degree[0]-2)//5)
                      for degree, coefficient in terms if coefficient != 0))
    difference = sp.expand(polynomial-X**2*Q)
    at_f_zero = sp.expand(difference.subs(F, 0))
    P1 = sp.cancel((difference-at_f_zero)/F)
    P2, remainder = sp.div(at_f_zero, G-X**5, G)
    P1, P2 = checked_coefficient(P1), checked_coefficient(P2)
    if sp.expand(remainder) != 0:
        raise AssertionError("Residue membership did not give exact divisibility")
    if sp.expand(polynomial-F*P1-(G-X**5)*P2-X**2*Q) != 0:
        raise AssertionError("Module decomposition identity failed")
    return {"member": True, "residue": residue, "forbidden_terms": [],
            "P1": P1, "P2": P2, "Q": Q}


def classify_primitive(coefficient: sp.Expr | str) -> dict:
    """Classify Delta(H)=a exactly, constructing and checking H when it exists."""
    a = checked_coefficient(coefficient)
    inverse, poles = inverse_L(a)
    result = {"kind": "primitive", "coefficient": a, "inverse_P": inverse,
              "inverse_verified": True, "g_poles": poles}
    if poles:
        return {**result, "status": "does_not_exist",
                "reason": "The unique inverse L(P)=a has genuine G denominators"}
    certificate = module_certificate(inverse)
    result["module_certificate"] = certificate
    if not certificate["member"]:
        return {**result, "status": "does_not_exist",
                "reason": "The residue P(X,0,X^5) is not in X^2*Q[X^5]"}
    H = sp.expand(r*actual(certificate["P1"])
                  + r*t_poly*actual(certificate["P2"])
                  + actual(certificate["Q"])*s_poly)
    verification = sp.expand(delta(H)-actual(a))
    if verification != 0:
        raise AssertionError("Constructed primitive failed independent Jacobian verification")
    return {**result, "status": "exists", "primitive": H,
            "verification_residual": verification,
            "reason": "A polynomial primitive was constructed and exactly verified"}


def classify_slice_coefficient(coefficient: sp.Expr | str) -> dict:
    """Specific full-C criterion for D_a, not a generic implication about primitives."""
    a = checked_coefficient(coefficient)
    A, P = canonical_decomposition(a)
    c = A.subs({X: 0, F: 0}, simultaneous=True)
    result = {"kind": "slice_for_specific_extension", "coefficient": a,
              "canonical_remainder_A": A, "canonical_correction_P": P,
              "constant_value": c,
              "scope": "D_a=Delta+a(x,f,g)*d/dw for the Delta defined in this file"}
    if c == 0:
        return {**result, "status": "does_not_exist", "reason": "The action has fixed points"}
    if A != c:
        reason = ("The nonconstant X remainder has the valuation-orbit obstruction"
                  if A.has(X) else "The nonconstant F remainder has the invariant-fiber obstruction")
        return {**result, "status": "does_not_exist", "reason": reason}
    certificate = module_certificate(P)
    result["module_certificate"] = certificate
    if not certificate["member"]:
        return {**result, "status": "does_not_exist",
                "reason": "The first-pole residue theorem excludes every polynomial slice"}
    primitive_result = classify_primitive(a-c)
    if primitive_result["status"] != "exists":
        raise AssertionError("Slice criterion disagrees with the primitive classification")
    H = primitive_result["primitive"]
    slice_expression = sp.expand((w-H)/c)
    verification = sp.expand(delta(slice_expression)+actual(a)*sp.diff(slice_expression, w)-1)
    if verification != 0:
        raise AssertionError("Constructed slice failed independent Jacobian verification")
    return {**result, "status": "exists", "primitive_of_a_minus_c": H,
            "slice": slice_expression, "verification_residual": verification,
            "reason": "An explicit polynomial slice was constructed and exactly verified"}


def jsonable(value):
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(item) for item in value]
    return value


class ExactClassifierTests(unittest.TestCase):
    def test_primitive_L_x_squared(self):
        result = classify_primitive(operator_L(X**2))
        self.assertEqual(result["status"], "exists")
        self.assertEqual(sp.expand(result["primitive"]-s_poly), 0)
        self.assertEqual(result["verification_residual"], 0)

    def test_primitive_delta_xr(self):
        result = classify_primitive(F*operator_L(X))
        self.assertEqual(result["status"], "exists")
        self.assertEqual(sp.expand(result["primitive"]-x*r), 0)

    def test_primitive_rt(self):
        result = classify_primitive(operator_L(G-X**5))
        self.assertEqual(result["status"], "exists")
        self.assertEqual(sp.expand(result["primitive"]-r*t_poly), 0)

    def test_mixed_module_primitive(self):
        P = F*(X+G)+(G-X**5)*(X**2+F)+X**2*(G**2+F)
        result = classify_primitive(operator_L(P))
        self.assertEqual(result["status"], "exists")
        self.assertEqual(delta(result["primitive"]), actual(operator_L(P)))

    def test_negative_L_x(self):
        result = classify_primitive(operator_L(X))
        self.assertEqual(result["status"], "does_not_exist")
        self.assertEqual(result["g_poles"], [])
        self.assertEqual(result["module_certificate"]["forbidden_terms"], [X])

    def test_negative_x(self):
        result = classify_primitive(X)
        self.assertEqual(result["status"], "does_not_exist")
        self.assertEqual({p["g_pole_order"] for p in result["g_poles"]}, {1, 2})

    def test_negative_f(self):
        result = classify_primitive(F)
        self.assertEqual(result["status"], "does_not_exist")
        self.assertEqual(result["inverse_P"], F/G)

    def test_zero(self):
        result = classify_primitive(0)
        self.assertEqual(result["primitive"], 0)
        self.assertEqual(result["verification_residual"], 0)

    def test_corrupt_primitive_negative_control(self):
        self.assertNotEqual(delta(s_poly+x)-actual(operator_L(X**2)), 0)

    def test_canonical_reduction(self):
        A, P = canonical_decomposition(G*X)
        self.assertEqual(A, 2*F**3/3)
        self.assertEqual(P, X/3)
        A, P = canonical_decomposition(1+operator_L(X**2))
        self.assertEqual((A, P), (1, X**2))

    def test_canonical_monomial_grid(self):
        """120 monomials; compare the remainder with an independent product formula."""
        for i in range(8):
            for j in range(3):
                for m in range(5):
                    with self.subTest(x_degree=i, f_degree=j, g_degree=m):
                        coefficient = X**i*F**j*G**m
                        A, P = canonical_decomposition(coefficient)
                        if m > i:
                            expected = sp.Integer(0)
                        else:
                            factor = sp.prod(sp.Rational(2*(i-k), 2*(i-k)+1)
                                             for k in range(m))
                            expected = factor*F**(j+3*m)*X**(i-m)
                        self.assertEqual(sp.expand(A-expected), 0)
                        self.assertEqual(sp.expand(A+operator_L(P)-coefficient), 0)

    def test_canonical_mixed_coefficients(self):
        samples = [
            1+G**3*X**4+F*G*X,
            sp.Rational(7, 3)*G**4*X**7-F**2*G**3+2*F*X**3,
            1+F*G**2*(X+F)+(G-X**5)*(X**2+F),
        ]
        for coefficient in samples:
            with self.subTest(coefficient=coefficient):
                A, P = canonical_decomposition(coefficient)
                self.assertEqual(sp.expand(A+operator_L(P)-coefficient), 0)
                self.assertEqual(canonical_decomposition(A), (A, 0))
                self.assertEqual(canonical_decomposition(operator_L(P)), (0, P))

    def test_positive_slice(self):
        result = classify_slice_coefficient(1+operator_L(X**2))
        self.assertEqual(result["status"], "exists")
        self.assertEqual(sp.expand(result["slice"]-(w-s_poly)), 0)

    def test_negative_slice_obstructions(self):
        for coefficient in (1+operator_L(X), 1+X, 1+F, G):
            with self.subTest(coefficient=coefficient):
                self.assertEqual(classify_slice_coefficient(coefficient)["status"], "does_not_exist")

    def test_constant_primitive_is_not_constant_slice(self):
        self.assertEqual(classify_primitive(1)["status"], "does_not_exist")
        self.assertEqual(classify_slice_coefficient(1)["slice"], w)

    def test_invariant_positive_slice(self):
        result = classify_slice_coefficient(2+F*G*(F+G))
        self.assertEqual(result["status"], "exists")
        self.assertEqual(result["verification_residual"], 0)

    def test_parser_and_validation(self):
        self.assertEqual(parse_coefficient("5*G*X**2 - 4*F**3*X"), operator_L(X**2))
        for bad in ("__import__('os')", "0.5*X", "Y+1", "1/G"):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                parse_coefficient(bad)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("coefficient", nargs="?", help="Exact polynomial in X,F,G")
    parser.add_argument("--mode", choices=("primitive", "slice", "decompose"), default="primitive")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ExactClassifierTests)
        outcome = unittest.TextTestRunner(verbosity=2).run(suite)
        raise SystemExit(0 if outcome.wasSuccessful() else 1)
    if args.coefficient is None:
        parser.error("Supply a coefficient or --self-test")
    try:
        coefficient = parse_coefficient(args.coefficient)
        if args.mode == "decompose":
            A, P = canonical_decomposition(coefficient)
            result = {"coefficient": coefficient, "remainder_A": A, "correction_P": P,
                      "identity_residual": sp.expand(coefficient-A-operator_L(P))}
        elif args.mode == "slice":
            result = classify_slice_coefficient(coefficient)
        else:
            result = classify_primitive(coefficient)
    except ValueError as error:
        parser.error(str(error))
    if args.json:
        print(json.dumps(jsonable(result), indent=2))
    else:
        for key, value in result.items():
            print(f"{key}: {jsonable(value)}")
        if args.mode == "primitive":
            print("Scope: this verdict concerns Delta(H)=a, not the slice question by itself.")


if __name__ == "__main__":
    main()
