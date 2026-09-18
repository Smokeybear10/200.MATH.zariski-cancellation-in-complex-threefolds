"""Bounded identities for repeated-smooth-support-pass48.md.

No test here proves compact-cohomology, monodromy, nonpolynomiality,
or the existence of a polynomial cylinder for the Russell cubic.
"""

import unittest

import sympy as sp


class RepeatedSmoothSupportChecks(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(sp.cancel(sp.expand(value)), 0)

    def test_normalization_branch_fibers_and_cusp_smoothness_gate(self):
        v, r, w, x, y = sp.symbols("v r w x y")
        b = sp.Integer(3)
        h = (v - b)**2 * (v - 4) * (v - 7)**2
        d = 4 * (v - b) * h**2
        parametrization = {
            v: b + w**2,
            r: 2 * sp.I * w * h.subs(v, b + w**2),
        }
        self.zero((r**2 + d).subs(parametrization, simultaneous=True))
        self.zero(
            (r / (2 * sp.I * h)).subs(
                parametrization, simultaneous=True
            ) - w
        )
        self.zero(
            ((r / (2 * sp.I * h))**2 - (v - b))
            + (r**2 + d) / (4 * h**2)
        )
        # Two distinct pairs collapse at two off-branch roots of h.
        for positive, residue in ((1, 4), (2, 7)):
            plus = [f.subs(w, positive) for f in parametrization.values()]
            minus = [f.subs(w, -positive) for f in parametrization.values()]
            self.assertEqual(plus, [residue, 0])
            self.assertEqual(minus, plus)
        self.assertEqual(sp.degree(sp.gcd(h, sp.diff(h, v)), v), 2)
        roots_away = [
            factor for factor, _ in sp.factor_list(h, v)[1]
            if factor.subs(v, b) != 0
        ]
        self.assertEqual(len(roots_away), 2)
        self.assertEqual(parametrization[v].subs(w, 0), b)
        self.assertEqual(parametrization[r].subs(w, 0), 0)
        self.assertNotEqual(parametrization[r].subs(w, 3), 0)

        for cusp in (3, 5, 7):
            for multiplicity in (1, 2, 4):
                with self.subTest(cusp=cusp, multiplicity=multiplicity):
                    equation = x**multiplicity * y - r**2 - x - v**cusp
                    gradient = [sp.diff(equation, q)
                                for q in (x, v, r, y)]
                    fiber = {x: 0, v: 0, r: 0}
                    self.zero(equation.subs(fiber))
                    if multiplicity == 1:
                        for entry in gradient:
                            self.zero(entry.subs({**fiber, y: 1}))
                    else:
                        self.assertEqual(gradient[0].subs(fiber), -1)
                        for entry in gradient[1:]:
                            self.zero(entry.subs(fiber))
            # A pure odd-power cusp has only the one normalization preimage.
            self.zero(
                (r**2 + v**cusp).subs(
                    {v: -w**2, r: w**cusp}, simultaneous=True
                )
            )

    def test_actual_russell_action_and_bounded_adapted_filtration(self):
        x, v, r, y, s, t = sp.symbols("x v r y s t")
        p = x**2
        equation = p * y - r**2 - x - v**3

        def deriv(f):
            return sp.expand(p * sp.diff(f, r) + 2 * r * sp.diff(f, y))

        def flow(time):
            return {r: r + p * time,
                    y: y + 2 * r * time + p * time**2}

        self.zero(deriv(equation))
        self.zero(deriv(r) - p)
        self.zero(deriv(y) - 2 * r)
        self.zero(deriv(deriv(y)) - 2 * p)
        self.zero(deriv(deriv(deriv(y))))
        self.zero(equation.subs(flow(s), simultaneous=True) - equation)
        for generator in (r, y):
            self.zero(
                flow(s)[generator].subs(flow(t), simultaneous=True)
                - flow(s + t)[generator]
            )
            self.zero(
                flow(s)[generator].subs(flow(-s), simultaneous=True)
                - generator
            )

        local_y = (r**2 + x + v**3) / p
        basis = [
            sp.expand(r**(n % 2) * local_y**(n // 2))
            for n in range(9)
        ]
        for n, member in enumerate(basis):
            with self.subTest(n=n):
                poly = sp.Poly(member, r)
                self.assertEqual(poly.degree(), n)
                self.zero(poly.LC() - p**(-(n // 2)))
                self.zero(p**n * sp.diff(member, r, n)
                          - sp.factorial(n) * p**((n + 1) // 2))
                self.zero(sp.diff(member, r, n + 1))
                for lower in basis[:n]:
                    self.zero(sp.diff(lower, r, n))
        # Actual monic presentation: no vector-space relation is inferred
        # solely from the localization; the written proof uses its global basis.
        self.assertEqual(sp.Poly(equation, r).LC(), -1)
        self.zero(equation.subs(y, local_y))


if __name__ == "__main__":
    unittest.main(verbosity=2)

