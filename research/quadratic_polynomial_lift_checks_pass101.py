"""Two finite intrinsic polynomial control methods for pass101.

Tests m=1,2,3, sample invariant-module coefficients, a finite parity
independence table, rational repairs and an exact polynomial shear.
The arbitrary-polynomial saturation theorem is a written proof, not
certified by this finite table. These intrinsic polynomial threefolds
are not original constant-acceleration four-coordinate frames.
The second method checks a distinct sharp base-order noniteration
control and exact global ideal equalities, not the full original J.
"""

import unittest

import sympy as S


class QuadraticPolynomialLiftChecks(unittest.TestCase):
    def test_intrinsic_module_residues_and_polynomial_shear(self):
        x, y, c, C, F = S.symbols("x y c C F")
        eta, d, a, b, r, s = S.symbols("eta d a b r s")
        for m in (1, 2, 3):
            with self.subTest(m=m):
                f = y**2 + x**m * c

                def N(expr):
                    return S.expand(-x**m * S.diff(expr, y)
                                    + 2 * y * S.diff(expr, c))

                def iterate(expr, count, action=N):
                    for _ in range(count):
                        expr = action(expr)
                    return S.cancel(expr)

                self.assertEqual(N(f), 0)
                self.assertEqual(S.gcd(x**m, 2*y), 1)
                self.assertEqual(iterate(c, 3), 0)
                self.assertEqual(N(N(c)), -2 * x**m)
                for element in (x, y, c):
                    jacobian = S.Matrix((x, f, element)).jacobian((x, y, c))
                    self.assertEqual(S.expand(jacobian.det() - N(element)), 0)

                a0 = eta + a*x + b*F + x**2 + x*F + F**2
                a1 = d + x + F + x*F
                a2 = r*x + s*F + x**2 + F**2
                h = S.expand((a0 + a1*y + a2*c).subs(F, f))
                self.assertEqual(iterate(h, 3), 0)
                self.assertEqual(S.rem(h.subs(x, 0), y**2, y), eta + d*y)
                normal = sum(coefficient * x**i * y**j
                             for (i, j), coefficient in S.Poly(h, x, y).terms()
                             if i + j < 2)
                expected = eta + d*y + x*(a + r*c)
                if m == 1:
                    expected += x*(b*c + s*c**2)
                self.assertEqual(S.expand(normal - expected), 0)

                self.assertEqual(iterate(y*c, 3), 6*x**(2*m))
                self.assertEqual(iterate(y*c**2, 3),
                                 12*x**(2*m)*c - 48*x**m*y**2)
                repair1 = y*c + y**3/x**m
                repair2 = y*c**2 + 2*y**3*c/x**m + y**5/x**(2*m)
                self.assertEqual(S.cancel(repair1 - y*f/x**m), 0)
                self.assertEqual(S.cancel(repair2 - y*f**2/x**(2*m)), 0)
                for repaired in (repair1, repair2):
                    self.assertEqual(iterate(repaired, 3), 0)
                    denominator = S.fraction(S.cancel(repaired))[1]
                    self.assertNotEqual(denominator.subs(x, 0), 1)
                    self.assertEqual(denominator.subs(x, 0), 0)

                # A base-preserving polynomial shear changes the actual
                # c-degree, but fixes the normal generators x,y.
                P = y**4 + x*y + 1
                forward = (x, y, c + P)
                backward = (x, y, C - P)
                self.assertEqual(
                    tuple(S.expand(expr.subs(dict(zip((x, y, C), forward)),
                                             simultaneous=True))
                          for expr in backward), (x, y, c))
                self.assertEqual(
                    tuple(S.expand(expr.subs(dict(zip((x, y, c), backward)),
                                             simultaneous=True))
                          for expr in forward), (x, y, C))
                self.assertEqual(S.Matrix(forward).jacobian((x, y, c)).det(), 1)
                sheared_c = c + P
                sheared_f = y**2 + x**m * sheared_c

                def sheared_N(expr):
                    return S.expand(-x**m * S.diff(expr, y)
                                    + (2*y + x**m*S.diff(P, y))*S.diff(expr, c))

                self.assertEqual(sheared_N(sheared_f), 0)
                self.assertEqual(sheared_N(sheared_c), 2*y)
                self.assertEqual(iterate(sheared_c, 3, sheared_N), 0)
                self.assertEqual(iterate(c, 3, sheared_N), 24*x**(3*m)*y)
                self.assertEqual(iterate(c, 5, sheared_N), 0)
                sheared_h = S.expand((a0 + a1*y + a2*sheared_c).subs(F, sheared_f))
                self.assertEqual(iterate(sheared_h, 3, sheared_N), 0)
                self.assertEqual(S.rem(sheared_h.subs(x, 0), y**2, y),
                                 eta + d*y)

        # A finite shadow of the source-free all-degree parity argument.
        columns = [y**(2*j) for j in range(4)]
        columns += [y**(2*j + 1) for j in range(4)]
        columns += [c*y**(2*j) for j in range(4)]
        monomials = sorted({powers for expr in columns
                            for powers, _ in S.Poly(expr, y, c).terms()})
        matrix = S.Matrix([[S.Poly(expr, y, c).coeff_monomial(y**i*c**j)
                            for expr in columns] for i, j in monomials])
        self.assertEqual(matrix.rank(), 12)

    def test_sharp_base_order_noniteration_control(self):
        x, y, c, t = S.symbols("x y c t")
        f = x*c + y**2
        a0 = y**2
        F = x + f*a0
        G = y
        h = x*c

        def N(expr):
            return S.expand(-x*S.diff(expr, y) + 2*y*S.diff(expr, c))

        def square(expr):
            return N(N(expr))

        self.assertEqual(N(f), 0)
        for element in (a0, F, G, h):
            self.assertEqual(N(square(element)), 0)
        self.assertEqual(square(a0), 2*x**2)
        self.assertEqual(square(h), -2*x**2)
        self.assertEqual(square(F), S.expand(2*x**2*f))
        self.assertNotEqual(square(F), 0)

        # Global ideal equality (F,G)=(x,y), by explicit polynomial recovery.
        self.assertEqual(S.expand(F - f*y*G - x), 0)
        self.assertEqual(G, y)
        # Global ideal equality (F,G²)=(x,f), with a determinant-one matrix.
        transition = S.Matrix(((1-c*f, f), (-c, 1)))
        inverse = S.Matrix(((1, -f), (c, 1-c*f)))
        self.assertEqual(S.expand(transition.det()), 1)
        self.assertEqual((transition*inverse).applyfunc(S.expand), S.eye(2))
        self.assertEqual((inverse*transition).applyfunc(S.expand), S.eye(2))
        self.assertEqual((transition*S.Matrix((x, f))).applyfunc(S.expand),
                         S.Matrix((S.expand(F), G**2)))
        self.assertEqual((inverse*S.Matrix((F, G**2))).applyfunc(S.expand),
                         S.Matrix((x, f)))

        def first_normal(expr):
            return S.expand(sum(coefficient*x**i*y**j
                                for (i, j), coefficient
                                in S.Poly(expr, x, y).terms() if i+j < 2))

        self.assertEqual(first_normal(F), x)
        self.assertEqual(first_normal(f-c*F), 0)

        # x,t are independent base variables; substituting t=f is injective.
        for base_value, intrinsic_value, exact_order in (
            (2*x**2, square(a0), 2),
            (-2*x**2, square(h), 2),
            (2*x**2*t, square(F), 3),
        ):
            self.assertEqual(S.expand(base_value.subs(t, f)-intrinsic_value), 0)
            powers = [i+j for (i, j), coefficient
                      in S.Poly(base_value, x, t).terms() if coefficient != 0]
            self.assertEqual(min(powers), exact_order)


if __name__ == "__main__":
    unittest.main(verbosity=2)
