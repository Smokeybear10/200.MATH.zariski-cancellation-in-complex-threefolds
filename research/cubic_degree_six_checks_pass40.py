"""Five finite controls, not an asserted actual degree-six realization."""

import unittest

import sympy as sp


class CubicDegreeSixChecks(unittest.TestCase):
    def assertZero(self, value):
        if isinstance(value, sp.MatrixBase):
            self.assertEqual(value.applyfunc(sp.expand), sp.zeros(*value.shape))
        else:
            self.assertEqual(sp.expand(value), 0)

    def test_auxiliary_rows_from_an_actual_lower_degree_action(self):
        # This is the actual cubic control, not a degree-six example.
        a, b, c, d = sp.symbols("a b c d")
        x = sp.Matrix([a, b, c, d])
        invariant = a + b + c - d**3 / 6
        p = sp.Matrix([1, 0, invariant*d**2/2 - 1, invariant])

        def action(value):
            return (value.jacobian(x)*p).applyfunc(sp.expand)

        def commutator(field):
            return (field.jacobian(x)*p
                    - p.jacobian(x)*field).applyfunc(sp.expand)

        u = commutator(commutator(sp.eye(4)[:, 3]))
        v = commutator(u)
        companion = p.jacobian(x).row_join(-u/2).row_join(-v/6)
        companion = companion.col_join(
            sp.Matrix([[0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0]]))
        iterates = [x]
        for _ in range(6):
            iterates.append(action(iterates[-1]))
        power = sp.eye(6)
        for exponent in range(1, 7):
            power = (power*companion).applyfunc(sp.expand)
            self.assertZero(
                power[:4, :4]
                - iterates[exponent].jacobian(x)/sp.factorial(exponent))
            self.assertZero(
                power[4, :4]
                - sp.Matrix([iterates[exponent-1][3]]).jacobian(x)
                / sp.factorial(exponent-1))
            if exponent >= 2:
                self.assertZero(
                    power[5, :4]
                    - sp.Matrix([iterates[exponent-2][3]]).jacobian(x)
                    / sp.factorial(exponent-2))
        self.assertZero(power)
        self.assertNotEqual(iterates[3], sp.zeros(4, 1))
        self.assertZero(iterates[4])

    def test_top_coefficient_extraction_and_corrected_commutator(self):
        # One scalar component of the free vector identities, with no claim
        # that these symbols define a polynomial action.
        cc, dd, ee, uu, vv = sp.symbols("cc dd ee uu vv")
        sigma, tau, lam = sp.symbols("sigma tau lam", nonzero=True)
        jc, jd, je = sp.symbols("jc jd je")
        for r in (4, 5):
            r = sp.Integer(r)
            eq_top = -jc + r*(r-1)*lam*vv/6
            jc_value = sp.solve(eq_top, jc)[0]
            eq_next = (cc/r - sigma*jc_value - jd
                       + (r-1)*lam*uu/2
                       + (r-1)*(r-2)*lam*sigma*vv/6)
            jd_value = sp.solve(eq_next, jd)[0]
            q = lam*sigma**2/2 + tau
            zeta = sigma**2/2 + (r-2)*tau/(r*lam)
            eq_lower = ((cc*sigma+dd)/(r-1)
                        - zeta*jc_value - sigma*jd_value - je
                        + (r-2)*lam*sigma*uu/2
                        + (r-2)*(r-3)*q*vv/6)
            je_value = sp.solve(eq_lower, je)[0]
            self.assertZero(
                je_value - (cc*sigma/(r*(r-1)) + dd/(r-1)
                            - lam*sigma*uu/2
                            + (lam*sigma**2/6-(r-2)*tau/3)*vv))
            c_coefficient = (sigma**2/(r*(r-1))
                             + 2*(r-2)*tau/(r*(r-1)*lam))
            bracket = (-je_value + dd/(r-1)
                       - sigma*jd_value/(r-1)
                       + sp.diff(c_coefficient, sigma)*cc
                       - c_coefficient*jc_value)
            self.assertZero(bracket)
            # Removing the tau correction really leaves a nonzero defect.
            bad_coefficient = sigma**2/(r*(r-1))
            bad_bracket = (-je_value + dd/(r-1)
                           - sigma*jd_value/(r-1)
                           + sp.diff(bad_coefficient, sigma)*cc
                           - bad_coefficient*jc_value)
            self.assertZero(bad_bracket - (r-2)*tau*vv/3)
            self.assertNotEqual(sp.expand(bad_bracket), 0)

    def test_rank_one_differential_ratio_and_its_rank_gate(self):
        alpha, beta = sp.symbols("alpha beta")
        lam, speed = sp.symbols("lam speed", nonzero=True)
        c0, c1, c2, c3 = sp.symbols("c0 c1 c2 c3")
        ratio = sp.Symbol("ratio")
        for r in (4, 5):
            for coefficient in (c0, c1, c2, c3):
                value = sp.solve(
                    sp.Eq(ratio*(-lam*speed/(r-2)),
                          -coefficient*speed/r), ratio)[0]
                self.assertZero(value - (r-2)*coefficient/(r*lam))
        tau = alpha**3 + alpha
        cc = sp.Matrix([1, -2, 3, 0])
        ee = sp.Matrix([2, 4, -1, lam])
        k = 3*cc*tau/(5*lam) + ee
        jacobian = k.col_join(sp.Matrix([tau])).jacobian((alpha, beta))
        self.assertEqual(jacobian.rank(), 1)
        self.assertZero(k.jacobian((alpha, beta))
                        - 3*cc*sp.Matrix([tau]).jacobian((alpha, beta))/(5*lam))
        # Values on one direction alone would not certify the rank gate.
        invalid = sp.Matrix([alpha, beta])
        self.assertEqual(invalid.jacobian((alpha, beta)).rank(), 2)

    def test_actual_nice_coordinate_slice_and_both_inverse_orders(self):
        a, b, c, t = sp.symbols("a b c t")
        z1, z2, z3, q = sp.symbols("z1 z2 z3 q")
        x = sp.Matrix([a, b, c, t])
        new = sp.Matrix([z1, z2, z3, q])
        lam = sp.Integer(3)
        sigma = c
        tau = b-c*t/(4*lam)
        coefficient = sigma**2/20 + 3*tau/(10*lam)
        field = sp.Matrix([coefficient, sigma/4, 0, lam])
        forward = sp.Matrix([a-t*coefficient/lam, tau, c, t/lam])
        inverse = sp.Matrix([
            z1 + q*(z3**2/20 + 3*z2/(10*lam)),
            z2 + q*z3/4, z3, lam*q])
        self.assertZero(
            forward.subs(dict(zip(x, inverse)), simultaneous=True) - new)
        self.assertZero(
            inverse.subs(dict(zip(new, forward)), simultaneous=True) - x)
        self.assertZero(field.jacobian(x)*field)
        self.assertZero(sp.Matrix([sigma, tau]).jacobian(x)*field)
        self.assertZero(forward.jacobian(x)*field - sp.Matrix([0, 0, 0, 1]))
        self.assertZero(inverse.diff(q).subs(
            dict(zip(new, forward)), simultaneous=True) - field)

    def test_actual_commuting_split_and_polynomial_integration(self):
        z1, z2, sigma, q = sp.symbols("z1 z2 sigma q")
        a, b, c, t, w = sp.symbols("a b c t w")
        lam = sp.Integer(3)
        old = sp.Matrix([a, b, c, t])
        straight = sp.Matrix([z1, z2, sigma, q])
        inverse = sp.Matrix([
            z1 + q*(sigma**2/20 + 3*z2/(10*lam)),
            z2 + q*sigma/4, sigma, lam*q])
        tau = b-c*t/(4*lam)
        forward = sp.Matrix([
            a-t*(c**2/20+3*tau/(10*lam))/lam, tau, c, t/lam])
        p = sigma**3+z1*sigma+z2**2
        integral = sigma**4/4+z1*sigma**2/2+z2**2*sigma
        self.assertZero(sp.diff(integral, sigma)-p)
        delta_straight = sp.Matrix([0, 0, 1, p])
        z_straight = sp.Matrix([0, 0, 0, 1])
        delta = (inverse.jacobian(straight)*delta_straight).subs(
            dict(zip(straight, forward)), simultaneous=True).applyfunc(sp.expand)
        zz = inverse.diff(q).subs(
            dict(zip(straight, forward)), simultaneous=True).applyfunc(sp.expand)
        self.assertZero(delta.jacobian(old)*zz - zz.jacobian(old)*delta)
        self.assertZero(sp.Matrix([c]).jacobian(old)*delta-sp.Matrix([1]))
        invariant_w = q-integral
        self.assertZero(
            sp.Matrix([invariant_w]).jacobian(straight)*delta_straight)
        final_inverse = inverse.subs(q, w+integral)
        final_forward = forward.copy()
        final_forward[3] = invariant_w.subs(
            dict(zip(straight, forward)), simultaneous=True)
        target = sp.Matrix([z1, z2, sigma, w])
        self.assertZero(
            final_forward.subs(dict(zip(old, final_inverse)),
                               simultaneous=True)-target)
        self.assertZero(
            final_inverse.subs(dict(zip(target, final_forward)),
                               simultaneous=True)-old)


if __name__ == "__main__":
    unittest.main(verbosity=2)
