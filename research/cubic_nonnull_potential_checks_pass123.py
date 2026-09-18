"""Finite exact identities for the conditional nonnull potential results123.

These checks do not prove valuation assertions for all primes, original
coordinate generation, full invariant kernels, or cancellation.
"""

import unittest

import sympy as sp


class NonnullPotentialChecks(unittest.TestCase):
    def test_scalar_normalization_and_original_quadratic_identity(self):
        h, Y, g = sp.symbols("h Y g")
        q, lam, C0, u, v, R = sp.symbols("q lam C0 u v R")
        D, A, C = (sp.Function(n)(h) for n in ("D", "A", "C"))
        norm = g**2-1-D*Y**2

        def zero(value):
            numerator = sp.fraction(sp.cancel(value))[0]
            self.assertEqual(sp.simplify(sp.rem(numerator, norm, g)), 0)

        def dh(value):
            return sp.diff(value, h)+sp.diff(value, g)*sp.diff(D, h)*Y**2/(2*g)

        def dy(value):
            return sp.diff(value, Y)+sp.diff(value, g)*D*Y/g

        w, wi = sp.I*(g+sp.sqrt(D)*Y), -sp.I*(g-sp.sqrt(D)*Y)
        zero(w*wi-1)
        zero(w+wi-2*sp.I*sp.sqrt(D)*Y)
        zero(w-wi-2*sp.I*g)
        zero(4*lam*sp.sqrt(D)*(w-wi)/(4*(w+wi))-lam*g/Y)
        psi0 = lam*g/Y+C
        zero(dh(psi0)-lam*sp.diff(D, h)*Y/(2*g)-sp.diff(C, h))
        zero(dy(psi0)+lam/(g*Y**2))

        Q = sp.Matrix([[-1, 0, 0],
            [0, sp.diff(D, h, 2)/2, (sp.diff(D, h)-h*sp.diff(D, h, 2))/2],
            [0, (sp.diff(D, h)-h*sp.diff(D, h, 2))/2,
             D-h*sp.diff(D, h)+h**2*sp.diff(D, h, 2)/2]])
        b = sp.Matrix([g, h*Y, Y])
        bh, by = b.applyfunc(dh), b.applyfunc(dy)
        rho = C0*g+A*Y
        x = b*(u+rho)+bh*v+by*R
        tangent = bh*v+by*R
        radial_quadratic = (tangent.T*Q*tangent)[0]
        z = q*u**2/2+psi0-q*rho**2/2-q*(dh(rho)*v+dy(rho)*R+radial_quadratic/2)
        zero((b.T*Q*b)[0]+1)
        zero((b.T*Q*bh)[0])
        zero((b.T*Q*by)[0])
        zero(z+q*(x.T*Q*x)[0]/2+q*C0*x[0]-psi0
             +q*sp.diff(A, h)*x[1]+q*(A-h*sp.diff(A, h))*x[2])

    def test_lower_volume_scalar_conversion(self):
        D, D1, D2, D3, delta = sp.symbols("D D1 D2 D3 delta", nonzero=True)
        A, A1, A2, A3, C1, C2 = sp.symbols("A A1 A2 A3 C1 C2")
        q, lam = sp.symbols("q lam", nonzero=True)
        derivative_rules = {D: D1, D1: D2, D2: D3,
                            delta: -D*D3/2, A: A1, A1: A2, A2: A3, C1: C2}

        def dh(value):
            return sum(sp.diff(value, variable)*speed
                       for variable, speed in derivative_rules.items())

        def zero(value):
            reduced = sp.simplify(value).subs(delta, (D1**2-2*D*D2)/4)
            self.assertEqual(sp.simplify(reduced), 0)

        d, kappa = sp.sqrt(D), sp.sqrt(delta)/(2*D)
        partial = lambda value: dh(value)/kappa
        e0 = D*D3/(4*delta)
        e = e0/kappa
        ell = 4*lam*d
        alpha = -partial(ell)/(4*ell)
        beta = -C1/(4*lam*d*kappa)
        ahat = A/(2*sp.I*d)
        j = -q*(4*ahat-partial(partial(ahat))+e*partial(ahat))/(2*ell)
        j_formula = -sp.I*q*D*A2/(4*lam*delta)
        zero(j-j_formula)
        k = -q*e/(3*ell)
        n = (partial(j_formula)+8*alpha*j_formula-2*e*j_formula)/(6*k)
        n_formula = 2*sp.I*d*A3/D3
        zero(n-n_formula)
        residual = partial(beta)+4*alpha*beta-e*beta-4*j_formula*n_formula
        zero(residual+(C2+2*q*A2*A3/D3)/(4*lam*d*kappa**2))
        zero(dh(C1+q*A2**2/D3)-(C2+2*q*A2*A3/D3))

    def test_cubic_matrix_and_polynomial_dual_row(self):
        h, Y, g, P = sp.symbols("h Y g P")
        a3, a2, a1, a0 = sp.symbols("a3 a2 a1 a0")
        D = a3*h**3+a2*h**2+a1*h+a0
        Q = sp.Matrix([[-1, 0, 0],
                       [0, 3*a3*h+a2, (-3*a3*h**2+a1)/2],
                       [0, (-3*a3*h**2+a1)/2, a3*h**3+a0]])
        canonical = sp.Matrix([[-1, 0, 0],
            [0, sp.diff(D, h, 2)/2, (sp.diff(D, h)-h*sp.diff(D, h, 2))/2],
            [0, (sp.diff(D, h)-h*sp.diff(D, h, 2))/2,
             D-h*sp.diff(D, h)+h**2*sp.diff(D, h, 2)/2]])
        self.assertEqual(sp.simplify(Q-canonical), sp.zeros(3))
        I, J = P**2/Y, P**3/Y**2
        dual = sp.Matrix([[g, -(3*a3*I+2*a2*P+a1*Y)/2,
                           (a3*J-a1*P-2*a0*Y)/2]])
        speed = sp.Matrix([g, P, Y])
        self.assertEqual(sp.simplify(dual+speed.T*Q.subs(h, P/Y)), sp.zeros(1, 3))
        norm_error = g**2-1-D.subs(h, P/Y)*Y**2
        self.assertEqual(sp.cancel((dual*speed)[0]-1-norm_error), 0)
        self.assertEqual(sp.cancel((g**2-1)/Y-a3*J-a2*I-a1*P-a0*Y-norm_error/Y), 0)
        self.assertEqual(sp.simplify(Y*Q.subs(h, P/Y)-sp.Matrix([
            [-Y, 0, 0], [0, 3*a3*P+a2*Y, (-3*a3*I+a1*Y)/2],
            [0, (-3*a3*I+a1*Y)/2, a3*J+a0*Y]])), sp.zeros(3))

    def test_cubic_surface_jacobian_with_full_residual(self):
        g, P, Y = sp.symbols("g P Y")
        gs, Ps, Ys, gt, Pt, Yt = sp.symbols("gs Ps Ys gt Pt Yt")
        a3, a2, a1, a0 = sp.symbols("a3 a2 a1 a0")
        F = Y*(g**2-1)-a3*P**3-a2*P**2*Y-a1*P*Y**2-a0*Y**3
        gradient = sp.Matrix([sp.diff(F, variable) for variable in (g, P, Y)])
        b, bs, bt = sp.Matrix([g, P, Y]), sp.Matrix([gs, Ps, Ys]), sp.Matrix([gt, Pt, Yt])
        omega = sp.Matrix.hstack(b, bs, bt).det()
        jac = Ps*Yt-Pt*Ys
        Fs, Ft = (gradient.dot(vector) for vector in (bs, bt))
        self.assertEqual(sp.expand(gradient.dot(b)-3*F-2*Y), 0)
        self.assertEqual(sp.expand(2*g*Y*omega-2*Y*jac-3*F*jac
                                  -Fs*(Pt*Y-Yt*P)-Ft*(P*Ys-Y*Ps)), 0)
        # This is a chain-rule residual, not a substitute for F=Fs=Ft=0.
        self.assertEqual(sp.expand(sp.diff(F, P)*jac+sp.diff(F, g)*(gs*Yt-gt*Ys)
                                  -Fs*Yt+Ft*Ys), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
