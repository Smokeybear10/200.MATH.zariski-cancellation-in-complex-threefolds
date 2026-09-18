"""Five finite controls for the dependent preceding-curve reduction.

Only the first method uses an actual full supplied polynomial frame.
Jordan and weighted-curve data in the other methods do not claim to
realize the unresolved nonzero-r frame. No solver imports are used.
"""

import unittest

import sympy as sp


def clean(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda entry: sp.cancel(sp.expand(entry)))
    return sp.cancel(sp.expand(value))


def act(field, value, variables):
    return clean(sum(a * sp.diff(value, x)
                     for a, x in zip(field, variables)))


def curve_data(m, variable, Q, K3, K4):
    A3 = clean(m * Q * sp.diff(K3, variable)
               - (m - 1) * sp.diff(Q, variable) * K3)
    A4 = clean(m * Q * sp.diff(K4, variable)
               - (m - 1) * sp.diff(Q, variable) * K4)
    common = sp.Poly(sp.gcd(A3, A4), variable).monic().as_expr()
    a0, b0 = clean(-A4 / common), clean(A3 / common)
    R = clean(a0 * K3 + b0 * K4)
    e = sp.Poly(sp.gcd(Q, R), variable).monic().as_expr()
    return A3, A4, common, a0, b0, R, clean(Q / e), clean(R / e)


class DependentPrecedingCurveChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_actual_cubic_frame_and_new_stacked_row_rank(self):
        u, v, a, c, s, r = sp.symbols("u v a c s r")
        variables = (u, v, a, c)
        G = v**2 + 1
        E = sp.Matrix([0, 0, v, G])
        D = sp.Matrix([1, 0, 0, 0])
        cubic = (a**3 + c**3) / 6
        physical = sp.Matrix([(u + cubic + v) / 2,
                              (u + cubic - v) / 2, a, c])
        x1, x2, x3, x4 = sp.symbols("x1 x2 x3 x4")
        inverse = sp.Matrix([x1 + x2 - (x3**3 + x4**3) / 6,
                             x1 - x2, x3, x4])
        self.assertZero(inverse.subs(dict(zip((x1, x2, x3, x4), physical)),
                                    simultaneous=True) - sp.Matrix(variables))
        self.assertZero(physical.subs(dict(zip(variables, inverse)),
                                     simultaneous=True)
                        - sp.Matrix([x1, x2, x3, x4]))
        slice_value = c - v * a
        invariant = G * a - v * c
        inverse_a, inverse_c = r + v * s, v * r + G * s
        self.assertZero(slice_value.subs({a: inverse_a, c: inverse_c},
                                        simultaneous=True) - s)
        self.assertZero(invariant.subs({a: inverse_a, c: inverse_c},
                                      simultaneous=True) - r)
        self.assertZero(inverse_a.subs({s: slice_value, r: invariant},
                                      simultaneous=True) - a)
        self.assertZero(inverse_c.subs({s: slice_value, r: invariant},
                                      simultaneous=True) - c)
        self.assertZero(act(E, slice_value, variables) - 1)

        P = sp.Matrix([act(E, point, variables) for point in physical])
        z = sp.Matrix([act(E, point, variables) for point in P])
        h = sp.Matrix([act(E, point, variables) for point in z])
        q = v**3 + G**3
        direction = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2), 0, 0])
        self.assertZero(h - direction * q)
        tau = 2 * z[0]
        k = clean(z - direction * tau)
        self.assertZero(k)
        self.assertEqual(sp.Matrix.vstack(z, sp.Matrix([q]))
                         .jacobian(variables).rank(), 2)
        self.assertEqual(sp.Matrix.vstack(k, sp.Matrix([q]))
                         .jacobian(variables).rank(), 1)
        for field in (E, D):
            self.assertZero(act(field, q, variables))
            for point in k:
                self.assertZero(act(field, point, variables))

        coordinate_jacobian = physical.jacobian(variables)
        J = clean(P.jacobian(variables) * coordinate_jacobian.inv())
        d = sp.Matrix([act(D, point, variables) for point in physical])
        ell = sp.Matrix([[0, 0, -v**2, -G**2]])
        M = J.row_join(-d / 2).col_join(ell.row_join(sp.zeros(1, 1)))
        self.assertZero(M**4)
        self.assertEqual((M**2).rank(), 2)
        self.assertEqual((M**3).rank(), 1)
        stacked = sp.Matrix.vstack((M**2)[:, :4], (M**3)[:, :4])
        self.assertEqual(stacked.rank(), 2)
        self.assertZero((M**2)[:4, :4]
                        - z.jacobian(variables) * coordinate_jacobian.inv() / 2)
        # This actual model has rho=r=0, not the unconstructed nonzero-r case.
        self.assertZero(ell * z)

    def test_jordan_row_nesting_for_both_permitted_highest_orders(self):
        # Formal Jordan controls: these matrices are not claimed actions.
        for m in (3, 4):
            long_block = sp.zeros(m + 1)
            for index in range(m):
                long_block[index, index + 1] = 1
            N = sp.diag(long_block, *([sp.zeros(1)] if m == 3 else []))
            self.assertEqual(N.shape, (5, 5))
            self.assertEqual((N**(m - 1)).rank(), 2)
            self.assertEqual((N**m).rank(), 1)
            self.assertZero(N**(m + 1))
            stacked = sp.Matrix.vstack(N**(m - 1), N**m)
            self.assertEqual(stacked.rank(), 2)
            # Every four-column restriction has rank at most that of the stack.
            for omitted in range(5):
                columns = [j for j in range(5) if j != omitted]
                self.assertLessEqual(stacked[:, columns].rank(), 2)

    def test_rotating_curve_full_repeated_division_and_principal_ideal(self):
        u, v = sp.symbols("u v")
        for m in (3, 4):
            Q, K3, K4 = (u - 1)**m, sp.Integer(1), u**2 + 1
            A3, A4, delta, a0, b0, R, Q1, R1 = curve_data(m, u, Q, K3, K4)
            self.assertZero(delta - (u - 1)**(m - 1))
            self.assertZero(Q1 - (u - 1)**(m - 1))
            self.assertZero(R1 + 2 * m * u)
            self.assertZero(R - m * Q * (sp.diff(K3, u) * K4
                                          - sp.diff(K4, u) * K3) / delta)
            H1 = v**2 + 1
            H = clean(Q1 * H1)
            a, b, r = clean(H * a0), clean(H * b0), clean(H1 * R1)
            rho = clean(a * K3 + b * K4)
            self.assertZero(rho - Q * r)
            self.assertZero(a * A3 + b * A4)
            for variable in (u, v):
                self.assertZero(r * sp.diff(Q, variable) + m * Q * sp.diff(r, variable)
                                - m * (K3 * sp.diff(a, variable)
                                       + K4 * sp.diff(b, variable)))
            Uab, Vab, gcd_ab = sp.gcdex(a0, b0, u)
            Uqr, Vqr, gcd_qr = sp.gcdex(Q1, R1, u)
            self.assertZero(gcd_ab - 1)
            self.assertZero(gcd_qr - 1)
            self.assertZero(Uqr * (Uab * a + Vab * b) + Vqr * r - H1)
            self.assertNotEqual(clean(sp.diff(a0 / b0, u)), 0)
            # Omitting the forced Q1 factor leaves a genuine repeated pole.
            unrepaired_r = clean(H1 * R / Q)
            self.assertEqual(sp.degree(sp.denom(unrepaired_r), u), m - 1)

    def test_common_power_alternative_retains_variable_multipliers(self):
        u, v = sp.symbols("u v")
        G = (u - 1)**2 * (u + 2)
        for m in (3, 4):
            Q = G**m
            K3, K4 = 2 * G**(m - 1), -3 * G**(m - 1)
            for Ki in (K3, K4):
                self.assertZero(m * Q * sp.diff(Ki, u)
                                - (m - 1) * sp.diff(Q, u) * Ki)
            a, r = u**2 + v, v**2 + 1
            b = (2 * a - G * r) / 3
            self.assertZero(2 * a - 3 * b - G * r)
            self.assertZero(a * K3 + b * K4 - Q * r)
            self.assertNotEqual(clean(sp.diff(a / b, v)), 0)
            for variable in (u, v):
                self.assertZero(r * sp.diff(Q, variable) + m * Q * sp.diff(r, variable)
                                - m * (K3 * sp.diff(a, variable)
                                       + K4 * sp.diff(b, variable)))
            # Nonzero formal data do not assert an actual supplied frame.
            self.assertNotEqual(r, 0)

    def test_parameter_motion_obstruction_has_an_actual_surviving_pole(self):
        u = sp.symbols("u")
        for m in (3, 4):
            Q = (u - 1)**m
            R1 = -2 * m * u
            residual = clean(R1 / sp.gcd(R1, sp.diff(Q, u)))
            self.assertEqual(sp.degree(residual, u), 1)
            coefficient = sp.Rational(m * (m - 1), 2)
            # With the actual partial d/du, H1=1, the required t is not polynomial.
            candidate_t = clean(sp.diff(Q, u) / (coefficient * R1))
            self.assertZero(sp.diff(Q, u) - coefficient * R1 * candidate_t)
            self.assertEqual(sp.degree(sp.denom(candidate_t), u), 1)
            self.assertNotEqual(clean(u * candidate_t).subs(u, 0), 0)
            # A different formal rotating curve passes this necessary test.
            data = curve_data(m, u, u, sp.Integer(1), u)
            good_R1 = data[-1]
            self.assertEqual(sp.degree(good_R1, u), 0)
            good_t = clean(1 / (coefficient * good_R1))
            self.assertZero(1 - coefficient * good_R1 * good_t)
            self.assertEqual(sp.denom(good_t).free_symbols, set())
            # Passing the necessary trace test does not certify realizability.


if __name__ == "__main__":
    unittest.main()
