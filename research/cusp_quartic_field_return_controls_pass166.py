"""Independent finite controls for the quartic actual-field argument166.

Generic jets verify polynomial identities only. Finite pencil-degree controls
do not replace the proof of irreducibility or exact field return. The final
index-eight data are expressly formal and fail actual field return; they are
not an actual polynomial four-coordinate frame. No earlier checker is imported.
"""

import unittest

import sympy as sp


class CuspQuarticFieldReturnControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_generic_line_coefficients_cubic_gate_and_Euler_identity(self):
        t = sp.Symbol("t", nonzero=True)
        y, rho, delta, h, Lam = sp.symbols("y rho delta h Lambda")
        K1, K2, N0, N1, L0, b0, d0 = sp.symbols("K1 K2 N0 N1 L0 b0 d0")
        p3 = 4*t*delta
        p2 = t*(-6*delta**2-3*t+Lam)
        P = -t*y**4+p3*y**3+p2*y**2+(rho/t+b0)*y+h*rho+d0
        kt, ktt, ell = -rho/t**2+K1, 2*rho/t**3+K2, -rho/t**2+L0
        z = 3*t*y**2+kt*y+P/t+N0
        w = t*ell-t*y**3-t*ktt*y**2/2+(y/t)*P-t*N1*y
        Z0 = (-y**4+4*delta*y**3+(-6*delta**2+Lam)*y**2
              +(K1+b0/t)*y+N0+d0/t)
        V0 = t*L0-4*t*y**3-(t*K2/2+K1)*y**2-(t*N1+N0)*y
        self.zero(t**3*(z-Z0-h*rho/t))
        self.zero(t**3*(w-y*Z0-V0-(y*h-1)*rho/t))
        G = sp.expand((1-y*h)*z+h*w)
        self.zero(t**3*(G-Z0-h*V0))
        self.zero(sp.diff(G, rho))
        self.zero(G.coeff(y, 4)+1)
        self.zero(G.coeff(y, 3)-4*(delta-t*h))

        hp, alpha, beta = sp.symbols("hp alpha beta")
        claimed_span_coefficient = delta-t*h-alpha-beta*h
        derivative = (sp.diff(claimed_span_coefficient, t)
                      +h*sp.diff(claimed_span_coefficient, delta)
                      +hp*sp.diff(claimed_span_coefficient, h))
        self.zero(derivative+(t+beta)*hp)
        # The implication h'=0 uses transcendence of t and the exact
        # constant field. It is not inferred from numerical samples here.

        j, b, c, q, K3 = sp.symbols("j b c q K3")
        # In this Euler step h and j are constants, after the preceding
        # mathematical argument. The jet K2 has derivative K3.
        first_integral = t**3*(K2+6*h*t+8*j)
        differentiated = sp.diff(first_integral, t)+K3*sp.diff(first_integral, K2)
        self.zero(differentiated-t**2*(t*K3+3*K2+24*h*t+24*j))
        k0 = -h*t**3-4*j*t**2+b*t+c+q/t
        self.zero(t**4*(t*sp.diff(k0, t, 3)+3*sp.diff(k0, t, 2)+24*h*t+24*j))
        self.zero(t**3*(sp.diff(k0, t, 2)+6*h*t+8*j)-2*q)
        homogeneous = b*t+c+q/t
        self.zero(t**4*(t*sp.diff(homogeneous, t, 3)+3*sp.diff(homogeneous, t, 2)))
        self.assertLessEqual(sp.degree(sp.expand(t*k0), t), 4)

    def test_pencil_leading_degree_and_linear_quadratic_boundaries(self):
        S, T, Z, W = sp.symbols("S T Z W")
        for degree in (1, 2, 3, 4):
            with self.subTest(degree=degree):
                coefficients = sp.symbols(f"c0:{degree+1}")
                top = sum(coefficients[j]*S**(degree-j)*T**j
                          for j in range(degree+1))
                relation = top+S**(degree-1)+T**(degree-1)
                transformed = sp.expand(relation.subs(T, W-Z*S))
                expected_leading = sum(coefficients[j]*(-Z)**j
                                       for j in range(degree+1))
                self.assertEqual(sp.degree(transformed, S), degree)
                self.zero(transformed.coeff(S, degree)-expected_leading)
                self.assertNotEqual(sp.expand(expected_leading), 0)
                self.zero(transformed.subs(W, T+Z*S)-relation)
                # No claim that each freely specified relation is
                # irreducible. Only the generic leading-degree mechanism.

        v, a, b = sp.symbols("v a b")
        linear_relation = T-a*S-b
        linear_W = v*Z+a*v+b
        self.zero(linear_relation.subs({S: v, T: a*v+b}, simultaneous=True))
        self.zero(linear_W-b-(Z+a)*v)
        recovered_v = (W-b)/(Z+a)
        numerator, denominator = sp.fraction(recovered_v)
        self.zero(numerator-(W-b))
        self.zero(denominator-(Z+a))
        self.zero(Z*numerator+a*numerator+denominator*(b-W))
        self.zero(numerator.subs(W, linear_W)-denominator*v)

        quadratic_W = v*Z+v**2
        quadratic = S**2+Z*S-W
        self.zero(quadratic.subs({S: v, W: quadratic_W}, simultaneous=True))
        self.assertEqual(sp.degree(quadratic, S), 2)
        self.zero((2*S+Z)**2-4*quadratic-(Z**2+4*W))
        other_root = -Z-v
        self.zero(other_root*Z+other_root**2-quadratic_W)
        self.zero(-Z-other_root-v)
        self.assertEqual(sp.degree(Z**2+4*W, W), 1)
        # The nonsquare/irreducibility and field-index conclusions require
        # the polynomial-ring argument, not a degree or Jacobian alone.

    def test_formal_index_eight_boundary_and_denominator(self):
        t = sp.Symbol("t", nonzero=True)
        rho, y, U, V, S, T, Z, W = sp.symbols("rho y U V S T Z W")
        k0 = -sp.Rational(2, 5)*t**4
        n0 = sp.Rational(2, 5)*t**5+t**2
        ell0 = sp.Rational(4, 7)*t**6+sp.Rational(7, 5)*t**3
        p3 = -t**2*sp.diff(k0, t, 3)/6-t*sp.diff(k0, t, 2)/2
        p2 = -t**2*sp.diff(n0, t, 2)/2-t*sp.diff(n0, t)
        b0 = t*ell0+t**2*sp.diff(ell0, t)
        delta = p3/(4*t)
        h = sp.diff(delta, t)
        self.zero(delta-t**2)
        self.zero(h-2*t)
        self.zero(p3-4*t**3)
        self.zero(p2+6*t**5+3*t**2)
        self.zero(b0-4*t**7-sp.Rational(28, 5)*t**4)
        self.zero(sp.diff(p3, t)-p3/t-4*t*h)
        self.zero(sp.diff(p2, t)-p2/t+3*p3*h+3*t)
        self.zero(sp.diff(b0, t)-b0/t+2*p2*h+t*sp.diff(k0, t, 2))

        k, ell = rho/t+k0, -rho/t**2+ell0
        P = -t*U**4+p3*U**3+p2*U**2+(rho/t+b0)*U+h*rho
        S_polynomial = sp.expand(
            sp.diff(P, t)+sp.diff(P, U)*sp.diff(P, rho)
            +t*(sp.diff(P, U)*(-U/t**2)+3*U**2
                +sp.diff(k, t, 2)*U-P/t**2+sp.diff(n0, t))
        )
        expected_S = 2*rho+8*t**8+sp.Rational(66, 5)*t**5+2*t**2
        self.zero(t**3*(S_polynomial-expected_S))
        self.assertNotEqual(expected_S, 0)
        theta = P.subs(U, y)
        z = 3*t*y**2+sp.diff(k, t)*y+theta/t+n0
        w = (t*ell-t*y**3-t*sp.diff(k, t, 2)*y**2/2
             +(y/t)*theta-t*sp.diff(n0, t)*y)
        G = sp.expand((1-y*h)*z+h*w)
        expected_G = (-y**4-4*t**2*y**3+2*t**4*y**2
                      -(sp.Rational(4, 5)*t**6+2*t**3)*y
                      +sp.Rational(8, 7)*t**8+sp.Rational(16, 5)*t**5+t**2)
        self.zero(t**3*(G-expected_G))
        f, g = y-1/(2*t), G/(2*t)
        self.zero(t**3*(w-f*z-g))
        self.zero(sp.diff(z, rho)-2)
        self.zero(2*t*(y-f)-1)

        P8 = (-y**4*V**8+(sp.Rational(1, 4)-y**3)*V**6
              -y*V**5/4+y**2*V**4/8+V**3/10-y*V**2/80+sp.Rational(1, 224))
        u = 1/(2*t)
        self.zero(t**8*(u**7*g-P8.subs(V, u)))
        self.assertEqual(sp.degree(P8, V), 8)
        self.zero(sp.Poly(P8, V).LC()+y**4)
        self.assertEqual(P8.subs(V, 0), sp.Rational(1, 224))
        self.assertEqual(sp.gcd(P8, V**7), 1)
        relation = sp.expand((y-S)**7*T-P8.subs(V, y-S))
        self.assertEqual(sp.Poly(relation, S, T).total_degree(), 8)
        self.zero(t**8*relation.subs({S: f, T: g}, simultaneous=True))
        transformed = sp.expand(relation.subs(T, W-Z*S))
        self.assertEqual(sp.degree(transformed, S), 8)
        self.zero(transformed.coeff(S, 8)-Z-y**4)
        # Coprimality and the rational return t=1/(2(y-f)) are the finite
        # algebra here. The exact index eight uses the written irreducibility
        # and pencil lemma, and means these are NOT actual frame data.


if __name__ == "__main__":
    unittest.main()
