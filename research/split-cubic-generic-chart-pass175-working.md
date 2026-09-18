# The actual split-cubic chart and its first coefficient potentials

**Status: working actual-chart derivation, with saved-source AI reviews.**

For the full split initial kernel \((XZ+YW)\), the fixed-\(X\)
chart has polynomial coefficient potentials over the exact intrinsic
field. Their derivation never divides by \(k_\rho-y\). It is not
assumed nonzero or a unit on the generic line in this derivation.

The literal polynomial \(XZ+YW\) is not assumed invariant or even
E-affine. The actual examples retained in157--158 rule out both
assumptions in this fixed frame. No split-case recognition is claimed.

## 1. Actual hypotheses and the selected coefficient field

Assume an actual sliced polynomial four-ring:
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad d=E^2W/2,\\
\theta_0:(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\eta,b\eta,e\eta^2,d\eta^2),\qquad
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W).
\end{gathered}
\tag{1}
\]
The formal weights are \((1,1,2,2)\), and \(\eta\) is independent
over \(A\). The ideal is the full initial kernel, not one leading
identity. All four ordinary leading coefficients are nonzero.
In particular \(ae+bd=0\).

The actual exact-shift theorem157 makes both bad-slot partials have
shift three. Select the original \(T=\partial_Z\), fixing \(X,Y,W\).
Its nonzero top \(N=[u^3](T|_A)\) is an LND on \(A\) killing all
four leading coefficients. Put \(S=\ker_A N\), \(L=\operatorname{Frac}S\).
An intrinsic local slice, normalized to \(Nv=1\), gives
\[
A_L=L[v],\quad \operatorname{Frac}A=L(v),\quad
t=b/a,\quad \rho=d/a^2,\quad [L:\mathbb C(t,\rho)]<\infty .
\tag{2}
\]
The ratios are algebraically independent and the extension is
separable. Indeed the initials of \(X,Y,W\) have no relation:
the contraction of (1) to their subring is zero. Their fraction
field is \(\mathbb C(a\eta,t,\rho)\), proving ratio independence.
The local-slice and finite-field mechanisms are those reconstructed
in159, with the same actual-ring hypotheses.

Extend \(\partial_t,\partial_\rho\) uniquely to \(L\), then to
\(L[v]\) by fixing \(v\). They commute with each other and with
\(\partial_v=N\). All coefficient derivatives below use this convention.

## 2. Actual projection and determinant calibration

The finite Taylor projection for \(E/a\) on the actual ring \(B_a\)
gives
\[
\begin{gathered}
B_a=A_a[X],\qquad A_a=\mathbb C[y,z,w]_{a_0},\qquad a=a_0(y,z,w),\\
Y=y+tX,\qquad Z=z+\sigma X-t\rho X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in A_a\subset L[v],\qquad
L[y,z,w]=L[v],\qquad \operatorname{Frac}A=\mathbb C(y,z,w).
\end{gathered}
\tag{3}
\]
The quadratic coefficient of \(Z\) is \(e/a^2=-t\rho\).
The projected entries are algebraically independent over \(\mathbb C\),
and \(a_0\) is a nonzero polynomial. This is the actual single
localization, not an assumption about a formal determinant.

The localized polynomial map and its inverse have inverse Jacobian
units. After pullback their determinant is independent of \(X\),
and evaluation at zero gives one in projected coordinates. Consequently
\[
\begin{aligned}
J(X)&=\det
\begin{pmatrix}
X+y_t&y_\rho&y_v\\
-\rho X^2+\sigma_tX+z_t&-tX^2+\sigma_\rho X+z_\rho&\sigma_vX+z_v\\
\vartheta_tX+w_t&X^2+\vartheta_\rho X+w_\rho&\vartheta_vX+w_v
\end{pmatrix}
=J_0,\\
J_0&=-a^3\in L^* .
\end{aligned}
\tag{4}
\]
The rows are \(Y,Z,W\), columns \(t,\rho,v\), with \(X\) fixed.
For calibration, the cofactor is still
\[
T(v)=-\frac{(X+y_t)(X^2+\vartheta_\rho X+w_\rho)
             -y_\rho(\vartheta_tX+w_t)}{J_0}.
\]
Writing \(X=x_0+au\) gives \([X^3]T(v)=1/a^3\), whereas the
displayed leading coefficient is \(-1/J_0\). This proves the
sign and scalar in (4), without making \(a\) a global unit.

## 3. The two highest coefficients and the literal split polynomial

The degree-four coefficient of (4) is
\([X^4]J=-\sigma_v-t\vartheta_v-\rho y_v\).
Vanishing and integration in \(L[v]\) give \(k\in L\) with
\[
\sigma=-t\vartheta-\rho y+k .
\tag{5}
\]
For the next coefficient put \(K_1=k_t-\vartheta\),
\(R_1=k_\rho-y\), and \(\mathcal D=dz+t\,dw\). All differentials
are total differentials over \(\mathbb C\), with \(X\) fixed.
Equation (5) gives the row identity
\[
dZ+t\,dW+\rho X\,dY
=\mathcal D+X(K_1dt+R_1d\rho).
\tag{6}
\]
These row additions preserve the determinant. Using also
\(dY=dy+Xdt\) and \(dW=dw+Xd\vartheta+X^2d\rho\), its
degree-three coefficient is
\[
[X^3]J=-z_v-tw_v+(k_t-\vartheta)y_v+(k_\rho-y)\vartheta_v.
\]
Thus there is \(n\in L\) satisfying
\[
z+tw=k_t y+k_\rho\vartheta-y\vartheta+n .
\tag{7}
\]
Neither \(y_v\) nor \(\vartheta_v\) was divided out.
The literal original split polynomial is therefore
\[
H:=XZ+YW=yw+(k_t y+k_\rho\vartheta+n)X+kX^2 .
\tag{8}
\]
Its vanishing cubic time coefficient does not force either
remaining positive coefficient to vanish.

## 4. A denominator-free quadratic potential for X-two

For \(c\in L\), define in independent formal \(U,V\)
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\]
Set
\[
\begin{gathered}
r=k_\rho\in L,\qquad f(U,V)=H_2(k;U,V)+H_1(n;U,V),\\
R_1=r-y,\qquad B_1=f_U(y,\vartheta)-w,\qquad
A_1=f_V(y,\vartheta).
\end{gathered}
\tag{9}
\]
Unlike the cusp chart, \(f\) has no added \(U^3\), and \(R_1\)
need not lie in \(L\). Explicitly
\(B_1=k_{tt}y+k_{t\rho}\vartheta+n_t-w\) and
\(A_1=k_{t\rho}y+k_{\rho\rho}\vartheta+n_\rho\).

Differentiate (7), retaining the \(w\,dt\) term of \(d(z+tw)\).
Then \(\mathcal D=K_1dy+R_1d\vartheta+B_1dt+A_1d\rho\).
Subtract \(K_1dY\) from the middle row of (6). The complete rows are
\[
dY=dy+Xdt,\qquad
dZ_{\rm red}=R_1q+B_1dt+A_1d\rho,\qquad
dW=dw+Xq,\qquad q=d\vartheta+Xd\rho .
\tag{10}
\]
Their \(X^2\) wedge coefficient is
\[
dt\wedge d\rho\wedge(R_1dw+B_1dy+A_1d\vartheta).
\]
Its scalar coefficient is the \(v\)-derivative of
\((r-y)w+f(y,\vartheta)\). Hence
\[
(r-y)w+f(y,\vartheta)=\ell,\qquad \ell\in L .
\tag{11}
\]
No division by \(R_1\) was used, including when \(R_1=0\).
If \(R_1\ne0\), solving (11) in a fraction field still does not
make that factor a unit of \(L[v]\).

## 5. A polynomial potential for X-one

Use a third independent formal variable \(S_0\), and define
\[
\begin{gathered}
g_3(U,V)=H_3(k;U,V)+H_2(n;U,V),\\
\Psi(U,V,S_0)=f_V(U,V)S_0+g_3(U,V)-\ell_tU-\ell_\rho V .
\end{gathered}
\tag{12}
\]
This is a polynomial of total degree at most three over \(L\),
not a plane polynomial obtained by dividing by \(r-U\).
The next coefficient identity is
\[
[X]J=\partial_v\Psi(y,\vartheta,w)=0,\qquad
\Psi(y,\vartheta,w)=m,\quad m\in L .
\tag{13}
\]
For a verification valid without inverting \(R_1\), differentiate
(11) totally:
\[
R_1dw=-B_1dy-A_1d\vartheta+L_tdt+L_\rho d\rho,\qquad
L_i=\ell_i-f_i(y,\vartheta)-r_iw\quad(i=t,\rho).
\]
The \(X\) wedge coefficient from (10) is
\[
\begin{aligned}
&R_1dt\wedge d\vartheta\wedge dw+A_1dt\wedge d\rho\wedge dw
 +R_1dy\wedge d\rho\wedge dw\\
&\hspace{12mm}+B_1dy\wedge dt\wedge d\vartheta
 +A_1dy\wedge d\rho\wedge d\vartheta .
\end{aligned}
\]
Substitute \(R_1dw\) only in its first and third terms.
The terms with \(B_1\) and the last \(A_1\)-wedge cancel.
The remaining expression is
\[
dt\wedge d\rho\wedge(-L_tdy-L_\rho d\vartheta+A_1dw).
\]
Since \((g_3)_U=f_t\), \((g_3)_V=f_\rho\), and the formal
partials of \(f_V\) are \(r_t,r_\rho\), this is exactly the
\(v\)-derivative in (13).

The constant coefficient remains the calibrated condition
\[
\left[dy\wedge(R_1d\vartheta+B_1dt+A_1d\rho)\wedge dw
\right]_{dt\wedge d\rho\wedge dv}=-a^3 .
\tag{14}
\]
The two equations (11), (13) and determinant (14) are simultaneous
constraints. They are not proved here to generate the full
evaluation ideal. The whole-line equality in this presentation is
\(L[y,\vartheta,w]=L[v]\): (7) puts \(z\) in the left side,
and (3) then gives equality. Its evaluation kernel in three formal
variables has height two, not a presumed principal plane relation.

## 6. The retained actual split boundaries

Use the actual157 example, not a newly claimed construction:
in \(\mathbb C[u,a_0,b_0,c_0]\), put \(p=c_0+a_0+b_0^2\),
and use the two inverse stages in
[cubic normal forms157, Sections 4--5](two-linear-cubic-normal-forms-pass157-working.md).
There \(X=u\), \(N=-\partial_{a_0}+\partial_{c_0}\), and
\[
L=\mathbb C(b_0,p),\quad t=b_0,\quad\rho=-p,\quad
v=-a_0,\quad y=-v,\quad w=t,\quad\vartheta=1-ty.
\]
The remaining data here are
\[
z=-\rho-y-t^2+ty^2,\qquad k=0,\quad n=-\rho,\quad
\ell=-1,\quad m=-t .
\]
Substitution verifies (5), (7), (11), (13). In particular (8)
is \(H=yt-\rho X\), so \(EH=-\rho=p\ne0\), consistently with
the actual inverse and determinant.

Even \(k=0\) is not universal.
[The retained correction obstruction158, Section 3](split-cubic-invariant-correction-obstruction-pass158-working.md)
already translates this example by \(X_{\rm new}=X+s\),
\(s\in\mathbb C^*\), retaining \(Y,Z,W\).
The full split initial ideal and exact time profile are unchanged.
The new literal split polynomial is \(H+sZ\), with
\(E^2(H+sZ)=2s\,b_0p\ne0\). Since the selected speed is one,
its new coefficient in (8) is
\[
k=s b_0p=-s\,t\rho .
\]
Subtracting the lower-weight term \(sZ\) restores the old affine
polynomial, not an invariant one. This is a chart interpretation
of an existing boundary, not a new example.

## Scope and source boundary

The argument reconstructs the actual split chart, its cofactor
sign, and the first four coefficient equations. It neither reduces
to the cusp relation nor assumes an invariant correction.
The zero of \(r-y\), the height-two formal evaluation ideal,
and integral coordinate reconstruction remain separate questions.

The actual shift and full-kernel facts come from
[the initial bound157](two-linear-two-quadratic-initial-bound-pass157-working.md),
fully read for this derivation. The projection and exact-field
mechanisms were fully reread in
[the actual chart159](cusp-generic-chart-first-reductions-pass159-working.md);
its cusp-specific quadratic coefficient and potentials were not
reused unchanged. The split normal form157 and its translated
boundary158 were fully reread too.

No checker was executed or imported for this note. There is no
split recognition, arbitrary-entry theorem, unrestricted cancellation
claim, historical novelty clearance, human expert review, or
proof-assistant certification. All174 and earlier artifacts are
unchanged.
