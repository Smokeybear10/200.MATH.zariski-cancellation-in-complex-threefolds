"""Three finite controls for the minimal quadratic local-slice proof.

The exact model is pi**n*Z = T**2-u, with residue field C(u)[sqrt(u)].
Finite residue-linear corrections, derivative stopping, explicit
coordinate inverses and bounded residue independence are checked.
No finite calculation represents the universal saturation argument.
"""

import unittest

import sympy as sp


pi, u, T, Z, X, Y, W = sp.symbols("pi u T Z X Y W")


def clean(value):
    return sp.cancel(sp.expand(value))


def normal(value, n):
    """Monic T-remainder in the stated exact quadratic model."""
    return clean(sp.rem(sp.expand(value), T**2-u-pi**n*Z, T))


def valuation(value):
    """Exact pi-order of a nonzero polynomial with symbolic coefficients."""
    polynomial = sp.Poly(sp.expand(value), pi)
    if polynomial.is_zero:
        raise ValueError("The test requires a nonzero polynomial.")
    return min(monomial[0] for monomial, coefficient in polynomial.terms()
               if coefficient != 0)


def derive(value, n):
    return normal(pi**n*sp.diff(value, T)+2*T*sp.diff(value, Z), n)


def lift_case(n):
    shift = 1+pi+pi**2+2*pi**(n+1)
    r = T+shift
    initial = ((X-1)**2-u+pi*(X+u)
               +pi**2*(2*X-u)+pi**3*(3*X+2*u))
    P = sp.expand(initial)
    history = []
    while True:
        evaluated = normal(P.subs(X, r), n)
        order = valuation(evaluated)
        if order >= n:
            break
        residue = clean(evaluated/pi**order).subs(pi, 0)
        if sp.degree(residue, T) > 1 or residue.has(Z):
            raise ValueError("Residue-linear correction hypothesis failed.")
        alpha = sp.expand(residue).coeff(T, 1)
        beta = clean(residue.subs(T, 0)-alpha*shift.subs(pi, 0))
        next_P = sp.expand(P-pi**order*(alpha*X+beta))
        next_order = valuation(normal(next_P.subs(X, r), n))
        history.append((order, next_order, alpha, beta, P, next_P))
        P = next_P
        if len(history) > n:
            raise ValueError("Finite correction did not terminate.")
    corrected_Y = clean(evaluated/pi**n)
    return shift, r, initial, P, corrected_Y, history


class MinimalQuadraticSliceChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = {n: lift_case(n) for n in range(1, 7)}

    def assertZero(self, value):
        self.assertEqual(clean(value), 0)

    def test_finite_monic_quadratic_corrections_reach_exact_valuation(self):
        for n, case in self.cases.items():
            shift, r, initial, P, corrected_Y, history = case
            self.assertEqual(sp.Poly(P, X).degree(), 2)
            self.assertEqual(sp.Poly(P, X).LC(), 1)
            self.assertZero(P.subs(pi, 0)-((X-1)**2-u))
            self.assertLessEqual(len(history), n-1)
            for order, next_order, alpha, beta, before, after in history:
                self.assertGreaterEqual(order, 1)
                self.assertLess(order, n)
                self.assertGreater(next_order, order)
                self.assertLessEqual(next_order, n)
                self.assertZero(after-before+pi**order*(alpha*X+beta))
                residue = clean(normal(before.subs(X, r), n)
                                /pi**order).subs(pi, 0)
                self.assertZero(residue-alpha*r.subs(pi, 0)-beta)
                self.assertEqual(sp.Poly(after, X).LC(), 1)
            self.assertEqual(valuation(normal(P.subs(X, r), n)), n)
            self.assertZero(normal(P.subs(X, r)-pi**n*corrected_Y, n))
            self.assertFalse(sp.denom(corrected_Y).has(pi, T, Z, u))
            # The resulting generator contains the full original Z
            # with coefficient one; it was not imposed on the iteration.
            self.assertEqual(sp.diff(corrected_Y, Z), 1)

    def test_derivative_stopping_uses_separable_nonzero_residue(self):
        residue_polynomial = (X-1)**2-u
        residue_derivative = sp.diff(residue_polynomial, X)
        self.assertEqual(sp.gcd(residue_polynomial, residue_derivative, X), 1)
        for n, case in self.cases.items():
            shift, r, initial, P, corrected_Y, history = case
            derivative_P = sp.diff(P, X).subs(X, r)
            self.assertZero(derive(P.subs(X, r), n)-pi**n*derivative_P)
            self.assertZero(derive(corrected_Y, n)-derivative_P)
            self.assertZero(derivative_P.subs(pi, 0)-2*T)
            self.assertEqual(valuation(pi**n*derivative_P), n)
            # In the actual residue field, (2T)^(-1)=T/(2u).
            self.assertZero(sp.rem(2*T*T/(2*u)-1, T**2-u, T))
            # If P(r) lay in pi^(n+1)A, D(P(r)) would as well.
            # Its displayed order n is the finite stopping obstruction.
            self.assertNotEqual(clean(pi**n*derivative_P/pi**n)
                                .subs(pi, 0), 0)
            # A deliberately nonminimal slice and inseparable/repeated
            # residue polynomial do not satisfy that argument's premises.
            bad_r = pi**(n+1)*T
            bad_value = normal(bad_r**2, n)
            bad_slice_order = valuation(derive(bad_r, n))
            self.assertEqual(bad_slice_order, 2*n+1)
            self.assertEqual(valuation(bad_value), 2*n+2)
            self.assertEqual((2*bad_r).subs(pi, 0), 0)
        self.assertNotEqual(sp.gcd(residue_polynomial.subs(u, 0),
                                  residue_derivative, X), 1)
        # This last specialization has a repeated residue root and is
        # expressly not the degree-two field in the theorem.

    def test_actual_inverse_full_residue_and_missing_saturation_control(self):
        for n, case in self.cases.items():
            shift, r, initial, P, corrected_Y, history = case
            correction = clean(corrected_Y-Z)
            self.assertLessEqual(sp.degree(correction, T), 1)
            self.assertFalse(correction.has(Z))
            inverse_T = X-shift
            inverse_Z = Y-correction.subs(T, inverse_T)
            self.assertZero(inverse_T.subs(
                {X: r, Y: corrected_Y}, simultaneous=True)-T)
            self.assertZero(inverse_Z.subs(
                {X: r, Y: corrected_Y}, simultaneous=True)-Z)
            self.assertZero(r.subs(
                {T: inverse_T, Z: inverse_Z}, simultaneous=True)-X)
            self.assertZero(corrected_Y.subs(
                {T: inverse_T, Z: inverse_Z}, simultaneous=True)-Y)
            # Exact relation transport, before taking any quotient.
            self.assertZero((pi**n*Y-P).subs(
                {X: r, Y: corrected_Y}, simultaneous=True)
                            -(pi**n*Z-T**2+u))
            self.assertZero((pi**n*Z-T**2+u).subs(
                {T: inverse_T, Z: inverse_Z}, simultaneous=True)
                            -(pi**n*Y-P))
            # A bounded independent residue-basis check. The actual
            # triangular inverse above gives the full coordinate claim.
            rbar, ybar = r.subs(pi, 0), corrected_Y.subs(pi, 0)
            monomials = [T**i*Z**j for j in range(4) for i in range(2)]
            images = [sp.rem(rbar**i*ybar**j, T**2-u, T)
                      for j in range(4) for i in range(2)]
            matrix = sp.Matrix([[sp.Poly(sp.expand(image), T, Z)
                                 .coeff_monomial(monomial)
                                 for image in images]
                                for monomial in monomials])
            self.assertEqual(clean(matrix.det()), 1)
            # Generic equality alone is insufficient: H_bad=R[T,pi Z]
            # has H_bad[1/pi]=A[1/pi], but W=pi Z survives in H_bad/pi
            # while mapping to zero in A/pi.
            relation_bad = pi**(n-1)*W-T**2+u
            self.assertZero(normal(relation_bad.subs(W, pi*Z), n))
            residue_bad = relation_bad.subs(pi, 0)
            if n == 1:
                surviving = sp.rem(W, residue_bad, W)
                self.assertZero(surviving-(T**2-u))
            else:
                surviving = sp.rem(W, residue_bad, T)
                self.assertEqual(surviving, W)
            self.assertNotEqual(surviving, 0)
            self.assertEqual((pi*Z).subs(pi, 0), 0)
            # These explicit rings illustrate the missing injection;
            # they are not a finite proof of arbitrary saturation.


if __name__ == "__main__":
    unittest.main()
