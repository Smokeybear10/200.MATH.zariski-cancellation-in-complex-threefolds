"""Exact finite operator controls, not a verifier of the geometric proof."""

import unittest

import sympy as S


class DoubleComponentInitialControls(unittest.TestCase):
    def test_quadratic_pencil_and_surface_initial_operators(self):
        p, q, z = S.symbols("p q z")
        a, b, c = S.symbols("a b c")
        f = p**2
        g = q*z + p*(a*p + b*q + c*z)

        def jac(first, second, value):
            return S.expand(S.Matrix([
                [S.diff(expression, variable) for variable in (p, q, z)]
                for expression in (first, second, value)
            ]).det())

        qp, zp = q + c*p, z + b*p
        self.assertEqual(S.expand(g - qp*zp - (a-b*c)*f), 0)
        self.assertEqual(jac(f, g, p), 0)
        self.assertEqual(S.expand(jac(f, g, qp) + 2*p*qp), 0)
        self.assertEqual(S.expand(jac(f, g, zp) - 2*p*zp), 0)
        value = qp
        for k in range(1, 7):
            value = jac(f, g, value)
            self.assertEqual(S.expand(value - (-2*p)**k*qp), 0)
            self.assertNotEqual(value, 0)

        # Strict higher-degree terms do not alter the quadratic vector field.
        perturbed_f = f + p**3 + p*q*z
        perturbed_g = g + p**2*q + q**2*z
        for coordinate in (p, q, z):
            polynomial = S.Poly(jac(perturbed_f, perturbed_g, coordinate), p, q, z)
            degree_two = sum(
                coefficient*p**i*q**j*z**k
                for (i, j, k), coefficient in polynomial.terms()
                if i+j+k == 2
            )
            self.assertEqual(S.expand(degree_two - jac(f, g, coordinate)), 0)

        # The rank-one surface calculation includes a nonconstant formal unit.
        y, w = S.symbols("y w")
        surface_g = (1 + y + w + y*w)*y**2*w**2

        def surface(value):
            return S.expand(
                S.diff(surface_g, y)*S.diff(value, w)
                - S.diff(surface_g, w)*S.diff(value, y)
            )

        def leading_surface(value):
            return S.expand(2*y*w*(w*S.diff(value, w)-y*S.diff(value, y)))

        for coordinate in (y, w):
            poly = S.Poly(surface(coordinate), y, w)
            degree_three = sum(
                coefficient*y**i*w**j
                for (i, j), coefficient in poly.terms()
                if i+j == 3
            )
            self.assertEqual(S.expand(degree_three-leading_surface(coordinate)), 0)
        self.assertEqual(leading_surface(y*w), 0)
        value = y
        for k in range(1, 7):
            value = leading_surface(value)
            self.assertEqual(S.expand(value - (-2*y*w)**k*y), 0)
            self.assertNotEqual(value, 0)

        # Actual N^3F=0 imposes this weighted coefficient on F*=p+B(t)q^2.
        t = S.symbols("t")
        B = S.Function("B")(t)

        def weighted(value):
            return S.expand(-p*S.diff(value, q) + 2*a*q*S.diff(value, t))

        second = 2*B*p**2 - 10*a*S.diff(B, t)*p*q**2 + 4*a**2*S.diff(B, t, 2)*q**4
        self.assertEqual(S.expand(weighted(weighted(B*q**2)) - second), 0)
        third = weighted(second)
        claim = (
            24*a*S.diff(B, t)*p**2*q
            - 36*a**2*S.diff(B, t, 2)*p*q**3
            + 8*a**3*S.diff(B, t, 3)*q**5
        )
        self.assertEqual(S.expand(third - claim), 0)
        self.assertEqual(
            S.expand(third.subs({B: t, a: 1}).doit() - 24*p**2*q), 0
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
