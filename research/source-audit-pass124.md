# The source boundary beyond constant acceleration

This bounded primary-source check does not supply recognition for every
sliced derivation of the complex polynomial four-ring, or for every
supplied frame with orbit degree at most two. The terminology matters:
the published quasi-nice conditions below concern second derivatives of
selected coordinates, not third derivatives of all coordinates.

This is a source/applicability audit, not a new theorem, an exhaustive
negative literature result, or a novelty claim. It updates the entry
question after the working AI-only recognition statement in
[synthesis123](cubic-exclusion-frontier-pass123.md). The unrestricted
cancellation goal remains unsolved.

## 1. Three different hypotheses

For an actual sliced LND E of B=C[x1,x2,x3,x4], distinguish

\[
\begin{array}{ll}
\text{nice:}&E^2x_i=0\quad\text{for all four coordinates},\\
\text{orbit degree at most two:}&E^3x_i=0\quad\text{for all four coordinates},\\
\text{constant acceleration:}&E^2x_i\in\mathbb C
       \quad\text{for all four coordinates}.
\end{array}
\tag{1}
\]

The current retained results recognize the first and third conditions
when a slice is present. They do not yet recognize the middle condition
with arbitrary invariant acceleration coefficients. None of these
conditions bounds ordinary polynomial degree in the supplied variables.

Dasgupta and Lahiri, Definitions2.2--2.3, use m-quasi-nice when D squared
kills m members of some actual coordinate system; strictness excludes a
larger such number. Their Theorem4.1 assumes an irreducible nice
R-derivation on an already supplied R[X1,X2], with R a UFD. Theorem5.2
again assumes that relative polynomial presentation, requires the action
not to be fixed-point-free, and requires DX1 irreducible in R.
These are not four-variable orbit-degree-two recognition theorems.
Lemma2.9 gives no further slice obstruction: all full image ideals are
the entire invariant ring for a sliced action.
See the [version-six primary paper](https://arxiv.org/html/2302.13787v6).

## 2. The closest recognition and counterexample statements

Dasgupta and Gupta's Corollary3.8 assumes a characteristic-zero field,
an irreducible derivation, an actual invariant coordinate X1, and
D squared killing the other three coordinates. Their Theorem4.1 is
instead a three-variable result with D squared killing two coordinates.
Proposition4.4 requires an actual polynomial three-ring over an invariant
PID and its specified generic alternative. A rational invariant or a
generic polynomial chart does not supply these presentations.
See [the primary paper](https://arxiv.org/html/1701.03635v1).

Its Example4.5 is particularly useful for preventing a false extension.
On the actual ring k[t,X,Y,Z], set

\[
Dt=0,\qquad DX=t,\qquad DY=tZ+X^2,\qquad DZ=-2X.
\tag{2}
\]

All four third derivatives vanish. The example's kernel is the singular
ring k[t,F,G,H]/(F squared-G cubed-tH), hence not a polynomial ring.
However its image ideal is (t,X), so it has no slice. Its reported
rank three is relative to k[t], not a lack of a global invariant
coordinate. Thus this is a primary counterexample to dropping the
slice or regularity hypotheses, not a counterexample to the sliced
question. The displayed kernel proof was read, not just its summary.

Bhatwadekar--Gupta--Lokhande Theorem3.5 assumes characteristic zero and
D nonzero on an actual k[T,X,Y,Z], with DT=0 and regular kernel. It
concludes ker(D)=k[T]^[2].
Its proof localizes at maximal ideals of k[T], invokes its DVR
Proposition3.3(ii), and patches over that PID. A slice supplies regularity;
it does not supply T. Consequently a genuine rank-at-most-three bound
for a sliced four-variable action would apply through the invariant
ambient coordinate in the definition of rank. A differential rank bound
or an invariant transcendence basis is not that premise.
See [Theorem3.5 and its proof](https://arxiv.org/html/1501.01438v1).

## 3. Stable coordinates are an already recorded reformulation

Makar-Limanov, van Rossum, Shpilrain and Yu's Theorem1.2 proves, in each
fixed ambient dimension and characteristic zero, that the stable
coordinate conjecture implies cancellation. Its proof begins with an
LND having a slice and adds one variable. The slice becomes a coordinate
in that enlarged polynomial ring. This implication does not require
the separate Abhyankar--Sathaye embedding conjecture.
See the [published primary paper, Theorem1.2 and Section3](https://ems.press/content/serial-article-files/43009).

For the current input B=A[u], the same elementary fact is the swap of
u and an added indeterminate T in A[u,T]. It was already recorded in
[the stable-coordinate audit](stable-coordinate-pass.md), not discovered
in124. Descending it remains the substantive problem. The
Abhyankar--Sathaye assertion concerns rectifying a hypersurface already
known to be affine space; applying it to B/(u)=A would first require the
polynomiality currently sought. The distinction is also explicit in
Popov's [primary introduction](https://www.math.uni-bielefeld.de/lag/man/546.pdf).

Likewise, the equivalence between recognition and finding an invariant
ambient coordinate under the slice hypothesis is already retained in
[entry108](global-entry-audit-pass108.md). Neither equivalence is new
progress or a weaker substitute for unrestricted entry.

## 4. What an orbit-degree-two extension would still have to prove

Writing P=Ex and Q=E squared x gives EQ=0. It does not make the vector
field with coefficient column Q a commuting LND or a quasi-translation.
The [actual acceleration control81](acceleration-field-obstruction-pass81.md)
already disproves those implications, even with a unit coefficient
ideal. The Hessian term in acceleration's nonlinear transformation law
prevents interpreting Q as an intrinsic vector field.

Nor does subtracting u squared Q/2 produce an actual nice coordinate
frame merely because it kills the second derivatives. Failure of this
particular scalar filter is already in the retained
[universal-filter obstruction81](universal-slice-filter-obstruction-pass81.md).
These are previously proved controls, not new124 counterexamples.

Thus the bounded next question is genuinely about actual coordinate
changes for the middle class in(1), using its global slice. Any proposed
degree reduction must prove a polynomial inverse and a termination
mechanism. A claimed auxiliary acceleration action must first prove
local nilpotence and the required commutation. The sources inspected
here supply neither missing step. The separate124 investigation of
nonincreasing elementary coordinate reduction is not a consequence of
these literature statements.

## 5. The stable-tameness commutator is already published

Drensky and Yu's Theorem3.6(iii), printed page533, explicitly attributes
to Martha Smith the fact that exp(w delta) is stably tame when delta is
triangular and w belongs to its kernel. Their proof displays the
commutator after adjoining a variable t: with Q translating t by w and
E=exp(t delta), their composition convention gives Q inverse, E, Q,
E inverse. Both participating automorphisms are tame.
See the [published research paper and proof](https://hub.hku.hk/bitstream/10722/48401/1/63202.pdf).

Their reference19 is Smith, *Stably tame automorphisms*, Journal of Pure
and Applied Algebra58(1989),209--212,
[DOI](https://doi.org/10.1016/0022-4049(89)90158-8).
The original Smith article was not successfully opened. The attribution
and commutator passage here were checked in the accessible Drensky--Yu
paper, not represented as a fresh audit of Smith's original proof.
Thus a new explicit stabilization calculation in124 is not a new
stable-tameness theorem. Nor does stable tameness imply that a chosen
derivation-degree measure decreases along the factorization.

## Reading scope

The fresh source reads were the displayed Definitions2.2--2.3,
Lemma2.9 including its proof, and exact statements of Theorems4.1/5.2
in Dasgupta--Lahiri; Corollary3.8, Theorem4.1, and the complete displayed
Proposition4.4 and Example4.5 proofs in Dasgupta--Gupta; and the complete
displayed Theorem3.5 statement and short proof in Bhatwadekar--Gupta--
Lokhande. Their cited predecessor proofs were not all reread.

The published stable-equivalence paper's Theorem1.2 and its complete
Section3 proof were read, along with its introduction's distinction
between embedding and cancellation. The author-hosted copy extracted
poorly, so the publisher PDF supplied the usable text. Popov was read
only for the introduction's exact embedding statement, not for a new
recognition theorem. No current open-status conclusion is inferred
solely from a historical paper.

For stable tameness, the full displayed Theorem3.6(iii) proof passage,
the composition convention, and reference19 in Drensky--Yu were read.
The other parts of that theorem and their dependencies were not
independently audited for this attribution.

Searches separately used quasi-nice, four variables, slice, polynomial
flow, quadratic time, third iterate, acceleration, stable coordinate
and Abhyankar--Sathaye. Unrelated nilpotent Lie theory, positive-
characteristic examples and unaudited automated research pages were
not mathematical inputs. No primary theorem classifying all supplied
orbit-degree-two sliced four-variable actions was located in this
bounded search. No test was run, and no file through123, live index,
external message, submission or automation was changed by this note.
