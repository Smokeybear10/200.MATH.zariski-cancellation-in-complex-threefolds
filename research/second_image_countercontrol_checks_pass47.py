"""Finite exact controls for second-image-countercontrol-pass47.md.

These tests check identities in the actual example and bounded image degrees.
They do not prove the universal filtration, flatness, Nagata, or Euler theorems.
Only unittest and SymPy are used; no research solver is imported.
"""

import unittest

import sympy as sp


u, v, z, w, r, t, s, eps, T, Z = sp.symbols(
    "u v z w r t s eps T Z"
)
r_actual = u * z + v * w
relation = r_actual**2 + 2 * w - v
G = 2 * u * z - v * r**2 - 2 * r + v**2
curve = v * r**2 + 2 * r - v**2
z_local = curve / (2 * u)
w_local = (v - r**2) / 2


def clean(expr):
    return sp.cancel(sp.expand(expr))


def deriv(expr):
    return clean(
        (1 + v * r_actual) * sp.diff(expr, z)
        - u * r_actual * sp.diff(expr, w)
    )


def flow(time):
    return {
        z: z + time * (1 + v * r_actual) + u * v * time**2 / 2,
        w: w - u * r_actual * time - u**2 * time**2 / 2,
    }


class SecondImageCountercontrolChecks(unittest.TestCase):
    def zero(self, expr):
        self.assertEqual(clean(expr), 0)

    def test_actual_presentations_action_and_two_sided_flow(self):
        # Both quotient maps, including their nonzero raw relation multiples.
        self.zero(G.subs(r, r_actual) + v * relation)
        r_round = r_actual.subs(w, w_local)
        self.zero(r_round - r - G / 2)
        self.zero(
            relation.subs(w, w_local) - (r * G + G**2 / 4)
        )
        self.zero(w_local.subs(r, r_actual) - w + relation / 2)
        self.zero(G.subs(z, z_local))
        self.zero(r_actual.subs({z: z_local, w: w_local},
                                simultaneous=True) - r)

        self.zero(deriv(relation))
        self.zero(deriv(r_actual) - u)
        self.zero(deriv(deriv(z)) - u * v)
        self.zero(deriv(deriv(w)) + u**2)
        for generator in (z, w):
            self.zero(deriv(deriv(deriv(generator))))

        ft = flow(t)
        self.zero(relation.subs(ft, simultaneous=True) - relation)
        self.zero(r_actual.subs(ft, simultaneous=True) - r_actual - u * t)
        for generator in (z, w):
            self.zero(
                flow(t)[generator].subs(flow(s), simultaneous=True)
                - flow(t + s)[generator]
            )
            self.zero(
                flow(t)[generator].subs(flow(-t), simultaneous=True)
                - generator
            )
        self.zero(u * sp.diff(z_local, r) - (1 + v * r))
        self.zero(u * sp.diff(w_local, r) + u * r)

    def test_smooth_curve_and_branch_polynomial_data(self):
        discriminant = sp.discriminant(-curve, v)
        self.zero(discriminant - (r**4 + 8 * r))
        self.assertEqual(sp.degree(discriminant, r), 4)
        self.assertEqual(sp.gcd(discriminant,
                                sp.diff(discriminant, r)), 1)
        singular = sp.groebner(
            [curve, sp.diff(curve, v), sp.diff(curve, r)], v, r
        )
        self.assertEqual(list(singular), [sp.Integer(1)])
        # Primitive linear relations used in the written domain arguments.
        self.assertEqual(sp.gcd(2 * u, curve), 1)
        self.assertEqual(sp.gcd(2 * u, v * r**2), 1)
        self.assertEqual(sp.Poly(G, r, z).coeff_monomial(r), -2)
        self.assertEqual(2 * (1 - 4) + 4, -2)
        # The last arithmetic is not a machine proof of the topological inputs.

    def test_bounded_actual_filtration_and_image_ideals(self):
        # The proof supplies all degrees; this reconstructs degrees 0 through 8.
        for n in range(9):
            with self.subTest(n=n):
                images = []
                for j in range(n // 2 + 1):
                    i = n - 2 * j
                    monomial = sp.expand(r**i * z_local**j)
                    dn = clean(u**n * sp.diff(monomial, r, n))
                    expected = (
                        sp.factorial(n) * u**(n - j) * v**j / 2**j
                    )
                    self.zero(dn - expected)
                    self.zero(sp.diff(monomial, r, n + 1))
                    images.append(dn)
                for j in range((n - 1) // 2 + 1):
                    i = n - 1 - 2 * j
                    lower = sp.expand(r**i * z_local**j)
                    self.zero(sp.diff(lower, r, n))
                power = n // 2
                target = [
                    u**((n + 1) // 2) * u**(power - j) * v**j
                    for j in range(power + 1)
                ]
                actual_basis = sp.groebner(images, u, v, domain=sp.QQ)
                target_basis = sp.groebner(target, u, v, domain=sp.QQ)
                self.assertEqual(list(actual_basis), list(target_basis))

    def test_free_second_module_and_scheme_theoretic_closed_fibers(self):
        columns = [
            [sp.Poly(item, r).coeff_monomial(r**i) for i in range(3)]
            for item in (sp.Integer(1), z_local, w_local)
        ]
        basis = sp.Matrix.hstack(*(sp.Matrix(column) for column in columns))
        self.zero(basis.det() + sp.Rational(1, 2) / u)
        image_row = sp.Matrix([[0, u * v, -u**2]])
        self.assertEqual(image_row * sp.Matrix([0, u, v]),
                         sp.zeros(1, 1))
        self.zero(u * z_local + v * w_local - r)
        self.zero(r**2 - v + 2 * w_local)

        ideal = sp.groebner([u * v, u**2], u, v)
        self.assertEqual(sp.gcd(u * v, u**2), u)
        self.assertEqual(ideal.reduce(u)[1], u)
        self.assertEqual(sp.groebner([u, v], u, v).reduce(
            sp.Integer(1))[1], 1)

        # The origin fiber is an actual line, with r=0 but nonzero action.
        self.zero(relation.subs({u: 0, v: 0}) - 2 * w)
        self.zero(r_actual.subs({u: 0, v: 0}))
        self.zero((1 + v * r).subs({u: 0, v: 0}) - 1)
        # At (0,-1) the nilpotent residue of r must not be discarded.
        self.zero(G.subs({u: 0, v: -1, r: 1 + eps}) - eps**2)
        self.zero((1 + v * r).subs({v: -1, r: 1 + eps}) + eps)
        doubled = sp.groebner([eps**2], eps)
        self.assertEqual(doubled.reduce(eps)[1], eps)
        self.assertEqual(sp.groebner([eps], eps).reduce(eps)[1], 0)

    def test_actual_divisor_normalization_and_fixed_scheme(self):
        eta = (1 + v**3) / v**2
        forward = {T: r + 1 / v, Z: 2 * z / v}
        inverse = {r: T - 1 / v, z: v * Z / 2}
        normalized = u * Z - T**2 + eta
        self.zero(normalized.subs(forward, simultaneous=True) - G / v)
        self.zero(G.subs(inverse, simultaneous=True) - v * normalized)
        for coordinate in (r, z):
            self.zero(
                inverse[coordinate].subs(forward, simultaneous=True)
                - coordinate
            )
        for coordinate in (T, Z):
            self.zero(
                forward[coordinate].subs(inverse, simultaneous=True)
                - coordinate
            )
        alt_derivative = lambda f: clean(
            u * sp.diff(f, r) + (1 + v * r) * sp.diff(f, z)
        )
        self.zero(alt_derivative(forward[T]) - u)
        self.zero(alt_derivative(forward[Z]) - 2 * forward[T])
        self.zero(sp.discriminant(curve, r) - 4 * (1 + v**3))
        self.zero(eta / (1 + v**3) - 1 / v**2)

        # Exact equality of fixed-scheme ideals in the alternative presentation.
        fixed = sp.groebner([G, u, 1 + v * r], u, v, r, z)
        three_lines = sp.groebner(
            [u, v**3 + 1, r - v**2], u, v, r, z
        )
        self.assertEqual(list(fixed), list(three_lines))
        self.assertEqual(sp.gcd(v**3 + 1, 3 * v**2), 1)
        # Divisor coordinates invert v; no global origin inverse is asserted.


if __name__ == "__main__":
    unittest.main(verbosity=2)

