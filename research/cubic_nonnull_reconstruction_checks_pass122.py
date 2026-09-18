"""Two finite algebraic checks for the non-null reconstruction122.

The first checks differential and row identities modulo the explicit norm
relation, retaining its residual in polynomial absorption. The second is
a polynomial-speed control, not a potential or original-frame realization.
Neither method certifies invariant-kernel contraction, the finite-place
lemma, prime cancellation, or a universal geometric exclusion.
"""

import unittest

import sympy as sp


class NonnullReconstructionChecks(unittest.TestCase):
    def test_connection_potential_and_polynomial_reconstruction(self):
        h, Y, g, P = sp.symbols("h Y g P")
        D = sp.Function("D")(h)
        norm = g**2-1-D*Y**2

        def dh(value):
            return sp.diff(value, h)+sp.diff(value, g)*sp.diff(D, h)*Y**2/(2*g)

        def dy(value):
            return sp.diff(value, Y)+sp.diff(value, g)*D*Y/g

        def zero(value, modulo_norm=False):
            entries = value if isinstance(value, sp.MatrixBase) else [value]
            for entry in entries:
                numerator = sp.fraction(sp.cancel(entry))[0]
                if modulo_norm:
                    numerator = sp.rem(numerator, norm, g)
                self.assertEqual(sp.simplify(numerator), 0)

        speed = sp.Matrix([g, h*Y, Y])
        bh, by = speed.applyfunc(dh), speed.applyfunc(dy)
        zero(sp.Matrix.hstack(speed, bh, by).det()-Y/g, True)
        zero(by.applyfunc(dy)-D/g**2*speed+D*Y/g**2*by, True)
        zero(by.applyfunc(dh)-sp.diff(D, h)*Y/(2*g**2)*speed-bh/Y
             +sp.diff(D, h)*Y**2/(2*g**2)*by, True)
        zero(dh(dy(g))-dy(dh(g)))

        rho = sp.Function("rho")(h, Y)
        B22 = (D*rho-D*Y*dy(rho)-g**2*dy(dy(rho)))/g**2
        constant_candidate = g*(rho-Y*dy(rho))
        linear_candidate = g**2*dy(rho)-D*Y*rho
        zero(dy(constant_candidate)-Y*g*B22)
        zero(dy(linear_candidate)+g**2*B22)
        zero(constant_candidate*g+linear_candidate*Y-rho, True)
        C, A = sp.Function("C")(h), sp.Function("A")(h)
        rho_form = C*g+A*Y
        zero(D/g**2*rho_form-dy(dy(rho_form))-D*Y/g**2*dy(rho_form), True)
        B12 = (sp.diff(D, h)*Y/(2*g**2)*rho_form-dh(dy(rho_form))
               +dh(rho_form)/Y-sp.diff(D, h)*Y**2/(2*g**2)*dy(rho_form))
        zero(B12-sp.diff(C, h)/(Y*g), True)

        x1, x2, x3, u = sp.symbols("x1 x2 x3 u")
        v = (x2-h*x3)/Y
        field_row = (-2*g*Y*x1+sp.diff(D, h)*Y**2*x2
                     +(2*g**2-h*sp.diff(D, h)*Y**2)*x3)
        R = field_row/2
        zero(speed*(x3-R)/Y+bh*v+by*R-sp.Matrix([x1, x2, x3]), True)
        zero(Y**2*v-(Y*x2-h*Y*x3))

        a3 = sp.Symbol("a3", nonzero=True)
        a2, a1, a0 = sp.symbols("a2 a1 a0")
        cubic = a3*h**3+a2*h**2+a1*h+a0
        specialized_row = field_row.subs({sp.diff(D, h): sp.diff(cubic, h), D: cubic})
        F = a3*P**3+a2*P**2*Y+a1*P*Y**2+a0*Y**3+Y-g**2*Y
        polynomial_row = (-2*g*Y*x1+(3*a3*P**2+2*a2*P*Y+a1*Y**2)*x2
                          +(3-g**2+a2*P**2+2*a1*P*Y+3*a0*Y**2)*x3)
        zero(Y*(specialized_row.subs(h, P/Y)-polynomial_row)+3*F*x3)
        E_row = sum(sp.diff(polynomial_row, x)*b
                    for x, b in zip((x1, x2, x3), (g, P, Y)))
        zero(E_row-3*F)
        zero(polynomial_row.subs({P: 0, Y: 0})-(3-g**2)*x3)
        K0 = (g**2-1-a2*P**2-a1*P*Y-a0*Y**2)/a3
        zero(a3*(P**3-Y*K0)-F)
        zero(K0.subs({P: 0, Y: 0})-(g**2-1)/a3)
        relative_R = sp.Symbol("relative_R")
        third_coordinate = Y*(u+rho_form)+relative_R
        zero(third_coordinate-Y*u-relative_R-C*g*Y-A*Y**2)

    def test_polynomial_speed_control_with_strict_divisor_orders(self):
        s, t, z = sp.symbols("s t z")
        H = s*t
        U = H**2+2
        g, P, Y = H**2+1, s*t**2*U, s*t**4*U**2
        h = 1/(t**2*U)
        speed = sp.Matrix([g, P, Y])
        self.assertEqual(sp.cancel(g**2-h**3*Y**2-1), 0)
        self.assertEqual(sp.expand(g**2-s*P), 1)
        omega = sp.Matrix.hstack(speed, speed.diff(s), speed.diff(t)).det()
        self.assertEqual(sp.expand(omega-4*s*t**5*U**2), 0)
        self.assertEqual(sp.expand(g**2-1-s**2*t**2*U), 0)
        self.assertEqual(sp.cancel(P**3/Y-s**2*t**2*U), 0)

        def order(value, variable):
            numerator, denominator = sp.fraction(sp.cancel(value))
            lowest = lambda p: min(power[0] for power, coefficient
                                   in sp.Poly(p, variable).terms() if coefficient != 0)
            return lowest(numerator)-lowest(denominator)

        for variable, expected in ((s, (1, 1)), (t, (4, 2))):
            with self.subTest(divisor=variable):
                oy, op = order(Y, variable), order(P, variable)
                self.assertEqual((oy, op), expected)
                self.assertLess(oy, 3*op)
                self.assertGreater(order(g**2-1, variable), 0)
        for root in (sp.I*sp.sqrt(2), -sp.I*sp.sqrt(2)):
            with self.subTest(divisor=f"s*t-({root})"):
                substitution = {t: (z+root)/s}
                oy = order(Y.subs(substitution), z)
                op = order(P.subs(substitution), z)
                self.assertEqual((oy, op), (2, 1))
                self.assertLess(oy, 3*op)
                self.assertGreater(order((g**2-1).subs(substitution), z), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
