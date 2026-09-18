# Current research status

[Home](../README.md) · [Plain-English introduction](start-here.md) · [Review guide](review-guide.md)

Mathematical checkpoint: September 18, 2026, through pass703.
This page is a reader's summary. The linked proof notes and dated ledger
contain the assumptions, arguments, and evidence.

## Bottom line

**The complex-threefold cancellation target remains unsolved here.**
There is no general proof or counterexample. Novelty is unknown. Human
expert review and full proof-assistant verification have not been obtained.
The professor has not confirmed the working interpretation of the field
and dimension in the original question.

## What the current notes establish

### 703: a conditional route to a translation

[Read the full proof](../research/raw-projection-centralizer-slice-criterion-pass703-working.md).

Let B be a complex polynomial ring and rho:B -> A a retraction with
nonzero principal kernel. Let D_i be the raw projected coordinate
partials, rho composed with partial_i and restricted to A.

The note proves that **any nonzero derivation X of A commuting with
every D_i is an LND with a slice**. It does not assume local nilpotence
of X or an initial product presentation B=A[s].

The missing hypothesis is not cosmetic: finding such an X is unproved
for an arbitrary cancellation input. In one displayed polynomial example,
the common centralizer at the specified slice is zero. This zero-centralizer
claim is not asserted for every slice or nonlinear coordinate frame.

### 702: a uniform obstruction to a particular extraction method

[Read the full proof](../research/all-slice-projected-lnd-obstruction-pass702-working.md).

In an explicit coordinate frame on C[a,b,c,u], with E=partial_u, the
note classifies constant ambient directions projected at **every**
polynomial slice u+h=0. The only locally nilpotent projections are
scalar multiples of D=a partial_b+b partial_c, which fixes a line.
Every nonzero projection is already primitive, so dividing out common
coefficient factors cannot repair an excluded projection.

The scope is that particular frame, arbitrary polynomial slice shifts,
constant affine reframings, and primitive division. It does not exclude
arbitrary polynomial combinations or nonlinear reframing. An explicit
nonlinear combination produces partial_c, a successful translation.
The base is already affine three-space, so this is not a cancellation
counterexample.

## What remains to be proved

The current route needs a construction of a nonzero compatible field
in a useful frame for **every** input A[s] isomorphic to C in four
polynomial variables. The conditional theorem does not provide that
construction. Alternatively, the main problem needs another global
recognition argument that avoids this requirement.

Formal approximations, finite searches, a unit Jacobian, or a failed
coordinate choice cannot be silently substituted for a polynomial
inverse or a universal existence argument.

## What the verification means

| Evidence | Present status | Limit |
| --- | --- | --- |
| Written proofs for702/703 | Complete working arguments in the linked notes | Still subject to mathematical scrutiny. |
| Separate full-source reviews | Three AI reviews per note, recorded in the ledger | Not human expert review. |
| Exact symbolic calculations | Inverse, projection, divergence, eliminant, and control identities checked as described in the ledger | Supporting calculations do not prove unrestricted claims by sampling. |
| Novelty | Unknown; bounded comparisons recorded | A search without a match is not a priority determination. |
| Formal verification | No full proof-assistant certification | No Lean-verified theorem is claimed. |

See the ledger entry titled
[“all-slice projection obstruction and a single-field translation criterion”](../research-ledger.md#september-18-2026-all-slice-projection-obstruction-and-a-single-field-translation-criterion)
for source hashes, read receipts, checks, attribution, and qualifications.

## Do not mistake historical indexes for current status

`claims.json` is dated September 13, 2026. The older experiment manifest
describes the frozen pass58–60 packet. Neither is a complete registry of
the latest results. Early notes and verification JSON retain their original
context; a historical "passed" flag is not current global certification.

No mathematical claim was upgraded by the navigation cleanup. The
[archive map](archive-map.md) explains how to use those older records.
