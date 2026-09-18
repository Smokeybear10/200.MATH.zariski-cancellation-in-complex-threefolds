"""Finite parameter and formal-matrix controls, not actual nice actions."""

import unittest

import sympy as s


class NormalRowParameterChecks(unittest.TestCase):
    def assert_zero(self, value):
        entries = list(value) if isinstance(value, s.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(s.cancel(s.expand(entry)), 0)

    @staticmethod
    def coefficient_rank(expressions, variables):
        polynomials = [s.Poly(s.expand(f), *variables) for f in expressions]
        monomials = sorted(set().union(*(set(f.monoms()) for f in polynomials)))
        return s.Matrix([[f.coeff_monomial(m) for f in polynomials] for m in monomials]).rank()

    def test_unimodular_rows_with_proper_primitive_normals(self):
        u, v, xi, eta = s.symbols("u v xi eta")
        for epsilon in (0, 1):
            with self.subTest(epsilon=epsilon):
                P = s.Matrix([1 + epsilon * u**2, u, v**2, u * v])
                U = P.jacobian((u, v))
                augmented = P.row_join(U)
                normal = s.Matrix([
                    (-1) ** (i + 3) * augmented.extract([j for j in range(4) if j != i], range(3)).det()
                    for i in range(4)
                ])
                expected = s.Matrix([u * v**2, -2 * v**2, -u * (1 - epsilon * u**2), 2 * v * (1 - epsilon * u**2)])
                self.assert_zero(normal - expected)
                self.assert_zero(normal.T * augmented)
                self.assertEqual(augmented.rank(), 3)
                self.assertEqual((s.Matrix([[1, -epsilon * u, 0, 0]]) * P)[0].expand(), 1)
                self.assertEqual(s.gcd_list(list(normal)), 1)
                self.assertEqual(self.coefficient_rank(list(normal), (u, v)), 4)

                ideal = s.groebner(list(normal), u, v)
                self.assertEqual(ideal.reduce(s.Integer(1))[1], 1)
                self.assert_zero(ideal.reduce(v**2)[1])
                self.assert_zero(ideal.reduce(u * (1 - epsilon * u**2))[1])
                points = [(0, 0, 2)] if epsilon == 0 else [(0, 0, 2), (1, 0, 1), (-1, 0, 1)]
                for u0, v0, expected_rank in points:
                    self.assert_zero(normal.subs({u: u0, v: v0}))
                    shifted = [s.Poly(f.subs({u: xi + u0, v: eta + v0}), xi, eta) for f in normal]
                    order = min(sum(m) for f in shifted for m, coefficient in f.terms() if coefficient != 0)
                    initials = [sum(coefficient * xi**m[0] * eta**m[1] for m, coefficient in f.terms() if sum(m) == order) for f in shifted]
                    self.assertEqual(order, 1)
                    self.assertEqual(self.coefficient_rank(initials, (xi, eta)), expected_rank)

                # The epsilon=1 tuple has no nonzero constant linear
                # combination which is a constant; epsilon=0 has P1=1.
                derivatives = [list(P.diff(u)), list(P.diff(v))]
                coeffs = []
                for column in derivatives:
                    polys = [s.Poly(f, u, v) for f in column]
                    monomials = sorted(set().union(*(set(f.monoms()) for f in polys)))
                    coeffs.extend([[f.coeff_monomial(m) for f in polys] for m in monomials])
                self.assertEqual(s.Matrix(coeffs).rank(), 4 if epsilon else 3)

    def test_formal_nilpotence_fails_original_partial_integrability(self):
        u, v = s.symbols("u v")
        X, Y, Z, W = s.symbols("X Y Z W")
        for epsilon in (0, 1):
            with self.subTest(epsilon=epsilon):
                h = 1 - epsilon * u**2
                P = s.Matrix([1 + epsilon * u**2, u, v**2, u * v])
                U = P.jacobian((u, v))
                N = s.Matrix([[u * v**2, -2 * v**2, -u * h, 2 * v * h]])
                L = s.Matrix([[-v**2, 2 * epsilon * u * v**2, h, 0], list(N)])
                C, J = L * U, U * L
                self.assert_zero(L * P)
                self.assert_zero(C - s.Matrix([[0, 2 * v * h], [0, 0]]))
                self.assert_zero(J * P)
                self.assert_zero(J**2 - 2 * v * h * U[:, 0] * N)
                self.assert_zero(J**3)
                self.assertEqual(J.rank(), 2)
                self.assertEqual((J**2).rank(), 1)
                D = lambda i, f: L[0, i] * s.diff(f, u) + L[1, i] * s.diff(f, v)
                self.assert_zero(D(3, D(0, u)) - D(0, D(3, u)) + 4 * v**2 * h)
                self.assertNotEqual(s.expand(D(3, D(0, u)) - D(0, D(3, u))), 0)
                self.assert_zero(D(3, v) - 2 * h * v)
                iterate = v
                for n in range(1, 4):
                    iterate = s.expand(D(3, iterate))
                    self.assert_zero(iterate - (2 * h)**n * v)

                equation = X * W**2 - Y**2 * Z if epsilon == 0 else X * Z * W**2 - Y**2 * Z**2 - W**4
                self.assertEqual(s.Poly(equation, X, Y, Z, W).total_degree(), 3 + epsilon)
                gradient = s.Matrix([s.diff(equation, z) for z in (X, Y, Z, W)])
                substitution = dict(zip((X, Y, Z, W), P))
                self.assert_zero(equation.subs(substitution, simultaneous=True))
                multiplier = u if epsilon == 0 else u * v**2
                self.assert_zero(gradient.subs(substitution, simultaneous=True) - multiplier * N.T)
                self.assertEqual(self.coefficient_rank(list(gradient), (X, Y, Z, W)), 4)
                self.assert_zero(gradient.subs({X: 1, Y: 0, Z: 1, W: 0}))
                self.assertEqual(s.gcd(s.diff(equation, X), equation.subs(X, 0)), 1)
        # L is formal derivative data, not a Jacobian of two original invariants.

    def test_formal_quadric_transfer_determinant_and_linear_part(self):
        au, av, bu, bv, cu, cv, lu, lv, Fu, Fv, FY, FZ = s.symbols(
            "alpha_u alpha_v beta_u beta_v gamma_u gamma_v ell_u ell_v Fu Fv FY FZ"
        )
        matrix = s.Matrix([
            [au, av, 0, 0, 1], [bu, bv, 1, 0, 0],
            [cu, cv, 0, 1, 0], [lu, lv, 0, 0, 0],
            [Fu, Fv, FY, FZ, 0],
        ])
        beta_det, gamma_det = bu * lv - bv * lu, cu * lv - cv * lu
        self.assert_zero(matrix.det() - (lu * Fv - lv * Fu + beta_det * FY + gamma_det * FZ))
        sig, b1u, b1v, c1u, c1v, b0u, b0v, c0u, c0v = s.symbols("sigma b1u b1v c1u c1v b0u b0v c0u c0v")
        substituted = s.expand(matrix.det().subs({bu: b1u * sig + b0u, bv: b1v * sig + b0v, cu: c1u * sig + c0u, cv: c1v * sig + c0v}))
        expected = (b1u * lv - b1v * lu) * FY + (c1u * lv - c1v * lu) * FZ
        self.assert_zero(s.Poly(substituted, sig).nth(1) - expected)

        Y, Z, du, dv, g11, g12, g22 = s.symbols("Y Z d_u d_v g11 g12 g22")
        G = s.Matrix([[g11, g12], [g12, g22]])
        ell_u = -(s.Matrix([[b1u, c1u]]) * G * s.Matrix([Y, Z]))[0] + du
        ell_v = -(s.Matrix([[b1v, c1v]]) * G * s.Matrix([Y, Z]))[0] + dv
        field = s.Matrix([b1u * ell_v - b1v * ell_u, c1u * ell_v - c1v * ell_u])
        determinant = b1u * c1v - b1v * c1u
        linear = field.jacobian((Y, Z))
        self.assert_zero(linear - determinant * s.Matrix([[0, -1], [1, 0]]) * G)
        self.assert_zero(s.trace(linear))
        self.assert_zero(linear.det() - determinant**2 * G.det())
        # This verifies the matrix algebra only, not the geometric hypotheses,
        # a unit generation determinant, or a classification of Darboux curves.

    def test_explicit_segre_frame_and_polynomial_inverse(self):
        u, v, left_scale, right_scale = s.symbols("u v left_scale right_scale")
        L = s.Matrix([[1 + u**2, u], [u, 1]])
        K = s.Matrix([[1, v], [v, 1 + v**2]])
        self.assert_zero(L.det() - 1)
        self.assert_zero(K.det() - 1)
        M = s.kronecker_product(L, K)
        inverse = s.kronecker_product(
            s.Matrix([[1, -u], [-u, 1 + u**2]]),
            s.Matrix([[1 + v**2, -v], [-v, 1]]),
        )
        self.assert_zero(M * inverse - s.eye(4))
        self.assert_zero(inverse * M - s.eye(4))
        self.assert_zero(M.det() - 1)
        coordinates = s.Matrix(s.symbols("sigma Y Z c"))
        original = s.Matrix(s.symbols("x1:5"))
        self.assert_zero(inverse * (M * coordinates) - coordinates)
        self.assert_zero(M * (inverse * original) - original)

        polar = s.Matrix([[0, 0, 0, 1], [0, 0, -1, 0], [0, -1, 0, 0], [1, 0, 0, 0]])
        self.assert_zero(M.T * polar * M - polar)
        P = M[:, 0]
        self.assert_zero(P[0] * P[3] - P[1] * P[2])
        normal = s.Matrix([[P[3], -P[2], -P[1], P[0]]])
        self.assert_zero(normal - inverse[3, :])
        self.assert_zero(normal * M - s.Matrix([[0, 0, 0, 1]]))

        # Two independent scalar determinants on a nonconstant SL2 scaffold.
        # The all-matrix determinant formula remains a written argument.
        scaled = s.kronecker_product(
            L * s.diag(left_scale, 1), K * s.diag(right_scale, 1)
        )
        self.assert_zero(scaled.T * polar * scaled - left_scale * right_scale * polar)
        self.assert_zero(scaled.det() - left_scale**2 * right_scale**2)
        bu, bv, cu, cv, du, dv, Y, Z = s.symbols("bu bv cu cv du dv Y Z")
        ell_u, ell_v = cu * Y + bu * Z + du, cv * Y + bv * Z + dv
        field = s.Matrix([bu * ell_v - bv * ell_u, cu * ell_v - cv * ell_u])
        delta = bu * cv - bv * cu
        self.assert_zero(field.jacobian((Y, Z)) - s.diag(delta, -delta))
        # Actual polynomial coordinate maps over C[u,v], not a full nice action.


if __name__ == "__main__":
    unittest.main(verbosity=2)
