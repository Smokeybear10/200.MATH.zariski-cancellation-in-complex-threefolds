# A hyperbolic quadratic coefficient reduces to an explicit coordinate

Let

\[
 P=xy-1,\qquad F=Pu+H(x,y,z)\in\mathbb C[x,y,z,u].
\]

There is no degree bound on \(H\). The following are equivalent:

1. \(F\) is a stable coordinate.
2. \(F\) is an LND slice.
3. \(F\) is a coordinate.
4. Under the identification \(y=x^{-1}\) on \(P=0\),
   \[
   H(x,x^{-1},z)=c x^k z+B(x),\quad
   c\in\mathbb C^*,\ k\in\mathbb Z,\ B\in\mathbb C[x,x^{-1}].
   \]

This is a working proof reconstructed in a separate model audit, with
supplementary exact inverse checks. No originality is claimed. Its purpose
is to close a precise quadratic-coefficient branch,
not to claim that every cubic slice has this form.

## 1. The cylinder hypothesis determines the intersection curves

Assume \(F\) is a stable coordinate. Every fiber \(X_\lambda=V(F-\lambda)\)
is smooth and its integral compactly supported cohomology is that of
complex affine three-space. This follows from
\(X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}\), the homotopy
equivalence induced by the projection, and Poincaré duality.

Write \(D=V(P)\subset\mathbb A^3_{x,y,z}\). Then
\(D\simeq\mathbb C^*\times\mathbb A^1\), and

\[
 H_c^j(D;\mathbb Z)=
 \begin{cases}\mathbb Z,&j=3,4,\\0,&\text{otherwise}.\end{cases}
\]

The open part of \(X_\lambda\) where \(P\ne0\) is
\(U=\mathbb A^3\setminus D\), by solving for \(u\).
The closed-open sequence for \(D\subset\mathbb A^3\) gives

\[
 H_c^4(U)=\mathbb Z,\quad H_c^5(U)=\mathbb Z,\quad
 H_c^6(U)=\mathbb Z
\]

and zero groups in smaller degrees.

Let \(h=H|_D\). Since \(F\) has no critical point, \(h\) is a smooth map:
if \(dh=0\) at a point of \(D\), then
\(\nabla H=\mu\nabla P\) there, and \(u=-\mu\) would be a critical
point of \(F\). Thus each \(C_\lambda=h^{-1}(\lambda)\) is a smooth
affine curve, or empty.

The closed complement of \(U\) in \(X_\lambda\) is
\(Z_\lambda=C_\lambda\times\mathbb A^1\). The vanishing of
\(H_c^j(X_\lambda)\) for \(j<6\) forces

\[
 H_c^1(C_\lambda;\mathbb Z)\simeq H_c^4(U;\mathbb Z)=\mathbb Z,
 \qquad
 H_c^2(C_\lambda;\mathbb Z)\simeq H_c^5(U;\mathbb Z)=\mathbb Z.
 \tag{1}
\]

These statements hold for every \(\lambda\). The second makes the curve
nonempty and connected. If \(g\) is its projective genus and \(r\ge1\)
its number of points at infinity, the first says \(2g+r-1=1\).
Consequently \(g=0,r=2\), and \(C_\lambda\simeq\mathbb C^*\).

## 2. The restricted polynomial is affine-linear in the radical variable

Use \(x,z\) as coordinates on
\(D=\operatorname{Spec}\mathbb C[x,x^{-1},z]\).
On any \(C_\lambda\simeq\mathbb C^*\), the invertible function \(x\)
is nonconstant. Otherwise the curve would be a one-dimensional closed
subset of the line \(x=a\) in \(D\), hence that whole affine line,
contradicting \(C_\lambda\simeq\mathbb C^*\).

Every nonconstant unit on \(\mathbb C^*\) has the form \(a t^n\),
\(n\ne0\). In characteristic zero this map to \(\mathbb C^*\) is étale.
Therefore \(x|_{C_\lambda}\) has no critical point.

The map \(h\) is smooth, so a nonzero tangent vector to its fiber in
the \(x,z\) coordinates is \((h_z,-h_x)\). The derivative of \(x\)
on that tangent is \(h_z\). Thus \(h_z\) never vanishes anywhere on
any fiber, hence anywhere on \(D\). The only units in
\(\mathbb C[x,x^{-1},z]\) are \(c x^k\), so

\[
 h_z=c x^k,\qquad h=c x^k z+B(x).
\]

This proves the required necessity without an assertion that Euler
characteristic alone characterizes affine space.

## 3. Explicit positive coordinates

Conversely, assume the displayed restricted form. Lift \(c x^k\) to
\(a(x,y)=c x^k\) if \(k\ge0\), and to \(c y^{-k}\) if \(k<0\).
Lift the Laurent polynomial \(B\) to \(b(x,y)\), replacing negative
powers of \(x\) by positive powers of \(y\). Then

\[
 H=a z+b+PK
\]

for a polynomial \(K(x,y,z)\). The triangular change \(U=u+K\) gives
\[
 F=PU+az+b.
\]

Since \(a\) is a unit modulo \(P\), choose \(A,B_0\in\mathbb C[x,y]\)
with \(AP+B_0a=1\). Such a pair is explicit. For \(k\ge0\), take
\[
 B_0=c^{-1}y^k,\qquad
 A=\frac{1-(xy)^k}{xy-1};
\]
the quotient is polynomial, including \(A=0\) when \(k=0\).
For \(k<0\), interchange \(x\) and \(y\) and use \(-k\).

The matrix
\[
 \begin{pmatrix}P&a\\-B_0&A\end{pmatrix}
\]
has determinant one. Put \(Z=PU+az\) and \(W=-B_0U+Az\).
Then \((x,y,Z,W)\) is a polynomial coordinate system, with inverse
\[
 U=AZ-aW,\qquad z=B_0Z+PW.
\]
Finally \(F=Z+b(x,y)\) is a coordinate by translation. Coordinates
are slices, and slices become coordinates after one stabilization.
This closes the equivalence.

## Scope

The same statement applies after an affine change and nonzero rescaling
to any rank-two quadratic coefficient with nonzero completed-square
constant and no linear term in its radical. Coefficients having a
nonzero radical-linear term are already coordinates themselves.

The proof uses integral cohomology and explicit polynomial inverses.
It is not a proof-assistant certificate. Known general results for
jointly affine-linear polynomials apply after the reduction in Section 3;
the exact prior-work overlap of this formulation is not established.
