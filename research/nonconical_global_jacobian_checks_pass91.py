"""Finite exact controls, not a proof of the general primitive-field theorem."""

import unittest

import sympy as sp


class GlobalJacobianControls(unittest.TestCase):
    def test_cofactor_actual_frame_and_primitive_boundary(self):
        # Formal rank-three factorization. No nilpotence or action is assumed.
        q = sp.symbols("q")
        b1 = sp.Matrix(sp.symbols("b11 b21 b31"))
        b2 = sp.Matrix(sp.symbols("b12 b22 b32"))
        v0 = sp.Matrix(3, 4, sp.symbols("v0:12"))
        e4 = sp.Matrix([0, 0, 0, 1])
        upper = sp.Matrix.hstack(b1.col_join(sp.zeros(1, 1)),
                                b2.col_join(sp.zeros(1, 1)), e4)
        jac = upper * sp.diag(1, 1, q) * v0
        normal = sp.Matrix([(-1) ** (i + 3) * v0[:, [j for j in range(4) if j != i]].det()
                            for i in range(4)])
        left = b1.cross(b2).col_join(sp.zeros(1, 1))
        residual = jac.adjugate() + q * normal * left.T
        self.assertTrue(all(sp.expand(entry) == 0 for entry in residual))

        # Actual previously retained polynomial inverse frame, q=2.
        u, r, ell, t = sp.symbols("u r ell t")
        x1, x2, x3, z = sp.symbols("x1 x2 x3 z")
        canonical = (u, r, ell, t)
        original = (x1, x2, x3, z)
        forward = sp.Matrix([u, t + u * ell, r * (t + u * ell) - ell, r + u**2])
        inverse_r = z - x1**2
        inverse_ell = inverse_r * x2 - x3
        inverse = sp.Matrix([x1, inverse_r, inverse_ell, x2 - x1 * inverse_ell])
        substitute = lambda f, mapping: sp.expand(f.subs(mapping, simultaneous=True))
        self.assertEqual(inverse.applyfunc(lambda f: substitute(f, dict(zip(original, forward)))),
                         sp.Matrix(canonical))
        self.assertEqual(forward.applyfunc(lambda f: substitute(f, dict(zip(canonical, inverse)))),
                         sp.Matrix(original))
        self.assertEqual(sp.expand(forward.jacobian(canonical).det()), 1)
        velocities = forward.diff(u).applyfunc(
            lambda f: substitute(f, dict(zip(canonical, inverse))))
        original_jac = velocities.jacobian(original)
        base_rows = sp.Matrix([inverse[1], inverse[2], inverse[0]]).jacobian(original)
        n = sp.Matrix([(-1) ** (i + 3) * base_rows[:, [j for j in range(4) if j != i]].det()
                       for i in range(4)]).applyfunc(sp.expand)
        expected_n = forward.diff(t).applyfunc(
            lambda f: substitute(f, dict(zip(canonical, inverse))))
        self.assertEqual(n, expected_n)
        omega = -inverse_ell
        h = 2 * original_jac**2 * e4
        self.assertEqual(h.applyfunc(sp.expand), (2 * omega * n).applyfunc(sp.expand))
        self.assertEqual((original_jac**3 + original_jac.adjugate()).applyfunc(sp.expand),
                         sp.zeros(4))
        self.assertEqual((original_jac * velocities).applyfunc(sp.expand), 2 * e4)
        self.assertEqual((original_jac**4).applyfunc(sp.expand), sp.zeros(4))
        self.assertEqual(sp.gcd_list(list(n)), 1)
        self.assertEqual((base_rows * n).applyfunc(sp.expand), sp.zeros(3, 1))
        self.assertEqual((n.jacobian(original) * velocities - original_jac * n).applyfunc(sp.expand),
                         sp.zeros(4, 1))

        # Actual polynomial quotient only, not an original strong-frame model.
        x, y, zz, uu = sp.symbols("x y zz uu")
        ambient = (x, y, zz, uu)
        base = sp.Matrix([x, x * zz - y**2, uu]).jacobian(ambient)
        boundary = sp.Matrix([(-1) ** (i + 3) * base[:, [j for j in range(4) if j != i]].det()
                              for i in range(4)])
        self.assertEqual(boundary, sp.Matrix([0, x, 2 * y, 0]))
        self.assertEqual(sp.gcd_list(list(boundary)), 1)
        self.assertEqual(boundary.subs({x: 0, y: 0}), sp.zeros(4, 1))
        fiber = sp.groebner([x, x * zz - y**2], x, y, zz, uu)
        self.assertEqual(fiber.reduce(y**2)[1], 0)
        self.assertEqual(fiber.reduce(boundary[2])[1], 2 * y)
        self.assertEqual((base * boundary).applyfunc(sp.expand), sp.zeros(3, 1))
        second = boundary.jacobian(ambient) * boundary
        self.assertEqual(second, sp.Matrix([0, 0, 2 * x, 0]))
        self.assertEqual(second.jacobian(ambient) * boundary, sp.zeros(4, 1))


if __name__ == "__main__":
    unittest.main(verbosity=2)
