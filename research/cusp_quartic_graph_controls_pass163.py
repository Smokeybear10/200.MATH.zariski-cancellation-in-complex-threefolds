"""Independent exact controls for the two distinct quartic graph examples163.

Formal coefficient identities and the index-two projected field example are
not asserted to be actual cusp frames. The separate polynomial fixture has
staged two-sided inverses, a computed selected partial, and an invariant
coordinate. Finite arithmetic does not prove the universal coefficient-field
arguments, invariant lifting, or cancellation. No older checker is imported.
"""

import math
import unittest

import sympy as sp


def gamma(x, y, t):
    return (
        4*t*y**3 + 3*t**2*y + (6*t**2*y**2+t**3)*x
        + 4*t**3*y*x**2 + t**4*x**3
    )


def actual_frame(x, y, t, q):
    return (
        x,
        y+t*x,
        t-y**4+(3*t**2*y+q)*x+t**3*x**2,
        -q-y**5-4*t*y**3-(3*t**2-t)*y
        +(q*y-t*y**4-3*t**2*y**2-t**3+t**2)*x+t*q*x**2,
    )


class CuspQuarticGraphControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_literal_potentials_S_and_coefficient_jets(self):
        U, V, X = sp.symbols("U V X")
        tau = sp.Symbol("tau", nonzero=True)
        rho = sp.Symbol("rho")
        r, k, n, ell = 1/tau, rho/tau, tau**2, -rho/tau**2
        lam = tau**-2

        def H(coefficient, degree):
            return sum(
                sp.diff(coefficient, tau, i, rho, degree-i)
                * U**i * V**(degree-i)
                / (math.factorial(i)*math.factorial(degree-i))
                for i in range(degree+1)
            )

        f = sp.expand(U**3+H(k, 2)+H(n, 1))
        phi = sp.expand(
            sp.diff(f, V)*(ell-f)/r + H(k, 3)+H(n, 2)
            -sp.diff(ell, tau)*U-sp.diff(ell, rho)*V
        )
        expected_phi = V/tau**2+U**4/tau+3*U**2-rho*U/tau**3
        self.zero(tau**4*(phi-expected_phi))
        self.zero(sp.diff(r, tau, 2)/2-sp.diff(r, tau)**2/r)
        self.zero(sp.diff(n, rho, 2))
        self.zero(lam-r**2)
        base_P = -tau*U**4-3*tau**2*U**2+rho*U/tau

        # Same literal coefficient data, different graph/evaluation constant.
        # Only the second row is later supplied an actual polynomial inverse.
        for shift, m, expected_S, expected_z in (
            (sp.S.Zero, sp.S.Zero, 2*tau**2, tau**2-U**4),
            (-tau**3+tau**2, 1-tau, tau, tau-U**4),
        ):
            with self.subTest(shift=shift):
                P = base_P+shift
                self.assertEqual(sp.degree(P, U), 4)
                self.zero(tau**4*(phi-lam*(V-P)-m))
                S = sp.expand(
                    sp.diff(P, tau)+sp.diff(P, U)*sp.diff(P, rho)
                    +(sp.diff(P, U)*(sp.diff(r, tau)*U+sp.diff(n, rho))
                      +3*U**2+sp.diff(k, tau, 2)*U
                      +sp.diff(r, tau)*P+sp.diff(n, tau))/r
                )
                self.zero(tau**3*(S-expected_S))
                z = sp.expand(
                    3*tau*U**2+sp.diff(k, tau)*U+r*P+n
                )
                w = sp.expand((ell-f.subs(V, P))/r)
                self.zero(z-expected_z)
                self.zero(tau**3*(r*w+f.subs(V, P)-ell))
                sigma = 3*tau**2*U+k
                chart = (U+tau*X, z+sigma*X+tau**3*X**2,
                         w+P*X+rho*X**2)
                matrix = sp.Matrix(chart).jacobian((tau, rho, U))
                # Known powers of tau clear denominators before expansion.
                cleared = sp.Matrix([
                    [sp.expand(entry) for entry in matrix.row(0)],
                    [sp.expand(tau**2*entry) for entry in matrix.row(1)],
                    [sp.expand(tau**2*entry) for entry in matrix.row(2)],
                ])
                self.zero(cleared.det()+tau**4*lam*expected_S)
                if shift != 0:
                    # y=tau*v: relative J in (tau,rho,v) is -1.
                    self.zero(tau*(-lam*expected_S)+1)

        # Independent polynomial jets detect the unique U^7 contribution.
        p = sp.symbols("p0:5")
        pt = sp.symbols("pt0:5")
        pr = sp.symbols("pr0:5")
        alpha, nr, inv_r, ktt, nt = sp.symbols("alpha nr inv_r ktt nt")
        polynomial = sum(p[i]*U**i for i in range(5))
        generic_S = sp.expand(
            sum(pt[i]*U**i for i in range(5))
            +sp.diff(polynomial, U)*sum(pr[i]*U**i for i in range(5))
            +sp.diff(polynomial, U)*(alpha*U+nr*inv_r)
            +(3*U**2+ktt*U+nt)*inv_r+alpha*polynomial
        )
        self.zero(generic_S.coeff(U, 7)-4*p[4]*pr[4])
        reduced = sp.expand(generic_S.subs({pr[4]: 0, pr[3]: 0, pr[2]: 0}))
        self.zero(reduced.coeff(U, 4)-pt[4]-4*p[4]*pr[1]-5*alpha*p[4])
        self.zero(reduced.coeff(U, 4).subs(pt[4], p[4]*pr[1])
                  -5*p[4]*(pr[1]+alpha))

    def test_old_index_two_projected_field_arithmetic(self):
        tau = sp.Symbol("tau", nonzero=True)
        rho, v = sp.symbols("rho v")
        y = v
        z = tau**2-v**4
        w = -v**5-4*tau*v**3-2*tau**2*v-rho/tau
        self.zero(z+y**4-tau**2)
        self.zero(-tau*(w+y**5+4*tau*y**3+2*tau**2*y)-rho)
        self.zero(sp.Matrix([y, z, w]).jacobian((tau, rho, v)).det()+2)

        # A nontrivial algebraic branch change fixes every projected output.
        # This is rational field arithmetic, not a polynomial inverse frame.
        deck = {tau: -tau, rho: -rho-8*tau**2*v**3, v: v}
        for expression in (y, z, w):
            self.zero(tau*(expression.xreplace(deck)-expression))
        for coordinate in (tau, rho, v):
            self.zero(coordinate.xreplace(deck).xreplace(deck)-coordinate)
        self.assertNotEqual(deck[tau], tau)
        Y, Z, W, T = sp.symbols("Y Z W T")
        branch_polynomial = T**2-Z-Y**4
        self.assertEqual(sp.degree(branch_polynomial, T), 2)
        self.assertEqual(sp.degree(Z+Y**4, Z), 1)
        self.zero(branch_polynomial.xreplace({T: tau, Y: y, Z: z}))
        # Irreducibility over the projected rational field is the note's
        # prime-valuation argument. These finite identities do not replace it.

    def test_actual_staged_inverse_selected_partial_and_initials(self):
        x, y, t, q = sp.symbols("x y t q")
        X, Y, Z, W, T0, Q0 = sp.symbols("X Y Z W T0 Q0")
        source = (x, y, t, q)
        forward = actual_frame(*source)
        xf, yf, zf, wf = forward
        T_source = sp.expand((1-xf*yf)*zf+xf*wf)
        Q_source = sp.expand(yf*zf-wf)
        self.zero(T_source-t+yf**4)
        self.zero(Q_source-q-gamma(x, y, t))

        recovered_t = sp.expand(T_source+yf**4)
        self.zero(recovered_t-t)
        recovered_y = sp.expand(yf-xf*recovered_t)
        self.zero(recovered_y-y)
        recovered_q = sp.expand(Q_source-gamma(xf, recovered_y, recovered_t))
        self.zero(recovered_q-q)
        self.zero(xf-x)

        # Reverse the two exact polynomial stages, not a nested substitution
        # into the fully composed inverse. This includes X=0 and t=0.
        Z_back = T0+X*Q0
        W_back = Y*T0+(X*Y-1)*Q0
        self.zero((1-X*Y)*Z_back+X*W_back-T0)
        self.zero(Y*Z_back-W_back-Q0)
        T_target = (1-X*Y)*Z+X*W
        Q_target = Y*Z-W
        self.zero(Z_back.xreplace({T0: T_target, Q0: Q_target})-Z)
        self.zero(W_back.xreplace({T0: T_target, Q0: Q_target})-W)
        t_star = T0+Y**4
        y_star = Y-X*t_star
        q_star = Q0-gamma(X, y_star, t_star)
        returned_Y = sp.expand(y_star+t_star*X)
        returned_T0 = sp.expand(t_star-returned_Y**4)
        returned_Q0 = sp.expand(q_star+gamma(X, y_star, t_star))
        self.zero(returned_Y-Y)
        self.zero(returned_T0-T0)
        self.zero(returned_Q0-Q0)
        self.zero(returned_T0+X*returned_Q0-Z_back)
        self.zero(returned_Y*returned_T0+(X*returned_Y-1)*returned_Q0-W_back)

        # Differentiate the inverse stages, retaining the moving t and y.
        Tt = sp.expand(sp.diff(T_target+Y**4, Z).xreplace(
            dict(zip((X, Y, Z, W), forward))
        ))
        Ty = sp.expand(-x*Tt)
        gamma_difference = sp.expand(sp.diff(gamma(x, y, t), t)
                                     -x*sp.diff(gamma(x, y, t), y))
        self.zero(gamma_difference-4*y**3-6*t*y)
        Tq = sp.expand(yf-gamma_difference*Tt)
        partial = (sp.S.Zero, Ty, Tt, Tq)
        expected = (0, -x+x**2*y+t*x**3, 1-x*y-t*x**2,
                    y+t*x-(4*y**3+6*t*y)*(1-x*y-t*x**2))
        for got, want in zip(partial, expected):
            self.zero(got-want)
        for i, coordinate in enumerate(forward):
            self.zero(sum(c*sp.diff(coordinate, a)
                          for c, a in zip(partial, source))-int(i == 2))
        self.assertEqual(tuple(sp.degree(a, x) for a in forward), (1, 1, 2, 2))
        for coordinate, leading in zip(forward, (1, t, t**3, t*q)):
            self.zero(sp.Poly(coordinate, x).LC()-leading)
        self.assertEqual(tuple(sp.expand(a).coeff(x, 3) for a in partial), (0, t, 0, 0))
        self.zero(t*sp.diff(y/t, y)-1)
        self.zero(sp.Matrix(forward[1:]).jacobian((y, t, q)).det()+1)

        eta = sp.Symbol("eta")
        initials = (eta, t*eta, t**3*eta**2, t*q*eta**2)
        self.zero(initials[0]*initials[2]-initials[1]**3)
        self.zero(initials[1]-t*initials[0])
        self.zero(initials[3]-q*initials[0]*initials[1])
        minor = sp.Matrix([initials[i] for i in (0, 1, 3)]).jacobian((eta, t, q)).det()
        self.zero(minor-t*eta**3)
        self.assertNotEqual(minor, 0)
        # Nonzero minor gives the image rank three in this explicit family.
        # Together with the primitive linear-Z cusp relation, the written
        # height-one prime argument identifies its full initial kernel.
        self.assertEqual(sp.gcd(X, Y**3), 1)

    def test_actual_invariant_coordinate_and_projected_ring_inverse(self):
        X, Y, Z, W, I, Q0 = sp.symbols("X Y Z W I Q0")
        invariant = Y**4+(1-X*Y)*Z+X*W
        companion = Y*Z-W
        inverse_Z = I-Y**4+X*Q0
        inverse_W = Y*(I-Y**4)+(X*Y-1)*Q0
        substitution = {Z: inverse_Z, W: inverse_W}
        self.zero(invariant.xreplace(substitution)-I)
        self.zero(companion.xreplace(substitution)-Q0)
        self.zero(inverse_Z.xreplace({I: invariant, Q0: companion})-Z)
        self.zero(inverse_W.xreplace({I: invariant, Q0: companion})-W)
        x, y, t, q = sp.symbols("x y t q")
        forward = actual_frame(x, y, t, q)
        actual_I = sp.expand(invariant.xreplace(dict(zip((X, Y, Z, W), forward))))
        self.zero(actual_I-t)
        self.zero(sp.diff(actual_I, x))
        weights = (1, 1, 2, 2)
        terms = sp.Poly(invariant, X, Y, Z, W).terms()
        degree = max(sum(a*b for a, b in zip(e, weights)) for e, c in terms)
        self.assertEqual(degree, 4)
        top = sum(c*sp.prod(a**b for a, b in zip((X, Y, Z, W), e))
                  for e, c in terms if sum(a*b for a, b in zip(e, weights)) == 4)
        self.zero(top+Y*(X*Z-Y**3))
        self.assertNotEqual(sp.expand(top), 0)

        z0 = t-y**4
        w0 = -q-y**5-4*t*y**3-(3*t**2-t)*y
        t_back = sp.expand(z0+y**4)
        q_back = sp.expand(-w0-y**5-4*t_back*y**3-(3*t_back**2-t_back)*y)
        self.zero(t_back-t)
        self.zero(q_back-q)
        A, B, C = sp.symbols("A B C")
        t_target = B+A**4
        q_target = -C-A**5-4*t_target*A**3-(3*t_target**2-t_target)*A
        self.zero(t_target-A**4-B)
        self.zero(-q_target-A**5-4*t_target*A**3-(3*t_target**2-t_target)*A-C)
        # No denominator in this actual three-ring inverse. Its contrast
        # with the old index-two example is a field-return distinction.


if __name__ == "__main__":
    unittest.main()
