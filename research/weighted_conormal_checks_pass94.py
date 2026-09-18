"""Finite weighted-operator controls, not actual action or recognition tests.

The one method checks multiplicities 2, 3, and 4. The accompanying
all-multiplicity proof supplies the geometric and completion hypotheses.
"""

import unittest

import sympy as S


class WeightedConormalControls(unittest.TestCase):
    def test_weighted_coefficient_and_strict_remainders(self):
        x, y, c = S.symbols("x y c")
        gamma, rho, lam, b, e = (
            S.Function(name)(c) for name in ("gamma", "rho", "lam", "b", "e")
        )

        for mu in (2, 3, 4):
            with self.subTest(multiplicity=mu):
                def leading(value):
                    return S.expand(
                        (gamma * x + rho * y**mu) * S.diff(value, y)
                        + lam * y**(mu - 1) * S.diff(value, c)
                    )

                def cube(operator, value):
                    for _ in range(3):
                        value = operator(value)
                    return value

                def target_coefficient(value):
                    return S.Poly(value, x, y).coeff_monomial(x**2 * y**(mu - 2))

                def expected(coefficient):
                    return (
                        coefficient * (mu - 1) * gamma
                        * (lam * S.diff(gamma, c) + mu * gamma * rho)
                        + (mu**2 - 1) * S.diff(coefficient, c) * lam * gamma**2
                    )

                coefficient_b = target_coefficient(cube(leading, b * y))
                coefficient_e = target_coefficient(cube(leading, e * y))
                self.assertEqual(S.expand(coefficient_b - expected(b)), 0)
                self.assertEqual(S.expand(coefficient_e - expected(e)), 0)
                wronskian = (mu**2 - 1) * lam * gamma**2 * (
                    e * S.diff(b, c) - b * S.diff(e, c)
                )
                self.assertEqual(
                    S.expand(e * coefficient_b - b * coefficient_e - wronskian), 0
                )

                # A one-unit error in the scalar is detected, not simplified away.
                wrong = expected(b) + S.diff(b, c) * lam * gamma**2
                residual = S.expand(coefficient_b - wrong)
                specialization = residual.subs({b: c, gamma: 1, lam: 1}).doit()
                self.assertEqual(specialization, -1)

                # With y itself a generator, the two successive coefficients
                # in D^3(y) enforce C = 0 and then K = 0 when gamma != 0.
                C = lam * S.diff(gamma, c) + mu * gamma * rho
                K = lam * S.diff(rho, c) + mu * rho**2
                second = C * x * y**(mu - 1) + K * y**(2 * mu - 1)
                self.assertEqual(S.expand(leading(leading(y)) - second), 0)
                self.assertEqual(
                    S.expand(target_coefficient(leading(second)) - (mu - 1) * gamma * C),
                    0,
                )
                remaining = leading(K * y**(2 * mu - 1))
                next_coefficient = S.Poly(remaining, x, y).coeff_monomial(
                    x * y**(2 * mu - 2)
                )
                self.assertEqual(S.expand(next_coefficient - (2 * mu - 1) * gamma * K), 0)

                # Strictly higher-weight polynomial perturbations cannot change
                # the first nonzero-weight component of a third derivative.
                gv, rv, lv, bv = c + 1, c - 1, c**2 + 1, c**2

                def polynomial_leading(value):
                    return S.expand(
                        (gv * x + rv * y**mu) * S.diff(value, y)
                        + lv * y**(mu - 1) * S.diff(value, c)
                    )

                def perturbed(value):
                    return S.expand(
                        polynomial_leading(value)
                        + y**(mu + 1) * S.diff(value, y)
                        + (x + y**mu) * S.diff(value, c)
                    )

                def weight_part(value, weight):
                    return S.expand(sum(
                        coefficient * x**i * y**j
                        for (i, j), coefficient in S.Poly(value, x, y).terms()
                        if mu * i + j == weight
                    ))

                generator = bv * y + c * x + y**2 + x * y
                full_cube = cube(perturbed, generator)
                leading_cube = cube(polynomial_leading, bv * y)
                weight = 3 * mu - 2
                self.assertEqual(S.expand(weight_part(full_cube, weight) - leading_cube), 0)
                self.assertTrue(all(
                    mu * i + j >= weight
                    for (i, j), coefficient in S.Poly(full_cube, x, y).terms()
                    if coefficient != 0
                ))


if __name__ == "__main__":
    unittest.main(verbosity=2)
