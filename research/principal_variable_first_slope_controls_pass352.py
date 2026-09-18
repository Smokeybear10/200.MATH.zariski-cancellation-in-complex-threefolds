"""Standalone exact finite controls for the held 349, 350, and 351 notes.

This suite rebuilds the raw potentials and differential rows. It does not
certify actual chart entry, exact constant fields, universal ring normality,
geometric degree theorems, ambient recognition, or cancellation. Formal
families are deliberately distinguished from fully calibrated actual maps.
No retained proof source or checker is imported or executed.
"""

import unittest

import sympy as sp


def polynomial_integral(expression, variable):
    """Exact zero-constant integral, treating other symbols as coefficients."""
    return sp.Add(*(
        coefficient * variable ** (power[0] + 1) / (power[0] + 1)
        for power, coefficient in sp.Poly(sp.expand(expression), variable).terms()
    ))


def raw_data():
    """Build literal264 H and corrected296 gradients with arbitrary functions."""
    t, s, U, P, V = sp.symbols("t s U P V")
    B = sp.Function("B")(t)
    f = sp.Function("f")(t)
    ell = sp.Function("ell")(t, s)
    level = sp.Function("h")(t, s)
    n = B * s + f
    u = sp.diff(n, t)
    b = sp.diff(B, t)
    w = ell - 2 * P * U - u * P - B * V
    H = (U**2 + u * U + B * w + sp.diff(n, t, 2) * P**2 / 2
         + b * P * V - sp.diff(ell, t) * P - sp.diff(ell, s) * V)
    HU, HP, HV = (sp.diff(H, z) for z in (U, P, V))
    gradients = (
        HP - 2 * P * HV + B * HU,
        sp.diff(H, t) - sp.diff(level, t) - (2 * U + u) * HV + B * HP,
        sp.diff(H, s) - sp.diff(level, s),
    )
    QU, QP, QV = gradients
    Q = (polynomial_integral(QU, U)
         + polynomial_integral(QP.subs(U, 0), P)
         + polynomial_integral(QV.subs({U: 0, P: 0}), V))
    return locals()


def homogeneous_part(expression, variables, degree):
    return sp.Add(*(
        coefficient * sp.prod(z**power for z, power in zip(variables, monomial))
        for monomial, coefficient in sp.Poly(sp.expand(expression), *variables).terms()
        if sum(monomial) == degree
    ))


class VariableFirstSlopeControls(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_raw_corrected_gradients_and_mixed_term_negative(self):
        d = raw_data()
        t, s, U, P, V = (d[k] for k in ("t", "s", "U", "P", "V"))
        B, b, n, u, ell, h = (d[k] for k in ("B", "b", "n", "u", "ell", "level"))
        expected = (
            -2*b*P**2 + (sp.diff(n, t, 2) + 2*sp.diff(ell, s))*P
            + b*V - sp.diff(ell, t),
            (sp.diff(n, t, 2) - 4*b*P + 2*sp.diff(ell, s))*U
            + sp.diff(n, t, 3)*P**2/2 + sp.diff(b, t)*P*V
            - (sp.diff(ell, t, 2) + 2*b*u)*P
            - (sp.diff(ell, t, s) + B*b)*V
            + b*ell + u*sp.diff(ell, s) - sp.diff(h, t),
            b*U + sp.diff(b, t)*P**2/2
            - (sp.diff(ell, t, s) + B*b)*P - sp.diff(ell, s, 2)*V
            + B*sp.diff(ell, s) - sp.diff(h, s),
        )
        for variable, raw_gradient, target in zip((U, P, V), d["gradients"], expected):
            self.assertZero(raw_gradient - target)
            self.assertZero(sp.diff(d["Q"], variable) - raw_gradient)
        self.assertZero(d["Q"].subs({U: 0, P: 0, V: 0}))
        self.assertEqual(sp.Poly(d["Q"], U, P, V).total_degree(), 3)
        self.assertZero(sp.Poly(d["Q"], U, P, V).coeff_monomial(U*P**2) + 2*b)
        self.assertZero(sp.diff(d["Q"], U, 2))

        # Suppressing H2(n)'s mixed term destroys the corrected gradient.
        wrong_H = d["H"] - b*P*V
        wrong_QU = sp.diff(wrong_H, P) - 2*P*sp.diff(wrong_H, V) + B*sp.diff(wrong_H, U)
        error = sp.expand(wrong_QU - d["gradients"][0])
        self.assertZero(error - (2*b*P**2 - b*V))
        self.assertNotEqual(error, 0)

    def test_centering_resultant_top_and_cofactor_identities(self):
        d = raw_data()
        t, s, U, P, V = (d[k] for k in ("t", "s", "U", "P", "V"))
        B, b, n, u, ell, h = (d[k] for k in ("B", "b", "n", "u", "ell", "level"))
        x, q0 = sp.symbols("x q0")
        A = sp.diff(n, t, 2)/2 - B**2
        C = sp.diff(ell, s) + B**2
        T = sp.diff(ell, t)
        hb = h - B*ell + u**2/4
        qb = q0 - u*T/2
        J = A*P**2 - T*P + (b*P-C)*V - hb
        D = -2*b*P**2 + 2*(A+C)*P + b*V - T
        E = ((sp.diff(n, t, 3)/6 - 2*B*b)*P**3 + sp.diff(b, t)*P**2*V/2
             + (2*B*(A+C) - sp.diff(ell, t, 2)/2)*P**2
             - sp.diff(ell, t, s)*P*V - sp.diff(ell, s, 2)*V**2/2
             + (-sp.diff(hb, t)-2*B*T)*P - sp.diff(hb, s)*V - qb)
        self.assertZero((d["H"]-h).subs(U, x-u/2+B*P) - (x**2+J))
        self.assertZero((d["Q"]-q0).subs(U, x-u/2+B*P) - (D*x+E))
        # Omitting the level correction in qbar is generically wrong.
        wrong_E = E - u*T/2
        self.assertNotEqual(sp.expand(D*x + wrong_E - (d["Q"]-q0).subs(U, x-u/2+B*P)), 0)

        jj, dd, ee = sp.symbols("jj dd ee")
        self.assertZero(sp.resultant(x**2+jj, dd*x+ee, x) - (ee**2+dd**2*jj))
        resultant = sp.expand(E**2 + D**2*J)
        a3 = sp.diff(n, t, 3)/6 - 2*B*b
        b3 = sp.diff(b, t)/2
        top = homogeneous_part(resultant, (P, V), 6)
        self.assertZero(top - P**4*((a3*P+b3*V)**2 + 4*b**2*(A*P**2+b*P*V)))
        self.assertZero(sp.Poly(top, P, V).coeff_monomial(P**4*V**2) - b3**2)
        self.assertZero(sp.Poly(top, P, V).coeff_monomial(P**5*V).subs(sp.diff(b, t), 0) - 4*b**3)
        self.assertEqual(sp.Poly(resultant, P, V).total_degree(), 6)
        solved_V = 2*P**2 - 2*(A+C)*P/b + T/b
        cubic = sp.expand(-J.subs(V, solved_V))
        self.assertEqual(sp.Poly(cubic, P).degree(), 3)
        self.assertZero(sp.Poly(cubic, P).coeff_monomial(P**3) + 2*b)

        # Formal derivative of the resultant, reduced by both evaluated levels.
        jp, dp, ep = sp.symbols("jp dp ep")
        resultant_derivative = 2*ee*ep + 2*dd*dp*jj + dd**2*jp
        minor = 2*x*(dp*x+ep) - jp*dd
        reduced = resultant_derivative.subs({ee: -dd*x, jj: -x**2}, simultaneous=True)
        self.assertZero(reduced + dd*minor)
        self.assertNotEqual(sp.expand(reduced - dd*minor), 0)

    def test_both_constant_sigma_obstructions_from_raw_rows(self):
        d = raw_data()
        t, s, U, P, V = (d[k] for k in ("t", "s", "U", "P", "V"))
        B, b, n, ell, h = (d[k] for k in ("B", "b", "n", "ell", "level"))
        x, p0, sig0, a2, d0 = sp.symbols("x p0 sig0 a2 d0")
        substitution = {U: x-p0, P: sig0, V: a2*x**2+d0}
        normal_derivative = sp.expand(
            d["gradients"][0].subs(substitution, simultaneous=True)
            + 2*a2*x*d["gradients"][2].subs(substitution, simultaneous=True))
        u0 = -2*b*sig0**2 + (sp.diff(n, t, 2)+2*sp.diff(ell, s))*sig0 - sp.diff(ell, t)
        v0 = (-b*p0 + sp.diff(b, t)*sig0**2/2
              - (sp.diff(ell, t, s)+B*b)*sig0 + B*sp.diff(ell, s)-sp.diff(h, s))
        expected = (-2*sp.diff(ell, s, 2)*a2**2*x**3 + 3*b*a2*x**2
                    + 2*a2*(v0-sp.diff(ell, s, 2)*d0)*x + b*d0+u0)
        self.assertZero(normal_derivative - expected)
        self.assertZero(sp.Poly(normal_derivative, x).coeff_monomial(x**2) - 3*b*a2)

        # D=0: theta is the new polynomial parameter; no moving-v derivatives.
        X, theta = sp.symbols("X theta")
        y = sp.Function("y")(t, s)
        sig = sp.Function("sigma")(t, s)
        Y = y + sig*X + t*X**2
        Z0 = 2*t*y + sig**2 + n + (2*t*sig+s)*X + t**2*X**2
        W0 = ell - 2*sig*y - sp.diff(n, t)*sig + s*X**2
        Z = theta + Z0
        W = (X-B)*theta + W0
        I = sp.expand(W0-(X-B)*Z0)
        literal = sp.Matrix([Y, Z, W]).jacobian([t, s, theta]).det()
        target = sp.diff(Y, s)*sp.diff(I, t)-sp.diff(Y, t)*sp.diff(I, s)-b*Z*sp.diff(Y, s)
        self.assertZero(literal-target)
        self.assertZero(sp.diff(literal, theta)+b*sp.diff(Y, s))
        for variable in (t, s, theta):
            dt_term = -b*Z if variable == t else 0
            self.assertZero(sp.diff(W, variable)-(X-B)*sp.diff(Z, variable)
                            - sp.diff(I, variable)-dt_term)
        zero_s = {sp.diff(y, s): 0, sp.diff(sig, s): 0}
        factor = X**2 + sp.diff(sig, t)*X + sp.diff(y, t)
        self.assertZero((literal + factor*sp.diff(I, s)).subs(zero_s))
        self.assertEqual(sp.Poly(factor, X).LC(), 1)
        self.assertEqual(sp.Poly(factor, X).degree(), 2)
        # Dropping the B_t row term loses an entire theta coefficient.
        wrong = target+b*Z*sp.diff(Y, s)
        self.assertNotEqual(sp.expand(sp.diff(wrong-literal, theta)), 0)

    def test_quadric_change_inverses_and_zero_level_boundary(self):
        U, P, V, x, p, q = sp.symbols("U P V x p q")
        A, C, T, hb, u, B = sp.symbols("A C T hb u B")
        b = sp.symbols("b", nonzero=True)
        forward = (U+u/2-B*P, P-C/b, V+A*P/b+A*C/b**2-T/b)
        inverse = (x-u/2+B*(p+C/b), p+C/b, q-A*(p+C/b)/b-A*C/b**2+T/b)
        for value, variable in zip(forward, (x, p, q)):
            self.assertZero(value.subs(dict(zip((U, P, V), inverse)), simultaneous=True)-variable)
        for value, variable in zip(inverse, (U, P, V)):
            self.assertZero(value.subs(dict(zip((x, p, q), forward)), simultaneous=True)-variable)
        self.assertZero(sp.Matrix(forward).jacobian([U, P, V]).det()-1)
        level = hb-A*C**2/b**2+T*C/b
        centered = (U+u/2-B*P)**2 + A*P**2-T*P+(b*P-C)*V-hb
        self.assertZero((x**2+b*p*q-level).subs(dict(zip((x, p, q), forward)), simultaneous=True)-centered)
        quadratic = x**2+A*P**2+b*P*V
        self.assertZero((sp.hessian(quadratic, (x, P, V))/2).det()+b**2/4)
        wrong_q = forward[2]+2*T/b
        wrong_residual = forward[0]**2+b*forward[1]*wrong_q-level-centered
        self.assertZero(wrong_residual-2*T*(P-C/b))
        self.assertNotEqual(sp.cancel(wrong_residual), 0)

        lam, r, s1 = sp.symbols("lam r s1", nonzero=True)
        self.assertZero((lam*r*s1)**2+b*(lam*r**2)*(-lam*s1**2/b))
        # The excluded common-factor boundary solves H=0 but meets its vertex.
        v = sp.symbols("v")
        bad = (v**2, v**2, -v**2/b)
        self.assertZero(bad[0]**2+b*bad[1]*bad[2])
        self.assertEqual(tuple(value.subs(v, 0) for value in bad), (0, 0, 0))

    def test_formal_family_birational_ring_boundary_and_minors(self):
        x, p, q, v, delta = sp.symbols("x p q v delta")
        x1, p1, q1 = sp.symbols("x1 p1 q1")
        b = sp.symbols("b", nonzero=True)
        phi = sp.Function("phi")
        forward = (x-b*p*phi(p), p, q+2*x*phi(p)-b*p*phi(p)**2)
        inverse = (x1+b*p1*phi(p1), p1, q1-2*x1*phi(p1)-b*p1*phi(p1)**2)
        for value, variable in zip(forward, (x1, p1, q1)):
            self.assertZero(value.subs(dict(zip((x, p, q), inverse)), simultaneous=True)-variable)
        for value, variable in zip(inverse, (x, p, q)):
            self.assertZero(value.subs(dict(zip((x1, p1, q1), forward)), simultaneous=True)-variable)
        self.assertZero(sp.Matrix(forward).jacobian([x, p, q]).det()-1)
        self.assertZero(forward[0]**2+b*forward[1]*forward[2]-(x**2+b*p*q))

        pv = v**2-delta
        fv = phi(pv)
        xv = v+b*pv*fv
        qv = -1/b-2*v*fv-b*pv*fv**2
        self.assertZero(xv**2+b*pv*qv-delta)
        self.assertZero(xv-b*pv*fv-v)
        self.assertZero(qv+1/b+2*xv*fv-b*pv*fv**2)
        self.assertZero((-qv-1/b-b*pv*fv**2)/(2*fv)-v)

        # A polynomial specialization with a genuine nonunit odd-module factor.
        xp = v+b*pv**2
        qp = -1/b-2*v*pv-b*pv**3
        self.assertZero(qp+1/b+b*pv**3+2*v*pv)
        self.assertEqual([sp.Poly(z, v).degree() for z in (pv, xp, qp)], [2, 4, 6])
        self.assertEqual(sp.rem(sp.Integer(1), p, p), 1)
        # R=L[p] + v*p*L[p]; multiplication and the conductor coefficient.
        aa, cc, ab, cb = sp.symbols("aa cc ab cb")
        product = (aa+v*p*cc)*(ab+v*p*cb)
        expected = aa*ab+(p+delta)*p**2*cc*cb+v*p*(aa*cb+ab*cc)
        self.assertZero(sp.rem(sp.expand(product-expected), v**2-p-delta, v))
        multiplied_by_v = sp.rem(sp.expand(v*(aa+v*p*cc)), v**2-p-delta, v)
        self.assertZero(sp.Poly(multiplied_by_v, v).coeff_monomial(v)-aa)
        # This coefficient must be divisible by p; aa=1 is the nonmembership control.
        self.assertEqual(sp.rem(sp.Integer(1), p, p), 1)

        H1 = x1**2+b*p1*q1-delta
        Q1 = q1+1/b
        minor = sp.diff(H1, p1)*sp.diff(Q1, q1)-sp.diff(H1, q1)*sp.diff(Q1, p1)
        self.assertZero(minor.subs(q1, -1/b)+1)
        self.assertEqual(sp.Poly(q+1/b+2*x*p-b*p**3, x, p, q).total_degree(), 3)
        # At zero level the full line is immersed despite a ramified projection.
        zero_level = [z.subs(delta, 0) for z in (pv, xp, qp)]
        self.assertEqual([sp.diff(z, v).subs(v, 0) for z in zero_level], [0, 1, 0])
        self.assertZero(-b*zero_level[2]-zero_level[0]*(2*b*v+b**2*zero_level[0]**2)-1)

    def test_literal_formal_family_fails_full_calibration(self):
        t, s, v, X, U, P, V = sp.symbols("t s v X U P V")
        n = t*s
        ell = -t**2*s
        h = -t**3*s-s**2/4
        p = v**2
        x = v+v**4
        q = -1-2*v**3-v**6
        theta = q+t**2*p-2*t*s
        y = x-s/2+t*p
        z = 2*t*y+p**2+theta+n
        w = ell-2*p*y-sp.diff(n, t)*p-sp.diff(n, s)*theta
        raw_w = ell-2*P*U-sp.diff(n, t)*P-sp.diff(n, s)*V
        H = (U**2+sp.diff(n, t)*U+sp.diff(n, s)*raw_w
             + sp.diff(n, t, 2)*P**2/2+sp.diff(n, t, s)*P*V
             - sp.diff(ell, t)*P-sp.diff(ell, s)*V)
        self.assertZero(H.subs({U: y, P: p, V: theta}, simultaneous=True)-h)
        self.assertZero(x-p**2-v)
        rows = sp.Matrix([y+p*X+t*X**2,
                          z+(2*t*p+s)*X+t**2*X**2,
                          w+theta*X+s*X**2])
        jacobian = rows.jacobian([t, s, v])
        full_J = sp.expand(jacobian.det())
        self.assertEqual(sp.Poly(full_J, X).degree(), 1)
        self.assertZero(full_J.subs(v, 0)-(t-X))
        self.assertZero(sp.Poly(full_J, X).coeff_monomial(X).subs(v, 0)+1)
        # Evaluation before differentiation wrongly destroys the transverse row.
        wrong = rows.subs(v, 0).jacobian([t, s, v]).det()
        self.assertEqual(wrong, 0)
        self.assertNotEqual(sp.expand(full_J.subs(v, 0)-wrong), 0)


if __name__ == "__main__":
    unittest.main()
