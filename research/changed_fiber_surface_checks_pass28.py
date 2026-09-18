"""Independent finite controls for the all-invariant-fiber theorem.

Only unittest and SymPy are imported. No project solver or prior checker
is imported. These finite examples do not replace the written proof.
"""

import unittest
import sympy as sp


u, x, y, t, z, X = sp.symbols("u x y t z X")
ii = sp.I
A = (u - 1) * (u - ii)
d = u**4 - 1
ROOTS = (sp.Integer(1), ii, sp.Integer(-1), -ii)
PAIRS = ((sp.Integer(1), ii), (sp.Integer(1), -ii),
         (sp.Integer(-1), ii))


def trunc(poly, variable, order):
    """Exact truncated arithmetic, permitting polynomial coefficients."""
    poly = sp.Poly(sp.expand(poly), variable)
    return sp.expand(sum(coefficient * variable**power[0]
                         for power, coefficient in poly.terms()
                         if power[0] < order))


def multiply(left, right, variable, order):
    return trunc(left * right, variable, order)


def power(base, exponent, variable, order):
    result = sp.Integer(1)
    for _ in range(exponent):
        result = multiply(result, base, variable, order)
    return result


def unit_power(unit, exponent, variable, order):
    """Finite binomial series for a unit with constant coefficient one."""
    assert sp.expand(unit).subs(variable, 0) == 1
    tail = trunc(unit - 1, variable, order)
    result = sp.Integer(0)
    current = sp.Integer(1)
    for k in range(order):
        result = trunc(result + sp.binomial(exponent, k) * current,
                       variable, order)
        current = multiply(current, tail, variable, order)
    return result


def multiplicity(poly, root):
    translated = sp.Poly(sp.expand(poly.subs(u, root + x)), x,
                         extension=ii)
    if translated.is_zero:
        raise ValueError("The invariant must be nonconstant.")
    return min(term[0][0] for term in translated.terms())


def conductor_orders(invariant):
    c0 = sp.expand(invariant.subs(u, 1))
    assert all(sp.expand(invariant.subs(u, r) - c0) == 0
               for r in ROOTS)
    return {r: multiplicity(invariant - c0, r) for r in ROOTS}


def passes_all_fiber_test(invariant):
    orders = conductor_orders(invariant)
    return all(min(orders[r], orders[s]) == 1 for r, s in PAIRS)


def quotient_data(relations):
    basis = sp.groebner(relations, x, y, order="lex", extension=ii)
    leading = [p.LM(order="lex").exponents for p in basis.polys]
    return basis, leading


def standard_monomials(leading, bound):
    return [(a, b) for a in range(bound) for b in range(bound)
            if not any(a >= p and b >= q for p, q in leading)]


class ChangedFiberSurfaceChecks(unittest.TestCase):
    def test_six_scaled_normalization_jet_charts(self):
        """Actual polynomial jets retain the original t on all six lines."""
        order = 6
        for root, epsilon in ((sp.Integer(1), 0), (sp.Integer(1), 1),
                              (ii, 0), (ii, 1)):
            aa = sp.expand(A.subs(u, root + x))
            zz = root * (2 * epsilon - 1) * t
            radicand = 1 + 4 * aa * zz
            sqrt = unit_power(radicand, sp.Rational(1, 2), x, order)
            yy = trunc((1 + (2 * epsilon - 1) * sqrt) / 2, x, order)
            equation = trunc(aa * zz - multiply(yy, yy - 1, x, order),
                             x, order)
            self.assertEqual(equation, 0)
            self.assertEqual(yy.subs(x, 0), epsilon)
            self.assertEqual(sp.cancel(zz / (root * (2 * epsilon - 1))),
                             t)

        for root in (sp.Integer(-1), -ii):
            aa = sp.expand(A.subs(u, root + x))
            a0 = sp.expand(A.subs(u, root))
            yy = root * a0 * t
            inv = unit_power(sp.expand(aa / a0), -1, x, order) / a0
            zz = multiply(yy * (yy - 1), inv, x, order)
            self.assertEqual(trunc(aa * zz - yy * (yy - 1), x, order), 0)
            self.assertEqual(sp.cancel(yy / (root * a0)), t)

    def test_actual_invariant_pair_quotients(self):
        """Actual j-j0 jets, not monomial substitutes, have predicted lengths."""
        examples = (d, d * (u**2 - 1), d * A, d**2,
                    d * (u - 1)**3 * (u + ii) * (u + 2)**2)
        for invariant in examples:
            invariant = sp.expand(invariant)
            c0 = invariant.subs(u, 1)
            orders = conductor_orders(invariant)
            jet_order = max(orders.values()) + 2
            for left, right in PAIRS:
                fr = trunc(invariant.subs(u, left + x) - c0, x, jet_order)
                fs = trunc(invariant.subs(u, right + y) - c0, y, jet_order)
                gb, leading = quotient_data(
                    (x * y, x**jet_order, y**jet_order, fr + fs))
                standard = standard_monomials(leading, 2 * jet_order)
                self.assertEqual(len(standard), orders[left] + orders[right])
                self.assertEqual(gb.reduce(x**(orders[left] + 1))[1], 0)
                self.assertEqual(gb.reduce(y**(orders[right] + 1))[1], 0)
                cotangent_rank = sp.Matrix(
                    [[sp.expand(fr).coeff(x, 1), sp.expand(fs).coeff(y, 1)]]
                ).rank()
                self.assertEqual(cotangent_rank,
                                 int(min(orders[left], orders[right]) == 1))

    def test_artinian_pair_length_cotangent_and_elimination(self):
        """Check independent Groebner bases for D_mn and explicit positive maps."""
        for m in range(1, 5):
            for n in range(1, 5):
                gb, leading = quotient_data((x * y, x**m + y**n))
                standard = standard_monomials(leading, m + n + 2)
                self.assertEqual(len(standard), m + n)
                self.assertEqual(gb.reduce(x**(m + 1))[1], 0)
                self.assertEqual(gb.reduce(y**(n + 1))[1], 0)
                linear_rank = sp.Matrix([[int(m == 1), int(n == 1)]]).rank()
                full_fiber_cotangent_dim = 3 - linear_rank
                self.assertEqual(full_fiber_cotangent_dim,
                                 2 if min(m, n) == 1 else 3)
                if m == 1:
                    self.assertEqual(sp.expand((x * y).subs(x, -y**n)),
                                     -y**(n + 1))
                    self.assertEqual(sp.expand((x + y**n).subs(x, -y**n)), 0)
                if n == 1:
                    self.assertEqual(sp.expand((x * y).subs(y, -x**m)),
                                     -x**(m + 1))

    def test_all_degree_classifier_on_mixed_positive_negative_controls(self):
        positives = (d, d * (u**2 - 1), d * (u - 1)**7,
                     d * (u**2 + 1)**4, 3 + d * (u + 2)**8)
        negatives = (d**2, d * A, d * (u - 1) * (u + ii),
                     d * (u + 1) * (u - ii),
                     7 + d**2 * (u + 2)**3)
        for invariant in positives:
            self.assertTrue(passes_all_fiber_test(sp.expand(invariant)))
        for invariant in negatives:
            self.assertFalse(passes_all_fiber_test(sp.expand(invariant)))
        for invariant in positives + negatives:
            invariant = sp.expand(invariant)
            c0 = invariant.subs(u, 1)
            ff = sp.div(invariant - c0, d, u, extension=ii)
            self.assertEqual(ff[1], 0)
            for root in ROOTS:
                self.assertEqual(sp.expand(
                    sp.diff(invariant, u).subs(u, root)
                    - 4 * root**3 * ff[0].subs(u, root)), 0)
        self.assertEqual(conductor_orders(d), {r: 1 for r in ROOTS})
        orders = conductor_orders(sp.expand(d * (u**2 - 1)))
        self.assertEqual([orders[r] + orders[s] for r, s in PAIRS], [3, 3, 3])
        with self.assertRaises(ValueError):
            passes_all_fiber_test(sp.Integer(7))

    def test_finite_unit_root_changes_with_polynomial_inverse(self):
        """Finite root extraction normalizes actual nonmonomial branches."""
        order = 9
        unit = 1 + 2*x - 3*x**2 + x**5
        for m in (1, 2, 3, 4):
            root = unit_power(unit, sp.Rational(1, m), x, order)
            self.assertEqual(power(root, m, x, order), trunc(unit, x, order))
            changed = multiply(x, root, x, order)
            self.assertEqual(power(changed, m, x, order),
                             trunc(x**m * unit, x, order))
            # Construct the inverse coefficient by coefficient in exact jets.
            inverse = x
            for degree in range(2, order):
                substituted = sp.Integer(0)
                for (exponent,), coefficient in sp.Poly(changed, x).terms():
                    substituted += coefficient * power(inverse, exponent, x, order)
                error_coefficient = trunc(substituted - x, x, order).coeff(x, degree)
                inverse = trunc(inverse - error_coefficient * x**degree, x, order)
            composition = sp.Integer(0)
            for (exponent,), coefficient in sp.Poly(changed, x).terms():
                composition += coefficient * power(inverse, exponent, x, order)
            self.assertEqual(trunc(composition, x, order), x)

    def test_ordinary_fiber_jets_include_the_u_zero_exception(self):
        """A(zeta)!=0, not h being a coordinate, controls ordinary fat fibers."""
        for root in (sp.Integer(0), sp.Integer(2), 2*ii):
            for order in (1, 2, 4, 5):
                aa = sp.expand(A.subs(u, root + x))
                a0 = sp.expand(A.subs(u, root))
                inv = unit_power(sp.expand(aa / a0), -1, x, order) / a0
                zz = multiply(y * (y - 1), inv, x, order)
                self.assertEqual(trunc(aa * zz - y * (y - 1), x, order), 0)
        self.assertEqual(sp.expand(d + 1), u**4)
        self.assertEqual(multiplicity(d + 1, sp.Integer(0)), 4)
        for root in (sp.Integer(2), -sp.Integer(2), 2*ii, -2*ii):
            self.assertEqual(sp.expand((d - 15).subs(u, root)), 0)
            self.assertEqual(multiplicity(d - 15, root), 1)

    def test_global_chinese_remainder_plane_embedding(self):
        """The X coordinate supplies a basis on a product of nonuniform fat lines."""
        values = (sp.Integer(0), sp.Integer(1), ii)
        lengths = (2, 3, 5)
        polynomial = sp.prod((X - a)**q for a, q in zip(values, lengths))
        total = sum(lengths)
        columns = []
        for degree in range(total):
            column = []
            for value, length in zip(values, lengths):
                restriction = trunc((value + x)**degree, x, length)
                column.extend(restriction.coeff(x, k) for k in range(length))
            columns.append(sp.Matrix(column))
        matrix = sp.Matrix.hstack(*columns)
        self.assertNotEqual(sp.expand(matrix.det()), 0)
        for value, length in zip(values, lengths):
            self.assertEqual(trunc(polynomial.subs(X, value + x), x, length), 0)
        p2 = (X * (X - 1) * (X - ii))**2
        p3 = (X * (X - 1) * (X - ii))**3
        self.assertEqual(sp.degree(p2, X), 6)
        self.assertEqual(sp.degree(p3, X), 9)


if __name__ == "__main__":
    unittest.main(verbosity=2)

