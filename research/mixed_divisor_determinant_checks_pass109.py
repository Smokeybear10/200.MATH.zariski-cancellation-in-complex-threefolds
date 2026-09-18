"""Two finite controls for pass109, not proofs of the universal geometry.

Method one checks the generic divided-conic determinant, shear identities,
and several affine DVR-basis determinants. It does not prove actual
divisibility, residue vanishing, or descent from all height-one primes.
Method two checks the retained actual frame and its two evaluation matrices.
The nonvanishing of arbitrarily long products is a separate written induction.
No weak/formal conic is asserted to be an actual original mixed frame.
"""

import unittest

import sympy as sp


class MixedDivisorDeterminantChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    @staticmethod
    def coefficient_matrix(polynomials, variable):
        return sp.Matrix([
            [sp.Poly(poly, variable).coeff_monomial(variable**j)
             for poly in polynomials]
            for j in range(len(polynomials))
        ])

    def test_divided_conic_and_divisor_basis_determinants(self):
        r, a, b, B1, P, eps, g0, delta, q = sp.symbols(
            "r a b B1 P eps g0 delta q")
        G = eps * b * r**2 / (2 * P) + B1 * r / P + g0
        H = (r - a * G) / b
        U = (eps * H**2 - 2 * delta * G - q) / B1
        candidates = [1, G, G**2, G * H, U]
        matrix = self.coefficient_matrix(candidates, r)
        determinant = matrix.det(method="domain-ge")
        self.assert_zero(determinant + eps**4 / (8 * P**4))

        # Two exact steps in the hand derivation, with all constants retained.
        h_square_matrix = self.coefficient_matrix([1, G, G**2, G * H, H**2], r)
        reduced_matrix = self.coefficient_matrix([1, G, G**2, r * G, r**2], r)
        hdet = h_square_matrix.det(method="domain-ge")
        rdet = reduced_matrix.det(method="domain-ge")
        self.assert_zero(determinant - eps * hdet / B1)
        self.assert_zero(hdet - rdet / b**3)
        self.assert_zero(rdet + (B1 / P) * (eps * b / (2 * P))**3)
        # A zero coefficient of G in r does not invalidate the algebraic
        # determinant. It is not claimed to be possible in the actual branch.
        self.assert_zero(determinant.subs(a, 0) + eps**4 / (8 * P**4))

        Gs, Hs, B2, v, u, beta, zeta = sp.symbols("Gs Hs B2 v u beta zeta")
        old_a = B1 * u + b * v
        old_r = old_a * Gs + b * Hs
        new_H = Hs + v * Gs
        new_B2 = B2 + v * B1
        old_Q = eps * old_r**2 - 2 * B2 * Gs + 2 * B1 * Hs
        new_Q = eps * old_r**2 - 2 * new_B2 * Gs + 2 * B1 * new_H
        self.assert_zero(old_r - (B1 * u * Gs + b * new_H))
        self.assert_zero(old_Q - new_Q)
        normalized_r = B1 * u * Gs + b * Hs
        conic = (eps * normalized_r**2
                 - 2 * (B1 * beta + b**2 * delta) * Gs + 2 * B1 * Hs
                 - (B1 * zeta + b**2 * q))
        divided_numerator = eps * Hs**2 - 2 * delta * Gs - q
        first_term = (eps * B1 * u**2 * Gs**2 + 2 * eps * u * b * Gs * Hs
                      - 2 * beta * Gs + 2 * Hs - zeta)
        self.assert_zero(conic - B1 * first_term - b**2 * divided_numerator)

        p, unit, shift, alpha, eta = sp.symbols("p unit shift alpha eta")
        local_r = (r - shift) / unit
        for e in (1, 2, 3):
            with self.subTest(divisor_exponent=e):
                local_t = (local_r**2 + alpha * local_r + eta) / p**e
                local_basis = [1, local_r, local_t, local_r * local_t, local_t**2]
                local_det = self.coefficient_matrix(local_basis, r).det()
                self.assert_zero(local_det - 1 / (p**(4 * e) * unit**10))
        slice_basis = [local_r**j for j in range(5)]
        self.assert_zero(self.coefficient_matrix(slice_basis, r).det() - unit**-10)

    def test_actual_frame_two_point_strong_nilpotence_failure(self):
        s, a, v, flow_p = sp.symbols("s a v flow_p")
        x1, x2, x3, z = sp.symbols("x1 x2 x3 z")
        coordinates = [x1, x2, x3, z]
        forward = [
            s,
            v + a**2 * s,
            a + v**2 + flow_p * s,
            2 * a**2 * v - flow_p + a**4 * s + s**2 / 2,
        ]
        inverse_a = x1 * (z - x1**2 / 2) - x2**2 + x3
        inverse = [
            x1,
            inverse_a,
            x2 - inverse_a**2 * x1,
            2 * inverse_a**2 * x2 - inverse_a**4 * x1 - z + x1**2 / 2,
        ]
        source_coordinates = [s, a, v, flow_p]
        for expr, original in zip(inverse, source_coordinates):
            self.assert_zero(expr.subs(dict(zip(coordinates, forward)), simultaneous=True)
                             - original)
        for expr, original in zip(forward, coordinates):
            self.assert_zero(expr.subs(dict(zip(source_coordinates, inverse)), simultaneous=True)
                             - original)
        for expr in forward[:3]:
            self.assert_zero(sp.diff(expr, s, 2))
        self.assert_zero(sp.diff(forward[3], s, 2) - 1)

        velocity = sp.Matrix([1, inverse_a**2, inverse[3], x1 + inverse_a**4])
        jacobian = velocity.jacobian(coordinates)
        origin = dict(zip(coordinates, (0, 0, 0, 0)))
        other = dict(zip(coordinates, (0, 0, 1, 0)))
        J0, J1 = jacobian.subs(origin), jacobian.subs(other)
        self.assertEqual(J0, sp.Matrix([
            [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, -1], [1, 0, 0, 0]]))
        self.assertEqual(J1, sp.Matrix([
            [0, 0, 0, 0], [0, 0, 2, 0], [-1, 2, 0, -1], [1, 0, 4, 0]]))
        self.assertEqual(J0**4, sp.zeros(4))
        self.assertEqual(J1**4, sp.zeros(4))
        product = J0 * J1
        expected = sp.Matrix([
            [0, 0, 0, 0], [0, 0, 0, 0], [-1, 0, -4, 0], [0, 0, 0, 0]])
        self.assertEqual(product, expected)
        self.assertEqual(sp.trace(product), -4)
        self.assertEqual(product**2, -4 * product)
        self.assertNotEqual(product**2, sp.zeros(4))
        for n in (1, 2, 3, 4):
            self.assertEqual(product**n, (-4)**(n - 1) * product)


if __name__ == "__main__":
    unittest.main(verbosity=2)
