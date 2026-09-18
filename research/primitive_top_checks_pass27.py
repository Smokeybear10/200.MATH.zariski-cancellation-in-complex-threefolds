"""Independent exact controls for the primitive-highest-adjoint example."""

import unittest

import sympy as sp


lam, a, b, c, U, V, H = sp.symbols("lam a b c U V H")
variables = (lam, a, b, c)
horizontal = (1, 0, 0, 0)
vertical = (0, 1, lam*a, lam*b)
top = (0, 0, a, b)
bpartial = (0, 0, 1, 0)
jfield = (0, 0, 0, lam)
cpartial = (0, 0, 0, 1)


def apply(values, expression):
    return sp.expand(sum(value*sp.diff(expression, variable)
                         for value, variable in zip(values, variables)))


def bracket(left, right):
    return tuple(sp.expand(apply(left, rv)-apply(right, lv))
                 for rv, lv in zip(right, left))


class PrimitiveTopChecks(unittest.TestCase):
    def test_actual_two_lnds_and_slices(self):
        self.assertEqual(apply(horizontal, lam), 1)
        self.assertEqual(apply(vertical, a), 1)
        self.assertEqual(apply(vertical, lam), 0)
        for field in (horizontal, vertical):
            for variable in variables:
                current = variable
                for _ in range(4):
                    current = apply(field, current)
                self.assertEqual(current, 0)

    def test_full_coordinate_inverse_forward(self):
        u = b-lam*a**2/2
        v = c-lam*a*b+lam**2*a**3/3
        inverse = {b: U+lam*a**2/2,
                   c: V+lam*a*U+lam**2*a**3/6}
        self.assertEqual(sp.expand(u.subs(inverse, simultaneous=True)), U)
        self.assertEqual(sp.expand(v.subs(inverse, simultaneous=True)), V)
        self.assertEqual(apply(vertical, u), 0)
        self.assertEqual(apply(vertical, v), 0)

    def test_full_coordinate_inverse_backward(self):
        forward = {U: b-lam*a**2/2,
                   V: c-lam*a*b+lam**2*a**3/3}
        self.assertEqual(sp.expand((U+lam*a**2/2).subs(forward, simultaneous=True)), b)
        self.assertEqual(sp.expand((V+lam*a*U+lam**2*a**3/6)
                                  .subs(forward, simultaneous=True)), c)

    def test_highest_adjoint_is_primitive_and_fixed(self):
        self.assertEqual(bracket(horizontal, vertical), top)
        self.assertEqual(bracket(horizontal, top), (0, 0, 0, 0))
        self.assertEqual(sp.gcd(a, b), 1)
        for variable in variables:
            self.assertEqual(apply(top, variable).subs({a: 0, b: 0}), 0)
            self.assertEqual(apply(top, apply(top, apply(top, variable))), 0)

    def test_kernel_plinth_and_even_odd_residue_controls(self):
        invariant = 2*a*c-b**2
        self.assertEqual(apply(top, invariant), 0)
        self.assertEqual(apply(top, b), a)
        for q0, q1 in ((lam+H, a*H+1), (H**3+lam*a, lam**2+H**2)):
            actual = q0.subs(H, invariant)+b*q1.subs(H, invariant)
            self.assertEqual(apply(top, actual), sp.expand(a*q1.subs(H, invariant)))
        for degree in (1, 2, 4):
            even = sp.symbols(f"e0:{degree+1}")
            odd = sp.symbols(f"o0:{degree+1}")
            residue = sum(even[j]*(-b**2)**j+b*odd[j]*(-b**2)**j
                          for j in range(degree+1))
            solution = sp.solve(sp.Poly(residue, b).all_coeffs(), (*even, *odd), dict=True)
            self.assertEqual(solution, [{q: 0 for q in (*even, *odd)}])

    def test_joint_kernel_coefficient_equations(self):
        fa, fb, fc = sp.symbols("fa fb fc")
        image = fa+lam*(a*fb+b*fc)
        self.assertEqual(sp.Poly(image, lam).coeff_monomial(1), fa)
        after_independence_of_a = sp.Poly(a*fb+b*fc, a)
        self.assertEqual(after_independence_of_a.coeff_monomial(a), fb)
        self.assertEqual(after_independence_of_a.coeff_monomial(1), b*fc)
        self.assertEqual(sp.solve([fa, fb, b*fc], (fa, fb, fc), dict=True),
                         [{fa: 0, fb: 0, fc: 0}])

    def test_complete_six_dimensional_bracket_table(self):
        fields = (horizontal, vertical, top, bpartial, jfield, cpartial)
        expected = {(0, 1): top, (1, 2): bpartial,
                    (1, 3): tuple(-q for q in jfield),
                    (2, 3): tuple(-q for q in cpartial),
                    (0, 4): cpartial}
        for i in range(6):
            for j in range(i+1, 6):
                self.assertEqual(bracket(fields[i], fields[j]),
                                 expected.get((i, j), (0, 0, 0, 0)))

    def test_additional_bracket_has_a_slice_outside_top_line(self):
        recovered = bracket(vertical, top)
        self.assertEqual(recovered, bpartial)
        self.assertEqual(apply(recovered, b), 1)
        self.assertEqual(apply(recovered, lam), 0)
        self.assertEqual(bracket(horizontal, recovered), (0, 0, 0, 0))
        # The b,c coefficient minor excludes rational proportionality.
        self.assertEqual(sp.det(sp.Matrix([[top[2], top[3]],
                                          [recovered[2], recovered[3]]])), -b)


if __name__ == "__main__":
    unittest.main()
