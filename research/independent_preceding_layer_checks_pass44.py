"""Two exact controls for the independent preceding-layer reduction.

The first uses polynomial lower-layer data and an actual sliced field,
but not the required identification as iterates of an ambient frame.
The second uses an actual normalizer model, not an independent-defect
high-flow realization. Neither replaces the written rank/source proof.
"""

import unittest

import sympy as sp


def clean(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda entry: sp.cancel(sp.expand(entry)))
    return sp.cancel(sp.expand(value))


def act(field, value, variables):
    return clean(sum(a * sp.diff(value, x)
                     for a, x in zip(field, variables)))


def bracket(left, right, variables):
    return clean(sp.Matrix([act(left, b, variables) - act(right, a, variables)
                            for a, b in zip(left, right)]))


class IndependentPrecedingLayerChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(clean(value), sp.zeros(*value.shape))
        else:
            self.assertEqual(clean(value), 0)

    def test_polynomial_lower_layer_cancellation_with_noncoordinate_parameter(self):
        x, y, v, w = sp.symbols("x y v w")
        variables = (x, y, v, w)
        u = x * y
        g = (u - 1)**2 * (u + 2)
        r = u**2 + 1
        lam = sp.Matrix([2, -3])
        direction = sp.Matrix([1, 0, 0, 0])
        for m in (3, 4, 5):
            tau = g * v - r
            k = sp.Matrix([0, u**2 + u, 2 * g**(m - 1), -3 * g**(m - 1)])
            z = direction * tau + k
            b = sp.Matrix([2 * v, -3 * v + u**3 + u])
            q = clean(g * b - lam * tau)
            E = sp.Matrix([0, 0, g**(m - 1), 1])
            self.assertZero(act(E, w, variables) - 1)
            self.assertZero(act(E, tau, variables) - g**m)
            self.assertZero(sp.Matrix([act(E, point, variables) for point in z])
                            - direction * g**m)
            self.assertZero(sp.Matrix([act(E, point, variables) for point in b])
                            - lam * g**(m - 1))
            self.assertEqual(sp.Matrix.vstack(z, b).jacobian(variables).rank(), 2)
            curve = sp.Matrix.vstack(sp.Matrix([g]), k, q)
            self.assertEqual(curve.jacobian(variables).rank(), 1)
            self.assertZero(k[1] - q[0] / 2 + 1 - u)
            recovered_v = b[0] / lam[0]
            recovered_r = q[0] / lam[0]
            self.assertZero(recovered_v - v)
            self.assertZero(recovered_r - r)
            self.assertZero(tau - g * recovered_v + recovered_r)
            lower_remainder = clean(b - lam * recovered_v)
            self.assertZero(lower_remainder - sp.Matrix([0, u**3 + u]))
            self.assertZero(lower_remainder - (q - lam * recovered_r) / g)
            self.assertTrue(all(point.is_polynomial(*variables)
                                for point in lower_remainder))
        # The parameter has reducible zero fiber; it is not being treated
        # as an ambient coordinate merely because it generates a curve field.
        self.assertEqual(sp.factor(u), x*y)
        # Polynomiality of b is essential for the claimed intersection gate.
        uncancelled = clean(u**3 + u + 1/g)
        self.assertFalse(uncancelled.is_polynomial(*variables))
        self.assertNotEqual(sp.numer(uncancelled).subs({x: 1, y: 1}), 0)

    def test_lower_exponent_replica_with_nonzero_horizontal_correction(self):
        g, w, b, z = sp.symbols("g w b z")
        variables = (g, w, b, z)
        E = sp.Matrix([0, 1, g*w, b])
        Tc = sp.Matrix([0, 0, 1, 0])
        Tlambda = sp.Matrix([0, 1, 0, 0])
        W = bracket(E, Tlambda, variables)
        V = bracket(E, W, variables)
        Y = clean(g * Tc + 2 * W)
        self.assertZero(V - sp.Matrix([0, 0, 0, g]))
        self.assertZero(Y - sp.Matrix([0, 0, -g, 0]))
        self.assertZero(bracket(E, Y, variables) - V)
        self.assertZero(bracket(Y, V, variables))
        invariant = b - g*w**2/2
        self.assertZero(act(E, invariant, variables))
        lower_v = g**2*w + invariant
        r = g**2 + g + 1
        tau = g*lower_v - r
        self.assertZero(act(E, lower_v, variables) - g**2)
        self.assertZero(act(E, tau, variables) - g**3)
        self.assertZero(act(V, lower_v, variables))
        Yv = act(Y, lower_v, variables)
        self.assertZero(Yv + g)
        self.assertNotEqual(Yv, 0)

        delta, L, C = E/g, Y/g, V/g**2
        sigma = lower_v/g
        self.assertZero(act(delta, sigma, variables) - 1)
        self.assertZero(act(C, sigma, variables))
        D0 = clean(L - sigma*C - act(L, sigma, variables)*delta)
        R1 = clean(g**2*Y - lower_v*V - Yv*E)
        self.assertZero(g**3*D0 - R1)
        self.assertTrue(all(value.is_polynomial(*variables) for value in R1))
        self.assertZero(R1 - sp.Matrix([0, g, g**2*w-g**3,
                                       g**2*w**2/2-g**3*w]))
        for field in (E, V):
            self.assertZero(bracket(field, R1, variables))
        for point in (g, lower_v):
            self.assertZero(act(R1, point, variables))
        for point in variables:
            value = point
            for unused in range(4):
                value = act(R1, value, variables)
            self.assertZero(value)
        R43 = clean(g**3*Y - tau*V - act(Y, tau, variables)*E)
        self.assertZero(R43 - g*R1 - r*V)
        self.assertZero(act(E, lower_v/g**2, variables) - 1)
        self.assertZero(act(V, lower_v/g**2, variables))
        # This tests the displayed smaller exponent, not its minimality.


if __name__ == "__main__":
    unittest.main()
