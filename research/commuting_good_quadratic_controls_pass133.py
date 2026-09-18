"""Independent exact controls for the commuting-direction theorem133.

The first method checks an actual coordinate family with arbitrary quadratic
P and a polynomial invariant multiplier h(V,K), including both coordinate
inverse orders, the commuting partial, and the quadratic Hessian identity.
The second checks a dense sliced specialization h=1, its explicit translation
coordinates, and an irreducible specialization h=V with fixed points and no
slice. The third checks covariance under an actual constant linear good change
and an affine bad change, producing a commuter with nonzero bad component.

These are finite symbolic families, not verification of Wang's classification,
the universal quadratic-correction theorem, or arbitrary-frame entry. No search
or previous checker internals are imported. Nonfree and already-straightened
examples are not counterexamples to cancellation.
"""

import unittest

import sympy as sp


class CommutingGoodQuadraticControls(unittest.TestCase):
    @staticmethod
    def act(field, value, variables):
        return sp.expand(sum(coefficient*sp.diff(value, variable)
                             for coefficient, variable in zip(field, variables)))

    @classmethod
    def bracket(cls, left, right, variables):
        return sp.Matrix([cls.act(left, value, variables)-cls.act(right, other, variables)
                          for value, other in zip(right, left)])

    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def assert_vector_equal(self, left, right):
        self.assertEqual(len(left), len(right))
        for actual, expected in zip(left, right):
            self.assert_zero(actual-expected)

    def test_actual_polynomial_multiplier_family_and_quadratic_hessian(self):
        V, Y, Z, X = sp.symbols("V Y Z X")
        x, y, z, w = sp.symbols("x y z w")
        lam = sp.symbols("lambda", nonzero=True)
        p20, p11, p02, p10, p01, p00 = sp.symbols("p20 p11 p02 p10 p01 p00")
        h0, h1, h2 = sp.symbols("h0 h1 h2")
        variables, original = (V, Y, Z, X), (x, y, z, w)

        def P(y0, z0):
            return p20*y0**2+p11*y0*z0+p02*z0**2+p10*y0+p01*z0+p00

        K = (V**2+1)*Y-V*Z
        h = h0+h1*V+h2*K
        field = sp.Matrix([0, h*V, h*(V**2+1), K])
        commuter = sp.Matrix([0, 0, 0, 1])
        W = (V-P(Y, Z))/lam
        frame = sp.Matrix([X, Y, Z, W])
        inverse = sp.Matrix([lam*w+P(y, z), y, z, x])
        self.assert_vector_equal(
            inverse.subs(dict(zip(original, frame)), simultaneous=True), variables)
        self.assert_vector_equal(
            frame.subs(dict(zip(variables, inverse)), simultaneous=True), original)
        self.assert_zero(frame.jacobian(variables).det()+1/lam)
        self.assert_zero(lam*W+P(Y, Z)-V)
        self.assert_zero(self.act(field, V, variables))
        self.assert_zero(self.act(field, K, variables))
        self.assert_zero(self.act(field, h, variables))
        self.assert_vector_equal(self.bracket(field, commuter, variables), (0, 0, 0, 0))
        self.assert_vector_equal([self.act(commuter, value, variables) for value in frame],
                                 (1, 0, 0, 0))

        speeds = sp.Matrix([self.act(field, value, variables) for value in frame[:3]])
        self.assert_vector_equal(speeds, (K, h*V, h*(V**2+1)))
        for value in frame[:3]:
            self.assert_zero(self.act(field, self.act(field, value, variables), variables))
        q = self.act(field, self.act(field, W, variables), variables)
        hessian_value = (2*p20*speeds[1]**2+2*p11*speeds[1]*speeds[2]
                         + 2*p02*speeds[2]**2)
        self.assert_zero(lam*q+hessian_value)
        self.assert_zero(self.act(field, q, variables))
        self.assert_zero(self.act(field, lam*W+P(Y, Z), variables))
        # The six coefficients of P are constants for E. This is exactly the
        # fixed-good correction W+P/lambda, with inverse W=V/lambda-P/lambda.
        # A generic quadratic P has degree-two W; degenerate specializations
        # are allowed by the identities and not claimed to retain exact degree.
        self.assert_zero(q.subs({p20: sp.Rational(1, 2), p11: 0, p02: 0},
                                simultaneous=True)+h**2*V**2/lam)

    def test_dense_slice_and_nonconstant_multiplier_without_slice(self):
        V, Y, Z, X = sp.symbols("V Y Z X")
        k, n, s, v0 = sp.symbols("k n s v0")
        variables = (V, Y, Z, X)
        K = (V**2+1)*Y-V*Z
        sliced = sp.Matrix([0, V, V**2+1, K])
        slice_value = Z-V*Y
        invariant_x = X-K*slice_value
        self.assert_zero(self.act(sliced, slice_value, variables)-1)
        self.assert_zero(self.act(sliced, invariant_x, variables))
        # Actual translation coordinates (V,K,X-Ks,s), not merely a local slice.
        coordinates = sp.Matrix([V, K, invariant_x, slice_value])
        inverse = sp.Matrix([v0, k+v0*s, v0*k+(v0**2+1)*s, n+k*s])
        self.assert_vector_equal(
            inverse.subs(dict(zip((v0, k, n, s), coordinates)), simultaneous=True), variables)
        self.assert_vector_equal(
            coordinates.subs(dict(zip(variables, inverse)), simultaneous=True), (v0, k, n, s))
        for value in (V, K, invariant_x):
            self.assert_zero(self.act(sliced, value, variables))

        # K is independent of V by the preceding polynomial coordinate inverse.
        speed_row = sp.Matrix([k, V, V**2+1])
        self.assertEqual(speed_row.jacobian((V, k)).rank(), 2)
        self.assert_zero(sp.Matrix.hstack(speed_row, speed_row.diff(V),
                                         speed_row.diff(k)).det()-V**2+1)
        self.assert_zero(speed_row[2]-V*speed_row[1]-1)

        # h=V is a nonconstant invariant multiplier on the Y,Z motion, while
        # EX remains K. It is not a global multiple of the entire derivation.
        nonfree = sp.Matrix([0, V**2, V*(V**2+1), K])
        self.assert_zero(self.act(nonfree, V, variables))
        self.assert_zero(self.act(nonfree, K, variables))
        self.assert_zero(self.act(nonfree, slice_value, variables)-V)
        self.assertEqual(sp.gcd(sp.gcd(V**2, V*(V**2+1)), K), 1)
        for value in (X, Y, Z):
            self.assert_zero(self.act(nonfree, self.act(nonfree, value, variables), variables))
        W = V-Y**2/2
        q = self.act(nonfree, self.act(nonfree, W, variables), variables)
        self.assert_zero(q+V**4)
        self.assert_zero(self.act(nonfree, q, variables))
        self.assert_zero(self.act(nonfree, W+Y**2/2, variables))
        self.assert_vector_equal(self.bracket(nonfree, sp.Matrix([0, 0, 0, 1]), variables),
                                 (0, 0, 0, 0))
        for coefficient in nonfree:
            self.assert_zero(coefficient.subs({V: 0, Y: 0}, simultaneous=True))
        self.assertEqual(sp.Integer(1).subs({V: 0, Y: 0}), 1)
        # Evaluation at the displayed fixed points kills every E(f), but not
        # 1. Thus no slice exists in this actual polynomial ring. This tests
        # why a slice is not an assumption of the commuting-direction theorem.
        nonfree_row = sp.Matrix([k, V**2, V*(V**2+1)])
        self.assert_zero(sp.Matrix.hstack(nonfree_row, nonfree_row.diff(V),
                                         nonfree_row.diff(k)).det()-V**2*(V**2-1))

    def test_constant_ambient_direction_covariance(self):
        V, Y, Z, X, W = sp.symbols("V Y Z X W")
        A, B, C, D = sp.symbols("A B C D")
        kappa, lam = sp.symbols("kappa lambda", nonzero=True)
        p20, p11, p02, p10, p01, p00 = sp.symbols("p20 p11 p02 p10 p01 p00")

        def P(y0, z0):
            return p20*y0**2+p11*y0*z0+p02*z0**2+p10*y0+p01*z0+p00

        # Constant linear good reframe and affine bad reframe, with both
        # inverse orders independently checked in the original four variables.
        changed = sp.Matrix([X+Y, Y+2*Z, Z, W+kappa*X])
        reverse = sp.Matrix([A-B+2*C, B-2*C, C, D-kappa*(A-B+2*C)])
        self.assert_vector_equal(
            reverse.subs(dict(zip((A, B, C, D), changed)), simultaneous=True), (X, Y, Z, W))
        self.assert_vector_equal(
            changed.subs(dict(zip((X, Y, Z, W), reverse)), simultaneous=True), (A, B, C, D))
        new_commuter = sp.Matrix([1, 0, 0, kappa])
        self.assert_vector_equal(changed.jacobian((X, Y, Z, W))[:, 0], new_commuter)

        variables = (V, Y, Z, X)
        K = (V**2+1)*Y-V*Z
        field = sp.Matrix([0, V, V**2+1, K])
        original_W = (V-P(Y, Z))/lam
        actual_changed = changed.subs(W, original_W)
        D0 = sp.Matrix([0, 0, 0, 1])
        self.assert_vector_equal([self.act(D0, value, variables) for value in actual_changed],
                                 new_commuter)
        for value in actual_changed:
            self.assert_zero(self.act(D0, self.act(field, value, variables), variables)
                             - self.act(field, self.act(D0, value, variables), variables))
        correction = P(B-2*C, C)/lam-kappa*(A-B+2*C)
        invariant = D+correction
        evaluated = invariant.subs(dict(zip((A, B, C, D), actual_changed)), simultaneous=True)
        self.assert_zero(evaluated-V/lam)
        self.assert_zero(self.act(field, evaluated, variables))
        self.assertEqual(sp.Poly(correction, A, B, C).total_degree(), 2)
        # This makes the constant commuter's bad component nonzero while the
        # required added polynomial remains quadratic in the three NEW goods.
        # It does not test the impossible pure-bad commuting case in the proof.


if __name__ == "__main__":
    unittest.main(verbosity=2)
