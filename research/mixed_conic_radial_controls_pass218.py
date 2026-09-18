"""Finite exact-algebra controls for the mixed-conic restrictions, pass218.

The author does not execute, import, or compile the saved source.
These controls do not prove actual chart existence, field return,
integration completeness, universal root-order arguments, or recognition.
All coefficient-field fixtures are formal, not claimed actual frames.
No retained checker or solver implementation is imported.
"""

import unittest

import sympy as sp


h, rho = sp.symbols("h rho", nonzero=True)
X, xi, U, V = sp.symbols("X xi U V")


def dt(expression):
    """Original t partial, expressed in the exact (h,rho) coefficients."""
    return sp.diff(expression, h) / rho


def dr_original(expression):
    """Original rho partial fixes t=h*rho, not h."""
    return sp.diff(expression, rho) - h * sp.diff(expression, h) / rho


def repeated(operator, expression, count):
    for _ in range(count):
        expression = operator(expression)
    return expression


def hj(coefficient, order):
    return sum(
        repeated(dt, repeated(dr_original, coefficient, order - i), i)
        * U**i * V**(order - i)
        / (sp.factorial(i) * sp.factorial(order - i))
        for i in range(order + 1)
    )


def raw_potentials(k, n, ell, m):
    q = h**2 * rho
    second = hj(q, 2) + hj(k, 1) + n
    ret = sp.diff(second, V)
    third = hj(q, 3) + hj(k, 2) + hj(n, 1)
    middle = dr_original(second)
    fourth = (hj(q, 4) + hj(k, 3) + hj(n, 2)
              - dt(ell) * U - dr_original(ell) * V - m)
    return second, ret, third, middle, fourth


def determinant(*columns):
    return sp.Matrix.hstack(*columns).det()


class MixedConicRadialControls(unittest.TestCase):
    def assert_zero(self, expression):
        self.assertEqual(sp.factor(sp.together(sp.expand(expression))), 0)

    def test_radial_integration_highest_jacobian_and_raw_cubic(self):
        C, F, G = [sp.Function(name)(h) for name in ("C", "F", "G")]
        delta = sp.Function("delta")(h, rho)
        arbitrary = sp.Function("arbitrary")(h, rho)
        self.assert_zero(dt(dr_original(arbitrary)) - dr_original(dt(arbitrary)))
        self.assert_zero(h * dt(arbitrary) + dr_original(arbitrary)
                         - sp.diff(arbitrary, rho))
        k = C / rho + F * rho + G
        radial_k2 = sp.diff(k, rho, 2) / 2
        self.assert_zero(rho**3 * radial_k2 - C)
        self.assert_zero(sp.diff(k, rho) + C / rho**2 - F)
        self.assert_zero(k - C / rho - F * rho - G)
        self.assert_zero(sp.diff(k, rho, 3) + 6 * radial_k2 / rho)
        alpha = rho / C
        self.assert_zero(alpha - 1 / (radial_k2 * rho**2))

        column = sp.Matrix([h, F + h**2 * (X - delta), X + delta])
        a2 = alpha * column
        highest = determinant(a2.diff(h), a2.diff(rho), 2 * a2)
        M = h * sp.diff(F, h) - F - 2 * h**2 * delta
        self.assert_zero(highest - 2 * alpha**3 * sp.diff(delta, rho) * M)
        self.assert_zero(sp.diff(M, rho) + 2 * h**2 * sp.diff(delta, rho))

        n = sp.Function("n")(h, rho)
        ell, m = sp.symbols("ell m")
        _, ret, third, _, _ = raw_potentials(k, n, ell, m)
        bb, cc, dd, ee, ff = sp.symbols("bb cc dd ee ff")
        theta = alpha * xi**2 + bb * xi + cc
        w = dd * xi**2 + ee * xi + ff
        at_graph = {U: xi + h * theta, V: theta}
        third_row = sp.expand(ret.subs(at_graph, simultaneous=True) * w
                              + third.subs(at_graph, simultaneous=True) - ell)
        expected = (-2 * h * dd / rho
                    + (bb - 2 * sp.diff(C, h) / C) / rho**2
                    - sp.diff(G, h) / (C * rho))
        self.assert_zero(third_row.coeff(xi, 4))
        self.assert_zero(third_row.coeff(xi, 3) - expected)
        b_value = (2 * sp.diff(C, h) + sp.diff(G, h) * rho
                   + 2 * h * delta * rho**2) / C
        self.assert_zero(expected.subs({bb: b_value, dd: alpha * delta}))

    def test_complete_fourth_jacobian_coefficient_and_square_root_boundary(self):
        # Independent polynomial column jets show that no constant column
        # can contribute to xi^4. This is an algebra identity, not calibration.
        vector = lambda name: sp.Matrix(sp.symbols(f"{name}_0:3"))
        a2, a1 = vector("a2"), vector("a1")
        a2h, a2r, a1h, a1r = [vector(name) for name in ("a2h", "a2r", "a1h", "a1r")]
        a0h, a0r = vector("a0h"), vector("a0r")
        raw = determinant(a2h * xi**2 + a1h * xi + a0h,
                          a2r * xi**2 + a1r * xi + a0r, 2 * a2 * xi + a1)
        three_terms = (determinant(a2h, a2r, a1)
                       + 2 * determinant(a2h, a1r, a2)
                       + 2 * determinant(a1h, a2r, a2))
        self.assert_zero(sp.expand(raw).coeff(xi, 4) - three_terms)

        C, F, G, delta = [sp.Function(name)(h) for name in ("C", "F", "G", "delta")]
        epsilon = sp.Function("epsilon")(h, rho)
        alpha = rho / C
        b = (2 * sp.diff(C, h) + sp.diff(G, h) * rho
             + 2 * h * delta * rho**2) / C
        e = b * delta + epsilon
        k = C / rho + F * rho + G
        column = sp.Matrix([h, F + h**2 * (X - delta), X + delta])
        direction = sp.Matrix([0, -h**2, 1])
        unit_z = sp.Matrix([0, 1, 0])
        a2 = alpha * column
        a1 = sp.Matrix([1 + h * b,
                        dt(k) + sp.diff(k, rho) * b - h**2 * e + (h**2 * b + 2*h) * X,
                        e + b * X])
        decomposition = (b * column + column.diff(h)
                         + (epsilon - sp.diff(delta, h)) * direction
                         - sp.diff(C, h) * unit_z / rho**2)
        for value in a1 - decomposition:
            self.assert_zero(value)
        self.assert_zero(determinant(a1.diff(h), a2.diff(rho), a2))
        full_fourth = (determinant(a2.diff(h), a2.diff(rho), a1)
                       + 2 * determinant(a2.diff(h), a1.diff(rho), a2)
                       + 2 * determinant(a1.diff(h), a2.diff(rho), a2))
        M = h * sp.diff(F, h) - F - 2 * h**2 * delta
        T = X + delta - h * sp.diff(delta, h)
        self.assert_zero(determinant(column.diff(h), direction, column) - M)
        self.assert_zero(determinant(column.diff(h), unit_z, column) - T)
        expected = alpha**2 * (
            M * (2 * sp.diff(epsilon, rho) - epsilon / rho + sp.diff(delta, h) / rho)
            + 5 * sp.diff(C, h) * T / rho**3)
        self.assert_zero(full_fourth - expected)
        self.assert_zero(sp.diff(expected, X) - 5 * sp.diff(C, h) / (rho * C**2))
        # The fourth coefficient alone admits this formal nonconstant mode.
        root_mode = sp.sqrt(rho)
        self.assert_zero(2 * rho * sp.diff(root_mode, rho) - root_mode)
        self.assert_zero(sp.diff(root_mode**2 / rho, rho))
        self.assertNotEqual(sp.diff(root_mode, rho), 0)

    def test_raw_moving_point_column_after_differentiation(self):
        C = sp.symbols("C", nonzero=True)
        F, G, delta = [sp.Function(name)(h) for name in ("F", "G", "delta")]
        epsilon, cc, ff, nn = [sp.Function(name)(h, rho)
                              for name in ("epsilon", "c", "f", "n")]
        alpha = rho / C
        b = (sp.diff(G, h) * rho + 2 * h * delta * rho**2) / C
        k = C / rho + F * rho + G
        theta = alpha * xi**2 + b * xi + cc
        y = xi + h * theta
        w = alpha * delta * xi**2 + (b * delta + epsilon) * xi + ff
        z = -h**2 * w + xi**2 / rho + dt(k) * xi + sp.diff(k, rho) * theta + nn
        sigma = h**2 * theta + 2 * h * xi + k
        original = sp.Matrix([y + h * rho * X,
                              z + sigma * X + h**2 * rho * X**2,
                              w + theta * X + rho * X**2])
        point_xi = -C / (2 * h * rho) - b / (2 * alpha)
        point_x = h * epsilon - delta
        self.assert_zero(point_xi + C / (2*h*rho) + sp.diff(G, h)/2 + h*delta*rho)
        M = h * sp.diff(F, h) - F - 2 * h**2 * delta
        # Differentiate RAW original columns first. No derivative of the
        # chosen coefficient-field point is taken in this substitution.
        evaluated = original.diff(xi).subs({xi: point_xi, X: point_x}, simultaneous=True)
        for value, target in zip(evaluated, [0, M / h, 0]):
            self.assert_zero(value - target)
        ret = dr_original(k) - 2 * h * xi / rho
        self.assert_zero(ret.subs(xi, point_xi) + M)
        first, second = sp.Matrix(sp.symbols("first0:3")), sp.Matrix(sp.symbols("second0:3"))
        self.assert_zero(determinant(first, second, sp.zeros(3, 1)))

    def test_exact_return_gradient_and_finite_root_orders(self):
        C = sp.symbols("C", nonzero=True)
        F, G, delta = [sp.Function(name)(h) for name in ("F", "G", "delta")]
        cc = sp.symbols("cc")
        k = C / rho + F * rho + G
        b = (sp.diff(G, h) * rho + 2 * h * delta * rho**2) / C
        theta = rho * xi**2 / C + b * xi + cc
        p = sp.diff(theta, xi)
        M = h * sp.diff(F, h) - F - 2 * h**2 * delta
        ret = dr_original(k) - 2 * h * xi / rho
        self.assert_zero(dr_original(k) + M + C * (1 + h * b) / rho**2)
        self.assert_zero(1 + h * p + rho**2 * (ret + M) / C)
        root = rho * dr_original(k) / (2*h)
        self.assert_zero(ret.subs(xi, root))
        self.assert_zero((1 + h*p).subs(xi, root) + rho**2 * M / C)

        rr, bb, c1, lt, lr = sp.symbols("rr bb c1 lt lr")
        hu = -rr * (c1 * bb + rr * lt)
        hv = -rr * (c1**2 + rr * lr)
        q1 = h * hu + hv
        self.assert_zero(q1 + rr * (c1 * (h*bb+c1) + rr*(h*lt+lr)))
        aa, pp = sp.symbols("aa pp")
        root_values = {bb: -aa * pp, c1: aa * (1+h*pp)}
        self.assert_zero(sp.cancel(q1 / rr).subs(root_values).subs(rr, 0)
                         + aa**2 * (1+h*pp))
        # Formal simple-root models only. The upper bound q1|R^2 and
        # the nonzero scalar wedge are written actual hypotheses.
        x, root0, unit = sp.symbols("x root0 unit", nonzero=True)
        linear = x - root0
        self.assert_zero((unit * linear).subs(x, root0))
        self.assert_zero(sp.diff(unit * linear, x).subs(x, root0) - unit)
        self.assert_zero(sp.diff(unit * linear**2, x).subs(x, root0))
        self.assert_zero(sp.diff(unit * linear**2, x, 2).subs(x, root0) - 2*unit)
        # In the M=0 branch, p=-1/h makes the tangent identity force C1=0.
        tangent = bb * (1+h*pp) + c1*pp
        self.assert_zero(tangent.subs(pp, -1/h) + c1/h)
        cbar = sp.symbols("cbar")
        self.assert_zero(hu.subs(c1, rr*cbar) + rr**2 * (cbar*bb+lt))
        first, last = sp.Matrix(sp.symbols("first0:3")), sp.Matrix(sp.symbols("last0:3"))
        self.assert_zero(determinant(first, sp.zeros(3, 1), last))

    def test_raw_lower_coefficients_integrals_and_distinct_radial_weights(self):
        C = sp.symbols("C", nonzero=True)
        F, G, delta, c0, n0 = [sp.Function(name)(h)
                              for name in ("F", "G", "delta", "c0", "n0")]
        epsilon, cc, ff, n, ell, m = [sp.Function(name)(h, rho)
                                     for name in ("epsilon", "c", "f", "n", "ell", "m")]
        k = C / rho + F * rho + G
        alpha = rho / C
        b = (sp.diff(G, h) * rho + 2*h*delta*rho**2) / C
        d, e = alpha * delta, b * delta + epsilon
        theta = alpha * xi**2 + b * xi + cc
        w = d * xi**2 + e * xi + ff
        _, ret, third, middle, fourth = raw_potentials(k, n, ell, m)
        to_radial = {U: xi + h*V}
        ret_r = ret.subs(to_radial)
        third_r = third.subs(to_radial)
        middle_r = middle.subs(to_radial)
        fourth_r = fourth.subs(to_radial)
        R0 = F - h*sp.diff(F, h) - h*sp.diff(G, h)/rho - C/rho**2
        self.assert_zero(ret_r + 2*h*xi/rho - R0)
        third_literal = (C*V**2/rho**3 - xi**2*V/rho**2
                         - sp.diff(G, h)*xi*V/rho**2 + dt(dt(k))*xi**2/2
                         + sp.diff(n, rho)*V + sp.diff(n, h)*xi/rho)
        middle_literal = (-xi**2/rho**2 + 2*h*xi*V/rho**2
                          + dr_original(dt(k))*xi + sp.diff(R0, rho)*V
                          + sp.diff(n, rho) - h*sp.diff(n, h)/rho)
        fourth_literal = (
            xi**2*V**2/rho**3 - C*V**3/rho**4 + sp.diff(G, h)*xi*V**2/rho**3
            + (-sp.diff(F, h, 2)/(2*rho**2) - sp.diff(G, h, 2)/rho**3)*xi**2*V
            + (sp.diff(F, h, 3)/rho**2 + sp.diff(G, h, 3)/rho**3)*xi**3/6
            + sp.diff(n, rho, 2)*V**2/2
            + (sp.diff(n, h, rho)/rho - sp.diff(n, h)/rho**2)*xi*V
            + sp.diff(n, h, 2)*xi**2/(2*rho**2)
            - sp.diff(ell, h)*xi/rho - sp.diff(ell, rho)*V - m
        )
        self.assert_zero(third_r - third_literal)
        self.assert_zero(middle_r - middle_literal)
        self.assert_zero(fourth_r - fourth_literal)
        third_row = sp.expand(ret_r*w + third_r.subs(V, theta) - ell)
        fourth_row = sp.expand(h**2*w**2/rho + middle_r.subs(V, theta)*w
                               + fourth_r.subs(V, theta))
        for degree in (3, 4):
            self.assert_zero(third_row.coeff(xi, degree))
        for degree in (5, 6):
            self.assert_zero(fourth_row.coeff(xi, degree))
        s2 = (-2*h*e/rho + R0*d + C*b**2/rho**3 + cc/rho**2
              - sp.diff(G, h)*b/rho**2 + dt(dt(k))/2 + alpha*sp.diff(n, rho))
        s1 = (R0*e - 2*h*ff/rho + (2*C*b/rho**3-sp.diff(G,h)/rho**2)*cc
              + b*sp.diff(n, rho) + sp.diff(n, h)/rho)
        self.assert_zero(third_row.coeff(xi, 2) - s2)
        self.assert_zero(third_row.coeff(xi, 1) - s1)
        self.assert_zero(third_row.coeff(xi, 0)
                         - (R0*ff+C*cc**2/rho**3+sp.diff(n,rho)*cc-ell))

        j3 = 2*h*alpha/rho**2
        j2 = -1/rho**2 + 2*h*b/rho**2 + sp.diff(R0,rho)*alpha
        j1 = 2*h*cc/rho**2 + dr_original(dt(k)) + sp.diff(R0,rho)*b
        L2 = -sp.diff(F,h,2)/(2*rho**2) - sp.diff(G,h,2)/rho**3
        L3 = sp.diff(F,h,3)/(6*rho**2) + sp.diff(G,h,3)/(6*rho**3)
        k4_convolution = (
            h**2*d**2/rho+j3*e+j2*d+(b**2+2*alpha*cc)/rho**3
            -3*C*(alpha**2*cc+alpha*b**2)/rho**4
            +2*sp.diff(G,h)*alpha*b/rho**3+L2*alpha+sp.diff(n,rho,2)*alpha**2/2
        )
        k3_convolution = (
            2*h**2*d*e/rho+j3*ff+j2*e+j1*d+2*b*cc/rho**3
            -C*(b**3+6*alpha*b*cc)/rho**4+sp.diff(G,h)*(b**2+2*alpha*cc)/rho**3
            +L2*b+L3+sp.diff(n,rho,2)*alpha*b
            +(sp.diff(n,h,rho)/rho-sp.diff(n,h)/rho**2)*alpha
        )
        self.assert_zero(fourth_row.coeff(xi, 4) - k4_convolution)
        self.assert_zero(fourth_row.coeff(xi, 3) - k3_convolution)
        nprime = (
            delta*(h*sp.diff(F,h)-F)+h*delta*sp.diff(G,h)/rho
            +(C*delta-C*sp.diff(F,h,2)/2+2*C*h*epsilon)/rho**2
            -(C*cc+C*sp.diff(G,h,2)/2)/rho**3
        )
        self.assert_zero(s2.subs(sp.diff(n,rho), nprime))
        k4_reduced = k4_convolution.subs(sp.diff(n,rho,2), sp.diff(nprime,rho))
        k4_expected = (
            4*C*h*rho**2*sp.diff(epsilon,rho)-2*C*rho*sp.diff(cc,rho)
            +2*C*cc-C*sp.diff(G,h,2)+4*h**2*rho**3*delta**2
            +2*h*rho**2*delta*sp.diff(G,h)
        )/(4*C**2*rho**2)
        self.assert_zero(k4_reduced-k4_expected)
        c_value = (2*h*rho*epsilon+sp.diff(G,h,2)/2+h**2*delta**2*rho**3/C
                   +h*delta*sp.diff(G,h)*rho**2/C+c0*rho)
        self.assert_zero(k4_expected.subs(cc,c_value).doit())
        integral = (cc/rho-2*h*epsilon-sp.diff(G,h,2)/(2*rho)
                    -h**2*delta**2*rho**2/C-h*delta*sp.diff(G,h)*rho/C)
        self.assert_zero(integral.subs(cc,c_value)-c0)
        A0 = delta*(h*sp.diff(F,h)-F)-h**2*delta**2
        B0 = delta-sp.diff(F,h,2)/2-c0
        n_value = A0*rho-C*B0/rho+C*sp.diff(G,h,2)/(2*rho**2)+n0
        self.assert_zero(nprime.subs(cc,c_value)-sp.diff(n_value,rho))
        f_value = rho/(2*h)*(
            R0*e+(2*C*b/rho**3-sp.diff(G,h)/rho**2)*c_value
            +b*sp.diff(n_value,rho)+sp.diff(n_value,h)/rho)
        self.assert_zero(s1.subs({cc:c_value,ff:f_value,n:n_value},
                                simultaneous=True).doit())
        # The raw xi^3 coefficient still includes every lower function here.
        # Only proved c,n,f formulas are substituted; epsilon and n0 stay free.
        lower = fourth_row.coeff(xi,3).subs(
            {cc:c_value,ff:f_value,n:n_value},simultaneous=True).doit()
        M = h*sp.diff(F,h)-F-2*h**2*delta
        astar = sp.diff(F,h,3)/3+sp.diff(c0-sp.diff(G,h)**2/(4*C),h)-sp.diff(delta,h)
        expected = -M*(epsilon-sp.diff(delta,h))/C-astar/rho**2-5*sp.diff(G,h,3)/(6*rho**3)
        self.assert_zero(lower-expected)
        radial_rhs = -C*astar/rho**2-5*C*sp.diff(G,h,3)/(6*rho**3)
        self.assert_zero(2*rho*sp.diff(radial_rhs,rho)-radial_rhs
                         -5*C*astar/rho**2-35*C*sp.diff(G,h,3)/(6*rho**3))
        self.assert_zero(sp.diff(astar*rho+7*sp.diff(G,h,3)/6,rho)-astar)
        g2,g1,g0,gamma = sp.symbols("g2 g1 g0 gamma")
        g_value = g2*h**2+g1*h+g0
        c0_value = delta-sp.diff(F,h,2)/3+sp.diff(g_value,h)**2/(4*C)+gamma
        self.assert_zero(astar.subs({G:g_value,c0:c0_value},simultaneous=True).doit())
        self.assert_zero(sp.diff(g_value,h,3))


if __name__ == "__main__":
    unittest.main()
