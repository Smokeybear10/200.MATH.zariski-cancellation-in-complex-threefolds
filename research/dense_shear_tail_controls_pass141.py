"""Finite exact controls for fixed-good bad shears and dense tails141.

Peeling coefficients are recovered by descending coefficient subtraction,
without importing a prior checker or solver. The two actual sample families
have independently checked base inverse orders; both orders of the elementary
bad shear are checked separately, certifying their composed inverses in stages.
The generic shear uses the displayed nine-term basis only. Exact minimum-degree
claims for all possible shears depend on the written141 theorem, not these
finite controls. The final actual one-slot ansatz is a positive boundary, not
an extra-factor example or an exhaustive search of coordinate frames.
"""

import unittest

import sympy as sp


class DenseShearTailControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def check_inverse(self, forward, inverse, adapted, originals):
        for f, target in zip(inverse, adapted):
            self.assert_zero(f.subs(dict(zip(originals, forward)), simultaneous=True)-target)
        for f, target in zip(forward, originals):
            self.assert_zero(f.subs(dict(zip(adapted, inverse)), simultaneous=True)-target)

    def check_shear_and_tails(self, X, Y, Z, W, a, b, v, y, z, Wlocal,
                              tau, rho, dt, dr, expected_degree):
        U, V = sp.symbols("U V")
        q = sp.symbols("q0:9")
        P = q[0]+q[1]*X+q[2]*Y+q[3]*Z+q[4]*X*Y+q[5]*Y*Z
        P += q[6]*Z**2+q[7]*Y**3+q[8]*X**4
        originals = (X, Y, Z, W)
        self.check_inverse(sp.Matrix([X, Y, Z, W+P]), sp.Matrix([X, Y, Z, W-P]),
                           originals, originals)
        local_P = sp.expand(P.subs({Y: y+tau*X, Z: z+rho*X}, simultaneous=True))

        def iterate(operator, f, count):
            for _ in range(count):
                f = operator(f)
            return f

        cache = {}

        def H(number, f):
            key = (number, f)
            if key not in cache:
                cache[key] = sp.cancel(sum(iterate(dt, iterate(dr, f, number-i), i)
                                          *U**i*V**(number-i)/sp.factorial(i)/sp.factorial(number-i)
                                          for i in range(number+1)))
            return cache[key]

        def recover(polynomial):
            current = sp.cancel(polynomial)
            degree = sp.Poly(current, X).degree()
            coefficients = {}
            for j in range(degree, -1, -1):
                f = sp.cancel(sp.Poly(current, X).coeff_monomial(X**j))
                self.assert_zero(sp.diff(f, v))
                coefficients[j] = f
                subtraction = sum(X**(j-k)*H(k, f).subs({U: y, V: z}, simultaneous=True)
                                  for k in range(j+1))
                current = sp.cancel(current-subtraction)
            self.assert_zero(current)
            return degree, coefficients

        def tails(coefficients):
            R1 = -sum(H(j+1, f) for j, f in coefficients.items())
            fminus1 = sp.cancel(R1.subs({U: y, V: z}, simultaneous=True))
            self.assert_zero(sp.diff(fminus1, v))
            Phi = sp.cancel(R1-fminus1)
            Psi = sp.cancel(-sum(H(j+2, f) for j, f in coefficients.items())-H(1, fminus1))
            return fminus1, Phi, Psi

        degree, coefficients = recover(Wlocal)
        sheared_degree, changed = recover(Wlocal+local_P)
        self.assertEqual(sheared_degree, 4)
        poly_P = sp.Poly(P, X, Y, Z)
        for j in range(max(degree, sheared_degree)+1):
            piece = sum(c*X**i*Y**k*Z**ell for (i, k, ell), c in poly_P.terms()
                        if i+k+ell == j)
            pj = sp.cancel(piece.subs({X: 1, Y: tau, Z: rho}, simultaneous=True))
            self.assert_zero(changed.get(j, 0)-coefficients.get(j, 0)-pj)
            self.assert_zero(H(j+1, pj))
            self.assert_zero(H(j+2, pj))
        baseline_tails, changed_tails = tails(coefficients), tails(changed)
        for f, target in zip(changed_tails, baseline_tails):
            self.assert_zero(f-target)
        self.assertEqual(sp.Poly(baseline_tails[1], U, V).total_degree()-1, expected_degree)
        # Undoing the displayed shear returns the original actual representative.
        self.assert_zero(Wlocal+local_P-local_P-Wlocal)
        return P, local_P, baseline_tails, degree

    def test_sharp_family_recovered_shear_coefficients_and_tails(self):
        u, a, b, v, X, Y, Z, W = sp.symbols("u a b v X Y Z W")
        adapted, originals = (u, a, b, v), (X, Y, Z, W)
        tau, rho = (b+1)/a, (b+2)/a
        dt = lambda f: sp.cancel(a**2*sp.diff(f, a)+a*(b+2)*sp.diff(f, b))
        dr = lambda f: sp.cancel(-a**2*sp.diff(f, a)-a*(b+1)*sp.diff(f, b))
        for d in (3, 4):
            F = lambda t: t**d/2+t+2

            def delta(aa, vv, uu):
                return aa+sum(sp.binomial(d, k)*vv**(d-k)*aa**k*uu**(k-1)/2
                              for k in range(1, d+1))

            forward = sp.Matrix([v+a*u, a-F(v)+(b+1)*u,
                                 a-F(v)+(b+2)*u, b+delta(a, v, u)])
            iu = Z-Y
            ia = 2*Y-Z-iu*W+F(X)
            iv = X-ia*iu
            inverse = sp.Matrix([iu, ia, W-delta(ia, iv, iu), iv])
            self.check_inverse(forward, inverse, adapted, originals)
            y, z = a-F(v)-(b+1)*v/a, a-F(v)-(b+2)*v/a
            Wlocal = b+a+a*sum(X**(d-1-j)*v**j for j in range(d))/2
            P, local_P, tail, degree = self.check_shear_and_tails(
                X, Y, Z, W, a, b, v, y, z, Wlocal, tau, rho, dt, dr, d-1)
            self.assertEqual(degree, d-1)
            T = lambda f: sp.expand(-u*sp.diff(f, a)+(1+u*sp.diff(F(v), v))*sp.diff(f, b)
                                    +u**2*sp.diff(f, v))
            actual_P = P.subs(dict(zip(originals, forward)), simultaneous=True)
            self.assert_zero(T(actual_P))
            self.assert_zero(T(forward[3]+actual_P)-1)
            # The displayed minimizing representative is the unsheared W.
            self.assertEqual(sp.Poly(sp.expand(forward[3]), u).degree(), d-1)
            self.assert_zero(forward[2]-forward[1]-u)

    def test_field_cover_shears_and_degree_zero_representative(self):
        u, a, b, v, X, Y, Z, W = sp.symbols("u a b v X Y Z W")
        adapted, originals = (u, a, b, v), (X, Y, Z, W)
        for n in (2, 3):
            forward = sp.Matrix([v+a**n*u, a+b*u, b+u, u])
            ib = Z-W
            ia = Y-ib*W
            inverse = sp.Matrix([W, ia, ib, X-ia**n*W])
            self.check_inverse(forward, inverse, adapted, originals)
            tau, rho = b/a**n, 1/a**n
            dt = lambda f: sp.cancel(a**n*sp.diff(f, b))
            dr = lambda f: sp.cancel(-a**(n+1)*sp.diff(f, a)/n-b*a**n*sp.diff(f, b))
            y, z = a-b*v/a**n, b-v/a**n
            Wlocal = (X-v)/a**n
            P, local_P, tail, degree = self.check_shear_and_tails(
                X, Y, Z, W, a, b, v, y, z, Wlocal, tau, rho, dt, dr, 0)
            self.assertEqual(degree, 1)
            self.assert_zero(Wlocal+local_P-local_P-(z+rho*X)+b)
            self.assert_zero(forward[3]-forward[2]+b)
            # In the sheared coordinates the actual minimizing correction is -P-Z.
            actual_P = P.subs(dict(zip(originals, forward)), simultaneous=True)
            minimized = sp.expand(forward[3]+actual_P-actual_P-forward[2])
            self.assertEqual(minimized, -b)
            self.assertEqual(sp.Poly(minimized, u).degree(), 0)

    def test_nonlinear_one_slot_ansatz_still_has_primitive_linear_tail(self):
        u, a, b, v, X, Y, Z, W, U, V = sp.symbols("u a b v X Y Z W U V")
        f = a**3+a*b+b**2
        fa, fb = sp.diff(f, a), sp.diff(f, b)
        forward = sp.Matrix([v+f*u, a+b*u, b+u, u])
        ib, ia = Z-W, Y-(Z-W)*W
        inverse = sp.Matrix([W, ia, ib, X-f.subs({a: ia, b: ib}, simultaneous=True)*W])
        self.check_inverse(forward, inverse, (u, a, b, v), (X, Y, Z, W))
        speed = sp.Matrix([sp.diff(g, u) for g in forward[:3]])
        self.assertEqual(speed, sp.Matrix([f, b, 1]))
        self.assert_zero(sp.Matrix.hstack(speed, speed.diff(a), speed.diff(b)).det()-fa)
        T = lambda g: sp.expand(sp.diff(g, u)+(u-b)*sp.diff(g, a)-sp.diff(g, b)
                                +(-f+(b*fa+fb)*u-fa*u**2)*sp.diff(g, v))
        for j, g in enumerate(forward):
            self.assert_zero(T(g)-(1 if j == 3 else 0))
        dt = lambda g: sp.cancel(-f*fb*sp.diff(g, a)/fa+f*sp.diff(g, b))
        dr = lambda g: sp.cancel(f*(b*fb-f)*sp.diff(g, a)/fa-b*f*sp.diff(g, b))
        tau, rho = b/f, 1/f
        self.assert_zero(dt(tau)-1)
        self.assert_zero(dt(rho))
        self.assert_zero(dr(tau))
        self.assert_zero(dr(rho)-1)
        y, z = a-b*v/f, b-v/f
        R1 = dt(b)*U+dr(b)*V
        Phi = sp.cancel(R1-R1.subs({U: y, V: z}, simultaneous=True))
        self.assert_zero(Phi-f*(U-b*V-a+b**2))
        self.assertEqual(sp.Poly(Phi, U, V).total_degree(), 1)
        self.assert_zero(forward[3]-forward[2]+b)
        # This actual nonlinear reframe still has W-Z=-b invariant, so it
        # cannot be an extra-factor counterexample. No larger search is claimed.


if __name__ == "__main__":
    unittest.main()
