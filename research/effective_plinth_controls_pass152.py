"""Finite controls for the effective selected-plinth bound.

The first method is coefficient-field arithmetic only. Its rational partials
are not asserted to arise from an actual selected frame. It tests several
ordered derivative words and an exact sharp pole recurrence, not the universal
valuation theorem.

The second method reorders the actual coefficient-cover family140. It checks
two-sided polynomial inverses, its actual selected partial, signed tail, and
global primitive slice for n=2,3. The speed-ratio critical divisor is
noncontracted, but mu=0 because W-X=-b. It is not a selected nonslice example,
a full divisor constant extension, or a test of the unresolved mu>=3 case.
No earlier checker, search implementation, or solver is imported.
"""

import itertools
import math
import unittest

import sympy as sp


class EffectivePlinthControls(unittest.TestCase):
    def zero(self, expression):
        numerator = sp.fraction(sp.together(expression))[0]
        self.assertEqual(sp.expand(numerator), 0)

    def zeros(self, expressions):
        for expression in expressions:
            self.zero(expression)

    @staticmethod
    def vector_derivative(expression, variables, values):
        return sum(sp.diff(expression, x)*value
                   for x, value in zip(variables, values))

    def test_coefficient_word_poles_and_first_step_improvement(self):
        p, q = sp.symbols("p q")
        for e in (1, 2, 3):
            with self.subTest(order=e):
                tau, rho = p**(e+1)/sp.Integer(e+1), q+p
                dt = lambda f: (sp.diff(f, p)-sp.diff(f, q))/p**e
                dr = lambda f: sp.diff(f, q)
                self.zeros((dt(tau)-1, dt(rho), dr(tau), dr(rho)-1))
                self.zero(sp.Matrix([tau, rho]).jacobian((p, q)).det()-p**e)
                sharp = p
                coefficient = sp.Integer(1)
                for degree in range(1, 5):
                    sharp = sp.cancel(dt(sharp))
                    if degree > 1:
                        coefficient *= 1-(degree-1)*(e+1)
                    M = degree*(e+1)-1
                    self.zero(p**M*sharp-coefficient)
                    self.assertNotEqual(coefficient, 0)
                if e == 3:
                    continue
                # The denominator 1+q is a unit in C[p,q]_(p).
                # Cleared expressions need be regular in that DVR, not
                # complex polynomials in both p and q.
                for length in range(1, 4):
                    for word in itertools.product((dt, dr), repeat=length):
                        result = p/(1+q)
                        for operation in word:
                            result = sp.cancel(operation(result))
                        cleared = sp.cancel(p**(length*(e+1)-1)*result)
                        denominator = sp.fraction(cleared)[1]
                        self.assertNotEqual(sp.expand(denominator.subs(p, 0)), 0)

    def test_actual_noncontracted_critical_divisor_has_mu_zero(self):
        u, a, b, v = sp.symbols("u a b v")
        X, Y, Z, W, U, V = sp.symbols("X Y Z W U V")
        source = (u, a, b, v)
        for n in (2, 3):
            with self.subTest(power=n):
                forward = (b+u, v+a**n*u, a+b*u, u)
                xf, yf, zf, wf = forward
                ui = wf
                bi = sp.expand(xf-wf)
                ai = sp.expand(zf-wf*bi)
                vi = sp.expand(yf-ai**n*wf)
                self.zeros((ui-u, bi-b, ai-a, vi-v))
                ui, bi = W, X-W
                ai = Z-W*bi
                vi = Y-ai**n*W
                reverse = (bi+ui, vi+ai**n*ui, ai+bi*ui, ui)
                self.zeros(f-target for f, target in zip(reverse, (X, Y, Z, W)))
                self.zero(sp.Matrix(forward).jacobian(source).det()+1)

                speeds = sp.Matrix([1, a**n, b])
                omega = sp.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(b)).det()
                self.zero(omega-n*a**(n-1))
                self.assertNotEqual(sp.expand(omega), 0)
                self.zeros(sp.diff(f, u, 2) for f in forward)
                Tvalues = (1, u-b, -1,
                           -a**n+n*a**(n-1)*b*u-n*a**(n-1)*u**2)
                self.zeros(self.vector_derivative(f, source, Tvalues)-expected
                           for f, expected in zip(forward, (0, 0, 0, 1)))
                self.zeros(sp.Poly(value, u).coeff_monomial(u**2)-expected
                           for value, expected in zip(Tvalues[1:], (0, 0, -omega)))
                # Nonzero invariant W-X=-b realizes degree zero, hence mu=0.
                self.zeros((wf-xf+b, sp.diff(wf-xf, u)))
                self.assertNotEqual(sp.expand(wf-xf), 0)

                tau, rho = a**n, b
                dt = lambda f: sp.diff(f, a)/omega
                dr = lambda f: sp.diff(f, b)
                self.zeros((dt(tau)-1, dt(rho), dr(tau), dr(rho)-1))
                self.zero(sp.Matrix([tau, rho]).jacobian((a, b)).det()-omega)
                self.zeros((tau.subs(a, 0), rho.subs(a, 0)-b))
                y, z = v-a**n*b, a-b*b
                Wchart = X-b

                def homogeneous(f, degree):
                    result = 0
                    for i in range(degree+1):
                        coefficient = f
                        for _ in range(i):
                            coefficient = dt(coefficient)
                        for _ in range(degree-i):
                            coefficient = dr(coefficient)
                        result += coefficient*U**i*V**(degree-i)/(
                            math.factorial(i)*math.factorial(degree-i))
                    return sp.cancel(result)

                evaluate = lambda f: f.subs({U: y, V: z}, simultaneous=True)
                f1 = sp.Poly(Wchart, X).coeff_monomial(X)
                f0 = sp.cancel(sp.Poly(Wchart, X).coeff_monomial(1)
                               -evaluate(homogeneous(f1, 1)))
                first = -homogeneous(f1, 2)-homogeneous(f0, 1)
                f_minus = sp.cancel(evaluate(first))
                phi = sp.cancel(first-f_minus)
                psi = -homogeneous(f1, 3)-homogeneous(f0, 2)-homogeneous(f_minus, 1)
                value = sp.cancel(evaluate(psi))
                self.zeros((f1-1, f0+b, f_minus-(a-b*b),
                            phi-(V-a+b*b), psi-(2*b*V-U/omega),
                            -omega*sp.diff(value, v)-1))
                # The primitive factor is D=-partial_v. Multiplying this
                # normalized tail by Omega already gives a global D-slice.
                primitive_slice = sp.cancel(omega*value)
                expected = -v+(2*n+1)*a**n*b-2*n*a**(n-1)*b**3
                self.zeros((primitive_slice-expected,
                            -sp.diff(primitive_slice, v)-1))
                sp.Poly(primitive_slice, a, b, v)
                self.zero(primitive_slice.subs(a, 0)+v)
                # The full generic divisor fiber is C(b)[v], directly from
                # A=C[a,b,v]; the surviving primitive slice is -v.


if __name__ == "__main__":
    unittest.main()
