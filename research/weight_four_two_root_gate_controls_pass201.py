"""Independent finite exact controls for the two-root differential gates.

These four methods check identities, exact resultants, and explicit candidate
arithmetic from the two pass201 notes.  They do not prove the finite-extension
trace argument, completeness of the differential classification, actual frame
realization, coefficient-field rationality, or cancellation recognition.
No previous checker, proof solver, or generated implementation is imported.
Root owns canonical execution after complete saved-source review.
"""

import unittest

import sympy as sp


class TwoRootGateControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def polynomial_zero(self, expression, *variables):
        self.assertTrue(sp.Poly(sp.expand(expression), *variables).is_zero)

    def test_linear_product_conic_parameter_and_residue_arithmetic(self):
        r, local = sp.symbols("r local")
        t = r**2/(1+r**2)
        q = r/(1+r**2)
        p, s = t*(1-t), 1-2*t
        dt = lambda expression: sp.factor(sp.diff(expression, r)/sp.diff(t, r))
        h = sp.Function("h")(r)

        def linear(expression):
            return -s*expression+p*dt(expression)-2*p**2*s*dt(dt(expression))

        self.zero(q**2-p)
        self.zero(t/q-r)
        self.zero(dt(q)-s/(2*q))
        self.zero(dt(dt(q))+1/(4*q**3))
        self.zero(linear(q))
        self.zero(linear(q*h)+2*p**2*dt(q*s*dt(h)))
        self.zero(sp.diff(t, r)/(q*s)-2/(1-r**2))
        self.assertEqual(sp.limit((r-1)*2/(1-r**2), r, 1), -1)
        self.assertEqual(sp.limit((r+1)*2/(1-r**2), r, -1), 1)
        # Finite local illustrations only; the written trace proof is universal.
        for ramification in (1, 2, 3, 5):
            pullback = (2*ramification*local**(ramification-1)
                        / (1-(1+local**ramification)**2))
            self.assertEqual(sp.limit(local*pullback, local, 0), -ramification)
        for exponent in (-4, -2, -1, 0, 1, 3):
            self.assertEqual(
                sp.residue(sp.diff(local**exponent, local), local, 0), 0)

    def test_scaled_first_flow_and_raw_second_gate_prefactor(self):
        z, u, v, F, d, vz = sp.symbols("z u v F d vz")
        D1 = z**2-1
        G = -4*u*z+4*z**2+1
        Uflow = (-u**2+2*u*z+v)/D1
        Vnumer = v*(4*u**2*z-8*u*z**2+2*u-3*v*z+4*z**3-5*z)
        Vflow = Vnumer/(D1*G)
        # a=d_t/d, computed from d=-z/(16q^5), q^2=(1-z^2)/4.
        a = -2*(4*z**2+1)/(z*D1)
        f1 = 2*F*u/D1
        f2 = 4*F*v/D1**2
        # Differentiate f2 before imposing the proposed v flow.
        f3_free = 8*F*((u-4*z)*v+D1*vz)/D1**3
        D0 = sp.factor(a*d*F/4+d*f1)
        D0prime = d*(2*sp.diff(a, z)+a**2)*F/4 + 5*a*d*f1/4 + d*f2
        first_gate = 20*D0*f3_free-3*d*f2**2-12*f2*D0prime
        self.zero(D0+d*F*G/(2*z*D1))
        self.zero(first_gate+80*d*F**2*G*(vz-Vflow)/(z*D1**3))

        def dz(expression):
            return sp.factor(
                sp.diff(expression, z)
                + Uflow*sp.diff(expression, u)
                + Vflow*sp.diff(expression, v)
                + F*u/D1*sp.diff(expression, F)
                + d*a/2*sp.diff(expression, d)
            )

        def dt(expression):
            return sp.factor(2*dz(expression))

        self.zero(dt(F)-f1)
        self.zero(dt(f1)-f2)
        self.zero(dt(f2)-f3_free.subs(vz, Vflow))
        self.zero(dt(D0)-D0prime)
        # All entries below are the raw defining R,nu,p2,p,L3,J3 equations.
        # The graded symbols F,d are retained until the final d^2 substitution.
        R = 1/F
        Delta = -f2/(2*F**3)
        nu = sp.factor(f2**2/(8*F**3*D0))
        p2 = sp.factor(-Delta/(R*nu))
        R1, R2 = dt(R), dt(dt(R))
        nu1, nu2 = dt(nu), dt(dt(nu))
        p = sp.factor(2*R1/R-nu1/nu)
        L3 = sp.factor((R*nu2/4-R1*nu1/2-nu*R2/2
                        -R*nu*p**2/2-nu**2*p2)/(3*R*p2))
        J3 = sp.factor(-R*dt(L3)+R1*L3-nu*nu1/2-p*(3*R*L3+nu**2))
        L = -u+v*z+2*z
        Q = (z**2*v**2+(u*z+2*z**2-1)*v-(4*z**2-2)*u**2
             +(8*z**3-3*z)*u-4*z**4+3*z**2-1)
        before_d_square = 224*v**3*z**2*L*Q/(F**4*d**2*D1**7*G**5)
        self.zero(J3-before_d_square)
        normalized_numerator = sp.cancel(J3*F**4*d**2)
        # d^2=-4z^2/D1^5 converts +224 to -56, including its sign.
        final_J3 = -normalized_numerator*D1**5/(4*z**2*F**4)
        self.zero(final_J3+56*v**3*L*Q/(F**4*D1**2*G**5))

    def test_first_exact_resultant_and_discriminant(self):
        z, u, v = sp.symbols("z u v")
        D1 = z**2-1
        G = -4*u*z+4*z**2+1
        Q = (z**2*v**2+(u*z+2*z**2-1)*v-(4*z**2-2)*u**2
             +(8*z**3-3*z)*u-4*z**4+3*z**2-1)
        Vnumer = v*(4*u**2*z-8*u*z**2+2*u-3*v*z+4*z**3-5*z)
        # Construct N from polynomial differentiation, not a stored expansion.
        N = (D1*G*sp.diff(Q, z)+G*(-u**2+2*u*z+v)*sp.diff(Q, u)
             +Vnumer*sp.diff(Q, v))
        H = ((64*z**4-37*z**2)*u**2+(-128*z**5+72*z**3+2*z)*u
             +64*z**6-32*z**4-7*z**2+2)
        resultant = sp.resultant(Q, N, v)
        expected = 4*z**3*(z-u)*(u-1)*(u+1)*D1*G*H
        self.polynomial_zero(resultant-expected, z, u)
        self.polynomial_zero(
            sp.discriminant(H, u)+12*z**2*D1*(8*z**2-5)**2, z)
        # These exact polynomial identities do not by themselves establish
        # which factor must vanish in an arbitrary differential field.

    def test_second_exact_resultant_and_all_candidate_gates(self):
        z, u, v = sp.symbols("z u v")
        D1 = z**2-1
        G = -4*u*z+4*z**2+1
        BQ = u*z+2*z**2-1
        CQ = -(4*z**2-2)*u**2+(8*z**3-3*z)*u-4*z**4+3*z**2-1
        Q = z**2*v**2+BQ*v+CQ
        H = ((64*z**4-37*z**2)*u**2+(-128*z**5+72*z**3+2*z)*u
             +64*z**6-32*z**4-7*z**2+2)
        Hu, Hz = sp.diff(H, u), sp.diff(H, z)
        VH = (u**2-2*u*z)*Hu-D1*Hz
        M = z**2*VH**2+BQ*VH*Hu+CQ*Hu**2
        self.zero(M-Hu**2*Q.subs(v, VH/Hu))
        resultant = sp.resultant(H, M, u)
        expected = (1296*z**12*D1**5*(4*z**2-1)**4*(8*z**2-5)**4
                    *(64*z**2-37)**2*(121*z**2-94))
        self.polynomial_zero(resultant-expected, z)
        self.assertFalse(sp.Poly(expected, z).is_zero)

        Uflow = (-u**2+2*u*z+v)/D1
        Vflow = v*(4*u**2*z-8*u*z**2+2*u-3*v*z+4*z**3-5*z)/(D1*G)
        pairs = ((z, -1, 1), (1, 1-2*z, (2*z-1)**2),
                 (-1, 1+2*z, (2*z+1)**2))
        for U, V, gate in pairs:
            substitution = {u: U, v: V}
            self.zero(Uflow.subs(substitution, simultaneous=True)-sp.diff(U, z))
            self.zero(Vflow.subs(substitution, simultaneous=True)-sp.diff(V, z))
            self.zero(Q.subs(substitution, simultaneous=True))
            self.zero(G.subs(substitution, simultaneous=True)-gate)

        r = sp.symbols("r")
        c = sp.symbols("c", nonzero=True)
        t = r**2/(1+r**2)
        q = r/(1+r**2)
        z_value = 2*t-1
        dt = lambda expression: sp.factor(sp.diff(expression, r)/sp.diff(t, r))
        d = dt(dt(dt(q)))/6
        self.zero(d-(1-2*t)/(16*q**5))
        self.zero(d**2+4*z_value**2/(z_value**2-1)**5)
        candidates = ((c*q, z_value, -1),
                      (c*q/t, 1, 1-2*z_value),
                      (c*q/(t-1), -1, 1+2*z_value))
        for f, expected_u, expected_v in candidates:
            f1, f2 = dt(f), dt(dt(f))
            D0 = sp.factor(dt(d)*f/4+d*f1)
            self.zero(2*t*(t-1)*f1/f-expected_u)
            self.zero(4*t**2*(t-1)**2*f2/f-expected_v)
            self.zero(20*D0*dt(f2)-3*d*f2**2-12*f2*dt(D0))
            self.assertNotEqual(sp.cancel(f*f2*D0), 0)
        # Sufficiency/completeness over arbitrary finite K and all geometric
        # applications remain the responsibility of the written arguments.


if __name__ == "__main__":
    unittest.main()
