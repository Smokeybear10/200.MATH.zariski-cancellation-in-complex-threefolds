# Proof reconstructions and verification for pass 20

This record distinguishes written argument audits, bounded exact computations,
and primary-source comparisons. No human expert review or proof-assistant
verification occurred. No audit establishes mathematical priority or solves
the unrestricted cancellation conjecture.

## 1. Root proof: fixed-frame multiplier and uncorrected pole

The main derivation is in
[the multiplier obstruction note](nonunit-inverse-obstruction-pass20.md).
It verifies the fixed-frame restriction a in C[f], the transformed monic
relation, the geometric-series slice, and the exact valuation ell-e.

A separate geometry/algebra agent read the whole proof and reconstructed
the leading coefficient. In particular, the divided-difference formula
justifies the hhat expansion without dividing by k in a residue ring,
and the Euler operator has no polynomial kernel in the stated degrees.
The positive direction proves only the first unchanged coordinate's
regularity. Both reviews retained that limitation.

## 2. Power-of-f coordinates

The coordinate agent wrote
[the nonunit local-slice proof](nonunit-local-slice-pass20.md).
The main agent read and reconstructed its complete power-of-f argument,
including the primitive kernel, both plinth branches, invariant replicas,
the Q correction, the polynomial surface-cylinder inverse, and the P lift.

A second algebra agent independently read the complete Sections 1-6
and reported no actionable gap. Its specific checks were:

- The Q correction at order e+1 retains ar modulo f^(e+1).
  No greater Q order is needed; the P correction handles the remaining
  finite-jet discrepancy.
- f is prime in the abstract surface cylinder, so hhat*N_x =
  f^(ed)*K_n forces polynomial xhat without a UFD assumption.
- Cylinder-variable independence of xhat modulo f^n follows from
  the two product identities, not a naive division losing ed orders.
- Before specialization, k-h^(d-1)Q^d is a-divisible, so B-b is
  fa-divisible. The middle correction retains its explicit h factor.
- The degree-one module of the nilpotent cone is free on x,h,r.
  This validates the vertex argument even though f is nilpotent.
- The inverse is constructed in an independent ring before its
  polynomiality is asserted.

The main reconstruction independently checked the exceptional quadratic
constant-residue branch. Its minimal plinth is f^n*k rather than
f^(n+e)*k; the displayed local slice alone does not certify minimality.

## 3. Arbitrary-multiplier CRT and the f-1 contrast

The coordinate agent subsequently wrote Sections 8-9. The main agent
read and reconstructed both sections, including the primewise
divisibility, e=0 case, repeated roots, and exact residue degrees for
a=f-1,Q=h. A different geometry/algebra agent conducted the full
[independent CRT audit](crt-audit-pass20.md).

No algebraic defect was found. Two exposition issues were corrected:
the arbitrary-a inverse compositions are checked after inverting af,
and coefficient sufficiency is stated with (13) for pure powers but
with the stronger (27) for arbitrary a. The latter is not asserted
necessary. The quadratic constant-Q control explicitly disproves that
unqualified necessity claim.

The CRT audit also reran all six new coordinate-checker methods.
That repeated run is not an additional method count.

## 4. Published cylinder and two-stage modification reductions

The literature/algebra agent wrote the
[literal cylinder comparison](cylinder-comparison-pass20.md).
The main agent read the complete note and reconstructed its BPV input
substitution, transported ideal, physical two-fraction presentation,
weighted-overring extension, and direct f-power presentation obstruction.
The six additional direct cylinder identities are controls, not six
new unittest methods.

The subsequent [priority-boundary note](priority-boundary-pass20.md)
reduces both weighted lifts to two applications of Kaliman-Zaidenberg's
Proposition 2.1. The main agent read the entire note and independently
verified the intermediate domain presentations and saturation identities.
It also read the complete primary Proposition 2.1 and its proof.

The coordinate agent separately audited Sections 2-4 and independently
read the primary Proposition 2.1 and Corollary 2.2. Its checks included:

- The first curve ideal is the full scheme-theoretic ideal, with
  quotient (C[f]/f^n)[x], not merely its radical.
- The intermediate presentations are domains and have inverse
  generators on localization, so no saturation component is omitted.
- In B_P/(f^m), the x-localization kernel is exactly (H).
  The image of x differs from x by a nilpotent, hence transports
  the full second center.
- The Q-stage argument works over C[f]/a^(d-1), including
  nonsquarefree a, with h and W in place of x and H.
- The source lifting proposition applies to affine domains and
  full ideals; it has no reduced-center or smoothness requirement.

No defect was identified. This audit confirms an implication from known
machinery, not novelty. The separate Freudenburg source comparison
retains the construction/recognition distinction.

## 5. Actual nodal conductor surface

The geometry agent wrote
[the conductor construction](nodal-conductor-pass20.md).
The main agent read the complete note and reconstructed finite generation,
normalization, the exact conductor, completed local rings, descent of the
LND, its invariant ring, the node fiber, and the compact-support
connecting homomorphism.

The main agent read the relevant Stacks finite-generation and pushout
statements with proofs and Kollár's double-normal-crossing residue
criterion. The residue scaling, pairwise cancellation, and integral
maximal minors were checked explicitly. The written proof distinguishes
a global integral surface from its two-branch completions.

No global three-generator presentation, embedding into C3, ambient
primitive LND, or disjoint partner surface is constructed. The local
quotient models and matching compact-support groups do not supply them.

## 6. Actual complete regression

The main execution ran from 2026-09-13 04:23:50 UTC through
04:25:09 UTC. All 437 test methods across 33 suites passed.
The exact commands, timings, counts, and exit statuses are in
[verification-pass-20.json](../verification-pass-20.json).

The new suites are:

| Suite | Methods | Main recorded unittest time |
| --- | ---: | ---: |
| multiplier_surface_controls_pass20.py | 11 | 2.282 seconds |
| nonunit_local_slice_checks_pass20.py | 6 | 0.557 seconds |

Both use exact SymPy algebra and import no project solver or other
project checker. Finite examples do not independently prove the general
kernel/plinth theorems, the global geometric statements, or the cited
external results. Repeated runs and isolated additional identities are
not counted as extra test methods.

The general goal remains active and unsolved. These were substantive
restricted proofs, inverse repairs, and a realizability control, not a
completion certificate for arbitrary cancellation.
