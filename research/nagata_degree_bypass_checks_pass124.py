"""Exact finite controls for the written Nagata degree-bypass argument.

Independent of research solvers and prior checker modules. These tests
certify explicit identities, not universal cancellation or termination.
"""

import unittest

import sympy as sp


class NagataDegreeBypassChecks(unittest.TestCase):
    def setUp(self):
        self.u, self.v, self.z, self.w = sp.symbols("u v z w")
        self.variables = (self.u, self.v, self.z, self.w)

    @staticmethod
    def expand_tuple(values):
        return tuple(sp.expand(value) for value in values)

    def degrees(self, values):
        return tuple(sp.Poly(value, self.u).degree() for value in values)

    def test_nagata_inverse_and_failed_nonunit_replacement(self):
        u, v, z, w = self.variables
        delta = z * u + v**2
        frame = (u - 2 * v * delta - z * delta**2, v + z * delta, z, w)
        inverse = (u + 2 * v * delta - z * delta**2, v - z * delta, z, w)
        for outer, inner in ((frame, inverse), (inverse, frame)):
            substitution = dict(zip(self.variables, inner))
            actual = [p.subs(substitution, simultaneous=True) for p in outer]
            self.assertEqual(self.expand_tuple(actual), self.variables)
        self.assertEqual(self.degrees(frame), (2, 1, 0, 0))
        invalid = sp.Matrix((z * u + v**2, v, z, w))
        self.assertEqual(invalid.jacobian(self.variables).det(), z)

    def test_six_elementary_moves_and_their_inverses(self):
        X, Y, Z, W = self.variables
        additions = (
            (3, Z * X + Y**2),
            (0, 2 * W * Y - W**2 * Z),
            (1, -W * Z),
            (3, -Z * X - Y**2),
            (0, -2 * W * Y - W**2 * Z),
            (1, W * Z),
        )
        for index, addition in additions:
            with self.subTest(index=index, addition=str(addition)):
                self.assertFalse(addition.has(self.variables[index]))
                forward = list(self.variables)
                reverse = list(self.variables)
                forward[index] += addition
                reverse[index] -= addition
                for outer, inner in ((forward, reverse), (reverse, forward)):
                    actual = [p.subs(dict(zip(self.variables, inner)),
                                     simultaneous=True) for p in outer]
                    self.assertEqual(self.expand_tuple(actual), self.variables)
                self.assertEqual(sp.Matrix(forward).jacobian(self.variables).det(), 1)

    def test_replica_factorizations_and_exact_degree_traces(self):
        u, v, z, w = self.variables
        T = sp.Symbol("T")
        polynomials = (T, T**2, z * T**2 + T + 1, T**3 + z * T, T**4 + z)
        for f in polynomials:
            with self.subTest(f=str(f)):
                m = sp.Poly(f, T).degree()
                delta = z * u + v**2
                h = f.subs(T, delta)
                current = list(self.expand_tuple(
                    (u - 2 * v * h - z * h**2, v + z * h, z, w)))
                trace = [self.degrees(current)]
                current[3] = sp.expand(current[3] +
                    f.subs({z: current[2], T: current[2] * current[0] + current[1]**2},
                           simultaneous=True))
                trace.append(self.degrees(current))
                current[0] = sp.expand(current[0] + 2 * current[3] * current[1]
                                       - current[3]**2 * current[2])
                trace.append(self.degrees(current))
                current[1] = sp.expand(current[1] - current[3] * current[2])
                trace.append(self.degrees(current))
                self.assertEqual(self.expand_tuple(current[:3]),
                                 (u + 2 * w * v - w**2 * z, v - w * z, z))
                current[3] = sp.expand(current[3] -
                    f.subs({z: current[2], T: current[2] * current[0] + current[1]**2},
                           simultaneous=True))
                trace.append(self.degrees(current))
                current[0] = sp.expand(current[0] - 2 * current[3] * current[1]
                                       - current[3]**2 * current[2])
                trace.append(self.degrees(current))
                current[1] = sp.expand(current[1] + current[3] * current[2])
                trace.append(self.degrees(current))
                self.assertEqual(tuple(current), self.variables)
                self.assertEqual(trace, [(2*m, m, 0, 0), (2*m, m, 0, m),
                                        (1, m, 0, m), (1, 0, 0, m),
                                        (1, 0, 0, 0), (1, 0, 0, 0),
                                        (1, 0, 0, 0)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
