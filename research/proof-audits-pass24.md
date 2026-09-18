# Pass 24 proof and verification record

## Mathematical status

The [main report](../deep-pass-24.md) separates four working derivations
from finite exact controls. No part of this packet proves unrestricted
complex threefold cancellation, establishes mathematical priority, or
constitutes human expert review or proof-assistant verification.

The coefficient criterion applies to c(f,h)+rB(f,h,x) in the specified
canonical base. It is complementary to the preceding C[f,h,r] theorem,
not a classification of all physical coefficients. Its positive example
1+2fxr has global coordinates but, for n>=2, cannot be moved into the
earlier coefficient ring by a polynomial automorphism fixing the base.
This obstruction does not exclude changes of the entire coordinate frame.

## Written reconstruction and corrections

The main agent wrote the
[coefficient proof](odd-coefficient-gauge-pass24.md).
Two separate model agents reconstructed its necessity curves, polynomial
gauges, finite inverse, and all-degree obstruction:

- [First independent reconstruction](odd-coefficient-audit-pass24.md).
- [Second independent reconstruction](odd-coefficient-second-audit-pass24.md).

Both caught the same transcription error: equation (11) originally lacked
the plus sign between the two primitive-difference summands. That sign
was restored before the final regression and report. The sufficiency
argument was also made explicit in the free monic remainder basis
1,x,...,x^4, so cancellation of h takes place coefficientwise.
Neither reconstruction reported a remaining substantive defect within
the stated family.

The first reconstruction supplies a second all-degree nongauge proof
using the ordinary degree-six part of the original physical equality.
It is distinct from the main proof's reduction modulo f^n. Neither proof
places a degree bound on an unknown polynomial gauge.

The main agent corrected one sentence in the second audit: L is not an
invariant. The correct relations are E(L)=-a and E(rho)=E(X)=0.
The formulas and their uses in the proof already had those relations.

The main agent also read and reconstructed the complete
[horizontal-action analysis](horizontal-lnd-pass24.md),
[intrinsic tangent-frame analysis](intrinsic-frame-repair-pass24.md),
and [surface quotient analysis](nodal-hypersurface-pass24.md).
Cross-checks reconstructed the horizontal recurrence and all six tangent
fields. The surface's added module countercontrol is explicitly a module
operator, not an algebra derivation. It therefore excludes a proposed
module-only argument, not an ambient polynomial realization.

The final report received an additional independent transcription and
hypothesis review. It requested one scope clarification in Section 5:
the ambient extension must be a locally nilpotent derivation, not an
arbitrary derivation extending the surface field. For an LND preserving
(P), one has D(P)=0, which is used by the displayed exact sequence.
The full source note already stated that premise. The report now does
so explicitly. The review found no other mathematical correction.

A separate independent final review read the full surface note and its
report summary. It verified the restriction exact sequence, the actual
all-degree kernels and higher images of the module operator, and the
generic-rank-two, three-generator defect summand. It also checked that
the proposed polynomial module realization is not closed under
multiplication. No correction was requested. The prescribed surface
defect is a rank-one normalization module; the rank-two module
countercontrol is not claimed to realize that surface defect.

## Exact execution, not proof substitution

The two new standalone checkers import only unittest and SymPy. They do
not import the research solvers or one another:

- [Reduction controls](reduction_controls_pass24.py): 23 test methods.
- [Surface controls](nodal_hypersurface_checks_pass24.py): 8 test methods.

The reduction checker initially had 22 methods, independently run in
1.000 seconds. The main agent added a 23rd method that checks the actual
four-variable slice gradient, all six primitive tangent fields, their
nonvanishing iterate recurrences, and the three successful combinations.
The surface checker initially had seven methods; its author added the
eighth for the module countercontrol. These are historical execution
counts, not additional methods.

The final complete regression ran from 07:06:53 through 07:08:08 UTC on
September 13, 2026. All 494 preceding methods and 31 new methods passed:
525 methods across 40 suites. The new reduction suite took 1.025 seconds
under unittest, and the surface suite took 0.113 seconds. Exact commands,
wall times and exit codes are in
[verification-pass-24.json](../verification-pass-24.json).

An earlier odd-coefficient audit ran 15 inline control groups in
1.894 seconds. The horizontal derivation check reported 56 inline
assertions, and the tangent derivation check took 0.056 seconds.
These inline checks, repeated runs, and the regression runner's five
parser controls are not counted as additional test methods.

The companion [artifact checker](consistency_checks_pass24.py) validates
claim numbering, suite-method counts, current manifest flags, dependencies,
local links, mathematical-equation numbering, whitespace and SHA256
hashes. Its [output](../consistency-pass-24.json) is file-integrity evidence,
not a mathematical proof checker.

## Sources and remaining obligations

The report cites the canonical base and degree-module literature, the
full-ideal affine-modification principle, the leading-LND construction,
and the proper-additive-action recognition theorem with their hypotheses.
The main agent directly read Gurjar, Masuda and Miyanishi's Theorem 4.1.1
on printed page 44 of
[*Affine Space Fibrations*](https://oa.tib.eu/renate/bitstreams/2db0f47c-00f9-4195-9c8a-a46722165a99/download).
That result requires a proper additive action on the stably affine
threefold. The mere existence of a nonzero LND does not establish its
hypothesis; an intrinsic polynomial slice would do so.

No comprehensive new novelty audit has been completed for these family
statements. Independent model agreement is not a substitute for that
audit, a human algebraic geometer's review, or formalization.
The arbitrary-X construction remains missing. No external message,
submission, public posting, payment, or automation was performed.
