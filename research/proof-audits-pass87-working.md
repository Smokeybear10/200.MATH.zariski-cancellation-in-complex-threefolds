# Proof and execution scope for the constant-acceleration investigation

The packet separates a broad one-quadratic-coordinate reduction from
a stronger frame with three E-affine companions. Neither proves general
cancellation. All independent reviews here are AI reconstructions, not
human expert review or a Lean/kernel-checked formal proof.

## Written proof reviews

The [core involution reduction](constant-acceleration-involution-boundary-pass87.md)
has seven numbered equations. Jet authored it; Root, Geometry and General
fully read and independently reconstructed the fixed-ring, fixed-scheme
and conditional reflection arguments. The original slice is not assumed
to be an ambient coordinate. This existing core remained unchanged.

The [fiber-row proof](constant-acceleration-fiber-row-pass87.md) has eight
equations. Geometry authored the difference-ideal, differential and
actual-frame arguments. Root and General independently read the complete
proof. Root connected its matrix-completion control to the standard
Reynolds map. Two accidental literal plus-sign joins were removed before
finalization. The final Reynolds connection was separately reread.

The [averaging obstruction](constant-acceleration-averaging-obstruction-pass87.md)
has six equations. Jet adapted a retained SL2 construction, with explicit
reuse provenance. Root, General and Geometry fully reconstructed both
actual inverse orders, the original partial, the averaging signs and the
all-n monic recurrence. It is not a new family or a counterexample to
cancellation, and it has no three-good-coordinate premise.

The [degree-band source note](involution-reynolds-source-gate-pass87.md)
has six equations. General authored it. Root and Geometry fully read
the final proof and its provenance paragraph. The Jurkiewicz hypothesis
is a range of homogeneous degrees, not arbitrary finite Taylor length.

The [odd-coordinate equivalence](coordinate-odd-generator-recognition-pass87.md)
has five equations. General authored it; Root and Geometry independently
reconstructed the branch-fiber identity, generic separable descent,
flatness over the PID, polynomial conclusion and converse unit argument.
It equates two recognition premises; it does not establish either one
unconditionally.

The [three-good-frame proof](constant-acceleration-three-good-frame-pass87.md)
has ten equations. Root identified the Jacobian, coefficient-split and
velocity-image questions; Jet supplied the exact adjoint argument,
rank-one branch and actual rank-three control. Root and General fully
read the final proof and checker. The highest-field construction uses
an actual localized LND and invariant specialization. In the explicit
control that field is nonzero but kills r. No r-slice follows.

The [synthesis](constant-acceleration-frontier-pass87.md) has five
equations. Root authored and read it through EOF; General independently
read the complete original and final expanded versions, clean.
There are 47 numbered equations across these seven notes, not 47
independently formalized theorems.

## Primary-source read boundaries

Root, General and Geometry visually read all three original Jurkiewicz
pages 243--245, including the degree-band theorem and its short proof.
A printed sign in the final inverse expansion is inconsistent with its
preceding identity; using that identity directly gives the stated
inverse. The source note does not copy that sign into a proof.

All three read the selected Lamy--Przytycki Corollary B statement and
complete short proof, not the full CAT(0) construction or its dependency
chain. General and Geometry additionally read the selected Proposition
4.11 proof in Lamy's September 2026 survey and the relevant 2024
Kraft--Zaidenberg paragraph. Root verified the 2026 survey's bibliographic
entry, without claiming to have read that proposition's proof this turn.

For the odd-coordinate lemma, all three checked Kambayashi's exact
statement as quoted in Dutta--Gupta--Lahiri Theorem 2.8 and the
affine-plane-fibration definition and PID consequence stated by
Babu--Das. Root additionally read their quoted Bass--Connell--Wright
Theorem 2.2. Original Kambayashi, Sathaye and Bass--Connell--Wright
proofs were not newly audited. Root's initial DGL PDF fetch failed;
the original arXiv HTML supplied the statement instead.

The retained new primary source is
[the Jurkiewicz PDF](../tmp/pdfs/general-jurkiewicz-reynolds-pass87.pdf),
SHA-256 98754b6eaf8fad7c8177604228e436e2cfc21315de26af7954d3859ee4fa697d.
Together with the 19 preceding tracked primary files this makes 20.
Temporary page renderings are not mathematical test evidence. No
exhaustive literature or historical novelty audit is claimed.

## Exact methods and canonical capture

Each new checker imports only unittest and SymPy, with no solver or
earlier checker imports. Each contains exactly one unittest method.

The [averaging checker](constant_acceleration_average_checks_pass87.py)
passed its author run in 0.152 seconds, Root's independent run in
0.156 seconds (chunk1410c1), and General's independent run in
0.152 seconds (chunkc93d50). Geometry fully read it without execution.
The infinite recurrence is proved in writing, not extrapolated from
the six tested instances.

The [row checker](constant_acceleration_row_checks_pass87.py) was authored
and fully read by Root. Its first run passed in 0.074 seconds,
chunk4d2050. General independently fully read and ran it in 0.151 seconds,
chunka00c7a; Geometry fully read it without execution. It includes an
exact distinct-point same-image check as well as the nonconstant Jacobian.

The [frame checker](constant_acceleration_frame_checks_pass87.py) was
authored by Jet. Its original single method passed in 0.067 seconds;
the highest-field checks were then added to that same method. The final
author, Root and General runs passed in 0.063, 0.063 and 0.062 seconds,
chunks a5d052, 297e9f and 605ceb respectively. No additional method
is counted for the expansion or the preliminary inline calculation.

Root adapted and fully read the [print-only runner](run_targeted_pass87.py).
General independently read it, without execution. Root's canonical run
in chunk58d887 produced the complete
[saved capture](verification-pass87-working.json), from
2026-09-14T11:28:42.171815+00:00 to
2026-09-14T11:28:42.693319+00:00. All three suites and three methods
passed. Unittest times were 0.155, 0.071 and 0.055 seconds; total
monotonic wall time was 0.521032 seconds. All five input hashes were
unchanged and all three full outputs are retained with hashes.
General independently fully read the capture and checked all those
hashes and counts in a read-only check, chunkd518b7.

No full regression or exhaustive action search ran. The preserved
full75 result remains 146 suites and 1,047 methods. The central
registry remains 544 historical claims and is not integrated with
this working packet. No mathematical test assertion failed in the
reported runs. An initial read-only search used an unmatched shell
glob; a filename-specific search replaced it without file changes.

## Integrity and goal status

Root's fresh predecessor audit at 2026-09-14T11:21:49.693Z verified
447 frozen records through pass86, plus the retained full-run input
and output accounting. The [checkpoint](checkpoint-pass87-working.json)
records this packet's current hashes and verification limits.
Hashes, consecutive equations and passing example checks do not prove
the universal mathematical statements.

The immediately preceding user check-in verified live agent status
with the agent-status tool; it did not itself add a proof. The preceding
mathematical continuation developed the core87 work. This continuation
is progress: it completed proof/source audits, derived and tested the
stronger-frame identities, and saved the complete87 evidence packet.

The goal remains active. The professor's interpretation, unrestricted
recognition, formal verification, expert review and novelty certification
are incomplete. No external message, submission or publication occurred.
