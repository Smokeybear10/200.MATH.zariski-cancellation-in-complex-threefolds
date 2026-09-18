"""Finite exact support checks for the higher-pole argument.

Python standard library only. This checks specified polynomial identities,
truncated formal branches, and finite Newton-edge examples. It does not prove
the general formal lifting argument or Zariski cancellation.
"""

from fractions import Fraction as Q
import json
import unittest


class Cyclo:
    """Q[zeta]/(1+zeta+zeta^2+zeta^3+zeta^4), in the basis 1,...,zeta^3."""

    def __init__(self, value=0):
        if isinstance(value, Cyclo):
            self.c = value.c
        elif isinstance(value, (tuple, list)):
            if len(value) != 4:
                raise ValueError("Cyclotomic coordinates must have length four")
            self.c = tuple(map(Q, value))
        else:
            self.c = (Q(value), Q(0), Q(0), Q(0))

    def __add__(self, other):
        other = Cyclo(other)
        return Cyclo(tuple(a+b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return Cyclo(tuple(-a for a in self.c))

    def __sub__(self, other):
        return self+-Cyclo(other)

    def __rsub__(self, other):
        return Cyclo(other)+-self

    def __mul__(self, other):
        other = Cyclo(other)
        values = [Q(0)]*7
        for i, a in enumerate(self.c):
            for j, b in enumerate(other.c):
                values[i+j] += a*b
        for n in range(6, 3, -1):
            for j in range(4):
                values[n-4+j] -= values[n]
        return Cyclo(values[:4])

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        columns = [(self*Cyclo(tuple(int(i == j) for i in range(4)))).c
                   for j in range(4)]
        rows = [[columns[j][i] for j in range(4)]+[Q(i == 0)]
                for i in range(4)]
        for j in range(4):
            pivot = next(i for i in range(j, 4) if rows[i][j])
            rows[j], rows[pivot] = rows[pivot], rows[j]
            divisor = rows[j][j]
            rows[j] = [a/divisor for a in rows[j]]
            for i in range(4):
                if i != j:
                    multiplier = rows[i][j]
                    rows[i] = [a-multiplier*b for a, b in zip(rows[i], rows[j])]
        return Cyclo(tuple(rows[i][4] for i in range(4)))

    def __truediv__(self, other):
        return self*Cyclo(other).inverse()

    def __rtruediv__(self, other):
        return Cyclo(other)*self.inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse()**-exponent
        result, value = Cyclo(1), self
        while exponent:
            if exponent & 1:
                result *= value
            value *= value
            exponent //= 2
        return result

    def __eq__(self, other):
        return self.c == Cyclo(other).c

    def __bool__(self):
        return any(self.c)

    def __repr__(self):
        return "Cyclo"+repr(self.c)


ZETA = Cyclo((0, 1, 0, 0))
PRECISION = 12  # coefficients through U^11, not an infinite verification


def series_mul(a, b):
    size = len(a)
    zero = a[0]*0
    answer = [zero for _ in range(size)]
    for i in range(size):
        for j in range(size-i):
            answer[i+j] += a[i]*b[j]
    return answer


def series_inverse(a):
    answer = [1/a[0]]+[a[0]*0 for _ in range(len(a)-1)]
    for n in range(1, len(a)):
        answer[n] = -sum((a[j]*answer[n-j] for j in range(1, n+1)), a[0]*0)/a[0]
    return answer


def series_power(a, exponent):
    if exponent < 0:
        return series_power(series_inverse(a), -exponent)
    result = [a[0]*0+1]+[a[0]*0 for _ in range(len(a)-1)]
    value = list(a)
    while exponent:
        if exponent & 1:
            result = series_mul(result, value)
        value = series_mul(value, value)
        exponent //= 2
    return result


def phi_series(precision=PRECISION):
    phi = [Q(1)]+[Q(0)]*(precision-1)
    for n in range(1, precision):
        residual = series_power(phi, 6)[n]-phi[n]+Q(n == 1)
        phi[n] = -residual/5
    return phi


PHI = phi_series()


class Poly:
    """Sparse exact polynomials in x,y,z, independent of the series code."""

    def __init__(self, terms=None):
        self.terms = {p: Q(c) for p, c in (terms or {}).items() if c}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly({(0, 0, 0): Q(value)})

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
                power = tuple(a+b for a, b in zip(p, r))
                result[power] = result.get(power, Q(0))+c*d
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("Negative powers belong in the series code")
        result, value = Poly.coerce(1), self
        while exponent:
            if exponent & 1:
                result *= value
            value *= value
            exponent //= 2
        return result

    def diff(self, variable):
        result = {}
        for power, coefficient in self.terms.items():
            if power[variable]:
                out = tuple(n-int(i == variable) for i, n in enumerate(power))
                result[out] = coefficient*power[variable]
        return Poly(result)

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms


x, y, z = (Poly({tuple(int(i == j) for j in range(3)): 1}) for i in range(3))
f = x*z-y*y
g = z*f*f+2*x*x*y*f+x**5
r = -x**3-f*y
df = [f.diff(i) for i in range(3)]
dg = [g.diff(i) for i in range(3)]
IMAGES = tuple(df[(i+1) % 3]*dg[(i+2) % 3]-df[(i+2) % 3]*dg[(i+1) % 3]
               for i in range(3))


def delta(poly):
    return sum((poly.diff(i)*IMAGES[i] for i in range(3)), Poly())


H3 = x**6+Q(12, 5)*f*x**3*y+Q(42, 25)*f**2*y**2
A3 = -Q(12, 25)*(5*x**3*z+2*x**2*y**2+7*x*y*z**2-7*y**3*z)
H4 = (x**9+Q(18, 5)*f*x**6*y+Q(117, 25)*f**2*x**3*y**2
      +f**3*(Q(312, 125)*y**3+Q(9, 5)*x**3))
A4 = -Q(72, 125)*(25*x**5+35*x**3*y*z-22*x**2*y**3+13*x*y**2*z**2-13*y**4*z)


def branch_coefficients(poly, max_j):
    """Collect exact coefficients d_(J,L) through F^max_j in H(p1)-H(p0).

    p0 uses x=B phi(U), p1 uses x=zeta B phi(zeta^-1 U), U=F^3/B^6.
    This is finite truncation in F; it does not numerically sample endpoints.
    """
    result = {}
    for (i, y_power, j), coefficient in poly.terms.items():
        if y_power or j > max_j:
            continue
        ell = i-j
        phi_power = series_power(PHI, ell)
        for n in range((max_j-j)//3+1):
            if n >= len(PHI):
                raise ValueError("Increase the independently checked series precision")
            J, L = j+3*n, ell-6*n
            value = coefficient*phi_power[n]*(ZETA**L-1)
            key = (J, L)
            result[key] = result.get(key, Cyclo())+value
    return {key: value for key, value in result.items() if value}


def newton_edge(poly, m):
    terms = branch_coefficients(poly, m-2)
    if not terms:
        return None, {}
    slope = min(Q(L+2, m-1-J) for J, L in terms)
    edge = {key: value for key, value in terms.items()
            if Q(key[1]+2, m-1-key[0]) == slope}
    return slope, edge


class HigherPoleChecks(unittest.TestCase):
    def test_cyclotomic_field_and_negative_control(self):
        self.assertEqual(sum((ZETA**i for i in range(5)), Cyclo()), 0)
        self.assertEqual(ZETA**5, 1)
        self.assertNotEqual(ZETA**3, 1)
        self.assertEqual((1+ZETA)*(1+ZETA).inverse(), 1)

    def test_phi_equation_through_degree_eleven(self):
        sixth = series_power(PHI, 6)
        self.assertEqual([sixth[n]-PHI[n]+Q(n == 1) for n in range(PRECISION)],
                         [0]*PRECISION)
        bad = list(PHI)
        bad[8] += 1
        self.assertNotEqual(series_power(bad, 6)[8]-bad[8], 0)

    def test_positive_and_negative_series_powers(self):
        for exponent in (-8, -3, -1, 0, 1, 2, 7, 11):
            product = series_mul(series_power(PHI, exponent), series_power(PHI, -exponent))
            self.assertEqual(product, [1]+[0]*(PRECISION-1))

    def test_exact_branches_and_root_of_unity_factor(self):
        first = [Cyclo(c) for c in PHI]
        second = [c*ZETA**(1-n) for n, c in enumerate(PHI)]
        # The normalized branch solves X^6-X+U=0 because zeta^5=1.
        sixth = series_power(second, 6)
        self.assertEqual([sixth[n]-second[n]+Q(n == 1) for n in range(PRECISION)],
                         [Cyclo()] * PRECISION)
        for ell in (-7, -2, -1, 0, 1, 5, 6, 10, 13):
            direct1 = series_power(second, ell)
            direct0 = series_power(first, ell)
            rational = series_power(PHI, ell)
            for n in range(PRECISION):
                self.assertEqual(direct1[n]-direct0[n],
                                 rational[n]*(ZETA**(ell-6*n)-1))

    def test_jacobian_and_genuine_higher_pole_identities(self):
        self.assertEqual(delta(f), 0)
        self.assertEqual(delta(g), 0)
        self.assertEqual(delta(r), f*g)
        self.assertEqual(delta(H3), f**3*A3)
        self.assertEqual(delta(H4), f**4*A4)
        self.assertNotEqual(delta(H3), f**3*(A3+1))
        self.assertEqual({p: c for p, c in H3.terms.items() if p[1] == p[2] == 0},
                         {(6, 0, 0): Q(1)})
        self.assertEqual({p: c for p, c in H4.terms.items() if p[1] == p[2] == 0},
                         {(9, 0, 0): Q(1)})

    def test_third_and_fourth_pole_newton_edges(self):
        q3, edge3 = newton_edge(H3, 3)
        q4, edge4 = newton_edge(H4, 4)
        self.assertEqual(q3, 4)
        self.assertEqual(edge3, {(0, 6): ZETA-1})
        self.assertEqual(q4, Q(11, 3))
        self.assertEqual(edge4, {(0, 9): ZETA**4-1})

    def test_raw_fifth_divisible_exponents_cannot_be_discarded(self):
        # This is an expansion stress test, not an asserted f^5-divisible primitive.
        synthetic = x**10+x**31
        slope, edge = newton_edge(synthetic, 5)
        self.assertEqual(slope, 6)
        self.assertEqual(edge, {(3, 4): -2*(ZETA**4-1)})
        self.assertNotEqual(slope, Q(33, 4))  # incorrect raw-monomial edge

    def test_collected_invariant_terms_cancel(self):
        # g|_(y=0)=x^5+x^2z^3. Its apparently nonzero corrections cancel.
        self.assertEqual(branch_coefficients(g**2, 9), {})
        slope, edge = newton_edge(g**2+x**31, 5)
        self.assertEqual(slope, Q(33, 4))
        self.assertEqual(edge, {(0, 31): ZETA-1})

    def test_degree_preservation_and_finite_weight_grid(self):
        for m in range(2, 9):
            for degree in range(2*m-3, 2*m+4):
                for j in range(degree+1):
                    i = degree-j
                    for n in range(4):
                        J, L = j+3*n, i-j-6*n
                        self.assertEqual(L+2*J, degree)
                        if J < m-1:
                            self.assertGreater(Q(L+2, m-1-J), 2)
                        else:
                            # One finite rational q>2 verifies the displayed identity.
                            M, N = 7, 3
                            residual = N*L+M*J-((m-1)*M-2*N)
                            expected = N*(degree-2*m+4)+(J-m+1)*(M-2*N)
                            self.assertEqual(residual, expected)
                            self.assertGreater(residual, 0)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(HigherPoleChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({"tests_run": result.testsRun,
                      "success": result.wasSuccessful(),
                      "arithmetic": "Python standard library, exact rational/cyclotomic",
                      "phi_coefficients_checked": PRECISION,
                      "verified_general_theorem": False,
                      "verified_zariski_cancellation": False}, indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)
