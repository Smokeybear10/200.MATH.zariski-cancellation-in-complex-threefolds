"""Standalone finite exact-algebra controls for the five pass210 notes.

No earlier checker or proof implementation is imported. These identities
do not certify the universal field, conductor, cone, immersion, cofactor,
irreducibility/valuation or recognition arguments. Formal coefficient
fixtures are not asserted to be actual frames. Actual elementary maps are
checked as polynomial maps, not inferred from generic parameters.

The affine-pair boundary intentionally retains P^2 Z != 0 and E(PW) != 0.
The full cancellation goal and recognition of that boundary remain open.
"""

import unittest

import sympy as sp


class RadicalWholePlaneReductionControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_center_fibers_and_local_gradient_orders(self):
        x, U, V, s, mu, nu, c, Vc = sp.symbols("x U V s mu nu c Vc")
        R = x**2 - s**2
        theta = Vc + R/2
        y = mu*theta + nu + c*x
        columns = []
        for power in range(2):
            remainder = sp.rem(sp.expand(y*x**power), R, x)
            columns.append(sp.Matrix([sp.expand(remainder).coeff(x, j)
                                      for j in range(2)]))
        characteristic = sp.Matrix.hstack(*columns).charpoly(U).as_expr()
        expected = (U - mu*Vc - nu)**2 - c**2*s**2
        self.zero(characteristic - expected)
        self.zero(characteristic.subs(s, 0) - (U - mu*Vc - nu)**2)
        for root in (s, -s):
            self.zero(sp.diff(expected, U).subs(U, y.subs(x, root)) - 2*c*root)

        eps, r1, r2, B0, B1, C0, C1, Lt, Lr = sp.symbols(
            "eps r1 r2 B0 B1 C0 C1 Lt Lr"
        )
        local_R = r1*eps + r2*eps**2
        local_B, local_C = B0 + B1*eps, C0 + C1*eps
        HU = -local_R*(local_C*local_B + local_R*Lt)
        HV = -local_R*(local_C**2 + local_R*Lr)
        self.zero(sp.expand(HU).coeff(eps, 1) + r1*C0*B0)
        self.zero(sp.expand(HU.subs(C0, 0)).coeff(eps, 1))
        self.zero(sp.expand(HV.subs(C0, 0)).coeff(eps, 2) + r1**2*Lr)
        repeated_HV = -r2*eps**2*(local_C**2 + r2*eps**2*Lr)
        self.zero(sp.expand(repeated_HV).coeff(eps, 2) + r2*C0**2)
        yt, yr, yv, wt, wr, wv = sp.symbols("yt yr yv wt wr wv")
        root_wedge = sp.Matrix([[yt, yr, yv], [B0, C0, 0],
                               [wt, wr, wv]]).det()
        self.zero(root_wedge.subs({C0: 0, yr: 0, yv: 0}))

        # Literal degree slots used by both quadratic-second arguments.
        tau, eta, kappa, Fu, Fv, F0 = sp.symbols("tau eta kappa Fu Fv F0")
        G = (U - mu*V - nu)**2 - tau*(V - Vc)
        model = G**2*(Fu*U + Fv*V + F0) + eta*2*(V - Vc)*G
        self.zero(sp.Poly(model, U, V).coeff_monomial(U**5) - Fu)
        self.zero(sp.Poly(model.subs(Fu, 0), U, V).coeff_monomial(U**4*V) - Fv)
        self.zero(sp.Poly(kappa**2*(U - mu*V)**4, U, V)
                  .coeff_monomial(U**3*V) + 4*kappa**2*mu)

    def test_zero_center_constant_projection_and_affine_pair_boundary(self):
        U, V, t, rho, X, v = sp.symbols("U V t rho X v")
        A, Ap, App, B, Bp, Bpp, n0, n0p = sp.symbols(
            "A Ap App B Bp Bpp n0 n0p"
        )
        b, c = t*Ap + Bp, t*App + Bpp
        n = b**2/4 + n0
        nt, nr = b*Ap/2, b*c/2 + n0p
        ell = -c*b**2/8 - b*n0p/2
        S = Ap*U*V + c*V**2/2 + nt*U + nr*V
        xi = V + b/2
        D = -Ap*U/2 - c*xi/4 - n0p/2
        R = 2*V + b
        self.zero(S.subs(V, -b/2) - ell)
        self.zero(S - ell + R*D)
        z = 2*rho*D + V**2 + A*U + b*V + n
        self.zero(z - (xi**2 + (A - rho*Ap)*U + n0
                       - rho*n0p - rho*c*xi/2))
        jets = sp.symbols("yt yr yv ht hr hv wt wr wv Du Dv rr")
        yt, yr, yv, ht, hr, hv, wt, wr, wv, Du, Dv, rr = jets
        J = sp.Matrix([[yt, yr, yv], [rr*(ht-Du), rr*(hr-Dv), rr*hv],
                       [wt, wr, wv]]).det()
        divided = sp.Matrix([[yt, yr, yv], [ht-Du, hr-Dv, hv],
                             [wt, wr, wv]]).det()
        self.zero(J - rr*divided)

        qrr, A2, A1, A0, f1, f0 = sp.symbols("qrr A2 A1 A0 f1 f0")
        g3, g2, g1, g0 = sp.symbols("g3 g2 g1 g0")
        quadratic_w = A2*U**2 + A1*U + A0
        fourth = qrr*quadratic_w**2/2 + (f1*U + f0)*quadratic_w \
            + g3*U**3 + g2*U**2 + g1*U + g0
        self.zero(sp.expand(fourth).coeff(U, 4) - qrr*A2**2/2)

        a = sp.symbols("a", nonzero=True)
        q, qr, k, kt, kr, nc, theta_c = sp.symbols("q qr k kt kr nc theta_c")
        py, y0, pw, w0 = sp.symbols("py y0 pw w0")
        y = py*v + y0
        w = pw*v + w0
        z = qr*w + qrr*theta_c**2/2 + kt*y + kr*theta_c + nc
        Y, W = y + t*X, w + theta_c*X + rho*X**2
        Z = z + (qr*theta_c + k)*X + q*X**2
        E = lambda expression: a*sp.diff(expression, X)
        P = lambda expression: a*sp.diff(expression, v)
        for coordinate in (X, Y, Z, W):
            self.zero(P(P(coordinate)))
            self.zero(E(P(coordinate)))
            self.zero(E(P(coordinate)) - P(E(coordinate)))

        # A separate affine-pair fixture: not a nice/invariant-coefficient case.
        btheta, theta0, mu, nu, lam, omega = sp.symbols(
            "btheta theta0 mu nu lam omega"
        )
        theta = btheta*v + theta0
        y, w = mu*theta + nu, lam*theta + omega
        z = theta**2 + (2*rho*lam + kt*mu + kr)*theta \
            + 2*rho*omega + kt*nu + nc
        Y, W = y + t*X, w + theta*X + rho*X**2
        Z = z + (2*rho*theta + k)*X + rho**2*X**2
        self.zero(P(P(Z)) - 2*a**2*btheta**2)
        self.zero(P(P(P(Z))))
        self.zero(P(P(Y)))
        self.zero(P(P(W)))
        self.zero(E(P(W)) - a**2*btheta)
        self.zero(E(P(Z)) - 2*a**2*rho*btheta)
        for coordinate in (X, Y, Z, W):
            self.zero(E(P(coordinate)) - P(E(coordinate)))
        ktt, ktr, krr, n_t, n_r, ell0 = sp.symbols("ktt ktr krr n_t n_r ell0")
        formal_y, formal_w = mu*V + nu, lam*V + omega
        third = (2*V + kr)*formal_w + ktt*formal_y**2/2 \
            + ktr*formal_y*V + krr*V**2/2 + n_t*formal_y + n_r*V - ell0
        self.zero(2*sp.expand(third).coeff(V, 2)
                  - (4*lam + ktt*mu**2 + 2*ktr*mu + krr))

    def test_actual_chart_transport_centers_and_inverse_orders(self):
        t, rho, U, V, W0, s = sp.symbols("t rho U V W0 s")
        kap, A, B, C, D, F, ell = sp.symbols("kap A B C D F ell")
        alpha, beta = sp.symbols("alpha beta")
        k = kap*t**2 + A*t*rho + B*rho**2/2 + C*t + D*rho + F
        n = sp.Function("n")(t, rho)

        def S(kfun, nfun):
            return sp.diff(kfun, t, 2)*U**2/2 + sp.diff(kfun, t, rho)*U*V \
                + sp.diff(kfun, rho, 2)*V**2/2 \
                + sp.diff(nfun, t)*U + sp.diff(nfun, rho)*V

        def potential(kfun, nfun, ellfun):
            return (2*V + sp.diff(kfun, rho))*W0 + S(kfun, nfun) - ellfun

        def center(kfun, nfun, ellfun):
            return S(kfun, nfun).subs(V, -sp.diff(kfun, rho)/2) - ellfun

        def slope(kfun, nfun):
            return sp.diff(nfun, t) - sp.diff(kfun, t, rho)*sp.diff(kfun, rho)/2

        kr = sp.diff(k, rho)
        kx = k + 2*s*rho**2
        nx = n + s*(t*sp.diff(k, t) + 2*rho*kr - k) + 3*s**2*rho**2
        delta_x = -s*(t*sp.diff(n, t) + 2*rho*sp.diff(n, rho)) \
            - s**2*(t**2*sp.diff(k, t, 2)/2 + 2*t*rho*sp.diff(k, t, rho)
                     + 2*rho**2*sp.diff(k, rho, 2) + rho*kr) - 4*s**3*rho**2
        shifted = {U: U-s*t, V: V-2*s*rho, W0: W0-s*V+s**2*rho}
        self.zero(potential(kx, nx, ell+delta_x).subs(shifted, simultaneous=True)
                  - potential(k, n, ell))
        self.zero(center(kx, nx, ell+delta_x).subs(U, U-s*t) - center(k, n, ell))
        self.zero(2*(V-2*s*rho) + sp.diff(kx, rho) - (2*V+kr))
        self.zero(slope(kx, nx) - slope(k, n) - 2*kap*s*t)

        l = alpha*t + beta
        kw = k - 2*rho*l
        nw = n - kr*l + l**2
        delta_w = sp.diff(n, rho)*l - sp.diff(k, rho, 2)*l**2/2
        self.zero(potential(kw, nw, ell+delta_w).subs(
            {V: V+l, W0: W0+alpha*U}, simultaneous=True) - potential(k, n, ell))
        self.zero(center(kw, nw, ell+delta_w) - center(k, n, ell))
        self.zero(2*(V+l) + sp.diff(kw, rho) - (2*V+kr))
        self.zero(slope(kw, nw) - slope(k, n))
        self.zero(potential(k-C*t-F, n, ell) - potential(k, n, ell))
        normalized_k = (k + 2*(-B/4)*rho**2) - 2*rho*(A*t/2+D/2) - C*t-F
        self.zero(normalized_k - kap*t**2)

        # Reconstruct the n transports from the second potential itself.
        y, theta, w, X = sp.symbols("y theta w X")
        z = 2*rho*w + theta**2 + sp.diff(k, t)*y + kr*theta + n
        zx = z - s*(2*rho*theta+k) + s**2*rho**2
        zx_from_new = 2*rho*(w-s*theta+s**2*rho) + (theta-2*s*rho)**2 \
            + sp.diff(kx, t)*(y-s*t) + sp.diff(kx, rho)*(theta-2*s*rho) + nx
        self.zero(zx - zx_from_new)
        zw_from_new = 2*rho*(w+alpha*y) + (theta+l)**2 \
            + sp.diff(kw, t)*y + sp.diff(kw, rho)*(theta+l) + nw
        self.zero(z - zw_from_new)

        Y, Z, W, Xn, Yn, Zn, Wn = sp.symbols("Y Z W Xn Yn Zn Wn")
        forwards = [X+s, Y, Z-C*Y-F*(X+s), W+alpha*Y+beta*(X+s)]
        inverses = [Xn-s, Yn, Zn+C*Yn+F*Xn, Wn-alpha*Yn-beta*Xn]
        source, target = (X, Y, Z, W), (Xn, Yn, Zn, Wn)
        for value, expected in zip(forwards, target):
            self.zero(value.subs(dict(zip(source, inverses)), simultaneous=True) - expected)
        for value, expected in zip(inverses, source):
            self.zero(value.subs(dict(zip(target, forwards)), simultaneous=True) - expected)
        for value, expected in zip(inverses, (0, 0, 1, 0)):
            self.zero(sp.diff(value, Zn) - expected)

    def test_quadratic_second_models_and_original_square(self):
        U, V, alpha, beta, ell, ellt, ellr, m, eta, tau = sp.symbols(
            "U V alpha beta ell ellt ellr m eta tau"
        )
        kap = sp.symbols("kap", nonzero=True)
        p = kap*U**2 + alpha*U - ell
        G = p/kap - tau*V
        model = kap**2*G**2 + 2*eta*V*G
        self.zero(sp.expand(model).coeff(V, 1) - 2*p*(eta/kap-kap*tau))
        self.zero(model.subs(eta, kap**2*tau) - p**2 + kap**2*tau**2*V**2)
        S = kap*U**2 + alpha*U + beta*V
        T = ell-S
        literal = T**2 + 2*V*beta*T + 4*V**2*(-ellt*U-ellr*V-m)
        residual = sp.Poly(literal-model.subs(eta, kap**2*tau), U, V)
        self.zero(residual.coeff_monomial(U*V**2) + 4*ellt)
        self.zero(residual.coeff_monomial(V**3) + 4*ellr)
        self.zero(residual.coeff_monomial(V**2) - (kap**2*tau**2-beta**2-4*m))
        self.zero(sp.discriminant(p, U) - (alpha**2+4*kap*ell))
        self.zero(p.subs(ell, -alpha**2/(4*kap)) - kap*(U+alpha/(2*kap))**2)

        X, y, t, rho, d0 = sp.symbols("X y t rho d0")
        c0 = sp.symbols("c0", nonzero=True)
        theta = (d0-kap*y**2)/c0
        z = rho*c0 + theta**2 + 2*kap*t*y
        Yf = y+t*X
        Wf = c0+2*theta*X+2*rho*X**2
        Zf = z+(2*rho*theta+kap*t**2)*X+rho**2*X**2
        square_expression = Wf**2+4*kap*X*Yf**2-4*X**2*Zf-4*d0*X
        self.zero(square_expression-c0**2)
        self.zero(square_expression.subs(d0, 0)-c0**2)
        Y, Z, W = sp.symbols("Y Z W")
        constant = W**2+4*kap*X*Y**2-4*d0*X
        self.zero(constant.subs(X, 0)-W**2)
        self.assertEqual(sp.gcd(-4*X**2, constant), 1)
        self.zero(sp.diff(constant-4*X**2*Z, Z)+4*X**2)
        # The gcd is an algebra control, not a test of the valuation theorem.
        h, gamma, Y1, Z1, W1 = sp.symbols("h gamma Y1 Z1 W1")
        forward = [Y+h, Z-gamma, 2*W+beta]
        inverse = [Y1-h, Z1+gamma, (W1-beta)/2]
        for expression, expected in zip(forward, (Y1, Z1, W1)):
            self.zero(expression.subs(dict(zip((Y, Z, W), inverse)), simultaneous=True)-expected)
        for expression, expected in zip(inverse, (Y, Z, W)):
            self.zero(expression.subs(dict(zip((Y1, Z1, W1), forward)), simultaneous=True)-expected)

    def test_affine_second_conic_and_actual_affine_square(self):
        U, V, kr, ktr, nt, ntt = sp.symbols("U V kr ktr nt ntt")
        R = 2*V+kr
        slope = nt-ktr*kr/2
        coefficient = (ktr*V+nt)**2-R*ktr*(ktr*V+nt)+ntt*R**2/2
        self.zero(coefficient-slope**2-(ntt-ktr**2/2)*R**2/2)
        gamma = sp.symbols("gamma", nonzero=True)
        A0, A1, A2, ell, ellt, ellr, eta, ntr, nrr, nr, m = sp.symbols(
            "A0 A1 A2 ell ellt ellr eta ntr nrr nr m"
        )
        graph = U-A2*V**2-A1*V-A0
        model = gamma**2*graph**2+2*eta*V*graph
        self.zero(sp.Poly(model, U, V).coeff_monomial(U) + 2*gamma**2*A0)
        self.zero(sp.Poly(model, U, V).coeff_monomial(U*V) + 2*gamma**2*A1-2*eta)
        reduced_model = model.subs({A0: ell/gamma, eta: gamma**2*A1})
        self.zero(reduced_model-gamma**2*((U-ell/gamma-A2*V**2)**2-A1**2*V**2))
        literal = (ell-gamma*U)**2+2*ntt*U**2*V**2+4*ntr*U*V**3 \
            +2*nrr*V**4-4*ellt*U*V**2-4*ellr*V**3-(nr**2+4*m)*V**2
        residual = sp.Poly(literal-reduced_model, U, V)
        for monomial, expected in ((U**2*V**2, 2*ntt), (U*V**3, 4*ntr),
                                   (U*V**2, -4*ellt+2*gamma**2*A2),
                                   (V**3, -4*ellr), (V**4, 2*nrr-gamma**2*A2**2)):
            self.zero(residual.coeff_monomial(monomial)-expected)

        X, x, t, rho, theta, lam, n1, n2, ell0 = sp.symbols(
            "X x t rho theta lam n1 n2 ell0"
        )
        n = gamma*t+lam**2*rho**2+n1*rho+n2
        ell = gamma*lam*t+ell0
        w = x-lam*theta-lam**2*rho-n1/2
        y = (ell-2*theta*x+2*lam*theta**2)/gamma
        z = 2*rho*w+theta**2+n
        Yf, Zf, Wf = y+t*X, z+2*rho*theta*X+rho**2*X**2, w+theta*X+rho*X**2
        H0 = theta+2*lam*rho
        j = H0+rho*U
        T0 = gamma*t-4*lam*rho*H0+4*lam**2*rho**2
        W0f = (Wf+n1/2).subs(X, U+lam)
        Z0f = (Zf-n2).subs(X, U+lam)
        V0f = (gamma*Yf-2*lam*Zf-ell0+2*lam*n2).subs(X, U+lam)
        self.zero(W0f-x-U*j)
        self.zero(Z0f-(T0+2*rho*x+j**2-2*lam*rho**2*U))
        self.zero(V0f-(-2*x*H0+T0*U-2*lam*rho**2*U**2))
        self.zero(W0f**2+U*V0f-U**2*Z0f-x**2)

        Y, Z, W, V0, Z0, W0 = sp.symbols("Y Z W V0 Z0 W0")
        forward = [X-lam, gamma*Y-2*lam*Z-ell0+2*lam*n2, Z-n2, W+n1/2]
        inverse = [U+lam, (V0+2*lam*Z0+ell0)/gamma, Z0+n2, W0-n1/2]
        source, target = (X, Y, Z, W), (U, V0, Z0, W0)
        for expression, expected in zip(forward, target):
            self.zero(expression.subs(dict(zip(source, inverse)), simultaneous=True)-expected)
        for expression, expected in zip(inverse, source):
            self.zero(expression.subs(dict(zip(target, forward)), simultaneous=True)-expected)
        I = W0**2+U*V0-U**2*Z0
        self.zero(sp.diff(I, V0)-U)
        self.zero(I.subs(U, 0)-W0**2)
        self.assertEqual(sp.gcd(U, W0**2-U**2*Z0), 1)


if __name__ == "__main__":
    unittest.main()
