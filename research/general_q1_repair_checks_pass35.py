"""Bounded exact controls for general-q1-repair-pass35.md.

Only the written proof supplies universal quantifiers. These tests do not
verify a general cancellation statement or the cited planar theorem.
"""
import unittest
import sympy as sp

x, lam, u, v, b, c, w, z, fcoord, vcoord, hcoord = sp.symbols(
    "x lam u v b c w z fcoord vcoord hcoord"
)


def apply(field, coordinates, polynomial):
    return sp.expand(sum(a * sp.diff(polynomial, q)
                         for a, q in zip(field, coordinates)))


def bracket(left, right, coordinates):
    return tuple(sp.expand(apply(left, coordinates, value)
                           - apply(right, coordinates, other))
                 for value, other in zip(right, left))


def substitute(polynomial, mapping):
    return sp.expand(polynomial.subs(mapping, simultaneous=True))


class GeneralQ1RepairChecks(unittest.TestCase):
    def test_generic_coordinate_inverse_and_common_slice(self):
        q = v**3 + 2*v
        potential = u + q
        g = fcoord**2 + x*fcoord + 1
        antiderivative = fcoord**3/3 + x*fcoord**2/2 + fcoord
        g_actual = g.subs(fcoord, potential)
        field = (1 + lam*g_actual*sp.diff(q, v), -lam*g_actual)
        invariant = v + lam*antiderivative.subs(fcoord, potential)
        self.assertEqual(apply(field, (u, v), potential), 1)
        self.assertEqual(apply(field, (u, v), invariant), 0)

        inverse_v = vcoord - lam*antiderivative
        inverse_u = fcoord - inverse_v**3 - 2*inverse_v
        # Reconstruct both triangular steps without expanding an artificial
        # degree-27 composition.
        self.assertEqual(sp.expand(inverse_u + inverse_v**3
                                   + 2*inverse_v), fcoord)
        self.assertEqual(sp.expand(inverse_v + lam*antiderivative), vcoord)
        back_v = substitute(inverse_v, {fcoord: potential,
                                        vcoord: invariant})
        self.assertEqual(back_v, v)
        self.assertEqual(sp.expand(potential - back_v**3 - 2*back_v), u)

        physical_u = b/x**2
        physical_v = x**2*c - b**2
        self.assertEqual(sp.cancel(x**2*physical_u), b)
        self.assertEqual(sp.cancel(physical_v/x**2
                                   + x**2*physical_u**2), c)

    def test_unit_ideal_and_exact_negative_controls(self):
        potential = u + v**3 + v
        g = potential**2 + 1
        coefficient_u = 1 + lam*g*(3*v**2 + 1)
        coefficient_v = -lam*g
        self.assertEqual(sp.expand(coefficient_u
                                   + (3*v**2 + 1)*coefficient_v), 1)

        # The actual coordinate F=v+u² has a common zero of the pencil
        # coefficients. Its companion is u, so the coordinate assertion
        # itself is not the source of failure.
        bad_f = v + u**2
        for replica in (sp.Integer(1), bad_f + 1, (bad_f + 1)**2):
            bad = (1 + lam*replica*sp.diff(bad_f, v),
                   -lam*replica*sp.diff(bad_f, u))
            self.assertEqual(tuple(value.subs({u: 0, v: 0, lam: -1})
                                   for value in bad), (0, 0))
        self.assertEqual((1 + lam).subs(lam, -1), 0)
        self.assertEqual(sp.diff((1 + lam)*sp.diff(u, u), u), 0)

        # Actual finite inverse modulo a nilpotent ideal.
        product = sp.expand((1 + lam*u)*(1 - lam*u + lam**2*u**2))
        self.assertEqual(sp.rem(product - 1, u**3, u), 0)
        self.assertNotEqual(product - 1, 0)

    def test_global_potential_and_common_local_slice(self):
        h = x**2*c - b**2
        p = 1 + x + x**2
        q_formal = hcoord**3 + x*hcoord
        potential = p*b + q_formal.subs(hcoord, h)
        # Actual differentiation constructs L independently of its claimed
        # expanded coefficient formula.
        field = (sp.diff(potential, c), -sp.diff(potential, b))
        q_h = sp.diff(q_formal, hcoord).subs(hcoord, h)
        expected = (x**2*q_h, 2*b*q_h - p)
        self.assertEqual(tuple(sp.expand(a - d)
                               for a, d in zip(field, expected)), (0, 0))
        self.assertEqual(apply(field, (b, c), potential), 0)
        self.assertEqual(apply(field, (b, c), h), sp.expand(-x**2*p))
        self.assertEqual(apply((x**2, 2*b), (b, c), potential),
                         sp.expand(x**2*p))
        self.assertEqual(sp.expand(sp.diff(field[0], b)
                                   + sp.diff(field[1], c)), 0)
        self.assertEqual(sp.gcd(field[0], field[1]), 1)
        g = potential**2 + x*potential + 1
        pencil = (x**2 + lam*g*field[0], 2*b + lam*g*field[1])
        self.assertEqual(apply(pencil, (b, c), potential), sp.expand(x**2*p))

    def test_highest_pole_residue_independence(self):
        # Bounded odd/even independence at x=0, including a constant term.
        residues = [b] + [(-b**2)**j for j in range(5)]
        matrix = sp.Matrix([[sp.expand(value).coeff(b, power)
                             for value in residues] for power in range(9)])
        self.assertEqual(matrix.rank(), len(residues))
        self.assertEqual(matrix.nullspace(), [])

        # At a nonzero fiber b,h are actual independent coordinates.
        alpha = sp.Integer(2)
        h = alpha**2*c - b**2
        inverse_c = (hcoord + b**2)/alpha**2
        self.assertEqual(substitute(inverse_c, {hcoord: h}), c)
        self.assertEqual(sp.expand(alpha**2*inverse_c - b**2), hcoord)
        # A nonprimitive potential shows why fiberwise nonconstancy cannot
        # be inferred from generic nonconstancy alone.
        bad_potential = x*(b + c**2)
        self.assertEqual(bad_potential.subs(x, 0), 0)
        self.assertEqual(sp.gcd(sp.diff(bad_potential, b),
                                sp.diff(bad_potential, c)), x)

    def test_complete_finite_bracket_chain_and_all_member_control(self):
        coordinates = (lam, fcoord, vcoord)
        a = x**2*(1 + x)
        g = fcoord**3 + x*fcoord**2 + (x + 1)*fcoord + 2
        horizontal = (sp.Integer(1), sp.Integer(0), sp.Integer(0))
        pencil = (sp.Integer(0), a, -lam*g)
        chain = [(sp.Integer(0), sp.Integer(0),
                  -a**j*sp.diff(g, fcoord, j)) for j in range(4)]
        zero = (0, 0, 0)
        self.assertEqual(bracket(horizontal, pencil, coordinates),
                         tuple(sp.expand(t) for t in chain[0]))
        for j, member in enumerate(chain):
            expected = chain[j + 1] if j < 3 else zero
            self.assertEqual(bracket(pencil, member, coordinates),
                             tuple(sp.expand(t) for t in expected))
            self.assertEqual(bracket(horizontal, member, coordinates), zero)
            for other in chain:
                self.assertEqual(bracket(member, other, coordinates), zero)
        self.assertNotEqual(chain[-1][-1], 0)
        determinant = sp.Matrix.hstack(sp.Matrix(horizontal),
                                      sp.Matrix(pencil),
                                      sp.Matrix(chain[0])).det()
        self.assertEqual(sp.expand(determinant + a*g), 0)

        combination = tuple(sp.expand(2*horizontal[j] + 3*pencil[j]
                                      + sum((i + 1)*member[j]
                                            for i, member in enumerate(chain)))
                            for j in range(3))
        iterate = vcoord
        for _ in range(5):
            iterate = apply(combination, coordinates, iterate)
        self.assertNotEqual(iterate, 0)
        self.assertEqual(apply(combination, coordinates, iterate), 0)
        self.assertEqual(apply(combination, coordinates,
                               apply(combination, coordinates, lam)), 0)
        self.assertEqual(apply(combination, coordinates,
                               apply(combination, coordinates, fcoord)), 0)

    def test_boundary_actual_inverse_and_nonconstant_speed_failure(self):
        alpha = sp.Integer(2)
        k = lam*b**3 + lam**2*b + lam**3
        forward_w, forward_z = b + alpha*lam, c + k
        inverse_b = w - alpha*lam
        inverse_c = z - k.subs(b, inverse_b)
        self.assertEqual(substitute(inverse_b, {w: forward_w, z: forward_z}), b)
        self.assertEqual(substitute(inverse_c, {w: forward_w, z: forward_z}), c)
        self.assertEqual(substitute(forward_w, {b: inverse_b, c: inverse_c}), w)
        self.assertEqual(substitute(forward_z, {b: inverse_b, c: inverse_c}), z)
        horizontal = (sp.Integer(1), alpha,
                      sp.diff(k, lam).subs(b, inverse_b))
        self.assertEqual(apply(horizontal, (lam, w, z), inverse_b), 0)
        self.assertEqual(apply(horizontal, (lam, w, z), inverse_c), 0)
        boundary_top = 2*(b + alpha*lam)
        self.assertEqual(sp.Poly(boundary_top, lam).degree(), 1)

        # Actual nontriangular shear with inverse w-lambda*z²,z.
        bad_w, bad_z = b + lam*c**2, c
        self.assertEqual(sp.expand(bad_w - lam*bad_z**2), b)
        potential = -bad_w**2
        coefficients = (sp.diff(potential, c), -sp.diff(potential, b))
        self.assertEqual(max(sp.Poly(t, lam).degree() for t in coefficients), 2)
        self.assertEqual(sp.expand(coefficients[0]).coeff(lam, 2), -4*c**3)

    def test_replica_boundary_degree_products(self):
        for degree in range(1, 5):
            replica = w**degree + 1
            translated = substitute(replica, {w: b + 2*lam})
            self.assertEqual(sp.Poly(translated, lam).degree(), degree)
            self.assertEqual(sp.expand(translated).coeff(lam, degree), 2**degree)
            for order in range(1, 4):
                actual_w = b + lam**order*c**2
                derivative = sp.diff(actual_w, b)
                product = substitute(replica, {w: actual_w})*derivative
                self.assertEqual(sp.Poly(product, lam).degree(),
                                 degree*order)
                self.assertEqual(sp.expand(product).coeff(lam, degree*order),
                                 c**(2*degree))
        # For every tested nonlinear replica, a fixed first coordinate
        # permits arbitrarily higher-degree triangular second-coordinate
        # shears without changing the replica.
        k = lam**5*b**3 + lam**2*b
        for degree in range(2, 5):
            inverse_c = z - k.subs(b, w)
            vertical_c = apply((sp.Integer(0), w**degree + 1),
                               (w, z), inverse_c)
            self.assertEqual(vertical_c, w**degree + 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
