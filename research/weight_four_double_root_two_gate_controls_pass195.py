"""Exact finite controls for the double-root two-gate classification195.

These tests verify differential rational identities, including reduction
modulo the first ODE, and the explicit candidate families. They do not
prove the constant-field/Euler completeness argument, actual frame
realizability, coordinate return, cancellation, or historical novelty.
No proof source or other checker is imported.
"""

import unittest

import sympy as sp


class DoubleRootTwoGateControls(unittest.TestCase):
    def assert_zero(self, value):
        self.assertEqual(sp.cancel(sp.together(value)), 0)

    def test_raw_first_ode_reduction_and_factored_second_gate(self):
        z, f, f1, f2 = sp.symbols("z f f1 f2", nonzero=True)
        t = z**2
        q = z
        d = 1 / (16 * z**5)
        den = -5 * f + 8 * t * f1
        f3 = 3 * f2 * (7 * f - 10 * t * f1 + 4 * t**2 * f2) / (2 * t * den)

        # This derivation enforces f'=f1, f1'=f2 and the solved first
        # ODE. It also enforces t=z^2 and q'=1/(2q), without radicals.
        def deriv(value):
            return sp.factor(
                sp.diff(value, z) / (2 * z)
                + f1 * sp.diff(value, f)
                + f2 * sp.diff(value, f1)
                + f3 * sp.diff(value, f2)
            )

        self.assert_zero(deriv(q) - 1 / (2 * z))
        self.assert_zero(deriv(deriv(deriv(q))) / 6 - d)
        Df = sp.factor(deriv(d) * f / 4 + d * f1)
        first = 20 * Df * f3 - 3 * d * f2**2 - 12 * f2 * deriv(Df)
        self.assert_zero(first)
        self.assert_zero(Df - den / (128 * z**7))

        R = 1 / f
        nu = sp.factor(f2**2 / (8 * f**3 * Df))
        Delta = sp.factor(R * deriv(deriv(R)) / 2 - deriv(R)**2)
        self.assert_zero(Delta + f2 / (2 * f**3))
        p2 = sp.factor(-Delta / (R * nu))
        slope = sp.factor(2 * deriv(R) / R - deriv(nu) / nu)
        L3 = sp.factor(
            (
                R * deriv(deriv(nu)) / 4
                - deriv(R) * deriv(nu) / 2
                - nu * deriv(deriv(R)) / 2
                - R * nu * slope**2 / 2
                - nu**2 * p2
            ) / (3 * R * p2)
        )
        J3 = sp.factor(
            -R * deriv(L3) + deriv(R) * L3
            - nu * deriv(nu) / 2
            - slope * (3 * R * L3 + nu**2)
        )
        factor_one = -f + 4 * t * f1 + 4 * t**2 * f2
        factor_two = f - t * f1 + 2 * t**2 * f2
        expected = -896 * f2**3 * t**4 * factor_one * factor_two**2 / (f**5 * den**5)
        self.assert_zero(J3 - expected)

        # The factors are distinct Euler operators, not sampled values.
        mu = sp.symbols("mu")
        self.assert_zero(-1 + 4 * mu + 4 * mu * (mu - 1) - (2 * mu - 1) * (2 * mu + 1))
        self.assert_zero(1 - mu + 2 * mu * (mu - 1) - (2 * mu - 1) * (mu - 1))

    def test_exact_surviving_families_and_excluded_euler_mixture(self):
        z, a, b = sp.symbols("z a b", nonzero=True)
        d = 1 / (16 * z**5)

        def deriv(value):
            return sp.factor(sp.diff(value, z) / (2 * z))

        def first_gate(value):
            ff = deriv(deriv(value))
            Df = deriv(d) * value / 4 + d * deriv(value)
            return sp.factor(20 * Df * deriv(ff) - 3 * d * ff**2 - 12 * ff * deriv(Df))

        def second_gate(value):
            R = 1 / value
            ff = deriv(deriv(value))
            Df = deriv(d) * value / 4 + d * deriv(value)
            nu = sp.factor(ff**2 / (8 * value**3 * Df))
            Delta = sp.factor(R * deriv(deriv(R)) / 2 - deriv(R)**2)
            p2 = -Delta / (R * nu)
            slope = sp.factor(2 * deriv(R) / R - deriv(nu) / nu)
            L3 = sp.factor(
                (
                    R * deriv(deriv(nu)) / 4
                    - deriv(R) * deriv(nu) / 2
                    - nu * deriv(deriv(R)) / 2
                    - R * nu * slope**2 / 2
                    - nu**2 * p2
                ) / (3 * R * p2)
            )
            return sp.factor(
                -R * deriv(L3) + deriv(R) * L3
                - nu * deriv(nu) / 2
                - slope * (3 * R * L3 + nu**2)
            ), nu, Df

        for value in (a * z**2 + b * z, b * z, a / z):
            self.assertNotEqual(sp.factor(deriv(deriv(value))), 0)
            self.assert_zero(first_gate(value))
            J3, nu, Df = second_gate(value)
            self.assertNotEqual(sp.factor(Df), 0)
            self.assertNotEqual(sp.factor(nu), 0)
            self.assert_zero(J3)

        self.assert_zero(first_gate(a * z + b / z) - 15 * a * b / (32 * z**13))
        self.assert_zero(second_gate(a * z**2 + b * z)[1] - b**2 / (z**3 * (a * z + b)**3 * (3 * a * z - b)))
        self.assert_zero(second_gate(a / z)[1] + z / a**2)


if __name__ == "__main__":
    unittest.main()

