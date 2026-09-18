"""One exact symbolic control method for the volume-normal lemma99.

Checks the cubic weighted coefficient for a symbolic function, affine
specializations and higher-degree negatives, a rank-one matrix identity,
and an intrinsic polynomial inverse-pair boundary. These calculations do
not certify the actual original frame, whole-fiber lengths, global volume
hypotheses, or any recognition theorem. No older checker is imported.
"""

import unittest

import sympy as S


class QuadraticVolumeNormalChecks(unittest.TestCase):
    def test_affine_column_and_full_derivation_boundary(self):
        c, x, y = S.symbols("c x y")
        nu, b = S.symbols("nu b", nonzero=True)
        a = S.Function("a")(c)

        def weighted(expr, column=a):
            return S.expand(
                -nu * S.diff(column, c) * x * S.diff(expr, y)
                + 2 * nu * b * y * S.diff(expr, c)
            )

        square = weighted(weighted(y))
        cube = weighted(square)
        expected = (
            2 * nu**3 * b * S.diff(a, c) * S.diff(a, c, 2) * x**2
            - 4 * nu**3 * b**2 * S.diff(a, c, 3) * x * y**2
        )
        self.assertEqual(S.expand(square + 2 * nu**2 * b
                                  * S.diff(a, c, 2) * x * y), 0)
        self.assertEqual(S.expand(cube - expected), 0)
        coefficients = S.Poly(cube, x, y)
        self.assertEqual(coefficients.coeff_monomial(x**2),
                         2 * nu**3 * b * S.diff(a, c) * S.diff(a, c, 2))
        self.assertEqual(coefficients.coeff_monomial(x * y**2),
                         -4 * nu**3 * b**2 * S.diff(a, c, 3))

        a0, a1 = S.symbols("a0 a1")
        affine = a0 + a1 * c
        self.assertEqual(weighted(weighted(y, affine), affine), 0)
        for column, answer in (
            (c**2, 8 * nu**3 * b * c * x**2),
            (c**3, 36 * nu**3 * b * c**3 * x**2
             - 24 * nu**3 * b**2 * x * y**2),
        ):
            value = y
            for _ in range(3):
                value = weighted(value, column)
            self.assertEqual(S.expand(value - answer), 0)
            self.assertNotEqual(value, 0)

        # Exact identities: det(C)=0 and (r,s)C=(1,0) force column two zero.
        aa, bb, cc, dd, r, s = S.symbols("aa bb cc dd r s")
        first = r * aa + s * cc
        second = r * bb + s * dd
        determinant = aa * dd - bb * cc
        self.assertEqual(S.expand(
            bb - (bb * (1 - first) + aa * second - s * determinant)), 0)
        self.assertEqual(S.expand(
            dd - (dd * (1 - first) + cc * second + r * determinant)), 0)

        # Intrinsic polynomial coordinates only, not an original C4 frame.
        # Start N=-x*d_y+2y*d_c; set G=y+xc with inverse y=G-xc.
        X, G, C = S.symbols("X G C")
        forward = (x, y + x * c, c)
        backward = (X, G - X * C, C)
        self.assertEqual(
            tuple(S.expand(expr.subs(dict(zip((X, G, C), forward)),
                                     simultaneous=True))
                  for expr in backward),
            (x, y, c),
        )
        self.assertEqual(
            tuple(S.expand(expr.subs(dict(zip((x, y, c), backward)),
                                     simultaneous=True))
                  for expr in forward),
            (X, G, C),
        )
        invariant = X * C + (G - X * C)**2

        def intrinsic(expr):
            return S.expand(
                -S.diff(invariant, C) * S.diff(expr, G)
                + S.diff(invariant, G) * S.diff(expr, C)
            )

        self.assertEqual(intrinsic(invariant), 0)
        self.assertEqual(intrinsic(X), 0)
        self.assertEqual(intrinsic(intrinsic(G)), -2 * X**2)
        self.assertNotEqual(intrinsic(intrinsic(G)), 0)
        self.assertEqual(intrinsic(intrinsic(intrinsic(G))), 0)
        # Weight X=2,G=1 gives f*=CX+G² and the affine leading column a=C.
        monomials = S.Poly(invariant, X, G)
        initial = sum(coefficient * X**i * G**j
                      for (i, j), coefficient in monomials.terms()
                      if 2 * i + j == 2)
        self.assertEqual(S.expand(initial), C * X + G**2)
        self.assertEqual(weighted(weighted(y, c), c), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

