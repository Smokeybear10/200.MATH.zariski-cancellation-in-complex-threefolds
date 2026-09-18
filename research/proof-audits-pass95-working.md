# Proof and execution audit for pass95

The general cancellation target is unsolved. Pass95 proves
additional conditional restrictions in the supplied actual
frame and an explicit obstruction to a global extraction
shortcut. This document records evidence scope, not novelty,
human mathematical endorsement or formal verification.

## Written deductions and reviews

Five mathematical notes are retained.

| Note | Numbered equations | Author | Separate saved-proof AI reviews |
|---|---:|---|---|
| [Double components disjoint](quadratic-double-components-disjoint-pass95.md) | 9 | Root | General, Geometry, Jet |
| [Noncollapsed local model](noncollapsed-quadratic-local-translation-model-pass95.md) | 8 | Jet | Root, General, Geometry |
| [Cubic leading pencil](nonconical-cubic-quadratic-pencil-pass95.md) | 12 | Geometry | Root, General, Jet |
| [Projected-generator obstruction](projected-generator-linear-extraction-obstruction-pass95.md) | 6 | General | Root, Geometry, Jet |
| [Everywhere quadratic quotient rank](quadratic-quotient-rank-everywhere-pass95.md) | 7 | Jet | Root, General, Geometry |

The five notes have 42 numbered equations. The synthesis
adds four, for 46 across this pass's mathematical material.
The number of equations is an inventory count, not a
mathematical strength or progress metric.

The first note was initially reviewed with eight equations.
The final ninth equation, forcing constant weighted
coefficients, received separate complete delta reviews.
The cubic note's final provenance and control clarifications
were also reviewed separately. General's everywhere-rank
review first concerned the outline; its subsequent review
read the complete saved seven-equation proof through EOF.
Root reread the entire rank proof and its whole-irreducible
ramification92 input, not just the earlier generic-rank
corollary.

The principal proof gates are as follows.

- Double-component disjointness uses actual saturated
  base change and relative lines, a direct length-four
  quadratic-initial argument, and nonnilpotent leading
  Jacobian fields at either possible intersection rank.
  It does not transfer generic component multiplicities
  automatically to a tangent cone.
- Everywhere rank uses pairwise disjoint reduced curves,
  lifted idempotents, actual embedded parameter subrings,
  whole-thickening finiteness and torsion-freeness, and a
  transverse length contradiction. The exclusion of a
  sole multiplicity-four component uses the full
  whole-irreducible-fiber topological theorem92.
- The noncollapsed model's differential parameters are
  actual polynomial functions. Its nonzero first normal
  action hypothesis is essential to the stated argument;
  the reduced smooth-open-line conclusion precedes and
  does not need that hypothesis.
- The cubic argument applies a kernel theorem on a literal
  polynomial associated-graded ring. It does not assume
  that an arbitrary coefficient-field localization or
  completion remains locally nilpotent.
- The extraction obstruction has an actual four-variable
  polynomial inverse and an all-coefficient complex-root
  proof. It concerns one specified slice and constant
  linear combinations, not all slice changes.

## Canonical execution

The [canonical retained capture](verification-pass95-working.json)
is one execution of three unittest suites with one method
each. All three methods passed.

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.double_component_initial_checks_pass95 research.projected_generator_extraction_checks_pass95 research.cubic_quadratic_pencil_checks_pass95
~~~

The execution started at 2026-09-14T16:07:34.066Z and ended
at 16:07:34.688Z. Retained process wall time is
0.615537166 seconds; unittest reported 0.177 seconds.
Exit status is zero. The canonical execution tool chunk
is c09b52.

The complete output hash, using stdout plus one newline
plus stderr, is
11801a403c48cab8e7a95159aa4e8237a03e878211506a094b111c1de1a80dbd.
The capture keeps the empty stdout and full stderr with
all three test names, the method count and OK. All three
input hashes were unchanged during execution.

| Input | SHA-256 |
|---|---|
| [Initial-operator controls](double_component_initial_checks_pass95.py) | ba08d2304141b49c6b23e86cc3624cb67b9757d941ebefad55f3741c99afe51b |
| [Projection and critical-curve controls](projected_generator_extraction_checks_pass95.py) | 5d1b11a2624e504984456e0bdbac4ba774eb8e3493fd4194c827263163dfea16 |
| [Cubic-pencil controls](cubic_quadratic_pencil_checks_pass95.py) | dc59941e7c7ae875a706d80adf2c3b5378a573a6ec5d2bd707b954b1c881d4d1 |

The initial-operator method checks the pencil normalization,
semisimple-replica iterates, a higher-order perturbation
control, the rank-one surface initial, and the appended
weighted third-derivative identity. The projected-generator
method checks both inverse directions, the transported
derivation, the slice projection and the gradient-curve
identity. The cubic method checks the determinant/inverse,
the sharp degree-three versus rejected degree-four frame,
and ideal-power ranks for the two displayed Artin algebras.

There is no additional test method for the global
everywhere-rank theorem or the noncollapsed local-model
theorem. The three methods are finite exact controls,
not proof-assistant certificates of the universal claims.

## Other executions and code reviews

The initial-operator checker had a pre-extension author
run and independent repeats by Jet and General. Those
executions did not contain the final weighted-coefficient
extension. The final author execution e3e54a passed one
method in 0.073 seconds; c09b52 contains this final version.
Jet read the complete final code and extension without
claiming another execution.

General's projection checker passed its author run
0a1763 in 0.098 seconds, and Jet's independent repeat
833313 in 0.102 seconds. These are repeats of one method,
not additional coverage units. Root and Geometry also
read its complete code.

Geometry's cubic checker passed author execution a3698e
in 0.038 seconds under /opt/anaconda3/bin/python.
Two preceding environment attempts failed to import
SymPy before any assertions ran. They were environment
failures, not passing runs and not mathematical
counterexamples. Root and Jet read the complete final
checker; Jet did not execute it.

## Source and retained-dependency scope

The Stacks Project
[tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S)
was checked in its complete displayed statement and proof.
Part (2) supports the coefficient-compatible regular
power-series description. Its full Cohen-structure
dependency tree was not independently reproved.

The Kaliman--Saveliev
[author paper](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf)
was read for the complete Corollary 2.8 statement and
proof. Geometry additionally read the complete displayed
Theorem 2.7 proof. Root's separate theorem extraction
omitted some intervening lines, so it is not recorded
as a complete fresh Theorem 2.7 proof read by Root.
The deeper surface-classification and topological inputs
were not all reconstructed anew.

The whole-irreducible-fiber ramification92 argument is a
retained derived theorem. The rank95 proof explicitly
requires its entire-fiber conclusion to exclude
multiplicity four. Jet, Geometry and Root reread that
saved argument; this is not the same as freshly proving
every primary-source topological input.

The primitive-fiber54, component-degree92, saturated
base-change94 and weighted94 inputs retain their original
scopes. Review of a dependent note does not create a
separate primary-source reconstruction of all of them.

No broad second novelty audit has been completed. Search
results, prior references and the new restricted proofs
do not establish that any statement is historically new.

## Saved-state integrity and remaining work

The 552 frozen records through pass94 were checked at
the start of this pass and again at
2026-09-14T16:18:12.318Z, tool chunk fd23e7.
All matched their retained hashes. The predecessor
checkpoint SHA-256 is
9471dabbf3f9f8b8a8099b7705b8dee6660ab4ece50fbc693bee276c5af6ce2b.

The last historical full regression remains pass75,
146 suites and 1047 methods. Its nine run sources and
six retained output hashes were checked unchanged.
The central historical registry still has 544 claims;
pass95 was not integrated into that registry. No fresh
full regression is asserted.

Current-pass file hashes, equation counts, local links
and output-digest validation belong in the checkpoint
and its separate postsave audit. A matching hash proves
file identity, not mathematical truth. The old proof
files remain frozen; README and the research ledger
are mutable indexes.

The remaining obligations are rank-one fixed-component
control, the original-frame global recognition step,
and the independent reduction from arbitrary sliced
actions. No public posting, submission, external contact,
human expert review, formal verification or cancellation
solution is represented by this packet.
