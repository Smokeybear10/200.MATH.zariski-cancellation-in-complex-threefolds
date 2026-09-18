#!/usr/bin/env python3
"""Independent exact controls for explicit quadratic-coefficient coordinates.

The finite SymPy substitutions below check the displayed inverse formulas in
``research/hyperbolic-coefficient-pass.md`` and two crossing families.  They do
not formalize the cohomological necessity argument and do not classify general
quadratic coefficients.

Run with ``/opt/anaconda3/bin/python verify_quadratic_coefficients.py``.
"""

from dataclasses import dataclass
import unittest

import sympy as sp


x, y, z, u = source = sp.symbols("x y z u")
X, Y, S, W, V = sp.symbols("X Y S W V")


def clean(value):
    """Put a rational expression into a comparison-friendly exact form."""
    return sp.cancel(sp.expand(value))


def substitute(expression, symbols, values):
    return clean(expression.subs(dict(zip(symbols, values)), simultaneous=True))


def require_nonzero(value, name):
    if clean(value) == 0:
        raise ValueError(f"{name} must be nonzero")


@dataclass(frozen=True)
class CoordinateMap:
    target: tuple
    forward: tuple
    inverse: tuple


def laurent_lift(terms, x_symbol=x, y_symbol=y):
    """Lift sum coeff[j] x**j from QQ[x,x^-1] modulo xy-1."""
    result = 0
    for exponent, coefficient in terms.items():
        if not isinstance(exponent, int):
            raise ValueError("Laurent exponents must be integers")
        result += coefficient * (
            x_symbol**exponent if exponent >= 0 else y_symbol**(-exponent)
        )
    return sp.expand(result)


def hyperbolic_bezout(k, c, x_symbol=x, y_symbol=y):
    """Return a, A, B0 with A*(xy-1)+B0*a=1."""
    if not isinstance(k, int):
        raise ValueError("k must be an integer")
    require_nonzero(c, "c")
    n = abs(k)
    a = c * (x_symbol**n if k >= 0 else y_symbol**n)
    B0 = (y_symbol**n if k >= 0 else x_symbol**n) / c
    A = -sum((x_symbol*y_symbol)**j for j in range(n)) if n else sp.Integer(0)
    return tuple(map(clean, (a, A, B0)))


def hyperbolic_map(k, c, laurent_terms, K):
    """Coordinates for (xy-1)u + a*z + b + (xy-1)K."""
    p = x*y-1
    a, A, B0 = hyperbolic_bezout(k, c)
    b = laurent_lift(laurent_terms)
    U = u+K
    polynomial = sp.expand(p*U+a*z+b)
    auxiliary = sp.expand(-B0*U+A*z)

    pt = X*Y-1
    at, At, B0t = hyperbolic_bezout(k, c, X, Y)
    bt = laurent_lift(laurent_terms, X, Y)
    translated = S-bt
    Ui = sp.expand(At*translated-at*W)
    zi = sp.expand(B0t*translated+pt*W)
    Ki = K.subs({x: X, y: Y, z: zi}, simultaneous=True)
    ui = sp.expand(Ui-Ki)
    return CoordinateMap((X, Y, S, W),
                         (x, y, polynomial, auxiliary),
                         (X, Y, zi, ui))


def crossing_linear_z_map(a, B, C, K):
    """Coordinates for xyu+a*z+B(x)+C(y)+xy*K."""
    require_nonzero(a, "a")
    U = u+K
    polynomial = sp.expand(x*y*U+a*z+B+C)
    Bt = B.subs(x, X)
    Ct = C.subs(y, Y)
    zi = clean((S-Bt-Ct-X*Y*W)/a)
    Ki = K.subs({x: X, y: Y, z: zi}, simultaneous=True)
    ui = clean(W-Ki)
    return CoordinateMap((X, Y, S, W),
                         (x, y, polynomial, U),
                         (X, Y, zi, ui))


def crossing_bezout(k, a, c, x_symbol=x, U_symbol=u):
    """Return q,r,A,B0 with q*A+r*B0=1 over QQ[x,U]."""
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    require_nonzero(a, "a")
    require_nonzero(c, "c")
    q = a+x_symbol*U_symbol
    r = c*x_symbol**k
    A = sum((-x_symbol*U_symbol/a)**j for j in range(k))/a
    B0 = (-1)**k*U_symbol**k/(a**k*c)
    return tuple(map(clean, (q, r, A, B0)))


def crossing_power_map(k, a, c, B, K):
    """Coordinates for xyu+a*y+c*x**k*z+B(x)+xy*K."""
    U = u+K
    q, r, A, B0 = crossing_bezout(k, a, c, x, U)
    polynomial = sp.expand(q*y+r*z+B)
    auxiliary = sp.expand(-B0*y+A*z)

    qt, rt, At, B0t = crossing_bezout(k, a, c, X, V)
    translated = S-B.subs(x, X)
    yi = sp.expand(At*translated-rt*W)
    zi = sp.expand(B0t*translated+qt*W)
    Ki = K.subs({x: X, y: yi, z: zi}, simultaneous=True)
    ui = sp.expand(V-Ki)
    return CoordinateMap((X, S, V, W),
                         (x, polynomial, U, auxiliary),
                         (X, yi, zi, ui))


class QuadraticCoefficientTests(unittest.TestCase):
    def assert_polynomial(self, expressions, symbols):
        for expression in expressions:
            self.assertEqual(sp.denom(clean(expression)).free_symbols, set())
            sp.Poly(clean(expression), *symbols)

    def assert_inverse(self, coordinate_map):
        for expression, expected in zip(coordinate_map.forward,
                                        coordinate_map.target):
            self.assertEqual(
                substitute(expression, source, coordinate_map.inverse), expected
            )
        for expression, expected in zip(coordinate_map.inverse, source):
            self.assertEqual(
                substitute(expression, coordinate_map.target,
                           coordinate_map.forward), expected
            )

    def test_hyperbolic_bezout_all_signs(self):
        for k in range(-5, 6):
            for c in (sp.Rational(2, 3), sp.Integer(-5)):
                a, A, B0 = hyperbolic_bezout(k, c)
                self.assertEqual(clean(A*(x*y-1)+B0*a), 1)
                self.assert_polynomial((a, A, B0), (x, y))

    def test_hyperbolic_inverse_negative_zero_positive_k(self):
        terms = {-3: sp.Rational(2, 5), -1: -3, 0: 7, 2: 4}
        controls = (
            (-3, sp.Rational(2, 3), x*z+y**2),
            (0, sp.Integer(-2), x*z**2+y*z+1),
            (2, sp.Rational(5, 2), x**2*z+y*z**2+x*y),
        )
        for k, c, K in controls:
            coordinate_map = hyperbolic_map(k, c, terms, K)
            self.assert_polynomial(coordinate_map.forward, source)
            self.assert_polynomial(coordinate_map.inverse,
                                   coordinate_map.target)
            self.assert_inverse(coordinate_map)

    def test_laurent_lift_has_correct_residue(self):
        terms = {-4: 3, -1: -2, 0: 5, 3: 7}
        lift = laurent_lift(terms)
        laurent = sum(coefficient*x**exponent
                      for exponent, coefficient in terms.items())
        self.assertEqual(clean(lift.subs(y, 1/x)-laurent), 0)

    def test_crossing_linear_z_inverses(self):
        controls = (
            (sp.Integer(2), x**3-x, y**2+1, x*z+y),
            (sp.Rational(-3, 2), x+4, y**4-y, x*z**2+y**2*z),
            (sp.Integer(7), sp.Integer(0), y, x**2*y*z+z**2),
        )
        for a, B, C, K in controls:
            coordinate_map = crossing_linear_z_map(a, B, C, K)
            self.assert_polynomial(coordinate_map.forward, source)
            self.assert_polynomial(coordinate_map.inverse,
                                   coordinate_map.target)
            self.assert_inverse(coordinate_map)

    def test_crossing_power_bezout_and_exponent_bounds(self):
        for k in range(1, 7):
            q, r, A, B0 = crossing_bezout(
                k, sp.Rational(3, 2), sp.Rational(-5, 3)
            )
            self.assertEqual(clean(q*A+r*B0), 1)
            self.assertEqual(sp.Poly(A, u).degree(), k-1)
            self.assertEqual(sp.Poly(B0, u).degree(), k)
            self.assert_polynomial((q, r, A, B0), (x, u))

    def test_crossing_power_inverses(self):
        controls = (
            (1, sp.Integer(2), sp.Integer(3), x**2+1, x*z+y**2),
            (2, sp.Rational(-3, 2), sp.Integer(5), x**3-x,
             x*y*z+z**2),
            # The all-k identity is checked above.  Keeping K=0 in this
            # higher-exponent inverse control avoids irrelevant expression
            # blow-up; nonlinear K is already exercised at k=1 and k=2.
            (4, sp.Integer(7), sp.Rational(-2, 3), x+4, sp.Integer(0)),
        )
        for k, a, c, B, K in controls:
            coordinate_map = crossing_power_map(k, a, c, B, K)
            self.assert_polynomial(coordinate_map.forward, source)
            self.assert_polynomial(coordinate_map.inverse,
                                   coordinate_map.target)
            self.assert_inverse(coordinate_map)

    def test_parameter_guards(self):
        with self.assertRaises(ValueError):
            hyperbolic_bezout(0, 0)
        with self.assertRaises(ValueError):
            hyperbolic_bezout(sp.Rational(1, 2), 1)
        with self.assertRaises(ValueError):
            crossing_linear_z_map(0, x, y, z)
        for arguments in ((0, 1, 1), (1, 0, 1), (1, 1, 0)):
            with self.assertRaises(ValueError):
                crossing_bezout(*arguments)
        with self.assertRaises(ValueError):
            laurent_lift({sp.Rational(1, 2): 1})

    def test_rank_three_smooth_coefficient_controls(self):
        p = x*y-z**2-1
        polynomial = p*u+x
        self.assertEqual(sp.hessian(p, (x, y, z)).rank(), 3)
        self.assertEqual(list(sp.groebner(
            [sp.diff(p, variable) for variable in (x, y, z)]+[p],
            x, y, z)), [1])
        self.assertEqual(list(sp.groebner(
            [sp.diff(polynomial, variable) for variable in source],
            *source)), [1])

        # A superficially similar diagonal example is not critical-point-free.
        bad = (x**2+y**2+z**2-1)*u+x
        point = {x: 1, y: 0, z: 0, u: sp.Rational(-1, 2)}
        self.assertEqual(tuple(sp.diff(bad, variable).subs(point)
                               for variable in source), (0, 0, 0, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
