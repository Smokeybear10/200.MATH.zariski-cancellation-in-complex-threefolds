"""Finite algebra controls for the cusp invariant-coordinate gate158.

Generic quadratic corrections check the actual polynomial normalization and
both inverse orders. Formal local-slice charts check an intercept identity,
not a claimed original polynomial coordinate frame. Polynomial composition
degrees and two actual boundary LNDs guard the hypotheses. Normality and the
universal integral-intercept argument remain written proof obligations.
No earlier checker is imported and no original157 example is rerun.
"""

import unittest

import sympy as sp


class CuspCubicGateControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    @staticmethod
    def deriv(expression, variables, coefficients):
        return sp.expand(sum(c*sp.diff(expression, v)
                             for v, c in zip(variables, coefficients)))

    def test_generic_actual_normalization_and_invariant_coordinate_inverse(self):
        X, Y, Z, W = original = sp.symbols("X Y Z W")
        x, y, z, w = normalized = sp.symbols("x y z w")
        lam, beta = sp.symbols("lam beta", nonzero=True)
        alpha = sp.symbols("alpha")
        q20, q11, q02, q10, q01, q00 = sp.symbols("q20 q11 q02 q10 q01 q00")
        Q = q20*X**2+q11*X*Y+q02*Y**2+q10*X+q01*Y+q00
        Qtilde = sp.expand(Q.subs({X: x-alpha/lam, Y: y}, simultaneous=True)/lam)
        remainder = Qtilde.subs(x, 0)
        quotient, rem = sp.div(Qtilde-remainder, x, x)
        self.zero(rem)
        self.zero(x*quotient+remainder-Qtilde)
        self.assertLessEqual(sp.Poly(quotient, x, y).total_degree(), 1)
        P = y**3-remainder
        self.assertEqual(sp.Poly(P, y).degree(), 3)
        self.zero(sp.Poly(P, y).LC()-1)

        forward = (X+alpha/lam, Y,
                   Z+quotient.subs({x: X+alpha/lam, y: Y}, simultaneous=True), W)
        inverse = (x-alpha/lam, y, z-quotient, w)
        for variable, expression in zip(original, inverse):
            self.zero(expression.xreplace(dict(zip(normalized, forward)))-variable)
        for variable, expression in zip(normalized, forward):
            self.zero(expression.xreplace(dict(zip(original, inverse)))-variable)
        H = lam*(X*Z-Y**3)+alpha*Z+Q
        self.zero(H.xreplace(dict(zip(original, inverse)))/lam-(x*z-P))
        self.zero(sp.Matrix(forward).jacobian(original).det()-1)

        # The affine correction has zero acceleration in two formal good slots.
        t, x0, y0, a, b = sp.symbols("t x0 y0 a b")
        self.zero(sp.diff(quotient.subs({x: x0+a*t, y: y0+b*t},
                                       simultaneous=True), t, 2))

        # If the fourth-coordinate coefficient is nonzero, this is a genuine
        # coordinate change irrespective of whether a derivation fixes H.
        I = sp.symbols("I")
        extended = H+beta*W
        replacement = (X, Y, Z, extended)
        reverse = (X, Y, Z, (I-H)/beta)
        destination = (X, Y, Z, I)
        for variable, expression in zip(original, reverse):
            self.zero(expression.xreplace(dict(zip(destination, replacement)))-variable)
        for variable, expression in zip(destination, replacement):
            self.zero(expression.xreplace(dict(zip(original, reverse)))-variable)
        self.zero(sp.Matrix(replacement).jacobian(original).det()-beta)

    def test_formal_intercept_and_polynomial_composition_degree(self):
        x, y, tau, T, Z, R = sp.symbols("x y tau T Z R")
        for degree in (2, 3, 4, 5):
            with self.subTest(degree=degree):
                P = T**degree+sum((i+1)*T**i for i in range(degree))
                shifted = sp.expand(P.subs(T, y+tau*x))
                intercept = P.subs(T, y)
                quotient, remainder = sp.div(shifted-intercept, x, x)
                self.zero(remainder)
                formal_H = sp.expand(x*quotient-shifted)
                self.zero(formal_H+intercept)
                self.zero(sp.diff(formal_H, x))
                self.assertEqual(sp.Poly(quotient, x).degree(), degree-1)
                # This is only a K[x] chart. x, y+tau*x, quotient are NOT
                # asserted to be independent original coordinate variables.
                self.zero((x*Z-shifted).subs(x, 0)+intercept)

                for z_degree in (0, 1, 2, 3):
                    inner = R if z_degree == 0 else R+Z**z_degree+Z**(z_degree-1)
                    composition = sp.expand(P.subs(T, inner))
                    self.assertEqual(sp.Poly(composition, Z).degree(),
                                     degree*z_degree)
                    self.assertNotEqual(degree*z_degree, 1)
                # These finite composition degrees support the degree check;
                # they do not prove the integrally-closed-ring inference.

    def test_actual_boundary_derivations_guard_both_hypotheses(self):
        X, Y, Z, W = variables = sp.symbols("X Y Z W")
        H_linear = X*Z-Y
        D = lambda f: self.deriv(f, variables, (1, Z, 0, 0))
        self.zero(D(H_linear))
        self.zero(D(X)-1)
        self.zero(D(D(X)))
        self.zero(D(D(Y)))
        for variable in variables:
            self.zero(D(D(variable)))
        # Genuine triangular LND with a slice and moving affine X:
        # degree(P)>=2 is the missing hypothesis in this boundary.

        cusp = X*Z-Y**3
        E = lambda f: self.deriv(f, variables, (0, X, 3*Y**2, 1))
        self.zero(E(cusp))
        self.zero(E(W)-1)
        self.zero(E(X))
        self.zero(E(E(Y)))
        self.zero(E(E(E(E(Z)))))
        self.zero(E(E(E(Z)))-6*X**2)
        # Genuine triangular LND with a global slice and nonlinear P:
        # EX!=0 fails, and Z has time degree three, not two.
        # A critical-line argument cannot exclude this actual invariant.


if __name__ == "__main__":
    unittest.main()
