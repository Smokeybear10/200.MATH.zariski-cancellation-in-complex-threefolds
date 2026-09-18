"""Independent exact example controls for the two pass132 restrictions.

One method supplies an actual successful NONprimitive unit-row boundary and
an invariant-divisor/coordinate-hyperplane ideal control. A second checks a
constant-coefficient cubic family of compensated two-shear words, including
both polynomial inverse orders and both correction gates. A third checks four
actual b-dependent words that fail the stipulated three-good profile.
A fourth checks the explicit normalized constant-speed family with a polynomial
eta(I), including its inverse and polynomial kernel-coordinate completion.
A fifth checks an irreducible normalized action with a nonempty reduced fixed
locus. It makes no equality claim for the nonreduced fixed-point scheme ideal.
A sixth checks the actual selected bad partial and its degree-two intrinsic
coefficient in the dense normal form, for a generic quadratic p(I).

These finite polynomial identities do not prove the all-degree two-shear
restriction, factorial closure, the unit-row theorem or any recognition/source
theorem, including Wang's classification. In particular, the negative words do
not establish the absence of other compensations. The nonprimitive example is
already a translation, not a cancellation counterexample.
No earlier checker/search internals are imported.
Runtime execution is left to Root.
"""

import unittest

import sympy as sp


class ThreeGoodUnitRowAndTwoShearChecks(unittest.TestCase):
    half = sp.Rational(1, 2)

    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def assert_vector_equal(self, left, right):
        self.assertEqual(len(left), len(right))
        for actual, expected in zip(left, right):
            self.assert_zero(actual-expected)

    @classmethod
    def delta(cls, a, v, u):
        return 3*cls.half*a*v**2+3*cls.half*a**2*v*u+cls.half*a**3*u**2

    def test_actual_nonprimitive_success_and_coordinate_hyperplane(self):
        a, b, v, u = sp.symbols("a b v u")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, original = (a, b, v, u), (X, Y, Z, W)
        frame = sp.Matrix([u, v+a*u, a+b*(v+a*u), b+self.half*u**2])
        inv_b = W-self.half*X**2
        inv_a = Z-inv_b*Y
        inverse = sp.Matrix([inv_a, inv_b, Y-inv_a*X, X])
        self.assert_vector_equal(
            inverse.subs(dict(zip(original, frame)), simultaneous=True), adapted)
        self.assert_vector_equal(
            frame.subs(dict(zip(adapted, inverse)), simultaneous=True), original)
        self.assert_zero(frame.jacobian(adapted).det()+1)

        speeds = sp.Matrix([sp.diff(value, u) for value in frame[:3]])
        self.assert_vector_equal(speeds, (1, a, a*b))
        for value in frame[:3]:
            self.assert_zero(sp.diff(value, u, 2))
        self.assertEqual(speeds[0], 1)
        self.assertEqual(speeds.jacobian((a, b)).rank(), 2)
        self.assert_zero(sp.Matrix.hstack(speeds, speeds.diff(a),
                                         speeds.diff(b)).det()-a)
        q = sp.diff(frame[3], u, 2)
        self.assertEqual(q, 1)
        self.assert_zero(sp.diff(frame[3], u, 3))
        L, F3 = Y, self.half*Y*X**2
        self.assert_zero(sp.gcd(L, F3)-Y)
        self.assert_zero(L.subs({X: 1, Y: a, Z: a*b})*q
                         - 2*F3.subs({X: 1, Y: a, Z: a*b}))
        H = frame[1]*frame[3]-self.half*frame[1]*frame[0]**2
        self.assert_zero(H-b*frame[1])
        self.assert_zero(sp.diff(H, u, 2))
        self.assert_zero(sp.diff(H, u)-sp.diff(frame[2], u))
        self.assert_zero(H-frame[2]+a)
        self.assertNotEqual(a, 0)  # L(speeds)=a is not a complex constant.
        self.assertEqual(sp.diff(a, a), 1)

        # Separate actual coordinate-hyperplane control. For E=partial_u,
        # p=a is invariant and X0=b+au moves, yet (p,X0)=(a,b) is proper.
        X0 = b+a*u
        self.assert_zero(sp.diff(a, u))
        self.assert_zero(sp.diff(X0, u)-a)
        self.assert_zero(X0-b-a*u)
        self.assert_zero(b-X0+a*u)
        self.assertEqual(sp.expand(X0.subs({a: 0, b: 0})), 0)
        self.assertEqual(sp.expand(a.subs({a: 0, b: 0})), 0)
        # The common evaluation annihilates the ideal but sends 1 to 1.
        self.assertEqual(sp.Integer(1).subs({a: 0, b: 0}), 1)
        x0 = sp.symbols("x0")
        self.assert_zero((X0.subs(b, x0-a*u))-x0)
        self.assert_zero((x0-a*u).subs(x0, X0)-b)

    def test_generic_compensated_constant_coefficient_two_shears(self):
        a, b, v, u, T = sp.symbols("a b v u T")
        X, Y, Z, W, A = sp.symbols("X Y Z W A")
        exponents = [(i, j) for total in range(4)
                     for i in range(total+1) for j in [total-i]]
        coefficients = {index: sp.Symbol(f"p{index[0]}{index[1]}")
                        for index in exponents}

        def P(x, y, degree=None):
            return sum(value*x**i*y**j for (i, j), value in coefficients.items()
                       if degree is None or i+j == degree)

        def quotient(old_a, old_v, x):
            # Exact polynomial (P(x,old_v+old_a*x)-P(0,old_v))/x.
            # Its binomial definition is valid at x=0 without localization.
            return sum(value*sp.binomial(j, k)*old_v**(j-k)*old_a**k*x**(i+k-1)
                       for (i, j), value in coefficients.items()
                       for k in range(j+1) if i+k >= 1)

        y = v+a*u
        J = quotient(a, v, u)
        self.assert_zero(u*J-P(u, y)+P(0, v))
        frame = sp.Matrix([u, y, a-self.half*v**3+b*u+P(0, v),
                           b+self.delta(a, v, u)-J])
        self.assert_zero(frame[2]-u*frame[3]+self.half*y**3-a-P(u, y))

        # First middle shear A=a+P(u,Y); the second uses this actual polynomial
        # G(u,Y,A), written in the polynomial coordinates (u,Y,A-P(u,Y)).
        # This expression makes its polynomiality explicit, including u=0.
        def G(x, y0, new_a):
            old_a = sp.expand(new_a-P(x, y0))
            old_v = sp.expand(y0-old_a*x)
            return (self.delta(old_a, old_v, x)-quotient(old_a, old_v, x)
                    - self.delta(new_a, y0-new_a*x, x))

        new_a = a+P(u, y)
        new_b = b+G(u, y, new_a)
        new_v = y-new_a*u
        self.assert_zero(new_b+self.delta(new_a, new_v, u)-frame[3])
        # The divided-difference identity also reconstructs Z, using the same
        # two shears. No Jacobian-only inverse claim is being made.
        self.assert_zero(u*self.delta(A, Y-A*u, u)
                         - self.half*(Y**3-(Y-A*u)**3))
        self.assert_zero(new_a-self.half*y**3+u*frame[3]-frame[2])

        # Endpoint inverse, forward order. Reduce each recovered coordinate
        # before the next substitution so large nested polynomials cancel early.
        inv_a = Z-X*W+self.half*Y**3-P(X, Y)
        recovered_a = sp.expand(inv_a.subs(
            dict(zip((X, Y, Z, W), frame)), simultaneous=True))
        recovered_v = sp.expand(frame[1]-recovered_a*frame[0])
        recovered_b = sp.expand(frame[3]-self.delta(recovered_a, recovered_v, u)
                                + quotient(recovered_a, recovered_v, u))
        self.assert_vector_equal((recovered_a, recovered_b, recovered_v, frame[0]),
                                 (a, b, v, u))

        # Reverse order uses an INDEPENDENT placeholder A for the recovered a.
        # First verify the entire forward map, then impose its polynomial
        # inverse value. This is an exact polynomial substitution, not a field
        # inverse or an assumption that the unknown frame is surjective.
        reverse_v = Y-A*X
        reverse_b = W-self.delta(A, reverse_v, X)+quotient(A, reverse_v, X)
        reverse = frame.subs({a: A, b: reverse_b, v: reverse_v, u: X},
                             simultaneous=True).applyfunc(sp.expand)
        self.assert_vector_equal(reverse,
                                 (X, Y, A+P(X, Y)-self.half*Y**3+X*W, W))
        self.assert_vector_equal(reverse.subs(A, inv_a), (X, Y, Z, W))
        self.assert_zero(frame.jacobian((a, b, v, u)).det()+1)

        speeds = sp.Matrix([sp.diff(value, u) for value in frame[:3]])
        self.assert_vector_equal(speeds, (1, a, b))
        self.assertEqual(sp.Matrix.hstack(speeds, speeds.diff(a),
                                         speeds.diff(b)).det(), 1)
        q = sp.expand(sp.diff(frame[3], u, 2))
        self.assert_zero(q-a**3+2*P(1, a, 3))
        self.assert_zero(sp.diff(frame[3], u, 3))
        self.assert_zero(sp.Poly(q, a).coeff_monomial(a**3)
                         - 1+2*coefficients[(0, 3)])
        # Every complex specialization p03 != 1/2 has a nonzero cubic term;
        # the six products of (1,a,b) have zero a^3 coefficient. This coefficient
        # certificate does not claim that the exceptional specialization is
        # still primitive or nonremovable.
        products = [speeds[i]*speeds[j] for i in range(3) for j in range(i, 3)]
        for value in products:
            self.assertEqual(sp.Poly(value, a, b).coeff_monomial(a**3), 0)
        F3 = self.half*Y**3-P(X, Y, 3)
        self.assert_zero(F3.subs(X, 0)
                         - (self.half-coefficients[(0, 3)])*Y**3)
        H = sp.expand(frame[0]*frame[3]-F3.subs({X: frame[0], Y: frame[1]},
                                                               simultaneous=True))
        self.assert_zero(H-frame[2]+a+P(u, y, 2)+P(u, y, 1)+P(0, 0))
        self.assert_zero(sp.diff(H, u, 2)+2*P(1, a, 2))
        self.assert_zero(sp.diff(H+P(u, y, 2), u)-b+P(1, a, 1))
        self.assert_zero(H+P(u, y, 2)-frame[2]+P(u, y, 1)+P(0, 0)+a)
        # Explicit denominator absorption and constant P0, not R0(b).
        self.assert_zero(sp.diff(P(0, 0), b))
        self.assert_zero((u*J).subs(u, 0))

    def test_four_b_dependent_actual_words_fail_the_good_profile(self):
        a, b, v, u = sp.symbols("a b v u")
        X, Y, Z, W, A, B = sp.symbols("X Y Z W A B")
        for j in (0, 1, 2, 3):
            with self.subTest(first_shear_degree=j):
                y = v+a*u
                # R=b*u^j and G=0 are actual middle shears for every j.
                new_a = a+b*u**j
                new_v = y-new_a*u
                w = sp.expand(b+self.delta(new_a, new_v, u))
                z = sp.expand(new_a-self.half*y**3+u*w)
                frame = (u, y, z, w)
                recovered_A = sp.expand(z-u*w+self.half*y**3)
                recovered_B = sp.expand(w-self.delta(recovered_A,
                                                     y-recovered_A*u, u))
                recovered_a = sp.expand(recovered_A-recovered_B*u**j)
                recovered_v = sp.expand(y-recovered_a*u)
                self.assert_vector_equal((recovered_a, recovered_B, recovered_v, u),
                                         (a, b, v, u))

                # Reverse inverse order, with independent middle coordinates.
                a0, v0 = A-B*X**j, Y-(A-B*X**j)*X
                reverse = [sp.expand(value.subs({a: a0, b: B, v: v0, u: X},
                                                simultaneous=True)) for value in frame]
                middle_W = B+self.delta(A, Y-A*X, X)
                self.assert_vector_equal(reverse,
                                         (X, Y, A-self.half*Y**3+X*middle_W, middle_W))
                inv_A = Z-X*W+self.half*Y**3
                inv_B_at_A = W-self.delta(A, Y-A*X, X)
                reverse = [sp.expand(value.subs(B, inv_B_at_A)) for value in reverse]
                self.assert_vector_equal(reverse, (X, Y, A-self.half*Y**3+X*W, W))
                self.assert_vector_equal([value.subs(A, inv_A) for value in reverse],
                                         (X, Y, Z, W))

                # These particular words do NOT meet the theorem premises:
                # j=0 retains quadratic W but Z is cubic; j>0 has even larger
                # degrees. This is not a search for all possible second G.
                expected_W_degree = 2 if j == 0 else 3*j+2
                self.assertEqual(sp.Poly(w, u).degree(), expected_W_degree)
                self.assertEqual(sp.Poly(z, u).degree(), expected_W_degree+1)
                self.assertNotEqual(sp.expand(sp.diff(z, u, 2)), 0)
                if j:
                    self.assert_zero(sp.Poly(w, u).coeff_monomial(u**expected_W_degree)
                                     - self.half*b**3)
                    self.assertNotEqual(sp.expand(sp.diff(w, u, 3)), 0)
                else:
                    self.assert_zero(sp.diff(w, u, 2)-a**3-b**3)
                    self.assert_zero(sp.Poly(z, u).coeff_monomial(u**3)-self.half*b**3)
                    self.assert_zero(sp.diff(w, u, 3))

    def test_explicit_constant_speed_normal_form_and_kernel_coordinates(self):
        I, x, v, j = sp.symbols("I x v j")
        X, Y, Z, W, K, t = sp.symbols("X Y Z W K t")
        c, gamma, delta = sp.symbols("c gamma delta", nonzero=True)
        beta, alpha, epsilon = sp.symbols("beta alpha epsilon")
        eta0, eta1, eta2 = sp.symbols("eta0 eta1 eta2")

        def eta(value):
            return eta0+eta1*value+eta2*value**2

        def F(value):
            return gamma*value**3+beta*value**2+alpha*value+epsilon

        Fprime = sp.diff(F(t), t)
        e = eta(I)
        y = v+e*x
        w = j+e**2*(3*gamma*v+beta)*x+gamma*e**3*x**2
        z = (x*w-F(y)-I)/delta
        frame = sp.Matrix([x, y, z, w])
        self.assert_zero(delta*z-x*(j-e*Fprime.subs(t, v))+F(v)+I)
        self.assert_zero(sp.diff(e, I)-eta1-2*eta2*I)

        # The inverse uses only polynomials and division by the fixed nonzero
        # COMPLEX delta already in the forward formula. eta is evaluated on the
        # recovered invariant, not on an independently chosen coefficient.
        inv_I = X*W-F(Y)-delta*Z
        recovered_I = sp.expand(inv_I.subs(
            dict(zip((X, Y, Z, W), frame)), simultaneous=True))
        recovered_v = sp.expand(y-eta(recovered_I)*x)
        recovered_j = sp.expand(w-eta(recovered_I)**2*(3*gamma*recovered_v+beta)*x
                                - gamma*eta(recovered_I)**3*x**2)
        self.assert_vector_equal((recovered_I, x, recovered_v, recovered_j),
                                 (I, x, v, j))

        # Reverse order first treats K as an independent prospective invariant.
        # Simplifying before substituting K=inv_I avoids huge nested eta powers.
        inverse_v_at_K = Y-eta(K)*X
        inverse_j_at_K = (W-eta(K)**2*(3*gamma*inverse_v_at_K+beta)*X
                          - gamma*eta(K)**3*X**2)
        reverse = frame.subs({I: K, x: X, v: inverse_v_at_K, j: inverse_j_at_K},
                             simultaneous=True).applyfunc(sp.expand)
        self.assert_vector_equal(reverse, (X, Y, (X*W-F(Y)-K)/delta, W))
        self.assert_vector_equal(reverse.subs(K, inv_I), (X, Y, Z, W))

        # E=c*partial_x in the independently specified polynomial coordinates
        # (I,x,v,j). These are family identities, not a classification argument.
        act = lambda value: sp.expand(c*sp.diff(value, x))
        speeds = sp.Matrix([act(value) for value in frame[:3]])
        expected_r = c*(j-e*Fprime.subs(t, v))/delta
        self.assert_vector_equal(speeds, (c, c*e, expected_r))
        for value in frame[:3]:
            self.assert_zero(act(act(value)))
        self.assert_zero(act(w)-c*e**2*(3*gamma*v+beta)-2*c*gamma*e**3*x)
        q = act(act(w))
        self.assert_zero(q-2*c**2*gamma*e**3)
        self.assert_zero(act(q))
        self.assert_zero(speeds[0]*q-2*gamma*speeds[1]**3)
        self.assert_zero(delta*speeds[2]-speeds[0]*w-x*act(w)
                         + Fprime.subs(t, y)*speeds[1])
        self.assertEqual(sp.Poly(sp.expand(w), x).degree(), 2)
        self.assertEqual(sp.Poly(sp.expand(z), x).degree(), 1)
        self.assert_zero(act(x/c)-1)

        # The three recovered kernel coordinates are independently actual
        # coordinates by the two inverse orders. Differentiation kills them;
        # the usual coefficient argument for partial_x then gives C[I,v,j].
        # The finite test checks the displayed derivatives/completion only.
        for value in (I, v, j):
            self.assert_zero(act(value))
        self.assert_zero(act(inv_I.subs(dict(zip((X, Y, Z, W), frame)),
                                        simultaneous=True)))
        self.assert_zero(frame.jacobian((I, x, v, j)).det()+1/delta)

    def test_irreducible_normalized_action_with_fixed_points(self):
        I, x, y, w = sp.symbols("I x y w")
        X, Y, Z, W = sp.symbols("X Y Z W")
        adapted, original = (I, x, y, w), (X, Y, Z, W)
        z = x*w-self.half*y**3-I
        frame = sp.Matrix([x, y, z, w])
        inverse = sp.Matrix([X*W-self.half*Y**3-Z, X, Y, W])
        self.assert_vector_equal(
            inverse.subs(dict(zip(original, frame)), simultaneous=True), adapted)
        self.assert_vector_equal(
            frame.subs(dict(zip(adapted, inverse)), simultaneous=True), original)
        self.assert_zero(frame.jacobian(adapted).det()+1)

        coefficients = sp.Matrix([0, I**3, I**2, (3*I*y-x)/2])

        def act(value):
            return sp.expand(sum(coefficient*sp.diff(value, variable)
                                 for coefficient, variable in zip(coefficients, adapted)))

        self.assert_zero(act(I))
        self.assert_zero(act(x)-I**3)
        self.assert_zero(act(y)-I**2)
        self.assert_zero(act(w)-(3*I*y-x)/2)
        self.assert_zero(act(act(x)))
        self.assert_zero(act(act(y)))
        self.assert_zero(act(act(w))-I**3)
        self.assert_zero(act(act(act(w))))
        self.assert_zero(act(z)-I**3*w-x*(3*I*y-x)/2
                         + 3*self.half*I**2*y**2)
        self.assert_zero(act(act(z)))
        self.assert_zero(act(frame[0]*frame[3]-self.half*frame[1]**3-frame[2]))
        self.assert_zero(act(x)*act(act(w))-act(y)**3)
        # The defining triangular coefficient dependencies and these bounds
        # exhibit local nilpotence; no localized derivation is substituted.

        # In the actual coordinate ring, the coefficient gcd is one, even
        # though their generated ideal is proper. This distinguishes
        # irreducibility from fixed-point freeness and the existence of a slice.
        self.assertEqual(sp.gcd(sp.gcd(I**3, I**2), 3*I*y-x), 1)
        for coefficient in coefficients:
            self.assert_zero(coefficient.subs({I: 0, x: 0}, simultaneous=True))
        for value in frame:
            self.assert_zero(act(value).subs({I: 0, x: 0}, simultaneous=True))
        self.assertEqual(sp.Integer(1).subs({I: 0, x: 0}), 1)

        # Reduced set only: DX=I^3=0 forces I=0 over C, and then
        # DW=-x/2=0 forces x=0. Every coefficient vanishes there.
        # We deliberately do NOT identify the image ideal with (I,x).
        self.assert_zero(coefficients[3].subs(I, 0)+x/2)
        self.assertNotEqual(I**3, 0)

    def test_dense_normal_form_selected_bad_partial_and_intrinsic_top(self):
        I, V, R, u, t = sp.symbols("I V R u t")
        c, delta, gamma = sp.symbols("c delta gamma", nonzero=True)
        beta, alpha, epsilon, p0, p1, p2 = sp.symbols(
            "beta alpha epsilon p0 p1 p2")
        variables = (I, V, R, u)
        p = p0+p1*I+p2*I**2
        prime = sp.diff(p, I)

        def F(value):
            return gamma*value**3+beta*value**2+alpha*value+epsilon

        Fprime = sp.diff(F(t), t).subs(t, V)
        divided = (gamma*(3*V**2*p+3*V*p**2*u+p**3*u**2)
                   + beta*(2*V*p+p**2*u)+alpha*p)
        self.assert_zero(u*divided-F(V+p*u)+F(V))
        frame = sp.Matrix([c*u, V+p*u, -(I+F(V))/delta+R*u,
                           (delta*R+divided)/c])
        self.assert_zero(frame[0]*frame[3]-F(frame[1])-delta*frame[2]-I)
        self.assert_vector_equal([sp.diff(value, u) for value in frame[:3]],
                                 (c, p, R))

        # Differentiate the explicit original coordinates against these
        # proposed pulled-back coefficients, instead of importing a previous
        # solver or assuming the partial's formula as its own test target.
        partial = sp.Matrix([c*u, -c*prime*u**2,
                             c/delta-c*prime*Fprime*u/delta, 0])

        def act(field, value):
            return sp.expand(sum(coefficient*sp.diff(value, variable)
                                 for coefficient, variable in zip(field, variables)))

        self.assert_vector_equal([act(partial, value) for value in frame],
                                 (0, 0, 0, 1))
        self.assert_vector_equal(frame.jacobian(variables)*partial, (0, 0, 0, 1))
        self.assert_zero(partial[3])
        self.assertEqual(max(sp.Poly(value, u).degree() for value in partial[:3]), 2)
        # T(u)=0, so no vertical coefficient contributes to its filtered shift.
        top = sp.Matrix([sp.Poly(value, u).coeff_monomial(u**2)
                         for value in partial[:3]]+[0])
        self.assert_vector_equal(top, (0, -c*prime, 0, 0))
        self.assertNotEqual(sp.expand(-c*prime), 0)
        self.assert_vector_equal([sp.diff(value, u, 2)/2 for value in partial], top)
        self.assert_vector_equal([sp.diff(value, u, 3) for value in partial],
                                 (0, 0, 0, 0))
        for value in (I, R, p, sp.diff(frame[3], u, 2)):
            self.assert_zero(act(top, value))
        self.assert_zero(act(top, V)+c*prime)
        # On the known polynomial kernel C[I,V,R], the nonzero intrinsic top
        # is -c*p'(I)*partial_V. Its kernel is C[I,R] by coefficient comparison
        # in V in a domain, not by inverting p'. This finite method checks the
        # displayed coefficients; it does not certify the classification or a
        # universal kernel presentation for an arbitrary supplied frame.


if __name__ == "__main__":
    unittest.main(verbosity=2)
