"""Independent bounded controls, not proofs of universal recognition."""

import unittest

import sympy as sp


lam, x, y, z, w, h = sp.symbols("lam x y z w h")
v = 1 + lam * x
physical_h = x**2 * z - v**2 * w**2
generators = (lam, x, w, z)


def apply_field(values, polynomial):
    return sp.expand(sum(a * sp.diff(polynomial, q) for a, q in zip(values, generators)))


class CoupledHomotopyControls(unittest.TestCase):
    def test_base_and_primitive_generator_values(self):
        old_h = x**2 * z - y**2
        old_d = lambda q: sp.expand(x**2 * sp.diff(q, y) + 2 * y * sp.diff(q, z))
        self.assertEqual(old_d(old_h), 0)
        self.assertEqual(old_d(y), x**2)
        self.assertEqual(sp.gcd(x**2, 2 * y), 1)
        self.assertEqual(sp.expand(old_h.subs(y, v * w) - physical_h), 0)
        vertical = (0, 0, x**2, 2 * v**2 * w)
        self.assertEqual(apply_field(vertical, physical_h), 0)
        self.assertEqual(sp.gcd(x**2, 2 * v**2 * w), 1)

    def test_regular_moving_normalizer_is_not_lnd(self):
        vertical = (0, 0, x**2, 2 * v**2 * w)
        normalizer = (1, 0, 0, 2 * x * z - 2 * lam * v * w**2)
        self.assertEqual(apply_field(normalizer, physical_h), sp.expand(2 * x * physical_h))
        for q in generators:
            self.assertEqual(
                sp.expand(apply_field(normalizer, apply_field(vertical, q))
                          - apply_field(vertical, apply_field(normalizer, q))),
                0,
            )
        iterate = physical_h
        for j in range(1, 7):
            iterate = apply_field(normalizer, iterate)
            self.assertEqual(iterate, sp.expand((2 * x)**j * physical_h))
            self.assertNotEqual(iterate, 0)

    def test_successful_horizontal_action_leaves_old_plane(self):
        horizontal = (1, 0, 0, 0)
        vertical = (0, 0, x**2, 2 * v**2 * w)
        image = apply_field(horizontal, physical_h)
        self.assertEqual(image, sp.expand(-2 * x * v * w**2))
        self.assertEqual(apply_field(vertical, image), sp.expand(-4 * x**3 * v * w))
        self.assertNotEqual(apply_field(vertical, image), 0)
        for q in generators:
            self.assertEqual(apply_field(horizontal, apply_field(horizontal, q)), 0)

    def test_normalizer_residue_parity(self):
        # An unrestricted finite polynomial basis independently solves the
        # first normal residue. The note supplies the all-degree parity proof.
        for degree in (1, 2, 5):
            gc = sp.symbols(f"g0:{degree + 1}")
            bc = sp.symbols(f"b0:{degree + 1}")
            gp = sum(gc[j] * h**j for j in range(degree + 1))
            bp = sum(bc[j] * h**j for j in range(degree + 1))
            residue = sp.Poly(sp.expand(gp.subs(h, -w**2) + 2 * w**2
                                       + 2 * w * bp.subs(h, -w**2)), w)
            solution = sp.solve(residue.all_coeffs(), (*gc, *bc), dict=True)
            expected = {q: 0 for q in (*gc, *bc)}
            expected[gc[1]] = 2
            self.assertEqual(solution, [expected])

    def test_affine_h_degree_recurrence(self):
        for gamma in (sp.Integer(3), 1 + lam, 2 - lam**3):
            beta = lam**2 + 7
            iterate = h
            m = sp.degree(gamma, lam)
            lead = sp.Poly(gamma, lam).LC()
            for j in range(1, 7):
                iterate = sp.expand(sp.diff(iterate, lam)
                                    + (gamma * h + beta) * sp.diff(iterate, h))
                coefficient = sp.Poly(iterate, h).coeff_monomial(h)
                self.assertEqual(sp.degree(coefficient, lam), j * m)
                self.assertEqual(sp.Poly(coefficient, lam).LC(), lead**j)
                self.assertNotEqual(coefficient, 0)

    def test_nonlinear_h_degree_growth(self):
        for degree in (2, 3, 4):
            leading = lam**2 + 1
            g = leading * h**degree + lam * h + 2
            iterate = h
            expected_leading = sp.Integer(1)
            for j in range(1, 5):
                expected_leading *= (1 + (j - 1) * (degree - 1)) * leading
                iterate = sp.expand(sp.diff(iterate, lam) + g * sp.diff(iterate, h))
                self.assertEqual(sp.degree(iterate, h), 1 + j * (degree - 1))
                self.assertEqual(sp.expand(sp.Poly(iterate, h).LC() - expected_leading), 0)

    def test_full_plinth_positive_boundary(self):
        unit_mod_plinth = 1 + lam * x**2
        invariant = x**2 * z - unit_mod_plinth**2 * w**2
        horizontal = (1, 0, 0, 2 * unit_mod_plinth * w**2)
        vertical = (0, 0, x**2, 2 * unit_mod_plinth**2 * w)
        self.assertEqual(apply_field(horizontal, invariant), 0)
        self.assertEqual(apply_field(vertical, invariant), 0)
        for q in generators:
            self.assertEqual(sp.expand(apply_field(horizontal, apply_field(vertical, q))
                                       - apply_field(vertical, apply_field(horizontal, q))), 0)
            self.assertEqual(apply_field(horizontal, apply_field(horizontal,
                                              apply_field(horizontal, q))), 0)


if __name__ == "__main__":
    unittest.main()
