"""One exact null-axis polynomial-speed control.

Checks reciprocal absorption and differentiated-identity certificates,
then an explicit cubic polynomial/unimodular speed and its canonical
metric. It does not prove UFD cancellation or the universal degree
argument, and it supplies no original polynomial-coordinate inverse.
"""

import unittest

import sympy as sp


class NullPolynomialSpeedChecks(unittest.TestCase):
    def test_reciprocal_certificates_and_cubic_speed_control(self):
        g, p, y, z = sp.symbols("g p y z")
        a2, a1, a0, c = sp.symbols("a2 a1 a0 c")
        lam = sp.symbols("lam", nonzero=True)
        mu = sp.symbols("mu")

        def zero(value):
            self.assertEqual(sp.cancel(value), 0)

        aa = a2 / lam**2
        bb = a1 / lam - 2 * a2 * mu / lam**2
        cc = a0 - a1 * mu / lam + a2 * mu**2 / lam**2
        zz = lam * p + mu * y
        gg = g + (bb * zz + cc * y) / 2
        old = (2 * g * y + a2 * p**2 + a1 * p * y
               + a0 * y**2 + c * y**3 / zz + 1)
        cleared = 2 * gg * y * zz + aa * zz**3 + c * y**3 + zz
        zero(cleared - zz * old)

        G, A = sp.symbols("G A")
        F = 2 * G * y * z + A * z**3 + c * y**3 + z
        fg, fy, fz = [sp.diff(F, item) for item in (G, y, z)]
        zero(fz.subs({y: 0, z: 0}) - 1)
        zero(fz.subs(y, 0) - 3 * (A * z**2 + 1) + 2)
        gs, gt, ys, yt, zs, zt = sp.symbols("gs gt ys yt zs zt")
        fs = fg * gs + fy * ys + fz * zs
        ft = fg * gt + fy * yt + fz * zt
        zero(fz * (ys * zt - yt * zs)
             - fg * (gs * yt - gt * ys) + fs * yt - ft * ys)

        s, t, h = sp.symbols("s t h")
        vv = s * t - 1
        yy = -s**3
        pp = s * (1 + s**3 * vv)
        gg = -(3 * vv + 3 * s**3 * vv**2 + s**6 * vv**3) / 2
        speed = sp.Matrix([gg, pp, yy])
        hh = sp.cancel(pp / yy)
        zero(2 * gg * yy**2 + pp**3 + yy)
        zero(2 * gg * yy + hh**3 * yy**2 + 1)
        omega = sp.Matrix.hstack(speed, speed.diff(s), speed.diff(t)).det()
        zero(omega - 3 * s**4)
        uu = t + s**2 * vv**2 + s**5 * vv**3 / 3
        zero(pp + s * vv * yy - s)
        zero(2 * gg / 3 + uu * pp + s * vv * uu * yy - 1)

        Q = sp.Matrix([[0, 0, 1],
                       [0, 3 * h, -3 * h**2 / 2],
                       [1, -3 * h**2 / 2, h**3]])
        normal = sp.Matrix([0, 1, -h])
        self.assertEqual((Q.diff(h) - 3 * normal * normal.T)
                         .applyfunc(sp.cancel), sp.zeros(3))
        evaluated = Q.subs(h, hh)
        zero((speed.T * evaluated * speed)[0] + 1)
        zero((normal.subs(h, hh).T * speed)[0])
        zero(evaluated.det() + 3 * hh)
        for variable in (s, t):
            zero((speed.T * evaluated * speed.diff(variable))[0])
        zero((1 / s - h / s**2 - 1 / s**4).subs(h, hh) - t)


if __name__ == "__main__":
    unittest.main(verbosity=2)

