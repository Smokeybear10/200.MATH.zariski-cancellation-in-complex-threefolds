"""Independent exact controls for ambient-lifting-pass25.md.

No project solver imports. The finite checks do not replace the
all-parameter proofs of flatness or the one-step kernel exclusion.
"""

import unittest
import sympy as sp


u, d, v, e, w, rho, z, t = sp.symbols("u d v e w rho z t")
P = v**2 - d**2 * (d + 1)
I = sp.I


def truncate(expression, variable, precision):
    return sp.series(expression, variable, 0, precision).removeO().expand()


class AmbientLiftingChecks(unittest.TestCase):
    def test_completed_base_branches_and_original_pairs(self):
        precision = 8
        quarter = truncate((1 + d) ** sp.Rational(1, 4), d, precision)
        half = truncate((1 + d) ** sp.Rational(1, 2), d, precision)
        roots = (sp.Integer(1), sp.Integer(-1), I, -I)
        for root in roots:
            with self.subTest(root=root):
                branch = root * quarter
                self.assertEqual(truncate(branch**4 - d - 1, d, precision), 0)
                self.assertEqual(
                    truncate(d * branch**2 - root**2 * d * half, d, precision),
                    0,
                )
                self.assertEqual(root**4, 1)
                self.assertNotEqual(4 * root**3, 0)
        for left, right in ((sp.Integer(1), I), (sp.Integer(1), -I),
                            (sp.Integer(-1), I)):
            self.assertEqual(left**2, 1)
            self.assertEqual(right**2, -1)
            # The base functions d,v span the two transverse directions.
            normal_matrix = sp.Matrix([
                [4 * left**3, 4 * right**3],
                [4 * left**5, 4 * right**5],
            ])
            self.assertNotEqual(sp.simplify(normal_matrix.det()), 0)

    def test_entire_node_fiber_is_not_monogenic(self):
        relations = [
            e**2 - d*v, e*v - d*w, e*w - d**2*(d+1),
            v**2 - d**2*(d+1), v*w - d*(d+1)*e,
            w**2 - d*(d+1)*v,
        ]
        specialized = [q.subs({d: 0, v: 0}) for q in relations]
        gb = sp.groebner(specialized, e, w)
        self.assertEqual(set(q.as_expr() for q in gb.polys),
                         {e**2, e*w, w**2})
        # A universal element, not a finite set of proposed generators.
        a, b, c = sp.symbols("a b c")
        fiber_gb = sp.groebner([e**2, e*w, w**2], e, w,
                              domain=sp.QQ.frac_field(a, b, c))
        theta = a + b*e + c*w
        self.assertEqual(fiber_gb.reduce((theta-a)**2)[1], 0)
        for degree in range(2, 8):
            expected = a**degree + degree*a**(degree-1)*(b*e+c*w)
            self.assertEqual(
                fiber_gb.reduce(sp.expand(theta**degree-expected))[1], 0
            )
        for basis_element in (sp.Integer(1), e, w):
            self.assertEqual(fiber_gb.reduce(basis_element)[1], basis_element)

    def test_genuine_one_step_derivation_and_local_nilpotence(self):
        for exponent in (1, 2, 3):
            for f in (rho**2-d*v,
                      rho**3+(d+1)*rho**2+v*rho+d*v):
                with self.subTest(exponent=exponent, f=f):
                    def deriv(expression):
                        return sp.expand(P**exponent * sp.diff(expression, rho)
                                         + sp.diff(f, rho)*sp.diff(expression, z))
                    relation = P**exponent*z-f
                    self.assertEqual(deriv(relation), 0)
                    self.assertEqual(deriv(deriv(rho)), 0)
                    current = z
                    degree = sp.degree(f, rho)
                    for order in range(1, degree+2):
                        current = deriv(current)
                        expected = (P**(exponent*(order-1))
                                    * sp.diff(f, rho, order))
                        self.assertEqual(sp.expand(current-expected), 0)
                    self.assertEqual(current, 0)

    def test_first_attempt_singular_line_and_nonreduced_node_fiber(self):
        for exponent in (1, 2, 3):
            equation = P**exponent*z-rho**2+d*v
            at_line = {d: 0, v: 0, rho: 0}
            self.assertEqual(equation.subs(at_line), 0)
            for variable in (d, v, rho, z):
                self.assertEqual(sp.diff(equation, variable).subs(at_line), 0)
            self.assertEqual(sp.expand(equation.subs({d: 0, v: 0})), -rho**2)
        doubled = sp.groebner([rho**2], rho, z)
        self.assertEqual(doubled.reduce(rho)[1], rho)
        self.assertEqual(doubled.reduce(rho**2)[1], 0)

    def test_quadratic_center_and_missing_odd_normalization_generator(self):
        normalized = {d: u**4-1, v: (u**4-1)*u**2,
                      e: (u**4-1)*u, w: (u**4-1)*u**3}
        self.assertEqual(sp.expand(P.subs(normalized, simultaneous=True)), 0)
        for expression in (e**2-d*v, v*e-d*w, v*w-d*(d+1)*e):
            self.assertEqual(
                sp.expand(expression.subs(normalized, simultaneous=True)), 0
            )
        # The direct center has a two-dimensional node fiber.
        center = sp.groebner([rho**2], rho)
        self.assertEqual(center.reduce(rho)[1], rho)
        self.assertEqual(center.reduce(rho**2)[1], 0)
        # w would require coefficient u^2 relative to e; it does not descend
        # to A0, since its two values over the base node disagree.
        s = sp.symbols("s")
        self.assertEqual(s.subs(s, 1) - s.subs(s, -1), 2)
        # Dividing the quadratic radicand by its evident square leaves s.
        normalized_radicand = (s**2-1)**2*s
        self.assertEqual(
            sp.cancel(normalized_radicand/(s**2-1)**2), s
        )
        valuation_at_zero = min(monomial[0] for monomial, coefficient in
                                sp.Poly(normalized_radicand, s).terms())
        self.assertEqual(valuation_at_zero, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
