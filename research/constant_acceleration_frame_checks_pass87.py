"""An actual three-good frame with constant acceleration and regular nilpotent J."""

import unittest

import sympy as S


def apply(vector, polynomial, variables):
    return S.expand(sum(a * S.diff(polynomial, x)
                        for a, x in zip(vector, variables)))


def bracket(left, right, variables):
    return S.Matrix([apply(left, f, variables) - apply(right, g, variables)
                     for f, g in zip(right, left)])


class ConstantAccelerationFrameChecks(unittest.TestCase):
    def zero(self, expression):
        entries = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(S.expand(entry), 0)

    def test_actual_three_good_frame_and_all_adjoint_columns(self):
        u, r, t, c = canonical = S.symbols("u r t c")
        x1, x2, x3, z = original = S.symbols("x1 x2 x3 z")
        forward = S.Matrix([u, t + u * r, c + u * t, r + u**2])
        r0 = z - x1**2
        t0 = x2 - x1 * r0
        inverse = S.Matrix([x1, r0, t0, x3 - x1 * t0])
        to_original = dict(zip(canonical, inverse))
        to_canonical = dict(zip(original, forward))
        self.zero(forward.subs(to_original, simultaneous=True) - S.Matrix(original))
        self.zero(inverse.subs(to_canonical, simultaneous=True) - S.Matrix(canonical))
        self.zero(forward.jacobian(canonical).det() - 1)
        self.zero(inverse.jacobian(original).det() - 1)

        P = S.Matrix([1, r0, t0, 2 * x1])
        self.zero(forward.diff(u).subs(to_original, simultaneous=True) - P)
        self.zero(S.Matrix([apply(P, f, original) for f in inverse])
                  - S.Matrix([1, 0, 0, 0]))
        e4 = S.eye(4)[:, 3]
        J = P.jacobian(original)
        self.zero(J * P - 2 * e4)
        self.zero(J.applyfunc(lambda f: apply(P, f, original)) + J**2)
        self.zero(J**4)
        self.zero(J**3 - 2 * S.eye(4)[:, 2] * S.eye(4)[:, 0].T)
        self.zero(J**3 * e4)
        self.zero(J**2 * e4 - S.eye(4)[:, 2])
        self.assertEqual([J.rank(), (J**2).rank(), (J**3).rank()], [3, 2, 1])
        self.assertEqual(P[:3, :].jacobian(original).rank(), 2)

        tau = S.symbols("tau")
        flow = S.Matrix(original) + tau * P + tau**2 * e4
        self.zero(flow.jacobian(original) - (S.eye(4) + tau * J))
        self.zero(flow.jacobian(original).det() - 1)
        backward = S.Matrix(original) - tau * P + tau**2 * e4
        self.zero(backward.subs(dict(zip(original, flow)), simultaneous=True)
                  - S.Matrix(original))
        self.zero(flow.subs(dict(zip(original, backward)), simultaneous=True)
                  - S.Matrix(original))

        heights = []
        for i in range(4):
            field = S.eye(4)[:, i]
            first_zero = None
            for j in range(1, 5):
                field = bracket(P, field, original)
                self.zero(field - (-1)**j * S.factorial(j) * J**j * S.eye(4)[:, i])
                if first_zero is None and all(S.expand(v) == 0 for v in field):
                    first_zero = j
            heights.append(first_zero)
        self.assertEqual(heights, [4, 2, 1, 3])
        self.assertEqual([S.Poly(f, u).degree() for f in forward], [1, 1, 1, 2])

        # The original bad partial has a genuine horizontal highest term.
        T_canonical = inverse.diff(z).subs(to_canonical, simultaneous=True)
        self.zero(T_canonical - S.Matrix([0, 1, -u, u**2]))
        highest = T_canonical.diff(u, 2)
        self.zero(highest - S.Matrix([0, 0, 0, 2]))
        self.zero(apply(highest, u, canonical))
        self.zero(apply(highest, r, canonical))
        self.zero(apply(highest, c, canonical) - 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
