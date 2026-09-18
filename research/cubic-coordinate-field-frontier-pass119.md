# The coordinate-first-integral branch is excluded

Under the supplied actual constant-acceleration framework90, an exact
cubic relative relation cannot have rational invariant field C(s) for
an actual polynomial coordinate s of the embedded invariant plane S.
This is a stronger conditional exclusion than118's prescribed speed
family. It does not establish that the invariant field has such a
coordinate generator, and it does not solve general cancellation.

The working cancellation target remains the unconfirmed interpretation
of the professor's email: A[u] isomorphic to C^[4] should imply A
isomorphic to C^[3]. The literal affine-line conclusion in the pasted
email has the wrong dimension for general r. All deductions below
concern the stated complex-threefold specialization and supplied frame.

## 1. The conditional theorem and complete reduction

Assume the full original-coordinate and slice hypotheses90, its actual
embedded invariant plane S=C[s,t], and an exact cubic relative relation.
Let V be the leading cubic direction118. Add the hypothesis
ker(V:Frac(S) to Frac(S))=C(s), where s is a polynomial coordinate of S.
Then these hypotheses are inconsistent.

Here is the proof, with each separate argument linked at its full scope.

1. [The line/rank lemma](cubic-coordinate-first-integral-line-pass119.md)
   uses Q,n over C(s), n transposed b=0, and b transposed Qb=-1.
   On the polynomial t-line, a nondegenerate binary quadratic level
   would require nonconstant polynomial units. Therefore its restriction
   to ker n has rank one and b=p(s)+d(s)H(s,t), with p,d polynomial,
   d primitive and H_t nonzero. Rank Q cannot be one. Rank two makes
   d a constant complex column; rank three makes det Q a nonzero constant.

2. [The ruled nondegenerate exclusion](cubic-ruled-nondegenerate-exclusion-pass119.md)
   treats rank three. The exact cubic tensor annihilates the ruling
   derivative, which is proportional to V. The connection identities
   force a specific ruled form. The cubic potential and its exact
   linear part, together with actual unit volume in K[v,u], produce a
   coefficient identity whose w-coefficient is -7ar3. Here a and r3
   are both nonzero functions of s, while w=H(s,t) is transcendental
   over C(s). That coefficient cannot vanish.

3. In rank two the constant column d can be sent to a coordinate vector
   by an actual constant ambient GL3 change. The speed becomes
   b=(a(s),H(s,t),f(s)). [The polynomial-curve exclusion](cubic-polynomial-curve-exclusion-pass119.md)
   treats this form without assuming a or H is a coordinate. Its
   scalar residual first forces deg f=3 deg a after a constant GL2
   normalization. A formal first-variation multiplier with roots
   1,3,5,7,9 excludes every lower correction except a linear term.
   Consequently f=lambda a cubed+mu a.

4. The actual reconstruction then makes an original affine-linear
   coordinate constant modulo s-s0, for any root s0 of a. The
   full invariant-kernel intersection supplies the needed polynomial
   residue. That coordinate is irreducible, while s-s0 is an invariant
   nonunit. Their forced association contradicts the coordinate's
   nonzero E-derivative.

Both possible metric ranks have now been excluded under the additional
coordinate-field hypothesis. These are parts of one result, not several
independently recognized branches. Neither the nice-slice recognition80
nor the superseded quadratic conic/fiber chain91--116 is an endpoint
of this proof. The actual cubic potential and volume framework90 and
moving-frame constraints118 remain premises.

## 2. What the countercontrols preserve

The ruled proof gives a globally unimodular polynomial velocity with
nondegenerate Q, det Q=1 and nonzero rank-one cubic tensor. Thus the
metric identities and absence of a common speed zero do not themselves
prove the exclusion. Its actual cubic potential and volume completion
are precisely what the coefficient contradiction prevents. No global
original coordinate frame is assigned to that tuple.

The principal-open models118 have stronger local realization, including
explicit inverse formulas and unit Jacobian, but retain a genuine global
slice pole. The new polynomial-curve proof agrees with those examples:
the contradiction uses original-coordinate irreducibility in the whole
polynomial ring, not a claim that the local identities are inconsistent.

There is a wording clarification for the frozen
[principal-open note118](cubic-principal-open-frame-control-pass118.md).
Its phrase about excluding the entire velocity family as a global
original frame means exclusion **in the exact cubic relative branch**.
It is not an exclusion of all actions with those velocities. The
theorem118 and its synthesis already have that qualification. The
frozen file is preserved, and this clarification changes no theorem.

## 3. Rational, polynomial, and coordinate generators remain different

The [first-integral source and obstruction note](cubic-first-integral-polynomial-gates-pass119.md)
records the exact criterion for the first of the missing improvements.
For the reduced rational generator H=A/B, the field C(H) contains a
nonconstant polynomial exactly when some constant linear combination
lambda A+mu B equals one. Then C(H)=C(g) for a polynomial g, and its
intersection with S is C[g]. This is the selected consequence of
de Bondt's Theorem3.1 and Lemma3.3.[^field] It does not make g a coordinate.

For example, s partial_s-t partial_t has polynomial invariant st,
which is not a coordinate. The everywhere nonzero field
s squared partial_s-partial_t has rational field C(s/(st-1)) but
no nonconstant polynomial invariant. These are boundary examples for
general derivations, not claimed actual cubic frames.

A second exclusion uses a finite common point of A and B. The actual
metric identities then exclude a generic affine pencil curve with only
constant geometric units. The relevant curve is the entire affine
closure A-HB=0, not just its B-nonzero open subset. The radial pencil
is excluded this way. A separate explicit unimodular coefficient
example shows why the unit assumption cannot be removed using those
metric facts alone. Its rational invariant field has no polynomial
generator. Geometric integrality follows from relative algebraic
closedness in characteristic zero, with the selected Stacks argument
recorded explicitly.[^geometric]

## 4. Verification and unresolved obligations

The [canonical targeted capture](verification-pass119-working.json)
passes six suites and twelve methods, five new and seven retained.
The new exact checks cover ruled tensor and volume coefficients, the
unimodular coefficient control, the indicial and first-variation
identities, and selected ramified-base and root-divisor calculations.
They do not establish the all-degree formal-series argument or the
global invariant and irreducibility premises. Independent full-file
AI proof reconstructions found no invalidating gap in these stated
scopes. This is not Lean verification, human expert review, or an
exhaustive novelty audit.

The result leaves the general rational first-integral case unresolved.
Even complete cubic recognition inside the supplied framework would
still leave the separate arbitrary-frame entry problem. The overall
cancellation goal is therefore active and unsolved. No public posting,
submission, external contact, paid resource, or new automation is part
of this pass.

The next proof task is to test which arguments actually need a coordinate
generator. In particular, rank-two metric geometry may force polynomial
projections, permitting the source intersection criterion to replace
the coordinate premise; the ruled nondegenerate calculation may also
transfer over an arbitrary rational invariant field. These are next
proof obligations, not additional theorems claimed by this checkpoint.

## Sources

[^field]: Michiel de Bondt, [*Rational maps H for which K(tH) has
transcendence degree 2 over K*, arXiv:1501.06046v4](https://arxiv.org/html/1501.06046v4),
Theorem1.1 statement and attribution; Theorem3.1, Corollary3.2 and
Lemma3.3, selected statements and displayed proofs. Their deeper
classical dependencies were not all reconstructed in this pass.

[^geometric]: The Stacks Project, [Lemma10.47.8, Tag037P](https://stacks.math.columbia.edu/tag/037P),
statement and complete displayed factor-coefficient proof. Characteristic
zero is used for the field-valued finite scalar extensions in the note.
