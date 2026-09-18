# Recognition under the full cusp initial-kernel hypothesis

Status: synthesis of working algebraic proofs. Separate source reviews
and finite exact controls do not amount to expert review, formal
verification, or novelty clearance.

The case split below recognizes every actual sliced frame with the
specified cusp initial kernel, subject to the retained proof inputs.
It does not supply such a frame for an arbitrary polynomial cylinder.

## Precise statement

Let
\[
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,
\]
where the four displayed generators are polynomial coordinates and
their exact E-degrees are \((1,1,2,2)\). Put
\[
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad d=E^2W/2.
\]
Assume the homomorphism from the formal polynomial four-ring to
\(A[\eta]\), with \(\eta\) independent, given by
\[
(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(a\eta,b\eta,e\eta^2,d\eta^2)
\]
has full kernel \((\mathsf X\mathsf Z-\mathsf Y^3)\).
Then the working arguments cited below imply
\[
A\simeq\mathbb C^{[3]}.
\]
The full-kernel requirement is stronger than the leading identity
\(ae=b^3\). No result in this note replaces it by that single equality.

## Exhaustive division of the actual chart

The [actual chart159](cusp-generic-chart-first-reductions-pass159-working.md)
constructs the selected nonzero LND
\(N=[u^3](\partial_Z|_A)\), its exact constant field
\(L=\operatorname{Frac}\ker_A N\), and the whole generic line
\(A_L=L[v]\). It supplies independent ratios
\(t=b/a,\rho=d/a^2\), the projected coordinate \(y\), and the
coefficient functions \(k,n\in L\).
Use \(r=k_\rho\) and \(s=n_\rho\) only in this fixed actual chart.

| Exhaustive branch | Working conclusion and proof |
| --- | --- |
| \(r\ne0,\ y\notin L\) | [Synthesis171](cusp-nonconstant-projected-coordinate-recognition-pass171-working.md) recognizes the kernel. It includes the nongraph exclusion, selected-extra-factor exclusion, and the degree-at-most-two, cubic, and quartic graph cases. |
| \(r\ne0,\ y\in L\) | [Field proof174](cusp-constant-projection-parabola-field-pass174-working.md) forces a projected parabola over \(\mathbb C(y)\). [Recognition174](cusp-constant-projection-global-recognition-pass174-working.md) removes its quadratic term and constructs an actual shear with a commuting coordinate partial. Wang's three-variable theorem and the regular-kernel theorem finish recognition. |
| \(r=0,\ s=0\) | [Exclusion172](cusp-zero-r-constant-projection-exclusion-pass172-working.md) proves that this actual branch cannot occur. This is exclusion, not a new family of examples. |
| \(r=0,\ s\ne0\) | [Normal form173](cusp-zero-r-coefficient-normal-form-pass173-working.md), [field forcing173](cusp-zero-r-field-forcing-pass173-working.md), and [global construction173](cusp-zero-r-global-coordinate-pass173-working.md) produce an invariant ambient coordinate and recognize the kernel. The genuine quadratic coefficient cover is allowed. |

There is no additional case: either \(r\) vanishes or it does not;
in the latter case \(y\) either belongs to \(L\) or does not;
in the former case \(s\) either vanishes or does not. All branches
retain the same actual chart, whole-line equality and finite
coefficient field. None silently changes these to arbitrary
formal determinant data.

In particular the proof does not assume a global slice for \(N\).
Nor does it assume that the initial cusp polynomial \(XZ-Y^3\)
itself is invariant, that every selected plane relation is pure,
that \(EX\) is a global unit, or that a generic field coordinate
automatically descends to the original polynomial ring.

## Exact remaining gaps toward the user's full question

Closing this table is not a proof that every sliced polynomial
four-ring has a frame satisfying its hypotheses.
The [initial bound157](two-linear-two-quadratic-initial-bound-pass157-working.md)
and [cubic normal forms157](two-linear-cubic-normal-forms-pass157-working.md)
leave other cases even within the exact E-profile \((1,1,2,2)\):

- The split cubic full initial kernel \((XZ+YW)\).
- Height-one initial relations of weight four.
- Height-two initial kernels, which must not be treated as principal.

These entries name the remaining cases in that retained reduction,
not a claim that each occurs as a counterexample.
For the split cubic,157 already supplies an actual polynomial-kernel
example; exclusion of every such frame would therefore be false.

The [three-good theorem156](three-good-all-degree-recognition-pass156-working.md)
recognizes an actual frame with three coordinates killed by \(E^2\),
without bounding the fourth degree. It does not prove that arbitrary
actions admit such a frame, or that their minimum total E-degree is
at most six. Higher minimizing profiles remain possible on the
current evidence. No new universal degree bound follows from this
cusp theorem.

Accordingly the unrestricted target
\(A[u]\simeq\mathbb C^{[4]}\Rightarrow A\simeq\mathbb C^{[3]}\)
remains open in this investigation. The professor has not confirmed
the field, dimension, or corrected interpretation of the emailed
statement. No public novelty or completion claim is made.

## Verification scope

This synthesis introduces no additional checker or execution.
The new174 finite suite checks the explicit determinant, derivative
compatibility, two-sided polynomial shear, and chart commutation.
It does not prove the field/localization argument or the imported
classification theorems. The173 suite is a separate completed run,
not counted again as174 evidence.

The case table uses saved source statements and their exact
hypotheses. This is not a fresh recursive certification of every
dependency in171. The proof notes state which results are imported,
including Wang's classification and Bhatwadekar--Gupta--Lokhande
Theorem 3.5. Those source statements have been checked in the primary
literature. AI agreement is not independent human expert review.

All173 and earlier proof artifacts remain unchanged. The active goal
is not complete, and there is no genuine external blocker to
continuing the remaining mathematical cases.
