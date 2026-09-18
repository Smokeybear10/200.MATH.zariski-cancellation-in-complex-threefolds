#!/usr/bin/env python3
"""Exact controls for invariant-slice descent and its geometric boundaries.

This module imports no research solver. The general DVR, normalization and
image-module arguments are written proofs, not consequences of these finite
identity tests. No general cancellation or formal-verification claim is made.
"""

import itertools
import unittest

import sympy as sp


def apply(field, value, coordinates):
    return sp.expand(sum(a*sp.diff(value, x) for a, x in zip(field, coordinates)))


def iterate(field, value, coordinates, count):
    for _ in range(count):
        value = apply(field, value, coordinates)
    return value


class InvariantSliceChecks(unittest.TestCase):
    def assertZero(self, value):
        self.assertEqual(sp.expand(value), 0)

    def test_triangular_invariant_and_quotient_relation(self):
        x, y, z = coords = sp.symbols("x y z")
        for m, P in ((1, y), (2, y*y+x), (3, 2*y+x*y*y), (4, y**3-x)):
            Q = sp.integrate(P, y)
            F = x**m*z-Q
            self.assertZero(apply((0, x**m, P), F, coords))
            self.assertZero(x**m*z-Q-F)

    def test_nonunit_A_has_an_explicit_affine_slice(self):
        x, y, z, t = coords = sp.symbols("x y z t")
        for m in range(1, 5):
            P = y*y+x
            F = x**m*z-y**3/3-x*y
            A, B = F, 1+x*F
            U = (-1)**m*F**(m-1)
            V = sum((-x*F)**j for j in range(m))
            self.assertZero(A*x**m*U+B*V-1)
            self.assertZero(apply((0, A*x**m, A*P, B), U*y+V*t, coords)-1)

    def test_scalar_mod_radical_is_not_scalar_mod_local_slice_value(self):
        x, f = sp.symbols("x f")
        B = 1+x*f
        self.assertEqual(B.subs(x, 0), 1)
        self.assertEqual(sp.rem(B-1, x*x, x), x*f)

    def test_finite_inverse_constructs_constant_residue_base_slices(self):
        x, y, z, f = sp.symbols("x y z f")
        P = 2+x*(y*y+1)+x*x*y
        Q = 2*y+x*(y**3/3+y)+x*x*y*y/2
        H = sp.cancel((Q-2*y)/x)
        for n in range(1, 5):
            I = -f/2
            for _ in range(n-1):
                I = sp.rem(sp.expand(-f/2-x*H.subs(y, I)/2), x**n, x)
            F = x**n*z-Q
            numerator = sp.expand(y-I.subs(f, F))
            quotient, remainder = sp.div(numerator, x**n, x)
            self.assertZero(remainder)
            self.assertZero(apply((0, x**n, P), quotient, (x,y,z))-1)

    def test_common_factor_replica_keeps_the_affine_certificate(self):
        x, y, z, t = coords = sp.symbols("x y z t")
        n, e = 2, 3
        F = x**n*z-y*y/2
        A, B = 1, 1+x*F
        m = n+e
        U = (-1)**m*F**m
        V = sum((-x*F)**j for j in range(m))
        self.assertZero(x**m*U+B*V-1)
        self.assertZero(apply((0, x**m, x**e*y, B), U*y+V*t, coords)-1)

    def test_zero_second_coefficient_is_a_coordinate_replica(self):
        x, y, z, t = coords = sp.symbols("x y z t")
        for m in range(1, 5):
            B = 1+x**m*z
            self.assertZero(apply((0, x**m, 0, B), -z*y+t, coords)-1)

    def test_split_and_nonreduced_special_fibers(self):
        y = sp.Symbol("y")
        for n in range(2, 7):
            self.assertEqual(sp.degree(sp.gcd(y**n-1, n*y**(n-1)), y), 0)
            self.assertEqual(sp.degree(sp.gcd(y**n, n*y**(n-1)), y), n-1)
            self.assertNotEqual(sp.rem(y, y**n, y), 0)
            self.assertEqual(sp.rem(y**n, y**n, y), 0)

    def test_singular_coefficient_curve_normalization(self):
        q, x, f, y, z = sp.symbols("q x f y z")
        self.assertZero((f*f-x**3).subs({x:q*q, f:q**3}))
        relation = x*x*z-y*y-f
        pulled = sp.expand(relation.subs({x:q*q, f:q**3}))
        self.assertEqual(pulled.subs(q, 0), -y*y)
        self.assertNotEqual(sp.rem(y, y*y, y), 0)

    def test_image_recurrence_factorials(self):
        x, y, z, t, b = coords = sp.symbols("x y z t b")
        delta = (0, x, y, 0, 0)
        E = (0, x, y, b, 0)
        for n in range(2, 6):
            S = (b*y-x*t)**n
            self.assertZero(apply(E, S, coords))
            s0 = S.subs(t, 0)
            leading = sp.Poly(S, t).nth(n)
            self.assertZero(iterate(delta, s0, coords, n)
                            -(-1)**n*sp.factorial(n)*b**n*leading)

    def test_top_in_image_can_be_cancelled_by_polynomial_invariant(self):
        y, t, b = coords = sp.symbols("y t b")
        E = (1, b, 0)
        for n in range(2, 7):
            S = y+(b*y-t)**n
            c = (-1)**n
            h = c*y**n/sp.factorial(n)
            J = sum(b**(n-j)*(-t)**j*sp.diff(h, y, j)/sp.factorial(j)
                    for j in range(n+1))
            self.assertZero(apply(E, J, coords))
            reduced = sp.expand(S-(-1)**n*sp.factorial(n)*J)
            self.assertEqual(reduced, y)
            self.assertZero(apply(E, reduced, coords)-1)

    def test_torsion_obstruction_alone_does_not_produce_a_slice(self):
        x, y, t = coords = sp.symbols("x y t")
        for n in range(2, 6):
            self.assertEqual(sp.rem(x**n, x**n, x), 0)
            self.assertEqual(sp.rem(1, x**n, x), 1)
        E = (0, x, x)
        self.assertEqual(tuple(a.subs(x,0) if hasattr(a, 'subs') else a for a in E), (0,0,0))

    def test_invariant_multiplier_image_identity(self):
        x, y, z = coords = sp.symbols("x y z")
        D = (0, x, y)
        A = 1+2*x*z-y*y
        delta = tuple(A*a for a in D)
        self.assertZero(apply(D, A, coords))
        for n in range(1, 5):
            self.assertZero(iterate(delta, z**3, coords, n)
                            -A**n*iterate(D, z**3, coords, n))

    def test_affine_slice_changes_the_commuting_basis(self):
        a, b, g, h = sp.symbols("a b g h")
        relation = a*g+b*h-1
        matrix = sp.Matrix(((a,b),(h,-g)))
        inverse = sp.Matrix(((g,b),(h,-a)))
        residual = matrix*inverse-sp.eye(2)
        for i,j in itertools.product(range(2),repeat=2):
            self.assertZero(residual[i,j]-(relation if i==j else 0))

    def test_nodal_factorization_is_finite_and_exact(self):
        t, u, w = sp.symbols("t u w")
        relation = w*w-u*(u-1)**2
        self.assertZero(relation.subs({u:t*t, w:t*(t*t-1)}))
        self.assertEqual(sp.Poly(relation,w).LC(),1)
        # Monic degree two in w is the exact finite-module certificate over C[u].

    def test_deleted_normalization_branch_has_same_node(self):
        t = sp.Symbol("t")
        images = (t*t,t*(t*t-1))
        self.assertEqual(tuple(f.subs(t,1) for f in images),(1,0))
        self.assertEqual(tuple(f.subs(t,-1) for f in images),(1,0))
        self.assertEqual((t+1).subs(t,-1),0)
        self.assertNotEqual((t+1).subs(t,1),0)

    def test_generic_two_fibers_special_one_after_localization(self):
        t, inv = sp.symbols("t inv")
        special = sp.groebner([t*t-1,(t+1)*inv-1],inv,t)
        self.assertEqual(special.reduce(t-1)[1],0)
        self.assertEqual(special.reduce(2*inv-1)[1],0)
        generic = sp.groebner([t*t-4,(t+1)*inv-1],inv,t)
        self.assertNotEqual(generic.reduce(t-2)[1],0)
        self.assertNotEqual(generic.reduce(t+2)[1],0)
        self.assertEqual(generic.reduce((t-2)*(t+2))[1],0)

    def test_retained_branch_is_unramified_and_node_is_singular(self):
        t, u, w = sp.symbols("t u w")
        self.assertEqual(sp.diff(t*t,t).subs(t,1),2)
        relation = w*w-u*(u-1)**2
        self.assertEqual(sp.diff(relation,u).subs({u:1,w:0}),0)
        self.assertEqual(sp.diff(relation,w).subs({u:1,w:0}),0)

    def test_mixed_root_global_slice_and_distinct_bad_residues(self):
        x, y, z, t = coords = sp.symbols("x y z t")
        a = x*x*(x-1)**3
        h = x+1
        F = a*z-y-x*y*y/2
        I = -F-x*F*F/2
        r, remainder = sp.div(sp.expand(y-I), x*x, x)
        self.assertZero(remainder)
        g = h*(x-1)**3
        V, remainder = sp.div(sp.expand(g+1), x, x)
        self.assertZero(remainder)
        E = (0,h*a,h*(1+x*y),x)
        self.assertZero(apply(E,F,coords))
        self.assertZero(apply(E,r,coords)-g)
        self.assertZero(apply(E,-r+V*t,coords)-1)
        self.assertNotEqual(x.subs(x,1),x.subs(x,-1))
        self.assertEqual(g.subs(x,0),-1)

    def test_nonmonic_repeated_good_root_finite_inverse(self):
        x, y, z, f = sp.symbols("x y z f")
        q = x-2
        a = 3*q**3*(x+1)**2
        P = 2+q*y
        F = a*z-2*y-q*y*y/2
        I = -f/2
        for _ in range(2):
            I = sp.expand(-f/2-q*I*I/4)
        r, remainder = sp.div(sp.expand(y-I.subs(f,F)),q**3,x)
        self.assertZero(remainder)
        self.assertZero(apply((0,a,P),r,(x,y,z))-3*(x+1)**2)
        self.assertNotEqual((3*(x+1)**2).subs(x,2),0)

    def test_bad_root_pole_cancellation_degree_obstruction(self):
        y, f = sp.symbols("y f")
        for d in range(2,6):
            Q = y**d+y+1
            for i,j in itertools.product(range(4),repeat=2):
                G, H = f**i+2, f**j+3
                first, second = y*G.subs(f,-Q), H.subs(f,-Q)
                self.assertEqual(sp.degree(first,y)%d,1)
                self.assertEqual(sp.degree(second,y)%d,0)
                self.assertNotEqual(sp.expand(first+second),0)

    def test_good_root_witness_gcd_is_full_bad_plinth_factor(self):
        x = sp.Symbol("x")
        a = 7*x**3*(x-1)**2*(x+2)**4
        first = sp.cancel(a/x**3)
        second = sp.cancel(a/(x+2)**4)
        actual = sp.Poly(sp.gcd(sp.gcd(a,first),second),x).monic().as_expr()
        self.assertZero(actual-(x-1)**2)

    def test_localized_cubic_slice_is_an_exact_identity(self):
        x, y, z, t = coords = sp.symbols("x y z t")
        v = x*x*z-y*y
        E = (0,x*x,2*y,x)
        rho = y-x*t
        Z = z-t*t
        w = x*Z-2*rho*t
        N = -y*z+3*x*z*t-3*y*t*t+x*t**3
        self.assertZero(apply(E,v,coords))
        self.assertZero(apply(E,rho,coords))
        self.assertZero(apply(E,w,coords))
        self.assertZero(v-(x*w-rho*rho))
        self.assertZero(N-(2*w*t-rho*Z))
        self.assertZero(apply(E,N,coords)-2*v)
        # This is a slice only after v is inverted, not in the polynomial ring.
        self.assertNotEqual(sp.div(N,v,z)[1],0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
