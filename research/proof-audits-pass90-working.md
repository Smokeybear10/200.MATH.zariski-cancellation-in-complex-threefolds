# Working90 proof and verification audit

The principal mathematical change is an additional recognized
nonconical subcase, not completion of cancellation. Under the actual
three-good-coordinate constant-acceleration hypotheses, a nonzero
constant velocity determinant gives a global free intrinsic action.
Kaliman--Saveliev Corollary 2.8(1) then gives a polynomial kernel.
For a nonconstant determinant, the current conclusions remain local.

## Written proofs and independent reconstruction

The [quadratic-potential proof](nonconical-quadratic-potential-pass90.md)
was proposed by Root and authored by General. Root, Jet and Geometry
read the complete saved proof and independently reconstructed the
determinant signs, symmetric potential, removal of the auxiliary
local-slice denominator, and both inclusions \(A_\Omega=R_\Omega\).
The preceding unramified-normalization note is explicitly superseded;
its nodal example only controls the weaker differential argument.

Root authored the
[cyclic/fiber proof](nonconical-cyclic-fiber-omission-pass90.md).
General, Jet and Geometry each completed independent full-file
reconstruction. The tensor map uses the whole generic divisor fiber
and permits a nontrivial finite residue-field extension. Its
noncollapse conclusion concerns the image of R, not \(R/pR\).

Root authored the
[cubic-relation proof](nonconical-cubic-relation-pass90.md).
General, Jet and Geometry each completed independent full-file
reconstruction after the transcription correction described below.
The reviews checked the mixed-derivative identity, full symmetry
of the cubic coefficients, the negative linear-volume coefficient,
the global relative degree bound, and the elementary degree-(2,3)
exclusion over an arbitrary characteristic-zero function field.

General authored the
[open free-derivation proof](nonconical-open-free-derivation-pass90.md).
Root, Jet and Geometry reconstructed its eight-equation core.
The final ten-equation version adds Root's unit-cofactor and relative
smoothness consequence. Root and Jet read this addition completely;
Jet's final review reread the whole final file. The fixed-point-free
conclusion is kept distinct from a global slice or a relative
polynomial presentation.

Geometry authored the
[constant-determinant recognition corollary](constant-omega-recognition-pass90.md).
Root, General and Jet each completed independent full-file
reconstruction. All four separately inspected the exact published
Kaliman--Saveliev Corollary 2.8 statement and its complete displayed
proof. The checks use the whole threefold's smoothness and
contractibility, not those properties on an unverified principal open.
The earlier free-action theorem and topology dependencies are
retained published inputs, not newly reconstructed core proofs.

The [source audit](homogeneous-speed-recognition-source-scope-pass90.md)
was authored by Geometry and received General's full-file
algebra/applicability review and a separate final-section review.
Root read the complete final file. The exact fresh primary-read scopes
are stated in that note's footnotes; reviews of its algebra are not
counted as new primary-proof audits.

The [synthesis](nonconical-volume-frontier-pass90.md) was authored by
Root and received General's and Geometry's full-file mathematical
and scope reviews. Root read the full saved synthesis and the
separate constant-determinant corollary. One forward filename was
corrected to the actual corollary filename.

These are AI proof reconstructions. They are not human expert
review, formal verification, historical novelty certification, or
a substitute for checking the complete source dependencies.

## Exact control methods

Jet authored two standalone unittest methods, with only unittest
and SymPy imports:

- The [actual-frame checker](nonconical_higher_commutator_checks_pass90.py)
  checks both polynomial inverse orders, transported coordinate
  partials, the velocity Jacobian, highest adjoint, and explicit
  commutators. The written induction, rather than finitely many
  iterate checks, proves that the selected bracket is not locally
  nilpotent. Its first author run passed in 0.309 seconds.
- The [formal coefficient checker](nonconical_quadratic_potential_checks_pass90.py)
  checks a full symbolic determinant with an arbitrary formal basis,
  the quadratic coefficient and both minor signs, the symmetric
  potential, and the nonzero curl if symmetry is dropped. Its first
  author run passed in 0.235 seconds. Formal coefficients are not
  an actual-action realization.

Root and General each read both complete checkers and their scope
notes and executed both methods. Geometry read the complete actual
control and its checker without executing it. Repeated executions,
subtests and inline calculations do not add test methods.

The canonical [verification record](verification-pass90-working.json)
captures the two methods together, with the complete output and
unchanged pre/post source hashes. Tool chunk 26e243 records
2026-09-14 13:16:17.328--13:16:18.274 UTC, 0.946123334 wall seconds
and 0.521 unittest seconds, exit zero. The output SHA-256 is
0635a2c3b1c7ede3a089cc705f0fd3c9f02abb260f23d2311412b9507933aa16.
An earlier Root combined run, chunk 2b277e, passed in 0.519 unittest
seconds. Neither run tests the universal ring-descent, cubic-degree,
conormal-unit, quotient, or recognition arguments.

## Corrections and integrity

The first saved cubic proof lost five literal leading plus signs
because they were consumed as patch-line markers. Root's full EOF
read caught them; Jet and Geometry independently reported the same
stale version. The corrections were applied and read in chunk 2b277e
before the final clean reconstructions. The intended mathematics
was not silently substituted for the defective saved formulas.

The first synthesis pointed to a descriptive forward filename rather
than the actual constant-determinant note. Root corrected it to
constant-omega-recognition-pass90.md after Geometry reported it;
General independently found the stale link. No theorem statement
was changed by that correction.

The readonly predecessor audit in chunk c0a7aa revalidated 493 prior
hash records through pass89 at 2026-09-14 13:16:17.237 UTC.
The previous checkpoint hash is
cf2b5cd4712817be97ebdbba20143d7b6329e3198b02697f2ac8bec3ed49f751.
It also revalidated the retained full75 inputs and six saved outputs.
The historical result remains 146 suites and 1,047 methods; the
claim registry remains 544 entries. No full regression, exhaustive
action search, central-registry integration, or new runner was
performed. No pass89 or earlier file was changed.

The [working checkpoint](checkpoint-pass90-working.json) records
the new packet's hashes separately. Hash matching checks file
integrity, not mathematical truth. README and the ledger are mutable
indexes and are not part of the frozen mathematical packet.

The general conjecture, nonconstant-determinant recognition,
arbitrary-frame reduction, human review, formal proof and novelty
determination remain incomplete. No external contact or public
submission has occurred. The goal remains active.
