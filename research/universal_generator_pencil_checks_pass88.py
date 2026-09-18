"""One algebra-only cusp control for a universal relative generator pencil.

This does not construct an actual C4 action or test the arbitrary-ring proof.
No solver, research helper, runner, or previous checker is imported.
"""

import unittest

import sympy as S


class UniversalGeneratorPencilChecks(unittest.TestCase):
    def test_cusp_relative_generation_and_nonreduced_tensor(self):
        v, tau = S.symbols("v tau")
        d = v + tau * v**3
        recovered = (1 - tau * v**2) * d + tau**2 * v**5
        self.assertEqual(S.expand(recovered - v), 0)
        self.assertEqual(S.expand(recovered + tau * recovered**3 - d), 0)
        self.assertEqual(S.Poly(d, v).degree(), 3)
        self.assertEqual(S.cancel(v**5 / (v**2)**2), v)
        # Every monomial in C[v^2,v^5] has exponent 2i+5j.
        # For target exponent 3, i<=1 and j=0 exhaust nonnegative options.
        self.assertFalse(any(2 * i + 5 * j == 3
                             for i in range(2) for j in range(1)))

        X, Y = S.symbols("X Y")
        tensor = S.groebner([X**2 - Y**2, X**5 - Y**5], X, Y, domain=S.QQ)

        def remainder(expression):
            return S.expand(tensor.reduce(S.expand(expression))[1])

        dc = X - Y
        dh = X**3 - Y**3
        g = X**2 + X * Y + Y**2
        self.assertEqual(remainder(dc), X - Y)
        self.assertEqual(remainder(dh), X * Y**2 - Y**3)
        self.assertEqual(S.expand(dh - dc * g), 0)
        self.assertEqual(remainder(dh**2), 0)
        self.assertEqual(remainder(Y**4 * dc), 0)
        self.assertEqual(remainder(dc * g**2), 0)

        # Test coefficientwise in D[tau], not by radicalizing the tensor ideal.
        annihilator_identity = dc * ((1 + tau * g) * (1 - tau * g) - 1)
        for coefficient in S.Poly(S.expand(annihilator_identity), tau).all_coeffs():
            self.assertEqual(remainder(coefficient), 0)
        self.assertNotEqual(remainder(dh), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
