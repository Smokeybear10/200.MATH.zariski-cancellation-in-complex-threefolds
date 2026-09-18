# Recognition of the entire square-root monomial nonzero-R branch

Status: bounded working theorem obtained by composing the actual
normalization196 with the graph exclusion196 and the polynomial
inverse197. For the supplied full square-root initial kernel, the
nonzero-R family \(f=\beta q\) is now recognized. This is not recognition
of the other surviving coefficient families or of unrestricted
cancellation.

## 1. Exact composed statement

Suppose
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^3\mathsf Y),\qquad q^2=t,\\
R=k_\rho\ne0,\qquad f=1/R=\beta_0q,\qquad
\beta_0\in\mathbb C^* .
\end{gathered}
\tag{1}
\]
The fields and potentials are the actual selected chart of
[universal184](weight-four-universal-chart-potentials-pass184-working.md).
The initial ideal is the entire kernel. The conclusion is
\[
A\cong\mathbb C^{[3]}.
\tag{2}
\]
The supplied time profile and the reciprocal-coefficient condition in
(1) are substantial hypotheses. Neither has been proved to hold for
an arbitrary cancellation instance.

The [nonzero-R reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
first leaves only the quadratic graph and quadratic projection.
Its constant-projection, curvature, and pure-quartic exclusions use
the actual hypotheses, not just the necessary differential equations.

The [actual normalization196](weight-four-square-root-monomial-actual-normalization-pass196-working.md)
applies to both remaining alternatives under (1). Its polynomial
scaling, translations, and shears have polynomial inverses, preserve the
selected intrinsic derivation and the exact fields, and give
\(k=\rho/q,\ n=-\rho^2/(2q^3)\). Their coefficient integrations hold
inside the actual finite coefficient field; they do not assume it is
rational.

The quadratic graph is impossible by the completed composition in
[synthesis196](weight-four-double-cover-frontier-synthesis-pass196-working.md).
That argument establishes \(z=g\in L^*\) before applying normality
and the irreducible-square obstruction.

The remaining quadratic projection is exactly the input of
[recognition197](weight-four-normalized-square-root-quadratic-projection-recognition-pass197-working.md).
Its scalar Jacobian forces a quadratic function of \(q\); exact field
return removes its quadratic term. The resulting polynomial inverse
gives the following particularly explicit endpoint.

## 2. The original polynomial inverse, after actual normalization

For constants \(b\in\mathbb C^*\) and \(c,d\in\mathbb C\), put
\[
\begin{aligned}
J&=\frac{d-Z^2+X^3Y+2X(W-c)}{2b},\\
z&=Z-XJ,\\
q&=\frac{W-c-zJ-XJ^2/2+X^2Y/2}{b},\\
y&=Y-q^2X .
\end{aligned}
\tag{3}
\]
Here \(b,c,d\) are the constants obtained after the actual
normalization and are not identified with the initial \(\beta_0\)
without the intervening derivation.
Only a nonzero complex constant is divided out.

Writing \(H=(d-z^2)/(2b)\), the inverse formulas are
\[
\begin{aligned}
Y&=y+q^2X,\\
Z&=z+HX+qX^2,\\
W&=c+bq+Hz+(qz+H^2/2)X+(qH-y/2)X^2 .
\end{aligned}
\tag{4}
\]
Both composition orders are proved as polynomial identities.
Thus \(B=\mathbb C[X,y,z,q]\), and the three recovered entries
are actually in the invariant ring. In these coordinates
\(E=(EX)\partial_X\). The global slice makes \(EX\) a nonzero
complex constant, and \(A=\mathbb C[y,z,q]\).

Composing (3) with the earlier normalization maps gives polynomial
invariants in the original, unnormalized four-ring. This is not
merely a birational parametrization or an inverse after localizing
at \(X\).

The formulas also define genuine examples with the full initial
kernel in (1). The written proof calculates the selected intrinsic
derivation and the calibrated scalar determinant for those examples.
Therefore the quadratic-projection branch is nonempty; it must be
recognized, not excluded by an argument imported from the graph.

## 3. Verification and what remains

The new [three-method finite checker197](weight_four_square_root_quadratic_projection_controls_pass197.py)
tests the raw scalar and potential identities, the literal selected
partial-derivative columns, both polynomial inverse orders, and the
exact leading time degrees. It does not prove field return, the
field-intersection argument, or arbitrary entry into (1).
The exact canonical execution and saved-source reviews are recorded
separately in the197 verification record.

For the same full initial kernel, zero-R recognition was already
supplied in195. In the nonzero-R branch, classification195 still
leaves the nonmonomial family \(f=at+bq\) with \(a\ne0\), and the
different reciprocal family \(f=b/q\), unresolved. For the two-root
form \(q^2=t(1-t)\), its nonzero-R square alternatives also remain.
No entire positive-quadratic-rank classification, higher-profile
reduction, or arbitrary coordinate-entry theorem has been proved.

The full goal remains active and unsolved. These are written
restricted proofs with AI source review and finite algebraic checks,
not human expert review, proof-assistant certification, or novelty
clearance. No external contact, public posting, or submission has
occurred, and no196 or earlier source was changed.

