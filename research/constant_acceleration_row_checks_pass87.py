"""One actual-frame counterexample, not a general linearization verifier."""

import unittest

import sympy as S


class ConstantAccelerationRowChecks(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(S.expand(expression), 0)

    def test_actual_row_reynolds_and_completion_obstructions(self):
        u, a, b, c = canonical = S.symbols("u a b c")
        x, y, z, w = original = S.symbols("x y z w")
        forward = S.Matrix([u, (1 + u**2)*a + u*b, u*a + b, c + u**2])
        inverse = S.Matrix([x, y - x*z, (1 + x**2)*z - x*y, w - x**2])
        to_original = dict(zip(canonical, inverse))
        to_canonical = dict(zip(original, forward))
        for actual, target in zip(forward, original):
            self.zero(actual.subs(to_original, simultaneous=True) - target)
        for actual, target in zip(inverse, canonical):
            self.zero(actual.subs(to_canonical, simultaneous=True) - target)
        self.zero(forward.jacobian(canonical).det() - 1)
        self.zero(inverse.jacobian(original).det() - 1)
        for actual, degree in zip(forward, [1, 2, 1, 2]):
            self.assertEqual(S.Poly(actual, u).degree(), degree)
        E = forward.diff(u).subs(to_original, simultaneous=True)
        self.zero(E[0] - 1)
        self.zero(sum(E[i]*S.diff(E[3], original[i]) for i in range(4)) - 2)

        # The fiber has original coordinates x,y,z and canonical u,a,b.
        coordinates = S.Matrix([x, y, z])
        iota = forward[:3, 0].subs(u, -u).subs(to_original, simultaneous=True)
        substitution = dict(zip(coordinates, iota))
        for actual, target in zip(iota, coordinates):
            self.zero(actual.subs(substitution, simultaneous=True) - target)
        A, B = inverse[1], inverse[2]
        Q = S.Matrix([1, B, A])
        P = S.Matrix([0, (1 + x**2)*A, B])
        for actual in Q:
            self.zero(actual.subs(substitution, simultaneous=True) - actual)
        for actual, target in zip(iota, coordinates - 2*x*Q):
            self.zero(actual - target)
        for actual, target in zip(coordinates, P + x*Q):
            self.zero(actual - target)

        # Check the fixed-divisor differential congruences in this control.
        JQ = Q.jacobian(coordinates)
        du = S.Matrix([[1, 0, 0]])
        Jiota = iota.jacobian(coordinates)
        for actual in Jiota - (S.eye(3) - 2*Q*du - 2*x*JQ):
            self.zero(actual)
        self.zero(Jiota.det() + 1)
        self.zero((du*Q)[0] - 1)
        for actual in JQ*Q:
            self.zero(actual.subs(x, 0))
        projector = Q*du
        for actual in projector**2 - projector:
            self.zero(actual.subs(x, 0))
        VQa = sum(Q[i]*S.diff(A, coordinates[i]) for i in range(3))
        self.zero(VQa + 2*x*A)
        self.assertNotEqual(S.expand(VQa), 0)

        # Free-module completion is not an ambient polynomial automorphism.
        M = S.Matrix([[1, 0, 0], [-B, 1, 0], [-A, 0, 1]])
        self.zero(M.det() - 1)
        for actual, target in zip(M*Q, [1, 0, 0]):
            self.zero(actual - target)
        completion = M*coordinates
        L = S.diag(-1, 1, 1)
        for actual in Jiota.subs({x: 0, y: 0, z: 0}) - L:
            self.zero(actual)
        reynolds = (coordinates + L*iota)/2
        for actual, target in zip(reynolds, completion):
            self.zero(actual - target)
        for actual, target in zip(reynolds.subs(substitution, simultaneous=True), L*reynolds):
            self.zero(actual - target)
        determinant = S.factor(reynolds.jacobian(coordinates).det())
        self.zero(determinant - (1 + x**2))
        self.assertNotEqual(determinant, S.Integer(1))

        # Exact degree-band failure, not a sample-based degree assertion.
        degrees = set()
        for polynomial in iota - L*coordinates:
            for monomial, coefficient in S.Poly(polynomial, x, y, z).terms():
                if coefficient:
                    degrees.add(sum(monomial))
        self.assertEqual(degrees, {2, 3, 4})

        # At u=i, different a values have the same Reynolds image.
        canonical_reynolds = reynolds.subs(to_canonical, simultaneous=True)
        first = canonical_reynolds.subs({u: S.I, a: 0, b: 0})
        second = canonical_reynolds.subs({u: S.I, a: 1, b: 0})
        for actual, target in zip(first, second):
            self.zero(actual - target)
        self.assertNotEqual(
            forward[2].subs({u: S.I, a: 0, b: 0}),
            forward[2].subs({u: S.I, a: 1, b: 0}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
