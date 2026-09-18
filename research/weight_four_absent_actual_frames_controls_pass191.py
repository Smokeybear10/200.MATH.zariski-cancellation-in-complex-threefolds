"""Finite exact controls for the two actual absent-variable frames191.

Both coordinate maps are checked through their polynomial stages in both
orders. Their original partial_Z is differentiated from the staged inverse
and independently applied to the forward coordinates. Time degrees, ordinary
leading coefficients, projected inverse maps and calibrated determinants are
literal identities, with no numerical specialization of invariant variables.
The full initial-kernel proof remains the written image-field, height-one and
Gauss argument. The finite algebra checks below do not replace that proof,
establish profile minimality, or prove general recognition or cancellation.
No earlier checker is imported. Authored source-only; Root owns execution.
"""

import unittest

import sympy as sp


class AbsentVariableActualFramesControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def check_inverse(self, source, target, forward, inverse):
        to_source = dict(zip(target, forward))
        to_target = dict(zip(source, inverse))
        for expression, variable in zip(inverse, source):
            self.zero(expression.subs(to_source, simultaneous=True) - variable)
        for expression, variable in zip(forward, target):
            self.zero(expression.subs(to_target, simultaneous=True) - variable)

    def test_zero_R_actual_frame_inverse_partial_and_time_profile(self):
        x, y, t, n = sp.symbols("x y t n")
        X, Y, Z, W, I = sp.symbols("X Y Z W I")
        Zf = n + 6 * t**2 * y**2 + 4 * t**3 * y * x + t**4 * x**2
        Wf = t - y**4 - 4 * t * y**3 * x + n * x**2
        forward = (x, y + t * x, Zf, Wf)
        I0 = W - X**2 * Z + Y**4
        self.zero(I0.subs(dict(zip((X, Y, Z, W), forward)), simultaneous=True) - t)

        # Source -> (X,Y,Z,I) and then -> (X,Y,Z,W). Checking both
        # stages avoids substituting a large expanded I0 into every power.
        yi = Y - I * X
        ni = Z - 6 * I**2 * yi**2 - 4 * I**3 * yi * X - I**4 * X**2
        intermediate = (x, y + t * x, Zf, t)
        inverse_stage = (X, yi, I, ni)
        self.check_inverse((x, y, t, n), (X, Y, Z, I), intermediate, inverse_stage)
        target_stage = (X, Y, Z, I + X**2 * Z - Y**4)
        target_inverse = (X, Y, Z, I0)
        self.check_inverse((X, Y, Z, I), (X, Y, Z, W), target_stage, target_inverse)
        self.zero(target_stage[3].subs(
            dict(zip((X, Y, Z, I), intermediate)), simultaneous=True
        ) - Wf)

        # The literal target partial has dI0/dZ=-X^2 in the intermediate ring.
        self.zero(sp.diff(I0, Z) + X**2)

        def target_partial(expression):
            return sp.diff(expression, Z) - X**2 * sp.diff(expression, I)

        source_substitution = dict(zip((X, Y, Z, I), intermediate))
        derived = tuple(sp.expand(target_partial(expression).subs(
            source_substitution, simultaneous=True
        )) for expression in inverse_stage)
        expected = (sp.Integer(0), x**3, -x**2, 1 + 12 * t * y**2 * x**2)
        for obtained, wanted in zip(derived, expected):
            self.zero(obtained - wanted)

        def TZ(expression):
            return sum(coefficient * sp.diff(expression, variable)
                       for coefficient, variable in zip(derived, (x, y, t, n)))

        for expression, value in zip(forward, (0, 0, 1, 0)):
            self.zero(TZ(expression) - value)
        self.assertEqual([sp.Poly(f, x).degree() for f in forward], [1, 1, 2, 2])
        for f, degree, leading in zip(forward, (1, 1, 2, 2), (1, t, t**4, n)):
            self.zero(sp.Poly(f, x).coeff_monomial(x**degree) - leading)
        self.zero(sp.diff(Zf, x, 2) / 2 - t**4)
        self.zero(sp.diff(Wf, x, 2) / 2 - n)
        self.zero(sp.diff(forward[0], x) - 1)
        # On ker(partial_x)=C[y,t,n], the cubic coefficient is partial_y.
        self.assertEqual([sp.expand(f).coeff(x, 3) for f in derived[1:]], [1, 0, 0])
        self.assertEqual(max(sp.Poly(f, x).degree() for f in derived[1:]), 3)

    def test_nonzero_R_actual_frame_inverse_partial_and_time_profile(self):
        x, y, t, h = sp.symbols("x y t h")
        X, Y, Z, W, I, J = sp.symbols("X Y Z W I J")
        Zf = y**4 + t + (4 * t**3 * y + h) * x + t**4 * x**2
        Wf = (h - 4 * t * y**3 + 4 * t**3 * y
              + (y**4 + t - 6 * t**2 * y**2 + t**4) * x + h * x**2)
        forward = (x, y + t * x, Zf, Wf)
        tail = (-4 * t * y**3 + 4 * t**3 * y
                + (-6 * t**2 * y**2 + t**4) * x
                - 4 * t**3 * y * x**2 - t**4 * x**3)
        intermediate = (x, y + t * x, t, h + tail)
        yi = Y - I * X
        tail_inverse = tail.subs({x: X, y: yi, t: I}, simultaneous=True)
        inverse_stage = (X, yi, I, J - tail_inverse)
        self.check_inverse((x, y, t, h), (X, Y, I, J), intermediate, inverse_stage)

        Z_stage = I + Y**4 + X * J
        W_stage = J + X * Z_stage
        I1, J1 = (1 + X**2) * Z - X * W - Y**4, W - X * Z
        self.check_inverse((X, Y, I, J), (X, Y, Z, W),
                           (X, Y, Z_stage, W_stage), (X, Y, I1, J1))
        source_substitution = dict(zip((X, Y, I, J), intermediate))
        self.zero(Z_stage.subs(source_substitution, simultaneous=True) - Zf)
        self.zero(W_stage.subs(source_substitution, simultaneous=True) - Wf)
        original_to_source = dict(zip((X, Y, Z, W), forward))
        self.zero(I1.subs(original_to_source, simultaneous=True) - t)
        self.zero(J1.subs(original_to_source, simultaneous=True) - h - tail)
        self.zero(sp.diff(I1, Z) - 1 - X**2)
        self.zero(sp.diff(J1, Z) + X)

        def target_partial(expression):
            return (1 + X**2) * sp.diff(expression, I) - X * sp.diff(expression, J)

        derived = tuple(sp.expand(target_partial(expression).subs(
            source_substitution, simultaneous=True
        )) for expression in inverse_stage)
        expected = (sp.Integer(0), -x * (1 + x**2), 1 + x**2,
                    4 * y * (y**2 - 3 * t**2) * (1 + x**2) - x)
        for obtained, wanted in zip(derived, expected):
            self.zero(obtained - wanted)

        def TZ(expression):
            return sum(coefficient * sp.diff(expression, variable)
                       for coefficient, variable in zip(derived, (x, y, t, h)))

        for expression, value in zip(forward, (0, 0, 1, 0)):
            self.zero(TZ(expression) - value)
        self.assertEqual([sp.Poly(f, x).degree() for f in forward], [1, 1, 2, 2])
        for f, degree, leading in zip(forward, (1, 1, 2, 2), (1, t, t**4, h)):
            self.zero(sp.Poly(f, x).coeff_monomial(x**degree) - leading)
        self.zero(sp.diff(Zf, x, 2) / 2 - t**4)
        self.zero(sp.diff(Wf, x, 2) / 2 - h)
        self.zero(sp.diff(forward[0], x) - 1)
        # Here N=-partial_y, Nv=1 for v=-y, and Gamma=Ny=-1.
        self.assertEqual([sp.expand(f).coeff(x, 3) for f in derived[1:]], [-1, 0, 0])
        self.zero(-sp.diff(-y, y) - 1)
        self.assertEqual(max(sp.Poly(f, x).degree() for f in derived[1:]), 3)

    def test_projected_inverses_potentials_and_initial_algebra_controls(self):
        y, t, n, h, v = sp.symbols("y t n h v")
        yp, zp, wp = sp.symbols("yp zp wp")
        z0, w0, theta0 = n + 6 * t**2 * y**2, t - y**4, -4 * t * y**3
        tp0 = wp + yp**4
        np0 = zp - 6 * tp0**2 * yp**2
        self.check_inverse((y, t, n), (yp, zp, wp),
                           (y, z0, w0), (yp, tp0, np0))
        self.zero(sp.Matrix([y, z0, w0]).jacobian([t, n, y]).det() + 1)
        self.zero(4 * t * y**3 + theta0)
        self.zero(w0 + y**4 - t)

        z1, w1 = y**4 + t, h - 4 * t * y**3 + 4 * t**3 * y
        theta1 = y**4 + t - 6 * t**2 * y**2 + t**4
        tp1 = zp - yp**4
        hp1 = wp + 4 * tp1 * yp**3 - 4 * tp1**3 * yp
        self.check_inverse((y, t, h), (yp, zp, wp),
                           (y, z1, w1), (yp, tp1, hp1))
        unnormalized = sp.Matrix([y, z1, w1]).jacobian([t, h, y]).det()
        normalized = sp.Matrix([f.subs(y, -v) for f in (y, z1, w1)]).jacobian([t, h, v]).det()
        self.zero(unnormalized - 1)
        self.zero(normalized + 1)
        self.zero(w1 + 4 * t * y**3 - 4 * t**3 * y - h)
        self.zero(y**4 - 6 * t**2 * y**2 - theta1 + t + t**4)

        X0, Y0, Z0, W0, xi, s, scale = sp.symbols("X0 Y0 Z0 W0 xi s scale")
        initial = (xi, t * xi, t**4 * xi**2, s * xi**2)
        relation = X0**2 * Z0 - Y0**4
        self.zero(relation.subs(dict(zip((X0, Y0, Z0, W0), initial)), simultaneous=True))
        self.zero(initial[1] / initial[0] - t)
        self.zero(initial[3] / initial[0]**2 - s)
        self.assertEqual(sp.Poly(relation, Z0).degree(), 1)
        self.assertEqual(sp.gcd(X0**2, Y0**4), 1)
        self.zero(relation.subs({X0: scale * X0, Y0: scale * Y0,
                                 Z0: scale**2 * Z0, W0: scale**2 * W0},
                                simultaneous=True) - scale**4 * relation)
        # These are the explicit algebraic ingredients, not a sampled proof
        # that the kernel has height one or is generated by the relation.


if __name__ == "__main__":
    unittest.main()
