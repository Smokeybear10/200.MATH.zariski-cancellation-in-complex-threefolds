"""Standalone exact algebra controls for the working conic scalar proof316.

The jets below impose the displayed necessary coefficient equations, not a
rational ansatz for their solutions. These tests check identities conditional
on those equations. They do not verify the exact fields, global slice, initial
kernel, universal factor classification or an ambient recognition theorem.
No solver or previous checker is imported.
"""

import unittest

import sympy as sp


def coefficient_fixture():
    m, p, delta, kt, ktt, ns, nt, bP, b0, eta, et, es, C = sp.symbols(
        "m p delta kt ktt ns nt bP b0 eta et es C")
    P, V, U, t, n, ell = sp.symbols("P V U t n ell")
    bV = (p-delta)/2
    mu = ktt-(kt*p+2*ns)/m
    nu = nt-kt*ns/m
    alpha, beta, chi = 2*p/m, 2*bP-mu, 2*b0-nu
    nts = 2*p*ns/m+mu*bV+delta*bP
    nss = (p**2-delta**2)/2
    ntt = 2*(mu-bP)*bP-4*p*b0/m+2*p*nt/m+ns*ktt/m
    kttt = 3*p*ktt/m-12*p*bP/m
    bPt = bV*ktt/m-4*bP*bV/m-2*alpha*C/delta
    b0t = bV*(nt-2*b0)/m+bP**2-bP*bV*kt/m-beta*C/delta
    b0s = C+bV*bP-bV**2*kt/m+bV*ns/m
    ellt = ell*p/m-nt*ns/m-mu*b0-nu*bP+2*bP*b0
    ells = -ns**2/m-delta*b0-nu*bV
    rates_t = {m: p, p: 2*p*delta/m, delta: delta*(p+delta)/m,
               kt: ktt, ktt: kttt, ns: nts, nt: ntt, bP: bPt,
               b0: b0t, eta: et, t: 1, n: nt, ell: ellt}
    rates_s = {kt: p, ktt: 2*p*delta/m, ns: nss, nt: nts,
               bP: bV*delta/m, b0: b0s, eta: es, n: ns, ell: ells}

    def derivative(expression, rates):
        return sp.cancel(sum(sp.diff(expression, variable)*rate
                             for variable, rate in rates.items()))

    def row(expression):
        return sp.Matrix([[derivative(expression, rates_t),
                           derivative(expression, rates_s),
                           sp.diff(expression, P)]])

    psi = delta*V-alpha*P**2-beta*P-chi
    B = bP*P+bV*V+b0
    theta = (eta+alpha*P**2+beta*P+chi)/delta
    y = -B.subs(V, theta)
    z = 2*t*y+P**2+kt*P+m*theta+n
    F = ktt*P**2/2+p*P*V+nt*P+ns*V
    w = (ell-(2*P+kt)*y-F.subs(V, theta))/m
    yrow, zrow, wrow = map(row, (y, z, w))
    M = zrow-2*t*yrow
    contact = sp.Matrix([[bP, bV, 1]])
    g1 = -(2*alpha*P+beta)/delta
    expected = (m*et-p*eta)/delta+(4*p*P+beta*m)*es/delta**2
    return locals()


class ConicScalarRigidityControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = coefficient_fixture()

    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def test_entire_raw_surface_factorization(self):
        g = self.g
        U, P, V, m = (g[name] for name in ("U", "P", "V", "m"))
        F, B, psi = (g[name] for name in ("F", "B", "psi"))
        raw_g = (g["ell"]-(2*P+g["kt"])*U-F)/m
        h0 = g["ns"]*g["ell"]/m-g["b0"]*(g["nu"]-g["b0"])
        H0 = (U**2+sp.diff(F, P)*U+sp.diff(F, V)*raw_g
              +g["kttt"]*P**3/6+g["p"]*g["delta"]*P**2*V/m
              +g["ntt"]*P**2/2+g["nts"]*P*V+g["nss"]*V**2/2
              -g["ellt"]*P-g["ells"]*V-h0)
        self.zero(H0-(U+B)*(U+B+psi))
        self.zero(psi.subs(V, g["theta"])-g["eta"])

    def test_formal_restricted_fourth_gradient(self):
        g = self.g
        U, P, V, m = (g[name] for name in ("U", "P", "V", "m"))
        B, psi = g["B"], g["psi"]
        H0 = (U+B)*(U+B+psi)
        lam = (g["p"]*P+g["ns"])/m
        HU, HP, HV = (sp.diff(H0, x) for x in (U, P, V))
        QU = HP-(2*P+g["kt"])*HV/m+lam*HU
        QP = (g["derivative"](H0, g["rates_t"])
              -(2*U+sp.diff(g["F"], P))*HV/m+lam*HP)
        QV = g["derivative"](H0, g["rates_s"])
        restricted_p = (QP-g["bP"]*QU).subs(U, -B)
        restricted_v = (QV-g["bV"]*QU).subs(U, -B)
        self.zero(restricted_p-psi*g["C"]*sp.diff(psi, P)/g["delta"])
        self.zero(restricted_v-psi*g["C"])
        primitive = g["C"]*psi**2/(2*g["delta"])
        self.zero(sp.diff(primitive, P)-restricted_p)
        self.zero(sp.diff(primitive, V)-restricted_v)

    def test_literal_contact_rows_and_scalar_orientation(self):
        g = self.g
        P, m, eta = (g[name] for name in ("P", "m", "eta"))
        Y, W, M, A = (g[name] for name in ("yrow", "wrow", "M", "contact"))
        first = m*W+(2*P+g["kt"])*Y+(g["p"]*P+g["ns"])*M/m+eta*A
        second = (Y+g["bV"]*M/m
                  +(g["bP"]-g["bV"]*(2*P+g["kt"])/m)*A
                  +sp.Matrix([[g["C"]*g["g1"], g["C"], 0]]))
        for value in list(first)+list(second):
            self.zero(value)
        pi = M[0]-g["g1"]*M[1]+(g["bV"]*g["g1"]-g["bP"])*M[2]
        self.zero(pi-g["expected"])
        self.zero(sp.Matrix.vstack(Y, M, A).det()-g["C"]*pi)

    def test_full_literal_determinant_and_missing_eta_derivative_negative(self):
        g = self.g
        matrix = sp.Matrix.vstack(g["yrow"], g["zrow"], g["wrow"])
        actual = sp.cancel(matrix.det(method="domain-ge"))
        target = -g["eta"]*g["C"]*g["expected"]/g["m"]
        self.zero(actual-target)
        linear = -4*g["C"]*g["eta"]*g["es"]*g["p"]/(g["delta"]**2*g["m"])
        self.zero(sp.diff(actual, g["P"])-linear)
        self.assertNotEqual(sp.cancel(linear), 0)
        self.zero(sp.diff(actual.subs(g["es"], 0), g["P"]))
        rigid = -g["eta"]*g["C"]*(g["m"]*g["et"]-g["p"]*g["eta"])/(g["m"]*g["delta"])
        self.zero(actual.subs(g["es"], 0)-rigid)

    def test_reciprocal_leading_coefficient_and_zero_d_boundary(self):
        t, s, c, d = sp.symbols("t s c d")
        f, n1, n0 = (sp.Function(name)(t) for name in ("f", "n1", "n0"))
        m = d+c/t
        p, q = sp.diff(m, t), sp.diff(m, t, 2)
        k = m*s+f
        bP = sp.diff(k, t, 2)/4-m*sp.diff(k, t, 3)/(12*p)
        bV, delta = p/2-m*q/(4*p), m*q/(2*p)
        nss = (p**2-delta**2)/2
        n = nss*s**2/2+n1*s+n0
        mu = sp.diff(k, t, 2)-(sp.diff(k, t)*p+2*sp.diff(n, s))/m
        b0 = m*((mu-bP)*bP-sp.diff(n, t, 2)/2
                +(p*sp.diff(n, t)+sp.diff(n, s)*sp.diff(k, t, 2)/2)/m)/(2*p)
        self.zero(sp.diff(b0, s, 2)+d**2/(2*t**3))
        self.zero(sp.diff(b0, s, 2)-2*bV**2*delta/m)
        self.zero(sp.diff(bP, s)-bV*delta/m)
        self.zero(sp.diff(bV, t)-bV*delta/m)
        self.zero(sp.diff(delta, t)-delta*(p+delta)/m)
        self.zero(sp.diff(b0, s, 2).subs(d, 0))
        self.assertNotEqual(sp.cancel(delta.subs(d, 0)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
