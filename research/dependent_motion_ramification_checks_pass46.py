"""Four finite controls for the dependent moving-parameter reduction.

The first two methods are formal matrix or curve controls, not actions.
The actual inverse example has heights (1, 4, 4, 4), explicitly outside
the target (1, 1, 2, 2) frame. No other solver or checker is imported.
"""

import unittest

import sympy as sp


def clean(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda entry: sp.cancel(sp.expand(entry)))
    return sp.cancel(sp.expand(value))


def act(field, value, variables):
    return clean(sum(coefficient * sp.diff(value, variable)
                     for coefficient, variable in zip(field, variables)))


def bracket(left, right, variables):
    return sp.Matrix([act(left, entry, variables)
                      - act(right, other, variables)
                      for entry, other in zip(right, left)])


def actual_control():
    s, u, v, z = sp.symbols("s u v z")
    a, S, V, U = sp.symbols("a S V U")
    old, new = (s, u, v, z), (a, S, V, U)
    forward = sp.Matrix([z + u*s**3/6 + v**2*s**2/2,
                         s, v + s*z, u - 6*v*z - 3*s*z**2])
    inverse_z = a - U*S**3/6 - V**2*S**2/2
    inverse = sp.Matrix([S, U + 6*V*inverse_z - 3*S*inverse_z**2,
                         V - S*inverse_z, inverse_z])
    return old, new, forward, inverse


class DependentMotionRamificationChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_full_auxiliary_factor_comparison_determines_next_speed(self):
        # Formal rank-two factor comparison only. These matrices are not
        # asserted to be powers of the companion of an actual action.
        r, psi, A, B1, eta, qp, t = sp.symbols(
            "r psi A B1 eta qp t", nonzero=True)
        d_tau = sp.Matrix([[0, 0, 1, 0]])
        d_u = sp.Matrix([[0, 0, 0, 1]])
        for m in (3, 4):
            alpha = sp.Rational(m - 1, 2)
            C1 = sp.Matrix([1, 0, 0, 0, (m - 1)*r])
            C2 = sp.Matrix([0, 1, 0, 0, psi])
            image = C1.row_join(C2)
            rows = d_tau.row_join(sp.Matrix([[-alpha*A]])).col_join(
                d_u.row_join(sp.Matrix([[-alpha*B1]])))
            N = image*rows/sp.factorial(m - 1)
            self.assertEqual(N.rank(), 2)
            self.assertEqual(N[:4, :4].rank(), 2)
            self.assertZero(N[:4, 4]
                            + alpha*(A*C1[:4, :] + B1*C2[:4, :])
                            / sp.factorial(m - 1))
            # M(C1)=0 and M(C2)=eta*C1 are independently explicit here.
            M = eta*C1*sp.Matrix([[0, 1, 0, 0, 0]])
            self.assertZero(M*C1)
            self.assertZero(M*C2 - eta*C1)
            target = C1*(qp*d_u).row_join(sp.Matrix([[-m*t/2]]))
            target /= sp.factorial(m)
            residual = clean(M*N - target)
            for entry in residual[:, :4]:
                self.assertZero(sp.diff(entry, B1))
            base_eta = sp.solve(residual[0, 3], eta)[0]
            self.assertZero(base_eta - qp/m)
            auxiliary = clean(residual[0, 4].subs(eta, base_eta))
            recovered = sp.solve(auxiliary, B1)[0]
            self.assertZero(recovered - m*t/((m - 1)*qp))
            self.assertZero(residual.subs(
                {eta: base_eta, B1: recovered}, simultaneous=True))

    def test_full_curve_derivative_gcd_keeps_repeated_obstruction(self):
        # Necessary curve data only: no original action is claimed.
        u = sp.symbols("u")
        Q, K3, K4 = u**3, sp.Integer(1), u**5
        qp = sp.diff(Q, u)
        for m in (3, 4):
            A3 = clean(m*Q*sp.diff(K3, u)
                       - (m - 1)*qp*K3)
            A4 = clean(m*Q*sp.diff(K4, u)
                       - (m - 1)*qp*K4)
            delta = sp.Poly(sp.gcd(A3, A4), u).monic().as_expr()
            a0, b0 = clean(-A4/delta), clean(A3/delta)
            R = clean(a0*K3 + b0*K4)
            e = sp.Poly(sp.gcd(Q, R), u).monic().as_expr()
            R1 = clean(R/e)
            self.assertZero(R1 + 5*m*u**2)
            self.assertZero(sp.rem(qp, R1, u))
            beta = sp.Rational(m*(m - 1), 2)
            # Old trace passes with actual d/du speed one and H1 one.
            t = clean(qp/(beta*R1))
            self.assertFalse(t.free_symbols)
            self.assertZero(qp - beta*R1*t)
            # Adding the good component K2=u destroys the common
            # ramification and reveals a genuine order-two pole.
            good_derivative = sp.Integer(1)
            G0 = sp.gcd(qp, sp.gcd(good_derivative, sp.diff(K4, u)))
            self.assertEqual(G0, 1)
            self.assertNotEqual(sp.rem(G0, R1, u), 0)
            pole = clean(good_derivative*t/qp)
            self.assertEqual(sp.degree(sp.denom(pole), u), 2)
            self.assertNotEqual(clean(u**2*pole).subs(u, 0), 0)
            # With that good component constant, the refined test passes.
            ramified_gcd = sp.Poly(sp.gcd(qp, sp.diff(K4, u)),
                                    u).monic().as_expr()
            self.assertEqual(ramified_gcd, u**2)
            self.assertZero(sp.rem(ramified_gcd, R1, u))
            # Explicit full-family Bezout certificate used to descend
            # divisibility into the actual polynomial ring.
            reduced_qp = clean(qp/ramified_gcd)
            reduced_k4 = clean(sp.diff(K4, u)/ramified_gcd)
            left, right, gcd_value = sp.gcdex(reduced_qp, reduced_k4, u)
            self.assertZero(gcd_value - 1)
            self.assertZero(left*qp + right*sp.diff(K4, u)
                            - ramified_gcd)

    def test_actual_inverse_highest_vector_and_exact_column_heights(self):
        old, new, forward, inverse = actual_control()
        s, u, v, z = old
        self.assertZero(inverse.subs(dict(zip(new, forward)),
                                     simultaneous=True) - sp.Matrix(old))
        self.assertZero(forward.subs(dict(zip(old, inverse)),
                                     simultaneous=True) - sp.Matrix(new))
        E, D = sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 0, 1, 0])
        C = sp.Matrix([0, 6*v, -s, 1])
        self.assertZero(sp.Matrix([act(C, f, old) for f in forward])
                        - sp.Matrix([1, 0, 0, 0]))
        self.assertZero(bracket(E, C, old) + D)
        self.assertZero(bracket(E, D, old))
        h = forward
        for _ in range(3):
            h = sp.Matrix([act(E, f, old) for f in h])
        self.assertZero(h - sp.Matrix([u, 0, 0, 0]))
        self.assertZero(sp.Matrix([act(E, f, old) for f in h]))
        tau = act(E, act(E, forward[0], old), old)
        self.assertZero(tau - (u*s + v**2))
        t = act(D, tau, old)
        self.assertZero(t - 2*v)
        self.assertZero(act(C, u, old) - 3*t)
        self.assertZero(act(E, t, old))
        self.assertEqual(act(D, t, old), 2)
        # Derive actual coordinate partials from the verified inverse,
        # not from a Jacobian-one premise alone.
        columns = clean(inverse.jacobian(new).subs(
            dict(zip(new, forward)), simultaneous=True))
        self.assertZero(columns[:, 0] - C)
        self.assertZero(forward.jacobian(old)*columns - sp.eye(4))
        heights = [max(sp.degree(entry, s) for entry in columns[:, i])
                   for i in range(4)]
        self.assertEqual(heights, [1, 4, 4, 4])
        top_four = clean(columns.applyfunc(
            lambda entry: sp.expand(entry).coeff(s, 4)))
        self.assertZero(top_four
                        - sp.Matrix([[0, 0, 0, 0], [0, 0, 0, 0],
                                     [0, -z**2/2, z, sp.Rational(1, 6)],
                                     [0, 0, 0, 0]]))

    def test_mixed_trace_redundancy_and_second_derivative_invariance_gate(self):
        # D=d/dv in this formal scalar comparison. The displayed
        # mixed identity imposes no new condition on D(t).
        v, qp, r, ai = sp.symbols("v qp r ai", nonzero=True)
        t = v**3 + v
        for m in (3, 4):
            alpha = sp.Rational(m - 1, 2)
            k = m*alpha*r*t/qp
            Wi_u = -m*ai*t/(2*qp)
            self.assertZero(-ai*sp.diff(k, v)
                            - 2*alpha*r*sp.diff(Wi_u, v))
            self.assertNotEqual(sp.diff(t, v), 0)
        old, new, forward, inverse = actual_control()
        s, u, v, z = old
        E, D = sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 0, 1, 0])
        C = sp.Matrix([0, 6*v, -s, 1])
        tau = act(E, act(E, forward[0], old), old)
        t = act(D, tau, old)
        second = act(C, act(C, u, old), old)
        self.assertZero(second + 6*s)
        self.assertZero(act(E, second, old) + 3*act(D, t, old))
        self.assertEqual(act(E, second, old), -6)


if __name__ == "__main__":
    unittest.main()
