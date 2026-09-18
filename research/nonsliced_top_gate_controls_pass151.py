"""Exact controls for an actual sliced pair that fails the three-good gate151.

The full coordinate inverse is verified in both orders. The top and
nilpotence assertions concern actual polynomial derivations. The finite
coefficient and parity controls do not replace the written all-polynomial
kernel, nonslice, residue-degree, or affine-first-integral arguments.
This pair is not asserted to be a dense three-good selected frame.
No earlier checker or solver is imported.
"""

import unittest

import sympy as sp


class NonslicedTopGateControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def apply(self, field, expression, variables):
        return sp.expand(sum(v*sp.diff(expression, x) for v, x in zip(field, variables)))

    def bracket(self, left, right, variables):
        return tuple(
            self.apply(left, rv, variables)-self.apply(right, lv, variables)
            for lv, rv in zip(left, right)
        )

    def test_actual_coordinate_actions_and_both_inverse_orders(self):
        u, a, b, c = sp.symbols("u a b c")
        variables = (u, a, b, c)
        E = (1, 0, 0, 0)
        T = (0, u, 1+u**2*a, u**2*b)
        w_coord = b-u*a**2/2
        p_coord = a-u*w_coord
        q_coord = (
            c-u**2*w_coord**2/2-u**3*p_coord**2*w_coord/2
            -u**4*p_coord*w_coord**2/2-u**5*w_coord**3/6
        )
        forward = (u, p_coord, q_coord, w_coord)
        U, P, Q, W = sp.symbols("U P Q W")
        target = (U, P, Q, W)
        inverse = (
            U,
            P+U*W,
            W+U*(P+U*W)**2/2,
            Q+U**2*W**2/2+U**3*P**2*W/2+U**4*P*W**2/2+U**5*W**3/6,
        )
        for expression, identity in zip(inverse, variables):
            self.zero(expression.subs(dict(zip(target, forward)), simultaneous=True)-identity)
        for expression, identity in zip(forward, target):
            self.zero(expression.subs(dict(zip(variables, inverse)), simultaneous=True)-identity)
        for expression, value in zip(forward, (0, 0, 0, 1)):
            self.zero(self.apply(T, expression, variables)-value)
        self.zero(self.apply(E, u, variables)-1)
        self.zero(self.apply(E, w_coord, variables)+a**2/2)
        self.zero(sp.diff(w_coord, u, 2))
        self.assertNotEqual(sp.expand(sp.diff(p_coord, u, 2)), 0)

        # The inverse derivative is independently the stated original T.
        for expression, coefficient in zip(inverse, T):
            transported = sp.diff(expression, W)
            pulled_back = transported.subs(dict(zip(target, forward)), simultaneous=True)
            self.zero(pulled_back-coefficient)

    def test_exact_top_nilpotence_and_full_residue_controls(self):
        u, a, b, c, H = sp.symbols("u a b c H")
        variables = (u, a, b, c)
        E = (1, 0, 0, 0)
        T = (0, u, 1+u**2*a, u**2*b)
        L = (0, 0, a, b)
        first = self.bracket(E, T, variables)
        second = self.bracket(E, first, variables)
        for value, target in zip(first, (0, 1, 2*u*a, 2*u*b)):
            self.zero(value-target)
        for value, target in zip(second, (0, 0, 2*a, 2*b)):
            self.zero(value-target)
        for value in self.bracket(E, second, variables):
            self.zero(value)
        for value, target in zip(T, L):
            self.zero(sp.Poly(value, u).coeff_monomial(u**2)-target)

        expected_chains = (
            (a, (u, 0)),
            (b, (1+u**2*a, u**3, 0)),
            (c, (u**2*b, u**2+u**4*a, u**5, 0)),
        )
        for start, chain in expected_chains:
            value = start
            for target in chain:
                value = self.apply(T, value, variables)
                self.zero(value-target)
        self.zero(self.apply(T, u, variables))
        self.assertEqual(sp.gcd(a, b), 1)
        for variable in variables:
            value = self.apply(L, variable, variables)
            self.zero(value.subs({a: 0, b: 0}, simultaneous=True))
        self.zero(self.apply(L, b, variables)-a)
        self.zero(self.apply(L, c, variables)-b)
        self.zero(self.apply(L, self.apply(L, self.apply(L, c, variables), variables), variables))
        invariant = 2*a*c-b**2
        self.zero(self.apply(L, invariant, variables))
        self.zero(invariant.subs(a, 0)+b**2)

        # In k[b,c]/(b^2+H), H is a nonzero element of k=C(H).
        # b^{-1}=-b/H; clear H to check the residue-slice identity.
        relation = b**2+H
        self.zero(sp.rem(-b**2-H, relation, b))
        self.zero(self.apply(L, c, variables).subs(a, 0)-b)
        # Irreducibility is the note's Eisenstein argument at H, not a
        # conclusion inferred from this finite polynomial remainder.

    def test_affine_coefficient_equations_and_parity(self):
        u, a, b, c, H = sp.symbols("u a b c H")
        variables = (u, a, b, c)
        T = (0, u, 1+u**2*a, u**2*b)
        L = (0, 0, a, b)
        F0, F1 = sp.Function("F0")(a, b, c), sp.Function("F1")(a, b, c)
        image = self.apply(T, F0+u*F1, variables)
        expected = (
            sp.diff(F0, b),
            sp.diff(F0, a)+sp.diff(F1, b),
            self.apply(L, F0, variables)+sp.diff(F1, a),
            self.apply(L, F1, variables),
        )
        for degree, coefficient in enumerate(expected):
            self.zero(sp.Poly(image, u).coeff_monomial(u**degree)-coefficient)
        self.assertEqual(sp.degree(image, u), 3)

        fcoeff = sp.symbols("f0:6")
        gcoeff = sp.symbols("g0:6")
        f0 = sum(coefficient*monomial for coefficient, monomial in zip(
            fcoeff, (1, a, c, a**2, a*c, c**2)
        ))
        G = sum(coefficient*monomial for coefficient, monomial in zip(
            gcoeff, (1, a, H, a**2, a*H, H**2)
        ))
        invariant = 2*a*c-b**2
        f1 = G.subs(H, invariant)
        self.zero(sp.diff(f1, b)+2*b*sp.diff(G, H).subs(H, invariant))
        second_coefficient = sp.expand(sp.diff(f0, a)+sp.diff(f1, b))
        self.zero(second_coefficient+second_coefficient.subs(b, -b)-2*sp.diff(f0, a))
        self.zero(
            second_coefficient-second_coefficient.subs(b, -b)
            +4*b*sp.diff(G, H).subs(H, invariant)
        )

        ph = sp.symbols("ph0:4")
        ps = sp.symbols("ps0:4")
        phi = sum(ph[j]*c**j for j in range(4))
        psi = sum(ps[j]*a**j for j in range(4))
        reduced = self.apply(L, phi, variables)+sp.diff(psi, a)
        self.zero(reduced-b*sp.diff(phi, c)-sp.diff(psi, a))
        self.zero(sp.Poly(reduced, b).coeff_monomial(b)-sp.diff(phi, c))
        self.zero(sp.Poly(reduced, b).coeff_monomial(1)-sp.diff(psi, a))

        c0, c1 = sp.symbols("c0 c1")
        self.zero(self.apply(T, c0+c1*u, variables))
        self.zero(sp.diff(c0+c1*u, u, 2))
        # The preceding exact identities implement the written proof's
        # reductions; finitely many samples do not classify all first integrals.


if __name__ == "__main__":
    unittest.main()
