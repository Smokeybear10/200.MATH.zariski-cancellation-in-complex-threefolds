# Pass74 proof, source, and exact-control audit

This packet records a necessary rank condition for actual nice sliced
actions, an exact boundary example, source-dependent recognition of a
quadratic subfamily, and explicit inverse-degree certificates. It does
not solve unrestricted cancellation, recognize arbitrary nice actions,
or increase the all-profile height threshold beyond ten.

The intervening check-in was a status response with live workers
confirmed, not a new root proof. This continuation produced mathematical
and applicability evidence that changes the next investigation. The
full objective and the unconfirmed complex-threefold interpretation
remain unchanged.

## 1. Saved mathematical arguments

| Artifact | Content | Independent AI review |
| --- | --- | --- |
| [Nice sliced rank exclusion](nice-slice-adjoint-rank-pass74.md) | Fifteen equations; actual adjoints, exclusion of the full nilpotent block, n-variable scope, quadratic source consequence, one-good-direction control and nonslice/localization control. | Root, Geometry and General read the complete saved proof. Root and Geometry also read the entire vertical69 proof; Jet reconstructed that dependency before writing. The final added section received separate changed-section reviews. |
| [Quadratic source scope](quadratic-nice-source-scope-pass74.md) | Eight equations; exact source assumptions, homogenization and strong-nilpotence descent, limited linear-slice degree bound. | Root, Jet and General read the complete saved argument. Root requested correction of the literal n=9 primary restatement and verified the zero-padding clarification. |
| [Affine adapted degree bound](affine-slice-degree-bound-pass74.md) | Eleven equations; actual affine flow and inverse coordinates adapted to the supplied slice, degree bounds max(4,d) and 4d. | Root, Jet and Geometry completed full proof reviews; the previously completed Jet review is not a newly repeated review. |
| [Quadratic projection certificate](quadratic-slice-projection-pass74.md) | Seventeen equations; exact graph and ideal, actual inverse coordinates, degree2/4 bound, non-slice retract control. | Root, Jet and Geometry read the entire saved proof. |
| [Single homogeneous projection layer](single-layer-slice-projection-pass74.md) | Twelve equations; full idempotence, actual flow inverse and degree bound, followed by the sharper constant-action/linear-slice dichotomy. | Root, Jet and Geometry read the full original note. Root and Jet separately checked the final scaling/dichotomy addition. That addition confirms there is no new recognition family. |
| [Nonlinear frontier synthesis](nonlinear-frontier-pass74.md) | Seven equations; remaining nice profiles, exact boundary control, certificate table and unrestricted obligation. | Jet and Geometry completed full saved-file reviews. Geometry requested a wording clarification that becoming nice alone is not sufficient; Root changed this to reduction to a recognized certificate family. |

The author of each separate note also performed a complete self-review.
That is not counted as an independent reconstruction. No review in this
table is human expert review or formal proof verification.

The important original-ring gates were checked explicitly. The nice
argument uses actual coordinate partials that are LNDs on the original
ring, and the vertical lemma uses the actual extension A[s]. Projection
recognition uses the actual slice ideal and both inverse orders. The
graph-image or Jacobian-rank statements alone do not supply coordinates.

## 2. Selected primary-source evidence

De Bondt's [quadratic Jacobian paper](https://arxiv.org/html/1601.00579v4),
Theorem3.2, requires both nilpotence and rank at most two. Root, Jet,
Geometry and General read its full displayed proof; this does not mean
every lemma referenced by that proof was freshly reconstructed. Root,
Geometry and General also read Proposition1.3 and its complete displayed
proof for strong nilpotence and constant triangularization.

The [de Bondt--Sun2018 primary article](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C0C49EEB0C49206F6A2D1065A7DA4B00/S0004972718000345a.pdf/classification_of_cubic_homogeneous_polynomial_maps_with_jacobian_matrices_of_rank_two.pdf),
printed p.90, was accessed by Root, Geometry and General. Item(3)
literally states dimension nine; the lower-dimensional implication is
explained by zero-padding and matrix block descent. Geometry also
accessed the original Sun publisher abstract. The original Sun article
body and proof remained unavailable and are not claimed read. The
independent rank-exclusion route uses the directly checked de Bondt
Theorem3.2 and does not require that unavailable original proof.

Root directly rechecked the domain-and-slice statement as Theorem2.5
in [Dasgupta--Gaifullin](https://arxiv.org/pdf/2306.00510v2). The original
four-variable invariant-coordinate endpoint remains an explicit
published dependency of the retained recognition chain. Geometry
rechecked the nice PID theorem and its exact fixed-coordinate scope;
no new four-variable coordinate is inferred from that hypothesis.

The related Liu--Sun sparse-retract article was located but its full
statements and proofs were not accessed. It is not invoked to establish
either projection certificate, and no novelty conclusion follows from
the bounded search. Unreviewed web research repositories were not used
as mathematical authority. This is a statement-level applicability
check, not a completed historical novelty audit.

## 3. Exact finite execution evidence

The [canonical capture](verification-pass74-working.json) contains
complete combined output, source hashes, output hashes, timestamps,
commands and per-suite exit codes. All three standalone suites passed:

| Suite | Methods | Reported unittest time |
| --- | --- | --- |
| [Affine actual-action controls](affine_linear_adapted_checks_pass74.py) | 2 | 2.350s |
| [Nice adjoint and boundary controls](nice_slice_adjoint_checks_pass74.py) | 3 | 1.610s |
| [Projection controls](slice_projection_checks_pass74.py) | 2 | 0.088s |

The capture ran from 2026-09-14T04:42:12.042829+00:00 to
2026-09-14T04:42:16.690357+00:00, total wall time4.647301 seconds.
Its SHA-256 is
`808a7ceb5c544ac265f35efe297eda78d9ffc25c2b8824cb9a5e3b35ca8025a6`.
All checker sources were unchanged during execution. Root then
recomputed the three output hashes and checked all exit/count records.

Each checker imports only unittest and SymPy, not solver or research
internals. Root read all three checkers completely; Jet independently
read the projection checker and General independently read the nice
checker. Their author and reviewer runs, including earlier versions
of the nice suite and the earlier aggregate capture, are not additional
methods. The saved [affine control scope](affine-linear-adapted-controls-pass74.md)
describes its finite coverage separately from the universal affine proof.

The last full regression is still
[full73](verification-pass73-working.json): 140 suites and1034 methods.
No full74 regression was run, and the new seven methods are not
presented as one fresh combined1041-method full run. These new artifacts
do not modify earlier checker sources. Python compilation of all three
new scripts passed. Git whitespace checking passed but did not cover
the untracked project by itself; the explicit saved-file text scan is
recorded separately in the checkpoint.

Finite examples test identities and failure modes. They do not verify
the written general rank lemma, the full source theorems, universal
coordinate existence, novelty, or any human/formal review condition.

## 4. Integrity and remaining obligations

Root revalidated284 frozen hash records through pass73, including
all ten working checkpoint files64--73 and their listed artifacts,
and the unchanged full60 source records other than the two explicitly
mutable presentation files. The pass73 checkpoint retained SHA-256
`f3116975ea22b144b38a8d0d5a36e51abc0ac1dbc61822265f96e0849cdb3e78`.
The central registry still contains544 claims and remains at full60.
The new packet does not silently update that integrated claim count.

The [working74 checkpoint](checkpoint-pass74-working.json) adds exact
hashes, local-link checks and equation counts for this packet. Hash
integrity verifies file identity, not mathematics. Link anchors and
remote URL availability are not certified by the local-path check.
Later75 drafts are explicitly outside the packet and its seven methods.

The remaining objective is an unrestricted coordinate-existence or
recognition argument. The nice subclass still has residual displayed
profiles(1,2,2,2) or(2,2,2,2), and an arbitrary sliced action has not
been put into any nice frame. The projection certificates do not
eliminate arbitrary higher homogeneous layers. No criterion's
sufficiency is substituted for proof of its universal applicability.

General cancellation, the professor's interpretation, historical
novelty, human expert review and formal verification remain incomplete.
No public claim, submission, external contact or financial action was
made. The active research goal is not marked complete or blocked.
