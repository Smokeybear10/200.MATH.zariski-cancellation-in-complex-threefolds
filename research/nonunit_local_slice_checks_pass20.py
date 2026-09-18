#!/usr/bin/env python3
"""Bounded exact controls for the two finite corrections in pass 20.

No solver or other project checker is imported. General divisibility and
polynomial invertibility are proved in the companion note, not by these
finite examples. Both the failed old formula and an independently
re-evaluated inverse of the repaired formula are tested.
"""

import unittest

import sympy as sp


f, x, X, h, H, r, T, y = sp.symbols("f x X h H r T y")


def generators(*values):
    symbols = set().union(*(sp.sympify(v).free_symbols for v in values))
    return (f, *sorted(symbols-{f}, key=str))


def cut(polynomial, order):
    terms = {powers: coefficient for powers, coefficient in polynomial.terms()
             if powers[0] < order}
    return sp.Poly.from_dict(terms, polynomial.gens,
                             domain=polynomial.domain).as_expr()


def trunc(value, order):
    return cut(sp.Poly(value, *generators(value), domain=sp.QQ), order)


def mul(left, right, order):
    variables = generators(left, right)
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
    result, term = sp.Integer(0), sp.Integer(1)
    for _ in range(order):
        result += term
        term = mul(term, 1-unit, order)
    return trunc(result, order)


def inverse_parameter(beta, variable, target, order):
    assert trunc(beta-variable, 1) == 0
    result = target
    for _ in range(order-1):
        result = trunc(target-compose(beta-variable, variable, result, order), order)
    return result


def q_correction(degree, Q, e):
    order = e+1
    k_curve = mul(h**(degree-1), power(Q, degree, order), order)
    b = trunc(1+f*k_curve, order)
    beta = mul(h, power(b, degree, order), order)
    inverse = inverse_parameter(beta, h, H, order)
    gamma = mul(Q, power(inverse_unit(b, order), degree-1, order), order)
    return compose(gamma, h, inverse, order).subs(H, h)


def monomial_next_k(old_x, old_h, old_r, Q, degree, e, order):
    ar = f**e*old_r
    next_r = trunc(ar+mul(old_h, Q, order), order)
    dd = sum(mul(power(next_r, degree-1-j, order), power(ar, j, order), order)
             for j in range(degree))
    return trunc(f**(e*degree)*old_x+mul(Q, dd, order), order), next_r


def homogeneous(F, value, scale):
    degree = sp.degree(F, y)
    return sum(coefficient*value**j*scale**(degree-j)
               for (j,), coefficient in sp.Poly(F, y).terms())


def difference(F, left, right, scale):
    degree = sp.degree(F, y)
    return sum(coefficient*scale**(degree-j)
               *sum(left**(j-1-k)*right**k for k in range(j))
               for (j,), coefficient in sp.Poly(F, y).terms() if j)


class NonunitLocalSliceChecks(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.cancel(value), 0)

    def test_exact_homogeneous_mutation_with_lower_coefficients(self):
        for F in (y*y+y+1, y**3-y):
            degree = sp.degree(F, y)
            for e, n in ((1, 1), (2, 1), (1, 2)):
                a, Q = f**e, h+f
                next_r = a*r+h*Q
                next_k = a**degree*x+Q*difference(F, next_r, a*r, a*f**n)
                old_relation = x*h-homogeneous(F, r, f**n)-f**(n*degree+1)
                new_relation = (h*next_k-homogeneous(F, next_r, a*f**n)
                                -a**degree*f**(n*degree+1))
                self.assertZero(new_relation-a**degree*old_relation)
                recovered_r = (next_r-h*Q)/a
                recovered_x = (next_k-Q*difference(
                    F, next_r, a*recovered_r, a*f**n))/a**degree
                self.assertZero(recovered_r-r)
                self.assertZero(recovered_x-x)

    def test_Q_forward_and_independent_inverse_normal_displacement(self):
        for degree, e, Q in ((2, 1, h), (2, 2, h), (2, 3, h),
                             (3, 1, h+1), (3, 2, h+1)):
            order, a = e+1, f**e
            repaired = q_correction(degree, Q, e)
            k, next_r = monomial_next_k(x, h, r, Q, degree, e, order)
            B = trunc(1+f*k, order)
            rho = mul(B, next_r, order)
            h_hat = mul(power(B, degree, order), h, order)
            defect = trunc(rho-mul(h_hat, compose(repaired, h, h_hat, order), order), order)
            self.assertZero(defect-a*r)
            # Start on the independent corrected curve with normal
            # displacement a*T. Re-evaluate k and B there.
            new_Q = repaired.subs(h, H)
            new_k, new_rho = monomial_next_k(X, H, T, new_Q, degree, e, order)
            V = inverse_unit(1+f*new_k, order)
            old_h = mul(power(V, degree, order), H, order)
            old_R = mul(V, new_rho, order)
            inverse_defect = trunc(old_R-mul(old_h, compose(Q, h, old_h, order), order), order)
            self.assertZero(inverse_defect-a*T)

    def test_actual_naive_pole_and_independent_Q_coefficients(self):
        # For e=2, the unchanged Q=h has numerator valuation exactly one.
        k, next_r = monomial_next_k(x, h, r, h, 2, 2, 3)
        B = trunc(1+f*k, 3)
        rho = mul(B, next_r, 3)
        h_hat = mul(power(B, 2, 3), h, 3)
        bad_numerator = trunc(rho-power(h_hat, 2, 3), 3)
        self.assertZero(trunc(bad_numerator, 2)+3*f*h**5)
        self.assertNotEqual(trunc(bad_numerator, 2), 0)
        # Derived separately by inverting h+2*f*h^4+f^2*h^7.
        repaired = q_correction(2, h, 2)
        self.assertZero(repaired-(h-3*f*h**4+24*f**2*h**7))
        corrected = trunc(rho-mul(h_hat, compose(repaired, h, h_hat, 3), 3), 3)
        self.assertZero(corrected-f**2*r)

    def test_two_stage_P_correction_and_independent_full_inverse_jet(self):
        e, n, precision = 2, 2, 4
        repaired_Q = q_correction(2, h, e)
        old_r, old_h = x**3, x**5
        k, next_r = monomial_next_k(x, old_h, old_r, old_h, 2, e, precision)
        B = trunc(1+f*k, precision)
        h_hat = mul(power(B, 2, precision), old_h, precision)
        rho = mul(B, next_r, precision)
        r_numerator = trunc(rho-mul(h_hat, compose(repaired_Q, h, h_hat, precision), precision), precision)
        self.assertZero(trunc(r_numerator, e))
        r_hat = trunc(sp.cancel(r_numerator/f**e), n)
        h_unit = trunc(sp.cancel(h_hat/old_h), n)
        x_hat = mul(sp.cancel(power(r_hat, 2, n)/old_h), inverse_unit(h_unit, n), n)
        gamma = mul(sp.cancel(r_hat/x), inverse_unit(sp.cancel(x_hat/x), n), n)
        inverse = inverse_parameter(x_hat, x, X, n)
        repaired_P = compose(gamma, x, inverse, n)
        # These coefficients were derived directly, not by q_correction.
        self.assertZero(x_hat-(x-f*(12*x**16+506*x**53)))
        self.assertZero(repaired_P-(X**2+f*(31*X**17+1265*X**54)))
        self.assertZero(r_hat-mul(x_hat, compose(repaired_P, X, x_hat, n), n))
        # Independent reverse: new corrected P-curve, new invariant k,
        # inverse scaling, old Q=h, and finally the old P=x^2 condition.
        new_r = trunc(X*repaired_P, precision)
        new_h = mul(X, power(repaired_P, 2, precision), precision)
        new_Q = compose(repaired_Q, h, new_h, precision)
        new_k, new_rho = monomial_next_k(X, new_h, new_r, new_Q, 2, e, precision)
        V = inverse_unit(1+f*new_k, precision)
        restored_h = mul(power(V, 2, precision), new_h, precision)
        restored_R = mul(V, new_rho, precision)
        restored_numerator = trunc(restored_R-power(restored_h, 2, precision), precision)
        self.assertZero(trunc(restored_numerator, e))
        restored_r = trunc(sp.cancel(restored_numerator/f**e), n)
        self.assertZero(restored_r-power(inverse, 3, n))
        self.assertZero(trunc(restored_h-power(inverse, 5, n), n))
        self.assertZero(compose(x_hat, x, inverse, n)-X)

    def test_quadratic_constant_Q_is_the_old_base_with_shifted_P(self):
        c, ell = sp.Rational(2), sp.Rational(3)
        F = y*y+ell*y+1
        for e, n in ((1, 1), (2, 1), (3, 2)):
            a = f**e
            next_r = a*r+c*h
            next_k = a*a*x+c*difference(F, next_r, a*r, a*f**n)
            shifted_h = h+2*a*r/c+a*a*x/(c*c)+ell*a*f**n/c
            self.assertZero(next_k-c*c*shifted_h)
            corrected_slice = sp.cancel((next_r-next_k/c)/a)
            self.assertZero(corrected_slice+r+a*x/c+ell*f**n)

    def test_CRT_Q_jet_at_two_distinct_multiplier_divisors(self):
        # a=f^2*(f-1)^2.  The f=0 jet has one extra order to
        # preserve the old normal displacement; the f=1 jet only
        # needs to make the first inverse numerator divisible by a.
        a = f**2*(f-1)**2
        local_jets = []
        for root, order in ((0, 3), (1, 2)):
            b = trunc(1+(f+root)*(f+root-1)*h**3, order)
            beta = mul(h, power(b, 2, order), order)
            parameter_inverse = inverse_parameter(beta, h, H, order)
            gamma = mul(h, inverse_unit(b, order), order)
            jet = compose(gamma, h, parameter_inverse, order).subs(H, h)
            local_jets.append(jet.subs(f, f-root))
        q_zero, q_one = local_jets
        modulus_one = (f-1)**2
        inverse_modulus = sp.invert(f**3, modulus_one, f)
        crt_tail = sp.rem((q_one-q_zero)*inverse_modulus, modulus_one, f)
        repaired = sp.expand(q_zero+f**3*crt_tail)
        self.assertZero(sp.rem(repaired-q_zero, f**3, f))
        self.assertZero(sp.rem(repaired-q_one, modulus_one, f))
        # Evaluate both forward and reverse at each root using the
        # actual normal ar and an independently reconstructed target k.
        for root, order in ((0, 3), (1, 2)):
            shifted_a = trunc(a.subs(f, f+root), order)
            shifted_q = trunc(repaired.subs(f, f+root), order)
            old_R = trunc(shifted_a*r+h*h, order)
            old_k = trunc(shifted_a**2*x+2*shifted_a*h*r+h**3, order)
            B = trunc(1+(f+root)*(f+root-1)*old_k, order)
            rho = mul(B, old_R, order)
            h_hat = mul(power(B, 2, order), h, order)
            numerator = trunc(rho-mul(h_hat, compose(shifted_q, h, h_hat, order), order), order)
            self.assertZero(numerator-shifted_a*r)
            new_Q = shifted_q.subs(h, H)
            new_rho = trunc(shifted_a*T+mul(H, new_Q, order), order)
            new_k = trunc(shifted_a**2*X+2*mul(shifted_a*T, new_Q, order)
                          +mul(H, power(new_Q, 2, order), order), order)
            V = inverse_unit(1+(f+root)*(f+root-1)*new_k, order)
            restored_h = mul(power(V, 2, order), H, order)
            restored_R = mul(V, new_rho, order)
            inverse_numerator = trunc(restored_R-power(restored_h, 2, order), order)
            self.assertZero(inverse_numerator-shifted_a*T)


if __name__ == "__main__":
    unittest.main(verbosity=2)
