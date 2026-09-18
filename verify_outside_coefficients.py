"""Exact identities for the outside-C symmetric-orbit pass.

This checker uses sparse Laurent monomials in (q, epsilon) whose coefficients
are ordinary polynomials in the normalized orbit time u.  It checks the orbit
parametrization and every moment used in the degree-two no-slice argument.
It does not formalize Newton--Puiseux lifting or prove the quantified theorem.
"""

from fractions import Fraction as Q
import json
import unittest


def trim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return tuple(poly)


def padd(left, right):
    out = [Q(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out)


def pmul(left, right):
    if not left or not right:
        return ()
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            out[i + j] += value * other
    return trim(out)


def pscale(poly, scalar):
    return trim(Q(scalar) * value for value in poly)


class Laurent:
    """Finite sum c_{ij}(u) q^i epsilon^j."""

    def __init__(self, terms=None):
        self.terms = {key: trim(value) for key, value in (terms or {}).items()
                      if trim(value)}

    @staticmethod
    def constant(value):
        return Laurent({(0, 0): (Q(value),)})

    @staticmethod
    def monomial(q_power=0, epsilon_power=0, upoly=(1,)):
        return Laurent({(q_power, epsilon_power): tuple(map(Q, upoly))})

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Laurent) else Laurent.constant(value)

    def __add__(self, other):
        other = self.coerce(other)
        out = dict(self.terms)
        for key, value in other.terms.items():
            out[key] = padd(out.get(key, ()), value)
            if not out[key]:
                del out[key]
        return Laurent(out)

    __radd__ = __add__

    def __neg__(self):
        return Laurent({key: pscale(value, -1) for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for (qi, ei), left in self.terms.items():
            for (qj, ej), right in other.terms.items():
                key = (qi + qj, ei + ej)
                out[key] = padd(out.get(key, ()), pmul(left, right))
                if not out[key]:
                    del out[key]
        return Laurent(out)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("Only nonnegative powers are needed")
        answer = Laurent.constant(1)
        base = self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent >>= 1
        return answer

    def average(self):
        """Integrate each coefficient polynomial over u from zero to one."""
        return {key: sum(value / Q(i + 1) for i, value in enumerate(poly))
                for key, poly in self.terms.items()
                if sum(value / Q(i + 1) for i, value in enumerate(poly))}

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms


u = (Q(0), Q(1))
v = padd(pmul(u, u), pscale(u, -1))            # u^2-u
kappa = (Q(1), Q(-2))                          # 1-2u

x = Laurent.monomial(-1, 0, pscale(v, 4))
y = (Laurent.monomial(0, 1, kappa)
     + Laurent.monomial(-3, -2, pscale(pmul(pmul(v, v), v), 64)))
z = (Laurent.monomial(1, 2)
     + Laurent.monomial(-2, -1, pscale(pmul(kappa, pmul(v, v)), 32))
     + Laurent.monomial(-5, -4,
                        pscale(pmul(pmul(pmul(v, v), pmul(v, v)), v), 1024)))

f = x * z - y * y
r = -(x ** 3) - f * y
g = z * (f ** 2) + 2 * (x ** 2) * y * f + x ** 5


class OutsideCoefficientChecks(unittest.TestCase):
    def test_orbit_invariants_pointwise(self):
        self.assertEqual(f, Laurent.monomial(0, 2, (-1,)))
        self.assertEqual(r, Laurent.monomial(0, 3, kappa))
        self.assertEqual(g, Laurent.monomial(1, 6))

    def test_basis_moments(self):
        expected = {
            "x": {(-1, 0): Q(-2, 3)},
            "y": {(-3, -2): Q(-16, 35)},
            "z": {(1, 2): Q(1), (-5, -4): Q(-256, 693)},
            "x2": {(-2, 0): Q(8, 15)},
            "xy": {(-4, -2): Q(128, 315)},
            "y2": {(0, 2): Q(1, 3), (-6, -4): Q(1024, 3003)},
            "xz": {(0, 2): Q(-2, 3), (-6, -4): Q(1024, 3003)},
            "yz": {(-2, 0): Q(-32, 105),
                   (-8, -6): Q(32768, 109395)},
        }
        actual = {"x": x, "y": y, "z": z, "x2": x*x, "xy": x*y,
                  "y2": y*y, "xz": x*z, "yz": y*z}
        for name, expression in actual.items():
            self.assertEqual(expression.average(), expected[name], name)

    def test_requested_coefficients(self):
        self.assertEqual((1 + x*y).average(),
                         {(0, 0): Q(1), (-4, -2): Q(128, 315)})
        self.assertEqual((1 + y*y).average(),
                         {(0, 0): Q(1), (0, 2): Q(1, 3),
                          (-6, -4): Q(1024, 3003)})


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(OutsideCoefficientChecks))
    print(json.dumps({
        "tests_run": result.testsRun,
        "successful": result.wasSuccessful(),
        "arithmetic": "exact Fraction coefficients; sparse Laurent q,epsilon powers",
        "external_packages": [],
        "scope": "orbit parametrization and degree-two moment identities only",
        "all_degree_argument_formalized": False,
        "general_criterion_resolved": False,
    }, indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)
