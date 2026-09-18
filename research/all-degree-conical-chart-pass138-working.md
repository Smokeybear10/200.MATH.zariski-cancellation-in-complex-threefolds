# An all-degree actual chart for nonlinear conical speeds

The selected-partial tangent chart extends to every finite last-coordinate
degree. Descending coefficients of the actual Jacobian first make the
entire last coordinate polynomial in the generic line parameter. The
whole-line identity then gives a constant, nonzero derivative of that
parameter, producing one polynomial differential equation.

This note proves the actual-ring premises for a subsequent coefficient
descent. It does not itself assert that the coefficient field is rational,
that its coefficients descend to a smaller polynomial ring, or that every
sliced polynomial fourfold admits the supplied coordinate frame.

## 1. Hypotheses and the selected intrinsic derivation

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
E^2X=E^2Y=E^2Z=0,\qquad s=EX,\quad t=EY,\quad b=EZ,\\
\operatorname{trdeg}_{\mathbb C}\mathbb C(s,t,b)=2,\qquad
\ker\bigl(\mathbb C[S,T,B_0]\longrightarrow A\bigr)=(H),
\end{gathered}
\tag{1}
\]
where the map sends \((S,T,B_0)\) to \((s,t,b)\), and \(H\) is
irreducible homogeneous of degree at least two. The four displayed
generators of \(B\) are actual polynomial coordinates. The global slice
\(u\) is not assumed to be one of them or an ambient coordinate.
There is no bound on the \(E\)-degree of \(W\).

Put \(T=\partial_W\), holding \(X,Y,Z\) fixed. The selected-partial
theorem135 applies without any last-coordinate degree assumption.[^1]
Its degree-zero alternative would give a nonzero constant linear
relation among the speeds, contrary to (1). Hence
\[
T(A)\subset A[u]_{\le1},\qquad T(u)\in A[u]_{\le1},\qquad
N=[u]T|_A\in\operatorname{LND}(A)\setminus\{0\},\qquad
N(s)=N(t)=N(b)=0 .
\tag{2}
\]
Here \([u]\) extracts the coefficient of \(u\). The result includes
the vertical coefficient of \(T\): the actual Laurent leading-LND
argument in135 excludes its possible quadratic term. No claim about
the lower coefficients of \(W\) being fixed by \(N\) is part of (2).

Let \(S_0=\ker_A N\), \(L=\operatorname{Frac}S_0\), and
\(F=\operatorname{Frac}A\). An intrinsic local slice gives
\(F=L(v_0)\), so \(\operatorname{trdeg}_{\mathbb C}L=2\).
The field \(L\) contains the speed field and is finite over it.
Indeed \(F\) is finitely generated because \(A\simeq B/(u)\), and
therefore \(F/\mathbb C(s,t,b)(v_0)\) is finite. Linear independence
over the speed field is preserved on adjoining the transcendental
\(v_0\), giving the asserted finiteness for \(L\).

No speed is zero and no ratio of two speeds is constant, since either
would give a linear homogeneous relation. Set
\[
\tau=t/s,\qquad \rho=b/s,\qquad \xi=s,\qquad
L/\mathbb C(\tau,\xi)\text{ finite and separable},\qquad
\rho\text{ algebraic over }\mathbb C(\tau).
\tag{3}
\]
For the field assertions, \(H(1,\tau,\rho)=0\) and nonconstant
\(\tau\) give transcendence degree one for
\(\mathbb C(\tau,\rho)\). The speed field
\(\mathbb C(s,\tau,\rho)\) has degree two, so \(s\) is transcendental
over \(\mathbb C(\tau)\). This proves (3).

Extend \(\partial_\tau,\partial_\xi\) uniquely through the finite
separable extension \(L/\mathbb C(\tau,\xi)\). The extensions commute,
and \(\rho_\xi=0\). Write \(\rho'=\rho_\tau\) and \(r=\rho''\).
One has \(r\ne0\): the constants of differentiation in an algebraic
function field of one variable over \(\mathbb C\) are \(\mathbb C\),
as follows by differentiating a monic minimal polynomial. Otherwise
\(\rho''=0\) would imply \(\rho=c_1\tau+c_0\), contradicting (1).

## 2. Actual localization and the entire generic line

Localize at the invariant \(s\). The derivation \(E/s\) is an LND
of \(B_s\) with slice \(X\). Its finite Taylor projection at \(X=0\)
gives
\[
\begin{gathered}
B_s=A_s[X],\qquad
A_s=\mathbb C[y,z,w]_{s_0(y,z,w)},\qquad s=s_0(y,z,w),\\
Y=y+\tau X,\qquad Z=z+\rho X,\qquad
W=\mathcal W(X,v)=\sum_{j=0}^{m}w_jX^j,\qquad w_0=w,\quad w_j\in A_s .
\end{gathered}
\tag{4}
\]
Here \(m=\deg_E W\ge0\) is finite, \(w_m\ne0\), and \(y,z,w\)
are the Taylor projections of \(Y,Z,W\).
Explicitly \(w_j\) is the Taylor projection of
\((E/s)^jW\), divided by \(j!\).
There is no assumption that \(N(w_j)=0\).

For completeness, quotienting \(B_s=A_s[X]\) by \(X\) identifies
\(A_s\) with
\(\mathbb C[Y,Z,W]_{s(0,Y,Z,W)}\).
This is nonzero, so
\(s_0(Y,Z,W)=s(0,Y,Z,W)\ne0\).
The identification proves both the algebraic independence of
\(y,z,w\) before localization and the displayed presentation of \(A_s\).
Projecting the invariant \(s\) proves \(s=s_0(y,z,w)\).

The Taylor inverse and (4) are isomorphisms of actual localized
polynomial rings. Their full Jacobian determinants are inverse units.
After pullback to \(\mathbb C[y,z,w]_{s_0}[X]\), such a unit is
independent of \(X\). At \(X=0\), the transformation has identity
diagonal and fixes \(y,z,w\) modulo \(X\), so its determinant is one.
Thus the Jacobian from \((X,y,z,w)\) to \((X,Y,Z,W)\) is exactly one.
This is a consequence of the actual inverse, not an inference from a
Jacobian condition to existence of an inverse.[^2]

Write \(X=b_X+su\), where \(b_X\in A\). Re-expanding (2) in \(X\)
and applying the quotient rule to fractions in \(A_s\) gives
\[
N'=[X]T|_{A_s}=N/s,\qquad
N'\in\operatorname{LND}(A_s)\setminus\{0\},\qquad
A_L=L[v]=L[y,z,w],\qquad N'v=1 .
\tag{5}
\]
The LND assertion uses \(N(s)=0\), so it is invariant localization
and multiplication by an invariant unit. The localized \(T\) is not
being declared locally nilpotent.
To obtain \(v\), choose \(a\in A\) with \(Na=h\ne0\) and
\(Nh=0\), and set \(v=sa/h\).
The intrinsic slice theorem gives \(A_L=L[a/h]=L[v]\).
Also \(s_0=s\in L^*\), so the denominator in (4) disappears on this
generic fiber. It is the entire affine line, not a punctured line.
Extend the coefficient derivatives on \(L\) to fix \(v\).
Then \(N'=\partial_v\), and every \(w_j\) lies in \(L[v]\).

## 3. The speed cofactor forces tangency in every degree

Let \(J(X)\) denote the Jacobian of \((Y,Z,W)\) with respect to
\((\tau,\xi,v)\), holding \(X\) fixed. The actual Jacobian identity
in Section 2 gives \(J(X)=J_0\in L(v)^*\), independent of \(X\).
All subscripts in this section hold \(v\) fixed unless they are \(v\).
The last row of the Jacobian matrix is now arbitrary polynomial
degree in \(X\):
\[
\begin{gathered}
\begin{pmatrix}
y_\tau+X&y_\xi&y_v\\
z_\tau+\rho'X&z_\xi&z_v\\
\mathcal W_\tau&\mathcal W_\xi&\mathcal W_v
\end{pmatrix},\\
T(\xi)=
\frac{y_vz_\tau-y_\tau z_v+X(\rho'y_v-z_v)}{J_0},\qquad
T(v)=
\frac{y_\tau z_\xi-y_\xi z_\tau+X(z_\xi-\rho'y_\xi)}{J_0}.
\end{gathered}
\tag{6}
\]
The cofactors do not involve the last row. Since \(N'\xi=0\),
the \(X\) coefficient of \(T(\xi)\) in (6) gives
\(z_v=\rho'y_v\). Subtracting and using
\(\ker(\partial_v|_{L[v]})=L\) yields
\[
z=\rho'y+k,\qquad k\in L,\qquad
\alpha(\zeta)=r\zeta+k_\tau,\qquad \beta=k_\xi,\qquad
J_0=\beta\ne0 .
\tag{7}
\]
For the last equality, compare the \(X\) coefficient of \(T(v)\)
with \(N'v=1\). It is
\((z_\xi-\rho'y_\xi)/J_0=k_\xi/J_0\).
No acceleration parameter or nonzero derivative of one is needed.
This is the speed-based cofactor argument137, with the arbitrary
last row left intact.[^3]

Subtracting \(\rho'\) times the first row in (6) from its second
row gives \((\alpha(y),\beta,0)\). Put
\(C=\beta y_\tau-\alpha(y)y_\xi\).
The exact determinant identity is
\[
\beta=(C+\beta X)\mathcal W_v+
y_v\{\alpha(y)\mathcal W_\xi-\beta\mathcal W_\tau\}.
\tag{8}
\]
This identity holds before \(y\) is known to be a coordinate on
the generic line and before any division by \(y_v\).

## 4. Descending coefficients before changing the line parameter

The coefficient of \(X^{m+1}\) in (8) is
\(\beta(w_m)_v\). Hence \(w_m\in L\).
For \(1\le j\le m\), the coefficient of \(X^j\) is
\[
\beta(w_{j-1})_v+C(w_j)_v+
y_v\{\alpha(y)(w_j)_\xi-\beta(w_j)_\tau\}=0 .
\tag{9}
\]
The same top argument applies when \(m=0\), and no recurrence is
then required.

We prove by downward induction that
\(w_j=P_j(y)\) for some \(P_j(\zeta)\in L[\zeta]\), with
\(\deg_\zeta P_j\le2(m-j)\).
The assertion holds for \(j=m\).
For the induction step define the coefficient derivation
\[
\mathcal D_\zeta
=\partial_\tau-\frac{\alpha(\zeta)}{\beta}\partial_\xi
\quad\text{on }L[\zeta],\qquad \mathcal D_\zeta\zeta=0 .
\]
Assuming \(w_j=P_j(y)\), the chain rules in (9) are
\[
\begin{gathered}
(w_j)_v=(P_j)_\zeta(y)y_v,\quad
(w_j)_\tau=(P_j)_\tau(y)+(P_j)_\zeta(y)y_\tau,\quad
(w_j)_\xi=(P_j)_\xi(y)+(P_j)_\zeta(y)y_\xi,\\
(w_{j-1})_v=y_v\,(\mathcal D_\zeta P_j)(y).
\end{gathered}
\tag{10}
\]
The terms with \((P_j)_\zeta\) cancel exactly because
\(C=\beta y_\tau-\alpha(y)y_\xi\).
Integrate the polynomial \(\mathcal D_\zeta P_j\) in the formal
variable \(\zeta\), obtaining \(Q(\zeta)\in L[\zeta]\).
Then \(\partial_v(w_{j-1}-Q(y))=0\), so their difference lies in
\(L\). Adding that constant to \(Q\) proves the induction step.
The derivation \(\mathcal D_\zeta\) increases polynomial degree in
\(\zeta\) by at most one, and integration by one more, proving the
degree bound.

In particular this induction does not assume \(y_v\ne0\), does
not divide by it, and does not assume that any lower \(w_j\) is
fixed by \(N'\). Its only integration is of an actual polynomial
in a formal line variable. No antiderivative in a coefficient field
is postulated.

Now (5), (7), and \(w=w_0=P_0(y)\) give
\(L[v]=L[y,z,w]=L[y]\).
The two polynomial-ring inclusions force \(y\) to have degree one
in \(v\); equivalently
\(y=\lambda v+\mu\) for \(\lambda\in L^*\), \(\mu\in L\).
Thus \(y_v=\lambda\in L^*\) is proved only after the induction.

## 5. The normalized polynomial differential equation

The positive-degree coefficients in (8), now using the independent
formal variable \(\zeta\), say
\((P_{j-1})_\zeta=\mathcal D_\zeta P_j\) for \(1\le j\le m\).
The top coefficient gives \((P_m)_\zeta=0\).
The constant coefficient in (8), with the same chain-rule
cancellation, gives
\(-\beta y_v\mathcal D_\zeta P_0=\beta\).
Consequently
\[
\begin{gathered}
\mathscr W(X,\zeta)=\sum_{j=0}^mP_j(\zeta)X^j\in L[X,\zeta],
\qquad
(X\partial_\zeta-\mathcal D_\zeta)\mathscr W=1/y_v\in L^*,\\
\deg_\zeta P_j\le2(m-j),\qquad
\deg_{\mathrm{wt}}\mathscr W\le2m,\qquad
\mathrm{wt}(X)=2,\quad \mathrm{wt}(\zeta)=1 .
\end{gathered}
\tag{11}
\]
The coefficient field has weight zero in this last bound.

Set \(\kappa=k\). Since \(k_\xi=\beta\ne0\),
\((\tau,\kappa)\) is another separating transcendence basis of \(L\).
The new coefficient derivatives are
\[
\begin{gathered}
\partial_\kappa=\beta^{-1}\partial_\xi,\qquad
\partial_\tau^{\rm new}
=\partial_\tau^{\rm old}-\frac{k_\tau}{\beta}\partial_\xi,\qquad
\mathcal D_\zeta=\partial_\tau^{\rm new}-r\zeta\partial_\kappa,\\
(X\partial_\zeta-\partial_\tau+r\zeta\partial_\kappa)
\mathscr W=1/y_v,\qquad
\zeta=Y-\tau X,\quad
\kappa=Z-\rho'Y+(\tau\rho'-\rho)X .
\end{gathered}
\tag{12}
\]
The last line uses the new basis, holds the formal \(\zeta\) fixed,
and reconstructs the original \(W\) by substitution.
It is the asserted all-degree polynomial equation.

For a subsequent coefficient descent, let
\(K=\ker(\partial_\kappa|_L)\).
Differentiating monic minimal polynomials shows that \(K\) is the
relative algebraic closure of \(\mathbb C(\tau)\) in \(L\).
It is finite over \(\mathbb C(\tau)\), is preserved by
\(\partial_\tau\), and contains \(\rho,\rho',r\).
These facts do not imply \(L=K(\kappa)\).
Nor does this note yet assert \(\mathscr W\in K[\kappa,X,\zeta]\);
that is the distinct coefficient-descent obligation.

In particular the actual partial does not preserve the coefficient
field merely because its leading derivation fixes it.
The cofactors give
\(T(\tau)=-y_v\) and \(T(\xi)=\alpha(y)y_v/\beta\).
After the whole-line conclusion,
\(N'(T(\xi))=r(y_v)^2/\beta\ne0\).
Thus \(T(L)\not\subset L\) under these conditional hypotheses.
The chart proof does not use such preservation.

The construction handles \(m=0\) as well as every positive finite
\(m\). It provides no actual example of the hypothesized nonlinear
conical sliced branch. Global recognition or exclusion would still
require the coefficient descent and the applicable exact-field
monic argument; neither an arbitrary frame-entry statement nor
unrestricted cancellation follows from this chart alone.

## Sources

1. [Conical three-good speeds lower the selected adjoint degree](conical-three-good-adjoint-degree-pass135.md),
   Sections 2--4. The selected degree bound has no last-coordinate
   degree hypothesis; the nonlinear conical case has exact degree one.
2. [A tangent-graph reduction for nonradial conical speeds](conical-mismatch-tangent-graph-reduction-pass136.md),
   Section 2. Actual invariant localization, Taylor coordinates,
   and the whole generic affine line. Those arguments are reproduced
   here with arbitrary finite last-coordinate degree.
3. [A speed-based tangent chart for nonlinear conical frames](universal-conical-tangent-reduction-pass137.md),
   Sections 1--4. The speed-based separating field and Cramer
   tangency, generalized here without the quadratic last row.

[^1]: [Selected-partial135](conical-three-good-adjoint-degree-pass135.md), Sections 2--4.
[^2]: [Actual localization136](conical-mismatch-tangent-graph-reduction-pass136.md), Section 2.
[^3]: [Speed-based chart137](universal-conical-tangent-reduction-pass137.md), Sections 1--4.
