"""Finite exact controls for the split projection-completion arguments in 175.

The independent coefficient jets below check polynomial elimination, its
prior-relation gradient substitutions, and a denominator-free determinant
calibration.  The cone controls check reconstruction and collision identities
in the low-degree cases of the written proof.  The nodal example is an abstract
polynomial parametrization, not an actual calibrated split-cubic frame.

These checks do not prove universal factorization, faithful field descent,
normality, a plane-completion theorem, or recognition of a fourfold.  In
particular they never assume that a nonzero R is a unit on the whole line.
No earlier checker is imported.  Canonical execution belongs to Root after
complete saved-source review.
"""

import unittest

import sympy as sp


class SplitProjectionCompletionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_cleared_quartic_gradient_and_independent_rows(self):
        U, V, S, r = sp.symbols("U V S r")
        k20, k11, k02, k30, k21, k12, k03 = sp.symbols(
            "k20 k11 k02 k30 k21 k12 k03"
        )
        n10, n01, n20, n11, n02 = sp.symbols("n10 n01 n20 n11 n02")
        ell, ell_t, ell_r, m = sp.symbols("ell ell_t ell_r m")
        f = (
            k20 * U**2 / 2 + k11 * U * V + k02 * V**2 / 2
            + n10 * U + n01 * V
        )
        g3 = (
            k30 * U**3 / 6 + k21 * U**2 * V / 2
            + k12 * U * V**2 / 2 + k03 * V**3 / 6
            + n20 * U**2 / 2 + n11 * U * V + n02 * V**2 / 2
        )
        # Independent coefficient jets, with formal U,V,S held fixed.
        f_t = k30 * U**2 / 2 + k21 * U * V + k12 * V**2 / 2 + n20 * U + n11 * V
        f_r = k21 * U**2 / 2 + k12 * U * V + k03 * V**2 / 2 + n11 * U + n02 * V
        self.zero(sp.diff(g3, U) - f_t)
        self.zero(sp.diff(g3, V) - f_r)
        R = r - U
        A, B = sp.diff(f, V), sp.diff(f, U) - S
        Ct, Cr = f_t + k11 * S - ell_t, f_r + k02 * S - ell_r
        P = R * S + f - ell
        Psi = A * S + g3 - ell_t * U - ell_r * V
        H = R * (g3 - ell_t * U - ell_r * V - m) + A * (ell - f)
        self.zero(H - (R * (Psi - m) - A * P))
        self.assertEqual(sp.Poly(H, U, V).total_degree(), 4)
        for actual, expected in zip(
            (sp.diff(P, U), sp.diff(P, V), sp.diff(P, S)),
            (B, A, R),
        ):
            self.zero(actual - expected)
        for actual, expected in zip(
            (sp.diff(Psi, U), sp.diff(Psi, V), sp.diff(Psi, S)),
            (Ct, Cr, A),
        ):
            self.zero(actual - expected)

        # These raw errors exhibit the exact prior relations required for
        # the shortened gradient formula; they are not silently set to zero.
        HU, HV = sp.diff(H, U), sp.diff(H, V)
        self.zero(HU - (R * Ct - A * B) + (Psi - m) + k11 * P)
        self.zero(HV - (R * Cr - A**2) + k02 * P)
        prior = {ell: R * S + f, m: Psi}
        for expression in (P, Psi - m, H, HU - R * Ct + A * B, HV - R * Cr + A**2):
            self.zero(expression.subs(prior, simultaneous=True))

        # Separate, unrestricted differential rows.  The numerator row dw_num
        # is R*dw after differentiating P=0 in all three directions.  No inverse
        # of R, denominator cancellation, or relation on the other rows is used.
        R0, A0, B0, C0, C1 = sp.symbols("R0 A0 B0 C0 C1")
        yt, yr, yv, vt, vr, vv = sp.symbols("yt yr yv vt vr vv")
        wt, wr, wv = sp.symbols("wt wr wv")
        dy, dv, dw = sp.Matrix([[yt, yr, yv]]), sp.Matrix([[vt, vr, vv]]), sp.Matrix([[wt, wr, wv]])
        dt, dr = sp.Matrix([[1, 0, 0]]), sp.Matrix([[0, 1, 0]])
        middle = R0 * dv + B0 * dt + A0 * dr
        dw_num = -B0 * dy - A0 * dv - C0 * dt - C1 * dr
        raw_det = sp.Matrix.vstack(dy, middle, dw).det()
        # Explicit cleared substitutions for the three entries of R*dw.
        rw_slots = sp.symbols("R_wt R_wr R_wv")
        linear_slots = sum(
            sp.diff(raw_det, slot) * rw_slot
            for slot, rw_slot in zip((wt, wr, wv), rw_slots)
        )
        self.zero(linear_slots.subs(
            dict(zip(rw_slots, (R0 * wt, R0 * wr, R0 * wv))),
            simultaneous=True,
        ) - R0 * raw_det)
        prior_det = linear_slots.subs(
            dict(zip(rw_slots, tuple(dw_num))), simultaneous=True
        )
        self.zero(prior_det - sp.Matrix.vstack(dy, middle, dw_num).det())
        CU = R0 * (vr * yv - yr * vv) + A0 * yv
        CV = R0 * (yt * vv - vt * yv) - B0 * yv
        self.zero(R0 * prior_det - CU * (R0 * C0 - A0 * B0) - CV * (R0 * C1 - A0**2))
        # A zero of R is allowed in this polynomial identity, but the identity
        # alone is not a determinant nonvanishing assertion at that zero.
        self.zero((R0 * prior_det - CU * (R0 * C0 - A0 * B0) - CV * (R0 * C1 - A0**2)).subs(R0, 0))

    def test_low_degree_square_factor_reconstruction_and_collisions(self):
        x, root = sp.symbols("x root", nonzero=True)
        b0, b1, b2, b3, c, a0, a1, a2, lam = sp.symbols(
            "b0 b1 b2 b3 c a0 a1 a2 lam", nonzero=True
        )

        def cone(a, b):
            triple = (a**2, a * b, b**2)
            self.zero(triple[0] * triple[2] - triple[1] ** 2)
            return triple

        # Degree(a)=0: only the displayed unit c is divided out in the proof.
        P, Q, S = cone(c, x)
        self.zero(Q - c * x)
        self.zero(Q**2 - P * S)

        # Degree(a)=1, no even quadratic term in b: exact reconstruction.
        b = b0 + b1 * x + b3 * x**3
        P, Q, S = cone(x, b)
        self.assertEqual((sp.degree(P, x), sp.degree(Q, x)), (2, 4))
        self.zero(b0 * x - (Q - b1 * P - b3 * P**2))
        # A polynomial Bezout certificate also certifies the vertex-free
        # condition for this family, using b=x*(b1+b3*x^2)+b0.
        q = b1 + b3 * x**2
        self.zero(S - 2 * q * Q + q**2 * P - b0**2)

        # If the quadratic even term survives, root^2=-b0/b2 supplies the
        # two-point collision.  This is its exact numerator identity, not
        # a finite proof of the algebraically closed square-root step.
        b = -b2 * root**2 + b1 * x + b2 * x**2 + b3 * x**3
        for coordinate in cone(x, b):
            self.zero(coordinate.subs(x, root) - coordinate.subs(x, -root))

        # Degree(a)=2, degree(b)=0 cannot recover an affine parameter.
        P, Q, S = cone(a2 * x**2 + a1 * x + a0, c)
        self.assertEqual((sp.degree(P, x), sp.degree(Q, x), sp.degree(S, x)), (4, 2, 0))

        # Degree(a)=2, degree(b)=1: the analogous distinct-point collision.
        a = a2 * x**2 + a1 * x - a2 * root**2
        linear_triple = cone(a, x)
        for coordinate in linear_triple:
            self.zero(coordinate.subs(x, root) - coordinate.subs(x, -root))

        # Degree(a)=degree(b)=2 reduces to the preceding case by b=lam*a+x.
        P, Q, S = cone(a, lam * a + x)
        self.zero(Q - lam * P - a * x)
        self.zero(S - 2 * lam * Q + lam**2 * P - x**2)
        self.zero(Q - (lam * linear_triple[0] + linear_triple[1]))
        self.zero(S - (lam**2 * linear_triple[0] + 2 * lam * linear_triple[1] + linear_triple[2]))
        for coordinate in (P, Q, S):
            self.zero(coordinate.subs(x, root) - coordinate.subs(x, -root))

    def test_vertex_gradient_and_nodal_scope_boundary(self):
        U, V, W, r, v0, kap, d0, d1, d2 = sp.symbols("U V W r v0 kap d0 d1 d2")
        D = d0 + d1 * U + d2 * V
        P, Q = r - U, V - v0
        Snum = -(W - D)  # kap*Scone; kap is nonzero in the cone proof.
        potential = P * (W - D) + kap * Q**2
        self.zero(P * Snum - kap * Q**2 + potential)
        gradient = (sp.diff(potential, U), sp.diff(potential, V), sp.diff(potential, W))
        expected = (-(W - D) - P * d1, 2 * kap * Q - P * d2, P)
        for actual, target in zip(gradient, expected):
            self.zero(actual - target)
        # Evaluation follows differentiation.  No moving-root derivatives.
        vertex = {U: r, V: v0, W: d0 + d1 * r + d2 * v0}
        for entry in gradient:
            self.zero(entry.subs(vertex, simultaneous=True))
        # The affine cone-coordinate formulas have both polynomial inverse
        # orders over the coefficient field with kap != 0.
        p, q, s = sp.symbols("p q s")
        backward = {U: r - p, V: v0 + q, W: d0 + d1 * (r - p) + d2 * (v0 + q) - kap * s}
        forward = {p: P, q: Q, s: Snum / kap}
        for expr, target in zip((P, Q, Snum / kap), (p, q, s)):
            self.zero(expr.subs(backward, simultaneous=True) - target)
        for expr, target in zip((backward[U], backward[V], backward[W]), (U, V, W)):
            self.zero(expr.subs(forward, simultaneous=True) - target)

        # Abstract nodal normalization: the full triple contains v, but the
        # first two entries identify v=0 and v=1 and meet the cone vertex.
        v, PP, QQ = sp.symbols("v PP QQ")
        Pn, Qn, Sn = v * (v - 1)**2, v * (v - 1), v
        self.zero(Pn * Sn - Qn**2)
        self.assertEqual((sp.degree(Pn, v), sp.degree(Qn, v)), (3, 2))
        self.zero(Sn - v)
        for entry in (Pn, Qn):
            self.zero(entry.subs(v, 0) - entry.subs(v, 1))
        for entry in (Pn, Qn, Sn):
            self.zero(entry.subs(v, 0))
        self.assertNotEqual(Sn.subs(v, 0), Sn.subs(v, 1))
        relation = QQ**3 - PP * QQ - PP**2
        self.zero(relation.subs({PP: Pn, QQ: Qn}, simultaneous=True))
        self.zero(Qn * v - Pn - Qn)  # birational return after inverting Qn.
        self.zero(sp.diff(relation, PP).subs({PP: 0, QQ: 0}))
        self.zero(sp.diff(relation, QQ).subs({PP: 0, QQ: 0}))
        quadratic_part = sum(
            coefficient * PP**i * QQ**j
            for (i, j), coefficient in sp.Poly(relation, PP, QQ).terms()
            if i + j == 2
        )
        self.zero(quadratic_part + PP * (PP + QQ))


if __name__ == "__main__":
    unittest.main()
