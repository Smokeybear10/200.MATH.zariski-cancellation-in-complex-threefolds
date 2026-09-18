"""Bounded exact controls for the constant-intercept cusp branch174.

Independent formal coefficient functions verify the determinant, its mixed
partial obstruction, and the resulting z-independent correction. The
polynomial W-shear is separately checked in both inverse orders. These
computations do not prove the field/localization return, existence of an
actual cusp frame for formal coefficients, or the Wang/BGL endpoint.
No older checker is imported or run. Canonical execution belongs to Root.
"""

import unittest

import sympy as sp


def zero(expression):
    assert sp.expand(expression) == 0, sp.expand(expression)


class ConstantInterceptCuspControls(unittest.TestCase):
    def test_literal_unrestricted_determinant_and_independence_gate(self):
        t, y, z, X = sp.symbols("t y z X")
        alpha, beta = sp.Function("alpha")(y), sp.Function("beta")(y)
        g, k, H, J, rho = [
            sp.Function(name)(t, y) for name in ("g", "k", "H", "J", "rho")
        ]
        sigma = 3 * t**2 * y + k
        w = alpha * z**2 + beta * z + g
        theta = H * z + J
        Y = y + t * X
        Z = z + sigma * X + t**3 * X**2
        W = w + theta * X + rho * X**2
        determinant = sp.Matrix(
            [[sp.diff(G, variable) for variable in (t, y, z)] for G in (Y, Z, W)]
        ).det()
        coefficients = sp.Poly(sp.expand(determinant), X)
        self.assertEqual(coefficients.degree(), 3)
        expected = {
            0: sp.diff(g, t),
            1: sp.diff(theta, t) - sp.diff(w, y)
            - sp.diff(sigma, t) * (2 * alpha * z + beta),
            2: sp.diff(rho, t) - sp.diff(theta, y)
            - H * sp.diff(sigma, t) + sp.diff(k, y) * (2 * alpha * z + beta),
            3: -sp.diff(rho, y) + H * sp.diff(k, y),
        }
        for degree in range(4):
            zero(coefficients.coeff_monomial(X**degree) - expected[degree])
        c1 = sp.Poly(sp.expand(expected[1]), z)
        zero(c1.coeff_monomial(z**2) + sp.diff(alpha, y))
        zero(c1.coeff_monomial(z) - sp.diff(H, t)
             + sp.diff(beta, y) + 2 * alpha * sp.diff(sigma, t))
        zero(sp.Poly(sp.expand(expected[2]), z).coeff_monomial(z)
             + sp.diff(H, y) - 2 * alpha * sp.diff(k, y))

        # If y_rho=0, the actual159 determinant has this first-row factor.
        # The finite identity does not replace the domain/unit-degree proof.
        yt = sp.Symbol("yt")
        aa, bb, cc, dd, ee, ff = sp.symbols("aa bb cc dd ee ff")
        blocked_matrix = sp.Matrix([[X + yt, 0, 0], [aa, bb, cc], [dd, ee, ff]])
        zero(blocked_matrix.det() - (X + yt) * (bb * ff - cc * ee))
        self.assertEqual(sp.Poly((X + yt) * (bb * ff - cc * ee), X).degree(), 1)

    def test_mixed_partial_obstruction_and_exact_shear_cancellation(self):
        t, y, z, X = sp.symbols("t y z X")
        alpha, beta = sp.Function("alpha")(y), sp.Function("beta")(y)
        k = sp.Function("k")(t, y)
        sigma = 3 * t**2 * y + k
        prescribed_Ht = 2 * alpha * sp.diff(sigma, t) + sp.diff(beta, y)
        prescribed_Hy = 2 * alpha * sp.diff(k, y)
        mixed = sp.diff(prescribed_Ht, y) - sp.diff(prescribed_Hy, t)
        zero(mixed - 2 * sp.diff(alpha, y) * sp.diff(sigma, t)
             - 12 * alpha * t - sp.diff(beta, y, 2))
        alpha0 = sp.Symbol("alpha0")
        reduced = 12 * alpha0 * t + sp.diff(beta, y, 2)
        zero(sp.diff(reduced, t) - 12 * alpha0)

        lam, nu, mu = sp.symbols("lam nu mu")
        beta_affine, H_affine = lam * y + nu, lam * t + mu
        zero(sp.diff(beta_affine, y, 2))
        zero(sp.diff(H_affine, y))
        zero(sp.diff(H_affine, t) - sp.diff(beta_affine, y))
        g, J, rho = [sp.Function(name)(t, y) for name in ("g", "J", "rho")]
        Y = y + t * X
        Z = z + sigma * X + t**3 * X**2
        W = beta_affine * z + g + (H_affine * z + J) * X + rho * X**2
        V = W - (lam * Y + nu + mu * X) * Z
        expected = (
            g + (J - beta_affine * sigma) * X
            + (rho - beta_affine * t**3 - H_affine * sigma) * X**2
            - H_affine * t**3 * X**3
        )
        zero(V - expected)
        zero(sp.diff(V, z))

        # An actual polynomial coordinate map of an independent four-ring.
        # It becomes an invariant-recognition step only under the proof's
        # separately established actual chart and coefficient hypotheses.
        XX, YY, ZZ, WW, VV = sp.symbols("XX YY ZZ WW VV")
        correction = (lam * YY + nu + mu * XX) * ZZ
        forward = (XX, YY, WW - correction, ZZ)
        inverse = (XX, YY, ZZ, VV + correction)
        forward_map = dict(zip((XX, YY, VV, ZZ), forward))
        inverse_map = dict(zip((XX, YY, ZZ, WW), inverse))
        for recovered, original in zip(inverse, (XX, YY, ZZ, WW)):
            zero(recovered.subs(forward_map, simultaneous=True) - original)
        for recovered, original in zip(forward, (XX, YY, VV, ZZ)):
            zero(recovered.subs(inverse_map, simultaneous=True) - original)

    def test_chart_partial_and_commuting_derivation_control(self):
        t, y, z, X = sp.symbols("t y z X")
        lam, nu, mu = sp.symbols("lam nu mu")
        speed, k, g, J, rho = [
            sp.Function(name)(t, y) for name in ("speed", "k", "g", "J", "rho")
        ]
        beta, H = lam * y + nu, lam * t + mu
        sigma = 3 * t**2 * y + k
        Y = y + t * X
        Z = z + sigma * X + t**3 * X**2
        W = beta * z + g + (H * z + J) * X + rho * X**2
        V = sp.expand(W - (lam * Y + nu + mu * X) * Z)
        E = lambda G: speed * sp.diff(G, X)
        Tz = lambda G: sp.diff(G, z)
        for G, value in zip((X, Y, V, Z), (0, 0, 0, 1)):
            zero(Tz(G) - value)
        for G in (t, y, z, X, Y, V, Z, W):
            zero(E(Tz(G)) - Tz(E(G)))
        zero(E(E(X)))
        zero(E(E(Y)))
        zero(E(E(Z)) - 2 * speed**2 * t**3)
        zero(sp.diff(E(V), z))

        # The coefficient's z-independence is essential for commutation.
        # This formal negative boundary is not an invariant selected speed.
        bad_E = lambda G: (speed + z) * sp.diff(G, X)
        zero(bad_E(Tz(X)) - Tz(bad_E(X)) + 1)


if __name__ == "__main__":
    unittest.main()
