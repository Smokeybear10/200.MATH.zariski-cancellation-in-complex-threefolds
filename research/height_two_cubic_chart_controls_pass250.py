"""Finite algebra controls for the supplied shift-two chart in pass250.

Standalone source: no retained solver, proof module, or checker is imported.
The generic maps retain arbitrary mixed coefficient jets. The checks do not
prove local nilpotence, exact-field existence, localization/return, descent,
or recognition. The final method is separately sourced from pass251 and is
only a negative control on a discarded differential-index shortcut.

Authoring boundary: this saved file was not executed, imported, or compiled.
The parent owns any canonical execution after complete source review.
"""

import itertools
import unittest

import sympy as sp


def determinant(rows):
    """Literal three-row determinant, without any chart simplification."""
    return sum(
        (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        * sp.prod(rows[i][p[i]] for i in range(3))
        for p in itertools.permutations(range(3))
    )


def cofactor(rows, row, column):
    minor = [
        [rows[i][j] for j in range(3) if j != column]
        for i in range(3)
        if i != row
    ]
    return (-1) ** (row + column) * (
        minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
    )


def derivative_rows(expressions, variables):
    return [[sp.diff(f, v) for v in variables] for f in expressions]


def coefficient(expression, variable, power):
    return sp.expand(expression).coeff(variable, power)


def weighted_monomials(weight):
    if weight < 0:
        return []
    return [
        (i, j, k, ell)
        for i in range(weight + 1)
        for j in range(weight + 1)
        for k in range(weight // 2 + 1)
        for ell in range(weight // 2 + 1)
        if i + j + 2 * k + 2 * ell == weight
    ]


class HeightTwoCubicChartControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.cancel(sp.expand(expression)), 0)

    def test_generic_top_determinant_and_literal_partial_cofactors(self):
        X, t, r, s = sp.symbols("X t r s")
        variables = (t, r, s)
        y, z, w, sigma, theta = [
            sp.Function(name)(*variables)
            for name in ("y", "z", "w", "sigma", "theta")
        ]
        q, rho = sp.Function("q")(t), sp.Function("rho")(t)
        raw_map = (y + t * X, z + sigma * X + q * X**2,
                   w + theta * X + rho * X**2)
        rows = derivative_rows(raw_map, variables)
        jacobian = determinant(rows)
        base = determinant(derivative_rows((y, z, w), variables))
        self.zero(coefficient(jacobian, X, 0) - base)
        self.assertLessEqual(sp.Poly(sp.expand(jacobian), X).degree(), 3)

        S = sigma - sp.diff(q, t) * y
        H = theta - sp.diff(rho, t) * y
        top = sp.diff(S, r) * sp.diff(H, s) - sp.diff(S, s) * sp.diff(H, r)
        self.zero(coefficient(jacobian, X, 3) - top)

        # Inverse-Jacobian column for the literal Z-partial: row index 1.
        numerators = [cofactor(rows, 1, j) for j in range(3)]
        expected = (0, sp.diff(H, s), -sp.diff(H, r))
        for numerator, leading in zip(numerators, expected):
            self.assertLessEqual(sp.Poly(sp.expand(numerator), X).degree(), 2)
            self.zero(coefficient(numerator, X, 2) - leading)
        for i in range(3):
            self.zero(sum(rows[i][j] * numerators[j] for j in range(3))
                      - (jacobian if i == 1 else 0))

        # This is an algebraic dependence condition, not an automatic identity.
        self.assertNotEqual(sp.expand(top), 0)

    def test_calibrated_raw_map_and_first_integral_rows(self):
        X, t, lam, v, speed = sp.symbols("X t lam v speed", nonzero=True)
        variables = (t, lam, v)
        y, z, w = [sp.Function(name)(*variables) for name in ("y", "z", "w")]
        q, rho = sp.Function("q")(t), sp.Function("rho")(t)
        k = sp.Function("k")(t, lam)
        m, d = sp.diff(k, lam), sp.diff(rho, t, 2)
        raw_map = (
            y + t * X,
            z + (sp.diff(q, t) * y + k) * X + q * X**2,
            w + (sp.diff(rho, t) * y + lam) * X + rho * X**2,
        )
        rows = derivative_rows(raw_map, variables)
        reduced = [rows[0]] + [
            [rows[i][j] - prime * X * rows[0][j] for j in range(3)]
            for i, prime in ((1, sp.diff(q, t)), (2, sp.diff(rho, t)))
        ]
        expected_rows = [
            [sp.diff(y, t) + X, sp.diff(y, lam), sp.diff(y, v)],
            [sp.diff(z, t) + X * (sp.diff(q, t, 2) * y + sp.diff(k, t)),
             sp.diff(z, lam) + X * m, sp.diff(z, v)],
            [sp.diff(w, t) + X * d * y, sp.diff(w, lam) + X, sp.diff(w, v)],
        ]
        for actual, expected in zip(reduced, expected_rows):
            for actual_entry, expected_entry in zip(actual, expected):
                self.zero(actual_entry - expected_entry)
        self.zero(determinant(rows) - determinant(reduced))

        j2 = (-sp.diff(z, v) + m * sp.diff(w, v)
              + ((sp.diff(q, t, 2) - d * m) * y + sp.diff(k, t)) * sp.diff(y, v))
        self.zero(coefficient(determinant(rows), X, 2) - j2)
        self.zero(coefficient(determinant(rows), X, 3))
        self.zero(coefficient(determinant(rows), X, 4))
        top_v_numerator = coefficient(cofactor(rows, 1, 2), X, 2)
        self.zero(top_v_numerator + 1)
        self.zero(speed**2 * top_v_numerator / (-speed**2) - 1)
        self.assertNotEqual(sp.cancel(speed**2 * top_v_numerator / (-speed**3) - 1), 0)
        self.assertNotEqual(sp.cancel(speed**2 * top_v_numerator / speed**2 - 1), 0)

        # Omitting rho'' y dt changes the determinant coefficient in general.
        wrong = [list(row) for row in reduced]
        wrong[2][0] -= X * d * y
        self.zero(coefficient(determinant(wrong), X, 2) - j2 - d * m * y * sp.diff(y, v))
        self.assertNotEqual(sp.expand(d * m * y * sp.diff(y, v)), 0)

    def test_two_integrals_depressed_cubic_and_complete_gradient_chains(self):
        X, U, V, t, lam, v = sp.symbols("X U V t lam v")
        y, w = sp.Function("y")(t, lam, v), sp.Function("w")(t, lam, v)
        q, rho = sp.Function("q")(t), sp.Function("rho")(t)
        k, n, ell = [sp.Function(name)(t, lam) for name in ("k", "n", "ell")]
        m, d = sp.diff(k, lam), sp.diff(rho, t, 2)
        f = (sp.diff(q, t, 2) - d * m) * U**2 / 2 + sp.diff(k, t) * U + n
        z = m * w + f.subs(U, y)
        B = sp.diff(m, t) * V + sp.diff(f, t)
        C = sp.diff(m, lam) * V + sp.diff(f, lam)
        B_eval, C_eval = [g.subs({U: y, V: w}, simultaneous=True) for g in (B, C)]
        self.zero(sp.diff(z, v) - m * sp.diff(w, v) - sp.diff(f, U).subs(U, y) * sp.diff(y, v))
        self.zero(sp.diff(f, lam, U) - sp.diff(m, t) + d * U * sp.diff(m, lam))

        raw_map = (
            y + t * X,
            z + (sp.diff(q, t) * y + k) * X + q * X**2,
            w + (sp.diff(rho, t) * y + lam) * X + rho * X**2,
        )
        rows = derivative_rows(raw_map, (t, lam, v))
        rows[1] = [rows[1][j] - sp.diff(q, t) * X * rows[0][j] for j in range(3)]
        rows[2] = [rows[2][j] - sp.diff(rho, t) * X * rows[0][j] for j in range(3)]
        middle = [rows[1][j] - m * rows[2][j] - sp.diff(f, U).subs(U, y) * rows[0][j]
                  for j in range(3)]
        for entry, expected in zip(middle, (B_eval, C_eval, 0)):
            self.zero(entry - expected)
        rows[1] = middle
        j1 = (B_eval - d * y * C_eval) * sp.diff(y, v) + C_eval * sp.diff(w, v)
        self.zero(coefficient(determinant(rows), X, 1) - j1)
        self.zero(coefficient(determinant(rows), X, 2))

        P = (d**2 * sp.diff(m, lam) * U**4 / 8
             + (sp.diff(q, t, 3) - sp.diff(rho, t, 3) * m - 3 * d * sp.diff(m, t)) * U**3 / 6
             + (sp.diff(k, t, 2) - d * sp.diff(n, lam)) * U**2 / 2 + sp.diff(n, t) * U)
        self.zero(sp.diff(P, U) - sp.diff(f, t) + d * U * sp.diff(f, lam))
        potential = sp.diff(m, lam) * V**2 / 2 + sp.diff(f, lam) * V + P - ell
        self.zero(sp.diff(potential.subs({U: y, V: w}, simultaneous=True), v) - j1)
        self.zero(sp.diff(potential, U) - B + d * U * C)
        self.zero(sp.diff(potential, V) - C)

        depressed = (
            sp.diff(k, lam, 2) * V**2 / 2
            + (sp.diff(k, t, lam) * U + sp.diff(n, lam)) * V
            + (sp.diff(q, t, 3) - sp.diff(rho, t, 3) * m) * U**3 / 6
            + sp.diff(k, t, 2) * U**2 / 2 + sp.diff(n, t) * U - ell
        )
        shifted = lambda expression: expression.subs(V, V - d * U**2 / 2)
        self.zero(shifted(depressed) - potential)
        self.zero(shifted(sp.diff(depressed, U)) - B)
        self.zero(shifted(sp.diff(depressed, V)) - C)
        # All coefficient and polynomial-variable partials, including curvature.
        for variable in (t, lam, U, V):
            shift_derivative = sp.diff(V - d * U**2 / 2, variable)
            direct = 0 if variable == V else shifted(sp.diff(depressed, variable))
            self.zero(sp.diff(potential, variable) - direct
                      - shifted(sp.diff(depressed, V)) * shift_derivative)
        self.assertLessEqual(sp.Poly(depressed, U, V).total_degree(), 3)
        wrong_cubic = depressed + sp.diff(rho, t, 3) * m * U**3 / 6
        self.zero(shifted(wrong_cubic) - potential - sp.diff(rho, t, 3) * m * U**3 / 6)
        self.assertNotEqual(sp.expand(shifted(wrong_cubic) - potential), 0)

    def test_actual_212_family_chart_and_initial_relation_boundary(self):
        X, Y, Z, W, u, t, y, z, lam, v, U, V = sp.symbols("X Y Z W u t y z lam v U V")
        for exponent in (4, 13):
            f = t**exponent
            forward = (u, y + t*u, z + (3*t**2*y + f)*u + t**3*u**2)
            forward += (t + forward[0]*forward[2] - forward[1]**3,)
            T = W-X*Z+Y**3
            y_back = Y-X*T
            z_back = Z-(3*T**2*y_back+T**exponent)*X-T**3*X**2
            self.zero(T.subs(dict(zip((X,Y,Z,W),forward)), simultaneous=True)-t)
            # Staged polynomial inverse checks retain verified T=t, avoiding blowup.
            self.zero(forward[1]-t*forward[0]-y)
            self.zero(forward[2]-(3*t**2*y+f)*forward[0]-t**3*forward[0]**2-z)
            self.zero(y_back+X*T-Y)
            self.zero(z_back+(3*T**2*y_back+T**exponent)*X+T**3*X**2-Z)
            self.zero(T+X*Z-Y**3-W)

            # N=partial_y+(6ty+f')partial_z, v=y, lambda=z-3ty²-f'y.
            invariant = z-3*t*y**2-sp.diff(f,t)*y
            self.zero(sp.diff(invariant,y)+(6*t*y+sp.diff(f,t))*sp.diff(invariant,z))
            y0 = v
            z0 = lam+3*t*v**2+sp.diff(f,t)*v
            w0 = t-v**3
            raw = (y0+t*X, z0+(3*t**2*y0+f)*X+t**3*X**2,
                   w0+(sp.diff(f,t)*y0+lam)*X+f*X**2)
            self.zero(determinant(derivative_rows(raw,(t,lam,v)))+1)
            self.zero(coefficient(cofactor(derivative_rows(raw,(t,lam,v)),1,2),X,2)+1)
            zeta = w0-sp.diff(f,t,2)*y0**2/2
            cubic = V+sp.diff(f,t,2)*U**2/2+U**3-t
            self.zero(cubic.subs({U:y0,V:zeta},simultaneous=True))
            self.assertEqual(sp.Poly(cubic,U,V).total_degree(),3)

        # Finite n=13 controls do not assert a universal initial-ideal theorem.
        for weight in range(9):
            monomials = weighted_monomials(weight)
            image_exponents = {j+3*k+13*ell for i,j,k,ell in monomials}
            kernel_dimension = len(monomials)-len(image_exponents)
            self.assertEqual(kernel_dimension,len(weighted_monomials(weight-3)))
        monomials = weighted_monomials(9)
        image_exponents = {j+3*k+13*ell for i,j,k,ell in monomials}
        self.assertGreater(len(monomials)-len(image_exponents),len(weighted_monomials(6)))
        eta = sp.symbols("eta")
        second_relation = X**7*W-Y*Z**4
        self.zero(second_relation.subs({X:eta,Y:t*eta,Z:t**3*eta**2,W:t**13*eta**2},simultaneous=True))
        # XZ-Y³ vanishes here, but the second relation does not: not a multiple.
        self.assertEqual(second_relation.subs({X:1,Y:0,Z:0,W:1}),1)

    def test_separate_pass251_differential_index_negative_control(self):
        # Provenance: pass251, not an additional conclusion of the cubic chart.
        X,Y,Z,W = sp.symbols("X Y Z W")
        variables = (X,Y,Z,W)
        T = W-X*Z+Y**3
        F = 3*T**2*Y+T**4-X*T**3
        H = sp.Matrix((1,T,F,Z+X*F-3*T*Y**2))
        self.zero(sum(H[i]*sp.diff(T,variables[i]) for i in range(4)))
        matrix = H.jacobian(variables).subs({X:0,Y:0,Z:0,W:1})
        self.assertEqual(matrix,sp.Matrix(((0,0,0,0),(0,0,0,1),(-1,3,0,4),(1,0,1,0))))
        eigenvalue = sp.symbols("eigenvalue")
        self.zero(matrix.charpoly(eigenvalue).as_expr()-eigenvalue**4+4*eigenvalue**2+3*eigenvalue)
        self.assertEqual(sp.trace(matrix**2),8)
        acceleration = lambda expression: 2*T**3*sp.diff(expression,Z)+2*T**4*sp.diff(expression,W)
        self.zero(acceleration(T)-2*T**3*(T-X))
        self.zero(acceleration(2*T**3)-12*T**5*(T-X))
        self.assertNotEqual(sp.expand(acceleration(2*T**3)),0)


if __name__ == "__main__":
    unittest.main()
