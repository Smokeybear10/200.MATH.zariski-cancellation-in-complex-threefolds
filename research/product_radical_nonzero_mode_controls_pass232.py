"""Finite exact-algebra controls for the bounded nonzero-mode proof232.

No retained proof, checker, or solver is imported. The actual map is rebuilt
before coefficient extraction. Algebraic differentiation uses eta**2=gamma*t.
These controls do not prove the actual chart, finite-field integration
completeness, the nonvertex theorem231, or any cancellation conclusion.
Authoring is source-only; the parent owns the sole canonical execution.
"""

import itertools
import unittest
from functools import lru_cache

import sympy as sp


t, s, x, X, eta = sp.symbols("t s x X eta", nonzero=True)
PERMUTATIONS = tuple(itertools.permutations(range(3)))


def raw_map(y, w, h, k, n, dt, ds):
    """Literal first/second-potential map, holding original X fixed."""
    return (
        y + t * X,
        w / (2 * s) + dt(k) * y - h**2 / (8 * s**3 * t**3)
        - ds(k) * h / (2 * s * t**2) + n
        + (s * y - h / (2 * s * t) + k) * X + s * t * X**2,
        w + (s**2 * y - h / t) * X + s**2 * t * X**2,
    )


def derivative_coefficients(raw, dt, ds):
    """Rows are Y,Z,W; columns are exact t,s,x derivatives."""
    return [
        [
            sp.Poly(sp.expand(derivative(entry)), X, x).as_dict()
            for derivative in (dt, ds, lambda f: sp.diff(f, x))
        ]
        for entry in raw
    ]


def determinant_coefficient(matrix, x_degree, parameter_degree):
    """Full signed convolution, not a preselected list of contributions."""
    answer = 0
    for permutation in PERMUTATIONS:
        sign = (-1) ** sum(
            permutation[i] > permutation[j]
            for i in range(3) for j in range(i + 1, 3)
        )
        for (i, j), first in matrix[0][permutation[0]].items():
            for (k, ell), second in matrix[1][permutation[1]].items():
                third = matrix[2][permutation[2]].get(
                    (x_degree - i - k, parameter_degree - j - ell), 0
                )
                if third != 0:
                    answer += sign * first * second * third
    return sp.cancel(answer)


@lru_cache(maxsize=1)
def centered_data():
    """Arbitrary lower functions remain present during raw differentiation."""
    alpha, gamma, beta, delta, epsilon = [
        sp.Function(name)(s)
        for name in ("alpha", "gamma", "beta", "delta", "epsilon")
    ]
    H, C, E, F, G, n = [
        sp.Function(name)(t, s) for name in ("H", "C", "E", "F", "G", "n")
    ]
    dt = lambda f: sp.diff(f, t) + sp.diff(f, eta) * eta / (2 * t)
    ds = lambda f: (
        sp.diff(f, s) + sp.diff(f, eta) * eta * sp.diff(gamma, s) / (2 * gamma)
    )
    zeta = eta - t**2
    k = (t**2 - gamma / t) / (8 * s**3 * alpha) + beta * t + delta
    y = alpha * x**2 + C
    w = alpha * x**3 + E * x**2 + F * x + G
    h = zeta * x + H
    raw = raw_map(y, w, h, k, n, dt, ds)
    matrix = derivative_coefficients(raw, dt, ds)
    a_s, g_s = sp.diff(alpha, s), sp.diff(gamma, s)
    b_s, d_s = sp.diff(beta, s), sp.diff(delta, s)
    N22 = (
        8*s**4*t**4*alpha**2*b_s + 8*s**4*t*eta*alpha**2*d_s
        - 4*s**2*t**4*E*alpha + 4*s**2*t**2*eta*E*alpha
        + 4*s**2*eta*H*alpha**2 - 2*s*t**5*a_s
        + s*t**3*eta*a_s + s*t**2*alpha*g_s - s*t**2*gamma*a_s
        - 2*s*eta*alpha*g_s + 2*s*eta*gamma*a_s
        - 5*t**5*alpha + 5*eta*alpha*gamma
    )
    N14 = (
        24*s**4*t**4*alpha**2*b_s + 24*s**4*t*eta*alpha**2*d_s
        + 8*s**2*t**5*alpha*dt(E) - 12*s**2*t**4*E*alpha
        - 8*s**2*t**3*eta*alpha*dt(E) + 4*s**2*t**2*eta*E*alpha
        - 8*s**2*t*eta*alpha**2*dt(H) + 20*s**2*eta*H*alpha**2
        - 7*s*t**5*a_s + 4*s*t**3*eta*a_s + 2*s*t**2*alpha*g_s
        - 2*s*t**2*gamma*a_s - 5*s*eta*alpha*g_s
        + 5*s*eta*gamma*a_s - 15*t**5*alpha + 15*eta*alpha*gamma
    )
    return locals()


class NonzeroModeControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(expression), 0)

    def field_zero(self, expression):
        """Equality in the quotient field; all displayed denominators nonzero."""
        gamma = centered_data()["gamma"]
        numerator = sp.fraction(sp.cancel(expression))[0]
        remainder = sp.rem(numerator, eta**2 - gamma * t, eta)
        self.assertEqual(sp.factor(remainder), 0)

    def test_01_upstream_raw_coefficients_and_exact_primitives(self):
        A, B, C, D, E, F, G, k, n = [
            sp.Function(name)(t, s)
            for name in ("A0", "B0", "C0", "D0", "E0", "F0", "G0", "k0", "n0")
        ]
        dt, ds = lambda f: sp.diff(f, t), lambda f: sp.diff(f, s)
        raw = raw_map(A*x**2+B*x+C, D*x**3+E*x**2+F*x+G, x, k, n, dt, ds)
        matrix = derivative_coefficients(raw, dt, ds)
        J07 = determinant_coefficient(matrix, 0, 7)
        J23 = determinant_coefficient(matrix, 2, 3)
        J15 = determinant_coefficient(matrix, 1, 5)
        third_top = D/(4*s**3*t**2) + A/(8*s**3*t**4) + A**2*dt(dt(k))/2
        self.zero(J07 - D*(2*A*dt(D)-3*D*dt(A))/(2*s**2))
        self.zero(J23 - 8*s*t*third_top)
        substitutions = {
            dt(dt(k)): -(2*t**2*D+A)/(4*s**3*t**4*A**2),
            dt(D): 3*D*dt(A)/(2*A),
        }
        self.zero(
            J15.subs(substitutions, simultaneous=True)
            - (A+t**2*D)*(t*dt(A)+A-3*t**2*D)/(2*s**2*t**4)
        )
        self.zero(dt(A**3/D**2).subs({dt(D): 3*D*dt(A)/(2*A)}))
        zeta = A/D
        reduced_zeta_t = dt(zeta).subs(
            {dt(D): 3*D*dt(A)/(2*A)}
        ).subs({dt(A): (3*t**2*D-A)/t})
        self.zero(reduced_zeta_t - zeta/(2*t) + 3*t/2)
        self.zero(2*t*(reduced_zeta_t+2*t) - (zeta+t**2))
        # D=0 is retained as a separate branch, not excluded by this control.
        self.zero(
            J15.subs({D: 0, dt(D): 0, dt(dt(k)): -1/(4*s**3*t**4*A)},
                     simultaneous=True)
            - A*(t*dt(A)+A)/(2*s**2*t**4)
        )
        data = centered_data()
        alpha, gamma, dtq = data["alpha"], data["gamma"], data["dt"]
        self.field_zero(dtq(eta**2-gamma*t))
        self.field_zero(data["ds"](eta**2-gamma*t))
        self.field_zero(dtq(data["ds"](eta))-data["ds"](dtq(eta)))
        self.field_zero(dtq(eta**2/t))
        self.field_zero(
            dtq(dtq(data["k"])) - (1-gamma/t**3)/(4*s**3*alpha)
        )
        self.field_zero(dtq(data["k"]-(t**2-gamma/t)/(8*s**3*alpha))-data["beta"])

    def test_02_centered_raw_columns_and_all_three_coefficients(self):
        d = centered_data()
        a, z, k = d["alpha"], d["zeta"], d["k"]
        H, C, E, F, G, n = (d[name] for name in ("H", "C", "E", "F", "G", "n"))
        dt, ds = d["dt"], d["ds"]
        columns = (
            (C+t*X,
             G/(2*s)+dt(k)*C-H**2/(8*s**3*t**3)-ds(k)*H/(2*s*t**2)+n
             +(s*C-H/(2*s*t)+k)*X+s*t*X**2,
             G+(s**2*C-H/t)*X+s**2*t*X**2),
            (0, F/(2*s)-z*H/(4*s**3*t**3)-ds(k)*z/(2*s*t**2)-z*X/(2*s*t),
             F-z*X/t),
            (a, E/(2*s)+a*dt(k)-z**2/(8*s**3*t**3)+s*a*X, E+s**2*a*X),
            (0, a/(2*s), a),
        )
        for power, column in enumerate(columns):
            for row in range(3):
                self.field_zero(sp.expand(d["raw"][row]).coeff(x, power)-column[row])
        J06 = determinant_coefficient(d["matrix"], 0, 6)
        J22 = determinant_coefficient(d["matrix"], 2, 2)
        J14 = determinant_coefficient(d["matrix"], 1, 4)
        self.field_zero(
            J06 - a*(8*s*t**2*a*dt(E)-t**2*sp.diff(a,s)+eta*sp.diff(a,s))
            /(8*s**3*t**2)
        )
        self.field_zero(J22 - 3*d["N22"]/(8*s**4*t**3*a))
        self.field_zero(J14 - d["N14"]/(8*s**4*t**4))
        # The parameter-dependent affine change has a triangular chain matrix.
        v_t, v_s, xi_v = sp.symbols("v_t v_s xi_v", nonzero=True)
        chain = sp.Matrix([[1, 0, 0], [s**2, 2*s*t, 0], [v_t, v_s, z/xi_v]])
        self.zero(chain.det()-2*s*t*z/xi_v)

    def test_03_full_derivative_substitution_eigenweights_and_root_offset(self):
        d = centered_data()
        a, gamma, beta = d["alpha"], d["gamma"], d["beta"]
        epsilon, E, H = d["epsilon"], d["E"], d["H"]
        dt, ds = d["dt"], d["ds"]
        a_s, g_s, b_s = sp.diff(a,s), sp.diff(gamma,s), sp.diff(beta,s)
        EE = a_s*(t+2*eta/t)/(8*s*a)+epsilon
        self.field_zero(dt(EE)-a_s*(t**2-eta)/(8*s*t**2*a))
        # Solve the verified raw N22, rather than importing a stored solution.
        HH = -d["N22"].subs({E: EE, H: 0}, simultaneous=True)/(4*s**2*eta*a**2)
        self.field_zero(d["N22"].subs({E: EE, H: HH}, simultaneous=True))
        J14 = determinant_coefficient(d["matrix"], 1, 4)
        replaced = J14.subs(
            {sp.diff(E,t): dt(EE), sp.diff(H,t): dt(HH), E: EE, H: HH},
            simultaneous=True,
        )
        expected = 5*(
            t**4*(16*s**4*a**2*b_s-8*s**2*a*epsilon)
            - 7*t**5*(s*a_s+2*a)
            + eta*(2*s*a*g_s-2*s*gamma*a_s-4*a*gamma)
        )/(16*s**4*t**4)
        self.field_zero(replaced-expected)
        # Distinct eigenvalue projectors are uniform algebra, not sampled t.
        c4, c5, ch = [sp.Function(name)(s) for name in ("c4", "c5", "ch")]
        terms = (c4*t**4, c5*t**5, ch*eta)
        weights = (sp.Integer(4), sp.Integer(5), sp.Rational(1,2))
        for index, weight in enumerate(weights):
            projected = sum(terms)
            for other in weights:
                if other != weight:
                    projected = (t*dt(projected)-other*projected)/(weight-other)
            self.field_zero(projected-terms[index])
        conclusions = {epsilon: 2*s**2*a*b_s, a_s: -2*a/s, g_s: 0}
        self.field_zero((HH+2*s**2*t*ds(d["k"])).subs(conclusions, simultaneous=True))
        h_at_root_offset = d["zeta"]*x
        R = h_at_root_offset/(4*s**3*t**2)
        self.zero(R.subs(x,0))
        self.zero(sp.diff(R,x)-d["zeta"]/(4*s**3*t**2))
        self.zero(sp.diff(a*x**2+d["C"],x).subs(x,0))
        self.zero(sp.diff(-h_at_root_offset/t,x)+d["zeta"]/t)
        # These verify the forbidden-root configuration, not theorem231 itself.

    def test_04_actual_swap_both_orders_and_zero_mode(self):
        Y, Z, W = sp.symbols("Y Z W")
        swapped = (Y, X, Z, W)
        forward = dict(zip((X,Y,Z,W), swapped))
        reverse = {X: Y, Y: X, Z: Z, W: W}
        for actual in (X,Y,Z,W):
            self.zero(forward[actual].subs(reverse, simultaneous=True)-actual)
            self.zero(reverse[actual].subs(forward, simultaneous=True)-actual)
        self.zero((Z**2-X*Y*W).subs(reverse, simultaneous=True)-(Z**2-X*Y*W))
        self.assertEqual(tuple(sp.diff(entry,Z) for entry in swapped), (0,0,1,0))
        y, theta, w, kval, h = sp.symbols("y theta w kval h")
        q, rho = s*t, s**2*t

        def swap_chart(tt, rr, qq, yy, th, ww, kk):
            return (1/tt, rr/tt**2, qq/tt**2, -yy/tt,
                    th/tt-2*rr*yy/tt**2,
                    ww-yy*th/tt+rr*yy**2/tt**2, kk/tt)

        initial = (t,rho,q,y,theta,w,kval)
        first = swap_chart(*initial)
        second = swap_chart(*first)
        for old, new in zip(initial, second):
            self.zero(old-new)
        tt, rr, qq, yy, th, ww, kk = first
        self.zero(qq/tt-s)
        self.zero(rr*yy-tt*th-(rho*y-t*theta)/t**3)
        self.zero(ww-w-(rho*y-t*theta)*y/t**2)
        sigma = q*y/(2*t)+q*theta/(2*rho)+kval
        sigma_star = sigma/t-2*q*y/t**2
        self.zero(sigma_star-(qq*yy/(2*tt)+qq*th/(2*rr)+kk))
        ks = sp.symbols("k_s")
        R = (h+2*s**2*t*ks)/(4*s**3*t**2)
        R_star = (h/t**3+2*s**2*(1/t)*(ks/t))/(4*s**3*(1/t)**2)
        self.zero(R_star-t*R)
        A, B, C, D, E, F, G, hstar = sp.symbols("A B C D E F G hstar")
        yp = A*h**2+B*h+C
        wp = D*h**3+E*h**2+F*h+G
        yp_star = sp.expand((-yp/t).subs(h,t**3*hstar))
        wp_star = sp.expand((wp+h*yp/t**2).subs(h,t**3*hstar))
        self.zero(yp_star.coeff(hstar,2)+t**5*A)
        self.zero(wp_star.coeff(hstar,3)-t**7*(t**2*D+A))
        self.zero(wp_star.coeff(hstar,3).subs(D,-A/t**2))
        # Full-ideal transport and exact degrees remain written proof gates.


if __name__ == "__main__":
    unittest.main()
