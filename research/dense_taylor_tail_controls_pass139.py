"""Finite exact dense-chart and Taylor-tail controls for pass139.

The determinant jets, truncated differential-field expansions, and plane-line
embedding controls are not asserted to realize sliced four-dimensional frames.
The actual examples in the third method have explicit polynomial inverses and
a slice. They are already translations in adapted coordinates. None of these
finite tests proves the general chart, exact-field descent, embedded-line
theorem, or unrestricted cancellation. No earlier checker or solver is imported.
"""

import unittest

import sympy as sp


class DenseTaylorTailControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_formal_determinant_and_top_three_coefficients(self):
        X = sp.Symbol("X")
        yt, yr, yv, zt, zr, zv = sp.symbols("yt yr yv zt zr zv")
        h, M = yt+zr, yt*zr-yr*zt
        A0, B0 = yr*zv-yv*zr, yv*zt-yt*zv
        for degree in (0, 1, 2, 4):
            wt = sp.symbols(f"wt0:{degree+1}")
            wr = sp.symbols(f"wr0:{degree+1}")
            wv = sp.symbols(f"wv0:{degree+1}")
            Wt = sum(wt[j]*X**j for j in range(degree+1))
            Wr = sum(wr[j]*X**j for j in range(degree+1))
            Wv = sum(wv[j]*X**j for j in range(degree+1))
            matrix = sp.Matrix([[yt+X, yr, yv], [zt, zr+X, zv],
                                [Wt, Wr, Wv]])
            determinant = sp.expand(matrix.det())
            expected = (X**2+h*X+M)*Wv+(A0-X*yv)*Wt+(B0-X*zv)*Wr
            self.assert_zero(determinant-expected)
            # Cramer's selected column uses these signed minors, not their negatives.
            for column, numerator in enumerate((A0-X*yv, B0-X*zv, X**2+h*X+M)):
                replaced = matrix.copy()
                replaced[:, column] = sp.Matrix([0, 0, 1])
                self.assert_zero(replaced.det()-numerator)
            polynomial = sp.Poly(determinant, X)
            for j in range(degree+3):
                target = wv[j-2] if 0 <= j-2 <= degree else 0
                if 0 <= j-1 <= degree:
                    target += h*wv[j-1]-yv*wt[j-1]-zv*wr[j-1]
                if j <= degree:
                    target += M*wv[j]+A0*wt[j]+B0*wr[j]
                self.assert_zero(polynomial.coeff_monomial(X**j)-target)
            self.assert_zero(polynomial.coeff_monomial(X**(degree+2))-wv[-1])
            if degree == 0:
                # Even m=0 has two positive-degree equations; J=1 is not automatic.
                self.assert_zero(polynomial.coeff_monomial(X)-h*wv[0]
                                 + yv*wt[0]+zv*wr[0])
                self.assert_zero(polynomial.coeff_monomial(1)-M*wv[0]
                                 - A0*wt[0]-B0*wr[0])

        # Independent fixed-v chain expansion of the first two integrations.
        y, z, ft, fr, ftt, ftr, frr, gt, gr, g, c = sp.symbols(
            "y z ft fr ftt ftr frr gt gr g c")
        p = ft*y+fr*z+g
        pt = ftt*y+ftr*z+gt+ft*yt+fr*zt
        pr = ftr*y+frr*z+gr+ft*yr+fr*zr
        pv = sp.diff(p, y)*yv+sp.diff(p, z)*zv
        self.assert_zero(pv-yv*ft-zv*fr)
        integrated = ftt*y**2/2+ftr*y*z+frr*z**2/2+gt*y+gr*z+c
        integrated_v = sp.diff(integrated, y)*yv+sp.diff(integrated, z)*zv
        third_coefficient = integrated_v+h*pv-yv*pt-zv*pr+A0*ft+B0*fr
        self.assert_zero(third_coefficient)

    def test_finite_taylor_products_in_an_algebraic_coefficient_field(self):
        a, rho, U, V, e = sp.symbols("a rho U V e")
        tau = a**2
        dt = lambda f: sp.cancel(sp.diff(f, a)/(2*a))
        dr = lambda f: sp.diff(f, rho)
        order = 4

        def repeated(operator, value, number):
            for _ in range(number):
                value = operator(value)
            return value

        def theta(value):
            result = 0
            for total in range(order+1):
                for i in range(total+1):
                    j = total-i
                    derivative = repeated(dt, repeated(dr, value, j), i)
                    result += derivative*U**i*V**j*e**total/sp.factorial(i)/sp.factorial(j)
            return sp.expand(result)

        def truncate(value):
            polynomial = sp.Poly(sp.expand(value), e)
            return sum(polynomial.coeff_monomial(e**j)*e**j for j in range(order+1))

        self.assert_zero(dt(tau)-1)
        self.assert_zero(dr(rho)-1)
        f, g = a*rho+1/a, a**2+rho**2
        self.assert_zero(dt(dr(f))-dr(dt(f)))
        self.assert_zero(theta(f+g)-theta(f)-theta(g))
        self.assert_zero(truncate(theta(f)*theta(g))-theta(f*g))
        self.assert_zero(theta(tau)-(tau+U*e))
        self.assert_zero(theta(rho)-(rho+V*e))
        expected_a = a+U*e/(2*a)-U**2*e**2/(8*a**3)+U**3*e**3/(16*a**5)
        expected_a -= 5*U**4*e**4/(128*a**7)
        self.assert_zero(theta(a)-expected_a)
        self.assert_zero(truncate(theta(a)**2)-(tau+U*e))
        # The deck involution fixes C(tau,rho) but not a. This is an actual
        # coefficient-field extension, not an assumption L=C(tau,rho).
        self.assert_zero(tau.subs(a, -a)-tau)
        self.assertNotEqual(sp.expand(a.subs(a, -a)-a), 0)
        self.assert_zero(theta(a).subs(a, -a)+theta(a))

    def test_actual_dense_slice_family_and_two_negative_tail_stages(self):
        u, a, b, c = sp.symbols("u a b c")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, originals = (u, a, b, c), (X, Y, Z, W)
        good = (u, a+b*u, b+c*u)
        E = lambda f: sp.expand(sp.diff(f, u))
        T = lambda f: sp.expand(sp.diff(f, c)-u*sp.diff(f, b)+u**2*sp.diff(f, a))
        for ell in (None, 3, 4):
            with self.subTest(last_degree=ell):
                shear = 0 if ell is None else good[1]**ell
                frame = sp.Matrix(good+(c+shear,))
                inverse_c = W if ell is None else W-Y**ell
                inverse_b = Z-inverse_c*X
                inverse_a = Y-inverse_b*X
                inverse = sp.Matrix([X, inverse_a, inverse_b, inverse_c])
                for value, target in zip(inverse, adapted):
                    self.assert_zero(value.subs(dict(zip(originals, frame)), simultaneous=True)-target)
                for value, target in zip(frame, originals):
                    self.assert_zero(value.subs(dict(zip(adapted, inverse)), simultaneous=True)-target)
                self.assert_zero(frame.jacobian(adapted).det()-1)
                self.assertEqual(tuple(E(f) for f in good), (1, b, c))
                for f in good:
                    self.assert_zero(E(E(f)))
                self.assert_zero(E(frame[0])-1)
                for index, value in enumerate(frame):
                    self.assert_zero(T(value)-(1 if index == 3 else 0))
                self.assertEqual(sp.Poly(sp.expand(frame[3]), u).degree(), 0 if ell is None else ell)
                if ell is not None:
                    self.assert_zero(sp.diff(frame[3], u, ell)-sp.factorial(ell)*b**ell)
                    self.assert_zero(sp.diff(frame[3], u, ell+1))
                self.assert_zero(frame[3]-shear-c)

        # Exact rank/density certificates for this actual speed row.
        t = sp.Symbol("t")
        self.assert_zero(sp.Matrix([b, c]).jacobian([b, c]).det()-1)
        self.assert_zero(sp.Matrix([t, t*b, t*c]).jacobian([t, b, c]).det()-t**2)
        self.assert_zero(E(T(a))-T(E(a))-2*u)
        self.assert_zero(E(E(T(a)))-2)
        N = lambda f: sp.Poly(T(f), u).coeff_monomial(u**2)
        for f in (a, b, c):
            self.assert_zero(N(f)-sp.diff(f, a))

        # tau=b, rho=c, y=a, z=b. All sheared powers are exact Taylor terms.
        tau, rho, y, z, e = sp.symbols("tau rho y z e")
        R1 = -z
        fminus1 = -tau
        F = R1-fminus1
        R2 = -sp.diff(fminus1, tau)*y-sp.diff(fminus1, rho)*z
        self.assert_zero(-F-(z-tau))
        self.assert_zero(R2-y)
        self.assert_zero(sp.diff(R2, y)-sp.diff(F, tau))
        self.assert_zero(sp.diff(R2, z)-sp.diff(F, rho))
        for ell in (0, 3, 4):
            actual_W = rho if ell == 0 else rho+(y+tau/e)**ell
            S = rho+z*e if ell == 0 else rho+z*e+(y+tau/e)**ell
            R = sp.cancel(actual_W-S)
            self.assert_zero(R+z*e)
            corrected = sp.expand(R-e*(-tau-y*e))
            self.assert_zero(corrected.subs(z, tau)-y*e**2)
        self.assert_zero(T(-b/u)-1)
        self.assert_zero(T(a/u**2)-1)
        self.assert_zero(N(a)-1)

    def test_whole_line_does_not_make_either_generator_linear(self):
        v, U, V, H, F = sp.symbols("v U V H F")
        y, z = v**2, v+v**4
        self.assert_zero(z-y**2-v)
        self.assertEqual(sp.Poly(y, v).degree(), 2)
        self.assertEqual(sp.Poly(z, v).degree(), 4)
        relation = (V-U**2)**2-U
        self.assert_zero(relation.subs({U: y, V: z}, simultaneous=True))
        # This is an actual plane automorphism completing the embedded line,
        # not an assertion of an actual sliced four-coordinate dense chart.
        plane = (V-U**2, relation)
        inverse = (H**2-F, H+(H**2-F)**2)
        for value, target in zip(plane, (H, F)):
            self.assert_zero(value.subs(dict(zip((U, V), inverse)), simultaneous=True)-target)
        for value, target in zip(inverse, (U, V)):
            self.assert_zero(value.subs(dict(zip((H, F), plane)), simultaneous=True)-target)

        # A quotient parameter need not itself complete the defining coordinate.
        G, P = V, U+V*U**2
        self.assert_zero(P.subs(V, 0)-U)
        jacobian = sp.Matrix([G, P]).jacobian([U, V]).det()
        self.assert_zero(jacobian+(1+2*U*V))
        self.assertNotEqual(sp.diff(jacobian, U), 0)
        self.assert_zero(jacobian.subs({U: 1, V: -sp.Rational(1, 2)}))


if __name__ == "__main__":
    unittest.main()
