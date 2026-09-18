"""Finite constant-GL2 certificates for reciprocal equivalence122.

One method verifies conditional rational and polynomial identities.
It does not certify the supplied actual frame, existence of its inverse,
or the full scalar classification. The displayed constant linear change
does have the two-sided inverse checked here.
"""

import unittest
import sympy as sp


class NonnullReciprocalEquivalenceChecks(unittest.TestCase):
    def test_constant_congruence_and_reciprocal_cubic(self):
        h = sp.symbols("h")
        alpha, beta, gamma, delta = sp.symbols("alpha beta gamma delta")
        transform = sp.Matrix([[alpha, beta], [gamma, delta]])
        determinant = alpha * delta - beta * gamma
        sigma = gamma * h + delta
        new_h = (alpha * h + beta) / sigma
        scalar = sp.Function("D")(h)

        def zero(expression):
            self.assertEqual(sp.cancel(expression), 0)

        def same_matrix(left, right):
            self.assertEqual(left.shape, right.shape)
            for entry in left - right:
                zero(entry)

        def new_derivative(expression):
            return sp.cancel(sigma**2 * sp.diff(expression, h) / determinant)

        def metric(ratio, value, first, second):
            return sp.Matrix([
                [second / 2, (first - ratio * second) / 2],
                [(first - ratio * second) / 2,
                 value - ratio * first + ratio**2 * second / 2],
            ])

        old_metric = metric(h, scalar, sp.diff(scalar, h), sp.diff(scalar, h, 2))
        new_scalar = scalar / sigma**2
        first = new_derivative(new_scalar)
        second = new_derivative(first)
        third = new_derivative(second)
        new_metric = metric(new_h, new_scalar, first, second)
        inverse = transform.inv()

        zero(sp.diff(new_h, h) - determinant / sigma**2)
        zero(new_derivative(new_h) - 1)
        zero((delta * new_h - beta) / (alpha - gamma * new_h) - h)
        same_matrix(new_metric, inverse.T * old_metric * inverse)
        same_matrix(
            inverse.T * sp.Matrix([1, -h]),
            sigma / determinant * sp.Matrix([1, -new_h]),
        )
        zero(third - sigma**4 * sp.diff(scalar, h, 3) / determinant**3)
        zero(new_metric.det() - old_metric.det() / determinant**2)
        zero(new_scalar * sigma**2 - scalar)

        lam, mu, pole, a2, a1, a0, xi = sp.symbols(
            "lambda mu pole a2 a1 a0 xi"
        )
        reciprocal = a2 * h**2 + a1 * h + a0 + pole / (lam * h + mu)
        cubic = (
            pole * xi**3
            + (a0 - mu * a1 / lam + mu**2 * a2 / lam**2) * xi**2
            + (a1 / lam - 2 * mu * a2 / lam**2) * xi
            + a2 / lam**2
        )
        zero(xi**2 * reciprocal.subs(h, (1 / xi - mu) / lam) - cubic)
        zero(sp.diff(cubic, xi, 3) - 6 * pole)
        zero(
            -(lam * h + mu)**4 * sp.diff(reciprocal, h, 3) / lam**3
            - 6 * pole
        )

        ambient = sp.Matrix([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, lam, mu, 0],
            [0, 0, 0, 1],
        ])
        ambient_inverse = sp.Matrix([
            [1, 0, 0, 0],
            [0, -mu / lam, 1 / lam, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ])
        same_matrix(ambient * ambient_inverse, sp.eye(4))
        same_matrix(ambient_inverse * ambient, sp.eye(4))
        zero(ambient.det() + lam)

        base_jacobian, omega, jacobian_field_value = sp.symbols("J Omega Nv")
        zero((determinant * base_jacobian) / (determinant * omega)
             - base_jacobian / omega)
        zero((determinant * base_jacobian)
             * (jacobian_field_value / determinant)
             - base_jacobian * jacobian_field_value)


if __name__ == "__main__":
    unittest.main()

