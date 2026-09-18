# Recognition of the zero plane-slope quadratic-first branch

Working result: the b=0 alternative of333's complex-quadratic,
\(\ell_s\ne0,\ell_{ss}=0\) plane framework is recognized. The full
scalar determinant forces a useful dichotomy. Either a literal partial
in the actual1123 frame has exact horizontal shift zero, or a further
actual polynomial change supplies three coordinates killed by \(E^2\).

The level \(q_1\) remains an arbitrary element of the exact L until the
scalar identity constrains its s-derivative. No rational coefficient
field, polynomial coefficient descent, or height-two shift-three entry
is assumed. This does not recognize the nonzero-b branch of333.

## 1. Exact actual branch and whole line

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md), and the
complete centered identities of the fully read
[333](principal-paraboloid-one-variable-first-potential-plane-reduction-pass333-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,
\quad a_0=EX\ne0,\quad \deg_E(X,Y,Z,W)=(1,2,2,2),\\
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2),\qquad
N=[u^4]\partial_Z|_A,\quad L=\operatorname{Frac}\ker_A N,\\
[L:\mathbb C(t,s)]<\infty,\quad Nv=1,\quad
K=\operatorname{Frac}A=L(v)=\mathbb C(y,z,w),\\
O=L[v]=L[y,\sigma,\theta],\qquad
J(X)=-a_0^4\in L^* .
\end{gathered}
\tag{1}
\]
The exact coefficient partials commute and fix v, and
\(\mathbb F=\ker_L\partial_s\) is finite over \(\mathbb C(t)\),
with t-derivative constants \(\mathbb C\).
Assume the actual normalized first potentials
\(k=s,n=gt^2\), with \(g\in\mathbb C^*\).

More specifically, consider333's b=0 branch. Its notation becomes
\[
H=-r/g+d(t),\qquad \mathcal L=e(t),\qquad d,e\in\mathbb F,
\qquad r=\ell .
\tag{2}
\]
Here H denotes s as a function of (t,r), not a new actual coordinate.
The exact identities in the old (t,s) coefficient field are
\[
\ell=g(d-s),\qquad \bar h=-ge,\qquad x=y+gt,
\qquad
\theta=-\frac{x^2}{g}-\sigma^2+d'\sigma-e .
\tag{3}
\]
Thus \(\ell_s=-g\ne0\); no vanishing coefficient has been divided
out in deriving this representation from (2).
The full plane primitive from333 specializes to
\[
\frac{d''}{2}\sigma^2+d'x-e'\sigma=q,
\qquad q=q_1\in L,
\qquad O=L[x,\sigma].
\tag{4}
\]
Primes on d and e denote the exact derivative on \(\mathbb F\).
The level q is not presumed to belong to \(\mathbb F\).

The first two potentials and the complete actual map are
\[
\begin{aligned}
y&=x-gt,& z&=-y^2/g+d'\sigma-e,&
w&=g(d-s)-2\sigma x,\\
Y&=y+\sigma X+tX^2,&
Z&=z+(2t\sigma+s)X+t^2X^2,&
W&=w+\theta X+sX^2.
\end{aligned}
\tag{5}
\]
The strong complex-field and whole polynomial returns in (1) remain
actual hypotheses, not conclusions from a formal plane equation.

## 2. The actual transferred frame and the constant-d endpoint

Use the actual polynomial map already established in
[332](principal-paraboloid-quadratic-affine-first-potential-transfer-pass332-working.md):
\[
T=Y^2+XW-X^2Z+gZ,\qquad S=XZ-W,
\qquad \mathcal B=\mathbb C[X,T,Y,S].
\tag{6}
\]
Both inverse orders follow from
\(Z=(T-Y^2+XS)/g\) and \(W=XZ-S\). The only denominator is
the nonzero complex constant g. Substitution of (3),(5) gives
\[
\begin{aligned}
T/g&=dX+d'\sigma-e,\\
S&=t^2X^3+2t\sigma X^2+(\sigma^2+2tx-gt^2)X
          +2\sigma x-gd+gs .
\end{aligned}
\tag{7}
\]
These are complete polynomials in X, not only leading terms.

If \(d'=0\), exact constants give \(d\in\mathbb C\).
The actual coordinate \(T-gdX\) is E-invariant by (7).
The original kernel A is regular because \(A[u]=\mathcal B\),
so the invariant-coordinate endpoint of Bhatwadekar--Gupta--Lokhande
Theorem3.5 recognizes A. No generic-line parameter needs to be selected
in this case. Henceforth put
\[
D=d'\ne0,
\qquad x=\frac{q-D'\sigma^2/2+e'\sigma}{D}.
\tag{8}
\]
Equation(4) and the whole return give \(O=L[\sigma]\).
Thus \(\sigma_v\in L^*\), and it is legitimate to use sigma as an
affine polynomial-line parameter. This is not an ambient coordinate
claim. Coefficient derivatives below hold the new formal line variable
P fixed; on L their restrictions are still the old (t,s) partials.

## 3. Full scalar reconstruction, with q still variable

Write \(x=x(t,s,P)\) using (8) with \(\sigma=P\), and set
\(R_0=P+tX\). For the actual coordinates
\((\widehat T,Y,S)=(T/g,Y,S)\), the complete fixed-X map is
\[
\widehat T=dX+DP-e,\qquad
Y=x+PX+t(X^2-g),\qquad
S=XR_0^2+2xR_0-gt^2X-gd+gs.
\tag{9}
\]
The determinant of the actual row change
\((Y,Z,W)\mapsto(T,Y,S)\), at fixed X, is g.
Dividing its first row by g cancels that factor. Consequently the
calibrated determinant of (9), in (t,s,P), is
\[
\mathscr J=-\frac{a_0^4}{\sigma_v}\in L^*.
\tag{10}
\]
The moving coefficients of the affine change from v to sigma contribute
only the triangular factor \(\sigma_v\). Thus this determinant is
independent of both X and P.

For a direct calculation, the three rows of its derivative matrix are
\[
\begin{pmatrix}
DX+D'P-e'&0&D\\
x_t+X^2-g&x_s&x_P+X\\
2X^2R_0+2x_tR_0+2Xx-2gtX-gD&2x_sR_0+g&2R_0(X+x_P)+2x
\end{pmatrix}.
\tag{11}
\]
All coefficient derivatives of q, d, and e are retained in this matrix.
From (8),
\(x_s=q_s/D\) and \(Dx_P+D'P-e'=0\).
Expanding (11) using just these identities gives
\[
\boxed{\mathscr J
=gD(x_t+x_P^2-g)
 +q_s\bigl(gD-2gP-2xx_P\bigr).}
\tag{12}
\]
The quadratic-X terms cancel directly. The linear-X coefficient before
using the displayed derivative relation is
\(-g(Dx_P+D'P-e')\), so no unused X-coefficient remains hidden.

Every term on the right of (12) has P-degree at most two except possibly
\(-2q_sxx_P\). Its exact cubic coefficient is
\[
[P^3]\mathscr J=-\frac{q_s(D')^2}{D^2}.
\tag{13}
\]
The nonzero scalar calibration (10) therefore forces
\[
\boxed{q_s=0\quad\hbox{or}\quad D'=d''=0.}
\tag{14}
\]
This is a field identity, not a case split by pointwise zeros or poles.
No ODE for D and no rationality of \(\mathbb F\) is needed below.

## 4. The q_s=0 branch has a literal shift-zero partial

Assume \(q_s=0\), so \(q\in\mathbb F\) and \(x_s=0\).
In (11), the first two rows have zero s-entry and the third has
s-entry g. The cofactors for the inverse S-partial are exactly
\[
\bigl(C_{S,t},C_{S,s},C_{S,P}\bigr)
=\bigl(0,\mathscr J/g,0\bigr).
\tag{15}
\]
For example the relevant two-by-two determinant is
\[
(DX+D'P-e')(x_P+X)-D(x_t+X^2-g)
=-D(x_t+x_P^2-g)=-\mathscr J/g.
\]
The cofactor sign gives (15).

Let \(\Delta=\partial_S\) be the literal actual partial in
\(\mathcal B=\mathbb C[X,T,Y,S]\), fixing X,T,Y.
Since (t,s,sigma) is a separating basis of K and (10) is nonzero,
(15) gives
\[
\Delta t=\Delta\sigma=0,\qquad \Delta s=1/g,
\qquad \Delta|_K=g^{-1}\partial_s
\quad\text{with sigma held fixed}.
\tag{16}
\]
Characteristic zero uniquely extends this derivation through the exact
finite coefficient extension. In particular its action on K is
independent of X. Since \(\Delta\mathcal B\subset\mathcal B\),
\[
\Delta A\subset\mathcal B\cap K=A.
\tag{17}
\]
It is nonzero on K by (16), hence nonzero on A. Thus this literal
partial has exact horizontal shift zero in the original slice u.
This verifies the relevant entry directly; it is not an appeal to
the shift-three chart of258.

Here is an elementary commutation argument retaining the whole actual
ring. If any LND \(\Delta\) of \(A[u]\) preserves A, then
\(\exp(z\Delta)\) and its inverse preserve \(A[z]\).
As an automorphism of the one-variable polynomial ring \(A[z][u]\)
over the induced base automorphism, it must send u to
\(b(z)u+c(z)\), with \(b(z)\in A[z]^*\).
The domain property gives \(A[z]^*=A^*\); at z=0 the map is the
identity, so \(b(z)=1\). The linear z-coefficient then shows
\(\Delta u\in A\). It follows on A and u that
\([\Delta,E]=0\). This argument assumes no slice for \(\Delta\).

Apply this to the literal partial above. Its actual kernel
\(R=\mathbb C[X,T,Y]\) is therefore E-stable, and
\(\delta=E|_R\) is nonzero with \(\delta X=a_0\ne0\) and
\(\delta^2X=0\). Divide its three coefficients by their gcd c.
Because \(c\mid a_0\in\ker\delta\), factorial closure gives
\(\delta c=0\). The quotient is an irreducible LND of the actual
three-ring R and retains X as a degree-one coordinate.
[Dasgupta--Gupta, Theorem4.8, restating Daigle](https://arxiv.org/html/1701.03635v1)
supplies an invariant actual coordinate of R, hence of
\(\mathcal B=R[S]\). The original slice gives a regular kernel,
so [Bhatwadekar--Gupta--Lokhande, Theorem3.5](https://arxiv.org/html/1501.01438v1)
recognizes \(A\cong\mathbb C^{[3]}\).
This is the actual three-ring endpoint retained in258 Section2,
with its polynomial and commutation hypotheses proved here.

## 5. The D'=0 branch has an actual three-good reframe

It remains to cover \(D'=0\). Exact constants give
\[
D\in\mathbb C^*,\qquad d=Dt+d_0,\qquad d_0\in\mathbb C.
\tag{18}
\]
There is no restriction on q_s in this case. Define the actual polynomial
\[
V=gD\,Y-XT+gd_0X^2.
\tag{19}
\]
It replaces Y in the coordinate frame (6), with polynomial inverse
\(Y=(V+XT-gd_0X^2)/(gD)\). Both coefficients divided out are
nonzero complex constants.
The complete first row and (7),(18) give the exact identity
\[
V=gD\,y+geX.
\tag{20}
\]
All coefficients in (20) are E-invariant. Thus
\(E^2X=E^2T=E^2V=0\) in the actual polynomial frame
\((X,T,V,S)\). The fully read retained working synthesis
[156](three-good-all-degree-recognition-pass156-working.md)
recognizes this supplied three-good frame, with its stated dependencies.
It requires no full initial-kernel condition or selected-partial shift
for this new frame. If one of these coordinates is invariant, the
invariant-coordinate endpoint also applies directly.

## 6. Conclusion and exact entry boundary

The constant-d case of Section2 and the exhaustive dichotomy (14) prove
\[
\boxed{\text{The full actual branch(1)--(4) is recognized:}
\qquad A\cong\mathbb C^{[3]}.}
\tag{21}
\]
The result is restricted to \(g\in\mathbb C^*\) and the b=0 branch
of333, equivalently the displayed exact identities (2),(3).
It does not cover333's nonzero-b alternative.

For clarity, when \(d'\ne0\), the actual frame (6) indeed has time
profile1123. Its leaders are
\((a_0,ga_0d,a_0^2t,a_0^3t^2)\).
Since d belongs to a finite extension of \(\mathbb C(t)\), the
leader-ratio field \(\mathbb C(t,d)\) has transcendence degree one.
The full initial kernel of this frame has height two, not the principal
height-one kernel of336. That fact alone does not supply the maximal
quadratic partial shift required by258's later chart.
Here the q_s=0 branch has a separately computed literal shift-zero
partial; the other branch has an explicit actual three-good change.

The complete direct sources264,333,332 and156, and258 Section2, were
read. The published three-variable and regular-kernel hypotheses were
freshly checked in the preceding337 work and are applied without a
slice assumption for the restricted derivation. A fresh unsaved
calculation reconstructed (11)--(13), all three cofactor identities
(15), and both inverse orders and the leading cancellation of (19).
No saved checker was executed, imported, compiled, or rerun. No retained
source or canonical index was edited. The proof inherits156's working
recognition dependencies only in Section5; it makes no arbitrary-entry
or unrestricted cancellation claim.
