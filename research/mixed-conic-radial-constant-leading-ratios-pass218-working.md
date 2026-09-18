# Radial-constant leading ratios in the remaining mixed conic

Status: new working necessary condition, separate from the217 packet.
The normalized conic is not recognized or excluded. This note retains
the full supplied-frame hypotheses, rather than asserting a result for
an arbitrary cancellation instance.

## 1. Normalized actual conic and exact radial derivatives

Use the actual exact1122 frame with full initial kernel \(ZW-X^2Y^2\)
and the selected chart of
[the quadratic reduction217](rank-two-mixed-ratio-quadratic-graph-reduction-pass217-working.md).
Assume its case II. The optional actual good-coordinate interchange in
that note makes all three projected intercepts quadratic; when applying
the radial conclusion to that changed chart, its coefficients and
potentials must be rebuilt. Nothing below preserves an old \(k\) through
the interchange.

The actual chart has
\[
\begin{gathered}
h=t/\rho,\quad \xi=y-h\vartheta,\quad
\deg_v\xi=1,\quad
\vartheta=\alpha\xi^2+b\xi+c,\quad \alpha\ne0,\\
y=h\vartheta+\xi,\qquad
w=d\xi^2+e\xi+f,\qquad \deg_vz\le2,\qquad
L[y,z,w]=L[v].
\end{gathered}
\tag{1}
\]
All coefficients are in the exact field \(L\), finite over
\(\mathbb C(t,\rho)=\mathbb C(h,\rho)\).
Let
\[
\mathcal D=h\partial_t+\partial_\rho,\qquad
\partial_h=\rho\partial_t .
\tag{2}
\]
These are the commuting extensions of differentiation in the independent
variables \(\rho,h\), respectively: \(\mathcal Dh=0\),
\(\mathcal D\rho=1\), \(\partial_hh=1\), and
\(\partial_h\rho=0\). Let \(L_0=\ker_L\mathcal D\).
No assertion \(L_0=\mathbb C(h)\) or \(L=\mathbb C(h,\rho)\) is made.
The derivative \(\partial_h\) preserves \(L_0\).

The case-II radial identities from217 are
\[
K=\mathcal D^2k/2\ne0,\qquad
\mathcal D^3k=-6K/\rho,\qquad
\alpha=1/(K\rho^2).
\tag{3}
\]

## 2. Exact integration without changing the constant field

Define
\[
C=\rho^3K,\qquad
F=\mathcal Dk+C/\rho^2,\qquad
G=k-C/\rho-F\rho .
\tag{4}
\]
Equation (3) gives \(\mathcal DK=-3K/\rho\).
Direct differentiation of (4), in order, proves
\[
C\in L_0^*,\quad F,G\in L_0,\qquad
k=C/\rho+F\rho+G,\qquad \alpha=\rho/C .
\tag{5}
\]
For instance \(\mathcal DF=\mathcal D^2k-2C/\rho^3=0\);
then \(\mathcal DG=\mathcal Dk+C/\rho^2-F=0\).
These are identities inside \(L\), not an assumption that a solution
of an ordinary differential equation is rational over the original
two-variable field.

Put \(\delta=d/\alpha\). The second universal potential, in the
variables of (1), reads
\[
z=-h^2w+\xi^2/\rho+k_t\xi+(\mathcal Dk)\vartheta+n .
\tag{6}
\]
Since \(\mathcal Dk=-C/\rho^2+F\) and \(\alpha=\rho/C\),
the coefficient of \(\xi^2\) in \(z\) is
\(\alpha F-h^2d\). The first potential is
\(\sigma=2hy-h^2\vartheta+k\), whose quadratic coefficient is
\(h^2\alpha\).
For the actual coordinates
\[
Y=y+tX,\quad Z=z+\sigma X+(t^2/\rho)X^2,\quad
W=w+\vartheta X+\rho X^2,
\tag{7}
\]
their quadratic coefficients in \(\xi\), as a column ordered \(Y,Z,W\),
are therefore
\[
\alpha\,c(X),\qquad
c(X)=
\begin{pmatrix}
h\\ F+h^2(X-\delta)\\ X+\delta
\end{pmatrix}.
\tag{8}
\]
Here \(X\) is independent of \(L\) and is held fixed under the three
chart derivatives.

## 3. The highest Jacobian coefficient forces a radial constant

The actual calibrated determinant in the coordinates \((t,\rho,v)\)
is \(-a^3\). Replacing these by \((h,\rho,\xi)\) changes it to
\[
\det\frac{\partial(Y,Z,W)}{\partial(h,\rho,\xi)}
=-a^3\,\frac{\rho}{\xi_v}\in L^* .
\tag{9}
\]
This follows from \(t=h\rho\) and the affine dependence of \(\xi\)
on \(v\). Dependence of that affine coordinate's coefficients on
\(h,\rho\) only adds multiples of the third column in the chain rule.
In particular the right side of (9) has no positive \(\xi\)-degree.
This is a change of parameters in the localized chart, not an ambient
coordinate change.

The coefficient of \(\xi^5\) on the left side is
\[
\begin{aligned}
&\det\bigl(\partial_h(\alpha c),\mathcal D(\alpha c),2\alpha c\bigr)\\
&\hspace{6mm}
=2\alpha^3(\mathcal D\delta)
       \{h\,\partial_hF-F-2h^2\delta\}.
\end{aligned}
\tag{10}
\]
Terms involving derivatives of the common factor \(\alpha\) disappear
because two columns become proportional. Expanding the remaining
three-by-three determinant gives (10), using
\(\mathcal DF=0\). All lower coefficients of \(Y,Z,W\) have degree at
most one and cannot contribute degree five.

Thus the product of the two final factors in (10) is zero in \(L\).
If \(\mathcal D\delta\ne0\), the bracket vanishes. Differentiating
that bracket by \(\mathcal D\), and using the commutation in (2),
then gives \(-2h^2\mathcal D\delta=0\), a contradiction.
Consequently
\[
\boxed{\delta=d/\alpha\in L_0.}
\tag{11}
\]
The normalized leading column (8) is therefore radial-constant.
This statement alone does not make its entries complex constants,
rational functions of \(h\), or regular functions in the original ring.

## 4. The next coefficient of the quadratic graph

Write \(C_h=\partial_hC\) and \(G_h=\partial_hG\). From (5),
\[
k_t=C_h/\rho^2+F_h+G_h/\rho,\qquad
\mathcal Dk_t=-2C_h/\rho^3-G_h/\rho^2 .
\tag{12}
\]
In the transformed third potential, the only terms contributing
\(\xi^3\) after substitution of \(\vartheta=\alpha\xi^2+b\xi+c\)
are
\[
K\vartheta^2-\rho^{-2}\xi^2\vartheta
       +(\mathcal Dk_t)\xi\vartheta .
\]
Their cubic coefficient is
\[
\frac{b-2C_h/C}{\rho^2}-\frac{G_h}{C\rho}.
\]
As \(Rw\) equals the negative third potential, and the leading
coefficient of \(R\) is \(-2h/\rho\), this gives
\[
d=\frac{b-2C_h/C}{2h\rho}-\frac{G_h}{2hC},\qquad
\boxed{b=\frac{2C_h+G_h\rho+2h\delta\rho^2}{C}.}
\tag{13}
\]
In particular this coefficient is explicitly at most quadratic in
\(\rho\) over \(L_0\). The factor \(\rho^2\) in its final summand
comes from \(d=\alpha\delta=\rho\delta/C\); it must not be dropped.
No assertion about the remaining coefficients \(c,e,f,n,\ell,m\)
follows without using further equations.

## 5. Scope and checks

The stable217 conic note was fully read before this continuation.
Fresh inline algebra6cbb6d checks the exact determinant factor in
(10) with arbitrary \(F(h)\) and \(\delta(h,\rho)\). It does not
prove the actual-chart determinant or field statements.
No saved checker has been run for this note, and no217 or earlier
source or verification packet was edited to incorporate it.

This is a necessary leading-coefficient restriction in a remaining
conic branch. The lower potentials and scalar determinant have not
been solved, and the original invariant-coordinate problem remains.
There is no arbitrary-entry, unrestricted cancellation, formal
verification, human-review or novelty claim.
