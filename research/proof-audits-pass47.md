# Independent proof and source audits for pass 47

This records the bounded independent reviews completed by
`geometry_audit17` on 13 September 2026. These are AI-agent
reconstructions and exact finite tests, not human expert review,
publication, proof-assistant certification, or a proof of the
unrestricted cancellation conjecture. No frozen mathematical file
or shared metadata was edited during this final audit.

## 1. Complete proof reviews

The following five notes were read completely and reconstructed
independently of their authors.

| Note | Exact points checked | Verdict |
|---|---|---|
| [Second-image closed fiber](second-image-closed-fiber-pass47.md) | Socle lifts in the actual local ring, invariant subtraction, faithful-flat regular-sequence cancellation, converse monic basis including nilpotents | Clean |
| [Second-image vector bundle](second-image-vector-bundle-pass47.md) | Finite denominator bound, actual height-one intersection, reflexivity and local freeness, unimodular constants, full section ideal with multiplicities, unit factor and exact conic kernel | Clean |
| [Flat conic and topology](flat-conic-topology-gate-pass47.md) | Unit-content module argument, flat height-one intersection without a finite-generation assumption, actual generation in the unit-linear case, full fiber, and the distinction between full and reduced plinth | Clean |
| [Smooth-plinth recognition](smooth-plinth-recognition-pass47.md) | Actual invariant-plane rectification, parallel components, square-completion signs, repeated-root singularity, normalized-cover input, CRT and both polynomial inverse directions | Clean |
| [Second-image countercontrol](second-image-countercontrol-pass47.md) | Actual presentations and action, smoothness, prime localization and kernel, faithful flatness, all-degree filtration, low-degree basis, nonreduced fibers, fixed scheme and Euler obstruction | Clean |

For the vector-bundle note, the multiplier identifying the two
rank-one ideals is understood in the direction
\((a,b)R\to pJR\). Constants split globally because the
quotient bundle is projective over the affine invariant plane.
These are explanatory details, not changes to its proof.

The geometry reviewer authored the remaining two notes, so this
record does not count rereading them as independent self-review:

- [Image-ideal source scope](image-ideal-source-scope-pass47.md).
- [Intrinsic pointwise plinth](intrinsic-pointwise-plinth-pass47.md).

`general_affine17` subsequently reported complete independent
algebra/scope reviews of both, followed by a complete cross-read
of the inherited pass-17 peripheral-cycle proof through its end.
That review found no correction. This is an attributed record
of the other agent's completed review, not a claim that the
reviewer newly accessed every literature source in the source note.

## 2. Exact independently observed test runs

The geometry reviewer read every line of each of these three
standalone checkers, then invoked it directly with
`/opt/anaconda3/bin/python` from the project root. All imports
are limited to `unittest` and SymPy. There are no project-solver
or research-package imports.

| Checker | Methods | Observed unittest runtime | Result |
|---|---:|---:|---|
| [flat_conic_gate_checks_pass47.py](flat_conic_gate_checks_pass47.py) | 2 | 0.031 s | Passed, exit 0 |
| [second_image_countercontrol_checks_pass47.py](second_image_countercontrol_checks_pass47.py) | 5 | 0.211 s | Passed, exit 0 |
| [smooth_plinth_recognition_checks_pass47.py](smooth_plinth_recognition_checks_pass47.py) | 3 | 0.856 s | Passed, exit 0 |

These are ten methods in three existing new-pass suites, not
additional methods created by rerunning them. The times are the
unittest-reported times from the geometry reviewer's own runs.
The countercontrol's bounded ideal comparison covers degrees
zero through eight; its universal all-degree assertion is proved
in the note by the saturated associated-graded argument.

No finite test is represented as proving flatness for all modules,
the peripheral-cycle theorem, an embedding theorem, monodromy,
factoriality, or the unrestricted coordinate-frame existence claim.
Repository-wide regression and integration are handled separately
by the root agent; no unobserved full-regression count is asserted
in this record.

## 3. Primary sources directly inspected and access limits

The geometry reviewer directly read the relevant statements and
complete proofs in these sources during the pass:

- [Kaliman's final 2004 author PDF](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf):
  the exceptional factorization, finiteness argument and retained
  quotient geometry used in the pointwise transfer. The transfer
  is a written deduction from that geometry, not a verbatim
  published theorem about the second-image ideal.
- Stacks [0AVB](https://stacks.math.columbia.edu/tag/0AVB) and
  [0B3N](https://stacks.math.columbia.edu/tag/0B3N): the precise
  finite-module and regular-surface hypotheses in the bundle proof.
  Also [01V9](https://stacks.math.columbia.edu/tag/01V9),
  [03GV](https://stacks.math.columbia.edu/tag/03GV), and
  [0AFU](https://stacks.math.columbia.edu/tag/0AFU) for the
  smooth-fiber, normalization and prime-localization steps.
- [Vistoli, arXiv:math/9904035v3](https://arxiv.org/pdf/math/9904035v3):
  the complex Suzuki–Abhyankar–Moh statement and proof on page 2,
  and supporting Theorem 1 and its proof. This is an actual plane
  embedding theorem, not a stable-coordinate theorem.
- [Cappell–Maxim–Shaneson](https://people.math.wisc.edu/~lmaxim/Euler.pdf),
  printed page 410, including its footnote: the exact Euler
  mechanism used for the weak-hypothesis example.
- [Dasgupta–Lahiri v6](https://arxiv.org/html/2302.13787v6),
  24 July 2026: the introduction, relevant definitions and
  filtration statements, and the statements and proofs of
  Theorems 4.1, 5.2 and 5.9. Their relative-coordinate
  assumptions were compared with the unknown intrinsic ring.

The current publisher abstracts for
[Ben Khaddah–El Kahoui–Ouali](https://link.springer.com/article/10.1007/s00031-022-09705-z)
and [El Kahoui–Labtaini–Ouali](https://link.springer.com/article/10.1007/s00031-026-09969-9)
were directly read. Their full original texts were not available
through the checked subscription-only routes. Accordingly, no
full-proof access is claimed; the first result's theorem numbering
and all-image formulation are additionally attributed through the
explicit v6 citation. The 2026 factorial-domain abstract explicitly
assumes freeness.

The current [Daigle arXiv:2009.14800 record](https://arxiv.org/abs/2009.14800)
was read with its withdrawal and proof-error notice. The retained
all-ranks abstract is not used as a theorem. No unsuccessful search
is treated as evidence of historical novelty or a complete proof
that no other theorem exists.

## 4. Synthesis audit

The complete 356-line initial version of
[deep-pass-47.md](../deep-pass-47.md) was read against all seven
new notes. All 22 tagged equations, the quadratic normalization,
conic signs, determinant-one inverse, all-degree control formula,
and topological versus algebraic boundaries were reconstructed.

Two local-notation clarifications were reported to the root author:

1. The socle lifts in Section 2 belong to the localized module
   \((F_2)_R\), not necessarily the global \(F_2\).
2. Before equation (8), writing \(r=az+bw\) requires the
   invariant translation of the local minimal slice used explicitly
   in the full bundle proof. It preserves \(Dr=p\), the section
   class and the scalar-fiber criterion.

The root author applied both wording changes. The geometry reviewer
then read the actual revised passages and confirmed both in place.
No mathematical or sign correction was otherwise found. The final
synthesis audit is clean. This reviewer did not edit the synthesis
or shared metadata.

## 5. Remaining mathematical limits

The proved recognition is conditional on the established quadratic
divisor setup and a smooth reduced full primitive plinth. It does
not cover singular or intersecting reduced components, or repeated
factors with smooth reduced support. At an unresolved second-image
basepoint, the exact condition is \(p\in\mathfrak mJ\), and
the conic subalgebra has a plane fiber. That fiber need not inject
into the actual full quotient fiber; its dimension alone is not
a contradiction.

The countercontrol is an actual smooth factorial algebra with the
specified nonprincipal image ideals, but its Euler characteristic
excludes every polynomial stabilization. It is not a cancellation
counterexample. Neither finiteness of an intermediate curve cover
nor primitivity on generic divisor fibers is silently promoted
to the necessary assertion on every full closed fiber.

The remaining moving higher-degree frame branches and the universal
existence of a recognized actual coordinate frame are separate
obligations. The original complex-threefold cancellation question
is not resolved by this packet.
