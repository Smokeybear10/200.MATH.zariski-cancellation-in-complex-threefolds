#!/usr/bin/env python3
"""Independent exact checks for the quadratic research notes.

Run with /opt/anaconda3/bin/python verify_quadratic_obstructions.py.
Only SymPy and the Python standard library are imported. These tests verify
polynomial identities and stated algebraic controls, not the cited topology.
"""

import unittest

import sympy as sp


x, y, z, u, gamma = sp.symbols("x y z u gamma")
S, T, U, Z = sp.symbols("S T U Z")
a, Y, V = sp.symbols("a Y V")
v, t, w, W, J, lam = sp.symbols("v t w W J lambda")


def slice_derivative(poly):
    return sp.diff(poly, x) - u * sp.diff(poly, y)


def quotient_remainder(poly, divisor, variable):
    return sp.div(sp.expand(poly), divisor, variable)


def repeated_root_data():
    """Use a=x-1 and Y=y+u**2 in the quartic positive example."""
    h = Y + a * (u**2 + (Y - u**2) ** 3)
    inverse = S - a * (u**2 + (S - u**2) ** 3)
    original = (a + 1) * u**2 + a**2 * z + y + a * y**3
    companion, remainder = quotient_remainder(
        y + u**2 - inverse.subs(S, original), a**2, a
    )
    inverse_Y = inverse + a**2 * V
    inverse_z, inverse_remainder = quotient_remainder(
        S - h.subs(Y, inverse_Y), a**2, a
    )
    return {
        "h": h,
        "inverse": inverse,
        "original": original,
        "companion": companion,
        "remainder": remainder,
        "inverse_Y": inverse_Y,
        "inverse_y": inverse_Y - u**2,
        "inverse_z": inverse_z,
        "inverse_remainder": inverse_remainder,
    }


class QuadraticObstructionTests(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_absolute_slice(self):
        polynomial = x * u**2 + y * u + x + z**4
        self.assertEqual(sp.Poly(polynomial, x, y, z, u).total_degree(), 4)
        self.assert_zero(slice_derivative(polynomial) - 1)
        for generator in (x, y, z, u):
            self.assert_zero(slice_derivative(slice_derivative(generator)))
        self.assert_zero(slice_derivative(y + x * u))
        # D fixes u,z and lowers degree in x,y, proving local nilpotence.

    def test_absolute_coordinate_two_sided_inverse(self):
        polynomial = x * u**2 + y * u + x + z**4
        companion = y + x * u
        inverse_x = S - U * T - Z**4
        inverse_y = T - U * inverse_x
        inverse_map = {x: inverse_x, y: inverse_y, u: U, z: Z}
        forward_map = {S: polynomial, T: companion, U: u, Z: z}
        for forward, target in ((polynomial, S), (companion, T), (u, U), (z, Z)):
            self.assert_zero(forward.subs(inverse_map, simultaneous=True) - target)
        self.assert_zero(inverse_x.subs(forward_map, simultaneous=True) - x)
        self.assert_zero(inverse_y.subs(forward_map, simultaneous=True) - y)

    def test_every_residual_specialization_is_critical(self):
        residual = gamma * u**2 + y * u + gamma + z**4
        origin = {u: 0, y: 0, z: 0}
        for variable in (u, y, z):
            self.assert_zero(sp.diff(residual, variable).subs(origin))
        self.assert_zero(residual.subs(origin) - gamma)
        # gamma remains an indeterminate, so this holds for every scalar.

    def test_polynomial_square_completion_degree_five(self):
        intermediate = x * y**2
        constant = z + x**4
        polynomial = x * u**2 + intermediate * u + constant
        completed = constant - x * y**4 / 4
        self.assert_zero(
            polynomial - (x * (u + y**2 / 2) ** 2 + completed)
        )
        self.assertEqual(sp.Poly(polynomial, x, y, z, u).total_degree(), 4)
        self.assertEqual(sp.Poly(completed, x, y, z).total_degree(), 5)
        degree_five_part = sp.Add(*(
            coefficient * x**powers[0] * y**powers[1] * z**powers[2]
            for powers, coefficient in sp.Poly(completed, x, y, z).terms()
            if sum(powers) == 5
        ))
        self.assert_zero(degree_five_part + x * y**4 / 4)

    def test_nondivisible_square_completion_is_laurent_only(self):
        intermediate = y
        constant = x + z**4
        polynomial = x * u**2 + intermediate * u + constant
        shifted = u + intermediate / (2 * x)
        completed = constant - intermediate**2 / (4 * x)
        self.assert_zero(polynomial - (x * shifted**2 + completed))
        self.assertEqual(intermediate.subs(x, 0), y)
        with self.assertRaises(sp.PolynomialError):
            sp.Poly(shifted, x, y, z, u)
        with self.assertRaises(sp.PolynomialError):
            sp.Poly(completed, x, y, z)
        self.assert_zero(sp.fraction(sp.cancel(completed))[1] - 4 * x)

    def test_pure_x_quotient_two_sided_inverse(self):
        remainder = x * v**2 + t * v + t**3
        G = v + x * remainder
        forward_W = w + remainder
        forward_J = x * w + G
        inverse_v = J - x * W
        inverse_w = W - remainder.subs(v, inverse_v)
        inverse_map = {v: inverse_v, w: inverse_w}
        forward_map = {J: forward_J, W: forward_W}
        self.assert_zero(forward_J.subs(inverse_map, simultaneous=True) - J)
        self.assert_zero(forward_W.subs(inverse_map, simultaneous=True) - W)
        self.assert_zero(inverse_v.subs(forward_map, simultaneous=True) - v)
        self.assert_zero(inverse_w.subs(forward_map, simultaneous=True) - w)

    def test_pure_x_cyclic_cover_equation(self):
        remainder = x * v**2 + t * v + t**3
        G = v + x * remainder
        inverse_v = lam - x * W
        branch_polynomial = W - remainder.subs(v, inverse_v)
        for exponent in (2, 3, 5):
            fiber_equation = x * u**exponent + G - lam
            self.assert_zero(
                fiber_equation.subs(v, inverse_v)
                - x * (u**exponent - branch_polynomial)
            )
        # The covering equation itself also retains w=u**n; no division
        # by x at x=0 is used to infer an isomorphism from this identity.

    def test_positive_repeated_root_finite_inverse_congruences(self):
        data = repeated_root_data()
        h, inverse = data["h"], data["inverse"]
        for composition in (h.subs(Y, inverse) - S, inverse.subs(S, h) - Y):
            _, remainder = quotient_remainder(composition, a**2, a)
            self.assert_zero(remainder)
        self.assert_zero(data["remainder"])
        self.assert_zero(data["inverse_remainder"])
        self.assert_zero(data["original"].subs(a, 0) - (y + u**2))

    def test_positive_repeated_root_coordinate_inverse(self):
        data = repeated_root_data()
        polynomial = data["original"]
        companion = data["companion"]
        inverse_y = data["inverse_y"]
        inverse_z = data["inverse_z"]
        inverse_map = {y: inverse_y, z: inverse_z}
        forward_map = {S: polynomial, V: companion}
        self.assert_zero(polynomial.subs(inverse_map, simultaneous=True) - S)
        self.assert_zero(companion.subs(inverse_map, simultaneous=True) - V)
        self.assert_zero(inverse_y.subs(forward_map, simultaneous=True) - y)
        self.assert_zero(inverse_z.subs(forward_map, simultaneous=True) - z)

    def test_degree_one_separated_sum_control(self):
        separated_s = sp.Symbol("s")
        G = z**2 + x * y
        polynomial = separated_s + G
        inverse_s = S - G
        self.assert_zero(polynomial.subs(separated_s, inverse_s) - S)
        self.assert_zero(inverse_s.subs(S, polynomial) - separated_s)
        self.assert_zero(sp.diff(polynomial, separated_s) - 1)
        for variable in (x, y, z):
            self.assert_zero(sp.diff(G, variable).subs({x: 0, y: 0, z: 0}))
        # Thus degree-one separated sums do not force G to be critical-free.

    def test_smooth_pure_x_control_with_disconnected_fixed_set(self):
        polynomial = x*u**2+y+x**2*y**2
        self.assertEqual(sp.Poly(polynomial, x, y, u).total_degree(), 4)
        self.assert_zero(polynomial.subs(x, 0)-y)
        gradient = [sp.diff(polynomial, variable) for variable in (x, y, u)]
        basis = sp.groebner(gradient, x, y, u, domain=sp.QQ)
        self.assertEqual(basis.reduce(sp.Integer(1))[1], 0)
        fixed_equation = polynomial.subs(u, 0)
        self.assert_zero(fixed_equation-y*(1+x**2*y))
        self.assert_zero((1+x**2*y)-x**2*y-1)
        # The two nonempty components are disjoint. Smith theory,
        # not this algebraic check alone, excludes a stable coordinate.
        self.assert_zero((1+x**2*y).subs({x: t, y: -1/t**2},
                                       simultaneous=True))

    def test_separated_binomial_positive_inverse(self):
        separated_s, A = sp.symbols("s A")
        companion = x+y**2
        coefficient = companion**3+2
        polynomial = separated_s**4+separated_s+y+coefficient*z**3
        inverse_y = S-separated_s**4-separated_s-(A**3+2)*z**3
        inverse_x = A-inverse_y**2
        inverse_map = {x: inverse_x, y: inverse_y}
        forward_map = {S: polynomial, A: companion}
        self.assert_zero(polynomial.subs(inverse_map, simultaneous=True)-S)
        self.assert_zero(companion.subs(inverse_map, simultaneous=True)-A)
        self.assert_zero(inverse_x.subs(forward_map, simultaneous=True)-x)
        self.assert_zero(inverse_y.subs(forward_map, simultaneous=True)-y)

    def test_linear_binomial_pair_criterion_does_not_extend(self):
        G = x*z+y+x*y**2
        companion = z+y**2
        inverse_y = S-x*T
        inverse_z = T-inverse_y**2
        self.assert_zero(G.subs({y: inverse_y, z: inverse_z},
                               simultaneous=True)-S)
        self.assert_zero(companion.subs({y: inverse_y, z: inverse_z},
                                       simultaneous=True)-T)
        self.assert_zero(inverse_y.subs({S: G, T: companion},
                                       simultaneous=True)-y)
        self.assert_zero(inverse_z.subs({S: G, T: companion},
                                       simultaneous=True)-z)
        # For nonzero lambda, the plane remainder's fiber is C*,
        # parametrized by y=t, x=(lambda-t)/t^2.
        self.assert_zero((y+x*y**2).subs(
            {y: t, x: (lam-t)/t**2}, simultaneous=True)-lam)
        self.assert_zero(y*(1+x*y)-(y+x*y**2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
