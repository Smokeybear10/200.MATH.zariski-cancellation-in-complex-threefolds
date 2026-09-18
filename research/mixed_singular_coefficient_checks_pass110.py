"""Three finite coefficient controls, not an actual mixed-frame realization.

The first isolates integral-but-nonregular a/b on a singular coefficient
curve. The second checks the derivative formula conditional on an available
shear and actual division. The third checks the general divided-W identities.
No flatness, divisor descent, purity, geometry, or cancellation is tested.
"""

import unittest

import sympy as sp


class MixedSingularCoefficientChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_singular_coefficient_and_artin_nonmembership(self):
        x, y = sp.symbols("x y")
        h, a, b = y**2 - x**5, y * (x + y), x**2
        B2, Q = x * h, y * h
        P = a * h + b * B2
        C1 = (x + y)**2 + x**5
        C2 = x**3 + 2 * x**2 * y + x**6
        self.assert_zero(P - h * (a + x**3))
        self.assertNotEqual(sp.expand(P), 0)
        self.assert_zero(a**2 - h * C1 - b**2 * C2)
        self.assertEqual(sp.gcd(a, b), 1)
        self.assertEqual(sp.gcd(h, b), 1)

        def order(poly):
            return min(sum(powers) for powers, coeff in sp.Poly(poly, x, y).terms()
                       if coeff != 0)

        self.assertEqual([order(f) for f in (a, h, b, B2, Q, P)], [2, 2, 2, 3, 3, 4])
        self.assertGreaterEqual(order(C1), 2)
        self.assertGreaterEqual(order(C2), 3)
        sharp = sp.groebner([
            x*h, y*h, x*a*b, y*a*b,
            x**2*b**2, x*y*b**2, y**2*b**2,
        ], x, y)
        for f in (Q, B2, a**2):
            self.assert_zero(sharp.reduce(sp.expand(f))[1])

        ideal = sp.groebner([h, b], x, y)
        artin = sp.groebner([x**2, y**2], x, y)
        for f in (x**2, y**2):
            self.assert_zero(ideal.reduce(f)[1])
        for f in (h, b):
            self.assert_zero(artin.reduce(f)[1])
        self.assertEqual(ideal.reduce(sp.expand(a))[1], x*y)
        self.assertEqual([artin.reduce(f)[1] for f in (sp.Integer(1), x, y, x*y)],
                         [1, x, y, x*y])
        self.assertEqual(artin.reduce(h)[1], 0)
        self.assertNotEqual(artin.reduce(sp.Integer(1))[1], 0)
        # Denominator-cleared monic relation for z=a/b modulo h.
        self.assert_zero(sp.rem(sp.expand(a**2 - b**2 * C2), h, y))
        # The parameter substitution checks the gap algebra, not normality.
        t = sp.symbols("t")
        z_on_curve = sp.cancel(a.subs({x: t**2, y: t**5})
                               / b.subs({x: t**2, y: t**5}))
        self.assert_zero(z_on_curve - t**3 - t**6)

        # The stronger actual argument requires b in this ideal. The tuple
        # fails that necessary condition and is not an actual counterexample.
        required = sp.groebner([
            h, x*a, y*a, x**2*b, x*y*b, y**2*b,
        ], x, y)
        expected_required = sp.groebner([y**2, x**2*y, x**4], x, y)
        for f in (y**2, x**2*y, x**4):
            self.assert_zero(required.reduce(f)[1])
        for f in (h, x*a, y*a, x**2*b, x*y*b, y**2*b):
            self.assert_zero(expected_required.reduce(sp.expand(f))[1])
        self.assertEqual(required.reduce(b)[1], x**2)

    def test_general_shear_conic_and_derivative_identity(self):
        h, b, u, eps, beta, delta, q, zeta, G, H = sp.symbols(
            "h b u eps beta delta q zeta G H")
        r = h*u*G + b*H
        B2 = h*beta + b**2*delta
        P = h**2*u + b*B2
        NG = eps*b*r + h
        NH = -eps*h*u*r + B2

        def deriv(expression):
            return sp.cancel(NG*sp.diff(expression, G) + NH*sp.diff(expression, H))

        self.assert_zero(deriv(r) - P)
        conic = eps*r**2 - 2*B2*G + 2*h*H - h*zeta - b**2*q
        remainder = (eps*h*u**2*G**2 + 2*eps*u*b*G*H
                     - 2*beta*G + 2*H - zeta)
        numerator = eps*H**2 - 2*delta*G - q
        self.assert_zero(conic - h*remainder - b**2*numerator)
        self.assert_zero(deriv(conic))
        U = numerator/h
        expected = (-2*eps**2*u*H*r + 2*eps*beta*H
                    - 2*eps*b*u*delta*G - 2*delta)
        self.assert_zero(deriv(U) - expected)
        self.assert_zero(expected.subs({H: 0, h: 0, b: 0, beta: 0, delta: 0}))

    def test_general_divided_W_and_determinant_identity(self):
        a, b, h, eps, G, H = sp.symbols("a b h eps G H")
        U0, V0, W0, beta, tau, delta, zeta, xi, q = sp.symbols(
            "U0 V0 W0 beta tau delta zeta xi q")
        r = a*G + b*H
        relation = a**2 - h*U0 - a*b*V0 - b**2*W0
        B2 = h*beta + a*b*tau + b**2*delta
        Q = h*zeta + a*b*xi + b**2*q
        NG, NH = eps*b*r+h, -eps*a*r+B2
        A = eps*U0*G**2 - 2*beta*G + 2*H - zeta
        B = (a*(eps*V0*G**2 + 2*eps*G*H - 2*tau*G - xi)
             + b*(eps*W0*G**2 + eps*H**2 - 2*delta*G - q))
        conic = eps*r**2 - 2*B2*G + 2*h*H - Q
        self.assert_zero(conic - h*A - b*B - eps*relation*G**2)
        W = -A/b
        derivative = NG*sp.diff(W, G) + NH*sp.diff(W, H)
        expected = (-2*eps**2*U0*G*r + 2*eps*beta*r
                    + 2*eps*((a*V0+b*W0)*G+a*H) - 2*a*tau - 2*b*delta)
        self.assert_zero(derivative - expected - 2*eps*G*relation/b)

        rvar, P, g0 = sp.symbols("rvar P g0")
        generic_G = eps*b*rvar**2/(2*P) + h*rvar/P + g0
        generic_H = (rvar-a*generic_G)/b
        generic_W = -(eps*U0*generic_G**2 - 2*beta*generic_G
                      + 2*generic_H-zeta)/b
        columns = [sp.Integer(1), generic_G, generic_G**2,
                   generic_G*generic_H, generic_W]
        matrix = sp.Matrix([
            [sp.Poly(f, rvar).coeff_monomial(rvar**j) for f in columns]
            for j in range(5)
        ])
        self.assert_zero(matrix.det(method="domain-ge") + eps**4*b/(8*P**4))

        # Finite identity behind unit absorption after b=h*s+a*v.
        s, v = sp.symbols("s v")
        substituted_relation = relation.subs(b, h*s+a*v)
        absorbed = (a**2*(1-v*V0-v**2*W0)
                    - h*(U0+a*s*V0+2*a*s*v*W0+h*s**2*W0))
        self.assert_zero(substituted_relation - absorbed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
