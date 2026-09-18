"""Two exact controls for the moving quadratic velocity form.

The first checks the formal connection identity with independent symmetric
G and torsion-free connection coefficients, after imposing T=0. The second
uses a nonplanar polynomial velocity column to compute its moving frame,
constant quadratic form, and the acceleration-cancelling triangular shear.
The velocity example is coefficient algebra only: no actual four-coordinate
inverse realizing that column is supplied. These finite identities do not
prove the actual Jacobian-unit argument, universal T-vanishing, frame entry,
recognition, or cancellation. No solver or earlier checker is imported.
"""

import unittest

import sympy as sp


class QuadraticVelocityShearChecks(unittest.TestCase):
    def test_formal_moving_metric_connection_identity(self):
        g11, g12, g22 = sp.symbols("g11 g12 g22")
        c111, c112, c122, c211, c212, c222 = sp.symbols(
            "c111 c112 c122 c211 c212 c222")
        G = sp.Matrix([[g11, g12], [g12, g22]])
        # C[ell][i,j] is symmetric in i,j; ell labels the tangent column.
        C = (sp.Matrix([[c111, c112], [c112, c122]]),
             sp.Matrix([[c211, c212], [c212, c222]]))
        H = sp.diag(-1, G)
        for i in range(2):
            M = sp.zeros(3)
            M[i + 1, 0] = 1
            for j in range(2):
                M[0, j + 1] = G[i, j]
                for ell in range(2):
                    M[ell + 1, j + 1] = C[ell][i, j]
            # This is exactly the derivative prescribed by T_ijk=0.
            dG = sp.Matrix(2, 2, lambda j, k: sum(
                G[ell, j] * C[ell][i, k]
                + G[ell, k] * C[ell][i, j] for ell in range(2)))
            dH = sp.zeros(3)
            dH[1:3, 1:3] = dG
            residual = dH - M.T * H - H * M
            self.assertEqual(residual.applyfunc(sp.expand), sp.zeros(3))
            self.assertEqual((dG - dG.T).applyfunc(sp.expand), sp.zeros(2))

    def test_nonplanar_velocity_constant_form_and_shear(self):
        s, t, u, q = sp.symbols("s t u q")
        b = sp.Matrix([1 + 2 * s * t, 2 * s, 2 * t + 2 * s * t**2])
        variables = (s, t)
        frame = sp.Matrix.hstack(b, b.diff(s), b.diff(t))
        self.assertEqual(sp.expand(frame.det()), 4)
        inverse = frame.inv()
        M = [(inverse * frame.diff(variable)).applyfunc(sp.expand)
             for variable in variables]
        G = sp.Matrix([[M[0][0, 1], M[0][0, 2]],
                       [M[1][0, 1], M[1][0, 2]]])
        self.assertEqual(G, sp.Matrix([[0, 2], [2, -4 * s**2]]))
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    cubic = -sp.diff(G[j, k], variables[i]) + sum(
                        G[ell, j] * M[i][ell + 1, k + 1]
                        + G[ell, k] * M[i][ell + 1, j + 1]
                        for ell in range(2))
                    self.assertEqual(sp.expand(cubic), 0)

        H = sp.diag(-1, G)
        Q = (inverse.T * H * inverse).applyfunc(sp.expand)
        half = sp.Rational(1, 2)
        expected = sp.Matrix([[-1, 0, 0], [0, 0, half], [0, half, 0]])
        self.assertEqual(Q, expected)
        self.assertEqual((frame.T * Q * frame - H).applyfunc(sp.expand), sp.zeros(3))
        self.assertEqual(sp.expand((b.T * Q * b)[0]), -1)
        self.assertEqual(sp.expand((b.T * (-Q) * b)[0]), 1)
        self.assertEqual(Q.diff(s), sp.zeros(3))
        self.assertEqual(Q.diff(t), sp.zeros(3))
        # Independence of 1,b1,b2,b3 excludes an affine-plane image.
        polynomials = [sp.Poly(value, s, t) for value in [sp.Integer(1), *b]]
        coefficient_minor = sp.Matrix([
            [value.coeff_monomial(monomial) for value in polynomials]
            for monomial in (sp.Integer(1), s, t, s * t)])
        self.assertEqual(coefficient_minor.det(), 8)

        a1, a2, a3, z0 = sp.symbols("a1 a2 a3 z0")
        path = sp.Matrix([a1, a2, a3]) + u * b
        original_z = z0 + q * u**2 / 2
        sheared_path = sp.expand(original_z + q * (path.T * Q * path)[0] / 2)
        self.assertEqual(sp.diff(original_z, u, 2), q)
        self.assertEqual(sp.expand(sp.diff(sheared_path, u, 2)), 0)

        x1, x2, x3, z, Z = sp.symbols("x1 x2 x3 z Z")
        x = sp.Matrix([x1, x2, x3])
        correction = q * (x.T * Q * x)[0] / 2
        forward_z, backward_z = z + correction, Z - correction
        self.assertEqual(sp.expand(forward_z.subs(z, backward_z) - Z), 0)
        self.assertEqual(sp.expand(backward_z.subs(Z, forward_z) - z), 0)
        jacobian = sp.Matrix([x1, x2, x3, forward_z]).jacobian([x1, x2, x3, z])
        self.assertEqual(jacobian.det(), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
