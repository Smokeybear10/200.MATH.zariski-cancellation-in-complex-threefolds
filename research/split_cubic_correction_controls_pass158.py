"""Exact algebra controls for the split-cubic invariant-lift obstruction158.

Generic complex coefficients check the unique critical point and invertible
Hessian of lambda*(XZ+YW)+alpha*Z+beta*W+Q(X,Y). The main control uses
every quadratic Q coefficient; one higher-degree Q illustrates the larger
critical-point lemma. Generic vector-field first jets independently check
the differentiated invariance identity. The written proof, not a finite
test, applies the slice contradiction to every polynomial derivation.

A genuine triangular LND fixes this H but has a fixed plane and no slice.
Conversely partial_W fixes XZ-Y^3 and has slice W; its Hessian is degenerate.
Neither boundary is asserted to have E-time profile (1,1,2,2). These controls
do not establish existence of an affine correction, recognize all split
frames, or settle coordinate entry or cancellation. No prior checker or
solver is imported, and no actual157 frame is rerun here.
"""

import unittest

import sympy as sp


class SplitCubicCorrectionControls(unittest.TestCase):
    def zero(self, expression):
        # Denominators below are powers of the fixed nonzero constant lambda.
        # Expansion suffices; no inversion of an original coordinate is used.
        self.assertEqual(sp.expand(expression), 0)

    @staticmethod
    def data():
        X, Y, Z, W = variables = sp.symbols("X Y Z W")
        lam = sp.symbols("lam", nonzero=True)
        alpha, beta = sp.symbols("alpha beta")
        q20, q11, q02, q10, q01, q00 = sp.symbols("q20 q11 q02 q10 q01 q00")
        Q = q20*X*X+q11*X*Y+q02*Y*Y+q10*X+q01*Y+q00
        return variables, lam, alpha, beta, (q20, q11, q02, q10, q01, q00), Q

    @staticmethod
    def critical(variables, lam, alpha, beta, Q):
        X, Y, Z, W = variables
        good_point = {X: -alpha/lam, Y: -beta/lam}
        return (-alpha/lam, -beta/lam,
                -sp.diff(Q, X).xreplace(good_point)/lam,
                -sp.diff(Q, Y).xreplace(good_point)/lam)

    @staticmethod
    def deriv(expression, variables, coefficients):
        return sp.expand(sum(c*sp.diff(expression, v)
                             for v, c in zip(variables, coefficients)))

    def test_generic_critical_point_hessian_and_polynomial_normalization(self):
        variables, lam, alpha, beta, qs, Q2 = self.data()
        X, Y, Z, W = variables
        q20, q11, q02, q10, q01, q00 = qs
        for Q in (Q2, Q2+X**3+X*Y*Y+Y**5):
            with self.subTest(good_polynomial_degree=sp.Poly(Q, X, Y).total_degree()):
                H = lam*(X*Z+Y*W)+alpha*Z+beta*W+Q
                point = self.critical(variables, lam, alpha, beta, Q)
                at_point = dict(zip(variables, point))
                gradient = sp.Matrix([sp.diff(H, v) for v in variables])
                for entry in gradient:
                    self.zero(entry.xreplace(at_point))
                self.zero(gradient[2]-(lam*X+alpha))
                self.zero(gradient[3]-(lam*Y+beta))
                # The last two equations uniquely fix X,Y; the first two
                # then uniquely fix Z,W since their coefficients are lambda.
                self.zero(gradient[0]-(lam*Z+sp.diff(Q, X)))
                self.zero(gradient[1]-(lam*W+sp.diff(Q, Y)))
                self.zero(H.xreplace(at_point)-Q.xreplace(at_point))
                hessian = sp.hessian(H, variables)
                block = sp.Matrix(((sp.diff(Q, X, 2), sp.diff(Q, X, Y), lam, 0),
                                   (sp.diff(Q, X, Y), sp.diff(Q, Y, 2), 0, lam),
                                   (lam, 0, 0, 0), (0, lam, 0, 0)))
                for entry in hessian-block:
                    self.zero(entry)
                self.zero(hessian.det()-lam**4)
                self.zero(hessian.det().subs(lam, 1)-1)
                self.zero(hessian.xreplace(at_point).det()-lam**4)

        # For quadratic Q the critical translation and linear shears give
        # an actual polynomial coordinate normalization over fixed constants.
        H = lam*(X*Z+Y*W)+alpha*Z+beta*W+Q2
        point = self.critical(variables, lam, alpha, beta, Q2)
        at_point = dict(zip(variables, point))
        x, y, z, w = normal = sp.symbols("x y z w")
        dx, dy = X-point[0], Y-point[1]
        forward = (dx, dy,
                   lam*(Z-point[2])+q20*dx+q11*dy,
                   lam*(W-point[3])+q02*dy)
        inverse = (point[0]+x, point[1]+y,
                   point[2]+(z-q20*x-q11*y)/lam,
                   point[3]+(w-q02*y)/lam)
        for variable, expression in zip(variables, inverse):
            self.zero(expression.xreplace(dict(zip(normal, forward)))-variable)
        for variable, expression in zip(normal, forward):
            self.zero(expression.xreplace(dict(zip(variables, inverse)))-variable)
        self.zero(H-H.xreplace(at_point)-forward[0]*forward[2]-forward[1]*forward[3])
        self.zero(sp.Matrix(forward).jacobian(variables).det()-lam**2)

    def test_independent_vector_jets_and_differentiated_invariance(self):
        variables, lam, alpha, beta, qs, Q = self.data()
        X, Y, Z, W = variables
        H = lam*(X*Z+Y*W)+alpha*Z+beta*W+Q
        point = self.critical(variables, lam, alpha, beta, Q)
        at_point = dict(zip(variables, point))
        displacement = sp.Matrix([v-p for v, p in zip(variables, point)])
        values = sp.Matrix(sp.symbols("e0:4"))
        jets = sp.Matrix(4, 4, sp.symbols("j0:16"))
        coefficients = values+jets*displacement
        gradient = sp.Matrix([sp.diff(H, v) for v in variables])
        hessian = sp.hessian(H, variables)
        EH = sum(coefficients[i]*gradient[i] for i in range(4))
        differentiated = sp.Matrix([sp.diff(EH, v) for v in variables])
        # Independent differentiation of the full scalar expression includes
        # both product-rule terms before evaluation at the critical point.
        for entry in differentiated-hessian*coefficients-jets.T*gradient:
            self.zero(entry)
        self.zero(EH.xreplace(at_point))
        constraints = differentiated.xreplace(at_point)
        for entry in constraints-hessian*values:
            self.zero(entry)

        q20, q11, q02, q10, q01, q00 = qs
        hessian_inverse = sp.Matrix(((0, 0, 1/lam, 0),
                                     (0, 0, 0, 1/lam),
                                     (1/lam, 0, -2*q20/lam**2, -q11/lam**2),
                                     (0, 1/lam, -q11/lam**2, -2*q02/lam**2)))
        for entry in hessian_inverse*hessian-sp.eye(4):
            self.zero(entry)
        for entry in hessian_inverse*constraints-values:
            self.zero(entry)

        # A polynomial's value under E at this point depends only on its
        # first jet. If EH is the zero POLYNOMIAL, all four constraints vanish,
        # hence values vanish and no first jet can have E-value one there.
        slice_gradient = sp.Matrix(sp.symbols("g0:4"))
        slice_jet = sp.symbols("s0")+(slice_gradient.T*displacement)[0]
        slice_value = self.deriv(slice_jet, variables, coefficients).xreplace(at_point)
        self.zero(slice_value-(slice_gradient.T*values)[0])
        self.zero(slice_value-(slice_gradient.T*hessian_inverse*constraints)[0])
        self.zero(slice_value.xreplace(dict.fromkeys(values, sp.Integer(0))))

        # Pointwise EH=0 alone is vacuous at a critical point. The vector
        # field partial_X gives that zero value but violates differentiated
        # invariance: its Z derivative is the nonzero constant lambda.
        pointwise_only = sp.diff(H, X)
        self.zero(pointwise_only.xreplace(at_point))
        self.zero(sp.diff(pointwise_only, Z)-lam)
        self.assertNotEqual(lam, 0)

    def test_nonsliced_invariant_and_degenerate_hessian_boundaries(self):
        variables, lam, alpha, beta, qs, Q = self.data()
        X, Y, Z, W = variables
        H = lam*(X*Z+Y*W)+alpha*Z+beta*W+Q
        coefficients = (sp.Integer(0), sp.Integer(0), -(lam*Y+beta), lam*X+alpha)
        D = lambda f: self.deriv(f, variables, coefficients)
        self.zero(D(H))
        for v in variables:
            self.zero(D(D(v)))
        self.assertNotEqual(D(Z), 0)
        self.assertNotEqual(D(W), 0)
        fixed_plane = {X: -alpha/lam, Y: -beta/lam}
        for c in coefficients:
            self.zero(c.xreplace(fixed_plane))
        # This genuine triangular LND has derivative ideal
        # (lambda*X+alpha,lambda*Y+beta), proper by the displayed evaluation.
        # Every polynomial derivative vanishes on this plane, so no slice
        # exists. At lambda=1,alpha=beta=0 it is X*partial_W-Y*partial_Z.
        specialization = {lam: 1, alpha: 0, beta: 0}
        self.zero(D(Z).xreplace(specialization)+Y)
        self.zero(D(W).xreplace(specialization)-X)

        # The other cubic normal form is a different boundary: it is fixed
        # by a derivation WITH a slice, but its critical Hessian is degenerate.
        # This is not an exact (1,1,2,2) frame and is not a cancellation claim.
        cusp = X*Z-Y**3
        self.zero(sp.diff(cusp, W))
        self.zero(sp.diff(W, W)-1)
        self.zero(sp.hessian(cusp, variables).det())
        critical_line = {X: 0, Y: 0, Z: 0}
        for v in variables:
            self.zero(sp.diff(cusp, v).xreplace(critical_line))


if __name__ == "__main__":
    unittest.main()
