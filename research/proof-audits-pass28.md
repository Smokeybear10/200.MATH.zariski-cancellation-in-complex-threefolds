# Pass 28: proof reconstruction and verification record

## Scope

This is a private working audit. It distinguishes universal written
arguments from finite symbolic tests, and independent AI reconstruction
from human review. No formal proof, priority certification, or general
cancellation solution is claimed. Professor Luo has not confirmed the
dimension correction or complex-field interpretation.

The main investigator read all four complete notes and all three checkers:

- [Finite transitive Lie recognition](finite-lie-recognition-pass28.md).
- [Fixed translation-frame criterion](translation-frame-pass28.md).
- [Canonical nonunit top-coefficient control](canonical-top-pass28.md).
- [Full changed-invariant surface fibers](changed-fiber-surface-pass28.md).

## Finite algebraic symmetry

A separate investigator reconstructed the integration argument from an
ordered PBW spanning set. Local nilpotence is applied from the rightmost
basis derivation to the left, so each successive finite set has a finite
orbit. This proves a finite stable span for each ring generator, not an
invalid uniform bound on arbitrary products.

Every member, not merely a chosen generating set, is locally nilpotent
in the primary criterion. Engel's theorem then applies to the faithful
finite-dimensional stable representation. The finite exponential/BCH
construction gives a regular unipotent algebraic action.

The source audit checked the full selected statements and proofs of
Kraft--Zaidenberg Theorem 3.1.1(1), Lemma 3.1.3, Corollary 3.1.4,
Theorem 5.2.2, Lemma 5.2.3, and its orbit-tangent result.
It did not claim to have read every page of the manuscript.

The main investigator independently read Milne's Proposition 14.32,
Theorem 14.37 and Theorem 17.64, and Brundan's Lemma 1.1 with its
preceding arbitrary-algebraic-group notation. The dense-orbit criterion
is not restricted by the reductive hypotheses of later results in
Brundan's paper.

The normalizer/right-torsor coordinate construction does not require
the specified cylinder-translation subgroup to be normal. Properness
of that subgroup's action follows from the actual slice and closed
fiber product. The main source audit read the proper-triangular
theorem, the three unnumbered corollaries on printed page 1963,
and the relevant definition in Dubouloz--Finston--Jaradat.

The final unnumbered corollary, not an invented numbered Corollary 0.3,
is the four-dimensional input. The finite-symmetry existence condition
is explicitly equivalent to polynomiality in the sliced-cylinder
setting, so its sufficiency is not a proof of universal existence.

## Fixed-frame recognition and exact negative control

The main proof was independently reconstructed by two investigators.
They checked the nonzero-center argument, preservation of remaining
coordinate translations after restriction, and the fact that all
coordinate changes in this particular criterion can be linear.

The weighted degree proof handles d=0 and d=1. The Jacobi spanning
argument applies to every word, not just repeated adjoints by D.
The word test's large finite size is not called an efficient algorithm.

The main source audit read Petravchuk--Sysak Theorem 2.5 and proof.
One source-scope correction was applied: their general-domain statement
assumes an algebraically closed field. The arbitrary characteristic-zero
polynomial-ring statement is supported separately by the adjoint-LND
and Engel argument, not by overstating that theorem.

The main audit also read de Bondt's Theorem 2.1 and Corollary 2.2 with
their proofs. Their smaller independent-tuple matrix criterion already
tests the same linear triangularization property. No new algorithm
claim was made.

The full nonlinear inverse of the two-dimensional counterexample was
verified in both directions. Its exact five-field algebra is perfect,
contains a non-LND bracket, and is finite-dimensional. This refutes
finite-dimension-implies-linear-triangularization; it is not a negative
cancellation example.

The ten-method checker passed in the author's main run in 0.079 seconds
and in an independent run in 0.075 seconds. The current complete regression
supersedes these timings for the saved checkpoint. Repeated runs are
not counted as extra methods.

## Canonical nonunit-plinth control

An independent investigator reconstructed the full canonical embedding,
the primitive vertical field, both polynomial coordinate inverses, and
the top coefficient in the horizontal slice coordinates.

The initial action has full plinth x², the perturbation is x in its
radical but not divisible by x², and the model is genuinely polynomial.
This removes the unit-plinth limitation of the pass-27 control.

The even/odd localization argument computes full second kernels and
plinth ideals, not just a displayed local slice. The nonsliced primitive
top has an actual fixed locus. Coprime coefficients prevent rational
saturation from producing a regular sliced direction on that orbit line.

The successful physical horizontal partial is retained as a positive
control on the identical canonical model. The failed choice changes
the old invariant plane. Neither failure of all choices nor failure of
every possible Lie-word construction is inferred.

The twelve-method checker passed in the author's run in 0.322 seconds
and the main run in 0.312 seconds. Separate algebra reconstruction found
no mathematical correction necessary.

## Actual global invariant fibers

A separate investigator reconstructed the entire written proof, not
only the completed local model. The main investigator read all six
finite jet formulas and the seven-method checker.

The conductor powers satisfy I^N=d^N B. The exact gluing quotient and
the actual residue parameters at split and ordinary roots are kept.
The proof separates the full affine fiber by lifting idempotents, and
uses nilpotence of I only on the conductor-supported factors.

The main source audit read the full Stacks idempotent-lifting lemma.
Large jet truncation is proved redundant after imposing the invariant
fiber equation. The unit-root changes are finite algebraic operations
inside nilpotent quotients. Thus the displayed node-thickening factors
describe global fiber rings rather than an extrapolation from finite
computer evidence.

The cotangent obstruction covers both multiplicities at least two.
When one is one, elimination gives a fat line. A Chinese-remainder
presentation embeds every finite product of those fat lines in a plane.

The positive controls j=d and j=d(u²-1) matter: they rule out a proposed
universal fiber-only obstruction. All-invariant global generator
exclusion, arbitrary generating triples and ambient realization are not
claimed in pass 28.

The seven-method checker passed in the author's run in 2.458 seconds,
the main run in 2.427 seconds, and the independent run in 2.482 seconds.

## Saved complete execution

The final synthesis received a separate complete cross-read against all
four notes. The audit corrected "nonzero affine-linear" to "nonconstant
affine-linear", corrected Kateryna Sysak's name against the primary
paper, and explicitly scoped the surface classification to closed fibers
over complex values. These corrections were applied before the final
integrity checkpoint. No checker source or mathematical formula changed.

The saved full regression ran from 2026-09-13 08:58:24 UTC to
2026-09-13 08:59:47 UTC. All 634 methods across 52 suites passed.
The new suite counts are 10, 12 and 7, totaling 29. All 605 preceding
methods were rerun. The five orchestration parser controls and repeated
executions are not added to the mathematical method count.

An earlier successful full run from 08:54:02 to 08:55:26 UTC was observed,
but its output was not captured as a file. The later run above is the
actual saved evidence, not a reconstruction of the earlier timings.

The checkers import only SymPy and unittest. They independently compute
finite identities without importing solver internals; that separation
does not turn them into a proof assistant or universal exact checker.

See [the saved execution](../verification-pass-28.json),
[the reproducible runner](run_regression_pass28.py), and
[the structural integrity log](../consistency-pass-28.json).
The latter checks hashes, syntax, counts, links, flags and numbering,
not mathematical validity.

No external contact, publication, submission, payment, new user-owned
task or automation occurred. A comprehensive novelty audit and specialist
review remain necessary before any originality claim.
