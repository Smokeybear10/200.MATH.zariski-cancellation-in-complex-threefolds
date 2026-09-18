#!/usr/bin/env python3
"""Standalone exact controls for the nonreduced rank-three family.

Run with /opt/anaconda3/bin/python research/nonreduced_jet_checks.py.
Only the standard library and SymPy are imported, never a research solver.

Derivations and all-degree proofs are in the sibling notes
nonreduced-rank-three-images-pass17.md and
nonreduced-coordinate-lift-pass17.md. These bounded symbolic controls check
their formulas, not their universal conclusions. The f-adic computations
take place in polynomial quotients, not at a grid of numerical points.

The relative chart retains V**5 in f**n*q = V**5*rho**5 + h**3.
Its polynomial change of chart has W = (1-(B*V)**5)/f**n;
both compositions are checked modulo the appropriate defining relation.
"""

import math
import unittest
from functools import lru_cache

import sympy as sp


f, h, r, x, X, rho, t, s = sp.symbols("f h r x X rho t s")


def trunc(value, n):
    """Canonical remainder in f, with every other symbol a coefficient."""
    return sp.Poly(sp.expand(value), f).rem(sp.Poly(f**n, f)).as_expr()


def mul(left, right, n):
    return trunc(left * right, n)


def power(value, exponent, n):
    result = sp.Integer(1)
    for _ in range(exponent):
        result = mul(result, value, n)
    return result


def compose(value, variable, replacement, n):
    """Polynomial Horner substitution with truncation at every step."""
    result = sp.Integer(0)
    for coefficient in sp.Poly(value, variable).all_coeffs():
        result = trunc(mul(result, replacement, n) + coefficient, n)
    return result


def q_value(ff, hh, nontrivial=True):
    return 1 + ff + hh if nontrivial else sp.Integer(1)


def inverse_power(unit, exponent, n):
    """Truncated binomial formula; callers must have unit == 1 mod f."""
    increment = trunc(unit - 1, n)
    assert trunc(increment, 1) == 0
    result, term = sp.Integer(0), sp.Integer(1)
    for j in range(n):
        result += sp.binomial(exponent, j) * term
        term = mul(term, increment, n)
    return trunc(result, n)


def jet_update(jet, n, nontrivial=True):
    hh = mul(X**5, power(jet, 2, n), n)
    unit = trunc(1 + f * hh * q_value(f, hh, nontrivial), n)
    return inverse_power(unit, -5, n)


@lru_cache(maxsize=None)
def finite_jet(n, nontrivial=True):
    """The note's n-1 finite updates, not a symbolic implicit solver."""
    jet = sp.Integer(1)
    for _ in range(n - 1):
        jet = jet_update(jet, n, nontrivial)
    return jet


def geometric_pair(n, nontrivial=False):
    qq = q_value(f, h, nontrivial)
    B = 1 + f*h*qq
    U = (-1)**n * h**(n - 1) * qq**n
    V = sum((-f*h*qq)**j for j in range(n))
    return B, U, V


def generic_chart(n):
    xx = (r*r + f**(2*n + 1))/h
    yy = -(r + xx**3)/f**n
    zz = (h + 2*xx*xx*r + xx**5)/f**(2*n)
    ss = (r*xx*xx + h)/f**n
    return xx, yy, zz, ss


class NonreducedJetChecks(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.cancel(value), 0)

    def test_physical_jacobian_orientation_and_local_slice(self):
        xx, yy, zz = sp.symbols("xx yy zz")
        variables = (xx, yy, zz)
        ff = xx*zz - yy*yy
        for n in (1, 2, 3):
            with self.subTest(n=n):
                rr = -xx**3 - yy*ff**n
                hh = zz*ff**(2*n) + 2*xx*xx*yy*ff**n + xx**5
                field = (2*ff**n*rr, -hh-6*xx*xx*rr,
                         2*xx*ff**(n+1)-10*xx*yy*rr)
                for variable, image in zip(variables, field):
                    jac = sp.Matrix([[sp.diff(poly, var) for var in variables]
                                     for poly in (ff, hh, variable)]).det()
                    self.assertZero(jac-image)
                image_r = sum(a*sp.diff(rr, var)
                              for a, var in zip(field, variables))
                self.assertZero(image_r-ff**n*hh)

    def test_uniform_polynomial_relations_and_q_witness(self):
        xx, yy, zz = sp.symbols("xx yy zz")
        ff = xx*zz - yy*yy
        for n in (1, 2, 3):
            rr = -xx**3 - yy*ff**n
            hh = zz*ff**(2*n) + 2*xx*xx*yy*ff**n + xx**5
            ss = xx*xx*yy + zz*ff**n
            qq = hh*hh*ss - 2*rr**3*ff**(n+1) - rr*ff**(3*n+2)
            self.assertZero(xx*hh-rr*rr-ff**(2*n+1))
            self.assertZero(ff**n*ss-rr*xx*xx-hh)
            self.assertZero(ff**n*qq-rr**5-hh**3)

    def test_uniform_h_chart_polynomial_inverse(self):
        for n in (1, 2, 3, 5):
            xx, yy, zz, _ = generic_chart(n)
            qq = (r**5+h**3)/f**n
            new_y = -(r*qq+3*r**4*f**(n+1)+3*r*r*f**(3*n+2)
                      +f**(5*n+3))/h**3
            new_z = (qq*qq+f*(5*r**8+4*h**3*r**3)
                     +f**(2*n+2)*(10*r**6+2*h**3*r)
                     +10*r**4*f**(4*n+3)+5*r*r*f**(6*n+4)
                     +f**(8*n+5))/h**5
            self.assertZero(new_y-yy)
            self.assertZero(new_z-zz)
            self.assertZero(xx*zz-yy*yy-f)
            self.assertZero(zz*f**(2*n)+2*xx*xx*yy*f**n+xx**5-h)
            self.assertZero(f**n*h*sp.diff(qq, r)-5*h*r**4)

    def test_uniform_witnesses_all_residues_and_two_periods(self):
        for n in (1, 2, 3, 5):
            xx, yy, zz, ss = generic_chart(n)
            basis = (1, r, xx, r*xx, xx*xx, ss,
                     yy, r*yy, xx*yy, r*xx*yy)
            for degree in range(30):
                k, i = divmod(degree, 10)
                polynomial = sp.Poly(basis[i]*zz**k, r)
                self.assertEqual(polynomial.degree(), degree)
                sign = 1 if i < 6 else -1
                # The degree-th derivative of sign*b_i*z^k/degree!
                # is sign*(f^n*h)^degree times its leading coefficient.
                top = sign*(f**n*h)**degree*polynomial.LC()
                expected = f**(n*(degree-degree//5))*h**((degree+1)//2)
                self.assertZero(top-expected)

    def test_localized_valuation_patterns_and_periodicity(self):
        for n in (1, 2, 3, 5):
            xx = (r*r+f**(2*n+1))/h
            qq = (r**5+h**3)/f**n
            for degree in range(40):
                a, i = divmod(degree, 5)
                b, epsilon = divmod(degree, 2)
                # These are the actual normal-form monomials of the
                # h-localized and f-localized rings, respectively. Extract
                # their top derivatives from their expanded r-polynomials;
                # do not simply restate the floor/ceiling formula.
                h_poly = sp.Poly(r**i*qq**a, r)
                f_poly = sp.Poly(r**epsilon*xx**b, r)
                self.assertEqual(h_poly.degree(), degree)
                self.assertEqual(f_poly.degree(), degree)
                h_top = sp.cancel((f**n*h)**degree*h_poly.LC())
                f_top = sp.cancel((f**n*h)**degree*f_poly.LC())
                self.assertEqual(h_top.as_powers_dict().get(f, 0),
                                 n*(degree-degree//5))
                self.assertEqual(f_top.as_powers_dict().get(h, 0),
                                 (degree+1)//2)
                if degree < 12:
                    self.assertZero(
                        (f**n*h)**degree*sp.diff(h_poly.as_expr(), r, degree)
                        -math.factorial(degree)*h_top)
                    self.assertZero(
                        (f**n*h)**degree*sp.diff(f_poly.as_expr(), r, degree)
                        -math.factorial(degree)*f_top)
                shifted_h = sp.Poly(r**i*qq**(a+2), r)
                shifted_f = sp.Poly(r**epsilon*xx**(b+5), r)
                self.assertZero((f**n*h)**(degree+10)*shifted_h.LC()
                                -f**(8*n)*h**10*h_top)
                self.assertZero((f**n*h)**(degree+10)*shifted_f.LC()
                                -f**(10*n)*h**5*f_top)

    def test_geometric_bezout_with_nontrivial_Q(self):
        for n in range(1, 7):
            B, U, V = geometric_pair(n, nontrivial=True)
            self.assertZero(f**n*h*U+B*V-1)
            self.assertZero(sp.rem(sp.Poly(V-1, f), sp.Poly(f, f)).as_expr())
            self.assertEqual(sp.denom(sp.cancel((V-1)/(f*h))), 1)
        # A reduced-axis unit is not necessarily scalar mod the full plinth.
        self.assertNotEqual(trunc(f*h, 2), 0)

    def test_polynomial_unimodular_matrices_both_compositions(self):
        for n in (1, 2, 3, 4):
            B, U0, V0 = geometric_pair(n)
            g = f**n*h
            A, U, V = 1+B, U0, V0-g*U0
            self.assertZero(A*g*U+B*V-1)
            matrix = sp.Matrix([[B, -A*g], [U, V]])
            inverse = sp.Matrix([[V, A*g], [-U, B]])
            for value in matrix*inverse-sp.eye(2):
                self.assertZero(value)
            for value in inverse*matrix-sp.eye(2):
                self.assertZero(value)

    def test_affine_slice_and_invariant_numerator(self):
        for n in range(1, 6):
            B, U, V = geometric_pair(n, nontrivial=True)
            g = f**n*h
            invariant, local_slice = B*r-g*t, U*r+V*t
            self.assertZero(g*sp.diff(invariant, r)+B*sp.diff(invariant, t))
            self.assertZero(g*sp.diff(local_slice, r)
                            +B*sp.diff(local_slice, t)-1)

    def test_explicit_first_three_jets(self):
        self.assertZero(finite_jet(1, False)-1)
        self.assertZero(finite_jet(2, False)-(1-5*f*X**5))
        self.assertZero(finite_jet(3, False)
                        -(1-5*f*X**5+65*f*f*X**10))
        self.assertZero(finite_jet(2, True)-(1-5*f*X**5*(1+X**5)))
        # Independent Lagrange-inversion coefficient formula for Q=1:
        # J=(1+w*J^2)^(-5), w=f*X^5. Unlike the fixed-point test,
        # this expectation does not reuse the finite-update routine.
        for n in range(1, 8):
            expected = sum(sp.Rational((-1)**k*math.comb(11*k+4, k), 2*k+1)
                           *(f*X**5)**k for k in range(n))
            self.assertZero(finite_jet(n, False)-expected)

    def test_nontrivial_jet_fixed_point_and_contraction(self):
        for n in range(1, 6):
            jet = finite_jet(n)
            self.assertZero(jet_update(jet, n)-jet)
            self.assertZero(trunc(jet-1, 1))
            for k in range(1, n):
                difference = jet_update(jet+f**k*(1+X), n)-jet_update(jet, n)
                self.assertZero(trunc(difference, k+1))

    def test_forward_y_numerator_congruence(self):
        for n in range(1, 5):
            B = trunc(1+f*x**5*q_value(f, x**5), n)
            new_x = mul(power(B, 2, n), x, n)
            actual_rho = -mul(B, x**3, n)
            jet = compose(finite_jet(n), X, new_x, n)
            numerator = actual_rho+mul(power(new_x, 3, n), jet, n)
            self.assertZero(trunc(numerator, n))

    def test_inverse_y_numerator_congruence(self):
        for n in range(1, 5):
            jet = finite_jet(n)
            hh = mul(X**5, power(jet, 2, n), n)
            B = trunc(1+f*hh*q_value(f, hh), n)
            V = inverse_power(B, -1, n)
            old_x = mul(power(V, 2, n), X, n)
            old_r = -mul(V, mul(X**3, jet, n), n)
            self.assertZero(trunc(old_r+power(old_x, 3, n), n))
            self.assertZero(trunc(old_x-X, 1))

    def test_both_z_numerator_identities_and_gcd_premise(self):
        F, Y, Z = sp.symbols("F Y Z")
        for n in range(1, 5):
            hh = (rho*rho+f**(2*n+1))/X
            numerator = hh+2*rho*F+X*F*F
            self.assertZero(X*numerator-(rho+X*F)**2-f**(2*n+1))
            old_h = (r*r+f**(2*n+1))/x
            old_numerator = old_h+2*x*x*r+x**5
            self.assertZero(x*old_numerator-(r+x**3)**2-f**(2*n+1))
            new_rho = -X*F-Y*f**n
            new_h = X*F*F+2*Y*F*f**n+(f+Y*Y)/X*f**(2*n)
            self.assertZero(X*new_h-new_rho**2-f**(2*n+1))
        self.assertEqual(sp.gcd(X, X*Z-Y*Y), 1)
        _, factors = sp.factor_list(X*Z-Y*Y)
        self.assertEqual(len(factors), 1)
        self.assertEqual(factors[0][1], 1)

    def test_polynomial_x_formula_and_inverse_f_congruence(self):
        for n in (1, 2, 3, 4):
            B, U, V = geometric_pair(n, nontrivial=True)
            g = f**n*h
            rrho = B*r-g*t
            new_x = (B*B*x+sp.cancel((1-B*B)/h)*f**(2*n+1)
                     -2*B*f**n*r*t+f**(2*n)*h*t*t)
            self.assertEqual(sp.denom(sp.cancel(new_x)), 1)
            self.assertZero(rrho**2+f**(2*n+1)-h*new_x
                            -B*B*(r*r+f**(2*n+1)-h*x))
            self.assertZero(trunc(new_x-x, 1))
            old_r = V*rho+g*s
            W = sp.cancel((V-1)/h)*rho+f**n*s
            self.assertZero(h*W-old_r+rho)
            self.assertZero(trunc(W, 1))
            self.assertZero(h*(X+W*(old_r+rho))-old_r**2
                            -(h*X-rho*rho))

    def test_naive_uncorrected_y_is_a_negative_control(self):
        n = 2
        B = 1+f*x**5
        new_x = mul(power(B, 2, n), x, n)
        rrho = -mul(B, x**3, n)
        naive = trunc(rrho+power(new_x, 3, n), n)
        self.assertZero(naive-5*f*x**8)
        self.assertNotEqual(naive, 0)
        corrected_jet = compose(finite_jet(n, False), X, new_x, n)
        self.assertZero(trunc(rrho+mul(power(new_x, 3, n), corrected_jet, n), n))

    def test_relative_kernel_slice_elimination(self):
        old_q = sp.symbols("old_q")
        for n in (2, 3, 4):
            B, U, V = geometric_pair(n)
            g = f**n*h
            old_r = V*rho+g*s
            correction = sum(sp.binomial(5, k)*(V*rho)**(5-k)
                             *f**(n*(k-1))*h**k*s**k for k in range(1, 6))
            invariant_q = old_q-correction
            self.assertZero(f**n*correction-old_r**5+(V*rho)**5)
            # E(old_q)=5*h*old_r^4, E(s)=1, E(rho)=0.
            self.assertZero(5*h*old_r**4-sp.diff(correction, s))
            self.assertZero(f**n*invariant_q-V**5*rho**5-h**3
                            -(f**n*old_q-old_r**5-h**3))

    def test_corrected_relative_chart_maps_are_polynomial(self):
        q, Q = sp.symbols("q Q")
        for n in (2, 3, 4):
            B, _, V = geometric_pair(n)
            W = sp.cancel((1-(B*V)**5)/f**n)
            self.assertEqual(sp.denom(W), 1)
            self.assertZero(f**n*W+(B*V)**5-1)
            source_relation = f**n*q-V**5*rho**5-h**3
            target_relation = f**n*Q-rho**5-B**5*h**3
            forward = B**5*q+W*rho**5
            inverse = V**5*Q+W*h**3
            self.assertZero(target_relation.subs(Q, forward)-B**5*source_relation)
            self.assertZero(source_relation.subs(q, inverse)-V**5*target_relation)

    def test_corrected_relative_chart_both_compositions(self):
        q, Q = sp.symbols("q Q")
        for n in (2, 3, 4):
            B, _, V = geometric_pair(n)
            W = sp.cancel((1-(B*V)**5)/f**n)
            forward, inverse = B**5*q+W*rho**5, V**5*Q+W*h**3
            source_relation = f**n*q-V**5*rho**5-h**3
            target_relation = f**n*Q-rho**5-B**5*h**3
            self.assertZero(inverse.subs(Q, forward)-q+W*source_relation)
            self.assertZero(forward.subs(q, inverse)-Q+W*target_relation)


if __name__ == "__main__":
    unittest.main(verbosity=2)
