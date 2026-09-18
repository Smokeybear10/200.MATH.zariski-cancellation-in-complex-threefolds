"""Formal coefficient and exact rational-basis controls for the speed curve.

These identities do not construct an actual four-coordinate polynomial frame.
In particular, the cubic b(r) below deliberately precedes the separate
actual-generator argument that would force b(r) to be affine.
"""

import unittest

import sympy as sp


class SpeedCurveGraphChecks(unittest.TestCase):
    def same(self, left, right):
        difference = left - right
        if isinstance(difference, sp.MatrixBase):
            self.assertEqual(
                difference.applyfunc(lambda entry: sp.cancel(sp.expand(entry))),
                sp.zeros(*difference.shape),
            )
        else:
            self.assertEqual(sp.cancel(sp.expand(difference)), 0)

    def test_fixed_bad_derivatives_and_arbitrary_scalar_integrations(self):
        u, w, y, z = sp.symbols("u w y z")
        h = sp.Function("h")(u)
        k = sp.Function("k")(u, w)
        Z = sp.Function("Z")(u, w, z)
        a0 = sp.Function("a0")(u)
        b0 = sp.Function("b0")(u)
        Q = Z + y * (z * sp.diff(h, u) / 2 + k) + y**2 * h / 2

        # The derivative holds the actual bad pair fixed, not y and z.
        fixed_bad_u = (
            sp.diff(Q, u)
            - a0 * z * sp.diff(Q, y)
            - (y + b0 * z) * sp.diff(Q, z)
        )
        fixed_bad_w = sp.diff(Q, w)
        self.same(sp.expand(fixed_bad_u).coeff(y, 2), 0)
        self.same(
            sp.expand(fixed_bad_u).coeff(y, 1),
            -sp.diff(Z, z)
            - b0 * z * sp.diff(h, u) / 2
            + z * sp.diff(h, u, 2) / 2
            + sp.diff(k, u)
            - a0 * z * h,
        )
        self.same(sp.expand(fixed_bad_w).coeff(y, 1), sp.diff(k, w))

        independent_k = sp.Function("k0")(u)
        ell = sp.Function("ell")(u, w)
        integrated_Z = (
            z**2 * (sp.diff(h, u, 2) - b0 * sp.diff(h, u) - 2 * a0 * h) / 4
            + z * sp.diff(independent_k, u)
            + ell
        )
        integrated_Q = (
            integrated_Z
            + y * (z * sp.diff(h, u) / 2 + independent_k)
            + y**2 * h / 2
        )
        final_u = (
            sp.diff(integrated_Q, u)
            - a0 * z * sp.diff(integrated_Q, y)
            - (y + b0 * z) * sp.diff(integrated_Q, z)
        )
        self.same(sp.diff(final_u, y), 0)
        self.same(sp.diff(integrated_Q, w), sp.diff(ell, w))

    def test_rational_speed_basis_and_nonlinear_parameter_schur_coefficients(self):
        u, w, r, y, z, X, Y = sp.symbols("u w r y z X Y")
        v = sp.Matrix([u, u**2 + 1])
        vu = v.diff(u)
        basis = sp.Matrix.hstack(v, vu)
        denominator = u**2 - 1
        self.same(basis.det(), denominator)
        a0, b0 = -2 / denominator, 2 * u / denominator
        self.same(v.diff(u, 2), a0 * v + b0 * vu)

        bad = y * v + z * vu
        inverse = sp.Matrix([
            (2 * u * X - Y) / denominator,
            (u * Y - (u**2 + 1) * X) / denominator,
        ])
        self.same(
            inverse.subs({X: bad[0], Y: bad[1]}, simultaneous=True),
            sp.Matrix([y, z]),
        )
        self.same(
            bad.subs({y: inverse[0], z: inverse[1]}, simultaneous=True),
            sp.Matrix([X, Y]),
        )
        self.same(
            inverse.diff(u),
            sp.Matrix([-a0 * inverse[1], -inverse[0] - b0 * inverse[1]]),
        )

        # This is a formal coefficient test, not an actual coordinate model.
        aa = r**2 + u * w * r
        bb = r**3 + (u + w) * r + u * w
        self.assertEqual(sp.degree(bb, r), 3)
        q = aa * v + bb * vu
        M = sp.Matrix.hstack(q.diff(r), v)
        self.same(M.det(), -sp.diff(bb, r) * denominator)
        h = sp.Function("h")(u)
        k = sp.Function("k")(u)
        ell = sp.Function("ell")(u, w)
        P = aa * h + bb * sp.diff(h, u) / 2 + k
        integrated_Z = (
            bb**2 * (sp.diff(h, u, 2) - b0 * sp.diff(h, u) - 2 * a0 * h) / 4
            + bb * sp.diff(k, u)
            + ell
        )
        X0 = integrated_Z + aa * (bb * sp.diff(h, u) / 2 + k) + aa**2 * h / 2
        base = (u, w)
        velocity_row = sp.Matrix([[sp.diff(P, r), h]])
        original_row = sp.Matrix([[sp.diff(X0, r), P]])
        inverse_M = M.inv()
        quadratic = (
            sp.Matrix([[sp.diff(h, u), sp.diff(h, w)]]) / 2
            - velocity_row * inverse_M * v.jacobian(base)
        )
        linear = (
            sp.Matrix([[sp.diff(P, u), sp.diff(P, w)]])
            - velocity_row * inverse_M * q.jacobian(base)
            - original_row * inverse_M * v.jacobian(base)
        )
        self.same(quadratic, sp.zeros(1, 2))
        self.same(linear, sp.zeros(1, 2))
        self.same(
            sp.diff(integrated_Z, r),
            (
                bb * (sp.diff(h, u, 2) - b0 * sp.diff(h, u) - 2 * a0 * h) / 2
                + sp.diff(k, u)
            ) * sp.diff(bb, r),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
