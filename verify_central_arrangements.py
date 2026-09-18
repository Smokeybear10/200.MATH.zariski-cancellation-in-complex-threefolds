#!/usr/bin/env python3
"""Independent exact identities for the central-arrangement argument.

No research solver is imported. These finite algebraic tests do not
implement Gysin theory, certify novelty, or prove general cancellation.
"""

import unittest

import sympy as sp

x, y, z, u, T, V = sp.symbols("x y z u T V")
GENS = (x, y, z, u, T, V)
LOCAL_GENS = (y, z, u, T, V)


def require_laurent(expr):
    """Reject reduced denominators other than nonzero rational times x**k."""
    denominator = sp.fraction(sp.cancel(expr))[1]
    if denominator.free_symbols - {x}:
        raise ValueError("A localized denominator may depend only on x")
    try:
        polynomial = sp.Poly(denominator, x, domain=sp.QQ)
    except (sp.PolynomialError, sp.polys.polyerrors.CoercionFailed) as exc:
        raise ValueError("A localized denominator must be rational in x") from exc
    if polynomial.is_zero or len(polynomial.terms()) != 1:
        raise ValueError("A localized denominator must be a scalar times x**k")


def divide(expr, divisor, localized=False):
    if localized:
        require_laurent(expr)
        require_laurent(divisor)
    gens = LOCAL_GENS if localized else GENS
    domain = sp.QQ.frac_field(x) if localized else sp.QQ
    p = sp.Poly(sp.cancel(expr), *gens, domain=domain)
    q = sp.Poly(divisor, *gens, domain=domain)
    quotient, remainder = p.div(q)
    quotient, remainder = quotient.as_expr(), remainder.as_expr()
    if localized:
        require_laurent(quotient)
        require_laurent(remainder)
    return quotient, remainder


def exact_quotient(expr, divisor, localized=False):
    quotient, remainder = divide(expr, divisor, localized)
    if remainder != 0:
        raise ValueError("Nonzero polynomial remainder")
    return quotient


def arrangement(slopes, powers):
    if len(powers) != len(slopes) + 1 or len(slopes) < 1:
        raise ValueError("One multiplicity per distinct line is required")
    if any(type(m) is not int or m < 1 for m in powers):
        raise ValueError("Multiplicities must be positive integers")
    slopes = [sp.sympify(a) for a in slopes]
    if any(a.is_Rational is not True for a in slopes):
        raise ValueError("Slopes must be exact rational numbers")
    if len(set(slopes)) != len(slopes):
        raise ValueError("Duplicate lines")
    factors = [x] + [y - a*x for a in slopes]
    return sp.prod(factors), sp.prod(f**m for f, m in zip(factors, powers))


def finite_inverse(slopes, powers, coefficient, base, remainder):
    coefficient = sp.sympify(coefficient)
    if coefficient.is_Rational is not True or coefficient == 0:
        raise ValueError("A nonzero rational linear coefficient is required")
    base, remainder = sp.sympify(base), sp.sympify(remainder)
    sp.Poly(base, x, y, domain=sp.QQ)
    sp.Poly(remainder, x, y, z, domain=sp.QQ)
    Q, P = arrangement(slopes, powers)
    I = (T-base)/coefficient
    for _ in range(max(powers)-1):
        I = divide((T-base-Q*remainder.subs(z, I))/coefficient, P)[1]
    return P, coefficient*z+base+Q*remainder, sp.expand(I)


class ArrangementChecks(unittest.TestCase):
    def zero(self, expr):
        self.assertEqual(sp.cancel(sp.expand(expr)), 0)

    def check_completion(self, slopes, powers, coefficient, base, remainder):
        P, H, I = finite_inverse(slopes, powers, coefficient, base, remainder)
        self.zero(divide(H.subs(z, I)-T, P)[1])
        self.zero(divide(I.subs(T, H)-z, P)[1])
        F = P*u+H
        companion = exact_quotient(z-I.subs(T, F), P)
        inverse_z = I+P*V
        inverse_u = exact_quotient(T-H.subs(z, inverse_z), P)
        backward = {z: inverse_z, u: inverse_u}
        forward = {T: F, V: companion}
        self.zero(F.subs(backward, simultaneous=True)-T)
        self.zero(companion.subs(backward, simultaneous=True)-V)
        self.zero(inverse_z.subs(forward, simultaneous=True)-z)
        self.zero(inverse_u.subs(forward, simultaneous=True)-u)

    def test_three_squarefree_lines(self):
        self.check_completion([0, -1], [1, 1, 1], 2, x+y, z**2+x)

    def test_three_repeated_lines_nonlinear(self):
        self.check_completion([0, 1], [2, 1, 2], 1, x+y, z**2)

    def test_higher_multiplicities(self):
        self.check_completion([0, 1], [1, 2, 3], 3, x-y, z+x)

    def test_four_lines(self):
        self.check_completion([0, 1, -1], [2, 1, 1, 2],
                              sp.Rational(2, 3), x+y, z-y)

    def test_rational_slopes(self):
        self.check_completion([sp.Rational(1, 2), sp.Rational(-2, 3)],
                              [1, 1, 1], -1, x**2+y, z**2)

    def test_nilpotence_order_is_needed(self):
        Q, P = arrangement([0, 1], [1, 2, 3])
        self.zero(divide(Q**3, P)[1])
        self.assertNotEqual(divide(Q**2, P)[1], 0)
        P, H, I = finite_inverse([0, 1], [1, 2, 3], 1, 0, z)
        self.assertNotEqual(divide(H.subs(z, T)-T, P)[1], 0)
        self.zero(divide(H.subs(z, I)-T, P)[1])

    def test_invalid_inputs_rejected(self):
        cases = [([0, 0], [1, 1, 1]), ([0], [1, 0]),
                 ([0], [1, 1.0]), ([0], [1]), ([x], [1, 1])]
        for slopes, powers in cases:
            with self.subTest(slopes=slopes, powers=powers):
                with self.assertRaises(ValueError):
                    arrangement(slopes, powers)
        for coefficient in [0, x, sp.Float(1.5)]:
            with self.assertRaises(ValueError):
                finite_inverse([0, 1], [1, 1, 1], coefficient, 0, z)

    def test_relatively_prime_is_not_comaximal(self):
        self.assertEqual(sp.gcd(y, y-x), 1)
        basis = sp.groebner([y, y-x], x, y)
        self.assertEqual(basis.reduce(sp.Integer(1))[1], 1)
        self.zero(y.subs({x: 0, y: 0}))
        self.zero((y-x).subs({x: 0, y: 0}))

    def test_localized_comaximal_powers(self):
        for a in range(1, 4):
            for b in range(1, 4):
                left, right = y**a, (y-x)**b
                inverse = sp.invert(left, right, y, domain=sp.QQ.frac_field(x))
                require_laurent(inverse)
                self.zero(divide(left*inverse-1, right, True)[1])

    def test_laurent_denominator_guards(self):
        for allowed in [0, sp.Rational(2, 3), (T+y*z)/(3*x**4),
                        (x-1)/(x*(x-1))]:
            require_laurent(allowed)
        for forbidden in [1/(x-1), 1/y, 1/z, 1/T, 1/(x+V)]:
            with self.subTest(expression=forbidden):
                with self.assertRaises(ValueError):
                    require_laurent(forbidden)
        with self.assertRaises(ValueError):
            divide(1/(x-1), y, True)
        # A field-based division can introduce a forbidden pole even when
        # both inputs are polynomial, so the outputs must be checked too.
        with self.assertRaises(ValueError):
            divide(y, (x-1)*y, True)

    def test_localized_crt_two_sided_inverse(self):
        # Different unit leading coefficients x^2 and x^3 on the lines.
        Q = x*y*(y-x)
        P = x*y**2*(y-x)**2
        H = y+(x**2+x*y*(x-1))*z+Q*z**2
        moduli = [y**2, (y-x)**2]
        mod_product = sp.prod(moduli)
        glued = 0
        for v, a, base, modulus in [(y, x**2, 0, moduli[0]),
                                     (y-x, x**3, x, moduli[1])]:
            R = exact_quotient(H-a*z-base, v, True)
            I0 = (T-base)/a
            require_laurent(I0)
            I = (T-base-v*R.subs(z, I0))/a
            require_laurent(I)
            I = divide(I, modulus, True)[1]
            self.zero(divide(H.subs(z, I)-T, modulus, True)[1])
            self.zero(divide(I.subs(T, H)-z, modulus, True)[1])
            cofactor = sp.cancel(mod_product/modulus)
            inverse = sp.invert(cofactor, modulus, y,
                                domain=sp.QQ.frac_field(x))
            require_laurent(cofactor)
            require_laurent(inverse)
            glued += I*cofactor*inverse
            require_laurent(glued)
        glued = divide(glued, P, True)[1]
        self.zero(divide(H.subs(z, glued)-T, P, True)[1])
        self.zero(divide(glued.subs(T, H)-z, P, True)[1])
        self.zero(H.subs(x, 0)-y)
        # Check actual coordinate completion on a nonzero rational base fiber.
        p, h, i = [sp.cancel(a.subs(x, 2)) for a in (P, H, glued)]
        f = p*u+h
        companion = exact_quotient(z-i.subs(T, f), p)
        iz = i+p*V
        iu = exact_quotient(T-h.subs(z, iz), p)
        self.zero(f.subs({z: iz, u: iu}, simultaneous=True)-T)
        self.zero(companion.subs({z: iz, u: iu}, simultaneous=True)-V)
        self.zero(iz.subs({T: f, V: companion}, simultaneous=True)-z)
        self.zero(iu.subs({T: f, V: companion}, simultaneous=True)-u)

    def test_residue_matrix_unimodular_for_every_distinguished_row(self):
        for d in range(3, 8):
            matrix = sp.zeros(d, d-1)
            for j in range(1, d):
                matrix[0, j-1] = 1
                matrix[j, j-1] = -1
            for missing in range(d):
                square = matrix.copy()
                square.row_del(missing)
                self.assertEqual(abs(square.det()), 1)

    def test_nonprimitive_radial_map_has_nonunit_index(self):
        for d in range(3, 7):
            for missing in range(d):
                weights = [j+1 for j in range(d)]
                matrix = sp.zeros(d, d-1)
                for j in range(1, d):
                    matrix[0, j-1] = weights[0]
                    matrix[j, j-1] = -weights[j]
                matrix.row_del(missing)
                expected = sp.prod(w for j, w in enumerate(weights)
                                   if j != missing)
                self.assertEqual(abs(matrix.det()), expected)
                self.assertGreater(expected, 1)

    def test_total_rank_alone_does_not_imply_surjectivity(self):
        # d=3 permits target ranks (2,0,0) numerically, but the
        # projected residue image on a single curve remains cyclic.
        matrix = sp.Matrix([[1, 1], [0, 0]])
        self.assertEqual(matrix.rows, matrix.cols)
        self.assertEqual(matrix.rank(), 1)
        self.assertEqual(matrix.det(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
