# Recognition theorems for the original one-line cylinder

The strongest immediately applicable recognition theorem in this audit
still needs one ambient coordinate fixed by the sliced derivation. Recent
retract results add useful sparse certificates, but do not produce such a
coordinate, a sparse frame, or an intrinsic slice for an unknown cylinder
base. The original implication remains unproved here.

Throughout, the actual hypothesis is
\[
B=A[s]\simeq\mathbb C^{[4]},\qquad E=\partial_s,
\qquad \pi:B\longrightarrow A,
\quad \pi(b)=\sum_{j\ge0}\frac{(-s)^j}{j!}E^j(b).
\tag{1}
\]
The sum is finite, and \(\pi\) is evaluation at \(s=0\).
An affine-threefold factor known polynomial only after adjoining three
variables is not substituted for (1).

## 1. What the cylinder already supplies

The elementary arguments in [research-note.md](../research-note.md),
Sections 3--4, give a finitely generated smooth factorial three-dimensional
domain \(A\), constant units, and the algebra retraction \(\pi\).
The complex space \(\operatorname{Spec}A\) is contractible because its
product with a line is contractible and deformation-retracts onto it.

Every finitely generated projective \(A\)-module is free: extend it
to the polynomial ring \(A[s]\), apply Quillen--Suslin, and evaluate
at \(s=0\). Thus the tangent module is free. This is the already
recorded [pass-31 module argument](contractible-symmetry-pass31.md),
not a new recognition theorem. It does not turn a tangent basis into
locally nilpotent derivations or commuting complete vector fields.

That distinction has an actual source control. Hoyois, Krishna and
Østvær prove triviality of every vector bundle on Koras--Russell
threefolds of the first and second kinds. Their introduction also records
the Russell cubic's nonpolynomiality and contractibility. Such examples
therefore rule out recognition from the listed topological and bundle
conditions alone. Their one-line cylinders are not asserted polynomial
in this audit.[^bundles]

## 2. Exact primary recognition gates

The following statements were read at theorem level, with the indicated
proofs or surrounding hypotheses. They are not extrapolated from titles.

| Source | Applicable theorem | Missing input under (1) |
| --- | --- | --- |
| Bhatwadekar--Gupta--Lokhande, Theorem 3.5 | A nonzero \(k[T]\)-linear LND of \(k[T,X,Y,Z]\), in characteristic zero, has kernel \(k[T]^{[2]}\) if that kernel is regular. | An ambient coordinate \(T\) killed by \(E\). Regularity is already available. |
| Nagamine, Theorem 2.5 | Every characteristic-zero retract of \(k^{[3]}\) is polynomial. | The ambient ring in (1) has four variables, not three. |
| Chakraborty--Dasgupta--Dutta--Gupta, Theorem 5.8 | A dimension-two retract of \(k^{[n]}\) is polynomial in characteristic zero. | \(A\) has dimension three. |
| Dasgupta--Gupta, Theorem 4.6 | For an affine three-dimensional UFD over an algebraically closed characteristic-zero field, polynomiality is equivalent to \(\mathrm{ML}^*(A)=\mathbb C\), or to \(\mathrm{ML}(A)=\mathbb C\) plus an intrinsic sliced LND. | The slice in (1) belongs to an action on \(B\), not to an action on \(A\). |

For the first row, the complete displayed proof localizes at primes of
\(k[T]\), applies its DVR kernel result, and patches over the PID.
Deleting the fixed-coordinate hypothesis is not licensed by the proof
or the abstract.[^bgl] Nagamine's proof instead uses a surface
characterization, which explains its dimension restriction.[^nagamine]
The retract source and its related relative and graded statements were
read directly, with their displayed proofs.[^retracts]

Sai Krishna's characteristic-free extension, Theorems 4.1 and 4.5,
retains the intrinsic-slice condition. Its Lemma 5.1 gives
\(\mathrm{ML}^*(A[s])\subseteq\mathrm{ML}(A)\), not the reverse
inclusion. Thus the known value \(\mathrm{ML}^*(B)=\mathbb C\)
does not establish \(\mathrm{ML}(A)=\mathbb C\).[^dg][^krishna]

## 3. The recent sparse-retraction result

Chakraborty and Pal's August 20, 2026 revision, now titled
*Monomial and binomial retracts of polynomial rings*, contains a useful
current result: a binomial retraction over a UFD has polynomial image
(Corollary 6.11(ii)). Here every coordinate image must be a sum of at
most two monomials, and constants count as monomials. Proposition 5.7
also reduces the number of arbitrary images when some images are
monomials; its proof and Corollary 5.8 were read. None asserts that an
arbitrary retraction can be made sparse by a coordinate change.[^sparse]

Consequently, if an actual coordinate system \(x_1,\ldots,x_4\)
of \(B\) has all four \(\pi(x_i)\) binomial, then \(A\) is
polynomial. The coordinate system must come with an actual inverse,
not merely a constant Jacobian.

For the special retraction in (1), even one zero or monomial image is
enough. Here is a direct deduction, without applying a general sparse
retraction classification.

**Single-image criterion.** If, in an actual polynomial coordinate
frame, \(\pi(x_i)\) is zero or one monomial, then
\(A\simeq\mathbb C^{[3]}\).

If \(\pi(x_i)=c\) is constant, then
\(x_i-c\in\ker\pi=sB\). The coordinate polynomial \(x_i-c\)
is irreducible. Since \(s\) is a nonunit, \(s\) is a constant
multiple of \(x_i-c\), and is therefore a coordinate.

Otherwise \(\pi(x_i)=c\prod_jx_j^{a_j}\) is a nonconstant
monomial in \(\ker E\). The kernel of an LND on a
characteristic-zero domain is factorially closed. For example, its
degree function satisfies
\(\deg_E(fg)=\deg_Ef+\deg_Eg\), because the top Leibniz
coefficient is nonzero. Hence every coordinate occurring in that
monomial is killed by \(E\). The first row of the table finishes.

Thus any hypothetical counterexample to (1) satisfies this exact
necessary condition in **every** ambient polynomial coordinate frame:
\[
\#\operatorname{supp}\pi(x_i)\ge2\quad\text{for every }i,
\qquad
\max_i\#\operatorname{supp}\pi(x_i)\ge3.
\tag{2}
\]
The first assertion uses factorial closure and the constant-image case;
the second uses the published binomial theorem. This is a criterion
for rejecting a proposed counterexample with sparse data, not a proof
that a sparse frame exists. Term counts in one chosen frame do not
establish the universal condition (2).

## 4. Which apparent bridges are equivalent to cancellation?

For the fixed sliced pair in (1), each of the following conditions is
equivalent to \(A\simeq\mathbb C^{[3]}\):

1. The particular slice \(s\) is an ambient coordinate.
2. Some slice of \(E\) is an ambient coordinate.
3. \(E\) fixes an ambient coordinate, or equivalently this individual
   derivation has coordinate rank at most three in the four-variable ring.
4. Some ambient frame has a zero or monomial Taylor image.
5. Some ambient frame has all Taylor images binomial.

For 1 and 2, quotient by the chosen coordinate slice. Conversely,
polynomial generators of \(A\) together with \(s\) are coordinates.
For 3 use the regular-kernel theorem; its converse uses the same
adapted frame. The sparse implications were proved above, and their
converses follow by choosing that adapted frame, where the images are
the three kernel coordinates and zero.

Consequently replacing “prove cancellation” by “find a coordinate
slice,” “exclude sliced rank four,” or “find a sparse frame” does not
by itself reduce the universal theorem. It can provide a useful finite
certificate for an explicitly presented candidate, but existence is
the original unresolved burden.

Likewise an abstract grading of \(A\) is not automatically compatible
with the actual inclusion \(A\subset B\). Changing to an associated
graded ring must not be treated as a polynomial coordinate change.

## 5. A precise intrinsic bridge worth isolating

One remaining algebraic obligation, stated existentially, is:

> Under (1), find a nonzero intrinsic LND \(D\) of \(A\) whose
> actual kernel \(K=\ker D\subset A\) admits an algebra
> retraction \(\rho:A\to K\) restricting to the identity on \(K\).

This targets a concrete invariant inclusion rather than treating
smoothness of its quotient as a section theorem. It is unproved here.
It is also equivalent to cancellation under (1), not a newly proved
weaker universal hypothesis.

Corollary 4.3 of the retract paper gives \(A=K[t]\) from this
retract-kernel condition and factoriality. Composing \(\rho\pi\)
makes \(K\) a dimension-two retract of \(B\). Theorem 5.8 then
gives \(K\simeq\mathbb C^{[2]}\), hence \(A\simeq\mathbb C^{[3]}\).
Conversely a coordinate partial on polynomial \(A\) supplies the
kernel and evaluation retraction. Neither step asserts an automatic
section of an arbitrary quotient morphism.

The quantifier cannot be changed to “every intrinsic LND.” In the
genuine polynomial example
\[
A_0=\mathbb C[x,y,z],\qquad
D=x\partial_y+2y\partial_z,\qquad h=xz-y^2,
\tag{3}
\]
one has \(\ker D=\mathbb C[x,h]\), but this inclusion has no
retraction. To verify the kernel, localize at \(x\) and use
\(y/x\) as a slice. Denominators contract away because
\(\mathbb C[h]\to\mathbb C[y,z]\), \(h\mapsto-y^2\), is
injective; successively canceling a minimal power of \(x\) proves
the asserted intersection.

If \(\rho\) were a retraction, applying it to \(h=xz-y^2\)
would give
\[
h=x\rho(z)-\rho(y)^2.
\]
Modulo \(x\), this requires a polynomial in \(h\) whose square
is \(-h\), impossible by degree. The displayed derivation is
primitive, since its coefficients have no common nonunit factor.
Nevertheless \(A_0[s]\) is actually \(\mathbb C^{[4]}\).
Thus neither the full cylinder nor primitivity ensures this
retraction for a prescribed intrinsic action. The next task would
have to choose or construct a different intrinsic action and prove
its retraction, not simply improve the presentation of (3).

## 6. Audit boundaries and source inventory

The targeted search covered rank-four sliced LNDs, characteristic-zero
threefold cancellation recognition, polynomial-ring retracts, and recent
monomial/binomial retractions. The August 2026 revision is a genuine
update to the available retract results, not evidence of a general
solution. No primary theorem read in this audit supplies the missing
existence step. This is a statement about this bounded source audit,
not a claim that every paper or expert has been checked.

The coordinate equivalences and the control (3) have complete arguments
above; they are not claims of novelty. No new numerical experiment or
unittest count is attached to this literature note. The full conjecture
and the existential bridge in Section 5 remain open in this work.

[^bgl]: S. M. Bhatwadekar, Neena Gupta, Swapnil A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438), Theorem 3.5 and its full proof, Remark 3.6, PDF pp. 11--12. Read directly. Its fixed-coordinate and regularity assumptions are retained.

[^nagamine]: Takanori Nagamine, [*A note on retracts of polynomial rings in three variables*](https://arxiv.org/pdf/1811.04153), Theorem 2.5 and full proof, Lemma 2.3 and Theorem 2.2, PDF pp. 2--4. Read directly. This is the ambient-three-variable result, not an ambient-four-variable theorem.

[^retracts]: Sagnik Chakraborty, Nikhilesh Dasgupta, Amartya Kumar Dutta, Neena Gupta, [*Some results on retracts of polynomial rings*](https://arxiv.org/pdf/1910.11023), Proposition 4.2 and Corollary 4.3, Theorems 5.8--5.9, Corollary 5.10, Theorem 5.13 and Corollary 5.15, with their displayed proofs, PDF pp. 7--8 and 13--16. Read directly; the paper's earlier patching inputs remain cited external theorems.

[^dg]: Nikhilesh Dasgupta, Neena Gupta, [*An algebraic characterization of the affine three space*](https://arxiv.org/pdf/1709.00169), Theorem 4.6 and proof, Remark 4.7, PDF p. 9. Read directly. The ambient slice is not substituted for an intrinsic sliced action.

[^krishna]: P. M. S. Sai Krishna, [*An algebraic characterization of the affine three space in arbitrary characteristic*](https://arxiv.org/pdf/2308.05424), Theorems 4.1 and 4.5, Lemma 5.1 and its proof, and the proof of Theorem 4.5, PDF pp. 6--8. Read directly. No characteristic-free cancellation conclusion in dimension three is inferred.

[^sparse]: Sagnik Chakraborty, Madhuparna Pal, [*Monomial and binomial retracts of polynomial rings*, arXiv:2504.14382v2](https://arxiv.org/pdf/2504.14382v2), revision dated August 20, 2026, definitions in Section 1, Proposition 5.7 with full proof, Corollary 5.8 with proof, and Corollary 6.11 with proof, PDF pp. 1--3, 17--19 and 27--28. Read directly. The underlying full classification in Section 6 is an external theorem, not independently reconstructed here. The [version record](https://arxiv.org/abs/2504.14382) confirms the changed title and revision date.

[^bundles]: Marc Hoyois, Amalendu Krishna, Paul Arne Østvær, [*A1-contractibility of Koras--Russell threefolds*](https://arxiv.org/pdf/1409.1293), introduction and Corollary 3.7 with proof, PDF pp. 1--2 and 11. Read directly. This paper proves the stated bundle control; its finite-suspension theorem is not mislabeled an unstabilized cancellation theorem.
