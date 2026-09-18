# Proof reconstructions and execution evidence

The pass completes bounded arguments, not the general cancellation goal.
All reviewers here are AI agents. Their separate reconstructions are not
human peer review, a proof-assistant check or certification of novelty.

## Geometric obstruction

The geometry author wrote the complete proof in
[nodal-second-exponent-pass36.md](nodal-second-exponent-pass36.md).
The main and general agents independently reconstructed its actual
completed-base normalization, open quotient sections, three exact
overlaps and arbitrary-pole graph contradiction. Both found the proof
sound under the retained previous invariant-image and isolation inputs.
The main agent additionally reread the primitive-Jacobian content proof
in pass 32.

The quotient step was checked against the full relevant primary lemmas.
The main agent specifically rejected using the constant-group statement
071R as the additive-group quotient theorem and read 06PH instead.
The final exposition proves the action relation is an open immersion
before invoking freeness and the quotient theorem. This is an ordering
clarification, not a change to the hypotheses or construction.

The author initially ran five methods successfully in 0.203 seconds.
The root's separate targeted run passed in 0.211 seconds. The general
agent's independent run passed in 0.195 seconds; the author's final
rerun passed in 0.201 seconds. These are executions of the same five
methods, not additional tests. No failed mathematical assertion was
reported in those runs.

## Integrability criterion

The jet author wrote
[q1-integrability-pass36.md](q1-integrability-pass36.md), including
the full nonzero-speed first jet and an explicit physical inverse.
The main, general and geometry agents independently checked the
single-U necessity, all-fiber pole contraction, slice theorem,
reduced triangular inverse, denominator clearing, finite nilpotent
inversion, CRT compatibility and both zero-speed parity branches.
No mathematical correction was requested.

The initial eight-method author run passed in 0.701 seconds. The main
run passed in 0.691 seconds; the general and geometry runs each passed
in 0.704 seconds. All reviewers read the standalone checker. It imports
only unittest and SymPy, not project proof or solver internals.
The checker has no floating-point literals. These finite controls do
not replace the written all-degree argument.

## The original-cylinder equivalence

The general author wrote
[intrinsic-transfer-pass36.md](intrinsic-transfer-pass36.md).
The main, jet and geometry agents separately checked the coefficient
bracket, volume descent, regular-multiplier saturation and divergence
step. In particular, H=aD initially gives only a regular multiplier;
divergence zero is what puts a in ker(D). The five-way equivalence is
proved, but none of its equivalent conditions is proved automatic.
No artificial example suite is counted as verification of that
universal missing implication.

## Synthesis corrections and new source lead

The geometry agent read the entire root synthesis. Four corrections
were applied: a missing backslash in a spacing command; local slice
instead of slice for derivative x²; the explicit nonzero polynomial
g hypothesis; and unproved, not false, for the Jacobian-one
invertibility shortcut. The last distinction matters because the
general Jacobian implication is not known false. The proof itself
uses a genuine inverse argument.

The geometry agent reread the final corrected synthesis, including the
added Su lead paragraph, and confirmed all four corrections were present.
It independently summed the saved regression to 77 suites and 802
methods with the stated time interval. No further correction was found.

The general agent found a concrete source lead in Tao Su's paper.
The main agent independently read the candidate statement, its field
and genericity conditions, and the quotient/trivialization construction.
The accessible source is arXiv v4; the initial BIMSA journal-PDF request
failed. The [lead note](su-candidate-lead-pass36.md) does not claim
pairwise distinctness, nonpolynomiality or an explicit reconstructed
quotient action. It identifies one bounded next task.

An oversized attempt to return old metadata was truncated and could
not be JSON-parsed. It made no edits. A smaller read of the exact last
claim, current packet and orchestration sources succeeded. Two synthesis
patch attempts had unmatched context and made no edits; the subsequent
patch applied against the actual text. These are tooling issues, not
failed mathematical tests.

## Authoritative full regression

The actual complete regression ran from 2026-09-13 12:46:50 UTC through
2026-09-13 12:48:14 UTC. All 789 preceding methods and 13 new methods
passed, totaling 802 methods across 77 suites. The process exited zero.
Its JSON output was captured directly on completion and saved in
[verification-pass-36.json](../verification-pass-36.json).

The new fork suite passed five methods in 0.208 seconds of unittest
time in that full run. The integrability suite passed eight in 0.726
seconds. Wall-clock process durations are separately retained in the
JSON. The five runner parser controls and two integrity link-parser
controls are not mathematical methods.

The separate artifact checker checks JSON, AST method counts, current
flags, links, whitespace, report numbering and source SHA256 hashes.
That is reproducibility evidence, not theorem verification. The
professor's interpretation, novelty, expert-review and formalization
flags remain false. The general conjecture remains unsolved.
