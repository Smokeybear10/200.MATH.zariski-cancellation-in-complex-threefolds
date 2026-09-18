#!/usr/bin/env python3
"""Bounded exact controls for the iterated local-slice bridge.

The general preservation argument is a separate written proof. These
controls import no solver and deliberately include the failed uncorrected
coordinate formula before checking its finite reparametrization repair.
"""

import unittest

import sympy as sp


x, X, h, r, f, y = sp.symbols("x X h r f y")


def polynomial_variables(*values):
    symbols = set().union(*(sp.sympify(v).free_symbols for v in values))
    return (f, *sorted(symbols-{f}, key=str))


def cut(polynomial, order):
    retained = {powers: coefficient for powers, coefficient in polynomial.terms()
                if powers[0] < order}
    return sp.Poly.from_dict(retained, polynomial.gens,
                             domain=polynomial.domain).as_expr()


def trunc(value, order):
    return cut(sp.Poly(value, *polynomial_variables(value), domain=sp.QQ), order)


def mul(left, right, order):
    variables = polynomial_variables(left, right)
    return cut(sp.Poly(left, *variables, domain=sp.QQ)
               *sp.Poly(right, *variables, domain=sp.QQ), order)


def power(value, exponent, order):
    result = sp.Integer(1)
    for _ in range(exponent):
        result = mul(result, value, order)
    return result


def compose(value, variable, argument, order):
    result = sp.Integer(0)
    for (degree,), coefficient in sp.Poly(value, f).terms():
        if degree >= order:
            continue
        remaining, part = order-degree, sp.Integer(0)
        for entry in sp.Poly(coefficient, variable).all_coeffs():
            part = trunc(mul(part, argument, remaining)+entry, remaining)
        result += f**degree*part
    return trunc(result, order)


def inverse_unit(unit, order):
    assert trunc(unit-1, 1) == 0
    answer, term = sp.Integer(0), sp.Integer(1)
    for _ in range(order):
        answer += term
        term = mul(term, 1-unit, order)
    return trunc(answer, order)


def inverse_parameter(beta, order):
    assert trunc(beta-x, 1) == 0
    result = X
    for _ in range(order-1):
        result = trunc(X-compose(beta-x, x, result, order), order)
    return result


def G(F, rr, ss):
    degree = sp.degree(F, y)
    return sum(coefficient*rr**k*ss**(degree-k)
               for (k,), coefficient in sp.Poly(F, y).terms())


def difference(F, left, right, ss):
    degree = sp.degree(F, y)
    return sum(coefficient*ss**(degree-k)
               *sum(left**(k-1-j)*right**j for j in range(k))
               for (k,), coefficient in sp.Poly(F, y).terms() if k)


def genuine_jet(order):
    k0 = x*(1+x**7)**2
    B = 1+f*k0
    L = trunc(1+(1-B**3)*x**7, order)
    beta = mul(x, power(L, 2, order), order)
    gamma = mul(B*x*x, inverse_unit(L, order), order)
    parameter_inverse = inverse_parameter(beta, order)
    repaired_P = compose(gamma, x, parameter_inverse, order)
    return beta, parameter_inverse, repaired_P


class IteratedLocalSliceChecks(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def test_exact_mutation_and_inverse_with_lower_coefficients(self):
        for F in (y*y+y+1, y**3-y):
            degree = sp.degree(F, y)
            for n in (1, 2):
                Q = h+f
                next_r = r+h*Q
                next_k = x+Q*difference(F, next_r, r, f**n)
                old_relation = x*h-G(F, r, f**n)-f**(n*degree+1)
                new_relation = h*next_k-G(F, next_r, f**n)-f**(n*degree+1)
                self.assertZero(new_relation-old_relation)
                recovered_r = next_r-h*Q
                recovered_x = next_k-Q*difference(F, next_r, recovered_r, f**n)
                self.assertZero(recovered_r-r)
                self.assertZero(recovered_x-x)

    def test_uncorrected_pole_and_independent_first_jet(self):
        k0 = x*(1+x**7)**2
        B = 1+f*k0
        L = trunc(1+(1-B**3)*x**7, 2)
        actual_x = trunc(x*L**2, 2)
        actual_r = trunc(B*x**3*L, 2)
        defect = trunc(actual_r-actual_x**3, 2)
        self.assertZero(defect-f*k0*x**3*(1+15*x**7))
        self.assertNotEqual(defect, 0)
        _, _, repaired_P = genuine_jet(2)
        expected_P = X**2+f*X**3*(1+X**7)**2*(1+15*X**7)
        self.assertZero(repaired_P-expected_P)

    def test_genuine_forward_and_independent_inverse_reparametrization(self):
        for n in (2, 3):
            beta, parameter_inverse, repaired_P = genuine_jet(n)
            self.assertZero(compose(beta, x, parameter_inverse, n)-X)
            self.assertZero(compose(parameter_inverse, X, beta, n)-x)
            k0 = x*(1+x**7)**2
            B = 1+f*k0
            L = trunc(1+(1-B**3)*x**7, n)
            actual_r = mul(B*x**3, L, n)
            actual_h = mul(power(B, 2, n), x**5, n)
            P_on_beta = compose(repaired_P, X, beta, n)
            self.assertZero(actual_r-mul(beta, P_on_beta, n))
            self.assertZero(actual_h-mul(beta, power(P_on_beta, 2, n), n))
            # Independently apply the reverse mutation and inverse scaling
            # to the reconstructed P_tilde curve. B is reevaluated at its
            # new invariant k, not copied from the old parameter.
            new_r = trunc(X*repaired_P, n)
            new_h = mul(X, power(repaired_P, 2, n), n)
            new_rho = trunc(new_r+power(new_h, 2, n), n)
            new_k = trunc(X+2*mul(new_h, new_r, n)+power(new_h, 3, n), n)
            V = inverse_unit(1+f*new_k, n)
            old_h = mul(power(V, 2, n), new_h, n)
            old_s = mul(V, new_rho, n)
            old_r = trunc(old_s-power(old_h, 2, n), n)
            old_x = trunc(new_k-2*mul(old_h, old_s, n)+power(old_h, 3, n), n)
            self.assertZero(old_x-parameter_inverse)
            self.assertZero(old_r-power(old_x, 3, n))
            self.assertZero(old_h-power(old_x, 5, n))

    def test_f_divisible_branch_has_a_finite_local_slice_correction(self):
        for n in (2, 3):
            P = x*x+f+1
            old_h = mul(x, power(P, 2, n), n)
            Q = f*old_h
            L = trunc(1+mul(P, Q, n), n)
            next_k = mul(x, power(L, 2, n), n)
            next_r = mul(x*P, L, n)
            parameter_inverse = inverse_parameter(next_k, n)
            invariant_correction = compose(next_r, x, parameter_inverse, n)
            self.assertZero(compose(invariant_correction, X, next_k, n)-next_r)
            self.assertZero(trunc(next_k-x, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
