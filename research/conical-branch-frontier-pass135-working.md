# The remaining conical branch of the cancellation investigation

A supplied three-good quadratic coordinate frame now admits a sharper
case split. In the conical branch, the selected last-coordinate partial
has adjoint degree at most one. A radial identity for the quadratic coefficient then separates
a degree-two-or-three cone equation from a different branch whose four
partial degrees sum to at most seven.

These are working mathematical restrictions on a special coordinate
presentation. They do not prove that the remaining branches have
polynomial kernels, and do not produce that presentation for an arbitrary
cylinder. Unrestricted complex-threefold cancellation remains unresolved.

## 1. Assumptions and terminology

Let
\[
B=\mathbb C[x_1,x_2,x_3,z]=A[u],\qquad
E=\partial_u,\qquad A=\ker E,\qquad
E^2x_i=0,\qquad E^3z=0.
\]
The four original generators must be actual polynomial coordinates.
Write \(a_i=Ex_i\) and \(q=E^2z\). The speed field
\(\mathbb C(a_1,a_2,a_3)\) is assumed to have transcendence degree two.
Assume \(q\ne0\) here, so the last coordinate has exact time degree two.
The zero-acceleration case is already a nice frame and belongs to the
separate [retained recognition theorem80](nice-slice-recognition-pass80.md).

In the conical branch, the speed relation is an irreducible homogeneous
polynomial \(H(a_1,a_2,a_3)=0\). A linear \(H\) already supplies an
invariant linear coordinate and a retained recognition route. The
unresolved sector considered here has \(\deg H\ge2\).

The selected partial \(T=\partial_z\) fixes the three original goods.
Its leading intrinsic locally nilpotent derivation \(N\) on \(A\) fixes
the speeds and \(q\). Put \(L=\operatorname{Frac}(\ker_A N)\).
The extension \(L/\mathbb C(a_1,a_2,a_3)\) is finite and separable.
The Euler derivation of the homogeneous speed ring extends uniquely to
a derivation \(\mathcal R\) of \(L\), with \(\mathcal R(a_i)=a_i\).
No polynomial coordinates for \(L\), or polynomial generation of its
subring by the speeds, are assumed.[^1]

## 2. The selected partial

The actual volume and its cofactors prove
\[
[E,[E,T]]=0.
\]
The horizontal coefficients alone are not sufficient: the proof also
removes a possible quadratic term in \(T(u)\), using a locally nilpotent
leading derivation on the original ring. In the nonlinear conical case
the degree is exactly one, since degree zero would give a homogeneous
linear speed relation.[^1]

Writing \(T|_A=D+uN\) and \(T(u)=h_0+h_1u\), the first commutator is
\(Q=[E,T]=N+h_1E\). The coefficient \(h_1\) need not vanish.
Although \(T(\ker N)\subset A\), preservation of \(\ker N\) would
additionally require \(N(Df)=0\) for every \(f\in\ker N\).
Degree one by itself does not supply that condition.

## 3. The radial split

| Condition in the actual coefficient field | Working deduction | Remaining obligation |
| --- | --- | --- |
| \(\mathcal R(q)\ne2q\) | The full coordinate-initial kernel is \((H)\), and \(\deg H\in\{2,3\}\). | Recognition for the quadratic and cubic cones. |
| \(\mathcal R(q)=2q\) | Each good partial has adjoint degree at most two; the bad partial has degree at most one. The full initial kernel has height two. | Recognition or reduction of the resulting degree profile. |

For the first row, the derivation
\(\mathcal R-\eta\partial_\eta\) kills the three good initials
\(\eta a_i\) but moves \((q/2)\eta^2\). The bad initial is therefore
transcendental over the good-initial field. This proves the entire
initial kernel assertion before a multiplicity estimate is used.
A good original partial lowers original weight by one and raises slice
degree by at most three. Exact repeated differentiation then bounds the
drop by four times the relation multiplicity. Degree four would force
linear filtered growth for \(A\), contradicting its three algebraically
independent invariants.[^2]

For the second row, the cubic horizontal cofactor of each good partial
is a signed two-speed Jacobian minor multiplied by \(2q-\mathcal R(q)\).
After its cancellation, the actual leading-derivation argument also
removes the cubic vertical coefficient. Thus the partial height is at
most eleven. Invoking the additional retained height-ten recognition
theorem leaves only sorted profile \((1,2,2,2)\) for an unrecognized
instance. That last statement inherits the earlier working theorem; it
is not a new recognition proof.[^3]

## 4. Verification and classical inputs

The proofs distinguish actual original-ring identities from calculations
over a coefficient field. Finite symbolic cofactor controls can check
signs and cancellations but cannot establish actual coordinate
realization, universal local nilpotence, or cancellation.

Leading-derivation homogenization is a classical technique. Daigle's
discussion explicitly requires a finite derivation degree before taking
the homogeneous leading part. Here the relevant degree bounds and the
Laurent-parameter specialization are proved in the actual product
\(A[u]\).[^4] The repeated-derivative multiplicity method is also
classical; Vénéreau's ordinary-degree theorem is a comparison, not a
black-box theorem for the slice filtration.[^5]

The restrictions above have not received human expert review,
proof-assistant verification, or comprehensive statement-level novelty
clearance. No publication claim follows.

## Sources

1. [Conical selected-adjoint bound](conical-three-good-adjoint-degree-pass135.md),
   Sections 1–4, and [intrinsic speed construction](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2–5. Actual rings, coefficient fields and degree reduction.
2. [Nonradial cone-degree bound](conical-nonradial-degree-bound-pass135.md),
   Sections 1–5. The entire initial kernel, multiplicity and growth.
3. [Resonant good-partial bounds](conical-resonant-good-partial-bounds-pass135.md),
   Sections 1–4, and [retained height-ten recognition](height-ten-closure-pass73.md).
   The height consequence uses the latter as a separate working input.
4. Daniel Daigle. *Tame and wild degree functions*. arXiv:1007.0508v1,
   July 3, 2010, Theorem 1.7 and Section 1.9.
   [Primary text](https://arxiv.org/html/1007.0508v1).
5. Stéphane Vénéreau. *A parachute for the degree of a polynomial in
   algebraically independent ones*. arXiv:0704.1561v2, May 7, 2007,
   pp. 1–3, Property (2), main theorem and multiplicity lemma.
   [Primary text](https://arxiv.org/pdf/0704.1561).

[^1]: [Selected-adjoint proof135](conical-three-good-adjoint-degree-pass135.md), Sections 1–4; [nonradial proof135](conical-nonradial-degree-bound-pass135.md), Section 1.
[^2]: [Nonradial proof135](conical-nonradial-degree-bound-pass135.md), Sections 2–4.
[^3]: [Resonant proof135](conical-resonant-good-partial-bounds-pass135.md), Sections 2–4; [height-ten working theorem73](height-ten-closure-pass73.md), Sections 1–2.
[^4]: Daigle, [Theorem 1.7 and Section 1.9](https://arxiv.org/html/1007.0508v1).
[^5]: Vénéreau, [pp. 1–3](https://arxiv.org/pdf/0704.1561).
