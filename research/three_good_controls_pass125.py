"""Exact controls for pass125, not a checker for its universal theorems."""

import unittest

import sympy as s


def expand_tuple(values):
    return tuple(s.expand(value) for value in values)


class ThreeGoodControls(unittest.TestCase):
    def test_nonconstant_acceleration_and_proper_speed_ideal(self):
        a, x, y, c = s.symbols("a x y c")
        v, u = s.symbols("v u")
        inv_v = x + a * x**2 / 2 - a**2 * y
        inv_u = s.cancel(y + (inv_v**2 - x**2) / (2 * a))
        self.assertEqual(s.denom(inv_u), 1)
        x_fwd = v - a * v**2 / 2 + a**2 * u
        y_fwd = s.cancel(u + (x_fwd**2 - v**2) / (2 * a))
        self.assertEqual(s.denom(y_fwd), 1)
        to_original = {v: inv_v, u: inv_u}
        to_adapted = {x: x_fwd, y: y_fwd}
        self.assertEqual(
            expand_tuple(f.subs(to_original, simultaneous=True) for f in (x_fwd, y_fwd)),
            (x, y),
        )
        self.assertEqual(
            expand_tuple(f.subs(to_adapted, simultaneous=True) for f in (inv_v, inv_u)),
            (v, u),
        )
        self.assertEqual(s.expand(s.diff(y_fwd, u, 2)), a**3)
        self.assertEqual(s.expand(s.diff(x_fwd, u)), a**2)
        self.assertEqual(s.diff(inv_v, y), -a**2)
        self.assertEqual(
            s.expand(s.diff(inv_u, y).subs(to_adapted, simultaneous=True)),
            1 - a * v,
        )
        # T=partial_y has shift zero and intrinsic top N=-a^2 partial_v.
        for f in (a**2, a**3):
            self.assertEqual(-a**2 * s.diff(f, v), 0)
        ideal = s.groebner([a**2], a, v, c, domain=s.QQ)
        ideal_squared = s.groebner([a**4], a, v, c, domain=s.QQ)
        self.assertEqual(ideal.reduce(a**6)[1], 0)
        self.assertNotEqual(ideal_squared.reduce(a**3)[1], 0)
        self.assertEqual(ideal.reduce(s.Integer(1))[1], 1)

    def test_arbitrary_last_degree_and_positive_shift(self):
        a, b, c, u = s.symbols("a b c u")
        X, Y, Z, W = s.symbols("X Y Z W")
        good = (a, b + a**2 * u, c + b * u)

        def T(f):
            return s.expand(
                s.diff(f, u) - a**2 * s.diff(f, b)
                + (a**2 * u - b) * s.diff(f, c)
            )

        # This is one explicit family, not an exhaustive search of frames.
        for ell in (2, 3, 5):
            with self.subTest(last_degree=ell):
                last = u + good[2]**ell
                frame = good + (last,)
                inv_u = W - Z**ell
                inv_b = Y - X**2 * inv_u
                inv_c = Z - inv_b * inv_u
                inverse = (X, inv_b, inv_c, inv_u)
                self.assertEqual(
                    expand_tuple(f.subs(dict(zip((X, Y, Z, W), frame)), simultaneous=True)
                                 for f in inverse),
                    (a, b, c, u),
                )
                self.assertEqual(
                    expand_tuple(f.subs(dict(zip((a, b, c, u), inverse)), simultaneous=True)
                                 for f in frame),
                    (X, Y, Z, W),
                )
                self.assertEqual(tuple(T(f) for f in frame), (0, 0, 0, 1))
                self.assertEqual(tuple(s.diff(f, u, 2) for f in good), (0, 0, 0))
                self.assertEqual(s.Poly(last, u).degree(), ell)
                self.assertEqual(s.Poly(last, u).LC(), b**ell)
                # T's shift-one leading part is u*N, with N=a^2 partial_c.
                for f in (a, b, c):
                    self.assertEqual(s.Poly(T(f), u).coeff_monomial(u), a**2 * s.diff(f, c))
                for f in tuple(s.diff(g, u) for g in good) + (b**ell,):
                    self.assertEqual(a**2 * s.diff(f, c), 0)

    def test_square_zero_inverse_and_first_power_boundary(self):
        e, u, v, p, t = s.symbols("e u v p t")
        modulus = s.groebner([e**2], e, u, v, domain=s.QQ)
        forward = u + e * u**2
        inverse = v - e * v**2
        self.assertEqual(modulus.reduce(s.expand(forward.subs(u, inverse) - v))[1], 0)
        self.assertEqual(modulus.reduce(s.expand(inverse.subs(v, forward) - u))[1], 0)
        self.assertNotEqual(modulus.reduce(e)[1], 0)
        # Bare ideal data only, not an actual speed/acceleration realization.
        h = p**2 * t**2
        ideal = s.groebner([p**3, t**3], p, t, domain=s.QQ)
        self.assertNotEqual(ideal.reduce(h)[1], 0)
        self.assertEqual(ideal.reduce(h**2)[1], 0)
        self.assertEqual(s.expand(h**3 - (p**3)**2 * (t**3)**2), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
