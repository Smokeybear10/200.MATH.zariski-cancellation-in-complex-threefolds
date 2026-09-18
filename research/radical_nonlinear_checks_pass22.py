"""Independent finite exact controls for the all-q slice classification.

Only unittest and SymPy are imported. These controls do not prove the
universal curve/dimension argument, minimality, novelty, or cancellation.
"""

import unittest
import sympy as sp


f, a, q, h, x, r, t, u = sp.symbols("f a q h x r t u")
Xv, Rv, Sv = sp.symbols("X R S")
L = q*x/2-a*t
RHO = sp.expand(r+h*L)
BIGX = sp.expand(x+L*(r+RHO))
SIGMA0 = sp.expand(t+q*(BIGX-x)/(2*a))
K = q**2*x*r/2+q**3*x**2*h/8


def trunc(expr, n):
    return sp.Add(*(coefficient*f**power[0]
                    for power, coefficient in sp.Poly(sp.expand(expr), f).terms()
                    if power[0] < n))


def compose(expr, values, n=None):
    if n is None:
        return expr.subs(values, simultaneous=True).expand()
    # Compose inside the finite quotient. Expanding an untruncated high
    # power first creates irrelevant terms of exponentially growing size.
    variables = tuple(values)
    powers = {(v, 0): sp.Integer(1) for v in variables}

    def power(v, exponent):
        if (v, exponent) not in powers:
            if exponent % 2:
                powers[v, exponent] = trunc(values[v]*power(v, exponent-1), n)
            else:
                powers[v, exponent] = trunc(power(v, exponent//2)**2, n)
        return powers[v, exponent]

    result = sp.Integer(0)
    for monomial, coefficient in sp.Poly(sp.expand(expr), *variables).terms():
        term = trunc(coefficient, n)
        for variable, exponent in zip(variables, monomial):
            term = trunc(term*power(variable, exponent), n)
        result += term
    return trunc(result, n)


def derivative(expr, av=a, qv=q):
    return sp.expand(2*av*r*sp.diff(expr, x)+av*h*sp.diff(expr, r)
                     +(1+qv*r)*sp.diff(expr, t))


def inverse_operator(expr, images, n):
    """Finite additive inverse of a substitution congruent to identity mod f."""
    current = trunc(expr, n)
    total = current
    for index in range(1, n):
        current = trunc(compose(current, images, n)-current, n)
        total += (-1)**index*current
    return trunc(total, n)


def repaired(n, qv):
    subs = {a: f**n, q: qv}
    bigx, rho, sigma0 = [compose(v, subs) for v in (BIGX, RHO, SIGMA0)]
    phi = {x: trunc(bigx, n), r: trunc(rho, n)}
    kval = trunc(compose(K, subs), n)
    correction = inverse_operator(kval, phi, n)
    numerator = sp.expand(f**n*sigma0-compose(correction, {x: bigx, r: rho}))
    sigma = sp.cancel(numerator/f**n).expand()
    return bigx, rho, sigma, correction, phi, kval, numerator


class RadicalNonlinearChecks(unittest.TestCase):
    def zero(self, value):
        self.assertEqual(sp.cancel(sp.expand(value)), 0)

    def test_generic_invariants_and_preserved_level(self):
        self.zero(derivative(BIGX))
        self.zero(derivative(RHO))
        self.zero(BIGX*h-RHO**2-(x*h-r**2))

    def test_rational_slice_two_independent_expressions(self):
        displayed = (t-q*r*t-q**2*x*h*t/2+a*h*q*t**2/2
                     +q**2*x*r/(2*a)+q**3*x**2*h/(8*a))
        self.zero(SIGMA0-displayed)
        self.zero(derivative(displayed)-1)

    def test_cubic_formula_derivative_and_degree(self):
        cubic = sp.expand(SIGMA0-q**2*BIGX*RHO/(2*a))
        displayed = (a**2*h**2*q**2*t**3/2
            +(-3*a*h**2*q**3*x/4-3*a*h*q**2*r/2+a*h*q/2)*t**2
            +(3*h**2*q**4*x**2/8+3*h*q**3*r*x/2+q**2*r**2-q*r+1)*t
            -h**2*q**5*x**3/(16*a)-3*h*q**4*r*x**2/(8*a)
            -h*q**3*x**2/(8*a)-q**3*r**2*x/(2*a))
        self.zero(cubic-displayed)
        self.zero(derivative(cubic)-1)
        self.assertEqual(sp.Poly(cubic, t).degree(), 3)
        self.zero(sp.Poly(cubic, t).LC()-a**2*h**2*q**2/2)
        for n, ell in ((3, 1), (5, 2), (6, 2), (8, 3)):
            candidate = sp.cancel(cubic.subs({a: f**n, q: f**ell*(1+h)}))
            self.assertTrue(candidate.is_polynomial(f, h, x, r, t))

    def test_finite_quotient_inverse_both_directions(self):
        for n, qv in ((3, f), (4, f*(1+h)), (5, f**2*(1+h+f))):
            with self.subTest(n=n, q=qv):
                phi = {x: trunc(BIGX.subs({a: f**n, q: qv}), n),
                       r: trunc(RHO.subs({a: f**n, q: qv}), n)}
                inverse = {v: inverse_operator(v, phi, n) for v in (x, r)}
                for v in (x, r):
                    self.zero(compose(inverse[v], phi, n)-v)
                    self.zero(compose(phi[v], inverse, n)-v)

    def test_correction_numerator_and_unit_slope(self):
        for n, qv in ((3, f), (4, f), (3, f*(1+h)), (4, f*(1+h))):
            with self.subTest(n=n, q=qv):
                _, _, sigma, correction, phi, kval, numerator = repaired(n, qv)
                self.zero(compose(correction, phi, n)-kval)
                self.zero(trunc(numerator, n))
                self.assertTrue(sigma.is_polynomial(f, h, x, r, t))
                self.zero(derivative(sigma, f**n, qv)-1)
                reduced = trunc(sigma, n)
                self.assertEqual(sp.Poly(reduced, t).degree(), 1)
                self.zero(trunc(sp.diff(reduced, t)*(1+qv*r)-1, n))

    def test_global_repaired_inverse_both_directions(self):
        n, qv = 3, f
        bigx, rho, sigma, correction, _, _, _ = repaired(n, qv)
        correction_target = compose(correction, {x: Xv, r: Rv})
        old_slice = Sv+correction_target/f**n
        inverse_l = f**n*old_slice-qv*Xv/2
        old_r = Rv+h*inverse_l
        old_x = Xv+inverse_l*(old_r+Rv)
        old_t = (old_slice+qv*old_slice*(old_r+Rv)/2
                 -qv**2*Xv*(old_r+Rv)/(4*f**n))
        inv = {x: sp.cancel(old_x).expand(), r: sp.cancel(old_r).expand(),
               t: sp.cancel(old_t).expand()}
        for expression in inv.values():
            self.assertTrue(expression.is_polynomial(f, h, Xv, Rv, Sv))
        forward = {Xv: bigx, Rv: rho, Sv: sigma}
        for source, expression in inv.items():
            self.zero(compose(expression, forward)-source)
        for expression, target in ((bigx, Xv), (rho, Rv), (sigma, Sv)):
            self.zero(compose(expression, inv)-target)

    def test_physical_curve_forward_and_inverse_jets(self):
        for n, qv in ((3, f), (4, f*(1+h)), (5, f**2*(1+h+f))):
            with self.subTest(n=n, q=qv):
                qu = qv.subs(h, u**5)
                unit = trunc((1+qu*u**3/2)**2, n)
                w = trunc(u**2*(1+qu*u**3/2), n)
                psi = trunc(u*unit, n)
                invpsi = inverse_operator(u, {u: psi}, n)
                invunit = trunc(sum((1-unit)**j for j in range(n)), n)
                ptilde = compose(trunc(w*invunit, n), {u: invpsi}, n)
                self.zero(compose(invpsi, {u: psi}, n)-u)
                self.zero(compose(psi, {u: invpsi}, n)-u)
                pcurve = compose(ptilde, {u: psi}, n)
                self.zero(trunc(psi*pcurve-u*w, n))
                self.zero(trunc(psi*pcurve**2-u**5, n))
                self.zero(trunc(invpsi.subs(u, 0), n))

    def test_cubic_correction_is_valid_exactly_at_needed_order(self):
        phi = {x: BIGX.subs(a, 0), r: RHO.subs(a, 0)}
        residue = sp.Poly(sp.expand(compose(q**2*x*r/2, phi)-K), q)
        self.assertGreaterEqual(min(power[0] for power, _ in residue.terms()), 3)

    def test_low_degree_basis_and_derivatives(self):
        powers = [0, 3, 1, 4, 2]
        self.assertEqual(sorted(powers), list(range(5)))
        basis = (sp.Integer(1), r, x, x*r, x**2)
        for degree, element in enumerate(basis):
            value = element
            for _ in range(degree):
                value = derivative(value)
            self.assertNotEqual(value, 0)
            self.zero(derivative(value))
        self.zero(derivative(x*r).subs(r**2, x*h-f**7)-(3*a*h*x-2*a*f**7))
        self.zero(derivative(x**2)-4*a*x*r)

    def test_quadratic_coefficient_comparison(self):
        U, b0, c1, c2, c3, c4, v = sp.symbols("U b0 c1 c2 c3 c4 v")
        biga = a*h*U
        bigb = b0-2*U*r-h*q*U*x
        self.zero(derivative(bigb)+2*biga*(1+q*r))
        expected = 1-b0-2*U*q*v+(2*U-b0*q)*r+3*h*q*U*x+h*q**2*U*x*r
        actual = sp.expand(1-bigb*(1+q*r)).subs(r**2, x*h-v).expand()
        self.zero(actual-expected)
        coeff_c = c1*r+c2*x+c3*x*r+c4*x**2
        remaining = sp.expand(derivative(coeff_c)).subs(r**2, x*h-v)
        solved = {c3: q*U/a, c2: (2*U-b0*q)/(2*a),
                  c1: (1-b0)/(a*h), c4: h*q**2*U/(4*a)}
        self.zero(remaining.subs(solved)-expected)

    def test_affine_and_zero_coefficient_boundaries(self):
        self.zero(derivative(t-q*x/(2*a))-1)
        for n in (1, 2, 4):
            _, _, sigma, _, _, _, _ = repaired(n, sp.Integer(0))
            self.zero(sigma-t)
        affine = (t-q*x/(2*a)).subs({a: f**3, q: f**2})
        self.assertFalse(sp.cancel(affine).is_polynomial(f, x, t))

    def test_orbit_endpoints_and_zero_t_displacement(self):
        r1, r2, v = sp.symbols("r1 r2 v")
        tau = (r2-r1)/(a*h)
        x1 = (r1**2+v)/h
        x2 = (r2**2+v)/h
        self.zero(r1+a*h*tau-r2)
        self.zero(x1+2*a*r1*tau+a**2*h*tau**2-x2)
        displacement = tau*(1+q*r1)+q*a*h*tau**2/2
        self.zero(displacement-tau*(1+q*(r1+r2)/2))
        self.zero(displacement.subs(q, -2/(r1+r2)))

    def test_multiple_root_control_does_not_need_hensel(self):
        polynomial = 2-sp.Rational(16, 5)*x**3+sp.Rational(6, 5)*x**8
        self.zero(polynomial.subs(x, 1))
        self.zero(sp.diff(polynomial, x).subs(x, 1))
        self.assertNotEqual(sp.diff(polynomial, x, 2).subs(x, 1), 0)
        self.assertNotEqual(polynomial, 0)
        self.assertEqual(polynomial.subs(x, 0), 2)

    def test_center_first_order_obstruction(self):
        alpha, b = sp.symbols("alpha b")
        residue = (h*(b-alpha*r)-6*x**2*r*b+6*alpha*h*x**3)
        self.zero(residue.subs({h: x**5, r: x**3})-5*x**5*(alpha*x**3-b))
        self.zero(f**2*h*h+(1-f*h)*(1+f*h)-1)

    def test_projected_curved_and_flat_connections(self):
        av, bv = sp.symbols("av bv")
        conormal = sp.Matrix([[-2*av, 0, 0, 1]])
        tangent = sp.Matrix([1, 0, 0, 2*av])
        normal_curved = sp.Matrix([bv, 0, 0, 1+2*av*bv])
        normal_flat = sp.Matrix([-sp.Rational(1, 2), 0, 0, 1-av])
        for normal, coefficient in ((normal_curved, -2*bv), (normal_flat, 1)):
            projection = sp.eye(4)-normal*conormal
            self.assertEqual((projection**2-projection).applyfunc(sp.expand), sp.zeros(4))
            self.assertEqual((projection*tangent.diff(av)-coefficient*tangent).applyfunc(sp.expand), sp.zeros(4, 1))
        self.zero(-sp.diff(-2*bv, bv)-2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
