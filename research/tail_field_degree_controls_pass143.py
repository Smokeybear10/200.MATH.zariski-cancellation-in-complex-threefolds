"""Finite exact field-degree and recovered-template controls for pass143.

The norm examples are synthetic field/source models, not realized Taylor
data or actual four-coordinate frames. Both component-boundary examples
are explicitly noninvertible formal families. Only the separately
identified recovered-invariant template method asserts an actual
polynomial inverse. Finite resultants, jets and coefficient comparisons
do not prove the universal field-degree, irreducibility or template
classification arguments. No previous checker or solver is imported.
"""

import unittest

import sympy as sp


class TailFieldDegreeControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def divided_difference(self, F, variable, speed, v, u):
        result = sp.S.Zero
        for (j,), coefficient in sp.Poly(F, variable).terms():
            for i in range(1, j + 1):
                result += coefficient * sp.binomial(j, i) * v ** (j - i) * speed**i * u ** (i - 1)
        return sp.expand(result)

    def test_synthetic_source_norm_degree_and_selected_factor(self):
        a, b, v, U, V, tau, root, ell, lam = sp.symbols("a b v U V tau root ell lam")
        for n in (2, 3):
            for degree in (2, 3):
                with self.subTest(n=n, d=degree):
                    # L=C(a,b), L0=C(a^n,b), F=L(v). This triple gives
                    # the exact source field, but no fourfold action is built.
                    y, z, w0 = v, v**degree + a, b
                    source_jacobian = sp.Matrix((y, z, w0)).jacobian((v, a, b))
                    self.zero(source_jacobian.det() - 1)
                    self.zero(z - y**degree - a)
                    self.zero(w0 - b)
                    selected = V - U**degree - a
                    norm = sp.resultant(root**n - tau, V - U**degree - root, root)
                    expected = (V - U**degree)**n - tau
                    self.zero(norm - expected)
                    self.assertEqual(sp.Poly(selected, U, V).total_degree(), degree)
                    self.assertEqual(sp.Poly(norm, U, V).total_degree(), n * degree)
                    self.zero(norm.subs({U: y, V: z, tau: a**n}, simultaneous=True))
                    quotient, remainder = sp.div(norm.subs(tau, a**n), selected, V)
                    self.zero(remainder)
                    self.zero(quotient.subs(V, U**degree + a) - n * a ** (n - 1))
                    self.zero(sp.diff(norm, V).subs({V: U**degree + a, tau: a**n}, simultaneous=True)
                              - n * a ** (n - 1))

                    # Generic linear projection retains the full plane degree.
                    projected_norm = sp.Poly(norm.subs(U, ell - lam * V), V)
                    projected_selected = sp.Poly(selected.subs(U, ell - lam * V), V)
                    self.assertEqual(projected_norm.degree(), n * degree)
                    self.assertEqual(projected_selected.degree(), degree)
                    self.assertEqual(sp.degree(y + lam * z, v), degree)
                    # The selected coefficient recovers a over L0; no finite
                    # test is being used to prove the extension degree for all n.
                    self.zero(-selected.subs({U: 0, V: 0}) - a)

    def test_formal_cubic_residual_enlarges_constant_field(self):
        k, rho, U, V, x, v, alpha, beta = sp.symbols("k rho U V x v alpha beta")
        P = lambda value: value**3 + value
        residual = V**2 + k * V + k**2 + 1
        self.zero(P(V) - P(k) - (V - k) * residual)
        discriminant = sp.discriminant(residual, V)
        self.zero(discriminant + 3 * k**2 + 4)
        self.assertEqual(sp.gcd(discriminant, sp.diff(discriminant, k)), 1)
        simple_root = 2 * sp.I / sp.sqrt(3)
        self.zero(discriminant.subs(k, simple_root))
        self.assertNotEqual(sp.simplify(sp.diff(discriminant, k).subs(k, simple_root)), 0)
        # Odd valuation at this root obstructs a square in C(rho)(k).
        # The written proof identifies the resulting quadratic constant field.
        self.zero(sp.diff(V, U))
        self.zero(sp.diff(U, U) - 1)
        self.zero(sp.rem(P(V) - P(k), residual, V))
        self.assertEqual(sp.degree(sp.rem(V - k, residual, V), V), 1)

        # Source-field ratios agree on the residual component, but its
        # primitive element V is algebraic over and not contained in L.
        omega = rho * (3 * V**2 + 1)
        self.zero(omega / (3 * V**2 + 1) - rho)
        Y, Z = v + P(k) * x, k + rho * x
        W = rho * (3 * k**2 + 1) + 3 * k * rho**2 * x + rho**3 * x**2
        self.zero(x * W - P(Z) + P(k))
        original_jacobian = sp.Matrix((x, Y, Z, W)).jacobian((x, k, rho, v))
        self.zero(original_jacobian.det() - (3 * k**2 + 1))
        self.assertGreater(sp.degree(original_jacobian.det(), k), 0)

        # After the written no-finite-poles argument, an automorphism must
        # send k to alpha*k+beta. Exact coefficient comparison forces identity.
        affine_residual = sp.Poly(P(alpha * k + beta) - P(k), k)
        self.zero(affine_residual.nth(3) - (alpha**3 - 1))
        self.zero(affine_residual.nth(2) - 3 * alpha**2 * beta)
        self.zero(affine_residual.nth(1) - (3 * alpha * beta**2 + alpha - 1))
        conditions = [affine_residual.nth(j) for j in range(4)]
        basis = sp.groebner(conditions, alpha, beta, order="lex")
        self.assertEqual(set(p.as_expr() for p in basis.polys), {alpha - 1, beta})

    def test_formal_split_tail_can_fail_initial_base_return(self):
        a, rho, q, X, U, V, intrinsic = sp.symbols("a rho q X U V intrinsic")
        Y, Z, W = q + a * X, a + rho * X, -2 * rho * a - rho**2 * X
        original = sp.Matrix((X, Y, Z, W)).jacobian((X, a, rho, q))
        self.zero(original.det() + 2 * a)
        normalized = [value.subs(q, -intrinsic / (2 * a)) for value in (Y, Z, W)]
        self.zero(sp.Matrix(normalized).jacobian((a, rho, intrinsic)).det() - 1)

        def selected(expression):
            return sp.cancel((X * sp.diff(expression, a) - sp.diff(expression, rho)
                              - X**2 * sp.diff(expression, q)) / (2 * a))

        for value, target in zip((X, Y, Z, W), (0, 0, 0, 1)):
            self.zero(selected(value) - target)
        self.zero(Z**2 + X * W - a**2)
        omega, phi, psi = -2 * rho * V, V**2 - a**2, -2 * a * U
        self.zero(phi - (V - a) * (V + a))
        self.zero(psi.subs({U: q, V: a}, simultaneous=True) + 2 * a * q)
        # The second component is a line over the same L, and Psi remains
        # transcendental there. It nevertheless sends source tau=z to -a.
        self.zero(phi.subs(V, -a))
        self.zero((-omega / (2 * V)).subs(V, -a) - rho)
        self.assertNotEqual(sp.expand((-a) - a), 0)
        self.zero(sp.diff(psi, U) + 2 * a)
        self.zero(sp.diff(psi, U) - sp.diff(phi, a))
        self.zero(sp.diff(psi, V) - sp.diff(phi, rho))

        # Signed reconstruction before imposing branch^2=Z^2+XW.
        x, y, z, w, branch = sp.symbols("x y z w branch")
        Q = z**2 + x * w
        branch_substitution = {X: x, a: branch, rho: (z - branch) / x, q: y - branch * x}
        reconstructed = [sp.cancel(value.subs(branch_substitution, simultaneous=True))
                         for value in (X, Y, Z, W)]
        for value, target, error in zip(reconstructed, (x, y, z, w),
                                        (0, 0, 0, (branch**2 - Q) / x)):
            self.zero(value - target - error)
        self.assertGreater(sp.degree(original.det(), a), 0)

    def test_recovered_template_jacobian_and_actual_positive_inverses(self):
        u, fv, fb, gv, gb, P_at_X, P_at_v = sp.symbols("u f_v f_b g_v g_b P_at_X P_at_v")
        formal_matrix = sp.Matrix(((1 + u * fv, u * fb),
                                   (gv + P_at_X * fv + (P_at_X - P_at_v) / u,
                                    gb + P_at_X * fb)))
        expected = gb + P_at_v * fb + u * (fv * gb - fb * gv)
        self.zero(formal_matrix.det() - expected)
        # Independent derivative jets are an identity control, not a
        # realization or a finite proof of the coupled-speed exclusion.

        a, b, v, t, X, Y, Z, W, A, U, V, beta = sp.symbols("a b v t X Y Z W A U V beta")
        c = sp.Symbol("c", nonzero=True)
        speed = a**2 + a + 1
        speed_prime = sp.diff(speed, a)
        G = a * v + v**2
        g = c * b + G
        for F in (t**3 / 2 + t + 2, t**4 + t**2 - t):
            with self.subTest(F=F):
                delta = self.divided_difference(F, t, speed, v, u)
                forward = (v + u * speed, a - F.subs(t, v) + u * g, u, g + delta)
                fx, fy, fz, fw = forward
                self.zero(u * delta - F.subs(t, fx) + F.subs(t, v))
                self.zero(fy - fz * fw + F.subs(t, fx) - a)
                recovered_a = sp.cancel(fy - fz * fw + F.subs(t, fx))
                recovered_v = sp.cancel(fx - fz * speed.subs(a, recovered_a))
                recovered_b = sp.cancel((fw - self.divided_difference(
                    F, t, speed.subs(a, recovered_a), recovered_v, fz
                ) - G.subs({a: recovered_a, v: recovered_v}, simultaneous=True)) / c)
                self.zero(recovered_a - a)
                self.zero(recovered_v - v)
                self.zero(recovered_b - b)
                self.zero(fz - u)

                # Reverse composition with independent A keeps the algebra
                # small. The sole residual is the monic recovered-A identity,
                # so substituting A=Y-ZW+F(X) completes the polynomial inverse.
                inv_u = Z
                inv_speed = speed.subs(a, A)
                inv_v = X - Z * inv_speed
                inv_delta = self.divided_difference(F, t, inv_speed, inv_v, Z)
                inv_G = G.subs({a: A, v: inv_v}, simultaneous=True)
                inv_b = (W - inv_delta - inv_G) / c
                reverse = (inv_v + Z * inv_speed,
                           A - F.subs(t, inv_v) + Z * (c * inv_b + inv_G),
                           inv_u, c * inv_b + inv_G + inv_delta)
                errors = (0, A - (Y - Z * W + F.subs(t, X)), 0, 0)
                for value, target, error in zip(reverse, (X, Y, Z, W), errors):
                    self.zero(value - target - error)
                jacobian = sp.Matrix(forward).jacobian((u, a, v, b))
                self.zero(jacobian.det(method="domain-ge") + c)
                self.assertEqual(sp.degree(fw, u), sp.degree(F, t) - 1)

                T_b = (1 + u * speed_prime * sp.diff(F.subs(t, v), v)
                       + u * sp.diff(G, a) - u**2 * speed_prime * sp.diff(G, v)) / c

                def selected(expression):
                    return sp.cancel(-u * sp.diff(expression, a) + T_b * sp.diff(expression, b)
                                     + u**2 * speed_prime * sp.diff(expression, v))

                for value, target in zip(forward, (0, 0, 0, 1)):
                    self.zero(selected(value) - target)
                self.zero(selected(g) - 1 - u * speed_prime * sp.diff(F.subs(t, v), v))
                top = lambda f: sp.cancel(speed_prime * (
                    sp.diff(f, v) - sp.diff(G, v) * sp.diff(f, b) / c))
                self.zero(top(a))
                self.zero(top(g))
                self.zero(top(v / speed_prime) - 1)
                self.zero(sp.Matrix((speed, g)).jacobian((a, b)).det() - c * speed_prime)

                dt = lambda f: sp.cancel(sp.diff(f, a) / speed_prime)

                def H(f, order):
                    total = sp.S.Zero
                    for i in range(order + 1):
                        term = sp.diff(f, beta, order - i)
                        for _ in range(i):
                            term = dt(term)
                        total += term * U**i * V ** (order - i) / (
                            sp.factorial(i) * sp.factorial(order - i))
                    return sp.cancel(total)

                degree = int(sp.degree(F, t))
                coefficients = [beta + sp.Poly(F, t).nth(1) * speed]
                coefficients.extend(sp.Poly(F, t).nth(j + 1) * speed ** (j + 1)
                                    for j in range(1, degree))
                fm1 = sp.Poly(F, t).nth(0) - a
                phi = -sum((H(fj, j + 1) for j, fj in enumerate(coefficients)), sp.S.Zero) - fm1
                psi = -sum((H(fj, j + 2) for j, fj in enumerate(coefficients)), sp.S.Zero) - H(fm1, 1)
                self.zero(phi - a + V + F.subs(t, U))
                self.zero(psi - U / speed_prime)
                self.zero(psi.subs({U: v, V: a - F.subs(t, v)}, simultaneous=True) - v / speed_prime)
                self.assertEqual(sp.degree(phi, V), 1)
                self.assertEqual(sp.Poly(phi, U, V).total_degree(), degree)


if __name__ == "__main__":
    unittest.main()
