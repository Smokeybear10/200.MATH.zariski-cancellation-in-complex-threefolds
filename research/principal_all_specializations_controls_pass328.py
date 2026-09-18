"""Finite exact controls for325 and the collision/immersion frontier.

These identities do not prove actual chart entry, polynomial-ring return,
or cancellation. The last test is a negative control: even an exact inverse
over the coefficient field does not replace the full calibrated Jacobian.
No other research checker is imported.
"""

import unittest

import sympy as sp


class AllSpecializationControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_quadratic_affine_profile_including_zero_z_leader(self):
        v, x = sp.symbols("v x")
        t, m, kt, ktt, mt, ms, nt, ns, n, ell = sp.symbols(
            "t m kt ktt mt ms nt ns n ell", nonzero=True
        )
        a, b = sp.symbols("a b", nonzero=True)
        a1, a0, b0, c, c0 = sp.symbols("a1 a0 b0 c c0")
        y = a * v**2 + a1 * v + a0
        sigma = b * v + b0
        theta = c * v + c0
        potential = (
            ktt * sigma**2 / 2 + mt * sigma * theta
            + ms * theta**2 / 2 + nt * sigma + ns * theta
        )
        yy = y + x * sigma + t * x**2
        zz = 2 * t * y + sigma**2 + kt * sigma + m * theta + n
        zz += 2 * t * x * sigma
        ww = (ell - (2 * sigma + kt) * y - potential) / m + x * theta
        z2 = 2 * t * a + b**2
        combination = sp.Poly(sp.expand(a * zz - z2 * yy), v)
        linear = combination.coeff_monomial(v)
        self.assert_zero(sp.diff(linear, x) + b**3)
        x0 = sp.expand(linear.subs(x, 0) / b**3)
        self.assert_zero(linear.subs(x, x0))
        self.assert_zero(sp.Poly(sp.expand(yy), v).coeff_monomial(v**2) - a)
        self.assert_zero(sp.Poly(sp.expand(ww), v).coeff_monomial(v**3) + 2*a*b/m)
        self.assert_zero(linear.subs({t: -b**2/(2*a), x: x0}))
        self.assert_zero(z2.subs(t, -b**2/(2*a)))

    def test_exact_infinitesimal_identity(self):
        y, p, q, dy, dp, dq, x = sp.symbols("y p q dy dp dq x")
        m, kt, ktt, mt, ms, nt, ns = sp.symbols("m kt ktt mt ms nt ns")
        gamma = 2 * p + kt
        fp = ktt * p + mt * q + nt
        fq = mt * p + ms * q + ns
        ss = gamma * dp + m * dq
        yy = dy + x * dp
        ww = (-gamma * dy - (2*y + fp)*dp - fq*dq) / m + x*dq
        hu = 2*y + fp - gamma*fq/m
        self.assert_zero(m*ww + gamma*yy - (x-fq/m)*ss + dp*hu)
        # Dropping the saturation exceptional set is not permitted.
        self.assert_zero(ss.subs({dp: 0, dq: 0}))
        self.assert_zero(yy.subs({dp: 0}) - dy)

    def test_exact_two_point_polarization(self):
        y1, y2, p1, p2, q1, q2, x = sp.symbols("y1 y2 p1 p2 q1 q2 x")
        m, kt, ktt, mt, ms, nt, ns, ell = sp.symbols(
            "m kt ktt mt ms nt ns ell"
        )

        def potential(p, q):
            return ktt*p**2/2 + mt*p*q + ms*q**2/2 + nt*p + ns*q

        f1, f2 = potential(p1, q1), potential(p2, q2)
        fp = ktt*(p1+p2)/2 + mt*(q1+q2)/2 + nt
        fq = mt*(p1+p2)/2 + ms*(q1+q2)/2 + ns
        self.assert_zero(f1-f2 - fp*(p1-p2) - fq*(q1-q2))
        gamma = p1+p2+kt
        ss = p1**2-p2**2+kt*(p1-p2)+m*(q1-q2)
        yy = y1-y2+x*(p1-p2)
        ww = (-(2*p1+kt)*y1-f1+(2*p2+kt)*y2+f2)/m + x*(q1-q2)
        collision = y1+y2+fp-gamma*fq/m
        self.assert_zero(m*ww+gamma*yy-(x-fq/m)*ss+(p1-p2)*collision)
        diagonal = collision.subs({y2: y1, p2: p1, q2: q1})
        self.assert_zero(diagonal - (2*y1+ktt*p1+mt*q1+nt
                                     -(2*p1+kt)*(mt*p1+ms*q1+ns)/m))

    def test_all_x_inverse_does_not_imply_actual_calibration(self):
        t, s, v, x = sp.symbols("t s v x")
        q = sp.Function("q")(v)
        sigma = v**2-s
        theta = q+6*s*v**2-s**2+s
        y = v
        z = 2*t*v+sigma**2+theta
        w = t-2*sigma*v
        yy = y+sigma*x+t*x**2
        zz = z+(2*t*sigma+s)*x+t**2*x**2
        ww = w+theta*x+s*x**2
        f = yy-t*x**2
        g = zz-2*t*yy-s*x+t**2*x**2
        h = ww-t-s*x**2
        v_squared = sp.expand(f**2+x*h-x**2*g)
        self.assert_zero(v_squared-v**2)
        self.assert_zero(f-x*(v_squared-s)-v)
        jacobian = sp.Matrix([yy, zz, ww]).jacobian([t, s, v]).det()
        expected = -1-(12*s*v+sp.diff(q, v)+1)*x
        self.assert_zero(jacobian-expected)
        self.assertNotEqual(sp.expand(expected.subs(sp.diff(q, v), 3*v**2)+1), 0)
        # H=U^2-P has h0=s; its corrected fourth level is Q=-U-V.
        self.assert_zero(sp.diff(-y-theta, v) + 12*s*v+sp.diff(q, v)+1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
