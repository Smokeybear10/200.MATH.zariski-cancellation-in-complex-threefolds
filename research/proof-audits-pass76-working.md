# Proof and evidence audit for the velocity-cone pass

The eight new written arguments below have separate complete AI
reconstructions within their stated hypotheses. They do not establish
unrestricted cancellation, historical novelty or formal correctness.
The [synthesis](velocity-cone-frontier-pass76.md) retains the full
objective and identifies the remaining no-apex and primitive fixed-point
obligations rather than defining success around these exclusions.

## 1. Previous-turn and current-pass classification

The immediately preceding user check-in was a status response.
Conservatively it is no progress on the mathematical objective, although
live agent handles and a completed saved proof were inspected. This
continuation re-read the working files, revalidated the frozen evidence,
completed further arguments and independently checked their hypotheses.
The current pass is progress, not completion or a verified claim of a
new cancellation theorem.

The deep-research skill and Thomas writing guide were read completely
before this continuation's research and drafting. The workflow led to
fresh selected primary-proof reads and explicit source-applicability
checks. No new request for the already known working format was needed.
The still-unconfirmed complex-threefold interpretation is visible in
the synthesis and README. The original email's dimensional typo has
not been treated as confirmation of a different conjecture.

## 2. Complete written-proof reconstructions

| Saved proof | Numbered equations | Independent review evidence |
| --- | --- | --- |
| [Direct two-invariant conic extension](two-invariant-conic-inverse-obstruction-pass76.md) | 9 | Root and Jet read through EOF and reconstructed the full determinant obstruction, zero axes, parameter-independence step and both inverse gauge orders. General is the author. |
| [Exact triangular f,g pencil](triangular-nice-pencil-classification-pass76.md) | 16 | Root and General read through EOF and reconstructed the arbitrary-coordinate two-jet obstruction, iff criterion, actual positive inverses and all zero boundaries. Jet is the author. |
| [Leading-boundary theorem](nice-leading-boundary-pass76.md) | 8 | Root, Jet and General read the full proof and independently checked augmented rank, homogenization, component purity, the radical ideal and the original linear-invariant endpoint. Geometry is the author. |
| [Linearly triangular original nice action](triangular-nice-primitive-freeness-pass76.md) | 15 | Root, Jet and Geometry read through EOF and reconstructed every actual-coordinate case, slice-evaluation Bezout identity, nonunit first speed and primitive slice. General is the author. |
| [Good directions and apex space](nice-leading-apex-pass76.md) | 7 | Root and General read through EOF and reconstructed generic gradient nonvanishing, the annihilator equality, cone-density descent and the exact dimension alternatives. Geometry is the author. |
| [Variable-direction commuting-slice family](commuting-slice-family-exclusion-pass76.md) | 6 | General and Jet independently reconstructed the entire proof, including the noncoprime normalization, actual inverses, exact goodness product, primitive slices and non-linear-triangular example. Root wrote and self-read it. |
| [Larger f,g,k pencil fixed-point exclusion](triangular-pencil-fixed-point-exclusion-pass76.md) | 15 | Root and General read through EOF and reconstructed the primitive fixed-point normalization, every vanishing order, both nonresonant cases, resonance and the invariant-generator contradiction. Jet is the author. |
| [Invariant omission and transverse gcd](nice-good-direction-invariant-omission-pass76.md) | 7 | Root and General read through EOF and reconstructed the actual coordinate permutation, source independence hypothesis, unique linear invariant, homogenization descent and full-gcd argument. Geometry is the author. |

The eight notes contain 83 numbered equations. The synthesis adds three.
Review means independent mathematical reconstruction of the displayed
arguments, not merely checking formatting or accepting an agent's
confidence. All reviewers are AI agents. No human mathematician or
proof assistant has certified this packet.

General also completed a final full-file scope audit of the synthesis
and this audit, and read the new top76 README and ledger sections plus
the saved targeted JSON. He checked the 83+3 equation total, the
targeted/full-run distinction and all review attributions. No scope,
count or provenance correction was required. This final review adds
no numerical method or mathematical theorem.

Jet initially suggested that the final conic nontriangularity statement
needed a different justification. General pointed out that every
triangular affine-linear frame has its last constant partial in G1,
whereas the conic family has G1=0. Jet explicitly corrected the earlier
objection and checked General's added one-sentence explanation. There
was no resulting theorem correction. The stronger k-pencil conclusion
is fixed-point-freeness, not the smaller family's proportionality iff.

## 3. Selected primary-source scope

The new geometric input is Michiel de Bondt's
[*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3),
arXiv:1501.04845v3, posted October 18, 2017. The retained complete text
and PDF remain unchanged. The new notes cite the exact statements and
printed pages rather than inferring applicability from the abstract.

For the leading-boundary application, Root freshly read the complete
displayed statements and proofs of Lemmas 6.1--6.2, Theorem 6.3 and
Corollary 6.4. Jet and General also freshly read the selected earlier
lemmas and propositions identified in their reviews. The source's
Lemma 6.1 incidence display does not visibly impose membership of the
normalized direction in the image closure. The saved note explicitly
retains that membership in the conical specialization actually needed
by the homogeneous application. It does not certify a broader
nonhomogeneous reading or claim a newly discovered error in the whole
paper.

For the apex scope, Root and General read Definition 3.9 and the full
displayed Corollary 3.10 proof. Its no-apex implication is compatible
with the already present homogenizing hyperplane and supplies no apex
existence conclusion. For invariant omission, Root, Geometry and
General read the complete displayed Theorem 5.1 statement and proof,
including both cases of part (iv). The application uses part (iv),
which allows the one linear invariant actually present. Part (v)'s
no-linear-invariant premise is false and is not invoked.

These are selected primary-proof and hypothesis audits, not a fresh
full-paper audit or a reconstruction of every theorem cited by that
paper. The previously retained original-slice recognition theorems
remain source-dependent. The five family/construction notes use
elementary coordinate and polynomial calculations, without importing
a new classification theorem. The apex row identification is also a
direct argument once the image cone has been supplied.

## 4. Actual finite verification

The standalone [checker](nice_frontier_checks_pass76.py) was written
independently of solver internals and imports only unittest and SymPy.
Root read the final saved file through EOF. General fully reviewed its
initial four methods and independently ran them: four passed in
0.710 seconds, exit zero, command chunk bf849c. Two methods were then
added for the variable-direction family and weighted pencil orders.
General reviewed those additions and reran the final file: six passed
in 0.485 seconds, exit zero, command chunk 445d09.
Jet independently read the complete final six-method checker and the
read-only runner. His checker execution passed all six methods in
0.508 seconds, exit zero, command chunk 8f3437. He did not execute
the runner main or create an additional capture.

Root's initial four-method run passed in 0.442 seconds. The expanded
six-method direct run passed in 0.497 seconds. No failed mathematical
or harness test occurred in these recorded76 runs. These repeats are
not extra methods and do not constitute independent formal proofs.

The [read-only targeted runner](run_targeted_pass76.py) captures actual
subprocess output and checks its exit code, six-method count, success
marker and unchanged source hashes. The canonical
[saved capture](verification-pass76-working.json) started at
2026-09-14T05:55:42.248121+00:00 and finished at
2026-09-14T05:55:43.103716+00:00. It passed six methods in one suite,
with unittest reporting 0.478 seconds and the runner's monotonic
elapsed time 0.855036 seconds. All three tracked inputs were unchanged.
The complete output and its SHA-256 are saved. Root read the runner
through EOF and checked the captured record.

The controls cover actual inverse substitutions, necessary Jacobian
identities, an arbitrary-function two-jet identity, exact leading
divisors and constant kernels in two examples, nonunit content removal,
the added family and the resonant coefficient elimination. The weighted
controls test several explicit orders and higher K terms; the written
argument proves the all-order claim. No finite test certifies the
published component theorem, invariant omission, general nice-action
recognition or unrestricted cancellation.

No full76 regression was run. The latest full record remains the
146 suites and 1047 methods in
[verification75](verification-pass75-working.json), SHA-256
`960cab63db3d427d5e25d142edc2f53b543f9fefd0d55d0b0d17dcd7d0fab247`.
Its two elapsed-clock readings remain as recorded, without a new claim
about their difference. The canonical76 capture is additional targeted
evidence, not a replacement full-run count.

## 5. Preservation and next obligations

A read-only predecessor audit at 2026-09-14T05:55:42.118Z checked
312 prior hash records through75, all nine full75 tracked inputs,
all six retained full75 output hashes and the 544-entry historical
central registry. All passed. The predecessor checkpoint is
[checkpoint75](checkpoint-pass75-working.json), SHA-256
`a6d710084cdcc1ca60ffc2fd3fc304e817291d979d30a265c0fcef2ea55ef45a`.
No pass75-or-earlier artifact, claim registry or experiment manifest
was edited.

The [new checkpoint](checkpoint-pass76-working.json) records current
artifact hashes, equation counts, local-link checks and targeted-run
provenance. Such integrity checks preserve evidence; they do not verify
mathematical truth. README and the research ledger are mutable indexes
and are not retroactively inserted into old frozen packets.

The general primitive fixed-point question remains unresolved outside
the stated construction classes. A unit transverse gcd is not a unit
ideal, an apex relation is not an invariant-coordinate identity, and
the existence of a nice frame for an arbitrary original action remains
unproved. No historical novelty, expert review, formal proof, professor
confirmation, public posting, external message or submission occurred.
The persistent unrestricted objective remains active.
