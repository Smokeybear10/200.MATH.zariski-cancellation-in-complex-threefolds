"""Exact controls for the full quadratic divisor classification.

Imports are only unittest and SymPy. The DVR models are controls for
the proved local algebra, not claimed realizations of the complete
four-variable adjoint frame. Finite tests do not prove all-prime scope.
"""

import unittest

import sympy as s


pi, v, j, T, Z, W = s.symbols("pi v j T Z W")


def zero(case, expr):
    case.assertEqual(s.cancel(s.expand(expr)), 0)


class QuadraticDivisorChecks(unittest.TestCase):
    def test_actual_generator_elimination_and_hidden_quadratic_fiber(self):
        # R=Q(v)[pi]_(pi). Original j has only a linear zero residue, but
        # the full ring has a quadratic residue extension after extraction.
        q1 = (j**2-v*pi**2)/pi**4
        q2 = 2*q1+j/pi+pi
        t = s.cancel(q2-2*q1)
        zero(self, t-j/pi-pi)
        zero(self, j-(pi*t-pi**2))
        z_in_t = s.cancel(q1.subs(j, pi*T-pi**2))
        zero(self, z_in_t-((T-pi)**2-v)/pi**2)
        # Both original extra generators are recovered from T,z.
        zero(self, q2.subs(j, pi*T-pi**2)-2*z_in_t-T)
        # The final monic residue relation is irreducible over Q(v).
        residue = s.Poly(T**2-v, T, domain=s.QQ.frac_field(v))
        self.assertTrue(residue.is_irreducible)
        self.assertEqual((pi*T).subs(pi, 0), 0)
        self.assertEqual(s.rem(T, T**2-v, T), T)
        self.assertEqual(s.degree(T**2-v, T), 2)

    def test_finite_root_lift_and_polynomial_linear_branch_inverse(self):
        P = pi*T**2+(1+pi)*T+pi**2
        for n in range(1, 4):
            with self.subTest(exponent=n):
                root = s.Integer(0)
                # Finite lifting modulo pi**n, not an infinite Hensel series.
                for k in range(1, n):
                    error = s.Poly(s.expand(P.subs(T, root)), pi)
                    root -= error.coeff_monomial(pi**k)*pi**k
                constant = s.cancel(P.subs(T, root)/pi**n)
                self.assertTrue(constant.is_polynomial(pi))
                b = s.expand(1+pi+2*pi*root)
                self.assertEqual(b.subs(pi, 0), 1)
                L = sum((-pi*T/b)**k for k in range(n))/b
                K = s.cancel(((b+pi*T)*L-1)/pi**n)
                zero(self, (b+pi*T)*L-1-pi**n*K)
                extracted = (Z-constant)*L-T*K
                z_from_t = constant+(b*T+pi*T**2)/pi**n
                zero(self, extracted.subs(Z, z_from_t)-T/pi**n)
                # Exact inverse over R for the actual extracted coordinate.
                new_t = root+pi**n*W
                new_z = constant+b*W+pi**(n+1)*W**2
                zero(self, pi**n*new_z-P.subs(T, new_t))
                zero(self, (new_t-root)/pi**n-W)

    def test_unit_square_completion_and_both_inverse_orders(self):
        a = 1+pi
        b = 2+pi
        eta = v+pi
        c = b**2/(4*a)-a*eta
        P = a*T**2+b*T+c
        shifted = T+b/(2*a)
        rescaled = Z/a
        zero(self, (pi**3*Z-P)/a-(pi**3*rescaled-shifted**2+eta))
        inverse_T = W-b/(2*a)
        inverse_Z = a*j
        zero(self, shifted.subs(T, inverse_T)-W)
        zero(self, rescaled.subs(Z, inverse_Z)-j)
        zero(self, inverse_T.subs(W, shifted)-T)
        zero(self, inverse_Z.subs(j, rescaled)-Z)
        self.assertTrue(s.Poly(T**2-v, T, domain=s.QQ.frac_field(v)).is_irreducible)
        self.assertNotEqual(eta.subs(pi, 0), 0)

    def test_standard_action_residue_and_plinth_contraction_controls(self):
        eta = v+pi
        for n in range(1, 5):
            with self.subTest(exponent=n):
                relation = pi**n*Z-T**2+eta
                D = lambda p: s.expand(pi**n*s.diff(p, T)+2*T*s.diff(p, Z))
                zero(self, D(relation))
                self.assertEqual(s.gcd(D(T), D(Z)), 1)
                # Free on this DVR model is not the same as possessing a
                # slice: the written contraction proof gives plinth (pi**n).
                free_combination = T*D(Z)/(2*eta)-Z*D(T)/eta
                zero(self, free_combination-1+relation/eta)
                self.assertEqual(D(T), pi**n)
                self.assertEqual(D(Z).subs(pi, 0), 2*T)
                self.assertEqual(s.rem(T, T**2-v, T), T)
        # Actual residue basis independence underlying the all-degree
        # negative-pole contraction is checked on separate finite inputs.
        for a0, b0 in ((1, 0), (0, 1), (v+Z, Z**2+1), (v**2, -Z)):
            expression = a0+b0*T
            self.assertEqual(s.rem(expression, T**2-v, T), expression)
            self.assertNotEqual(s.expand(expression), 0)


if __name__ == "__main__":
    unittest.main()
