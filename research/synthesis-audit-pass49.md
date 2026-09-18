# Independent synthesis audit for pass 49

The complete [deep-pass-49.md](../deep-pass-49.md) was read, including all
24 tagged equations, the verification discussion and all four source notes.
It was compared against the complete frozen
[normalized-cover proof](normalized-cover-surjectivity-pass49.md),
[nodal-obstruction proof](nodal-plinth-obstruction-pass49.md), and
[actual-frame proof](frame-filtration-generation-pass49.md). The existing
[proof-audits-pass49.md](proof-audits-pass49.md) record was also read.

No mathematical or sign correction was found. One self-contained notation
correction was requested from the root author: before using the local
symbols, define \(F_n=\ker D^{n+1}\), \(\operatorname{pl}(D)=pC\), and
\(I_2=pJ\), with \(J\) in the local formulas denoting its localization.
The root author added these definitions at the start of Section 4. The
actual revised paragraph was reread and is correct. This was a notation
clarification, not a change to the proof. The final scoped audit is clean;
this audit did not edit the synthesis.

## 1. The homology condensation retains the support argument

Section 2 uses the actual quotient factorization, the reduced pullback
divisors and the product complement. The exact diagram therefore gives the
correct implication from a lower Thom-image class to an upper Thom-image
class. The phrase about representing upper boundaries near the whole fiber
is supported by the typed relative-boundary and local Thom maps in the full
proof. It does not assume a retraction onto the fiber.

The reached-disk construction includes the entire normalization-preimage of
the fiber by its definition. Properness of finite normalization then gives
the required whole-fiber neighborhood, without compactness, reducedness or
smoothness of that fiber. Finite peripheral loops cannot cancel against the
total puncture relation because each affine normalization component has an
additional puncture at infinity. The weighted selected loops consequently
give the stated contradiction.

The separate [pass-50 adversarial re-audit](normalized-cover-adversarial-audit-pass50.md)
reconstructed those support gates again. It is a subsequent re-audit by the
same geometry agent, not another independent external reviewer or part of
the frozen pass-49 proof packet. The synthesis does not silently replace
the argument by an assumption of normalized surjectivity.

## 2. Finite invariant rings and the quadratic trace

Section 3 has the corrected ring/field distinction: invariant localization
gives the curve ring, then passage to fraction fields identifies its rational
field. The no-pole argument and finite-module containment are correctly
condensed. No equality between the particular intermediate curve and the
full invariant spectrum is claimed.

In Section 4, the finite rank-two statement has the required separate
justifications. The normalized cover is finite, its local algebra embeds in
the actual invariant field, and that field has degree two over the normalized
base field. Thus its integral closure over the base DVR is finite and torsion
free of rank two, hence free. It need not be local, étale or split. The cited
normalization statement alone does not assert rank two; the synthesis's
source note correctly identifies the separate actual-field input.

Vanishing at every normalized cover point puts the slice residue in the
radical of the residue algebra's maximal-ideal extension. Multiplication by
that residue is nilpotent modulo the base parameter, so its matrix trace
vanishes even at ramified points. The actual minimal-slice argument is
retained before the displayed quadratic is used as a minimal polynomial.
Both identically-zero denominator cases remain covered by the swapped
argument and coprimality.

The contradiction uses the order-two initial form of the full plinth, not
just two tangent directions or a nodal reduced support with repetitions.
No reducedness of \(J\) or premise \(B_1,B_2\in J\) has been added. The
consequence \(J=C\) for a reduced full nodal divisor is not promoted to
polynomial recognition of the resulting global quadratic equation.

## 3. Actual frame generation and the arbitrary-slice control

Sections 5–6 keep the narrower actual-frame hypotheses separate from the
general normalized-cover statement. The generic equality
\(B_L=L[x_3,x_4]\) is used as an equality of rings, not merely a Jacobian or
function-field assertion. Each displayed slice is an actual element on the
specified invariant open. Its generic affine coefficients need not belong
to that localized invariant ring.

The inverse linear system, projection degrees and surjectivity of the slice
projection prove generation of the entire localized ring by its degree-two
module. The unit-ideal-open gluing is valid element by element, without a
finite-module premise for the quotient. The conic-plane contradiction then
gives a set-theoretic support inclusion only.

The genuine coordinate control has the stated adjoint profile, determinant,
slice inverse and projected degree list. The all-degree leading-coefficient
argument distinguishes an unbounded projected generating list from the
minimum degree needed to generate that same ring. The simultaneous zero
locus and universal frame-existence questions remain open in the synthesis.

## 4. Verification and provenance limits

This is a written synthesis audit. No new checker was added or rerun during
this review. The report correctly describes its standalone control as one
method with three selected parameter values, not three methods or a
mechanical verification of the geometric statements. No numerical full-run
total or integrity checkpoint is asserted in this audit; the root author
handles integration of captured logs separately.

Source access for the topology, normalization and prior pass-49 proof audits
is recorded in the linked notes. This comparison does not claim a fresh
source search for every inherited theorem. It does not infer historical
novelty, human expert approval or proof-assistant certification. No frozen
proof or shared metadata was changed.
