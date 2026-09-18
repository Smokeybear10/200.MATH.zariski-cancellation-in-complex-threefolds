"""Independent finite multiplicity and lower-weight-drop controls.

The actual cubic129 frame is reconstructed here with its polynomial inverse
and selected bad partial. For k=1,...,4, powers of its invariant v realize the
sharp original-weight bound, while powers of a realize the strict case. The
last method distinguishes those ORIGINAL coordinate weights from weights after
adjoining an invariant generator, with explicit successive cancellations.

No earlier checker/search is imported. These examples do not verify the
universal multiplicity theorem, generation of the full associated graded
ring, termination of subduction, or any unrestricted recognition claim.
"""

import unittest

import sympy as sp


class WeightedSubductionControls(unittest.TestCase):
    @staticmethod
    def act(field, value, variables):
        return sp.expand(sum(coefficient*sp.diff(value, variable)
                             for coefficient, variable in zip(field, variables)))

    @staticmethod
    def weighted_top(value, variables, weights):
        poly = sp.Poly(sp.expand(value), *variables, domain=sp.QQ)
        weighted_terms = [(sum(i*w for i, w in zip(exponents, weights)),
                           coefficient*sp.prod(x**i for x, i in zip(variables, exponents)))
                          for exponents, coefficient in poly.terms()]
        degree = max(weight for weight, term in weighted_terms)
        return degree, sp.expand(sum(term for weight, term in weighted_terms if weight == degree))

    def assert_zero(self, value):
        self.assertEqual(sp.expand(value), 0)

    def assert_vector_equal(self, left, right):
        self.assertEqual(len(left), len(right))
        for actual, expected in zip(left, right):
            self.assert_zero(actual-expected)

    @staticmethod
    def fixture():
        a, b, v, u = sp.symbols("a b v u")
        X, Y, Z, W = sp.symbols("X Y Z W")
        half = sp.Rational(1, 2)
        base, original = (a, b, v, u), (X, Y, Z, W)
        frame = sp.Matrix([u, v+a*u, a-half*v**3+b*u,
                           b+3*half*a*v**2+3*half*a**2*v*u+half*a**3*u**2])
        inverse_a = Z-X*W+half*Y**3
        inverse_v = Y-X*inverse_a
        inverse_b = (W-3*half*inverse_a*inverse_v**2
                     - 3*half*inverse_a**2*inverse_v*X-half*inverse_a**3*X**2)
        inverse = sp.Matrix([inverse_a, inverse_b, inverse_v, X])
        partial = sp.Matrix([-u, 1+3*half*v**2*u, u**2, 0])
        return base, original, frame, inverse, partial

    def test_actual_fixture_inverse_and_selected_partial(self):
        base, original, frame, inverse, partial = self.fixture()
        a, b, v, u = base
        X, Y, Z, W = original
        self.assert_vector_equal(
            inverse.subs(dict(zip(original, frame)), simultaneous=True), base)
        self.assert_vector_equal(
            frame.subs(dict(zip(base, inverse)), simultaneous=True), original)
        self.assert_zero(frame.jacobian(base).det()+1)
        self.assert_vector_equal([self.act(partial, value, base) for value in frame],
                                 (0, 0, 0, 1))
        self.assert_vector_equal(frame.jacobian(base)*partial, (0, 0, 0, 1))
        self.assert_vector_equal([sp.diff(value, u) for value in frame[:3]], (1, a, b))
        self.assert_zero(sp.diff(frame[3], u, 2)-a**3)
        self.assert_zero(partial[3])
        top = sp.Matrix([sp.Poly(value, u).coeff_monomial(u**2) for value in partial])
        self.assert_vector_equal(top, (0, 0, 1, 0))
        self.assertEqual(self.act(top, v, base), 1)
        for value in (a, b):
            self.assert_zero(self.act(top, value, base))
        phi = 2*X*W-Y**3
        self.assert_zero(phi.subs(dict(zip(original, frame)), simultaneous=True)-2*frame[2]+2*a)
        self.assert_zero(inverse[2]-Y+X*Z-X**2*W+X*Y**3/2)

    def test_finite_sharp_and_strict_multiplicity_powers(self):
        base, original, frame, inverse, partial = self.fixture()
        a, b, v, u = base
        X, Y, Z, W = original
        weights = (1, 1, 1, 2)
        phi = 2*X*W-Y**3
        # The abstract theorem calls its bad variable Z; in this concrete
        # fixture the bad variable is W, and Phi_W=2X.
        phi_bad = sp.diff(phi, W)
        initial_sub = {X: 1, Y: a, Z: b, W: a**3/2}
        actual_sub = dict(zip(original, frame))
        self.assert_zero(phi.subs(initial_sub, simultaneous=True))
        self.assert_zero(phi_bad.subs(initial_sub, simultaneous=True)-2)
        for k in range(1, 5):
            for label, original_generator, actual_generator, weight_per_power in (
                    ("sharp_v", inverse[2], v, 4),
                    ("strict_a", inverse[0], a, 3)):
                with self.subTest(k=k, case=label):
                    P = sp.expand(original_generator**k)
                    m, initial_P = self.weighted_top(P, original, weights)
                    self.assertEqual(m, weight_per_power*k)
                    psi = (X/2)**k if label == "sharp_v" else (-sp.Rational(1, 2))**k
                    self.assert_zero(initial_P-phi**k*psi)
                    quotient, remainder = sp.div(initial_P, phi**k, *original, domain=sp.QQ)
                    self.assert_zero(remainder)
                    self.assert_zero(quotient-psi)
                    _, next_remainder = sp.div(quotient, phi, *original, domain=sp.QQ)
                    self.assertNotEqual(sp.expand(next_remainder), 0)

                    actual_P = sp.expand(P.subs(actual_sub, simultaneous=True))
                    self.assert_zero(actual_P-actual_generator**k)
                    n = sp.Poly(actual_P, u).degree()
                    self.assertEqual(n, 0)
                    self.assertLessEqual(m-4*k, n)
                    self.assertLessEqual(n, m-1)
                    # Two independent descriptions of the actual kth partial:
                    # original W differentiation and the transported derivation.
                    from_original = sp.expand(sp.diff(P, W, k).subs(actual_sub, simultaneous=True))
                    from_actual = actual_P
                    for _ in range(k):
                        from_actual = self.act(partial, from_actual, base)
                    self.assert_zero(from_original-from_actual)
                    self.assertEqual(sp.Poly(from_actual, u).degree(), m-2*k)
                    expected = (sp.factorial(k)*u**(2*k) if label == "sharp_v"
                                else (-1)**k*sp.factorial(k)*u**k)
                    self.assert_zero(from_actual-expected)
                    rhs = sp.factorial(k)*psi.subs(initial_sub, simultaneous=True)*2**k
                    coefficient = sp.Poly(from_actual, u).coeff_monomial(u**(m-2*k))
                    self.assert_zero(coefficient-rhs)
                    self.assertNotEqual(sp.expand(rhs), 0)

                    h_n = sp.Poly(actual_P, u).coeff_monomial(u**n)
                    N_k = sp.diff(h_n, v, k)
                    if label == "sharp_v":
                        self.assertEqual(n, m-4*k)
                        self.assert_zero(N_k-rhs)
                        self.assert_zero(N_k-sp.factorial(k))
                        self.assert_zero(sp.diff(h_n, v, k+1))
                    else:
                        self.assertGreater(n, m-4*k)
                        self.assert_zero(N_k)
                        self.assert_zero(sp.Poly(from_actual, u).coeff_monomial(u**(n+2*k)))

    def test_iterated_drop_uses_different_enlarged_generator_weights(self):
        base, original, frame, inverse, partial = self.fixture()
        a, b, v, u = base
        X, Y, Z, W = original
        A0 = sp.symbols("A0")
        actual_sub = dict(zip(original, frame))
        phi = 2*X*W-Y**3
        self.assertEqual(self.weighted_top(phi, original, (1, 1, 1, 2))[0], 3)
        actual_phi = sp.expand(phi.subs(actual_sub, simultaneous=True))
        self.assertEqual(sp.Poly(actual_phi, u).degree(), 1)
        recovered_a = sp.expand((phi-2*Z).subs(actual_sub, simultaneous=True))
        self.assert_zero(recovered_a+2*a)
        self.assertEqual(sp.Poly(recovered_a, u).degree(), 0)

        # Adjoin the ACTUAL invariant a with weight zero. The new expression
        # Y-aX has weight one in these enlarged variables, but is moved by N.
        extended_v = Y-A0*X
        self.assertEqual(self.weighted_top(extended_v, (A0, X, Y, Z, W),
                                           (0, 1, 1, 1, 2))[0], 1)
        actual_v = sp.expand(extended_v.subs({A0: a, X: frame[0], Y: frame[1]},
                                            simultaneous=True))
        self.assert_zero(actual_v-v)
        self.assertEqual(sp.Poly(actual_v, u).degree(), 0)
        self.assertEqual(sp.diff(actual_v, v), 1)
        original_v = sp.expand(extended_v.subs(A0, inverse[0]))
        self.assert_zero(original_v-inverse[2])
        self.assertEqual(self.weighted_top(original_v, original, (1, 1, 1, 2))[0], 4)

        # The same original-weight-four top is successively corrected by
        # original terms of weights two and one. Their E-degrees are 2,1,0;
        # the actual selected partial remains u^2 at every stage.
        stages = [X*phi/2, X*phi/2-X*Z, X*phi/2-X*Z+Y]
        for stage, degree in zip(stages, (2, 1, 0)):
            self.assertEqual(self.weighted_top(stage, original, (1, 1, 1, 2))[0], 4)
            evaluated = sp.expand(stage.subs(actual_sub, simultaneous=True))
            self.assertEqual(sp.Poly(evaluated, u).degree(), degree)
            self.assert_zero(self.act(partial, evaluated, base)-u**2)
        self.assertEqual(self.weighted_top(-X*Z, original, (1, 1, 1, 2))[0], 2)
        self.assertEqual(self.weighted_top(Y, original, (1, 1, 1, 2))[0], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
