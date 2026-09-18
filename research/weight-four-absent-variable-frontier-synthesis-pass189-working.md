# Every supplied absent-variable quartic chart now has affine generic projection

**Status: working exact-field reduction of a restricted configuration.
Original-ring recognition and unrestricted cancellation remain open.**

The new arguments187--189 reduce both coefficient branches of the
full initial relation \(X^2Z-Y^4\) to explicit polynomial graphs over
the exact coefficient field. Constant projection is impossible.
This is a reduction of the remaining problem, not a solution of it.

## 1. The hypothesis that must not be dropped

Assume an actual polynomial frame and globally sliced action
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad
\deg_E(X,Y,Z,W)=(1,1,2,2),
\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf Y^4).
\tag{1}
\]
The last assertion is the full weighted initial kernel, not a single
vanishing equation. The retained
[universal chart184](weight-four-universal-chart-potentials-pass184-working.md)
supplies the actual selected LND \(N=[u^3](\partial_Z|_A)\), and
\[
\begin{gathered}
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\quad
a=EX\in L^*,\\
t=EY/a,\quad \rho=(E^2W/2)/a^2,\quad q=(E^2Z/2)/a^2=t^4,\quad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+(4t^3y+k)X+t^4X^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\qquad
\det\frac{\partial(y,z,w)}{\partial(t,\rho,v)}=-a^3 .
\end{gathered}
\tag{2}
\]
Use the commuting coefficient partials on \(L\), and set
\(K=\ker_L\partial_\rho\) and \(R=k_\rho\).
Then \(K/\mathbb C(t)\) is finite, with \(t\)-constant field
\(\mathbb C\). It is not assumed rational.

## 2. Exhaustive current conclusion

Under (1)--(2), both branches below have
\[
L[y]=L[v],\qquad y=\gamma v+\eta,\quad
\gamma=Ny\in L^*,\quad\eta\in L.
\tag{3}
\]
All coordinates and equalities in the next paragraphs, except where
explicitly stated otherwise, are over these exact fields.

If \(R=0\), the
[zero-R reduction187](weight-four-absent-variable-zero-r-reduction-pass187-working.md)
first excludes constant \(y\), proves \(n_\rho\ne0\), and obtains
\[
z=6t^2y^2+k'y+n,\qquad
\vartheta=P(y),\quad \deg P=3,\qquad
w=\mathcal W(y),\quad \deg\mathcal W\le6 .
\]
Its calibrated identities retain the factor \(\gamma=Ny\).
The [cover-collapse proof189](weight-four-absent-zero-r-cover-collapse-pass189-working.md)
then gives the stronger necessary conditions
\[
L=K(n),\qquad \rho=b n+c,\qquad
b\in\mathbb C^*,\quad c\in K,\qquad n_\rho=1/b .
\tag{4}
\]
The proof rules out genuine quadratic covers and nonconstant linear
slopes using the actual function-field return and pole degrees.
Euler differential equations alone would allow those formal covers.
Equation (4) does not assert that \(K=\mathbb C(t)\), nor that a
field coordinate is an original polynomial coordinate.

If \(R\ne0\), the
[constant-projection exclusion188](weight-four-absent-variable-constant-projection-exclusion-pass188-working.md)
uses an actual commuting LND, justified primitive division, an
actual polynomial three-ring kernel, and Wang's two-coordinate
classification. It excludes constant \(y\), including the case
where the auxiliary affine coefficients generate the unit ideal.
The separate [rigidity188](weight-four-absent-variable-nonzero-r-rigidity-pass188-working.md)
then forces \(R_\rho=0\).
The [quartic-graph reduction189](weight-four-absent-nonzero-r-quartic-graph-reduction-pass189-working.md)
excludes the degree-drop case and both quadratic-projection
possibilities. Its conclusion is
\[
\vartheta=P(y),\quad \deg P=4,\qquad
R=\frac1{A_1t+B_1},\quad
k=R\rho+k_0,\quad n=C_1R^2\rho+n_0,
\quad A_1,B_1,C_1\in\mathbb C,\quad k_0,n_0\in K .
\tag{5}
\]
Here \((A_1,B_1)\ne(0,0)\), while \(A_1=0\) and \(C_1=0\)
are allowed. The notation \(A_1\) is a complex scalar, not
the invariant ring \(A\).

The decisive algebraic-function lemma in that argument is that every
nonzero algebraic solution of
\[
(f+4tf')f'''-3f'f''-3t(f'')^2=0
\]
is affine in \(t\). The proof analyzes the first nonzero term of
a finite-ramification Laurent expansion at infinity, including
all tails after a constant or linear leading term. It is not
a check of power-law solutions alone.

## 3. Separate actual example and verification boundaries

The [actual-frame example187](weight-four-common-factor-actual-frame-pass187-working.md)
belongs to the different relation \(X^2Z+XYW-Y^4\), recognized
in186. It supplies an explicit polynomial automorphism, both inverse
orders, the literal selected original partial and the full initial
kernel. It validates that configuration's surviving branch.
It is not an example of the absent-variable relation in (1), and
its time profile is not claimed minimal over all frames.

The proof sources have separate saved-source AI reconstructions.
Their finite symbolic controls check polynomial identities and
negative formal boundaries. They do not prove the field-return
assumptions, published classification, curve-degree statements,
or universal algebraic-function lemma by numerical sampling.
The grouped verification record records the canonical executions
separately from those written arguments.

## 4. The remaining task, without redefining success

For the zero-R branch, solve the remaining scalar coefficient equations
after (4), then determine whether the exact field return forces a
polynomial invariant coordinate in the original four-ring.
For the nonzero-R branch, analyze the remaining potentials and scalar
determinant after (5), including reciprocal coefficients with poles.
No localization denominator may be treated as an original-ring unit.

Even recognition of every chart satisfying (1) would not solve
unrestricted cancellation. The split one-dimensional coefficient form,
positive quadratic bad-variable rank, height-two initial kernels,
higher possible minimum time profiles and arbitrary coordinate entry
remain separate obligations. The working interpretation of the
professor's email as complex-threefold cancellation is unconfirmed.

The full goal stays active. No expert review, historical novelty
clearance, proof-assistant verification, submission, public posting,
external contact or new automation is asserted or authorized here.
No186 or earlier frozen source has been changed.
