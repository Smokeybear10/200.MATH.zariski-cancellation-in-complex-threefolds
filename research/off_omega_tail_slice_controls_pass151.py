"""Finite actual controls for the off-Omega Taylor-tail slice construction.

The fixtures are the retained sharp divided-difference frame140 (degrees 2, 3)
and the reordered frame146 with Omega=-h**2. Both polynomial inverse orders
are checked with an independent recovered-coordinate placeholder. The signed
peeling coefficients are recomputed, not imported from another checker.

These tests verify exact identities in these examples only. They do not prove
the all-degree coefficient-descent argument, the invariant-ring intersection,
or the global patching of local slices. The split projected fiber in the second
fixture is not a nontrivial constant extension in its full invariant fiber.
No solver, search implementation, or earlier checker is imported.
"""

import math
import unittest

import sympy as sp


class OffOmegaTailSliceControls(unittest.TestCase):
    def zero(self, expression):
        # All denominators used below are products of the explicitly localized
        # independent coefficient variables. Test a numerator, without a large
        # multivariable rational gcd calculation.
        numerator = sp.fraction(sp.together(expression))[0]
        self.assertEqual(sp.expand(numerator), 0)

    def zeros(self, expressions):
        for expression in expressions:
            self.zero(expression)

    @staticmethod
    def divided_difference(coefficients, a, v, u):
        return sum(
            coefficient * math.comb(k, j) * v ** (k - j)
            * a**j * u ** (j - 1)
            for k, coefficient in enumerate(coefficients)
            for j in range(1, k + 1)
        )

    @staticmethod
    def vector_derivative(expression, variables, values):
        return sum(sp.diff(expression, x) * value
                   for x, value in zip(variables, values))

    def recover_tails(self, W, x, y, z, dt, dr, U, V, moving_variable):
        """Descending finite coefficients and the first two signed tails."""
        degree = sp.Poly(W, x).degree()

        def homogeneous(f, order):
            result = 0
            for i in range(order + 1):
                coefficient = f
                for _ in range(i):
                    coefficient = dt(coefficient)
                for _ in range(order - i):
                    coefficient = dr(coefficient)
                result += coefficient * U**i * V ** (order - i) / (
                    math.factorial(i) * math.factorial(order - i)
                )
            return sp.cancel(result)

        def evaluate(polynomial):
            return polynomial.subs({U: y, V: z}, simultaneous=True)

        coefficients = {}
        for j in range(degree, -1, -1):
            recovered = sp.Poly(W, x).coeff_monomial(x**j)
            recovered -= sum(evaluate(homogeneous(coefficients[k], k - j))
                             for k in range(j + 1, degree + 1))
            coefficients[j] = sp.cancel(recovered)
            self.zero(sp.diff(coefficients[j], moving_variable))

        first = -sum(homogeneous(coefficients[j], j + 1)
                     for j in range(degree + 1))
        f_minus = sp.cancel(evaluate(first))
        self.zero(sp.diff(f_minus, moving_variable))
        phi = sp.cancel(first - f_minus)
        psi = -sum(homogeneous(coefficients[j], j + 2)
                   for j in range(degree + 1)) - homogeneous(f_minus, 1)
        self.zero(evaluate(phi))
        return coefficients, f_minus, phi, sp.cancel(psi), evaluate(psi)

    def test_actual_sharp_family_tail_slice(self):
        u, a, b, v = sp.symbols("u a b v")
        X, Y, Z, W, A, U, V = sp.symbols("X Y Z W A U V")
        source = (u, a, b, v)
        for degree in (2, 3):
            with self.subTest(degree=degree):
                coefficients = [sp.Integer(2), sp.Integer(1)]
                coefficients += [sp.Integer(0)] * (degree - 2)
                coefficients += [sp.Rational(1, 2)]
                F = lambda t: sum(c * t**j for j, c in enumerate(coefficients))
                delta = lambda aa, vv, uu: self.divided_difference(
                    coefficients, aa, vv, uu)
                forward = (v + a*u, a - F(v) + (b + 1)*u,
                           a - F(v) + (b + 2)*u, b + delta(a, v, u))
                xf, yf, zf, wf = forward
                recovered_u = sp.expand(zf - yf)
                recovered_a = sp.expand(2*yf - zf - recovered_u*wf + F(xf))
                recovered_v = sp.expand(xf - recovered_a*recovered_u)
                recovered_b = sp.expand(wf - delta(recovered_a, recovered_v,
                                                  recovered_u))
                self.zeros((recovered_u-u, recovered_a-a,
                            recovered_v-v, recovered_b-b))

                # Reverse composition first treats recovered a as independent.
                # Its sole remaining residual is A-a_inverse; substituting the
                # displayed polynomial a_inverse makes every residual zero.
                ui = Z-Y
                ai = 2*Y-Z-ui*W+F(X)
                vi = X-A*ui
                bi = W-delta(A, vi, ui)
                reverse = (vi+A*ui, A-F(vi)+(bi+1)*ui,
                           A-F(vi)+(bi+2)*ui, bi+delta(A, vi, ui))
                self.zeros((reverse[0]-X, reverse[1]-Y-(A-ai),
                            reverse[2]-Z-(A-ai), reverse[3]-W))
                self.zero(sp.Matrix(forward).jacobian(source).det()-1)

                speeds = sp.Matrix([a, b+1, b+2])
                omega = sp.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(b)).det()
                self.zero(omega-1)
                self.zeros(sp.diff(f, u, 2) for f in forward[:3])
                self.zero((speeds[2]-speeds[1])-1)
                Tvalues = (0, -u, 1+u*sp.diff(F(v), v), u**2)
                self.zeros(self.vector_derivative(f, source, Tvalues)-expected
                           for f, expected in zip(forward, (0, 0, 0, 1)))
                self.zero(sp.Poly(Tvalues[3], u).coeff_monomial(u**2)-1)

                tau, rho = (b+1)/a, (b+2)/a
                dt = lambda f: a*a*sp.diff(f, a)+a*(b+2)*sp.diff(f, b)
                dr = lambda f: -a*a*sp.diff(f, a)-a*(b+1)*sp.diff(f, b)
                self.zeros((dt(tau)-1, dt(rho), dr(tau), dr(rho)-1))
                self.zero(sp.Matrix([tau, rho]).jacobian((a, b)).det()-omega/a**3)
                y, z = a-F(v)-(b+1)*v/a, a-F(v)-(b+2)*v/a
                Wchart = b+a*sum(c*sum(X**j*v**(k-1-j) for j in range(k))
                                for k, c in enumerate(coefficients) if k)
                fs, fm, phi, psi, value = self.recover_tails(
                    Wchart, X, y, z, dt, dr, U, V, v)
                self.zero(fs[0]-(b+a))
                for j in range(1, degree):
                    self.zero(fs[j]-coefficients[j+1]*a)
                self.zero(fm-a*(2-a))
                G = (b+2)*U-(b+1)*V+F(a*(U-V))-a
                self.zeros((phi+a*G, psi-(a**3*(U-V)-a*a*(U-V)*G),
                            value-a*a*v, sp.diff(value, v)/a**2-1))
                # N=partial_v, D=N/Omega; the rescaled tail is already v.
                d_slice = sp.cancel(omega*value/a**2)
                self.zeros((d_slice-v, sp.diff(d_slice, v)-1))

    def test_actual_nonconstant_omega_and_localized_tail(self):
        h, k, a, u = sp.symbols("h k a u")
        X, Y, Z, W, H, U, V = sp.symbols("X Y Z W H U V")
        source = (h, k, a, u)
        forward = (h+a*a+k*u, a+h*u, k-2*a*h-h*h*u, u)
        xf, yf, zf, wf = forward
        hi = sp.expand(xf-yf*yf-wf*zf)
        ai = sp.expand(yf-wf*hi)
        ki = sp.expand(zf+2*hi*yf-wf*hi*hi)
        self.zeros((hi-h, ai-a, ki-k, wf-u))
        h_inverse = X-Y*Y-W*Z
        aa, kk = Y-W*H, Z+2*H*Y-W*H*H
        reverse = (H+aa*aa+kk*W, aa+H*W, kk-2*aa*H-H*H*W, W)
        self.zeros((reverse[0]-X-(H-h_inverse), reverse[1]-Y,
                    reverse[2]-Z, reverse[3]-W))
        self.zero(sp.Matrix(forward).jacobian(source).det()+1)

        speeds = sp.Matrix([k, h, -h*h])
        omega = sp.Matrix.hstack(speeds, speeds.diff(h), speeds.diff(k)).det()
        self.zero(omega+h*h)
        self.zeros(sp.diff(f, u, 2) for f in forward[:3])
        Tvalues = (-k+2*a*h+h*h*u, -h*h-2*a*k+4*a*a*h+2*a*h*h*u,
                   -h+(k-2*a*h)*u-h*h*u*u, 1)
        self.zeros(self.vector_derivative(f, source, Tvalues)-expected
                   for f, expected in zip(forward, (0, 0, 0, 1)))
        self.zeros(sp.Poly(value, u).coeff_monomial(u**2)-expected
                   for value, expected in zip(Tvalues[:3], (0, 0, -h*h)))

        tau, rho = h/k, -h*h/k
        dt = lambda f: -k*sp.diff(f, h)-2*k*k*sp.diff(f, k)/h
        dr = lambda f: -k*sp.diff(f, h)/h-k*k*sp.diff(f, k)/h**2
        self.zeros((dt(tau)-1, dt(rho), dr(tau), dr(rho)-1))
        self.zero(sp.Matrix([tau, rho]).jacobian((h, k)).det()-omega/k**3)
        y, z = a-h*(h+a*a)/k, k-2*a*h+h*h*(h+a*a)/k
        Wchart = (X-h-a*a)/k
        fs, fm, phi, psi, value = self.recover_tails(
            Wchart, X, y, z, dt, dr, U, V, a)
        G = (V+h*U)**2-k*V+h**3
        self.zeros((fs[1]-1/k, fs[0]+k/h**2, fm-k/h,
                    phi+k*G/h**4,
                    psi-(k*k*(V+h*U)/h**3-k*k*V*G/h**6),
                    value-(-k*k*a/h**2+k**3/h**3)))
        self.zero((-h*h/k**2)*sp.diff(value, a)-1)
        # Omega=-h^2 and s=k: D=N/Omega=partial_a, over R=C[h,k,1/(hk)].
        d_slice = sp.cancel(omega*value/k**2)
        self.zeros((d_slice-(a-k/h), sp.diff(d_slice, a)-1))
        self.assertEqual(sp.fraction(d_slice)[1], h)
        self.zero(G.subs(h, 0)-V*(V-k))
        # The projected split lies on h=0, which D(Omega) removes. The full
        # ring is S[a] even there; this is not a full-fiber cover counterexample.
        self.zero(omega.subs(h, 0))


if __name__ == "__main__":
    unittest.main()
