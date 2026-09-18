"""Finite algebra controls for the conditional cubic-conic exclusion242.

These independently rebuild the q=rho**2-t**3 potentials, centered graph
coefficients, differentiated coefficient gates, and projected determinant.
The actual graph/cofactor hypothesis and universal-chart calibration remain
written geometric inputs, not conclusions certified by these tests.  The
affine parameter change is checked with its nontrivial determinant factor.
No retained proof, checker, or solver is imported; no whole-model claim.
"""

import unittest

import sympy as sp


t, rho = sp.symbols("t rho", nonzero=True)
U, V, zeta, h, v = sp.symbols("U V zeta h v")
A = sp.Symbol("A", nonzero=True)
B, C, At, Ar, Bt, Br, Ct, Cr = sp.symbols("B C At Ar Bt Br Ct Cr")
K = {(i, j): sp.Symbol(f"k{i}{j}") for i in range(5) for j in range(5-i)}
N = {(i, j): sp.Symbol(f"n{i}{j}") for i in range(4) for j in range(4-i)}
L = {(i, j): sp.Symbol(f"ell{i}{j}") for i in range(3) for j in range(3-i)}
m = sp.Symbol("m")


def clean(expression):
    return sp.cancel(sp.expand(expression))


def partial(expression, axis):
    """Original coefficient derivative; h and formal plane variables are fixed."""
    result = sp.diff(expression, (t, rho)[axis])
    for symbol, values in ((A, (At, Ar)), (B, (Bt, Br)), (C, (Ct, Cr))):
        result += sp.diff(expression, symbol)*values[axis]
    for table in (K, N, L):
        for (i, j), symbol in table.items():
            derivative = sp.diff(expression, symbol)
            if derivative == 0:
                continue
            target = (i+(axis == 0), j+(axis == 1))
            if target not in table:
                raise ValueError("The finite jet table is too short")
            result += derivative*table[target]
    return sp.expand(result)


def divided_jet(table, degree):
    return sum(table[i, degree-i]*U**i*V**(degree-i)
               / (sp.factorial(i)*sp.factorial(degree-i)) for i in range(degree+1))


def raw_polynomials():
    eps = sp.Symbol("eps")
    q = rho**2-t**3
    shifted = sp.expand(q.subs({t: t+eps*U, rho: rho+eps*V}, simultaneous=True))
    f = shifted.coeff(eps, 2)+divided_jet(K, 1)+N[0, 0]
    S = shifted.coeff(eps, 3)+divided_jet(K, 2)+divided_jet(N, 1)
    Q = shifted.coeff(eps, 4)+divided_jet(K, 3)+divided_jet(N, 2) \
        - L[1, 0]*U-L[0, 1]*V-m
    R, beta, T = sp.diff(f, V), partial(f, 1), L[0, 0]-S
    H = sp.expand(T**2+R*beta*T+R**2*Q)
    centered = sp.Poly(sp.expand(H.subs(V, zeta-K[0, 1]/2)), U, zeta)
    return f, S, Q, R, beta, centered


def first_gates():
    c, d = K[0, 2], K[1, 1]
    return {K[0, 3]: 0, K[1, 2]: 0, K[2, 1]: 0,
            N[0, 2]: 3*c**2/8, N[1, 1]: c*d/2}


class RepeatedRootCubicConicControls242(unittest.TestCase):
    def assertZero(self, expression):
        self.assertEqual(clean(expression), 0)

    def test_complete_raw_coefficients_and_center_graph_comparisons(self):
        f, S, Q, R, beta, raw = raw_polynomials()
        kappa, c, d = K[0, 1], K[0, 2], K[1, 1]
        self.assertZero(f-V**2+3*t*U**2-K[1, 0]*U-kappa*V-N[0, 0])
        self.assertZero(R-2*V-kappa)
        self.assertZero(beta-d*U-c*V-N[0, 1])
        self.assertZero(beta-sp.diff(S, V))
        p = S.subs(V, -kappa/2)-L[0, 0]
        self.assertZero(raw.as_expr().subs(zeta, 0)-p**2)
        self.assertZero(sp.Poly(raw.as_expr(), zeta).coeff_monomial(zeta))
        top = sum(coefficient*U**powers[0]*zeta**powers[1]
                  for powers, coefficient in raw.terms() if sum(powers) == 6)
        self.assertZero(top-U**6)
        expected = {(0, 5): 2*K[0, 3]/3, (1, 4): 2*K[1, 2],
                    (0, 4): 2*N[0, 2]-3*c**2/4-kappa*K[0, 3],
                    (2, 3): 2*K[2, 1],
                    (1, 3): 4*N[1, 1]-2*c*d-2*kappa*K[1, 2],
                    (3, 2): 2*K[3, 0]/3+c,
                    (2, 2): 2*N[2, 0]-d**2-c*K[2, 0]/2-kappa*K[2, 1]}
        for powers, coefficient in expected.items():
            self.assertZero(raw.coeff_monomial(U**powers[0]*zeta**powers[1])-coefficient)

        P = A*U**2+B*U+C
        linear = -U/A-B/(2*A**2)
        e = 2/A**3
        eta = (C*e-2*(B/(2*A**2))**2)/2
        M = linear**2+e*zeta
        model = sp.Poly(sp.expand((zeta-P)**2*M+2*eta*zeta*(zeta-P)), U, zeta)
        self.assertZero(P*e-2*linear**2-2*eta)
        self.assertZero(sp.Poly(P*linear, U).coeff_monomial(U**3)+1)
        self.assertZero(sp.Poly(P*linear, U).coeff_monomial(U**2)+3*B/(2*A))
        self.assertZero((-3*B/(2*A)).subs(B, -A*K[2, 0]/3)-K[2, 0]/2)
        self.assertZero(sp.Poly(model.as_expr(), zeta).coeff_monomial(zeta**3)-e)
        self.assertZero(sp.Poly(model.as_expr(), zeta).coeff_monomial(zeta**2)
                        -linear**2+2*e*P-2*eta)
        self.assertZero(model.coeff_monomial(U**2*zeta**2)+3/A**2)
        self.assertZero(model.coeff_monomial(U*zeta**2)+3*B/A**3)
        self.assertEqual(sp.degree(model.as_expr(), zeta), 3)

    def test_differentiated_coefficients_force_both_A_partials_to_vanish(self):
        _, _, _, _, _, raw = raw_polynomials()
        kappa, c, d = K[0, 1], K[0, 2], K[1, 1]
        gates = first_gates()
        self.assertZero(partial(c, 0).subs(gates))
        self.assertZero(partial(c, 1).subs(gates))
        self.assertZero(partial(d, 0).subs(gates))
        self.assertZero(partial(d, 1).subs(gates))
        self.assertZero(partial(c*d/2, 0).subs(gates))  # n_ttr=0 by commuting derivatives.

        equation12 = 2*N[2, 0]-d**2-c*K[2, 0]/2+3/A**2
        rho12 = partial(equation12, 1).subs({**gates, N[2, 1]: 0}, simultaneous=True)
        self.assertZero(rho12+6*Ar/A**3)
        self.assertZero(-A**3*rho12/6-Ar)  # Unit coefficient extracts A_rho.

        raw_e = c**2*kappa/4-4*L[0, 1]-2*c*N[0, 1]
        raw15 = -4*L[1, 0]-2*d*N[0, 1]-c*N[1, 0]+c*kappa*d/2
        self.assertZero(raw.coeff_monomial(zeta**3).subs(gates, simultaneous=True)-raw_e)
        self.assertZero(raw.coeff_monomial(U*zeta**2).subs(gates, simultaneous=True)-raw15)
        rho15 = partial(raw15, 1).subs(gates, simultaneous=True)
        te = partial(raw_e, 0).subs(gates, simultaneous=True)
        self.assertZero(rho15+4*L[1, 1]+3*c**2*d/4)
        self.assertZero(rho15-te)
        self.assertZero(partial(K[2, 0]/A**2, 1).subs({**gates, Ar: 0}, simultaneous=True))
        model_et = partial(2/A**3, 0)
        self.assertZero(model_et+6*At/A**4)
        self.assertZero(-A**4*model_et/6-At)  # Unit coefficient extracts A_t.

    def test_h_fixed_projected_map_and_complete_determinant(self):
        f, S, Q, Rformal, beta, _ = raw_polynomials()
        kappa, c, d = K[0, 1], K[0, 2], K[1, 1]
        P = A*h**2+B*h+C
        linear = -h/A-B/(2*A**2)
        theta = P-kappa/2
        D = -d*h/2-N[0, 1]/2-c*theta/4+c*kappa/8
        w = D-linear/2
        z = 2*rho*w+f.subs({U: h, V: theta}, simultaneous=True)
        gates = {**first_gates(), At: 0, Ar: 0, Bt: A*c/2, Br: 0,
                 Ct: c*B/4+3/(2*A), Cr: 0, K[2, 0]: -3*B/A,
                 K[3, 0]: -3*c/2,
                 N[2, 0]: d**2/2-3*c*B/(4*A)-3/(2*A**2),
                 N[1, 0]: -C/A-B**2/(2*A**2)+kappa*d/2}
        impose = lambda expression: clean(expression.subs(gates, simultaneous=True))
        Pt = A*c*h/2+c*B/4+3/(2*A)
        Bexpression = -A*K[2, 0]/3
        p1 = N[1, 0]-kappa*d/2
        Cexpression = -A*p1-B**2/(2*A)
        self.assertZero(impose(partial(Bexpression, 0))-A*c/2)
        self.assertZero(impose(partial(Bexpression, 1)))
        self.assertZero(impose(Cexpression)-C)
        self.assertZero(impose(partial(Cexpression, 0))-c*B/4-3/(2*A))
        self.assertZero(impose(partial(Cexpression, 1)))
        self.assertZero(impose(partial(P, 0))-Pt)
        self.assertZero(impose(partial(P, 1)))
        self.assertZero(Pt+A**2*c*linear/2-3/(2*A))
        self.assertZero(sp.diff(P, h)+2*A**2*linear)
        self.assertZero(impose(partial(linear, 0))+c/(4*A))
        self.assertZero(impose(partial(linear, 1)))

        theta_t, theta_r = impose(partial(theta, 0)), impose(partial(theta, 1))
        wt, wr = impose(partial(w, 0)), impose(partial(w, 1))
        self.assertZero(theta_t-Pt+d/2)
        self.assertZero(theta_r+c/2)
        self.assertZero(wt+c*Pt/4-c/(8*A))
        self.assertZero(wr-c**2/16)
        # Direct actual projected rows (h,z,w), not merely a copied wedge formula.
        zt, zr = impose(partial(z, 0)), impose(partial(z, 1))
        Jprojected = clean(zt*wr-zr*wt)
        B1 = impose(partial(f, 0).subs({U: h, V: theta}, simultaneous=True))
        C1 = impose(beta.subs({U: h, V: theta}, simultaneous=True)+2*w)
        R = 2*P
        self.assertZero(C1-c*P/2+linear)
        self.assertZero(R*theta_t+B1-2*P*Pt+2*A**2*linear**2+P/A)
        Jreduced = clean((R*theta_t+B1)*wr-(R*theta_r+C1)*wt)
        self.assertZero(Jprojected-Jreduced)
        self.assertZero(Jprojected+c*linear/(4*A))

    def test_affine_parameter_factor_and_both_c_branches(self):
        speed = sp.Symbol("speed", nonzero=True)
        offset, ht, hr = sp.symbols("offset ht hr")
        entries = sp.symbols("j0:9")
        new_rows = sp.Matrix(3, 3, entries)
        parameter_change = sp.Matrix([[1, 0, 0], [0, 1, 0], [ht, hr, speed]])
        self.assertZero((new_rows*parameter_change).det()-speed*new_rows.det())
        J0 = sp.Symbol("J0", nonzero=True)
        self.assertZero(speed*(J0/speed)-J0)
        self.assertNotEqual(clean(J0/speed-speed*J0), 0)

        c = K[0, 2]
        linear = -h/A-B/(2*A**2)
        Jnew = -c*linear/(4*A)
        self.assertZero(sp.diff(Jnew, h)-c/(4*A**2))
        old = sp.expand(speed*Jnew.subs(h, speed*v+offset))
        self.assertZero(sp.Poly(old, v).coeff_monomial(v)-c*speed**2/(4*A**2))
        self.assertZero(Jnew.subs(c, 0))
        self.assertZero(old.subs(c, 0))
        self.assertNotEqual(Jnew.subs(c, 0), J0/speed)
        nonzero_c = sp.Symbol("nonzero_c", nonzero=True)
        nonconstant_coefficient = sp.diff(Jnew, h).subs(c, nonzero_c)
        self.assertNotEqual(nonconstant_coefficient, 0)
        self.assertZero(nonconstant_coefficient*(4*A**2/nonzero_c)-1)
        # The first branch is zero, not a permitted scalar unit; the other
        # branch remains nonconstant even after the correctly calibrated change.


if __name__ == "__main__":
    unittest.main()
