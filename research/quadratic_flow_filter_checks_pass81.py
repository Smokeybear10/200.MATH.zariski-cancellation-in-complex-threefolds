"""Actual quadratic-flow inverse/filter controls, not universal frame tests."""

import unittest

import sympy as sp


class QuadraticFlowFilterChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_actual_frame_all_scalar_filters_and_lowering_failure(self):
        a, s, b, c, lam, mu = sp.symbols("a s b c lambda mu")
        original = sp.Matrix([a, s, b, c])
        x = sp.Matrix([s + a**2, a + (s + a**2)**2, b, c])
        X = sp.Matrix(sp.symbols("X1:5"))
        inverse = sp.Matrix([X[1] - X[0]**2, X[0] - (X[1] - X[0]**2)**2, X[2], X[3]])
        self.assert_zero(inverse.subs(dict(zip(X, x)), simultaneous=True) - original)
        self.assert_zero(x.subs(dict(zip(original, inverse)), simultaneous=True) - X)
        self.assert_zero(x.diff(s, 3))
        self.assert_zero(x.diff(s, 2) - sp.Matrix([0, 2, 0, 0]))
        self.assert_zero(inverse.jacobian(X) * sp.Matrix([1, 2 * X[0], 0, 0]) - sp.Matrix([0, 1, 0, 0]))

        k, h = 1 + lam, 1 + 2 * lam + 2 * mu
        y = x + lam * s * x.diff(s) + mu * s**2 * x.diff(s, 2)
        self.assert_zero(y - sp.Matrix([a**2 + k * s, a + a**4 + 2 * k * a**2 * s + h * s**2, b, c]))
        determinant = sp.expand(y.jacobian(original).det())
        self.assert_zero(determinant + k - 4 * a * s * (h - k**2))
        self.assert_zero(y.diff(s, 2) - sp.Matrix([0, 2 * h, 0, 0]))
        self.assert_zero(determinant.subs(mu, -(1 + 2 * lam) / 2) + k + 4 * k**2 * a * s)
        naive = y.subs({lam: -sp.Rational(1, 2), mu: 0})
        self.assert_zero(naive.diff(s, 2))
        self.assert_zero(naive.jacobian(original).det() + sp.Rational(1, 2) + a * s)
        self.assert_zero(determinant.subs(mu, lam**2 / 2) + k)
        # Constancy/nonzero of this determinant is a necessary coordinate gate.
        # The written proof treats all scalar cases, including k=0.

    def test_true_slice_dilation_inverse_and_positive_linear_slice(self):
        a, s, b, c, t = sp.symbols("a s b c t")
        # Work symbolically over C(t); each allowed specialization has t != 0.
        original = sp.Matrix([a, s, b, c])
        x = sp.Matrix([s + a**2, a + (s + a**2)**2, b, c])
        y = sp.simplify(x + (t - 1) * s * x.diff(s) + (t - 1)**2 * s**2 * x.diff(s, 2) / 2)
        self.assert_zero(y - x.subs(s, t * s))
        Y = sp.Matrix(sp.symbols("Y1:5"))
        inverse = sp.Matrix([Y[1] - Y[0]**2, (Y[0] - (Y[1] - Y[0]**2)**2) / t, Y[2], Y[3]])
        self.assert_zero(inverse.subs(dict(zip(Y, y)), simultaneous=True) - original)
        self.assert_zero(y.subs(dict(zip(original, inverse)), simultaneous=True) - Y)
        self.assert_zero(y.jacobian(original).det() + t)
        for order in range(4):
            self.assert_zero(y.diff(s, order) - t**order * x.diff(s, order).subs(s, t * s))
        self.assert_zero(y.subs(t, sp.Rational(1, 2)).diff(s, 2) - sp.Matrix([0, sp.Rational(1, 2), 0, 0]))

        # The same action with its other, linear slice admits a nice filter.
        linear_slice = x[0]
        positive = x - linear_slice * x.diff(s) / 2
        self.assert_zero(positive - sp.Matrix([(s + a**2) / 2, a, b, c]))
        positive_inverse = sp.Matrix([Y[1], 2 * Y[0] - Y[1]**2, Y[2], Y[3]])
        self.assert_zero(positive_inverse.subs(dict(zip(Y, positive)), simultaneous=True) - original)
        self.assert_zero(positive.subs(dict(zip(original, positive_inverse)), simultaneous=True) - Y)
        self.assert_zero(positive.diff(s, 2))
        self.assert_zero(positive.jacobian(original).det() + sp.Rational(1, 2))

    def test_finite_higher_degree_weights_and_recurrence(self):
        a, u, s, dilation = sp.symbols("a u s dilation")
        for degree in range(2, 7):
            with self.subTest(degree=degree):
                coefficients = [sp.Integer(1), *sp.symbols(f"c1:{degree + 1}")]
                weights = [
                    sum(coefficients[j] * sp.factorial(n) / sp.factorial(n - j) for j in range(n + 1))
                    for n in range(degree + 1)
                ]
                k = weights[1]
                G = sum(sp.binomial(degree, n) * weights[n] * u**(degree - n) * s**n for n in range(degree + 1))
                x1, x2 = s + a**2, a + (s + a**2)**degree
                filtered2 = sum(coefficients[j] * s**j * sp.diff(x2, s, j) for j in range(degree + 1))
                self.assert_zero(filtered2 - a - G.subs(u, a**2))
                self.assert_zero(sp.diff(x2, s, degree) - sp.factorial(degree))
                self.assert_zero(sp.diff(x2, s, degree + 1))
                self.assert_zero(sp.Matrix([x1, x2]).jacobian((a, s)).det() + 1)

                H = sp.diff(G, s) - k * sp.diff(G, u)
                y = sp.Matrix([a**2 + k * s, a + G.subs(u, a**2)])
                determinant = y.jacobian((a, s)).det()
                self.assert_zero(determinant + k - 2 * a * H.subs(u, a**2))
                self.assert_zero(determinant.subs(a, 0) + k)
                polynomial = sp.Poly(sp.expand(H), u, s)
                for n in range(degree):
                    expected = degree * sp.binomial(degree - 1, n) * (weights[n + 1] - k * weights[n])
                    self.assert_zero(polynomial.coeff_monomial(u**(degree - n - 1) * s**n) - expected)

                substitution = {coefficients[j]: (dilation - 1)**j / sp.factorial(j) for j in range(1, degree + 1)}
                for n, weight in enumerate(weights):
                    self.assert_zero(weight.subs(substitution) - dilation**n)
                self.assert_zero(G.subs(substitution) - (u + dilation * s)**degree)
                self.assert_zero(determinant.subs(substitution) + dilation)
                transform = sp.Matrix([
                    [sp.factorial(n) / sp.factorial(n - j) if j <= n else 0 for j in range(degree + 1)]
                    for n in range(degree + 1)
                ])
                self.assert_zero(transform.det() - sp.prod(sp.factorial(n) for n in range(degree + 1)))
        # These five finite bounds do not prove the arbitrary-degree theorem.


if __name__ == "__main__":
    unittest.main(verbosity=2)
