# Independent synthesis audit for checkpoint 60

The complete [checkpoint report](../deep-pass-60.md), including all
29 tagged equations and four source footnotes, has been independently
read and reconstructed. No mathematical, sign, or scope correction
was found. This audit creates no new theorem and changes no frozen
proof or shared verification record.

## 1. Documents actually reviewed

The review used the complete saved texts of:

- [The simple common-speed-zero exclusion](simple-speed-zero-exclusion-pass60.md).
- [The primitive Euler divisor criterion](primitive-euler-divisor-pass59.md).
- [The actual affine-slice determinant condition](actual-frame-affine-ideal-pass58.md).
- [The faithful fixed-family frame obstruction](faithful-frame-rank-obstruction-pass58.md).
- [The complete faithful quadratic module](faithful-quadratic-module-pass59.md)
  and its [separate completed audit](faithful-quadratic-module-audit-pass59.md).
- [The time-degree source-scope note](coordinate-slice-degree-scope-pass58.md).

The generic graph theorem from pass44 was already reread completely
for these reviews. The affine-module and faithful-cylinder inputs from
pass57 were also covered in the earlier complete
[checkpoint-57 synthesis audit](synthesis-audit-pass57.md). Their
recognition boundaries have not been silently strengthened.

## 2. The two exclusion arguments

Equations (1)--(13) retain the full actual frame, the independent bad
speeds, the actual invariant plane, and the exact good-column graph.
At a simple common zero, the inverse ordinary Jacobian makes the
uniquely extended speed partials preserve the local ring. The Euler
field acts by degree on its associated graded ring.

The eigenfunction argument is exact: a nonzero rational local germ
has finite order. After subtracting its matching homogeneous initial
form, a nonzero remainder cannot both have higher order and have the
same Euler eigenvalue. No finite-jet approximation or convergence
assumption substitutes for equality.

In particular, the rational linear potentials are not assumed regular.
The actual velocity identity first places them in the intersection
of the actual ring with the invariant fraction field. Only then is
the eigenfunction lemma applied to them. The constant graph terms
are contracted in the same actual intersection. The resulting
equality with the local polynomial ring in the bad pair uses the
original coordinate generators.

The arbitrary supplied slice is used after that whole-ring equality.
It need not have been affine beforehand. The Jacobian radical
condition and the nonreduced isolated-zero corollary are correct.
The speed condition \((f,g)R=\mathfrak m\) is explicitly distinct from
the second-image condition \(JR=\mathfrak m\).

For (14)--(19), the primitive normalization is of the rational base
Euler field, not a replica of either LND. At a transverse invariant
prime, differentiating \(\pi^n u\) handles negative as well as
positive valuations. Every nonzero zero-weight coefficient has
valuation zero. Actual constant contraction then proves the whole
DVR polynomial presentation and the displayed affine inverse.

The unit primitive-plinth conclusion uses the original primitive
intrinsic derivation, primality of invariant irreducibles in the
factorial actual ring, and invariant localization of the full
plinth. A tangent normalized Euler field induces a nonzero residue
derivation; a nonconstant invariant residue would contradict
separability of the one-variable field extension. Thus constant
projective speed direction is a necessary condition at the surviving
divisors, not a converse construction.

## 3. Affine ideals and the faithful fixed-pair control

Equations (20)--(22) keep the affine module separate from ambient
coordinates and from degree modules of either derivation. The
Jacobian determinant is actual and invariant before ideal contraction.
The adjugate calculation uses no inverse of a nonunit determinant.
Multiplying by the actual partials of the supplied slice gives full
ideal membership, not merely radical membership.

The lattice determinant contains exactly three powers of
\(\Delta\): two arise from the two affine coefficients and one
from the basis element corresponding to the constant function.
Base-dependent basis derivatives disappear in the determinant
after the invariant-coordinate rows are included.

Equations (23)--(27) agree with the complete six-element monic module
calculation. Necessity includes the unit base coefficient that
forces the \(X^2\) coefficient to be regular. The Hessian and linear
gradient conditions give the exact stated normal form, including
the constant correction. The result applies individually to every
compatible quadratic for the fixed pair, not only to invertible
changes of two selected generators. It does not classify changes
of the bad pair or identify arbitrary generators with coordinates.

Equation (28) is the second adjoint of the true local dual Jacobian
field on the indicated line. Restriction commutes with the
\(s\)-derivatives there. Its nonzero value does not assert that the
rational field is an LND on a non-invariant open.

The minimum-three statement remains an all-actual-slices assertion
for the faithful control. It is not a full-frame realization and
does not contradict a theorem using the missing coordinate
compatibility.

## 4. Primary-source scope

The full statement and proof of
[Stacks Tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S)
were freshly read for this review. Part (2), and the proof's choice
of prescribed regular parameters, support the optional
coefficient-compatible completion description. I also directly read
the statement and proof of
[Stacks Tag 07NM](https://stacks.math.columbia.edu/tag/07NM), which
checks the same parameter-change point in a power series ring.
Neither result is needed for the report's finite-order proof.

The Zygadło, Freudenburg, and Dasgupta--Lahiri footnotes were checked
against the completed primary-source reads recorded in the
[pass58 scope note](coordinate-slice-degree-scope-pass58.md) and
[pass59 source/proof audit](faithful-quadratic-module-audit-pass59.md).
This integration review does not claim another fresh complete read
of all three papers. In particular, the final Zygadło publisher
text has not been compared line by line.

Equation (29) is an identity of coordinate maps, not a cube-zero
pullback operator on the entire polynomial algebra. The fixed-module
saturation algorithm gives no asserted uniform degree bound. The
positive-index sliced-image equivalence concerns the sliced
derivation itself, not the separate affine module or the intrinsic
derivation. No unrelated relative-plane theorem is imported.

## 5. Verification actually checked

I inspected the saved
[verification record](../verification-pass-60.json) directly and
aggregated its suite entries. It records:

- 126 distinct suite entries and 1,000 test methods.
- Every suite exit code zero and every suite marked passed.
- Three newly counted suites containing five methods: two from
  pass58, one from pass59, and two from pass60.
- Start 2026-09-13 22:42:27 UTC and completion
  2026-09-13 22:44:01 UTC.
- The previous numeric checkpoint is pass57; working passes58--60
  are consolidated together. No pass61 command is present.

These are checks of the root-captured completed record, not an
independent rerun of all 126 suites. No separate complete pass58 or
pass59 regression is inferred.

The complete sources of the three new standalone checkers were
independently read. My observed individual runs were:

- [Faithful frame-rank checks](faithful_frame_rank_checks_pass58.py):
  two methods passed in 0.163 seconds, exit zero.
- [Faithful quadratic-module checks](faithful_quadratic_module_checks_pass59.py):
  one method passed in 0.036 seconds, exit zero.
- [Simple speed-zero checks](simple_speed_zero_checks_pass60.py):
  two methods passed in 0.060 seconds, exit zero.

These suites use only unittest and SymPy, with no solver-internal
imports. They verify the stated exact controls, not the universal
local eigenfunction proof, all-function quantifiers, or published
classification inputs. Separate exploratory pass61 checks are not
part of this checkpoint or these totals.

## 6. Remaining scope

The report correctly leaves ramified isolated speed zeros and
constant-direction divisor cases unresolved at this checkpoint.
The necessary normalized-Jacobian ideal containment is not a proof
of unitness. The fixed-pair faithful control does not settle other
bad pairs.

Recognition of every supplied frame would still not supply an
unrestricted frame-reduction theorem. The original complex
threefold cancellation implication, the professor's intended
dimension and field interpretation, human expert review, formal
proof-assistant verification, and historical novelty remain
unconfirmed. No stronger conclusion is certified by this audit.
