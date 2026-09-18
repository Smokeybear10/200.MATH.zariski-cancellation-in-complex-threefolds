# Proper degree-two flows: bounded primary-source applicability audit, pass 55

## Outcome and deduplication

The checked primary theorems do **not presently supply an applicable recognition
step** from the actual sliced degree-two flow and its supplied
\((1,1,2,2)\) adjoint frame to a polynomial quotient. The strongest relevant
proper-action endpoint requires one invariant **ambient coordinate**. The
relative nice/quasi-nice results require an actual polynomial presentation over
a fixed base. Neither hypothesis follows just by renaming the leading
invariants or passing to the generic quotient.

This is a bounded applicability conclusion, not a proof that no such theorem
exists. It does not certify an open-problem status or mathematical novelty.
The main distinctions were already recorded in
[mixed-time-degree-literature-addendum.md](mixed-time-degree-literature-addendum.md)
and [mixed-flow-literature-pass.md](mixed-flow-literature-pass.md). This note
records a fresh targeted primary-source check, the current quasi-nice source
version, and an additional distinction in the endpoint of an older
proper-action theorem. It introduces no new recognized coefficient family.

## 1. Exact input and distinct degree notions

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4]=A[s_*],\qquad
A=\ker E,\qquad Es_*=1,
\]
where \(E\) is locally nilpotent. In the branch under review,
\[
E^3x_i=0\quad(1\leq i\leq4),\qquad E^2x\ne0,
\tag{1}
\]
and the actual coordinate partials \(T_i=\partial_{x_i}\) satisfy
\[
\operatorname{ad}_E^2T_1=\operatorname{ad}_E^2T_2=0,\qquad
\operatorname{ad}_E^3T_3=\operatorname{ad}_E^3T_4=0.
\tag{2}
\]
The outstanding degree-two branch has independent bad top fields
\(V_i=\operatorname{ad}_E^2T_i\), \(i=3,4\).

The exact flow is
\[
\exp(tE)x=x+tEx+\frac{t^2}{2}E^2x.
\tag{3}
\]
Thus (1) bounds **degree in the group parameter \(t\)**, not ordinary degree in
the four spatial variables. It says neither that the vector \(Ex\) is
spatially quadratic nor that the fixed-time automorphisms have spatial degree
two. No theorem for quadratic polynomial maps or quadratic spatial vector
fields is imported here. The earlier mixed-time-degree addendum already
supplies explicit distinctions, so its coefficient examples are not repeated.

The actual full-frame consequences used here are precisely those proved in
[two-quadratic-degree-two-pass42.md](two-quadratic-degree-two-pass42.md):
\(E^2x_3=E^2x_4=0\), while the leading ambient distribution has rank two.
The latter is a fraction-field rank of fields. It is not the coordinate rank
of \(E\), and it is not a two-variable polynomial coordinate subring in its
kernel. In particular, the two moving bad coordinates are not fixed base
coordinates.

## 2. Properness is available, but the polynomial quotient is not

The slice itself gives properness without another theorem. In the product
\(\operatorname{Spec}A\times\mathbb A^1\), the action graph map has image the
closed locus in the square where the two \(\operatorname{Spec}A\) components
agree. Its inverse on this locus takes the difference of the slice coordinates.
Consequently the graph map is a closed immersion, hence proper. This proves
more than absence of fixed points; no free-to-proper implication is being used.

The distinction between
\[
B=A[s_*]
\quad\hbox{and}\quad
A\simeq\mathbb C^{[3]}
\tag{4}
\]
must remain visible. A theorem that supplies only a slice has already reached
the left-hand side of (4), not the right-hand side. Likewise, every slice has
\(E\)-degree one by definition. A desired low ordinary spatial degree, or low
degree in a separate intrinsic derivation, is an additional requirement.

## 3. Proper-action primary endpoints and their gates

Kaliman's *Proper Ga-actions on C4 preserving a coordinate*, Algebra & Number
Theory **12** (2018), 227–258, Theorem 0.1, concludes polynomial-coordinate
translation for a proper action fixing an ambient coordinate. Theorem 0.2(3)
instead assumes a fibration over a smooth affine curve, a specified polynomial
generic invariant ring, a restriction on maps from every fiber to curves,
normal fibers, and translating fiber actions, in addition to properness and
Cohen–Macaulayness. Its conclusion is a plane bundle quotient. Corollary 0.3
and its proof explain why an actual invariant coordinate on \(\mathbb C^4\)
supplies the required fiber geometry. An arbitrary invariant polynomial does
not establish those hypotheses. The concluding proof uses the fiber
translation assumption before applying the bundle-recognition step.
[Primary article](https://msp.org/ant/2018/12-2/ant-v12-n2-p01-s.pdf).

Dubouloz, Finston, and Jaradat, *Proper triangular Ga-actions on A4 are
translations*, Algebra & Number Theory **8** (2014), 1959–1984, assume a
Zariski-locally trivial affine-three-space bundle with a proper locally
triangulable relative action in their main theorem. It yields an
affine-plane bundle away from codimension two in the base. The Dedekind-base
corollaries, and then the \(\mathbb A^4\) corollary, use a genuine triangular
polynomial presentation. Their reduction over a DVR explicitly starts with
\(a\partial_y+q(y)\partial_z+p(y,z)\partial_u\). A generic polynomial plane
or generic triangularization cannot replace that relative input.
[Primary article, pp. 1962–1964](https://msp.org/ant/2014/8-8/ant-v8-n8-p06-p.pdf).

Deveney and Finston, *Additive group actions with finitely generated
invariants*, Osaka Journal of Mathematics **44** (2007), 91–98,
Theorem 3.1, treats a GICO action on \(\mathbb C^4\) with finitely generated
regular invariant ring and a smooth omitted quotient locus whose irreducible
components are disjoint. Its conclusion is **equivariant triviality**. The
paper's definition on p. 91 identifies that conclusion with existence of a
slice; the proof on pp. 94–95 eliminates the omitted locus. It does not identify
the invariant ring with \(\mathbb C^{[3]}\). Here the slice and surjective
quotient map are already present, so this theorem supplies no new endpoint.
[Primary article](https://ir.library.osaka-u.ac.jp/repo/ouka/all/6947/ojm44_01_04.pdf).

## 4. Nice and quasi-nice theorems do not remove the base hypothesis

Dasgupta and Gupta, *Nice derivations over principal ideal domains*,
arXiv:1701.03635v1 (2017), Corollary 3.8, requires actual coordinates with
\(DX_1=0\) and \(D^2X_i=0\) for all three remaining coordinates. Their
Theorem 4.1 records Wang's two-quasi classification on a **three-variable
polynomial ring over a field**. Proposition 4.4 is relative over a PID and
adds a specific generic classification case. Its proof clears a linear form
and completes a unimodular row over that PID. None is a theorem on a
four-variable ring merely having two coordinates annihilated by \(D^2\).
[Primary preprint, §§3–4](https://arxiv.org/pdf/1701.03635v1).

The current inspected Dasgupta–Lahiri revision is arXiv:2302.13787v6,
24 July 2026. Its PDF title is *On image ideals of nice and quasi-nice
derivations on R[X1,X2]*; some search metadata retains the earlier title.
Definitions 2.2–2.3 make quasi-niceness a statement in an actual polynomial
coordinate system, and strict quasi-niceness requires exclusion of every
better such system. Lemma 2.12 and Theorems 4.1, 5.2, 5.9 are relative to a
fixed base and an actual polynomial **plane** over it. The two bad coordinates
here do give two-quasi-niceness over \(\mathbb C\), but do not make \(B\) a
relative polynomial plane over its common invariant surface. Strictness is
not asserted. The source's slice criterion, Lemma 2.9, is again already
satisfied by \(E\).
[Current primary PDF](https://arxiv.org/pdf/2302.13787v6).

## 5. Exact remaining applicability obligations

One verified sufficient endpoint is to produce an actual invariant ambient
coordinate. Properness then allows the Kaliman theorem in §3. Producing only
an invariant with transcendence degree one, a rational coordinate, a coordinate
after invariant localization, or an intrinsic coordinate in a different ring
does not meet this endpoint.

A different sufficient route would establish every premise of the relative
bundle theorem, including its actual polynomial or locally trivial bundle
structure. The generic rank-two quotient and quadratic generator description
do not alone establish this. No assertion that local quadratic neighborhoods
glue globally is made here.

Finally, even complete recognition of this supplied frame would remain
conditional in the unrestricted cancellation problem: an arbitrary sliced
locally nilpotent derivation has not been shown to admit this frame or a
recognized alternative. The existing
[universal-frame-reduction-audit-pass52.md](universal-frame-reduction-audit-pass52.md)
records that separate gate. General's pass55 quadratic-generator slice
selection task is independent of this source audit.

## 6. Verification and access boundary

This audit directly read the cited proper-action statements, the complete
Deveney–Finston Theorem 3.1 proof and definition of equivariant triviality,
the DFJ main theorem and all three immediate corollaries with their proofs,
and Kaliman's Corollary 0.3 deduction and concluding Theorem 0.2 proof.
It did not reread every intermediate lemma in the two long proper-action
papers. The earlier full source audits remain separate evidence.

The current quasi-nice definitions and exact relative statements were read
directly. The Dasgupta–Gupta relative-coordinate extraction in Theorem 3.6
and Proposition 4.4 was checked directly; Wang's theorem was read as the
explicitly attributed statement in that primary paper, not newly certified
from Wang's original article. No positive application here depends on
discarding a premise of those statements.

Targeted searches combined proper additive actions, four-space, flow/time
degree two, quadratic flows, and two-quasi-nice derivations. Unrelated
spatial-quadratic and birational-flow results were not promoted to evidence.
Two Citeseer PDF openings failed and contribute no theorem or proof claim.
Search-result dates were not treated as publication dates. The finite search
does not establish nonexistence of a theorem.

No new symbolic checker, full regression, or shared metadata update belongs
to this note. No file from pass 54 or earlier was edited.
