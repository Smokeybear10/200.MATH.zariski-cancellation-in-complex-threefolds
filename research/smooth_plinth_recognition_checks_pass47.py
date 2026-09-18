"""Finite exact controls, not verification of the geometric recognition inputs."""

import unittest

import sympy as sp


class SmoothPlinthRecognitionChecks(unittest.TestCase):
    def setUp(self):
        self.u, self.v, self.r, self.y, self.z = sp.symbols("u v r y z")

    def test_interpolation_and_two_sided_quotient_inverse(self):
        u, v, r, y, z = self.u, self.v, self.r, self.y, self.z
        roots = (-2, 0, 3)
        slopes = (1, 3, 2)
        intercepts = (4, -1, 5)
        p = sp.prod(u - a for a in roots)
        a0 = sp.interpolate(list(zip(roots, slopes)), u)
        b0 = sp.interpolate(list(zip(roots, intercepts)), u)
        h = u * v**2 + v**3 + u**2
        d = sp.expand(a0 * v + b0 + p * h)
        for ai, slope, intercept in zip(roots, slopes, intercepts):
            self.assertEqual(sp.expand(d.subs(u, ai) - slope * v - intercept), 0)
        recovered_a = sp.interpolate(
            [(ai, sp.diff(d, v).subs({u: ai, v: 0})) for ai in roots], u
        )
        recovered_b = sp.interpolate(
            [(ai, d.subs({u: ai, v: 0})) for ai in roots], u
        )
        q, remainder = sp.div(d - recovered_a * v - recovered_b, p, u)
        self.assertEqual(sp.expand(remainder), 0)
        self.assertEqual(sp.expand(q - h), 0)

        alpha, beta, gcd = sp.gcdex(p, a0, u)
        self.assertEqual(gcd, 1)
        matrix = sp.Matrix([[p, -a0], [beta, alpha]])
        inverse = sp.Matrix([[alpha, a0], [-beta, p]])
        self.assertEqual((matrix * inverse).applyfunc(sp.expand), sp.eye(2))
        self.assertEqual((inverse * matrix).applyfunc(sp.expand), sp.eye(2))

        w_param = r**2 + b0
        v_param = sp.expand(-beta * w_param + p * z)
        yp_param = sp.expand(alpha * w_param + a0 * z)
        y_param = yp_param + h.subs(v, v_param)
        equation = p * y - r**2 - d
        self.assertEqual(sp.expand(equation.subs({v: v_param, y: y_param}, simultaneous=True)), 0)
        z_old = beta * (y - h) + alpha * v
        self.assertEqual(sp.expand(z_old.subs({v: v_param, y: y_param}, simultaneous=True) - z), 0)

        v_back = sp.expand(v_param.subs(z, z_old))
        yp_back = sp.expand(yp_param.subs(z, z_old))
        self.assertEqual(sp.expand(v_back - v - beta * equation), 0)
        self.assertEqual(sp.expand(yp_back - (y - h) + alpha * equation), 0)
        y_back = yp_back + h.subs(v, v_back)
        # The equation is monic up to sign in r, so this is exact quotient reduction.
        self.assertEqual(sp.rem(sp.expand(y_back - y), equation, r), 0)

    def test_repeated_residue_root_and_repeated_plinth_boundary(self):
        u, v, r, y = self.u, self.v, self.r, self.y
        p = (u + 1) * (u - 2)
        d = (v - 3) ** 2 + (u - 2) * (v + u)
        equation = p * y - r**2 - d
        y_critical = sp.diff(d, u).subs({u: 2, v: 3}) / sp.diff(p, u).subs(u, 2)
        point = {u: 2, v: 3, r: 0, y: y_critical}
        for value in (equation, *(sp.diff(equation, x) for x in (u, v, r, y))):
            self.assertEqual(value.subs(point), 0)

        linear_d = 5 * v + 1 + p * (u + v**2)
        linear_equation = p * y - r**2 - linear_d
        self.assertEqual(sp.diff(linear_equation, v).subs(u, 2), -5)

        # Repeated full plinth: the same residue square need not force singularity.
        repeated_p = (u - 2) ** 2
        repeated_d = (u - 2) + (v - 3) ** 2
        repeated_equation = repeated_p * y - r**2 - repeated_d
        self.assertEqual(repeated_equation.subs({u: 2, v: 3, r: 0}), 0)
        self.assertEqual(sp.diff(repeated_equation, u).subs(u, 2), -1)
        self.assertEqual(sp.diff(repeated_p, u).subs(u, 2), 0)

    def test_squarefree_residue_and_one_finite_odd_valuation(self):
        v = self.v
        one_branch_with_square = 7 * (v - 2) * (v + 1) ** 2
        _, factors = sp.factor_list(one_branch_with_square, v)
        odd_factors = [factor for factor, exponent in factors if exponent % 2]
        self.assertEqual(odd_factors, [v - 2])
        self.assertEqual(sp.degree(sp.gcd(one_branch_with_square, sp.diff(one_branch_with_square, v)), v), 1)

        squarefree_three = (v - 2) * (v + 1) * (v - 5)
        self.assertEqual(sp.degree(sp.gcd(squarefree_three, sp.diff(squarefree_three, v)), v), 0)
        _, factors_three = sp.factor_list(squarefree_three, v)
        self.assertEqual(sum(sp.degree(factor, v) for factor, exponent in factors_three if exponent % 2), 3)

        accepted = 7 * (v - 2)
        self.assertEqual(sp.degree(accepted, v), 1)
        self.assertEqual(sp.degree(sp.gcd(accepted, sp.diff(accepted, v)), v), 0)
        # Nonzero complex constants are squares and cannot supply a degree-two field.
        self.assertEqual(sp.sqrt(sp.Integer(9)) ** 2, 9)


if __name__ == "__main__":
    unittest.main()
