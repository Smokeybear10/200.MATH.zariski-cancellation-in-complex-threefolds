# Proof audits for the fixed-fiber investigation

This continuation makes mathematical progress, but does not solve
the general cancellation conjecture. The immediately preceding
user check-in was status-only and is classified as no progress.
The earlier substantive pass91 remains progress. The present pass
revalidated the existing state and completed the local and total
fiber bounds, quadratic generic-rank exclusion and actual-plane
deduction recorded below.

## Mathematical reconstruction

| Artifact | Full-file reconstruction completed |
| --- | --- |
| [Fixed scheme](nonconical-fixed-scheme-structure-pass92.md), eight equations | Geometry author; Root, General and Jet independent EOF reconstructions. The unit factor retains du, all syzygies descend before the depth argument, and whole-fiber multiplicity is not fixed-scheme thickness. |
| [Local multiplicity](nonconical-closed-fiber-multiplicity-pass92.md), eight equations | Root author; General, Geometry and Jet independent EOF reconstructions. All checked exact contraction, the nonfinite flat local map, J-adic rather than maximal-ideal grading, the residue field factor and ambient cotangent rank. |
| [Total multiplicity](nonconical-total-fiber-multiplicity-pass92.md), four equations | Root author; General, Geometry and Jet independent EOF reconstructions. The common surviving function, all semilocal maximal ideals, Artinian product and cubic profiles were checked. |
| [Ramification](nonconical-irreducible-fiber-ramification-pass92.md), seven equations | Geometry author; Root, General and Jet independent EOF reconstructions. The existing general-cylinder applicability is deduplicated to pass46; the whole-irreducible hypothesis is retained inside this theorem. The final forward paragraph records its use with the stronger total bound. |
| [Collapsed plane](nonconical-collapsed-component-plane-pass92.md), eight equations | General author; Root, Geometry and Jet independent EOF reconstructions. The balanced tensor map, exact original plane ideal and everywhere-on-plane Jacobian statements were checked. |
| [Synthesis](nonconical-fixed-fiber-frontier-pass92.md), five equations | Root author; General, Geometry and Jet independent EOF mathematical and scope reviews. Generic quotient rank is not rank at every closed point or the rank of the original velocity Jacobian. |

These are separate AI reconstructions, not human peer review or
formal proof certificates. Every theorem above remains conditional
on the specified actual original frame. They do not establish its
existence for an arbitrary sliced action.

The new total bound is stronger than the first irreducible-fiber
comparison. A degree-two generic rank-zero component has multiplicity
four, exhausts the total length bound, and is therefore the whole
irreducible reduced fiber. Only at that point is the topological
multiplicity-two conclusion applied, giving the contradiction.
Neither arbitrary irreducibility nor elimination of rank-one fixed
curves is presumed.

## Primary-source scope

Root freshly read the complete displayed Stacks proofs of 00R4,
00LX, 00LK, 00NQ and the relevant regular-local statements of
00NN, together with 00HT(7)'s target-local flatness proof.
The exact local and semilocal applications are proved in the
new notes. Their deeper commutative-algebra dependencies were not
all freshly reconstructed.

Root and Geometry freshly read Kaliman's final author PDF through
the full proofs of Lemmas 2.1--2.2, Notation 2.3, Lemma 3.1,
all of Proposition 3.2, Lemma 4.1, Proposition 4.2, Proposition 5.1,
and Theorem 5.2's statement and displayed deduction. The primary
paper's theorem already has the general-threefold hypotheses;
pass46 had already checked their applicability to the cylinder.
The integral lattice and multiplicity argument is a separate
derived argument inherited from passes33--34. Underlying analytic,
Thom, Stein and contraction results were not all freshly re-proved.

General freshly read the selected complete Stacks 00R4, 00NN and
00HT arguments, and the retained passes33,34,46 for its topology
reconstruction; it did not claim a fresh Kaliman primary read.
Jet freshly read the selected 00LX, 00LK, 00NQ, 00R4 and 00NN
proofs for the two eight-equation notes. Jet subsequently freshly
read the complete selected Kaliman statements and proofs listed
above, the retained passes33,34,46 and Stacks 00HT for its topology
and total-bound audits. Geometry's additional
primary reads of Masuda and Dasgupta--Lahiri have their exact
limited scopes recorded in fixed-scheme92. They supplied no new
arbitrary-frame or closed-point classification theorem.

## Finite computation

The [standalone checker](fixed_scheme_artin_checks_pass92.py)
imports only the standard library and SymPy. Root and General
read all its code and the [scope note](fixed-scheme-artin-controls-pass92.md).
Its two methods test the length-four/five/six Artinian examples
and the distinct fiber and fixed-scheme lengths in eight selected
triangular-family parameter pairs. Gröbner standard monomials,
multiplication matrices, nilpotence and socle checks have explicit
finite scope. None establishes the universal proof conclusions
or realizes a nonconical original frame.

The [canonical capture](verification-pass92-working.json) ran:

    /opt/anaconda3/bin/python -m unittest -v research.fixed_scheme_artin_checks_pass92

It passed one suite/two methods, exit zero, in 0.447691458 measured
wall seconds and 0.059 unittest seconds. It began at
2026-09-14T14:30:45.080Z and finished at 14:30:45.535Z.
The input hash was unchanged. Complete stdout and stderr are saved;
the output hash is calculated from stdout, one newline, then stderr.
The canonical tool chunk is ea82cc.

Jet's author run passed in 0.062 unittest seconds (4ad5a7).
General's independent run passed in 0.060 seconds (51169e).
These are reruns of the same two methods, not additional methods.
There was no full regression or exhaustive action search.

## Rejected shortcuts and bounded dead ends

Formal first-jet controls allow the remaining nilpotent Jordan
types at a fixed point. The orbit determinant gives no extra
constraint beyond nilpotence at that order. Those inline tables
are not an actual polynomial inverse frame and are not counted
as new unittest methods.

A conditional leading-degree cancellation in an aligned graph
ansatz was not promoted to a theorem: the needed base alignment
has not been justified. The old zero-first-jet quintic-filtration
obstruction54 also retains hypotheses not supplied by the present
plane ideal. No result is inferred from either missing hypothesis.

A source search returned an unreviewed public AI research
repository; its snippets were not used as mathematical authority.
No negative search establishes absence of prior work or novelty.
The present claims have not received a statement-level novelty
clearance or expert review.

## Integrity and limits

The predecessor audit at 2026-09-14T14:20:58.434Z (372ae1)
revalidated all 520 frozen hash records through pass91, the
historical full75 record, its nine input and six output records,
and the unchanged 544-claim registry. The last full-regression
count remains 146 suites and 1,047 methods. The new two-method
capture is not added to that historical count.

One stray `+then` text join in Root's first total-bound save was
repaired before final independent reviews. Jet disclosed a
patch-wrapper parse error before any file action while adding
provenance to its scope note. Neither was a test failure or a
change to an earlier frozen mathematical claim.

Only pass92 artifacts and the mutable README/ledger indexes are
being added or updated. The final checkpoint records their
individual hashes after reviews. Hash checks establish artifact
integrity, not mathematical truth. The unrestricted conjecture,
arbitrary-frame reduction, expert review, formal certification
and novelty determination remain unfinished. No external contact,
public posting or submission occurred.
