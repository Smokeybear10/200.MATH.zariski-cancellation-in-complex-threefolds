"""One finite filtration-control method, not a divisor classification.

Quadratic e=1,...,4 and j=0,...,8 checks are supplemented by finite
replica and cubic-cover contrasts. Exact module saturation for all j,
smoothness, actual conic generation and the original frame are not
certified by these finite computations.
"""

import math
import unittest

import sympy as sp


class QuadraticDivisorFiltrationChecks(unittest.TestCase):
    def test_conic_filtration_and_hypothesis_controls(self):
        p, s, r, t = sp.symbols("p s r t")

        for cover_degree in (2, 3):
            for e in range(1, 5):
                relation = p**e*t-r**cover_degree-s
                t_generic = (r**cover_degree+s)/p**e

                def reduction(expr):
                    return sp.Poly(sp.expand(expr), r).rem(
                        sp.Poly(r**cover_degree+s-p**e*t, r)
                    ).as_expr()

                def derivative(expr):
                    return reduction(
                        p**e*sp.diff(expr, r)
                        + cover_degree*r**(cover_degree-1)*sp.diff(expr, t)
                    )

                self.assertEqual(derivative(relation), 0)
                self.assertEqual(
                    reduction(p**e*t-r**cover_degree-s), 0
                )
                # The displayed unit s belongs to the derivative-value ideal.
                self.assertEqual(sp.expand(
                    t*p**e-(r/sp.Integer(cover_degree))
                    *(cover_degree*r**(cover_degree-1))-s-relation), 0)

                for j in range(9):
                    with self.subTest(cover=cover_degree, e=e, j=j):
                        basis = [
                            r**(degree % cover_degree)
                            * t**(degree // cover_degree)
                            for degree in range(j+1)
                        ]
                        generic_basis = [
                            sp.expand(term.subs(t, t_generic)) for term in basis
                        ]
                        coefficient_matrix = sp.Matrix([
                            [term.coeff(r, row) for term in generic_basis]
                            for row in range(j+1)
                        ])
                        expected_det_power = -e*sum(
                            degree//cover_degree for degree in range(j+1)
                        )
                        self.assertEqual(
                            sp.cancel(coefficient_matrix.det()
                                      -p**expected_det_power), 0
                        )
                        for degree, term in enumerate(basis):
                            current = term
                            for iteration in range(j+1):
                                if iteration == j:
                                    expected = (
                                        math.factorial(j)
                                        * p**(e*(j-j//cover_degree))
                                        if degree == j else 0
                                    )
                                    self.assertEqual(
                                        sp.expand(current-expected), 0
                                    )
                                current = derivative(current)
                            self.assertEqual(current, 0)

                        high = basis[-1]
                        generic_high = high.subs(t, t_generic)
                        expected = math.factorial(j)*p**(
                            e*(j-j//cover_degree)
                        )
                        self.assertEqual(sp.cancel(
                            p**(e*j)*sp.diff(generic_high, r, j)-expected
                        ), 0)

                        if cover_degree == 2:
                            expected_valuation = e*((j+1)//2)
                            self.assertEqual(
                                e*(j-j//2), expected_valuation
                            )
                            for replica_order in (1, 2):
                                replica_image = (
                                    p**(replica_order*j)*expected
                                )
                                self.assertEqual(
                                    sp.expand(replica_image
                                              -math.factorial(j)*p**(
                                                  replica_order*j
                                                  +expected_valuation)), 0
                                )

                residue_basis = [
                    r**(degree % cover_degree)
                    *t**(degree//cover_degree)
                    for degree in range(3)
                ]
                if cover_degree == 2:
                    self.assertEqual(residue_basis, [1, r, t])
                    self.assertEqual(sp.diff(residue_basis[-1], t), 1)
                else:
                    self.assertEqual(residue_basis, [1, r, r**2])
                    self.assertTrue(all(sp.diff(term, t) == 0
                                        for term in residue_basis))
                    self.assertEqual(e*(4-4//3), 3*e)
                    self.assertNotEqual(e*(4-4//3), e*((4+1)//2))

        # A nonsquare/noncube assertion is proved by valuations in the note,
        # not inferred from a numerical specialization or this finite suite.
        self.assertEqual(
            sp.Poly(r**2+s, r).degree(), 2
        )
        self.assertEqual(
            sp.Poly(r**3+s, r).degree(), 3
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

