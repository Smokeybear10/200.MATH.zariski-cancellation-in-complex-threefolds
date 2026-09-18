# Recognition of every supplied exact1122 time frame

The retained working proofs, together with the height-two endpoints
253--256, now recognize every globally sliced complex polynomial
four-ring supplied with an actual coordinate frame of time degrees
\((1,1,2,2)\). No height condition on its entire initial kernel is
an additional hypothesis of this synthesis.

This is a restricted working theorem with explicitly retained proof
dependencies. It does not prove that an arbitrary sliced action
admits such a frame. It is not a solution of unrestricted cancellation,
a recursively checked formal proof, or a historically novel result.

## 1. Statement and the distinction between the two kinds of degree

Let the four displayed generators be actual polynomial coordinates:
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,
\qquad (\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2).
\tag{1}
\]
Here \(\deg_E f\) is the polynomial degree in the global slice
parameter \(u\), equivalently the largest \(j\) with \(E^jf\ne0\).
It is not ordinary degree in the four displayed coordinates.
Neither \(u\) nor an invariant element is assumed to be an ambient
polynomial coordinate.

**Working theorem, subject to the retained inputs below.**
Under (1),
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{2}
\]
Consequently there exist polynomial generators \(p_1,p_2,p_3\) of
\(A\) with \(B=\mathbb C[p_1,p_2,p_3,u]\). The coordinate property
of the given slice is a conclusion, not an entry assumption.

Put
\[
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2.
\]
All four are nonzero elements of \(A\). For an independent
indeterminate \(\tau\), use the entire weighted initial map
\[
\Theta:\mathbb C[\mathsf X,\mathsf Y,\mathsf Z,\mathsf W]
 \longrightarrow A[\tau],\qquad
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \longmapsto(a\tau,b\tau,e\tau^2,h\tau^2),
\qquad I=\ker\Theta.
\tag{3}
\]
The source weights are \(1,1,2,2\). A relation belonging to \(I\)
is not substituted for the full ideal \(I\).

## 2. Exhaustive initial-height reduction

If \(a,b\) are proportional over \(\mathbb C\), a nonzero
constant linear combination of \(X,Y\) is an invariant actual
coordinate. The slice makes \(A\) regular, and the invariant-coordinate
endpoint, Bhatwadekar--Gupta--Lokhande Theorem 3.5, gives (2).
This endpoint is used with its actual polynomial-coordinate hypothesis.

Otherwise \(t=b/a\) is transcendental over \(\mathbb C\).
The two initial forms \(a\tau,b\tau\) are algebraically independent:
a relation would give a homogeneous binary relation among \(a,b\),
and its linear factorization over \(\mathbb C\) would contradict
their nonproportionality.
The actual-partial bound of
[157](two-linear-two-quadratic-initial-bound-pass157-working.md)
gives
\[
2\le\operatorname{trdeg}_{\mathbb C}\operatorname{im}\Theta\le3.
\tag{4}
\]
The upper bound uses a nonzero intrinsic LND of \(A\) fixing
all four leaders. Thus the full prime \(I\) has height one or two.
There is no missing height-zero case, and no height-three case
after the proportional-speed endpoint.

For height one, the complete
[synthesis248](full-height-one-exact1122-recognition-pass248-working.md)
proves (2). It retains the weight bound \(2\le\operatorname{wt}F\le4\)
for the generator of \(I\), the weight-two actual shear, both
cubic normal forms, and all three ranks of the quadratic part
in the two bad variables for weight four.
That proof is about the entire principal kernel, not an arbitrary
equation inside a height-two kernel.

It remains only to establish (2) when \(\operatorname{ht}I=2\).
In that case, with \(q=e/a^2,\rho=h/a^2\), one has
\[
[\mathbb C(t,q,\rho):\mathbb C(t)]<\infty.
\tag{5}
\]
Indeed the initial fraction field is
\(\mathbb C(t,q,\rho)(a\tau)\), of transcendence degree two.

## 3. Height two: an exhaustive split by actual selected shifts

Let \(T_Z=\partial_Z,T_W=\partial_W\) be the literal partials
in the actual frame (1). Their exact all-ring \(E\)-degree
shifts \(k_Z,k_W\), defined in157, satisfy
\[
k_Z,k_W\in\{0,1,2\},\qquad
0\ne N_i=[u^{k_i}]T_i|_A\in\operatorname{LND}(A).
\tag{6}
\]
The height-two bound is157, Section 8.
The [wedge and zero-shift theorem249](height-two-selected-partial-wedge-rank-pass249-working.md)
shows that a zero shift recognizes \(A\). Its proof first
obtains an \(E\)-stable actual polynomial three-ring, then uses
the stated three-variable theorem to construct an invariant
ambient coordinate before applying the regular-kernel endpoint.
No rational invariant is promoted to an ambient coordinate.

The following table covers every remaining selected-shift pair.

| Exact selected shifts | Retained actual-frame resolution |
| --- | --- |
| \(\min(k_Z,k_W)=0\) |249, Section 5. |
| \((1,1)\) | The exact chart253 followed by the pencil endpoint254. |
| \((2,1),(2,2)\) | The shift-two chart250, projection reduction252, reciprocal normalization255 and canonical endpoint256. |
| \((1,2)\) | Interchange the two actual bad coordinates, then use the preceding row with the rebuilt selected chart. |

The interchange in the last row is an invertible constant
polynomial change. It preserves the exact degree tuple and the
height of the full initial kernel. No comparison of selected
coefficient fields before and after an unproved reframe is needed.

### 3.1. The shift-one pair

The complete
[chart253](height-two-shift-one-affine-chart-pass253-working.md)
uses the vanishing top cofactors of both literal partials to
produce an affine first projection and an exact coefficient-field
presentation. Its determinant equations and actual field return
are the hypotheses of
[endpoint254](height-two-shift-one-pencil-recognition-pass254-working.md).

In the only remaining coefficient case,254 gives a finite curve
field \(F/\mathbb C(t)\) and independent parameters \(y,w\) with
\[
\mathbb C(y,z,w)=F(y,w),\qquad
z=mw+Cy^2+Dy+n_0,\qquad m,C,D,n_0\in F.
\tag{7}
\]
The degree-one generic-pencil argument in254 forces all four
coefficients to be affine functions of one curve parameter.
Combined with the determinant derivative identities, it forces
\(q-c\rho\in\mathbb C[t]\) of degree at most two for some
complex \(c\).
The resulting actual shear of \(Z\) has a polynomial inverse
and produces a third coordinate killed by \(E^2\).
The all-last-degree three-good theorem156 gives (2).
Its application is to the actual sheared frame.

The pencil argument uses the field equality in (7), not just
a nonzero formal Jacobian. The index-two formal negative control
in the independent254 algebra suite shows that this distinction
cannot be discarded.

### 3.2. A selected shift two

After the indicated possible interchange, choose \(T_Z\) of
exact shift two. The complete
[chart250](height-two-shift-two-cubic-chart-pass250-working.md)
derives its calibrated determinant, exact local line
\(L[y,z,w]=L[v]\), and actual field return
\(\operatorname{Frac}A=\mathbb C(y,z,w)\).
Here \(L=\operatorname{Frac}\ker_A N_Z\) is its actual invariant
field, not a chosen rational substitute.

The [projection reduction252](height-two-cubic-plane-projection-reduction-pass252-working.md)
is exhaustive. If its quadratic plane coefficient is nonzero,
the square-plus-cubic alternative is incompatible with the whole
polynomial line, and the remaining case gives a genuine three-good
shear. If the first projection is constant, its separate primitive
commuting-derivation argument produces an \(E\)-invariant actual
coordinate. Both branches give (2).

Every branch not already recognized has affine first projection
and a graph of degree at most three. The same source proves that
the coefficient \(m=k_\lambda\) is complex and makes the actual
shear \(Z\mapsto Z-mW\), with its polynomial inverse.
If this lowers the time degree,156 applies. Otherwise the rebuilt
exact1122 chart has \(k_\lambda=0\).

The complete
[reciprocal normalization255](height-two-graph-reciprocal-normalization-pass255-working.md)
then proves the following exhaustive alternative. Either \(q\)
is complex quadratic and an actual three-good shear recognizes
the kernel, or there are actual polynomial coordinate changes
with explicit inverses putting this selected chart into
\[
q=t^3,\qquad k_\lambda=0,\qquad
n=\nu\lambda+n_0,\qquad \nu\in\mathbb C^*,\qquad
y=\Gamma v+\eta,\quad\Gamma\in L^*.
\tag{8}
\]
The nonconstant reciprocal branch uses a constant invertible
change of the two good coordinates. It never divides an ambient
coordinate by a nonconstant polynomial.
The selected partial, its normalized generic-line parameter, and
the full determinant calibration are transported explicitly.

Thus all hypotheses of
[canonical endpoint256](height-two-canonical-cubic-pencil-recognition-pass256-working.md)
hold in the rebuilt frame. That source applies the generic-pencil
argument to the exact original function-field return. It proves
that the required coefficients are complex and exhibits an
invariant actual polynomial coordinate
\[
\mathcal I=\nu W-\mu Z-XZ+Y^3-A_2Y^2-A_1Y
              -c_1XY-c_2X-c_3X^2,\qquad E\mathcal I=0.
\tag{9}
\]
All coefficients displayed in (9) are complex, with \(\nu\ne0\).
Solving (9) for \(W\) is a polynomial inverse; only the complex
unit \(\nu\) is divided out. The regular-kernel theorem therefore
gives (2).
The notation conventions compose by
\(\mu_{\!255}=\nu\mu_{\!256}\); no unproved normalization
\(\nu=1\) is made.

The table and Sections 3.1--3.2 recognize every height-two branch.
Together with Section 2, they prove the restricted working theorem.

## 4. Consequence for a hypothetical unrestricted counterexample

For a globally sliced action on \(\mathbb C^{[4]}\), define the
true coordinate minimum
\[
\mathcal M(E)=
\min_{(r_1,r_2,r_3,r_4)\text{ an actual polynomial coordinate frame}}
 \sum_i\deg_E r_i .
\tag{10}
\]
The minimum exists by well-ordering. It is not a minimum over
elementary shears alone.

Suppose its kernel were not a polynomial three-ring.
No frame could contain an invariant coordinate, by the
regular-kernel endpoint. All four degrees are therefore positive.
No frame could have three degree-one coordinates, by the
[all-last-degree three-good theorem156](three-good-all-degree-recognition-pass156-working.md).
The only remaining positive sorted partition of a sum at most
six is \(1,1,2,2\), now recognized by (2). Consequently,
subject to these retained working proofs,
\[
\boxed{\mathcal M(E)\ge7
 \quad\text{for a hypothetical nonpolynomial globally sliced kernel}.}
\tag{11}
\]
At sum seven, the only unrecognized sorted partitions are
\((1,1,2,3)\) and \((1,2,2,2)\); the other positive partition
\((1,1,1,4)\) has three good coordinates.
This is a boundary for future work, not recognition of either
new profile or evidence that a counterexample exists.

Nothing here supplies an upper bound on \(\mathcal M(E)\),
an algorithm finding a minimizing frame, or descent into the
recognized sector from arbitrary coordinates.
In particular the corrected complex-threefold target
\(A[u]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\)
remains unsolved.
Its field and dimension remain a working interpretation of the
professor's email, not a confirmation from the professor.

## 5. Verification boundary and next obligation

This synthesis composes the complete saved statements156,157,248,
249,250,252,253,254,255 and256. Their individual proof notes
retain further dependencies. The present synthesis does not
recursively recertify every earlier proof or every published theorem.
The new endpoint proofs have separate saved-source AI reviews.
Finite symbolic controls check their stated identities and inverse
maps, not universal function-field or recognition statements.

The external invariant-coordinate endpoint is
[Bhatwadekar--Gupta--Lokhande, Theorem 3.5](https://arxiv.org/html/1501.01438v1).
The curve-pencil proofs state their use of the function-field and
pole-degree theorems with links to the primary Stacks sources.
No conjectural curve parameter is treated as an ambient coordinate.

No numerical test can certify the exhaustive composition or the
arbitrary-entry problem. No saved checker is executed or imported
by this note. Exact hashes, source-review provenance and separate
finite execution results belong in the research ledger.
Earlier proofs and frozen packets are unchanged.

There is no human expert review, Lean or other proof-assistant
certification, historical novelty clearance, public submission
or claim of an unrestricted solution.
The next mathematical obligation is recognition or entry beyond
this time-degree sector, accompanied by a review of the retained
proof chain before any publication claim.
