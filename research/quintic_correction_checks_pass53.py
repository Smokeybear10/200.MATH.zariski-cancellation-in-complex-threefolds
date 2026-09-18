"""Finite exact controls for the actual quintic correction in pass53.

The first method checks a universal coefficient certificate before the
conic quotient. The second checks rational derivative and local-basis
identities. Neither method proves actual flatness, regular-sequence
division, divisor contraction, or existence of an obstruction point.
Only the written theorem, with its full hypotheses, makes those claims.
"""

import unittest
import sympy as sp


def coefficient_data():
    a, b, z, w, epsilon = sp.symbols("a b z w epsilon")
    c, d, e, f, g, h, q1, q2, q3 = sp.symbols(
        "c d e f g h q1 q2 q3")
    b1 = a**2*c + a*b*d + b**2*e
    b2 = a**2*f + a*b*g + b**2*h
    q = a**2*q1 + a*b*q2 + b**2*q3
    r = a*z + b*w
    conic = epsilon*r**2 - 2*b2*z + 2*b1*w - q
    u = (epsilon*w**2 - 2*h*z + 2*e*w - q3)/a
    v = (epsilon*z**2 - 2*f*z + 2*c*w - q1)/b
    t = -(b*u-a*v)/2 - g*z + d*w - q2/2
    numerators = (
        a*(2*c*q3-f*q2)
        + b*(2*d*q3-(e+g)*q2+2*h*q1),
        a*(4*c*h-2*f*g)
        + b*(4*d*h-2*e*g+4*f*h-2*g**2+epsilon*q3),
        -a*(4*c*e-2*d*f+epsilon*q1)
        - b*(4*c*h+2*d*e-2*d*g+epsilon*q2),
        2*a**2*c+2*a*b*d+a*b*f+b**2*(e+g),
        a**2*f+a*b*(e+g)+2*b**2*h,
    )
    ra = (
        2*c*q3-f*q2+(4*c*h-2*f*g)*z
        -(4*c*e-2*d*f+epsilon*q1)*w
        +(2*a*c+2*b*d+b*f)*u+(a*f+b*(e+g))*v
    )/epsilon
    rb = (
        2*d*q3-(e+g)*q2+2*h*q1
        +(4*d*h-2*e*g+4*f*h-2*g**2+epsilon*q3)*z
        -(4*c*h+2*d*e-2*d*g+epsilon*q2)*w
        +b*(e+g)*u+2*b*h*v
    )/epsilon
    return {
        "a": a, "b": b, "z": z, "w": w, "epsilon": epsilon,
        "coefficients": (c, d, e, f, g, h, q1, q2, q3),
        "b1": b1, "b2": b2, "r": r, "conic": conic,
        "u": u, "v": v, "t": t, "numerators": numerators,
        "ra": ra, "rb": rb,
    }


class QuinticCorrectionChecks(unittest.TestCase):
    def test_complete_coefficient_reduction_and_parameter_ideal(self):
        data = coefficient_data()
        a, b, z, w, epsilon = (
            data[name] for name in ("a", "b", "z", "w", "epsilon"))
        c, d, e, f, g, h, q1, q2, q3 = data["coefficients"]
        r, conic, u, v, t, ra, rb = (
            data[name] for name in
            ("r", "conic", "u", "v", "t", "ra", "rb"))
        numerators = data["numerators"]
        reduction = sum(n*value for n, value in zip(
            numerators, (1, z, w, u, v)))/epsilon
        certificate = (
            a*epsilon*z-2*a*f-2*b*e-b*epsilon*w-2*b*g
        )/(2*a*b*epsilon)

        # Exact in the rational polynomial ring, not just sampled
        # modulo the conic or inferred from a coefficient matrix.
        self.assertEqual(sp.cancel(r*t-reduction-conic*certificate), 0)
        self.assertEqual(sp.cancel(a*ra+b*rb-reduction), 0)
        self.assertNotEqual(sp.cancel(r*t-reduction), 0)
        self.assertEqual(sp.cancel(
            a*(z*t-ra)+b*(w*t-rb)-conic*certificate), 0)
        self.assertEqual(sp.cancel(
            (z*t-ra)/b+(w*t-rb)/a
            -conic*certificate/(a*b)), 0)

        # Polynomial m-membership, including the stronger m² terms,
        # is checked with exact coefficient-ring operations.
        for index, numerator in enumerate(numerators):
            polynomial = sp.Poly(sp.expand(numerator), a, b)
            required_order = 2 if index >= 3 else 1
            self.assertTrue(polynomial.terms())
            self.assertTrue(all(
                sum(monomial) >= required_order
                for monomial, coefficient in polynomial.terms()
                if coefficient != 0))
        self.assertEqual(
            sp.expand(numerators[3]).subs({a: 0, b: 0}), 0)
        self.assertEqual(
            sp.expand(numerators[4]).subs({a: 0, b: 0}), 0)

    def test_quintic_derivatives_and_full_local_fifth_basis(self):
        data = coefficient_data()
        a, b, z, w, epsilon = (
            data[name] for name in ("a", "b", "z", "w", "epsilon"))
        r, u, v, t, ra, rb = (
            data[name] for name in ("r", "u", "v", "t", "ra", "rb"))
        # These highest-derivative identities hold even before
        # imposing the coherent B1,B2 coefficient specialization.
        b1, b2 = sp.symbols("B1 B2")
        p = a*b1+b*b2

        def derive(value):
            return sp.expand(
                sp.diff(value, z)*(epsilon*b*r+b1)
                + sp.diff(value, w)*(-epsilon*a*r+b2))

        def iterate(value, count):
            for _ in range(count):
                value = derive(value)
            return value

        self.assertEqual(sp.cancel(derive(r)-p), 0)
        self.assertEqual(sp.cancel(iterate(t, 3)-3*epsilon**2*p**2), 0)
        self.assertEqual(iterate(t, 4), 0)
        for quartic, parameter in ((u, a), (v, b)):
            self.assertEqual(sp.cancel(
                iterate(quartic, 4)-6*epsilon**3*parameter*p**2), 0)
            self.assertEqual(iterate(quartic, 5), 0)
        for correction in (ra, rb):
            self.assertEqual(iterate(correction, 5), 0)
        for value, parameter in ((r*u, a), (r*v, b),
                                 (z*t, b), (w*t, -a)):
            self.assertEqual(sp.cancel(
                iterate(value, 5)-30*epsilon**3*parameter*p**3), 0)
            self.assertEqual(iterate(value, 6), 0)
        for candidate in ((z*t-ra)/b, -(w*t-rb)/a):
            self.assertEqual(sp.cancel(
                iterate(candidate, 5)-30*epsilon**3*p**3), 0)
            self.assertEqual(iterate(candidate, 6), 0)

        # Independent normalized monic quadratic chart. The diagonal
        # leading coefficients prove generic independence only;
        # actual local spanning and global contraction stay in the proof.
        rho, eta, local_p = sp.symbols("rho eta local_p")
        upsilon = (rho**2-eta)/local_p
        basis = (sp.Integer(1), rho, upsilon,
                 rho*upsilon, upsilon**2, rho*upsilon**2)
        expected = (1, local_p, 2*local_p,
                    6*local_p**2, 24*local_p**2, 120*local_p**3)
        for degree, (value, top) in enumerate(zip(basis, expected)):
            self.assertEqual(sp.cancel(
                local_p**degree*sp.diff(value, rho, degree)-top), 0)
            self.assertEqual(sp.diff(value, rho, degree+1), 0)
        matrix = sp.Matrix([
            [sp.expand(value).coeff(rho, degree) for degree in range(6)]
            for value in basis])
        self.assertEqual(sp.cancel(matrix.det()-local_p**-6), 0)


if __name__ == "__main__":
    unittest.main()

