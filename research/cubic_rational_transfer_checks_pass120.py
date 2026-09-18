"""One exact rational/finite-field transfer control, not an actual frame.

H=s/t and w=s**2+t**2 give a degree-two extension
C(s,t)/C(H,w). The displayed derivations and pulled-back volume are
finite identities. They do not prove the general constant-field or
actual-generation hypotheses of cubic-general-ruled-exclusion120.
The pulled-back coordinate expressions are deck-invariant, so this
control expressly does not supply an original polynomial inverse.
"""

import unittest

import sympy as sp


class RationalTransferChecks(unittest.TestCase):
    def test_quadratic_field_transfer_and_missing_original_inverse(self):
        s, t, u, v, h, w, theta = sp.symbols("s t u v h w theta")
        H, W = s / t, s**2 + t**2

        def zero(value):
            self.assertEqual(sp.cancel(value), 0)

        def dh(value):
            return sp.cancel((t**3 * sp.diff(value, s)
                              - s * t**2 * sp.diff(value, t)) / W)

        def dw(value):
            return sp.cancel((s * sp.diff(value, s)
                              + t * sp.diff(value, t)) / (2 * W))

        base = sp.Matrix([H, W]).jacobian([s, t])
        delta = sp.cancel(base.det())
        zero(delta - 2 * W / t**2)
        inverse = sp.Matrix([[t**3 / W, s / (2 * W)],
                             [-s * t**2 / W, t / (2 * W)]])
        self.assertEqual((base * inverse).applyfunc(sp.cancel), sp.eye(2))
        self.assertEqual((inverse * base).applyfunc(sp.cancel), sp.eye(2))
        for value, expected in ((H, 1), (W, 0)):
            zero(dh(value) - expected)
            zero(dw(value) - (1 - expected))
        for value in (s, t, s * t, s**2 / t):
            zero(dh(dw(value)) - dw(dh(value)))

        # Exact quadratic relation. Its irreducibility is the written
        # odd-w-valuation argument, not a conclusion of these samples.
        relation = (h**2 + 1) * theta**2 - w
        zero(relation.subs({h: H, theta: t, w: W}, simultaneous=True))
        self.assertEqual(sp.Poly(relation, theta).degree(), 2)
        self.assertEqual(sp.Poly(relation.subs(theta, 0), w).degree(), 1)

        original = sp.Matrix([
            h * u + v,
            h + w * u + 3 * w * v / h + 4 * v**3,
            h**3 * u + 3 * h**2 * v,
            u**2 / 2 + 3 * v**2 / (2 * h**2) + w / h**3,
        ])
        substitution = {h: H, w: W}
        pulled = original.subs(substitution, simultaneous=True)
        old_jacobian = original.jacobian([u, h, w, v])
        new_jacobian = pulled.jacobian([u, s, t, v])
        transition = sp.Matrix([u, H, W, v]).jacobian([u, s, t, v])
        certificate = (new_jacobian
                       - old_jacobian.subs(substitution) * transition)
        self.assertEqual(certificate.applyfunc(sp.cancel), sp.zeros(4))
        zero(old_jacobian.det() + 2)
        zero(transition.det() - delta)
        zero(new_jacobian.det() + 2 * delta)

        # The nontrivial deck involution fixes every displayed output.
        # Therefore these outputs cannot recover s or t rationally.
        deck = {s: -s, t: -t}
        zero(H.subs(deck, simultaneous=True) - H)
        zero(W.subs(deck, simultaneous=True) - W)
        for value in pulled:
            zero(value.subs(deck, simultaneous=True) - value)
        self.assertNotEqual(sp.cancel(s.subs(deck) - s), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
