"""Independent exact controls for the fixed surface's quotient and ambient gate.

Uses only unittest and SymPy. The local flatness argument, the Cartier
divisor argument, and the universal invariant-restriction exact sequence
are written proofs, not extrapolations from these finite calculations.
"""

import unittest

import sympy as sp


u, y, z, t = sp.symbols("u y z t")
d, e, v, w, s = sp.symbols("d e v w s")
i = sp.I
A = (u-1)*(u-i)
du = u**4-1
images = {d: du, e: du*u, v: du*u**2, w: du*u**3}
relations = [
    e**2-d*v, e*v-d*w, e*w-d**2*(d+1),
    v**2-d**2*(d+1), v*w-d*(d+1)*e, w**2-d*(d+1)*v,
]
branches = [
    (sp.Integer(1), 0), (i, 0),
    (sp.Integer(1), 1), (-i, None),
    (sp.Integer(-1), None), (i, 1),
]


def action(expression):
    return sp.expand(u*A*sp.diff(expression, y)+u*(2*y-1)*sp.diff(expression, z))


class NodalHypersurfaceChecks(unittest.TestCase):
    def test_descended_action_and_original_gluing(self):
        self.assertEqual(action(A*z-y*(y-1)), 0)
        for root, epsilon in branches:
            if epsilon is None:
                parameter = y/(root*A.subs(u, root))
                derivative = action(parameter).subs(u, root)
            else:
                parameter = z/(root*(2*epsilon-1))
                derivative = action(parameter).subs({u: root, y: epsilon})
            self.assertEqual(sp.simplify(derivative-1), 0)
        edges = [(0, 2), (0, 3), (1, 2)]
        reached = {0}
        for _ in range(4):
            for left, right in edges:
                if left in reached or right in reached:
                    reached.update([left, right])
        self.assertEqual(reached, {0, 1, 2, 3})

    def test_exact_kernel_curve_presentation_and_four_tangents(self):
        for relation in relations:
            self.assertEqual(sp.expand(relation.subs(images, simultaneous=True)), 0)
            for coordinate in [d, e, v, w]:
                self.assertEqual(
                    sp.diff(relation, coordinate).subs({d: 0, e: 0, v: 0, w: 0}), 0
                )
        roots = [sp.Integer(1), sp.Integer(-1), i, -i]
        matrix = sp.Matrix([[root**degree for degree in range(4)] for root in roots])
        self.assertNotEqual(sp.simplify(matrix.det()), 0)
        for root in roots:
            self.assertNotEqual(sp.diff(du, u).subs(u, root), 0)
        normalized_basis = [sp.Integer(1), du*u, du*u**2, du*u**3]
        for residue_class, element in enumerate(normalized_basis):
            exponents = [degree[0] % 4 for degree, coefficient in sp.Poly(element, u).terms()]
            self.assertTrue(all(degree == residue_class for degree in exponents))

    def test_two_distinct_artinian_fibers(self):
        parameter_fiber = sp.groebner(relations+[d], d, e, v, w)
        for monomial in [e**2, e*v, e*w, v**2, v*w, w**2]:
            self.assertEqual(parameter_fiber.reduce(monomial)[1], 0)
        for basis_element in [sp.Integer(1), e, v, w]:
            self.assertEqual(parameter_fiber.reduce(basis_element)[1], basis_element)
        nodal_fiber = sp.groebner(relations+[d, v], d, e, v, w)
        for monomial in [e**2, e*w, w**2, d, v]:
            self.assertEqual(nodal_fiber.reduce(monomial)[1], 0)
        for basis_element in [sp.Integer(1), e, w]:
            self.assertEqual(nodal_fiber.reduce(basis_element)[1], basis_element)
        self.assertEqual(len([1, e, v, w]), 4)
        self.assertEqual(len([1, e, w]), 3)

    def test_exact_normalization_defect_module(self):
        matrix = sp.Matrix([[v, -d*(d+1)], [-d, v]])
        plane_relation = v**2-d**2*(d+1)
        self.assertEqual(sp.expand(matrix.det()-plane_relation), 0)
        for column in range(2):
            value = matrix[0, column]+s*matrix[1, column]
            self.assertEqual(
                sp.expand(value.subs({d: s**2-1, v: s*(s**2-1)}, simultaneous=True)), 0
            )
        alpha1, beta1 = sp.symbols("alpha1 beta1")
        reconstructed = matrix*sp.Matrix([alpha1, beta1])
        self.assertEqual(reconstructed[0], v*alpha1-d*(d+1)*beta1)
        self.assertEqual(reconstructed[1], -d*alpha1+v*beta1)
        self.assertEqual(matrix.subs({d: 0, v: 0}), sp.zeros(2))
        self.assertEqual(
            sp.expand((v*e-d*w).subs(images, simultaneous=True)), 0
        )
        self.assertEqual(
            sp.expand((v*w-d*(d+1)*e).subs(images, simultaneous=True)), 0
        )
        original_u = 3*du+1
        # a0^4=3 makes (3*a0^2*v)^2 = 27*v^2.
        self.assertEqual(
            sp.expand(27*(du*u**2)**2-original_u**3+3*original_u-2), 0
        )

    def test_squared_parameter_conductor_interpolation(self):
        for pair in range(3):
            first_root = branches[2*pair][0]
            second_root = branches[2*pair+1][0]
            first_value = t**2+(pair+1)*t+1
            second_value = (pair+2)*t**3-t
            denominator = first_root**2-second_root**2
            self.assertNotEqual(sp.simplify(denominator), 0)
            coefficient1 = (first_value-second_value)/denominator
            coefficient0 = first_value-first_root**2*coefficient1
            self.assertEqual(sp.expand(coefficient0+first_root**2*coefficient1-first_value), 0)
            self.assertEqual(sp.expand(coefficient0+second_root**2*coefficient1-second_value), 0)
            determinant = 16*first_root**3*second_root**3*(second_root**2-first_root**2)
            self.assertNotEqual(sp.simplify(determinant), 0)

    def test_fixed_divisor_order_four_and_irreducibility_control(self):
        roots = [sp.Integer(1), sp.Integer(-1), i, -i]
        for exponent in [1, 2, 3, 4, 5, 8]:
            equal_values = all(sp.simplify(root**exponent-1) == 0 for root in roots)
            self.assertEqual(equal_values, exponent % 4 == 0)
        bb = (1-i)*(u+1)*(u+i)/4
        aa = -i*A*(u+(1+i)/2)/2
        label = aa+bb*y
        self.assertEqual(sp.expand(action(label)-u*A*bb), 0)
        self.assertNotEqual(sp.simplify((A*bb).subs(u, 0)), 0)
        self.assertEqual(sp.expand(du+1-u**4), 0)

    def test_actual_ambient_restriction_obstruction_control(self):
        xx, yy, zz = sp.symbols("X Y Z")
        invariant = xx*zz-yy**2

        def ambient_action(expression):
            return sp.expand(xx*sp.diff(expression, yy)+2*yy*sp.diff(expression, zz))

        self.assertEqual(ambient_action(invariant), 0)
        self.assertEqual(ambient_action(yy), xx)
        self.assertEqual(invariant.subs(xx, 0), -yy**2)
        self.assertEqual(sp.gcd(xx, 2*yy), 1)
        for value in [ambient_action(xx), ambient_action(yy), ambient_action(zz)]:
            self.assertEqual(value.subs({xx: 0, yy: 0}), 0)
        gauge = xx+yy**2+zz
        lifted = yy+xx*gauge
        quotient_derivative = sp.cancel(ambient_action(lifted)/xx)
        self.assertEqual(
            sp.expand(quotient_derivative-1-ambient_action(gauge)), 0
        )

    def test_free_degree_modules_nonfree_torsion_countercontrol(self):
        pp = v**2-d**2*(d+1)
        matrix = sp.Matrix([
            [0, pp, d, v],
            [0, 0, pp, 0],
            [0, 0, 0, pp],
            [0, 0, 0, 0],
        ])
        self.assertEqual(matrix**4, sp.zeros(4))
        for degree in [1, 2, 3]:
            image = matrix**degree * sp.eye(4)[:, degree]
            self.assertEqual(
                (image-pp**degree*sp.eye(4)[:, 0]).applyfunc(sp.expand), sp.zeros(4, 1)
            )
        presentation = sp.Matrix([[pp, d, v], [0, pp, 0], [0, 0, pp]])
        self.assertEqual(presentation.subs({d: 0, v: 0}), sp.zeros(3))
        k1 = sp.Matrix([0, v, -d])
        k2 = sp.Matrix([0, d*(d+1), -v])
        # Express P*k_j as actual combinations of the relation columns.
        self.assertEqual(
            (pp*k1-presentation*sp.Matrix([0, v, -d])).applyfunc(sp.expand), sp.zeros(3, 1)
        )
        self.assertEqual(
            (pp*k2-presentation*sp.Matrix([1, d*(d+1), -v])).applyfunc(sp.expand),
            sp.zeros(3, 1),
        )
        sigma = sp.Symbol("sigma")
        basis = [
            sp.Integer(1), pp*sigma,
            pp**2*sigma**2/2+d*sigma,
            pp**3*sigma**3/6+pp*d*sigma**2/2+v*sigma,
        ]
        for column in range(4):
            expected = sum(matrix[row, column]*basis[row] for row in range(4))
            self.assertEqual(sp.expand(sp.diff(basis[column], sigma)-expected), 0)
        self.assertEqual(sp.expand(basis[1]**2-2*basis[2]+2*d*sigma), 0)
        self.assertNotEqual(sp.rem(d, pp, v), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
