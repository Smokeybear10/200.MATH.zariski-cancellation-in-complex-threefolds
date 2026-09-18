# Strict slice and embedded-support audit

The new working deductions retain the original polynomial action,
actual coordinate frame, and supplied global slice. They strengthen
necessary conditions in the restricted rank-one quadratic branch.
The unrestricted cancellation goal remains open. The
[synthesis](rank-one-strict-frontier-pass84.md) states the exact scope.

## Complete mathematical reviews

Geometry's nine-equation
[strict-slice proof](rank-one-strict-slice-certificate-pass84.md) was
read through EOF and reconstructed separately by Root, General and Jet.
The return now fixes the original z without specialization and uses
the supplied slice identity. Frozen Taylor derivatives give a monic
equation after localization at U=1 modulo I. Each coefficient has
one additional ideal power. The finite reduction at exponent
(D-1) squared and the exact contraction were checked independently.
No transfer from an arbitrary representative modulo I is used.

The valuation inequality and stronger gcd multiplicity consequence
follow from actual ideal-power membership. The degree-two statement
is q in I squared; it is not the different statement q squared in I.
The original sliced example with I=(a squared) and q=a cubed attains
the additional-divisor bound and prevents an unrestricted q in I
squared claim. One missing TeX backslash in the ideal-only example
was corrected before final recording, with no mathematical change.

General's six-equation
[square-support proof](rank-one-square-embedded-support-pass84.md)
received complete Root, Geometry and Jet reviews. Root separately
checked the final linear-rank refinement and its source-parameter
scope. The reductions at height at most two, the regular-parameter
auxiliary ideal, and the support/associated-prime argument give the
claimed finite embedded critical support. Rank-two first-power
membership also has a direct regular-local-ring proof. No actual
unmixedness or exclusion of embedded maximal primes was inferred.

General's five-equation
[return-determinant note](rank-one-return-jacobian-pass84.md) was read
through EOF by Root and Geometry. The variable-time chain rule factors the Jacobian
as M times Id+P d tau, with det M=1 and E(tau)=-2. The rank-one
determinant formula gives minus one. The genuine-pole example verifies
why this does not turn the return into a polynomial automorphism.
Geometry independently reconstructed the full variable-time factorization,
the fixed-z block determinant, and the genuine-pole control. Root and
Geometry also read the complete synthesis and this audit record.

The five-equation
[ideal-boundary note](embedded-square-ideal-boundary-pass84.md) and
its checker were read completely by Root and General. The first
example meets strict power containment and has a length-two embedded
square defect, but violates the actual trace relation at its leading
degree. The companion meets the trace relation and strict containment
but violates the second quotient determinant coefficient. Neither
example has an actual action realization.

## Source gates

The strict-slice power proof and return determinant are elementary.
Epstein--Hochster, *Continuous Closure, Axes Closure, and Natural
Closure*, printed pp. 20--21, is cited only to identify the established
term inner integral closure. Root and Geometry read the definition
and complete displayed Theorem 5.4 statement and proof. The preceding
valuation-equivalence dependencies were not freshly reconstructed and
are not needed for the new elementary proof.

The square-support result uses the exact Lipman--Sathaye Theorem 1,
printed p.199, and the minimal-reduction discussion on pp.203--204.
General, Geometry and Jet read the selected reduction discussion;
Root's earlier p.199--203 visual read was extended to the complete
printed p.204 for this argument. The auxiliary ideal has regular
associated graded ring in each application. The parameters d=0,1,2
are nonnegative; no possibly negative spread correction is used as
an ideal-power exponent. The core Theorem 2 proofs and the original
minimal-reduction reference remain published inputs, not freshly
reconstructed proofs. This is not a novelty audit.

## Exact finite controls and execution record

Root's [strict-slice checker](strict_slice_checks_pass84.py) has two
methods. Both check actual coordinate inverse maps in both directions,
the transported action and slice, the whole-z rational return, its
determinant, and the frozen Taylor certificate. One has supplied
good-variable slice degree two and verifies q in I squared. The
other has degree five and verifies the stated N=16 certificate,
the sharp extra common-divisor copy, and failure of q in I squared.
The arbitrary-degree monic reduction remains a written proof, not
an assertion that two finite examples establish it.

An initial author run was interrupted at rational involution
composition after symbolic expression expansion became expensive.
The saved process ended with KeyboardInterrupt, exit130, output chunk
55e472. Cancelling each rational component before composing removed
that representation blowup. No mathematical assertion failed or was
weakened. The subsequent two-method run passed in 0.224 seconds.
After adding the determinant check, the final author run passed in
0.243 seconds, chunk e8bc04. General independently read the complete
final checker and ran both methods successfully in 0.253 seconds,
chunk aa051f. Jet read the complete final checker as well.

Jet's [ideal-only checker](embedded_square_controls_pass84.py) has
one method. Its final strengthened examples passed in 0.074 seconds;
Root's independent run passed in 0.069 seconds, chunk cc23ed, and
General's run in 0.072 seconds, chunk 3c715e. Earlier GroebnerBasis
wrapper comparisons failed because of domains/options; comparing
canonical basis expressions fixed the harness. The separate ideal
note records both failed chunks and the replacement of the weaker
unfrozen examples. Neither was an actual-action counterexample.

Jet wrote the [print-only runner](run_targeted_pass84.py); Root read
it completely before executing it. The
[canonical capture](verification-pass84-working.json) contains two
suites and three passing methods. UTC start was
2026-09-14T10:22:18.247912+00:00 and finish was
2026-09-14T10:22:18.726973+00:00. Total monotonic wall time was
0.478799 seconds. The two unittest times were 0.246 and 0.068
seconds; the subprocesses ran in parallel. Both exit codes were zero.
All four input hashes stayed unchanged, and both complete outputs
are retained with their individual hashes. The saved capture SHA-256
is 9c4103bee1645dfc5dcebe41306d589ee2b59894eb6bebd2ede9906d1f9e9579.

There was no full84 regression or bounded action search. The retained
full75 evidence remains 146 suites and 1047 methods. Repeated runs,
helper calculations and ideal examples add no test methods beyond
the three defined methods. The central registry remains 544 claims.

## Integrity and unresolved scope

The preceding check-in was status only, classified as no progress.
This continuation completed the pass83 packet, obtained and checked
the new strict-slice proof, reviewed the local support refinement,
and added exact controls. It is therefore a progress turn, without
changing the unrestricted goal or treating a partial theorem as success.

The pass83 independent checkpoint audit caught and corrected a
missing nonzero-q_0 qualification in one degree-bound metadata item.
The final frozen83 checkpoint hash is
a38ac6020eb5ef3ca482d7f7d21b1541aa99b22882519f4a9e3b9fab7750d27d.
The read-only check at 2026-09-14T10:22:19.004Z validated all417
retained records through83. The
[checkpoint](checkpoint-pass84-working.json) keeps current hashes,
equation counts and later reviews separate from mathematical evidence.

General first-power membership, universal square membership, actual
coordinate reduction and unrestricted cancellation remain unproved.
The professor's intended field, dimension and correction are unconfirmed.
There has been no human expert review, formal verification, public
novelty claim, outside contact, posting or submission.
