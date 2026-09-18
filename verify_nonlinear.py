"""Exact identity checks for the fourth cancellation research pass.

Standard-library arithmetic only. This imports the independently implemented
polynomial arithmetic, not a symbolic solver. Tests do not formalize the
all-degree geometric proofs or settle cancellation.
"""

from fractions import Fraction as Q
from math import factorial
import json
import unittest

from verify_extension import Poly, V, DX, DY, DZ, f, g, r, endpoint


def derivative(poly, images):
    return sum((poly.diff(i)*value for i, value in enumerate(images)), Poly())


def quotient_reduce(poly, multiplicity):
    """Normal form using x**multiplicity*y=z**2-1, with no division."""
    answer = Poly()
    x, y, z = V[:3]
    for powers, coefficient in poly.terms.items():
        count = min(powers[0]//multiplicity, powers[1])
        reduced = list(powers)
        reduced[0] -= multiplicity*count
        reduced[1] -= count
        answer += Poly({tuple(reduced): coefficient})*(z*z-1)**count
    return answer


class NonlinearChecks(unittest.TestCase):
    def test_replica_slice(self):
        b, r, w = V[:3]
        h = Q(1, 2)*r*r-b*w
        s = w+r*h+Q(1, 2)*b*h*h
        images = (0, b*b, 1+b*r)
        self.assertEqual(derivative(h, images), -b)
        self.assertEqual(derivative(s, images), 1)
        self.assertNotEqual(derivative(w+r*h, images), 1)

    def test_replica_invariant_and_inverse(self):
        b, r, w = V[:3]
        h = Q(1, 2)*r*r-b*w
        v = r+b*h
        s = w+r*h+Q(1, 2)*b*h*h
        hp = b*s-Q(1, 2)*v*v
        self.assertEqual(derivative(v, (0, b*b, 1+b*r)), 0)
        self.assertEqual(hp, -h)
        self.assertEqual(v+b*hp, r)
        self.assertEqual(s+v*hp+Q(1, 2)*b*hp*hp, w)

    def test_replica_forward_after_inverse(self):
        b, v, s = V[:3]
        hp = b*s-Q(1, 2)*v*v
        r = v+b*hp
        w = s+v*hp+Q(1, 2)*b*hp*hp
        h = Q(1, 2)*r*r-b*w
        self.assertEqual(r+b*h, v)
        self.assertEqual(w+r*h+Q(1, 2)*b*h*h, s)

    def test_general_polynomial_replica(self):
        b, r, w = V[:3]
        # Finite examples of the all-degree Taylor identity proved in the note.
        for F in (r, r*r, r**3+r, r**4+2*r*r+3):
            h = F-b*w
            s = w
            current = F.diff(1)
            j = 1
            while current != 0:
                s += Q(1, factorial(j))*b**(j-1)*h**j*current
                current = current.diff(1)
                j += 1
            images = (0, b*b, 1+b*F.diff(1))
            self.assertEqual(derivative(s, images), 1)
            self.assertEqual(derivative(r+b*h, images), 0)

    def test_nongauge_example_modulo_square(self):
        x, y, w = V[:3]
        a = 1+x*y
        # x**2*d/dy has image exactly x**2*k[x,y].
        remainder = Poly({p: c for p, c in (a-1).terms.items() if p[0] < 2})
        self.assertEqual(remainder, x*y)
        self.assertNotEqual(remainder, 0)

    def test_danielewski_relation_is_preserved(self):
        x, y, z, w = V[:4]
        E = (0, 2*z, x, Q(3, 2)*y)
        self.assertEqual(derivative(x*y-z*z+1, E), 0)

    def test_danielewski_slice(self):
        x, y, z, w = V[:4]
        s = Q(1, 2)*z*y-x*w
        actual = derivative(s, (0, 2*z, x, Q(3, 2)*y))
        self.assertEqual(quotient_reduce(actual-1, 1), 0)
        self.assertNotEqual(quotient_reduce(actual+1, 1), 0)

    def test_danielewski_invariants(self):
        x, y, z, w = V[:4]
        Z = x*x*w+Q(1, 2)*(3*z-z**3)
        Y = x*x*w*w+(3*z-z**3)*w+Q(1, 4)*y*y*(z*z-4)
        E = (0, 2*z, x, Q(3, 2)*y)
        self.assertEqual(quotient_reduce(derivative(Z, E), 1), 0)
        self.assertEqual(quotient_reduce(derivative(Y, E), 1), 0)
        self.assertEqual(quotient_reduce(x*x*Y-Z*Z+1, 1), 0)

    def test_danielewski_inverse_after_forward(self):
        x, y, z, w = V[:4]
        Z = x*x*w+Q(1, 2)*(3*z-z**3)
        Y = x*x*w*w+(3*z-z**3)*w+Q(1, 4)*y*y*(z*z-4)
        s = Q(1, 2)*z*y-x*w
        recovered = (
            x*Y+2*Z*s+x*s*s,
            Z+x*s,
            Q(1, 2)*Z*Y+Q(3, 2)*x*Y*s+Q(3, 2)*Z*s*s+Q(1, 2)*x*s**3,
        )
        for value, original in zip(recovered, (y, z, w)):
            self.assertEqual(quotient_reduce(value-original, 1), 0)

    def test_danielewski_forward_after_inverse(self):
        x, Y, Z, s = V[:4]
        z = Z+x*s
        y = x*Y+2*Z*s+x*s*s
        w = Q(1, 2)*Z*Y+Q(3, 2)*x*Y*s+Q(3, 2)*Z*s*s+Q(1, 2)*x*s**3
        self.assertEqual(quotient_reduce(x*y-z*z+1, 2), 0)
        self.assertEqual(quotient_reduce(Q(1, 2)*z*y-x*w-s, 2), 0)
        self.assertEqual(quotient_reduce(x*x*w+Q(1, 2)*(3*z-z**3)-Z, 2), 0)
        image_Y = x*x*w*w+(3*z-z**3)*w+Q(1, 4)*y*y*(z*z-4)
        self.assertEqual(quotient_reduce(image_Y-Y, 2), 0)

    def test_danielewski_rational_primitive(self):
        x, unused, z = V[:3]
        c = V[4]
        H = Q(1, 2)*(z**3-3*z)*x**-2-c*z*x**-1
        # On the generic fiber y=(z**2-1)/x and delta=x*d/dz.
        self.assertEqual(x*H.diff(2), Q(3, 2)*(z*z-1)*x**-1-c)
        difference = H.at({2: 1})-H.at({2: -1})
        self.assertEqual(difference, -2*x**-2-2*c*x**-1)
        self.assertNotEqual(difference, 0)

    def test_integration_certificate(self):
        b, r, u = V[:3]
        images = (0, b, 0)
        for degree in range(7):
            M = sum((r**j*(u+j+1) for j in range(degree+1)), Poly())
            J = Poly()
            current = M
            for j in range(degree+1):
                J += Q((-1)**j, factorial(j+1))*b**(degree-j)*r**(j+1)*current
                current = derivative(current, images)
            self.assertEqual(current, 0)
            self.assertEqual(derivative(J, images), b**(degree+1)*M)

    def test_bezout_certificate(self):
        b, q = V[:2]
        for c in (Q(1), Q(3), Q(-2, 3)):
            u = c+b*q
            for n in range(1, 8):
                P = sum((Q(1, 1)/c*(-Q(1, 1)/c*b*q)**j
                         for j in range(n)), Poly())
                tail = (-Q(1, 1)/c*q)**n
                self.assertEqual(P*u+tail*b**n, 1)

    def test_second_pole_primitive(self):
        x, y, z = V[:3]
        S = x*x*y+f*z
        H = r+Q(1, 6)*x**3
        self.assertEqual(derivative(H, (DX, DY, DZ)), f*f*S)
        self.assertEqual(H, -Q(5, 6)*x**3-f*y)
        # Homogeneity gives the written proof that S cannot be Delta-exact.
        self.assertEqual({sum(p) for p in S.terms}, {3})
        for value in (DX, DY, DZ):
            self.assertEqual({sum(p) for p in value.terms}, {5})

    def test_second_pole_endpoint_relations(self):
        b, t, F = V[:3]
        S4 = sum((t**j for j in range(5)), Poly())
        S5 = S4+t**5
        G = b**5*S5
        constraint = F**3-b**6*t*S4
        p = {0: b, 1: 0, 2: F*b**-1}
        q = {0: b*t, 1: 0, 2: F*b**-1*t**-1}
        self.assertEqual(f.at(p), F)
        self.assertEqual(f.at(q), F)
        self.assertEqual(b*(g.at(p)-G), constraint)
        self.assertEqual(b*t*(g.at(q)-G), constraint)
        self.assertEqual(r.at(q)-r.at(p), b**3*(1-t**3))

    def test_second_pole_hensel_simple_root_identity(self):
        b, t = V[:2]
        S4 = sum((t**j for j in range(5)), Poly())
        self.assertEqual((t-1)*(t*S4).diff(1), 5+(5*t-6)*S4)
        # At a primitive fifth root, S4=0 and t-1 is nonzero.
        self.assertEqual((S4+t**5)-1, t*S4)

    def test_second_pole_zero_fourth_displacement(self):
        b, t, F, G = V[:4]
        numerator = b**3*(1-t**3)
        time = numerator*F**-1*G**-1
        H_difference = Q(5, 6)*numerator
        displacement = time+H_difference*F**-2
        self.assertEqual(displacement.at({2: -Q(5, 6)*G}), 0)
        self.assertNotEqual(displacement.at({2: Q(5, 6)*G}), 0)

    def test_nonzero_f_fiber_nonproperness_certificate(self):
        v, G = V[4:6]
        p = {0: 0, 1: v, 2: G*v**-4, 3: 0}
        q = {0: 0, 1: -v, 2: G*v**-4, 3: 0}
        time = 2*v*G**-1
        self.assertEqual(f.at(p), -v*v)
        self.assertEqual(g.at(p), G)
        self.assertEqual((r.at(q)-r.at(p)), time*(-v*v)*G)
        for variable in V[:4]:
            self.assertEqual(endpoint(variable, time=time, point=p,
                                      images=(DX, DY, DZ, 0)), variable.at(q))
        self.assertEqual(min(powers[5] for powers in time.terms), -1)
        for point in (p, q):
            for variable in V[:4]:
                self.assertTrue(all(powers[5] >= 0
                                    for powers in variable.at(point).terms))


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(NonlinearChecks))
    print(json.dumps({
        "tests_run": result.testsRun,
        "successful": result.wasSuccessful(),
        "arithmetic": "exact sparse Laurent polynomials over Fraction",
        "external_packages": [],
        "scope": "finite identities; written structural proofs remain separate",
        "general_cancellation_solved": False,
        "novelty_established": False,
        "lean_formalized": False,
    }, indent=2))
    raise SystemExit(0 if result.wasSuccessful() else 1)
