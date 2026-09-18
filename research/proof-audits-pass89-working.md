# Proof and verification record for homogeneous-speed recognition

The bounded result is the recognition theorem in
[the combined proof](constant-acceleration-relative-slice-descent-pass89.md):
an actual four-variable LND with three time-linear coordinates,
nonzero constant acceleration in the fourth, and a homogeneous relation
among the three good speeds has polynomial three-dimensional kernel.
The unrestricted cancellation conjecture is not proved.

Reviews below are separate AI reconstructions of saved written
arguments. They are not human expert reviews, a Lean proof, a
formal certificate, or a novelty determination.

## 1. Saved-file proof reviews

Each full-file review includes the entire saved proof, not only a
message outline. Shared inherited source theorems remain explicit
inputs; this table does not imply independent reconstruction of
every historical dependency.

| Proof | Equations | Authoring and completed independent reconstruction |
| --- | ---: | --- |
| [Conical unit normal](constant-acceleration-conical-normal-pass89.md) | 8 | General author; Root, Geometry and Jet full-file reviews |
| [Curve-speed normal and commutator](constant-acceleration-curve-speed-pass89.md) | 8 | Geometry author; Root, General and Jet full-file reviews, including the final common-kernel strengthening |
| [Valuation gap](universal-pencil-valuation-gap-pass89.md) | 7 | Root author; Jet, General and Geometry full-file reviews |
| [Whole-divisor pole support](constant-acceleration-pole-support-pass89.md) | 7 | General author; Root, Geometry and Jet full-file reviews |
| [Generic degree one](constant-acceleration-relative-degree-one-pass89.md) | 6 | Jet author; Root, General and Geometry full-file reviews |
| [Combined recognition](constant-acceleration-relative-slice-descent-pass89.md) | 11 | General author; Root, Geometry and Jet final full-file reviews |
| [Binary-normal control](binary-normal-unit-control-pass89.md) | 4 | Jet author; Root and General full proof/code reviews |
| [Pole-order family](generator-pencil-pole-order-control-pass89.md) | 4 | Jet author; Root and General full proof/code reviews; Geometry full proof review |
| [Synthesis](homogeneous-speed-recognition-frontier-pass89.md) | 6 | Root author; General, Geometry and Jet final full-file reviews, including the completed combined dependency |

The critical-point proof was independently reconstructed before
integration, then read in its final six-equation file. It keeps
all original Jacobian identities, works over the generic invariant
field, and derives the nonzero companion derivative from the
actual generation identity. It does not use an unproved
coordinate-volume condition or a global descent premise.

The whole-fiber argument retains the possibly nontrivial residue
field \(k'\), makes its fiber a polynomial line only after proving
the relevant residue of \(Y\) algebraic, and uses tensor nilpotence
of \(h\). Applying that conclusion to poles of \(c\), rather than
only poles of \(h\), is stated explicitly in the final argument.

Root's synthesis reread added the already recognized algebraic-\(Y\)
case before its generic integrality argument. Geometry checked the
saved clarification. This was an assumption-explication change,
not a change to the theorem or its numbered equations.

## 2. Executed finite verification

The [canonical capture](verification-pass89-working.json) was produced
by the [print-only runner](run_targeted_pass89.py). Its UTC interval
is September 14, 2026, 12:34:48.490210 through 12:34:49.042789.
The monotonic total is 0.552434 seconds.

| Standalone suite | Methods | Canonical unittest time | Result |
| --- | ---: | ---: | --- |
| [Binary-normal checker](binary_normal_unit_checks_pass89.py) | 1 | 0.144 s | Pass |
| [Pole-order checker](generator_pencil_valuation_checks_pass89.py) | 1 | 0.030 s | Pass |

The five parameter subtests in the second suite are one test method,
not five proofs of the all-integer theorem. Four input files were
hashed before and after the canonical run and were unchanged.
Both complete outputs are stored with their SHA-256 hashes.
Root and Jet read the runner and capture through EOF; Jet independently
rehashed all four inputs and both outputs without rerunning them.

Earlier actual runs are corroborating executions, not additional
methods: the binary control passed for Jet in 0.147 seconds, General
in 0.138 seconds, and Root in 0.137 seconds. The pole-order family
passed for Jet in 0.030 seconds, General in 0.029 seconds, and Root
in 0.026 seconds. All exited zero.

No fresh full regression or exhaustive action search ran. The
retained full75 evidence remains 146 suites and 1,047 methods,
with nine input hashes and six complete output hashes revalidated.
The historical claim registry remains 544 entries; this packet
does not silently integrate new claims into that registry.

## 3. Primary-source access

Root reread the selected de Bondt Theorem 2.7 statement and displayed
proof through parts (i)--(viii), and Corollary 3.2 with Lemma 3.3
through their displayed proofs, in the retained version-four text.
General and Geometry checked the selected source gates for their
normal and curve arguments; Jet checked the conical normal's
selected theorem earlier in this pass. The deeper Lüroth and
homogeneous-gcd dependencies were not all reproved.

Root freshly checked the entire displayed Dasgupta--Gupta Theorem
3.1 statement and the complete short displayed proof of
Bhatwadekar--Gupta--Lokhande Theorem 3.5. The former reproduces
Wang's result; Wang's original proof was not newly reviewed.
The latter's DVR proposition and PID patching inputs remain inherited.
The actual invariant-coordinate and regular-kernel hypotheses were
checked when those results are used.

For the separate valuation theorem, Root read the complete displayed
statements/proofs at Stacks tags
[09E8](https://stacks.math.columbia.edu/tag/09E8) and
[0AVB](https://stacks.math.columbia.edu/tag/0AVB).
The former is a remark giving the DVR-extension construction.
Other reviewers reconstructed the deduction but did not claim fresh
reads of those original Stacks proofs.

A fresh bounded search was inconclusive on exact-statement novelty.
It does not support a claim that no prior result exists.
Source URLs and selected scopes appear in the individual notes and
the synthesis. Retained source-file hash checks are not counts of
new papers read or full-paper proof audits.

## 4. Integrity and status

The [checkpoint](checkpoint-pass89-working.json) separates this packet
from the 478 predecessor hash records through pass88. Those records
were revalidated before integration. Pass88 and earlier artifacts
remain unchanged; README and the ledger are the mutable navigation
indexes.

The initial critical-point file patch was rejected for a missing
patch-line marker before creating the file, then corrected. A
curve-speed draft reread restored two missing TeX spacing backslashes.
The final whitespace audit also found an explicit TeX backslash-space
at a line ending in the pole-support display; it was replaced by
an explicit quad spacing command. These formatting events did not
change the mathematics. No failed mathematical test occurred in this pass.

The unresolved cases are nonconical rank-two speed geometry and,
separately, the missing reduction from arbitrary sliced actions to
this coordinate frame. The original professor's intended field and
dimension are still unconfirmed. No external message, submission,
publication, expert approval, formal verification, or verified novelty
is recorded. The full goal remains active.
