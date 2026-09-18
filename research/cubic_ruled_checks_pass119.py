"""Two exact algebra controls for the ruled cubic branch.

The first method checks conditional connection and volume identities. The
second derives a polynomial unit-speed coefficient control independently.
Neither supplies an original coordinate frame or proves the generic field,
plane-curve generation, or recognition steps of the written theorem.
"""

import unittest

import sympy as sp


class CubicRuledChecks(unittest.TestCase):
    def zero(self, expression):
        entries = expression if isinstance(expression, sp.MatrixBase) else [expression]
        for entry in entries:
            self.assertEqual(sp.cancel(entry), 0)

    def test_conditional_ruled_tensor_and_volume_coefficients(self):
        s, w, v, orbit = sp.symbols("s w v orbit")
        a, beta, f, h = [sp.Function(name)(s) for name in ("a", "beta", "f", "h")]
        c = sp.diff(a, s)/a-beta
        G = sp.Matrix([[f+2*a*beta*w-a**2*w**2, a], [a, 0]])
        C211 = (h+(sp.diff(beta, s)+2*beta**2-f-sp.diff(a, s)*beta/a)*w
                -3*a*beta*w**2+a**2*w**3)
        connection = {(0, 0): (c+a*w, C211), (0, 1): (0, beta-a*w),
                      (1, 0): (0, beta-a*w), (1, 1): (0, 0)}
        tau = -sp.diff(f, s)+2*f*c+2*a*h
        base = (s, w)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tensor = -sp.diff(G[j, k], base[i])+sum(
                        G[l, j]*connection[i, k][l]+G[l, k]*connection[i, j][l]
                        for l in range(2))
                    self.zero(tensor-(tau if (i, j, k) == (0, 0, 0) else 0))

        O0, O1, numerator = sp.symbols("O0 O1 numerator")
        omega = O0+w*O1
        self.zero(-sp.diff(numerator/omega, w)+(numerator/omega)*(O1/omega)
                  -2*numerator*O1/omega**2)
        arbitrary_c = sp.Symbol("arbitrary_c")
        radial = f+(sp.diff(a, s)+a*beta-a*arbitrary_c)*w-a**2*w**2
        self.zero(-sp.diff(radial, w)+2*a*(beta-a*w)
                  -(-sp.diff(a, s)+a*beta+a*arbitrary_c))

        r = sp.symbols("r0:4")
        rs = sp.symbols("r0s r1s r2s r3s")
        rw = sp.symbols("r0w r1w r2w r3w")
        R = sum(r[i]*v**i for i in range(4))
        Rs = sum(rs[i]*v**i for i in range(4))
        Rw = sum(rw[i]*v**i for i in range(4))
        rho, L2 = sp.symbols("rho L2", nonzero=True)
        Kv11 = rho+(c+a*w)*v
        Kv21 = Rs+C211*v+(beta-a*w)*R
        Kv22 = rho+Rw+(beta-a*w)*v
        determinant = sp.Matrix([[orbit+Kv11, 0, 1],
                                 [Kv21, orbit+Kv22, sp.diff(R, v)],
                                 [-L2*sp.diff(R, v), L2, 0]]).det()
        volume = (Rs+sp.diff(R, v)*Rw+(beta-a*w)*R+C211*v
                  +(beta-c-2*a*w)*v*sp.diff(R, v))
        self.zero(determinant-L2*volume)
        poly = sp.Poly(sp.expand(volume), v)
        self.zero(poly.coeff_monomial(v**5)-3*r[3]*rw[3])
        self.zero(poly.coeff_monomial(v**4).subs(rw[3], 0)-3*r[3]*rw[2])
        cubic = poly.coeff_monomial(v**3).subs({rw[3]: 0, rw[2]: 0})
        self.zero(cubic-(rs[3]+3*r[3]*rw[1]+(4*beta-3*c-7*a*w)*r[3]))
        self.zero(sp.diff(cubic, w)+7*a*r[3])

        # Exactness of L1 ds+L2 dw after L2 is independent of w.
        L = sp.Function("L")(s)
        J = sp.Function("J")(s)
        L1 = sp.diff(L, s)*w+J
        self.zero(sp.diff(-L1/L, w)+sp.diff(L, s)/L)

    def test_unit_speed_metric_control_without_actual_frame(self):
        s, t = sp.symbols("s t")
        a = s**2-1
        p = sp.Matrix([0, s, s**2+1])
        q = sp.Matrix([1, s**4/4-s**2/2, s**5/5-s])
        velocity = p+t*q
        self.zero(q.diff(s)-a*p)
        self.zero(p.diff(s, 2)+2*p/a-2*s*p.diff(s)/a)
        self.zero(velocity[2]-s*velocity[1]-(q[2]-s*q[1])*velocity[0]-1)
        frame = velocity.row_join(velocity.diff(s)).row_join(velocity.diff(t))
        self.zero(frame.det()-a)
        base = (s, t)
        G, connection = sp.zeros(2), {}
        for i in range(2):
            for j in range(2):
                column = frame.inv()*velocity.diff(base[i], base[j])
                G[i, j] = sp.cancel(column[0])
                connection[i, j] = tuple(sp.cancel(value) for value in column[1:])
        self.zero(G-sp.Matrix([[-2/a-a**2*t**2, a], [a, 0]]))
        self.zero(G.det()+a**2)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tensor = -sp.diff(G[j, k], base[i])+sum(
                        G[l, j]*connection[i, k][l]+G[l, k]*connection[i, j][l]
                        for l in range(2))
                    self.zero(tensor-(-12*s/a**2 if (i, j, k) == (0, 0, 0) else 0))
        metric = (frame.inv().T*sp.diag(-1, G)*frame.inv()).applyfunc(sp.cancel)
        self.zero(metric.diff(t))
        self.zero(metric.det()-1)
        self.zero((velocity.T*metric*velocity)[0]+1)
        normal = frame.inv().T*sp.Matrix([0, 1, 0])
        self.zero(metric.diff(s)-12*s/a**2*normal*normal.T)
        self.assertNotEqual(sp.cancel(q.diff(s)[1]), 0)
        self.assertEqual(q[0], 1)
        self.assertEqual(q.diff(s)[0], 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
