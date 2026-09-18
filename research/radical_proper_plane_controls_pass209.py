"""Finite exact-algebra controls for the three proper-plane pass209 notes.

Standalone: imports only unittest and SymPy, never proof or earlier-checker
internals. The multiplication matrices and polynomial identities below do
not prove the universal conductor, field-return, simple-factor, finite-field,
or exhaustive branch arguments. Nor do tests prove that a formal fixture is
an actual frame, that a speed is a unit, or any cancellation theorem.

The last method checks the written actual polynomial maps in both orders;
their applicability and the global-slice endpoint remain written proofs.
"""

import unittest

import sympy as sp


class RadicalProperPlaneControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_center_multiplication_and_cofactor_membership(self):
        x, U, V, c, s = sp.symbols("x U V c s")
        y0, A2, A3, kappa = sp.symbols("y0 A2 A3 kappa")
        # Exact rank-three quotient, including c=0's nonreduced center fiber.
        R = (x**2 + c) * (x - s)
        y = y0 + A2*x**2 + A3*x*(x**2 + c)
        columns = []
        for power in range(3):
            remainder = sp.rem(sp.expand(y*x**power), sp.expand(R), x)
            columns.append(sp.Matrix([
                sp.expand(remainder).coeff(x, j) for j in range(3)
            ]))
        multiplication = sp.Matrix.hstack(*columns)
        characteristic = multiplication.charpoly(U).as_expr()
        yc = y0 - A2*c
        ys = y.subs(x, s)
        expected = (U - yc)**2 * (U - ys)
        self.zero(characteristic - expected)
        self.zero(characteristic.subs(c, 0)
                  - (U - y0)**2 * (U - y.subs({x: s, c: 0})) )
        center = kappa*(U - yc)*(U - ys)
        cofactor = kappa**2*(U - ys)
        self.zero(characteristic*cofactor - center**2)
        self.zero(cofactor.subs(U, yc) - kappa**2*(yc - ys))

        cusp_linear = []
        node_odd = []
        for power in (1, 2, 3):
            polynomial = sp.Poly((x - s)**power, x)
            cusp_linear.append(polynomial.nth(1))
            node_odd.append(sum(
                polynomial.nth(2*j + 1)*(-c)**j for j in range(2)
            ))
        self.assertEqual(cusp_linear, [1, -2*s, 3*s**2])
        self.assertEqual(node_odd, [1, -2*s, 3*s**2 - c])
        self.zero(node_odd[1].subs(s, 0))
        self.zero(node_odd[2].subs(c, 3*s**2))

        # The distinct (3,2) parametrization and its double center fiber.
        b = sp.symbols("b", nonzero=True)
        center_y, center_v = sp.symbols("center_y center_v")
        y32 = center_y + (x**2 + c)*(A2 + A3*x)
        theta32 = center_v + b*(x**2 + c)
        S0 = V - center_v
        G32 = (b*(U - center_y) - A2*S0)**2 \
            - A3**2*S0**2*(S0/b - c)
        self.zero(G32.subs({U: y32, V: theta32}, simultaneous=True))
        self.zero(G32.subs(V, center_v) - b**2*(U - center_y)**2)
        p10, p11 = sp.symbols("p10 p11")
        p1 = p10 + p11*U
        self.zero(G32.subs(V, center_v)*p1**2/b**2
                  - ((U - center_y)*p1)**2)

    def test_cubic_node_gradient_and_literal_top_cancellation(self):
        x, s, eps, U, V = sp.symbols("x s eps U V")
        A3, r1, B0 = sp.symbols("A3 r1 B0", nonzero=True)
        y0, C0, C1, L0 = sp.symbols("y0 C0 C1 L0")
        c = 3*s**2
        A2 = 3*s*A3
        y = y0 + A2*x**2 + A3*x*(x**2 + c)
        R = r1*(x**2 + c)*(x - s)
        self.zero(sp.diff(y, x).subs(x, s) - 12*s**2*A3)
        self.zero(sp.diff(R, x).subs(x, s) - 4*r1*s**2)
        # H_V=-R(C_1^2+R Lambda_rho). Its first local coefficient
        # remains visible before C_1(s)=0 is imposed by order >=3.
        local_R = sp.expand(R.subs(x, s + eps))
        local_HV = -local_R*((C0 + C1*eps)**2 + local_R*L0)
        self.zero(sp.expand(local_HV).coeff(eps, 1)
                  + 4*r1*s**2*C0**2)
        gradient_at_s = B0*sp.diff(y, x).subs(x, s) \
            + C0*sp.diff(R/2, x).subs(x, s)
        self.zero(gradient_at_s.subs(C0, 0) - 12*B0*s**2*A3)
        self.zero((x - s)**3 + (x + s)**3/2
                  - 3*R/(2*r1) - 4*s**3)
        m0 = sp.symbols("m0", nonzero=True)
        top_model = sp.Poly((V - m0*U/3)*(V - m0*U)**3, U, V)
        self.zero(top_model.coeff_monomial(U**3*V) + 2*m0**3)

        ktt, ktr, krr, ntt, ntr, nrr = sp.symbols(
            "ktt ktr krr ntt ntr nrr"
        )
        H2k = ktt*U**2/2 + ktr*U*V + krr*V**2/2
        H1kr = ktr*U + krr*V
        H2n = ntt*U**2/2 + ntr*U*V + nrr*V**2/2
        literal_top = sp.Poly(H2k**2 - 2*V*H1kr*H2k + 4*V**2*H2n,
                              U, V)
        self.zero(literal_top.coeff_monomial(U**3*V))
        kappa = sp.symbols("kappa", nonzero=True)
        self.zero(literal_top.as_expr().subs({ktt: 2*kappa, ktr: 0, krr: 0})
                  - (kappa**2*U**4 + 2*ntt*U**2*V**2
                     + 4*ntr*U*V**3 + 2*nrr*V**4))

    def test_retained_quadratic_center_and_fixed_parameter_jacobians(self):
        U, V, x, t, rho, ys = sp.symbols("U V x t rho ys")
        kappa, e, gamma, D = sp.symbols("kappa e gamma D", nonzero=True)
        alpha, beta, ell, ell_t, ell_r, m = sp.symbols(
            "alpha beta ell ell_t ell_r m"
        )
        S = kappa*U**2 + alpha*U + beta*V
        R = 2*V
        T = ell - S
        H = T**2 + R*beta*T + R**2*(-ell_t*U - ell_r*V - m)
        p = kappa*U**2 + alpha*U - ell
        self.zero(H - p**2 + V**2*(4*ell_t*U + 4*ell_r*V + beta**2 + 4*m))
        centered = sp.expand(H.subs({U: ys, ell: kappa*ys**2 + alpha*ys}))
        self.zero(centered.coeff(V, 3) + 4*ell_r)
        self.zero(centered.coeff(V, 2) + 4*ell_t*ys + beta**2 + 4*m)
        reduced = H.subs({ell: kappa*ys**2 + alpha*ys, ell_r: 0,
                         ell_t: e, m: -beta**2/4 - e*ys})
        self.zero(reduced - (U - ys)*(
            (U - ys)*(kappa*(U + ys) + alpha)**2 - 4*e*V**2
        ))

        # These are fixed-x coefficient jets, not fixed-old-v derivatives.
        y = ys + x**2/e
        ys_r, e_r, ys_t, e_t = sp.symbols("ys_r e_r ys_t e_t")
        y_r = ys_r - x**2*e_r/e**2
        theta_r = -( (2*kappa*y + alpha)*y_r - ell_r )/(2*x)
        gates = {ys_r: 0, e_r: 0, ell_r: 0}
        self.zero(y_r.subs(gates))
        self.zero(theta_r.subs(gates))
        theta = -x*(kappa*x**2/e**2 + (2*kappa*ys + alpha)/e)/2
        w = x - beta/2
        self.zero(2*theta*x + kappa*y**2 + alpha*y
                  - (kappa*ys**2 + alpha*ys))
        self.zero(x**2 - e*(y - ys))
        y_t = ys_t - x**2*e_t/e**2
        theta_t = sp.diff(theta, ys)*ys_t + sp.diff(theta, e)*e_t
        z = 2*rho*w + theta**2 + 2*kappa*t*y + alpha*t + beta*rho
        z_t = 2*theta*theta_t + 2*kappa*y + 2*kappa*t*y_t + alpha
        jacobian_r2 = sp.Matrix([
            [y_t, 0, sp.diff(y, x)],
            [z_t, sp.diff(z, rho), sp.diff(z, x)],
            [0, 0, 1],
        ]).det()
        self.zero(jacobian_r2 - 2*x*y_t)
        self.zero(sp.expand(jacobian_r2).coeff(x, 0))

        # Independent unrestricted (3,2) coefficient jets, before scalar gates.
        K, Kt, Kr, Dr = sp.symbols("K Kt Kr Dr")
        theta32 = (x**2 - K)/D
        theta_t32 = -Kt/D
        theta_r32 = -(Kr + Dr*theta32)/D
        y_t32 = -2*x*theta_t32/gamma
        y_r32 = (D - 2*x*theta_r32)/gamma
        J32 = y_t32*(2*x + 2*theta32*theta_r32) \
            - y_r32*(gamma + 2*theta32*theta_t32)
        expected = -D + 2*(3*x**2 - K)*Kt/(gamma*D) \
            - 2*x*Kr/D - 2*x*(x**2 - K)*Dr/D**2
        self.zero(J32 - expected)
        polynomial = sp.Poly(sp.cancel(J32), x)
        self.zero(polynomial.nth(3) + 2*Dr/D**2)
        self.zero(polynomial.nth(2) - 6*Kt/(gamma*D))
        self.zero(polynomial.nth(1).subs({Dr: 0, Kt: 0}) + 2*Kr/D)
        self.zero(J32.subs({Dr: 0, Kt: 0, Kr: 0}) + D)

    def test_actual_inverse_orders_and_unified_lambda_zero(self):
        U, x, t, rho, V, Z, W = sp.symbols("U x t rho V Z W")
        gamma, delta = sp.symbols("gamma delta", nonzero=True)
        kappa, n1, n2, ell0, lam = sp.symbols("kappa n1 n2 ell0 lam")
        theta0 = (x**2 - kappa)/delta
        j = theta0 + rho*U
        Vf = delta*rho - 2*x*theta0 + gamma*t*U
        Zf = gamma*t + 2*rho*x + j**2
        Wf = x + U*j
        I = W**2 + U*V - U**2*Z
        J = (I - kappa)/delta
        xh = W - U*J
        rh = (V - U*Z + 2*W*J - U*J**2)/delta
        th = (Z - 2*rh*xh - J**2)/gamma
        forward = {V: Vf, Z: Zf, W: Wf}
        self.zero(I.subs(forward, simultaneous=True) - x**2 - delta*rho*U)
        # Verify the inner J first, then the remaining literal inverse slots.
        self.zero(J.subs(forward, simultaneous=True) - j)
        self.zero(Wf - U*j - x)
        self.zero((Vf - U*Zf + 2*Wf*j - U*j**2)/delta - rho)
        self.zero((Zf - 2*rho*x - j**2)/gamma - t)
        # Reverse order uses only independent target coordinates. This bridge
        # justifies replacing the reconstructed theta+j before larger expansions.
        self.zero(delta*(J - rh*U) - xh**2 + kappa)
        self.zero((xh**2 - kappa)/delta + rh*U - J)
        self.zero(xh + U*J - W)
        self.zero(gamma*th + 2*rh*xh + J**2 - Z)
        self.zero(delta*rh - 2*xh*(J - rh*U) + gamma*th*U - V)
        self.zero(sp.Matrix([U, Vf, Zf, Wf]).jacobian([U, x, t, rho]).det()
                  + gamma*delta)

        # Both affine orders into the actual original normalized four-ring.
        Xo, Yo, Zo, Wo = sp.symbols("Xo Yo Zo Wo")
        original = [U, (V + ell0)/gamma, Z + n2, W - n1/2]
        to_normal = {U: Xo, V: gamma*Yo - ell0, Z: Zo - n2, W: Wo + n1/2}
        for expression, target in zip(original, (Xo, Yo, Zo, Wo)):
            self.zero(expression.subs(to_normal, simultaneous=True) - target)
        back = dict(zip((Xo, Yo, Zo, Wo), original))
        for expression, target in zip(to_normal.values(), (U, V, Z, W)):
            self.zero(expression.subs(back, simultaneous=True) - target)

        # Synthesis209's full symbolic family, including the lambda=0 boundary.
        K = 2*lam*delta*rho + kappa
        theta = (x**2 - K)/delta
        n = gamma*t + lam**2*rho**2 + n1*rho + n2
        ell = gamma*lam*t + delta*rho + ell0
        w = x - lam*theta - lam**2*rho - n1/2
        y = (ell - 2*theta*x + 2*lam*theta**2)/gamma
        z = 2*rho*w + theta**2 + n
        nr = sp.diff(n, rho)
        m = K - nr**2/4 - lam*ell
        self.zero(2*theta*w + gamma*y + nr*theta - ell)
        self.zero(w**2 + nr*w + lam**2*theta**2
                  - gamma*lam*y - delta*theta - m)
        self.zero(x**2 - delta*theta - K)
        self.zero(x*(x**2 - K) - delta*(ell + 2*lam*theta**2 - gamma*y)/2)
        y32 = (delta*rho + ell0 - 2*theta0*x)/gamma
        z32 = 2*rho*x + theta0**2 + gamma*t + n2
        for expression, target in ((theta, theta0), (w, x - n1/2),
                                   (y, y32), (z, z32)):
            self.zero(expression.subs(lam, 0) - target)
        self.zero(sp.expand(y).coeff(x, 4) - 2*lam/(gamma*delta**2))
        self.zero(sp.expand(y32).coeff(x, 3) + 2/(gamma*delta))
        self.zero(gamma*(y32 + t*U) - ell0 - Vf)
        self.zero(z32 + 2*rho*theta0*U + rho**2*U**2 - n2 - Zf)
        self.zero(x - n1/2 + theta0*U + rho*U**2 + n1/2 - Wf)


if __name__ == "__main__":
    unittest.main()
