#!/usr/bin/env python3
"""Independent finite exact controls for the general rank-three jet lift.

Run with /opt/anaconda3/bin/python research/general_jet_lift_checks.py.
No research solver or other checker is imported. The checks cover the stated
finite sets of parameters, not the universal coordinate theorem. In particular,
successful identities do not establish novelty or general cancellation.

Here f=x*z-y**m, r=x*P(x,f)+y*f**n, and
x*h=r**m+f**(m*n+1). The locally nilpotent derivation has sign
delta=-Jac(f,h,.), so delta(r)=f**n*h.
"""

import unittest
from functools import lru_cache

import sympy as sp


f, h, x, X, r, rho, t, s = sp.symbols("f h x X r rho t s")


def polynomial_variables(*values):
    others = set().union(*(sp.sympify(value).free_symbols for value in values))
    return (f, *sorted(others-{f}, key=str))


def truncate_polynomial(polynomial, n):
    retained = {monomial: coefficient for monomial, coefficient in polynomial.terms()
                if monomial[0] < n}
    return sp.Poly.from_dict(retained, polynomial.gens,
                             domain=polynomial.domain).as_expr()


def truncate(value, n):
    polynomial = sp.Poly(value, *polynomial_variables(value), domain=sp.QQ)
    return truncate_polynomial(polynomial, n)


def multiply(left, right, n):
    variables = polynomial_variables(left, right)
    product = sp.Poly(left, *variables, domain=sp.QQ)*sp.Poly(right, *variables,
                                                           domain=sp.QQ)
    return truncate_polynomial(product, n)


def positive_power(value, exponent, n):
    result = sp.Integer(1)
    for _ in range(exponent):
        result = multiply(result, value, n)
    return result


def unit_power(value, exponent, n):
    increment = truncate(value-1, n)
    assert truncate(increment, 1) == 0
    answer, term = sp.Integer(0), sp.Integer(1)
    for k in range(n):
        answer += sp.binomial(exponent, k)*term
        term = multiply(term, increment, n)
    return truncate(answer, n)


def base_polynomial(xx, ff, choice):
    return xx+1 if choice == 0 else xx**2+ff*xx+1


def coefficient_polynomial(ff, hh):
    return 1+ff+hh


def substitute_X(value, replacement, n):
    """Horner evaluation with tighter truncation for each f coefficient."""
    result = sp.Integer(0)
    for (degree,), coefficient in sp.Poly(value, f).terms():
        if degree >= n:
            continue
        order, part = n-degree, sp.Integer(0)
        for entry in sp.Poly(coefficient, X).all_coeffs():
            part = truncate(multiply(part, replacement, order)+entry, order)
        result += f**degree*part
    return truncate(result, n)


def jet_update(H, m, n, choice):
    hh = multiply(X**(m-1), positive_power(H, m, n), n)
    B = truncate(1+f*hh*coefficient_polynomial(f, hh), n)
    argument = multiply(unit_power(B, -m, n), X, n)
    base = truncate(base_polynomial(argument, f, choice), n)
    return multiply(unit_power(B, 1-m, n), base, n)


@lru_cache(maxsize=None)
def finite_jet(m, n, choice):
    H = truncate(base_polynomial(X, f, choice), n)
    for _ in range(n-1):
        H = jet_update(H, m, n, choice)
    return H


class GeneralJetLiftChecks(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def test_quotient_arithmetic_against_direct_expansion(self):
        value = 1+f*(X+1)+f*f*X
        expression = (X+f*X**2+f*f)**4+f*X**5
        replacement = x+f*(x*x+1)+f*f*x**3
        for n in range(1, 5):
            self.assertZero(positive_power(value, 4, n)-truncate(value**4, n))
            for exponent in (-4, -2, -1):
                expected = sp.series(value**exponent, f, 0, n).removeO()
                self.assertZero(unit_power(value, exponent, n)-expected)
            self.assertZero(substitute_X(expression, replacement, n)
                            -truncate(expression.subs(X, replacement), n))

    def test_physical_binomial_chart_and_jacobian(self):
        xx, yy, zz = sp.symbols("xx yy zz")
        variables = (xx, yy, zz)
        for m in (2, 3):
            ff = xx*zz-yy**m
            for n in (1, 2):
                for choice in (0, 1):
                    with self.subTest(m=m, n=n, choice=choice):
                        P = base_polynomial(xx, ff, choice)
                        rr = xx*P+yy*ff**n
                        hh = sum(sp.binomial(m, k)*xx**(m-k-1)*P**(m-k)
                                 *yy**k*ff**(n*k) for k in range(m))
                        hh += zz*ff**(m*n)
                        self.assertZero(xx*hh-rr**m-ff**(m*n+1))
                        # A directly differentiated Jacobian is independent
                        # of the advertised derivation images.
                        jac_r = sp.Matrix([
                            [sp.diff(poly, variable) for variable in variables]
                            for poly in (ff, hh, rr)]).det()
                        jac_x = sp.Matrix([
                            [sp.diff(poly, variable) for variable in variables]
                            for poly in (ff, hh, xx)]).det()
                        self.assertZero(-jac_r-ff**n*hh)
                        self.assertZero(-jac_x-m*ff**n*rr**(m-1))

    def test_all_requested_jets_fixed_point_and_contraction(self):
        for m in (2, 3, 4):
            for n in range(1, 5):
                for choice in (0, 1):
                    with self.subTest(m=m, n=n, choice=choice):
                        H = finite_jet(m, n, choice)
                        self.assertZero(jet_update(H, m, n, choice)-H)
                        for k in range(1, n):
                            perturbed = jet_update(H+f**k*(1+X), m, n, choice)
                            self.assertZero(truncate(perturbed-H, k+1))

    def test_independently_derived_first_order_jet(self):
        for m in (2, 3, 4):
            for choice in (0, 1):
                P0 = base_polynomial(X, 0, choice)
                P1 = sp.diff(base_polynomial(X, f, choice), f)
                h0 = X**(m-1)*P0**m
                correction = h0*(1+h0)*((1-m)*P0-m*X*sp.diff(P0, X))
                expected = P0+f*(P1+correction)
                self.assertZero(finite_jet(m, 1, choice)-P0)
                self.assertZero(finite_jet(m, 2, choice)-expected)
                # The uncorrected choice is a deliberate negative control.
                self.assertNotEqual(sp.expand(correction), 0)

    def test_forward_numerator_divisibility(self):
        for m in (2, 3, 4):
            for n in range(1, 5):
                for choice in (0, 1):
                    with self.subTest(m=m, n=n, choice=choice):
                        P = base_polynomial(x, f, choice)
                        hh = multiply(x**(m-1), positive_power(P, m, n), n)
                        B = truncate(1+f*hh*coefficient_polynomial(f, hh), n)
                        new_x = multiply(positive_power(B, m, n), x, n)
                        new_rho = multiply(B, x*P, n)
                        H = substitute_X(finite_jet(m, n, choice), new_x, n)
                        self.assertZero(truncate(new_rho-multiply(new_x, H, n), n))

    def test_inverse_numerator_divisibility(self):
        for m in (2, 3, 4):
            for n in range(1, 5):
                for choice in (0, 1):
                    with self.subTest(m=m, n=n, choice=choice):
                        H = finite_jet(m, n, choice)
                        hh = multiply(X**(m-1), positive_power(H, m, n), n)
                        B = truncate(1+f*hh*coefficient_polynomial(f, hh), n)
                        V = unit_power(B, -1, n)
                        old_x = multiply(positive_power(V, m, n), X, n)
                        old_r = multiply(V, X*H, n)
                        P = truncate(base_polynomial(old_x, f, choice), n)
                        self.assertZero(truncate(old_r-multiply(old_x, P, n), n))
                        self.assertZero(truncate(old_x-X, 1))

    def test_general_binomial_Z_identity_and_coprimality(self):
        H, Y, Z = sp.symbols("H Y Z")
        for m in (2, 3, 4, 5):
            for n in range(1, 5):
                new_rho = X*H+Y*f**n
                new_h = (new_rho**m+f**(m*n+1))/X
                correction = sum(sp.binomial(m, k)*X**(m-k-1)*H**(m-k)
                                 *Y**k*f**(n*k) for k in range(m))
                self.assertZero(X*(new_h-correction)-f**(m*n)*(Y**m+f))
                # The reconstructed invariant relation is checked separately.
                reconstructed_h = correction+Z*f**(m*n)
                self.assertZero(X*reconstructed_h-new_rho**m
                                -f**(m*n)*(X*Z-Y**m))
            physical_f = X*Z-Y**m
            self.assertEqual(sp.gcd(X, physical_f), 1)
            _, factors = sp.factor_list(physical_f)
            self.assertEqual(len(factors), 1)
            self.assertEqual(factors[0][1], 1)

    def test_unimodular_X_lift_and_polynomial_inverse(self):
        Q = coefficient_polynomial(f, h)
        B = 1+f*h*Q
        for m in (2, 3, 4):
            for n in range(1, 5):
                g = f**n*h
                U = (-1)**n*h**(n-1)*Q**n
                V0 = sum((-f*h*Q)**j for j in range(n))
                A, V = 1+B, V0-g*U
                self.assertZero(A*g*U+B*V-1)
                matrix = sp.Matrix([[B, -A*g], [U, V]])
                inverse = sp.Matrix([[V, A*g], [-U, B]])
                for entry in matrix*inverse-sp.eye(2):
                    self.assertZero(entry)
                for entry in inverse*matrix-sp.eye(2):
                    self.assertZero(entry)
                L = m*n+1
                actual_rho = B*r-A*g*t
                new_x = B**m*x+sp.cancel((1-B**m)/h)*f**L
                new_x += sum(sp.binomial(m, k)*(B*r)**(m-k)
                             *(-A)**k*f**(n*k)*h**(k-1)*t**k
                             for k in range(1, m+1))
                self.assertEqual(sp.denom(sp.cancel(new_x)), 1)
                self.assertZero(h*new_x-actual_rho**m-f**L
                                -B**m*(h*x-r**m-f**L))
                self.assertZero(truncate(new_x-x, 1))
                old_r = V*rho+A*g*s
                W = sp.cancel((V-1)/h)*rho+A*f**n*s
                old_x = X+W*sum(old_r**(m-1-j)*rho**j for j in range(m))
                self.assertEqual(sp.denom(sp.cancel(old_x)), 1)
                self.assertZero(h*old_x-old_r**m-h*X+rho**m)
                self.assertZero(truncate(old_x-X, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
