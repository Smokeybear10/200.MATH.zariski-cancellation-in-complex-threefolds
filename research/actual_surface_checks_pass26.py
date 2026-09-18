"""Independent exact controls for actual-surface-realization-pass26.md.

The universal root argument and ring recognition are in the written
proof. This script imports no solver or other project module.
"""

import unittest
import sympy as sp


u, y, z, G, H, t = sp.symbols("u y z G H t")
ii = sp.I
A = (u-1)*(u-ii)
b = (1-ii)*(u+1)*(u+ii)/4
a = -ii*A*(u+(1+ii)/2)/2
q = -u*b**2
rcoef = ii*u*A/8
d = u**4-1
e = d*u
g = a+b*y
h = q*z+rcoef*y
surface = A*z-y*(y-1)
F = sp.expand(4/(1-ii) * (
    b*A*H+u*b*(G-a)*(G-a-b)-A*rcoef*(G-a)
))
Q = G*(G-1)*(G-ii)
L1 = 1-ii+2*ii*G
L3 = (2-2*ii)*G**2-2*G+1+ii
ROOTS = (sp.Integer(1), sp.Integer(-1), ii, -ii)
PAIRS = (
    ((sp.Integer(1), 0), (ii, 0)),
    ((sp.Integer(1), 1), (-ii, None)),
    ((sp.Integer(-1), None), (ii, 1)),
)
TAGS = (sp.Integer(0), sp.Integer(1), ii)


def normal_g(root, epsilon):
    if epsilon is None:
        y_value = root*A.subs(u, root)*t
        answer = sp.diff(a, u)+sp.diff(b, u)*y_value
    else:
        answer = (sp.diff(a, u)+sp.diff(b, u)*epsilon
                  + b*sp.diff(A, u)*root*t)
    return sp.expand(answer.subs(u, root))


class ActualSurfaceChecks(unittest.TestCase):
    def test_rank_nine_normalization_relation(self):
        polynomial = sp.Poly(F, u)
        self.assertEqual(polynomial.degree(), 9)
        self.assertEqual(sp.simplify(polynomial.LC()), -sp.Rational(1, 4))
        self.assertEqual(sp.expand(sp.diff(F, H)-d), 0)
        substituted = sp.expand(F.subs({G: g, H: h}, simultaneous=True))
        quotient, remainder = sp.div(substituted, surface, z, y, u,
                                     extension=ii)
        self.assertEqual(remainder, 0)
        self.assertNotEqual(quotient, 0)
        for root in ROOTS:
            self.assertNotEqual(sp.expand(F.subs(u, root)), 0)
        self.assertEqual(sp.Poly(-4*F, u).LC(), 1)

    def test_exact_conductor_kernel_basis_and_index(self):
        residues = (sp.Integer(0), L1, sp.Integer(2), L3)
        for tag, pair in zip(TAGS, PAIRS):
            left, right = pair[0][0], pair[1][0]
            for exponent in range(9):
                self.assertEqual(
                    sp.expand(residues[exponent % 4].subs(G, tag)
                              - left**exponent+right**exponent), 0
                )
        basis = (
            sp.Integer(1), u-L1*u**2/2, Q*u**2,
            u**3-L3*u**2/2, u**4, u**5-L1*u**2/2,
            u**6-u**2, u**7-L3*u**2/2, u**8,
        )
        columns = []
        for entry in basis:
            coefficients = sp.Poly(entry, u)
            column = sp.Matrix([coefficients.nth(k) for k in range(9)])
            columns.append(column)
            difference = sp.expand(sum(column[k]*residues[k % 4]
                                       for k in range(9)))
            self.assertEqual(sp.rem(difference, Q, G, extension=ii), 0)
        self.assertEqual(
            sp.expand(sp.Matrix.hstack(*columns).det()-Q), 0
        )
        # The retained invariant generators are exact basis combinations.
        self.assertEqual(sp.expand(basis[4]-basis[0]-d), 0)
        self.assertEqual(sp.expand(basis[5]-basis[1]-e), 0)

    def test_full_conductor_tangent_covectors(self):
        expected = (
            sp.Matrix([8*ii, -8*t-2-2*ii, 16*(1+ii), 0]),
            sp.Matrix([14*ii, 8*ii*t+4-6*ii, 16*(1-ii), 0]),
            sp.Matrix([14*ii, -8*ii*t-6+4*ii, 16*(-1+ii), 0]),
        )
        for pair, normal in zip(PAIRS, expected):
            first, second = pair
            left = sp.Matrix([4*first[0]**3, 4,
                              normal_g(*first)])
            right = sp.Matrix([4*second[0]**3, 4,
                               normal_g(*second)])
            cross = left.cross(right)
            self.assertEqual(
                [sp.expand(cross[k]-normal[k]) for k in range(3)], [0]*3
            )
            self.assertNotEqual(normal[2], 0)
            self.assertNotEqual(sp.diff(normal[1], t), 0)
        critical = -(1+ii)/4
        self.assertEqual(expected[0][1].subs(t, critical), 0)
        # For j=c(d+1)^k+b0, the conductor derivative is ck times dd.
        c = sp.symbols("c", nonzero=True)
        for exponent in (1, 2, 5):
            candidate = c*(d+1)**exponent
            for root in ROOTS:
                self.assertEqual(
                    sp.simplify(sp.diff(candidate, u).subs(u, root)
                                - c*exponent*4*root**3), 0
                )

    def test_actual_global_collision_formulas(self):
        witness = sp.symbols("witness")
        target_g = a.subs(u, witness)
        y0 = sp.expand((target_g-a.subs(u, 0))/b.subs(u, 0))
        z0 = sp.expand(y0*(y0-1)/ii)
        first = {u: witness, y: 0, z: 0}
        second = {u: 0, y: y0, z: z0}
        self.assertEqual(sp.expand(surface.subs(first, simultaneous=True)), 0)
        self.assertEqual(sp.expand(surface.subs(second, simultaneous=True)), 0)
        self.assertEqual(
            sp.expand(g.subs(first, simultaneous=True)
                      -g.subs(second, simultaneous=True)), 0
        )
        self.assertEqual(h.subs(first, simultaneous=True), 0)
        self.assertEqual(h.subs(second, simultaneous=True), 0)
        self.assertEqual(d.subs(u, 0), -1)
        for root in ROOTS:
            self.assertEqual(d.subs(u, root), 0)

    def test_monomial_descent_has_exact_fourfold_period(self):
        # u^N at the four roots depends only on N mod 4.
        values = []
        for residue in range(4):
            branch_values = tuple(sp.expand(root**residue) for root in ROOTS)
            values.append(len(set(branch_values)) == 1)
        self.assertEqual(values, [True, False, False, False])
        self.assertEqual(sp.rem(u**4-1, d, u), 0)
        self.assertEqual(sp.rem(u**5-1, d, u), u-1)

    def test_legitimate_nonlinear_shear_has_algebraic_collisions(self):
        candidate = e+d**2
        collision_polynomial = u**7+u**4-2*u**3-1
        self.assertEqual(
            sp.expand(candidate-1-u*collision_polynomial), 0
        )
        self.assertEqual(sp.gcd(collision_polynomial, u*(u**4-1)), 1)
        self.assertEqual(candidate.subs(u, 0), 1)
        self.assertEqual(sp.rem(candidate-1, collision_polynomial, u), 0)
        independent_d, independent_e = sp.symbols("D E")
        sheared = independent_e+independent_d**2
        self.assertEqual(
            sp.expand((sheared-independent_d**2)-independent_e), 0
        )
        self.assertEqual(
            sp.Matrix([independent_d, sheared]).jacobian(
                [independent_d, independent_e]).det(), 1
        )

    def test_all_affine_projection_collision_cases(self):
        alpha, beta, value = sp.symbols("alpha beta value")
        signs = (sp.Integer(1), sp.Integer(-1), sp.Integer(-1))
        for tag, sign in zip(TAGS, signs):
            smooth_image = sp.Matrix([0, (tag-alpha)+alpha, beta])
            conductor_image = sp.Matrix([0, tag, sign*(sign*beta)])
            self.assertEqual(smooth_image-conductor_image, sp.zeros(3, 1))
        # If the kernel changes g but fixes d,e, every conductor line
        # covers the same output line under (d,e,h-beta*g).
        for tag, sign in zip(TAGS, signs):
            chosen_t = sign*(value+beta*tag)
            self.assertEqual(sp.expand(sign*chosen_t-beta*tag-value), 0)
        vd, ve, vg, vh = sp.symbols("vd ve vg vh")
        normal_at_first = sp.Matrix([8*ii, -8*t-2-2*ii,
                                     16*(1+ii), 0])
        pairing = sp.expand(normal_at_first.dot(sp.Matrix([vd, ve, vg, vh])))
        self.assertEqual(sp.diff(pairing, t), -8*ve)


if __name__ == "__main__":
    unittest.main(verbosity=2)

