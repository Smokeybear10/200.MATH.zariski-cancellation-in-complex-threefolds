"""Exact controls for horizontal gauges and canonical normalizer obstruction.

The universal normalizer proof is written in horizontal-gauge-pass30.md.
No old checker or project solver is imported.
"""

import unittest

import sympy as sp


lam, x, w, z, U, V = sp.symbols("lam x w z U V")
coordinates = (lam, x, w, z)
v = 1+lam*x
F = 2*x*z-w**2
vertical = (0, 0, x**2, 2*v**2*w)
examples = (
    ((1, 0, 1, 0), 3),
    ((1, 0, z**2, 0), 3),
    ((1, 0, lam*z**2, 0), 4),
    ((1, 0, x*F, w*F), 4),
)


def apply(field, expression):
    return sp.expand(sum(value*sp.diff(expression, variable)
                         for value, variable in zip(field, coordinates)))


def projection(field, expression, bound):
    result = sp.Integer(0)
    current = expression
    for j in range(bound):
        result += (-lam)**j*current/sp.factorial(j)
        current = apply(field, current)
    if current != 0:
        raise ValueError("The supplied nilpotence bound is not sufficient")
    return sp.expand(result)


def reconstruction(field, expression, bound):
    result = sp.Integer(0)
    current = expression
    for j in range(bound):
        result += lam**j*current.subs({lam: 0, w: U, z: V}, simultaneous=True)/sp.factorial(j)
        current = apply(field, current)
    if current != 0:
        raise ValueError("The supplied nilpotence bound is not sufficient")
    return sp.expand(result)


def normalizer(scale, shift, parameter):
    forward = {
        w: scale*w+x**2*parameter,
        z: scale**2*z+shift+2*scale*v**2*w*parameter+x**2*v**2*parameter**2,
    }
    backward = {
        w: (w-x**2*parameter)/scale,
        z: (z-shift-2*v**2*w*parameter+x**2*v**2*parameter**2)/scale**2,
    }
    return forward, backward


class HorizontalGaugeChecks(unittest.TestCase):
    def test_actual_horizontal_inputs_and_finite_bounds(self):
        for field, bound in examples:
            self.assertEqual(apply(field, lam), 1)
            self.assertEqual(apply(field, x), 0)
            for generator in coordinates:
                current = generator
                for _ in range(bound):
                    current = apply(field, current)
                self.assertEqual(current, 0)

    def test_finite_slice_projection_and_multiplicativity_controls(self):
        for field, bound in examples:
            pu = projection(field, w, bound)
            pv = projection(field, z, bound)
            self.assertEqual(apply(field, pu), 0)
            self.assertEqual(apply(field, pv), 0)
            self.assertEqual(pu.subs(lam, 0), w)
            self.assertEqual(pv.subs(lam, 0), z)
            self.assertEqual(projection(field, lam, bound), 0)
            self.assertEqual(projection(field, x, bound), x)
            actual = projection(field, w*z+x*w+lam*z, 2*bound)
            self.assertEqual(sp.expand(actual-(pu*pv+x*pu)), 0)

    def test_constructed_gauges_have_full_polynomial_inverse(self):
        for field, bound in examples:
            pu = projection(field, w, bound)
            pv = projection(field, z, bound)
            rw = reconstruction(field, w, bound)
            rz = reconstruction(field, z, bound)
            for actual, expected in ((rw, w), (rz, z)):
                self.assertEqual(sp.expand(actual.subs({U: pu, V: pv}, simultaneous=True)
                                          -expected), 0)
            for actual, expected in ((pu, U), (pv, V)):
                self.assertEqual(sp.expand(actual.subs({w: rw, z: rz}, simultaneous=True)
                                          -expected), 0)

    def test_nontrivial_actual_canonical_normalizers_and_inverse(self):
        choices = ((sp.Integer(1), lam, x+lam),
                   (sp.Integer(2), x+lam**2, lam+x**2),
                   (-sp.Integer(1), 1+x*lam, lam**2))
        for scale, shift, parameter in choices:
            forward, backward = normalizer(scale, shift, parameter)
            for generator in (w, z):
                self.assertEqual(sp.expand(forward[generator].subs(backward, simultaneous=True)
                                          -generator), 0)
                self.assertEqual(sp.expand(backward[generator].subs(forward, simultaneous=True)
                                          -generator), 0)
                actual = apply(vertical, forward[generator])
                expected = scale*apply(vertical, generator).subs(forward, simultaneous=True)
                self.assertEqual(sp.expand(actual-expected), 0)
            self.assertEqual(forward[w].subs(x, 0), scale*w)

    def test_normalizer_residue_equation_forces_zero_translation(self):
        scale, gamma = sp.symbols("scale gamma", nonzero=True)
        translation = lam**2+1
        plane_restriction = scale*w+translation
        z_restriction = gamma*scale*z+lam*w**2+lam**3
        actual = sp.expand(2*w*sp.diff(z_restriction, z)-2*gamma*plane_restriction)
        self.assertEqual(actual, sp.expand(-2*gamma*translation))
        self.assertNotEqual(actual, 0)
        self.assertEqual(sp.expand(actual+2*gamma*translation), 0)
        # Setting the prohibited translation to zero permits all the displayed P(lambda,w).
        self.assertEqual(sp.expand(2*w*sp.diff(z_restriction, z)-2*gamma*scale*w), 0)

    def test_actual_gauges_cannot_fix_auxiliary_plane_for_delta_one(self):
        horizontal = (1, 0, 1, 0)
        for scale in (sp.Integer(1), sp.Integer(2), -sp.Integer(1)):
            forward, backward = normalizer(scale, x+lam**2, lam+x**2)
            conjugated_w = apply(horizontal, forward[w]).subs(backward, simultaneous=True)
            conjugated_z = apply(horizontal, forward[z]).subs(backward, simultaneous=True)
            self.assertEqual(sp.expand(conjugated_w).subs(x, 0), scale)
            image_f = sp.expand(2*x*conjugated_z-2*w*conjugated_w)
            self.assertEqual(image_f.subs(x, 0), -2*scale*w)

    def test_actual_fixed_ideal_and_tangency_obstruction(self):
        inverse_unit = 1-2*lam*x
        self.assertEqual(sp.expand(inverse_unit*v**2), 1-3*lam**2*x**2-2*lam**3*x**3)
        recovered_w = inverse_unit*v**2*w+x**2*(3*lam**2+2*lam**3*x)*w
        self.assertEqual(sp.expand(recovered_w-w), 0)
        for coefficient in (1, lam+x, F, lam*F**2+x):
            field = (1, 0, x*coefficient, w*coefficient)
            self.assertEqual(apply(field, F), 0)
            self.assertEqual(apply(field, x).subs({x: 0, w: 0}), 0)
            self.assertEqual(apply(field, w).subs({x: 0, w: 0}), 0)
        self.assertEqual(apply((1, 0, 1, 0), w).subs({x: 0, w: 0}), 1)

    def test_unrestricted_success_changes_the_vertical_action(self):
        horizontal = (1, 0, 1, 0)
        forward = {w: w-lam, z: z}
        backward = {w: w+lam, z: z}
        self.assertEqual(apply(horizontal, forward[w]), 0)
        self.assertEqual(apply(horizontal, forward[z]), 0)
        conjugated_w = apply(vertical, forward[w]).subs(backward, simultaneous=True)
        conjugated_z = apply(vertical, forward[z]).subs(backward, simultaneous=True)
        self.assertEqual(sp.expand(conjugated_w-x**2), 0)
        self.assertEqual(sp.expand(conjugated_z-2*v**2*(w+lam)), 0)
        self.assertNotEqual(sp.expand(conjugated_z-apply(vertical, z)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
