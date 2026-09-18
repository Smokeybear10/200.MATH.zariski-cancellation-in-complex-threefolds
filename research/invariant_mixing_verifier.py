#!/usr/bin/env python3
"""Independent checker for univariate mixing words and matrix-lift controls.

The row generator is not imported. This verifier recomputes the gcd and
replays every operation using SymPy, independently of the generator's
Fraction arithmetic. A valid word is conditional on the written hypotheses
D0 locally nilpotent, D0(b)=g and D0(g)=0. It does not verify those hypotheses
for an unspecified derivation, or prove unrestricted cancellation.
"""

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
import subprocess
import sys
import unittest

import sympy as sp


G = sp.Symbol("g")


class CertificateError(ValueError):
    """The supplied record does not certify its claimed normal form."""


def rational(value):
    if not isinstance(value, str) or len(value) > 1000:
        raise CertificateError("Rational coefficients must be short strings")
    try:
        q = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError("Invalid rational coefficient") from exc
    return sp.Rational(q.numerator, q.denominator)


def polynomial(values):
    if not isinstance(values, list) or not 1 <= len(values) <= 1001:
        raise CertificateError("Expected a nonempty rational coefficient array")
    return sp.Poly(sum(rational(value)*G**i for i, value in enumerate(values)),
                   G, domain=sp.QQ)


def verify(certificate):
    if not isinstance(certificate, dict):
        raise CertificateError("Expected an object")
    required = {"version", "a", "b", "gcd", "normalized_a", "normalized_b",
                "branch", "constant", "operations", "final_a", "final_b"}
    if not required.issubset(certificate):
        raise CertificateError("Missing certificate fields")
    if type(certificate["version"]) is not int or certificate["version"] != 1:
        raise CertificateError("Unsupported certificate version")
    a, b = polynomial(certificate["a"]), polynomial(certificate["b"])
    if a.is_zero and b.is_zero:
        raise CertificateError("The zero derivation has no stated normal form")
    divisor = sp.gcd(a, b).monic()
    if polynomial(certificate["gcd"]) != divisor:
        raise CertificateError("Incorrect monic gcd")
    normalized_a, normalized_b = a.exquo(divisor), b.exquo(divisor)
    if (polynomial(certificate["normalized_a"]) != normalized_a
            or polynomial(certificate["normalized_b"]) != normalized_b):
        raise CertificateError("Incorrect primitive coefficient pair")
    branch = "translation" if normalized_b.eval(0) != 0 else "base"
    constant = normalized_b.eval(0) if branch == "translation" else normalized_a.eval(0)
    if certificate["branch"] != branch or rational(certificate["constant"]) != constant:
        raise CertificateError("Incorrect branch or terminal constant")
    if constant == 0:
        raise CertificateError("A primitive pair must have a nonzero terminal constant")
    operations = certificate["operations"]
    if not isinstance(operations, list) or len(operations) > 10000:
        raise CertificateError("Invalid operation list")
    u = sp.Poly(G, G, domain=sp.QQ)
    for operation in operations:
        if not isinstance(operation, dict) or set(operation) != {"kind", "coefficient"}:
            raise CertificateError("Malformed operation")
        h = polynomial(operation["coefficient"])
        if operation["kind"] == "upper":
            a = a-h*b
        elif operation["kind"] == "lower":
            b = b-u*h*a
        else:
            raise CertificateError("Unknown operation kind")
    zero = sp.Poly(0, G, domain=sp.QQ)
    expected = (zero, constant*divisor) if branch == "translation" else (constant*divisor, zero)
    if (a, b) != expected:
        raise CertificateError("Operation word does not reach the claimed normal form")
    if (polynomial(certificate["final_a"]), polynomial(certificate["final_b"])) != expected:
        raise CertificateError("Incorrect recorded terminal row")
    return {
        "valid_generic_row_certificate": True,
        "branch": branch,
        "common_factor_degree": int(divisor.degree()),
        "operation_count": len(operations),
        "slice_if_base_is_nonslice": branch == "translation" and divisor.degree() == 0,
        "unverified_hypotheses": [
            "R is a complex polynomial three-ring",
            "D0 is a specified nonzero locally nilpotent derivation of R",
            "D0(b)=g is a specified nonconstant nonzero invariant",
        ],
        "general_cancellation_verified": False,
        "proof_assistant_verified": False,
    }


def field_apply(field, value, coordinates):
    return sp.expand(sum(q*sp.diff(value, x) for q, x in zip(field, coordinates)))


class MixingChecks(unittest.TestCase):
    @staticmethod
    def generate(pairs):
        """Treat the separate solver as an untrusted CLI producer."""
        producer = Path(__file__).with_name("invariant_mixing_solver.py")
        result = subprocess.run(
            [sys.executable, str(producer), "--batch", json.dumps(pairs)],
            capture_output=True, text=True, check=False, timeout=60)
        if result.returncode:
            raise AssertionError(result.stdout+result.stderr)
        return json.loads(result.stdout)

    @staticmethod
    def basic_certificate():
        return {"version": 1, "a": ["0"], "b": ["1"], "gcd": ["1"],
                "normalized_a": ["0"], "normalized_b": ["1"],
                "branch": "translation", "constant": "1", "operations": [],
                "final_a": ["0"], "final_b": ["1"]}

    def assertZero(self, value):
        entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
        self.assertTrue(all(sp.expand(entry) == 0 for entry in entries), value)

    def test_all_728_ternary_quadratic_pairs(self):
        polys = [list(map(str, p)) for p in itertools.product((-1, 0, 1), repeat=3)]
        pairs = [{"a": a, "b": b} for a in polys for b in polys
                 if any(Fraction(c) for c in a+b)]
        self.assertEqual(len(pairs), 728)
        records = self.generate(pairs)
        self.assertEqual(len(records), 728)
        for pair, record in zip(pairs, records):
            self.assertEqual(polynomial(record["a"]), polynomial(pair["a"]))
            self.assertEqual(polynomial(record["b"]), polynomial(pair["b"]))
            self.assertTrue(verify(record)["valid_generic_row_certificate"])

    def test_rational_and_high_degree_pairs(self):
        pairs = [
            {"a": ["1/2", "-3/7", "0", "2/5"], "b": ["-2/3", "1/11", "3"]},
            {"a": ["7/3", "1", "0", "4"], "b": ["0", "2/7", "-5/9"]},
            {"a": ["1"]+["0"]*15+["-1"], "b": ["2"]+["0"]*10+["1"]},
            {"a": ["0", "0", "-3/5"], "b": ["0", "0", "0", "7/8"]},
        ]
        records = self.generate(pairs)
        self.assertEqual(len(records), len(pairs))
        for pair, record in zip(pairs, records):
            self.assertEqual(polynomial(record["a"]), polynomial(pair["a"]))
            self.assertEqual(polynomial(record["b"]), polynomial(pair["b"]))
            verify(record)

    def test_zero_and_constant_boundaries(self):
        pairs = [{"a": ["0"], "b": ["3", "2"]},
                 {"a": ["2", "-1"], "b": ["0"]},
                 {"a": ["3/2"], "b": ["-7/3"]}]
        records = self.generate(pairs)
        self.assertEqual(len(records), len(pairs))
        for pair, record in zip(pairs, records):
            self.assertEqual(polynomial(record["a"]), polynomial(pair["a"]))
            self.assertEqual(polynomial(record["b"]), polynomial(pair["b"]))
        results = [verify(record) for record in records]
        self.assertEqual([r["branch"] for r in results], ["translation", "base", "translation"])
        self.assertEqual([r["slice_if_base_is_nonslice"] for r in results], [False, False, True])

    def test_bad_version_is_rejected(self):
        for value in (True, "1", 2):
            record = self.basic_certificate()
            record["version"] = value
            with self.assertRaises(CertificateError):
                verify(record)

    def test_wrong_gcd_or_primitive_pair_is_rejected(self):
        for field in ("gcd", "normalized_a", "normalized_b"):
            record = self.basic_certificate()
            record[field] = ["2", "1"]
            with self.assertRaises(CertificateError):
                verify(record)

    def test_wrong_terminal_claim_is_rejected(self):
        for field, value in (("branch", "base"), ("constant", "2"), ("final_b", ["2"])):
            record = self.basic_certificate()
            record[field] = value
            with self.assertRaises(CertificateError):
                verify(record)

    def test_forged_operation_is_rejected(self):
        record = self.basic_certificate()
        record["operations"] = [{"kind": "upper", "coefficient": ["1"]}]
        with self.assertRaises(CertificateError):
            verify(record)

    def test_unknown_operation_and_malformed_rationals_are_rejected(self):
        record = self.basic_certificate()
        record["operations"] = [{"kind": "scale", "coefficient": ["1"]}]
        with self.assertRaises(CertificateError):
            verify(record)
        for value in (1, True, "1/0", "nan", "__import__('os')"):
            record = self.basic_certificate()
            record["constant"] = value
            with self.assertRaises(CertificateError):
                verify(record)

    def test_zero_derivation_is_rejected(self):
        record = self.basic_certificate()
        record["b"] = ["0"]
        with self.assertRaises(CertificateError):
            verify(record)

    def test_generic_lift_determinant_and_inverse_parameters(self):
        g, h, j, a, ell, b, t = sp.symbols("g h j a ell b t")
        B, M = 1+g*h, 1+g*j
        relation = h+j+g*h*j+a*ell
        matrix = sp.Matrix(((B, -g*a), (ell, M)))
        self.assertZero(matrix.det()-1-g*relation)
        W, V = h*b-a*t, j*b+a*t
        image_b, image_t = matrix*sp.Matrix((b, t))
        inverse_b, inverse_t = sp.Matrix(((M, g*a), (-ell, B)))*sp.Matrix((b, t))
        self.assertZero(V.subs({b: image_b, t: image_t}, simultaneous=True)+W-relation*b)
        self.assertZero(W.subs({b: inverse_b, t: inverse_t}, simultaneous=True)+V-relation*b)

    def test_bezout_completion_identity(self):
        g, h, a, u, v = sp.symbols("g h a u v")
        B, L, M = 1+g*h, -u*h, v+a*u
        bezout = a*u+B*v-1
        self.assertZero(B*M+g*a*L-1-bezout)
        self.assertZero(M-1+g*v*h-bezout)

    def test_cohn_matrix_and_non_elementary_boundary_identity(self):
        g, h = sp.symbols("g h")
        cohn = sp.Matrix(((1+g*h, g*g), (-h*h, 1-g*h)))
        self.assertEqual(sp.expand(cohn.det()), 1)
        A, B, L, M = g*g, 1+g*h, -h**3, 1-g*h+g*g*h*h
        self.assertZero(B*M+g*A*L-1)
        # Determinants are checked here; non-elementarity is a sourced theorem.

    def test_variable_time_need_not_be_an_lnd_multiplier(self):
        g, h, b, t = coords = sp.symbols("g h b t")
        D0 = sp.Matrix((0, 0, g, 0))
        W = h*b-g*g*t
        self.assertEqual(field_apply(D0, W, coords), g*h)
        self.assertNotEqual(field_apply(D0, W, coords), 0)

    def test_characteristic_zero_domain_is_not_enough_without_rationals(self):
        x, y, t = coords = sp.symbols("x y t")
        D = sp.Matrix((1, x, 0))
        self.assertEqual(field_apply(D, x, coords), 1)
        self.assertEqual(field_apply(D, field_apply(D, y, coords), coords), 1)
        for i, j, k in itertools.product(range(4), repeat=3):
            value = sp.diff(x**i*y**j*t**k, t, 2)
            self.assertTrue(sp.Poly(value, x, y, t, modulus=2).is_zero)
        # The universal identity partial_t^2=0 in characteristic two follows
        # from k(k-1) even. D^2(y)=1 disproves conjugacy over Z in all degrees.

    def test_matrix_lift_two_sided_inverse_on_higher_jet(self):
        g, h, b, c, t = coords = sp.symbols("g h b c t")
        A, B, L, M = g*g, 1+g*h, -h**3, 1-g*h+g*g*h*h
        W, V = h*b-A*t, ((M-1)/g)*b+A*t
        phi = sp.Matrix((g, h, b+g*W, c+b*W+g*W**2/2, L*b+M*t))
        psi = sp.Matrix((g, h, b+g*V, c+b*V+g*V**2/2, -L*b+B*t))
        self.assertZero(phi.subs(dict(zip(coords, psi)), simultaneous=True)-sp.Matrix(coords))
        self.assertZero(psi.subs(dict(zip(coords, phi)), simultaneous=True)-sp.Matrix(coords))

    def test_matrix_lift_slice_and_invariants_on_higher_jet(self):
        g, h, b, c, t = coords = sp.symbols("g h b c t")
        A, B, L, M = g*g, 1+g*h, -h**3, 1-g*h+g*g*h*h
        W = h*b-A*t
        E = sp.Matrix((0, 0, A*g, A*b, B))
        images = sp.Matrix((g, h, b+g*W, c+b*W+g*W**2/2, L*b+M*t))
        self.assertZero(sp.Matrix([field_apply(E, p, coords) for p in images])
                        - sp.Matrix((0, 0, 0, 0, 1)))

    def test_three_variable_specialization_preserves_invariant_relation(self):
        g, h, b, c, t = sp.symbols("g h b c t")
        W = h*b-g*g*t
        new_b, new_c = b+g*W, c+b*W+g*W**2/2
        self.assertZero(2*g*new_c-new_b**2-(2*g*c-b*b))
        # Thus h=2gc-b^2 descends the higher-jet certificate to a C3 base.

    def test_rank_three_freudenburg_local_slice_hypotheses(self):
        x, y, z = coords = sp.symbols("x y z")
        f = x*z-y*y
        q = z*f*f+2*x*x*y*f+x**5
        r = -x**3-f*y
        gradients = sp.Matrix((f, q)).jacobian(coords)
        D0 = sp.Matrix((gradients[:, [1, 2]].det(),
                        -gradients[:, [0, 2]].det(), gradients[:, [0, 1]].det()))
        self.assertZero(field_apply(D0, r, coords)-f*q)
        self.assertEqual(field_apply(D0, f*q, coords), 0)
        self.assertEqual(field_apply(D0, f, coords), 0)
        # The source theorem supplies rank and local nilpotence, not this test.

    def test_fixed_ideal_wedge_for_an_extension(self):
        x, y, z, t = coords = sp.symbols("x y z t")
        E, U = sp.Matrix((0, x, 2*y, 1+x*z)), sp.Matrix((0, 0, 0, 1))
        matrix = sp.Matrix.hstack(E, U)
        minors = [sp.expand(matrix[list(pair), :].det())
                  for pair in itertools.combinations(range(4), 2)]
        self.assertEqual([p for p in minors if p != 0], [x, 2*y])

    def test_fixed_ideal_with_quadratic_slice(self):
        x, y, t = coords = sp.symbols("x y t")
        f = 1+x*y
        E = sp.Matrix((0, x*x, f))
        s = t+y**3/2+x*y**4/8-x*y*t-x*x*y*y*t/2+x**3*t*t/2
        q = sp.diff(s, t)
        d = sp.Matrix((0, 0, 1))-q*E
        self.assertEqual(field_apply(E, s, coords), 1)
        self.assertEqual(field_apply(d, s, coords), 0)
        self.assertZero(x*x*d[2]-f*d[1]-x*x)
        self.assertEqual(sp.rem(d[2], x*x, x), 0)

    def test_fixed_scheme_nonreduced_slice_restriction(self):
        x, y, t = sp.symbols("x y t")
        f = 1+x*y
        restricted = (1-x*y)*t+y**3/2+x*y**4/8
        self.assertEqual(sp.rem(f*sp.diff(restricted, t)-1, x*x, x), 0)
        self.assertEqual(sp.rem(f*(1-x*y)-1, x*x, x), 0)
        self.assertNotEqual(sp.rem(x, x*x, x), 0)

    def test_quotient_can_acquire_additional_invariants(self):
        x, y, z = coords = sp.symbols("x y z")
        D = sp.Matrix((0, x, 2*y))
        v = x*z-y*y
        self.assertEqual(field_apply(D, v, coords), 0)
        self.assertEqual(field_apply(D, y, coords).subs(x, 0), 0)
        self.assertEqual(v.subs(x, 0), -y*y)
        self.assertNotEqual(y.subs(y, -y), y)
        # All polynomials in -y^2 are even, whereas the new invariant y is odd.

    def test_comaximal_plinth_does_not_force_scalar_congruence(self):
        u, v, w, t = coords = sp.symbols("u v w t")
        g = u*v-1
        E = sp.Matrix((0, 0, g, u))
        h, s = u*w-g*t, -w+v*t
        self.assertEqual(field_apply(E, h, coords), 0)
        self.assertEqual(field_apply(E, s, coords), 1)
        self.assertZero(v*h+g*s-w)
        self.assertZero(h+u*s-t)
        self.assertEqual(sp.expand(u*v-g), 1)
        scalar = sp.Symbol("scalar")
        remainder = sp.groebner([g], v, u, scalar).reduce(u-scalar)[1]
        self.assertEqual(remainder, u-scalar)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", help="JSON file, or - for standard input")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(MixingChecks)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1
    if args.certificate is None:
        parser.error("choose --certificate or --self-test")
    try:
        data = sys.stdin.read() if args.certificate == "-" else Path(args.certificate).read_text()
        record = json.loads(data)
        result = [verify(item) for item in record] if isinstance(record, list) else verify(record)
        print(json.dumps(result, indent=2))
    except (CertificateError, ValueError, OSError) as exc:
        print(json.dumps({"valid_generic_row_certificate": False, "error": str(exc)}))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
