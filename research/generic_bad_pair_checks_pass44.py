"""Exact controls for the generic bad-coordinate-pair reduction.

Only unittest and SymPy are imported. Formal Schur data and generic-field
coordinates are not represented as actual unresolved four-variable actions.
The original-generator argument remains a written proof.
"""

import unittest

import sympy as s


def reduced(expr):
    return s.cancel(s.expand(expr))


def assert_zero(case, expr):
    case.assertEqual(reduced(expr), 0)


def act(field, expr, variables):
    return s.expand(sum(a * s.diff(expr, z) for a, z in zip(field, variables)))


def bracket(left, right, variables):
    return s.Matrix([
        act(left, entry, variables) - act(right, other, variables)
        for entry, other in zip(right, left)
    ])


class GenericBadPairChecks(unittest.TestCase):
    def test_rational_base_schur_coefficients_and_quadratic_graph(self):
        # Homogeneous rational base data exercise nonzero derivatives of the
        # Hessian. They are formal Schur controls, not an actual ambient frame.
        f, g, r, t = s.symbols("f g r t", nonzero=True)
        base = (f, g)
        v = s.Matrix([f, g])
        h = s.Matrix([f**3 / g, g**2 + f*g])
        k = s.Matrix([f**2 / g, g])
        ell = s.Matrix([f + g**2, g - f**2])
        q = s.Matrix([r**2 + r, r**3])
        H = h.jacobian(base)
        hess = [s.hessian(entry, base) for entry in h]
        P = H*q / 2 + k
        X = s.Matrix([
            (q.T * hess[i] * q)[0] / 4
            + (k.jacobian(base)[i, :] * q)[0] + ell[i]
            for i in range(2)
        ])
        M = s.Matrix.hstack(q.diff(r), v)
        xB = q + t*v
        xG = X + t*P + t**2*h/2
        K = (
            X.jacobian(base) + t*P.jacobian(base)
            + t**2*H/2
            - s.Matrix.hstack(X.diff(r) + t*P.diff(r), P + t*h)
            * M.inv() * (q.jacobian(base) + t*s.eye(2))
        )
        for value in H*v - 2*h:
            assert_zero(self, value)
        for value in k.jacobian(base)*v - k:
            assert_zero(self, value)
        for value in K.diff(t):
            assert_zero(self, value)
        for i in range(2):
            graph = (
                (xB.T*hess[i]*xB)[0]/4
                + (k.jacobian(base)[i, :]*xB)[0] + ell[i]
            )
            assert_zero(self, xG[i] - graph)
        self.assertNotEqual(reduced(s.diff(hess[0][0, 0], f)), 0)

    def test_actual_independent_defect_frame_and_global_determinants(self):
        # This is the inherited actual degree-two model, not a new example.
        u, v, a, c = s.symbols("u v a c")
        z = (u, v, a, c)
        g = u*v - 1
        physical = s.Matrix([u + a*a/2, v + c*c/2, a, c])
        E = s.Matrix([0, 0, u, g])
        partials = physical.jacobian(z).inv()
        W = [bracket(E, partials[:, i], z) for i in range(4)]
        V = [bracket(E, W[i], z) for i in (2, 3)]
        bad = s.Matrix([
            [act(V[j], physical[i], z) for j in range(2)]
            for i in (2, 3)
        ])
        Delta = s.expand(bad.det())
        self.assertEqual(Delta, s.expand(4*u*u*g))
        U = s.Matrix([[1, 0], [v, u]])
        H = s.diag(2*u, 2*g)
        self.assertEqual(s.simplify(bad - U*H), s.zeros(2))
        K3 = bad[0, 1]*V[0] - bad[0, 0]*V[1]
        K4 = bad[1, 1]*V[0] - bad[1, 0]*V[1]
        for value in bracket(K3, K4, z):
            assert_zero(self, value)
        self.assertEqual(s.simplify(Delta*E - u*K4 + g*K3), s.zeros(4, 1))
        for field in (E, K3, K4):
            assert_zero(self, act(field, Delta, z))
        for field in (K3, K4):
            for coordinate in physical:
                value = coordinate
                for _ in range(3):
                    value = act(field, value, z)
                assert_zero(self, value)
        j = g*a - u*c
        assert_zero(self, act(K3, j, z) - u*Delta)
        assert_zero(self, act(K4, j, z) - g*Delta)
        assert_zero(self, act(E, v*a - c, z) - 1)

    def test_generic_bad_pair_with_nonlinear_common_gauge(self):
        # Actual coordinates over L=C(f,g), not a new global C-four-ring
        # model. Individual q_i may be cubic even though g*q1-f*q2 is linear.
        f, g, r, t, X, Y = s.symbols("f g r t X Y", nonzero=True)
        z = (r, t)
        q1 = r**3
        q2 = (g*r**3 - r)/f
        x3, x4 = f*t + q1, g*t + q2
        inverse_r = g*X - f*Y
        inverse_t = (X - inverse_r**3)/f
        assert_zero(self, inverse_r.subs({X: x3, Y: x4}) - r)
        assert_zero(self, inverse_t.subs({X: x3, Y: x4}) - t)
        replacement = {r: inverse_r, t: inverse_t}
        assert_zero(self, x3.subs(replacement, simultaneous=True) - X)
        assert_zero(self, x4.subs(replacement, simultaneous=True) - Y)
        V3, V4 = s.Matrix([1, 0]), s.Matrix([0, 1])
        bad = s.Matrix([[s.diff(x3, r), s.diff(x3, t)],
                        [s.diff(x4, r), s.diff(x4, t)]])
        assert_zero(self, bad.det() - 1)
        K3 = bad[0, 1]*V3 - bad[0, 0]*V4
        K4 = bad[1, 1]*V3 - bad[1, 0]*V4
        for value in bracket(K3, K4, z):
            assert_zero(self, value)
        assert_zero(self, act(K3, x4, z) + 1)
        assert_zero(self, act(K4, x3, z) - 1)
        assert_zero(self, g*s.diff(q1, r, 2) - f*s.diff(q2, r, 2))
        self.assertEqual(s.degree(q1, r), 3)
        self.assertEqual(s.degree(q2, r), 3)

    def test_quadratic_graph_alone_does_not_supply_original_generators(self):
        # This map is NOT an ambient coordinate frame. Its generic image is
        # L[p, psi(r)] inside L[p,r], with psi of degree three. This checks
        # why the proof must use the original-generator equality explicitly.
        f, g, r, t = s.symbols("f g r t")
        z = (f, g, r, t)
        x3, x4 = r**2 + f*t, r**3 + g*t
        x = s.Matrix([f + x3**2/2, g + x4**2/2, x3, x4])
        psi = s.expand(g*x3 - f*x4)
        self.assertEqual(psi, g*r**2 - f*r**3)
        self.assertEqual(s.degree(psi, r), 3)
        jacobian = reduced(x.jacobian(z).det())
        assert_zero(self, jacobian - s.diff(psi, r))
        self.assertNotEqual(jacobian, 0)
        self.assertGreater(s.degree(jacobian, r), 0)
        # A nonzero Jacobian is not a polynomial inverse certificate.
        assert_zero(self, x[0] - x3*x3/2 - f)
        assert_zero(self, x[1] - x4*x4/2 - g)


if __name__ == "__main__":
    unittest.main()

