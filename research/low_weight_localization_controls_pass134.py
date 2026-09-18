"""Exact finite low-weight and localization boundary controls for pass134.

The actual129 polynomial frame is reconstructed without previous imports.
Its beta invariant and original-weight initials provide a concrete graded
ring control; finite monomial signatures do not prove an arbitrary invariant
graded-ring theorem or correction passage. The second method localizes this
same actual frame at a leading-invariant denominator. It distinguishes the
localized leading LND from the actual selected partial, which need not remain
locally nilpotent after localization, and a localized Jacobian unit from a
complex constant. No localized rational inverse is called a global one.
The deliberately rescaled xi=u/a is not the X-fixed, normalized Jacobian-one
chart in the localization proof. That proof inherits N/s^2 and does not need
local nilpotence of the actual partial after localization.
"""

import itertools
import math
import unittest

import sympy as s


def expanded_zero(expr):
    return s.expand(expr) == 0


def weighted_initial(expr, variables, weights):
    poly = s.Poly(expr, *variables, domain=s.QQ)
    terms = poly.terms()
    degree = max(sum(i*w for i, w in zip(monomial, weights)) for monomial, _ in terms)
    top = sum(coefficient*s.prod(variable**power for variable, power in zip(variables, monomial))
              for monomial, coefficient in terms
              if sum(i*w for i, w in zip(monomial, weights)) == degree)
    return degree, s.expand(top)


class LowWeightLocalizationControls(unittest.TestCase):
    def test_actual_beta_and_original_weight_initials(self):
        a, b, v, u = s.symbols("a b v u")
        X, Y, Z, W = s.symbols("X Y Z W")
        AA, BB, VV, BETA = s.symbols("AA BB VV BETA")
        half = s.Rational(1, 2)

        def delta(aa, vv, xx):
            return 3*half*aa*vv**2+3*half*aa**2*vv*xx+half*aa**3*xx**2

        frame = [u, v+a*u, a-half*v**3+b*u, b+delta(a, v, u)]
        actual = dict(zip((X, Y, Z, W), frame))
        a_original = Z-X*W+half*Y**3
        v_original = Y-a_original*X
        b_original = W-delta(a_original, v_original, X)
        recovered_a = s.expand(a_original.subs(actual, simultaneous=True))
        recovered_v = s.expand(frame[1]-recovered_a*frame[0])
        recovered_b = s.expand(frame[3]-delta(recovered_a, recovered_v, frame[0]))
        self.assertEqual([recovered_a, recovered_b, recovered_v, frame[0]], [a, b, v, u])

        # Reverse composition uses independent placeholders before imposing
        # the displayed inverse a=Z-XW+Y^3/2, not a sampled relation.
        reverse = [X, VV+AA*X, AA-half*VV**3+BB*X, BB+delta(AA, VV, X)]
        reverse = [s.expand(f.subs(BB, W-delta(AA, VV, X))) for f in reverse]
        reverse = [s.expand(f.subs(VV, Y-AA*X)) for f in reverse]
        reverse = [s.expand(f.subs(AA, a_original)) for f in reverse]
        self.assertEqual(reverse, [X, Y, Z, W])
        self.assertTrue(expanded_zero(s.Matrix(frame).jacobian((a, b, v, u)).det()+1))
        self.assertEqual([s.diff(f, u) for f in frame[:3]], [1, a, b])
        self.assertEqual(s.diff(frame[3], u, 2), a**3)

        beta = b+half*a*v**2
        beta_original = W-a_original*Y**2+half*a_original**2*X*Y
        self.assertTrue(expanded_zero(beta_original-b_original-half*a_original*v_original**2))
        self.assertTrue(expanded_zero(beta_original.subs(actual, simultaneous=True)-beta))
        self.assertEqual(s.diff(beta, u), 0)
        self.assertEqual((BETA-half*a*v**2).subs(BETA, beta), b)
        self.assertEqual((b+half*a*v**2).subs(b, BETA-half*a*v**2), BETA)

        Phi = 2*X*W-Y**3
        self.assertTrue(expanded_zero(Phi.subs(actual, simultaneous=True)-2*frame[2]+2*a))
        targets = [(a_original, 3, -Phi/2),
                   (v_original, 4, X*Phi/2),
                   (beta_original, 8, X*Y*Phi**2/8)]
        for polynomial, expected_degree, expected_top in targets:
            degree, top = weighted_initial(polynomial, (X, Y, Z, W), (1, 1, 1, 2))
            with self.subTest(weight=expected_degree):
                self.assertEqual(degree, expected_degree)
                self.assertTrue(expanded_zero(top-expected_top))

        # Phi,X,Y are independent: at X!=0, W=(Phi+Y^3)/(2X).
        P = s.symbols("P")
        self.assertTrue(expanded_zero(Phi.subs(W, (P+Y**3)/(2*X))-P))
        initials = s.Matrix([-P/2, X*P/2, X*Y*P**2/8])
        self.assertTrue(expanded_zero(initials.jacobian((P, X, Y)).det()+X*P**3/32))
        aa0, vv0, bb0 = s.symbols("aa0 vv0 bb0", nonzero=True)
        rational_inverse = {P: -2*aa0, X: -vv0/aa0, Y: -2*bb0/(aa0*vv0)}
        self.assertEqual([s.cancel(f.subs(rational_inverse, simultaneous=True)) for f in initials],
                         [aa0, vv0, bb0])
        self.assertEqual(s.cancel((X*Phi)/Phi), X)

        # Finite signatures in the independent coordinates (Phi,X,Y).
        # The polynomial/normal graded-ring conclusion rests on the note.
        signatures = {(i+j+2*k, j+k, k)
                      for i, j, k in itertools.product(range(5), repeat=3)}
        self.assertEqual(len(signatures), 125)
        exponent_matrix = s.Matrix([[1, 1, 2], [0, 1, 1], [0, 0, 1]])
        self.assertEqual(exponent_matrix.det(), 1)
        small_weights = {3*i+4*j+8*k for i in range(3) for j in range(3) for k in range(2)
                         if 3*i+4*j+8*k <= 8}
        self.assertNotIn(1, small_weights)
        self.assertIn(3, small_weights)

    def test_leading_invariant_denominator_and_localized_jacobian_unit(self):
        a, b, v, u, xi = s.symbols("a b v u xi")
        half = s.Rational(1, 2)
        frame = [u, v+a*u, a-half*v**3+b*u,
                 b+3*half*a*v**2+3*half*a**2*v*u+half*a**3*u**2]

        def T(f):
            return s.cancel(-u*s.diff(f, a)+(1+3*half*v**2*u)*s.diff(f, b)
                            +u**2*s.diff(f, v))

        def N(f):
            return s.diff(f, v)

        # Before localization this is the actual partial in the last slot.
        self.assertEqual([T(f) for f in frame], [0, 0, 0, 1])
        self.assertEqual([s.expand(T(f)).coeff(u, 2) for f in (a, b, v)], [0, 0, 1])
        self.assertEqual(N(a), 0)
        self.assertEqual(N(1/a), 0)
        self.assertEqual(N(v/a), 1/a)
        self.assertEqual(N(N(v/a)), 0)

        # A_a[u]=A_a[xi] with the deliberately rescaled xi=u/a. This is
        # not the X-fixed normalized chart of the rigidity proof. Its
        # Jacobian is a localized unit, not a complex constant; xi itself
        # is not a global polynomial.
        self.assertEqual(s.cancel((u/a).subs(u, a*xi)), xi)
        self.assertEqual(s.cancel((a*xi).subs(xi, u/a)), u)
        localized_map = s.Matrix([a, b, v, u/a])
        jac = localized_map.jacobian((a, b, v, u)).det()
        self.assertEqual(s.cancel(jac), 1/a)
        self.assertEqual(s.cancel(jac*a), 1)
        self.assertNotEqual(s.diff(jac, a), 0)
        self.assertEqual(s.Poly(u, a).coeff_monomial(1), u)
        self.assertEqual(u.subs({a: 0, u: 1}), 1)
        self.assertEqual(s.diff(u/a, u), 1/a)

        # Leading-invariance of a is insufficient to localize T as an LND.
        # The following four exact iterates are finite controls, not an
        # arbitrary-denominator theorem. In fact T(xi)=xi^2 after change.
        iterate = 1/a
        for j in range(1, 5):
            iterate = T(iterate)
            expected = math.factorial(j)*u**j/a**(j+1)
            with self.subTest(iterate=j):
                self.assertEqual(s.cancel(iterate-expected), 0)
                self.assertNotEqual(iterate, 0)
        self.assertEqual(s.cancel(T(u/a).subs(u, a*xi)), xi**2)
        localized_horizontal = [s.expand(T(f).subs(u, a*xi)) for f in (a, b, v)]
        self.assertEqual([f.coeff(xi, 2) for f in localized_horizontal], [0, 0, a**2])
        self.assertEqual(s.diff(a, v)*a**2, 0)
        self.assertEqual(s.diff(1/a, v)*a**2, 0)
        # The vertical xi-degree is two, so its filtration shift is one,
        # below the horizontal shift two. It does not enter the top N.
        self.assertEqual(s.Poly(xi**2, xi).degree()-1, 1)


if __name__ == "__main__":
    unittest.main()
