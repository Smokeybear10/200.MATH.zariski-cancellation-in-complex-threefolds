"""Independent exact controls for the horizontal-selection criterion.

The all-parameter proof is in horizontal-selection-pass29.md.
Only unittest and SymPy are used; no old checker or solver is imported.
"""

import unittest

import sympy as sp


lam, x, w, z, a, b, c, Q = sp.symbols("lam x w z a b c Q")
F = 2*x*z-w**2
kappa = 2*a*c-b**2
variables = (lam, x, w, z)
vertical = (0, 0, x**2, 2*(1+lam*x)**2*w)
physical_examples = (lam, lam*Q, lam**2+lam*Q,
                     lam**2*(1+x)+lam*Q)


def apply(field, expression, coordinates=variables):
    return sp.expand(sum(value*sp.diff(expression, variable)
                         for value, variable in zip(field, coordinates)))


def frame(polynomial):
    jp = polynomial.subs(Q, F)
    jf = polynomial.subs({x: a, Q: kappa}, simultaneous=True)
    gf = sp.diff(polynomial, lam).subs(Q, F)
    invariant = (x, w-x*jp, z-jp*w+x*jp**2/2)
    inverse = {x: a, w: b+a*jf, z: c+b*jf+a*jf**2/2}
    horizontal = (1, 0, x*gf, w*gf)
    return invariant, inverse, horizontal


def conjugated_values(polynomial):
    jj = polynomial.subs({x: a, Q: kappa}, simultaneous=True)
    jq = sp.diff(polynomial, Q).subs({x: a, Q: kappa}, simultaneous=True)
    vv = 1+lam*a
    ww = b+a*jj
    tt = 2*a*ww*(2*vv**2-a)
    return (sp.Integer(0), a**2-a*jq*tt,
            2*vv**2*ww-jj*a**2-b*jq*tt)


class HorizontalSelectionChecks(unittest.TestCase):
    def test_pointwise_plane_fixing_alone_does_not_give_an_lnd(self):
        # G=w fixes x,F but lies outside the classified invariant-coefficient ring.
        bad = (1, 0, x*w, w**2)
        self.assertEqual(apply(bad, x), 0)
        self.assertEqual(apply(bad, F), 0)
        self.assertEqual(apply(bad, lam), 1)
        current = w
        for j in range(1, 7):
            current = apply(bad, current)
            self.assertEqual(current, x**j*w)
            self.assertNotEqual(current, 0)

    def test_planar_nonnilpotence_degree_controls(self):
        for m in (2, 3, 4):
            coefficient = (lam+1)*w**m+lam**2
            current = w
            for j in range(1, 5):
                current = sp.expand(sp.diff(current, lam)
                                    +coefficient*sp.diff(current, w))
                self.assertEqual(sp.degree(current, w), 1+j*(m-1))
                self.assertNotEqual(current, 0)
        for aa in (sp.Integer(2), lam+1, lam**2+3):
            coefficient = aa*w+lam**3
            current = w
            for j in range(1, 5):
                current = sp.expand(sp.diff(current, lam)
                                    +coefficient*sp.diff(current, w))
                actual = current.coeff(w, 1)
                self.assertEqual(sp.degree(actual, lam), j*sp.degree(aa, lam))
                self.assertEqual(sp.LC(sp.Poly(actual, lam)),
                                 sp.LC(sp.Poly(aa, lam))**j)

    def test_actual_time_dependent_frames_have_both_polynomial_inverses(self):
        for polynomial in physical_examples:
            invariant, inverse, _ = frame(polynomial)
            for actual, expected in zip(invariant, (a, b, c)):
                self.assertEqual(sp.expand(actual.subs(inverse, simultaneous=True)-expected), 0)
            forward = dict(zip((a, b, c), invariant))
            for generator in (x, w, z):
                self.assertEqual(sp.expand(inverse[generator].subs(forward, simultaneous=True)
                                          -generator), 0)
            self.assertEqual(sp.expand(F.subs(inverse, simultaneous=True)-kappa), 0)

    def test_actual_horizontal_invariants_and_slice(self):
        for polynomial in physical_examples:
            invariant, _, horizontal = frame(polynomial)
            self.assertEqual(apply(horizontal, lam), 1)
            self.assertEqual(apply(horizontal, x), 0)
            self.assertEqual(apply(horizontal, F), 0)
            for coordinate in invariant:
                self.assertEqual(apply(horizontal, coordinate), 0)
            # The explicit original generators have finite degree under this actual action.
            for generator in variables:
                current = generator
                for _ in range(2*sp.degree(polynomial, lam)+2):
                    current = apply(horizontal, current)
                self.assertEqual(current, 0)

    def test_full_conjugated_values_of_the_actual_canonical_action(self):
        for polynomial in physical_examples:
            invariant, inverse, _ = frame(polynomial)
            for coordinate, expected in zip(invariant, conjugated_values(polynomial)):
                actual = apply(vertical, coordinate).subs(inverse, simultaneous=True)
                self.assertEqual(sp.expand(actual-expected), 0)

    def test_both_exact_top_branches_including_r_less_than_s(self):
        examples = (
            (sp.Integer(0), 2, True), (lam, 3, True),
            (lam**2*(x+1), 4, True), (lam*Q, 4, False),
            (lam**3+lam*Q, 6, False),
            (lam*x**2+lam**4*(Q+1)**2, 10, False),
        )
        for polynomial, expected_degree, sliced in examples:
            values = tuple(sp.expand(v) for v in conjugated_values(polynomial))
            actual_degree = max(sp.degree(v, lam) for v in values)
            self.assertEqual(actual_degree, expected_degree)
            top = tuple(v.coeff(lam, expected_degree) for v in values)
            if not sliced:
                ss = sp.degree(polynomial, lam)
                derivative = sp.diff(polynomial, Q)
                rr = sp.degree(derivative, lam)
                self.assertEqual(expected_degree, ss+rr+2)
                hs = polynomial.coeff(lam, ss).subs({x: a, Q: kappa}, simultaneous=True)
                kr = derivative.coeff(lam, rr).subs({x: a, Q: kappa}, simultaneous=True)
                factor = -4*a**4*hs*kr
                self.assertEqual(tuple(sp.expand(v-e) for v, e
                                       in zip(top, (0, factor*a, factor*b))), (0, 0, 0))
            else:
                self.assertEqual(top[:2], (0, 0))
                self.assertNotEqual(top[2], 0)
                self.assertEqual(sp.diff(polynomial, Q), 0)
                if polynomial == 0:
                    expected = 2*a**2*b
                else:
                    ss = sp.degree(polynomial, lam)
                    expected = 2*a**3*polynomial.coeff(lam, ss).subs(x, a)
                self.assertEqual(sp.expand(top[2]-expected), 0)

    def test_equal_degree_opposite_outcomes_and_nonmonotonicity(self):
        for degree in range(4, 9):
            good = lam**(degree-2)
            bad = lam**(degree-3)+lam*Q
            for polynomial in (good, bad):
                values = conjugated_values(polynomial)
                self.assertEqual(max(sp.degree(v, lam) for v in values), degree)
            self.assertEqual(sp.diff(good, Q), 0)
            self.assertEqual(sp.diff(bad, Q), lam)
            good_top = tuple(sp.expand(v).coeff(lam, degree)
                             for v in conjugated_values(good))
            bad_top = tuple(sp.expand(v).coeff(lam, degree)
                            for v in conjugated_values(bad))
            self.assertEqual(good_top[:2], (0, 0))
            self.assertNotEqual(good_top[2], 0)
            self.assertEqual(sp.expand(a*bad_top[2]-b*bad_top[1]), 0)
            self.assertNotEqual(bad_top[1], 0)
        self.assertEqual(max(sp.degree(v, lam) for v in conjugated_values(lam**3)), 5)
        self.assertEqual(max(sp.degree(v, lam) for v in conjugated_values(lam*Q)), 4)

    def test_primitive_top_obstructions_and_identical_joint_field_gate(self):
        top = (0, a, b)
        coords = (a, b, c)
        self.assertEqual(sp.gcd(a, b), 1)
        self.assertEqual(apply(top, kappa, coords), 0)
        self.assertEqual(apply(top, b, coords), a)
        for generator in coords:
            self.assertEqual(apply(top, generator, coords).subs({a: 0, b: 0}), 0)
        self.assertEqual(apply((0, 0, 1), c, coords), 1)
        self.assertEqual(sp.det(sp.Matrix([[a**2, 2*b], [a, b]])), a**2*b-2*a*b)
        for polynomial in physical_examples:
            self.assertEqual(tuple(sp.expand(v).coeff(lam, 0)
                                   for v in conjugated_values(polynomial)), (0, a**2, 2*b))


if __name__ == "__main__":
    unittest.main(verbosity=2)
