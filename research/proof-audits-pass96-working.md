# Proof and execution audit for pass96

Pass96 is substantive progress on conditional geometric
restrictions, not completion of cancellation. The
preceding check-in was status-only and is no progress;
this continuation finished the saved95 packet and then
derived the new affine-line and compatibility results.

## Mathematical evidence

- Root's [affine-line proof](quadratic-fiber-affine-lines-pass96.md)
  has six equations. It uses the actual smooth disjoint
  reduced fibers95, ordinary Thom isomorphisms in degrees
  four and five, and contractibility to remove punctures.
  Root read the saved proof through EOF; Jet, General
  and Geometry completed separate full saved-proof
  reviews, including the ordinary noncompact-Thom point.
- Jet's [compatibility proof](quadratic-component-compatibility-pass96.md)
  has ten equations. The initial nine-equation version
  excluded a mixed (2,2) fiber. The final version rules
  out every companion to a noncollapsed fixed component.
  Root read the initial proof and the complete new
  section and forward-link delta. General separately
  reviewed the full expanded saved proof; Geometry also
  reviewed the final version. The projection
  argument does not depend on the new affine-line theorem.
- Geometry's [dependency audit](irreducible-fiber-dependency-audit-pass96.md)
  has eight equations. Root, General and Jet read the
  complete saved argument. General additionally checked
  the selected original primary-source proof passages.
  The new normalization-H1 argument reduces the source
  dependence of the multiplicity-four exclusion, with
  no reliance on a later free-action conclusion.
- General's [bridge obstruction](quadratic-global-bridge-pass96.md)
  has eight equations. Root and Jet read the complete
  final tangent-bearing proof and code. Geometry read
  the full proof and independently reconstructed its
  determinant and tangent calculations. Root requested
  the precision edit from unqualified speed-map rank
  two to generic rank two; its rank does drop at some
  base points. This prose correction does not change
  the checker.

The four notes have 32 numbered equations. The synthesis
adds four. These are inventory counts, not measures
of mathematical strength. Reviews by AI agents are not
human expert review, a proof-assistant certificate or
historical novelty clearance.

## Canonical exact control

The [retained capture](verification-pass96-working.json)
records one suite and one test method:

~~~sh
/opt/anaconda3/bin/python -m unittest -v research.quadratic_global_bridge_checks_pass96
~~~

The final checker passed at
2026-09-14T16:34:57.323Z--16:34:57.810Z, exit zero.
The canonical tool chunk is dca956. Process wall time
is 0.481187666 seconds; unittest reported 0.094 seconds.

Its input SHA-256 is
f482c0bb934986d1bb5e438469eccdd4e60628bec1b7995d4fc23f37a3de649e.
The complete stdout-plus-newline-plus-stderr SHA-256 is
9d767260723bcc372c73dea2ef2c29be9b7ce6ca2cb2c7d2c80c792d6ad5b3b7.
The input was unchanged during execution and the
entire output is retained.

The method checks the unit row, determinant-one
relative frame, quotient identities, the actual
polynomial inverse for Z, the relative inverse,
the failed tuple's Jacobian and singular point,
and the tangent obstruction to coefficient recovery.
It does not prove the all-coefficient speed comparison,
the full-kernel contraction, universal fiber geometry
or cancellation.

General's final author run 747968 passed in
0.094 seconds. Jet independently ran the final
tangent-bearing checker in a7097c, one method in
0.097 seconds. These are repeats of the same method.
An earlier pre-tangent run with a similar rounded
time is not evidence for the final extension.

No numerical method was added for the universal
Thom, normalization-homology or finite-flat arguments.
The algebraic controls in the dependency note have
written verifications, not additional Python methods.

## Primary-source and dependency scope

Root freshly read Kaliman's Lemmas 2.1--2.2,
Notation 2.3, and the quotient homology diagram,
then the complete selected Proposition3.2 passage,
including the Step2 normalization rank comparison.
Geometry's deeper complete source reading and the
publisher-metadata check are itemized in its note.
General separately read the selected complete
primary Lemmas2.1--2.2,3.1 and Proposition3.2.
Jet's reviews of the dependent notes do not count
as a fresh original-source topology audit.

The ordinary Thom and affine-surface CW-dimension
facts are retained foundational inputs. No complete
new reconstruction of Dold, Milnor, or the full
Stein/Thom literature is asserted. The source was
read as primary extracted mathematical text; no
visual PDF-layout verification is represented.

Root and Jet freshly read the complete displayed
Stacks 00R4 statement/proof. Root also freshly read
00MC and the complete retained flat-rank93 proof.
Geometry freshly read Stacks 0AFU for its factorial
quadric control. Their deeper reference trees
were not all reconstructed.

A bounded literature search reencountered the
Venegas--Venegas survey's unconditional ML-stability
claim and incompatible characteristic-zero status
claims. The repository already excluded version2
in its early source audits. Reencountering those
claims is not a new result or a new bridge; no
theorem or status assertion from that survey was
adopted. The Gupta ICM characterization was also
rechecked but supplied no missing hypothesis.
No comprehensive new novelty audit is claimed.

## Saved-state and remaining obligations

The new checkpoint95 was saved with SHA-256
c5e66c8f7efedb48a69dbb341c3216e832b99cc9b2049724ad4d6dff57956bec.
Its postsave audit e65226 checked 11 artifacts,
46 equations, all three final checker inputs,
the output digest and 776 local links, with no
missing or deferred links.

General's independent checkpoint95 audit de5b36 read
the complete checkpoint, proof-audit and capture and
checked all 11 artifact hashes, sizes and line counts,
46 tags, three final inputs and the complete output
digest. It confirmed the resolved self-links and
552+11+1=564 accounting without a rerun.

The complete predecessor chain through95 was
revalidated at 2026-09-14T16:26:41.783Z in 0bdc85:
564 frozen records unchanged. Historical full75
remains 146 suites/1047 methods, with nine run
sources and six retained output hashes checked.
The central registry remains 544 claims; the new
proofs are not represented as already integrated.

Current96 artifact hashes and links are recorded
in its checkpoint and postsave audit. The older
proofs remain unchanged. A matching hash establishes
file identity, not theorem validity.

The remaining goal requires global recognition
and the independent arbitrary-frame reduction.
Rank-one fixed fibers, including the remaining
collapsed reducible configurations, have not been
excluded or recognized. Professor confirmation,
human expert review, formal verification and
novelty clearance remain outstanding. No public
posting, external contact or submission occurred.
