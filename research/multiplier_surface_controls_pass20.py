#!/usr/bin/env python3
"""Finite exact controls for multiplier poles and the nodal surface.

The general algebraic and geometric arguments are written separately.
These checks import no solver and do not certify a universal theorem.
"""
import itertools
import unittest

import sympy as sp

f, x, h, r, t, T, k = sp.symbols("f x h r t T k")


def trunc(expr, order):
    value = sp.Poly(sp.expand(expr), f)
    return sp.Add(*(coefficient * f**powers[0]
                    for powers, coefficient in value.terms()
                    if powers[0] < order))


def dd_power(left, right, degree):
    return sum(left**(degree - 1 - j) * right**j for j in range(degree))


class MultiplierSurfaceControls(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.cancel(value), 0)

    def test_transformed_monic_relation(self):
        a, s, q = sp.symbols("a s q")
        for degree in (2, 3, 4):
            old_K = r**degree + f**(degree + 1)
            new_r = a*r + h*q
            new_k = a**degree*x + q*dd_power(new_r, a*r, degree)
            new_relation = h*new_k - new_r**degree - a**degree*f**(degree+1)
            self.assertZero(new_relation - a**degree*(h*x-old_K))

    def test_physical_derivative_and_primitivity_controls(self):
        y, z = sp.symbols("y z")
        physical_f = x*z-y*y
        variables = (x, y, z)
        for n in (1, 2):
            rr = x*x+y*physical_f**n
            hh = sp.cancel((rr*rr+physical_f**(2*n+1))/x)
            for aa in (physical_f, physical_f-1):
                next_r = sp.expand(aa*rr+hh*hh)
                next_k = sp.expand(aa*aa*x+2*aa*hh*rr+hh**3)
                grad_f = [sp.diff(physical_f, v) for v in variables]
                grad_k = [sp.diff(next_k, v) for v in variables]
                coefficients = list(sp.Matrix(grad_f).cross(sp.Matrix(grad_k)))
                derivative = sum(c*sp.diff(next_r, v)
                                 for c, v in zip(coefficients, variables))
                self.assertZero(derivative-aa*physical_f**n*next_k)
                self.assertEqual(sp.gcd_list(coefficients), 1)

    def test_exact_uncorrected_pole_leading_coefficient(self):
        for degree, e, ell in ((2, 2, 1), (2, 3, 1), (2, 3, 2), (3, 2, 1)):
            q = h + 1
            order, N = ell+1, e+1
            next_r = f**e*r + h*q
            next_k = f**(e*degree)*x + q*dd_power(next_r, f**e*r, degree)
            rho = trunc((1+f**ell*next_k)*next_r-f**N*next_k*t, order)
            hh = trunc(h+(f**ell*next_r-f**N*t)
                       *dd_power(rho, next_r, degree), order)
            numerator = trunc(rho-hh*(hh+1), order)
            expected = f**ell*h**degree*q**degree*((1-degree)*q-degree*h)
            self.assertZero(numerator-expected)
            self.assertNotEqual(sp.expand(expected/f**ell), 0)

    def test_first_reverse_coordinate_positive_threshold(self):
        for e in (1, 2, 3):
            for ell in (e, e+1):
                order, N = e, e+1
                next_r = f**e*r+h*h
                next_k = f**(2*e)*x+2*f**e*h*r+h**3
                rho = trunc((1+f**ell*next_k)*next_r-f**N*next_k*t, order)
                hh = trunc(h+(f**ell*next_r-f**N*t)*(rho+next_r), order)
                self.assertZero(trunc(rho-hh*hh, order))

    def test_geometric_series_really_supplies_slice(self):
        for N in (2, 3, 4):
            for ell in (1, 2):
                displacement = f**ell*k*(1+k)
                B = 1+displacement
                L = sum((-displacement)**j for j in range(N))
                U = sp.cancel((1-B*L)/(f**N*k))
                self.assertEqual(sp.denom(U), 1)
                self.assertZero(U*f**N*k+L*B-1)

    def test_euler_operator_has_no_nonzero_polynomial_kernel(self):
        for degree in range(2, 7):
            for exponent in range(9):
                q = h**exponent
                actual = (1-degree)*q-degree*h*sp.diff(q, h)
                self.assertZero(actual-(1-degree-degree*exponent)*q)
                self.assertNotEqual(actual, 0)

    def test_nodal_curve_identity(self):
        w = sp.symbols("w")
        u, v = w**4-2, (w**4-3)*w*w
        self.assertZero(v*v-u**3+3*u-2)
        self.assertZero((w**4-3)*(w**4+3)-(w**8-9))

    def test_conductor_incidence_and_integral_cokernel(self):
        matrix = sp.Matrix([[1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 0]])
        minors = [matrix[list(rows), :].det()
                  for rows in itertools.combinations(range(4), 3)]
        self.assertEqual(matrix.rank(), 3)
        self.assertEqual(minors, [1, -1, -1, 1])
        self.assertEqual(sp.gcd_list(minors), 1)

    def test_scaled_gluing_residues_cancel(self):
        a = sp.symbols("a", nonzero=True)
        roots = (a, -a, sp.I*a, -sp.I*a)
        for left, right in ((0, 2), (0, 3), (1, 2)):
            residue_left = 1/(4*roots[left]**2)
            residue_right = 1/(4*roots[right]**2)
            self.assertZero(residue_left+residue_right)
        # Unscaled residues provide a negative control.
        self.assertNotEqual(sp.simplify(1/(4*a**3)+1/(4*(sp.I*a)**3)), 0)

    def test_node_fiber_is_transverse_on_each_pair(self):
        a = sp.symbols("a", nonzero=True)
        roots = (a, -a, sp.I*a, -sp.I*a)
        for left, right in ((0, 2), (0, 3), (1, 2)):
            self.assertNotEqual(sp.simplify(roots[right]**2-roots[left]**2), 0)

    def test_local_primitive_ramification_model(self):
        s, w, tau = sp.symbols("s w tau")
        invariant = w*w+s*tau
        derivative = s*sp.diff(invariant, w)-2*w*sp.diff(invariant, tau)
        self.assertZero(derivative)
        self.assertEqual(sp.gcd(s, 2*w), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
