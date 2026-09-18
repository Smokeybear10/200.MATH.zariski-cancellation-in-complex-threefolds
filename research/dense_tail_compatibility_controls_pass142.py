"""Finite exact coefficient-compatibility controls for pass142.

The first two methods use actual inverse-verified frames from140. The third
uses the formal inverse-branch family141, whose projected source field is
rational but whose four-polynomial tuple is not a coordinate frame. The
last method checks small elimination examples and a deliberately synthetic
repeated denominator factor. It does not realize that synthetic polynomial
as an actual first tail. No universal compatibility, primitivity, saturation
or cancellation theorem is certified by these finite calculations.
No solver, earlier checker or search module is imported.
"""

import unittest

import sympy as sp


class DenseTailCompatibilityControls(unittest.TestCase):
    def setUp(self):
        self.a, self.b, self.v, self.u = sp.symbols("a b v u")
        self.X, self.Y, self.Z, self.W = sp.symbols("X Y Z W")
        self.U, self.V, self.t = sp.symbols("U V t")
        self.xi = sp.symbols("xi1 xi2 xi3")

    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def divided_difference(self, polynomial, a, v, u):
        result = sp.S.Zero
        for (j,), coefficient in sp.Poly(polynomial, self.t).terms():
            for i in range(1, j + 1):
                result += coefficient * sp.binomial(j, i) * v ** (j - i) * a**i * u ** (i - 1)
        return sp.expand(result)

    def both_inverses(self, forward, inverse):
        original = (self.X, self.Y, self.Z, self.W)
        adapted = (self.a, self.b, self.v, self.u)
        for expression, target in zip(inverse, adapted):
            self.zero(expression.subs(dict(zip(original, forward)), simultaneous=True) - target)
        for expression, target in zip(forward, original):
            self.zero(expression.subs(dict(zip(adapted, inverse)), simultaneous=True) - target)

    def H(self, f, order, dt, dr, first, second):
        result = sp.S.Zero
        for i in range(order + 1):
            term = f
            for _ in range(order - i):
                term = dr(term)
            for _ in range(i):
                term = dt(term)
            result += term * first**i * second ** (order - i) / (
                sp.factorial(i) * sp.factorial(order - i)
            )
        return sp.cancel(result)

    def projected_tail(self, coefficients, dt, dr, y, z):
        U, V = self.U, self.V
        omega = sum((self.H(fj, j, dt, dr, U, V)
                     for j, fj in enumerate(coefficients)), sp.S.Zero)
        first = -sum((self.H(fj, j + 1, dt, dr, U, V)
                      for j, fj in enumerate(coefficients)), sp.S.Zero)
        fm1 = first.subs({U: y, V: z}, simultaneous=True)
        return sp.cancel(omega), sp.cancel(first - fm1)

    def cleared(self, omega, q, numerators, values):
        U, V = self.U, self.V
        substitution = dict(zip(self.xi, (U, V, omega)))
        delta = sp.cancel(q.subs(substitution, simultaneous=True))
        rows = [sp.cancel(p.subs(substitution, simultaneous=True) - alpha * delta)
                for p, alpha in zip(numerators, values)]
        return delta, rows

    def source_identities(self, source, q, numerators, values):
        substitution = dict(zip(self.xi, source))
        denominator = sp.cancel(q.subs(substitution, simultaneous=True))
        self.assertNotEqual(denominator, 0)
        for p, alpha in zip(numerators, values):
            self.zero(p.subs(substitution, simultaneous=True) - alpha * denominator)

    def poly(self, expression, parameters):
        return sp.Poly(sp.cancel(expression), self.U, self.V,
                       domain=sp.QQ.frac_field(*parameters))

    def associated(self, left, right, parameters):
        self.assertEqual(self.poly(left, parameters).monic(), self.poly(right, parameters).monic())

    def recover(self, phi, delta, rows, parameters):
        common = self.poly(phi, parameters)
        for row in rows:
            common = common.gcd(self.poly(row, parameters))
        degree = self.poly(phi, parameters).total_degree()
        denominator_part = common.gcd(self.poly(delta, parameters) ** degree)
        return common.as_expr(), common.exquo(denominator_part).monic().as_expr()

    def redundant_denominator(self, phi, omega, q, numerators, values, g, parameters):
        # Multiplication by an actual complex source polynomial changes no
        # rational identity. It need not introduce a factor into genuine Phi.
        multiplier = self.xi[0]**2
        delta, rows = self.cleared(omega, q * multiplier,
                                   [p * multiplier for p in numerators], values)
        _, recovered = self.recover(phi, delta, rows, parameters)
        self.associated(recovered, g, parameters)

    def test_actual_sharp_family_projected_source_and_gcd(self):
        a, b, v, u = self.a, self.b, self.v, self.u
        X, Y, Z, W, U, V = self.X, self.Y, self.Z, self.W, self.U, self.V
        F = self.t**3 / 2 + self.t + 2
        delta_F = self.divided_difference(F, a, v, u)
        forward = (v + a * u, a - F.subs(self.t, v) + (b + 1) * u,
                   a - F.subs(self.t, v) + (b + 2) * u, b + delta_F)
        inv_u = Z - Y
        inv_a = 2 * Y - Z - inv_u * W + F.subs(self.t, X)
        inv_v = X - inv_a * inv_u
        inv_b = W - self.divided_difference(F, inv_a, inv_v, inv_u)
        self.both_inverses(forward, (inv_a, inv_b, inv_v, inv_u))

        tau, rho = (b + 1) / a, (b + 2) / a
        dt = lambda f: sp.cancel(a**2 * sp.diff(f, a) + a * (b + 2) * sp.diff(f, b))
        dr = lambda f: sp.cancel(-a**2 * sp.diff(f, a) - a * (b + 1) * sp.diff(f, b))
        y, z, w0 = [sp.cancel(f.subs(u, -v / a)) for f in forward[1:]]
        coefficients = [b + a, sp.S.Zero, a / 2]
        omega, phi = self.projected_tail(coefficients, dt, dr, y, z)
        self.zero(omega.subs({U: y, V: z}, simultaneous=True) - w0)

        p, qv, r = self.xi
        source_a = 2 * p - qv + (p - qv) * r + F.subs(self.t, 0)
        source_b = r - sum((sp.Poly(F, self.t).nth(j) * source_a**j * (p - qv) ** (j - 1)
                            for j in range(1, 4)), sp.S.Zero)
        denominator = source_a
        numerators = (source_b + 1, source_b + 2, source_a**2)
        values = (tau, rho, a)  # Here L=K already; e=a is an allowed redundant generator.
        self.source_identities((y, z, w0), denominator, numerators, values)
        delta, rows = self.cleared(omega, denominator, numerators, values)
        g = (b + 2) * U - (b + 1) * V + F.subs(self.t, a * (U - V)) - a
        self.zero(phi + a * g)
        self.zero(delta - a - g)
        self.zero(rows[1] - rows[0] + g / a)
        common, recovered = self.recover(phi, delta, rows, (a, b))
        self.associated(common, g, (a, b))
        self.associated(recovered, g, (a, b))
        self.assertEqual(self.poly(phi, (a, b)).gcd(self.poly(delta, (a, b))).total_degree(), 0)
        self.redundant_denominator(phi, omega, denominator, numerators, values, g, (a, b))

    def test_actual_proper_coefficient_cover_and_three_source_values(self):
        a, b, v, u = self.a, self.b, self.v, self.u
        X, Y, Z, W, U, V = self.X, self.Y, self.Z, self.W, self.U, self.V
        p, qv, r = self.xi
        source_b = qv - r
        source_a = p - source_b * r
        for n in (2, 3):
            with self.subTest(n=n):
                forward = (v + a**n * u, a + b * u, b + u, u)
                inv_u, inv_b = W, Z - W
                inv_a = Y - inv_b * W
                inv_v = X - inv_a**n * W
                self.both_inverses(forward, (inv_a, inv_b, inv_v, inv_u))
                tau, rho = b / a**n, 1 / a**n
                dt = lambda f: sp.cancel(a**n * sp.diff(f, b))
                dr = lambda f: sp.cancel(-a ** (n + 1) * sp.diff(f, a) / n
                                         - b * a**n * sp.diff(f, b))
                y, z, w0 = [sp.cancel(f.subs(u, -v / a**n)) for f in forward[1:]]
                omega, phi = self.projected_tail((-b, rho), dt, dr, y, z)
                self.zero(omega - V + b)
                self.zero(omega.subs({U: y, V: z}, simultaneous=True) - w0)
                denominator = source_a**n
                numerators = (source_b, sp.S.One, source_a ** (n + 1))
                values = (tau, rho, a)
                self.source_identities((y, z, w0), denominator, numerators, values)
                delta, rows = self.cleared(omega, denominator, numerators, values)
                pulled_a = U - b * V + b**2
                g = pulled_a - a
                self.zero(phi - a**n * g)
                self.zero(delta - pulled_a**n)
                self.zero(rows[2] - pulled_a**n * g)
                # The two speed identities alone permit conjugate values of a.
                two_rows = self.poly(rows[0], (a, b)).gcd(self.poly(rows[1], (a, b)))
                self.associated(two_rows.as_expr(), pulled_a**n - a**n, (a, b))
                common, recovered = self.recover(phi, delta, rows, (a, b))
                self.associated(common, g, (a, b))
                self.associated(recovered, g, (a, b))
                self.redundant_denominator(phi, omega, denominator, numerators, values, g, (a, b))

    def test_formal_inverse_branch_primitive_element_selects_conjugate(self):
        k, rho = sp.symbols("k rho")
        U, V, X, v = self.U, self.V, self.X, self.v
        p, qv, r = self.xi
        for F in (self.t**2 / 2, self.t**3 + self.t + 2):
            with self.subTest(F=F):
                tau = F.subs(self.t, k)
                slope = sp.diff(tau, k)
                dt = lambda f: sp.cancel(sp.diff(f, k) / slope)
                dr = lambda f: sp.diff(f, rho)
                degree = int(sp.degree(F, self.t))
                coefficients = [sp.Poly(F, self.t).nth(j + 1) * rho ** (j + 1)
                                for j in range(degree)]
                omega, phi = self.projected_tail(coefficients, dt, dr, v, k)
                self.zero(omega - rho * sp.diff(F.subs(self.t, V), V))
                self.zero(phi - tau + F.subs(self.t, V))
                # This source triple really generates C(v,k,rho) rationally,
                # although the four-polynomial tuple has nonunit Jacobian.
                source = (v, k, slope * rho)
                denominator = sp.diff(F.subs(self.t, qv), qv)
                numerators = (F.subs(self.t, qv) * denominator, r, qv * denominator)
                values = (tau, rho, k)
                self.source_identities(source, denominator, numerators, values)
                projected_jacobian = sp.Matrix(source).jacobian((v, k, rho))
                self.zero(projected_jacobian.det() - slope)
                self.assertGreater(sp.degree(slope, k), 0)
                self.zero((r / denominator).subs(dict(zip(self.xi, source)), simultaneous=True) - rho)
                delta, rows = self.cleared(omega, denominator, numerators, values)
                g = V - k
                self.zero(rows[0] + phi * delta)
                self.zero(rows[1])
                self.zero(rows[2] - g * delta)
                _, with_two = self.recover(phi, delta, rows[:2], (k, rho))
                self.associated(with_two, phi, (k, rho))
                _, with_three = self.recover(phi, delta, rows, (k, rho))
                self.associated(with_three, g, (k, rho))
                self.redundant_denominator(phi, omega, denominator, numerators, values, g, (k, rho))

    def test_small_saturations_and_synthetic_repeated_denominator_factor(self):
        a, b, U, V = self.a, self.b, self.U, self.V
        aux = sp.Symbol("saturation_aux")

        def elimination(rows, delta, parameters):
            basis = sp.groebner(list(rows) + [1 - aux * delta], aux, U, V,
                                order="lex", domain=sp.QQ.frac_field(*parameters))
            return [p.as_expr() for p in basis.polys if not p.as_expr().has(aux)]

        pulled_a = U - b * V + b**2
        g = pulled_a - a
        delta = pulled_a**2
        rows = (b - b * delta / a**2, 1 - delta / a**2, delta * g)
        eliminated = elimination(rows, delta, (a, b))
        self.assertEqual(len(eliminated), 1)
        self.associated(eliminated[0], g, (a, b))

        # A distinct actual129 projected source, not the reframed140 family:
        # (y,z,w0)=(v,a-F(v),b+aF'(v)). The redundant source denominator y
        # gives the genuine localization L[v,v^-1], not the whole L[v].
        F = self.t**3 / 2 + self.t + 2
        p, qv, r = self.xi
        slope_p = sp.diff(F.subs(self.t, p), p)
        source_a = qv + F.subs(self.t, p)
        source_b = r - source_a * slope_p
        values = (a, b, sp.S.Zero)
        numerators = (p * source_a, p * source_b, sp.S.Zero)
        source = (self.v, a - F.subs(self.t, self.v),
                  b + a * sp.diff(F.subs(self.t, self.v), self.v))
        self.source_identities(source, p, numerators, values)
        omega = b + a * sp.diff(F.subs(self.t, U), U)
        denominator, actual_rows = self.cleared(omega, p, numerators, values)
        actual_g = V + F.subs(self.t, U) - a
        self.zero(denominator - U)
        self.zero(actual_rows[0] - U * actual_g)
        self.zero(actual_rows[1] + U * sp.diff(F.subs(self.t, U), U) * actual_g)
        eliminated = elimination(actual_rows, denominator, (a, b))
        self.assertEqual(len(eliminated), 1)
        self.associated(eliminated[0], actual_g, (a, b))

        k = sp.Symbol("k")
        phi = (k**2 - V**2) / 2
        formal_rows = (-phi * V, sp.S.Zero, (V - k) * V)
        eliminated = elimination(formal_rows, V, (k,))
        self.assertEqual(len(eliminated), 1)
        self.associated(eliminated[0], V - k, (k,))
        unselected = elimination(formal_rows[:2], V, (k,))
        self.assertEqual(len(unselected), 1)
        self.associated(unselected[0], phi, (k,))

        # Pure factor arithmetic: this deliberately augmented polynomial is
        # NOT asserted to be any actual or formally realizable first tail.
        synthetic_phi = (V - k) * U**4
        synthetic_rows = (synthetic_phi, 2 * synthetic_phi, sp.S.Zero)
        common, recovered = self.recover(synthetic_phi, U, synthetic_rows, (k,))
        self.associated(common, synthetic_phi, (k,))
        self.associated(recovered, V - k, (k,))
        one_power = self.poly(common, (k,)).exquo(
            self.poly(common, (k,)).gcd(self.poly(U, (k,)))
        )
        self.assertEqual(one_power.total_degree(), 4)
        self.assertEqual(self.poly(recovered, (k,)).total_degree(), 1)


if __name__ == "__main__":
    unittest.main()
