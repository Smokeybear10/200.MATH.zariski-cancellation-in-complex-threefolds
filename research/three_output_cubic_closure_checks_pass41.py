"""Exact shear controls, not a constructed full degree-five residual.

Only unittest and SymPy are used. Polynomial coordinate inverses and
actual localized nice examples are kept separate from formal residual
coefficient identities. Published recognition theorems are not tested.
"""

import unittest

import sympy as sp


def reduced(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda item: sp.cancel(sp.expand(item)))
    return sp.cancel(sp.expand(value))


def act(field, value, variables):
    return reduced(sum(coefficient * sp.diff(value, variable)
                       for coefficient, variable in zip(field, variables)))


def bracket(left, right, variables):
    return reduced(sp.Matrix([
        act(left, right[index], variables) - act(right, left[index], variables)
        for index in range(len(variables))
    ]))


def substitute(value, variables, images):
    return reduced(value.subs(dict(zip(variables, images)), simultaneous=True))


class ThreeOutputCubicClosureChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(reduced(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(reduced(value), 0)

    def test_nonconstant_speed_universal_shear_and_surviving_partial(self):
        w, a, b, z, ap = sp.symbols("w a b z ap")
        nu, lam = sp.symbols("nu lam", nonzero=True)
        kappa, a0, sigma = sp.symbols("kappa a0 sigma")
        variables = (w, a, b, z)
        targets = (w, ap, b, z)
        x = sp.Matrix(variables)
        coefficient = w/(6*nu) + a0/(3*lam)
        forward = sp.Matrix([w, a + kappa*b/(2*nu) - coefficient*z, b, z])
        inverse = sp.Matrix([w, ap - kappa*b/(2*nu) + coefficient*z, b, z])
        self.assertZero(substitute(forward, variables, inverse) - sp.Matrix(targets))
        self.assertZero(substitute(inverse, targets, forward) - x)
        self.assertZero(forward.jacobian(variables).det() - 1)
        tau = lam/(2*nu)*(w-kappa*sigma-nu*sigma**2/2) + a0
        first = sigma**2/12 + tau/(3*lam)
        self.assertZero(first - coefficient + kappa*sigma/(6*nu))
        # Sigma is a formal invariant coefficient in this identity, not
        # an independently claimed fifth coordinate of the actual model.
        nice = sp.Matrix([0, first, sigma/3, 1])
        self.assertZero(forward.jacobian(variables)*nice
                        - sp.Matrix([0, 0, sigma/3, 1]))
        old_good = sp.Matrix([0, -kappa/(2*nu), 1, 0])
        self.assertZero(forward.jacobian(variables)*old_good
                        - sp.Matrix([0, 0, 1, 0]))

    def test_nonconstant_speed_actual_rational_nice_model(self):
        w, a, b, z, time = sp.symbols("w a b z time")
        variables = (w, a, b, z)
        x = sp.Matrix(variables)
        ap = a+b-w*z/6
        sigma = (ap+w**2)/w**2
        tau = sp.Rational(3, 2)*(w-2*sigma-sigma**2/2)
        first = sigma**2/12 + tau/9
        nice = sp.Matrix([0, first, sigma/3, 1])
        self.assertZero(first-(w-2*sigma)/6)
        self.assertZero(act(nice, w, variables))
        self.assertZero(act(nice, ap, variables))
        self.assertZero(act(nice, sigma, variables))
        self.assertZero(act(nice, tau, variables))
        self.assertZero(nice.jacobian(variables)*nice)
        self.assertTrue(all(sp.denom(reduced(value)) == 1
                            for value in w**2*nice))
        self.assertNotEqual(sp.denom(reduced(nice[2])), 1)
        forward = x+time*nice
        inverse = x-time*nice
        self.assertZero(substitute(inverse, variables, forward)-x)
        self.assertZero(substitute(forward, variables, inverse)-x)
        self.assertZero(forward.jacobian(variables).det()-1)

    def test_constant_speed_universal_shear_and_exact_partial(self):
        w, a, b, z, bp = sp.symbols("w a b z bp")
        kappa = sp.symbols("kappa", nonzero=True)
        lam = sp.symbols("lam", nonzero=True)
        eta, tau = sp.symbols("eta tau")
        variables = (w, a, b, z)
        targets = (w, a, bp, z)
        sigma = w/kappa+eta
        forward = sp.Matrix([w, a, b-sigma*z/3, z])
        inverse = sp.Matrix([w, a, bp+sigma*z/3, z])
        self.assertZero(substitute(forward, variables, inverse)-sp.Matrix(targets))
        self.assertZero(substitute(inverse, targets, forward)-sp.Matrix(variables))
        self.assertZero(forward.jacobian(variables).det()-1)
        first = sigma**2/12 + tau/(3*lam)
        nice = sp.Matrix([0, first, sigma/3, 1])
        self.assertZero(forward.jacobian(variables)*nice
                        - sp.Matrix([0, first, 0, 1]))
        old_good = sp.Matrix([0, 1, 0, 0])
        self.assertZero(forward.jacobian(variables)*old_good-old_good)

    def test_constant_speed_actual_rational_nice_model(self):
        w, a, b, z, time = sp.symbols("w a b z time")
        variables = (w, a, b, z)
        x = sp.Matrix(variables)
        sigma = w/2+1
        bp = b-sigma*z/3
        tau = (bp+w**2)/w
        first = sigma**2/12 + tau/9
        nice = sp.Matrix([0, first, sigma/3, 1])
        self.assertZero(act(nice, bp, variables))
        self.assertZero(act(nice, sigma, variables))
        self.assertZero(act(nice, tau, variables))
        self.assertZero(nice.jacobian(variables)*nice)
        self.assertTrue(all(sp.denom(reduced(value)) == 1 for value in w*nice))
        self.assertNotEqual(sp.denom(reduced(first)), 1)
        forward = x+time*nice
        inverse = x-time*nice
        self.assertZero(substitute(inverse, variables, forward)-x)
        self.assertZero(substitute(forward, variables, inverse)-x)
        self.assertZero(forward.jacobian(variables).det()-1)

    def test_actual_sliced_action_keeps_good_partials_under_both_shears(self):
        w, a, b, z, ap, bp = sp.symbols("w a b z ap bp")
        variables = (w, a, b, z)
        action = sp.Matrix([a+2*b, 1, 1, 0])
        pa = sp.Matrix([0, 1, 0, 0])
        pb = sp.Matrix([0, 0, 1, 0])
        self.assertZero(act(action, a, variables)-1)
        self.assertZero(bracket(action, bracket(action, pa, variables), variables))
        self.assertZero(bracket(action, bracket(action, pb, variables), variables))
        forward = sp.Matrix([w, a+b/2-w*z/12, b, z])
        inverse = sp.Matrix([w, ap-b/2+w*z/12, b, z])
        target_variables = (w, ap, b, z)
        transformed = substitute(forward.jacobian(variables)*action,
                                 variables, inverse)
        transformed_good = sp.Matrix([0, 0, 1, 0])
        first = bracket(transformed, transformed_good, target_variables)
        self.assertNotEqual(first, sp.zeros(4, 1))
        self.assertZero(bracket(transformed, first, target_variables))
        self.assertZero(act(transformed, inverse[1], target_variables)-1)
        old_good = pb-pa/2
        self.assertZero(substitute(forward.jacobian(variables)*old_good,
                                   variables, inverse)-transformed_good)
        sigma = w/2+1
        second_forward = sp.Matrix([w, a, b-sigma*z/3, z])
        second_inverse = sp.Matrix([w, a, bp+sigma*z/3, z])
        second_variables = (w, a, bp, z)
        second_action = substitute(second_forward.jacobian(variables)*action,
                                   variables, second_inverse)
        self.assertZero(bracket(second_action,
                                bracket(second_action, pa, second_variables),
                                second_variables))
        self.assertZero(act(second_action, a, second_variables)-1)
        # This genuine sliced action is a good-partial transport control,
        # not a claimed realization of the degree-five residual.

    def test_repeated_denominator_with_nonunimodular_primitive_pair(self):
        u, v, a, b, j, time = sp.symbols("u v a b j time")
        variables = (u, v, a, b)
        denominator = u**2
        numerator = v
        invariant = denominator*a-numerator*b
        nice = sp.Matrix([0, 0, numerator, denominator])
        action = sp.Matrix([0, 0, 1, 0])
        self.assertEqual(sp.gcd(denominator, numerator), 1)
        self.assertTrue(all(value.subs({u: 0, v: 0}) == 0 for value in nice))
        self.assertZero(act(nice, invariant, variables))
        self.assertZero(bracket(action, nice, variables))
        self.assertZero(act(action, a, variables)-1)
        self.assertZero(act(action, invariant, variables)-denominator)
        self.assertZero(invariant.subs(a, (j+numerator*b)/denominator)-j)
        self.assertZero(((j+numerator*b)/denominator).subs(j, invariant)-a)
        self.assertEqual(invariant.subs(u, 0), -v*b)
        # These are finite illustrations of residue injectivity, not its
        # all-polynomial or all-denominator proof.
        for degree in range(1, 5):
            polynomial = j**degree+j+2
            residue = polynomial.subs(j, -v*b)
            self.assertEqual(sp.degree(residue, b), degree)
            self.assertNotEqual(sp.LC(sp.Poly(residue, b)), 0)
        x = sp.Matrix(variables)
        forward = x+time*nice
        inverse = x-time*nice
        self.assertZero(substitute(inverse, variables, forward)-x)
        self.assertZero(substitute(forward, variables, inverse)-x)


if __name__ == "__main__":
    unittest.main(verbosity=2)
