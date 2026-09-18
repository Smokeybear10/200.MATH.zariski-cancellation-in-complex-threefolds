# Proof audit for the exceptional-fiber investigation

This audit distinguishes written mathematical reconstruction, finite
symbolic controls, selected published inputs and file integrity.
None is represented as independent human expert review or a formal
proof certificate. The unrestricted goal is still active.

## 1. What changed mathematically

The preceding user check-in was a status-only turn, classified as
no progress for goal accounting. This continuation revalidated the
saved state and completed substantive pass91 work, including the
linear-case proof begun before that check-in. Pass90 itself was a
progress pass and is not reclassified as no progress.

The [synthesis](nonconical-exceptional-fiber-frontier-pass91.md)
records a recognized relative degree-one branch and sharper necessary
conditions on the degree-two and degree-three branches. In particular,
the actual highest adjoint has the global factor H=2 Omega N, and
N is primitive with possible fixed points over finitely many base
points in V(Omega). The generic divisor constant extension has degree
at most three. The localized full-gradient obstruction is exactly
disconnectedness, with two or three parallel lines in a bad closed
fiber. No argument here excludes all those possibilities.

## 2. Written proof reconstruction

Each selected mathematical file was read through EOF by its author
and separately reconstructed by the reviewers listed below. A review
of one file is not a new review of every historical dependency.

| File | Author and independent review scope |
| --- | --- |
| [Linear recognition](nonconical-linear-relation-recognition-pass91.md) | General author; Root, Geometry and Jet full-file reconstructions of all eight equations, including both zero-coefficient cases and the final canonical-slice clarification. |
| [Full-gradient source gate](low-degree-full-gradient-source-gate-pass91.md) | Geometry author; Root and General full-file reviews of all five equations. Jet read the complete note while independently checking the fiber lemma and its exact conditional source consequence. |
| [Global Jacobian field](nonconical-global-jacobian-field-pass91.md) | Jet author; Root, Geometry and General full-file reconstructions of all eight equations. Root proposed and reviewed the final nonnumbered argument proving N itself free on D(Omega); Geometry and General reviewed that final paragraph too. |
| [Residue-degree bound](nonconical-residue-degree-bound-pass91.md) | Root author; General, Geometry and Jet full-file reconstructions of all six equations and the specified surviving-degree-one local corollary. |
| [Full-gradient fibers](nonconical-full-gradient-fiber-pass91.md) | Geometry author; Root, Jet and General full-file reconstructions of all six equations, including the potentially nonreduced off-zero critical scheme. |
| [DVR descent and multiplicity](nonconical-divisor-descent-multiplicity-boundary-pass91.md) | General author; Root and Jet full-file mathematical reconstructions of all six equations. The final added checker paragraph changes only verification scope, not the argument. |

Root authored and read the complete six-equation synthesis; General
and Geometry independently reviewed it through EOF, and Jet separately
read the complete synthesis and this audit. General and Geometry requested
the same base-localization notation clarification, which was applied:
the whole divisor fiber is A_V/pA_V for V=S_(p), not the residue
field of A localized at pA. Geometry also read the final multiplicity
proof, both checker inputs and the saved capture without running them.

The linear proof does not confuse a coprime pair with a unit ideal.
The Jacobian proof does not confuse a primitive derivation with a
free one. The residue proof does not assume a finite map R to A
or trivial constants. The fiber proof does not replace a whole
nonreduced fiber by its reduction. These are substantive review
gates, not consequences of a passing test count.

## 3. Source scope

The source gate adds an exact reading of Bhatwadekar--Dutta's original
1997 Proposition 4.4 and the Section 4 ring hypotheses. Root,
Geometry and General each inspected the original displayed statement
and proof; the deeper invoked classification criteria were not
fully re-audited. Geometry's attempted visual PDF fetch failed,
which is disclosed in the source note. Text access succeeded.
The later Babu--Das restatement and selected propositions have the
precise access scope recorded in that note.

Root freshly read the selected Kaliman--Saveliev Corollary 2.8
statement and complete displayed proof, and reread the entire saved
intrinsic-quotient application. The underlying topology and deeper
published dependencies remain inherited. The conclusion needed for
recognition still requires an action free on the entire threefold.

The primitive-fiber54 note was reread for deduplication and for its
distinction between whole-scheme nonvanishing and reduced-fiber
freeness. Its socle theorem is earlier published input, not a new
result or a newly repeated primary-source audit in this pass.
The valuation dimension estimate is proved by independent-residue
lifts in the new note, not asserted solely by an uncited theorem name.

## 4. Two finite controls

The new test inputs are
[global Jacobian controls](nonconical_global_jacobian_checks_pass91.py)
and [multiplicity controls](nonconical_multiplicity_boundary_checks_pass91.py).
Each contains one standalone unittest method. The former checks
formal cofactor signs, an actual retained polynomial inverse frame,
and the reused fixed-line boundary. The latter checks the changed
presentation, its whole-fiber identities, a genuine quadratic
coordinate inverse and the failed candidate Jacobian.

Root read both complete inputs before the canonical combined run.
The [saved capture](verification-pass91-working.json) has both full
output streams, the saved input hashes and the unchanged-hash check.
It passed two suites
and two methods, exit zero, in 0.824507125 wall seconds and 0.302
unittest seconds. Canonical tool chunk: 3269e6. Complete output SHA256:

`0d4c035d1933f1e8f8589f62bd9f89d20f6ac315fd554be3f80dedc3bd7789aa`.

Earlier successful runs are not extra methods: Jet's global checker
author run was 0.145 seconds, Root's separate run 0.143 seconds,
and General's independent run 0.150 seconds. General's multiplicity
author run was 0.026 seconds and Jet's independent run 0.031 seconds.
No full regression ran. The frozen full75 record remains 146 suites
and 1,047 methods, and the historical claim registry remains 544.

The two bounded inverse-frame construction routes reported by Jet
did not produce an actual new nonconical example. The inline finite
nullspace calculations and candidate-family shear arguments were
not saved as independently audited universal proof artifacts and
are not counted as new theorem results or unittest methods here.

## 5. Repairs and integrity boundaries

The first global-Jacobian note save had inline math-delimiter and
thin-space transcription issues caught and repaired on author reread;
its eight displayed equations were unchanged. The source-gate author
corrected one literal '+with' prose join. Root replaced a pending
Jacobian-note link with its actual final filename and clarified in
the synthesis that a connected fiber can be a nonlinear embedded
copy of A1, not necessarily a straight line. Independent synthesis
review also led to the explicit base-DVR localization just described.
Jet's final review clarified that the codimension-two example is
algebra-only, not an actual nonconical construction, and aligned
the capture description with the single stored hash map and its
unchanged-hash check.

General encountered two JavaScript orchestration syntax errors before
any file or tool action while preparing a final checker-scope paragraph.
They were not failing mathematical assertions. The final patch and
checks succeeded. These repairs are not described as pristine first
saves or hidden inside a numerical success count.

The fresh predecessor audit at 2026-09-14T13:43:59.724Z checked all
508 retained hash records through pass90 unchanged, with checkpoint90
SHA256 `36e684eaec0bace1269b26d6151c19a477723e786974c882f153013e31361afd`.
That check also revalidated the historical full-run source/output
hashes and the 544-claim count. It is integrity evidence, not a
proof of the historical mathematical claims.

The parent git status lists this project as untracked, so an empty
git diff would not prove preservation. Pass90 and earlier remain
frozen; README and the research ledger are mutable navigation files.
The new checkpoint will record actual pass91 file hashes separately.

## 6. Remaining claims not certified

General cancellation, a reduction of arbitrary sliced actions to
the supplied frame, automatic global freeness, automatic connected
fibers and trivial residue constants remain unproved. Luo's intended
field and dimension have not been confirmed. Human expert review,
formal verification, historical novelty and publication readiness
have not been established. No external contact, public posting,
submission, or publication is authorized by or performed in this pass.
