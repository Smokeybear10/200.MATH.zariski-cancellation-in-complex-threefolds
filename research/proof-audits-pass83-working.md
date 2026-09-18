# Return-map proof and verification audit

The completed working argument proves integral dependence of the actual
acceleration over the full good-speed ideal, cubic membership, and the
absence of isolated good-speed zeros. It assumes the sliced polynomial
four-variable action and the three nice coordinates stated in the
[synthesis](rank-one-return-frontier-pass83.md). It does not prove the
unrestricted cancellation conjecture or recognize every such action.

## Written reconstructions

Geometry derived the rational return involution from the original
polynomial flow. Root independently supplied the valuation argument
and the explicit frozen-direction Taylor equation. General and Geometry
reconstructed both. The final
[return-map note](rank-one-return-map-integral-closure-pass83.md) contains
ten numbered equations, including the monic ideal-integrality certificate,
the regular-return sufficient condition, and the precise cubic-power
application. Root, General and Jet read the complete final argument.
The frozen directional derivatives act on b_0 only, not on the entries
of the direction f. This distinction was expressly checked.

The power step is algebraic: the Rees algebra is integral over its
third Veronese subring. Transitivity and homogeneous coefficient
extraction put q_0 cubed in the integral closure of the third power
of the ideal. Lipman--Sathaye then puts it in the ideal itself.
The optional valuation reconstruction is not needed by this main proof.

General's eight-equation
[socle note](rank-one-cubic-acceleration-socle-pass83.md) was independently
read in full by Root, Geometry and Jet. It combines the actual flow
determinant with the field-characteristic-zero Jacobian/socle theorem.
The colon ideal is the intersection of the maximal ideals of isolated
points. Combining this with cubic membership makes that set empty.
Embedded points on positive-dimensional components are not isolated
points and are not excluded by the argument.

Root reread both complete saved mathematical notes and the complete
[source record](primary-source-scope-pass83.md) during integration.
Jet independently read the full four-equation synthesis against those
notes and checked the saved canonical verification record. That audit
reported no discrepancy. These are separate AI reviews, not independent
human expert review or machine-checked proofs.

## Published inputs and read limits

The source record preserves the precise original URLs and local hashes.
For the cubic application, Root and Geometry visually inspected
Lipman--Sathaye printed pages 199--203, including Theorem 1 and its
deduction, the core Theorem 2 statement, and the auxiliary lemma and
proof. The later core Theorem 2 proofs were not freshly reconstructed.
Jet separately inspected page 199. Later reading of pages 203--204
for the separate conditional square argument does not change this
packet's mathematical claim or source-read boundary.

For Hickel, Root and General inspected the complete field statement,
the relevant residue inputs in Section 2, and the field-specialized
proofs in Section 3. The broader Artinian-base alternatives are not
used. Jet inspected the displayed field statement; Geometry read the
complete new socle deduction without claiming a fresh Hickel proof read.
The original residue-theory dependencies and the second half of the
paper were not audited in full. No novelty certification follows from
these bounded applicability checks.

## Exact finite controls

The [checker](rank_one_return_checks_pass83.py) has three methods:

1. An actual polynomial two-speed coordinate frame, its inverse and
   slice, its rational return involution, and its nontrivial Taylor
   integral equation with the direction held fixed.
2. An integrable isolated polynomial jet satisfying the earlier
   quotient identities, but whose attempted full lift has a nonconstant
   Jacobian determinant. It is not an actual action counterexample.
3. An ideal-integrality example that is not ideal membership, and an
   explicit weighted-valuation obstruction for the isolated jet.

The actual return can have a pole even when acceleration belongs to
the speed ideal. Hence regularity of the return was checked as a
sufficient condition only. Finite controls do not verify a universal
theorem or exhaust all polynomial actions.

The checker SHA-256 is
1ef8779766686d8c324ca8074aa47814e5d04e62af2e2f1cf344af0297fb0639.
The print-only runner SHA-256 is
ad533ef399cde6b12991a503b357758af3f79146ef42f01db6a9de9d37ddd52e.
The author run passed in 0.154 seconds, Root's direct run in 0.147
seconds, and General's independent run in 0.148 seconds. Repeated
runs do not add test methods. The checker and control note were read
in full by their author, Root and General.

Root executed the [canonical runner](run_targeted_pass83.py). Its
[saved capture](verification-pass83-working.json) records three passing
methods in one suite, 0.138 seconds of unittest time and 0.318398
seconds of monotonic wall time. It started at
2026-09-14T10:03:11.591812+00:00 and ended at
2026-09-14T10:03:11.910515+00:00, with exit code zero. All three
tracked input hashes were unchanged. The full retained stdout hash is
7dd787818ee05c305054c039c650ac0baea9cef626e58c8d5094b68172d6d9f3.
Jet independently rehashed the three inputs and complete stdout and
confirmed the count, timing and scope fields. The saved capture hash is
677e16338d590b1ddd4e2f6521687008181f0f68a81c19ad325d358a4b228cd2.

No new search or full regression ran in this pass. The last full75
capture remains 146 suites and 1047 methods. The historical central
registry remains 544 claims and is not updated by this packet.

## Persistence and remaining obligations

The immediately preceding user check-in was status only and is
classified as no progress. This continuation performs proof/source
review and integrates the completed working result; it also investigates
the separate conditional square-support argument in pass84. That later
argument is not silently incorporated into the frozen pass83 theorem.

The predecessor hash check at 2026-09-14T10:03:12.192Z validated all
407 retained records through pass82. The
[checkpoint](checkpoint-pass83-working.json) records a fresh final
predecessor check and the exact current file hashes. File checks,
equation numbering and saved-output hashes are integrity evidence,
not mathematical proof certificates.

First-power membership, universal square membership, a valid coordinate
reduction, and unrestricted cancellation remain unresolved. The intended
field, dimension and correction of the professor's statement remain
unconfirmed. No human review, formal verification, public novelty claim,
external contact, posting or submission has occurred.
