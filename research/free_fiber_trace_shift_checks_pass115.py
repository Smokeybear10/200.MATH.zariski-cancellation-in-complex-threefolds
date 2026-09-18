"""Two exact algebraic controls for the reduced free-fiber argument.

The first checks a quadratic multiplication matrix, specialization trace,
and the constant-acceleration invariant. The second checks the idempotent
coefficient shift and centered conic without imposing geometric relations.
These identities do not prove finite flatness, the degree bound, analytic
prime support, an actual-frame realization, or global recognition. No
solver or retained checker is imported.
"""

import unittest

import sympy as sp


class FreeFiberTraceShiftChecks(unittest.TestCase):
    def test_quadratic_trace_and_opposite_slopes(self):
        p, U, eta, r, T = sp.symbols("p U eta r T")
        square = 2 * p * U - eta
        multiplication = sp.Matrix([[0, square], [1, 0]])
        self.assertEqual(multiplication.trace(), 0)
        self.assertEqual(multiplication**2, square * sp.eye(2))
        self.assertEqual(sp.expand(multiplication.charpoly(T).as_expr()
                                   - (T**2 - square)), 0)

        def N(value):
            return sp.expand(r * sp.diff(value, U) + p * sp.diff(value, r))

        self.assertEqual(N(2 * p * U - r**2), 0)
        self.assertEqual(N(U), r)
        self.assertEqual(N(N(U)), p)
        self.assertEqual(N(N(N(U))), 0)

        delta = sp.symbols("delta", nonzero=True)
        closed_matrix = multiplication.subs({p: 0, eta: -delta**2})
        eigenvectors = sp.Matrix([[delta, -delta], [1, 1]])
        opposite = sp.diag(delta, -delta)
        same = sp.diag(delta, delta)
        self.assertEqual(eigenvectors.det(), 2 * delta)
        self.assertEqual(closed_matrix * eigenvectors, eigenvectors * opposite)
        self.assertEqual(opposite.trace(), 0)
        self.assertEqual(same**2, delta**2 * sp.eye(2))
        self.assertEqual(same.trace(), 2 * delta)
        self.assertNotEqual(same.trace(), closed_matrix.trace())
        # Equal slopes satisfy the square equation but fail the required trace.
        self.assertEqual((opposite**2 - same**2), sp.zeros(2))

    def test_idempotent_shift_and_centered_conic(self):
        a, b, eps, h, B2, G, H = sp.symbols("a b eps h B2 G H")
        r = a * G + b * H
        P = a * h + b * B2
        NG, NH = eps * b * r + h, -eps * a * r + B2

        def N(value):
            return sp.expand(NG * sp.diff(value, G) + NH * sp.diff(value, H))

        Q = eps * r**2 - 2 * B2 * G + 2 * h * H
        self.assertEqual(N(r), P)
        self.assertEqual(N(Q), 0)
        half = sp.Rational(1, 2)
        Gp, rp = G - half, r - a * half
        hp, Bp = h + eps * a * b * half, B2 - eps * a**2 * half
        Qp = eps * rp**2 - 2 * Bp * Gp + 2 * hp * H
        self.assertEqual(sp.expand(rp - a * Gp - b * H), 0)
        self.assertEqual(sp.expand(N(Gp) - eps * b * rp - hp), 0)
        self.assertEqual(sp.expand(NH + eps * a * rp - Bp), 0)
        self.assertEqual(sp.expand(P - a * hp - b * Bp), 0)
        self.assertEqual(sp.expand(Qp - Q - B2 + eps * a**2 / 4), 0)
        self.assertEqual(N(Qp), 0)

        original_remainder = (eps * a**2 * (G**2 - G)
                              + 2 * eps * a * b * G * H
                              + eps * b**2 * H**2 + 2 * h * H)
        centered_remainder = (eps * a**2 * (Gp**2 - sp.Rational(1, 4))
                              + 2 * eps * a * b * Gp * H
                              + eps * b**2 * H**2 + 2 * hp * H)
        self.assertEqual(sp.expand(Q + 2 * Bp * G - original_remainder), 0)
        self.assertEqual(sp.expand(Qp - eps * a**2 / 4
                                   + 2 * Bp * Gp - centered_remainder), 0)
        self.assertEqual(sp.expand(Gp**2 - sp.Rational(1, 4) - G * (G - 1)), 0)
        self.assertEqual([Gp.subs(G, value) for value in (0, 1)], [-half, half])

        # A nonzero translation speed on each summand is a unit in C[G]/G(G-1).
        speed0, speed1 = sp.symbols("speed0 speed1", nonzero=True)
        speed = (1 - G) * speed0 + G * speed1
        inverse = (1 - G) / speed0 + G / speed1
        self.assertEqual(sp.rem(sp.expand(speed * inverse - 1), G * (G - 1), G), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
