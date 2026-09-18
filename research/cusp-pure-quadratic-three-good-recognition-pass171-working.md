# A pure low-degree cusp graph supplies a third actual good coordinate

**Status: complete working argument, pending independent review of this saved artifact.**

In the actual cusp chart159, suppose \(r=k_\rho\ne0\) and the
whole plane relation is a scalar times a fixed-axis graph of degree at
most two. There is then an explicit triangular change of the original
four polynomial coordinates that supplies a third coordinate annihilated
by \(E^2\). The retained supplied-three-good recognition theorem156
therefore recognizes the invariant ring.

No hypothesis on the rho dependence of the graph's constant coefficient
is required. In particular this reduction removes the extra linear-
intercept premise from the pure quadratic recognition statement170.
It does not infer a global coordinate from a projected coordinate:
the new coordinate and its polynomial inverse are written in the
original ring.

## 1. Exact actual hypotheses

Retain the actual hypotheses and chart of
[cusp reductions159](cusp-generic-chart-first-reductions-pass159-working.md),
Sections 1--5. Thus
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX\ne0,\qquad
\ker\bigl(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W
 \mapsto a\eta,b\eta,e\eta^2,d\eta^2\bigr)
   =(\mathsf X\mathsf Z-\mathsf Y^3).
\end{gathered}
\tag{1}
\]
Here \(b=EY\), \(e=E^2Z/2\), \(d=E^2W/2\), and \(\eta\)
is independent over \(A\). The kernel in (1) is the full formal
weighted initial kernel. In particular \(ae=b^3\).

Use the selected derivation \(N=[u^3](\partial_Z|_A)\ne0\),
\(S=\ker_A N\), \(L=\operatorname{Frac}S\), and \(t=b/a\),
\(\rho=d/a^2\). The actual159 chart gives commuting coefficient
partials on the finite separable field \(L/\mathbb C(t,\rho)\)
and
\[
\begin{gathered}
A_L=L[v],\quad Nv=1,\quad L[y,\vartheta]=L[v],
 \qquad B_a=A_a[X],\\
Y=y+tX,\qquad
Z=z+(3t^2y+k)X+t^3X^2,\qquad
W=w+\vartheta X+\rho X^2,\\
z=3ty^2+k_t y+k_\rho\vartheta+n,\\
F:=XZ-Y^3=-y^3+(k_t y+k_\rho\vartheta+n)X+kX^2 ,
\qquad k,n\in L .
\end{gathered}
\tag{2}
\]
All projected entries are in the indicated actual localization.
In particular \(E\) kills \(y,z,w,\vartheta,t,\rho,k,n\).
The equality for \(F\) is literal, not merely a leading-term identity.

For independent formal variables \(U,V\), write
\(H_j(c;U,V)=\sum_{i=0}^j
c_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
The exact potential159 is
\[
\begin{gathered}
r=k_\rho\ne0,\qquad
f=U^3+H_2(k)+H_1(n),\qquad A_1=f_V,\\
rw+f(y,\vartheta)=\ell,\qquad
\Phi=A_1(\ell-f)/r+H_3(k)+H_2(n)-\ell_tU-\ell_\rho V,\\
\Phi(y,\vartheta)=m,\qquad
\Phi_4=-U^3(r_tU+r_\rho V)/r,\qquad \ell,m\in L .
\end{gathered}
\tag{3}
\]
Assume the *whole* relation is pure:
\[
\Phi-m=\lambda\{V-P(U)\},\qquad
\lambda\in L^*,\quad P\in L[U],\quad \deg P\le2 .
\tag{4}
\]
A constant polynomial \(P\), including zero, is allowed in this
hypothesis. Its impossibility under the other actual assumptions is
not needed for the coordinate construction.

Equation (4) is stronger than the statement that \(V-P(U)\) is
one selected factor. This note does not obtain (4) from a unit-gradient
identity alone. It neither assumes nor proves that \(L\) is rational.

## 2. Exact constants and the three forced coefficients

The common constants of the two coefficient partials in \(L\) are
exactly \(\mathbb C\). Indeed, let \(c\in L\) be killed by both,
and differentiate its monic minimal polynomial over
\(\mathbb C(t,\rho)\). The resulting polynomial evaluated at \(c\)
has smaller degree, so minimality makes each differentiated
coefficient zero. Applying this to both partials puts every
coefficient in \(\mathbb C\). Thus \(c\) is algebraic over the
algebraically closed field \(\mathbb C\), and belongs to it.

Set \(K=\ker_L\partial_\rho\). Commutation makes it stable under
\(\partial_t\), and its \(\partial_t\)-constants are \(\mathbb C\)
by the preceding argument. In fact \(K/\mathbb C(t)\) is finite:
the same minimal-polynomial argument with just \(\partial_\rho\)
shows algebraicity. Also rho is transcendental over \(K\), since
it has derivative one under a derivation killing \(K\), whereas
a derivation killing the base field kills any separable algebraic
extension. Linear independence over \(\mathbb C(t)\) persists
after adjoining the transcendental rho; the given finite degree
of \(L/\mathbb C(t,\rho)\) then bounds the degree of \(K\).
Only the exact constant field, not rationality of \(K\), is used below.
A prime denotes \(\partial_t\) on \(K\).

Since (4) has degree at most two, the quartic part in (3) vanishes.
Thus \(r_t=r_\rho=0\), and \(r\in\mathbb C^*\).
It follows that \(k=r\rho+k_0\) with \(k_0\in K\).
At this stage \(A_1=n_\rho\), and literal comparison of the
\(V^2\) and \(UV\) coefficients gives
\[
[V^2]\Phi=\tfrac12 n_{\rho\rho}=0,\qquad
[UV]\Phi=n_{t\rho}=0,\qquad
n=s\rho+n_0,\quad s\in\mathbb C,\quad n_0\in K .
\tag{5}
\]
The right side of (4) contains neither of these monomials.
The product \(A_1(\ell-f)/r\) contributes neither: with \(r\)
constant, \(f=U^3+k_0''U^2/2+n_tU+n_\rho V\).
The other terms in (3) give exactly (5).

Now \(A_1=s\). The \(U^3\) coefficient is
\(k_0'''/6-s/r\), so its vanishing gives
\[
k_0'''=6s/r,\qquad
\mathsf b:=s t^3-rk_0,\qquad
\mathsf b'''=0,\qquad
\mathsf b=j t^2+\beta_1t+\beta_0,\quad
j,\beta_1,\beta_0\in\mathbb C .
\tag{6}
\]
For the last assertion, first \(\mathsf b''=2j\in\mathbb C\);
then \((\mathsf b'-2jt)'=0\) and finally
\((\mathsf b-jt^2-\beta_1t)'=0\). This is exact integration
in \(K\), using its proved constants. No unspecified primitives,
extension of the coefficient field, or rationality assumption
enter (6).

The missing \(UV\) coefficient in (4) is important in this direct
argument. Merely knowing \(\deg\Phi\le2\), without controlling its
quadratic mixed coefficient, is not substituted for that premise.

## 3. The actual triangular good-coordinate correction

Define the complex polynomial
\(Q_2(X,Y)=jY^2+\beta_1XY+\beta_0X^2\), and set
\[
\begin{gathered}
V_{\mathrm{new}}
 =r^2W+sZ-r(XZ-Y^3)-Q_2(X,Y)\\
 =r^2W+(s-rX)Z+rY^3-Q_2(X,Y),\\
W=\frac{V_{\mathrm{new}}-(s-rX)Z-rY^3+Q_2(X,Y)}{r^2}.
\end{gathered}
\tag{7}
\]
This is a global polynomial coordinate change holding \(X,Y,Z\)
fixed. Substitution in either direction immediately recovers the
four original or the four new variables. Its only denominator
is the nonzero complex constant \(r^2\). Thus the new coordinate
does not require localization at \(a\), at a base divisor, or
at a coefficient of \(P\).

The chart (2) proves its time degree. The \(X^2\) coefficient of
the first three terms in (7) is
\[
r^2\rho+s t^3-rk
 =s t^3-rk_0=\mathsf b(t)
 =[X^2]Q_2(X,y+tX).
\]
The \(X\) coefficient of those terms is
\[
r^2\vartheta+s(3t^2y+k)
-r(k_ty+r\vartheta+n)
=\mathsf b' y+\mathsf c,\qquad
\mathsf c:=sk_0-rn_0 .
\]
Since \([X]Q_2(X,y+tX)=(2jt+\beta_1)y=\mathsf b'y\),
the complete identity is
\[
V_{\mathrm{new}}
 =h_0+\mathsf c X,\qquad
h_0=r^2w+sz+ry^3-jy^2\in A_a,\qquad
\mathsf c=sk_0-rn_0\in A_a,
\qquad E^2V_{\mathrm{new}}=0 .
\tag{8}
\]
Membership of \(\mathsf c\) in \(A_a\) follows either from (2)
and (5), or by uniqueness of the coefficients of the actual
polynomial \(V_{\mathrm{new}}\in B_a=A_a[X]\).
In this localization \(E=a\partial_X\), with \(Ea=0\), so the
last equality follows directly from the displayed affine form.
Both \(V_{\mathrm{new}}\) and \(E^2V_{\mathrm{new}}\) are in \(B\).
The domain inclusion \(B\hookrightarrow B_a\) therefore proves
the equality in the original ring, not only on an open set.

Consequently the actual coordinate frame
\((X,Y,V_{\mathrm{new}},Z)\) has three slots killed by \(E^2\),
and the last slot still has time degree two. The new slot may
have degree zero or one; neither is excluded or needed.

## 4. Recognition and scope

The retained
[three-good recognition156](three-good-all-degree-recognition-pass156-working.md),
Section 1, assumes exactly an actual polynomial four-frame, a
global slice \(Eu=1\), and three coordinates killed by \(E^2\).
It explicitly includes an invariant slot. All those hypotheses
hold for the frame just constructed. Therefore, under that retained
working theorem and its stated dependencies,
\[
A\simeq\mathbb C^{[3]},\qquad
B=\mathbb C[p_1,p_2,p_3,u]
\quad\text{for polynomial generators }p_1,p_2,p_3\text{ of }A .
\tag{9}
\]
There is no assertion that \(V_{\mathrm{new}}\) itself is invariant
or has constant nonzero speed. In fact (8) gives
\(EV_{\mathrm{new}}=a\mathsf c\), which can be nonconstant.
Recognition follows from the supplied-three-good theorem, not
from treating that speed as a unit.

For completeness, the lower-degree graphs in (4) cannot actually
occur. Since (4) and \(L[y,\vartheta]=L[v]\) imply \(L[y]=L[v]\),
\(y\) is an affine parameter. The constant determinant159, after
putting \(\vartheta=P(y)\), makes
\[
P_t+P_U P_\rho+(s/r)P_U
 +(3U^2+k_0''U+n_0')/r
\]
independent of \(U\). If \(\deg P\le1\), its \(U^2\) coefficient
is \(3/r\ne0\), a contradiction. This observation is separate
from, and unnecessary for, the coordinate construction (7).

The main reduction uses neither a rho-linear intercept for \(P\),
nor a constant-leading-ratio subcase, nor the exact actual
field-return pencil arguments166--170. It applies uniformly to
the pure quadratic whole relation. The separate
[extra-factor exclusion169](cusp-quadratic-extra-factor-exclusion-pass169-working.md)
can be combined with this result when its stated quadratic graph
hypotheses apply; (4) must not silently be assumed for other
selected factors.

Other cusp branches and entry into the cusp profile are not
resolved by this note. It makes no claim of unrestricted
cancellation, historical novelty, human expert certification, or
proof-assistant verification. The proof of the new coordinate
reduction is algebraic; finite controls are not a proof of its
universal statement.

## Sources and dependency boundary

1. [Actual cusp chart159](cusp-generic-chart-first-reductions-pass159-working.md),
   Sections 1--5, supplies the exact actual chart, coefficient field,
   and literal potential (2)--(3). Those stated inputs were freshly
   read for this note; the entire earlier dependency chain was not
   recursively re-audited.
2. [Supplied-three-good recognition156](three-good-all-degree-recognition-pass156-working.md),
   Sections 1--4, is the explicit retained recognition endpoint.
   The present note does not replace its all-profile proof.
3. [Conditional pure quadratic recognition170](cusp-pure-quadratic-linear-intercept-pass170-working.md)
   records the earlier additional intercept premise. The direct
   coordinate correction here does not depend on its coefficient
   integration or pencil argument.
4. [Quadratic extra-factor exclusion169](cusp-quadratic-extra-factor-exclusion-pass169-working.md)
   is a separately scoped predecessor, not an assumption that
   every low-degree selected curve is already the whole potential.

All sources through170 remain unchanged.

