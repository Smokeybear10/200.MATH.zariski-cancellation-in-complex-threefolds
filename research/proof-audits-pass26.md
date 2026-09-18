# Pass 26: proof reconstruction and verification record

## Scope

This is a record of separate AI reconstructions, primary-source checks,
finite symbolic tests and artifact checks. It is not human peer review,
Lean verification, or a novelty certificate. The target interpretation
remains unconfirmed by the professor.

## Simultaneous-frame proof

The main investigator read the complete proof and standalone checker.
A separate investigator independently reconstructed the one-LND
completion argument, including the descent from Frac(S) to S.
The key step is g(t)q'(t)=1 after two-variable triangularization,
not an inference from a unit Jacobian.

The proof retains both commutation and local nilpotence as separate
hypotheses. Removing the latter is identified precisely with the
two-variable Jacobian conjecture. The tangent-field application retains
the missing actual relative-plane and unimodular-complement hypotheses.
The height calculation is for an explicitly invertible coordinate word,
not a universal decreasing procedure.

The author corrected one initial test expectation about a bracket
with an old base partial. The final test uses the verified nonzero
brackets; the coordinate formulas and written theorem did not change.
All four actual new coordinate partials and their six mutual brackets
are checked. This correction is not hidden as successful initial output.

## Moving-plane and Lie proof

The main investigator read the entire proof and checker.
A second investigator separately checked the coefficient formulas,
joint invariant ring and rational field argument, nonnilpotent Q4
recurrence, and infinite Lie-bracket recurrence.

Finite local nilpotence of ad(delta) on each derivation is not confused
with local nilpotence of each resulting derivation on the ring.
Nor is it confused with finite-dimensional Lie closure.

The successful primitive part of the highest adjoint is retained:
partial_a is sliced in the actual control. The new common invariant
plane is for delta and partial_a, not for the original delta and Delta.
No universal primitive-slice consequence is claimed.

## Fence and intrinsic-centralizer proof

A separate investigator reconstructed the root proof.
Commutation preserves the full plinth ideal, the LND divisibility
lemma kills its generator, and the non-fence restriction to the plane
is zero. Primitive UFD saturation supplies the exact orbit-line
conclusion. In the fence case, one finite power of p clears the
derivatives of every algebra generator, preserving nilpotence because
partial_h(p)=0.

The audit also checked the fiberwise modification identification.
If pU+vG=1 and the slice is Ur+vt, its quotient is
R[w]/(vw-r): t maps to -Uw, and w maps to Gr-pt.
The base for the cited slice theorem is C[u], not C[u,lambda].

One wording correction was applied: the intrinsic application now says
“when its full plinth is principal as in (5).” Merely having identified
an arbitrary plinth is not the hypothesis of that proposition.
The ambient-coordinate conclusion is restricted to the published
polynomial-three-ring case.

The final synthesis audit also required the adapted coordinate choice
p in C[u] in its intrinsic fence bullet. The full proof already used
that choice; the synthesis was corrected rather than claiming the
assertion for an arbitrary naming of the invariant plane coordinates.

## Actual surface proof

The main investigator read the complete note and checker.
A separate investigator independently audited the complete proof,
ran its seven methods, and found no actionable error.

The invariant-replacement proof includes constant j, every nonconstant
polynomial with a nonzero root of j-j(0), and the remaining monomial
case. In the last case 4 divides the exponent, and the differential
fails in the full pinched cotangent space, not only on one branch.

The affine-projection kernel case split is exhaustive.
The normalization relation is irreducible by its primitive
H-linear expression. Actual normalization recovery gives the
height-one presentation. The conductor difference is an S-linear
map with quotient S/(Q), not a ring quotient. Its u^2-image is two
on every pair, proving surjectivity.

The displayed free basis has determinant Q inside the normalization
basis, correctly a nonunit. Cayley-Hamilton justifies the exact
nine-power determinant criterion. Neither argument determines the
abstract minimum number of generators, which remains between three
and four.

## Primary sources checked during this pass

- Derksen's lecture notes: Theorem 2.13; Section 4 slice identities
  and Proposition 4.6; Theorem 5.9 and its proof. These supply credited
  classical inputs, not an unconditional Jacobian theorem.
- Stampfli's primary manuscript: Section 5.3 through Remark 5.3.4,
  including Lemma 5.3.1, the exact rank/fence Remark 5.3.1, and the
  stronger polynomial-ambient admissible-complement construction.
- Dasgupta and Gaifullin's primary manuscript: Proposition 2.14,
  Lemma 2.15, and Proposition 5.3. The polynomial ambient assumption
  was explicitly retained.
- Derksen, van den Essen and van Rossum's author-uploaded manuscript:
  Theorem 4.4 and Corollary 4.5, including proofs. The Dedekind-base
  restriction prevents the proposed two-dimensional-base shortcut.

Exact links and statement locations appear in
[the synthesis](../deep-pass-26.md) and the individual proof notes.
Selected sections, not every page of every manuscript, were read.
This was a targeted proof-input audit, not a comprehensive priority
search across all publications or subscription databases.

## Actual test and integrity evidence

The three new checkers import only unittest and SymPy and have
12, 8 and 7 test methods. They do not import solver internals or
other project modules. All were read by the main investigator and
run independently of the authors' runs.

A full regression completed at 08:09:45 UTC on September 13, 2026,
with 580 methods across 46 suites, all passing. The saved repeat
run is recorded verbatim in
[verification-pass-26.json](../verification-pass-26.json).
Repeat runs and the runner's five parser controls are not additional
mathematical test methods. A large combined metadata read exceeded
its tool-output limit and was discarded; smaller read-only append
anchors were used instead. No project data were changed by that read.

The separate [integrity checker](consistency_checks_pass26.py)
checks current links, claim continuity, flags, AST method counts,
new checker imports, JSON, report numbering, whitespace and hashes.
Its [result](../consistency-pass-26.json) is file integrity, not a
formal certificate for the mathematical arguments.

The full conjecture, novelty determination, human expert review and
proof-assistant formalization all remain incomplete. No external
message, submission, public posting or new automation occurred.
