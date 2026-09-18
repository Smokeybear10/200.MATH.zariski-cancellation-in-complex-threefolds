"""Independent finite controls for the two coefficient-field notes in pass213.

The ring recovery identities below are over a coefficient field. They are not
ambient polynomial coordinate changes or actual-frame realizations. Finite
fibers and degree enumerations do not prove monicity in general, conductor
theorems, the geometric odd-part argument, or original-ring recognition.
No retained checker or solver implementation is imported.
"""

import unittest

import sympy as s


class RankTwoCenterProjectionControls(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(s.cancel(s.expand(value)), 0)

    def test_monic_center_fibers_and_degree_pair_bounds(self):
        U, root0, root1 = s.symbols("U root0 root1")
        rho, leading = s.symbols("rho leading", nonzero=True)
        # Formal squarefree-center fibers with every possible root multiplicity
        # in its square, including a nonreduced block. No reduced-fiber premise.
        for roots in ((root0,), (root0, root1)):
            multiplicities = [(1,), (2,)] if len(roots) == 1 else [
                (i, j) for i in range(3) for j in range(3) if i + j > 0
            ]
            for powers in multiplicities:
                degree = sum(powers)
                selected = s.prod((U - root)**power for root, power in zip(roots, powers))
                cofactor = leading**2 / rho**3 * s.prod(
                    (U - root)**(2 - power) for root, power in zip(roots, powers)
                )
                center = leading * s.prod(U - root for root in roots)
                self.zero(selected * cofactor - center**2 / rho**3)
                self.assertEqual(s.Poly(selected, U).degree(), degree)
                self.zero(s.Poly(selected, U).LC() - 1)
                self.assertEqual(s.Poly(cofactor, U).degree(), 2 * len(roots) - degree)
                self.zero(s.Poly(cofactor, U).LC() - leading**2 / rho**3)
                blocks = [s.Matrix([[root]]) if power == 1
                          else s.Matrix([[root, 1], [0, root]])
                          for root, power in zip(roots, powers) if power]
                multiplication_y = s.diag(*blocks)
                self.zero((U * s.eye(degree) - multiplication_y).det() - selected)

        expected = {
            1: [(2, 1), (3, 1), (4, 1), (3, 2), (4, 2), (6, 2)],
            2: [(2, 1), (3, 2), (6, 4)],
        }
        for center_degree in (1, 2):
            allowed = []
            for d in range(2, 7):
                for e in range(1, min(d, 5)):
                    remainder_degree = 2 * center_degree - e
                    if remainder_degree < 0:
                        continue
                    # Do not apply the positive-U-degree argument when it is zero.
                    if remainder_degree > 0 and d > 5 - 2 * center_degree + e:
                        continue
                    if e > 1 and s.igcd(d, e) == 1 and (d - 1) * (e - 1) > e:
                        continue
                    allowed.append((d, e))
            self.assertEqual(sorted(allowed), sorted(expected[center_degree]))
        self.assertIn((6, 2), expected[1])
        self.assertIn((6, 4), expected[2])

    def test_exact_division_and_projected_ring_recovery(self):
        rho, B1 = s.symbols("rho B1", nonzero=True)
        U, V, U0, kr, ktr, krr, nr, ktt = s.symbols("U V U0 kr ktr krr nr ktt")
        Vc = -rho**3 * kr / 2
        R = 2 * (V - Vc) / rho**3
        phi = -V**3 / rho**4 + krr * V**2 / 2 + nr * V
        nt = B1 - ktr * Vc
        S = ktr * U * V + nt * U + phi
        ell = B1 * U0 + phi.subs(V, Vc)
        self.zero(s.Poly((S + ktt * U**2 / 2).subs(V, Vc), U).coeff_monomial(U**2) - ktt / 2)
        self.zero(S.subs(V, Vc) - ell - B1 * (U - U0))
        alpha = -rho**3 * ktr / 2
        D0 = (V**2 + V * Vc + Vc**2) / (2 * rho)
        D0 -= rho**3 * krr * (V + Vc) / 4 + rho**3 * nr / 2
        D = alpha * U + D0
        self.zero(R * D0 + phi - phi.subs(V, Vc))
        self.zero(S - ell - B1 * (U - U0) + R * D)
        self.assertLessEqual(s.Poly(s.expand(D0), V).degree(), 2)

        y, w, wt = s.symbols("y w wt")
        shifted = w - alpha * y - D0
        first = R * w + S.subs(U, y) - ell
        self.zero(first - (R * shifted + B1 * (y - U0)))
        recovered_y = U0 - R * wt / B1
        recovered_w = wt + alpha * recovered_y + D0
        self.zero(recovered_w - alpha * recovered_y - D0 - wt)
        self.zero(first.subs({y: recovered_y, w: recovered_w}, simultaneous=True))
        self.zero(U0 - R * shifted / B1 - y + first / B1)

        # After the written odd-part gate, the recovery uses only field units.
        A2, b1 = s.symbols("A2 b1", nonzero=True)
        x, c0 = s.symbols("x c0")
        theta = A2 * x**2 + c0
        projected_R = R.subs(V, theta)
        P = s.Function("P")(theta)
        shifted_w = P + b1 * x
        projected_y = U0 - projected_R * shifted_w / B1
        self.zero((shifted_w - P) / b1 - x)
        self.zero(-(B1 / b1) * (projected_y - U0) - projected_R * P / b1 - projected_R * x)
        r = 2 * A2 / rho**3
        c1 = (2 * c0 / rho**3 + kr) / r
        self.zero(projected_R - r * (x**2 + c1))

    def test_even_odd_conductor_and_node_cusp_identities(self):
        x, z, c, U, V = s.symbols("x z c U V")
        odd_generator = x**3 + c * x
        relation = V**2 - U * (U + c)**2
        self.zero(relation.subs({U: x**2, V: odd_generator}, simultaneous=True))
        self.zero(odd_generator**2 - (z * (z + c)**2).subs(z, x**2))
        self.zero(relation.subs(c, 0) - (V**2 - U**3))
        h = s.symbols("h")
        self.zero(relation.subs(U, h - c) - (V**2 + c * h**2 - h**3))
        self.zero(s.hessian(relation, (U, V)).det().subs({U: -c, V: 0}, simultaneous=True) - 4 * c)

        ac, bc = s.symbols("a0:5"), s.symbols("b0:5")
        A = sum(coefficient * z**j for j, coefficient in enumerate(ac))
        B = sum(coefficient * z**j for j, coefficient in enumerate(bc))
        quotient = lambda coefficients: sum(
            coefficient * sum(z**(j - 1 - k) * (-c)**k for k in range(j))
            for j, coefficient in enumerate(coefficients) if j
        )
        QA, QB = quotient(ac), quotient(bc)
        self.zero(A - (z + c) * QA - A.subs(z, -c))
        self.zero(B - (z + c) * QB - B.subs(z, -c))
        polynomial = A.subs(z, x**2) + x * B.subs(z, x**2)
        self.zero(polynomial - A.subs(z, x**2) - odd_generator * QB.subs(z, x**2)
                  - x * B.subs(z, -c))
        self.zero(x * polynomial - (z * B).subs(z, x**2)
                  - odd_generator * QA.subs(z, x**2) - x * A.subs(z, -c))
        # Divisibility of both parity coefficients gives the conductor ideal.
        multiple = (x**2 + c) * (A.subs(z, x**2) + x * B.subs(z, x**2))
        self.zero(multiple - ((z + c) * A).subs(z, x**2) - odd_generator * B.subs(z, x**2))
        self.zero(x * multiple - odd_generator * A.subs(z, x**2)
                  - (z * (z + c) * B).subs(z, x**2))
        self.zero(multiple.subs(c, 0) - x**2 * polynomial.subs(c, 0))

    def test_projection_degrees_and_davenport_negative_control(self):
        x, c0, c1, U0, p0 = s.symbols("x c0 c1 U0 p0")
        A2, r, B1, b1, leading = s.symbols("A2 r B1 b1 leading", nonzero=True)
        theta, R = A2 * x**2 + c0, r * (x**2 + c1)
        cases = [(s.Integer(0), 0), (p0, 0)]
        variable = s.symbols("variable")
        for degree in (1, 2, 3):
            lower = s.symbols("p0:" + str(degree))
            polynomial = leading * variable**degree + sum(value * variable**j for j, value in enumerate(lower))
            cases.append((polynomial.subs(variable, theta), degree))
        for P, degree in cases:
            wt = P + b1 * x
            y = U0 - R * wt / B1
            expected_y = 3 if degree == 0 else 2 * degree + 2
            expected_w = 1 if degree == 0 else 2 * degree
            self.assertEqual(s.Poly(s.expand(y), x).degree(), expected_y)
            self.assertEqual(s.Poly(s.expand(wt), x).degree(), expected_w)
            self.assertEqual(expected_w, expected_y - 2)
            target = -r * b1 / B1 if degree == 0 else -r * leading * A2**degree / B1
            self.zero(s.Poly(s.expand(y), x).LC() - target)
        self.assertGreater(2 * 3 + 2, 6)

        # Formal cancellation example only, not an actual differential chart.
        theta_bad = x**4 + x
        y_bad = x**6 + s.Rational(3, 2) * x**3 + s.Rational(3, 8)
        residue = s.expand(y_bad**2 - theta_bad**3)
        self.zero(residue - x**3 / 8 - s.Rational(9, 64))
        self.assertEqual(s.Poly(y_bad, x).degree(), 6)
        self.assertEqual(s.Poly(theta_bad, x).degree(), 4)
        self.assertEqual(s.Poly(residue, x).degree(), 3)


if __name__ == "__main__":
    unittest.main()
