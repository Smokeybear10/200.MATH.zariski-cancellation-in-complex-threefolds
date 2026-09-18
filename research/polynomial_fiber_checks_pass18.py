#!/usr/bin/env python3
"""Exact finite controls for replacing y**m by an arbitrary monic F(y).

Only SymPy and the standard library are imported. The written argument in
polynomial-fiber-findings-pass18.md, not these finite examples, supplies the
general local-nilpotence and kernel conclusions. No rank-three or exact-plinth
claim is assumed. Polynomial coefficient gcds are checked only in eight
explicit cases.

The additional jet tests use the actual divided-difference X expressions
in both directions, not only their advertised B**d and V**d congruences.
They cover three monic polynomials with lower coefficients, two choices
of P, n=1,2,3, and B=1+f*h*(1+f+h).
"""

import math
import unittest
from functools import lru_cache

import sympy as sp


x, y, z, f, h, r, R, S = sp.symbols("x y z f h r R S")
X, Y, Z, H, rho, t, s, a, b, v = sp.symbols("X Y Z H rho t s a b v")
FAMILIES = (y**2+y+1, y**3-y)
JET_FAMILIES = FAMILIES+(y**4+2*y**2-3*y+5,)


def P_value(xx, ff, choice):
    return xx if choice == 0 else xx**2+ff+1


def homogenization(F, rr, ss):
    degree = sp.degree(F, y)
    return sum(coefficient*rr**k*ss**(degree-k)
               for (k,), coefficient in sp.Poly(F, y).terms())


def taylor_tail(F, xx, yy, PP, ff, n):
    degree = sp.degree(F, y)
    return sum(sp.diff(F, y, k).subs(y, yy)/math.factorial(k)
               *xx**(k-1)*PP**k*ff**(n*(degree-k))
               for k in range(1, degree+1))


def divided_difference(F, left, right, ss):
    degree = sp.degree(F, y)
    return sum(coefficient*ss**(degree-k)
               *sum(left**(k-1-j)*right**j for j in range(k))
               for (k,), coefficient in sp.Poly(F, y).terms() if k)


def truncate(value, n):
    variables = (f, *sorted(sp.sympify(value).free_symbols-{f}, key=str))
    polynomial = sp.Poly(value, *variables, domain=sp.QQ)
    return cut_polynomial(polynomial, n)


def cut_polynomial(polynomial, n):
    retained = {powers: coefficient for powers, coefficient in polynomial.terms()
                if powers[0] < n}
    return sp.Poly.from_dict(retained, polynomial.gens,
                             domain=polynomial.domain).as_expr()


def multiply(left, right, n):
    symbols = sp.sympify(left).free_symbols | sp.sympify(right).free_symbols
    variables = (f, *sorted(symbols-{f}, key=str))
    product = sp.Poly(left, *variables, domain=sp.QQ)*sp.Poly(right, *variables,
                                                           domain=sp.QQ)
    return cut_polynomial(product, n)


def positive_power(value, exponent, n):
    result = sp.Integer(1)
    for _ in range(exponent):
        result = multiply(result, value, n)
    return result


def unit_power(value, exponent, n):
    increment = truncate(value-1, n)
    assert truncate(increment, 1) == 0
    result, term = sp.Integer(0), sp.Integer(1)
    for k in range(n):
        result += sp.binomial(exponent, k)*term
        term = multiply(term, increment, n)
    return truncate(result, n)


def jet_update(jet, degree, n, choice):
    hh = multiply(X**(degree-1), positive_power(jet, degree, n), n)
    B = truncate(1+f*multiply(hh, 1+f+hh, n), n)
    argument = multiply(unit_power(B, -degree, n), X, n)
    PP = P_value(argument, f, choice)
    return multiply(unit_power(B, 1-degree, n), truncate(PP, n), n)


@lru_cache(maxsize=None)
def finite_jet(degree, n, choice):
    jet = truncate(P_value(X, f, choice), n)
    for _ in range(n-1):
        jet = jet_update(jet, degree, n, choice)
    return jet


def substitute_X(value, replacement, n):
    answer = sp.Integer(0)
    for (degree,), coefficient in sp.Poly(value, f).terms():
        if degree >= n:
            continue
        order, part = n-degree, sp.Integer(0)
        for entry in sp.Poly(coefficient, X).all_coeffs():
            part = truncate(multiply(part, replacement, order)+entry, order)
        answer += f**degree*part
    return truncate(answer, n)


@lru_cache(maxsize=None)
def physical_case(index, n, choice):
    F = FAMILIES[index]
    degree = sp.degree(F, y)
    ff = x*z-F
    PP = P_value(x, ff, choice)
    rr = x*PP+y*ff**n
    hh = sp.expand(z*ff**(n*degree)+taylor_tail(F, x, y, PP, ff, n))
    return ff, rr, hh


class PolynomialFiberChecks(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def test_homogeneous_polynomial_relations(self):
        for index, F in enumerate(FAMILIES):
            degree = sp.degree(F, y)
            self.assertZero(homogenization(F, R, S)-S**degree*F.subs(y, R/S))
            for n in (1, 2):
                for choice in (0, 1):
                    ff, rr, hh = physical_case(index, n, choice)
                    self.assertZero(x*hh-homogenization(F, rr, ff**n)
                                    -ff**(n*degree+1))

    def test_physical_jacobian_and_primitive_controls(self):
        for index, F in enumerate(FAMILIES):
            G_R = sp.diff(homogenization(F, R, S), R)
            for n in (1, 2):
                for choice in (0, 1):
                    with self.subTest(F=str(F), n=n, choice=choice):
                        ff, rr, hh = physical_case(index, n, choice)
                        images = [sp.expand(-sp.Matrix([
                            [sp.diff(poly, variable) for variable in (x, y, z)]
                            for poly in (ff, hh, target)]).det())
                            for target in (x, y, z)]
                        actual_r = sum(image*sp.diff(rr, variable)
                                       for image, variable in zip(images, (x, y, z)))
                        expected_H_R = G_R.subs({R: rr, S: ff**n})
                        PP = P_value(x, f, choice)
                        self.assertZero(actual_r-ff**n*hh)
                        self.assertZero(images[0]-ff**n*expected_H_R)
                        self.assertZero(images[1]-hh
                                        +(PP+x*sp.diff(PP, x)).subs(f, ff)*expected_H_R)
                        self.assertEqual(sp.gcd_list(images), 1)

    def test_localized_charts_and_distinct_kernel_degrees(self):
        expected = {(0, 0): (2, 4, 6), (0, 1): (2, 6, 10),
                    (1, 0): (3, 6, 15), (1, 1): (3, 9, 24)}
        for index, F in enumerate(FAMILIES):
            degree = sp.degree(F, y)
            for n in (1, 2):
                xx = (homogenization(F, r, f**n)+f**(n*degree+1))/h
                for choice in (0, 1):
                    PP = P_value(xx, f, choice)
                    yy = (r-xx*PP)/f**n
                    zz = (h-taylor_tail(F, xx, yy, PP, f, n))/f**(n*degree)
                    self.assertZero(xx*zz-F.subs(y, yy)-f)
                    self.assertZero(xx*PP+yy*f**n-r)
                    self.assertEqual(tuple(sp.Poly(item, r).degree()
                                           for item in (xx, yy, zz)), expected[index, choice])
                observed = []
                for power_x in range(4):
                    for power_r in range(degree):
                        polynomial = sp.Poly(xx**power_x*r**power_r, r)
                        observed.append(polynomial.degree())
                        self.assertZero(polynomial.LC()-h**(-power_x))
                self.assertEqual(observed, list(range(4*degree)))

    def test_lower_coefficient_Z_identities(self):
        for F in FAMILIES:
            degree = sp.degree(F, y)
            for n in (1, 2, 3):
                new_rho = X*H+Y*f**n
                new_h = (homogenization(F, new_rho, f**n)+f**(n*degree+1))/X
                tail = taylor_tail(F, X, Y, H, f, n)
                self.assertZero(X*(new_h-tail)-f**(n*degree)*(F.subs(y, Y)+f))
                reconstructed_h = tail+Z*f**(n*degree)
                self.assertZero(X*reconstructed_h-homogenization(F, new_rho, f**n)
                                -f**(n*degree)*(X*Z-F.subs(y, Y)))

    def test_divided_difference_coordinate_identities(self):
        for F in FAMILIES:
            degree = sp.degree(F, y)
            for n in (1, 2, 3):
                B, V = 1+f*h*b, 1+f*h*v
                new_rho = B*r-a*f**n*h*t
                forward_W = f*b*r-a*f**n*t
                new_x = x+forward_W*divided_difference(F, new_rho, r, f**n)
                self.assertEqual(sp.denom(sp.cancel(new_x)), 1)
                self.assertZero(h*(new_x-x)-homogenization(F, new_rho, f**n)
                                +homogenization(F, r, f**n))
                forward_remainder = new_x-B**degree*x
                forward_remainder -= sp.cancel((B**degree-1)/h)*(r**degree-h*x)
                self.assertZero(truncate(forward_remainder, n))
                old_r = V*rho+a*f**n*h*s
                inverse_W = f*v*rho+a*f**n*s
                old_x = X+inverse_W*divided_difference(F, old_r, rho, f**n)
                self.assertEqual(sp.denom(sp.cancel(old_x)), 1)
                self.assertZero(h*(old_x-X)-homogenization(F, old_r, f**n)
                                +homogenization(F, rho, f**n))
                inverse_remainder = old_x-V**degree*X
                inverse_remainder -= sp.cancel((V**degree-1)/h)*(rho**degree-h*X)
                self.assertZero(truncate(inverse_remainder, n))

    def test_residue_denominator_descent_premises(self):
        for F in FAMILIES:
            degree = sp.degree(F, y)
            # The coefficient gcd is the Gauss-lemma premise for the
            # polynomial x*z-F(y), which is linear in z.
            self.assertEqual(sp.gcd(x, F), 1)
            self.assertEqual(sp.degree(x*z-F, z), 1)
            for n in (1, 2, 3):
                self.assertZero(truncate(homogenization(F, r, f**n)-r**degree, n))
                for choice in (0, 1):
                    PP = P_value(x, f, choice)
                    hh = z*f**(n*degree)+taylor_tail(F, x, y, PP, f, n)
                    self.assertZero(truncate(hh-x**(degree-1)*PP**degree, n))
                    residue = x**(degree-1)*P_value(x, 0, choice)**degree
                    self.assertGreater(sp.degree(residue, x), 0)

    def test_actual_forward_jet_divisibility_with_lower_coefficients(self):
        for F in JET_FAMILIES:
            degree = sp.degree(F, y)
            for n in (1, 2, 3):
                for choice in (0, 1):
                    with self.subTest(F=str(F), n=n, choice=choice):
                        PP = P_value(x, f, choice)
                        rr = truncate(x*PP+y*f**n, n)
                        hh = truncate(z*f**(n*degree)
                                      +taylor_tail(F, x, y, PP, f, n), n)
                        Q = truncate(1+f+hh, n)
                        B = truncate(1+f*multiply(hh, Q, n), n)
                        actual_rho = truncate(multiply(B, rr, n)-f**n*hh*t, n)
                        W = truncate(f*multiply(Q, rr, n)-f**n*t, n)
                        actual_x = truncate(x+multiply(W, divided_difference(
                            F, actual_rho, rr, f**n), n), n)
                        jet = finite_jet(degree, n, choice)
                        self.assertZero(jet_update(jet, degree, n, choice)-jet)
                        evaluated_jet = substitute_X(jet, actual_x, n)
                        self.assertZero(truncate(actual_rho
                                                -multiply(actual_x, evaluated_jet, n), n))
                        if n == 2:
                            # Independent first-order Taylor expectation.
                            P0 = P_value(X, 0, choice)
                            P1 = sp.diff(P_value(X, f, choice), f)
                            h0 = X**(degree-1)*P0**degree
                            expected = P0+f*(P1+h0*(1+h0)
                                *((1-degree)*P0-degree*X*sp.diff(P0, X)))
                            self.assertZero(jet-expected)
                            naive = truncate(actual_rho-multiply(actual_x,
                                             P_value(actual_x, f, choice), n), n)
                            self.assertNotEqual(naive, 0)

    def test_actual_inverse_jet_divisibility_with_lower_coefficients(self):
        for F in JET_FAMILIES:
            degree = sp.degree(F, y)
            for n in (1, 2, 3):
                for choice in (0, 1):
                    with self.subTest(F=str(F), n=n, choice=choice):
                        jet = finite_jet(degree, n, choice)
                        actual_rho = truncate(X*jet+Y*f**n, n)
                        hh = truncate(taylor_tail(F, X, Y, jet, f, n)
                                      +Z*f**(n*degree), n)
                        Q = truncate(1+f+hh, n)
                        B = truncate(1+f*multiply(hh, Q, n), n)
                        V = unit_power(B, -1, n)
                        old_r = truncate(multiply(V, actual_rho, n)+f**n*hh*s, n)
                        # The polynomial quotient (V-1)/h is constructed
                        # from its geometric sum, not canceled modulo f**n.
                        quotient = sum((-1)**k*f**k*positive_power(hh, k-1, n)
                                       *positive_power(Q, k, n) for k in range(1, n))
                        W = truncate(multiply(quotient, actual_rho, n)+f**n*s, n)
                        old_x = truncate(X+multiply(W, divided_difference(
                            F, old_r, actual_rho, f**n), n), n)
                        self.assertZero(truncate(old_r-multiply(old_x,
                                         P_value(old_x, f, choice), n), n))
                        self.assertZero(truncate(old_x-X, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
