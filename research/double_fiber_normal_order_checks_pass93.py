"""Symbolic two-jet control, not a verifier for the geometric theorem."""

import unittest

import sympy as sp


class DoubleFiberNormalOrderChecks(unittest.TestCase):
    def test_third_derivative_identity_and_wrong_coefficient(self):
        x, y, c = sp.symbols("x y c")
        names = "gamma delta lam A B C U V W a b d e"
        funcs = {name: sp.Function(name)(c) for name in names.split()}
        gamma, delta, lam = (funcs[name] for name in ("gamma", "delta", "lam"))
        ny = gamma*x + funcs["A"]*x**2 + funcs["B"]*x*y + funcs["C"]*y**2
        nc = delta*x + lam*y + funcs["U"]*x**2 + funcs["V"]*x*y + funcs["W"]*y**2

        def truncate(expr):
            poly = sp.Poly(sp.expand(expr), x, y)
            return sp.Add(*(co*x**i*y**j for (i, j), co in poly.terms() if i+j < 3))

        def deriv(expr):
            return truncate(ny*sp.diff(expr, y) + nc*sp.diff(expr, c))

        def cube(expr):
            return deriv(deriv(deriv(expr)))

        for monomial in (x*x, x*y, y*y):
            self.assertEqual(cube(monomial), 0)
        self.assertEqual(cube(funcs["a"]*x), 0)
        expected_y = gamma*(2*funcs["C"]*gamma + lam*sp.diff(gamma, c))*x*x
        self.assertEqual(sp.simplify(cube(y)-expected_y), 0)
        f = funcs["a"]*x + funcs["b"]*y
        g = funcs["d"]*x + funcs["e"]*y
        expected_f = funcs["b"]*cube(y) + 3*sp.diff(funcs["b"], c)*lam*gamma**2*x*x
        self.assertEqual(sp.simplify(cube(f)-expected_f), 0)
        wronskian = funcs["e"]*sp.diff(funcs["b"], c)-funcs["b"]*sp.diff(funcs["e"], c)
        self.assertEqual(sp.simplify(funcs["e"]*cube(f)-funcs["b"]*cube(g)
                                     -3*lam*gamma**2*wronskian*x*x), 0)
        wrong = funcs["b"]*cube(y) + 2*sp.diff(funcs["b"], c)*lam*gamma**2*x*x
        self.assertNotEqual(sp.simplify(cube(f)-wrong), 0)
        specialized = sp.simplify((cube(f)-wrong).subs({funcs["b"]: c,
                                                       lam: 1, gamma: 1}).doit())
        self.assertEqual(specialized, x*x)


if __name__ == "__main__":
    unittest.main()
