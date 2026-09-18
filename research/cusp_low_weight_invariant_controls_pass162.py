"""Independent finite controls for the low-weight and plinth obstructions162.

Formal coefficient jets test the invariant's quadratic time coefficient.
An exhaustive exact linear system checks all fixed-frame monomials of
weight at most three in one actual example. Separate actual polynomial
families exhibit a nonunit selected plinth. No older checker is imported
or rerun. These tests do not prove universal invariant existence, global
descent, or cancellation.
"""

import itertools
import unittest

import sympy as sp


class CuspLowWeightControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_quadratic_time_coefficient_and_independent_rho_jets(self):
        X, y, theta = sp.symbols("X y theta")
        tau, rho, k, kt, r, n, z, sigma, w = sp.symbols(
            "tau rho k kt r n z sigma w"
        )
        lam, alpha, beta = sp.symbols("lam alpha beta")
        q20, q11, q02, q10, q01, q00 = sp.symbols(
            "q20 q11 q02 q10 q01 q00"
        )
        Y = y+tau*X
        Z = z+sigma*X+tau**3*X**2
        W = w+theta*X+rho*X**2
        F = -y**3+(kt*y+r*theta+n)*X+k*X**2
        Q = q20*X**2+q11*X*Y+q02*Y**2+q10*X+q01*Y+q00
        candidate = sp.Poly(sp.expand(lam*F+alpha*Z+beta*W+Q), X)
        coefficient = candidate.coeff_monomial(X**2)
        expected = lam*k+alpha*tau**3+beta*rho+q20+q11*tau+q02*tau**2
        self.zero(coefficient-expected)
        # k_rho=r; tau and all complex coefficients are fixed. The
        # projected intercept and the other jets do not enter this term.
        derivative = r*sp.diff(coefficient, k)+sp.diff(coefficient, rho)
        self.zero(derivative-lam*r-beta)
        self.zero(sp.diff(coefficient, y))
        k_forced = -(alpha*tau**3+beta*rho+q20+q11*tau+q02*tau**2)/lam
        self.zero(lam*(sp.diff(k_forced, rho)+beta/lam))
        # beta!=0 is a separate mathematical input from158, not inferred
        # from a vanishing formal top coefficient in this test.

    def test_exhaustive_fixed_frame_low_weight_linear_system(self):
        x, t, p, v = sp.symbols("x t p v")
        X, Y, Z, W = sp.symbols("X Y Z W")
        source = (x, t, p, v)
        original = (X, Y, Z, W)
        forward = (
            x, v+t*x,
            p+3*t*v**2+3*t**2*v*x+t**3*x**2,
            t-v**3*x+p*x**2,
        )
        weights = (1, 1, 2, 2)
        powers = [
            e for e in itertools.product(range(4), repeat=4)
            if sum(a*b for a, b in zip(e, weights)) <= 3
        ]
        self.assertEqual(len(powers), 16)
        monomials = [sp.prod(q**d for q, d in zip(original, e)) for e in powers]
        transported = [
            sp.expand(m.xreplace(dict(zip(original, forward)))) for m in monomials
        ]
        derivatives = [sp.Poly(sp.diff(m, x), *source) for m in transported]
        row_powers = sorted({e for derivative in derivatives for e in derivative.monoms()})
        matrix = sp.Matrix([
            [derivative.coeff_monomial(e) for derivative in derivatives]
            for e in row_powers
        ])
        self.assertEqual(matrix.rank(), 15)
        kernel = matrix.nullspace()
        self.assertEqual(len(kernel), 1)
        expected = sp.zeros(16, 1)
        expected[powers.index((0, 0, 0, 0)), 0] = 1
        self.assertEqual(kernel[0], expected)

        F = X*Z-Y**3
        invariant = W-X*F
        self.zero(invariant.xreplace(dict(zip(original, forward)))-t)
        self.zero(sp.diff(invariant.xreplace(dict(zip(original, forward))), x))
        actual_weight = max(
            sum(a*b for a, b in zip(e, weights))
            for e, coefficient in sp.Poly(invariant, *original).terms()
        )
        self.assertEqual(actual_weight, 4)
        # The source polynomial top is nonzero although its initial
        # evaluation vanishes. These two operations are not interchangeable.
        weighted_top = sum(
            coefficient*sp.prod(q**d for q, d in zip(original, e))
            for e, coefficient in sp.Poly(invariant, *original).terms()
            if sum(a*b for a, b in zip(e, weights)) == 4
        )
        self.zero(weighted_top+X*F)
        self.assertNotEqual(weighted_top, 0)

    def test_actual_nonunit_selected_plinth_families(self):
        x, t, p, v = sp.symbols("x t p v")
        X, Y, Z, W = sp.symbols("X Y Z W")
        source, original = (x, t, p, v), (X, Y, Z, W)
        for P in (t**2, t**3+t):
            with self.subTest(P=P):
                dP = sp.diff(P, t)
                forward = (
                    x, v+P*x,
                    p+3*P*v**2+3*P**2*v*x+P**3*x**2,
                    t-v**3*x+p*x**2,
                )
                F = X*Z-Y**3
                inv_t = W-X*F
                to_source = dict(zip(original, forward))
                # Forward inverse composition, simplifying each verified
                # stage before evaluating the next polynomial. No branch
                # or division is introduced by these reductions.
                recovered_t = sp.expand(inv_t.xreplace(to_source))
                self.zero(recovered_t-t)
                recovered_P = P.subs(t, recovered_t)
                recovered_v = sp.expand(forward[1]-recovered_P*x)
                self.zero(recovered_v-v)
                recovered_p = sp.expand(
                    forward[2]-3*recovered_P*recovered_v**2
                    -3*recovered_P**2*recovered_v*x-recovered_P**3*x**2
                )
                self.zero(recovered_p-p)
                self.zero(forward[0]-x)
                # Reverse composition is first a polynomial identity for
                # independent A, then applies upon A=P(inv_t). This avoids
                # expanding a large nested polynomial before cancellation.
                A = sp.Symbol("A")
                inverse_v = Y-A*X
                inverse_p = Z-3*A*Y**2+3*A**2*X*Y-A**3*X**2
                self.zero(inverse_p*X-inverse_v**3-F)
                self.zero(inv_t-inverse_v**3*X+inverse_p*X**2-W)
                self.zero(inverse_v+A*X-Y)
                self.zero(inverse_p+3*A*inverse_v**2+3*A**2*inverse_v*X+A**3*X**2-Z)
                self.assertEqual(tuple(sp.degree(q, x) for q in forward), (1, 1, 2, 2))
                for coordinate, expected_lc in zip(forward, (1, P, P**3, p)):
                    self.zero(sp.Poly(coordinate, x).LC()-expected_lc)

                inverse_Tt = sp.diff(inv_t, Z)
                self.zero(inverse_Tt+X**2)
                # Chain rule for A=P(inv_t) after its source pullback:
                # T(A)=P'(t)*T(t). Differentiate the independent inverse
                # expressions, then substitute A=P(t) and source variables.
                TA = dP*inverse_Tt.xreplace(to_source)
                def transported_partial(expression):
                    fixed_A = sp.diff(expression, Z)
                    moving_A = sp.diff(expression, A)
                    pullback = {**to_source, A: P}
                    return sp.expand(
                        fixed_A.xreplace(pullback)+moving_A.xreplace(pullback)*TA
                    )
                partial = (
                    sp.S.Zero, sp.expand(inverse_Tt.xreplace(to_source)),
                    transported_partial(inverse_p), transported_partial(inverse_v)
                )
                expected_partial = (0, -x**2, 1+3*v**2*dP*x**2, dP*x**3)
                for got, want in zip(partial, expected_partial):
                    self.zero(got-want)
                for i, coordinate in enumerate(forward):
                    self.zero(sum(
                        c*sp.diff(coordinate, q) for c, q in zip(partial, source)
                    )-int(i == 2))
                top = tuple(sp.expand(q).coeff(x, 3) for q in partial)
                self.assertEqual(top, (0, 0, 0, dP))
                self.assertGreater(sp.degree(dP, t), 0)
                self.zero(dP*sp.diff(v, v)-dP)
                self.zero(dP*sp.diff(dP, v))
                self.zero(forward[1]-P*forward[0]-v)
                self.zero(sp.Matrix(forward).jacobian(source).det()+1)
                # Divisibility of N(f) by P' is universal from its formula,
                # not from these samples. These samples check the primitive
                # normalization on generators and its slice v.
                self.assertEqual(sp.diff(v, v), 1)
                self.assertEqual(sp.diff(t, v), 0)
                self.assertEqual(sp.diff(p, v), 0)


if __name__ == "__main__":
    unittest.main()
