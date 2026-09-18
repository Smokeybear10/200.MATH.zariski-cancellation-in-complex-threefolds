"""Exact finite controls for the held 358, 360, and 362 arguments.

Standalone source only. No earlier checker is imported. These identities do
not certify the universal field-return, selected-derivation, or proof claims.
The author has not executed, imported, or compiled this saved source.
"""

import unittest

import sympy as sp


def literal_map(X, t, s, P, y, theta, n, nt, B, ell):
    z = 2*t*y + P**2 + theta + n
    w = ell - 2*P*y - nt*P - B*theta
    return (y + P*X + t*X**2,
            z + (2*t*P + s)*X + t**2*X**2,
            w + theta*X + s*X**2)


def compose(expressions, variables, values):
    substitution = dict(zip(variables, values))
    return tuple(sp.expand(f.subs(substitution, simultaneous=True))
                 for f in expressions)


def symmetric_difference(expression, variable, total, product):
    """(f(v)-f(w))/(v-w), with total=v+w and product=v*w."""
    polynomial = sp.Poly(sp.expand(expression), variable)
    differences = [sp.S.Zero, sp.S.One]
    for degree in range(2, polynomial.degree() + 1):
        differences.append(total*differences[-1] - product*differences[-2])
    return sp.expand(sum(coefficient*differences[power[0]]
                         for power, coefficient in polynomial.terms()))


class MovingSlopeFamilyControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_equal_quadratic_quadric_and_collision_polynomial(self):
        v, w, X, R, total, product = sp.symbols('v w X R total product')
        alpha, epsilon, lam, b = sp.symbols('alpha epsilon lam b', nonzero=True)
        A, C, B, nt, T, delta, t, s, n, ell = sp.symbols(
            'A C B nt T delta t s n ell')
        p = alpha*(v**2 - delta)
        x = lam*p + epsilon*v
        q = -lam**2*p/b - 2*lam*epsilon*v/b - epsilon**2/(alpha*b)
        self.assert_zero(x**2 + b*p*q - delta*epsilon**2)
        self.assert_zero((x-lam*p)/epsilon-v)
        sigma0 = C/b-alpha*delta
        P = alpha*v**2 + sigma0
        j, k0 = lam+B, -nt/2-lam*C/b
        r, d1 = -(lam**2+A)/b, -2*lam*epsilon/b
        e1 = (lam**2-A)*C/b**2 + T/b - epsilon**2/(alpha*b)
        y, theta = j*P+epsilon*v+k0, r*P+d1*v+e1
        rows = literal_map(X, t, s, P, y, theta, n, nt, B, ell)
        # Validate the recurrence against the literal quotient and diagonal.
        for degree in range(1, 5):
            divided = symmetric_difference(v**degree, v, total, product)
            self.assert_zero(divided.subs({total:v+w, product:v*w})
                             - sp.cancel((v**degree-w**degree)/(v-w)))
        differences = [symmetric_difference(row, v, total, product)
                       for row in rows]
        for row, divided in zip(rows, differences):
            self.assert_zero(divided.subs(product, total**2/4)
                             - sp.diff(row, v).subs(v, total/2))
        chosen_total = -epsilon/(alpha*R)
        sigma_sum = d1*R/epsilon-r
        chosen_product = (chosen_total**2-(sigma_sum-2*sigma0)/alpha)/2
        values = {X:R-j, total:chosen_total, product:chosen_product}
        evaluated = [sp.cancel(d.subs(values, simultaneous=True))
                     for d in differences]
        collision = (-2*lam**2*R**2/b
                     + lam*(lam**2+A-2*C)*R/b-epsilon**2/alpha)
        self.assert_zero(evaluated[0])
        self.assert_zero(evaluated[1])
        self.assert_zero(evaluated[2]-epsilon*collision/R**2)
        self.assert_zero(sp.Poly(collision, R).LC()+2*lam**2/b)
        self.assert_zero(collision.subs(R, 0)+epsilon**2/alpha)
        wrong = collision+epsilon**2/alpha
        self.assert_zero(evaluated[2]-epsilon*wrong/R**2
                         + epsilon**3/(alpha*R**2))
        self.assertNotEqual(sp.cancel(evaluated[2]-epsilon*wrong/R**2), 0)

    def test_actual_inverse_maps_and_both_family_transports(self):
        X, Y, Z, W, tau, j, kap = sp.symbols('X Y Z W tau j kap')
        ambient = (X, Y, Z, W)
        maps = [
            ((X, Y-tau*X**2, Z-2*tau*Y+tau**2*X**2, W),
             (X, Y+tau*X**2, Z+2*tau*Y+tau**2*X**2, W)),
            ((X+j, Y+kap*(X+j)/2, Z, W+2*j*Z-kap*Y),
             (X-j, Y-kap*X/2, Z, W-2*j*Z+kap*Y-kap**2*X/2)),
            ((X+j, Y, Z, W+2*j*Z), (X-j, Y, Z, W-2*j*Z)),
        ]
        for forward, inverse in maps:
            for result in (compose(forward, ambient, inverse),
                           compose(inverse, ambient, forward)):
                for actual, expected in zip(result, ambient):
                    self.assert_zero(actual-expected)
            self.assert_zero(sp.Matrix(forward).jacobian(ambient).det()-1)
        t, s, P, Xs, b, B0, f1, f0, k0, e0, ell = sp.symbols(
            't s P Xs b B0 f1 f0 k0 e0 ell')
        gamma, rho, r = sp.symbols('gamma rho r')
        for reciprocal in (False, True):
            if reciprocal:
                B = B0+gamma/t
                f = (-j**2+2*B0*j)*t**2-gamma*rho/t+f1*t+f0
                theta = (r-4*j*t)*P+e0
                s_value = r*t-2*j*t**2+rho
                shift = sp.S.Zero
            else:
                B = b*t+B0
                f = 2*b*j*t**3+(2*B0*j-j**2-b*kap)*t**2+f1*t+f0
                theta = (kap-4*j*t)*P+e0
                s_value = s
                shift = kap
            n = B*s+f
            # Differentiate before substituting the transported s expression.
            nt = sp.diff(n, t)
            rows = literal_map(X, t, s, P, j*P+k0, theta, n, nt, B, ell)
            oldY, oldZ, oldW = [row.subs(s, s_value) for row in rows]
            newY = oldY.subs(X, Xs-j)+shift*Xs/2
            newZ = oldZ.subs(X, Xs-j)
            newW = (oldW+2*j*oldZ-shift*oldY).subs(X, Xs-j)
            ys = k0+j**2*t
            Ps = P-2*j*t+shift/2
            ss = s_value+2*j*t**2-shift*t
            thetas = theta+(4*j*t-shift)*P-4*j**2*t**2+2*shift*j*t
            Bs = B-j
            if reciprocal:
                ns = Bs*ss-gamma*rho/t+(f1-2*j*gamma)*t+f0
                nts = -gamma*(ss-rho)/t**2+f1-2*j*gamma
                self.assert_zero(sp.diff(thetas, P)-r)
            else:
                ns = Bs*ss+(f1+kap*(B0-j))*t+f0-kap**2/4
                nts = b*ss+f1+kap*(B0-j)
                self.assert_zero(sp.diff(thetas, P))
            zs, ws = newZ.subs(Xs, 0), newW.subs(Xs, 0)
            self.assert_zero(newY-ys-Ps*Xs-t*Xs**2)
            self.assert_zero(newZ-zs-(2*t*Ps+ss)*Xs-t**2*Xs**2)
            self.assert_zero(newW-ws-thetas*Xs-ss*Xs**2)
            self.assert_zero(zs-2*t*ys-Ps**2-thetas-ns)
            ells = ws+2*Ps*ys+nts*Ps+Bs*thetas
            self.assert_zero(sp.diff(ells, P))
        # The actual tau-map keeps the first potential with t replaced by t-tau.
        yy, th, nn = sp.symbols('yy th nn')
        zz = 2*t*yy+P**2+th+nn
        self.assert_zero(zz-2*tau*yy-(2*(t-tau)*yy+P**2+th+nn))

    def test_affine_scalar_and_corrected_fourth_coefficient(self):
        t, s, P, U, V, X = sp.symbols('t s P U V X')
        b = sp.Symbol('b', nonzero=True)
        beta, f1, f0 = sp.symbols('beta f1 f0')
        B = b*t+beta
        n = B*s+f1*t+f0
        nt = sp.diff(n, t)
        ell, level = sp.Function('ell')(t, s), sp.Function('level')(t, s)
        formal_w = ell-2*P*U-nt*P-B*V
        H = U**2+nt*U+B*formal_w+b*P*V-sp.diff(ell,t)*P-sp.diff(ell,s)*V
        HP, HV = sp.diff(H, P), sp.diff(H, V)
        # Corrected 296 formal Q_P, not a derivative after evaluating U or V.
        QP = sp.diff(H,t)-sp.diff(level,t)-(2*U+nt)*HV+B*HP
        q2 = sp.expand(QP).coeff(P, 1)/2
        self.assert_zero(q2-(-2*b*U-sp.diff(ell,t,2)/2-b*nt))
        wrong_q2 = -2*b*U-sp.diff(ell,t,2)/2
        self.assert_zero(q2-wrong_q2+b*nt)
        self.assertNotEqual(sp.expand(q2-wrong_q2), 0)
        y, theta, w0 = [sp.Function(name)(t,s) for name in ('y','theta','w0')]
        h = 2*y+nt
        z, w = P**2+2*t*y+theta+n, w0-h*P
        J0 = sp.expand(sp.Matrix([y,z,w]).jacobian([t,s,P]).det())
        self.assert_zero(J0.coeff(P,2)-2*b*sp.diff(y,t))
        self.assert_zero(HP.subs({U:y,V:theta})-(b*theta-B*h-sp.diff(ell,t)))
        conditions = {sp.diff(y,t):0, sp.diff(theta,t):-h, sp.diff(w0,t):0}
        self.assert_zero(J0.subs(conditions, simultaneous=True))
        for intercept in (y,z,w):
            self.assert_zero(sp.diff(intercept,t).subs(conditions, simultaneous=True))
        # Differentiate the third-level gate with h_t=0 and compare Q's gate.
        derivative_gate = b*sp.diff(theta,t)-b*h
        self.assert_zero((derivative_gate+2*b*h).subs(sp.diff(theta,t),-h))

    def test_reciprocal_full_scalar_both_cases_and_missing_term(self):
        t, r, P, X = sp.symbols('t r P X')
        beta, gamma, rho, f1, f0 = sp.symbols('beta gamma rho f1 f0')
        y, e, w0 = [sp.Function(name)(t,r) for name in ('y','e','w0')]
        h = 2*y+beta*r+f1
        z = P**2+r*P+t*h+e+gamma*r+beta*rho+f0
        w = w0-h*P
        rows = (y+P*X+t*X**2,
                z+(2*t*P+r*t+rho)*X+t**2*X**2,
                w+(r*P+e)*X+(r*t+rho)*X**2)
        J = sp.Poly(sp.expand(sp.Matrix(rows).jacobian([t,r,P]).det()), X,P)
        yt, yr, et, wt, wr = sp.diff(y,t), sp.diff(y,r), sp.diff(e,t), sp.diff(w0,t), sp.diff(w0,r)
        targets = {(2,0):-(beta*t+gamma)*(h+et)-t*wt,
                   (1,1):-beta*(h+et)+2*(beta*t+gamma)*yt-wt,
                   (0,2):2*beta*yt,
                   (0,1):-(h-beta*r)*yt-2*wr*yt+2*wt*yr}
        for powers, expected in targets.items():
            self.assert_zero(J.coeff_monomial(X**powers[0]*P**powers[1])-expected)
        wrong_P = -h*yt-2*wr*yt+2*wt*yr
        self.assert_zero(J.coeff_monomial(P)-wrong_P-beta*r*yt)
        self.assertNotEqual(sp.expand(J.coeff_monomial(P)-wrong_P), 0)
        # Nonzero beta: the first two gates reduce to -gamma*(h+e_t).
        self.assert_zero((targets[(2,0)]-t*targets[(1,1)]).subs(yt,0)
                         + gamma*(h+et))
        final = {yt:0, et:-h, wt:0}
        self.assert_zero(J.as_expr().subs(final, simultaneous=True))
        # Zero beta: D=w0-2*gamma*y has D_t=0; retain its r derivative.
        Dr = sp.Symbol('Dr')
        reduced_P = targets[(0,1)].subs(beta,0).subs(
            {wt:2*gamma*yt, wr:Dr+2*gamma*yr}, simultaneous=True)
        self.assert_zero(reduced_P+yt*(2*y+f1+2*Dr))
        self.assert_zero((wt-2*gamma*yt).subs(wt,2*gamma*yt))
        # Calibration change s=r*t+rho has exact determinant t, not one.
        self.assert_zero(sp.Matrix([t,r*t+rho]).jacobian([t,r]).det()-t)
        self.assert_zero(J.as_expr().subs(beta,0).subs(
            {yt:0, et:-(2*y+f1), wt:0}, simultaneous=True))


if __name__ == '__main__':
    unittest.main()
