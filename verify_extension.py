"""Standalone exact certificate checks for deep-pass-02.md.

Uses only Python's standard library. Does not import the exploratory solver,
SymPy, or any earlier checker. Finite identities support, but do not replace,
the written all-degree proof and do not prove Zariski cancellation.
"""

from fractions import Fraction as Q
from math import factorial
import json
import unittest

N = 6  # x,y,z,w,e,q; Laurent exponents are allowed for orbit time.
ZERO_POWER = (0,)*N


class Poly:
    def __init__(self, terms=None):
        self.terms = {p: Q(c) for p, c in (terms or {}).items() if c}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly({ZERO_POWER: Q(value)})

    def __add__(self, other):
        result = dict(self.terms)
        for p, c in self.coerce(other).terms.items():
            result[p] = result.get(p, Q(0))+c
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({p: -c for p, c in self.terms.items()})

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        result = {}
        for p, c in self.terms.items():
            for r, d in self.coerce(other).terms.items():
                out = tuple(a+b for a, b in zip(p, r))
                result[out] = result.get(out, Q(0))+c*d
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            if len(self.terms) != 1:
                raise ValueError("Only a nonzero Laurent monomial can be inverted")
            p, c = next(iter(self.terms.items()))
            return Poly({tuple(n*a for a in p): c**n})
        answer, base = Poly.coerce(1), self
        while n:
            if n % 2:
                answer = answer*base
            base = base*base
            n //= 2
        return answer

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def diff(self, i):
        result = {}
        for p, c in self.terms.items():
            if p[i]:
                out = tuple(a-(j == i) for j, a in enumerate(p))
                result[out] = c*p[i]
        return Poly(result)

    def at(self, substitutions):
        answer = Poly()
        for p, c in self.terms.items():
            term = Poly.coerce(c)
            for i, power in enumerate(p):
                if power:
                    term = term*self.coerce(substitutions.get(i, V[i]))**power
            answer = answer+term
        return answer


V = tuple(Poly({tuple(int(i == j) for j in range(N)): 1}) for i in range(N))
x, y, z, w, e, q = V
f = x*z-y*y
g = z*f*f+2*x*x*y*f+x**5
r = -x**3-f*y
DX = 2*f*r
DY = -g-6*x*x*r
DZ = 2*x*f*f-10*x*y*r
IMAGES = (DX, DY, DZ, 1+Q(3,2)*q*x)


def D(poly, images=IMAGES):
    return sum((poly.diff(i)*value for i, value in enumerate(images)), Poly())


def jacobian(a, b, c):
    return (a.diff(0)*(b.diff(1)*c.diff(2)-b.diff(2)*c.diff(1))
            -a.diff(1)*(b.diff(0)*c.diff(2)-b.diff(2)*c.diff(0))
            +a.diff(2)*(b.diff(0)*c.diff(1)-b.diff(1)*c.diff(0)))


P = {0: 0, 1: e, 2: q*e*e, 3: 0}
END = {0: 0, 1: -e, 2: q*e*e, 3: 0}
TIME = 2*q**-1*e**-5


def endpoint(poly, time=TIME, limit=12, point=P, images=IMAGES):
    answer = Poly()
    current = poly
    for j in range(limit):
        if current == 0:
            return answer
        answer += Q(1, factorial(j))*time**j*current.at(point)
        current = D(current, images)
    raise AssertionError("Nilpotence bound was not verified")


class ExtensionChecks(unittest.TestCase):
    def test_arithmetic_negative_control(self):
        self.assertNotEqual((x+y)**2, x*x+y*y)
        self.assertEqual((x+y)**2, x*x+2*x*y+y*y)
        self.assertEqual(e**-5*e**5, 1)

    def test_jacobian_matches_independently_factored_derivation(self):
        for v, actual in zip(V[:3], IMAGES):
            self.assertEqual(jacobian(f, g, v), actual)

    def test_invariants_and_local_slice(self):
        self.assertEqual(D(f), 0)
        self.assertEqual(D(g), 0)
        self.assertEqual(D(r), f*g)
        self.assertEqual(D(x), 2*f*r)

    def test_algebraic_relation(self):
        self.assertEqual(r*r+f**3, x*g)

    def test_localized_generating_identities(self):
        # These justify the all-degree local-nilpotence proof in the note.
        self.assertEqual(g*x, r*r+f**3)
        self.assertEqual(f*y, -r-x**3)
        self.assertEqual(f*f*z, g+2*r*x*x+x**5)

    def test_nilpotence_indices(self):
        for v, index in zip(V[:4], (3, 7, 11, 4)):
            derivative = v
            for _ in range(index-1):
                derivative = D(derivative)
            self.assertNotEqual(derivative, 0)
            self.assertEqual(D(derivative), 0)

    def test_fixed_line(self):
        for value in IMAGES[:3]:
            self.assertEqual(value.at({0: 0, 1: 0}), 0)
        self.assertEqual(IMAGES[3].at({0: 0, 1: 0}), 1)
        # Equality of the full fixed locus uses the written two-case proof.

    def test_start_invariants(self):
        self.assertEqual(f.at(P), -e*e)
        self.assertEqual(r.at(P), e**3)
        self.assertEqual(g.at(P), q*e**6)

    def test_all_four_flow_endpoints(self):
        for v in V[:4]:
            self.assertEqual(endpoint(v), v.at(END))

    def test_wrong_time_rejected(self):
        self.assertNotEqual(endpoint(x, TIME*2), x.at(END))

    def test_normalized_x_trajectory(self):
        # w is a dummy integration variable here, not the fourth coordinate.
        trajectory = x.at(P)+2*(f*r).at(P)*w*TIME+(f*f*g).at(P)*w*w*TIME**2
        self.assertEqual(trajectory, 4*q**-1*(w*w-w))

    def test_invariant_coefficient_positive_slice_and_wrong_sign(self):
        p = 1+f+g
        a = 3+f*g*p
        def chosen_derivative(poly):
            return sum((poly.diff(i)*value for i, value in
                        enumerate((DX, DY, DZ, a))), Poly())
        self.assertEqual(chosen_derivative(Q(1,3)*(w-p*r)), 1)
        self.assertNotEqual(chosen_derivative(Q(1,3)*(w+p*r)), 1)

    def test_nonconstant_x_extension_rule_cannot_be_overgeneralized(self):
        h = x*r
        a = 1+3*f*g*x-2*f**4
        self.assertEqual(D(h), a-1)
        actual = sum((value*(w-h).diff(i) for i, value in
                      enumerate((DX, DY, DZ, a))), Poly())
        self.assertEqual(actual, 1)

    def test_one_plus_y_algebraic_endpoint_certificate(self):
        # Here e is H, q is C, with C^3=16/35. Reduce Laurent q powers exactly.
        point = {0: 0, 1: e**3, 2: q*e**4, 3: 0}
        end = {0: 0, 1: -e**3, 2: q*e**4, 3: 0}
        time = 2*q**-1*e**-13
        def reduce_cubic(poly):
            result = {}
            for powers, coefficient in poly.terms.items():
                quotient, remainder = divmod(powers[5], 3)
                out = powers[:5]+(remainder,)
                result[out] = result.get(out, Q(0))+coefficient*Q(16,35)**quotient
            return Poly(result)
        for variable in V[:4]:
            actual = endpoint(variable, time=time, point=point,
                              images=(DX, DY, DZ, 1+y))
            self.assertEqual(reduce_cubic(actual-variable.at(end)), 0)
        self.assertEqual(min(p[4] for p in time.terms), -13)

    def test_beta_coefficients_through_degree_twelve(self):
        for j in range(13):
            polynomial = (w*w-w)**j
            integral = sum(c/Q(p[3]+1) for p, c in polynomial.terms.items())
            expected = Q((-1)**j*factorial(j)**2, factorial(2*j+1))
            self.assertEqual(integral, expected)
            self.assertNotEqual(expected, 0)
        # The general formula is proved by integration by parts in the note.

    def test_pole_certificate(self):
        # Every polynomial evaluated at either endpoint has nonnegative e powers.
        # TIME has valuation -5; the written proof covers arbitrary polynomials.
        self.assertEqual(min(p[4] for p in TIME.terms), -5)
        for v in V[:4]:
            for point in (P, END):
                self.assertTrue(all(p[4] >= 0 for p in v.at(point).terms))


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ExtensionChecks))
    print(json.dumps({
        "tests_run": result.testsRun,
        "successful": result.wasSuccessful(),
        "arithmetic": "independent sparse Laurent polynomials over Fraction",
        "external_packages": [],
        "scope": "identities supporting a written family-specific no-slice proof",
        "general_cancellation_solved": False,
        "novelty_established": False,
        "lean_formalized": False,
    }, indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)
