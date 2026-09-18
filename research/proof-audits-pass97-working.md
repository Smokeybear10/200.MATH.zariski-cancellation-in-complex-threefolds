# Proof and verification audit for the quadratic source-balance investigation

The full cancellation conjecture remains unresolved. This pass records
a restricted total-four fiber exclusion, an exact weighted saturation
identity, and the resulting degree defect for all total-three fibers.
The unchanged original-frame assumptions are not consequences of
these new calculations.

## 1. Current conclusions and dependencies

The [source-balance proof](quadratic-saturated-source-balance-pass97.md)
uses equality in the retained flat-rank lemma to make the entire
actual local base change finite free of rank four. It then normalizes
an actual prime exceptional surface. The degree above every normalized
source-curve label is the sum of ramification index times residue
degree. Generic complex sections identify these contributions with
the actual Thom entries. The total column has even entries and
remains divisible inside the full supported lattice, contrary to
primitivity of the sum of its component basis.

This excludes every total-four quadratic fiber, not merely profiles
(3,1) and (2,2). The retained whole-irreducible multiplicity restriction
then excludes multiplicity-three components. Fibers containing a fixed
component have only profiles (2) and (2,1). Degree-one exceptional
branches are retained, and no first-normal-action hypothesis is used.

The [weighted extension](quadratic-weighted-rank-defect-pass97.md)
keeps all component residue degrees d_i. Under saturation the actual
row vector is the weighted component sum, and
n=lcm_j(N_j) gcd_i(d_i). This is not a claim that a weighted basis sum
is primitive. For total multiplicity three, weighted saturation is
impossible for any actual admissible function. Every admissible linear
projection therefore has generic degree four and special dimension
three, and its flat semilocal module is provably nonfinite.

All relative generators restrict affinely to each reduced component
of a total-three fiber. In profile (2,1), a constant affine combination
of the two good generators separates the reduced components. That
function is constant on both, is not an admissible projection, and
is not a coordinate theorem.

The [double-branch proof](quadratic-double-branch-pass97.md) gives a
singular even-multiplicity tangent for the essential split base branch
of (2,1), conditional on nonzero first normal action. The analogous
[triple proof](quadratic-triple-branch-pass97.md) is superseded as a
profile obstruction by total-four exclusion. Both retain exact formal
controls that descend to an unnormalized cusp and are formally
invariant but not rational on the actual exceptional surface.

The [original-volume proof](original-volume-constraints-pass97.md)
gives an actual quadratic graph and global complete-intersection
ideal for a noncollapsed whole double fiber. It also gives tangent
partial identities and cube-zero original Jacobian on its cylinder.
Neither identity is extended off the cylinder, and the projected
ideal generators are not claimed to be coordinates of A.

## 2. Saved-file proof reviews

The source-balance argument received separate reconstructions by Root,
Geometry, General and Jet. Root read the saved proof through EOF and
reread its finite-rank93, base-change94 and supported-lattice96 inputs.
Geometry authored the nine-equation note. General and Jet each read
the saved nine-equation proof through EOF, including the finite
localization, field tower, surviving labels and transverse-section
identification. Their verdicts did not rest on the integer checker.

Geometry authored the weighted extension after Root proposed keeping
the projection residue degrees. General independently reconstructed
the weighted balance and strengthened the divisibility to exact gcd
equality. Root reconstructed the same argument and the extension to
every total-three fiber, and read the saved eight-equation proof,
including its separator and explicit rank-defect control. Jet read
the saved eight-equation argument and checked the generic-section
residue factors, nonfiniteness, separator and graph limitation.
General also read the saved final eight-equation note, including its
broader total-three statement, and reconstructed every conclusion.
That statement follows from the same displayed gcd argument, rather
than a new numerical enumeration.

For the double note, Root supplied the proof and checker. General,
Geometry and Jet reconstructed the local argument. General and Jet
also checked the final conductor descent, formal invariance and
nonrationality strengthening, and independently reviewed the
extension to the surviving (2,1) profile. Final forward-status wording
distinguishes the local tangent restriction from global total-four
exclusion.

For the triple note and checker, Jet supplied the derivation.
Root read its original proof and the complete conductor/invariance
delta. General reconstructed that final delta and ran the checker;
Geometry checked all ten equations including the final strengthening.
The final forward pointer changes the status of its (3,1) hypothesis,
not its formal control.

General authored the original-volume note. Root, Geometry and Jet
read the proof and its final pointwise rank/nilpotence refinement.
The actual triangular inverse, slice projection, surface-only
commutator and original Jacobian identities were checked separately.

The supported-lattice note was authored by Geometry and read by Root
and General. Its gcd identity was already present in93 and is
explicitly not counted as a new identity. Its total-four column
calculations remain conditional intermediate results after the
source-balance exclusion.

These are separate AI proof reconstructions. They are not independent
human expert review, proof-assistant certification, or an exhaustive
reconstruction of every foundational result in the retained chain.

## 3. Exact finite verification

The [canonical capture](verification-pass97-working.json) records:
~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_double_branch_checks_pass97 research.quadratic_triple_branch_checks_pass97 research.quadratic_source_balance_checks_pass97
~~~

The final combined run exited zero, with three suites and three
methods, in 0.474191875 wall seconds and 0.081 unittest seconds.
All three input hashes were unchanged during the run. The capture
retains stdout and stderr in full, with a digest of stdout plus
one newline plus stderr. The canonical tool chunk is c84535.

The double checker tests the weighted coefficient, exact intrinsic
and formal relations, conductor/norm identities, formal derivative
calculation, nonsquare obstruction and finitely many prepared
quadratic valuation examples. The triple checker tests its intrinsic
fiber, three-to-two formal labels, conductor relation and invariance
identities. These finite calculations do not prove the universal
power-series preparation or geometric normalization arguments.

The source checker uses only standard-library integer arithmetic.
It tests the conditional full-lattice columns, their failed rank-four
row balance, seven branch-group tables, weighted (2,1) possibilities,
an unsaturated retained case and a positive weighted singleton case.
Its mixed degree-two/degree-three cubic control deliberately survives.
These examples do not verify the general ef-to-Thom identification.

Jet independently ran the final double and triple methods in chunks
7c6138 and 04af18, with unittest times 0.059 and 0.043 seconds.
After adding the weighted integer controls within the same source
method, Jet ran its final code in 9ea60b, passing in 0.000 seconds.
Root then read that final code before the canonical combined run.
General independently read and ran the final weighted source checker
in a93c6b, passing the same one method. Earlier source-checker hashes
and unweighted runs are superseded, not counted as extra coverage.

The historical full75 capture remains 146 suites and 1047 methods.
It was not rerun in this pass. The central claim registry remains
at 544 historical entries and has not absorbed the later working
notes. Neither that registry count nor a large old regression is
used as proof of the current universal statements.

## 4. Adversarial distinctions retained

The first local branch-count heuristic could not identify two complex
source labels with exactly two arithmetic transverse branches.
The triple control demonstrates three arithmetic branches assigned
to two labels. This mistake is not used in the saved exclusion.

Formal descent alone also failed as an obstruction. The conductor
moves the candidate into the original completed cusp ring, and the
candidate is formally invariant. A separate rational-function-field
argument is needed to show that it is not global algebraic invariant
data. No formal derivation is declared locally nilpotent merely
because the original derivation was an LND.

Strict flat-rank inequality cannot be upgraded to finiteness.
The weighted note includes a regular semilocal domain of generic
rank four with a double and a simple residual point of total length
three. Its missing fourth point is explicit in that control only.
The actual mixed fiber is not assigned a compactification point
without a construction.

Affine relative lines do not automatically have affine-linear
cylinders in the original coordinates. On a simple noncollapsed
component h can remain quadratic, giving a triangular graph of
degree up to three. The whole noncollapsed double case has a
stronger degree bound and is treated in its separate note.

## 5. Primary-source scope and preservation

During this pass the selected complete Stacks statements and proofs
for finite normalization, separable integral closure, faithfully flat
completion, henselian completeness, finite-algebra decomposition and
normalization lifting were read as recorded in the individual notes.
The present continuation freshly reread complete 0BXR, 032L and
00MC. Their use is limited to their stated algebraic hypotheses.

The retained Kaliman argument is the actual curve factorization and
integral homology diagram detailed in dependency96. Earlier selected
pass97 readings included Lemmas 2.1, 2.2, 3.1 and the start of
Proposition 3.2; this continuation additionally checked the displayed
scope of Proposition 4.2 and Theorem 5.2. The latter free-action
recognition theorem is not applied to a still-possibly-fixed N.
No fresh wholesale topology proof, exhaustive novelty audit or
visual PDF page audit is claimed.

The predecessor audit in chunk177c09 rechecked all 573 frozen
records through96 unchanged, the retained run inputs and outputs,
and the historical claim count. README and the research ledger
are live navigation documents, not frozen proof inputs. The project
remains untracked in its parent worktree, so git diff alone is not
an integrity certificate.

## 6. Unfinished work

The exact-defect-one (2,1) case, whole collapsed double fibers and
whole noncollapsed double fibers have not been excluded. The
first-normal-zero sector has not been folded into the local tangent
theorem. The reduction of arbitrary sliced actions to the original
constant-acceleration frame remains a separate unsolved requirement.

The [synthesis](quadratic-tangent-and-coordinate-frontier-pass97.md)
and [checkpoint](checkpoint-pass97-working.json) preserve the full
target and these boundaries. The intervening user check-in was a
status-only turn, classified as no progress; this continuation
revalidated the saved state and made new weighted proof progress.
No professor confirmation, expert outreach, submission, publication,
historical novelty claim or formal certificate was obtained.
