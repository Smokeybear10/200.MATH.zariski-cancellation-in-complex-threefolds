# Proof and verification audit for the invariant-plane pencil packet

This audit separates written arguments, independent AI reconstructions,
finite exact checks, and imported source assumptions. None is human
expert review or a formal proof of general cancellation. The persistent
goal and the unconfirmed corrected complex-threefold interpretation
remain unchanged.

## Written proof reviews

| Artifact | Content | Completed review scope |
| --- | --- | --- |
| [Invariant plane](constant-acceleration-invariant-plane-pass88.md) | 11 equations: actual highest LND, intrinsic polynomial plane, unit speed row, module completion and relative generators. | Jet author; Root, General and Geometry full independent EOF reconstructions. |
| [Universal pencil](universal-generator-pencil-pass88.md) | 9 equations: field descent, transcendental branch recognition, tensor-annihilator argument and cusp boundary. | Jet author with Root proposals; Root, General and Geometry full saved-file reviews. General also independently supplied the transcendental strengthening. |
| [Laurent control](nonintegral-generator-pencil-control-pass88.md) | 4 equations: universal pencil with nonintegral slope and exact tensor agreement. | Root construction; Jet author; Root and General full proof/code reviews and independent runs. |
| [Normal-ring control](normal-generator-pencil-coordinate-boundary-pass88.md) | 6 equations: polynomial three-rings, S-flat cylinder, nonintegral slope and explicit failed-coordinate fiber. | Root construction; Jet author; Root, General and Geometry full independent proof/code reviews. Root and General ran it independently. |
| [Generic degree](constant-acceleration-generic-degree-pass88.md) | 6 equations: nonzero velocity determinant forces equal fraction fields. | Geometry author; Root, General and Jet full saved-file reconstructions, with source scope below. |
| [Conical good direction](constant-acceleration-conical-good-direction-pass88.md) | 7 equations: original last partial is good, common highest line and conditional normal-row reduction. | General author; Root, Geometry and Jet full independent EOF reviews. |
| [Global volume descent](constant-acceleration-volume-descent-pass88.md) | 6 equations: actual volume coefficient gives global Omega h in S+SA_1+SA_2. | Jet author with Root refinement; Root, General and Geometry full independent reconstructions. |
| [Source gate](pencil-descent-source-gate-pass88.md) | 2 equations: relative weak-normalization terminology versus missing integrality and faithful flatness. | Root author and full EOF review; Geometry independent full EOF review with fresh selected primary reads. |
| [Synthesis](invariant-plane-pencil-frontier-pass88.md) | 7 equations: scope, deductions, controls and outstanding obligations. | Root complete read and corrected-delta review; Jet independent full EOF review of the synthesis, runner and capture, including six input and four output hashes. |

The total is 58 numbered equations in nine mathematical/source notes.
The volume proof's positive coefficient with du last and the localized
Jacobian proof's negative coefficient with u first agree after changing
orientation. This sign was reconstructed independently, not inferred
from an example.

## Exact tests and captured evidence

The print-only [runner](run_targeted_pass88.py) executes four independent
files, each containing exactly one unittest method. It writes no saved
capture itself. Each checker imports only unittest and SymPy, not the
research proofs, another checker or a solver.

| Suite | Author/initial execution | Separate execution |
| --- | --- | --- |
| [Cusp pencil](universal_generator_pencil_checks_pass88.py) | Jet 0.065 s, chunk 799a41. | General 0.033 s, b469b7; Root 0.032 s, 5644e2. |
| [Laurent pencil](nonintegral_generator_pencil_checks_pass88.py) | Jet 0.029 s, b0121c. | Root 0.028 s, 988208; General 0.027 s, 165b91. |
| [Normal-ring pencil](normal_generator_pencil_checks_pass88.py) | Jet final 0.027 s, cef94f. | Root 0.029 s, db9f40; General 0.032 s, c771a9. Jet's later 0.027 s, 6b8826, is an author repeat. |
| [Volume coefficients](constant_acceleration_volume_checks_pass88.py) | Root 0.089 s, 90d916. | Jet 0.090 s, 5f7731, after complete independent code review. |

The [canonical capture](verification-pass88-working.json), tool chunk
df22c3, began at 2026-09-14T12:00:18.844979+00:00 and ended at
12:00:19.333909+00:00. It passed four suites/four methods in
0.488809 monotonic seconds. The per-suite unittest times were
0.027, 0.025, 0.023 and 0.084 seconds. All six tracked inputs were
unchanged, and all four complete outputs have saved SHA-256 values.
The immediately preceding runner invocation, e6eda1, also passed;
it is a diagnostic repeat, not four additional methods or the
canonical saved capture.

These methods check finite exact identities and algebraic boundaries.
The volume suite computes coefficients for a formal polynomial matrix;
it does not assert that every such matrix comes from an action.
The normal-ring example explicitly fails the original-coordinate
hypothesis. Neither these controls nor the written lemmas prove
unrestricted recognition.

No full regression or exhaustive action search was executed. The last
full regression remains the preserved
[pass75 capture](verification-pass75-working.json): 146 suites and
1,047 methods. The central registry remains 544 historical claims;
pass88 has not been silently added as formally certified claims.

## Source scope

The invariant-plane proof uses the complete retained intrinsic-quotient
argument and its Kaliman--Saveliev gates. During development of this
packet, Root freshly checked the selected original Lemma 2.1 statement,
Theorem 2.7 displayed proof and Corollary 2.8 displayed proof; this was
not an audit of every topological dependency. General and Geometry
reconstructed the retained application. No quotient-fiber smoothness,
reducedness, connectedness or freeness was inferred.

For Quillen--Suslin, the original publisher metadata and the exact field
case were checked during packet development. Jet and Root read the
complete terminal Theorem 6 argument in Dicks's accessible write-up.
The original 1976 papers and every intermediate dependency were not
fully re-audited. Only freeness over the actual polynomial plane is used.

For the generic-degree criterion, Root and General freshly read the
retained de Bondt 1501.06046v4 text around Corollary 3.2 and Lemma 3.3,
including their complete displayed proofs and the relevant Theorem 3.1
implications. Geometry's selected primary read additionally checked
the arbitrary-field statement of Theorem 1.1. Jet reconstructed the
application against the retained exact statement without claiming a
fresh de Bondt proof read. Classical Luroth and every earlier dependency
were not newly reconstructed.

Root and Geometry freshly read da Silva v7's introduction, Definition
1.5 and the localization example, and Vitulli's Definitions 3.3, 3.4
and 3.7. The exact primary URLs and dates are in the
[source note](pencil-descent-source-gate-pass88.md). The former permits
a general relative definition; the latter explicitly assumes integrality.
No contraction theorem or global integrality result was imported.

The current source-file audit retains the 20 predecessor source files
and adds hash accounting for the already present versioned de Bondt
1501.06046v4 PDF and extracted text. These are 22 file checks, not
22 newly read papers. The two weak-normalization sources were accessed
online with exact links; no locally checksummed copy is asserted.

## Corrections and preservation

Jet's first normal-control run failed a structural comparison between
equal expanded and factored SymPy expressions. The comparison was
corrected to test the expanded difference; no mathematical identity
changed. This failure and its passing final runs are retained explicitly.
Root's synthesis EOF read caught a plus-joined line and lost TeX spacing
backslashes, which were repaired before final review. Its draft source
title was corrected to the exact C+-actions title. The source note was
also clarified so the C-algebra notation applies only to the actual
complex-algebra application, not every characteristic-zero domain.
Jet's two precision suggestions were applied: the tensor factor is
proved invertible in the annihilator quotient, without excluding
invertibility before quotienting in special cases; the Omega-zero
locus includes the identically-zero case and is not always a divisor.

The frozen predecessor audit at 2026-09-14T11:50:11.110Z verified 461
records through pass87, together with the retained full75 accounting.
No predecessor artifact was modified. The
[checkpoint](checkpoint-pass88-working.json) adds current file hashes,
equation counts, local-link checks and complete-output accounting.
Those integrity checks are not mathematical proofs.

The first integrity orchestration attempt stopped at a JavaScript
template-string syntax error before execution. A corrected read-only
harness then falsely matched the legitimate expression z(p)+q as a
joined Markdown link; its matcher was narrowed to Markdown filenames.
Neither event changed a mathematical file or invalidated a test result.

An additional conical-normal-row deduction was started separately as
pass89 while this packet was integrated. It is not included in this
packet's proof, method or artifact counts. No public novelty claim,
expert review, formal certification, external contact or submission
occurred. The full goal remains active.
