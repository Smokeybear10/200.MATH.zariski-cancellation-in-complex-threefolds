"""Two conditional non-null-axis algebra checks for pass121.

The first computes the full normalized potential/volume residuals.
The second checks the scaled-derivative and square-root certificates.
Neither establishes a splitting field, a primitive for the normalized
derivation, its constant field, integration, or a global original frame.
"""

import unittest

import sympy as sp


class NonnullAxisChecks(unittest.TestCase):
    def zero(self, value):
        entries = value if isinstance(value, sp.MatrixBase) else [value]
        for entry in entries:
            self.assertEqual(sp.cancel(entry), 0)

    def test_normalized_potential_and_all_volume_coefficients(self):
        s, w, v, u = sp.symbols("s w v u")
        e = sp.Function("e")(s)
        Z, W = w+1/w, w-1/w
        ell = sp.diff(Z, w)/Z
        A, B = sp.Function("A")(s), sp.Function("B")(s)
        rho = A*Z+B*W
        self.zero(rho/w**2-sp.diff(rho, w, 2)-sp.diff(rho, w)/w)
        self.zero(-sp.diff(rho, s, w)+ell*sp.diff(rho, s)
                  +4*sp.diff(B, s)/(w*Z))
        B11 = (rho*Z**2-sp.diff(rho, s, 2)+e*sp.diff(rho, s)
               -w**2*Z*sp.diff(Z, w)*sp.diff(rho, w))
        self.zero(B11-Z*(4*A-sp.diff(A, s, 2)+e*sp.diff(A, s))
                  -W*(-sp.diff(B, s, 2)+e*sp.diff(B, s)))

        r = [sp.Function(f"r{i}")(s, w) for i in range(4)]
        R = sum(r[i]*v**i for i in range(4))
        Rv = sp.diff(R, v)
        L2, rho0 = sp.symbols("L2 rho")
        K11, K12 = rho0+e*v+ell*R, ell*v
        K21 = sp.diff(R, s)-w**2*Z*sp.diff(Z, w)*v
        K22 = rho0+sp.diff(R, w)-R/w
        matrix = sp.Matrix([[u+K11, K12, 1], [K21, u+K22, Rv],
                            [-L2*Rv, L2, 0]])

        def volume(poly):
            pv = sp.diff(poly, v)
            return (sp.diff(poly, s)+pv*sp.diff(poly, w)
                    -w**2*Z*sp.diff(Z, w)*v-e*v*pv
                    +(-1/w-ell)*poly*pv-ell*v*pv**2)

        self.zero(matrix.det()-L2*volume(R))
        coefficients = sp.Poly(sp.expand(volume(R)), v)
        self.zero(coefficients.coeff_monomial(v**5)
                  -3*r[3]*(sp.diff(r[3], w)-(1/w+4*ell)*r[3]))
        self.zero(coefficients.coeff_monomial(v**4).subs(
            sp.diff(r[3], w), (1/w+4*ell)*r[3])
            -3*r[3]*(sp.diff(r[2], w)-(1/w+3*ell)*r[2]))

        l, C = sp.Function("l")(s), sp.Function("C")(s)
        psi = l*W/(4*Z)+C
        self.zero(sp.diff(psi, w)-l/(w*Z**2))
        a0, b0 = -sp.diff(l, s)/(4*l), -sp.diff(C, s)/l
        self.zero(-sp.diff(psi, s)/(l/(w*Z**2))
                  -(a0*w*Z*W+b0*w*Z**2))

        a, b, j, k, m, n = [sp.Function(name)(s)
                            for name in ("a", "b", "j", "k", "m", "n")]
        lower_part = ((a*w*Z*W+b*w*Z**2)*v
                      +j*w*Z**3*v**2+k*w*Z**4*v**3)
        # Derive the r0 equation before imposing its claimed solution.
        general_r0 = sp.Poly(sp.expand(volume(r[0]+lower_part)), v)
        self.zero(general_r0.coeff_monomial(v**2)
                  -(w*Z**3*(sp.diff(j, s)+8*a*j-2*e*j)
                    +3*k*w*Z**4*(sp.diff(r[0], w)-(1/w+ell)*r[0])))
        reduced = m*(w**2+1)+n+lower_part
        lower = sp.Poly(sp.expand(volume(reduced)), v)
        target = {
            0: (sp.diff(m, s)-2*b*n)*(w**2+1)+sp.diff(n, s)-2*a*n*(w**2-1),
            1: w*Z*W*(sp.diff(a, s)+4*a**2-a*e-1)
               +w*Z**2*(sp.diff(b, s)+4*a*b-b*e-4*j*n),
            2: w*Z**3*(sp.diff(j, s)+8*a*j-2*e*j-6*k*n),
            3: w*Z**4*(sp.diff(k, s)+12*a*k-3*e*k),
            4: 0, 5: 0,
        }
        for degree, residual in target.items():
            self.zero(lower.coeff_monomial(v**degree)-residual)
        z = 1/l
        self.zero(sp.diff(a0, s)+4*a0**2-a0*e-1
                  -(sp.diff(z, s, 2)-e*sp.diff(z, s)-4*z)/(4*z))
        q0 = sp.Symbol("q0", nonzero=True)
        k0 = -q0*e/(3*l)
        self.zero(sp.diff(k0, s)/k0+12*a0-3*e
                  -(sp.diff(e, s)/e+4*sp.diff(z, s)/z-3*e))

    def test_scalar_derivative_conversion_and_first_integral(self):
        h = sp.Symbol("h")
        D, z = sp.Function("D")(h), sp.Function("z")(h)
        kap, root = sp.Function("kappa")(h), sp.Function("rootD")(h)
        Delta = (sp.diff(D, h)**2-2*D*sp.diff(D, h, 2))/4
        self.zero(sp.diff(Delta, h)+D*sp.diff(D, h, 3)/2)
        kap_log = sp.diff(Delta, h)/(2*Delta)-sp.diff(D, h)/D
        e_old = -sp.diff(Delta, h)/(2*Delta)
        e = e_old/kap

        def prime(value):
            return sp.diff(value, h)/kap

        scaled = kap**2*(prime(prime(z))-e*prime(z)-4*z)
        scaled = sp.cancel(scaled.subs(sp.diff(kap, h), kap_log*kap))
        scaled = scaled.subs(kap**2, Delta/(4*D**2))
        target = sp.diff(z, h, 2)+sp.diff(D, h)*sp.diff(z, h)/D-Delta*z/D**2
        self.zero(scaled-target)
        product = sp.diff(root*z, h, 2)/root
        product = product.subs({
            sp.diff(root, h, 2): (sp.diff(D, h, 2)/(2*D)
                                  -sp.diff(D, h)**2/(4*D**2))*root,
            sp.diff(root, h): sp.diff(D, h)*root/(2*D),
        }, simultaneous=True)
        self.zero(product-target)

        top = kap*(prime(e)/e+4*prime(z)/z-3*e)
        top = sp.cancel(top.subs(sp.diff(kap, h), kap_log*kap))
        logarithmic = (sp.diff(D, h, 4)/sp.diff(D, h, 3)
                       +2*sp.diff(D, h)/D+4*sp.diff(z, h)/z)
        self.zero(top-logarithmic)
        invariant = sp.diff(D, h, 3)*D**2*z**4
        self.zero(top-sp.diff(invariant, h)/invariant)

        # Conditional linear numerator after the written constant-field step.
        A, B = sp.symbols("A B")
        linear = A*h+B
        after_linear = logarithmic.subs(
            sp.diff(z, h), z*(A/linear-sp.diff(D, h)/(2*D)))
        self.zero(after_linear*sp.diff(D, h, 3)*linear**4
                  -sp.diff(sp.diff(D, h, 3)*linear**4, h))


if __name__ == "__main__":
    unittest.main(verbosity=2)
