#!/usr/bin/env python3
"""Independent exact controls for F=x^m*y+g(x,z,w).

Finite identities support, but do not replace, the written all-degree proof.
No imports from a research solver. SymPy is used over exact rationals.
"""

import unittest

import sympy as sp


x, y, z, w = sp.symbols("x y z w")
Y, Z = sp.symbols("Y Z")


def clean(value):
    return sp.cancel(sp.expand(value))


def truncated_inverse(h, m):
    """Inverse of h=z mod x in QQ[x,z,w], modulo x**m."""
    if m < 1 or clean(h.subs(x, 0)-z) != 0:
        raise ValueError("Requires m >= 1 and h(0,z,w)=z")
    result = Z
    for degree in range(1, m):
        error = sp.expand(h.subs(z, result)-Z).coeff(x, degree)
        result = sp.expand(result-x**degree*error)
    return result


def cubic_direction(h):
    """Exact two-unknown gate; rejects use beyond its proved degree scope."""
    if sp.Poly(h, z, w).total_degree() > 3:
        raise ValueError("The constant-direction equivalence is cubic only")
    alpha, beta = sp.symbols("alpha beta")
    equations = sp.Poly(alpha*sp.diff(h, z)+beta*sp.diff(h, w)-1, z, w).coeffs()
    return sp.linsolve(equations, (alpha, beta))


class LinearVariableTests(unittest.TestCase):
    def test_four_cubic_inverse_controls(self):
        for Q in (sp.Integer(7), z+w, z**2+z*w+w**2, z**3+z*w**2+w**4):
            F = z+x*Q+x**2*y
            Yf = clean(-y+(Q.subs(z, F)-Q)/x)
            zi = Z-x*Q.subs(z, Z)+x**2*Y
            yi = clean(-Y+(Q.subs(z, Z)-Q.subs(z, zi))/x)
            for expression, expected in ((zi, z), (yi, y)):
                self.assertEqual(clean(expression.subs(
                    {Y: Yf, Z: F}, simultaneous=True)-expected), 0)
            for expression, expected in ((F, Z), (Yf, Y)):
                self.assertEqual(clean(expression.subs(
                    {y: yi, z: zi}, simultaneous=True)-expected), 0)

    def test_truncated_inverse_both_orders(self):
        h = z+x*(z**2+w)+x**2*z*w
        for m in range(1, 6):
            inverse = truncated_inverse(h, m)
            for value in (h.subs(z, inverse)-Z,
                          inverse.subs(Z, h)-z):
                self.assertEqual(sp.rem(sp.expand(value), x**m, x), 0)

    def test_general_inverse_both_directions(self):
        for h, m in ((z+x*(z+w), 1),
                     (z+x*(z**2+w), 2),
                     (z+x*z**2+x**2*w, 3),
                     (z+x*w*z+x**2*(z+w), 4)):
            R = truncated_inverse(h, m)
            F = x**m*y+h
            Yf = clean((z-R.subs(Z, F))/x**m)
            zi = R+x**m*Y
            yi = clean((Z-h.subs(z, zi))/x**m)
            for expression in (Yf, zi, yi):
                self.assertFalse(sp.denom(clean(expression)).free_symbols)
            self.assertEqual(clean(zi.subs({Y: Yf, Z: F}, simultaneous=True)-z), 0)
            self.assertEqual(clean(yi.subs({Y: Yf, Z: F}, simultaneous=True)-y), 0)
            self.assertEqual(clean(F.subs({y: yi, z: zi}, simultaneous=True)-Z), 0)
            self.assertEqual(clean(Yf.subs({y: yi, z: zi}, simultaneous=True)-Y), 0)

    def test_explicit_slice_formula(self):
        Q = z**2+z*w+w**2
        F = z+x*Q+x**2*y
        Qz = sp.diff(Q, z)
        Dz = 1-x*Qz.subs(z, F)
        Dy = clean((Qz.subs(z, F)-Qz)/x+Qz*Qz.subs(z, F))
        self.assertEqual(clean(Dz*sp.diff(F, z)+Dy*sp.diff(F, y)), 1)
        Yf = clean(-y+(Q.subs(z, F)-Q)/x)
        self.assertEqual(clean(Dz*sp.diff(Yf, z)+Dy*sp.diff(Yf, y)), 0)

    def test_cubic_positive_direction_controls(self):
        for h in (z, z+w**2, z+w**3, 2*z+3*w**3,
                  z+w+(z-w)**3):
            self.assertNotEqual(cubic_direction(h), sp.EmptySet)

    def test_cubic_negative_direction_controls(self):
        for h in (sp.Integer(0), z*w, z**2+w**3, z**3, z*w**2+w):
            self.assertEqual(cubic_direction(h), sp.EmptySet)

    def test_high_degree_rejected_and_positive_coordinate_control(self):
        h = w+(z+w**2)**2
        with self.assertRaises(ValueError):
            cubic_direction(h)
        alpha, beta = sp.symbols("alpha beta")
        equations = sp.Poly(alpha*sp.diff(h, z)+beta*sp.diff(h, w)-1, z, w).coeffs()
        self.assertEqual(sp.linsolve(equations, (alpha, beta)), sp.EmptySet)
        # h and z+w² are coordinates despite the failed constant-direction gate.
        zi = Y-(Z-Y**2)**2
        wi = Z-Y**2
        self.assertEqual(clean(h.subs({z: zi, w: wi}, simultaneous=True)), Z)
        self.assertEqual(clean((z+w**2).subs({z: zi, w: wi}, simultaneous=True)), Y)

    def test_smooth_negative_control(self):
        F = x**2*y+x+z*w
        self.assertEqual(list(sp.groebner(
            [sp.diff(F, variable) for variable in (x, y, z, w)], x, y, z, w)), [1])
        self.assertEqual(cubic_direction(F.subs(x, 0)), sp.EmptySet)

    def test_bad_normalization_rejected(self):
        with self.assertRaises(ValueError):
            truncated_inverse(z**2+x*w, 2)
        with self.assertRaises(ValueError):
            truncated_inverse(z+x*w, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
