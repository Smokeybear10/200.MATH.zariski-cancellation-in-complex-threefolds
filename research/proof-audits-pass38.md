# Pass 38 process and proof audit

## Outcome and scope

The original complex threefold cancellation conjecture is not solved.
The supplied whole-frame theorem and the fixed-model vanishing-divisor
criterion have complete written arguments and separate AI reconstructions.
The main [report](../deep-pass-38.md) states the hypotheses and unresolved
existence step. The [claim registry](../claims.json) records Z355-Z361.
Novelty, human expert review, full formalization and professor confirmation
remain false.

This pass returned from the completed rank-two Su candidate family to the
actual single-line cylinder. It did not assume a higher-rank source cell
with several stabilizing variables satisfied that hypothesis.

## Whole-frame proof reconstruction

The general-affine agent developed the simultaneous-frame argument and the
non-quasi-translation projective-image branch. The root supplied the
homogenization closure for the quasi-translation case, retaining the extra
Jacobian column. Both directly read de Bondt's Proposition 2.5 and
Theorem 3.6(i),(iii), including the applicable dimension-five proof.
The fixed-coordinate regular-kernel theorem was checked at statement and
proof level, not inferred from the paper's abstract.

An early exploratory coefficient argument purported to make the Jacobian
rank one. Mixed commutator terms invalidate that assertion, and it was
discarded before entering the saved theorem. The final proof instead uses
the correct augmented rank, a nilpotent cyclic chain, and the projective
orbit line or homogeneous quasi-translation theorem.

The root then removed a needless dependency from the higher-rank branch.
Every first commutator centralizes E and therefore restricts directly to
the kernel. A relation among its restrictions lifts to a multiple of E,
contradicting ambient independence. The author and both reviewers checked
this replacement. The completed proof needs no pass-35 homogeneous-space
criterion, Brion stable-open theorem or separable-form descent.

The jet and geometry agents independently read the complete theorem,
source gates, checker and revised direct descent. Both found no remaining
mathematical gap. Geometry's detailed reconstruction is saved in
[actual-frame-audit-pass38.md](actual-frame-audit-pass38.md).
The root independently checked the explicit rank-three invariant-coordinate
example by exact symbolic differentiation and determinant calculation.
That scratch control adds no unittest methods.

## Vanishing-divisor proof reconstruction

The jet agent completed the p(0)=0 branch and its standalone checker.
The root, geometry and general-affine agents independently read the
complete proof and the predecessor's exact recognition theorem.
Each reconstruction retained the actual polynomial inverse requirement.

The audits specifically checked:

- Primitivity forces Q0 nonconstant; the zeroth-order parity equation
  forces g0=0 and fixes the reduced W.
- The e=1 Taylor error has order three before dividing by x and hence
  cannot contribute to the retained first jet.
- Comparing every U with U* by injectivity of substitution T to -b²
  accounts for all correction terms, not a selected ansatz.
- The all-degree even equation forces linear Q0 and the exact g1 slope;
  the odd equation removes the remaining first-jet correction.
- CRT modulo x^(e+2) and the full u retains repeated-root multiplicities.
- The all-e explicit family has both physical inverse divisibilities,
  not merely an invertible matrix on a localized auxiliary plane.

No mathematical correction was requested for that proof. All reconstructions
preserve its fixed polynomial-normal-form scope and the distinction between
the common-local-slice factor p and the full primitive-top plinth ideal.

## Sources and retained inputs

The deep-research skill was used for a cited private Markdown synthesis
and this separate process record. The writing guide was read before
drafting. There was no material format or scope choice requiring another
clarifying question. No PDF or externally submitted document was authored.
The primary PDFs were read semantically; no new visual-layout claim was
based on them.

The geometry audit checked fixed-coordinate recognition, retract theorems,
intrinsic-slice characterizations and the August 20, 2026 binomial-retract
revision. The root directly read the decisive de Bondt, BGL, sparse-retract
and kernel-retract passages and proofs, including the dimension-two
retract theorem. The larger classification and earlier patching theorems
remain cited mathematical dependencies, not machine-verified results.

Four versioned PDFs and their extracted texts are retained:

- de Bondt, arXiv:1501.04845v3.
- Bhatwadekar, Gupta and Lokhande, arXiv:1501.01438v1.
- Chakraborty, Dasgupta, Dutta and Gupta, arXiv:1910.11023v1.
- Chakraborty and Pal, arXiv:2504.14382v2.

All four ordinary public downloads and text extractions succeeded.
Poppler reported a font-type mismatch warning for the sparse-retraction
PDF; extraction exited successfully, and the retained decisive theorem
and version text match the web reader. The warning is not concealed as
a failed mathematical check. Earlier web-reader attempts at a de Bondt
mirror timed out or returned access denial; arXiv supplied the source.

The source audit is targeted, not an exhaustive priority review of
MathSciNet, zbMATH, theses or unpublished expert work. A generated web
result encountered in broad searching was not used as theorem evidence.
The individual derivation's coordinate rank was explicitly distinguished
from the generic rank of all intrinsic LNDs.

## Actual exact-check executions

Both new suites import only unittest and SymPy, with no solver or project
imports. The root and reviewers read the complete checker sources.
The following are actual direct runs, not estimates:

| Execution | Frame methods / time | Vanishing-divisor methods / time |
| --- | --- | --- |
| Author's first passing run | 6 / 0.150 s | 8 / 3.605 s |
| Root direct run | 6 / 0.147 s | 8 / 3.682 s |
| Jet independent frame audit | 6 / 0.145 s | Author of the eight-method suite |
| Geometry independent audit | 6 / 0.142 s | 8 / 3.662 s |
| General-affine independent integrability audit | Author of the six-method suite | 8 / 3.602 s |

The frame author's initial invocation caught an unparenthesized generator
expression before tests ran. After that syntax fix all six methods
passed. An unchanged author rerun after the proof-only descent revision
also passed in 0.152 s. The vanishing-divisor suite passed on its first
run without an assertion or mathematical correction.

The complete regression actually ran from **2026-09-13 13:36:14 UTC**
through **2026-09-13 13:37:41 UTC**. All **824 methods in 80 suites**
passed. The new suite durations in that run were 0.142 s and 3.711 s.
The completed output was captured directly and saved as
[verification-pass-38.json](../verification-pass-38.json).
No timing was reconstructed from an approximate wall-clock recollection.

Repeated runs, the scratch direct-restriction identity, five runner-parser
controls and two integrity-link-parser controls add no unittest methods.
These are finite exact controls. They do not prove the external
classification, all-order general quantifiers, novelty or frame existence.
Agreement among AI reconstructions is not human expert review or Lean
verification; test counts are not probabilities of correctness.

## Final synthesis corrections and integrity

The report's first draft had escaped-spacing transcription errors in
several displayed formulas, corrected before the independent final audit.
The geometry reviewer caught two additional concise-summary errors:
the orbit is dense in the projective line, and the intrinsic retraction
criterion requires a nonzero LND. The jet reviewer independently caught
the same issues and two further precision errors: only the curve map's
difference from T has nilpotent coefficients, and at e=1 the error-order
lower bound, not necessarily the actual error, equals e+2. All four
were corrected. The full underlying proofs retain the correct statements.

One metadata patch failed because its context omitted a trailing comma;
one README patch failed due to a malformed fenced-block patch line.
Both failures were atomic for the affected files. Corrected patches
succeeded without removing unrelated content. Neither failure changed
the mathematical tests or their saved output.

The current read-only integrity command checks contiguous claim IDs,
all status flags, AST method counts, independent imports, every recorded
suite command in README, local links, equation and footnote numbering,
whitespace and SHA256 hashes of artifacts, suite sources and retained
primary inputs. Its output is stored separately as consistency-pass-38.json.
The first integrity invocation correctly rejected a forward link to this
not-yet-created output; the audit now names that generated file without
a premature link. No mathematical test failed.
Those checks establish record consistency, not theorem validity.

No external contact, email, public posting, submission, paid access,
credentials, new user-owned task or automation was authorized or performed.
The next mathematical work must address an actual coordinate-preserving
height-reduction argument or another justified existence step. It should
not repeat the completed fixed-model decision without identifying a defect.
