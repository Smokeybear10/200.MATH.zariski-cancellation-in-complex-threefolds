"""Two bounded actual-action controls for the pass74 projection proofs.

These checks do not classify arbitrary retracts or prove the written
all-degree homogeneous-layer criterion. No research solver is imported.
"""

import unittest

import sympy as sp


class SliceProjectionChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_quadratic_actual_inverse_action_and_nonslice_retract(self):
        u0, u1, u2, t, U0, U1, U2, S, time = sp.symbols(
            "u0 u1 u2 t U0 U1 U2 S time"
        )
        x = sp.Matrix([u0, u1, u2, t])
        target = sp.Matrix([U0, U1, U2, S])
        forward = sp.Matrix([u0 + t**2, u1 + t*u0, u2 + t*u1, t])
        inverse = sp.Matrix([
            U0 - S**2,
            U1 - S*U0 + S**3,
            U2 - S*U1 + S**2*U0 - S**4,
            S,
        ])
        self.assert_zero(forward.subs(dict(zip(x, inverse)), simultaneous=True) - target)
        self.assert_zero(inverse.subs(dict(zip(target, forward)), simultaneous=True) - x)
        velocity = sp.Matrix([-2*t, 2*t**2-u0, -u1+t*u0-2*t**3, 1])

        def act(f):
            return sum(p*sp.diff(f, v) for p, v in zip(velocity, x))

        self.assert_zero(forward.applyfunc(act) - sp.Matrix([0, 0, 0, 1]))
        self.assert_zero(inverse.diff(S).subs(dict(zip(target, forward)), simultaneous=True) - velocity)
        flow_target = forward + sp.Matrix([0, 0, 0, time])
        flow = inverse.subs(dict(zip(target, flow_target)), simultaneous=True).applyfunc(sp.expand)
        self.assert_zero(flow.diff(time) - velocity.subs(dict(zip(x, flow)), simultaneous=True))
        self.assert_zero(flow.subs(time, 0) - x)

        projection = sp.zeros(4, 1)
        iterate = x
        for j in range(5):
            projection += (-t)**j / sp.factorial(j) * iterate
            iterate = iterate.applyfunc(act)
        self.assert_zero(iterate)
        projection = projection.applyfunc(sp.expand)
        expected = sp.Matrix([forward[0], forward[1], forward[2], 0])
        self.assert_zero(projection - expected)
        self.assert_zero(projection.subs(dict(zip(x, projection)), simultaneous=True) - projection)
        self.assert_zero(projection.applyfunc(act))
        self.assert_zero(flow.subs(time, -t) - projection)
        ds = sp.Matrix([[0, 0, 0, 1]])
        self.assert_zero(projection.jacobian(x)
                         - flow.jacobian(x).subs(time, -t)*(sp.eye(4)-velocity*ds))
        self.assert_zero(ds*velocity - sp.ones(1, 1))
        self.assertEqual(max(sp.Poly(f, *x).total_degree() for f in forward), 2)
        self.assertEqual(max(sp.Poly(f, *target).total_degree() for f in inverse), 4)

        # Q != 0 branch: an actual translation with a quadratic supplied slice.
        q = u0**2 + u1*u2
        graph_forward = sp.Matrix([u0, u1, u2, t-q])
        graph_inverse = sp.Matrix([U0, U1, U2, S+U0**2+U1*U2])
        self.assert_zero(graph_forward.subs(dict(zip(x, graph_inverse)), simultaneous=True)-target)
        self.assert_zero(graph_inverse.subs(dict(zip(target, graph_forward)), simultaneous=True)-x)
        self.assert_zero(graph_forward.diff(t)-sp.Matrix([0, 0, 0, 1]))

        # An abstract quadratic retract is not an actual adapted coordinate map.
        retract = sp.Matrix([u0*(1+t), u1, u2, 0])
        self.assert_zero(retract.subs(dict(zip(x, retract)), simultaneous=True)-retract)
        attempted = sp.Matrix([retract[0], u1, u2, t])
        self.assert_zero(attempted.jacobian(x).det()-(1+t))
        self.assertEqual(attempted.jacobian(x).det().subs(t, -1), 0)
        # Et=1 and E(u0(1+t))=0 would demand the nonpolynomial -u0/(1+t).
        self.assert_zero((1+t)*(-u0/(1+t))+u0)
        self.assertNotEqual(u0.subs(t, -1), 0)

    def test_sparse_graph_and_upper_layer_controls(self):
        u0, u1, u2, t, U0, U1, U2, S, scale = sp.symbols(
            "u0 u1 u2 t U0 U1 U2 S scale"
        )
        x = sp.Matrix([u0, u1, u2, t])
        target = sp.Matrix([U0, U1, U2, S])
        L = sp.diag(1, 1, 1, 0)
        for degree in (3, 5):
            with self.subTest(degree=degree):
                # Arbitrary-degree graph formula, instantiated at two finite degrees.
                q = u0**degree + u1**(degree-1)*u2
                projection = sp.Matrix([u0, u1, u2, q])
                homogeneous = projection-L*x
                self.assert_zero(homogeneous.subs(dict(zip(x, scale*x)), simultaneous=True)
                                 - scale**degree*homogeneous)
                self.assert_zero(L*homogeneous
                                 + homogeneous.subs(dict(zip(x, L*x)), simultaneous=True)
                                 - homogeneous)
                self.assert_zero(projection.subs(dict(zip(x, projection)), simultaneous=True)-projection)
                forward = sp.Matrix([u0, u1, u2, t-q])
                inverse = sp.Matrix([U0, U1, U2, S+U0**degree+U1**(degree-1)*U2])
                self.assert_zero(forward.subs(dict(zip(x, inverse)), simultaneous=True)-target)
                self.assert_zero(inverse.subs(dict(zip(target, forward)), simultaneous=True)-x)
                self.assert_zero(forward.diff(t)-sp.Matrix([0, 0, 0, 1]))
                self.assertEqual(max(sp.Poly(f, *x).total_degree() for f in forward), degree)
                self.assertEqual(max(sp.Poly(f, *target).total_degree() for f in inverse), degree)

                # Nonzero upper homogeneous layer with an actual linear slice.
                upper = u0+t*u1**(degree-1)
                forward = sp.Matrix([upper, u1, u2, t])
                inverse = sp.Matrix([U0-S*U1**(degree-1), U1, U2, S])
                velocity = sp.Matrix([-u1**(degree-1), 0, 0, 1])
                projection = sp.Matrix([upper, u1, u2, 0])
                self.assert_zero(forward.subs(dict(zip(x, inverse)), simultaneous=True)-target)
                self.assert_zero(inverse.subs(dict(zip(target, forward)), simultaneous=True)-x)
                self.assert_zero(forward.jacobian(x)*velocity-sp.Matrix([0, 0, 0, 1]))
                self.assert_zero(velocity.jacobian(x)*velocity)
                self.assert_zero(projection-(x-t*velocity))
                self.assert_zero(projection.subs(dict(zip(x, projection)), simultaneous=True)-projection)
                self.assert_zero(projection.subs(t, 0)-sp.Matrix([u0, u1, u2, 0]))
                inverse_bound = degree+(2-1)*(degree*((degree-1)-1)+1)
                self.assertLessEqual(max(sp.Poly(f, *target).total_degree() for f in inverse),
                                     inverse_bound)


if __name__ == "__main__":
    unittest.main()
