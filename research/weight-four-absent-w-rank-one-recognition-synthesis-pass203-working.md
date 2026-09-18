# Complete recognition of the absent-W rank-one weight-four boundary

Status: restricted working theorem. The two-root full initial kernel is
recognized by composing the completed necessary classification, actual
normalizations and branch proofs. Together with the previous square-root
case and squarefree obstruction, this treats the entire absent-\(W\),
rank-one boundary under the stated supplied actual hypotheses.
The general cancellation problem remains unsolved.

## 1. Exact theorem and the meaning of the initial kernel

Let
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,
\qquad (\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2).
\tag{1}
\]
The entries are actual polynomial coordinates. Define
\(a=EX,\ b=EY,\ e=E^2Z/2,\ h=E^2W/2\), and the weighted initial map
\[
\theta_0:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
\longrightarrow A[\tau],\qquad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\tau,b\tau,e\tau^2,h\tau^2).
\tag{2}
\]
Here \(\tau\) is independent, with source weights \((1,1,2,2)\).

**Theorem.** If the entire kernel of (2) is
\[
\ker\theta_0=
(\mathsf Z^2-\mathsf X^2\mathsf Y(\mathsf X-\mathsf Y)),
\tag{3}
\]
then \(A\simeq\mathbb C^{[3]}\).

**Corollary.** The same conclusion holds if, after the actual homogeneous
normalizations in [classification184](weight-four-positive-bad-rank-normal-forms-pass184-working.md),
the entire kernel has the form
\[
\ker\theta_0=(\mathsf Z^2-P_4(\mathsf X,\mathsf Y))
\tag{4}
\]
for a binary quartic \(P_4\). In this situation (4) is irreducible because
it is the full height-one prime kernel. Thus square or zero \(P_4\)
cannot occur. The corollary does not include rank-one forms with a
nonzero coefficient of \(\mathsf W\), or rank-two product forms.

Neither statement follows from one leading relation alone. There is
no theorem here putting an arbitrary sliced four-ring into (1) or (4).

## 2. Exhaustion of the two-root case

The [actual chart184](weight-four-universal-chart-potentials-pass184-working.md)
gives the selected nonzero locally nilpotent derivation
\(N=[u^3](\partial_Z|_A)\), its coefficient field
\(L=\operatorname{Frac}(\ker_A N)\), and a full generic line \(A_L=L[v]\).
The quantities
\[
t=b/a,\qquad q=e/a^2,\qquad \rho=h/a^2,\qquad q^2=t(1-t)
\tag{5}
\]
belong to \(L\), with \(t,\rho\) algebraically independent.
The coefficient partials extend to \(L\). Their exact field
\(K=\ker_L\partial_\rho\) is finite over \(\mathbb C(t,q)\).
It is not assumed equal to that rational conic field.

The first potential is \(k\), with \(R=k_\rho\). If \(R=0\), the
[zero-R proof196](weight-four-two-root-zero-r-coordinate-recognition-pass196-working.md)
constructs an original invariant coordinate and recognizes \(A\).
That written result applies directly to (1),(3),(5), without a
nonzero-R or rational-\(K\) assumption.

If \(R\ne0\), the
[nonzero-R reduction195](weight-four-double-cover-nonzero-r-reduction-pass195-working.md)
excludes constant projection and the other degenerate alternatives.
It gives the nondegenerate necessary square equations for \(f=1/R\).
The [complete classification201](weight-four-two-root-two-gate-classification-pass201-working.md)
then leaves exactly
\[
f=cq,\qquad f=cq/t,\qquad f=cq/(t-1),\qquad c\in\mathbb C^*.
\tag{6}
\]
Its finite-field argument uses differential constants, a residue
obstruction and exact resultants; it is not a rational ansatz.

For the first family, the
[actual monomial normalization202](weight-four-two-root-monomial-actual-normalization-pass202-working.md)
removes all lower modes by polynomial coordinate changes with
polynomial inverses. The
[new monomial branch proof203](weight-four-two-root-monomial-coordinate-recognition-pass203-working.md)
excludes the graph by normality and irreducibility in the original ring.
For its other alternative, scalarity forces
\(g=\alpha t+\beta q+\gamma\), with \(\beta\ne0\), and gives an actual
invariant coordinate by the inverse displayed below. Hence \(A\)
is a polynomial three-ring.

For the other two families, the
[actual reciprocal-pair normalization202](weight-four-two-root-reciprocal-actual-normalization-pass202-working.md)
preserves every actual gate and puts both into one normal form.
The [new field-obstruction proof203](weight-four-two-root-reciprocal-field-obstruction-pass203-working.md)
excludes its graph by degree two and its quadratic projection by degree
three in the exact projected field. The proof includes zero offsets
and arbitrary allowed finite \(K\).

The cases \(R=0\) and \(R\ne0\), all three possibilities (6), and both
remaining square alternatives are exhausted. This proves the theorem.

## 3. The actual coordinate step, not only a fraction-field change

In the monomial projection branch, the normalized original coordinates
admit constants \(\alpha,\beta,\gamma,\delta\in\mathbb C\), with
\(\beta\ne0\). Set
\[
\begin{gathered}
I=Z^2-X^2Y(X-Y)-2X(W-\gamma),\qquad
J=(2\delta-I-2\alpha Y)/(2\beta),\\
z_*=Z-XJ,\qquad
G_*=W-\gamma-ZJ+XJ^2/2-XY(Y-X)/2 .
\end{gathered}
\tag{7}
\]
These are polynomials, since their denominators are nonzero complex
constants. For independent \(X,Y,z_*,G_*\), the inverse is
\[
\begin{gathered}
J_*=(2\delta-z_*^2+2XG_*-2\alpha Y)/(2\beta),\\
Z=z_*+XJ_*,\qquad
W=G_*+\gamma+XY(Y-X)/2+z_*J_*+XJ_*^2/2 .
\end{gathered}
\tag{8}
\]
Both compositions are identities in independent polynomial variables.
The scalar and literal chart equations prove \(EG_*=0\).
Consequently \(B=\mathbb C[X,Y,z_*,G_*]\) with an invariant ambient
coordinate, not merely a rational invariant.

The slice identity \(Eu=1\) makes \(A\simeq B/(u)\) regular: the
partial derivatives of \(u\) generate the unit ideal. The precise
[Bhatwadekar--Gupta--Lokhande Theorem3.5](https://arxiv.org/html/1501.01438v1)
now applies to the nonzero \(\mathbb C[G_*]\)-linear locally nilpotent
derivation \(E\). It gives \(A=\mathbb C[G_*]^{[2]}\).
This published theorem is used only after (7)--(8) provide its
invariant-coordinate hypothesis.

## 4. Why the full absent-W boundary follows

The homogeneous normalizations184 are actual polynomial automorphisms.
Their coordinate weights are one or two, less than the initial
generator's weight four, so fullness of the initial kernel prevents a
time-degree drop. They preserve the supplied exact profile and transport
the entire initial ideal.

For (4), the nonsquare binary quartic has root multiplicities
\(3+1,\ 2+1+1,\) or \(1+1+1+1\). The first two types normalize respectively
to \(X^3Y\) and \(X^2Y(X-Y)\). The first is recognized by
[synthesis200](weight-four-square-root-complete-recognition-synthesis-pass200-working.md);
the second is the theorem just proved.

The squarefree type is impossible by the
[double-cover obstruction184](weight-four-squarefree-double-cover-exclusion-pass184-working.md).
It restricts the actual nonconstant ratio \(t=b/a\) to a suitable affine
line in the ambient polynomial space. The equation \(q^2=P_4(1,t)\)
would then give a nonzero rational differential \(dt/q\) on
\(\mathbb P^1\) with no pole, which is impossible.
This argument uses actual rational functions, not an assumption that
the invariant surface is rational. These alternatives prove the corollary.

## 5. Verification boundary and the remaining full goal

The two new203 proofs have complete written derivations, including exact
finite-field integration, actual field-return gates and every relevant
constant case. The normalization202 checker passed six finite methods
in one canonical run. Its controls are separate from the203 inverse
and field-obstruction checker. Passing finite algebra identities is
not proof-assistant certification of either whole proof.

Root freshly read both203 branch sources, both202 normalization sources,
classification184 and the squarefree exclusion184. The older zero-R196,
reduction195 and synthesis200 are explicit retained dependencies, not
newly counted checks or a claim of a fresh recursive review of every
historical source. Saved-source AI cross-reviews and exact run records
belong in verification203.

The unrestricted target remains open here. Other positive bad-quadratic
rank forms, height-two initial kernels, higher time profiles and arbitrary
coordinate entry are not covered. In particular no argument says that
every slice derivation of a polynomial four-ring has this low-degree
profile or this leading kernel.

These are private, AI-reviewed working proofs. Human expert review,
formal verification and novelty clearance have not occurred. No public
claim, submission or external contact is authorized or made.

