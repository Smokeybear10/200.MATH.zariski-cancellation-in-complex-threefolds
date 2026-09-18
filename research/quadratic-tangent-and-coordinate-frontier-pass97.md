# Quadratic fiber exclusion and the remaining degree defect

In the supplied nonconical quadratic frame, every closed quotient
fiber has total generic multiplicity at most three. Every component
has multiplicity at most two. A fiber containing a fixed component
can therefore have only profile (2) or (2,1), where the entries are
the whole-fiber multiplicities, not the lengths of the fixed scheme.

The proof combines an exact finite local cover with the integral
topology of the actual quotient. It rules out all total-four
configurations without a first-normal-action hypothesis. A weighted
version explains the obstruction to extending this argument: in any
total-three fiber, including a surviving (2,1) fiber, every admissible
linear projection has generic degree four and special dimension three,
so the relevant flat module is not finite.

These are restricted deductions, not a solution of the cancellation
conjecture. The assumptions defining the original frame remain an
independent obstacle to reaching that conjecture.

## 1. Target and hypotheses

The working target is the unconfirmed interpretation of the
professor's question as complex-threefold cancellation:
\[
A[u]\simeq\mathbb C^{[4]}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{1}
\]
The email's stated conclusion \(X\simeq\mathbb A^1\) has the wrong
dimension for general \(r\). Neither its intended field and dimension
nor the corrected interpretation has been confirmed.

The present calculation assumes more than (1). In actual original
coordinates \(B=\mathbb C[x_1,x_2,x_3,z]=A[u]\), there is an LND E
with canonical slice \(u=Ez/q\), \(Eu=1\), \(E^2x_i=0\),
and \(E^2z=q\in\mathbb C^*\).
Its retained nonconical construction supplies a canonical primitive
LND N on A, full kernel \(S=\mathbb C[s_1,s_2]\), and
\(A=S[A_1,A_2,c]\). Writing \(K=\operatorname{Frac}S\), the generic
ring is \(A_K=K[v]\), with degrees at most two for the actual
generators \(A_i\) and at most four for c.

The actual quotient \(X=\operatorname{Spec}A\to\operatorname{Spec}S\)
is faithfully flat, and X is smooth, factorial and contractible.
Every base prime divisor remains prime in A. Its whole generic
divisor field is \(k'_p(w)\), with \([k'_p:k_p]\le2\), not merely
the field of the image of selected generators. The
[retained dependency argument96](irreducible-fiber-dependency-audit-pass96.md)
specifies the quotient-homology input from Kaliman.[^kaliman]

The [previous synthesis96](quadratic-fiber-recognition-frontier-pass96.md)
also gives smooth, disjoint, entire affine-line reduced components
and everywhere quotient rank at least one. A noncollapsed fixed
component is the whole reduced fiber, with multiplicity two.
Here collapsed means both actual relative good generators \(A_1,A_2\)
are constant on the component. The results below retain these
assumptions rather than infer them from a finite integer table.

## 2. Saturation produces the missing finite cover

Let \(\mu_i\) be the generic length of the entire closed fiber
along component \(C_i\). Choose a complex linear combination
\(U=\lambda_1A_1+\lambda_2A_2+\lambda_3c\) that is nonconstant on
each component. If the total multiplicity is four, the retained
flat-rank inequality forces equality everywhere:
\[
4=\sum_i\mu_i
\le\sum_i\mu_i[\kappa(C_i):\mathbb C(\bar U_i)]
\le\deg_v U\le4.
\tag{2}
\]
In particular every residue degree is one.

Put \(T=(S[U])_{\mathfrak m S[U]}\), a regular local ring of
dimension two. The semilocal component localization of A is flat
over T, with generic rank and residue dimension both four.
The [flat-rank lemma93](nonconical-saturated-flat-rank-pass93.md)
makes it finite free. Its proof uses graded independence and
faithful flatness of completion; it does not apply Nakayama's
lemma to a module whose finiteness is unknown.[^completion]

Moreover this semilocal ring equals the entire actual base change
\(D=A\otimes_{S[U]}T\). Indeed it is an integral localization of D,
and an integral localization of a domain cannot invert any new
element. Thus D is finite free of rank four. No component or
normalized branch is permitted to disappear at this step.

## 3. Finite normalization meets the integral component basis

The [source-balance proof97](quadratic-saturated-source-balance-pass97.md)
normalizes an actual prime exceptional surface. Above a normalized
source-curve point a on a base branch j, its finite function-field
extension has degree \(4/N_j\), where \(N_j\) is one or two.
Finite normalization is justified on the actual affine variety
and its localized curve, not on a freely chosen formal model.[^normalization]

A discrete-valuation calculation counts this degree as the sum
of ramification index times residue degree. A generic complex
U-section turns a residue-degree-f normalized curve into f
distinct transverse points, each contributing its ramification
index to the actual positive winding number. Consequently
\[
\sum_i(v_i)_a=\frac4{N_j}\in\{2,4\},
\qquad
v_i\text{ form a }\mathbb Z\text{-basis of }
L=T_{\rm ram}^{-1}(\mathbb Z\mathbf1),
\qquad T_{\rm ram}v_i=\mu_i\mathbf1.
\tag{3}
\]
The detailed proof checks finite normalization, surviving labels
and generic transverse sections separately. It does not assume
that normalization commutes with every special fiber.

Every entry of \(v_{\rm tot}=\sum_i v_i\) is even, and
\(T_{\rm ram}(v_{\rm tot}/2)=2\mathbf1\); therefore
\(v_{\rm tot}/2\in L\). But the sum of a basis is primitive in
that lattice, because its basis coordinates are all one.
This contradiction proves the total-four exclusion.

A component of multiplicity three would then be the whole
reduced fiber, contrary to the retained whole-irreducible
multiplicity restriction. Since a multiplicity-one component
has nonzero translation action, the conclusion is
\[
\sum_i\mu_i\le3,\qquad \mu_i\le2,\qquad
\text{fixed-fiber profiles only }(2)\text{ or }(2,1).
\tag{4}
\]
There cannot be two fixed components in a fiber. This does not
exclude the remaining single double component.

The [supported-lattice calculation97](quadratic-supported-lattice-pass97.md)
still records the now-excluded (3,1) and (2,2) columns as
conditional intermediate results and exact finite controls.
The lattice alone did not exclude them. The new finite
source-balance condition supplies the contradiction.

## 4. Every total-three fiber has exact defect one

The [weighted extension97](quadratic-weighted-rank-defect-pass97.md)
retains the residue degrees \(d_i=[\kappa(C_i):\mathbb C(\bar U_i)]\).
If \(n=\deg_vU=\sum_i\mu_i d_i\), the same finite-cover argument
gives weighted row sums \(\sum_i d_i(v_i)_a=n/N_j\).
Thus the arithmetic content of those rows must equal the gcd
of the coordinates in the actual component basis. Explicitly,
\(n=\operatorname{lcm}_j(N_j)\gcd_i(d_i)\) under saturation.

For total multiplicity three this would force n to be at most
twice that gcd, while the weighted sum is at least three times
it. Thus no actual function nonconstant on all components can
saturate the projection bound. For admissible linear U, the
generic upper bound four then forces exact defect one and every
residue degree one. The conclusion applies to all total-three
fibers, not only the mixed case detailed next.

For (2,1), the split columns are (1,1) and (1,0), up to ordering.
The double component is collapsed and has c as its affine
parameter. The weighted bound leaves only degrees (1,1) or
(1,2). Saturation at n=3 is incompatible with the degree-two
constant subextension. Saturation at n=4 with degrees (1,2)
would give split row sums (3,1), whereas finiteness requires
(2,2). Therefore every admissible linear U satisfies
\[
\deg_vU=4,\qquad(d_{\rm double},d_{\rm simple})=(1,1),
\qquad
\dim_{\mathbb C(U)}O'/\mathfrak mO'=3.
\tag{5}
\]
Its flat semilocal T-module has exact defect one and cannot be
finite: a finite flat module over the local ring T would be
free and have equal generic and special dimensions.

A generic projection now shows that all three relative
generators restrict affinely to every reduced component.
Otherwise its largest polynomial degree would persist in a
generic linear combination, contradicting its degree-one
restriction. This concerns the actual relative-generator
embedding. It must not be confused with an affine-linear
embedding in the original four coordinates.

In the mixed case the collapsed double line is vertical in
relative (A1,A2,c)-space. Disjointness forces the simple line's
good projection to avoid the double line's constant good point.
A constant affine combination F of A1,A2 therefore equals zero
on the double component and one on the simple component.
Its generic degree is at most two, but it is constant on both
components and is not admissible for the projection argument.
It does not supply a global coordinate of A.

The defect is a precise failure of one proof step, not a
contradiction to the existence of the mixed fiber. No geometric
point at infinity has been constructed merely by subtracting
these dimensions.

## 5. A local restriction that still applies

In the surviving (2,1) profile, the double component has split
column (1,1). If its first normal action is nonzero, the
[double-branch proof97](quadratic-double-branch-pass97.md) puts
its completed local map in the form
\[
z=cx+ay^2+R,\quad
a\in\mathbb C^*,\quad
R\in(x^2,xy,y^3)\mathbb C(c)[[x,y]];
\quad
\operatorname{ord}_t x(t)>
\operatorname{ord}_t z(t)\in2\mathbb Z_{>0}
\tag{6}
\]
on the essential split base branch. Hence that branch is singular
and has a prescribed tangent.

The proof keeps all higher terms using formal preparation.
A Laurent root of the prepared quadratic would have valuation
half the branch multiplicity and leading square
\((z_0-cx_0)/a\). Odd multiplicity or a simple zero in c prevents
a root. Irreducibility then leaves one arithmetic normalization
branch, which cannot carry two distinct source labels.

The related [triple-branch calculation97](quadratic-triple-branch-pass97.md)
is now a superseded conditional diagnostic because all (3,1)
fibers are already excluded globally. Its distinction between
arithmetic branches and complex normalized source labels remains
important.

Both local calculations have exact formal controls that descend
through the original cusp conductor and are formally invariant.
Their candidate invariant K is nevertheless not rational on the
actual algebraic exceptional surface: the rational invariant field
is \(\mathbb C(t)\), while \(K^2\) is an even power of t times
\(1+t\), which has an odd-order zero. Formal invariant descent
therefore cannot supply the required global algebraic factorization.

These controls are not actual examples of the original frame or
counterexamples to cancellation. The first-normal-zero sector of
the surviving double component remains outside (6).

## 6. Original equations for the other fixed case

The [original-volume calculation97](original-volume-constraints-pass97.md)
handles a noncollapsed fixed component, which is a whole double
fiber, without a first-normal-action hypothesis. Its cylinder
has the actual original-coordinate ideal
\((L_0,z-qW^2/2-R(U))\), with \(\deg R\le2\).
The coordinates W,U,L0 are affine-linear in the original good
coordinates, and the last change is a genuine triangular shear
with a displayed polynomial inverse.

Evaluation at the canonical slice u=0 produces two global
invariant generators for the component ideal in A. This proves
a global complete-intersection description, not that those
generators are global coordinates of A.

An actual triangular translation commutes with E after restriction
to this surface. The original velocity Jacobian has rank at most
two and cube zero there. Neither commutation nor the Jacobian
identity has been extended off the surface. That extension, or
another global argument using these original equations, remains
an open task.

## 7. Evidence and remaining obligations

The [verification capture97](verification-pass97-working.json)
records three finite exact checker methods: the double and triple
formal controls and the integer source-balance controls. Input
hashes and full outputs identify what was actually run. They do
not verify the universal geometry, the whole predecessor proof
chain, or cancellation.

The [proof audit97](proof-audits-pass97-working.md) and
[checkpoint97](checkpoint-pass97-working.json) distinguish saved-file
AI proof reconstructions from computation. No human expert review,
Lean proof, historical novelty clearance, outreach or submission
has occurred. The files remain private working material.

The next mathematical obligations are to constrain or eliminate
the exact-defect-one mixed fiber, handle the remaining whole
double fibers, and separately address the reduction of arbitrary
sliced actions to the supplied original frame. Recognizing this
restricted frame would still not prove (1) without that reduction.

## Sources

[^kaliman]: Shulim Kaliman, *Free C+-actions on C3 are translations*,
    Inventiones mathematicae 156 (2004), 163–173,
    [author-hosted paper](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).
    The retained input is its earlier curve factorization and
    integral homology diagram, not an unverified free-action
    conclusion for the present N. Exact dependency scope is in96.

[^completion]: The Stacks Project, [Lemma 10.97.3, tag 00MC](https://stacks.math.columbia.edu/tag/00MC),
    faithful flatness of Noetherian local completion. Used in
    the retained finite-rank lemma's ideal contraction.

[^normalization]: The Stacks Project,
    [Lemma 33.27.1, tag 0BXR](https://stacks.math.columbia.edu/tag/0BXR),
    finite birational normalization of varieties, and
    [Lemma 10.161.8, tag 032L](https://stacks.math.columbia.edu/tag/032L),
    finite integral closure of a Noetherian normal domain in
    a finite separable field extension. These justify the
    actual normalization steps; they do not assert (3) on
    behalf of an arbitrary local model.
