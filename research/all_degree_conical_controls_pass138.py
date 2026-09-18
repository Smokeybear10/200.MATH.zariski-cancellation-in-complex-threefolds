"""Finite exact controls for the all-degree conical calculations in138.

Formal determinant jets and weighted coefficient functions in the first two
methods are not asserted to be actual coordinates. In particular the raw
Jacobian calculation retains y_v, and a v^2 example deliberately fails the
whole-line/unit-Jacobian premises. The weighted checks do not prove the
all-degree differential-field descent lemma.

The final method verifies actual polynomial inverse maps for three nonsliced
examples of bad time degrees 3,4,5. They have polynomial kernels and are not
cancellation counterexamples. No previous checker or solver is imported.
"""

import unittest

import sympy as sp


class AllDegreeConicalControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_raw_determinant_recurrence_before_whole_line(self):
        X, y, beta, alpha, r1 = sp.symbols("X y beta alpha r1")
        yt, yi, yv = sp.symbols("yt yi yv")
        C = beta*yt-alpha*yi
        for degree in (1, 2, 4):
            wv = sp.symbols(f"wv0:{degree+1}")
            wt = sp.symbols(f"wt0:{degree+1}")
            wi = sp.symbols(f"wi0:{degree+1}")
            Pv = sum(wv[j]*X**j for j in range(degree+1))
            Pt = sum(wt[j]*X**j for j in range(degree+1))
            Pi = sum(wi[j]*X**j for j in range(degree+1))
            matrix = sp.Matrix([
                [yt+X, yi, yv],
                [alpha+r1*yt+r1*X, beta+r1*yi, r1*yv],
                [Pt, Pi, Pv],
            ])
            determinant = sp.expand(matrix.det())
            self.assert_zero(determinant-(C+beta*X)*Pv-yv*(alpha*Pi-beta*Pt))
            polynomial = sp.Poly(determinant, X)
            for j in range(degree+2):
                previous = beta*wv[j-1] if j > 0 else 0
                current = C*wv[j]+yv*(alpha*wi[j]-beta*wt[j]) if j <= degree else 0
                self.assert_zero(polynomial.coeff_monomial(X**j)-previous-current)
            self.assert_zero(polynomial.coeff_monomial(X**(degree+1))-beta*wv[-1])

            # If w_j=P_j(y), these fixed-v jets contain the full chain terms.
            py = sp.symbols(f"py0:{degree+1}")
            pt = sp.symbols(f"pt0:{degree+1}")
            pi = sp.symbols(f"pi0:{degree+1}")
            chain = {}
            for j in range(degree+1):
                chain.update({wv[j]: py[j]*yv, wt[j]: pt[j]+py[j]*yt,
                              wi[j]: pi[j]+py[j]*yi})
            expected = beta*yv*sum(
                (X*py[j]-pt[j]+alpha*pi[j]/beta)*X**j
                for j in range(degree+1)
            )
            self.assert_zero(determinant.subs(chain, simultaneous=True)-expected)

        # Explicit pre-whole-line example: y=v^2, so its derivative is not in L*.
        # All chosen coefficients lie in L[y]; these data cannot generate L[v].
        tau, kappa, v = sp.symbols("tau kappa v")
        P = kappa*X**3+tau*y**2*X**2+kappa*y*X+y**3+tau
        Y = v**2+tau*X
        Z = 2*tau*v**2+kappa+tau**2*X
        W = P.subs(y, v**2)
        J = sp.Matrix([Y, Z, W]).jacobian([tau, kappa, v]).det()
        operator_P = X*sp.diff(P, y)-sp.diff(P, tau)+2*y*sp.diff(P, kappa)
        self.assert_zero(J-2*v*operator_P.subs(y, v**2))
        self.assert_zero(J.subs(v, 0))
        self.assertNotEqual(sp.expand(J-1), 0)

    def test_weighted_operator_indexing_with_variable_r(self):
        tau, kappa, X, y = sp.symbols("tau kappa X y")
        r = sp.Function("r")(tau)
        delta0 = lambda f: X*sp.diff(f, y)+r*y*sp.diff(f, kappa)
        for weight in range(8):
            current = [sp.Function(f"c{weight}_{i}")(tau, kappa)
                       for i in range(weight//2+1)]
            higher = [sp.Function(f"b{weight+1}_{i}")(tau, kappa)
                      for i in range((weight+1)//2+1)]
            Wn = sum(c*X**i*y**(weight-2*i) for i, c in enumerate(current))
            Wnext = sum(c*X**i*y**(weight+1-2*i) for i, c in enumerate(higher))
            residual = sp.Poly(sp.expand(delta0(Wn)-sp.diff(Wnext, tau)), X, y)
            for i in range((weight+1)//2+1):
                derivative = r*sp.diff(current[i], kappa) if i < len(current) else 0
                previous = (weight-2*i+2)*current[i-1] if i > 0 else 0
                target = derivative+previous-sp.diff(higher[i], tau)
                monomial = X**i*y**(weight+1-2*i)
                self.assert_zero(residual.coeff_monomial(monomial)-target)
            if weight % 2:
                # The final, pure-X coefficient is an additional compatibility equation.
                self.assert_zero(residual.coeff_monomial(X**((weight+1)//2))
                                 - current[-1]+sp.diff(higher[-1], tau))

        # Finite polynomial examples for genuinely variable r, not a constant-r shortcut.
        r0 = tau**2+1
        R = tau**3/3+tau
        S = tau**4/12+tau**2/2
        self.assert_zero(sp.diff(R, tau)-r0)
        self.assert_zero(sp.diff(S, tau)-R)
        self.assertNotEqual(sp.diff(r0, tau), 0)
        L = lambda f: X*sp.diff(f, y)-sp.diff(f, tau)+r0*y*sp.diff(f, kappa)
        A, B = y+tau*X, kappa+R*y+S*X
        self.assert_zero(L(A))
        self.assert_zero(L(B))
        for p, q in ((1, 2), (2, 3), (3, 4)):
            polynomial = sp.expand(-tau+A**p+B**q)
            self.assert_zero(L(polynomial)-1)
            terms = sp.Poly(polynomial, X, y)
            max_weight = max(2*i+j for (i, j), coefficient in terms.terms())
            for (i, j), coefficient in terms.terms():
                weight = 2*i+j
                self.assertLessEqual(sp.Poly(coefficient, kappa).degree(), max_weight-weight+i)
            self.assertLessEqual(sp.Poly(polynomial, kappa, X, y).total_degree(), max_weight)

    def test_actual_higher_degree_nonsliced_inverse_family(self):
        x, tau, xi, v = sp.symbols("x tau xi v")
        X, Y, Z, U = sp.symbols("X Y Z U")
        adapted, originals = (x, tau, xi, v), (X, Y, Z, U)
        good_Y = 2*v+tau*x
        good_Z = 4*tau*v+xi+tau**2*x
        old_W = -tau/2+v*x+tau*x**2/2
        E = lambda f: sp.expand(xi*sp.diff(f, x))
        T = lambda f: sp.expand(-2*sp.diff(f, tau)+8*v*sp.diff(f, xi)+x*sp.diff(f, v))
        for ell in (3, 4, 5):
            forward = sp.Matrix([x, good_Y, good_Z, old_W+good_Y**ell])
            inverse_tau = X*Y-2*(U-Y**ell)
            inverse_v = (Y-inverse_tau*X)/2
            inverse_xi = Z-2*inverse_tau*Y+inverse_tau**2*X
            inverse = sp.Matrix([X, inverse_tau, inverse_xi, inverse_v])
            for value, expected in zip(inverse, adapted):
                self.assert_zero(value.subs(dict(zip(originals, forward)), simultaneous=True)-expected)
            for value, expected in zip(forward, originals):
                self.assert_zero(value.subs(dict(zip(adapted, inverse)), simultaneous=True)-expected)
            self.assert_zero(forward.jacobian(adapted).det()-1)
            self.assertEqual(sp.Poly(sp.expand(forward[3]), x).degree(), ell)
            self.assert_zero(xi**ell*sp.diff(forward[3], x, ell)
                             - sp.factorial(ell)*xi**ell*tau**ell)
            self.assert_zero(xi**(ell+1)*sp.diff(forward[3], x, ell+1))
            self.assertEqual(sp.Matrix([E(f) for f in forward[:3]]),
                             sp.Matrix([xi, xi*tau, xi*tau**2]))
            for f in forward[:3]:
                self.assert_zero(E(E(f)))

            # The derivative ideal is still exactly (xi), not the unit ideal.
            self.assert_zero(E(forward[0])-xi)
            for f in forward:
                self.assert_zero(E(f).subs(xi, 0))
            invariant = forward[3]-forward[1]**ell-forward[0]*forward[1]/2
            self.assert_zero(invariant+tau/2)
            self.assert_zero(E(invariant))
            for j, f in enumerate(forward):
                self.assert_zero(T(f)-(1 if j == 3 else 0))


if __name__ == "__main__":
    unittest.main()
