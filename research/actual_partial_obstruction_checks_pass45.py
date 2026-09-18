"""Exact controls for one actual-partial compatibility counterexample.

These four methods verify the displayed polynomial example. They do not
prove a universal compatible-slice theorem or realize the remaining
nonzero-projection highest-flow branch. Only unittest and SymPy are used.
"""

import unittest
import sympy as sp


x, y, z, t, s, eta, zeta, v, u = sp.symbols("x y z t s eta zeta v u")
physical = (x, y, z, t)
E = sp.Matrix([0, x, 2*y, 1 + x*z + 2*y**2])


def act(field, polynomial, coordinates=physical):
    return sp.expand(sum(field[i]*sp.diff(polynomial, coordinates[i])
                         for i in range(len(coordinates))))


def bracket(left, right, coordinates=physical):
    return sp.Matrix([sp.expand(act(left, right[i], coordinates)
                                - act(right, left[i], coordinates))
                      for i in range(len(coordinates))])


def substitute(expressions, mapping):
    return [sp.expand(f.subs(mapping, simultaneous=True)) for f in expressions]


class ActualPartialObstructionChecks(unittest.TestCase):
    def assert_zero_vector(self, entries):
        self.assertTrue(all(sp.cancel(f) == 0 for f in entries))

    def test_coordinate_changes_action_and_flow(self):
        # Actual shear and its inverse, including the distinguished partial.
        self.assertEqual((s+y*z).subs(s, t-y*z), t)
        self.assertEqual((t-y*z).subs(t, s+y*z), s)
        intermediate = (x, y, z, s)
        ei = sp.Matrix([0, x, 2*y, 1])
        tc = sp.Matrix([0, 0, 1, -y])
        self.assertEqual(act(ei, s+y*z, intermediate), E[3])
        self.assertEqual(act(tc, s+y*z, intermediate), 0)
        self.assertEqual(act(tc, z, intermediate), 1)
        self.assert_zero_vector(bracket(ei, tc, intermediate)
                                - sp.Matrix([0, 0, 0, -x]))

        inv = (x, y-x*s, z-2*y*s+x*s**2, s)
        forward = (x, eta+x*s, zeta+2*eta*s+x*s**2, s)
        back = substitute(inv, dict(zip(intermediate, forward)))
        self.assertEqual(back, [x, eta, zeta, s])
        again = substitute(forward, {eta: inv[1], zeta: inv[2]})
        self.assertEqual(again, list(intermediate))
        self.assert_zero_vector([act(ei, inv[1], intermediate),
                                 act(ei, inv[2], intermediate)])

        # Exact finite physical action induced by exp(u E).
        yp = y+x*u
        zp = z+2*y*u+x*u**2
        tp = t+u+(yp*zp-y*z)
        flow = [x, yp, zp, tp]
        inverse = [sp.expand(f.subs(u, -u)) for f in flow]
        self.assertEqual(substitute(inverse, dict(zip(physical, flow))),
                         list(physical))
        self.assertEqual(substitute(flow, dict(zip(physical, inverse))),
                         list(physical))
        self.assertEqual(sp.expand(sp.Matrix(flow).jacobian(physical).det()), 1)
        self.assert_zero_vector([sp.diff(flow[i], u)
                                 - E[i].subs(dict(zip(physical, flow)),
                                             simultaneous=True)
                                 for i in range(4)])

    def test_actual_adjoint_profile_and_highest_direction(self):
        basis = [sp.eye(4)[:, i] for i in range(4)]
        first = [bracket(E, q) for q in basis]
        second = [bracket(E, q) for q in first]
        self.assertEqual(second[0], sp.Matrix([0, 0, 2, 2*y]))
        self.assertEqual(second[1], sp.Matrix([0, 0, 0, -2*x]))
        self.assertEqual(first[2], sp.Matrix([0, 0, 0, -x]))
        self.assert_zero_vector(first[3])
        for q in second:
            self.assert_zero_vector(bracket(E, q))
        self.assertEqual(sp.Matrix.hstack(second[0], second[1])
                         .extract([2, 3], [0, 1]).det(), -4*x)

        # Actual good-plane change: a=z-t, b=t, hence Ta=Tz, Tb=Tz+Tt.
        for q in (basis[2], basis[2]+basis[3]):
            self.assertNotEqual(bracket(E, q), sp.zeros(4, 1))
            self.assert_zero_vector(bracket(E, bracket(E, q)))
        for q in basis[:2]:
            self.assertNotEqual(bracket(E, bracket(E, q)), sp.zeros(4, 1))

        h2 = sp.Matrix([act(E, f) for f in E])
        h3 = sp.Matrix([act(E, f) for f in h2])
        self.assertEqual(h3, sp.Matrix([0, 0, 0, 6*x**2]))
        self.assert_zero_vector([act(E, f) for f in h3])
        self.assert_zero_vector(h2[:2])
        self.assert_zero_vector(bracket(E, basis[3]))

    def test_heisenberg_intrinsic_action_and_local_compatibility(self):
        U = sp.Matrix([0, 0, 0, -x])
        Y = sp.Matrix([0, 0, 0, x*y])
        self.assert_zero_vector(bracket(E, U))
        self.assert_zero_vector(bracket(Y, U))
        self.assert_zero_vector(bracket(E, Y)+x*U)
        self.assert_zero_vector([act(E, x), act(U, x), act(Y, x)])
        self.assertEqual(sp.Matrix.hstack(E, U, Y).rank(), 2)
        self.assertEqual(sp.Matrix.hstack(E, U).rank(), 2)
        sl = t-y*z
        et = y-x*sl
        ze = z-2*y*sl+x*sl**2
        self.assertEqual(act(U, sl), -x)
        self.assertEqual(act(U, et), x**2)
        self.assertEqual(sp.expand(act(U, ze)-2*x*et), 0)
        self.assertEqual(sp.cancel(act(E, y/x)), 1)
        self.assertEqual(act(U, y/x), 0)
        self.assertEqual(sp.cancel(sl+et/x-y/x), 0)

        # Primitive intrinsic field and actual multiplier, not a unit-ideal claim.
        ai = (x, eta, zeta)
        d0 = sp.Matrix([0, x, 2*eta])
        self.assertEqual(sp.gcd(d0[1], d0[2]), 1)
        self.assertEqual(sp.gcd(x*d0[1], x*d0[2]), x)
        self.assertEqual(act(d0, x*zeta-eta**2, ai), 0)
        self.assertEqual(act(d0, eta, ai), x)
        self.assertEqual(act(x*d0, eta, ai), x**2)

    def test_plinth_parity_and_failed_constant_normalization(self):
        # Exact bounded image controls supporting the full parity proof.
        ai = (x, eta, zeta)
        d0 = sp.Matrix([0, x, 2*eta])
        for coefficient in (sp.Integer(1), v, v**2+x*v+2):
            a = coefficient.subs(v, x*zeta-eta**2)
            self.assertEqual(sp.expand(act(d0, eta*a, ai)-x*a), 0)
            self.assertEqual(sp.expand(act(x*d0, eta*a, ai)-x**2*a), 0)
        coeffs = sp.symbols("a0:4")
        invariant = sum(coeffs[k]*v**k for k in range(4))
        odd = sp.expand(eta*invariant.subs(v, -eta**2))
        self.assertEqual(sp.expand(odd.subs(eta, -eta)+odd), 0)
        self.assertEqual(sp.solve(sp.Poly(odd, eta).all_coeffs(), coeffs),
                         dict.fromkeys(coeffs, 0))
        # Universal coefficient comparison for every constant direction lambda.
        lx, ly = sp.symbols("lambda_x lambda_y")
        alpha = sp.symbols("alpha", nonzero=True)
        vlam = sp.Matrix([0, 0, 2*lx, 2*lx*y-2*ly*x])
        U = sp.Matrix([0, 0, 0, -x])
        relation = x*U+alpha*vlam
        self.assertEqual(relation[2], 2*alpha*lx)
        tail = sp.expand(relation[3].subs(lx, 0))
        self.assertEqual(tail, -x**2-2*alpha*ly*x)
        self.assertEqual(sp.Poly(tail, x).coeff_monomial(x**2), -1)
        # No constant ly can erase that coefficient; allowing ly=-x/(2alpha)
        # would change the required constant-direction hypothesis.
        self.assertEqual(sp.simplify(tail.subs(ly, -x/(2*alpha))), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
