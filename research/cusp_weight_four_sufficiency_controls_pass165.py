"""Independent finite controls for the conditional weight-four criterion165.

All-constant formal chart identities do not assert realization of arbitrary
coefficient data. Euler identities do not prove the joint-constant-field
theorem, normality, or universal invariant existence. Polynomial changes and
their inverses are checked separately, using only nonzero complex constants.
No solver or earlier checker is imported, and no older tests are rerun.
"""

import math
import unittest

import sympy as sp


def normalized_data(t, X, Y):
    h, j, b, c, q, e, f, g, i, Lam = sp.symbols("h j b c q e f g i Lambda")
    k0 = -h*t**3-4*j*t**2+b*t+c+q/t
    n0 = h**2*t**3+(4*h*j+1)*t**2+(6*j**2-Lam)*t+e+f/t
    ell0 = (h**3*t**3+(4*h**2*j+2*h)*t**2
            +(6*h*j**2-h*Lam+4*j)*t+g+i/t-q/t**2)
    Q = (q*X**3+c*X**2*Y+b*X*Y**2-4*j*Y**3
         +(f+h*q)*X**2+(e+h*c)*X*Y+(6*j**2-Lam+h*b)*Y**2
         -(i+c-h*f)*X-(g+b-h*e)*Y)
    return (h, j, b, c, q, e, f, g, i, Lam), k0, n0, ell0, Q


class CuspWeightFourSufficiencyControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_all_constant_invariant_and_its_coordinate_inverse(self):
        X, Y, Z, W, y, rho, theta, d0 = sp.symbols("X Y Z W y rho theta d0")
        t = sp.Symbol("t", nonzero=True)
        constants, k0, n0, ell0, Q = normalized_data(t, X, Y)
        h, j, b, c, q, e, f, g, i, Lam = constants
        k, ell = rho/t+k0, -rho/t**2+ell0
        chart_Y = y+t*X
        z = 3*t*y**2+sp.diff(k, t)*y+theta/t+n0
        chart_Z = z+(3*t**2*y+k)*X+t**3*X**2
        w = (t*ell-t*y**3-t*sp.diff(k, t, 2)*y**2/2
             +(y/t)*theta-t*sp.diff(n0, t)*y)
        chart_W = w+theta*X+rho*X**2
        H = X*Z-Y**3
        invariant = -Y*H+(X+h)*W+(1-h*Y)*Z+Q
        transported = sp.expand(invariant.xreplace(
            {Y: chart_Y, Z: chart_Z, W: chart_W}
        ))
        # theta is independent here. Thus no special graph constant or
        # numerical parameter choice hides a positive-time coefficient.
        for power in (3, 2, 1):
            self.zero(t**4*transported.coeff(X, power))
        self.zero(t**4*sp.diff(transported, X))
        self.zero(t**4*(transported-transported.subs(X, 0)))

        p3 = -t**2*sp.diff(k0, t, 3)/6-t*sp.diff(k0, t, 2)/2
        p2 = -t**2*sp.diff(n0, t, 2)/2-t*sp.diff(n0, t)
        b0 = t*ell0+t**2*sp.diff(ell0, t)
        graph = -t*y**4+p3*y**3+p2*y**2+(rho/t+b0)*y+h*rho+d0
        projected = sp.expand(transported.subs(X, 0).subs(theta, graph))
        self.zero(t**4*(projected-n0-d0/t-h*t*ell0))
        self.zero(t**4*sp.diff(projected, rho))
        self.zero(t**4*sp.diff(projected, y))
        # d0 is retained as an arbitrary rho-constant coefficient, not zero.
        self.zero(t*sp.diff(projected, d0)-1)

        I, J = sp.symbols("I J")
        companion = W-Y*Z
        inverse_Z = I-(X+h)*J-Y**4-Q
        inverse_W = J+Y*inverse_Z
        back = {Z: inverse_Z, W: inverse_W}
        self.zero(invariant.xreplace(back)-I)
        self.zero(companion.xreplace(back)-J)
        self.zero(inverse_Z.xreplace({I: invariant, J: companion})-Z)
        self.zero(inverse_W.xreplace({I: invariant, J: companion})-W)
        weights = (1, 1, 2, 2)
        terms = sp.Poly(invariant, X, Y, Z, W).terms()
        degree = max(sum(a*b for a, b in zip(e, weights)) for e, c in terms)
        self.assertEqual(degree, 4)
        top = sum(c*sp.prod(a**b for a, b in zip((X, Y, Z, W), e))
                  for e, c in terms if sum(a*b for a, b in zip(e, weights)) == 4)
        self.zero(top+Y*H)
        self.assertNotEqual(sp.expand(top), 0)

    def test_Euler_equations_and_algebraic_field_boundary(self):
        t = sp.Symbol("t", nonzero=True)
        X, Y = sp.symbols("X Y")
        constants, k0, n0, ell0, Q = normalized_data(t, X, Y)
        h, j, b, c, q, e, f, g, i, Lam = constants
        p3 = -t**2*sp.diff(k0, t, 3)/6-t*sp.diff(k0, t, 2)/2
        p2 = -t**2*sp.diff(n0, t, 2)/2-t*sp.diff(n0, t)
        b0 = t*ell0+t**2*sp.diff(ell0, t)
        R = -6*(h*t+j)**2-3*t+Lam
        self.zero(t**4*(p3-4*h*t**2-4*j*t))
        self.zero(t**4*(sp.diff(p3, t)-p3/t-4*t*h))
        self.zero(t**4*(p2-t*R))
        self.zero(t**4*(sp.diff(p2, t)-p2/t+3*p3*h+3*t))
        self.zero(t**4*(sp.diff(b0, t)-b0/t+2*p2*h+t*sp.diff(k0, t, 2)))
        forcing_n = 12*h**2*t**2+(24*h*j+6)*t+12*j**2-2*Lam
        forcing_ell = (12*h**3*t**2+(24*h**2*j+12*h)*t
                       +12*h*j**2-2*h*Lam+8*j-2*q/t**3)
        self.zero(t**4*(t*sp.diff(n0, t, 2)+2*sp.diff(n0, t)-forcing_n))
        self.zero(t**4*(t*sp.diff(ell0, t, 2)+2*sp.diff(ell0, t)-forcing_ell))

        F0, F1, F2 = sp.symbols("F0 F1 F2")
        total_dt = lambda expression: sp.diff(expression, t)+F1*sp.diff(expression, F0)+F2*sp.diff(expression, F1)
        self.zero(total_dt(t**2*F1)-t*(t*F2+2*F1))
        A, B = sp.symbols("A B")
        homogeneous = A+B/t
        self.zero(t**3*(t*sp.diff(homogeneous, t, 2)+2*sp.diff(homogeneous, t)))

        # Proper algebraic extension K=C(z), t=z^2. The coefficient
        # derivation is (1/(2z))*d/dz, not d/dz. These tests do not prove
        # the exact-constant-field assertion used for completeness in the note.
        z = sp.Symbol("z", nonzero=True)
        dt = lambda expression: sp.diff(expression, z)/(2*z)
        algebraic_homogeneous = A+B/z**2
        self.zero(z**6*(z**2*dt(dt(algebraic_homogeneous))+2*dt(algebraic_homogeneous)))
        self.zero(z**4*dt(algebraic_homogeneous)+B)
        self.zero(2*z*dt(z)-1)
        # The algebraic element z has half-integer Euler degree. It does
        # not solve the homogeneous equation merely by being algebraic.
        failure = sp.expand(z**2*dt(dt(z))+2*dt(z))
        self.zero(4*z*failure-3)
        self.assertNotEqual(failure, 0)

    def test_actual_constant_reframe_and_literal_scaling(self):
        X, Y, Z, W, Xp, Yp, Zp, Wp = sp.symbols("X Y Z W Xp Yp Zp Wp")
        A, eta = sp.symbols("A eta", nonzero=True)
        B, C = sp.symbols("B C")
        xi, theta, omega = eta/A, eta*B/A, eta**3
        forward = (xi*X, eta*Y+theta*X,
                   (eta**3*Z+3*eta**2*theta*Y**2
                    +3*eta*theta**2*X*Y+theta**3*X**2)/xi,
                   omega*W)
        self.zero(A**4*(forward[0]*forward[2]-forward[1]**3-eta**3*(X*Z-Y**3)))
        recovered_X = sp.expand(forward[0]/xi)
        recovered_Y = sp.expand((forward[1]-theta*recovered_X)/eta)
        recovered_W = sp.expand(forward[3]/omega)
        recovered_Z = sp.expand((xi*forward[2]-3*eta**2*theta*recovered_Y**2
            -3*eta*theta**2*recovered_X*recovered_Y-theta**3*recovered_X**2)/eta**3)
        for got, want in zip((recovered_X, recovered_Y, recovered_Z, recovered_W), (X, Y, Z, W)):
            self.zero(A**4*eta**3*(got-want))
        inverse_X = Xp/xi
        inverse_Y = (Yp-theta*inverse_X)/eta
        inverse_Z = (xi*Zp-3*eta**2*theta*inverse_Y**2
            -3*eta*theta**2*inverse_X*inverse_Y-theta**3*inverse_X**2)/eta**3
        inverse_W = Wp/omega
        substitution = dict(zip((X, Y, Z, W), (inverse_X, inverse_Y, inverse_Z, inverse_W)))
        for expression, wanted in zip(forward, (Xp, Yp, Zp, Wp)):
            self.zero(A**4*eta**4*(expression.xreplace(substitution)-wanted))

        tau, rho, r, lam, ell, lt, lr = sp.symbols("tau rho r lam ell lt lr")
        U, V, Uh, Vh = sp.symbols("U V Uh Vh")
        K2, K3 = sp.symbols("k20 k11 k02"), sp.symbols("k30 k21 k12 k03")
        N1, N2 = sp.symbols("n10 n01"), sp.symbols("n20 n11 n02")

        def H(jets, degree, first, second, scale=sp.S.One, change=False):
            result = 0
            for j, coefficient in enumerate(jets):
                i = degree-j
                factor = scale/(A**i*(eta*A**2)**j) if change else sp.S.One
                result += factor*coefficient*first**i*second**j/(math.factorial(i)*math.factorial(j))
            return result

        old_f = U**3+H(K2, 2, U, V)+H(N1, 1, U, V)
        new_f = Uh**3+H(K2, 2, Uh, Vh, eta*A**2, True)+H(N1, 1, Uh, Vh, eta**2*A, True)
        old_phi = sp.diff(old_f, V)*(ell-old_f)/r+H(K3, 3, U, V)+H(N2, 2, U, V)-lt*U-lr*V
        new_phi = (sp.diff(new_f, Vh)*(eta**3*ell-new_f)/r
            +H(K3, 3, Uh, Vh, eta*A**2, True)+H(N2, 2, Uh, Vh, eta**2*A, True)
            -(eta**3/A)*lt*Uh-(eta**2/A**2)*lr*Vh)
        evaluate = {Uh: eta*U, Vh: eta**2*A*V}
        self.zero(A**6*r*(new_f.xreplace(evaluate)-eta**3*old_f))
        self.zero(A**6*r*(new_phi.xreplace(evaluate)-(eta**4/A)*old_phi))
        # D=A^2/eta^2 implements eta^2=A^2/D without choosing a branch.
        D = A**2/eta**2
        old_r = 1/(A*tau+B)
        old_lambda = D*old_r**2
        self.zero((A*tau+B)**2*(xi**2*old_lambda-old_r**2))
        self.zero((eta*tau+theta)/xi-A*tau-B)
        self.zero(omega*rho/xi**2-eta*A**2*rho)

        # Signed constant translation Ynew=Yold+epsilon. These equations
        # use old y=new y-epsilon; the sign on k_t is therefore negative.
        t = sp.Symbol("t", nonzero=True)
        y, eps, kval, kt, nval, th = sp.symbols("y eps kval kt nval th")
        new_k = kval-3*t**2*eps
        new_n = nval+3*t*eps**2-eps*kt
        old_z = 3*t*(y-eps)**2+kt*(y-eps)+th/t+nval
        new_z = 3*t*y**2+(kt-6*t*eps)*y+th/t+new_n
        self.zero(old_z-new_z)
        self.zero(3*t**2*(y-eps)+kval-3*t**2*y-new_k)
        Cnew = eta*C/A
        shifted_s = Cnew/t**2-(-Cnew)*sp.diff(1/t, t)
        self.zero(A*t**2*shifted_s)
        self.zero((Y+eps)-eps-Y)


if __name__ == "__main__":
    unittest.main()
