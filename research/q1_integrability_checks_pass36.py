"""Independent bounded exact checks for q1-integrability-pass36.md.

Only unittest and SymPy are imported. Finite examples do not certify
the universal recognition theorem or the unknown-cylinder premise.
"""
import unittest
import sympy as sp

x, lam, b, c, h, w, z, T, eps, s = sp.symbols(
    "x lam b c h w z T eps s"
)


def expand(value):
    return sp.expand(value)


def rem(value, modulus, variable=x):
    return sp.rem(expand(value), modulus, variable)


def substitute(value, mapping):
    return expand(value.subs(mapping, simultaneous=True))


def act(field, coordinates, value):
    return expand(sum(a*sp.diff(value, q)
                      for a, q in zip(field, coordinates)))


def quotient(value, divisor, variable=x):
    result, remainder = sp.div(expand(value), divisor, variable)
    if expand(remainder) != 0:
        raise AssertionError("The proposed polynomial quotient has a remainder")
    return expand(result)


def even(value, variable=b):
    return expand((value + value.subs(variable, -variable))/2)


class Q1IntegrabilityChecks(unittest.TestCase):
    def test_generic_correction_identity_and_modulus(self):
        p = x + 2
        potential = p*b + h
        g = x*p*(T + 1)
        primitive = sp.integrate(g, (T, 0, T))
        invariant = h + lam*primitive.subs(T, potential)
        correction = T**2 + lam*T + 1
        numerator = potential - invariant + lam*correction.subs(T, invariant)
        field = (x**2*(1 + lam*g.subs(T, potential)),
                 -lam*x**2*p*g.subs(T, potential))
        self.assertEqual(act(field, (b, h), invariant), 0)
        self.assertEqual(sp.cancel(act(field, (b, h), numerator)/p), x**2)
        extra = T + lam
        changed = correction + p*x**2*extra
        difference = lam*(changed - correction).subs(T, invariant)/p
        self.assertEqual(sp.cancel(difference
                                   - lam*x**2*extra.subs(T, invariant)), 0)
        self.assertEqual(rem(difference, x**2), 0)

    def test_finite_nilpotent_inverse_and_divisor_correction(self):
        # A genuine repeated-root ring, with nonzero first nilpotent order.
        phi = T + lam*eps*T**2/2
        psi = T - lam*eps*T**2/2 + lam**2*eps**2*T**3/2
        self.assertEqual(rem(substitute(phi, {T: psi}) - T, eps**3, eps), 0)
        self.assertEqual(rem(substitute(psi, {T: phi}) - T, eps**3, eps), 0)
        iterate = T
        error = phi - T
        for _ in range(3):
            iterate = rem(T - error.subs(T, iterate), eps**3, eps)
        self.assertEqual(expand(iterate - psi), 0)
        correction = quotient(T - psi, lam, lam)
        potential = eps**3*b + h
        invariant = h + lam*eps*potential**2/2
        numerator = potential - invariant + lam*correction.subs(T, invariant)
        self.assertEqual(rem(numerator, eps**3, eps), 0)
        self.assertNotEqual(rem(eps, eps**3, eps), 0)

    def test_crt_constructs_a_repeated_root_realization(self):
        p = (x - 1)**3
        g = sp.Rational(2, 3)*x*(1 - x)
        potential = p*b + h
        invariant = h + lam*g*potential
        at_p = T*(g - lam*g**2)
        at_x = x*(2*T - 1)/3
        # p*(-1-3x) is zero modulo p and one modulo x².
        projector = expand(p*(-1 - 3*x))
        self.assertEqual(rem(projector, p), 0)
        self.assertEqual(rem(projector - 1, x**2), 0)
        correction = rem(at_p*(1 - projector) + at_x*projector, p*x**2)
        self.assertEqual(rem(correction - at_p, p), 0)
        self.assertEqual(rem(correction - at_x, x**2), 0)
        numerator = potential - invariant + lam*correction.subs(T, invariant)
        first = quotient(numerator, p)
        physical_h = x**2*c - b**2
        W = substitute(first, {h: physical_h})
        K = substitute(invariant, {h: physical_h})
        self.assertEqual(rem(K + (1 + lam*x)**2*W**2, x**2), 0)
        Z = quotient(K + (1 + lam*x)**2*W**2, x**2)
        self.assertEqual(W.subs(lam, 0), b)
        self.assertEqual(Z.subs(lam, 0), c)

        # First and invariant coordinates are affine-linear in (b,h);
        # verify the actual full matrix determinant, not just its residue.
        matrix = sp.Matrix([[sp.diff(first, b), sp.diff(first, h)],
                            [sp.diff(invariant, b), sp.diff(invariant, h)]])
        self.assertEqual(expand(matrix.det()), 1)
        shift = first.subs({b: 0, h: 0})
        inverse_b = expand(matrix[1, 1]*(w - shift) - matrix[0, 1]*z)
        inverse_h = expand(-matrix[1, 0]*(w - shift) + matrix[0, 0]*z)
        self.assertEqual(substitute(inverse_b, {w: first, z: invariant}), b)
        self.assertEqual(substitute(inverse_h, {w: first, z: invariant}), h)

    def test_general_first_jet_including_nonzero_speed(self):
        p0, p1 = sp.Integer(2), sp.Integer(5)
        for gamma, q0 in ((sp.Integer(0), T**2 + T),
                          (sp.Integer(2), sp.Integer(3))):
            q1 = T**2 + T
            g1 = T**3 + 2*T
            G1 = sp.integrate(g1, (T, 0, T))
            alpha = -gamma*p0/2
            F0 = p0*b + q0.subs(T, -b**2)
            F1 = p1*b + q1.subs(T, -b**2)
            s_actual = b + alpha*lam
            k0 = alpha**2*lam**2 + lam*gamma*q0.subs(T, 0)
            K0 = k0 - s_actual**2
            J = G1.subs(T, F0) + gamma*F1
            divided_q = quotient(q1.subs(T, -b**2) - q1.subs(T, K0),
                                  lam, lam)
            E = expand((p0 - 2*s_actual*sp.diff(q0, T).subs(T, K0))*J
                       + 2*s_actual*(divided_q - p1*alpha)
                       + 2*p0*s_actual**2)
            U1 = lam + T**2

            # Reconstruct the jets from the original formulas, without
            # using the claimed W1 or E expression.
            potential = F0 + x*F1
            G = gamma*T + x*G1
            invariant = rem(-b**2 + lam*G.subs(T, potential), x**2)
            Q = q0 + x*q1
            U = p0*alpha + x*U1
            numerator = rem(potential - Q.subs(T, invariant)
                            + lam*U.subs(T, invariant), x**2)
            inverse_p = 1/p0 - x*p1/p0**2
            W = rem(numerator*inverse_p, x**2)
            computed = rem(invariant + (1 + lam*x)**2*W**2, x**2)
            expected = k0 + x*lam*(E + 2*s_actual*U1.subs(T, K0))/p0
            self.assertEqual(expand(computed - expected), 0)

    def test_all_degree_parity_controls(self):
        for qdegree in range(1, 5):
            F0 = 2*b + 3*(-b**2)**qdegree
            for hdegree in range(2, 6):
                composition = F0**hdegree + F0
                odd_part = expand((composition - composition.subs(b, -b))/2)
                self.assertEqual(sp.Poly(odd_part, b).degree(),
                                 2*qdegree*(hdegree - 1) + 1)
                expected = hdegree*2*(3*(-1)**qdegree)**(hdegree - 1)
                power = 2*qdegree*(hdegree - 1) + 1
                self.assertEqual(odd_part.coeff(b, power), expected)

        p0, q0, q1 = sp.Integer(2), sp.Integer(3), sp.Integer(5)
        F0 = p0*b + q0 - q1*b**2
        G1 = 2*T/(3*q1)
        E = G1.subs(T, F0)*sp.diff(F0, b) + 2*p0*b**2
        self.assertEqual(sp.diff(even(E), b), 0)
        # Constant-Q branch: high even terms in g1 are genuinely allowed.
        shifted = T - q0
        g1 = shifted**6 + 2*shifted**2 + 1 - 4*shifted/p0**2
        G1 = sp.integrate(g1, (T, 0, T))
        E = p0*G1.subs(T, p0*b + q0) + 2*p0*b**2
        self.assertEqual(sp.diff(even(E), b), 0)
        bad_G1 = sp.integrate(g1 + shifted**3, (T, 0, T))
        bad_E = p0*bad_G1.subs(T, p0*b + q0) + 2*p0*b**2
        self.assertNotEqual(sp.diff(even(bad_E), b), 0)

    def test_explicit_constant_p_realization_and_physical_inverse(self):
        time = sp.Rational(2, 3)*lam*x
        potential = b + h
        invariant = h + time*potential
        first = (1 - time + time**2)*b + time**2*h - time/2
        matrix = sp.Matrix([[1 - time + time**2, time**2],
                            [time, 1 + time]])
        self.assertEqual(expand(matrix.det()), 1)
        inv_b = (1 + time)*(w + time/2) - time**2*z
        inv_h = -time*(w + time/2) + (1 - time + time**2)*z
        self.assertEqual(substitute(inv_b, {w: first, z: invariant}), b)
        self.assertEqual(substitute(inv_h, {w: first, z: invariant}), h)
        self.assertEqual(substitute(first, {b: inv_b, h: inv_h}), w)
        self.assertEqual(substitute(invariant, {b: inv_b, h: inv_h}), z)

        W = substitute(first, {h: x**2*c - b**2})
        K = substitute(invariant, {h: x**2*c - b**2})
        Z = quotient(K + (1 + lam*x)**2*W**2, x**2)
        original_invariant = x**2*z - (1 + lam*x)**2*w**2
        physical_b = substitute(inv_b, {z: original_invariant})
        physical_h = substitute(inv_h, {z: original_invariant})
        physical_c = quotient(physical_h + physical_b**2, x**2)
        self.assertEqual(physical_b.subs(lam, 0), w)
        self.assertEqual(physical_c.subs(lam, 0), z)
        field = (x**2*(1 + time), 2*b + time*(2*b - 1))
        self.assertEqual(act(field, (b, c), W), x**2)
        self.assertEqual(act(field, (b, c), K), 0)
        self.assertEqual(expand(act(field, (b, c), Z)
                                - 2*(1 + lam*x)**2*W), 0)

    def test_exact_common_slice_but_nonsliced_primitive_top(self):
        potential = x**2*c - b**2 + b
        top = (sp.diff(potential, c), -sp.diff(potential, b))
        self.assertEqual(top, (x**2, 2*b - 1))
        self.assertEqual(sp.gcd(*top), 1)
        self.assertEqual(act(top, (b, c), potential), 0)
        pencil = (x**2 + sp.Rational(2, 3)*lam*x*top[0],
                  2*b + sp.Rational(2, 3)*lam*x*top[1])
        self.assertEqual(act(pencil, (b, c), potential), x**2)
        fixed_line = {x: 0, b: sp.Rational(1, 2)}
        self.assertEqual(tuple(value.subs(fixed_line) for value in top), (0, 0))
        self.assertEqual(tuple(sp.diff(potential, q).subs(fixed_line)
                               for q in (x, b, c)), (0, 0, 0))

    def test_distinct_exact_integrability_failures(self):
        # Off-boundary obstruction, although the zero-speed parity test
        # for Q0=T and g1=2/3 passes.
        p = x - 1
        potential = p*b + h
        g = sp.Rational(2, 3)*x
        field = (x**2*(1 + lam*g), -lam*x**2*p*g)
        self.assertEqual(tuple(value.subs({x: 1, lam: -sp.Rational(3, 2)})
                               for value in field), (0, 0))
        # Pure first-jet obstruction with no other p-divisor.
        F0 = b + b**4
        E = F0*sp.diff(F0, b) + 2*b**2
        self.assertNotEqual(sp.diff(even(E), b), 0)
        # Zeroth-order speed obstruction: g0=1, Q0=T is forbidden.
        F0 = b - b**2
        self.assertEqual(sp.Poly(F0, b).degree(), 2)
        self.assertNotEqual(sp.diff(F0, b, 2), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

