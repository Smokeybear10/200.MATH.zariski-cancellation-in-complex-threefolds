"""Finite exact controls for divisorial noncollapse and residue degrees147.

The first method uses the actual inverse-verified dense146 frame. The
second uses an abstract triangular LND on C[p,U,V], not a claimed
selected derivation of an actual dense four-coordinate frame. Its finite
quotient arithmetic does not prove the universal residue-degree bound
or the all-degree irreducibility statement. No previous checker, search,
or solver internals are imported, and no numerical sampling is used.
"""

import unittest

import sympy as sp


class DivisorResidueControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_actual_divisor_needs_rescaled_leading_derivation(self):
        h, k, a, u = sp.symbols("h k a u")
        X, Y, Z, W = sp.symbols("X Y Z W")
        source, target = (h, k, a, u), (X, Y, Z, W)
        frame = (h + a**2 + k*u, a + h*u, k - 2*a*h - h**2*u, u)
        H = X - Y**2 - W*Z
        recovered_a = Y - W*H
        inverse = (H, Z + 2*H*Y - W*H**2, recovered_a, W)
        for expression, expected in zip(inverse, source):
            self.zero(expression.subs(dict(zip(target, frame)), simultaneous=True) - expected)
        for expression, expected in zip(frame, target):
            self.zero(expression.subs(dict(zip(source, inverse)), simultaneous=True) - expected)
        speeds = sp.Matrix([sp.diff(expression, u) for expression in frame[:3]])
        self.assertEqual(speeds, sp.Matrix([k, h, -h**2]))
        self.zero(sp.Matrix.hstack(speeds, speeds.diff(h), speeds.diff(k)).det() + h**2)
        for expression in frame:
            self.zero(sp.diff(expression, u, 2))
        self.zero(sp.diff(frame[3], u) - 1)

        transported = [sp.expand(sp.diff(expression, W).subs(
            dict(zip(target, frame)), simultaneous=True)) for expression in inverse]
        leading = [sp.expand(expression).coeff(u, 2) for expression in transported[:3]]
        self.assertEqual(leading, [0, 0, -h**2])
        for expression, expected in zip(frame, (0, 0, 0, 1)):
            self.zero(sum(coefficient * sp.diff(expression, variable)
                          for coefficient, variable in zip(transported, source)) - expected)

        # Work over S_k=C[h,k,k^-1]; p=(h) survives since k is a unit.
        initial_time = -(h + a**2)/k
        y = sp.cancel(frame[1].subs(u, initial_time))
        z = sp.cancel(frame[2].subs(u, initial_time))
        self.zero(frame[0].subs(u, initial_time))
        self.assertEqual(sp.degree(y, a), 2)
        self.assertEqual(sp.degree(z, a), 2)
        ybar, zbar = sp.cancel(y.subs(h, 0)), sp.cancel(z.subs(h, 0))
        self.zero(ybar - a)
        self.zero(zbar - k)
        self.assertEqual(sp.degree(ybar, a), 1)
        self.assertEqual(sp.degree(zbar, a), 0)
        self.zero(speeds[0].subs(h, 0) - k)

        # N=-h^2*d/da kills the coefficient ring. Its direct reduction
        # is zero, while the valid coefficient division gives D=-d/da.
        N = lambda expression: -h**2 * sp.diff(expression, a)
        D = lambda expression: -sp.diff(expression, a)
        for expression in (h, k, a, y, z, a**2 + k*a):
            self.zero(N(expression) - h**2 * D(expression))
            self.zero(N(expression).subs(h, 0))
        self.zero(D(h))
        self.zero(D(k))
        self.zero(D(y).subs(h, 0) + 1)
        self.zero(D(z).subs(h, 0))
        # Thus one projected good survives nonconstantly. The statement
        # is not that both degrees stay unchanged on the divisor.
        normalized = -k**2*a/h**2
        self.zero((-h**2/k**2) * sp.diff(normalized, a) - 1)
        self.zero(sp.cancel(h**2 * normalized).subs(h, 0) + k**2*a)

    def test_abstract_triangular_family_has_finite_residue_constants(self):
        p, U, V, eta, T = sp.symbols("p U V eta T")
        for d in (2, 3):
            with self.subTest(degree=d):
                eta_source = p*V - U**d
                delta = lambda expression: p*sp.diff(expression, U) + d*U**(d-1)*sp.diff(expression, V)
                self.zero(delta(p))
                self.zero(delta(eta_source))
                self.zero(delta(delta(U)))
                iterate = V
                for j in range(1, d + 1):
                    iterate = sp.expand(delta(iterate))
                    self.zero(iterate - sp.factorial(d)/sp.factorial(d-j)
                              * p**(j-1) * U**(d-j))
                self.zero(delta(iterate))
                self.assertNotEqual(iterate, 0)

                # Generic localization over L=C(p,eta) is explicitly L[U].
                generic_V = (eta + U**d)/p
                self.zero(p*generic_V - U**d - eta)
                self.zero(generic_V.subs(eta, eta_source) - V)
                self.assertEqual(sp.degree(generic_V, U), d)

                # At p=0 the coefficient fiber is K[U,V]/(U^d+eta),
                # K=C(eta). The polynomial U^d+eta is Eisenstein at the
                # prime eta in C[eta][U], hence irreducible over C(eta).
                # The finite quotient checks below are not that proof.
                relation = U**d + eta
                rem = lambda expression: sp.rem(sp.expand(expression), relation, U, domain=sp.EX)
                self.zero(eta_source.subs(p, 0) + U**d)
                self.zero(relation.subs(eta, -U**d))
                self.assertEqual(sp.degree(relation, U), d)
                for j in range(d):
                    self.zero(rem(U**j) - U**j)
                self.zero(rem(U**d) + eta)
                # U is a unit after the actual base residue eta is inverted.
                self.zero(rem(U * (-U**(d-1)/eta) - 1))
                self.zero(relation - U*sp.diff(relation, U)/d - eta)

                reduced_delta = lambda expression: d*U**(d-1)*sp.diff(expression, V)
                residue_slice = -U*V/(d*eta)
                self.zero(rem(reduced_delta(residue_slice) - 1))
                self.zero(reduced_delta(U))
                self.zero(reduced_delta(eta))
                self.assertEqual(sp.degree(V, V), 1)
                self.zero(rem(reduced_delta(reduced_delta(V))))
                # In this example generic degree d equals extension degree d
                # times the surviving V-degree 1. Finite arithmetic alone is
                # not a proof of the universal bound or of field irreducibility.
                self.assertEqual(sp.degree(generic_V, U), sp.degree(relation, U) * sp.degree(V, V))
                # eta=-T^d embeds the coefficient field into C(T); the
                # selected algebraic residue U=T satisfies exactly this relation.
                self.zero(relation.subs({U: T, eta: -T**d}, simultaneous=True))


if __name__ == "__main__":
    unittest.main()
