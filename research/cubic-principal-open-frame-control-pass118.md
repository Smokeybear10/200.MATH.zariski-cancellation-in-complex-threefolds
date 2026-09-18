# A cubic relative curve with an exact principal-open coordinate frame

The cubic branch is compatible with the actual moving-frame differential
identities and a constant nonzero coordinate Jacobian on a principal open
set. The following example has an explicit coordinate inverse there.
Its transported derivation has a genuine pole on the omitted divisor, so
it is not an original polynomial constant-acceleration frame on all of
affine four-space. In particular it is not a cancellation counterexample.

This is a boundary control for the cubic branch of
[the volume calculation90](nonconical-cubic-relation-pass90.md).
It is separate from the quadratic-frame reduction in
[the velocity shear117](quadratic-velocity-shear-pass117.md), whose
recognition endpoint retains the stated working theorem80 dependency.

## 1. The localized coordinate map

Work over the complex numbers and put
\(R=\mathbb C[s,s^{-1},t,v,u]\). Take \(q=1\) and define
\[
\begin{gathered}
b=(s,t,s^3)^t,\qquad \rho=0,\qquad \chi=t/s^3,\\
y_1=v,\qquad y_2=s+3tv/s+4v^3,\\
X_1=su+v,\qquad
X_2=s+tu+3tv/s+4v^3,\\
X_3=s^3u+3s^2v,\qquad
Z=u^2/2+3v^2/(2s^2)+t/s^3.
\end{gathered}
\tag{1}
\]
Thus \(X_{\rm tr}=bu+b_s y_1+b_t y_2\), exactly in the
moving-frame form, not merely a choice of unrelated connection arrays.
The derivation \(E=\partial_u\) of R has slice u and satisfies
\(E^2X_i=0\), \(EZ=u\), and \(E^2Z=1\).

Let \(B=\mathbb C[X_1,X_2,X_3,Z]\) be an abstract polynomial
ring and set \(\Sigma=X_2-ZX_3+X_1^3/2\). The formulas (1) give
\[
\begin{gathered}
\Sigma=s,\qquad
v=\frac{X_3-\Sigma^2X_1}{2\Sigma^2},\qquad
u=\frac{3\Sigma^2X_1-X_3}{2\Sigma^3},\\
t=\Sigma^3Z-\frac32\Sigma X_1^2
   +\frac{3X_1X_3}{2\Sigma}-\frac{X_3^2}{2\Sigma^3},\\
B[1/\Sigma]\ \simeq\ R .
\end{gathered}
\tag{2}
\]
For both inverse orders, first solve the two linear equations for
\(X_1,X_3\) to obtain u and v. Solving the expression for Z gives
t. Substitution in the remaining expression for \(X_2\) gives
\(\Sigma+ZX_3-X_1^3/2\). Conversely, substituting (1) in
\(\Sigma\) gives s and the same linear equations recover u and v,
followed by t. These are polynomial identities after clearing powers
of the displayed localization elements. In particular the four
functions in (1) are algebraically independent.

## 2. Exact moving-frame compatibility and cubic relation

The determinant \(\Omega=\det[b,b_s,b_t]\) and the only nonzero
coefficients of the second-derivative decomposition are
\[
\Omega=-2s^3,\qquad
G_{11}=-3/s^2,\qquad
C^1_{11}=3/s,\qquad C^2_{11}=3t/s^2.
\tag{3}
\]
All entries with a second-derivative index 2 vanish. Directly,
\(b_{ss}=G_{11}b+C^1_{11}b_s+C^2_{11}b_t\), while
\(b_{st}=b_{tt}=0\). Therefore the actual mixed-derivative
compatibilities hold. The cubic tensor defined in90 is zero except
for \(T_{111}=-24/s^3\).

With formal variables \(Y_1,Y_2\), the potential and its relation are
\[
\begin{gathered}
\Psi=-\frac{3Y_1^2}{2s^2},\qquad
\Phi=-\frac{3tY_1}{s^4}+\frac{Y_2}{s^3}
                  -\frac{4Y_1^3}{s^3},\qquad
\zeta=\frac1{s^2},\\
F=Y_2-s-\frac{3t}{s}Y_1-4Y_1^3,\qquad
\Phi-\zeta=F/s^3,\\
\mathbb C[s,s^{-1},t][y_1,y_2]
 =\mathbb C[s,s^{-1},t][v],\qquad \deg_YF=3.
\end{gathered}
\tag{4}
\]
The kernel is exactly (F), because F is monic linear in \(Y_2\)
and \(y_1=v\). This does not make its total relative degree one.
The expression for Z in (1) is \(\chi-\Psi(s,y)+u^2/2\), as
required by the retained potential formula.

In the original base coordinates and with v held fixed, the remaining
two-by-two block and gradient are
\[
\begin{gathered}
K=\begin{pmatrix}3v/s&0\\1&3v/s\end{pmatrix},\qquad
(Z_1,Z_2)=\left(-3t/s^4-12v^2/s^3,\ 1/s^3\right),\\
\det\begin{pmatrix}
u+K_{11}&K_{12}&1\\
K_{21}&u+K_{22}&3t/s+12v^2\\
Z_1&Z_2&0
\end{pmatrix}=1/s^3,\qquad
\det\frac{\partial(X_1,X_2,X_3,Z)}{\partial(u,s,t,v)}=-2.
\end{gathered}
\tag{5}
\]
The displayed K includes the base derivatives of \(y_2\). For
example its lower-left entry is
\(1-3tv/s^2+C^2_{11}v=1\). Omitting that derivative would
destroy the constant term that makes the determinant a unit.

## 3. Affine normalization is not a base-coordinate change

The cubic graph can be written as the tangent-vector-valued polynomial
\(y=D+vX+v^3V\), where
\[
\begin{gathered}
D=s\partial_t,\qquad
X=\partial_s+(3t/s)\partial_t,\qquad V=4\partial_t,\\
\nabla_XX=(3/s)X,\quad \nabla_XV=0,\quad
\nabla_VX=(3/s)V,\quad \nabla_VV=0,\\
\nabla_XD=V/4,\qquad \nabla_VD=0,\qquad
[X,V]=-(3/s)V.
\end{gathered}
\tag{6}
\]
Here \(\nabla\) is defined by the actual C coefficients in (3).
Thus X,V are an invertible moving basis but are not commuting base
coordinate fields. This example satisfies the normalized cubic
determinant constraints while explicitly retaining their commutator.
It does not justify imposing coordinate-index symmetry on a
base-dependent affine normalization.

## 4. The exact global failure

The polynomial \(\Sigma\) is prime: it is monic linear in \(X_2\),
and \(B/(\Sigma)\simeq\mathbb C[X_1,X_3,Z]\). At the point
\((X_1,X_2,X_3,Z)=(0,0,1,0)\), its value is zero whereas the
numerator of the formula for u in (2) is \(-1\). Consequently
\[
u\notin B,\qquad E(Z)=u\notin B,
\qquad E(B)\not\subset B.
\tag{7}
\]
No polynomial derivation of B restricts to this E on \(B[1/\Sigma]\).
There is also a separate invariant-base boundary: the polynomial
speed tuple \((s,t,s^3)\) generates the proper ideal \((s,t)\) in
\(\mathbb C[s,t]\), although it becomes unimodular after s is
inverted. Thus neither the global slice nor the global original-frame
speed hypotheses have been supplied. The
[cylinder exclusion118](cubic-cylinder-velocity-exclusion-pass118.md)
uses that global speed gate to exclude this surviving local family.

## 5. A unimodular-speed pullback still has the pole

Set \(t_{\rm old}=s t-1\) in the preceding principal-open example.
This is an isomorphism of the s-localized base planes, with inverse
\(t=(t_{\rm old}+1)/s\), but not an automorphism of the whole
polynomial base plane. The new data satisfy
\[
\begin{gathered}
\widetilde b=(s,st-1,s^3)^t,\qquad
t\widetilde b_1-\widetilde b_2=1,\qquad
\widetilde\Omega=-2s^4,\\
\widetilde G_{11}=-3/s^2,\qquad
\widetilde T_{111}=-24/s^3,\qquad
\widetilde G_{12}=\widetilde G_{22}
 =\widetilde T_{112}=\widetilde T_{122}=\widetilde T_{222}=0,\\
\widetilde y_1=v,\qquad
\widetilde y_2=1+(2t/s-3/s^2)v+4v^3/s,\qquad
\widetilde{\mathcal J}=-2s .
\end{gathered}
\tag{8}
\]
The relative vector changes by the inverse base Jacobian, which gives
the displayed \(\widetilde y\); it must not be left unchanged.
The new connection additionally has
\(\widetilde C^2_{11}=-3/s^3\) and
\(\widetilde C^2_{12}=\widetilde C^2_{21}=1/s\), while
\(\widetilde C^1_{11}=3/s\) and its other entries vanish.
These verify the tensor assertions directly.

The inverse (2) still applies, with the final base variable replaced
by \((t_{\rm old}+1)/\Sigma\). The formula for u and its pole
witness are unchanged. Thus even a globally unimodular polynomial
speed row, nonzero rank-one cubic tensor, and exact principal-open
coordinate inverse do not make this transported E polynomial on B.
The cylinder theorem uses its specified whole-base coordinate form;
this noninvertible whole-base substitution cannot extend that theorem
to every rank-one cubic tensor with unimodular speed.

The separate [polynomial-pullback exclusion118](cubic-polynomial-pullback-exclusion-pass118.md)
now excludes this entire velocity family as a global original frame,
using original-coordinate irreducibility rather than the speed row
alone. Both localized controls remain valid. They demonstrate exactly
why their local identities and, in (8), unimodular speed do not supply
the missing global polynomial derivation.

## Verification scope

[The shared checker118](cubic_moving_frame_checks_pass118.py) has
three finite symbolic methods. Its principal-open method checks both
inverse orders, both actual connections, the potential identities,
the Jacobians and the explicit pole witness, including (8). The other
methods check the general affine-block coefficient and rank-one metric
identities and bounded cylinder residual calculations. None proves a
universal geometric classification or supplies a global original
polynomial frame.
The displayed control and its scope are proved algebraically above;
test execution and independent written reviews are separate evidence.

The author ran the final three-method checker once in execution
`bfd035`: all three passed in 0.658 seconds of unittest time,
0.911114583 seconds of command wall time, exit zero. Complete saved
code and proof reads were `a2d712` and `f7c0b9`, followed by the
metadata and whitespace check `cfba88`. The subsequent provenance and
forward-status additions do not change the checker or add numerical
coverage; the linked global exclusion is a separate written proof.
