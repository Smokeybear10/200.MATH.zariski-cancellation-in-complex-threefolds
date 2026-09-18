"""Actual inverse/gradient controls; all-coefficient existence is proved in prose."""

import unittest

import sympy as S


class ProjectedGeneratorExtractionControls(unittest.TestCase):
    def test_actual_inverse_projection_and_critical_curve(self):
        s, a, b, c = S.symbols("s a b c")
        x0, x1, x2, x3 = S.symbols("x0 x1 x2 x3")
        source = (s, a, b, c)
        target = (x0, x1, x2, x3)

        def F(aa, bb, cc):
            return aa**2 / 2 + bb**3 / 3 + cc**5 / 5

        first = s + F(a, b, c)
        forward = (first, a + first**2, b + first**3, c + first**4)
        aa, bb, cc = x1 - x0**2, x2 - x0**3, x3 - x0**4
        inverse = (x0 - F(aa, bb, cc), aa, bb, cc)
        for expression, variable in zip(inverse, source):
            self.assertEqual(
                S.expand(expression.subs(dict(zip(target, forward)), simultaneous=True)
                         - variable), 0
            )
        for expression, variable in zip(forward, target):
            self.assertEqual(
                S.expand(expression.subs(dict(zip(source, inverse)), simultaneous=True)
                         - variable), 0
            )

        velocity = (1, 2 * first, 3 * first**2, 4 * first**3)
        for expression, expected in zip(forward, velocity):
            self.assertEqual(S.expand(S.diff(expression, s) - expected), 0)
        self.assertEqual(
            S.expand(sum(p * S.diff(inverse[0], x)
                         for p, x in zip((1, 2*x0, 3*x0**2, 4*x0**3), target)) - 1),
            0,
        )

        projected = tuple(expression.subs(s, 0) for expression in forward)
        f0, f1, f2, f3 = projected
        self.assertEqual(S.expand(f1 - f0**2 - a), 0)
        self.assertEqual(S.expand(f2 - f0**3 - b), 0)
        self.assertEqual(S.expand(f3 - f0**4 - c), 0)
        self.assertEqual([S.Poly(f, a, b, c).total_degree() for f in projected],
                         [5, 10, 15, 20])

        al0, al1, al2, al3, t, beta, gamma = S.symbols(
            "al0 al1 al2 al3 t beta gamma"
        )
        coefficients = (al0, al1, al2, al3)
        h = sum(alpha * f for alpha, f in zip(coefficients, projected))
        Tf = al0 + 2*al1*f0 + 3*al2*f0**2 + 4*al3*f0**3
        gradient = tuple(S.diff(h, v) for v in (a, b, c))
        expected = (al1 + a*Tf, al2 + b**2*Tf, al3 + c**4*Tf)
        for actual, claim in zip(gradient, expected):
            self.assertEqual(S.expand(actual - claim), 0)

        curve = {a: -al1*t**4, b: beta*t**2, c: gamma*t,
                 al2: -beta**2, al3: -gamma**4}
        Ft = al1**2*t**8/2 + beta**3*t**6/3 + gamma**5*t**5/5
        Tt = al0 + 2*al1*Ft - 3*beta**2*Ft**2 - 4*gamma**4*Ft**3
        common = 1 - t**4*Tt
        for derivative, coefficient in zip(gradient, (al1, -beta**2, -gamma**4)):
            self.assertEqual(
                S.expand(derivative.subs(curve, simultaneous=True) - coefficient*common),
                0,
            )
        self.assertEqual(common.subs(t, 0), 1)

        # One exact critical point, separately from the all-vector proof.
        particular = h.subs({al0: 0, al1: 1, al2: 0, al3: 0})
        self.assertEqual(
            [S.diff(particular, v).subs({a: -1, b: 0, c: 0}) for v in (a, b, c)],
            [0, 0, 0],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
