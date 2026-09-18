"""Two finite symbolic controls for the proposed all-L nilpotent-rank proof.

These check invariant/conic and variable-volume weighted identities only.
They do not verify fixed-point specialization, flat coefficient descent,
choice of actual normal parameters, or any original-frame theorem.
"""

import unittest

import sympy as sp


class WholeDoubleNilrankChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_conic_and_cyclic_invariants(self):
        a, b, theta, B1, B2, U, V = sp.symbols("a b theta B1 B2 U V")
        r = a*U+b*V
        P = a*B1+b*B2
        NU, NV = theta*b*r+B1, -theta*a*r+B2

        def deriv(expression):
            return sp.expand(NU*sp.diff(expression, U)+NV*sp.diff(expression, V))

        self.assert_zero(deriv(r)-P)
        self.assert_zero(deriv(NU)-theta*b*P)
        self.assert_zero(deriv(NV)+theta*a*P)
        self.assert_zero(deriv(deriv(NU)))
        self.assert_zero(deriv(deriv(NV)))
        conic = theta*r**2-2*B2*U+2*B1*V
        self.assert_zero(deriv(conic))
        for element, first in ((U, NU), (V, NV)):
            second = deriv(first)
            cyclic = 2*second*element-first**2
            self.assert_zero(deriv(cyclic))

        # Algebraic consequence once the two invariant values specialize
        # to zero. The test does not establish that geometric premise.
        p, eta, u, v = sp.symbols("p eta u v")
        fiber = sp.groebner([v**2-2*p*u+eta, p, eta], p, eta, v, u)
        self.assert_zero(fiber.reduce(v**2)[1])
        self.assertEqual(fiber.reduce(v)[1], v)

    def test_variable_volume_weighted_connection(self):
        x, y, c = sp.symbols("x y c")
        a, b, phi, nu = [sp.Function(name)(c) for name in ("a", "b", "phi", "nu")]
        leading_f = a*x+b*y**2

        def leading_deriv(expression):
            return sp.expand(nu*(sp.diff(leading_f, y)*sp.diff(expression, c)
                                 - sp.diff(leading_f, c)*sp.diff(expression, y)))

        Dy = leading_deriv(y)
        Dphi_y = leading_deriv(phi*y)
        self.assert_zero(Dy+nu*(sp.diff(a, c)*x+sp.diff(b, c)*y**2))
        self.assert_zero(Dphi_y+nu*sp.diff(a, c)*phi*x
                         - nu*(2*b*sp.diff(phi, c)-sp.diff(b, c)*phi)*y**2)
        self.assert_zero(Dphi_y-phi*Dy-2*nu*b*sp.diff(phi, c)*y**2)
        self.assert_zero(leading_deriv(leading_f))
        self.assertEqual(sp.Poly(Dy, x, y).coeff_monomial(x), -nu*sp.diff(a, c))
        self.assertEqual(sp.Poly(Dy, x, y).coeff_monomial(y**2), -nu*sp.diff(b, c))
        constant_conormal = {sp.diff(a, c): 0, sp.diff(b, c): 0}
        self.assert_zero(Dphi_y.xreplace(constant_conormal)
                         - 2*nu*b*sp.diff(phi, c)*y**2)
        # A nonconstant volume factor was never differentiated away or
        # silently replaced by a constant in these first-order identities.
        self.assertTrue(Dphi_y.has(nu))
        self.assertFalse(Dphi_y.has(sp.diff(nu, c)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
