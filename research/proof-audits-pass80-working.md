# Proof and verification audit for nice-slice recognition

The mathematical change in this packet is recognition of every nice
sliced action on the actual complex polynomial four-ring. The full
complex-threefold cancellation conjecture remains unproved. The previous
user check-in was status only, conservatively classified as no progress;
this continuation revalidated the worktree and completed new proofs and
finite exact checks toward the unchanged unrestricted objective.

## 1. Written proof inventory

| Note | Author | Numbered equations | Completed independent written reconstructions |
| --- | --- | ---: | --- |
| [No-apex quadratic cone](nice-no-apex-quadric-pass80.md) | Geometry | 10 | Root, General and Jet, complete EOF; final elementary source-dependency refinement separately read by Root. |
| [Explicit Segre frame](quadric-segre-frame-pass80.md) | Root | 10 | General, Geometry and Jet, complete EOF. |
| [Quadric recognition](nondegenerate-quadric-nice-recognition-pass80.md) | General | 13 | Root, Geometry and Jet, complete final Segre-version EOF. |
| [Parameter controls](normal-row-parameter-boundary-pass80.md) | Jet | 10 | Root and General reconstructed the complete parameter and formal-determinant proof; Root and Geometry additionally read the final Segre-method update. |
| [All-nice recognition](nice-slice-recognition-pass80.md) | Root | 4 | General, Geometry and Jet, complete EOF and exhaustive-case scope. |

There are 47 numbered equations in these five notes. Independent here
means separate AI derivations and source-hypothesis checks, not human
expert review or a formal proof kernel. No reviewer was asked merely to
accept a green test or another reviewer's conclusion.

Geometry's cone argument was checked at each incidence gate: the generic
points lie on no other zero-set component; finitely many projective lines
pass through each point of a non-conical surface; every covering Fano
component has generic incidence degree one; the pair-incidence premise
forces two covering components; and three pairwise skew lines give an
explicit determinant quadric. Smoothness of the projective surface is
a conclusion. The affine quadric cone is still singular at its vertex.

The Segre construction was checked with actual UFD division and two
unit-ideal Bezout identities. Gcd one is not replaced by a unit ideal.
The four-by-four inverse is polynomial over the actual common plane S,
but is not called an ambient coordinate change before generation has
been proved. The final endpoint no longer uses Quillen--Suslin or an
algebraic extension of Frac(S).

The recognition determinant was reconstructed with all coefficients
differentiated before row operations. Its constancy is proved in the
actual quotient by conormal exactness and the original differential
basis, not assumed from formal matrix algebra. The affine saddle field
is not an LND. Its irreducible eigenpolynomials are classified over
Frac(S); the actual generic polynomial line excludes the hyperbola.
The last globalization uses every closed fiber as a nonempty curve.

## 2. Finite checks and exact retained evidence

The final [checker](normal_row_parameter_checks_pass80.py) imports only
unittest and SymPy and contains four methods. Root read the complete
three-method version and the entire added fourth method before running
the final version. The new [runner](run_targeted_pass80.py) was read
completely by Root and Geometry. It only prints a fresh JSON result;
it does not overwrite saved captures.

The [canonical targeted capture](verification-pass80-working.json)
ran four methods in one suite, passed with exit zero, and retained the
complete output and its SHA-256. Its start and end were
2026-09-14T08:40:41.136520+00:00 and
2026-09-14T08:40:41.890271+00:00. Monotonic elapsed time was
0.753500 seconds; unittest reported 0.407 seconds. Three input hashes
were identical before and after execution.

The checker SHA-256 is
`c77a2ebbf789ad6e161abd0d434cc84c7f23575848200a7a7bdfa680712f55bf`.
The retained canonical output SHA-256 is
`291cbfe59588110442a1a6730488a4f75dd6c008bca64509801b9a44a8c56898`.

The methods cover the two parameter rows and their proper primitive
normal ideals, the false derivative matrices and their exact
mixed-partial failure, the formal generation determinant and saddle
matrix, and an explicit polynomial Segre-frame inverse. The tests do
not certify the Fano-incidence argument, the universal Darboux-curve
classification, the original-coordinate generation hypotheses, or
general cancellation.

Jet's final four-method author run passed in 0.392 seconds. General's
independent 0.337-second run was of the earlier three-method version,
not the final four-method file. He subsequently read the complete final
four-method checker and ran it successfully in 0.378 seconds, exit zero,
tool chunk a80e17, with the final checker hash matching. Geometry and
Jet separately read the full final runner without executing it.
Root also reran the unchanged four-method
pass79 checker in this continuation; it passed in 0.197 seconds, exit
zero, tool chunk 258e4f. These reruns do not create additional methods.
There were no failed test runs in the supplied evidence.

No full80 regression ran. The preserved full75 record remains 146 suites
and 1047 methods. The targeted80 result is not silently added to that
historical full-run count. The central claim registry remains the
historical 544 claims and was not integrated or rewritten in this pass.

## 3. Primary sources and precise review scope

The deep-research workflow directed a fresh primary-source investigation
of the no-apex case. The useful input is de Bondt's Theorem 3.8(i),
not the previously used containing-hyperplane conclusion.[^bondt]
Root read the complete displayed Theorem 3.8 statement and proof,
Definition 3.7, Lemmas 3.1--3.4 with proofs, and the selected later
zero-set statements and proofs. Geometry's broader selected reading
and General's complete Theorem 3.8 reading are separately documented
in the cone note and review messages. This is not a fresh audit of all
references cited by that paper.
Jet also freshly read the complete displayed Theorem 3.8 and Lemmas
3.1--3.4 proofs, with Definitions 3.7 and the intervening 3.5--3.6
material. His source review does not claim a fresh Cid or whole
Kaliman--Saveliev audit.

The final no-apex proof explicitly avoids the later classification of
other zero-set components, Corollary 6.4 and its Lemma 6.1 input.
Homogenized rank, the slice-implied unit velocity, the highest flow
coefficient and the dimension bound already make the image cone a
zero-set component. Only the finite number of other components is used.
The apex-space identity likewise needs only the rank-three annihilator,
the image equation and homogeneity. This materially reduces the source
dependency without changing the ten-equation conclusion.

Root freshly read the full displayed conormal lemma proof.[^conormal]
Its general statement does not assert injectivity; the actual
irreducible hypersurface and domain provide that here. The intrinsic
quotient-plane and flat-fiber inputs remain the explicitly checked
cylinder application of Kaliman--Saveliev in the retained note.[^ks]
Root reread that complete saved applicability note in this pass, not
all primary topological and surface-classification proofs afresh.

Root, Geometry and General each read the selected Lemma 5.3 and
Theorem 5.4 proofs and Section 6.4 of Cid's 2026 preprint.[^cid]
This source supplies a nearby linearization/conjugacy criterion, not
universal four-variable nice recognition. The associated multiplicative
action in this packet is linearized directly by the now-polynomial
kernel and original slice, so it does not depend on that preprint.
The landing-page submission date and different HTML heading date are
both retained in the synthesis. Broad web queries were noisy and do
not justify an exhaustive novelty conclusion. Unreviewed online proof
claims were not used as theorem inputs.

## 4. Countercontrols and corrections

The two parameter rows have primitive normal zeros whose lowest terms
span at most two dimensions. They disprove a parameter-only inference
from the old local bound to a unit normal. Their formal matrix products
also satisfy rank and nilpotence identities, yet their proposed
original partials neither commute nor remain locally nilpotent.
They are not actual actions or cancellation counterexamples.

The main proof's initial abstract module completion was replaced by
Root's explicit Segre factorization. Three transcription defects in
the initial endpoint were corrected before final review: two stray
plus signs and a missing TeX backslash. The cone-note title was changed
to avoid calling the singular affine cone nonsingular. These are not
failed theorem tests or concealed mathematical counterexamples.
The first read-only integrity harness over-escaped its equation-tag
regular expression and consequently reported zero tags. The harness
was corrected without changing any proof or checker; this was not a
mathematical test failure.

## 5. Integrity and the remaining goal

The fresh predecessor audit at 2026-09-14T08:34:11.569Z passed 370
historical hash records through79, all nine tracked full75 inputs,
six retained full75 outputs and the unchanged claim count. The
pass79 checkpoint SHA-256 remains
`527d0ef2f5d0bf19aff4dd28fb7af4706dc16c482a5c1006fca682998ba269fa`.
The [checkpoint80](checkpoint-pass80-working.json) records the final
current-file hashes separately. Hash checks establish file integrity,
not mathematical truth. The project is untracked in the parent git
worktree, so a clean git diff check alone would not cover its contents.

All files through79 remain frozen. README and the research ledger
receive a new latest-result section without rewriting their historical
entries. The next mathematical task must leave the now-recognized nice
class: find an actual nice frame for a general cylinder action, a valid
frame-reduction step, or another recognition argument for non-nice
actions. Niceness is not inferred from local nilpotence.

The professor has not confirmed the corrected complex-threefold
interpretation. General cancellation, universal nice-frame existence,
historical novelty, human expert review and formal verification remain
unproved or incomplete. No external contact, submission or public
posting occurred. The unrestricted persistent goal stays active.

[^bondt]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3), arXiv:1501.04845v3, October 18, 2017, Definition 3.7 and Theorem 3.8(i). The retained PDF/text and exact selected reading scope are linked in the cone proof.

[^conormal]: The Stacks Project, [Lemma 10.131.9, Tag 00RU](https://stacks.math.columbia.edu/tag/00RU).

[^ks]: Shulim Kaliman and Nikolai Saveliev, [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf), with exact cylinder applicability in [intrinsic-quotient-surface-pass.md](intrinsic-quotient-surface-pass.md).

[^cid]: Luis Cid, [*On nice Gm-actions arising from locally nilpotent derivations with slice*](https://arxiv.org/html/2604.03471v1), arXiv:2604.03471v1, selected Theorem 5.4 and Section 6.4; submission and HTML dates are distinguished in the synthesis.
