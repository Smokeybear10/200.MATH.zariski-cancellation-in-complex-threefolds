"""Two exact algebra controls for the conic-axis restriction120.

The tests establish conditional identities, not the existence of a global
original frame, a finite splitting field, or a cancellation theorem.
"""

import unittest

import sympy as sp


class CubicConicAxisChecks(unittest.TestCase):
    def zero(self, expression):
        entries = expression if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(entry), 0)

    def test_normalized_conic_connection_and_tensor(self):
        s, w = sp.symbols("s w")
        a, c, d, e = [sp.Function(name)(s) for name in ("a", "c", "d", "e")]
        ambient = sp.Matrix([[a, 0, 2*d], [0, -a, 2*c], [c, d, e]])
        gram = sp.Matrix([[0, -sp.Rational(1, 2), 0],
                          [-sp.Rational(1, 2), 0, 0], [0, 0, 1]])
        normal = sp.Matrix([0, 0, 1])
        self.zero(ambient.T*gram+gram*ambient-2*e*normal*normal.T)
        b = sp.Matrix([w, 1/w, 0])
        bs, bw = ambient*b, b.diff(w)
        frame = b.row_join(bs).row_join(bw)
        Z = c*w+d/w
        ell = sp.diff(Z, w)/Z
        C1 = e+sp.diff(Z, s)/Z+a*w*ell
        C211 = w*(sp.diff(a, s)-a*C1)-w**2*Z*sp.diff(Z, w)
        self.zero(frame.det()-2*Z/w)
        derivatives = {(0, 0): bs.diff(s)+ambient*bs,
                       (0, 1): bs.diff(w), (1, 0): bs.diff(w),
                       (1, 1): bw.diff(w)}
        expected = {(0, 0): sp.Matrix([a**2+Z**2, C1, C211]),
                    (0, 1): sp.Matrix([a/w, ell, -a*w*ell]),
                    (1, 0): sp.Matrix([a/w, ell, -a*w*ell]),
                    (1, 1): sp.Matrix([1/w**2, 0, -1/w])}
        G, connection = sp.zeros(2), {}
        for (i, j), column in derivatives.items():
            coordinates = (frame.inv()*column).applyfunc(sp.cancel)
            self.zero(coordinates-expected[i, j])
            G[i, j] = coordinates[0]
            connection[i, j] = tuple(coordinates[1:])
        base = (s, w)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tensor = -sp.diff(G[j, k], base[i])+sum(
                        G[l, j]*connection[i, k][l]+G[l, k]*connection[i, j][l]
                        for l in range(2))
                    self.zero(tensor-(2*e*Z**2 if (i, j, k) == (0, 0, 0) else 0))

    def test_volume_coefficients_exactness_and_finite_gauge(self):
        s, w, v, u = sp.symbols("s w v u")
        ell, C1, C21, C2, rho, L2 = sp.symbols("ell C1 C21 C2 rho L2")
        r = sp.symbols("r0:4")
        rs, rw = sp.symbols("r0s r1s r2s r3s"), sp.symbols("r0w r1w r2w r3w")
        R = sum(r[i]*v**i for i in range(4))
        Rs = sum(rs[i]*v**i for i in range(4))
        Rw = sum(rw[i]*v**i for i in range(4))
        Rv = sp.diff(R, v)
        K11, K12 = rho+C1*v+ell*R, ell*v
        K21, K22 = Rs+C21*v+C2*R, rho+Rw+C2*v-R/w
        matrix = sp.Matrix([[u+K11, K12, 1], [K21, u+K22, Rv],
                            [-L2*Rv, L2, 0]])
        volume = (Rs+Rv*Rw+C21*v+C2*R+(C2-C1)*v*Rv
                  +(-1/w-ell)*R*Rv-ell*v*Rv**2)
        self.zero(matrix.det()-L2*volume)
        poly = sp.Poly(sp.expand(volume), v)
        self.zero(poly.coeff_monomial(v**5)-3*r[3]*(rw[3]-(1/w+4*ell)*r[3]))
        top = {rw[3]: (1/w+4*ell)*r[3]}
        self.zero(poly.coeff_monomial(v**4).subs(top)
                  -3*r[3]*(rw[2]-(1/w+3*ell)*r[2]))
        top[rw[2]] = (1/w+3*ell)*r[2]
        cubic = sp.cancel(poly.coeff_monomial(v**3).subs(top)/r[3])
        self.zero(cubic-(rs[3]/r[3]+3*rw[1]-(3/w+6*ell)*r[1]+4*C2-3*C1))
        Llog = sp.Symbol("Llog")
        exact = cubic.subs(rw[1], -Llog+(1/w+2*ell)*r[1])
        self.zero(exact-(rs[3]/r[3]-3*Llog+4*C2-3*C1))

        a, c, d, e, k = [sp.Function(name)(s) for name in ("a", "c", "d", "e", "k")]
        q0 = sp.Symbol("q0", nonzero=True)
        Z = c*w+d/w
        ell_actual = sp.diff(Z, w)/Z
        r3 = k*w*Z**4
        l0 = -q0*e/(3*k)
        linear = l0/(w*Z**2)
        C1_actual = e+sp.diff(Z, s)/Z+a*w*ell_actual
        C2_actual = -a*w*ell_actual
        residual = (sp.diff(r3, s)/r3-3*sp.diff(linear, s)/linear
                    +4*C2_actual-3*C1_actual)
        quotient = (sp.diff(Z, s)-a*w*sp.diff(Z, w))/Z
        self.zero(residual-(sp.diff(e, s)/e-4*sp.diff(l0, s)/l0-3*e+7*quotient))
        compatibility = sp.diff(c, s)*d-c*sp.diff(d, s)-2*a*c*d
        self.zero(sp.diff(quotient, w)-2*w*compatibility/(c*w**2+d)**2)

        # Algebraic-compatible coefficients c=sigma*theta,d=sigma/theta.
        theta, sigma = sp.Function("theta")(s), sp.Function("sigma")(s)
        a0, c0, d0 = sp.diff(theta, s)/theta, sigma*theta, sigma/theta
        old = sp.Matrix([[a0, 0, 2*d0], [0, -a0, 2*c0], [c0, d0, e]])
        change = sp.diag(1/theta, theta, 1)
        new = change.inv()*(old*change+change.diff(s))
        expected = sp.Matrix([[0, 0, 2*sigma], [0, 0, 2*sigma], [sigma, sigma, e]])
        self.zero(new-expected)
        axis = sp.Matrix([1, -1, 0])
        self.zero(new*axis)
        self.zero(sp.diff(c0, s)*d0-c0*sp.diff(d0, s)-2*a0*c0*d0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
