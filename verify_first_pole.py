"""Exact checks supporting the all-degree proof in deep-pass-03.md.

Standard library only. Reuses the independent sparse arithmetic checker, not
the research solver or SymPy. These are identity checks, not a formalization
of the theorem, Hensel lifting, or the open cancellation conjecture.
"""

import json
import unittest
from verify_extension import Poly, V, D, f, g, r, DX, DY, DZ

x, y, z, w, b, t = V


def geometric_sum(n):
    return sum((t**i for i in range(n+1)), Poly())


def reduce_fifth_root(poly):
    """Reduce modulo Phi_5(t)=1+t+t²+t³+t⁴, including Laurent powers."""
    answer = Poly()
    for powers, coefficient in poly.terms.items():
        remainder = powers[5] % 5
        base = list(powers)
        base[5] = 0
        factor = t**remainder if remainder < 4 else -geometric_sum(3)
        answer += Poly({tuple(base): coefficient})*factor
    return answer


def reduce_pair_surface(poly):
    """Reduce modulo w³=b⁶*t*S4(t); w denotes F, not the fourth endpoint."""
    answer = Poly()
    for powers, coefficient in poly.terms.items():
        if powers[3] < 0:
            raise ValueError("Clear negative F powers before surface reduction")
        quotient, remainder = divmod(powers[3], 3)
        base = list(powers)
        base[3] = remainder
        answer += Poly({tuple(base): coefficient})*(b**6*t*geometric_sum(4))**quotient
    return answer


class FirstPoleChecks(unittest.TestCase):
    def test_cyclotomic_arithmetic_and_negative_controls(self):
        self.assertEqual(reduce_fifth_root(t**5), 1)
        self.assertEqual(reduce_fifth_root(geometric_sum(4)), 0)
        self.assertEqual(reduce_fifth_root(t*t**-1), 1)
        for j in range(1, 5):
            self.assertNotEqual(reduce_fifth_root(t**j-1), 0)

    def test_residue_test_for_monomials_through_degree_thirty(self):
        # The proof handles arbitrary polynomials by independence of powers b^j.
        for n in range(31):
            difference = reduce_fifth_root((b*t)**n-b**n)
            self.assertEqual(difference == 0, n % 5 == 0)

    def test_hard_candidate_and_polynomial_shear(self):
        h = x*r
        coefficient = 3*g*x-2*f**3
        self.assertEqual(D(h), f*coefficient)
        self.assertEqual(h, -x**4-f*x*y)
        self.assertEqual(coefficient, -8*x**3*r-D(x*y))

    def test_normalized_positive_case_degree_five(self):
        k = -f*z-2*x*x*y
        self.assertEqual(x**5-g, f*k)
        self.assertEqual(D(k), 10*x**4*r)
        images = (DX, DY, DZ, 1+10*x**4*r)
        self.assertEqual(D(w-k, images), 1)
        self.assertNotEqual(D(w+k, images), 1)

    def test_positive_polynomial_composition(self):
        k = (-f*z-2*x*x*y)*(x**5+g+1)
        self.assertEqual(x**10+x**5-g*g-g, f*k)
        self.assertEqual(D(k), 2*r*(10*x**9+5*x**4))
        self.assertEqual(D(w-k, (DX, DY, DZ, 1+D(k))), 1)

    def test_naive_primitive_ansatz_counterexample(self):
        h = f*z+x*x*y
        self.assertEqual(f*h, r*x*x+g)
        self.assertEqual(D(h), 5*g*x*x-4*f**3*x)
        # This image is not divisible by f, witnessed on the cone f=0.
        self.assertEqual(D(h).at({0: b*b, 1: b*t, 2: t*t}), 5*b**14)

    def test_reduced_derivation_on_the_cone(self):
        cone = {0: b*b, 1: b*t, 2: t*t}
        self.assertEqual(f.at(cone), 0)
        self.assertEqual(g.at(cone), b**10)
        self.assertEqual(DX.at(cone), 0)
        self.assertEqual(DY.at(cone), 5*b**10)
        self.assertEqual(DZ.at(cone), 10*b**9*t)

    def test_paired_points_have_same_invariants(self):
        # F=w, a=b, ratio=t; all denominators here are units in the proof.
        left = {0: b, 1: 0, 2: w*b**-1}
        right = {0: b*t, 1: 0, 2: w*b**-1*t**-1}
        common_g = b**5*geometric_sum(5)
        for point in (left, right):
            self.assertEqual(f.at(point), w)
            self.assertEqual(reduce_pair_surface(g.at(point)-common_g), 0)
        self.assertEqual(r.at(left), -b**3)
        self.assertEqual(r.at(right), -b**3*t**3)

    def test_cleared_zero_w_certificate(self):
        # For H=xr, clear F*b²*S5 from T+(H(Q)-H(P))/F.
        cleared = 1-t**3+b**6*geometric_sum(5)*(1-t**4)
        defining_equation = geometric_sum(2)+b**6*geometric_sum(5)*geometric_sum(3)
        self.assertEqual(cleared, (1-t)*defining_equation)
        self.assertNotEqual(cleared, 0)  # relation must actually be imposed

    def test_units_at_the_fifth_root_boundary(self):
        self.assertEqual(reduce_fifth_root(geometric_sum(5)), 1)
        self.assertNotEqual(reduce_fifth_root(geometric_sum(2)), 0)
        self.assertNotEqual(reduce_fifth_root(geometric_sum(3)), 0)
        self.assertNotEqual(reduce_fifth_root(1-t**3), 0)
        self.assertNotEqual(reduce_fifth_root(geometric_sum(4).diff(5)), 0)

    def test_formal_root_simple_derivative(self):
        # X^6-dX+epsilon^3 at epsilon=0, d=b^5, X=b or zeta*b.
        equation = x**6-b**5*x+w**3
        for root in (b, b*t):
            self.assertEqual(reduce_fifth_root(equation.at({0: root, 3: 0})), 0)
            self.assertEqual(reduce_fifth_root(equation.diff(0).at({0: root})), 5*b**5)

    def test_general_formal_lift_first_nonconstant_term(self):
        # Hensel starts at alpha - epsilon^3/(5d). Remainder has order >=6.
        from fractions import Fraction
        equation = x**6-b**5*x+w**3
        for root in (b, b*t):
            approximation = root-Fraction(1, 5)*w**3*b**-5
            residual = reduce_fifth_root(equation.at({0: approximation}))
            self.assertNotEqual(residual, 0)
            self.assertTrue(all(powers[3] >= 6 for powers in residual.terms))

    def test_L_monomial_identity(self):
        for n in range(6):
            expected = (2*n+1)*g*x**n
            if n:
                expected -= 2*n*f**3*x**(n-1)
            self.assertEqual(D(r*x**n), f*expected)

    def test_average_L_correction_on_symmetric_orbit(self):
        # Here x,y,z are formal X,F,G and b,t are epsilon,q.
        # w is the normalized integration variable u.
        for p in (Poly.coerce(1), x, x*x, x*x+y*z+x*z*z):
            lp = z*p+2*(x*z-y**3)*p.diff(0)
            along = lp.at({0: 4*t**-1*(w*w-w), 1: -b*b, 2: t*b**6})
            average = Poly()
            from fractions import Fraction
            for powers, coefficient in along.terms.items():
                exponent = powers[3]
                self.assertGreaterEqual(exponent, 0)
                out = list(powers)
                out[3] = 0
                average += Poly({tuple(out): coefficient*Fraction(1, exponent+1)})
            expected = t*b**6*p.at({0: 0, 1: -b*b, 2: t*b**6})
            self.assertEqual(average, expected)

    def test_unit_middle_coefficient_with_large_correction(self):
        # For A=1+F*X² and P(0,F,G)=1+G², q²*J(q) has
        # nonzero constant, unit q² coefficient, and only higher correction terms.
        from fractions import Fraction
        polynomial = t*t-Fraction(8, 15)*b*b+t**3*b**6+t**5*b**18
        self.assertEqual(polynomial.at({5: 0}), -Fraction(8, 15)*b*b)
        middle = {powers: c for powers, c in polynomial.terms.items() if powers[5] == 2}
        self.assertEqual(Poly(middle), t*t)

    def test_fiber_shear_identity(self):
        # Clearing alpha=f verifies the shear on every nonzero f fiber.
        p = x*x+f*g+x*g*g
        lp = g*p+2*(x*g-f**3)*(2*x+g*g)
        self.assertEqual(D(r*p), f*lp)


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(FirstPoleChecks))
    print(json.dumps({
        "tests_run": result.testsRun,
        "successful": result.wasSuccessful(),
        "dependencies": "standard library; arithmetic from verify_extension.py",
        "scope": "exact identities supporting the written first-pole theorem",
        "general_cancellation_solved": False,
        "novelty_established": False,
        "formal_proof_assistant_verification": False,
    }, indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)
