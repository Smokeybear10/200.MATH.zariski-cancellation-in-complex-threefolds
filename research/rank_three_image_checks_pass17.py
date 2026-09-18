#!/usr/bin/env python3
"""Independent exact controls for the canonical rank-three image calculation.

No research module is imported. The all-degree ideal equality is proved in
rank-three-image-pass17.md; these finite controls check its formulas only.
"""

import math
import unittest

import sympy as sp


x, y, z = sp.symbols("x y z")
f = x*z-y*y
g = z*f*f+2*x*x*y*f+x**5
r = -x**3-f*y
S = x*x*y+f*z
field = (2*f*r, -g-6*x*x*r, 2*x*f*f-10*x*y*r)


def delta(value):
    return sp.expand(sum(a*sp.diff(value, v)
                         for a, v in zip(field, (x, y, z))))


class RankThreeImageChecks(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.cancel(value), 0)

    def test_jacobian_orientation_and_local_slice(self):
        for v, image in zip((x, y, z), field):
            jac = sp.Matrix([[sp.diff(h, w) for w in (x, y, z)]
                             for h in (f, g, v)]).det()
            self.assertZero(jac-image)
        self.assertZero(delta(f))
        self.assertZero(delta(g))
        self.assertZero(delta(r)-f*g)

    def test_polynomial_relations_and_second_chart_parameter(self):
        q = g*g*S-2*r**3*f*f-r*f**5
        self.assertZero(r*r+f**3-x*g)
        self.assertZero(f*S-r*x*x-g)
        self.assertZero(f*q-r**5-g**3)
        self.assertZero(delta(q)-5*g*r**4)

    def test_generic_chart_inverse_formulas(self):
        F, G, R = sp.symbols("F G R")
        X = (R*R+F**3)/G
        Y = -(R+X**3)/F
        Z = (G+2*X*X*R+X**5)/F**2
        Q = (R**5+G**3)/F
        newY = -(R*Q+3*R**4*F**2+3*R*R*F**5+F**8)/G**3
        newZ = (Q*Q+F*(5*R**8+4*G**3*R**3)
                +F**4*(10*R**6+2*G**3*R)+10*R**4*F**7
                +5*R*R*F**10+F**13)/G**5
        self.assertZero(Y-newY)
        self.assertZero(Z-newZ)
        self.assertZero(X*Z-Y*Y-F)
        self.assertZero(Z*F*F+2*X*X*Y*F+X**5-G)

    def test_all_ten_witnesses_and_two_periods(self):
        F, G, R = sp.symbols("F G R")
        X = (R*R+F**3)/G
        Y = -(R+X**3)/F
        Z = (G+2*X*X*R+X**5)/F**2
        SS = (R*X*X+G)/F
        basis = (1, R, X, R*X, X*X, SS, Y, R*Y, X*Y, R*X*Y)
        for n in range(30):
            k, i = divmod(n, 10)
            sign = 1 if i < 6 else -1
            polynomial = sp.Poly(basis[i]*Z**k, R)
            self.assertEqual(polynomial.degree(), n)
            top = math.factorial(n)*(F*G)**n*polynomial.LC()
            expected = sign*math.factorial(n)*F**(n-n//5)*G**((n+1)//2)
            self.assertZero(top-expected)

    def test_chart_valuation_bounds_and_periodicity(self):
        for n in range(80):
            i, j = n % 5, n // 5
            self.assertEqual(i+5*j, n)
            self.assertEqual(n-j, n-n//5)
            epsilon, power = n % 2, n // 2
            self.assertEqual(2*power+epsilon, n)
            self.assertEqual(n-power, (n+1)//2)
            self.assertEqual((n+10)-(n+10)//5, n-n//5+8)
            self.assertEqual((n+11)//2, (n+1)//2+5)

    def test_primary_decomposition_monomial_intersection(self):
        F, G = sp.symbols("F G")
        for n in range(1, 20):
            a, b = n-n//5, (n+1)//2
            self.assertZero(sp.lcm(F**a,G**b)-F**a*G**b)
            self.assertEqual(sp.gcd(F**a,G**b),1)

    def test_gcd_does_not_replace_the_coefficient_unit_ideal(self):
        F, G = sp.symbols("F G")
        A, B = F-1, 1+F*G
        self.assertEqual(sp.gcd(A,B),1)
        self.assertEqual(A.subs({F:1,G:-1}),0)
        self.assertEqual(B.subs({F:1,G:-1}),0)
        self.assertEqual(B.subs(F,0),1)
        self.assertEqual(B.subs(G,0),1)

    def test_invariant_pair_matrix_and_variable_time_inverse(self):
        F, G, rr, t = sp.symbols("F G rr t")
        p, eta = F*G, F+G
        a, b = p**2, 1+p*eta
        M, L = 1-p*eta+p*p*eta*eta, -eta**3
        self.assertZero(b*M+p*a*L-1)
        W = eta*rr-a*t
        Wprime = sp.cancel((M-1)/p)*rr+a*t
        phi = {rr:b*rr-p*a*t, t:L*rr+M*t}
        psi = {rr:M*rr+p*a*t, t:-L*rr+b*t}
        self.assertZero(Wprime.subs(phi,simultaneous=True)+W)
        self.assertZero(W.subs(psi,simultaneous=True)+Wprime)
        self.assertZero(a*p*sp.diff(W,rr)+b*sp.diff(W,t)+a)
        self.assertZero(a*p*sp.diff(L*rr+M*t,rr)
                        +b*sp.diff(L*rr+M*t,t)-1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
