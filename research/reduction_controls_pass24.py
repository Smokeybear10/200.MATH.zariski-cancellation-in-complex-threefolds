"""Independent exact controls, not a universal theorem or novelty verifier.

Run: python research/reduction_controls_pass24.py
Only unittest and sympy are imported. No solver or project modules are used.
"""

import unittest
import sympy as sp


f, h, x, r, t, a = sp.symbols("f h x r t a")
y, z, u, lam, w, zz, q = sp.symbols("y z u lam w zz q")


def delta0(poly):
    return sp.expand(2 * r * sp.diff(poly, x) + h * sp.diff(poly, r))


def odd_data(c, coefficient):
    """Reconstruct the literal monic tests from an independent primitive."""
    primitive = sp.integrate(coefficient, x) / 2
    primitive -= primitive.subs(x, 0)
    c0 = sp.expand(c.subs({f: 0, h: 0}, simultaneous=True))
    residue = sp.rem(
        x**3 * c.subs(f, 0) + h * primitive.subs(f, 0), x**5 - h, x
    )
    tail = sp.expand(residue - c0 * x**3)
    accepted = (
        c0 != 0
        and sp.expand(c.subs(h, 0) - c0) == 0
        and sp.diff(tail, x) == 0
    )
    return accepted, primitive, c0, sp.expand(residue)


def gauge_data(c, coefficient):
    accepted, primitive, c0, _ = odd_data(c, coefficient)
    if not accepted:
        raise ValueError("The exact remainder conditions fail")
    c1 = sp.cancel((c - c0) / h)
    ell1 = sp.expand(primitive + c1 * x**3)
    ell10 = ell1.subs(f, 0)
    ell_constant = sp.rem(ell10, x**5 - h, x)
    jj = sp.cancel((ell10 - ell_constant) / (h - x**5))
    kk = sp.cancel((ell1 - ell_constant - (h - x**5) * jj) / f)
    return c1, ell_constant, jj, kk


def example_positive():
    c = 2 + h * (f + h)
    ell1 = (h - x**5) * (x + h) - h**2 + f * x**2 * (1 + h)
    primitive = sp.expand(ell1 - (f + h) * x**3)
    return c, 2 * sp.diff(primitive, x)


def physical_data(n):
    ff = x * z - y**2
    aa = ff**n
    rr = x**3 + aa * y
    hh = aa**2 * z + 2 * aa * x**2 * y + x**5
    gradients = [[sp.diff(ff, v) for v in (x, y, z)],
                 [sp.diff(hh, v) for v in (x, y, z)]]
    values = tuple(-sp.det(sp.Matrix(gradients + [
        [sp.Integer(i == j) for i in range(3)]
    ])) for j in range(3))
    return ff, aa, rr, hh, values


def apply_physical(poly, values):
    return sp.expand(sum(v * sp.diff(poly, var)
                         for var, v in zip((x, y, z), values)))


def horizontal_data():
    vv = 1 + lam * x
    gg = 1 - lam * x
    ss = y + vv * t
    ww = gg * y - lam**2 * x**2 * t
    zinv = z - 2 * lam**2 * y * ss + lam**4 * x**2 * ss**2
    return vv, gg, ss, ww, zinv


class OddCoefficientControls(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_primitive_identity(self):
        for c, bb in [(1 + h, -6 * x**2), example_positive()]:
            c = sp.sympify(c)
            _, ell, _, _ = odd_data(c, bb)
            self.assertZero(delta0(c * r + h * ell) - h * (c + r * bb))

    def test_positive_remainder_cases(self):
        for c, bb in [(1, 0), (1, 2 * f * x), (1 + h, -6 * x**2),
                      example_positive()]:
            with self.subTest(c=c, coefficient=bb):
                self.assertTrue(odd_data(sp.sympify(c), sp.sympify(bb))[0])

    def test_negative_remainder_cases(self):
        for c, bb in [(0, 0), (h, 2 * f * x), (1 + f, 2 * f * x),
                      (1 + h, 0), (1, 2 * x)]:
            with self.subTest(c=c, coefficient=bb):
                c, bb = sp.sympify(c), sp.sympify(bb)
                self.assertFalse(odd_data(c, bb)[0])
                with self.assertRaises(ValueError):
                    gauge_data(c, bb)

    def test_monic_remainder_matches_physical_curve(self):
        for c, bb in [example_positive(), (sp.Integer(1) + h, sp.Integer(0)),
                      (sp.Integer(1), 2 * x**6)]:
            _, ell, _, residue = odd_data(c, bb)
            on_curve = (u**3 * c.subs({f: 0, h: u**5}, simultaneous=True)
                        + u**5 * ell.subs({f: 0, h: u**5, x: u},
                                         simultaneous=True))
            self.assertZero(on_curve - residue.subs({h: u**5, x: u},
                                                   simultaneous=True))

    def test_gauge_decomposition_in_independent_ring(self):
        c, bb = example_positive()
        _, ell, c0, _ = odd_data(c, bb)
        c1, constant, jj, kk = gauge_data(c, bb)
        for poly in (c1, constant, jj, kk):
            self.assertIsInstance(sp.Poly(poly, f, h, x), sp.Poly)
        self.assertZero(ell + c1 * x**3 - constant - (h - x**5) * jj - f * kk)
        self.assertZero(c + r * bb - c1 * (h - 6 * x**2 * r)
                        - delta0((h - x**5) * jj) - c0 - delta0(f * kk))

    def test_gauge_is_physical_polynomial(self):
        c, bb = 1 + h, -6 * x**2 + 2 * h - 12 * x**5 + 4 * f * x
        c1, constant, jj, kk = gauge_data(sp.sympify(c), bb)
        ff, aa, rr, hh, values = physical_data(1)
        subst = {f: ff, h: hh, r: rr}
        g1 = ((2 * x**2 * y + aa * z) * jj.subs({f: ff, h: hh},
                                               simultaneous=True))
        target = delta0((h - x**5) * jj).subs(subst, simultaneous=True)
        self.assertZero(apply_physical(g1, values) - target)
        self.assertZero(hh - x**5 - aa * (2 * x**2 * y + aa * z))

    def test_f_divisible_variable_time_invariants(self):
        for n in (1, 2, 3):
            aa = f**n
            ell = f * x**2 * (1 + h)
            ll = ell - aa * t
            rho = r + h * ll
            xx = x + 2 * r * ll + h * ll**2
            deriv = lambda poly: sp.expand(aa * delta0(poly)
                               + (1 + delta0(ell)) * sp.diff(poly, t))
            self.assertZero(deriv(ll) + aa)
            self.assertZero(deriv(rho))
            self.assertZero(deriv(xx))
            self.assertZero(xx * h - rho**2 - x * h + r**2)

    def test_variable_time_localized_inverse(self):
        xx0, rho0, sigma0 = sp.symbols("X0 Rho0 Sigma0")
        for n in (2, 3):
            aa = f**n
            ell = f * x**2
            ll = ell - aa * t
            rho = r + h * ll
            xx = x + 2 * r * ll + h * ll**2
            ss = t - ell / aa
            old_r = rho0 + aa * h * sigma0
            old_x = xx0 + 2 * aa * rho0 * sigma0 + aa**2 * h * sigma0**2
            old_t = sigma0 + ell.subs(x, old_x) / aa
            inverse = {x: old_x, r: old_r, t: old_t}
            for forward, target in ((xx, xx0), (rho, rho0), (ss, sigma0)):
                self.assertZero(sp.cancel(forward.subs(inverse, simultaneous=True) - target))
            for backward, target in ((old_x, x), (old_r, r), (old_t, t)):
                self.assertZero(sp.cancel(backward.subs(
                    {xx0: xx, rho0: rho, sigma0: ss}, simultaneous=True) - target))

    def test_finite_nilpotent_inverse_and_slice_correction(self):
        for n in (2, 3):
            aa = f**n
            ell = f * x**2
            def truncate(poly):
                return sp.rem(sp.expand(poly), aa, f)
            phi_x = truncate(x + 2 * r * ell + h * ell**2)
            phi_r = truncate(r + h * ell)
            def phi(poly):
                return truncate(poly.subs({x: phi_x, r: phi_r}, simultaneous=True))
            def inverse(poly):
                answer = sp.Integer(0)
                layer = truncate(poly)
                for j in range(n):
                    answer += (-1)**j * layer
                    layer = truncate(phi(layer) - layer)
                self.assertZero(layer)
                return truncate(answer)
            for generator in (x, r):
                self.assertZero(truncate(phi(inverse(generator)) - generator))
                self.assertZero(truncate(inverse(phi(generator)) - generator))
            repair = inverse(-ell)
            ll = ell - aa * t
            xx = x + 2 * r * ll + h * ll**2
            rho = r + h * ll
            numerator = -ell - repair.subs({x: xx, r: rho}, simultaneous=True)
            self.assertZero(truncate(numerator))
            sigma = sp.cancel(t + numerator / aa)
            self.assertIsInstance(sp.Poly(sigma, f, h, x, r, t), sp.Poly)
            self.assertZero(aa * delta0(sigma) + (1 + delta0(ell))
                            * sp.diff(sigma, t) - 1)

    def test_n1_affine_slice(self):
        ff, aa, rr, hh, values = physical_data(1)
        self.assertZero(apply_physical(x**2 / 2, values) - 2 * ff * x * rr)
        self.assertZero(apply_physical(rr, values) - aa * hh)

    def test_n2_polynomial_slice(self):
        ll = f * x**2 / 2 - f**2 * t
        xx = x + 2 * r * ll + h * ll**2
        sigma = sp.cancel(t + (xx**2 - x**2) / (2 * f))
        self.assertIsInstance(sp.Poly(sigma, f, h, x, r, t), sp.Poly)
        self.assertZero(f**2 * delta0(sigma) + (1 + 2 * f * x * r)
                        * sp.diff(sigma, t) - 1)

    def test_h_divisor_primitive_difference(self):
        c, bb = example_positive()
        _, ell, _, _ = odd_data(c, bb)
        primitive = c * r + h * ell
        difference = primitive.subs({x: 1, r: -r}, simultaneous=True)
        difference -= primitive.subs(x, 1)
        self.assertZero(difference + 2 * c * r)
        for n in (1, 2, 3):
            aa = f**n
            tau = -2 * r / (aa * h)
            self.assertZero(2 * aa * r * tau + aa**2 * h * tau**2)

    def test_reduced_derivation_at_all_checked_multiplicities(self):
        for n in (1, 2, 3):
            ff, aa, rr, hh, values = physical_data(n)
            delta_values = (0, x, 2 * y)
            for actual, reduced in zip(values, delta_values):
                quotient = sp.cancel((actual + 5 * x**4 * reduced) / aa)
                self.assertIsInstance(sp.Poly(quotient, x, y, z), sp.Poly)
            self.assertZero(rr - x**3 - aa * y)
            self.assertZero(hh - x**5 - aa * (2 * x**2 * y + aa * z))

    def test_nongauge_degree_two_matrix(self):
        basis = (x**2, x * y, x * z, y**2, y * z, z**2)
        image = [sp.Poly(x * sp.diff(b, y) + 2 * y * sp.diff(b, z), x, y, z)
                 for b in basis]
        matrix = sp.Matrix([[poly.coeff_monomial(b) for poly in image] for b in basis])
        target = sp.Matrix([0, 0, 2, -2, 0, 0])
        functional = sp.Matrix([[0, 0, 2, -1, 0, 0]])
        self.assertEqual(matrix.rank(), 4)
        self.assertEqual(functional * matrix, sp.zeros(1, 6))
        self.assertEqual((functional * target)[0], 6)
        self.assertEqual(matrix.row_join(target).rank(), 5)
        # For n=1, the relation f=0 itself removes this obstruction.
        self.assertEqual(matrix.row_join(target / 2).row_join(target).rank(), 5)

    def test_semigroup_and_nilpotent_coefficient_independence(self):
        small = {3 * i + 5 * j for i in range(5) for j in range(5)
                 if 3 * i + 5 * j < 5}
        self.assertEqual(small, {0, 3})
        for n in (1, 2, 3, 4):
            matrix = sp.Matrix([[sp.Poly((-y**2)**j, y).coeff_monomial(y**i)
                                 for j in range(n)] for i in range(2 * n)])
            self.assertEqual(matrix.rank(), n)
            self.assertEqual(sp.Poly((x * z - y**2)**n, x, y, z).total_degree(), 2 * n)


class HorizontalControls(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_stable_coordinates_both_directions(self):
        vv, gg, ss, ww, zinv = horizontal_data()
        inverse = {y: lam**2 * x**2 * u + vv * w, t: gg * u - w,
                   z: zz + 2 * lam**2 * vv * w * u + lam**4 * x**2 * u**2}
        for old, new in ((ss, u), (ww, w), (zinv, zz)):
            self.assertZero(old.subs(inverse, simultaneous=True) - new)
        for old, expr in inverse.items():
            self.assertZero(expr.subs({u: ss, w: ww, zz: zinv}, simultaneous=True) - old)

    def test_stable_derivation(self):
        vv, gg, ss, ww, zinv = horizontal_data()
        def deriv(poly):
            return lam**2 * x**2 * sp.diff(poly, y) + 2 * lam**2 * y * sp.diff(poly, z) + gg * sp.diff(poly, t)
        for poly, expected in ((ss, 1), (ww, 0), (zinv, 0), (x, 0), (lam, 0)):
            self.assertZero(deriv(poly) - expected)

    def test_projected_horizontal_formula(self):
        vv, gg, ss, _, _ = horizontal_data()
        for aa, bb, ee in ((0, 0, 0), (1, x + lam, lam * x),
                          (lam**2, x**2 + lam, lam + x)):
            ys = sp.diff(ss, lam) + aa * sp.diff(ss, x) + bb * sp.diff(ss, y) + ee * sp.diff(ss, t)
            actual = (-ee + ys * gg).subs({y: vv * w, t: -w}, simultaneous=True)
            expected = -(x + lam * aa) * gg * w + bb * gg - ee * lam**2 * x**2
            self.assertZero(actual - expected)

    def test_projection_repair_invisibility(self):
        vv, gg, ss, _, _ = horizontal_data()
        def ee(poly):
            return lam**2 * x**2 * sp.diff(poly, y) + 2 * lam**2 * y * sp.diff(poly, z) + gg * sp.diff(poly, t)
        hh = y * t + lam * x
        def zz_der(poly):
            return (x + t) * sp.diff(poly, y) + y * sp.diff(poly, lam)
        for poly in (lam, x, y, z, t):
            base = sp.diff(poly, lam) - sp.diff(ss, lam) * ee(poly)
            corrected_y = sp.diff(poly, lam) + hh * ee(poly) + ss * zz_der(poly)
            corrected_s = sp.diff(ss, lam) + hh * ee(ss) + ss * zz_der(ss)
            difference = corrected_y - corrected_s * ee(poly) - base
            self.assertZero(difference - ss * (zz_der(poly) - zz_der(ss) * ee(poly)))

    def test_affine_recurrence_has_nonzero_leading_term(self):
        for aa in (sp.Integer(0), sp.Integer(1), lam**2, 1 + lam):
            antiderivative = sp.integrate(aa, lam)
            gamma = sp.expand((q + antiderivative + lam * aa) * (1 - lam * (q + antiderivative)))
            self.assertEqual(sp.Poly(gamma, q).coeff_monomial(q**2), -lam)
            m = sp.Poly(gamma, lam).degree()
            leading = sp.Poly(gamma, lam).LC()
            self.assertGreaterEqual(m, 1)
            pp = sp.Integer(1)
            for j in range(1, 5):
                pp = sp.expand(sp.diff(pp, lam) - gamma * pp)
                self.assertEqual(sp.Poly(pp, lam).degree(), j * m)
                self.assertZero(sp.Poly(pp, lam).LC() - (-leading)**j)

    def test_successful_coupled_lift(self):
        vv, gg, ss, ww, zinv = horizontal_data()
        dy = 2 * lam * x**2 * ss + x * ww
        dt = -x * ss
        dz = (4 * lam + 6 * lam**2 * x) * ww * ss + 4 * lam**3 * x**2 * ss**2
        def deriv(poly):
            return sp.expand(sp.diff(poly, lam) + dy * sp.diff(poly, y) + dt * sp.diff(poly, t) + dz * sp.diff(poly, z))
        for poly in (ss, ww, zinv):
            self.assertZero(deriv(poly))
        for poly, count in ((y, 3), (t, 2), (z, 5)):
            for _ in range(count):
                poly = deriv(poly)
            self.assertZero(poly)
        self.assertZero(sp.diff(x**2 * z - vv**2 * w**2, lam) + 2 * x * vv * w**2)

    def test_full_congruence_horizontal_relation(self):
        hh = x + 1
        pp = x**2
        dd = pp * hh
        relation = (1 + lam * dd) * w - y
        def deriv(poly):
            return sp.expand(sp.diff(poly, lam) + hh * w * (x**2 * sp.diff(poly, y) + 2 * y * sp.diff(poly, z)))
        self.assertZero(deriv(relation))
        self.assertZero(deriv(deriv(y)))
        self.assertZero(deriv(deriv(deriv(z))))


class TangentSyzygyControls(unittest.TestCase):
    def test_six_genuine_primitive_fields_and_successful_combinations(self):
        old = sp.symbols("X1 X2 X3 X4")
        base = [old[j] + old[3] for j in range(3)]
        quadratic = sum(value**2 for value in base)
        slice_poly = old[3] - quadratic
        gradient = [sp.diff(slice_poly, coordinate) for coordinate in old]
        e_values = [-1, -1, -1, 1]
        self.assertEqual(sp.expand(sum(e*value for e, value in zip(e_values, gradient))), 1)
        intrinsic = [x, y, z]
        ss = sp.Symbol("S")
        qq = x**2 + y**2 + z**2
        inverse = {old[j]: intrinsic[j]-ss-qq for j in range(3)}
        inverse[old[3]] = ss+qq
        self.assertEqual(sp.expand(slice_poly.subs(inverse, simultaneous=True)), ss)
        for expression, coordinate in zip(base, intrinsic):
            self.assertEqual(sp.expand(expression.subs(inverse, simultaneous=True)), coordinate)
        fields = {}
        for first in range(4):
            for second in range(first+1, 4):
                coefficients = [sp.Integer(0)]*4
                coefficients[second] = gradient[first]
                coefficients[first] = -gradient[second]
                tangent_value = sum(value*derivative for value, derivative
                                    in zip(coefficients, gradient))
                self.assertEqual(sp.expand(tangent_value), 0)
                for value in coefficients:
                    self.assertEqual(sp.expand(sum(e*sp.diff(value, coordinate)
                                                   for e, coordinate in zip(e_values, old))), 0)
                vector = [sp.expand(sum(value*sp.diff(expression, coordinate)
                                       for value, coordinate in zip(coefficients, old))
                                    .subs(inverse, simultaneous=True)) for expression in base]
                fields[first, second] = sp.Matrix(vector)
                gcd = sp.Integer(0)
                for value in vector:
                    gcd = sp.gcd(gcd, value)
                self.assertTrue(sp.sympify(gcd).is_number)
                squared = sum(vector[j]*sp.diff(vector[first], intrinsic[j]) for j in range(3))
                multiplier = -4 if second < 3 else -8
                self.assertEqual(sp.expand(squared-multiplier*intrinsic[first]), 0)
        successful = [
            fields[0, 1]+fields[0, 2]-fields[0, 3],
            -fields[0, 1]+fields[1, 2]-fields[1, 3],
            -fields[0, 2]-fields[1, 2]-fields[2, 3],
        ]
        for index, vector in enumerate(successful):
            self.assertEqual(vector.applyfunc(sp.expand), sp.eye(3)[:, index])


if __name__ == "__main__":
    unittest.main(verbosity=2)
