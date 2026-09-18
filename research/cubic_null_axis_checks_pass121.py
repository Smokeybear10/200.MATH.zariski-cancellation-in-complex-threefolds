"""One exact null-axis coefficient/control method for pass121.

The method checks conditional differential identities and a rational
generic potential with unit volume. It does not establish an original
polynomial frame, the full constant field, or differential-field
integration. The displayed control has nonpolynomial velocity.
"""

import unittest

import sympy as sp


class NullAxisChecks(unittest.TestCase):
    def test_null_connection_lower_volume_and_generic_control(self):
        h, y, v, u = sp.symbols("h y v u")
        D = sp.Function("D")(h)
        f = sp.diff(D, h, 2) / 2

        def zero(value):
            entries = value if isinstance(value, sp.MatrixBase) else [value]
            for entry in entries:
                self.assertEqual(sp.cancel(entry), 0)

        b = sp.Matrix([-(1 + D * y**2) / (2 * y), h * y, y])
        frame = b.row_join(b.diff(h)).row_join(b.diff(y))
        zero(frame.det() + 1)
        inverse = frame.inv()
        expected = {(0, 0): sp.Matrix([f*y**2, 0, -f*y**3]),
                    (0, 1): sp.Matrix([0, 1/y, 0]),
                    (1, 0): sp.Matrix([0, 1/y, 0]),
                    (1, 1): sp.Matrix([1/y**2, 0, -1/y])}
        base = (h, y)
        G, connection = sp.zeros(2), {}
        for i in range(2):
            for j in range(2):
                column = (inverse * b.diff(base[i], base[j])).applyfunc(sp.cancel)
                zero(column - expected[i, j])
                G[i, j] = column[0]
                connection[i, j] = tuple(column[1:])
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tensor = -sp.diff(G[j, k], base[i]) + sum(
                        G[l, j]*connection[i, k][l] + G[l, k]*connection[i, j][l]
                        for l in range(2))
                    zero(tensor - (-sp.diff(f, h)*y**2
                                   if (i, j, k) == (0, 0, 0) else 0))

        A, B = sp.Function("A")(h), sp.Function("B")(h)
        rho = A*y + B/y
        zero(rho/y**2 - sp.diff(rho, y, 2) - sp.diff(rho, y)/y)
        zero(-sp.diff(rho, h, y) + sp.diff(rho, h)/y
             - 2*sp.diff(B, h)/y**2)
        zero(rho*f*y**2 - sp.diff(rho, h, 2) - f*y**3*sp.diff(rho, y)
             - ((2*B*f-sp.diff(A, h, 2))*y-sp.diff(B, h, 2)/y))

        r = [sp.Function(f"r{i}")(h, y) for i in range(4)]
        R = sum(r[i]*v**i for i in range(4))

        def volume(poly):
            return (sp.diff(poly, h) + sp.diff(poly, v)*sp.diff(poly, y)
                    - f*y**3*v - 2*poly*sp.diff(poly, v)/y
                    - v*sp.diff(poly, v)**2/y)

        coefficients = sp.Poly(sp.expand(volume(R)), v)
        zero(coefficients.coeff_monomial(v**5)
             - 3*r[3]*(sp.diff(r[3], y)-5*r[3]/y))
        zero(coefficients.coeff_monomial(v**4).subs(sp.diff(r[3], y), 5*r[3]/y)
             - 3*r[3]*(sp.diff(r[2], y)-4*r[2]/y))

        alpha, beta, j, k, m, n = [sp.Function(name)(h)
                                  for name in ("alpha", "beta", "j", "k", "m", "n")]
        reduced = m*y**2+n+(alpha*y+beta*y**3)*v+j*y**4*v**2+k*y**5*v**3
        lower = sp.Poly(sp.expand(volume(reduced)), v)
        targets = {
            0: (sp.diff(m, h)-2*beta*n)*y**2+sp.diff(n, h)-2*alpha*n,
            1: (sp.diff(alpha, h)-2*alpha**2)*y
               +(sp.diff(beta, h)-2*alpha*beta-4*j*n-f)*y**3,
            2: (sp.diff(j, h)-4*alpha*j-6*k*n)*y**4,
            3: (sp.diff(k, h)-6*alpha*k)*y**5,
            4: 0, 5: 0,
        }
        for degree, target in targets.items():
            zero(lower.coeff_monomial(v**degree)-target)

        ell, q0 = sp.Function("ell")(h), sp.Symbol("q0", nonzero=True)
        a0 = sp.diff(ell, h)/(2*ell)
        zero(sp.diff(a0, h)-2*a0**2+ell*sp.diff(1/ell, h, 2)/2)
        k0 = q0*sp.diff(f, h)/(6*ell)
        invariant = sp.diff(f, h)/ell**4
        zero(sp.diff(k0, h)/k0-3*sp.diff(ell, h)/ell
             - sp.diff(invariant, h)/invariant)
        lam, mu, cstar = sp.symbols("lam mu cstar", nonzero=True)
        reciprocal = -cstar/(3*lam**3*(lam*h+mu))
        zero(sp.diff(reciprocal, h, 3)-2*cstar/(lam*h+mu)**4)

        # A full rational generic control, explicitly not a global frame.
        D0 = h**3
        b0 = b.subs(D, D0)
        R0 = h*y**2 + sp.Rational(3, 2)*h**2*y**3*v + y**5*v**3/2
        chi = -1/(2*y**2)-h**3/2
        L1, L2, tau = -3*h**2/2, y**-3, -3*y**2
        zero(L1*v+L2*R0+tau*v**3/6-h/y)
        zero(volume(R0).subs(sp.diff(D, h, 2), 6*h)-y**2)
        x = b0*u + b0.diff(h)*v + b0.diff(y)*R0
        z = chi+u**2/2-(3*h*y**2*v**2+R0**2/y**2)/2
        outputs = x.col_join(sp.Matrix([z])).applyfunc(sp.expand)
        zero(outputs.jacobian([u, h, y, v]).det()+1/y)
        numerator = sp.fraction(sp.cancel(b0[0]))[0]
        self.assertNotEqual(numerator.subs(y, 0), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
