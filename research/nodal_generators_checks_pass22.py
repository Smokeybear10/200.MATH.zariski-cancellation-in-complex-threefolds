"""Exact controls for the fixed conductor surface's five generators.

Uses only unittest and SymPy. The global conclusion also uses the written
finite-morphism and local Nakayama argument in the companion note.
"""

import unittest

import sympy as sp


u, y, z, c, t = sp.symbols("u y z c t")
i = sp.I
m = (1 + i) / 2
A = (u - 1) * (u - i)
a = 1 + i - (1 - i) * A / 2
b = -i * (u - m) * (u + 1) * (u + i)
p = -i * u * A / 8
q = i * b / 2
trace = sp.expand(a + b * y)
tau = sp.expand(q * (2 * y - 1) * z + p * y)
beta = sp.expand(
    -i * t * (c**2 * t * (1 - i) - c**2 - 2 * c * t
              + c * (1 + i) - 2 * i) / 2
)
norm = sp.expand(u**2 - trace * u)
d = u**4 - 1
bezout_u = (1 + i) * u**2 - 3 * i * u / 2 - 1 + i
bezout_v = -8 * (1 + i) * u**2 - 12 * i * u + 6 - 6 * i
labels = [1 + i, 1 - i, -1 + i]
branches = [
    (sp.Integer(1), 0, 0), (i, 0, 0),
    (sp.Integer(1), 1, 1), (-i, None, 1),
    (sp.Integer(-1), None, 2), (i, 1, 2),
]


def line_substitution(root, epsilon):
    if epsilon is None:
        yy = sp.expand(root * A.subs(u, root) * t)
        zz = sp.expand(root**2 * A.subs(u, root) * t**2 - root * t)
    else:
        yy = sp.Integer(epsilon)
        zz = root * (2 * epsilon - 1) * t
    return {u: root, y: yy, z: zz}


def rational_chart():
    yy = sp.cancel((c - a) / b)
    zz = sp.cancel(yy * (yy - 1) / A)
    tt = sp.cancel(q * (2 * yy - 1) * zz + p * yy)
    return yy, zz, tt


def numerator_polynomial(expression):
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.Poly(numerator, u, extension=i)


def branch_normal_ratios(root, epsilon, pair):
    """Differentiate along u while keeping the common parameter tau fixed."""
    sub = line_substitution(root, epsilon)
    yy, zz = sub[y], sub[z]
    ar = A.subs(u, root)
    apr = sp.diff(A, u).subs(u, root)
    if epsilon is None:
        zu = -apr * zz / ar
        zy = (2 * yy - 1) / ar
        tau_u = sp.diff(tau, u).subs(sub) + sp.diff(tau, z).subs(sub) * zu
        tau_y = sp.diff(tau, y).subs(sub) + sp.diff(tau, z).subs(sub) * zy
        yp = sp.cancel(-tau_u / tau_y)
        zp = sp.cancel(zu + zy * yp)
    else:
        yp = apr * root * t
        tau_u = sp.diff(tau, u).subs(sub) + sp.diff(tau, y).subs(sub) * yp
        zp = sp.cancel(-tau_u / sp.diff(tau, z).subs(sub))
    cp = sp.cancel(sp.diff(trace, u).subs(sub) + sp.diff(trace, y).subs(sub) * yp)
    bp = beta.subs(c, labels[pair])
    bc = sp.diff(beta, c).subs(c, labels[pair])
    zetap = sp.cancel(zp - bp - root * bc * cp)
    return sp.cancel(cp / (4 * root**3)), sp.cancel(zetap / (4 * root**3))


class NodalGeneratorChecks(unittest.TestCase):
    def test_six_branch_restrictions_and_fixed_gluing(self):
        expected_norms = [-i, i, i]
        expected_zetas = [
            0,
            (1 + i) * t - 2 * i * t**2,
            (1 + i) * t + 2 * i * t**2,
        ]
        for root, epsilon, pair in branches:
            with self.subTest(root=root, epsilon=epsilon):
                sub = line_substitution(root, epsilon)
                self.assertEqual(sp.simplify((A*z-y*(y-1)).subs(sub)), 0)
                self.assertEqual(sp.simplify(trace.subs(sub)-labels[pair]), 0)
                self.assertEqual(sp.simplify(tau.subs(sub)-t), 0)
                self.assertEqual(sp.simplify(norm.subs(sub)-expected_norms[pair]), 0)
                value = sub[z] - beta.subs(c, labels[pair]) * root
                self.assertEqual(sp.simplify(value-expected_zetas[pair]), 0)

    def test_bezout_and_polynomial_recovery(self):
        self.assertEqual(sp.expand(bezout_u*b+bezout_v*p-1), 0)
        recovered = (
            bezout_u*(trace-a)
            + bezout_v*(tau-i*z*(trace-a)+i*b*z/2)
        )
        self.assertEqual(sp.expand(recovered-y), 0)
        self.assertEqual(sp.expand(u**2-trace*u-norm), 0)

    def test_off_conductor_collision_gcd_certificates(self):
        _, zz, tt = rational_chart()
        for epsilon in [sp.Integer(-1), i, -i]:
            with self.subTest(epsilon=epsilon):
                common_c = (1+epsilon)*u
                here_t = sp.cancel(tt.subs(c, common_c))
                there_t = sp.cancel(tt.subs(u, epsilon*u).subs(c, common_c))
                here_z = sp.cancel(zz.subs(c, common_c))
                there_z = sp.cancel(zz.subs(u, epsilon*u).subs(c, common_c))
                ff = numerator_polynomial(here_t-there_t)
                gg = numerator_polynomial(
                    here_z-there_z-(1-epsilon)*u*beta.subs({c: common_c, t: here_t})
                )
                self.assertEqual(sp.gcd(ff, gg).monic(), sp.Poly(u, u, extension=i))
                aa, bb, divisor = sp.gcdex(ff, gg)
                self.assertEqual(divisor.monic(), sp.Poly(u, u, extension=i))
                self.assertTrue((aa*ff+bb*gg-divisor).is_zero)

    def test_exceptional_slope_root_and_conductor_pairs(self):
        self.assertEqual(sp.simplify(b.subs(u, m)), 0)
        self.assertEqual(sp.simplify(a.subs(u, m)-3*m/2), 0)
        for epsilon in [sp.Integer(-1), i, -i]:
            self.assertNotEqual(sp.simplify((1+epsilon)*m-3*m/2), 0)
            self.assertNotEqual(sp.simplify((1+1/epsilon)*m-3*m/2), 0)
        for first in range(len(branches)):
            r1, eps1, pair1 = branches[first]
            for second in range(first+1, len(branches)):
                r2, eps2, pair2 = branches[second]
                if r1 != r2 and labels[pair1] == labels[pair2]:
                    self.assertEqual(pair1, pair2)
                    self.assertEqual(sp.simplify(labels[pair1]-r1-r2), 0)

    def test_smooth_locus_cotangent_coverage(self):
        self.assertNotEqual(sp.simplify(p.subs(u, m)), 0)
        self.assertNotEqual(sp.simplify(b.subs(u, 0)), 0)
        yy, _, tt = rational_chart()
        self.assertEqual(sp.simplify(yy.subs({u: 0, c: 0})), 1)
        self.assertEqual(sp.simplify(sp.diff(tt, u).subs({u: 0, c: 0})), -sp.Rational(3, 8))

    def test_all_conductor_cotangent_spaces(self):
        data = [branch_normal_ratios(*entry) for entry in branches]
        roots = [
            (1+i)/4,
            -sp.Rational(1, 10)-i/20,
            -sp.Rational(1, 20)-i/10,
        ]
        expected_values = [
            sp.Rational(3, 16),
            sp.Rational(9381, 20000)+sp.Rational(4691, 40000)*i,
            sp.Rational(9381, 20000)-sp.Rational(4691, 40000)*i,
        ]
        for pair in range(3):
            dc = sp.cancel(data[2*pair][0]-data[2*pair+1][0])
            dz = sp.cancel(data[2*pair][1]-data[2*pair+1][1])
            self.assertEqual(sp.Poly(dc, t).degree(), 1)
            self.assertEqual(sp.simplify(dc.subs(t, roots[pair])), 0)
            self.assertEqual(sp.simplify(dz.subs(t, roots[pair])), expected_values[pair])
            self.assertNotEqual(expected_values[pair], 0)

    def test_explicit_failed_three_generator_candidate(self):
        first = {u: 0, y: 0, z: 0}
        second = {u: 1+i, y: 0, z: 0}
        for point in [first, second]:
            self.assertEqual(sp.simplify(trace.subs(point)), m)
            self.assertEqual(sp.simplify(tau.subs(point)), 0)
            self.assertEqual(sp.simplify(beta.subs({c: m, t: 0})), 0)
        self.assertEqual(sp.simplify(d.subs(first)), -1)
        self.assertEqual(sp.simplify(d.subs(second)), -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
