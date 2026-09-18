# Contractible cylinder controls for symmetry extraction

Date: 2026-09-13.

September 18 status update: the historical full-flexibility uncertainty
below is superseded for the Russell cubic. Poloni's September 12 preprint
proves full flexibility of its cylinder. The complete reconstruction and
general-h extension are in [673](quadratic-cylinder-flexibility-and-modified-derksen-pass673-working.md).
The bounded earlier assertions and finite-dimensional-group distinctions
below are retained as a dated record. No polynomial-cylinder isomorphism
or solution of cancellation follows from the update.

This pass strengthens the symmetry-transfer control to a contractible
threefold. It does not produce a nonpolynomial cancellation kernel or
prove a new positive recognition theorem.

Let
\[
A=\mathbb C[x,y,z,t]/(F),\qquad
F=x+x^2y+z^2+t^3,\qquad X=\operatorname{Spec}A,
\quad Y=X\times\mathbb A^1_s.
\tag{1}
\]
The Koras-Russell cubic X is A1-contractible and has only trivial
algebraic vector bundles. Its one-cylinder Y is flexible outside a
closed subset of codimension at least two. Nevertheless X has no
open special-automorphism orbit and no algebraic tangent frame
consisting of LNDs.

The assertion about Y is flexibility in codimension one, not full
flexibility. No isomorphism Y=A4 is established or claimed here. The
already recorded result ML(Y)=C is inherited input, not a discovery
of this pass. The useful additional deductions are the field-invariant
and codimension statements, and a fully explicit tangent frame showing
why vector-bundle triviality cannot supply the missing additive frame.

## 1. What the stable-cylinder hypothesis actually gives

Suppose K[s] is isomorphic to C^[4]. Every finite projective K-module
P is free. Indeed, extend P to K[s], use the Quillen-Suslin theorem
on that polynomial ring, and then restrict along s=0:
\[
P\simeq (P\otimes_K K[s])\otimes_{K[s]}K\simeq K^r.
\tag{2}
\]
Smoothness descends from the cylinder. Consequently the algebraic
tangent bundle of Spec(K) is actually trivial, not merely stably
trivial. This argument uses the retract to descend a free module;
it does not infer cancellation of a general stably free module.

The same cylinder hypothesis gives topological contractibility and
A1-contractibility: the projection along A1 is respectively a homotopy
equivalence and an equivalence in the A1-homotopy category. It also
gives a nonzero intrinsic LND, by the already proved
[one-cylinder rigidity argument](intrinsic-actions-pass.md).

These are necessary consequences of stable polynomiality. They are
not sufficient to extract a transitive additive action or an LND
tangent frame. The cubic (1) satisfies all these listed consequences,
including triviality of every vector bundle, but is not A3.
This does not assert that it satisfies the stronger premise K[s]=C^[4].

## 2. An explicit free tangent module, with no possible LND frame

Set
\[
a=1+2xy,\quad b=x^2,\quad
\alpha=1-2xy,\quad\beta=4y^2.
\]
Then
\[
a\alpha+b\beta=1,
\qquad \nabla F=(a,b,2z,3t^2).
\tag{3}
\]
In the coordinate order (x,y,z,t), form the four columns
\[
N=\begin{pmatrix}\alpha\\\beta\\0\\0\end{pmatrix},\quad
V_1=\begin{pmatrix}b\\-a\\0\\0\end{pmatrix},\quad
V_2=\begin{pmatrix}-2z\alpha\\-2z\beta\\1\\0\end{pmatrix},\quad
V_3=\begin{pmatrix}-3t^2\alpha\\-3t^2\beta\\0\\1\end{pmatrix}.
\tag{4}
\]
Direct multiplication gives
\[
\nabla F\,[N,V_1,V_2,V_3]=(1,0,0,0),\qquad
\det[N,V_1,V_2,V_3]=-1.
\tag{5}
\]
Thus the last three columns, viewed as polynomial vector fields,
annihilate F and form an A-basis of Der_C(A). This is an actual
unimodular completion and a global algebraic tangent frame.

It cannot be replaced by a basis consisting of LNDs. Makar-Limanov's
theorem says that every LND of A kills x, while V_1(x)=x^2 is nonzero
in the domain A. Therefore the A-span of all LNDs is contained in the
proper module of derivations annihilating x. In particular it cannot
equal Der_C(A). Already the displayed first field is explicitly not
locally nilpotent:
\[
V_1^j(x)=j!x^{j+1}\ne0\quad(j\ge1).
\tag{6}
\]
This is not just a badly chosen frame: the common invariant x
excludes every LND frame. The full known invariant statements are
\[
\operatorname{ML}(X)=\mathbb C[x],\qquad
\operatorname{ML}(Y)=\mathbb C.
\tag{7}
\]
They were already recorded in the earlier intrinsic-action note and
are used here with that inherited credit.[^ml]

There is also a published stronger bundle statement. Hoyois, Krishna
and Østvær's Corollary 3.7 says that every vector bundle on a
Koras-Russell threefold of the first or second kind is trivial.
Their proof uses the vanishing Chow groups and the rank-three,
rank-two and line-bundle splitting results.[^bundles] Hence merely
replacing tangent triviality with triviality of all projective
modules does not repair the proposed symmetry extraction.

## 3. The one-cylinder is flexible in codimension one

### 3.1. Factoriality upgrades the field invariant

For a characteristic-zero UFD C_0 and any family of LNDs on it,
the common invariant subfield of Frac(C_0) is the fraction field
of the common invariant subring. To see this, take a nonzero
reduced fraction a/b. If D(a/b)=0, then
\[
bD(a)=aD(b).
\]
Coprimality gives a divides D(a) and b divides D(b). The
principal-ideal property of LNDs forces D(a)=D(b)=0. Applying this
to every member of the family proves, in particular,
\[
\operatorname{FML}(C_0)=
\operatorname{Frac}(\operatorname{ML}(C_0)).
\tag{8}
\]
Factoriality is essential to this argument; (8) is not asserted
for arbitrary normal affine varieties.

For (1), the element x is prime because
\[
A/(x)=\mathbb C[y,z,t]/(z^2+t^3)
\]
is a domain. Also
\[
A_x=\mathbb C[x,x^{-1},z,t].
\tag{9}
\]
The usual localization criterion for factoriality, or its divisor
class proof, now makes A a UFD: any divisor class is supported on
the single principal prime divisor x=0 after localization. The
smoothness needed for the divisor argument follows already from
(3). Polynomial extension preserves factoriality, so A[s] is a UFD.

Combining (7) and (8) yields
\[
\operatorname{FML}(X)=\mathbb C(x),\qquad
\operatorname{FML}(Y)=\mathbb C.
\tag{10}
\]
Arzhantsev, Flenner, Kaliman, Kutzschebauch and Zaidenberg's
Proposition 5.1 identifies trivial FML with an open SAut orbit
and with the existence of a flexible point.[^flex] Consequently
Y has such an orbit O, whereas X does not.

### 3.2. No divisor can be left outside that orbit

Here is the factorial special case of the same paper's
Proposition 4.22. Suppose an irreducible divisor D were a component
of Y minus O. Each additive one-parameter subgroup preserves D:
it preserves the complement and, being connected, cannot nontrivially
permute its finite set of irreducible components. Since Y is
factorial, D=V(f) for a prime element f of A[s]. Every LND then
preserves (f), hence kills f. This puts the nonconstant f in
ML(Y)=C, a contradiction.

Thus
\[
\operatorname{codim}_Y(Y\setminus O)\ge2,
\tag{11}
\]
with the possibility that the complement is empty. Every point
of O is flexible because flexibility is invariant under SAut.
This proves flexibility in codimension one, not transitivity on
all of the smooth fourfold Y.

Both X and Y are contractible, even in the unstable A1-homotopy
sense, by Dubouloz and Fasel's theorem for the first-kind
threefolds.[^a1] Therefore the following proposed transfer is false:

> A1-contractibility, trivial algebraic tangent bundle, and
> flexibility in codimension one after adjoining one variable
> force an open additive-automorphism orbit on the base.

This is a threefold control with the contractibility missing from
the older Danielewski example. It still does not replace the unknown
isomorphism Y=A4 by an established fact.

### 3.3. The additive centralizer has precisely the missing rank

For the distinguished delta=partial_s on A[s], commuting LNDs are
exactly D+h partial_s with D in LND(A), h in A, as proved in
[pass 30](intrinsic-symmetry-pass30.md). Every such field kills x,
so their generic rank on the fourfold Y is at most three. It is
exactly three: the fields
\[
\partial_s,\qquad
D_z=x^2\partial_z-2z\partial_y,\qquad
D_t=x^2\partial_t-3t^2\partial_y
\tag{12}
\]
are independent after x is inverted. They are commuting LNDs.
Thus the additively generated centralizer cannot have an open
orbit, although SAut(Y) has the orbit O of Section 3.2.
This assertion concerns the additive centralizer, not every
algebraic subgroup of the full centralizer.

## 4. Algebraic homogeneity is a strictly stronger demand

For a contractible complex variety, transitivity of a
finite-dimensional affine algebraic group is much stronger than
an open SAut orbit. The complex proof of Bruce, du Plessis and
Wall's Theorem (3.6), and its explicit following remark, give
transitivity of the unipotent radical also in the contractible
case.[^bdw] A unipotent homogeneous space over C is an affine
space. One direct argument is induction: place its isotropy
subgroup H in a codimension-one normal subgroup N of the
unipotent group U; an exponential one-parameter complement
identifies U/H with A1 times N/H. Nilpotence supplies such an N
whenever H is proper.

In particular X cannot be homogeneous under any finite-dimensional
affine algebraic group, since X is not A3. If Y were homogeneous
under such a group, it would be A4. This last implication is a
boundary, not a proof that Y is or is not homogeneous. Nor is it
offered as a new recognition criterion whose premise follows
from the stable-cylinder hypothesis by the present argument.

Even generic transitivity of a finite-dimensional group is not
enough. On X, the torus
\[
\tau\cdot(x,y,z,t)=
(\tau^6x,\tau^{-6}y,\tau^3z,\tau^2t)
\tag{13}
\]
normalizes the two commuting additive actions D_z,D_t. Their
semidirect product acts transitively on x!=0: the torus changes
the nonzero x-value, and D_z,D_t translate the free z,t-coordinates
of (9). This finite-dimensional solvable group has a proper
closed invariant complement. Its torus direction is not an LND,
so it does not satisfy the previously proved all-LND or
Ga-generated solvable finite-closure hypotheses.

## 5. What the primary search does and does not establish

The primary statements checked in this pass establish the
codimension-one flexibility assertion above. They do not establish
full flexibility of the cubic's one-cylinder. No non-A3 smooth
contractible threefold with a proved fully flexible one-cylinder
was verified in this bounded audit. This is not an assertion
that no such example is known anywhere in the literature.

Two recent sources require particular scope care. Gaifullin and
Petrov's July 2026 preprint proves generic flexibility for
one-cylinders over specified nonrigid trinomial varieties in
Theorem 10.1; Remark 10.3 announces a forthcoming full-flexibility
result. Its discussion of the Koras-Russell cubic reiterates the
ML theorem. Neither the word "trinomial" nor the announced result
establishes the required presentation and hypotheses for (1).[^recent]
The other local-slice suspension preprint requires an actual
suspension presentation over a flexible base and additional
local-slice/exceptional-locus conditions; these were not supplied
for (1).[^susp]

Likewise, a new preprint on vector bundles over rational
contractible threefolds does not supply an additive action from
a free module. Its first/second-kind Koras-Russell bundle claim
is explicitly credited there to the older theorem already used
in Section 2.[^recentbundles] No unreviewed strengthening is
needed for our countercontrol. Holomorphic or Weinstein
flexibility is also not algebraic flexibility and was not used.

The narrowed main gap is therefore integration and compatible
symmetry extraction, not obtaining a free algebraic tangent
module. The stable-cylinder hypothesis already supplies the
module in (2). Recovering enough intrinsic LND directions or a
usable finite-dimensional transitive action requires additional
algebraic information not contained in these contractibility,
bundle, and codimension-one orbit data.

## 6. Verification and attribution

The principal new work here is an explicit boundary deduction
from inherited theorems, not a novelty claim. The matrix pairing
and determinant in (5) were also checked by exact SymPy
arithmetic. These inline controls are not a standalone test suite
and are not counted as unittest methods. No expert or proof
assistant has certified this note.

[^ml]: Adrien Dubouloz, [*The cylinder over the Koras-Russell cubic threefold has a trivial Makar-Limanov invariant*](https://arxiv.org/pdf/0807.4085), the displayed theorem and introduction, PDF p. 1; *Transformation Groups* 14 (2009), 531-539. The introduction identifies the exact base invariant C[x] and credits Makar-Limanov. These same results were already inputs of [the earlier intrinsic-action note](intrinsic-actions-pass.md).

[^bundles]: Marc Hoyois, Amalendu Krishna and Paul Arne Østvær, [*A1-contractibility of Koras-Russell threefolds*, Corollary 3.7 and proof](https://content.algebraicgeometry.nl/2016-4/2016-4-019.pdf), *Algebraic Geometry* 3 (2016), 407-423, printed p. 417. The theorem is triviality of bundles on the first and second kinds; the paper's motivic suspension theorem must not be confused with an isomorphism of polynomial cylinders.

[^flex]: Ivan Arzhantsev, Hubert Flenner, Shulim Kaliman, Frank Kutzschebauch and Mikhail Zaidenberg, [*Flexible varieties and automorphism groups*, Propositions 4.22 and 5.1, with their proofs](https://arxiv.org/pdf/1011.5375), PDF pp. 30-31; *Duke Mathematical Journal* 162 (2013), 767-823. The first controls a divisor outside an open additive-group-generated orbit; the second identifies the open-orbit field invariant. Neither assertion upgrades codimension-one flexibility to flexibility everywhere.

[^a1]: Adrien Dubouloz and Jean Fasel, [*Families of A1-contractible affine threefolds*, Theorem 1](https://arxiv.org/pdf/1512.01933), PDF p. 1; *Algebraic Geometry* 5 (2018), 1-14. In their parameters take m=2, r=2, s=3; their coordinates (x,y,z,t) correspond to our (x,z,-y,t). The result concerns actual unstable A1-contractibility. The topological contractibility of (1) is also recorded in the primary source for (7).

[^bdw]: J. W. Bruce, A. A. du Plessis and C. T. C. Wall, *Determinacy and unipotency*, *Inventiones Mathematicae* 88 (1987), 521-554, [Theorem (3.6), printed p. 535](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0088/00000541?_format=xml), and [completion of the complex proof and contractible-case remark, printed p. 536](https://gdz.sub.uni-goettingen.de/fulltext/PPN356556735_0088/00000542?_format=xml). The complex proof was audited in pass 29; the explicit remark was reread here. The real case in that remark is not needed.

[^recent]: Sergey Gaifullin and Mikhail Petrov, [*Non-cancellative varieties, maximal tori, and the Makar-Limanov invariant*, Construction 2.16, Theorem 10.1 and Remark 10.3](https://arxiv.org/pdf/2607.13593), July 2026 preprint, PDF pp. 6-7 and 44-45. Only these precise scopes and the introductory Koras-Russell discussion were audited here, not the full 49-page paper.

[^susp]: [*The flexibility of m-suspensions constructed via a local slice*](https://arxiv.org/pdf/2607.11678), July 2026 preprint, the G-orbit decomposition theorem and Corollary 4.1, PDF pp. 15-17. The checked statements require an actual flexible base and local slice; the cubic is mentioned in the introductory history, not thereby verified to satisfy those hypotheses. No theorem from this preprint is used in the proof above.

[^recentbundles]: Haoyang Liu and Biman Roy, [*Vector Bundles on Rational Topologically Contractible Affine Threefolds*, Corollaries 1.0.7 and 1.0.13](https://arxiv.org/pdf/2607.05444), current July/August 2026 preprint, PDF pp. 4-5. Its stronger general statement assumes a smooth projective compactification with the specified Chow or rational-connectedness condition. Only the statement and prior-work boundary were checked, not a full reconstruction of its proof.
