"""Finite exact controls for double-branch97, not a geometric proof checker."""

import unittest

import sympy as sp


class DoubleBranchControls(unittest.TestCase):
    def test_weighted_coefficient_and_tangent_boundary(self):
        x, y, c, t, nu = sp.symbols("x y c t nu", nonzero=True)
        a = sp.Function("a")(c)

        def leading(expr):
            return sp.expand(
                (-nu*x - nu*sp.diff(a, c)*y**2)*sp.diff(expr, y)
                + 2*nu*a*y*sp.diff(expr, c)
            )

        cube = leading(leading(leading(y)))
        coefficient = sp.Poly(cube, x, y).coeff_monomial(x**2)
        self.assertEqual(sp.simplify(coefficient + 2*nu**3*sp.diff(a, c)), 0)
        self.assertEqual(leading(y).subs(a, 3).doit(), -nu*x)

        # Exact relation after adjoining the specified formal square roots.
        theta, s = sp.symbols("theta s")
        relations = [theta**2-(1-c*t), s**2-(1+t), y**2-t**2*(1-c*t)]
        groebner = sp.groebner(relations, s, theta, y, t, c)
        cleared_relation = s**2*y**2 - t**2*(1+t)*theta**2
        self.assertEqual(groebner.reduce(cleared_relation)[1], 0)
        for sign in (-1, 1):
            self.assertEqual(sp.cancel((s*y/theta).subs(y, sign*t*theta)), sign*t*s)

        # Replacing the formal unit by 1 is not a valid exact identity.
        incorrect = s**2*y**2 - t**2*(1+t)
        self.assertNotEqual(groebner.reduce(incorrect)[1], 0)

        # Conductor-scaled map to a finite cover of the original cusp.
        self.assertEqual(sp.expand(t**6*(1+t) - ((t**3)**2+t**3*(t**2)**2)), 0)
        w = sp.symbols("w")
        base_t = w**2-1
        base_x, base_z, base_k = base_t**3, base_t**2, base_t**3*w
        self.assertEqual(sp.expand(base_x**2-base_z**3), 0)
        self.assertEqual(sp.expand(base_k**2-base_x**2-base_x*base_z**2), 0)
        self.assertEqual([base_k.subs(w, sign) for sign in (-1, 1)], [0, 0])
        # Each n>=2 is either even or 3 plus an even nonnegative integer.
        for exponent in range(2, 16):
            self.assertTrue(exponent % 2 == 0 or (exponent >= 3 and (exponent-3) % 2 == 0))

        # Formal invariance after y=theta*Y, not global rational recovery.
        capital_y = sp.symbols("capital_y")
        self.assertEqual(sp.rem(t**3-t*capital_y**2, capital_y**2-t**2, capital_y), 0)
        rational_c = (t**2-y**2)/t**3
        self.assertEqual(sp.cancel(t**3*sp.diff(rational_c, y)), -2*y)
        nonsquare = t**6*(1+t)
        self.assertEqual(nonsquare.subs(t, -1), 0)
        self.assertNotEqual(sp.diff(nonsquare, t).subs(t, -1), 0)

        # In these finite perturbed prepared quadratics, coefficients above
        # the Newton edge cannot change its leading valuation or residual.
        v = sp.symbols("v")
        for n in range(1, 9):
            with self.subTest(multiplicity=n):
                vertical = y**2 + t**n*(1+t*c)*y - t**n + t**(n+1)*c
                nonvertical = y**2 + t**n*(1+t*c)*y - (7-5*c)*t**n + t**(n+1)*c
                if n % 2 == 0:
                    vertical_scaled = sp.cancel(vertical.subs(y, t**(n//2)*v)/t**n)
                    nonvertical_scaled = sp.cancel(nonvertical.subs(y, t**(n//2)*v)/t**n)
                    self.assertEqual(sp.expand(vertical_scaled).subs(t, 0), v**2-1)
                    self.assertEqual(sp.expand(nonvertical_scaled).subs(t, 0), v**2-(7-5*c))
                else:
                    # Twice an integer cannot equal this required root order.
                    self.assertEqual(n % 2, 1)

        # The residual rational function has a simple zero, not square order.
        residual = 7-5*c
        self.assertEqual(residual.subs(c, sp.Rational(7, 5)), 0)
        self.assertNotEqual(sp.diff(residual, c).subs(c, sp.Rational(7, 5)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
