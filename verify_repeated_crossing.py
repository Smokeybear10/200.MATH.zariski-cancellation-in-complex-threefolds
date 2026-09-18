#!/usr/bin/env python3
"""Exact checks for pass 08, independent of every research solver.

These check polynomial identities and integer maps. They do not implement
algebraic topology, certify novelty, or prove general cancellation.
"""

import unittest

import sympy as sp

x, y, z, u, S, V, t, s, w = sp.symbols("x y z u S V t s w")
GENS = (x, y, z, u, S, V, t, s, w)


def exact_quotient(numerator, denominator):
    quotient, remainder = sp.div(sp.expand(numerator), denominator, *GENS)
    if sp.expand(remainder) != 0:
        raise ValueError("Not divisible in the polynomial ring")
    return sp.expand(quotient)


def reduced_mod_monomial(expr, a, b):
    return sp.div(sp.expand(expr), x**a * y**b, *GENS)[1]


def nilpotent_inverse(a, b, coefficient, D, R):
    """Invert coefficient*z+D+xy*R in QQ[x,y]/(x^a*y^b)[z]."""
    if type(a) is not int or type(b) is not int or min(a, b) < 1:
        raise ValueError("Exponents must be positive integers")
    coefficient = sp.sympify(coefficient)
    if coefficient.is_Rational is not True or coefficient == 0:
        raise ValueError("The z coefficient must be a nonzero rational constant")
    D, R = sp.sympify(D), sp.sympify(R)
    sp.Poly(D, x, y, domain=sp.QQ)
    sp.Poly(R, x, y, z, domain=sp.QQ)
    I = (S - D) / coefficient
    for _ in range(max(a, b) - 1):
        I = reduced_mod_monomial(
            (S - D - x * y * R.subs(z, I)) / coefficient, a, b
        )
    return sp.expand(I)


def coordinate_completion(a, b, coefficient, D, R):
    P = x**a * y**b
    H = coefficient * z + D + x * y * R
    I = nilpotent_inverse(a, b, coefficient, D, R)
    F = P * u + H
    forward_V = exact_quotient(z - I.subs(S, F), P)
    inverse_z = I + P * V
    inverse_u = exact_quotient(S - H.subs(z, inverse_z), P)
    return F, forward_V, inverse_z, inverse_u


class RepeatedCrossingChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def check_inverse(self, a, b, coefficient, D, R):
        F, forward_V, inverse_z, inverse_u = coordinate_completion(
            a, b, coefficient, D, R
        )
        for expression in (F, forward_V, inverse_z, inverse_u):
            sp.Poly(expression, *GENS, domain=sp.QQ)
        backward = {z: inverse_z, u: inverse_u}
        forward = {S: F, V: forward_V}
        self.assert_zero(F.subs(backward, simultaneous=True) - S)
        self.assert_zero(forward_V.subs(backward, simultaneous=True) - V)
        self.assert_zero(inverse_z.subs(forward, simultaneous=True) - z)
        self.assert_zero(inverse_u.subs(forward, simultaneous=True) - u)

    def test_squarefree_inverse(self):
        self.check_inverse(1, 1, sp.Rational(3, 2), x**2 + y, z**2 + x)

    def test_repeated_y_nonlinear_inverse(self):
        self.check_inverse(1, 2, sp.Rational(-2), x + y**2, z**2 + x*z)

    def test_repeated_x_nonlinear_inverse(self):
        self.check_inverse(2, 1, sp.Rational(1, 3), x**2 + y, z**2 + y)

    def test_higher_exponents(self):
        for a, b in ((2, 3), (3, 2), (3, 3), (1, 4)):
            with self.subTest(a=a, b=b):
                self.check_inverse(a, b, sp.Rational(2), x+y, z+x)

    def test_two_sided_modular_inverse(self):
        for a, b in ((1, 1), (1, 2), (2, 1), (2, 3)):
            D, R = x+y, z**2+x
            I = nilpotent_inverse(a, b, 1, D, R)
            H = z+D+x*y*R
            self.assert_zero(reduced_mod_monomial(H.subs(z, I)-S, a, b))
            self.assert_zero(reduced_mod_monomial(I.subs(S, H)-z, a, b))

    def test_reduced_inverse_alone_is_insufficient(self):
        H = z+x*y*z**2
        self.assertNotEqual(reduced_mod_monomial(H.subs(z, S)-S, 1, 2), 0)
        I = nilpotent_inverse(1, 2, 1, 0, z**2)
        self.assert_zero(I-(S-x*y*S**2))

    def test_invalid_inputs_rejected(self):
        for a, b, coefficient in ((0, 1, 1), (1, -1, 1), (1, 2, 0),
                                  (1, 2, x), (1.0, 2, 1)):
            with self.subTest(a=a, b=b, coefficient=coefficient):
                with self.assertRaises(ValueError):
                    nilpotent_inverse(a, b, coefficient, 0, z)

    def test_venereau_scope_boundary(self):
        F = x*y**2*u+y+x**2*z+x*y*z**2
        self.assertEqual(sp.Poly(F, x, y, z, u).total_degree(), 4)
        self.assert_zero(F.subs({x: 0, y: 0}))
        # The nonconstant-intersection theorem has no conclusion for this F.
        self.assertEqual(sp.diff(F.subs({x: 0, y: 0}), z), 0)

    def test_constant_axis_laurent_localization(self):
        # These are coordinates over QQ[x,x^-1], not claimed global mates.
        local_gens = (y,z,u,S,V)
        def local_div(numerator, denominator):
            num = sp.Poly(sp.cancel(numerator), *local_gens,
                          domain=sp.QQ.frac_field(x))
            den = sp.Poly(denominator, *local_gens,
                          domain=sp.QQ.frac_field(x))
            quotient, remainder = num.div(den)
            self.assertEqual(remainder.as_expr(), 0)
            return quotient.as_expr()
        for r, exponent, k, R in ((1,2,2,z**2), (2,3,4,z+x)):
            P = x**r*y**exponent
            H = y+x**k*z+x*y*R
            F = P*u+H
            I = (S-y)/x**k
            for _ in range(exponent-1):
                value = sp.cancel((S-y-x*y*R.subs(z,I))/x**k)
                poly = sp.Poly(value, *local_gens, domain=sp.QQ.frac_field(x))
                I = poly.rem(sp.Poly(y**exponent, *local_gens,
                                     domain=sp.QQ.frac_field(x))).as_expr()
            forward_V = local_div(z-I.subs(S,F),P)
            inverse_z = I+P*V
            inverse_u = local_div(S-H.subs(z,inverse_z),P)
            for expression, expected in ((F,S),(forward_V,V)):
                self.assertEqual(sp.cancel(expression.subs(
                    {z:inverse_z,u:inverse_u}, simultaneous=True)-expected),0)
            for expression, expected in ((inverse_z,z),(inverse_u,u)):
                self.assertEqual(sp.cancel(expression.subs(
                    {S:F,V:forward_V}, simultaneous=True)-expected),0)
            self.assert_zero(F.subs(x,0)-y)

    def test_jacobian_locus_keeps_nonreduced_leading_form(self):
        cubic = y**3
        for variable in (x,y,z,u):
            self.assert_zero(sp.diff(cubic,variable).subs(y,0))
        self.assertEqual(sp.diff(y,y),1)
        # Thus the Jacobian locus differs from Sing of the reduced plane.

    def test_torsion_family_critical_locus_and_parameterization(self):
        for a, b, q in ((1, 2, 2), (2, 3, 3), (1, 4, 5)):
            F = x**a*y**b*u+y+x*z**q
            self.assert_zero(sp.diff(F, u)-x**a*y**b)
            self.assert_zero(sp.diff(F, y).subs(x, 0)-1)
            self.assert_zero(sp.diff(F, y).subs(y, 0)-1)
            self.assert_zero(F.subs({x: S/z**q, y: 0})-S)
            # For S nonzero, z is the C* parameter of the closed stratum.
            self.assert_zero(z*sp.diff(S/z**q, z)/(S/z**q)+q)

    def test_integral_residue_map_is_not_a_rational_test(self):
        for q in range(2, 13):
            residue_map = sp.Matrix([[q]])
            self.assertEqual(residue_map.rank(), 1)
            self.assertEqual(abs(residue_map.det()), q)
            self.assertNotIn(residue_map.det(), (-1, 1))
        # Cokernel of multiplication by q on Z is Z/q; over Q it is zero.

    def test_equivariant_slice_averaging_counterexample(self):
        a = (1+t**2)*s-t*y
        b = -t*s+y
        def D(poly):
            return sp.expand(sp.diff(poly, t)+(-t*s+y)*sp.diff(poly, s)
                             +((1-t**2)*s+t*y)*sp.diff(poly, y))
        self.assert_zero(D(a))
        self.assert_zero(D(b))
        self.assert_zero(a+t*b-s)
        self.assert_zero(t*a+(1+t**2)*b-y)
        def E(poly):
            return sp.expand(sp.diff(poly, t)-t*s*sp.diff(poly, s)
                             +t*y*sp.diff(poly, y))
        iterate = y
        for n in range(1, 13):
            iterate = E(iterate)
            coefficient = sp.Poly(exact_quotient(iterate, y), t)
            self.assertEqual(coefficient.degree(), n)
            self.assertEqual(coefficient.LC(), 1)

    def test_square_completion_degree_six_control(self):
        F = u**2+x**3*u+y+x**4
        G = y+x**4-x**6/4
        self.assert_zero(F-(u+x**3/2)**2-G)
        self.assertEqual(sp.Poly(F, x,y,u).total_degree(), 4)
        self.assertEqual(sp.Poly(G, x,y).total_degree(), 6)

    def test_russell_saturated_pair_algebra(self):
        relation = x**2*y+x+z**2+t**3
        def D1(poly):
            return sp.expand(2*z*sp.diff(poly, y)-x**2*sp.diff(poly, z))
        def D2(poly):
            return sp.expand(3*t**2*sp.diff(poly, y)-x**2*sp.diff(poly, t))
        self.assert_zero(D1(relation))
        self.assert_zero(D2(relation))
        for generator in (x,y,z,t):
            self.assert_zero(D1(D2(generator))-D2(D1(generator)))
        A, B = sp.symbols("A B")
        remainder = sp.rem(2*A*z+3*B*t**2, z**2+t**3, z)
        self.assertEqual(sp.Poly(remainder, z,t).coeffs(), [2*A,3*B])


if __name__ == "__main__":
    unittest.main(verbosity=2)
