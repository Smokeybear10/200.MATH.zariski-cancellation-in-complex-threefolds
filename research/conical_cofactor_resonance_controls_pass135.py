"""Finite exact controls for the conical cofactor calculations in pass135.

The lower b/c derivatives are independent formal jets. No unit Jacobian,
integrability, polynomial inverse, or actual four-coordinate realization is
asserted for them. We compute adjugate numerators, not a coordinate partial
obtained by dividing by a possibly nonconstant formal determinant.

The quadratic parametrization a=(s**2, s*t, t**2) has radial derivation
R=(s*d_s+t*d_t)/2. Generic quartic and quadratic accelerations illustrate
resonance and mismatch, respectively. These examples do not prove the
entire-kernel, multiplicity/growth, or universal adjoint theorems. The final
method records why the actual local-nilpotence hypothesis cannot be replaced
by a horizontal coefficient bound. No earlier checker or search is imported.
"""

import unittest

import sympy as sp


def formal_frame():
    """Return a Jacobian-shaped jet matrix with column order (s,t,v,u)."""
    s, t, u = sp.symbols("s t u")
    q, qs, qt = sp.symbols("q qs qt")
    bs = sp.Matrix(sp.symbols("bs1:4"))
    bt = sp.Matrix(sp.symbols("bt1:4"))
    bv = sp.Matrix(sp.symbols("bv1:4"))
    c0s, c1s, c0t, c1t, c0v, c1v, c1 = sp.symbols(
        "c0s c1s c0t c1t c0v c1v c1"
    )
    a = sp.Matrix([s**2, s*t, t**2])
    good = sp.Matrix.hstack(bs + u*a.diff(s), bt + u*a.diff(t), bv, a)
    bad = sp.Matrix([[
        c0s + c1s*u + qs*u**2/2,
        c0t + c1t*u + qt*u**2/2,
        c0v + c1v*u,
        c1 + q*u,
    ]])
    return good.col_join(bad), (s, t, u), (q, qs, qt), a, bv, c1v


def inverse_numerators(matrix):
    """Cramer's signed minors: row = input direction, column = output partial."""
    return sp.Matrix(4, 4, lambda k, j: sp.expand(
        (-1)**(j+k) * matrix.minor_submatrix(j, k).det()
    ))


class ConicalCofactorResonanceControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_independent_jets_and_signed_radial_defect(self):
        matrix, (s, t, u), (q, qs, qt), a, bv, c1v = formal_frame()
        cof = inverse_numerators(matrix)
        normal = sp.Matrix([t**2, -2*s*t, s**2])
        defect = 2*q - (s*qs + t*qt)/2
        self.assert_zero(a[0]*a[2] - a[1]**2)
        self.assertEqual(a.diff(s).cross(a.diff(t)), 2*normal)
        self.assertEqual(a, (s*a.diff(s) + t*a.diff(t))/2)

        for j in range(3):
            # Only the v-direction numerator can have a cubic horizontal term.
            for k in (0, 1):
                self.assertLessEqual(sp.Poly(cof[k, j], u).degree(), 2)
            self.assertLessEqual(sp.Poly(cof[2, j], u).degree(), 3)
            self.assertLessEqual(sp.Poly(cof[3, j], u).degree(), 3)
            cubic_v = sp.Poly(cof[2, j], u).coeff_monomial(u**3)
            self.assert_zero(cubic_v - normal[j]*defect)

            # A cubic slice coefficient is NOT removed by these jet identities.
            cubic_slice = sp.Poly(cof[3, j], u).coeff_monomial(u**3)
            self.assert_zero(sp.diff(cubic_slice, c1v) + 2*normal[j])

        # The bad partial has horizontal degree <=1 before any vertical LND step.
        for k in range(3):
            self.assertLessEqual(sp.Poly(cof[k, 3], u).degree(), 1)
        self.assertLessEqual(sp.Poly(cof[3, 3], u).degree(), 2)
        quadratic_slice = sp.Poly(cof[3, 3], u).coeff_monomial(u**2)
        self.assert_zero(quadratic_slice - 2*normal.dot(bv))
        self.assertNotEqual(sp.expand(quadratic_slice), 0)

    def test_quartic_resonance_quadratic_mismatch_and_initial_maps(self):
        matrix, (s, t, u), (q, qs, qt), a, _, _ = formal_frame()
        cof = inverse_numerators(matrix)
        eta = sp.Symbol("eta")
        c40, c31, c22, c13, c04 = sp.symbols("c40 c31 c22 c13 c04")
        d20, d11, d02 = sp.symbols("d20 d11 d02")
        q4 = c40*s**4 + c31*s**3*t + c22*s**2*t**2 + c13*s*t**3 + c04*t**4
        q2 = d20*s**2 + d11*s*t + d02*t**2
        radial = lambda f: sp.expand((s*sp.diff(f, s) + t*sp.diff(f, t))/2)
        self.assert_zero(radial(q4) - 2*q4)
        self.assert_zero(radial(q2) - q2)

        for acceleration, degree_bound in ((q4, 2), (q2, 3)):
            substitution = {q: acceleration, qs: sp.diff(acceleration, s),
                            qt: sp.diff(acceleration, t)}
            for j in range(3):
                specialized = sp.expand(cof[2, j].subs(substitution))
                self.assertLessEqual(sp.Poly(specialized, u).degree(), degree_bound)
                if acceleration == q2:
                    self.assertEqual(sp.Poly(specialized, u).degree(), 3)

            # A single explicit Jacobian minor detects the two finite rank cases.
            initials = sp.Matrix([eta*a[0], eta*a[1], eta**2*acceleration/2])
            minor = initials.jacobian([s, t, eta]).det()
            self.assert_zero(minor - eta**3*s**2*(2*acceleration-radial(acceleration)))
            if acceleration == q4:
                self.assert_zero(minor)
            else:
                self.assertNotEqual(sp.expand(minor), 0)

        # Resonance has an additional initial relation in this explicit family.
        x1, x2, x3, z = sp.symbols("x1 x2 x3 z")
        quartic_in_speeds = (c40*x1**2 + c31*x1*x2 + c22*x1*x3
                            + c13*x2*x3 + c04*x3**2)
        relation = z - quartic_in_speeds/2
        evaluation = {x1: eta*a[0], x2: eta*a[1], x3: eta*a[2], z: eta**2*q4/2}
        self.assert_zero(relation.subs(evaluation, simultaneous=True))
        self.assert_zero((x1*x3-x2**2).subs(evaluation, simultaneous=True))
        # This finite minor is nonzero, so the resonant image is not rank one.
        self.assert_zero(sp.Matrix([eta*a[0], eta*a[1]]).jacobian([s, t]).det()
                         - 2*eta**2*s**2)

    def test_vertical_divisibility_requires_local_nilpotence(self):
        s, t, v, u = sp.symbols("s t v u")
        bad_derivation = lambda f: sp.expand(u**3*sp.diff(f, u))
        for invariant_generator in (s, t, v):
            self.assert_zero(bad_derivation(invariant_generator))
        self.assert_zero(bad_derivation(u) - u**3)

        # D=u^3*d_u is not LND: the recurrence gives nonzero odd double factorials.
        # The loop checks only six terms of that explicitly stated recurrence.
        iterate, coefficient = u, 1
        for k in range(1, 7):
            iterate = bad_derivation(iterate)
            coefficient *= 2*k - 1
            self.assert_zero(iterate - coefficient*u**(2*k+1))
            self.assertNotEqual(iterate, 0)

        # In contrast, the triangular LND u^2*d_v has zero vertical coefficient.
        triangular = lambda f: sp.expand(u**2*sp.diff(f, v))
        self.assert_zero(triangular(u))
        self.assert_zero(triangular(v) - u**2)
        self.assert_zero(triangular(triangular(v)))


if __name__ == "__main__":
    unittest.main()
