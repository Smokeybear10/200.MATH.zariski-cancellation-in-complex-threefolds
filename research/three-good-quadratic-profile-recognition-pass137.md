# Recognition of every supplied three-good quadratic frame

The recorded working proofs now cover every sliced polynomial
fourfold supplied with three affine-in-time coordinates and a fourth
coordinate of time degree at most two. The remaining nonlinear
conical case is excluded by the speed-based tangent argument137.
This note records the exhaustive case split and its inherited inputs.

It does not produce this coordinate profile for an arbitrary sliced
action. Unrestricted complex-threefold cancellation remains unresolved.

## 1. Exact coverage statement

Let the displayed generators be actual polynomial coordinates and assume
\[
B=\mathbb C[x_1,x_2,x_3,z],\qquad
E\in\operatorname{LND}_{\mathbb C}(B),\qquad Eu=1,\qquad
E^2x_1=E^2x_2=E^2x_3=0,\qquad E^3z=0 .
\tag{1}
\]
Put \(A=\ker E\). Then, using the working theorems listed below,
\[
A\simeq\mathbb C^{[3]} .
\tag{2}
\]
Consequently there are polynomial generators \(p_1,p_2,p_3\)
of \(A\) for which
\(B=\mathbb C[p_1,p_2,p_3,u]\).
The given slice becomes part of an actual coordinate system as a
conclusion; that property is not an entry assumption.

Write \(a_i=Ex_i\), \(q=E^2z\), and
\(r=\operatorname{trdeg}_{\mathbb C}\mathbb C(a_1,a_2,a_3)\).
If a speed is nonzero, the intrinsic leading-LND construction125
gives a nonzero LND on \(A\) fixing all three speeds.
Its invariant field has transcendence degree two, so \(r\le2\).
If all speeds vanish, \(r=0\) directly.
Thus no speed-rank-three case has been omitted.[^1]

## 2. Exhaustive proof-dependency table

Apply the first row when \(q=0\). In all subsequent rows assume
\(q\ne0\).
Put \(W_2=\operatorname{span}_{\mathbb C}\{a_i a_j:1\le i\le j\le3\}\).

| Remaining condition | Resolution | Exact working input |
| --- | --- | --- |
| \(q=0\) | All four original coordinates are nice, so \(A\simeq\mathbb C^{[3]}\). | Nice-slice80, Sections 1--2. |
| \(r\le1\) | Recognition, with no restriction needed on the last coordinate's time degree. | Speed-curve127, Sections 1--7; rank zero is handled directly in Section 2. |
| \(r=2\), with a nonzero homogeneous linear speed relation | The corresponding linear good coordinate is invariant; regular-kernel recognition applies. | The direct argument in Section 3 below and Bhatwadekar--Gupta--Lokhande Theorem 3.5. |
| \(r=2\), with a homogeneous speed relation but none linear | This nonlinear conical case cannot occur with the supplied slice and quadratic profile. | Universal conical tangent137, Sections 1--5, using the general monic-pencil and fixed-point-free obstruction from136. |
| \(r=2\), no homogeneous speed relation, and \(q\in W_2\) | A quadratic shear of the bad coordinate gives a nice frame; then recognize. | The explicit shear below and nice-slice80, Sections 1--2. |
| \(r=2\), no homogeneous speed relation, and \(q\notin W_2\) | A primitive mixed-cubic relation exists, both corrections pass, and the kernel is polynomial. | Leading dichotomy133, Sections 1--4; correction-existence134, Sections 1--7, especially its direct normalization in Section 6 and normalized classification132, Sections 1--5. |

These inputs are separate working proofs, not consequences inferred
from their checkpoint labels.[^2][^3][^4][^5]

## 3. Why the cases and transformations are exact

At rank two the speed evaluation kernel in
\(\mathbb C[T_1,T_2,T_3]\) is a height-one prime.
If it contains a nonzero homogeneous polynomial, an irreducible
factor generating that prime is homogeneous: factors of a
homogeneous polynomial in this positively graded polynomial ring
are homogeneous. Its degree is either one or at least two.
These are precisely the third and fourth rows.

If there is no homogeneous relation, then the three elements
\(\eta a_i\), for an independent indeterminate \(\eta\), are
algebraically independent. Indeed any polynomial relation among them
can be separated into its powers of \(\eta\), producing a nonzero
homogeneous relation among the \(a_i\). This is exactly the dense
homogeneous-cone hypothesis required in133 and134.
There is no other rank-two cone case.

In the linear-relation row, take a nonzero constant row \(c\) with
\(\sum c_i a_i=0\). Then \(v=\sum c_i x_i\) is an actual
invariant coordinate. The slice theorem gives \(A\simeq B/(u)\),
and the polynomial identity
\(1=Eu=\sum E(x_i)u_{x_i}+(Ez)u_z\) makes this hypersurface
smooth, hence \(A\) regular.
The nonzero \(\mathbb C[v]\)-linear LND on
\(B=\mathbb C[v]^{[3]}\) therefore satisfies every hypothesis of
the published regular-kernel theorem.[^3]

For the quadratic-span row, choose a constant-coefficient homogeneous
quadratic \(J_2\) with \(q=2J_2(a)\). The change and its inverse are
\[
z'=z-J_2(x_1,x_2,x_3),\qquad
z=z'+J_2(x_1,x_2,x_3),\qquad
E^2z'=q-2J_2(a)=0 .
\tag{3}
\]
It fixes the goods and preserves the actual global slice and LND.
No unit-speed-row assumption is needed.
The \(q=0\) row is the same nice endpoint without a shear.

In the final row,133 proves the existence of
\(L(a)q=2F_3(a)\) with \(\gcd(L,F_3)=1\);
that relation is not an extra hypothesis.
The full134 argument then constructs the invariant and an explicit
normalized cubic presentation. Its Section 6 invokes132,
Sections 1--5, directly. It does not require the invariant-suspension
topology theorem130 or the geometric normalization in132, Section 6.

## 4. Inherited status and the remaining entry problem

This is a synthesis of written working proofs. It inherits their
mathematical and source dependencies rather than replacing them with
a new numerical certificate. In particular:

- The nice endpoint80 retains its geometric and invariant-quotient
  inputs. They are not removed by the conical argument137.
- Speed-curve127 retains polynomial curve factorization and the
  regular-kernel theorem.
- Dense primitive recognition134 and conical exclusion137 retain
  their stated classical rational-field and three-variable
  linear-invariant or classification theorems.

The case-coverage argument adds no new theorem about arbitrary
coordinate entry. From \(A[u]\simeq\mathbb C^{[4]}\), one obtains
a sliced LND, but not automatically three generators killed by
\(E^2\) and a fourth killed by \(E^3\).
A hypothetical nonpolynomial cylinder kernel must therefore avoid
every actual coordinate frame satisfying (1).
This is a restriction on a hypothetical counterexample, not a
construction of the needed frame.

The synthesis does not assert human expert review, proof-assistant
verification, or historical novelty. Finite symbolic controls for
individual identities do not independently establish all these
working theorem inputs or solve unrestricted cancellation.

## Sources

1. [An intrinsic additive action fixing every good-coordinate speed](three-good-intrinsic-speed-quotient-pass125.md),
   Sections 2--5. The rank bound uses the elementary local-slice
   field calculation, not the additional quotient-plane assertion
   in Section 6.
2. [Recognition of nice sliced actions on complex four-space](nice-slice-recognition-pass80.md),
   Sections 1--2; [Recognition of a supplied three-good frame with a speed curve](three-good-speed-curve-recognition-pass127.md),
   Sections 1--7.
3. S. M. Bhatwadekar, Neena Gupta and Swapnil A. Lokhande,
   [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/html/1501.01438v1),
   Theorem 3.5. Exact invariant-coordinate and regular-kernel endpoint.
4. [A speed-based tangent chart for nonlinear conical frames](universal-conical-tangent-reduction-pass137.md),
   Sections 1--5. Its final argument uses the separately general
   Sections 3 and 5 of [the136 monic-descent and fixed-point-free obstruction](conical-nonradial-quartic-coordinate-pass136-working.md).
5. [A quadratic-or-primitive-cubic dichotomy for actual coordinate initials](three-good-quadratic-cubic-leading-dichotomy-pass133.md),
   Sections 1--4; [A weight-three invariant in every supplied primitive quadratic frame](primitive-cubic-correction-existence-pass134-working.md),
   Sections 1--7; [Classification of irreducible actions preserving a normalized cubic suspension](normalized-cubic-action-classification-pass132.md),
   Sections 1--5.

[^1]: [Intrinsic-speed125](three-good-intrinsic-speed-quotient-pass125.md), Sections 2--5.
[^2]: [Nice-slice80](nice-slice-recognition-pass80.md), Sections 1--2; [speed-curve127](three-good-speed-curve-recognition-pass127.md), Sections 1--7.
[^3]: Bhatwadekar--Gupta--Lokhande, [Theorem 3.5](https://arxiv.org/html/1501.01438v1).
[^4]: [Universal conical137](universal-conical-tangent-reduction-pass137.md), Sections 1--5.
[^5]: [Leading dichotomy133](three-good-quadratic-cubic-leading-dichotomy-pass133.md), Sections 1--4; [primitive correction134](primitive-cubic-correction-existence-pass134-working.md), Sections 1--7.
