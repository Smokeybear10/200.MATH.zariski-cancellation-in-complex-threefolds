# Closing the auxiliary action route and deciding a class of pencils

The full complex threefold cancellation conjecture remains unsolved.
This pass does finish two bounded investigations. The unchanged pinched
surface cannot carry any nonzero action induced by an ambient additive
action under a hypothetical hypersurface presentation. Separately, the
entire degree-one polynomial normal form now has an exact integrability
criterion, constructive on the branch where its common-slice factor is
nonzero at the marked divisor.

These are private working proofs with separate AI reconstructions and
finite exact controls. They are not an expert-reviewed result, a Lean
formalization, or a novelty claim. The professor has not confirmed the
dimensional correction or the choice of field in the working question

\[
A[s]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]

## 1. The auxiliary action route is now closed

The fixed auxiliary ring is the same pinched surface used in the earlier
passes. Its normalization is

\[
B_0=\mathbb C[u,y,z]/((u-1)(u-i)z-y(y-1)),
\qquad d=u^4-1.
\tag{2}
\]

Six normalization lines are paired into three conductor lines. The
pairings are \((1,0)\sim(i,0)\), \((1,1)\sim(-i,*)\), and
\((-1,*)\sim(i,1)\), with the previously specified scaled line
parameters. The ring itself, not just the number of lines, is retained.

The earlier all-speed reduction showed that any nonzero ambient
extension under a hypothetical presentation \(R=W/(F)\),
\(W\simeq\mathbb C^{[3]}\), would yield a primitive extension of
\(u\delta_0\) and the actual nodal invariant image

\[
S=\mathbb C+d\mathbb C[u^2]
  =\mathbb C[d,v]/(v^2-d^2(1+d)).
\tag{3}
\]

Pass 35 excluded exponent one. The new proof excludes every exponent.
It uses separatedness, so it does not have to classify all possible
later modification centers.

### The local obstruction

Let \(H=\mathbb C[[x,y]]\). Suppose three open copies of
\(\operatorname{Spec}H\) in a quotient space have overlaps

\[
U_A\cap U_B=D(y),\qquad U_A\cap U_C=D(x),\qquad
U_B\cap U_C=D(xy).
\tag{4}
\]

An additive torsor trivializes on each affine chart. Its transitions
are translations. Separatedness of its total space forces the first
two translations, in reduced form, to be

\[
t_B-t_A=P/y^n,\qquad t_C-t_A=Q/x^m,
\quad m,n\ge1,\quad P,Q\in H^*.
\tag{5}
\]

Here the unit requirement is essential. If, for example, \(P\) were
a nonunit, the exact graph closure
\(y^n(t_B-t_A)-P=0\) would meet the closed product fiber even
though the overlap excludes that fiber. A regular translation gives
the same failure. Primitivity of the defining polynomial proves the
claimed graph closure by saturation, without a bounded pole-order
assumption.

The third transition is forced by the cocycle identity:

\[
t_C-t_B=\frac{Qy^n-Px^m}{x^my^n}.
\tag{6}
\]

Its numerator lies in \((x,y)\) but is divisible by neither
\(x\) nor \(y\). Its graph closure therefore contains the
closed product fiber too. This contradicts separatedness. Extra
quotient charts cannot repair a nonclosed diagonal on these three.

### Why the actual surface forces these overlaps

The primitive Jacobian identity makes the ambient quotient map smooth
of relative dimension one wherever the action is nonzero. The earlier
isolation result removes other exceptional components near this node.
The node fiber consists of three free orbits; the fixed fiber lies at
a different base point.

Use ordinary scheme base change to the completed invariant plane,
not a claimed algebraization of a formal total space. The nodal
equation becomes a unit times \(xy\). The free action has an
algebraic-space torsor quotient, étale over \(\operatorname{Spec}H\).
This follows from the actual action relation being an open immersion,
not from an assumption that the invariant quotient has connected
fibers.[^1]

Henselian lifting gives an open section through each of the three
closed orbit points. Their preimages are genuine open trivial torsors.
The completed normalization splits into four explicit components,
indexed by \(u=r(1+d)^{1/4}\), \(r=1,-1,i,-i\). Normalizing
the restrictions of those open charts proves their generic incidences:

| Chart | Orbit over the generic first branch | Orbit over the generic second branch |
| --- | --- | --- |
| \(U_A\) | \(r=1\) | \(r=i\) |
| \(U_B\) | \(r=1\) | \(r=-i\) |
| \(U_C\) | \(r=-1\) | \(r=i\) |

All three agree off the two branch divisors. The table and their
distinct closed points prove exactly (4). These are not hypothetical
labels assigned to an unconstructed quotient. The graph obstruction
then contradicts the separatedness of the actual affine base change.

Consequently, in any hypothetical hypersurface presentation of this
unchanged \(R\), an ambient LND preserving its equation cannot
induce a nonzero LND on \(R\). The full proof, including the
four-component normalization, is in
[the geometry note](research/nodal-second-exponent-pass36.md).

This does not prove that \(R\) cannot embed in affine three-space.
An embedding whose surface actions all fail to extend remains possible.
The generator bound \(3\le\mu(R)\le4\) is still unresolved.
The classical use of torsors over nonseparated curves is explicitly
credited; priority for this precise consequence is not established.[^2]

## 2. An exact integrability criterion for degree-one pencils

For the fixed canonical model, retain polynomial data

\[
h=x^2c-b^2,\quad F=p(x)b+Q(x,h),\quad
\mathcal D=D_0+\lambda g(x,F)J_F,
\quad D_0=x^2\partial_b+2b\partial_c,
\tag{7}
\]

where \(p\ne0\), \(g\in\mathbb C[x,T]\) is nonzero,
\(J_F\) is primitive, and
\(J_H=H_c\partial_b-H_b\partial_c\). Let
\(G(x,T)=\int_0^Tg(x,z)\,dz\), and set
\(K=h+\lambda G(x,F)\). Then \(\mathcal DK=0\) and
\(\mathcal DF=x^2p\).

An actual normalized isomorphism intertwining this pencil with
\(x^2\partial_w+2(1+\lambda x)^2w\partial_z\) exists if and
only if one polynomial \(U\in\mathbb C[x,\lambda,T]\) satisfies

\[
N=F-Q(x,K)+\lambda U(x,\lambda,K)\in pR,
\qquad K+(1+\lambda x)^2(N/p)^2
          \in\mathbb C[x,\lambda]+x^2R,
\tag{8}
\]

where \(R=\mathbb C[x,\lambda,b,c]\). Only \(U\) modulo
\(px^2\) matters. This bounds its needed \(x\)-degree, not its
degrees in the other variables.

Necessity comes from the exact generic slice coordinates followed by
pole contraction at every \(x\)-fiber. For sufficiency, the first
congruence gives a polynomial local slice \(W=N/p\); the second gives
a polynomial \(Z\). The proof obtains an actual inverse off \(x\)
by kernel contraction and the slice theorem, and an actual triangular
inverse modulo \(x\). Injectivity modulo \(x\) then clears every
inverse denominator. It never invokes the unproved shortcut that a
Jacobian-one polynomial map must be invertible.

When \(p(0)\ne0\), this becomes a constructive test on the
supplied data. It requires coefficientwise radical divisibility
\(\operatorname{rad}(p)\mid g\), an explicit constant-speed
boundary condition, and one first-jet parity condition. Finite
nilpotent inversion constructs \(U\) modulo \(p\); the parity
calculation constructs it modulo \(x^2\). The Chinese remainder
theorem joins them. The complete formulas, including nonzero boundary
speed, are in [the integrability proof](research/q1-integrability-pass36.md).

At zero boundary speed, write \(g=xg_1+O(x^2)\) and
\(Q=Q_0+O(x)\). The all-degree parity calculation forces
\(\deg Q_0\le1\). If \(Q_0=q_0+q_1T\), \(q_1\ne0\),
it requires \(g_1=2/(3q_1)\). If \(Q_0=q_0\) is constant,
the odd part of \(g_1(q_0+z)\) must equal
\(-4z/p(0)^2\), while its even part is unrestricted.

### A sharp limit on what a common local slice proves

Take \(p=1\), \(Q(T)=T\), \(g=2x/3\). These data pass the
constructive test and admit explicit polynomial maps in both directions.
Yet

\[
L=x^2\partial_b+(2b-1)\partial_c,
\qquad \mathcal D(x^2c-b^2+b)=x^2,
\tag{9}
\]

has a nonsliced primitive top: \(L\) vanishes on
\(x=0,b=1/2\). Thus even a common local-slice derivative exactly
equal to \(x^2\) cannot replace the missing global coordinate
companion. A determinant-one two-by-two matrix and physical
divisibility checks verify this example independently of the general
recognition proof.

This is integrability of supplied data in an already polynomial
model. It is not a degree-preserving repair path for every horizontal,
and it does not produce such a model for an unknown \(A\) in (1).

## 3. The exact remaining gate under the original cylinder hypothesis

There is also a bounded deduction directly under (1). Assume the
intrinsic LND rank of \(A\) is one, write its primitive direction
as \(D\), and let \(C=\ker D=\operatorname{ML}(A)\). For an
actual ambient LND \(T\) with genuine degree one relative to
\(E=\partial_s\), write

\[
T=D_0+s fD+(b_0+s b_1)E,\qquad 0\ne f\in C.
\tag{10}
\]

Its opposite double commutator has no \(s\)-dependent coefficients.
The polynomial cylinder supplies a volume form that descends to
\(A\). Divergence zero and primitive saturation prove the exact
equivalence

\[
T(C)\subseteq C
\quad\Longleftrightarrow\quad
[T,[E,T]]\text{ is locally nilpotent}.
\tag{11}
\]

The proof allows \(T(s)\ne0\). It does not assume that \(T\)
descends. But neither side of (11) is proved automatic, and preserving
\(C\) is weaker than killing it. The needed finite all-LND closure
and a useful independent intrinsic direction remain unconstructed.
See [the full cylinder-specific deduction](research/intrinsic-transfer-pass36.md).

## 4. A concrete next candidate from the literature

Tao Su's character-variety paper explicitly identifies 80 affine
threefold cells whose cylinders are affine four-space. The paper
presents their nonpolynomiality as an expectation, not a theorem.[^3]
This is a directly relevant candidate family, not a discovery of ours.

The [bounded source audit](research/su-candidate-lead-pass36.md)
selects one braid walk and generic rational eigenvalues. The next
task is to extract that cell's four-coordinate additive action and
verify an explicit slice and cylinder inverse. Its quotient ring has
not yet been reconstructed here, and no nontrivial example or
counterexample is claimed.

## 5. Verification, status, and next work

The standalone suites check bounded exact branch expansions, graph
saturation, congruences, repeated-root inversion, parity and explicit
inverse maps. They do not prove the algebraic-space existence theorems
or universal quantifiers. All 802 methods across 77 suites passed in
the complete run from 2026-09-13 12:46:50 UTC through 12:48:14 UTC.
Thirteen methods in two suites are new; repeated executions and
orchestration assertions are not extra methods. The actual output is in
[verification-pass-36.json](verification-pass-36.json); the separate
[proof audit](research/proof-audits-pass36.md) records the reconstructions.

The deep-research workflow prompted the additional quotient-source
audit, especially the distinction between an abstract constant-group
quotient and an additive-group torsor. Source access, inherited inputs,
the classical torsor comparison and search limits are recorded in
[the literature audit](research/literature-scope-pass36.md).

The ambient-action route for this fixed surface should now stay closed.
There is no reason to search its higher plinth exponents again unless
the proof is corrected. The full cancellation problem needs a different
step: reconstructing and recognizing one of the published candidate
quotients, or proving that the original cylinder's actual ambient
actions yield useful intrinsic recognition structure. Neither task
has been completed here.

No external contact, submission, public posting, payment, new task or
automation was performed. No novelty or expert-review status is implied
by the completion of these bounded proofs.

[^1]: [Stacks 06PH](https://stacks.math.columbia.edu/tag/06PH), [0DU0, Lemma 101.32.1](https://stacks.math.columbia.edu/tag/0DU0), [04GG](https://stacks.math.columbia.edu/tag/04GG), and [024T](https://stacks.math.columbia.edu/tag/024T). The exact hypotheses and proof-access record are in the separate literature audit.

[^2]: Adrien Dubouloz, [*Danielewski-Fieseler surfaces*](https://arxiv.org/pdf/math/0401225), Proposition 2.6 and discussion through Proposition 2.9. Its base is a curve; the two-dimensional mixed-overlap obstruction above is proved directly rather than imported from that classification.

[^3]: Tao Su, [*Cell decomposition and dual boundary complexes of character varieties*](https://arxiv.org/pdf/2307.16657v4), Theorem 2.10 and Remark 2.12, manuscript pp. 21-24. The author's [publication list](https://tao-su-math.github.io/research/) records publication in *Advances in Mathematics*, volume 498 (2026). The accessible 2024 arXiv version was read, not the inaccessible journal PDF.
