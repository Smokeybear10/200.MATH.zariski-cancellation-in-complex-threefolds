"""Exact controls for two different failures of naive coordinate descent.

The first fixture is an actual polynomial automorphism from the retained
Chamberland--van den Essen seed. Its generic projected plane equation
splits over a divisor, although the full invariant algebra is polynomial.
The second has a globally valid plane equation but a pole in the canonical
normalized parameter. These are not cancellation counterexamples.

Only unittest and SymPy are imported. Finite identities supplement the
written proofs; this is not proof-assistant verification of those proofs.
"""

import unittest

import sympy as sp


class DivisorialDescentControls(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(sp.cancel(sp.expand(value)), 0)

    def test_actual_seed_inverse_dense_speeds_and_intrinsic_derivation(self):
        h, k, a, u = sp.symbols("h k a u")
        X, Y, Z, W = sp.symbols("X Y Z W")
        source = (h, k, a, u)
        target = (X, Y, Z, W)
        frame = (h + a**2 + k*u, a + h*u, k - 2*a*h - h**2*u, u)
        recovered_h = X - Y**2 - W*Z
        recovered_a = Y - W*recovered_h
        recovered_k = Z + W*recovered_h**2 + 2*recovered_a*recovered_h
        inverse = (recovered_h, recovered_k, recovered_a, W)
        forward_map = dict(zip(target, frame))
        inverse_map = dict(zip(source, inverse))
        for expression, expected in zip(inverse, source):
            self.zero(expression.subs(forward_map, simultaneous=True) - expected)
        for expression, expected in zip(frame, target):
            self.zero(expression.subs(inverse_map, simultaneous=True) - expected)
        speeds = sp.Matrix([sp.diff(f, u) for f in frame[:3]])
        self.assertEqual(speeds, sp.Matrix([k, h, -h**2]))
        for f in frame:
            self.zero(sp.diff(f, u, 2))
        radial = sp.Matrix.hstack(speeds, speeds.diff(h), speeds.diff(k)).det()
        self.zero(radial + h**2)
        self.assertNotEqual(radial, 0)
        tau, rho = h/k, -h**2/k
        self.zero(-rho/tau - h)
        self.zero(-rho/tau**2 - k)
        T = [sp.expand(sp.diff(f, W).subs(forward_map, simultaneous=True)) for f in inverse]
        expected_T = [
            -k + 2*a*h + h**2*u,
            -h**2 - 2*a*k + 4*a**2*h + 2*a*h**2*u,
            -h + (k - 2*a*h)*u - h**2*u**2,
            sp.S.One,
        ]
        for actual, expected in zip(T, expected_T):
            self.zero(actual - expected)
        for actual, expected in zip(T[:3], (0, 0, -h**2)):
            self.zero(actual.coeff(u, 2) - expected)
        for expression, expected in zip(frame, (0, 0, 0, 1)):
            self.zero(sum(T[i]*sp.diff(expression, source[i]) for i in range(4)) - expected)

    def test_generic_coordinate_special_fiber_and_overring_repair(self):
        h, k, a, U, V, C, D0, G0, q = sp.symbols("h k a U V C D0 G0 q")
        y = a - h*(h + a**2)/k
        z = k - 2*a*h + h**2*(h + a**2)/k
        w0 = -(h + a**2)/k
        D = V + h*U
        G = D**2 - k*V + h**3
        self.zero(G.subs({U: y, V: z}, simultaneous=True))
        self.zero(D.subs({U: y, V: z}, simultaneous=True) - (k - a*h))
        inv_V = (D0**2 + h**3 - G0)/k
        inv_U = (D0 - inv_V)/h
        self.zero(inv_V.subs({D0: D, G0: G}, simultaneous=True) - V)
        self.zero(inv_U.subs({D0: D, G0: G}, simultaneous=True) - U)
        self.zero(D.subs({U: inv_U, V: inv_V}, simultaneous=True) - D0)
        self.zero(G.subs({U: inv_U, V: inv_V}, simultaneous=True) - G0)
        self.zero(G.subs(h, 0) - V*(V-k))
        self.zero((V/k) - ((V-k)/k) - 1)  # Coprime factors after k is inverted.
        self.zero(y.subs(h, 0) - a)
        self.zero(z.subs(h, 0) - k)  # The actual fiber picks V=k, not V=0.
        self.zero(y - h*w0 - a)  # Full projected overring recovers a without 1/h.
        self.zero((k-z-h*y)/h - a)
        # Adjoining a=(k-D)/h to the projected subring gives exactly R[a].
        self.zero(w0 + (h+a**2)/k)
        relation1 = h+U**2+C*V
        relation2 = k-V-2*h*U+C*h**2
        actual_map = {U: y, V: z, C: w0}
        self.zero(relation1.subs(actual_map, simultaneous=True))
        self.zero(relation2.subs(actual_map, simultaneous=True))
        a_star = U-h*C
        self.zero(h+a_star**2+k*C-relation1-C*relation2)
        # The inverse presentation is polynomial over S_k, not S_(hk).
        self.zero(k*w0+h+a**2)
        self.zero(y-a-h*w0)
        self.zero(z-k+2*h*y-h**2*w0)
        # Both rational parameter formulas agree wherever their respective
        # denominators are invertible. They cover the actual invariant ring.
        q_actual = z+h*y
        self.zero(q_actual*(k-q_actual)-h*(k*y+h**2))
        self.zero((k*y+h**2)/q_actual-a)
        self.zero(q_actual+h*a-k)
        # The second projected component is at parameter infinity. It is
        # parametrized over Laurent series by a=k/h-q; q remains arbitrary.
        pole_y = sp.cancel(y.subs(a, k/h-q))
        pole_z = sp.cancel(z.subs(a, k/h-q))
        self.zero(pole_y - (q - h*q**2/k - h**2/k))
        self.zero(pole_z - (h**3/k + h**2*q**2/k))
        pole_w = sp.cancel(w0.subs(a, k/h-q))
        self.zero(sp.limit(h**2*pole_w, h, 0) + k)
        # Although the zero hypersurface is smooth in the special fiber,
        # the full-plane gradient vanishes away from that zero level.
        self.zero(sp.diff(G, U).subs(h, 0))
        self.zero(sp.diff(G, V).subs(h, 0) - (2*V-k))
        self.zero(G.subs({h: 0, V: k/2}) + k**2/4)
        self.zero(sp.diff(G, U)-h*sp.diff(G, V)-h*k)
        self.zero(sp.diff(G, V)**2-4*G+4*h*(k*U+h**2)-k**2)

    def test_canonical_tail_matches_the_degenerate_primitive_equation(self):
        h, k, a, U, V, tau, rho = sp.symbols("h k a U V tau rho")
        f1, f0, fminus = -tau**2/rho, 1/rho, 1/tau
        base_map = {tau: h/k, rho: -h**2/k}

        def H(order, value):
            return sum(sp.diff(value, tau, i, rho, order-i)
                       * U**i * V**(order-i)
                       / (sp.factorial(i)*sp.factorial(order-i))
                       for i in range(order+1))

        phi = sp.cancel((-H(2, f1)-H(1, f0)-fminus).subs(base_map, simultaneous=True))
        psi = sp.cancel((-H(3, f1)-H(2, f0)-H(1, fminus)).subs(base_map, simultaneous=True))
        D = V+h*U
        G = D**2-k*V+h**3
        self.zero(phi + k*G/h**4)
        self.zero(psi - k**2*D/h**3 + k**2*V*G/h**6)
        y = a - h*(h+a**2)/k
        z = k - 2*a*h + h**2*(h+a**2)/k
        source_map = {U: y, V: z}
        self.zero(phi.subs(source_map, simultaneous=True))
        self.zero(psi.subs(source_map, simultaneous=True) + k**2*a/h**2 - k**3/h**3)
        self.zero((-h**2/k**2)*sp.diff(-k**2*a/h**2, a) - 1)
        # Check the nonnegative peeling and the first evaluated remainder.
        self.zero(f1.subs(base_map, simultaneous=True) - 1/k)
        self.zero((H(1, f1)+f0).subs(base_map, simultaneous=True)
                  .subs(source_map, simultaneous=True) + (h+a**2)/k)
        self.zero(fminus.subs(base_map, simultaneous=True) - k/h)

    def test_normalized_parameter_can_have_a_pole_with_a_good_plane_equation(self):
        a, b, v, u, U, V = sp.symbols("a b v u U V")
        X, Y, Z, W = sp.symbols("X Y Z W")
        P = a**2+1
        F = lambda r: r**3/2
        delta = sp.cancel((F(v+P*u)-F(v))/u)
        sp.Poly(delta, a, v, u)  # The divided difference is polynomial at u=0.
        frame = (v+P*u, a-F(v)+b*u, u, b+delta)
        A = Y-Z*W+F(X)
        inv_v = X-Z*(A**2+1)
        inv_delta = sp.expand(
            sp.Rational(3, 2)*inv_v**2*(A**2+1)
            + sp.Rational(3, 2)*inv_v*(A**2+1)**2*Z
            + sp.Rational(1, 2)*(A**2+1)**3*Z**2
        )
        inv_b = W-inv_delta
        source = (a, b, v, u)
        target = (X, Y, Z, W)
        # Factored staged recovery avoids a large gratuitous expansion.
        forward_map = dict(zip(target, frame))
        recovered_a = sp.cancel(A.subs(forward_map, simultaneous=True))
        recovered_v = sp.cancel(frame[0]-frame[2]*(recovered_a**2+1))
        recovered_b = sp.cancel(frame[3]-delta.subs(
            {a: recovered_a, v: recovered_v}, simultaneous=True))
        for actual, expected in zip((recovered_a, recovered_b, recovered_v, frame[2]), source):
            self.zero(actual-expected)
        # Last two recoveries and X are tautological; Y reduces by the
        # divided-difference polynomial identity at the same formal values.
        self.zero(inv_v+(A**2+1)*Z-X)
        self.zero(inv_b+inv_delta-W)
        self.zero(A-F(inv_v)+inv_b*Z-Y)
        for expression in frame[:3]:
            self.zero(sp.diff(expression, u, 2))
        self.zero(sp.diff(frame[3], u, 2)-P**3)
        G = a-V-U**3/2
        self.zero(G.subs({U: v, V: a-v**3/2}, simultaneous=True))
        self.zero(sp.diff(G, V)+1)
        normalized = v/(2*a)
        self.zero(2*a*sp.diff(normalized, v)-1)
        self.zero(sp.limit(a*normalized, a, 0)-v/2)
        self.zero(P.subs(a, 0)-1)  # Inverting P does not remove the pole divisor.
        for sample in (v, a*v, v**2+b*v, a**2*v**3+b):
            derivative = sp.expand(2*a*sp.diff(sample, v))
            self.zero(derivative.subs(a, 0))
        # These samples supplement, not replace, the written all-polynomial
        # divisibility proof N(S[v])=a*S[v].


if __name__ == "__main__":
    unittest.main()
