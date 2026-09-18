#!/usr/bin/env python3
"""Independent exact controls for pass-19 global-bridge arguments.

Only finite polynomial identities are tested. The all-base image-ideal
and relative-isomorphism statements depend on their separate written
proofs, not on this parameter grid. No research solver is imported.
"""

import math
import unittest

import sympy as sp


x, y, z, w, h, q, b, r, T, H = sp.symbols("x y z w h q b r T H")


def binomial_polynomial(variable, degree):
    return sp.prod(variable-j for j in range(degree))/sp.factorial(degree)


def order_at_x(value):
    polynomial = sp.Poly(sp.expand(value), x)
    if polynomial.is_zero:
        return math.inf
    return min(powers[0] for powers, coefficient in polynomial.terms()
               if coefficient != 0)


class GlobalBridgeChecks(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.cancel(value), 0)

    def test_affine_iterate_displacement(self):
        current = r
        for exponent in range(1, 9):
            current = sp.expand((1+q)*current+b)
            geometric = sum((1+q)**j for j in range(exponent))
            self.assertZero(current-r-(q*r+b)*geometric)

    def test_geometric_sum_finite_truncation(self):
        for bound in range(1, 7):
            truncation = sum(binomial_polynomial(T, j)*q**(j-1)
                             for j in range(1, bound+2))
            for integer in range(bound+5):
                geometric = sum((1+q)**j for j in range(integer))
                error = sp.expand(truncation.subs(T, integer)-geometric)
                self.assertZero(sp.rem(error, q**(bound+1), q))
            self.assertZero(truncation.subs(q, 0)-T)

    def test_truncation_linear_coefficient_is_a_unit(self):
        for bound in range(1, 9):
            truncation = sum(binomial_polynomial(T, j)*q**(j-1)
                             for j in range(1, bound+2))
            derivative = sp.diff(truncation, T).subs(T, 0)
            expected = sum(sp.Rational((-1)**(j-1), j)*q**(j-1)
                           for j in range(1, bound+2))
            self.assertZero(derivative-expected)
            self.assertZero(derivative.subs(q, 0)-1)

    def test_near_identity_affine_pole_threshold(self):
        for multiplicity in range(1, 5):
            for scale_order in range(1, multiplicity+2):
                for shift_order in range(multiplicity+2):
                    lam = 1+x**scale_order
                    shift = x**shift_order
                    numerator = sp.expand((lam*y+shift)**2-y*y)
                    polynomial = order_at_x(numerator) >= multiplicity
                    self.assertEqual(polynomial,
                                     scale_order >= multiplicity
                                     and shift_order >= multiplicity)
                    image_z = z+numerator/x**multiplicity
                    self.assertZero(x**multiplicity*image_z
                                    -(lam*y+shift)**2
                                    -(x**multiplicity*z-y*y))

    def test_radical_multiplier_hypothesis_is_essential(self):
        # Reflection is an automorphism despite lambda-1 not dividing p.
        for multiplicity in range(1, 6):
            self.assertZero(x**multiplicity*z-(-y)**2
                            -(x**multiplicity*z-y*y))
            self.assertLess(order_at_x(sp.Integer(-2)), multiplicity)

    def test_residue_linear_independence_parity_control(self):
        for degree in range(1, 7):
            invariant_residue = -y*y
            a = (1+h**degree).subs(h, invariant_residue)
            shift = (h+h**(degree+1)).subs(h, invariant_residue)
            combined = sp.Poly(sp.expand(a*y+shift), y)
            odd = sum(coefficient*y**power[0]
                      for power, coefficient in combined.terms()
                      if power[0] % 2)
            even = sum(coefficient*y**power[0]
                       for power, coefficient in combined.terms()
                       if power[0] % 2 == 0)
            self.assertZero(odd-a*y)
            self.assertZero(even-shift)
            self.assertNotEqual(odd, 0)

    def test_full_congruence_relative_inverse(self):
        for multiplicity in range(1, 5):
            p = x**multiplicity
            for scalar in (sp.Integer(-1), sp.Integer(1), sp.Integer(2)):
                V = scalar+p*H
                correction = 2*scalar*H+p*H*H
                image_y = scalar*w
                image_z = z-correction*w*w
                self.assertZero(p*image_z-image_y**2-(p*z-V*V*w*w))
                inverse_w = y/scalar
                inverse_z = z+correction*y*y/scalar**2
                self.assertZero(image_y.subs(w, inverse_w)-y)
                self.assertZero(image_z.subs({w: inverse_w, z: inverse_z},
                                            simultaneous=True)-z)
                self.assertZero(inverse_z.subs({y: image_y, z: image_z},
                                              simultaneous=True)-z)

    def test_finite_power_cannot_hide_nilpotent_order(self):
        for multiplicity in range(2, 7):
            for order in range(1, multiplicity+1):
                for exponent in range(1, 6):
                    difference = sp.expand((1+x**order)**exponent-1)
                    self.assertEqual(order_at_x(difference), order)

    def test_disconnected_root_of_unity_positive_control(self):
        p = x*(x-1)
        V = 2*x-1
        self.assertZero(V*V-1-4*p)
        self.assertZero(p*(z-4*w*w)-w*w-(p*z-V*V*w*w))
        self.assertEqual(V.subs(x, 0), -1)
        self.assertEqual(V.subs(x, 1), 1)

    def test_old_coordinate_fiber_presentation(self):
        f = x*z-y*y
        local_slice = x*x+y*f*f
        invariant = z*f**4+2*x*y*f*f+x**3
        self.assertZero(x*invariant-local_slice**2-f**5)
        p = f*f*invariant
        V = 1+f*invariant
        self.assertZero(p*invariant+(1-f*invariant)*V-1)
        self.assertZero(f.subs(x, 0)+y*y)
        self.assertZero(local_slice.subs(x, 0)-y**5)
        self.assertZero(invariant.subs(x, 0)-y**8*z)
        self.assertZero(V.subs(x, 0)-(1-y**10*z))
        # The numerator identity for the nonlinear replacement coordinate,
        # with r=V*w, is checked in independent f,h,w.
        ff = sp.Symbol("f")
        VV = 1+ff*h
        rr = VV*w
        xx = (rr*rr+ff**5)/h
        self.assertZero(xx-ff*w*(w+rr)-(w*w+ff**5)/h)

    def test_fiber_unit_certificate(self):
        J = 1-y**10*z
        relation = J*w-y**5
        self.assertZero(J*(1+y**5*z*w)-1-y**5*z*relation)
        self.assertNotEqual(J, 1)
        self.assertZero(relation.subs(w, y**5/J))

    def test_leading_image_ideals_in_triangular_modifications(self):
        for multiplicity in range(1, 4):
            p, V = x**multiplicity, 1+x

            def derivation(value, modified):
                if modified:
                    return sp.expand(p*sp.diff(value, w)
                                     +2*V*V*w*sp.diff(value, z))
                return sp.expand(p*sp.diff(value, y)+2*y*sp.diff(value, z))

            for degree in range(1, 7):
                for modified in (False, True):
                    variable = w if modified else y
                    coefficients = []
                    for z_power in range(degree//2+1):
                        value = variable**(degree-2*z_power)*z**z_power
                        for _ in range(degree):
                            value = derivation(value, modified)
                        coefficients.append(sp.expand(value/sp.factorial(degree)))
                    gcd = sp.Poly(coefficients[0], x)
                    for coefficient in coefficients[1:]:
                        gcd = sp.gcd(gcd, sp.Poly(coefficient, x))
                    self.assertZero(gcd.monic().as_expr()
                                    -x**(multiplicity*((degree+1)//2)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
