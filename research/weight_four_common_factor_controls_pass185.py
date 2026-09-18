"""Finite exact controls for the common-factor high-graph proof185.

These formulas do not establish actual chart entry, unit cofactor, exact
coefficient-field constants, or the regular-kernel recognition theorem.
They test the supplied translation normalization, determinant forcing
coefficients, and the original polynomial coordinate inverse.  No earlier
checker, solver, or proof implementation is imported.
"""

import unittest

import sympy as sp


class CommonFactorQuarticControls(unittest.TestCase):
    def zero(self, expression):
        self.assertEqual(sp.expand(expression), 0)

    def test_actual_translation_and_normalized_coefficients(self):
        t, rho, y, theta, w = sp.symbols("t rho y theta w")
        mu, nu, s0 = sp.symbols("mu nu s0")
        k0, n0 = [sp.Function(name)(t) for name in ("k0", "n0")]
        r, s = mu * t + nu, -mu**2 * t + s0
        d = mu * nu + s0
        k, n, q = r * rho + k0, s * rho + n0, -t * rho + t**4

        def H2(y_arg, theta_arg):
            return (sp.diff(q, t, 2) * y_arg**2 / 2
                    + sp.diff(q, t, rho) * y_arg * theta_arg
                    + sp.diff(q, rho, 2) * theta_arg**2 / 2)

        sigma = sp.diff(q, t) * y + sp.diff(q, rho) * theta + k
        z = (sp.diff(q, rho) * w + H2(y, theta)
             + sp.diff(k, t) * y + sp.diff(k, rho) * theta + n)
        yn, thetan = y - r, theta - 2 * mu * rho
        wn, zn, sigman = w - mu * theta + mu**2 * rho, z - mu * sigma + mu**2 * q, sigma - 2 * mu * q
        kn = k0 + 4 * r * t**3 - 2 * mu * t**4
        nn0 = (n0 - mu * k0 + r * sp.diff(k0, t)
               + 6 * t**2 * r**2 - 4 * mu * t**3 * r + mu**2 * t**4)
        nn = d * rho + nn0
        self.zero(sigman - (sp.diff(q, t) * yn + sp.diff(q, rho) * thetan + kn))
        self.zero(zn - (sp.diff(q, rho) * wn + H2(yn, thetan)
                       + sp.diff(kn, t) * yn + sp.diff(kn, rho) * thetan + nn))
        general_kn = k + sp.diff(q, t) * r + 2 * mu * rho * sp.diff(q, rho) - 2 * mu * q
        general_nn = (n - mu * k + r * sp.diff(k, t) + 2 * mu * rho * sp.diff(k, rho)
                      + H2(r, 2 * mu * rho) - mu * sp.diff(q, t) * r
                      + mu**2 * (q - rho * sp.diff(q, rho)))
        self.zero(general_kn - kn)
        self.zero(general_nn - nn)
        self.zero(sp.diff(kn, rho))
        self.zero(sp.diff(nn, rho) - d)
        X = sp.Symbol("X")
        Xn = X + mu
        self.zero((y + t * X - nu) - (yn + t * Xn))
        self.zero((w + theta * X + rho * X**2)
                  - (wn + thetan * Xn + rho * Xn**2))
        self.zero((z + sigma * X + q * X**2)
                  - (zn + sigman * Xn + q * Xn**2))
        # Translation is an actual invertible operation independently of
        # whether these formal coefficients arise from an original frame.
        self.zero(Xn - mu - X)
        self.zero((y + t * X - nu) + nu - (y + t * X))

    def test_normalized_fixed_y_determinant_forcing_coefficients(self):
        t, rho, y = sp.symbols("t rho y")
        d = sp.Symbol("d", nonzero=True)
        k, n0, ell = [sp.Function(name)(t) for name in ("k", "n0", "ell")]
        m = sp.Function("m")(t, rho)
        w = (m / d - y**4 / d - sp.diff(k, t, 3) * y**3 / (6 * d)
             - sp.diff(n0, t, 2) * y**2 / (2 * d) + sp.diff(ell, t) * y / d)
        theta = (y * w - 4 * t * y**3 - sp.diff(k, t, 2) * y**2 / 2
                 - sp.diff(n0, t) * y + ell) / d
        z = -t * w + 6 * t**2 * y**2 + sp.diff(k, t) * y - y * theta + d * rho + n0
        determinant = sp.expand(sp.diff(z, t) * sp.diff(w, rho) - sp.diff(z, rho) * sp.diff(w, t))
        bracket = (5 * y**4 / d + 2 * sp.diff(k, t, 3) * y**3 / (3 * d)
                   + (12 * t + 3 * sp.diff(n0, t, 2) / (2 * d)) * y**2
                   + (sp.diff(k, t, 2) - 2 * sp.diff(ell, t) / d) * y
                   + sp.diff(n0, t) - m / d)
        expected = (sp.diff(m, rho) * bracket / d - sp.diff(m, t)
                    + sp.diff(k, t, 4) * y**3 / 6
                    + sp.diff(n0, t, 3) * y**2 / 2 - sp.diff(ell, t, 2) * y)
        self.zero(determinant - expected)
        self.assertEqual(sp.degree(determinant, y), 4)
        self.zero(determinant.coeff(y, 4) - 5 * sp.diff(m, rho) / d**2)
        reduced = sp.expand(determinant.subs(sp.diff(m, rho), 0))
        self.zero(reduced.coeff(y, 3) - sp.diff(k, t, 4) / 6)
        self.zero(reduced.coeff(y, 2) - sp.diff(n0, t, 3) / 2)
        self.zero(reduced.coeff(y, 1) + sp.diff(ell, t, 2))
        self.zero(reduced.coeff(y, 0) + sp.diff(m, t))
        # The written proof, not this calculation, supplies the nonzero
        # scalar determinant -a^3/(Ny), hence coefficient vanishing.

    def test_invariant_return_and_two_original_inverse_orders(self):
        X, y, t, rho = sp.symbols("X y t rho")
        d = sp.Symbol("d", nonzero=True)
        k3, k2, k1, k0, n2, n1, n00, ell1, ell0 = sp.symbols("k3 k2 k1 k0 n2 n1 n00 ell1 ell0")
        m = sp.Function("m")(t)
        k = k3 * t**3 + k2 * t**2 + k1 * t + k0
        n0 = n2 * t**2 + n1 * t + n00
        ell = ell1 * t + ell0
        w = m / d - y**4 / d - k3 * y**3 / d - n2 * y**2 / d + ell1 * y / d
        theta = (y * w - 4 * t * y**3 - sp.diff(k, t, 2) * y**2 / 2
                 - sp.diff(n0, t) * y + ell) / d
        z = -t * w + 6 * t**2 * y**2 + sp.diff(k, t) * y - y * theta + d * rho + n0
        sigma = (-rho + 4 * t**3) * y - t * theta + k
        Y = y + t * X
        Z = z + sigma * X + (-t * rho + t**4) * X**2
        W = w + theta * X + rho * X**2

        def correction(x_arg, y_arg):
            K3 = k3 * y_arg**3 + k2 * x_arg * y_arg**2 + k1 * x_arg**2 * y_arg + k0 * x_arg**3
            N2 = n2 * y_arg**2 + n1 * x_arg * y_arg + n00 * x_arg**2
            return y_arg**4 + K3 + N2 - ell1 * y_arg - ell0 * x_arg

        I_chart = -X**2 * Z + (d - X * Y) * W + correction(X, Y)
        self.zero(I_chart - m)
        # The coordinate test below uses independent original-ring axes,
        # not only the generic chart or a numerical specialization.
        Y0, Z0, W0, I0, J0 = sp.symbols("Y0 Z0 W0 I0 J0")
        P0 = correction(X, Y0)
        I = -X**2 * Z0 + (d - X * Y0) * W0 + P0
        J = (d + X * Y0) * Z0 + Y0**2 * W0
        inverse_Z = ((d - X * Y0) * J0 - Y0**2 * (I0 - P0)) / d**2
        inverse_W = ((d + X * Y0) * (I0 - P0) + X**2 * J0) / d**2
        self.zero(inverse_Z.subs({I0: I, J0: J}, simultaneous=True) - Z0)
        self.zero(inverse_W.subs({I0: I, J0: J}, simultaneous=True) - W0)
        self.zero(I.subs({Z0: inverse_Z, W0: inverse_W}, simultaneous=True) - I0)
        self.zero(J.subs({Z0: inverse_Z, W0: inverse_W}, simultaneous=True) - J0)
        matrix = sp.Matrix([[-X**2, d - X * Y0], [d + X * Y0, Y0**2]])
        self.zero(matrix.det() + d**2)


if __name__ == "__main__":
    unittest.main()
