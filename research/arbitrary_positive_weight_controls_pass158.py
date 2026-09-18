"""Finite actual-family controls for arbitrary positive E-time weights158.

For r=2,3,5 the inverse-verified polynomial frame has weights (1,1,r,2)
and full initial kernel (Z-Y^r). All FOUR original coordinate partials
are recovered by differentiating the inverse, then checked on the forward
coordinates. Their shifts are (3,r+2,3,2); the occurring Y,Z pivots attain
the other-row degree maximum, while omitted X,W do not.

Independent partial iteration checks multiplicities one through three at
both pivots, with ordinary leading coefficients and factorials. The actual
translation frame (u,a,b,c) is a zero-weight boundary: its leading coefficient
field has transcendence degree three and its initial algebra has transcendence
degree four.

These finite controls do not prove the universal volume, leading-LND, growth
or wedge arguments, do not bound a minimum weight sum, and do not give an
entry or cancellation theorem. No previous checker or solver is imported;
the completed split-cubic checker158 is not changed or executed here.
"""

import math
import unittest

import sympy as sp


class ArbitraryPositiveWeightControls(unittest.TestCase):
    DEGREES = (2, 3, 5)

    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    @staticmethod
    def degree(expression, variable):
        return sp.Poly(sp.expand(expression), variable).degree()

    @staticmethod
    def deriv(expression, variables, coefficients):
        return sp.expand(sum(c*sp.diff(expression, v)
                             for v, c in zip(variables, coefficients)))

    @staticmethod
    def weighted_degree(expression, variables, weights):
        return max(sum(e*w for e, w in zip(exponents, weights))
                   for exponents, coefficient in sp.Poly(expression, *variables).terms())

    @staticmethod
    def frame(r):
        u, a, b, c = base = sp.symbols("u a b c")
        X, Y, Z, W = original = sp.symbols("X Y Z W")
        y0, z0 = a+b*u, b+c*u
        forward = (u, y0, z0+y0**r, c+u*z0)
        old_z = Z-Y**r
        inv_c = W-X*old_z
        inv_b = old_z-X*inv_c
        inverse = (X, Y-X*inv_b, inv_b, inv_c)
        return base, original, forward, inverse

    def test_actual_inverses_all_four_partials_and_projection_wedges(self):
        for r in self.DEGREES:
            with self.subTest(r=r):
                base, original, forward, inverse = self.frame(r)
                u, a, b, c = base
                X, Y, Z, W = original
                weights = (1, 1, r, 2)
                S = sum(weights)
                to_base = dict(zip(original, forward))
                to_original = dict(zip(base, inverse))
                for v, f in zip(base, inverse):
                    self.zero(f.xreplace(to_base)-v)
                for v, f in zip(original, forward):
                    self.zero(f.xreplace(to_original)-v)
                self.zero(sp.Matrix(forward).jacobian(base).det()-1)
                self.zero(sp.diff(u, u)-1)
                self.assertEqual(tuple(self.degree(f, u) for f in forward), weights)
                leading = tuple(sp.Poly(f, u).LC() for f in forward)
                self.assertEqual(leading, (1, b, b**r, c))
                for f, d, lc in zip(forward, weights, leading):
                    self.zero(sp.diff(f, u, d+1))
                    self.zero(sp.diff(f, u, d)-math.factorial(d)*lc)

                y0, z0 = a+b*u, b+c*u
                Ry = r*y0**(r-1)
                explicit = (
                    (1, -(1+u*u)*z0+2*u*c, u*z0-c, -z0),
                    (0, 1+u*(1+u*u)*Ry, -(1+u*u)*Ry, u*Ry),
                    (0, -u-u**3, 1+u*u, -u),
                    (0, u*u, -u, 1),
                )
                shifts = (3, r+2, 3, 2)
                tops = ((-c, 0, 0), (r*b**(r-1), 0, 0),
                        (-1, 0, 0), (1, 0, 0))
                eta = sp.symbols("eta")
                initials = tuple(lc*eta**d for lc, d in zip(leading, weights))
                F = Z-Y**r
                self.zero(F.xreplace(dict(zip(original, initials))))
                self.assertEqual(self.weighted_degree(F, original, weights), r)
                # Eliminating Z=Y^r leaves C[X,Y,W]. Its images recover
                # eta=X,b=Y/X,c=W/X² rationally, proving the full kernel (F).
                # The divisions here describe a fraction field, not an inverse
                # of the actual four-coordinate map, whose inverse is polynomial.
                independent = sp.Matrix((initials[0], initials[1], initials[3]))
                self.assertNotEqual(sp.expand(independent.jacobian((b, c, eta)).det()), 0)
                self.zero(sp.Matrix((leading[1], leading[3])).jacobian((b, c)).det()-1)

                for j, target in enumerate(original):
                    with self.subTest(r=r, partial=str(target)):
                        # Recover the actual partial from the inverse first.
                        coefficients = tuple(sp.expand(sp.diff(f, target).xreplace(to_base))
                                             for f in inverse)
                        for recovered, expected in zip(coefficients, explicit[j]):
                            self.zero(recovered-expected)
                        T = lambda f: self.deriv(f, base, coefficients)
                        for i, f in enumerate(forward):
                            self.zero(T(f)-int(i == j))
                        horizontal_degree = max(self.degree(f, u) for f in coefficients[1:])
                        self.assertEqual(horizontal_degree, shifts[j])
                        self.assertLessEqual(self.degree(coefficients[0], u), shifts[j])
                        self.assertEqual(max(horizontal_degree,
                                             self.degree(coefficients[0], u)-1), shifts[j])
                        self.assertLessEqual(shifts[j], S-weights[j]-1)
                        top = tuple(f.coeff(u, shifts[j]) for f in coefficients[1:])
                        self.assertEqual(top, tops[j])
                        for lc in leading:
                            self.zero(self.deriv(lc, base[1:], top))
                        # Each displayed N is a nonzero invariant multiple of
                        # partial_a, so it is locally nilpotent on C[a,b,c].
                        self.assertNotEqual(top[0], 0)
                        self.zero(sp.diff(top[0], a))

                        # Direct inverse derivatives verify finite generator
                        # nilpotence bounds, without expanding high iterates.
                        nilpotence_bound = (4, r+1, 2, 2)[j]
                        for f in inverse:
                            self.zero(sp.diff(f, target, nilpotence_bound))

                        other = [i for i in range(4) if i != j]
                        other_initials = sp.Matrix([initials[i] for i in other])
                        projection = sp.expand(other_initials.jacobian((b, c, eta)).det())
                        occurring = j in (1, 2)
                        self.assertEqual(projection != 0, occurring)
                        if occurring:
                            self.assertEqual(shifts[j], S-weights[j]-1)
                        else:
                            self.assertLessEqual(shifts[j], S-weights[j]-2)

                        # Independently form the mixed (db wedge dc) coefficient
                        # from the three leading coefficients and their weights.
                        l1, l2, l3 = [leading[i] for i in other]
                        w1, w2, w3 = [weights[i] for i in other]
                        minor = lambda f, g: sp.diff(f, b)*sp.diff(g, c)-sp.diff(f, c)*sp.diff(g, b)
                        mixed = (w3*l3*minor(l1, l2)-w2*l2*minor(l1, l3)
                                 +w1*l1*minor(l2, l3))
                        self.zero(projection-eta**(S-weights[j]-1)*mixed)
                        self.assertEqual(sp.expand(mixed) != 0, occurring)
                self.assertLessEqual(r, S-2)

    def test_actual_two_pivot_multiplicities_and_factorial_coefficients(self):
        for r in self.DEGREES:
            base, original, forward, inverse = self.frame(r)
            u, a, b, c = base
            X, Y, Z, W = original
            weights = (1, 1, r, 2)
            to_base = dict(zip(original, forward))
            F = Z-Y**r
            for ell in (1, 2, 3):
                P = F**ell*W+X
                M = self.weighted_degree(P, original, weights)
                self.assertEqual(M, r*ell+2)
                self.assertEqual(sp.rem(W, F, Z), W)
                actual = sp.expand(P.xreplace(to_base))
                self.zero(actual-((b+c*u)**ell*(c+u*(b+c*u))+u))
                self.assertEqual(self.degree(actual, u), ell+2)
                for j in (1, 2):
                    with self.subTest(r=r, multiplicity=ell, pivot=str(original[j])):
                        pivot = original[j]
                        coefficients = tuple(sp.expand(sp.diff(f, pivot).xreplace(to_base))
                                             for f in inverse)
                        T = lambda f: self.deriv(f, base, coefficients)
                        direct_source = sp.diff(P, pivot, ell)
                        residue = math.factorial(ell)*W*sp.diff(F, pivot)**ell
                        self.zero(sp.rem(direct_source-residue, F, Z))
                        transported = actual
                        for _ in range(ell):
                            transported = T(transported)
                        self.zero(transported-direct_source.xreplace(to_base))
                        self.assertEqual(self.degree(transported, u), M-weights[j]*ell)
                        expected_lc = math.factorial(ell)*c
                        if j == 1:
                            expected_lc *= (-r*b**(r-1))**ell
                        self.zero(sp.Poly(transported, u).LC()-expected_lc)
                        k = r+2 if j == 1 else 3
                        self.assertGreaterEqual(self.degree(actual, u), M-(weights[j]+k)*ell)
                        # The nonzero residue uses the FULL kernel (F), not
                        # merely one vanishing relation or a finite rank guess.

    def test_actual_zero_weight_boundary_breaks_leading_rank_claim(self):
        u, a, b, c = base = sp.symbols("u a b c")
        X, Y, Z, W = original = sp.symbols("X Y Z W")
        forward, inverse = base, original
        for v, f in zip(base, inverse):
            self.zero(f.xreplace(dict(zip(original, forward)))-v)
        for v, f in zip(original, forward):
            self.zero(f.xreplace(dict(zip(base, inverse)))-v)
        self.zero(sp.diff(u, u)-1)
        weights = tuple(self.degree(f, u) for f in forward)
        self.assertEqual(weights, (1, 0, 0, 0))
        leading = tuple(sp.Poly(f, u).LC() for f in forward)
        self.assertEqual(leading, (1, a, b, c))
        self.zero(sp.Matrix(leading[1:]).jacobian((a, b, c)).det()-1)
        eta = sp.symbols("eta")
        initials = sp.Matrix([lc*eta**d for lc, d in zip(leading, weights)])
        self.zero(initials.jacobian((eta, a, b, c)).det()-1)
        # Actual leading-field rank3 and initial-algebra rank4 are outside
        # the all-positive theorem, not counterexamples to its conclusions.
        for v in (a, b, c):
            self.zero(sp.diff(v, u))
        self.assertEqual(self.degree(sp.diff(u, u), u)-1, -1)
        # T_X is purely vertical with shift -1, while T_Y=partial_a has
        # horizontal shift0 and does NOT kill the leading coefficient of Y.
        self.zero(sp.diff(leading[1], a)-1)


if __name__ == "__main__":
    unittest.main()
