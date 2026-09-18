"""Independent finite controls for the primitive cubic profile orbit.

The coefficient identities use the actual divided-difference frame with a
general constant cubic. The normal-monomial tests enumerate a stated finite
bound, not the all-degree normal-form theorem. A theta=0 specialization is
still a polynomial coordinate frame but loses the dense speed cone. The final
seven-shear example deliberately leaves the required profile, then reenters
with a different invariant subring; it is not a counterexample to an orbit
theorem restricted to profile-preserving steps. No solver or search code is
imported. These examples do not establish the absence of other gate failures.
Root owns canonical runtime execution.
"""

import itertools
import unittest

import sympy as sp


class ThreeGoodPrimitiveProfileOrbitChecks(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def assert_vector(self, left, right):
        self.assertEqual(len(left), len(right))
        for first, second in zip(left, right):
            self.assert_zero(first-second)

    @staticmethod
    def polynomial(value, coefficients):
        gamma, beta, alpha, epsilon = coefficients
        return gamma*value**3+beta*value**2+alpha*value+epsilon

    @staticmethod
    def divided_difference(a, v, u, coefficients):
        gamma, beta, alpha, _ = coefficients
        return gamma*(3*a*v**2+3*a**2*v*u+a**3*u**2)+beta*(2*a*v+a**2*u)+alpha*a

    @classmethod
    def frame(cls, a, b, v, u, coefficients):
        return [u, v+a*u, a-cls.polynomial(v, coefficients)+b*u,
                b+cls.divided_difference(a, v, u, coefficients)]

    def test_general_cubic_inverse_and_exceptional_good_slot(self):
        a, b, v, u = sp.symbols("a b v u")
        X, Y, Z, W = sp.symbols("X Y Z W")
        gamma = sp.symbols("gamma", nonzero=True)
        beta, alpha, epsilon = sp.symbols("beta alpha epsilon")
        coefficients = (gamma, beta, alpha, epsilon)
        cubic = lambda value: self.polynomial(value, coefficients)
        delta = lambda A, V, U: self.divided_difference(A, V, U, coefficients)
        frame = self.frame(a, b, v, u, coefficients)
        forward = dict(zip((X, Y, Z, W), frame))
        self.assert_zero(u*delta(a, v, u)-cubic(v+a*u)+cubic(v))
        self.assert_zero(sp.Matrix(frame).jacobian((a, b, v, u)).det()+1)

        # Forward followed by the polynomial inverse, with each recovered
        # variable simplified before the next substitution.
        inverse_a = Z-X*W+cubic(Y)
        recovered_a = sp.expand(inverse_a.subs(forward, simultaneous=True))
        recovered_v = sp.expand(frame[1]-recovered_a*frame[0])
        recovered_b = sp.expand(frame[3]-delta(recovered_a, recovered_v, frame[0]))
        self.assert_vector([recovered_a, recovered_b, recovered_v, frame[0]], [a, b, v, u])

        # The opposite order is checked first with an independent placeholder
        # A, avoiding a needlessly large expansion of the nested inverse.
        # The residual Z is exactly A+XW-F(Y)-Z, then A=inverse_a kills it.
        A = sp.symbols("A")
        V = Y-A*X
        B = W-delta(A, V, X)
        opposite = self.frame(A, B, V, X, coefficients)
        self.assert_vector([opposite[0], opposite[1], opposite[3]], [X, Y, W])
        self.assert_zero(opposite[2]-(A+X*W-cubic(Y)))
        self.assert_zero((A+X*W-cubic(Y)-Z).subs(A, inverse_a))
        H0 = X*W-cubic(Y)
        self.assert_zero(H0.subs(forward, simultaneous=True)-(frame[2]-a))
        self.assert_zero(sp.diff(frame[3], u, 2)-2*gamma*a**3)

        kappa, theta = sp.symbols("kappa theta", nonzero=True)
        lx, ly, lc = sp.symbols("lx ly lc")
        Znew = kappa*Z+(theta-kappa)*H0+lx*X+ly*Y+lc
        T = sp.symbols("T")
        Zback = (T-(theta-kappa)*H0-lx*X-ly*Y-lc)/kappa
        self.assert_zero(Zback.subs(T, Znew)-Z)
        self.assert_zero(Znew.subs(Z, Zback)-T)
        new_frame = frame[:]
        new_frame[2] = sp.expand(Znew.subs(forward, simultaneous=True))
        self.assert_zero(sp.Matrix(new_frame).jacobian((a, b, v, u)).det()+kappa)
        speeds = sp.Matrix([sp.diff(value, u) for value in new_frame[:3]])
        self.assert_vector(speeds, [1, a, theta*b+lx+ly*a])
        self.assert_zero(sp.Matrix.hstack(speeds, speeds.diff(a), speeds.diff(b)).det()-theta)

        # Scale the leading relation by theta so all displayed corrections
        # are polynomial in the constant parameters.
        actual_H = sp.expand(theta*(frame[0]*frame[3]-gamma*frame[1]**3))
        G2 = theta*beta*frame[1]**2
        corrected = sp.expand(actual_H-G2)
        G1 = new_frame[2]-lx*frame[0]+(theta*alpha-ly)*frame[1]
        invariant = sp.expand(corrected-G1-(theta*epsilon-lc))
        self.assert_zero(sp.diff(actual_H, u, 2)-2*theta*beta*a**2)
        self.assert_zero(sp.diff(corrected, u, 2))
        self.assert_zero(invariant+kappa*a)
        self.assert_zero(sp.diff(invariant, u))
        self.assertEqual(sp.gcd(X, gamma*Y**3), 1)

        # The change itself is invertible at theta=0, but this is NOT a
        # qualifying dense-cone frame. Here kappa=1,lx=ly=lc=0 gives Znew=a.
        collapsed = [sp.expand(value.subs({theta: 0, kappa: 1, lx: 0, ly: 0, lc: 0}))
                     for value in new_frame]
        self.assert_zero(collapsed[2]-a)
        collapsed_speeds = sp.Matrix([sp.diff(value, u) for value in collapsed[:3]])
        self.assert_vector(collapsed_speeds, [1, a, 0])
        self.assertEqual(collapsed_speeds.jacobian((a, b, v)).rank(), 1)
        self.assert_zero(sp.Matrix.hstack(collapsed_speeds, collapsed_speeds.diff(a),
                                          collapsed_speeds.diff(b)).det())
        self.assert_zero(sp.Matrix(collapsed).jacobian((a, b, v, u)).det()+1)

    def test_bad_linear_shear_and_finite_normal_monomials(self):
        a, b, v, u = sp.symbols("a b v u")
        X, Y, Z, W, T = sp.symbols("X Y Z W T")
        eta = sp.symbols("eta", nonzero=True)
        coefficients = (sp.Rational(1, 2), 2, -3, 5)
        cubic = lambda value: self.polynomial(value, coefficients)
        frame = self.frame(a, b, v, u, coefficients)
        Wnew = W+eta*Z
        self.assert_zero((T-eta*Z).subs(T, Wnew)-W)
        self.assert_zero(Wnew.subs(W, T-eta*Z)-T)
        sheared = frame[:]
        sheared[3] = sp.expand(frame[3]+eta*frame[2])
        Hbeta = sp.expand(frame[0]*sheared[3]-cubic(frame[1]))
        self.assert_zero(Hbeta-(frame[2]-a+eta*frame[0]*frame[2]))
        self.assert_zero(sp.diff(Hbeta, u, 2)-2*eta*b)
        self.assert_zero(sp.diff(sheared[3], u, 2)-a**3)

        # An affine good correction after the bad shear has its explicit
        # elementary inverse. The exceptional Hbeta correction is forbidden
        # by E-degree, not by failure of polynomial invertibility.
        affine = 2*X-3*Y+5
        self.assert_zero((T-affine).subs(T, Z+affine)-Z)
        self.assert_zero((Z+affine).subs(Z, T-affine)-T)
        self.assert_zero(sp.diff(frame[2]+affine.subs({X: frame[0], Y: frame[1]},
                                                    simultaneous=True), u, 2))
        self.assertEqual(sp.Poly(sp.expand(frame[2]+Hbeta), u).degree(), 2)

        # In this finite bound, signatures are exponents of (a,b,u).
        # H has degree e=1 before, e=2 after a nonzero linear-Z bad shear.
        # Two disjoint normal forms: X^iY^jH^k, and Y^jH^kW^l with l>=1.
        # This enumerates 125+100=225 monomials per weight, not all degrees.
        for e in (1, 2):
            with self.subTest(weight=e):
                signatures, affine_names = {}, []
                for i, j, k in itertools.product(range(5), repeat=3):
                    signature = (j, k, i+j+e*k)
                    self.assertNotIn(signature, signatures)
                    signatures[signature] = ("first", i, j, k)
                    self.assertEqual(signature[2]-signature[0]-e*signature[1], i)
                    if signature[2] <= 1:
                        affine_names.append(("first", i, j, k))
                for j, k in itertools.product(range(5), repeat=2):
                    for ell in range(1, 5):
                        signature = (j+3*ell, k, j+e*k+2*ell)
                        self.assertNotIn(signature, signatures)
                        signatures[signature] = ("second", j, k, ell)
                        self.assertEqual(signature[2]-signature[0]-e*signature[1], -ell)
                        self.assertGreater(signature[2], 1)
                self.assertEqual(len(signatures), 225)
                expected = {("first", 0, 0, 0), ("first", 1, 0, 0), ("first", 0, 1, 0)}
                if e == 1:
                    expected.add(("first", 0, 0, 1))
                self.assertEqual(set(affine_names), expected)

        # Independently obtain the generators' actual leading coefficients;
        # the finite signature test is not based only on guessed weights.
        H0 = sp.expand(frame[0]*frame[3]-cubic(frame[1]))
        for generators, expected in (([frame[0], frame[1], H0, frame[3]],
                                      [(1, 1), (1, a), (1, b), (2, a**3/2)]),
                                     ([frame[0], frame[1], Hbeta, sheared[3]],
                                      [(1, 1), (1, a), (2, eta*b), (2, a**3/2)])):
            for value, (degree, leading) in zip(generators, expected):
                polynomial = sp.Poly(sp.expand(value), u)
                self.assertEqual(polynomial.degree(), degree)
                self.assert_zero(polynomial.LC()-leading)

    def test_multi_step_profile_word_and_seven_shear_boundary(self):
        a, b, v, u = sp.symbols("a b v u")
        X, Y, Z, W = sp.symbols("X Y Z W")
        coefficients = (sp.Rational(1, 2), 0, 0, 0)
        seed = self.frame(a, b, v, u, coefficients)
        variables = (X, Y, Z, W)

        def apply_word(values, steps):
            current, history = list(values), [list(values)]
            for target, addition in steps:
                self.assert_zero(sp.diff(addition, variables[target]))
                actual_addition = addition.subs(dict(zip(variables, current)), simultaneous=True)
                current[target] = sp.expand(current[target]+actual_addition)
                history.append(list(current))
            return current, history

        # Every step of this first word preserves the requested profile.
        # The first step is exceptional; the remaining two are affine shears.
        preserving = [(2, X*W-Y**3/2), (1, X+1), (3, Z+X)]
        result, history = apply_word(seed, preserving)
        inverse = [(target, -addition) for target, addition in reversed(preserving)]
        recovered, _ = apply_word(result, inverse)
        self.assert_vector(recovered, seed)
        reversed_result, _ = apply_word(seed, inverse)
        both_orders, _ = apply_word(reversed_result, preserving)
        self.assert_vector(both_orders, seed)
        for current in history:
            self.assertEqual([sp.Poly(value, u).degree() for value in current], [1, 1, 1, 2])
            speeds = sp.Matrix([sp.diff(value, u) for value in current[:3]])
            self.assertNotEqual(sp.expand(sp.Matrix.hstack(speeds, speeds.diff(a),
                                                          speeds.diff(b)).det()), 0)
        final_X, final_Y, final_Z, final_W = result
        old_Y = final_Y-final_X-1
        old_W = final_W-final_Z-final_X
        lifted_invariant = final_X*old_W-old_Y**3/2-final_Z/2
        self.assert_zero(lifted_invariant+a/2)

        delta = self.divided_difference(Z, Y, X, coefficients)
        bypass = [(2, -X*W+Y**3/2), (1, -Z*X), (3, -delta), (2, W),
                  (3, delta), (1, Z*X), (2, X*W-Y**3/2)]
        endpoint, history = apply_word(seed, bypass)
        self.assert_vector(history[3], [u, v, a, b])
        self.assert_vector(history[4], [u, v, a+b, b])
        self.assert_vector(endpoint, self.frame(a+b, b, v, u, coefficients))
        inverse_bypass = [(target, -addition) for target, addition in reversed(bypass)]
        back, _ = apply_word(endpoint, inverse_bypass)
        self.assert_vector(back, seed)
        inverse_first, _ = apply_word(seed, inverse_bypass)
        self.assert_vector(inverse_first, self.frame(a-b, b, v, u, coefficients))
        back_other_order, _ = apply_word(inverse_first, bypass)
        self.assert_vector(back_other_order, seed)
        self.assertEqual([sp.Poly(value, u).degree() for value in history[3]], [1, 0, 0, 0])
        first_speeds = sp.Matrix([sp.diff(value, u) for value in history[1][:3]])
        self.assert_zero(sp.Matrix.hstack(first_speeds, first_speeds.diff(a),
                                          first_speeds.diff(b)).det())
        endpoint_speeds = sp.Matrix([sp.diff(value, u) for value in endpoint[:3]])
        self.assert_zero(sp.Matrix.hstack(endpoint_speeds, endpoint_speeds.diff(a),
                                          endpoint_speeds.diff(b)).det()-1)
        self.assertEqual([sp.Poly(value, u).degree() for value in endpoint], [1, 1, 1, 2])
        old_I = seed[0]*seed[3]-seed[1]**3/2-seed[2]
        new_I = endpoint[0]*endpoint[3]-endpoint[1]**3/2-endpoint[2]
        self.assert_zero(old_I+a)
        self.assert_zero(new_I+a+b)
        self.assert_zero(sp.diff(old_I, b))
        self.assertEqual(sp.diff(sp.expand(new_I), b), -1)
        # Hence the two displayed invariant subrings C[a] and C[a+b] differ.
        # Both endpoints are already translations; no cancellation obstruction.


if __name__ == "__main__":
    unittest.main(verbosity=2)
