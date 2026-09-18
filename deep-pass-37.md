# The rank-two candidate family has polynomial quotients

The full complex threefold cancellation conjecture is still unsolved.
This pass finishes the selected published-candidate investigation: the
80 indexed threefold factors in Tao Su's six-puncture rank-two example
are ordinary affine three-spaces, by the source-dependent working proof
below. The proof has separate AI reconstructions and exact algebraic
controls. It has not received human expert review or Lean verification,
and no novelty or priority claim is made. The literature audit found
an explicit antecedent: Mellit already states rank-two cancellation
compatible with his stratification. This pass is an explicit
reconstruction and identification of Su's indexed factors, not a new
rank-two cancellation theorem.

This is a negative result for a proposed source of counterexamples,
not a proof of the original conjecture. The professor has not confirmed
the dimensional correction or complex-field interpretation of his email.
The working target remains

\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]

## 1. What is actually resolved

Work over an algebraically closed field of characteristic zero, within
Su's very generic character-variety setup. For every nonempty rank-two
braid cell, its affine prequotient has a polynomial coordinate translated
by the actual additive action. Its quotient is therefore polynomial.
In particular,

\[
\mathcal A_j\simeq\mathbb A^3,
\qquad 1\le j\le80,
\tag{2}
\]

for the indices in Remark 2.12 with
\((g,k,n,\boldsymbol\mu)=(0,6,2,((1,1)^6))\).
These are 80 indices, not 80 asserted isomorphism classes.

The [2026 journal paper](https://bimsa.net/doc/publication/5764.pdf)
still presents these as potential cancellation counterexamples on page
50. It does not prove their nonpolynomiality. Both this version and
[arXiv v4](https://arxiv.org/pdf/2307.16657v4) were inspected directly.
The journal version adds a useful rank-two worked example supporting
the calculation, but the all-80 conclusion here is our deduction from
its construction, not a theorem attributed to the author.[^1]

## 2. The short geometric proof

First distinguish an arbitrary slice from a coordinate slice. Suppose
an additive algebraic action on
\(Y=\operatorname{Spec}k[q,z_2,\ldots,z_N]\) satisfies
\(q(t\cdot y)=q(y)-t\), where \(q\) is one of the displayed
polynomial coordinates. Then the hyperplane \(H=\{q=0\}\) is
\(\mathbb A^{N-1}\), and the maps

\[
\begin{aligned}
\Phi:\mathbb A^1\times H&\longrightarrow Y,
& (a,h)&\longmapsto(-a)\cdot h,\\
\Psi:Y&\longrightarrow\mathbb A^1\times H,
& y&\longmapsto\bigl(q(y),q(y)\cdot y\bigr)
\end{aligned}
\tag{3}
\]

are regular inverses. Their compositions follow directly from the
action law. Consequently the geometric quotient is \(H\).
Without the coordinate hypothesis, identifying the zero fiber as
affine space would be the missing step, not a justified conclusion.

For Su's braid matrices in rank two, put

\[
H(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},
\qquad B(e)=\begin{pmatrix}0&1\\1&e\end{pmatrix}.
\quad B(e_1)H(-t)=B(e_1-t).
\tag{4}
\]

The paper defines its Borel action by pushing the inverse group element
through the chronological first crossing. Equation (4) immediately
absorbs the whole rank-two unipotent element. There is no residual
factor. Thus only the first raw braid coordinate changes, by \(-t\).
This is also an identity of the prescribed diagrams, not an inference
of uniqueness from a long matrix product.

Every nonempty walk starts with an up step. Appendix A starts its
coordinate recursion at the identity matrix, so the first normalized
up coordinate is exactly \(e'_1=e_1\). It is an actual affine
coordinate, not merely a polynomial with derivative one.

The remaining identification matters. Lemma 2.5(a) makes the projection
from the character-variety prequotient to the braid variety equivariant.
Proposition 2.9 gives its actual variety coordinates as a torus times
the up-coordinate affine space times additional unipotent affine
factors. The additive subgroup fixes the torus coordinates. On a fixed
torus fiber we therefore have

\[
Y\simeq\mathbb A^{|U_p|+n_{\mathbf w}},
\qquad e'_1(t\cdot y)=e'_1(y)-t.
\tag{5}
\]

Theorem 2.10 defines its affine factor as precisely this fiber's
geometric quotient. Applying (3) proves that factor is
\(\mathbb A^{|U_p|+n_{\mathbf w}-1}\).
The extra variables need not be fixed by the action. Their actual
motion is handled by (3), which is why the argument includes cells
having identity Bruhat indices.[^2]

The empty braid causes no exception: its positive-word length formula
forces all handle and puncture Weyl indices to be identities. With no
stays, its admissibility subgroup is trivial, hence not transitive in
rank two. Such a cell does not occur in the admissible decomposition.

## 3. A completely explicit selected threefold

Take five nontrivial puncture Bruhat indices and the chronological walk
\((1,s,s,s,1,s,1,s,1,s,1)\) of \(\sigma_1^{10}\).
Write its normalized up coordinates as \(a,b,c,d\), and its two
nonzero stay coordinates as \(r,z\). Set \(q=-z/r\). The raw
coordinates are

\[
\begin{aligned}
(e_1,\ldots,e_{10})={}&
\left(a,r,\frac{q-1}{r},-\frac rq,
q^2(b-a)-\frac{q(q-1)}r,0,\right.\\
&\left. q^2(c-b),0,q^2(d-c),0\right).
\end{aligned}
\tag{6}
\]

These formulas are regular on the specified torus-times-affine cell.
Both inverse coordinate maps and every prefix matrix are given in the
[selected-cell proof](research/su-selected-cell-pass37.md).
Direct multiplication gives

\[
B(e_{10})\cdots B(e_1)
=\operatorname{diag}(q,q^{-1})H(d).
\tag{7}
\]

The original monodromies are not replaced by arbitrary constants.
If \(C_i=\operatorname{diag}(c_{i,1},c_{i,2})\), the source's
fixed diagonal is \(D^0=(\prod_{i=1}^5 C_i^s)C_6
=\operatorname{diag}(\kappa,\kappa^{-1})\), where
\(\kappa=c_{6,1}\prod_{i=1}^5c_{i,2}\).
Its defining equation imposes \(q=\kappa^{-1}\), and eliminates
the remaining upper-unipotent factor as \(u^0=H(-d)\).
Choose the torus section \(r=1\).

On its four-dimensional affine fiber the actual action and quotient are

\[
\begin{aligned}
t\cdot(a,b,c,d)&=(a-t,b-t,c-t,d-t),\\
(X,Y,Z,\tau)&=(b-a,c-a,d-a,-a),\\
(a,b,c,d)&=(-\tau,X-\tau,Y-\tau,Z-\tau).
\end{aligned}
\tag{8}
\]

Thus the invariant ring is exactly \(k[X,Y,Z]\), not just a
subring of it. For the whole projective-Borel quotient before fixing
\(r\), the three global coordinates are
\(r(b-a),r(c-a),r(d-a)\). The residual torus scales
\((r,a,b,c,d)\) with weights \((-1,1,1,1,1)\), which verifies
these full-quotient coordinates directly.

## 4. Why this covers all 80 indices

Let \(r_0\) be the number of nontrivial Bruhat indices among the
five puncture choices. A threefold factor has two stays, so

\[
2\le r_0\le5,\qquad |U_p|=r_0-1,\qquad
n_{\mathbf w}=5-r_0,\qquad |U_p|+n_{\mathbf w}=4.
\tag{9}
\]

Every one has the coordinate slice in (5). The number of such walks
for a fixed tuple is \(\binom{r_0}{2}\): distribute the two stays
among its \(r_0-1\) up/down excursions. Therefore the number of
indices is

\[
\sum_{r_0=2}^{5}\binom5{r_0}\binom{r_0}{2}
=10+30+30+10=80.
\tag{10}
\]

The [full geometric proof](research/su-geometry-audit-pass37.md)
includes the extra-factor and empty-word checks. No brute-force grid
is being substituted for those universal statements.

## 5. Evidence, priority and the next gap

The independent checker imports only SymPy and unittest. Its eight
methods verify all prefix matrices, the prescribed walk, both
raw/normalized coordinate directions, monodromy, the additive and
torus actions, quotient inverses and a concrete generic eigenvalue
choice. The written source-identification proof is separate from those
identities. The current full regression and its exact timing are in
[verification-pass-37.json](verification-pass-37.json).

There is definite prior-work evidence, not merely a failed novelty
search. Mellit's *Toric stratifications of character varieties*,
Section 1.4, page 160, explicitly states compatible cancellation of
the extra affine line in rank two. The statement also appears in
his 2019 arXiv v1. A different stratification's existence would not
alone identify Su's particular factors; Sections 2-4 supply that
source-specific identification. Nevertheless the broader rank-two
cancellation phenomenon must be credited as prior work.[^3]

The journal version of Su's paper is important too: Example A.2, pages 68-71,
already supplies the four-crossing rank-two raw translation and
normalized-coordinate calculation. That elementary calculation must
not be presented as a discovery of this project. The exact
source-specific deduction needs a specialist priority and proof check
before any public claim.
The [literature audit](research/literature-scope-pass37.md) records
the actual search scope and unresolved priority question.[^3]

This candidate family is closed as a counterexample route under the
audited source construction. Do not search these same 80 indices for
nonpolynomiality unless a specific source-identification error is found.
Higher rank is not covered: its unipotent group is larger, and one
translated coordinate does not quotient out the whole group.
The next bounded investigation can test whether successive coordinate
slices survive the remaining higher-rank action. It must use the actual
action and product coordinates, not assume a triangularization.

There are two immediate boundaries on that next task. A simple-root
subgroup need not be normal in the larger unipotent group, so its
quotient does not automatically inherit a quotient-group action.
Also, Su's rank-three stabilization adds three affine coordinates,
not one. It does not itself supply the single-line cylinder in (1).
Any higher-rank calculation must be recorded as a separate recognition
subproblem unless that additional reduction is actually proved.

The general problem in (1) has no corresponding known coordinate-slice
guarantee. Establishing that guarantee for the selected construction
does not establish it for every polynomial cylinder.

The [process and proof audit](research/proof-audits-pass37.md) records
independent reconstructions, source-version changes, exact checks and
limitations. No expert contact, submission, posting, paid access or
new automation has occurred.

[^1]: Tao Su, *Cell decomposition and dual boundary complexes of character varieties*, [Advances in Mathematics 498 (2026), 111043](https://doi.org/10.1016/j.aim.2026.111043), Remark 2.12, page 50. The public [author-hosted institutional PDF](https://bimsa.net/doc/publication/5764.pdf) was downloaded successfully after the web reader timed out. The [arXiv record](https://arxiv.org/abs/2307.16657) identifies v4 and the journal reference.

[^2]: Su, [journal PDF](https://bimsa.net/doc/publication/5764.pdf), Definition 1.15, Lemma 2.5(a), Proposition 2.9, Theorem 2.10 and Appendix A. In arXiv v4 the braid-action definition is numbered 1.14, and the cell proposition 1.16; in the journal they are 1.15 and 1.18. The actual geometric deductions (3)-(5) are reconstructed here.

[^3]: Anton Mellit, [*Toric stratifications of character varieties*](https://link.springer.com/content/pdf/10.1007/s10240-025-00158-0.pdf), Section 1.4, journal page 160; also [arXiv:1905.10685v1](https://arxiv.org/pdf/1905.10685v1), Section 1.4, pages 7-8. Su's journal Example A.2 explicitly refines Mellit's Example 5.26. These are positive prior-work findings, not evidence of project novelty.
