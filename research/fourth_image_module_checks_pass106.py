"""Two finite algebra controls for pass106, not universal geometry.

The ring method checks explicit rational embeddings and identities for an
intrinsic LND algebra whose closed fiber is nonflat and has zero induced
derivation. It does not prove the arbitrary-element degree-module lattice.

The inverse method checks dual-number and simple-line parameter changes.
It does not verify normalization, flatness, boundary purity, or the actual
all-parameter theorem. No other checker or solver is imported.
"""

import unittest

import sympy as sp


class FourthImageModuleChecks(unittest.TestCase):
    def test_intrinsic_ring_matrix_and_products(self):
        a, b, z, u0, v0 = sp.symbols("a b z u0 v0")
        u = z**4 / a
        v = (z**3 - z**4) / b

        def normal(expr):
            return sp.cancel(sp.expand(expr))

        def deriv(expr, order=1):
            for _ in range(order):
                expr = normal(a * b * sp.diff(expr, z))
            return expr

        def zero(expr):
            self.assertEqual(normal(expr), 0)

        zero(a * u - z**4)
        zero(b * v - z**3 + z**4)
        zero(a * u + b * v - z**3)
        for element, expected in (
            (z, a * b),
            (u, 4 * b * z**3),
            (v, 3 * a * z**2 - 4 * a * z**3),
        ):
            zero(deriv(element) - expected)

        bases = [
            [sp.Integer(1)],
            [sp.Integer(1), z],
            [sp.Integer(1), z, z**2],
            [sp.Integer(1), z, z**2, z**3],
            [sp.Integer(1), z, z**2, u, v],
        ]
        for degree, basis in enumerate(bases):
            for element in basis:
                zero(deriv(element, degree + 1))
            coefficient_matrix = sp.Matrix(
                [[sp.expand(element).coeff(z, row) for element in basis]
                 for row in range(degree + 1)]
            )
            self.assertEqual(coefficient_matrix.rank(), degree + 1)
        zero(deriv(z**2, 2) - 2 * a**2 * b**2)
        zero(deriv(z**3, 3) - 6 * a**3 * b**3)
        zero(deriv(u, 4) - 24 * a**3 * b**4)
        zero(deriv(v, 4) + 24 * a**4 * b**3)

        inclusion = sp.Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, a],
            [0, 0, 0, b],
        ])
        images = sp.Matrix([bases[4]]) * inclusion
        for got, expected in zip(images, bases[3]):
            zero(got - expected)
        self.assertEqual(inclusion.rank(), 4)
        self.assertEqual(inclusion.subs({a: 0, b: 0}).rank(), 3)
        fourth_row = sp.Matrix([[0, 0, 0,
                               24 * a**3 * b**4, -24 * a**4 * b**3]])
        self.assertEqual(fourth_row * inclusion, sp.zeros(1, 4))
        residual = [a, b]
        self.assertEqual(sp.gcd(*residual), 1)
        self.assertTrue(all(term.subs({a: 0, b: 0}) == 0
                            for term in residual))

        theta, t, p, q = sp.Integer(4), z**3, sp.Integer(0), 3*a*z**2
        g = deriv(t, 3)
        zero(deriv(u) - theta*b*t - p)
        zero(deriv(v) + theta*a*t - q)
        zero(g - a*deriv(p, 2) - b*deriv(q, 2))
        zero(deriv(u, 4) - theta*g*b)
        zero(deriv(v, 4) + theta*g*a)

        i1, i2, i3 = a*b, 2*a**2*b**2, 6*a**3*b**3
        generator_a = 24*a**4*b**3
        generator_b = 24*a**3*b**4
        zero(i2**2 - (a/sp.Integer(6))*generator_b)
        zero(i1*i3 - (a/sp.Integer(4))*generator_b)
        zero(i1 - (b/sp.Integer(4))*(theta*a))
        zero(g - (3*a*b)*i2)
        zero(z**4 - a*u)
        zero(z**3 - a*u - b*v)
        for left_degree, right_degree in ((1, 1), (1, 2), (1, 3), (2, 2)):
            for left in bases[left_degree]:
                for right in bases[right_degree]:
                    product = normal(left*right)
                    self.assertLessEqual(sp.degree(product, z),
                                         left_degree + right_degree)

        # Exact polynomial relations and the closed-fiber regular-sequence
        # obstruction. This is not an algorithmic proof of prime presentation.
        relations = [a*u0-z**4, b*v0-z**3+z**4]
        groebner = sp.groebner(relations, u0, v0, z, a, b)
        self.assertEqual(
            groebner.reduce(b*v0*z-a*u0*(1-z))[1], 0
        )
        special = sp.groebner([z**4, -z**3+z**4], z, u0, v0)
        self.assertEqual(special.reduce(z**3)[1], 0)
        self.assertNotEqual(special.reduce(v0*z)[1], 0)
        self.assertEqual(special.reduce(z**2)[1], z**2)
        for derivative_polynomial in (a*b, 4*b*z**3, 3*a*z**2-4*a*z**3):
            self.assertEqual(derivative_polynomial.subs({a: 0, b: 0}), 0)

    def test_dual_number_and_simple_parameter_inverses(self):
        c, t, epsilon = sp.symbols("c t epsilon")
        slope, offset = sp.symbols("slope offset", nonzero=True)

        def mod_nilpotent(expr):
            return sp.Poly(sp.expand(expr), epsilon).rem(
                sp.Poly(epsilon**2, epsilon)
            ).as_expr()

        for beta in (sp.Integer(0), sp.Integer(3), c, c**2+1,
                     c**4-2*c+3):
            with self.subTest(beta=beta):
                forward = slope*c + offset + epsilon*beta
                normalized_t = (t-offset)/slope
                inverse = normalized_t - epsilon*beta.subs(
                    c, normalized_t
                )/slope
                self.assertEqual(
                    sp.simplify(mod_nilpotent(
                        forward.subs(c, inverse)-t)), 0
                )
                self.assertEqual(
                    sp.simplify(mod_nilpotent(
                        inverse.subs(t, forward)-c)), 0
                )
        simple_forward = slope*c+offset
        simple_inverse = (t-offset)/slope
        self.assertEqual(sp.simplify(
            simple_forward.subs(c, simple_inverse)-t), 0)
        self.assertEqual(sp.simplify(
            simple_inverse.subs(t, simple_forward)-c), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

