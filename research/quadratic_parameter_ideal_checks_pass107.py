"""One formal matrix/conic control method for pass107.

The determinant is checked by polynomial ideal-membership certificates,
not by division or an example claimed to satisfy the actual hypotheses.
Derivative constants and a=x^2,b=y^3 substitutions are finite formal
identities. No test establishes purity, a flat quotient, generation,
a reduced parameter ideal, an actual frame, or cancellation.
"""

import unittest

import sympy as sp


class QuadraticParameterIdealChecks(unittest.TestCase):
    def test_matrix_certificates_and_nonreduced_conic_identities(self):
        a, b, c, d, zeta = sp.symbols("a b c d zeta")
        x11, x12, x21, x22 = sp.symbols("x11 x12 x21 x22")
        matrix = sp.Matrix([[x11, x12], [x21, x22]])
        determinant = matrix.det()
        e1 = d*x11-c*x21-zeta*a
        e2 = d*x12-c*x22-zeta*b
        e3 = b*x11-a*x12+2*c
        e4 = b*x21-a*x22+2*d
        self.assertEqual(sp.expand(
            a*(determinant-2*zeta)
            -(2*e1-x11*e4+x21*e3)), 0)
        self.assertEqual(sp.expand(
            b*(determinant-2*zeta)
            -(2*e2-x12*e4+x22*e3)), 0)

        # One formal specialization satisfies the row and column equations.
        # It is not asserted to meet any of the actual ring hypotheses.
        sample = {x11: 1, x12: 0, x21: 0, x22: 2*zeta,
                  c: -b/2, d: zeta*a}
        self.assertTrue(all(sp.expand(eq.subs(sample)) == 0
                            for eq in (e1, e2, e3, e4)))
        self.assertEqual(sp.expand(
            determinant.subs(sample)-2*zeta), 0)

        z, w = sp.symbols("z w")
        r = a*z+b*w
        p_value = a*c+b*d
        nz = b*r+c
        nw = -a*r+d

        def derivative(expr, order=1):
            for _ in range(order):
                expr = sp.expand(nz*sp.diff(expr, z)
                                 +nw*sp.diff(expr, w))
            return expr

        conic = r**2-2*d*z+2*c*w
        self.assertEqual(derivative(r), p_value)
        self.assertEqual(derivative(conic), 0)
        self.assertEqual(sp.expand(derivative(z, 2)-b*p_value), 0)
        self.assertEqual(sp.expand(derivative(w, 2)+a*p_value), 0)
        self.assertEqual(derivative(z, 3), 0)
        self.assertEqual(derivative(w, 3), 0)
        for polynomial, expected in (
            (z**2, 6*b**2*p_value**2),
            (z*w, -6*a*b*p_value**2),
            (w**2, 6*a**2*p_value**2),
        ):
            self.assertEqual(sp.expand(
                derivative(polynomial, 4)-expected), 0)
        self.assertEqual(sp.expand(
            derivative(r*z, 3)-3*b*p_value**2), 0)
        self.assertEqual(sp.expand(
            derivative(r*w, 3)+3*a*p_value**2), 0)

        c20, c11, c02, d20, d11, d02 = sp.symbols(
            "c20 c11 c02 d20 d11 d02")
        q20, q11, q02 = sp.symbols("q20 q11 q02")
        c_quadratic = c20*a**2+c11*a*b+c02*b**2
        d_quadratic = d20*a**2+d11*a*b+d02*b**2
        q_quadratic = q20*a**2+q11*a*b+q02*b**2
        conic_relation = sp.expand(
            conic.subs({c: c_quadratic, d: d_quadratic})-q_quadratic
        )
        coefficient_forms = (
            z**2-2*d20*z+2*c20*w-q20,
            2*z*w-2*d11*z+2*c11*w-q11,
            w**2-2*d02*z+2*c02*w-q02,
        )
        self.assertEqual(sp.expand(
            conic_relation
            -a**2*coefficient_forms[0]
            -a*b*coefficient_forms[1]
            -b**2*coefficient_forms[2]), 0)

        x, y = sp.symbols("x y")
        substitution = {a: x**2, b: y**3}
        self.assertEqual(sp.expand(
            conic_relation.subs(substitution)
            -x**4*coefficient_forms[0]
            -x**2*y**3*coefficient_forms[1]
            -y**6*coefficient_forms[2]), 0)
        self.assertEqual(sp.gcd(x**2, y**3), 1)

        parameter_ideal = sp.groebner([x**2, y**3], x, y)
        self.assertEqual(parameter_ideal.reduce(x**2)[1], 0)
        self.assertEqual(parameter_ideal.reduce(y**3)[1], 0)
        self.assertEqual(parameter_ideal.reduce(x*y)[1], x*y)
        parameter_square = sp.groebner(
            [x**4, x**2*y**3, y**6], x, y
        )
        # A maximal-ideal-square coefficient need not belong to J^2.
        self.assertEqual(parameter_square.reduce(x**2)[1], x**2)
        self.assertEqual(parameter_square.reduce(y**2)[1], y**2)
        for generator in (x**4, x**2*y**3, y**6):
            self.assertEqual(parameter_square.reduce(generator)[1], 0)

        for certificate in (
            a*(determinant-2*zeta)-(2*e1-x11*e4+x21*e3),
            b*(determinant-2*zeta)-(2*e2-x12*e4+x22*e3),
        ):
            self.assertEqual(sp.expand(
                certificate.subs(substitution)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
