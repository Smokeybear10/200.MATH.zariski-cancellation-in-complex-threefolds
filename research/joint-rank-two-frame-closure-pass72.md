# Recognition when the original action and defects have joint rank at most two

Under the actual supplied two-quadratic coordinate frame and an
original polynomial slice, the written proof chain now recognizes
every action whose joint span with its two quadratic defects has
fraction-field dimension at most two. The new moving-quintic
endpoint completes the independent-defect rank-drop cases.

This is not recognition of the entire supplied frame. The
independent moving sectors with original joint rank three remain,
as does the separate universal-frame problem.

## 1. Exact conditional theorem

Let
\[
B=k[Q_1,Q_2,X,Y],\qquad k=\mathbb C,\qquad
E\in\operatorname{LND}_k(B),\qquad Es_*=1,\qquad A=\ker E.
\]
The four displayed generators are actual polynomial coordinates.
Their genuine coordinate partials satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_X=\operatorname{ad}_E^3T_Y=0.
\tag{1}
\]
Put \(V_i=\operatorname{ad}_E^2T_i\) for \(i=X,Y\), and
let \(K=\operatorname{Frac}B\). Then
\[
\boxed{\operatorname{rank}_K(E,V_X,V_Y)\le2
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.}
\tag{2}
\]
This rank is the dimension of a span of rational derivations.
It is not the coordinate rank of a single LND.
No slice for either defect or for an auxiliary symmetry is
included in the conclusion.

Write \(x=(Q_1,Q_2,X,Y)^t\), and let
\[
m=\max\{j:E^jx\ne0\}.
\]
It exists by local nilpotence and is positive because of the
original slice. It is coordinate flow degree, not spatial
degree of a coefficient of \(E\).

## 2. Reduction to independent moving tops of degrees four and five

If \(\operatorname{rank}_K(V_X,V_Y)\le1\), the complete
[dependent-frame theorem](dependent-frame-closure-pass71.md)
recognizes \(A\). Every such dependent pair automatically
has joint rank at most two after adjoining the one action \(E\).
That theorem includes zero defects, a complex constant
relation, all low-flow cases, both higher constant-top cases,
and the completed dependent moving quartic.

Hence suppose \(\operatorname{rank}_K(V_X,V_Y)=2\).
Under (2)'s premise the original joint rank is then exactly two.
The earlier cases are exhausted as follows.

| Independent-defect case | Complete recognition input |
| --- | --- |
| \(m\le3\) | The [supplied-frame cubic theorem](cubic-frame-closure-pass70.md), which includes all lower flow degrees. |
| \(m\ge4\) with nonzero constant highest vector \(E^mx\) | The independent six-dimensional companion gives \(m\le6\); the [higher constant-top theorem](independent-higher-constant-closure-pass68.md) covers \(m=4,5,6\). |
| \(m\ge4\) with nonconstant highest vector | The [full highest-vector theorem](two-quadratic-top-line-pass42.md) forces \(m=4\) or \(5\). These are handled below. |

The companion bounds are all-degree consequences of actual
inverse-flow identities, not numerical cutoffs.
Thus the table leaves no independent low-flow or constant-top
case unexamined.

In its nonconstant-top case, the full highest-vector theorem
first recognizes a zero preceding bad vector by a commuting
actual good partial. Otherwise it proves actual common powers.
Constant coordinate changes within the good and bad pairs give
\[
E^mx=cg^m,\qquad E^{m+1}x=0,\qquad
E^{m-1}(X,Y)=(g^{m-1},0),\qquad c=e_1,
\qquad g\in\ker E\setminus k,
\tag{3}
\]
where \(m\in\{4,5\}\).
These are identities in the original polynomial ring.
No polynomial root or coordinate status of \(g\) is assumed.

## 3. The normalized rank-one bridge

Put \(\delta=E/g\) on \(B_g\), and write
\(W_i=[E,T_i]\). The exact rescaling formula is
\[
\widetilde V_i
=g^{-2}V_i+2g^{-3}(W_i g)E,\qquad
\operatorname{rank}_K(\widetilde V_X,\widetilde V_Y)
=\operatorname{rank}_K(E,V_X,V_Y)-1=1.
\tag{4}
\]
The surviving line is independent of \(\delta\).
The normalized adjoint bounds hold, but the localized
coordinate partials are not presumed LNDs.

The [higher rank-drop bridge](independent-higher-rank-drop-pass72.md)
establishes every rational companion hypothesis directly.
If \(\widetilde V_X=0\), the normalized highest identity
gives \([\delta,T_c]=0\). The original-slice unit argument
then gives \(T_cg=0\) and \([E,T_c]=0\), so the original
commuting-good-partial recognition applies.

Otherwise set \(D=\widetilde V_X\) and
\(\widetilde V_Y=\eta D\). Only rationality and
\([\delta,D]=0,\ \delta\eta=0\) are needed for the subsequent
five-dimensional companion calculations.
No global primitive polynomial factorization of the normalized
defects is used.

For \(m=4\), the bridge transfers both full images of the
[moving-quartic calculation](common-power-moving-quartic-reduction-pass70.md).
Its nonconstant residual-pair alternatives satisfy the
original [rational two-direction theorem](rational-two-direction-recognition-pass69.md).
For its constant terminal pair, the actual original top
identity is
\[
g[E,T_c]=-\frac32V_X.
\tag{5}
\]
Together with the [parabolic form](terminal-quartic-parabolic-form-pass71.md),
this supplies the actual good-partial cancellation required
by the [terminal quartic theorem](terminal-quartic-recognition-pass71.md).
Thus the moving quartic is recognized using the original
action and slice.

## 4. The completed moving-quintic endpoint

For \(m=5\), the bridge likewise transfers the two rational
residual-pair calculations. A nonconstant first pair, a zero
transverse component of the first pair, or a nonconstant second pair is
recognized by rational69 with the original good partial.
Here “zero transverse” is the normalized \(G=0\) alternative;
its differential identity forces the other first-pair
component to be constant.

It remains a constant transverse first pair and a constant
second pair. The [third full-image lemma](quintic-rank-drop-third-image-pass72.md)
proves that an actual surviving good coordinate has
\(\delta^2w=\lambda\in k\), without assuming \(\lambda=0\).
The [explicit clearing calculation](quintic-rank-drop-polynomial-symmetry-pass72.md)
then supplies an actual constant coordinate change and a
rational symmetry with the precise properties
\[
\begin{gathered}
S=\partial_z+\beta\partial_b+\kappa\partial_a,\qquad
[\delta,S]=0,\qquad Sg=S\beta=S\kappa=Sw=0,\\
\delta\beta=\frac13,\qquad
\delta\kappa=\frac{\beta}{2},\qquad
\delta^2w=\lambda\in k,\qquad g^4S(B)\subseteq B,\\
D=\operatorname{ad}_\delta^2\partial_b\ne0,\qquad
[\delta,\partial_a]=-2D,\qquad
\operatorname{ad}_\delta^2\partial_a
=\operatorname{ad}_E^2\partial_a=0.
\end{gathered}
\tag{6}
\]
All four labels in (6) are actual coordinates.
The original derivation and supplied slice have not changed.

These are exactly the hypotheses of the complete
[terminal quintic theorem](terminal-quintic-recognition-pass72.md).
It handles both \(\lambda=0\) and \(\lambda\ne0\).
The established nice three-variable linear-invariant statement
first supplies a relation over \(k(w)\).
Actual polynomial shears reduce the symmetry to two outputs.
In its parallel alternative, the
[fixed-good-base lemma](fixed-good-base-coefficient-pass72.md)
uses the normalized good base partial and its nonzero defect
line; it does not falsely declare the varying output good.
The radial alternative instead forces the original polynomial
action to preserve an actual coordinate plane.

All final recognition steps use the original slice and their
stated actual-coordinate source gates.
Neither a localized polynomial three-ring nor a global slice
for a cleared auxiliary replica is inferred.
The terminal theorem recognizes the last quintic case, completing
the table and proving (2).

## 5. Exact remaining frontier and evidence limits

Together with the earlier dependent-frame, constant-top and
cubic results, (2) leaves only independent moving tops of flow
degrees four and five with
\(\operatorname{rank}_K(E,V_X,V_Y)=3\), after their existing
individual recognition criteria, inside the supplied frame.
It does not recognize those sectors.

Even full recognition of this supplied frame would leave the
separate obligation of obtaining an applicable actual frame
for an arbitrary sliced action on a polynomial four-ring.
No universal frame-height bound, unrestricted complex-threefold
cancellation theorem, or professor confirmation of the working
field and dimension is supplied here.

This note organizes complete written conditional deductions.
The relevant original companion bounds and theorem hypotheses,
the full rank-drop bridge, the clearing identities, and the
complete terminal quintic proof were read before this synthesis.
Independent reviews and finite controls must be recorded
separately. No new test method, full regression, human expert
review, formal proof-assistant certificate, historical novelty
verdict, or shared metadata change is claimed.
Frozen pass71 and earlier files are unchanged.
