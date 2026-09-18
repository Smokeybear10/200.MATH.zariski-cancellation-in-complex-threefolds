"""Exact identities supporting research-note.md, NOT a cancellation solver.

No floating-point sampling or solver-discovery code is used. General claims
still require the written proofs and any explicitly cited external theorem.
"""

import json
import sys
import unittest

import sympy as sp


x, y, z, w = sp.symbols("x y z w")
s, u, v, h = sp.symbols("s u v h")
SOURCE = (x, y, z, w)
TARGET = (s, u, v, h)


def compose(expressions, old, new):
    return tuple(sp.expand(f.subs(dict(zip(old, new)), simultaneous=True))
                 for f in expressions)


def inverse_residuals(forward, inverse, source=SOURCE, target=TARGET):
    """Both compositions, not just a Jacobian or one-sided inverse."""
    return (tuple(a - b for a, b in zip(compose(forward, source, inverse), target))
            + tuple(a - b for a, b in zip(compose(inverse, target, forward), source)))


def derivation(f, images, variables=SOURCE):
    return sp.expand(sum(sp.diff(f, q) * dq for q, dq in zip(variables, images)))


def slice_projection(f, slice_polynomial, images, max_steps=32):
    """Finite Taylor projection; refuses to assume unverified termination."""
    if derivation(slice_polynomial, images) != 1:
        raise ValueError("The supplied polynomial does not satisfy D(s)=1")
    answer = sp.Integer(0)
    derivative = sp.sympify(f)
    for degree in range(max_steps):
        if derivative == 0:
            return sp.expand(answer)
        answer += (-slice_polynomial)**degree * derivative / sp.factorial(degree)
        derivative = derivation(derivative, images)
    raise ValueError("Local nilpotence not verified within the supplied bound")


class ExactIdentityTests(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_generic_bezout_matrix(self):
        a, b, c, r, q = sp.symbols("a b c r q")
        F = a*z + b*w + c
        G = -q*z + r*w
        determinant = a*r + b*q
        self.assert_zero(r*(F-c)-b*G-determinant*z)
        self.assert_zero(q*(F-c)+a*G-determinant*w)
        self.assert_zero(a*(r*(s-c)-b*u)+b*(q*(s-c)+a*u)+c
                         - (determinant*(s-c)+c))
        self.assert_zero(-q*(r*(s-c)-b*u)+r*(q*(s-c)+a*u)
                         - determinant*u)

    def test_nonlinear_bezout_example_both_compositions(self):
        # a=x, b=1-xy, r=y, q=1, c=x²+y³.
        F = x*z+(1-x*y)*w+x*x+y**3
        G = -z+y*w
        forward = (x, y, F, G)
        target = sp.symbols("X Y S G")
        X, Y, S, Gnew = target
        inverse = (X, Y, Y*(S-X*X-Y**3)-(1-X*Y)*Gnew,
                   S-X*X-Y**3+X*Gnew)
        for residual in inverse_residuals(forward, inverse, target=target):
            self.assert_zero(residual)

    def test_bezout_wrong_inverse_is_rejected(self):
        forward = (x, y, x*z+(1-x*y)*w+x*x+y**3, -z+y*w)
        X, Y, S, G = sp.symbols("X Y S G")
        bad = (X, Y, Y*(S-X*X-Y**3)+(1-X*Y)*G,
               S-X*X-Y**3+X*G)
        self.assertTrue(any(sp.expand(r) != 0 for r in
                            inverse_residuals(forward, bad, target=(X,Y,S,G))))

    def test_coprime_does_not_mean_unit_ideal(self):
        self.assertEqual(sp.gcd(x, y), 1)
        basis = sp.groebner([x, y], x, y)
        self.assertEqual(basis.reduce(sp.Integer(1))[1], 1)
        self.assertEqual((x*z+y*w).subs({x:0,y:0,z:0,w:0}), 0)

    def test_affine_chain_is_nilpotent_on_generators(self):
        images = (sp.Integer(1), x, y, z)
        for variable in SOURCE:
            derivative = variable
            for _ in range(5):
                derivative = derivation(derivative, images)
            self.assert_zero(derivative)

    def test_affine_chain_invariants(self):
        images = (sp.Integer(1), x, y, z)
        invariants = (y-x*x/2, z-x*y+x**3/3,
                      w-x*z+x*x*y/2-x**4/8)
        self.assertEqual(derivation(x, images), 1)
        for invariant in invariants:
            self.assert_zero(derivation(invariant, images))

    def test_affine_chain_inverse_both_compositions(self):
        forward = (x, y-x*x/2, z-x*y+x**3/3,
                   w-x*z+x*x*y/2-x**4/8)
        inverse = (s, u+s*s/2, v+s*u+s**3/6,
                   h+s*v+s*s*u/2+s**4/24)
        for residual in inverse_residuals(forward, inverse):
            self.assert_zero(residual)

    def test_affine_chain_wrong_inverse_is_rejected(self):
        forward = (x, y-x*x/2, z-x*y+x**3/3,
                   w-x*z+x*x*y/2-x**4/8)
        bad = (s, u+s*s/2, v+s*u+s**3/6, h+s*v+s*s*u/2)
        self.assertTrue(any(sp.expand(r) != 0 for r in inverse_residuals(forward, bad)))

    def test_flow_group_law(self):
        t, r = sp.symbols("t r")
        def flow(time):
            return (x+time, y+time*x+time**2/2,
                    z+time*y+time**2*x/2+time**3/6,
                    w+time*z+time**2*y/2+time**3*x/6+time**4/24)
        composed = compose(flow(t), SOURCE, flow(r))
        for actual, expected in zip(composed, flow(t+r)):
            self.assert_zero(actual-expected)

    def test_projection_matches_inverse_coordinates(self):
        images = (sp.Integer(1), x, y, z)
        expected = (0, y-x*x/2, z-x*y+x**3/3,
                    w-x*z+x*x*y/2-x**4/8)
        for variable, target in zip(SOURCE, expected):
            self.assert_zero(slice_projection(variable, x, images)-target)

    def test_projection_multiplicativity_on_explicit_polynomials(self):
        images = (sp.Integer(1), x, y, z)
        f = x*z+y*y
        g = w+y*z
        self.assert_zero(slice_projection(f*g, x, images)
                         - slice_projection(f, x, images)*slice_projection(g, x, images))

    def test_projection_refuses_nonterminating_derivation(self):
        # D(x)=1, D(y)=y has a slice but is not locally nilpotent.
        with self.assertRaises(ValueError):
            slice_projection(y, x, (sp.Integer(1), y, sp.Integer(0), sp.Integer(0)),
                             max_steps=5)

    def test_projection_rejects_invalid_slice(self):
        with self.assertRaises(ValueError):
            slice_projection(z, y, (sp.Integer(1), x, y, z))

    def test_coordinate_projection_can_be_noncoordinate(self):
        images = (sp.Integer(1), 2*x, sp.Integer(0), sp.Integer(0))
        g = y-x*x
        chosen_slice = x-g*g-g
        self.assert_zero(derivation(g, images))
        self.assertEqual(derivation(chosen_slice, images), 1)
        px = slice_projection(x, chosen_slice, images)
        py = slice_projection(y, chosen_slice, images)
        self.assert_zero(px-g*(g+1))
        self.assert_zero(py-g*(g**3+2*g*g+g+1))
        self.assert_zero(py-px*px-g)
        # Non-coordinate conclusions use the written reducible-fiber argument.

    def test_characteristic_two_parameters_and_smoothness(self):
        p, m, e, coefficient = 2, 2, 2, 3
        self.assertGreater(m, 1)
        self.assertNotEqual((coefficient*p) % (p**e), 0)
        self.assertNotEqual((p**e) % (coefficient*p), 0)
        f = x*x*y+z**4+w+w**6
        partial = sp.Poly(sp.diff(f, w), *SOURCE, modulus=2)
        self.assertEqual(partial.as_expr(), 1)
        # Neither stable polynomiality nor non-polynomiality is proved here.

    def test_characteristic_two_derivative_trap(self):
        self.assertEqual(sp.Poly(sp.diff(w*w,w), w, modulus=2).as_expr(), 0)
        self.assertEqual(sp.Poly(sp.diff(w,w), w, modulus=2).as_expr(), 1)
        self.assertEqual(sp.Poly(w*w,w,modulus=2).degree(), 2)

    def test_affine_linear_slice_linear_algebra(self):
        N = sp.Matrix([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
        b = sp.Matrix([1,0,0,0])
        ell = sp.Matrix([[1,0,0,0]])
        self.assertEqual(N**4, sp.zeros(4))
        self.assertEqual(N.row_join(b).rank(), N.rank()+1)
        self.assertEqual(ell*N, sp.zeros(1,4))
        self.assertEqual(ell*b, sp.Matrix([1]))
        b_no_slice = sp.Matrix([0,1,0,0])
        self.assertEqual(N.row_join(b_no_slice).rank(), N.rank())
        point = sp.Matrix([-1,0,0,0])
        self.assertEqual(N*point+b_no_slice, sp.zeros(4,1))

    def test_slice_lost_in_deformation(self):
        epsilon = sp.symbols("epsilon")
        images = (epsilon, x, y, z)
        # This identity is over Q(epsilon); epsilon=0 is excluded.
        self.assertEqual(derivation(x/epsilon, images), 1)
        for variable in SOURCE:
            derivative = variable
            for _ in range(5):
                derivative = derivation(derivative, images)
            self.assert_zero(derivative)
        specialized = tuple(value.subs(epsilon, 0) for value in images)
        self.assertEqual(specialized, (0, x, y, z))
        self.assertEqual(tuple(value.subs(dict.fromkeys(SOURCE,0)) for value in specialized),
                         (0,0,0,0))
        self.assertEqual(derivation(x, specialized), 0)

    def test_highest_degree_derivation_loses_slice(self):
        images = (sp.Integer(1), x, y, z)
        # The top standard-degree derivation has degree 0. The translation
        # term has derivation degree -1 and is discarded.
        top_images = tuple(sp.Add(*(term for term in sp.Add.make_args(value)
                                  if sp.Poly(term, *SOURCE).total_degree() == 1))
                           for value in images)
        self.assertEqual(top_images, (0, x, y, z))
        self.assertEqual(derivation(x, images), 1)
        self.assertEqual(derivation(x, top_images), 0)


if __name__ == "__main__":
    if sys.flags.optimize:
        raise SystemExit("Run without -O: this companion preserves standard verification settings.")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ExactIdentityTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({
        "tests_run": result.testsRun,
        "successful": result.wasSuccessful(),
        "arithmetic": "exact rational polynomial identities and characteristic-2 reductions",
        "scope": "explicit examples and algebraic identities only",
        "full_cancellation_conjecture_verified": False,
        "gupta_nonpolynomiality_independently_verified": False,
        "lean_formalization": False,
        "sympy_version": sp.__version__,
    }, indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)
