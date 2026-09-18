"""Exact actual-action checks for the two-sliced-actions obstruction.

The example is recognized by displayed inverse coordinates. These
finite identities are not a proof of unrestricted cancellation.
No research solver or previous checker is imported.
"""

import unittest

import sympy as sp


class NiceCommonSliceChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    @staticmethod
    def data():
        x, y, z, w = sp.symbols("x y z w")
        variables = sp.Matrix([x, y, z, w])
        a = x*z-y**2+w
        u, v = a, a**2+1
        U = v**2*x-2*u*v*y+u**2*z
        V = -a*v*x+(v+a*u)*y-u*z
        S = a**2*x-2*a*y+z
        P = sp.Matrix([u**2, u*v, v**2, -U])
        return variables, a, sp.Matrix([a, U, V, S]), P, P.diff(w)

    def test_actual_coordinates_velocity_and_jacobian_factorization(self):
        variables, a, forward, P, Q = self.data()
        x, y, z, w = variables
        A, U, V, S = sp.symbols("A U V S")
        u, v = A, A**2+1
        target = sp.Matrix([A, U, V, S])
        inverse = sp.Matrix([
            U+2*u*V+u**2*S,
            A*U+(v+A*u)*V+u*v*S,
            A**2*U+2*A*v*V+v**2*S,
            A-U*S+V**2,
        ])
        # Verify the invariant first, then substitute the resulting exact
        # identity into the remaining forward components to control expansion.
        self.assert_zero(a.subs(dict(zip(variables, inverse)), simultaneous=True)-A)
        independent_forward = sp.Matrix([
            A,
            v**2*x-2*u*v*y+u**2*z,
            -A*v*x+(v+A*u)*y-u*z,
            A**2*x-2*A*y+z,
        ])
        self.assert_zero(independent_forward.subs(dict(zip(variables, inverse)), simultaneous=True)
                         - target)
        self.assert_zero(inverse.subs(dict(zip(target, forward)), simultaneous=True)-variables)
        self.assert_zero(forward.jacobian(variables)*P-sp.Matrix([0, 0, 0, 1]))
        self.assert_zero(forward.jacobian(variables)*Q-sp.Matrix([0, 0, 1-a**2, 2*a]))
        self.assert_zero(P.jacobian(variables)*P)
        self.assert_zero(P.jacobian(variables)*Q)
        self.assert_zero(Q.jacobian(variables)*P)

        J = P.jacobian(variables)
        row = sp.Matrix([[z, -2*y, x, 1]])
        ell = sp.Matrix([[-(a**2+1)**2, 2*a*(a**2+1), -a**2, 0]])
        ew = sp.Matrix([0, 0, 0, 1])
        self.assert_zero(J-Q*row-ew*ell)
        self.assert_zero(row*Q)
        self.assert_zero(ell*Q)
        self.assert_zero(row*ew-sp.ones(1, 1))
        self.assert_zero(ell*ew)
        self.assert_zero(J**2-Q*ell)
        self.assert_zero(J*(Q*ell))
        self.assert_zero(J*ew-Q)
        self.assert_zero(2*(Q*ell)*ew)
        self.assertNotEqual(Q[1], 0)
        constants = sp.symbols("c0:4")
        # a is an actual coordinate, so coefficient comparison over A
        # is exact, not evaluation at finitely many numerical points.
        independent_ell = sp.Matrix([[-(A**2+1)**2, 2*A*(A**2+1), -A**2, 0]])
        coefficients = sp.Poly((independent_ell*sp.Matrix(constants))[0], A).coeffs()
        matrix, rhs = sp.linear_eq_to_matrix(coefficients, constants)
        self.assert_zero(rhs)
        self.assertEqual(matrix.nullspace(), [ew])

    def test_two_global_slices_and_all_degree_common_slice_obstruction(self):
        variables, a, forward, P, Q = self.data()
        A, U, V, S = sp.symbols("A U V S")
        target = sp.Matrix([A, U, V, S])
        E_target = sp.Matrix([0, 0, 0, 1])
        Q_target = sp.Matrix([0, 0, 1-A**2, 2*A])

        def act(field, expression, frame):
            return sp.expand(sum(value*sp.diff(expression, variable)
                                 for variable, value in zip(frame, field)))

        self.assertEqual(act(E_target, S, target), 1)
        rho = V+A*S/2
        self.assertEqual(act(Q_target, rho, target), 1)
        self.assert_zero(Q_target.subs(A, 1)-2*E_target)
        self.assert_zero(Q_target.subs(A, -1)+2*E_target)
        self.assertEqual(E_target.row_join(Q_target).rank(), 2)
        self.assert_zero(Q_target-2*A*E_target-sp.Matrix([0, 0, 1-A**2, 0]))
        # The formal unknown h(A,U,V) gives the complete slice family,
        # not a finite-degree ansatz.
        h = sp.Function("h")(A, U, V)
        derivative = 2*A+(1-A**2)*sp.diff(h, V)
        self.assert_zero(derivative.subs(A, 1)-2)
        self.assert_zero(derivative.subs(A, -1)+2)
        self.assert_zero(act(Q, forward[3], variables)-2*a)
        original_rho = forward[2]+a*forward[3]/2
        self.assert_zero(act(Q, original_rho, variables)-1)
        acceleration = Q.applyfunc(lambda entry: act(Q, entry, variables))
        self.assert_zero(acceleration-sp.Matrix([0, 0, 0, 2*(1-a**2)**2]))
        self.assert_zero(acceleration.applyfunc(lambda entry: act(Q, entry, variables)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
