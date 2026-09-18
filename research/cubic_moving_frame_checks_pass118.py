"""Finite cubic moving-frame controls, exactly three unittest methods.

Checks affine-block and metric identities, a genuine principal-open inverse
and its unimodular-speed pullback, and selected cylinder residuals. Neither
localized control has a global
polynomial derivation on its unlocalized target. No test proves universal
classification, actual global-frame entry, or all-degree asymptotics.
"""

import unittest

import sympy as sp


class CubicMovingFrameChecks(unittest.TestCase):
    def zero(self, expression):
        if isinstance(expression, sp.MatrixBase):
            for entry in expression:
                self.assertEqual(sp.cancel(entry), 0)
        else:
            self.assertEqual(sp.cancel(expression), 0)

    def test_affine_block_and_moving_basis_coefficients(self):
        v, orbit = sp.symbols("v orbit")
        aa = sp.symbols("A11 A12 A21 A22")
        bb = sp.symbols("B11 B12 B21 B22")
        dd = sp.symbols("D11 D12 D21 D22")
        A, B, D = (sp.Matrix(2, 2, entries) for entries in (aa, bb, dd))
        K = A + v * B + v**3 * D
        determinant = sp.Matrix([
            [orbit + K[0, 0], K[0, 1], 1],
            [K[1, 0], orbit + K[1, 1], 3*v**2],
            [-3*v**2, 1, 0],
        ]).det()
        expected = (aa[2] + bb[2]*v + 3*(aa[3]-aa[0])*v**2
                    + (dd[2]+3*(bb[3]-bb[0]))*v**3 - 9*aa[1]*v**4
                    + (3*(dd[3]-dd[0])-9*bb[1])*v**5 - 9*dd[1]*v**7)
        self.zero(determinant - expected)
        constraints = {bb[2]: 0, aa[3]: aa[0], dd[2]: -3*(bb[3]-bb[0]),
                       aa[1]: 0, dd[3]: dd[0]+3*bb[1], dd[1]: 0}
        constrained = K.subs(constraints, simultaneous=True)
        tangent = sp.Matrix([1, 3*v**2])
        scalar = aa[0]+bb[0]*v+(dd[0]+3*bb[1])*v**3
        self.zero(constrained*tangent-scalar*tangent-sp.Matrix([0, aa[2]]))
        self.zero(determinant.subs(constraints, simultaneous=True)-aa[2])

        a, b, c, d, e, f, g, h, i, j, k, l = sp.symbols("a b c d e f g h i j k l")
        covariant = (sp.Matrix([i, k]) + 3*v**2*sp.Matrix([l, j])
                     + v*sp.Matrix([a, b]) + v**3*sp.Matrix([c+3*e, d+3*f])
                     + 3*v**5*sp.Matrix([g, h]))
        area = tangent.row_join(covariant).det()
        coefficient_form = (k+b*v+3*(j-i)*v**2+(d+3*f-3*a)*v**3
                            -9*l*v**4+(3*h-3*c-9*e)*v**5-9*g*v**7)
        self.zero(area-coefficient_form)
        self.zero(area.subs({b: 0, j: i, l: 0, d: 3*a-3*f,
                             h: c+3*e, g: 0}, simultaneous=True)-k)

        # Formal connection residual, without an integrability assertion.
        G11, G12, G22, ell1, ell2, tau = sp.symbols("G11 G12 G22 ell1 ell2 tau")
        c111, c112, c122, c211, c212, c222 = sp.symbols("c111 c112 c122 c211 c212 c222")
        G = sp.Matrix([[G11, G12], [G12, G22]])
        connection = {(0, 0): (c111, c211), (0, 1): (c112, c212),
                      (1, 0): (c112, c212), (1, 1): (c122, c222)}
        ell = (ell1, ell2)
        H = sp.diag(-1, G)
        normal = sp.Matrix([0, ell1, ell2])
        for ii in range(2):
            M = sp.Matrix([[0, G[ii, 0], G[ii, 1]],
                           [int(ii == 0), connection[ii, 0][0], connection[ii, 1][0]],
                           [int(ii == 1), connection[ii, 0][1], connection[ii, 1][1]]])
            dG = sp.Matrix(2, 2, lambda jj, kk: sum(
                G[mm, jj]*connection[ii, kk][mm]+G[mm, kk]*connection[ii, jj][mm]
                for mm in range(2))-tau*ell[ii]*ell[jj]*ell[kk])
            self.zero(sp.diag(0, dG)-M.T*H-H*M+tau*ell[ii]*normal*normal.T)

    def test_principal_open_inverse_geometry_and_global_pole(self):
        s = sp.Symbol("s", nonzero=True)
        t, v, u = sp.symbols("t v u")
        base = (s, t)
        velocity = sp.Matrix([s, t, s**3])
        frame = velocity.row_join(velocity.diff(s)).row_join(velocity.diff(t))
        self.zero(frame.det()+2*s**3)
        connection = {}
        G = sp.zeros(2)
        for i in range(2):
            for j in range(2):
                column = frame.inv()*velocity.diff(base[i], base[j])
                G[i, j] = column[0]
                connection[i, j] = sp.Matrix(column[1:])
        self.zero(G-sp.diag(-3/s**2, 0))
        self.zero(connection[0, 0]-sp.Matrix([3/s, 3*t/s**2]))
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    tensor = -sp.diff(G[j, k], base[i]) + sum(
                        G[m, j]*connection[i, k][m]+G[m, k]*connection[i, j][m]
                        for m in range(2))
                    self.zero(tensor-(-24/s**3 if (i, j, k) == (0, 0, 0) else 0))
        metric = frame.inv().T*sp.diag(-1, G)*frame.inv()
        normal = frame.inv().T*sp.Matrix([0, 1, 0])
        self.zero(metric.diff(s)-24/s**3*normal*normal.T)
        self.zero(metric.diff(t))

        def covariant(left, right):
            result = sp.zeros(2, 1)
            for ii in range(2):
                result += left[ii]*right.diff(base[ii])
                for kk in range(2):
                    result += connection[ii, kk]*left[ii]*right[kk]
            return result

        X, V, offset = sp.Matrix([1, 3*t/s]), sp.Matrix([0, 4]), sp.Matrix([0, s])
        self.zero(covariant(X, X)-3*X/s)
        self.zero(covariant(X, V))
        self.zero(covariant(V, X)-3*V/s)
        self.zero(covariant(V, V))
        self.zero(covariant(X, offset)-V/4)
        self.zero(covariant(V, offset))
        y = sp.Matrix([v, s+3*t*v/s+4*v**3])
        good = velocity*u+velocity.diff(s)*y[0]+velocity.diff(t)*y[1]
        bad = u**2/2+3*v**2/(2*s**2)+t/s**3
        forward = sp.Matrix([*good, bad])
        self.zero(forward.jacobian((u, s, t, v)).det()+2)
        self.zero(good.diff(u)-velocity)
        self.zero(sp.diff(bad, u)-u)
        self.zero(sp.diff(bad, u, 2)-1)

        Y1, Y2 = sp.symbols("Y1 Y2")
        phi = -3*t*Y1/s**4+Y2/s**3-4*Y1**3/s**3
        F = Y2-s-3*t*Y1/s-4*Y1**3
        self.zero(phi-1/s**2-F/s**3)
        self.zero(F.subs({Y1: y[0], Y2: y[1]}, simultaneous=True))
        K = sp.zeros(2)
        for j in range(2):
            for i in range(2):
                K[j, i] = sp.diff(y[j], base[i])+sum(
                    connection[i, k][j]*y[k] for k in range(2))
        self.zero(K-sp.Matrix([[3*v/s, 0], [1, 3*v/s]]))
        gradient = [sp.diff(phi, YY).subs({Y1: y[0], Y2: y[1]}, simultaneous=True)
                    for YY in (Y1, Y2)]
        reduced = sp.Matrix([[u+K[0, 0], K[0, 1], sp.diff(y[0], v)],
                             [K[1, 0], u+K[1, 1], sp.diff(y[1], v)],
                             [*gradient, 0]])
        self.zero(reduced.det()-1/s**3)

        X1, X2, X3, Z, sigma = sp.symbols("X1 X2 X3 Z sigma")
        localization = X2-Z*X3+X1**3/2
        inverse = {s: sigma, v: (X3-sigma**2*X1)/(2*sigma**2),
                   u: (3*sigma**2*X1-X3)/(2*sigma**3),
                   t: sigma**3*Z-sp.Rational(3, 2)*sigma*X1**2
                      +3*X1*X3/(2*sigma)-X3**2/(2*sigma**3)}
        # The forward result has this X2 after imposing sigma=localization.
        self.zero(forward.subs(inverse, simultaneous=True)
                  -sp.Matrix([X1, sigma+Z*X3-X1**3/2, X3, Z]))
        image = {X1: good[0], X2: good[1], X3: good[2], Z: bad}
        self.zero(localization.subs(image, simultaneous=True)-s)
        for variable, expression in inverse.items():
            self.zero(expression.subs({sigma: s, **image}, simultaneous=True)-variable)
        pole_point = {X1: 0, X2: 0, X3: 1, Z: 0}
        self.assertEqual(localization.subs(pole_point), 0)
        self.assertEqual((3*localization**2*X1-X3).subs(pole_point), -1)
        self.zero(sp.diff(localization, X2)-1)
        self.zero(velocity.subs({s: 0, t: 0}))

        # Noninvertible on the whole base, invertible on the same s-open.
        pulled_velocity = velocity.subs(t, s*t-1)
        self.zero(t*pulled_velocity[0]-pulled_velocity[1]-1)
        pulled_frame = pulled_velocity.row_join(pulled_velocity.diff(s)).row_join(pulled_velocity.diff(t))
        self.zero(pulled_frame.det()+2*s**4)
        pulled_connection, pulled_G = {}, sp.zeros(2)
        for ii in range(2):
            for jj in range(2):
                column = pulled_frame.inv()*pulled_velocity.diff(base[ii], base[jj])
                pulled_G[ii, jj] = sp.cancel(column[0])
                pulled_connection[ii, jj] = sp.Matrix(column[1:])
        self.zero(pulled_G-G)
        for ii in range(2):
            for jj in range(2):
                for kk in range(2):
                    tensor = -sp.diff(pulled_G[jj, kk], base[ii])+sum(
                        pulled_G[mm, jj]*pulled_connection[ii, kk][mm]
                        +pulled_G[mm, kk]*pulled_connection[ii, jj][mm] for mm in range(2))
                    self.zero(tensor-(-24/s**3 if (ii, jj, kk) == (0, 0, 0) else 0))
        pulled = forward.subs(t, s*t-1)
        pulled_y = sp.Matrix([v, 1+(2*t/s-3/s**2)*v+4*v**3/s])
        self.zero(pulled[:3, :]-pulled_velocity*u
                  -pulled_velocity.diff(s)*pulled_y[0]-pulled_velocity.diff(t)*pulled_y[1])
        self.zero(pulled.jacobian((u, s, t, v)).det()+2*s)
        pulled_inverse = {**inverse, t: (inverse[t]+1)/sigma}
        self.zero(pulled.subs(pulled_inverse, simultaneous=True)
                  -sp.Matrix([X1, sigma+Z*X3-X1**3/2, X3, Z]))
        pulled_image = dict(zip((X1, X2, X3, Z), pulled))
        for variable, expression in pulled_inverse.items():
            self.zero(expression.subs({sigma: s, **pulled_image}, simultaneous=True)-variable)

    def test_finite_cylinder_residual_coefficients(self):
        s = sp.Symbol("s", nonzero=True)

        def residual(polynomial):
            omega = polynomial-s*sp.diff(polynomial, s)
            g = sp.cancel(sp.diff(polynomial, s, 2)/omega)
            tensor = sp.cancel(-sp.diff(g, s)-2*s*g**2)
            h = sp.cancel(-(3*s*g+sp.diff(tensor, s)/tensor)/4)
            return sp.cancel(sp.diff(h, s)+h**2+s*g*h-g)

        for degree in (2, 3, 4):
            with self.subTest(degree=degree):
                self.zero(residual(s**degree)
                          +sp.Rational((3*degree-1)*(degree-3), 16)/s**2)
        a, b, c, d = sp.symbols("a b c d", nonzero=True)
        cubic = a*s**3+b*s**2+c*s+d
        numerator, denominator = sp.fraction(residual(cubic))
        np, dp = sp.Poly(numerator, s), sp.Poly(denominator, s)
        self.assertEqual(dp.degree()-np.degree(), 3)
        self.zero(np.LC()/dp.LC()-35*b/(64*a))
        numerator, denominator = sp.fraction(residual(cubic.subs(b, 0)))
        np, dp = sp.Poly(numerator, s), sp.Poly(denominator, s)
        self.assertEqual(dp.degree()-np.degree(), 5)
        self.zero(np.LC()/dp.LC()+315*d/(64*a))
        self.zero(residual(a*s**3+c*s))


if __name__ == "__main__":
    unittest.main(verbosity=2)
