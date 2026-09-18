"""Independent exact controls for the pass-23 polynomial coefficient theorem.

Only unittest and SymPy are imported. The two-divisor classifier, gauge
normal form, and finite-jet engine are implemented here from their formulas,
not imported from a project solver. Jet multiplication discards inadmissible
f-degrees before multiplying coefficient polynomials.

The examples verify algebraic identities, not the universal DVR-existence,
minimal-denominator, formal-descent, or cancellation arguments.
"""

import unittest

import sympy as sp


f, h, r, x, y, z, t, u = sp.symbols("f h r x y z t u")


def expanded_zero(expression):
    return sp.expand(expression) == 0


def remainder(expression, modulus, variable=r):
    return sp.expand(sp.rem(sp.expand(expression), modulus, variable))


def antiderivative(coefficient):
    polynomial = sp.Poly(sp.expand(coefficient), r)
    return sp.expand(sum(
        value * r**(degree[0] + 1) / (degree[0] + 1)
        for degree, value in polynomial.terms()
    ))


def classify(coefficient, n):
    primitive = antiderivative(coefficient)
    constant = sp.expand(coefficient).subs({f: 0, h: 0, r: 0})
    nu = 2 * n + 1
    rf = remainder(primitive.subs(f, 0), r**5 - h**3)
    rh = remainder(primitive.subs(h, 0), r**2 + f**nu)
    hf = rf.subs(r, 0)
    hh = rh.subs(r, 0)
    first = expanded_zero(rf - constant * r - hf)
    second = expanded_zero(rh - constant * r - hh)
    return {
        "F": primitive, "c": constant, "Rf": rf, "Rh": rh,
        "Hf": hf, "Hh": hh, "f_test": first, "h_test": second,
        "positive": constant != 0 and first and second,
    }


def normal_form(expression, n):
    return remainder(expression, r**2 - x * h + f**(2 * n + 1))


def delta0(expression):
    return sp.expand(2 * r * sp.diff(expression, x) + h * sp.diff(expression, r))


def gauge_reduce(coefficient, n):
    data = classify(coefficient, n)
    if not data["positive"]:
        raise ValueError("The polynomial coefficient fails a necessary test.")
    nu = 2 * n + 1
    jj, _ = sp.div(data["F"].subs(f, 0), r**5 - h**3, r)
    jj = sp.expand(jj)
    g0_numerator = r**5 - h**3 - f**(2 * nu) * r
    delta_f = data["F"] - data["c"] * r - data["Hf"] - data["Hh"]
    reduced = normal_form(delta_f - jj * g0_numerator, n)
    ell = sp.cancel(reduced / h)
    if not ell.is_polynomial(f, h, x, r) or not expanded_zero(ell.subs(f, 0)):
        raise AssertionError("Gauge reduction did not give a polynomial in f*S0.")
    return data, jj, sp.expand(ell), g0_numerator


def jet(expression, precision):
    if precision < 1:
        raise ValueError("Jet precision must be positive.")
    terms = sp.Poly(sp.expand(expression), f).terms()
    return sp.expand(sum(
        coefficient * f**degree[0]
        for degree, coefficient in terms if degree[0] < precision
    ))


def jmul(left, right, precision):
    # Never form the full product before truncation.
    aa = sp.Poly(jet(left, precision), f).as_dict()
    bb = sp.Poly(jet(right, precision), f).as_dict()
    result = {}
    for (da,), ca in aa.items():
        for (db,), cb in bb.items():
            degree = da + db
            if degree < precision:
                result[degree] = result.get(degree, 0) + sp.expand(ca * cb)
    return sp.expand(sum(value * f**degree for degree, value in result.items()))


def jpow(base, exponent, precision):
    result = sp.Integer(1)
    current = jet(base, precision)
    while exponent:
        if exponent & 1:
            result = jmul(result, current, precision)
        exponent //= 2
        if exponent:
            current = jmul(current, current, precision)
    return result


def jsubstitute(expression, images, precision):
    variables = tuple(images)
    terms = sp.Poly(jet(expression, precision), *variables).terms()
    powers = {}
    result = sp.Integer(0)
    for degrees, coefficient in terms:
        term = jet(coefficient, precision)
        for variable, degree in zip(variables, degrees):
            key = (variable, degree)
            if key not in powers:
                powers[key] = jpow(images[variable], degree, precision)
            term = jmul(term, powers[key], precision)
        result = jet(result + term, precision)
    return result


def inverse_pullback(expression, images, precision):
    """Finite additive-operator inverse sum (id - (phi-id) + ...)."""
    term = jet(expression, precision)
    answer = term
    for _ in range(1, precision):
        term = jet(term - jsubstitute(term, images, precision), precision)
        answer = jet(answer + term, precision)
    return answer


def inverse_unit(expression, precision):
    perturbation = jet(expression - 1, precision)
    if not expanded_zero(perturbation.subs(f, 0)):
        raise ValueError("Only units congruent to one modulo f are used.")
    answer = sp.Integer(1)
    term = sp.Integer(1)
    for _ in range(1, precision):
        term = jmul(term, -perturbation, precision)
        answer = jet(answer + term, precision)
    return answer


def divide_f_power(expression, power):
    terms = sp.Poly(sp.expand(expression), f).terms()
    if any(degree[0] < power and coefficient != 0 for degree, coefficient in terms):
        raise AssertionError("A proposed numerator is not f-power divisible.")
    return sp.expand(sum(
        coefficient * f**(degree[0] - power)
        for degree, coefficient in terms if coefficient != 0
    ))


def mixed_coefficient(n):
    nu = 2 * n + 1
    g0_numerator = r**5 - h**3 - f**(2 * nu) * r
    jj = 1 + h**2 + r**2 + f * r
    primitive = (
        3 * r + jj * g0_numerator
        + f * h * (r**3 + h * r**4)
        + f * (r**2 + f**nu) * (r**3 + f * r)
    )
    return sp.expand(sp.diff(primitive, r))


class PolynomialCoefficientChecks(unittest.TestCase):
    def test_constants_zero_and_n_one_boundary(self):
        for n in [1, 2, 3]:
            for constant in [sp.Integer(1), sp.Integer(-2), sp.Rational(3, 5)]:
                self.assertTrue(classify(constant, n)["positive"])
            for coefficient in [sp.Integer(0), f * h, r, 5 * r**4 - f**(4*n+2)]:
                self.assertFalse(classify(coefficient, n)["positive"])
            aa = f**n
            rr = x**3 + aa * y
            hh = aa**2 * z + 2 * aa * x**2 * y + x**5
            vector = [
                2 * aa * rr,
                hh - 6 * x**2 * rr,
                -10*x**4*y - 8*aa*x*y**2 - 2*aa*x**2*z,
            ]
            for value in vector:
                self.assertEqual(sp.expand(value.subs({x: 0, y: 0, f: 0})), 0)

    def test_affine_qr_recovery(self):
        positive_q = [sp.Integer(0), f, f*(1+h), f**2*(1+h**2)]
        negative_q = [sp.Integer(1), h, 1+f, h**3+f*h]
        for n in [1, 2, 3]:
            for qq in positive_q:
                self.assertTrue(classify(1 + qq*r, n)["positive"])
            for qq in negative_q:
                data = classify(1 + qq*r, n)
                self.assertFalse(data["positive"])
                self.assertFalse(data["f_test"])
                self.assertTrue(data["h_test"])

    def test_invariant_coefficient_boundary(self):
        for n in [1, 2]:
            for coefficient in [2 + f*h, -1 + f*h*(f**2+h**3)]:
                self.assertTrue(classify(coefficient, n)["positive"])
            for coefficient in [1+f, 1+h, 1+f**2+h**3]:
                self.assertFalse(classify(coefficient, n)["positive"])

    def test_higher_power_positive_and_negative_remainders(self):
        for n in [1, 2, 3]:
            nu = 2*n+1
            data = classify(1 + f*r**2, n)
            self.assertTrue(data["f_test"])
            self.assertFalse(data["h_test"])
            self.assertEqual(
                sp.expand(sp.diff(data["Rh"], r) - (1-f**(nu+1)/3)), 0
            )
            data = classify(1 + f*r**3, n)
            self.assertTrue(data["positive"])
            self.assertEqual(sp.expand(data["Hh"] - f**(2*nu+1)/4), 0)
            self.assertTrue(classify(1 + f*r**5 + f*h*r**8, n)["positive"])
            # Physical slice existence does not pass to the raw five-ring lift.
            lifted_coefficient = 1 + 5*h*r**4
            lifted = classify(lifted_coefficient, n)
            self.assertTrue(lifted["positive"])
            self.assertEqual(lifted["Rf"], r+h**4)
            self.assertEqual(lifted["Rh"], r)
            for value in [f**n*h, 2*f**n*r, lifted_coefficient]:
                at_fixed_locus = value.subs({f: 0, h: 1})
                self.assertEqual(remainder(at_fixed_locus, r**4+sp.Rational(1, 5)), 0)

    def test_mixed_high_degree_and_gauge_examples(self):
        for n in [1, 2, 3]:
            coefficient = mixed_coefficient(n)
            self.assertTrue(classify(coefficient, n)["positive"])
            self.assertFalse(classify(coefficient + r, n)["positive"])
            self.assertFalse(classify(coefficient + f*r**2, n)["positive"])
            pure_gauge = 1 + 5*r**4 - f**(4*n+2)
            self.assertTrue(classify(pure_gauge, n)["positive"])

    def test_G0_physical_polynomial_identity(self):
        for n in [1, 2, 3]:
            aa = f**n
            nu = 2*n+1
            rr = x**3 + aa*y
            hh = aa**2*z + 2*aa*x**2*y + x**5
            gg = -hh*(x**2*y+aa*z) - 2*x*f**(n+1)*rr
            residual = rr**5 - hh**3 - f**(2*nu)*rr - aa*hh*gg
            self.assertEqual(remainder(residual, f-x*z+y**2, f), 0)
            self.assertEqual(
                sp.expand(x**2*rr-hh+aa*(x**2*y+aa*z)), 0
            )

    def test_exact_gauge_reduction_and_differentiation(self):
        for n in [1, 2, 3]:
            cases = [
                1 + f*r, 1 + f*r**3,
                1 + 5*r**4 - f**(4*n+2), mixed_coefficient(n),
            ]
            for coefficient in cases:
                data, jj, ell, g0_numerator = gauge_reduce(coefficient, n)
                residual = (
                    data["F"] - data["c"]*r - data["Hf"] - data["Hh"]
                    - jj*g0_numerator - h*ell
                )
                self.assertEqual(normal_form(residual, n), 0)
                self.assertEqual(sp.expand(ell.subs(f, 0)), 0)
                derivative_residual = (
                    coefficient - sp.diff(jj*g0_numerator, r)
                    - data["c"] - delta0(ell)
                )
                self.assertEqual(normal_form(derivative_residual, n), 0)
        with self.assertRaises(ValueError):
            gauge_reduce(1 + f*r**2, 1)

    def test_variable_time_invariants_and_localized_inverse(self):
        for n in [1, 2, 3]:
            aa = f**n
            ell = f*(x+r**2) + f**2*x*r
            ll = ell-aa*t
            rho = r+h*ll
            xx = x+2*r*ll+h*ll**2
            coefficient = 1+delta0(ell)

            def action(value):
                return sp.expand(aa*delta0(value)+coefficient*sp.diff(value, t))

            self.assertEqual(action(ll), -aa)
            self.assertEqual(action(rho), 0)
            self.assertEqual(action(xx), 0)
            self.assertEqual(sp.expand(xx*h-rho**2-x*h+r**2), 0)
            sigma0 = -ll/aa
            recovered_r = rho+aa*h*sigma0
            recovered_x = xx+2*aa*rho*sigma0+aa**2*h*sigma0**2
            self.assertEqual(sp.cancel(recovered_r-r), 0)
            self.assertEqual(sp.cancel(recovered_x-x), 0)
            self.assertEqual(sp.cancel(sigma0+ell/aa-t), 0)
        xx0, rr0, ss0, aa0 = sp.symbols("X0 R0 S0 a0")
        old_r = rr0+aa0*h*ss0
        old_x = xx0+2*aa0*rr0*ss0+aa0**2*h*ss0**2
        self.assertEqual(sp.expand(old_r+h*(-aa0*ss0)-rr0), 0)
        self.assertEqual(
            sp.expand(old_x+2*old_r*(-aa0*ss0)+h*(-aa0*ss0)**2-xx0), 0
        )

    def test_finite_jet_inverse_and_polynomial_slice_correction(self):
        for n, ell in [
            (1, f*(x+r)), (2, f*(x+r)), (3, f*r**2+f**2*x),
        ]:
            aa = f**n
            phi = {
                x: jet(x+2*jmul(r, ell, n)+jmul(h, jpow(ell, 2, n), n), n),
                r: jet(r+jmul(h, ell, n), n),
            }
            kk = inverse_pullback(-ell, phi, n)
            self.assertEqual(jet(jsubstitute(kk, phi, n)+ell, n), 0)
            for coordinate in [x, r]:
                inverse_coordinate = inverse_pullback(coordinate, phi, n)
                self.assertEqual(
                    jet(jsubstitute(inverse_coordinate, phi, n)-coordinate, n), 0
                )
            precision = 2*n+1
            ll = jet(ell-aa*t, precision)
            rho = jet(r+jmul(h, ll, precision), precision)
            xx = jet(
                x+2*jmul(r, ll, precision)+jmul(h, jpow(ll, 2, precision), precision),
                precision,
            )
            numerator = jet(
                ell+jsubstitute(kk, {x: xx, r: rho}, precision), precision
            )
            self.assertEqual(jet(numerator, n), 0)
            sigma = jet(t-divide_f_power(numerator, n), n+1)
            e_sigma = jet(
                jmul(aa, delta0(sigma), n+1)
                +jmul(1+delta0(ell), sp.diff(sigma, t), n+1), n+1
            )
            self.assertEqual(e_sigma, 1)
            sigma_mod_a = jet(sigma, n)
            self.assertLessEqual(sp.Poly(sigma_mod_a, t).degree(), 1)
            self.assertEqual(sp.diff(sigma_mod_a, t).subs(f, 0), 1)

    def test_finite_physical_curve_lift_congruences(self):
        for n, ell in [
            (1, f*(x+r)), (2, f*(x+r)), (3, f*r**2+f**2*x),
        ]:
            vv = jet(ell.subs({h: u**5, x: u, r: u**3}, simultaneous=True), n)
            unit0 = jet(1+jmul(u**2, vv, n), n)
            unit = jpow(unit0, 2, n)
            ww = jmul(u**2, unit0, n)
            psi = jmul(u, unit, n)
            inverse_psi = inverse_pullback(u, {u: psi}, n)
            self.assertEqual(jet(jsubstitute(inverse_psi, {u: psi}, n)-u, n), 0)
            self.assertEqual(jet(jsubstitute(psi, {u: inverse_psi}, n)-u, n), 0)
            ratio = jmul(ww, inverse_unit(unit, n), n)
            p_tilde = jsubstitute(ratio, {u: inverse_psi}, n)
            evaluated_p = jsubstitute(p_tilde, {u: psi}, n)
            self.assertEqual(jet(jmul(psi, evaluated_p, n)-jmul(u, ww, n), n), 0)
            self.assertEqual(jet(jmul(psi, jpow(evaluated_p, 2, n), n)-u**5, n), 0)
            self.assertEqual(jet(p_tilde-u**2, 1), 0)

    def test_f_divisor_integral_endpoint_orbit_identities(self):
        x1, x2, time = sp.symbols("x1 x2 time")
        for n in [1, 2]:
            aa = f**n
            nu = 2*n+1
            local_h = []
            for xx in [x1, x2]:
                yy = sp.Integer(0)
                zz = f/xx
                rr = xx**3+aa*yy
                hh = aa**2*zz+2*aa*xx**2*yy+xx**5
                self.assertEqual(sp.cancel(xx*zz-yy**2-f), 0)
                self.assertEqual(rr, xx**3)
                self.assertEqual(sp.cancel(hh-(xx**5+f**nu/xx)), 0)
                local_h.append(hh)
            endpoint1 = x1*h-x1**6-f**nu
            endpoint2 = x2*h-x2**6-f**nu
            self.assertEqual(
                sp.expand(h*(x2-x1)-(x2**6-x1**6)-endpoint2+endpoint1), 0
            )
            orbit_time = (x2**3-x1**3)/(aa*h)
            orbit_x = x1+2*aa*x1**3*orbit_time+aa**2*h*orbit_time**2
            self.assertEqual(
                sp.cancel(h*(orbit_x-x2)-(endpoint1-endpoint2)), 0
            )
            coefficient = 1+r+f*r**2+h*r**3
            primitive = antiderivative(coefficient)
            displacement = (primitive.subs(r, r+aa*h*time)-primitive)/(aa*h)
            self.assertEqual(
                sp.expand(sp.diff(displacement, time)-coefficient.subs(r, r+aa*h*time)),
                0,
            )
            at_endpoint = displacement.subs({r: x1**3, time: orbit_time})
            expected = (primitive.subs(r, x2**3)-primitive.subs(r, x1**3))/(aa*h)
            self.assertEqual(sp.cancel(at_endpoint-expected), 0)
        epsilon = sp.Symbol("epsilon")
        primitive_at_f = u**3+u**6/2
        divided = sp.cancel(
            (primitive_at_f-primitive_at_f.subs(u, epsilon*u))/u**3
        )
        self.assertEqual(divided.subs(u, 0), 1-epsilon**3)
        self.assertEqual(sp.Poly(divided, u).degree(), 3)

    def test_h_divisor_integral_endpoint_orbit_identities(self):
        for n in [1, 2]:
            aa = f**n
            nu = 2*n+1
            for sign in [sp.Integer(1), sp.Integer(-1)]:
                yy = (sign*r-1)/aa
                zz = f+yy**2
                actual_r = 1+aa*yy
                actual_h = aa**2*zz+2*aa*yy+1
                self.assertEqual(sp.cancel(actual_r-sign*r), 0)
                self.assertEqual(sp.cancel(actual_h-r**2-f**nu), 0)
                self.assertEqual(sp.cancel(zz-yy**2-f), 0)
            orbit_time = -2*r/(aa*h)
            self.assertEqual(sp.cancel(r+aa*h*orbit_time+r), 0)
            self.assertEqual(sp.cancel(1+2*aa*r*orbit_time+aa**2*h*orbit_time**2-1), 0)
            for coefficient in [1+f*r**2, mixed_coefficient(n)]:
                primitive = antiderivative(coefficient)
                odd = sp.cancel((primitive-primitive.subs(r, -r))/(2*r))
                gamma = remainder(odd, r**2-h+f**nu)
                self.assertEqual(sp.diff(gamma, r), 0)
                b_remainder = sp.diff(classify(coefficient, n)["Rh"], r)
                self.assertEqual(sp.expand(gamma.subs(h, 0)-b_remainder), 0)
                self.assertEqual(
                    remainder(primitive.subs(r, -r)-primitive+2*r*gamma, r**2-h+f**nu),
                    0,
                )
            bad_b = sp.diff(classify(1+f*r**2, n)["Rh"], r)
            self.assertEqual(bad_b.subs(f, 0), 1)
            self.assertGreater(sp.Poly(bad_b, f).degree(), 0)

    def test_presentation_homotopy_bounded_controls(self):
        parameter, dd = sp.symbols("lambda d")
        for order in range(1, 5):
            pp = dd**order
            gg = sum((-parameter*dd)**j for j in range(order))
            aa = (-parameter)**order
            vv = 1+parameter*dd
            self.assertEqual(sp.expand(pp*aa+vv*gg-1), 0)
            polynomial = sp.Integer(1)
            for iterate in range(1, 4):
                polynomial = sp.expand(sp.diff(polynomial, parameter)-dd*gg*polynomial)
                self.assertEqual(sp.Poly(polynomial, parameter).degree(), iterate*(order-1))
                expected_lc = ((-1)**order*dd**order)**iterate
                self.assertEqual(
                    sp.expand(sp.Poly(polynomial, parameter).LC()-expected_lc), 0
                )
        eta = sp.Symbol("eta")
        for precision in [1, 2, 4]:
            inverse = sum((-parameter*eta)**j for j in range(precision))
            self.assertEqual(
                remainder((1+parameter*eta)*inverse-1, parameter**precision, parameter), 0
            )

    def test_leading_derivation_bounded_controls(self):
        aa, ss = sp.symbols("a s")

        def vector_action(vector, expression):
            return sp.expand(vector[0]*sp.diff(expression, aa)+vector[1]*sp.diff(expression, ss))

        tu = [-2*(ss+aa**2), 1+4*aa*(ss+aa**2)]
        tv = [sp.Integer(1), -2*aa]
        pu = [value.subs(ss, 0) for value in tu]
        pv = tv
        for coordinate, expected in [(aa, 4*aa), (ss, -8*aa**2)]:
            self.assertEqual(vector_action(tu, vector_action(tv, coordinate))
                             -vector_action(tv, vector_action(tu, coordinate)), 0)
            self.assertEqual(sp.expand(
                vector_action(pu, vector_action(pv, coordinate))
                -vector_action(pv, vector_action(pu, coordinate))-expected
            ), 0)
        iterate = aa
        for degree in range(1, 5):
            iterate = vector_action(pu, iterate)
            self.assertEqual(sp.expand(iterate-(-2)**degree*sp.factorial(degree)*aa**(degree+1)), 0)
        bb, cc = sp.symbols("b c")
        beta = bb-aa*ss
        gamma = cc-bb*ss+aa*ss**2/2

        def sliced_action(expression):
            return sp.expand(aa*sp.diff(expression, bb)+bb*sp.diff(expression, cc)
                             +sp.diff(expression, ss))

        self.assertEqual(sliced_action(beta), 0)
        self.assertEqual(sliced_action(gamma), 0)
        self.assertEqual(sliced_action(ss), 1)
        self.assertEqual(sp.gcd(aa, bb), 1)
        self.assertEqual(aa.subs(aa, 0), 0)
        self.assertEqual(bb.subs(bb, 0), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
