"""Finite exact controls for the conditional cubic-graph square obstruction244.

These verify coefficient identities, polynomial primitive formulas, both
orders of the actual affine maps, and the complete original-coordinate square
identity.  They do not prove the actual cofactor premise, finite-field constant
theorem, completeness of integration, normality, or the universal odd-degree
square argument.  Those remain written proof inputs.  Lambda is never assumed
constant under coefficient derivatives or regular in the original ring.
No retained proof, checker, or solver is imported; no whole-model claim.
"""

import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, zeta, y, h = sp.symbols("U V zeta y h")
X, Y, Z, W = sp.symbols("X Y Z W")
x1, y1, z1, w1 = sp.symbols("X1 Y1 Z1 W1")
lam = sp.Symbol("lambda", nonzero=True)
a, b, c, d, e, f0, g0, j, k0, k1 = sp.symbols("a b c d e f g j k0 k1")
m = sp.Symbol("m")


def clean(expression):
    return sp.cancel(sp.expand(expression))


def primitives():
    k = c*rho**2/2+(a*t+b)*rho-c*t**3/4+d*t**2/2+k1*t+k0
    n = 3*c**2*rho**2/16+(c*a*t/2+e)*rho-c**2*t**3/16 \
        +(a**2/4+c*d/8)*t**2+f0*t+g0
    ell = c**3*t**3/64-(c*a**2/8+c**2*d/32)*t**2 \
        +(-3*a*c**2*rho/16-a*e/2-c*f0/4+c*a*b/8)*t \
        -c**3*rho**2/16+(b*c**2/16-c*e/2)*rho+j
    return k, n, ell


def constants_for_affine_map():
    n0 = g0-b**2/4+c*k0/4+d*k1/6
    B0 = f0-a*b/2+d**2/12
    C0 = -a*b*d/12+b**2*c/8-b*e/2+d**3/108+d*f0/6-j
    return n0, B0, C0


def affine_maps():
    n0, _, _ = constants_for_affine_map()
    forward = (X-c/4, Y-d/6,
               Z-k1*(Y-d/6)-k0*(X-c/4)-n0,
               W+a*Y/2+b*X/2-b*c/4+e/2)
    inverse = (x1+c/4, y1+d/6, z1+k1*y1+k0*x1+n0,
               w1-a*(y1+d/6)/2-b*(x1+c/4)/2+b*c/4-e/2)
    return forward, inverse


def raw_jet_eliminant():
    K = {(i, j): sp.Symbol(f"k{i}{j}") for i in range(4) for j in range(4-i)}
    N = {(i, j): sp.Symbol(f"n{i}{j}") for i in range(3) for j in range(3-i)}
    L = {(i, j): sp.Symbol(f"ell{i}{j}") for i in range(2) for j in range(2-i)}
    def jet(table, degree):
        return sum(table[i, degree-i]*U**i*V**(degree-i)
                   / (sp.factorial(i)*sp.factorial(degree-i)) for i in range(degree+1))
    eps = sp.Symbol("eps")
    shifted_q = sp.expand((rho+eps*V)**2-(t+eps*U)**3)
    f = shifted_q.coeff(eps, 2)+jet(K, 1)+N[0, 0]
    S = shifted_q.coeff(eps, 3)+jet(K, 2)+jet(N, 1)
    Q = shifted_q.coeff(eps, 4)+jet(K, 3)+jet(N, 2) \
        -L[1, 0]*U-L[0, 1]*V-m
    R = sp.diff(f, V)
    beta = sum(sp.diff(f, K[i, j])*K[i, j+1]
               for i, j in K if (i, j+1) in K) \
        + sum(sp.diff(f, N[i, j])*N[i, j+1]
              for i, j in N if (i, j+1) in N)
    T = L[0, 0]-S
    H = sp.expand((T**2+R*beta*T+R**2*Q).subs(V, zeta-K[0, 1]/2))
    p = sp.expand(S.subs(V, -K[0, 1]/2)-L[0, 0])
    return K, N, L, H, p


def literal_chart():
    k, n, ell = primitives()
    kappa = sp.diff(k, rho)
    p = -y**3+sp.diff(k, t, 2)*y**2/2 \
        +(sp.diff(n, t)-kappa*sp.diff(k, t, rho)/2)*y \
        +kappa**2*sp.diff(k, rho, 2)/8-kappa*sp.diff(n, rho)/2-ell
    P = p/lam
    theta = P-kappa/2
    w = -lam/2-(a*y+sp.diff(n, rho)-kappa*c/2)/2-c*P/4
    z = 2*rho*w+P**2-kappa**2/4-3*t*y**2+sp.diff(k, t)*y+n
    sigma = -3*t**2*y+2*rho*theta+k
    return p, (X, y+t*X, z+sigma*X+(rho**2-t**3)*X**2,
               w+theta*X+rho*X**2)


class RepeatedRootCubicGraphControls244(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_arbitrary_lower_jets_and_all_polynomial_primitive_identities(self):
        k, n, ell = primitives()
        kappa, cc, aa = sp.diff(k, rho), sp.diff(k, rho, 2), sp.diff(k, t, rho)
        residuals = [sp.diff(k, rho, 3), sp.diff(k, t, rho, 2),
                     sp.diff(n, rho, 2)-3*cc**2/8, sp.diff(k, t, 2, rho),
                     sp.diff(n, t, rho)-cc*aa/2, sp.diff(k, t, 3)+3*cc/2,
                     sp.diff(n, t, 2)-aa**2/2-cc*sp.diff(k, t, 2)/4,
                     sp.diff(ell, rho)-kappa*cc**2/16+cc*sp.diff(n, rho)/2,
                     sp.diff(ell, t)+aa*sp.diff(n, rho)/2+cc*sp.diff(n, t)/4-kappa*cc*aa/8]
        for residual in residuals:
            self.assertZero(residual)
        recovered = [cc-c, aa-a, sp.diff(k, t, 2)+3*c*t/2-d,
                     kappa-c*rho-a*t-b,
                     sp.diff(k, t)-a*rho+3*c*t**2/4-d*t-k1,
                     sp.diff(n, rho)-3*c**2*rho/8-c*a*t/2-e,
                     sp.diff(n, t)-c*a*rho/2+3*c**2*t**2/16-(a**2/2+c*d/4)*t-f0]
        for residual in recovered:
            self.assertZero(residual)

        K, N, L, H, p = raw_jet_eliminant()
        substitutions = {}
        for table, primitive in ((K, k), (N, n), (L, ell)):
            substitutions.update({symbol: sp.diff(primitive, t, i, rho, j)
                                  for (i, j), symbol in table.items()})
        remainder = sp.Poly(sp.expand(H-p**2), U, zeta)
        scalar_z2 = None
        for powers, coefficient in remainder.terms():
            evaluated = clean(coefficient.subs(substitutions, simultaneous=True))
            if powers == (0, 2):
                scalar_z2 = evaluated
            else:
                self.assertZero(evaluated)
        self.assertIsNotNone(scalar_z2)
        self.assertZero(sp.diff(scalar_z2, m)+4)
        m_solution = (scalar_z2.subs(m, 0)+lam**2)/4
        self.assertZero(scalar_z2.subs(m, m_solution)+lam**2)
        # This completes the formal scalar coefficient only. No extra differential
        # equation or constancy assumption on lambda is imposed.

    def test_both_orders_of_the_actual_complex_affine_coordinate_map(self):
        forward, inverse = affine_maps()
        for actual, expected in zip(forward, (x1, y1, z1, w1)):
            self.assertZero(actual.subs(dict(zip((X, Y, Z, W), inverse)), simultaneous=True)-expected)
        for actual, expected in zip(inverse, (X, Y, Z, W)):
            self.assertZero(actual.subs(dict(zip((x1, y1, z1, w1), forward)), simultaneous=True)-expected)
        self.assertZero(sp.Matrix(forward).jacobian((X, Y, Z, W)).det()-1)
        self.assertZero(sp.Matrix(inverse).jacobian((x1, y1, z1, w1)).det()-1)
        # All integration constants are unconstrained symbols, including zero.
        zero_constants = {symbol: 0 for symbol in (a, b, c, d, e, f0, g0, j, k0, k1)}
        for actual, expected in zip(forward, (X, Y, Z, W)):
            self.assertZero(actual.subs(zero_constants)-expected)

    def test_full_literal_chart_transports_to_all_three_normalized_entries(self):
        p, chart = literal_chart()
        n0, B0, C0 = constants_for_affine_map()
        p0 = -h**3+B0*h+C0
        P0 = p0/lam
        shift = {X: x1+c/4, y: h-c*t/4+d/6}
        self.assertZero(p.subs(shift, simultaneous=True)-p0)
        forward, _ = affine_maps()
        pulled_back = [clean(value.subs(dict(zip((X, Y, Z, W), chart)), simultaneous=True)
                             .subs(shift, simultaneous=True)) for value in forward]
        expected_Y = h+t*x1
        expected_W = -lam/2+P0*x1+rho*x1**2
        expected_Z = -rho*lam+P0**2-3*t*h**2+B0*t \
            +(-3*t**2*h+2*rho*P0)*x1+(rho**2-t**3)*x1**2
        for actual, expected in zip(pulled_back, (x1, expected_Y, expected_Z, expected_W)):
            self.assertZero(actual-expected)
        # Verify the square directly in the pulled-back original affine entries,
        # retaining every complex constant and the nonzero field symbol lambda.
        xx, yy, zz, ww = pulled_back
        original_expression = xx**2*zz-ww**2+xx*yy**3-B0*xx*yy-C0*xx
        self.assertZero(original_expression+lam**2/4)

    def test_complete_square_cancellation_and_odd_coordinate_degree_boundaries(self):
        B0, C0 = sp.symbols("B0 C0")
        p0 = -h**3+B0*h+C0
        P0 = p0/lam
        YY = h+t*x1
        WW = -lam/2+P0*x1+rho*x1**2
        ZZ = -rho*lam+P0**2-3*t*h**2+B0*t \
            +(-3*t**2*h+2*rho*P0)*x1+(rho**2-t**3)*x1**2
        F = x1**2*ZZ-WW**2+x1*YY**3-B0*x1*YY-C0*x1
        self.assertZero(F+lam**2/4)
        # Omitting -rho*lambda from the projected Z intercept destroys the identity.
        wrong = F+rho*lam*x1**2
        self.assertZero(wrong+lam**2/4-rho*lam*x1**2)
        self.assertNotEqual(clean(wrong+lam**2/4), 0)

        ambient_F = x1**2*z1-w1**2+x1*y1**3-B0*x1*y1-C0*x1
        squared_candidate = -4*ambient_F
        self.assertEqual(sp.degree(squared_candidate, z1), 1)
        self.assertZero(sp.Poly(squared_candidate, z1).coeff_monomial(z1)+4*x1**2)
        self.assertNotEqual(sp.Poly(squared_candidate, z1).coeff_monomial(z1), 0)
        # A special coordinate fiber masks the global odd-degree obstruction.
        self.assertZero(squared_candidate.subs(x1, 0)-(2*w1)**2)
        self.assertEqual(sp.degree(squared_candidate.subs(x1, 0), z1), 0)
        # Finite leading-term fixtures illustrate, but do not prove, the general
        # integral-domain degree-of-a-square fact used in the written argument.
        r0, r1, r2 = sp.symbols("r0 r1 r2")
        square = sp.expand((r2*z1**2+r1*z1+r0)**2)
        self.assertEqual(sp.degree(square, z1), 4)
        self.assertZero(sp.Poly(square, z1).coeff_monomial(z1**4)-r2**2)
        self.assertEqual(sp.degree(square.subs(r2, 0), z1), 2)
        self.assertEqual(sp.degree(square.subs({r2: 0, r1: 0}), z1), 0)


if __name__ == "__main__":
    unittest.main()
