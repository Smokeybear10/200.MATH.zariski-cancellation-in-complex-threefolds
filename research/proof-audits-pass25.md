# Pass 25 proof reconstruction and evidence record

This is a process record, separate from the mathematical report.
The unrestricted complex threefold cancellation conjecture remains
unsolved. No result is called novel or expert-reviewed.

## Independent reconstructions

### Coordinate-pair elimination and rank-one saturation

The general-affine investigator wrote
[commuting-leading-pass25.md](commuting-leading-pass25.md)
and its standalone 16-method checker. The main agent read the whole
note and checker, reconstructed the positive primitive integral,
the nonlinear and linear degree recurrences, the exact matched frame,
and the UFD rational-multiplier argument. A targeted main run passed
16 methods in 0.304 seconds.

The jet investigator separately checked the coordinate-pair criterion
and its applicability to the actual coordinate partials, not merely
their associated graded fields. The existing frame's provenance is
explicit: the new tested assertion is the forced row elimination,
not the inherited leading-rank collapse.

The author removed a trailing blank and added explicit primary credit
to Stampfli's UFD multiplier/same-kernel facts and plinth rescaling.
The saturation statement is an application of established mechanics,
not a claimed new abstract theorem.

### Coupled homotopy normalizer

The jet investigator wrote
[coupled-homotopy-pass25.md](coupled-homotopy-pass25.md)
and its seven-method checker. The main agent read both completely
and reconstructed the UFD ratio argument on the actual stable algebra,
the degree-one vertical filtration, the full multiplicity of the
plinth, the factor-field specialization, the residual-pair contradiction,
and the all-degree parity obstruction in the polynomial fence control.

The slice theorem was checked on the pair of included algebras,
not just on the ambient ring: the horizontal normalizer is equivalent
to a parameter-preserving isomorphism carrying the old invariant
subalgebra onto the corresponding included subalgebra. The main agent
read the added pair-isomorphism paragraph and its source-credit changes.
A targeted main run passed seven methods in 0.285 seconds.

The normalizer is not assumed to fix the old plane pointwise.
The explicit polynomial control excludes all setwise normalizers,
while retaining a successful coordinate partial that changes that plane.
The regular commuting alternative is explicitly not locally nilpotent.

### Non-fence rigidity

The main agent wrote
[nonfence-plane-rigidity-pass25.md](nonfence-plane-rigidity-pass25.md)
after reading the actual primary stabilizer and torus statements.

The jet investigator and general-affine investigator independently
reconstructed the proof. Both found no actionable defect.
The second audit explicitly checked both composition orders for
the inverse specialized at lambda=c+tau, uniform degree bounds
for the map and inverse, and the genuine regular morphism into
the closed algebraic stabilizer.

The full effective-divisor scope, affineness and connectedness
hypotheses for the torus step, and the common-residue full-plinth
application were checked. No connected-support premise was added.
The plane fence converse is not presented as a guarantee of an
ambient lift. An affine-line family need not be a group homomorphism;
the proof correctly uses constancy for all regular maps into a torus.

### Actual nodal-base map and one-step algebraic exclusion

The geometry investigator wrote
[ambient-lifting-pass25.md](ambient-lifting-pass25.md)
and its five-method checker. The main agent read both completely,
reconstructed the actual opposite-sign formal base map, completion
descent, exact two-generator node fiber, restricted one-step kernel,
and the domain/kernel/primitive/singular-line assertions for the
quadratic attempt. A targeted main run passed five methods in
1.191 seconds.

The jet investigator independently audited the whole note and checker.
No actionable defect was found. In particular, for two formal branch
series F_plus and F_minus agreeing at d=0, the inverse map is

    (F_plus+F_minus)/2
      + v*(F_plus-F_minus)/(2*d*sqrt(1+d)).

The second coefficient is a genuine formal series; this verifies
compatibility with A0, coefficientwise in the common t. At the split
normalization roots the derivative in y is nonzero; at ordinary
roots the coefficient of z is a unit. Thus the asserted transverse
parameters really are available on every original branch.

The independent five-method run passed in 1.185 seconds.
The audit distinguished primitive common-divisor status from a
nowhere-vanishing vector field and distinguished the free rank-one
defect of the quadratic attempt from the required nonfree module.
No files were changed by that audit.

### Final report transcription audit

The general-affine investigator read the whole consolidated report and
checked equations (2)-(9) against the proof notes. Two scope phrases
were corrected: the fence converse now chooses adapted coordinates,
and a construction covering every homotopy input must allow the plane
to change, without denying the proved plane-fixing positive cases.

The geometry investigator checked Section 3, equations (13)-(15) and
the Kaliman/Masuda source limitations against the full note. It caught
one precision issue in both the report and the note's proposition lead:
the displayed completion over C with a common power-series variable
is at a closed conductor point. The qualifier was added in both files
and the claim registry. The proof already handled nonclosed points by
localization. No mathematical conclusion or checker source changed.

## Primary-source boundaries

The main agent read the selected Stampfli propositions and UFD passages
and Milne's connected algebraic-group convention and Corollary 17.25,
including its proof. The general-affine investigator independently
reread Stampfli for the inherited multiplier credit.

The main agent read the statements and proofs of Stacks tags 00MB
and 00MC. It also checked Kaliman's Lemma 2.2/Notation 2.3,
Proposition 3.2 and Theorem 5.2, and Masuda's Section 3 normal-form
and one-step hypothesis passages. These checks support precise
applications and precise non-applications, not an exhaustive
literature novelty audit.

The historical semistable multiplicative-action reformulation was
read in Zaidenberg's primary survey introduction. It is recorded
as a known reformulation, not a new reduction.

An old Okayama-hosted Kuroda PDF URL returned 404 through the local
fetch and an error through the web reader. No current-pass full-text
reading of that inaccessible copy is claimed, and no new conclusion
depends on it. Search-only snippets from other recent papers were
not promoted to verified theorem inputs.

## Exact execution

The complete regression actually ran from 2026-09-13 07:41:06 to
07:42:21 UTC. All 525 previous methods and 28 new methods passed:
553 methods across 43 suites.

The new suites in that execution were:

| Suite | Methods | unittest seconds | Wall seconds |
| --- | ---: | ---: | ---: |
| Coordinate elimination and saturation controls | 16 | 0.304 | 0.512 |
| Coupled homotopy controls | 7 | 0.284 | 0.505 |
| Ambient lifting controls | 5 | 1.212 | 1.465 |

The [actual JSON log](../verification-pass-25.json) records commands
and every preceding suite. Repeated author, main and independent
runs are not additional test methods. Five runner parser controls
are also not counted as mathematical unittest methods.

These finite exact controls check identities and selected boundary
instances. Universal LND statements, the algebraic-group argument,
formal-local flatness and all-parameter exclusions rely on the
written proofs. No proof assistant or human expert has verified them.

## Unresolved obligations

The homotopy exclusion leaves actions that change the embedded old
invariant plane itself. The matched elimination failure leaves more
general nonlinear frame changes. The intrinsic route still lacks a
slice or another sufficient recognition condition for arbitrary X.

The fixed surface is now proved flat over the smaller nodal base,
so that possible contradiction is closed negatively. Its invariant
algebra rules out every specified relative one-step model, not all
multi-stage modifications or all polynomial ambient realizations.
No actual C^3 ambient LND with the required nonfree restriction defect
has been constructed or ruled out.

No external message, submission, public claim, contact, automation,
expert review, comprehensive novelty audit or general solution
occurred in this pass.
