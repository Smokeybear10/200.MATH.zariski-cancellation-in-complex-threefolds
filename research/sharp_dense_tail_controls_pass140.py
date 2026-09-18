"""Independent finite controls for the actual sharp dense-tail family140.

The first three methods use constant linear reframings of the retained
divided-difference family129, not new cancellation examples. Each has a linear
good-coordinate slice. Samples of degrees 2,3,4 test the explicit formulas,
including Taylor extraction with independent coefficient derivations. They do
not prove the all-polynomial family theorem, generic descent, or a general
primitivity statement for the first tail. A separate final method checks actual
degree-two and degree-three coefficient-field covers; finite samples do not
prove the uniform extension-degree theorem. No earlier checker is imported.
"""

import unittest

import sympy as sp


class SharpDenseTailControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_actual_inverse_orders_and_nonconstant_first_speed(self):
        u, a, b, v = sp.symbols("u a b v")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, originals = (u, a, b, v), (X, Y, Z, W)
        for d in (2, 3, 4):
            F = lambda t: t**d/2+t+2
            Fprime = sp.diff(F(v), v)
            T = lambda f: sp.expand(-u*sp.diff(f, a)
                                    +(1+u*Fprime)*sp.diff(f, b)+u**2*sp.diff(f, v))

            def delta(aa, vv, uu):
                return aa+sum(sp.binomial(d, k)*vv**(d-k)*aa**k*uu**(k-1)/2
                              for k in range(1, d+1))

            forward = sp.Matrix([v+a*u, a-F(v)+(b+1)*u,
                                 a-F(v)+(b+2)*u, b+delta(a, v, u)])
            inverse_u = Z-Y
            inverse_a = 2*Y-Z-inverse_u*W+F(X)
            inverse_v = X-inverse_a*inverse_u
            inverse_b = W-delta(inverse_a, inverse_v, inverse_u)
            inverse = sp.Matrix([inverse_u, inverse_a, inverse_b, inverse_v])
            for value, target in zip(inverse, adapted):
                self.assert_zero(value.subs(dict(zip(originals, forward)), simultaneous=True)-target)
            for value, target in zip(forward, originals):
                self.assert_zero(value.subs(dict(zip(adapted, inverse)), simultaneous=True)-target)
            self.assert_zero(forward.jacobian(adapted).det()-1)
            speed = sp.Matrix([sp.diff(f, u) for f in forward[:3]])
            self.assertEqual(speed, sp.Matrix([a, b+1, b+2]))
            self.assert_zero(sp.Matrix.hstack(speed, speed.diff(a), speed.diff(b)).det()-1)
            self.assert_zero(speed[2]-speed[1]-1)
            self.assert_zero(forward[2]-forward[1]-u)
            self.assertNotEqual(sp.diff(speed[0], a), 0)
            for f in forward[:3]:
                self.assert_zero(sp.diff(f, u, 2))
            self.assertEqual(sp.Poly(forward[3], u).degree(), d-1)
            self.assert_zero(sp.Poly(forward[3], u).LC()-a**d/2)
            for index, f in enumerate(forward):
                self.assert_zero(T(f)-(1 if index == 3 else 0))
            for f in (a, b, v):
                self.assert_zero(sp.Poly(T(f), u).coeff_monomial(u**2)-sp.diff(f, v))

    def test_independent_taylor_extraction_and_sharp_two_tails(self):
        a, b, v, U, V = sp.symbols("a b v U V")
        dt = lambda f: sp.expand(a**2*sp.diff(f, a)+a*(b+2)*sp.diff(f, b))
        dr = lambda f: sp.expand(-a**2*sp.diff(f, a)-a*(b+1)*sp.diff(f, b))

        def iterate(operator, f, number):
            for _ in range(number):
                f = operator(f)
            return f

        def homogeneous_taylor(number, f):
            return sp.expand(sum(iterate(dt, iterate(dr, f, number-i), i)
                                 * U**i*V**(number-i)/sp.factorial(i)/sp.factorial(number-i)
                                 for i in range(number+1)))

        tau, rho = (b+1)/a, (b+2)/a
        for coordinate in (a, b):
            self.assert_zero(dt(dr(coordinate))-dr(dt(coordinate)))
        self.assert_zero(dt(tau)-1)
        self.assert_zero(dr(tau))
        self.assert_zero(dt(rho))
        self.assert_zero(dr(rho)-1)

        for d in (2, 3, 4):
            F = lambda t: t**d/2+t+2
            y = a-F(v)-(b+1)*v/a
            z = a-F(v)-(b+2)*v/a
            # f_j are the actual nonnegative peeling coefficients. Taylor
            # derivatives are computed before evaluating independent U,V.
            coefficients = [b+a]+[sp.Integer(0)]*(d-2)+[a/2]
            R1 = -sum(homogeneous_taylor(j+1, f) for j, f in enumerate(coefficients))
            fminus1 = a*(2-a)
            self.assert_zero(R1.subs({U: y, V: z}, simultaneous=True)-fminus1)
            Phi = sp.expand(R1-fminus1)
            Psi = -sum(homogeneous_taylor(j+2, f) for j, f in enumerate(coefficients))
            Psi -= homogeneous_taylor(1, fminus1)
            D = U-V
            G = (b+2)*U-(b+1)*V+F(a*D)-a
            self.assert_zero(Phi+a*G)
            self.assert_zero(Psi-a**3*D+a**2*D*G)
            self.assert_zero(Psi.subs({U: y, V: z}, simultaneous=True)-a**2*v)
            self.assert_zero(sp.diff(Psi, U)-dt(Phi))
            self.assert_zero(sp.diff(Psi, V)-dr(Phi))
            self.assertEqual(sp.Poly(y, v).degree(), d)
            self.assertEqual(sp.Poly(z, v).degree(), d)
            self.assertEqual(sp.Poly(G, U, V).total_degree(), d)
            self.assertEqual(sp.Poly(Psi, U, V).total_degree(), d+1)

    def test_intrinsic_normalization_generating_tail_and_noncomplement(self):
        a, b, v, X, U, V, H, K = sp.symbols("a b v X U V H K")
        tau, rho = (b+1)/a, (b+2)/a
        # Coefficient partials below fix r=a^2*v, not the original adapted v.
        dt = lambda f: sp.cancel(a**2*sp.diff(f, a)+a*(b+2)*sp.diff(f, b)
                                 -2*a*v*sp.diff(f, v))
        dr = lambda f: sp.cancel(-a**2*sp.diff(f, a)-a*(b+1)*sp.diff(f, b)
                                 +2*a*v*sp.diff(f, v))
        Nv = lambda f: sp.diff(f, v)/a**2
        intrinsic = a**2*v
        self.assert_zero(dt(intrinsic))
        self.assert_zero(dr(intrinsic))
        self.assert_zero(Nv(intrinsic)-1)
        for d in (2, 3, 4):
            F = lambda t: t**d/2+t+2
            y = a-F(v)-(b+1)*v/a
            z = a-F(v)-(b+2)*v/a
            Wlocal = b+a+a*sum(X**(d-1-j)*v**j for j in range(d))/2
            local_frame = (y+tau*X, z+rho*X, Wlocal)
            matrix = sp.Matrix([[dt(f), dr(f), Nv(f)] for f in local_frame])
            self.assert_zero(matrix.det()-1)
            self.assert_zero(y-z-v/a)
            self.assert_zero(intrinsic-a**3*(y-z))

            # Exact rational generating expressions, interpreted at X=infinity.
            theta_a = a/(1-a*(y-z)/X)
            theta_b = b+a*((b+2)*y-(b+1)*z)/(X-a*(y-z))
            polynomial_C = X**(d-1)/2+1
            S = theta_b+polynomial_C*theta_a
            tail = Wlocal-S
            self.assert_zero(tail-a*(2-a)/(X-v))

            D = U-V
            G = (b+2)*U-(b+1)*V+F(a*D)-a
            Psi = a**3*D-a**2*D*G
            self.assert_zero(sp.Matrix([G, Psi]).jacobian([U, V]).det()-a**2*(G-a))
            self.assertEqual(sp.Poly(a**2*(G-a), U, V).total_degree(), d)
            # G has a complement, but the particular tail Psi is not it.
            inverse_U = K+a-(b+1)*H-F(a*H)
            inverse_V = K+a-(b+2)*H-F(a*H)
            for f, target in zip((D, G), (H, K)):
                self.assert_zero(f.subs({U: inverse_U, V: inverse_V}, simultaneous=True)-target)
            for f, target in zip((inverse_U, inverse_V), (U, V)):
                self.assert_zero(f.subs({H: D, K: G}, simultaneous=True)-target)

    def test_actual_proper_coefficient_field_covers(self):
        u, a, b, v, X, Y, Z, W, U, V = sp.symbols("u a b v X Y Z W U V")
        adapted, originals = (u, a, b, v), (X, Y, Z, W)
        for n in (2, 3):
            forward = sp.Matrix([v+a**n*u, a+b*u, b+u, u])
            inverse_b = Z-W
            inverse_a = Y-inverse_b*W
            inverse_v = X-inverse_a**n*W
            inverse = sp.Matrix([W, inverse_a, inverse_b, inverse_v])
            for f, target in zip(inverse, adapted):
                self.assert_zero(f.subs(dict(zip(originals, forward)), simultaneous=True)-target)
            for f, target in zip(forward, originals):
                self.assert_zero(f.subs(dict(zip(adapted, inverse)), simultaneous=True)-target)
            self.assert_zero(forward.jacobian(adapted).det()+1)
            speed = sp.Matrix([sp.diff(f, u) for f in forward[:3]])
            self.assertEqual(speed, sp.Matrix([a**n, b, 1]))
            self.assert_zero(sp.Matrix.hstack(speed, speed.diff(a), speed.diff(b)).det()
                             - n*a**(n-1))
            self.assert_zero(sp.diff(forward[3], u)-1)
            for f in forward:
                self.assert_zero(sp.diff(f, u, 2))

            T = lambda f: sp.expand(sp.diff(f, u)+(u-b)*sp.diff(f, a)-sp.diff(f, b)
                                    +(-a**n+n*a**(n-1)*b*u-n*a**(n-1)*u**2)*sp.diff(f, v))
            for j, f in enumerate(forward):
                self.assert_zero(T(f)-(1 if j == 3 else 0))
            for f in (a, b, v):
                self.assert_zero(sp.Poly(T(f), u).coeff_monomial(u**2)
                                 + n*a**(n-1)*sp.diff(f, v))
            intrinsic = -a**(n+1)*v/n
            Nv = lambda f: -n*sp.diff(f, v)/a**(n+1)
            self.assert_zero(Nv(intrinsic)-1)

            tau, rho = b/a**n, 1/a**n
            self.assert_zero(b-tau/rho)
            self.assert_zero(a**n-1/rho)
            omega = -sp.Integer(1) if n == 2 else (-1+sp.sqrt(3)*sp.I)/2
            self.assert_zero(omega**n-1)
            self.assertNotEqual(sp.expand(omega-1), 0)
            self.assert_zero(tau.subs(a, omega*a)-tau)
            self.assert_zero(rho.subs(a, omega*a)-rho)
            self.assertNotEqual(sp.expand(omega*a-a), 0)

            dt = lambda f: sp.expand(a**n*sp.diff(f, b))
            dr = lambda f: sp.expand(-a**(n+1)*sp.diff(f, a)/n-b*a**n*sp.diff(f, b))
            y, z = a-b*v/a**n, b-v/a**n
            Wlocal = (X-v)/a**n
            fixed_r_dr = lambda f: dr(f)+(n+1)*a**n*v*sp.diff(f, v)/n
            matrix = sp.Matrix([[dt(f), fixed_r_dr(f), Nv(f)]
                                for f in (y+tau*X, z+rho*X, Wlocal)])
            self.assert_zero(matrix.det()-1)
            self.assert_zero(dt(intrinsic))
            self.assert_zero(fixed_r_dr(intrinsic))

            # Independent first/second Taylor pieces for f_1=rho, f_0=-b.
            H1 = lambda f: dt(f)*U+dr(f)*V
            H2 = lambda f: dt(dt(f))*U**2/2+dt(dr(f))*U*V+dr(dr(f))*V**2/2
            self.assert_zero(H2(rho))
            R1 = H1(b)
            fminus1 = a**n*(a-b**2)
            g = U-b*V-a+b**2
            self.assert_zero(R1-fminus1-a**n*g)
            self.assert_zero(g.subs({U: y, V: z}, simultaneous=True))
            Psi = H2(b)-H1(fminus1)
            target = a**(2*n)*(-U*V+b*V**2+2*b*U+((n+1)*a/n-3*b**2)*V)
            self.assert_zero(Psi-target)
            self.assert_zero(Nv(Psi.subs({U: y, V: z}, simultaneous=True))-1)


if __name__ == "__main__":
    unittest.main()
