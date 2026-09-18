"""Two actual-action differential controls, not a universal smoothness proof."""

import unittest

import sympy as S


class CriticalValueChecks(unittest.TestCase):
    def zero(self, value):
        entries = list(value) if isinstance(value, S.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(S.cancel(S.expand(entry)), 0)

    def test_cancellation_frame_full_reduced_open(self):
        for multiplicity in [1, 2]:
            with self.subTest(common_factor_multiplicity=multiplicity):
                self.check_cancellation_frame(multiplicity)

    def check_cancellation_frame(self, multiplicity):
        a, x, c, z, u, s, t = S.symbols("a x c z u s t")
        g = (a-1)**multiplicity
        H = -u-a*u-a*u*u/2 if multiplicity == 1 else u+a*(2*u-u*u/2)
        invariant_u = g*(x+a*x*x/2)-a*a*z
        sigma = S.cancel((x-H.subs(u, invariant_u))/a**2)
        inverse_x = H+a*a*s
        inverse_z = S.cancel((g*(inverse_x+a*inverse_x**2/2)-u)/a**2)
        S.Poly(sigma, a, x, c, z)
        S.Poly(inverse_z, a, u, c, s)
        self.zero(inverse_x.subs({u: invariant_u, s: sigma}, simultaneous=True)-x)
        self.zero(inverse_z.subs({u: invariant_u, s: sigma}, simultaneous=True)-z)
        self.zero(invariant_u.subs({x: inverse_x, z: inverse_z}, simultaneous=True)-u)
        self.zero(sigma.subs({x: inverse_x, z: inverse_z}, simultaneous=True)-s)
        self.zero(a*a*S.diff(invariant_u, x)+g*(1+a*x)*S.diff(invariant_u, z))
        self.zero(a*a*S.diff(sigma, x)+g*(1+a*x)*S.diff(sigma, z)-1)

        h, v = a**3, 1+a*H
        w = S.cancel((g*(H+a*H*H/2)-u)/a**2)
        S.Poly(w, a, u)
        F = w+g*v*s+g*h*s*s/2
        self.zero(F-inverse_z)
        self.zero(S.diff(F, s)-g*(v+h*s))
        self.zero(S.diff(F, s, 2)-g*h)
        self.zero(S.diff(F, s, 3))
        # The original coordinate partial has base part -a^2 partial_u.
        self.zero(-a*a*S.diff(F, u)+S.diff(H, u)*S.diff(F, s)-1)
        self.zero(-a*a*S.diff(w, u)+g*v*S.diff(H, u)-1)
        r = S.cancel(w-g*v*v/(2*h))
        self.zero(r+u/a**2+g/(2*a**3))
        self.zero(-a*a*S.diff(r, u)-1)
        self.zero(S.diff(F, s).subs(s, -v/h))
        for y in [a, u, c]:
            self.zero(S.diff(F, y).subs(s, -v/h)-S.diff(r, y))
        discriminant = 2*h*(w-t)-g*v*v
        self.zero(discriminant-2*h*(r-t))
        raw_discriminant = S.discriminant(F-t, s)
        self.zero(raw_discriminant+g*discriminant)
        self.zero(-a*a*S.diff(discriminant, u)-2*h)
        self.zero(r.subs(a, 1)+u)
        self.zero(w.subs(a, 1)+u)
        self.zero(S.diff(w, u).subs(a, 1)+1)
        self.zero((g*h).subs(a, 1))
        self.zero(h.subs(a, 1)-1)
        self.zero(discriminant.subs(a, 1)+2*(u+t))
        self.zero(S.cancel(raw_discriminant/g).subs(a, 1)-2*(u+t))
        if multiplicity == 2:
            self.zero(S.diff(g, a).subs(a, 1))
            self.zero(raw_discriminant.subs(a, 1))
            self.zero(S.diff(raw_discriminant, a).subs(a, 1))

    def test_two_speed_smooth_function_not_lnd_slice(self):
        s, a, b, c, t = S.symbols("s a b c t")
        A, X, Y, Z = S.symbols("A X Y Z")
        old, original = S.Matrix([s, a, b, c]), S.Matrix([A, X, Y, Z])
        x, y = b+a*s, c+b*s
        forward = S.Matrix([a, x, y, s+x*y])
        sigma = Z-X*Y
        invariant_b = X-A*sigma
        inverse = S.Matrix([sigma, A, invariant_b, Y-invariant_b*sigma])
        self.zero(inverse.subs(dict(zip(original, forward)), simultaneous=True)-old)
        self.zero(forward.subs(dict(zip(old, inverse)), simultaneous=True)-original)
        h, v, w = 2*a*b, 1+a*c+b*b, b*c
        F = w+v*s+h*s*s/2
        self.zero(F-forward[3])
        self.zero(forward.diff(s, 2)-S.Matrix([0, 0, 0, h]))
        self.zero(forward.diff(s, 3))
        D = lambda f: -a*S.diff(f, b)-(b+v/(2*b))*S.diff(f, c)
        self.zero(-a*S.diff(w, b)-b*S.diff(w, c)+v-1)
        r = S.cancel(w-v*v/(2*h))
        self.zero(D(r)-1)
        for y in [a, b, c]:
            self.zero(S.diff(F, y).subs(s, -v/h)-S.diff(r, y))
        discriminant = 2*h*(w-t)-v*v
        self.zero(D(discriminant)-2*h-2*(r-t)*D(h))
        self.zero(D(b)+a)
        self.assertNotEqual(D(b), 0)
        # These finite identities support, not replace, the written LND argument.
        self.assertEqual(S.Poly(r, c).degree(), 2)
        self.zero(S.Poly(r, c).nth(2)+a/(4*b))
        self.zero(S.diff(r, c, 2)+a/(2*b))


if __name__ == "__main__":
    unittest.main(verbosity=2)
