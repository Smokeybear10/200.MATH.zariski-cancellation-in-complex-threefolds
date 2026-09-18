# Exact actions on the whole quadratic fiber

The supplied quadratic branch now has exact formulas for both the canonical
Jacobian derivation and the original last-coordinate partial on its collapsed
nonreduced fibers. The formulas remove an apparent arbitrary coefficient from
the canonical action. A global cubic identity then makes the two slice-related
actions commute on the whole fiber when the first normal action is nonzero.
When that first normal action is zero, a quadratic nilpotent correction remains.

These are conditional working results, not a solution to affine-space
cancellation. The original working target remains
\(A[u]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\).
The corrected conclusion, field and dimension have not been confirmed by
Xiangrui Luo. No historical novelty, human review or formal certification is
claimed.

## Hypotheses and the exact object being computed

The [whole-fiber theorem99](quadratic-whole-plane-fiber-pass99.md) applies to
the supplied original frame
\(B=\mathbb C[x_1,x_2,x_3,z]=A[u]\), with \(E=\partial_u\),
\(E^2x_i=0\), and \(E^2z=q\in\mathbb C^*\). In its unresolved nonconical
quadratic sector, the canonical locally nilpotent derivation \(N\) on \(A\)
has kernel \(S=\mathbb C[s_1,s_2]\). At the closed base point under study,
the speed-map normal \(L(\mathfrak m)\) is nonzero, and the fiber is a
collapsed whole double or a collapsed double with a simple companion.

With the specified actual coordinates, not merely abstractly isomorphic
rings, the whole fiber has presentations
\[
\mathcal A=A/\mathfrak mA=D_0[c],\qquad
\mathcal B=B/\mathfrak mB=D_0[c,u]=D_0[\sigma,z],\qquad
D_0=\mathbb C[G]/H(G),
\]
where \(H(G)=G^2\) or \(G^2(G-1)\). Here
\(\sigma=u-h\) is the alternative actual slice and
\(z=c+q\sigma h+q\sigma^2/2\). The original partial \(T=\partial_z\)
preserves the whole fiber ideal. That fact alone does not say it preserves
the subring \(\mathcal A\), much less \(A\) itself.

For a whole double, put \(\epsilon=G\). For the mixed case, put
\(e_1=G^2\), \(e_2=1-G^2\), and \(\epsilon=G-G^2\). The element
\(\epsilon\) is nonzero and square-zero. The exact slice correction is
\(h=\eta+\epsilon\beta(c)\), where \(\eta\) is constant on each reduced
component and \(\beta\in\mathbb C[c]\). Retaining this term is essential:
passing to the reduced fiber erases the remaining obstruction.

## The canonical coefficient has no hidden polynomial dependence

The [eight-equation proof](quadratic-whole-fiber-actions-pass100.md) begins
with the two regular generating sequences for the actual whole fiber ideal:
the base parameters and \((\ell,H(Y))\). Their change-of-generators
determinant is a unit modulo that ideal. The defining Jacobian for \(N\)
therefore contains the factor \(H'(G)\), multiplied by a unit and by the
relative Jacobian of the actual polynomial coordinate change between
\((u,c)\) and \((\sigma,z)\).

That relative Jacobian is also a unit because the coordinate change has a
polynomial inverse over \(D_0\). On each reduced affine-plane factor every
unit is a nonzero complex constant. The difference from these constants is
nilpotent, and multiplication by \(H'(G)\) annihilates the entire nilpotent
correction. Consequently, on the whole fiber,
\[
N=n(G)\partial_c,\qquad
n(G)=\lambda G\quad\hbox{or}\quad
\lambda(G-G^2)+\rho G^2,
\]
with the displayed constants nonzero. In particular \(NG=N^2c=Nh=0\)
on the whole fiber. In the original ring this says only that these three
elements belong to \(\mathfrak mA\). It is not an identity in \(A\).

## The original partial and the remaining nilpotent term

Since \(T\) fixes \(G\) and \(\sigma\), differentiating the exact
coordinate equations gives \(Tu=h_cTc\) and
\((1+q\sigma h_c)Tc=1\). Here \(h_c=\epsilon\beta'(c)\) has square
zero, so the inverse is exact. Thus
\[
T=h_c\partial_u+(1-q\sigma h_c)\partial_c,
\qquad [E,T]=-qh_c\partial_c,
\qquad [N,T]=0.
\]
All these formulas are on \(\mathcal B\). In particular, \(E\) and
\(T\) commute there exactly when \(\beta\) is constant, which is also
exactly when \(T\) preserves \(\mathcal A\). A nonzero nilpotent
coefficient of \(u\) cannot be ignored in this test.

The global identity \(N^3h=0\) supplies the extra restriction. In the
normalized conormal coordinates from99, the leading derivation is
\(D_* =\gamma x\partial_y+\lambda y\partial_c\), with \(\lambda\ne0\),
and \(\gamma\ne0\) exactly when the first normal action is nonzero.
Applying it three times to the actual leading term \(\beta(c)y\) gives
\[
3\gamma^2\lambda\beta' x^2+
6\gamma\lambda^2\beta''xy^2+
\lambda^3\beta'''y^4=0.
\]
The strict weighted filtration prevents higher terms from canceling these
coefficients. Therefore \(\beta\) is constant if \(\gamma\ne0\), and
has degree at most two if \(\gamma=0\).

This does not exclude either type of actual fixed fiber. The distinction is
between an exact quotient commutation result and a still-allowed nilpotent
correction, not between a recognized and an unrecognized threefold.

## A failed shortcut, with an exact countercontrol

Over \(D=\mathbb C[\epsilon]/(\epsilon^2)\), take
\(h=\epsilon c^2\), \(E=\partial_u\), \(N=\lambda\epsilon\partial_c\),
\(\sigma=u-\epsilon c^2\), and \(z=c+qu^2/2\). The coordinate change
has an explicit polynomial inverse. Nevertheless
\([E,T]=-2q\epsilon c\partial_c\ne0\).

Thus polynomial invertibility on the nonreduced fiber, the induced canonical
action and its displayed vanishing identities cannot alone eliminate the
quadratic correction. This example is only a fiber algebra. It does not
provide the required smooth threefold, base map, canonical Jacobian in an
original four-coordinate frame, or an actual lift with zero first normal
action. Testing such lifts is the next mathematical task, rather than
asserting that the quotient example is a global counterexample.

## Verification and independent reconstruction

Geometry wrote the complete joint proof. Jet independently derived the
weighted coefficient bound and then read the complete joint proof through
its end. General independently reconstructed all eight displayed equations,
including the two unit arguments, the agreement of the actual conormal
coefficient with \(\beta\), and the strict filtration step. Root read the
saved proof and checker completely and reread the volume-normal dependency99.
These are separate AI reconstructions, not independent human endorsement.

The [canonical execution record](verification-pass100-working.json) contains
one suite and one test method, with exit code zero, unchanged input hashes,
the complete output, and its hash. The run took 0.474934792 wall seconds and
reported 0.276 unittest seconds. The [checker](quadratic_whole_fiber_checks_pass100.py)
verifies the symbolic cubic coefficients, both specified Artin coefficient
rings, the induced derivation identities, and both polynomial inverse orders
for a quadratic correction. It imports no older checker or solver.

The checker does not prove the geometric hypotheses, the actual conormal
transition, the filtered lifting premise, or recognition. The author's run
and the root check-in run are repetitions of this same method, not extra
coverage. The historical full75 result remains 146 suites and 1047 methods;
it was not rerun. The central claim registry remains at 544 entries and does
not absorb these conditional working notes by implication.

Reproduction:

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_whole_fiber_checks_pass100
~~~

## Relation to the global problem and sources

Even complete recognition in this supplied frame would require a separate
reduction from an arbitrary sliced derivation on \(\mathbb C^{[4]}\).
The current work has not supplied that reduction. A renewed comparison with
Cid's linearization criterion did not supply it either: the criterion relates
linearization to conjugacy with a coordinate partial, rather than proving
that conjugacy for every candidate.[^cid]

The fresh search was a bounded dependency and relevance check, not a second
exhaustive literature or priority audit. The nearby nice-derivation lead was
already present in the project. None of the calculations here is being
advertised as historically new.

The immediate next tests concern higher normal order and the polynomial
module of elements killed by \(N^3\). They must retain the actual generating
frame or explicitly state when an intrinsic polynomial model replaces it.
The \(L=0\) sector, noncollapsed whole double fibers, global recognition,
and arbitrary-frame reduction remain unresolved.

[^cid]: Luis Cid, [*On nice Gm-actions arising from locally nilpotent derivations with slice*](https://arxiv.org/html/2604.03471v1), arXiv:2604.03471v1. The primary HTML introduction, Lemma5.3 and Theorem5.4 with their proofs were re-inspected. Its header says April3,2026; the rendered manuscript says August24,2026. No new validity claim about its other results or all cited dependencies follows from this comparison.

## Sources

1. [Whole-plane-fiber theorem99](quadratic-whole-plane-fiber-pass99.md), actual whole-fiber presentations and preserved original partial.
2. [Volume-normal splitting99](quadratic-volume-normal-splitting-pass99.md), exact conormal normalization and strict weighted leading derivation.
3. [Whole-fiber actions100](quadratic-whole-fiber-actions-pass100.md), complete working derivation and explicit algebra-only boundary.
4. Luis Cid, [*On nice Gm-actions arising from locally nilpotent derivations with slice*](https://arxiv.org/html/2604.03471v1), Theorem5.4, comparison only.
