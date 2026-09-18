"""Finite local-algebra controls; no original nonconical frame is asserted."""

import itertools
import unittest

import sympy as sp


def quotient_data(generators, variables, domain=sp.QQ):
    """Enumerate standard monomials using pure-power initial-ideal bounds."""
    groebner = sp.groebner(generators, *variables, order="lex", domain=domain)
    leading = [tuple(poly.LM(order=groebner.order).exponents)
               for poly in groebner.polys]
    bounds = []
    for i in range(len(variables)):
        powers = [exponents[i] for exponents in leading
                  if exponents[i] > 0
                  and all(exponents[j] == 0 for j in range(len(variables)) if j != i)]
        if not powers:
            raise ValueError("Initial ideal has no pure-power bound for a variable")
        bounds.append(min(powers))
    standard = [
        exponents for exponents in itertools.product(*(range(n) for n in bounds))
        if not any(all(a >= b for a, b in zip(exponents, lead)) for lead in leading)
    ]
    monomials = [sp.prod(x**n for x, n in zip(variables, exponents))
                 for exponents in standard]
    locations = {exponents: i for i, exponents in enumerate(standard)}
    matrices = []
    for variable in variables:
        matrix = sp.zeros(len(standard))
        for column, monomial in enumerate(monomials):
            remainder = groebner.reduce(variable * monomial)[1]
            for exponents, coefficient in sp.Poly(remainder, *variables, domain=domain).terms():
                if coefficient:
                    if exponents not in locations:
                        raise AssertionError("Normal form escaped the standard monomial basis")
                    matrix[locations[exponents], column] = coefficient
        matrices.append(matrix)
    return groebner, monomials, matrices


class ArtinLengthControls(unittest.TestCase):
    def test_three_artin_complete_intersections(self):
        x, y = sp.symbols("x y")
        cases = [
            ([x**2, y**2], 4, {1, x, y, x*y}, x*y),
            ([x**2 + y**3, x*y], 5, {1, x, y, y**2, y**3}, y**3),
            ([x**2, y**3], 6, {1, x, y, x*y, y**2, x*y**2}, x*y**2),
        ]
        for generators, length, expected, socle in cases:
            with self.subTest(generators=generators, length=length):
                groebner, basis, matrices = quotient_data(generators, (x, y))
                self.assertEqual(len(basis), length)
                self.assertEqual(set(basis), expected)
                mx, my = matrices
                self.assertEqual(mx * my, my * mx)
                # Nilpotence certifies support only at the origin in these examples.
                self.assertEqual(mx**length, sp.zeros(length))
                self.assertEqual(my**length, sp.zeros(length))
                for generator in generators:
                    value = sp.zeros(length)
                    for (a, b), coefficient in sp.Poly(generator, x, y).terms():
                        value += coefficient * mx**a * my**b
                    self.assertEqual(value, sp.zeros(length))
                self.assertEqual(len(mx.col_join(my).nullspace()), 1)
                self.assertNotEqual(groebner.reduce(socle)[1], 0)
                self.assertEqual(groebner.reduce(x * socle)[1], 0)
                self.assertEqual(groebner.reduce(y * socle)[1], 0)

    def test_fiber_length_and_fixed_scheme_thickness(self):
        p, y, z = sp.symbols("p y z")
        field = sp.QQ.frac_field(z)
        for m, e in itertools.product((1, 2, 4, 7), (2, 3)):
            with self.subTest(m=m, e=e):
                eta = p**m * z - y**e
                fixed, fixed_basis, fixed_matrices = quotient_data(
                    [p**m, y**(e-1)], (p, y), domain=field)
                fiber, fiber_basis, fiber_matrices = quotient_data(
                    [p, eta], (p, y), domain=field)
                self.assertEqual(len(fixed_basis), m * (e-1))
                self.assertEqual(set(fixed_basis),
                                 {p**i * y**j for i in range(m) for j in range(e-1)})
                self.assertEqual(len(fiber_basis), e)
                self.assertEqual(set(fiber_basis), {y**j for j in range(e)})
                self.assertEqual(fixed.reduce(eta)[1], 0)
                self.assertEqual(fiber.reduce(p)[1], 0)
                self.assertEqual(fiber.reduce(y**e)[1], 0)
                self.assertNotEqual(fiber.reduce(y**(e-1))[1], 0)
                mp, my = fixed_matrices
                self.assertEqual(mp**m, sp.zeros(len(fixed_basis)))
                self.assertEqual(my**(e-1), sp.zeros(len(fixed_basis)))
                self.assertEqual(len(mp.col_join(my).nullspace()), 1)
                self.assertEqual(fiber_matrices[0], sp.zeros(e))
                self.assertEqual(fiber_matrices[1]**e, sp.zeros(e))
                if m > 1:
                    self.assertNotEqual(fixed.reduce(p)[1], 0)
                    self.assertNotEqual(fixed.reduce(p**(m-1))[1], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
