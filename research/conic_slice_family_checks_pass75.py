"""Exact finite controls for the coprime conic-velocity family.

The tests use independent polynomial coordinates (a,x,y,z), with
w=a-x*z+y**2, to keep the complete inverse identities small.
They do not classify all nice actions or prove cancellation.
Only unittest and SymPy are imported, not research solvers/checkers.
"""

import unittest

import sympy as sp


class ConicSliceFamilyChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    @staticmethod
    def act(field, expression, frame):
        return sp.expand(sum(value * sp.diff(expression, variable)
                             for variable, value in zip(frame, field)))

    @staticmethod
    def bezout(u, v, a):
        # SymPy 1.13.3 gcdex can divide by zero when its second input is
        # zero. Handle both constant-axis cases by their exact identities.
        if v == 0:
            if u != 0 and sp.degree(u, a) == 0:
                return sp.cancel(1/u), sp.Integer(0)
            raise ValueError("The two velocity parameters must be coprime")
        if u == 0:
            if sp.degree(v, a) == 0:
                return sp.Integer(0), sp.cancel(1/v)
            raise ValueError("The two velocity parameters must be coprime")
        r, s, gcd = sp.gcdex(u, v, a)
        if gcd != 1:
            raise ValueError("The two velocity parameters must be coprime")
        return sp.expand(r), sp.expand(s)

    @staticmethod
    def matrices(u, v, r, s):
        forward = sp.Matrix([
            [v**2, -2*u*v, u**2],
            [v*r, v*s-u*r, -u*s],
            [r**2, 2*r*s, s**2],
        ])
        inverse = sp.Matrix([
            [s**2, 2*s*u, u**2],
            [-r*s, s*v-r*u, u*v],
            [r**2, -2*r*v, v**2],
        ])
        return forward, inverse

    def test_actual_inverse_pairs_derived_fields_and_original_flow_degree(self):
        a, x, y, z, U, V, S = sp.symbols("a x y z U V S")
        parameters = [(1, a), (a, a**2+1), (a**2, a**2+1),
                      (a**2, a**4+1), (0, 2), (3, 0), (2, 3)]
        for raw_u, raw_v in parameters:
            u, v = map(sp.sympify, (raw_u, raw_v))
            with self.subTest(u=u, v=v):
                r, s = self.bezout(u, v, a)
                self.assert_zero(r*u+s*v-1)
                forward, inverse = self.matrices(u, v, r, s)
                self.assert_zero(forward*inverse-sp.eye(3))
                self.assert_zero(inverse*forward-sp.eye(3))
                target = forward*sp.Matrix([x, y, z])
                original = inverse*sp.Matrix([U, V, S])
                # Both determinant identities also check the fourth original
                # coordinate w and the recovery of a=w+x*z-y**2.
                self.assert_zero(target[0]*target[2]-target[1]**2-(x*z-y**2))
                self.assert_zero(original[0]*original[2]-original[1]**2-(U*S-V**2))
                w_inverse = a-U*S+V**2
                self.assert_zero(w_inverse+original[0]*original[2]-original[1]**2-a)
                self.assert_zero((a-target[0]*target[2]+target[1]**2)-(a-x*z+y**2))

                p = sp.Matrix([u**2, u*v, v**2])
                q = p.diff(a)  # Original partial_w is partial_a here.
                W = sp.expand(v*sp.diff(u, a)-u*sp.diff(v, a))
                B = sp.expand(2*(r*sp.diff(u, a)+s*sp.diff(v, a)))
                self.assert_zero(forward*p-sp.Matrix([0, 0, 1]))
                self.assert_zero(forward*q-sp.Matrix([0, W, B]))
                k = a**2+a
                changed_forward, _ = self.matrices(u, v, r+k*v, s-k*u)
                change = sp.Matrix([[1, 0, 0], [k, 1, 0], [k**2, 2*k, 1]])
                self.assert_zero(changed_forward-change*forward)
                changed_B = 2*((r+k*v)*sp.diff(u, a)+(s-k*u)*sp.diff(v, a))
                self.assert_zero(changed_B-B-2*k*W)
                if W != 0:
                    c = sp.symbols("c0:4")
                    ell = sp.Matrix([[-v**2, 2*u*v, -u**2, 0]])
                    equations = sp.Poly((ell*sp.Matrix(c))[0], a).coeffs()
                    coefficient_matrix, rhs = sp.linear_eq_to_matrix(equations, c)
                    self.assert_zero(rhs)
                    self.assertEqual(coefficient_matrix.nullspace(),
                                     [sp.Matrix([0, 0, 0, 1])])
                frame = [a, U, V, S]
                E = sp.Matrix([0, 0, 0, 1])
                Q = sp.Matrix([0, 0, W, B])
                actual_original = sp.Matrix([*original, w_inverse])
                self.assert_zero(actual_original.applyfunc(
                    lambda f: self.act(E, self.act(E, f, frame), frame)))
                acceleration = actual_original.applyfunc(
                    lambda f: self.act(Q, self.act(Q, f, frame), frame))
                self.assert_zero(acceleration-sp.Matrix([0, 0, 0, 2*W**2]))
                self.assert_zero(acceleration.applyfunc(lambda f: self.act(Q, f, frame)))

    def test_slice_criteria_with_ramification_and_constant_boundaries(self):
        a, U, V, S = sp.symbols("a U V S")
        # Expected: Q globally sliced, and an E-slice fixed by Q exists.
        cases = [(1, a, True, True), (a, a**2+1, True, False),
                 (a**2, a**2+1, False, True),
                 (a**2, a**4+1, False, False),
                 (0, 2, False, True), (3, 0, False, True),
                 (2, 3, False, True)]
        frame = [a, U, V, S]
        for raw_u, raw_v, sliced, common in cases:
            u, v = map(sp.sympify, (raw_u, raw_v))
            with self.subTest(u=u, v=v):
                r, s = self.bezout(u, v, a)
                up, vp = sp.diff(u, a), sp.diff(v, a)
                W = sp.expand(v*up-u*vp)
                B = sp.expand(2*(r*up+s*vp))
                Q = sp.Matrix([0, 0, W, B])
                if W == 0:
                    self.assert_zero(Q)
                    self.assertEqual(sp.degree(u, a) <= 0, True)
                    self.assertEqual(sp.degree(v, a) <= 0, True)
                    self.assertFalse(sliced)
                    self.assertTrue(common)
                    continue
                d = sp.Poly(sp.gcd(W, B), a).monic().as_expr()
                derivative_gcd = sp.Poly(sp.gcd(up, vp), a).monic().as_expr()
                self.assert_zero(d-derivative_gcd)
                self.assertEqual(d == 1, sliced)
                quotient, remainder = sp.div(B, W, a)
                self.assertEqual(remainder == 0, common)
                alpha, gamma = sp.symbols("alpha gamma")
                equations = sp.Poly(alpha*u+gamma*v-1, a).coeffs()
                solutions = sp.linsolve(equations, (alpha, gamma))
                self.assertEqual(solutions != sp.EmptySet, common)
                if common:
                    F = S-quotient*V
                    self.assert_zero(self.act(Q, F, frame))
                    self.assertEqual(sp.diff(F, S), 1)
                    ac, gc = next(iter(solutions))
                    self.assert_zero((ac*u+gc*v)**2-1)
                    self.assert_zero(sp.diff((ac*u+gc*v)**2, a))
                if sliced:
                    b1, b2 = self.bezout(W, B, a)
                    self.assert_zero(b1*W+b2*B-1)
                    self.assert_zero(self.act(Q, b1*V+b2*S, frame)-1)
                # The primitive Q has a slice even in the ramified cases.
                q1, q2 = sp.cancel(W/d), sp.cancel(B/d)
                b1, b2 = self.bezout(q1, q2, a)
                self.assert_zero(b1*q1+b2*q2-1)
                self.assert_zero(self.act(sp.Matrix([0, 0, q1, q2]),
                                          b1*V+b2*S, frame)-1)

        # Explicit zero of Q proves the nonslice assertion without a
        # bounded-degree search for a possible slice.
        u, v = a**2, a**4+1
        r, s = self.bezout(u, v, a)
        W, B = sp.expand(v*sp.diff(u, a)-u*sp.diff(v, a)), \
            sp.expand(2*(r*sp.diff(u, a)+s*sp.diff(v, a)))
        self.assert_zero(sp.Matrix([W, B]).subs(a, 0))

    def test_arbitrary_slice_adjustment_and_exact_high_flow_controls(self):
        a, U, V, S, F = sp.symbols("a U V S F")
        frame = [a, U, V, S]
        u, v, r, s = a, a**2+1, -a, 1
        _, inverse = self.matrices(u, v, r, s)
        original = sp.Matrix([*(inverse*sp.Matrix([U, V, S])), a-U*S+V**2])
        E = sp.Matrix([0, 0, 0, 1])
        W, B = 1-a**2, 2*a
        Q = sp.Matrix([0, 0, W, B])
        for degree in (3, 5):
            with self.subTest(degree=degree):
                h = V**degree+U*V
                supplied = S+h
                coefficient = self.act(Q, supplied, frame)
                adjusted = Q-coefficient*E
                primitive = sp.Matrix([0, 0, 1, -sp.diff(h, V)])
                self.assert_zero(adjusted-W*primitive)
                self.assert_zero(self.act(adjusted, supplied, frame))
                self.assert_zero(self.act(primitive, supplied, frame))
                self.assertEqual(self.act(primitive, V, frame), 1)
                self.assert_zero((F-h+h)-F)
                self.assert_zero((supplied-h)-S)
                moved = original
                for _ in range(degree):
                    moved = moved.applyfunc(lambda f: self.act(adjusted, f, frame))
                self.assert_zero(moved[0]+W**degree*u**2*sp.factorial(degree))
                self.assertNotEqual(sp.expand(moved[0]), 0)
                self.assert_zero(moved.applyfunc(lambda f: self.act(adjusted, f, frame)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
