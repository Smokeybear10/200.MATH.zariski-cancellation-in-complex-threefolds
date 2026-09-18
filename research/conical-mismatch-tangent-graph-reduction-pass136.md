# A tangent-graph reduction for nonradial conical speeds

For an actual sliced three-good quadratic frame with nonlinear conical
speeds, nonradial acceleration gives a two-dimensional coefficient field
adapted to one actual good coordinate. The unit Jacobian in that chart
forces the generic intrinsic affine line to be a polynomial graph.

This is a reduction inside the supplied frame. It neither recognizes
the remaining action nor supplies such a frame for an arbitrary cylinder.
In particular, the original bad-coordinate partial does not preserve the
coefficient field in this nonlinear branch.

## 1. Actual hypotheses and the coefficient field

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad E^3W=0,\\
s=EX,\quad t=EY,\quad r=EZ,\quad q=E^2W,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,r)=2,\qquad
\ker(\mathbb C[S,T,R]\longrightarrow A)=(H),
\end{gathered}
\tag{1}
\]
where \(H\) is irreducible homogeneous of degree at least two.
All four original generators are actual polynomial coordinates.
The given slice \(u\) need not be an ambient coordinate.

Put \(T=\partial_W\), holding the three original goods fixed.
The conical selected-partial theorem gives exact adjoint degree one:
\(T(A)\subset A[u]_{\le1}\), \(T(u)\in A[u]_{\le1}\), and
\(N=[u]T|_A\) is a nonzero locally nilpotent derivation of \(A\).
It fixes \(s,t,r,q\). The degree-zero alternative is impossible under
the nonlinear homogeneous relation in (1).[^1]

Set \(S_0=\ker_A N\), \(L=\operatorname{Frac}S_0\).
An intrinsic local slice gives \(\operatorname{Frac}A=L(v_0)\);
in particular \(L\) has transcendence degree two. The field
\(L/\mathbb C(s,t,r)\) is finite and separable. One elementary
justification is to choose two independent speeds: their field,
together with \(v_0\), has finite index in the finitely generated
field \(\operatorname{Frac}A\); adjoining the transcendental \(v_0\)
preserves linear independence among elements of \(L\).

The homogeneous Euler derivation extends uniquely to
\(\mathcal R\) on \(L\), with
\(\mathcal R(s)=s,\mathcal R(t)=t,\mathcal R(r)=r\).
Assume \(\mathcal R(q)\ne2q\). No coordinate speed can vanish,
and no two have constant ratio, since either would give a linear
homogeneous relation. Thus the following definitions are valid:
\[
\tau=t/s,\qquad \rho=r/s,\qquad \sigma=q/s^2,\qquad
\mathcal R(\tau)=\mathcal R(\rho)=0,\qquad
\mathcal R(\sigma)=\frac{\mathcal R(q)-2q}{s^2}\ne0.
\tag{2}
\]
The projective speed field \(\mathbb C(\tau,\rho)\) has
transcendence degree one. Indeed it has a nonzero relation obtained
by setting \(S=1\) in \(H\), and \(\tau\) is nonconstant.
Consequently \(\rho\) is algebraic over \(\mathbb C(\tau)\).
If \(\sigma\) were algebraic over \(\mathbb C(\tau)\),
separability and (2) would give \(\mathcal R(\sigma)=0\).
Therefore \(\tau,\sigma\) are algebraically independent.

It follows that \(L/\mathbb C(\tau,\sigma)\) is finite and
separable, by the same finite-index argument using \(v_0\).
Extend \(\partial_\tau,\partial_\sigma\) uniquely through this
extension. They commute. The extended \(\partial_\sigma\) kills
\(\rho\), and we write \(\rho'=\partial_\tau\rho\) and
\(\rho''=\partial_\tau^2\rho\).
All these assertions concern the actual coefficient field, not a
chosen component after an unspecified extension.

## 2. The fixed-\(X\) localization is an actual polynomial chart

Localize at the invariant \(s\), and put \(D=E/s\).
Then \(D\) is locally nilpotent on \(B_s\), with \(DX=1\).
If \(b_X=X-su\in A\), the slice theorem and finite Taylor projection
give
\[
\begin{gathered}
B_s=A_s[X],\qquad
A_s=\mathbb C[y,z,w]_{s_0(y,z,w)},\qquad
s=s_0(y,z,w),\\
s_0(Y,Z,W)=s(0,Y,Z,W)\ne0,\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=w+dX+\tfrac12\sigma X^2,\qquad d\in A_s.
\end{gathered}
\tag{3}
\]
Here \(y,z,w\) are the Taylor projections of \(Y,Z,W\) for the
slice \(X\) of \(D\). To see the ring equality precisely, quotient
\(B_s=A_s[X]\) by \(X\), then use the original coordinate ring:
\(B_s/(X)\simeq\mathbb C[Y,Z,W]_{s_0}\).
Its nonzero value proves \(s_0\ne0\).
Projecting the invariant \(s\) proves the displayed identity for \(s\).
In particular \(y,z,w\) are algebraically independent.

The forward substitution (3) and the Taylor inverse are inverse
isomorphisms of the actual localized polynomial rings. Their
Jacobian determinants multiply to one. After pulling back to
\(\mathbb C[y,z,w]_{s_0}[X]\), the forward determinant is therefore
a unit. Units in this polynomial ring are independent of \(X\).
At \(X=0\) the last three coordinates are \(y,z,w\), so the
Jacobian of \((X,Y,Z,W)\) with respect to \((X,y,z,w)\) is exactly
one. This is an actual inverse argument, not an inference that a
unit Jacobian alone supplies an inverse.[^2]

Re-expanding the degree-one coefficient of \(T\) using
\(u=(X-b_X)/s\) yields
\[
N'=[X]T|_{A_s}=s^{-1}N,\qquad
N'\in\operatorname{LND}(A_s)\setminus\{0\},\qquad
A_L=L[v],\quad N'v=1,\quad A_L=L[y,z,w].
\tag{4}
\]
The quotient rule proves the same coefficient identity on fractions.
Local nilpotence follows by localizing \(N\) at its invariant \(s\)
and multiplying by the invariant unit \(s^{-1}\).
It is not asserted that \(T\) stays locally nilpotent after this
localization.

Here \(A_L=(S_0\setminus\{0\})^{-1}A\).
For completeness, choose an intrinsic local slice \(a\) with
\(Na=h\in S_0\setminus\{0\}\). Then
\(A_L=L[a/h]\), and \(v=sa/h\) satisfies \(N'v=1\).
Since \(s=s_0(y,z,w)\) already lies in \(L^*\), the denominator
in (3) disappears over \(L\), giving the final equality in (4).
Thus the generic fiber is the whole affine line, not merely an
open subset. Extend \(\partial_\tau,\partial_\sigma\) to fix \(v\),
so that \(N'=\partial_v\).

## 3. The tangent graph and its nonzero denominator

Let \(J(X)\) be the Jacobian of \((Y,Z,W)\) with respect to
\((\tau,\sigma,v)\), holding \(X\) fixed.
The unit Jacobian in Section 2 gives \(J(X)=J_0\in L(v)^*\),
independent of \(X\).
In this section coefficient subscripts initially mean derivatives
at fixed \(v\). The rows of this matrix are
\[
\begin{pmatrix}
y_\tau+X&y_\sigma&y_v\\
z_\tau+\rho'X&z_\sigma&z_v\\
w_\tau+d_\tau X&w_\sigma+d_\sigma X+X^2/2&w_v+d_vX
\end{pmatrix}.
\tag{5}
\]
Its possible fourth-degree coefficient is zero because the
degree-one parts of its first two rows occupy the same column.
Its third-degree coefficient is
\((\rho'y_v-z_v)/2\). Hence
\[
z=\rho'y+k,\quad k\in L,\qquad
\alpha(\xi)=\rho''\xi+k_\tau,\quad \beta=k_\sigma,\qquad
J_0=\beta\ne0 .
\tag{6}
\]
The first equality follows by integration in \(v\), meaning that
\(\partial_v(z-\rho'y)=0\). To prove the last assertion rather
than assume it, Cramer's rule before this substitution gives
\[
\begin{aligned}
T(\tau)&=(y_\sigma z_v-y_vz_\sigma)/J_0,\\
T(\sigma)&=(y_vz_\tau-y_\tau z_v
                  +X(\rho'y_v-z_v))/J_0,\\
T(v)&=(y_\tau z_\sigma-y_\sigma z_\tau
                  +X(z_\sigma-\rho'y_\sigma))/J_0,\qquad T(X)=0 .
\end{aligned}
\tag{7}
\]
These formulas apply to the derivation on the actual fraction field.
The coefficient rule (4), also valid there, and \(N'v=1\) give
\(1=(z_\sigma-\rho'y_\sigma)/J_0=k_\sigma/J_0\).
This proves \(\beta=J_0\ne0\). Although a generic Jacobian unit
was initially only in \(L(v)^*\), this computation places it in
\(L^*\).

Subtract \(\rho'\) times the first row of (5) from its second row.
The second row becomes \((\alpha(y),\beta,0)\). With
\(C=\beta y_\tau-\alpha(y)y_\sigma\), the full determinant is
\[
J(X)=(C+\beta X)(w_v+d_vX)
 +y_v\{\alpha(y)(w_\sigma+d_\sigma X+X^2/2)
                     -\beta(w_\tau+d_\tau X)\}.
\tag{8}
\]
If \(y_v=0\), its quadratic coefficient gives \(d_v=0\), and
its linear coefficient then gives \(w_v=0\), since \(\beta\ne0\).
Together with \(z_v=\rho'y_v=0\), these would make the
determinant zero. Therefore \(y_v\ne0\).

## 4. The remaining coefficients are polynomial in the line parameter

The quadratic coefficient of (8) gives
\(d_v=-\alpha(y)y_v/(2\beta)\).
Define the polynomial in the formal variable \(\xi\)
\[
\begin{gathered}
\mathfrak d(\xi)=
-\frac{\rho''}{4\beta}\xi^2-\frac{k_\tau}{2\beta}\xi+\ell,
\qquad \ell\in L,\qquad d=\mathfrak d(y),\\
\mathfrak w(\xi)=
\int_0^\xi
\left(\mathfrak d_\tau(\zeta)
       -\frac{\alpha(\zeta)}{\beta}\mathfrak d_\sigma(\zeta)\right)
\,d\zeta+m,\qquad m\in L,\qquad w=\mathfrak w(y).
\end{gathered}
\tag{9}
\]
The first constant is defined by subtracting the displayed
quadratic expression from \(d\), then using
\(\ker\partial_v=L\).
In the second line, the subscripts differentiate coefficients at
fixed formal variable; the integral is only polynomial integration
in \(\zeta\), valid in characteristic zero. It does not assume
that a coefficient has an antiderivative in \(\tau\) or \(\sigma\).

To verify that line, expand the linear coefficient of (8) and
substitute the first line. Its terms involving \(y_\tau,y_\sigma\)
cancel, leaving
\(w_v=(\mathfrak d_\tau(y)
-\alpha(y)\mathfrak d_\sigma(y)/\beta)y_v\).
Subtracting the formal integral evaluated at \(y\) leaves an
element killed by \(\partial_v\), which defines \(m\).
Consequently \(\deg_\xi\mathfrak d\le2\) and
\(\deg_\xi\mathfrak w\le4\).

Equations (4), (6), and (9) now give
\(L[v]=L[y,z,w]=L[y]\).
Since \(y\in L[v]\) is nonconstant, equality of these polynomial
rings forces \(y=av+b\), with \(a\in L^*\) and \(b\in L\).
For example, write \(v=P(y)\) and compare polynomial degrees.
Thus \(y_v=a\in L^*\); this conclusion was not assumed when
the determinant coefficients were taken.

The remaining constant coefficient of (8), and the complete
Cramer formulas, reduce to
\[
\begin{gathered}
1=y_v\left(
\frac{\alpha(y)}{\beta}\mathfrak w_\sigma(y)
                -\mathfrak w_\tau(y)\right),\\
T(\tau)=-y_v,\qquad
T(\sigma)=\frac{\alpha(y)}{\beta}y_v,\qquad
T(v)=X+y_\tau-\frac{\alpha(y)}{\beta}y_\sigma,\qquad T(X)=0 .
\end{gathered}
\tag{10}
\]
The derivatives on \(\mathfrak w\) again hold its formal variable
fixed; those on \(y\) hold \(v\) fixed.
The scalar identity is a further compatibility condition, not
a statement that arbitrary choices of its coefficients are realized
by original polynomial coordinates.

## 5. Coefficient-field instability and the remaining obligation

Nonlinearity also implies \(\rho''\ne0\).
Indeed the constants of \(\partial_\tau\) in a finite algebraic
extension of \(\mathbb C(\tau)\) are \(\mathbb C\).
One can prove this by differentiating a monic minimal polynomial:
uniqueness makes its coefficients constant when its root is killed.
Thus \(\rho''=0\) would imply
\(\rho=c_1\tau+c_0\), \(c_i\in\mathbb C\), giving the forbidden
linear speed relation \(r-c_1t-c_0s=0\).

It follows from (10) that
\[
N'\bigl(T(\sigma)\bigr)
=\frac{\rho''(y_v)^2}{\beta}\ne0 .
\tag{11}
\]
Since \(\sigma\in L\) and \(N'\) kills \(L\), this proves
\(T(L)\not\subset L\) under the actual hypotheses.
The first coordinate formula \(T(\tau)\in L^*\) therefore does
not justify preservation of the whole coefficient field.

The reduction uses neither polynomial coordinates for
\(\ker N\), nor a unit good-speed ideal, nor a rationality
assumption on \(L\). It does not classify the solutions of
(9)--(10), prove a polynomial inverse for arbitrary formal
solutions, or recognize all conical frames. Those are separate
remaining obligations.

## Sources

1. [Conical three-good speeds lower the selected adjoint degree](conical-three-good-adjoint-degree-pass135.md),
   Sections 2--4. Actual selected-partial degree, its leading LND,
   and exclusion of degree zero for a nonlinear cone.
2. [Nonradial acceleration bounds the degree of a conical speed image](conical-nonradial-degree-bound-pass135.md),
   Section 1. The exact coefficient field, finite separable extension,
   and radial derivation.
3. [Pure-cube leading rigidity after invariant localization](primitive-binary-cubic-localization-rigidity-pass134-working.md),
   Sections 2--3. The fixed-coordinate Taylor chart and the distinction
   between a localized original partial and its locally nilpotent
   leading coefficient. Those ring arguments are repeated here with
   leading degree one instead of two.

[^1]: [Conical selected-partial135](conical-three-good-adjoint-degree-pass135.md), Sections 2--4; [coefficient field135](conical-nonradial-degree-bound-pass135.md), Section 1.
[^2]: [Localized chart134](primitive-binary-cubic-localization-rigidity-pass134-working.md), Sections 2--3.
