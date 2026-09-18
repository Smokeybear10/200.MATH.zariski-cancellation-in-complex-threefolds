"""Exact controls for the actual zero-r square-root boundary in pass171.

Throughout c is a nonzero complex constant.  The polynomial four-frame
has an explicit staged inverse and E=d/dx.
It is already a translation, not a cancellation counterexample.  The
tests distinguish the coefficient rho derivative from its fixed-v
extension and retain the actual degree-two coefficient cover.  Finite
checks do not prove the general kernel or irreducibility statements.
No older checker is imported.  Root executes after full source review.
"""

import unittest

import sympy as sp


class ZeroRSquareRootControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_actual_staged_inverse_and_initial_profile(self):
        x, y, t, n, c = sp.symbols("x y t n c")
        X, Y, Z, W, T = sp.symbols("X Y Z W T")
        Yf = y+t*x
        Zf = n+3*t*y**2+3*t**2*y*x+t**3*x**2
        Hf = n*x-y**3
        Wf = t+c*Hf**2
        self.zero(x*Zf-Yf**3-Hf)
        Htarget = X*Z-Y**3
        tback = W-c*Htarget**2
        yback_T = Y-T*X
        nback_T = Z-3*T*Y**2+3*T**2*Y*X-T**3*X**2

        # Inverse after forward: simplify the invariant stage first.
        self.zero(tback.xreplace({X: x, Y: Yf, Z: Zf, W: Wf})-t)
        self.zero(yback_T.xreplace({X: x, Y: Yf, T: t})-y)
        self.zero(nback_T.xreplace({X: x, Y: Yf, Z: Zf, T: t})-n)
        # Forward after inverse, with T independent until the last step.
        Hback = nback_T*X-yback_T**3
        self.zero(Hback-Htarget)
        self.zero(yback_T+T*X-Y)
        self.zero(nback_T+3*T*yback_T**2+3*T**2*yback_T*X+T**3*X**2-Z)
        self.zero(T+c*Htarget**2-W-(T-tback))

        frame = (x, Yf, Zf, Wf)
        self.assertEqual([sp.degree(f, x) for f in frame], [1, 1, 2, 2])
        leaders = [sp.Poly(f, x).LC() for f in frame]
        self.assertEqual(leaders, [1, t, t**3, c*n**2])
        self.zero(leaders[0]*leaders[2]-leaders[1]**3)
        eta = sp.symbols("eta")
        initials = sp.Matrix([eta, t*eta, c*n**2*eta**2])
        self.zero(initials.jacobian((eta, t, n)).det()-2*c*n*eta**3)
        self.assertEqual(sp.diff(x, x), 1)
        # T^2-rho/c is Eisenstein at rho over C(t)[rho], hence irreducible
        # over C(t,rho).  The finite deck check is not that degree proof.
        rho = c*n**2
        self.zero(rho.subs(n, -n)-rho)
        self.assertNotEqual(sp.expand((-n)-n), 0)

    def test_inverse_derived_actual_partial_and_selected_top(self):
        x, y, t, n, c = sp.symbols("x y t n c")
        X, Y, Z, W, T = sp.symbols("X Y Z W T")
        Htarget = X*Z-Y**3
        tback = W-c*Htarget**2
        nback_T = Z-3*T*Y**2+3*T**2*Y*X-T**3*X**2
        self.zero(sp.diff(tback, Z)+2*c*X*Htarget)
        self.zero(sp.diff(nback_T, T)+3*(Y-T*X)**2)
        # These follow by the inverse chain rule at fixed X,Y,W.
        H = n*x-y**3
        Tt = -2*c*x*H
        Ty = -x*Tt
        Tn = 1-3*y**2*Tt
        coefficients = [sp.Integer(0), Tt, Tn, Ty]
        variables = (x, t, n, y)
        Yf = y+t*x
        Zf = n+3*t*y**2+3*t**2*y*x+t**3*x**2
        Wf = t+c*H**2

        def actual_partial(f):
            return sum(sp.diff(f, variable)*coefficient
                       for variable, coefficient in zip(variables, coefficients))

        for f, expected in zip((x, Yf, Zf, Wf), (0, 0, 1, 0)):
            self.zero(actual_partial(f)-expected)
        self.zero(Tt-(2*c*y**3*x-2*c*n*x**2))
        self.zero(Tn-(1-6*c*y**5*x+6*c*n*y**2*x**2))
        self.zero(Ty-(-2*c*y**3*x**2+2*c*n*x**3))
        top = [sp.Poly(f, x).coeff_monomial(x**3) for f in (Tt, Tn, Ty)]
        self.assertEqual(top, [0, 0, 2*c*n])

        def selected_N(f):
            return 2*c*n*sp.diff(f, y)

        for invariant in (t, n, c*n**2):
            self.zero(selected_N(invariant))
        self.zero(selected_N(y)-2*c*n)
        self.zero(selected_N(selected_N(y)))
        self.zero(selected_N(y/(2*c*n))-1)
        # The content factor n is retained, not silently made a global unit.
        self.assertEqual(sp.rem(2*c*n, n, n), 0)

    def test_exact_coefficient_partials_graph_and_calibrated_determinant(self):
        x, y, t, n, c, U, v = sp.symbols("x y t n c U v")
        rho = c*n**2
        s = 1/(2*c*n)

        def Drho(f):
            return sp.diff(f, n)/(2*c*n)

        self.zero(Drho(rho)-1)
        self.zero(Drho(t))
        self.zero(Drho(n)-s)
        self.zero(Drho(s)+1/(4*c**2*n**3))
        self.assertNotEqual(sp.cancel(Drho(s)), 0)
        P = -2*c*n*U**3
        R = t+c*U**6
        self.zero(U**3+s*P)  # k=0, ell=0 in the exact zero-r potential.
        self.zero(Drho(P)+U**3/n)
        self.zero(Drho(R))
        self.zero(sp.diff(R, U)-sp.diff(P, t)-sp.diff(P, U)*Drho(P))
        self.zero(sp.diff(R, t)+sp.diff(P, U)*Drho(R)-1)

        # Independent finite normal-form control, allowing either A=0 or
        # A nonzero.  It is not a classification or field-degree proof.
        A0, B0, C0 = sp.symbols("A0 B0 C0")
        q_general = A0*n+B0
        rho_general = A0*n**2/2+B0*n+C0

        def Drho_general(f):
            return sp.diff(f, n)/q_general

        self.zero(Drho_general(rho_general)-1)
        self.zero(Drho_general(Drho_general(q_general**2)))
        self.zero(q_general*Drho_general(q_general)-A0)
        self.zero(q_general*Drho_general(n)-1)
        z = n+3*t*y**2
        theta = P.subs(U, y)
        w = R.subs(U, y)
        Yf = y+t*x
        Zf = z+3*t**2*y*x+t**3*x**2
        Wf = w+theta*x+rho*x**2
        self.zero(Wf-(t+c*(n*x-y**3)**2))
        rows = sp.Matrix([[sp.diff(f, t), Drho(f), sp.diff(f, y)]
                          for f in (Yf, Zf, Wf)])
        fixed_y_determinant = rows.det()
        self.zero(fixed_y_determinant+1/(2*c*n))

        # y=2cn*v.  The rho column at fixed v has an additional y term;
        # checking it prevents confusing coefficient and full-chart partials.
        replacement = {y: 2*c*n*v}
        for f in (Yf, Zf, Wf):
            fv = f.xreplace(replacement)
            self.zero(Drho(fv)-(Drho(f)+y*sp.diff(f, y)/(2*c*n**2)).xreplace(replacement))
            self.zero(sp.diff(fv, v)-(2*c*n*sp.diff(f, y)).xreplace(replacement))
            self.zero(sp.diff(fv, t)-sp.diff(f, t).xreplace(replacement))
        # The column operations just checked multiply the determinant by 2cn.
        self.zero(2*c*n*fixed_y_determinant+1)


if __name__ == "__main__":
    unittest.main()
