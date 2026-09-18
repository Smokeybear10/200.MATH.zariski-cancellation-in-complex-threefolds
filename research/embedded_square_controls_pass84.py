"""One exact ideal-only control; no ambient action or return map is asserted."""

import unittest

import sympy as S


class EmbeddedSquareControls(unittest.TestCase):
    def test_embedded_square_defect_and_trace_boundary(self):
        x, y, z, tau = S.symbols("x y z tau")
        variables = (x, y, z)
        f = [x**10, x*y**9, x*z**9]
        q = x**4*y**4*z**4
        ideal = S.groebner(f, *variables)
        self.assertEqual(ideal.reduce(q*q)[1], q*q)
        self.assertEqual(ideal.reduce(q**3)[1], 0)
        strict_witness = x**8*f[0]**2*f[1]**4*f[2]**4
        monic = tau**9-strict_witness
        self.assertEqual(S.expand(monic.subs(tau, q)), 0)
        tenth_power_generators = [f[0]**i*f[1]**j*f[2]**(10-i-j)
                                  for i in range(11) for j in range(11-i)]
        tenth_power = S.groebner(tenth_power_generators, *variables)
        self.assertEqual(tenth_power.reduce(strict_witness)[1], 0)
        self.assertEqual(S.expand(q**9-strict_witness), 0)

        # Monomial intersections use pairwise lcms; colons use g/gcd(g,q^2).
        intersection = [S.lcm(x, g) for g in (x**10, y**9, z**9)]
        self.assertEqual(S.groebner(intersection, *variables), ideal)
        colon = [S.cancel(g/S.gcd(g, q*q)) for g in f]
        self.assertEqual(S.groebner(colon, *variables),
                         S.groebner([x*x, y, z], *variables))
        self.assertEqual(ideal.reduce(x*q*q)[1], x*q*q)
        for annihilator in (x*x, y, z):
            self.assertEqual(ideal.reduce(annihilator*q*q)[1], 0)
        exponent_matrix = S.Matrix([[10, 1, 1], [0, 9, 0], [0, 0, 9]])
        self.assertEqual(exponent_matrix.det(), 810)
        jacobian = S.Matrix(f).jacobian(variables)
        self.assertEqual(jacobian.subs({x:0,y:0,z:0}), S.zeros(3))
        self.assertEqual(S.expand(jacobian.det()-810*x**11*y**8*z**8), 0)
        self.assertEqual(ideal.reduce(jacobian.det())[1], 0)

        divergence = sum(S.diff(fi, xi) for fi, xi in zip(f, variables))
        self.assertEqual(divergence, 10*x**9+9*x*y**8+9*x*z**8)
        self.assertNotEqual(ideal.reduce(q+divergence)[1], 0)
        degree = lambda p: min(sum(monomial) for monomial, coeff in S.Poly(p, *variables).terms())
        self.assertEqual(degree(divergence), 9)
        self.assertEqual(degree(q), 12)
        self.assertEqual(min(map(degree, f)), 10)
        # The nonzero degree-nine term remains after multiplication by any
        # local unit, so no admissible b0 supplies q=-b0*div(f) modulo I.

        companion = S.Matrix([y**3+x**3*y**2/3, x**3, 0])
        companion_ideal = S.groebner(list(companion), *variables)
        expected_companion = S.groebner([x**3, y**3], *variables, domain=S.QQ)
        self.assertEqual([g.as_expr() for g in companion_ideal.polys],
                         [g.as_expr() for g in expected_companion.polys])
        div_companion = sum(S.diff(fi, xi) for fi, xi in zip(companion, variables))
        self.assertEqual(div_companion, x*x*y*y)
        traced_q = -div_companion
        self.assertEqual(companion_ideal.reduce(traced_q)[1], -x*x*y*y)
        self.assertEqual(companion_ideal.reduce(traced_q**2)[1], 0)
        self.assertEqual(S.expand((tau**3+x**6*y**6).subs(tau, traced_q)), 0)
        fourth = S.groebner([x**(3*j)*y**(3*(4-j)) for j in range(5)], *variables)
        self.assertEqual(fourth.reduce(traced_q**3)[1], 0)
        t = S.symbols("t")
        L = companion.jacobian(variables)
        determinant = S.Poly(S.expand((1+t*traced_q)*(S.eye(3)+t*L).det()-1), t)
        self.assertEqual(companion_ideal.reduce(determinant.nth(1))[1], 0)
        self.assertEqual(companion_ideal.reduce(determinant.nth(2))[1], -9*x*x*y*y)
        # Even this trace-linked integral element fails the full quotient
        # determinant identities required of an actual rank-one action.


if __name__ == "__main__":
    unittest.main(verbosity=2)
