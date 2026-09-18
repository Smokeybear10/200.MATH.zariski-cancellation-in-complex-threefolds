"""Five bounded exact controls for the separate pass72 arguments.

Companion-image and derivative tables are formal algebra, not original
four-coordinate actions. The displayed polynomial shear maps and their
two-sided inverses are actual coordinate-map calculations. Finite degree
and valuation cases do not certify the general written theorems.
"""

import unittest

import sympy as sp


class QuinticRankDropChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(sp.expand(entry)), 0)

    def test_third_full_image_subtraction_and_span(self):
        sigma, tau, eta, mu1, ell_h2 = sp.symbols("sigma tau eta mu1 ell_h2")
        mu2 = sp.Symbol("mu2", nonzero=True)
        e0, e1, v0, v1 = sp.symbols("e0 e1 v0 v1")
        c = sp.Matrix([1, 0, 0, 0])
        e = sp.Matrix([e0, e1, 1, 0])
        v = sp.Matrix([v0, v1, mu1, mu2])
        s0 = mu1 + eta * mu2
        h4, h3 = c * sigma + e, c * tau + e * sigma + v
        # These stand for 24 M^4(P,0), 6 M^3(P,0), 2 M^2(P,0).
        p4 = c.col_join(sp.Matrix([4]))
        p3 = h4.col_join(sp.Matrix([3 * (sigma + s0)]))
        p2 = h3.col_join(sp.Matrix([2 * ell_h2]))
        w1 = p3 - sigma * p4
        w2 = p2 - tau * p4 - sigma * w1
        self.assert_zero(w1 - e.col_join(sp.Matrix([3 * s0 - sigma])))
        self.assert_zero(w2 - v.col_join(sp.Matrix([
            2 * ell_h2 - 4 * tau - sigma * (3 * s0 - sigma)])))
        image_columns = sp.Matrix.hstack(p4, w1, w2)
        self.assert_zero(image_columns.extract([0, 2, 3], [0, 1, 2]).det() - mu2)
        self.assertEqual(image_columns.rank(), 3)
        constant_basis = sp.Matrix.hstack(c, e, v, sp.Matrix([0, 1, 0, 0]))
        dual_w = constant_basis.inv()[3, :]
        self.assert_zero(dual_w * image_columns[:4, :])

        # Independent Jordan-size control, not an assertion that this
        # constant matrix is the actual companion of a polynomial action.
        jordan = sp.zeros(5)
        for row in range(4):
            jordan[row, row + 1] = 1
        self.assertEqual([(jordan**power).rank() for power in (2, 3, 4, 5)], [3, 2, 1, 0])

    def test_polynomial_clearing_chain_and_repeated_factor_boundaries(self):
        sigma, u0, nu1, nu2, g = sp.symbols("sigma u0 nu1 nu2 g")
        beta = (sigma - 2 * nu2) / 3
        gamma = sigma**2 / 12 - nu2 * sigma / 6 + u0 / 3 - nu1 / 2
        kappa = gamma - nu2 * beta / 2
        n = g**2 * beta
        q = g**2 * (sigma + nu2)
        b2 = g**2 * (sigma**2 / 2 + 4 * u0 / 3 + nu1)
        Q = (g**2 * b2 / 4 - 3 * n**2 / 8 - 3 * nu2 * g**2 * n / 2
             - (nu2**2 / 2 + 3 * nu1 / 4) * g**4)
        Qq = (g**2 * b2 / 4 - q**2 / 24 - nu2 * g**2 * q / 4
              + (5 * nu2**2 / 8 - 3 * nu1 / 4) * g**4)
        self.assert_zero(n - (q - 3 * nu2 * g**2) / 3)
        self.assert_zero(Q - g**4 * kappa)
        self.assert_zero(Qq - Q)
        self.assert_zero(g * sp.diff(n, sigma) - g**3 / 3)
        self.assert_zero(g * sp.diff(Q, sigma) - g**3 * n / 2)
        self.assert_zero(g**2 * sp.diff(Q, sigma, 2) - g**6 / 6)
        self.assert_zero(g * sp.diff(Q - 3 * n**2 / 4, sigma))
        self.assert_zero(sp.diff(kappa, sigma) - beta / 2)

        # A formal polynomial representative with independent n and Q.
        a, b, z, w, nf, qf = sp.symbols("a b z w nf qf")
        coordinates = (a, b, z, w, g, nf, qf)
        values = (qf, g**2 * nf, g**4, 0, 0, 0, 0)

        def T(expression):
            return sum(value * sp.diff(expression, coordinate)
                       for coordinate, value in zip(coordinates, values))

        for coordinate in coordinates:
            self.assert_zero(T(T(coordinate)))

        x, y, r, B2 = sp.symbols("x y r B2")
        repeated_g = x**2 * y**3
        cases = ((repeated_g * r, (True, True, True)),
                 (x * y**2, (False, True, True)),
                 (sp.Integer(1), (False, False, True)))

        def is_polynomial(expression):
            denominator = sp.fraction(sp.cancel(expression))[1]
            return sp.Poly(denominator, x, y, r, B2).total_degree() == 0

        for numerator, expected in cases:
            with self.subTest(n=numerator):
                polynomial_Q = (repeated_g**2 * B2 / 4 - 3 * numerator**2 / 8
                                - sp.Rational(9, 2) * repeated_g**2 * numerator
                                - 6 * repeated_g**4)
                observed = tuple(is_polynomial(repeated_g**power * numerator / repeated_g**2)
                                 and is_polynomial(repeated_g**power * polynomial_Q / repeated_g**4)
                                 for power in (2, 3, 4))
                self.assertEqual(observed, expected)
                self.assertEqual(observed[0], is_polynomial(numerator / repeated_g))
                self.assertEqual(observed[1], is_polynomial(numerator**2 / repeated_g))
        # In the coprime numerator case the exact pole is four times
        # each repeated multiplicity, not four times the radical.
        coprime_Q = repeated_g**2 * B2 / 4 - sp.Rational(3, 8) - sp.Rational(9, 2) * repeated_g**2 - 6 * repeated_g**4
        denominator = sp.fraction(sp.cancel(coprime_Q / repeated_g**4))[1]
        self.assertEqual(sp.degree(denominator, x), 8)
        self.assertEqual(sp.degree(denominator, y), 12)

    def test_linear_and_quadratic_flow_coefficient_identities(self):
        w, time, beta, kappa, k, j = sp.symbols("w time beta kappa k j")
        p, g, lam = sp.symbols("p g lam", nonzero=True)
        aa, bb, cc = sp.symbols("aa bb cc", nonzero=True)
        cases = ((0, 0, cc), (0, bb, cc * w + 1),
                 (aa, bb * w + 1, cc * w**2 + 1),
                 (aa * w + 1, bb * w**2 + 1, cc * w**3 + 1),
                 (aa, bb, cc * w + 1),
                 (aa, bb * w + 1, cc),
                 (aa * w + 1, bb, cc))
        factors = (kappa + time * g * beta / 2 + time**2 * g**2 / 12,
                   beta + time * g / 3, sp.Integer(1))
        for w_degree, w_flow, w_top in (
                (1, w + p * time, p),
                (2, w + p * time + lam * g**2 * time**2 / 2, lam * g**2 / 2)):
            for case in cases:
                with self.subTest(w_degree=w_degree, coefficients=case):
                    polys = tuple(sp.sympify(entry) for entry in case)
                    degrees = [sp.degree(poly, w) if poly != 0 else None for poly in polys]
                    weighted = [w_degree * degree + offset if degree is not None else None
                                for degree, offset in zip(degrees, (2, 1, 0))]
                    top_degree = max(value for value in weighted if value is not None)
                    flow = sum(poly.subs(w, w_flow) * factor for poly, factor in zip(polys, factors))
                    extracted = sp.Poly(sp.expand(flow), time).coeff_monomial(time**top_degree)
                    expected = sum(sp.Poly(poly, w).LC() * w_top**degree * factor
                                   for poly, degree, weight, factor in zip(
                                       polys, degrees, weighted, (g**2 / 12, g / 3, 1))
                                   if weight == top_degree)
                    self.assert_zero(extracted - expected)
                    if w_degree == 1:
                        stars = [sp.Poly(poly, w).LC() if weight == top_degree else 0
                                 for poly, weight in zip(polys, weighted)]
                        self.assert_zero(extracted / p**(top_degree - 2)
                                         - stars[0] * g**2 / 12 - stars[1] * p * g / 3 - stars[2] * p**2)

        special_p = g * (3 * lam * beta + 2 * lam * k)
        quadratic_w = w + time * special_p + lam * g**2 * time**2 / 2
        relation = factors[0] - quadratic_w / (6 * lam) + k * factors[1] - j
        self.assert_zero(relation - (kappa - w / (6 * lam) + k * beta - j))
        self.assert_zero(sp.diff(quadratic_w, time, 2) - lam * g**2)
        invariant_u, invariant_v = sp.symbols("invariant_u invariant_v")
        quadratic_parameter = sp.Rational(9, 2) * lam * beta**2 + 3 * invariant_v * beta + invariant_u
        self.assert_zero((9 * lam * beta + 3 * invariant_v)**2
                         - 18 * lam * quadratic_parameter - 9 * invariant_v**2 + 18 * lam * invariant_u)
        simple_root_polynomial = sp.Poly(18 * lam * w + 9 * invariant_v**2 - 18 * lam * invariant_u, w)
        self.assertEqual(simple_root_polynomial.degree(), 1)
        self.assertEqual(sp.gcd(simple_root_polynomial, simple_root_polynomial.diff()).degree(), 0)

    def test_endpoint_shears_and_normalized_defect_signs(self):
        a, b, z, w = sp.symbols("a b z w")
        A, B, Z, W = sp.symbols("A B Z W")
        rho, lam = sp.symbols("rho lam", nonzero=True)
        alpha, gamma, u, k, j, beta = sp.symbols("alpha gamma u k j beta")
        old, new = sp.Matrix([a, b, z, w]), sp.Matrix([A, B, Z, W])

        def check_map(forward, inverse):
            self.assert_zero(forward.subs(dict(zip(old, inverse)), simultaneous=True) - new)
            self.assert_zero(inverse.subs(dict(zip(new, forward)), simultaneous=True) - old)
            jacobian = forward.jacobian(old)
            transported = inverse.jacobian(new).subs(dict(zip(new, forward)), simultaneous=True)
            self.assert_zero(jacobian * transported - sp.eye(4))
            self.assert_zero(transported * jacobian - sp.eye(4))
            self.assertEqual(jacobian.det(), 1)
            return jacobian, transported

        # Linear w-flow branch. Constants alpha,gamma encode the
        # stated coefficient relation; no classification is performed.
        f = w / (3 * rho)
        beta0 = f + u
        h = alpha * u + gamma - sp.Rational(3, 4) * u**2
        kappa0 = sp.Rational(3, 4) * beta0**2 + h
        L, R = 3 * f / 2 + alpha, -3 * f**2 / 4 - alpha * f + gamma
        self.assert_zero(kappa0 - L * beta0 - R)
        forward = sp.Matrix([a - L * b - R * z, b - f * z, z, w])
        fp, lp, rp = (entry.subs(w, W) for entry in (f, L, R))
        inverse = sp.Matrix([A + lp * B + (lp * fp + rp) * Z, B + fp * Z, Z, W])
        jacobian, transported = check_map(forward, inverse)
        self.assert_zero(jacobian * sp.Matrix([kappa0, beta0, 1, 0]) - sp.Matrix([0, u, 1, 0]))
        self.assert_zero(transported[:, 0] - sp.eye(4)[:, 0])
        self.assert_zero(transported[:, 1] - sp.eye(4)[:, 1] - L * sp.eye(4)[:, 0])
        dl = rho * sp.diff(L, w)
        ddl = rho * sp.diff(dl, w)
        self.assert_zero(dl - sp.Rational(1, 2))
        self.assert_zero(ddl)
        d = sp.Matrix([1, *sp.symbols("d1:4")])
        wa = -2 * d
        d_prime = d + 2 * dl * wa + ddl * sp.eye(4)[:, 0]
        self.assert_zero(d_prime + d)
        self.assert_zero(wa - 2 * d_prime)

        # Once the written fixed-base argument has made u constant,
        # a further constant-coefficient shear removes the last output.
        forward_constant = sp.Matrix([a - L * b - R * z, b - (f + u) * z, z, w])
        inverse_constant = sp.Matrix([A + lp * B + (lp * (fp + u) + rp) * Z,
                                      B + (fp + u) * Z, Z, W])
        jacobian_constant, transported_constant = check_map(forward_constant, inverse_constant)
        self.assert_zero(jacobian_constant * sp.Matrix([kappa0, beta0, 1, 0]) - sp.Matrix([0, 0, 1, 0]))
        self.assert_zero(transported_constant[:, 0] - sp.eye(4)[:, 0])

        # The separate A=0 coefficient-relation branch retains the
        # original good output without using a defect cancellation.
        u1, chi = sp.symbols("u1 chi")
        beta_linear = f + u1
        primitive = w**2 / (12 * rho**2) + u1 * w / (2 * rho)
        self.assert_zero(rho * sp.diff(primitive, w) - beta_linear / 2)
        forward_linear = sp.Matrix([a - primitive * z, b - beta_linear * z, z, w])
        inverse_linear = sp.Matrix([A + primitive.subs(w, W) * Z,
                                    B + beta_linear.subs(w, W) * Z, Z, W])
        jacobian_linear, transported_linear = check_map(forward_linear, inverse_linear)
        self.assert_zero(jacobian_linear * sp.Matrix([primitive + chi, beta_linear, 1, 0])
                         - sp.Matrix([chi, 0, 1, 0]))
        self.assert_zero(transported_linear[:, 0] - sp.eye(4)[:, 0])

        # Quadratic w-flow branch. This coordinate map is actual;
        # its companion and commutator inputs remain formal tables.
        coefficient = w / (6 * lam) + j
        kappa1 = coefficient - k * beta
        forward1 = sp.Matrix([a + k * b - coefficient * z, b, z, w])
        inverse1 = sp.Matrix([A - k * B + (W / (6 * lam) + j) * Z, B, Z, W])
        jacobian1, transported1 = check_map(forward1, inverse1)
        self.assert_zero(jacobian1 * sp.Matrix([kappa1, beta, 1, 0]) - sp.Matrix([0, beta, 1, 0]))
        self.assert_zero(transported1[:, 0] - sp.eye(4)[:, 0])
        self.assert_zero(transported1[:, 1] - sp.eye(4)[:, 1] + k * sp.eye(4)[:, 0])
        d_prime1 = d  # ad_delta^2 partial_a=0 and k is constant.
        self.assert_zero(wa + 2 * d_prime1)

    def test_fixed_base_actual_derivations_and_zero_defect_boundary(self):
        a, w, b, z = sp.symbols("a w b z")
        coordinates = sp.Matrix([a, w, b, z])
        partial_a, partial_b = sp.eye(4)[:, 0], sp.eye(4)[:, 2]

        def act(field, expression):
            return sum(value * sp.diff(expression, coordinate)
                       for coordinate, value in zip(coordinates, field))

        def bracket(left, right):
            return right.jacobian(coordinates) * left - left.jacobian(coordinates) * right

        J = b - w * z
        delta = sp.Matrix([J**2, 1, z + 1, 0])
        symmetry = sp.Matrix([0, 0, w, 1])
        self.assert_zero(act(delta, w) - 1)
        self.assert_zero(act(delta, J) - 1)
        self.assert_zero(bracket(delta, symmetry))
        self.assert_zero(bracket(delta, partial_a))
        self.assert_zero(bracket(delta, bracket(delta, partial_a)))
        defect = bracket(delta, bracket(delta, partial_b))
        self.assert_zero(defect + 2 * partial_a)
        self.assertNotEqual(defect, sp.zeros(4, 1))
        self.assert_zero(act(defect, w))
        self.assert_zero(sp.diff(w, a))
        # The computed field bracket also acts correctly on a rational
        # probe; the zero and nonzero brackets are not supplied as inputs.
        probe = (a + b) / (w + z + 1)
        self.assert_zero(act(delta, act(symmetry, probe))
                         - act(symmetry, act(delta, probe)))
        self.assert_zero(act(defect, probe) + 2 * sp.diff(probe, a))

        # Actual polynomial slice coordinates prove this particular
        # delta is an LND, without asserting the terminal quintic frame.
        A, W, B, Z = sp.symbols("A W B Z")
        new = sp.Matrix([A, W, B, Z])
        forward = sp.Matrix([a - J**3 / 3, w, J - w, z])
        inverse = sp.Matrix([A + (B + W)**3 / 3, W, B + W + W * Z, Z])
        self.assert_zero(forward.subs(dict(zip(coordinates, inverse)), simultaneous=True) - new)
        self.assert_zero(inverse.subs(dict(zip(new, forward)), simultaneous=True) - coordinates)
        self.assert_zero(forward.jacobian(coordinates) * delta - sp.Matrix([0, 1, 0, 0]))
        self.assertEqual(forward.jacobian(coordinates).det(), 1)

        # Dropping only nonzero defect permits dependence on the fixed
        # good coordinate: v=a, delta=partial_w, S=partial_z+a partial_b.
        zero_defect_delta = sp.eye(4)[:, 1]
        zero_defect_symmetry = sp.Matrix([0, 0, a, 1])
        self.assert_zero(bracket(zero_defect_delta, zero_defect_symmetry))
        self.assert_zero(act(zero_defect_delta, a))
        self.assert_zero(sp.diff(a, b))
        self.assert_zero(bracket(zero_defect_delta, partial_a))
        self.assert_zero(bracket(zero_defect_delta, bracket(zero_defect_delta, partial_a)))
        self.assert_zero(bracket(zero_defect_delta, bracket(zero_defect_delta, partial_b)))
        self.assertEqual(sp.diff(a, a), 1)


if __name__ == "__main__":
    unittest.main()
