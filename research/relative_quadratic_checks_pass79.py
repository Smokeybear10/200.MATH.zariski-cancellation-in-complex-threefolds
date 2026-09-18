"""Finite exact controls, not a realization or proof of the general frame.

The first and third methods are formal coefficient calculations. The second
uses the actual retained conic action and both polynomial inverse orders.
The fourth is a weaker intrinsic curve/replica boundary, not a full frame.
"""

import unittest

import sympy as s


class RelativeQuadraticChecks(unittest.TestCase):
    def assert_zero(self, value):
        entries = list(value) if isinstance(value, s.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(s.cancel(s.expand(entry)), 0)

    def test_formal_five_row_determinant_and_all_cofactors(self):
        Au, Av, Bu, Bv, Lu, Lv, pu, pv, p, t, Fu, Fv, FY, FZ = s.symbols(
            "Au Av Bu Bv Lu Lv pu pv p t Fu Fv FY FZ"
        )
        mat = s.Matrix([
            [Au, Av, 0, 0, 1],
            [Bu, Bv, 1, 0, 0],
            [Lu, Lv, 0, 0, 0],
            [t * pu, t * pv, 0, 1, p],
            [Fu, Fv, FY, FZ, 0],
        ])
        aa, bb = Au * Lv - Av * Lu, Bu * Lv - Bv * Lu
        base_F, base_p = Lv * Fu - Lu * Fv, Lv * pu - Lu * pv
        det = base_F - bb * FY + (p * aa - t * base_p) * FZ
        self.assert_zero(mat.det() - det)
        cofactors = s.Matrix([
            -FZ * Lv, FZ * Lu, FZ * bb, base_F - bb * FY, FZ * aa
        ])
        self.assert_zero(mat.adjugate()[:, 3] - cofactors)
        self.assert_zero(mat * cofactors - det * s.eye(5)[:, 3])

        au, av, bu, bv, a0u, a0v, b0u, b0v = s.symbols(
            "au av bu bv a0u a0v b0u b0v"
        )
        substitutions = {
            Au: au * t + a0u, Av: av * t + a0v,
            Bu: bu * t + b0u, Bv: bv * t + b0v,
        }
        rho, chi = bu * Lv - bv * Lu, au * Lv - av * Lu
        expanded = s.Poly(s.expand(det.subs(substitutions)), t)
        self.assertEqual(expanded.degree(), 1)
        self.assert_zero(expanded.nth(1) - (-rho * FY + (p * chi - base_p) * FZ))

        # This coefficient is exactly what mixed H-partials eliminate.
        Y, l0u, l0v, l1u, l1v = s.symbols("Y l0u l0v l1u l1v")
        rho_Y = s.expand(rho.subs({Lu: l0u + l1u * Y, Lv: l0v + l1v * Y}))
        self.assert_zero(s.diff(rho_Y, Y) - (bu * l1v - bv * l1u))
        self.assert_zero(rho_Y.subs({l1u: bu, l1v: bv}) - (bu * l0v - bv * l0u))
        # No matrix here is asserted to arise from an original polynomial action.

    def test_actual_conic_inverse_transport_and_second_iterate(self):
        sig, u, Y, v = s.symbols("sigma u Y v")
        x, y, z, w = s.symbols("x y z w")
        new, old = (sig, u, Y, v), (x, y, z, w)
        forward = s.Matrix([
            sig, u * sig + Y, u**2 * sig + 2 * u * Y + v,
            u + Y**2 - v * sig,
        ])
        parameter = x * z - y**2 + w
        inverse = s.Matrix([
            x, parameter, y - parameter * x,
            z - 2 * parameter * y + parameter**2 * x,
        ])
        self.assert_zero(forward.subs(dict(zip(new, inverse)), simultaneous=True) - s.Matrix(old))
        self.assert_zero(inverse.subs(dict(zip(old, forward)), simultaneous=True) - s.Matrix(new))

        E = lambda f: s.diff(f, sig)
        Q = lambda f: s.diff(f, Y)
        T = lambda f: s.diff(f, u) - 2 * Y * s.diff(f, v) - sig * s.diff(f, Y)
        theta = lambda f: s.diff(f, u) - 2 * Y * s.diff(f, v)
        self.assert_zero(forward.applyfunc(T) - s.Matrix([0, 0, 0, 1]))
        self.assert_zero(forward.applyfunc(lambda f: E(E(f))))
        for f in new:
            self.assert_zero(T(E(f)) - E(T(f)) - Q(f))
            self.assert_zero(E(Q(f)) - Q(E(f)))
        H, V, W = s.Matrix([1, u, u**2]), s.Matrix([0, 1, 2 * u]), s.Matrix([0, 0, 1])
        self.assert_zero(H.applyfunc(theta) - V)
        self.assert_zero((V * Y + W * v).applyfunc(theta))
        self.assertEqual(theta(u) * Q(theta(v)) - theta(v) * Q(theta(u)), -2)

        Z = s.symbols("Z")
        F = Z - u - Y**2
        lifts = s.Matrix([sig, u * sig + Y, u**2 * sig + 2 * u * Y + v, Z - v * sig, F])
        jac = lifts.jacobian((u, v, Y, Z, sig))
        self.assertEqual(s.expand(jac.det()), -1)
        transported_T = s.Matrix([1, -2 * Y, -sig, 1 - 2 * sig * Y, 0])
        self.assert_zero(jac * transported_T - s.Matrix([0, 0, 0, 1, 0]))
        self.assert_zero(-transported_T.diff(sig) - s.Matrix([0, 0, 1, 2 * Y, 0]))

        qx, q2x = forward.applyfunc(Q), forward.applyfunc(lambda f: Q(Q(f)))
        self.assert_zero(q2x - s.Matrix([0, 0, 0, 2]))
        self.assert_zero(forward.applyfunc(lambda f: Q(Q(Q(f)))))
        self.assertEqual(s.expand(qx[1] * q2x[3] - qx[3] * q2x[1]), 2)
        # The action is actual; its prior recognition is not a new theorem here.

    def test_formal_quadratic_normal_form_and_cubic_bound(self):
        Y, Z, t, U = s.symbols("Y Z t U")
        a, b, c, d, rho, kap, chi0, chi1 = s.symbols("a b c d rho kappa chi0 chi1")
        F = a * Z + b * Y**2 + c * Y + d
        invariant = Z + b * Y**2 / a + c * Y / a
        inverse_Z = U - b * Y**2 / a - c * Y / a
        self.assert_zero(invariant.subs(Z, inverse_Z) - U)
        self.assert_zero(inverse_Z.subs(U, invariant) - Z)
        L = lambda f: s.diff(f, Y) - (2 * b * Y + c) / a * s.diff(f, Z)
        self.assert_zero(L(invariant))
        self.assert_zero(L(F))
        self.assert_zero(F - (a * invariant + d))

        Q = lambda f: (
            -rho * a / kap * s.diff(f, Y)
            + rho * (2 * b * Y + c) / kap * s.diff(f, Z)
            - a * (chi0 + chi1 * Y) / kap * s.diff(f, t)
        )
        self.assert_zero(Q(F))
        self.assert_zero(Q(Q(Y)))
        self.assert_zero(Q(Q(Z)) + 2 * rho**2 * a * b / kap**2)
        self.assert_zero(Q(Q(t)) - rho * a**2 * chi1 / kap**2)
        for f in (Y, Z, t):
            self.assert_zero(Q(Q(Q(f))))
        self.assert_zero(Q(Y) * Q(Q(Z)) - Q(Z) * Q(Q(Y)) - 2 * rho**3 * a**2 * b / kap**3)

        # The endpoint's cofactor divisibility is formal; LND and omission
        # are additional written-proof hypotheses, not established by this test.
        au, av, Lu, Lv = s.symbols("a_u a_v ell_u ell_v")
        Tu, Tv = -a * Lv / kap, a * Lu / kap
        self.assert_zero(au * Tu + av * Tv - a * (-au * Lv + av * Lu) / kap)

        # A genuine polynomial derivation, but not an LND: self-divisibility
        # alone does not force zero. The exact eigenfunction identity makes
        # every iterate equal to u; the loop only checks four instances.
        u = s.symbols("u")
        non_lnd = lambda f: u * s.diff(f, u)
        self.assertEqual(non_lnd(u), u)
        self.assertEqual(s.rem(non_lnd(u), u, u), 0)
        iterate = u
        for _ in range(4):
            iterate = non_lnd(iterate)
            self.assertEqual(iterate, u)

    def test_whole_relative_gradient_and_replica_boundary(self):
        u, y, z, v, t = s.symbols("u y z v t")
        invariant = u * z - y**2
        D = lambda f: u * s.diff(f, y) + 2 * y * s.diff(f, z)
        self.assert_zero(D(invariant))
        self.assert_zero(D(D(y)))
        self.assert_zero(D(D(D(z))))
        self.assertEqual(s.gcd(u, 2 * y), 1)
        self.assertEqual(u.subs(u, 0), 0)
        self.assertEqual((2 * y).subs(y, 0), 0)

        # The actual fiber ideal is (u, y^2), not its radical (u, y).
        ideal = s.groebner([u, invariant], u, y, z)
        reduce_fiber = lambda f: s.expand(ideal.reduce(s.expand(f))[1])
        self.assertEqual(reduce_fiber(D(z)), 2 * y)
        self.assertEqual(reduce_fiber(y**2), 0)
        self.assertNotEqual(reduce_fiber(y), 0)

        replica = lambda f: u * D(f)
        self.assert_zero(replica(invariant))
        self.assertEqual(s.gcd(replica(y), replica(z)), u)
        self.assert_zero(replica(y) / u - D(y))
        self.assert_zero(replica(z) / u - D(z))
        self.assertEqual(reduce_fiber(replica(y)), 0)
        self.assertEqual(reduce_fiber(replica(z)), 0)

        # Over the fraction field of S, t=y/u is a D-slice. These rational
        # formulas are not claimed to give a global slice or global inverse.
        yt, zt = u * t, u * t**2 + v / u
        self.assert_zero(u * zt - yt**2 - v)
        self.assert_zero(D(y / u) - 1)
        gradient = s.Matrix([-2 * yt, u])
        kernel_generator = s.Matrix([-s.diff(zt, t), s.diff(yt, t)])
        self.assert_zero(gradient - kernel_generator)
        self.assert_zero(gradient.dot(s.Matrix([s.diff(yt, t), s.diff(zt, t)])))
        self.assert_zero(s.diff(yt, t) / u - 1)
        # This is an intrinsic polynomial model, not a simultaneous nice/good frame.


if __name__ == "__main__":
    unittest.main(verbosity=2)
