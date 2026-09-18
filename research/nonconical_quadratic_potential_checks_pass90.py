"""One formal coefficient control, not an actual-action realization."""

import unittest

import sympy as S


class NonconicalQuadraticPotentialChecks(unittest.TestCase):
    def test_generic_volume_coefficient_and_symmetric_potential(self):
        u, q, rv, r1, r2, v1, v2 = S.symbols("u q rv r1 r2 v1 v2")
        a10, a11, a12, a20, a21, a22 = S.symbols(
            "a10 a11 a12 a20 a21 a22",
        )
        c = S.Matrix(3, 3, S.symbols("c0:9"))
        omega = c.det()
        basis = S.Matrix([
            [1, a10, a20, 0],
            [0, u + a11, a21, v1],
            [0, a12, u + a22, v2],
            [q * u, r1, r2, rv],
        ])
        original_order = S.diag(c, S.Matrix([[1]])) * basis
        determinant = S.expand(original_order.det(method="berkowitz"))
        self.assertEqual(
            S.expand(determinant - omega * basis.det(method="berkowitz")),
            0,
        )
        coefficients = S.Poly(determinant, u)
        self.assertEqual(coefficients.coeff_monomial(u**3), 0)
        quadratic = coefficients.coeff_monomial(u**2)
        self.assertEqual(
            S.expand(quadratic - omega * (rv + q * (a10 * v1 + a20 * v2))),
            0,
        )

        e2, e3 = S.eye(3)[:, 1], S.eye(3)[:, 2]
        first = S.Matrix([a10, a11, a12])
        second = S.Matrix([a20, a21, a22])
        vertical = S.Matrix([0, v1, v2])
        minor1 = S.Matrix.hstack(c * e2, c * second, c * vertical).det()
        minor2 = S.Matrix.hstack(c * first, c * e3, c * vertical).det()
        self.assertEqual(S.expand(minor1 + omega * a20 * v2), 0)
        self.assertEqual(S.expand(minor2 + omega * a10 * v1), 0)
        self.assertEqual(
            S.expand(quadratic - (omega * rv - q * (minor1 + minor2))),
            0,
        )

        y1, y2, rho1, rho2 = S.symbols("y1 y2 rho1 rho2")
        gamma11, gamma12, gamma22 = S.symbols("gamma11 gamma12 gamma22")
        g1 = rho1 + gamma11 * y1 + gamma12 * y2
        g2 = rho2 + gamma12 * y1 + gamma22 * y2
        potential = (
            rho1 * y1 + rho2 * y2
            + gamma11 * y1**2 / 2
            + gamma12 * y1 * y2
            + gamma22 * y2**2 / 2
        )
        self.assertEqual(S.diff(potential, y1), g1)
        self.assertEqual(S.diff(potential, y2), g2)
        potential_velocity = S.diff(potential, y1) * v1 + S.diff(potential, y2) * v2
        self.assertEqual(
            S.expand(quadratic.subs(
                {a10: g1, a20: g2, rv: -q * potential_velocity},
                simultaneous=True,
            )),
            0,
        )

        # The mixed-partial equality is a real input to this potential.
        gamma21 = S.symbols("gamma21")
        nonsymmetric_g2 = rho2 + gamma21 * y1 + gamma22 * y2
        curl = S.diff(nonsymmetric_g2, y1) - S.diff(g1, y2)
        self.assertEqual(curl, gamma21 - gamma12)
        self.assertNotEqual(curl, 0)
        self.assertEqual(curl.subs(gamma21, gamma12), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
