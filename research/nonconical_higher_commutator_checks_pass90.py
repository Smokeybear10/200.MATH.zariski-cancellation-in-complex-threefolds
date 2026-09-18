"""One actual inverse-frame control; no universal theorem is certified."""

import unittest

import sympy as S


class NonconicalHigherCommutatorChecks(unittest.TestCase):
    def test_actual_frame_and_failed_commutator_lnd_inferences(self):
        u, r, ell, t = S.symbols("u r ell t")
        canonical = S.Matrix([u, r, ell, t])
        x1, x2, x3, z = S.symbols("x1 x2 x3 z")
        original = S.Matrix([x1, x2, x3, z])
        forward = S.Matrix([
            u, t + u * ell, r * (t + u * ell) - ell, r + u**2,
        ])
        inverse_r = z - x1**2
        inverse_ell = inverse_r * x2 - x3
        inverse = S.Matrix([
            x1, inverse_r, inverse_ell, x2 - x1 * inverse_ell,
        ])
        to_original = dict(zip(canonical, inverse))
        to_canonical = dict(zip(original, forward))
        zero = S.zeros(4, 1)

        def expand(value):
            return value.applyfunc(S.expand)

        def action(field, polynomial):
            return S.expand(sum(
                field[i] * S.diff(polynomial, canonical[i])
                for i in range(4)
            ))

        def bracket(left, right):
            return expand(
                right.jacobian(canonical) * left
                - left.jacobian(canonical) * right
            )

        self.assertEqual(
            expand(inverse.subs(to_canonical, simultaneous=True) - canonical),
            zero,
        )
        self.assertEqual(
            expand(forward.subs(to_original, simultaneous=True) - original),
            zero,
        )
        jacobian = forward.jacobian(canonical)
        self.assertEqual(S.expand(jacobian.det()), 1)
        self.assertEqual(S.expand(inverse.jacobian(original).det()), 1)

        e = S.Matrix([1, 0, 0, 0])
        last_partial = S.Matrix([
            0, 1, t + u * ell, -u * (t + u * ell),
        ])
        self.assertEqual(
            expand(jacobian * last_partial), S.Matrix([0, 0, 0, 1]),
        )
        velocity = expand(jacobian * e)
        self.assertEqual(velocity, S.Matrix([1, ell, r * ell, 2 * u]))
        self.assertEqual(expand(velocity.diff(u)), S.Matrix([0, 0, 0, 2]))
        b = S.Matrix([1, ell, r * ell])
        self.assertEqual(
            S.expand(S.Matrix.hstack(b, b.diff(r), b.diff(ell)).det()),
            -ell,
        )

        qfield = bracket(e, last_partial)
        highest = bracket(e, qfield)
        rfield = bracket(last_partial, qfield)
        self.assertEqual(qfield, S.Matrix([0, 0, ell, -t - 2 * u * ell]))
        self.assertEqual(highest, S.Matrix([0, 0, 0, -2 * ell]))
        self.assertEqual(bracket(e, highest), zero)
        self.assertEqual(bracket(last_partial, highest), 2 * qfield)
        self.assertEqual(bracket(qfield, highest), 2 * highest)
        self.assertEqual(bracket(e, rfield), 2 * qfield)
        self.assertEqual(bracket(last_partial, rfield), zero)
        self.assertEqual(bracket(rfield, highest), 4 * qfield)
        self.assertEqual(
            expand(jacobian * rfield), S.Matrix([0, 0, -2 * forward[1], 0]),
        )
        self.assertEqual(action(rfield, ell), 2 * (t + u * ell))
        self.assertEqual(S.diff(action(rfield, ell), u), 2 * ell)
        self.assertEqual(
            S.expand(S.Matrix.hstack(e, last_partial, qfield, highest).det()),
            -2 * ell**2,
        )
        for f in [u, r, ell, *list(b)]:
            self.assertEqual(action(highest, f), 0)
        for f in forward:
            self.assertEqual(action(highest, action(highest, f)), 0)
        self.assertEqual(highest.subs(ell, 0), zero)

        q_iterate, th_iterate = ell, ell
        th = bracket(last_partial, highest)
        for n in range(1, 7):
            with self.subTest(iterate=n):
                q_iterate = action(qfield, q_iterate)
                th_iterate = action(th, th_iterate)
                self.assertEqual(q_iterate, ell)
                self.assertEqual(th_iterate, 2**n * ell)

        original_velocity = expand(
            velocity.subs(to_original, simultaneous=True),
        )
        j = original_velocity.jacobian(original)
        self.assertEqual([expand(j**n).rank() for n in (1, 2, 3)], [3, 2, 1])
        self.assertEqual(expand(j**4), S.zeros(4))
        self.assertEqual(
            expand(j * original_velocity), S.Matrix([0, 0, 0, 2]),
        )
        original_highest = expand(
            (jacobian * highest).subs(to_original, simultaneous=True),
        )
        self.assertEqual(
            expand(original_highest - 2 * j**2 * S.Matrix([0, 0, 0, 1])),
            zero,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
