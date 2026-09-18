"""Exact controls for the written two-shear dichotomy, not its full proof."""

import unittest
import sympy as sp


u, v, x, y, s = sp.symbols("u v x y s")


def apply(field, f, variables=(u, v)):
    return sp.expand(sum(c*sp.diff(f, z) for c, z in zip(field, variables)))


def bracket(a, b):
    return tuple(sp.expand(apply(a, c)-apply(b, d)) for c, d in zip(b, a))


def ham(f):
    return (-sp.diff(f, v), sp.diff(f, u))


def poisson(f, g):
    return sp.expand(sp.diff(f, u)*sp.diff(g, v)-sp.diff(f, v)*sp.diff(g, u))


class FrameControls(unittest.TestCase):
    def test_actual_inverse_both_directions(self):
        for m in range(1, 5):
            for n in range(1, 5):
                U, S = x+y**m, y+(x+y**m)**n
                X, Y = u-(s-u**n)**m, s-u**n
                self.assertEqual(sp.expand(U.subs({x:X, y:Y}, simultaneous=True)-u), 0)
                self.assertEqual(sp.expand(S.subs({x:X, y:Y}, simultaneous=True)-s), 0)
                self.assertEqual(sp.expand(X.subs({u:U, s:S}, simultaneous=True)-x), 0)
                self.assertEqual(sp.expand(Y.subs({u:U, s:S}, simultaneous=True)-y), 0)

    def test_slice_and_invariant(self):
        for m, n in ((1, 1), (1, 4), (4, 1), (2, 2), (2, 3), (3, 2)):
            U = x+y**m
            delta = (1+m*n*y**(m-1)*U**(n-1), -n*U**(n-1))
            self.assertEqual(apply(delta, U, (x, y)), 1)
            self.assertEqual(apply(delta, y+U**n, (x, y)), 0)
            # Coordinatewise nilpotence via explicit inverse coordinates.
            self.assertEqual(sp.diff(u-(s-u**n)**m, u, m*n+1), 0)
            self.assertEqual(sp.diff(s-u**n, u, n+1), 0)

    def test_intermediate_coordinate_fields(self):
        for m, n in ((1, 3), (3, 1), (2, 2), (2, 3), (3, 2)):
            U = x+y**m
            delta = (1+m*n*y**(m-1)*U**(n-1), -n*U**(n-1))
            self.assertEqual(apply(delta, U, (x, y)), 1)
            self.assertEqual(sp.expand(apply(delta, y, (x, y)).subs(x, u-y**m)), -n*u**(n-1))
            self.assertEqual(sp.diff(U, y), m*y**(m-1))

    def test_constant_partial_extraction(self):
        for n in range(2, 8):
            field = (sp.Integer(1), -n*u**(n-1))
            for _ in range(n-1):
                field = bracket((1, 0), field)
            self.assertEqual(field, (0, -sp.factorial(n)))

    def test_hamiltonian_bracket_identity(self):
        samples = (u**3*v**2+v, u*v+u**2, v**4-u, u**2*v**5)
        for f in samples:
            for g in samples:
                self.assertEqual(bracket(ham(f), ham(g)), tuple(map(sp.expand, ham(poisson(f, g)))))

    def test_infinite_word_exact_formula(self):
        for m, n in ((2, 2), (2, 3), (3, 2), (3, 3), (4, 2)):
            h, coefficient = u**n, sp.Integer(1)
            for r in range(6):
                a, b = n+r*(n-2), r*(m-2)
                self.assertEqual(h, coefficient*u**a*v**b)
                self.assertNotEqual(coefficient, 0)
                self.assertEqual(max(sp.Poly(c, u, v).total_degree() for c in ham(h) if c != 0), n-1+r*(m+n-4))
                h = poisson(u**n, poisson(v**m, h))
                coefficient *= -n*m*a*(b+m-1)

    def test_nilpotent_finite_bases(self):
        for n in range(1, 7):
            for j in range(n):
                field = (0, u**j)
                expected = (0, j*u**(j-1)) if j else (0, 0)
                self.assertEqual(bracket((1, 0), field), expected)
                for k in range(n):
                    self.assertEqual(bracket(field, (0, u**k)), (0, 0))
            top = (0, u**(n-1))
            for _ in range(n-1):
                top = bracket((1, 0), top)
            self.assertEqual(top, (0, sp.factorial(n-1)))
            self.assertEqual(bracket((1, 0), top), (0, 0))
            for j in range(n):
                expected = (j*v**(j-1), 0) if j else (0, 0)
                self.assertEqual(bracket((0, 1), (v**j, 0)), expected)

    def test_five_dimensional_perfect_boundary(self):
        P, Q, E, F, H = (1, 0), (0, 1), (0, u), (v, 0), (u, -v)
        basis = (P, Q, E, F, H)
        expected = {
            (0, 1): (0, 0), (0, 2): Q, (0, 3): (0, 0), (0, 4): P,
            (1, 2): (0, 0), (1, 3): P, (1, 4): (0, -1),
            (2, 3): H, (2, 4): (0, -2*u), (3, 4): (2*v, 0),
        }
        for (i, j), result in expected.items():
            self.assertEqual(bracket(basis[i], basis[j]), result)
        vectors = [sp.Matrix([sp.Poly(c, u, v).coeff_monomial(t)
                              for c in f for t in (1, u, v)]) for f in basis]
        self.assertEqual(sp.Matrix.hstack(*vectors).rank(), 5)

    def test_affine_translation_span_invariance(self):
        matrix = sp.Matrix([[1, 2, 0, 0], [0, 1, 1, 0], [0, 0, 1, 3], [0, 0, 0, 1]])
        inverse = matrix.inv()
        self.assertEqual(matrix*inverse, sp.eye(4))
        self.assertEqual(inverse.rank(), 4)
        self.assertTrue(all(value.is_Rational for value in inverse))

    def test_nonincreasing_boundary_and_good_frame(self):
        self.assertEqual([1+r*(2+2-4) for r in range(8)], [1]*8)
        self.assertEqual([2+r*(2+3-4) for r in range(6)], [2, 3, 4, 5, 6, 7])
        coords = sp.symbols("U S Z1 Z2")
        partials = [tuple(sp.Integer(i == j) for i in range(4)) for j in range(4)]
        for a in partials:
            for b in partials:
                self.assertEqual(tuple(apply(a, c, coords)-apply(b, d, coords)
                                       for c, d in zip(b, a)), (0, 0, 0, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
