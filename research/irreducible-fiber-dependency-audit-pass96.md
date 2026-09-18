# Dependency audit of the irreducible-fiber multiplicity exclusion

The exclusion of a whole irreducible fiber of multiplicity four in
the actual quadratic frame survives this adversarial audit. Its
required source dependence can be narrowed: Kaliman's finite-curve
factorization and normalization-homology argument suffice. The
later translation theorem, an affine-line normalization of every
exceptional component, and injectivity of the normalization of Z
are not needed for this exclusion.

This is a replacement dependency argument for the particular use
of [ramification92](nonconical-irreducible-fiber-ramification-pass92.md)
in [rank-everywhere95](quadratic-quotient-rank-everywhere-pass95.md).
It is not a counterexample to that use, a proof of general
cancellation, or an audit of every earlier result. No frozen
proof is changed.

## 1. Exact hypotheses and the primary input

The retained setting supplies
\[
\begin{gathered}
X=\operatorname{Spec}A,\qquad A[u]=\mathbb C^{[4]},\qquad
0\ne N\in\operatorname{LND}(A),\qquad
S=\ker N=\mathbb C[s_1,s_2],\\
Y=\operatorname{Spec}S,\qquad \pi:X\to Y,\qquad
A\text{ faithfully flat over }S,\\
A_{S_{(p)}}/pA_{S_{(p)}}=k'_p[t],\quad
k_p=\operatorname{Frac}(S/p),\quad [k'_p:k_p]\le2
\quad(p\in S\text{ irreducible}).
\end{gathered}
\tag{1}
\]
The last statement is the actual whole generic-divisor conclusion
of [degree-bound91](nonconical-residue-degree-bound-pass91.md),
not a statement about the image of two selected generators.
The cylinder makes X smooth and factorial. On complex points,
projection from the cylinder is a homotopy equivalence, so X is
contractible. In particular all the integral homology vanishings
used below hold before recognizing A.

Here is the primary input in its needed scope. Kaliman's Lemmas
2.1--2.2 give reduced irreducible divisor pullbacks, a product
complement, and a curve factorization. Proposition 3.2(i) makes
the curve map finite. Its proof's Step 2 equates the first Betti
numbers of the total normalizations. These statements apply to
a factorial affine threefold with X smooth and
\(H_2(X)=H_3(X)=0\); no free-action hypothesis is imposed.[^1]

Choose a product-complement curve \(\Gamma\subset Y\). It need
not be the fully retained curve of Theorem 5.2(i). Write
\(E=\pi^{-1}(\Gamma)\) and use the actual factorization
\[
E\xrightarrow{\kappa}Z\xrightarrow{\theta}\Gamma,
\qquad \theta\text{ finite},\qquad
\check X\simeq\check Y\times\mathbb A^1,
\qquad \check Y=Y\setminus\Gamma.
\tag{2}
\]
Each component of E is the reduced prime divisor defined by
the corresponding irreducible base equation. Each dominates
one component of Z, with a generic affine-line cylinder. Thus
the actual relative algebraic constant field of that divisor
identifies the degree of the corresponding normalized curve
cover with \([k'_p:k_p]\) in (1). For the present choice of
\(\Gamma\), cover degree one is allowed.

Neither \(\pi\) nor \(\kappa\) is assumed proper. The
finite map \(\theta\) is proper; that is a proved conclusion,
not a properness assumption on the additive quotient.

## 2. What replaces affine-line normalizations

Choose a finite set \(\Sigma\subset\Gamma\) containing
all singular and exceptional values needed for the smooth
product strata in the source. It may also contain the particular
fiber value under examination. Let stars denote removal of
these values or their inverse images. Then \(Z^*\) and
\(\Gamma^*\) are the corresponding normalizations with
finitely many points removed.

Let \(G_Z\) and \(G_\Gamma\) be the kernels of the maps from
the first integral homology of these punctured curves to the
first homology of their full normalizations. For any smooth
affine curve, its second homology vanishes. The pair sequence
therefore identifies each G with the free group on its finite
puncture loops. These groups split by base value. The full
normalization homology can still contain handle and infinity
classes; none is discarded.

The induced map
\(H_1(Z^{\rm norm};\mathbb Z)\to
H_1(\Gamma^{\rm norm};\mathbb Z)\) is injective. Here is the
additional argument, rather than an assumption about normality
or connectedness. A finite dominant map of smooth affine curves
is an unramified finite topological cover after removing the
finitely many branch values and their preimages. A cycle on
the target can be moved off these points. Summing its lifts
over all sheets gives a cycle whose image is the degree times
the original cycle. Filling the punctures proves surjectivity
on H1 over \(\mathbb Q\). Apply this componentwise. The rank
equality in Proposition 3.2, Step 2, makes this rational map an
isomorphism. The integral H1 groups of smooth affine curves
are free abelian, so its integral kernel is zero.

The proof uses finiteness of the normalized maps. This follows
from finiteness of \(\theta\): take integral closures of the
affine curve rings in their finite function-field extensions.
No hypothesis that Z itself is normal, or that its distinct
normalized points remain distinct in Z, enters the argument.

## 3. The exact integral diagram and the puncture lift

The relevant source diagram specializes here to
\[
\begin{array}{ccccccccc}
0&\longrightarrow&H_3(X^*)&\xrightarrow{\phi'}&H_1(Z^*)&
\longrightarrow&H_2(\check X)&\longrightarrow&0\\
&&\downarrow&&\downarrow\theta_1&&\downarrow\simeq\\
0&\longrightarrow&H_3(Y^*)&\xrightarrow{\phi}&H_1(\Gamma^*)&
\longrightarrow&H_2(\check Y)&\longrightarrow&0.
\end{array}
\tag{3}
\]
All groups in (3) have integral coefficients. The right-hand
map is induced by the product complement. Removing complex
curves from the smooth contractible threefold does not change
H2; this gives the upper zero on the right. The base is the
plane with finitely many points removed. The left zeros use
the vanishing of H3 of the smooth affine surface \(\check Y\)
and the product identification. These are exactly the diagram's
vanishing hypotheses, not a claim that every open set is
contractible.

There is no omitted transverse multiplier in the middle map.
Off the removed finite set, a base component and its pullback
are smooth, and the latter is the reduced prime divisor of
the pulled-back base equation. That equation has normal
order one. The induced map on the oriented normal discs
therefore has degree one, leaving exactly \(\theta_1\) on
the Thom groups. This follows already from the divisor and
product-stratum properties of Lemmas 2.1--2.2.

For clarity, the same diagram and its support argument prove
the rank equality used in Section 2. The images of \(\phi\)
and \(\phi'\) lie in the puncture groups. The map
\(G_Z\to G_\Gamma\) has finite-index image, since every
base puncture has a preimage with a positive ramification
index. Consequently the ranks of both the puncture quotients
and the normalization H1 on the source are at least those
on the target. Their sums agree by (3). Both inequalities
are equalities. This is the source's Step 2 with its two
separate rank comparisons retained.

Now take an integral target puncture class w. The right-hand
isomorphism in (3) supplies \(\beta\in H_1(Z^*)\) such that
\(\theta_1\beta-w\in\operatorname{im}\phi\). Project this
identity to normalization H1. Both w and the base-sphere
image disappear. Injectivity from Section 2 forces \(\beta\)
to lie in \(G_Z\). Therefore
\[
G_\Gamma=\theta_1(G_Z)+\operatorname{im}\phi.
\tag{4}
\]
This is an integral equality. Surjectivity over \(\mathbb Q\)
alone would not suffice for the multiplicity conclusion.
The normalization-H1 argument is precisely what rules out
using an extra handle or infinity class to repair a local
puncture cokernel.

## 4. Support, full lattices, and the transverse multiplicity

Fix \(b\in\Sigma\). Let r count normalized base branches
there, q the source normalization points over those branches,
and h the irreducible components of the entire reduced fiber.
Let \(e_a\) be the ramification index of source point a over
its base branch j. In the corresponding puncture bases put
\[
\begin{gathered}
T_b:\mathbb Z^q\to\mathbb Z^r,
\qquad T_b(e_a^{\rm basis})=e_a e_j^{\rm basis},
\qquad \mathbf1=(1,\ldots,1),\\
\mathbb Z^r=\operatorname{im}T_b+\mathbb Z\mathbf1,
\qquad
\phi' H_{3,b}(X^*)=T_b^{-1}(\mathbb Z\mathbf1),
\qquad h=q-r+1.
\end{gathered}
\tag{5}
\]
The first equality is (4), split by base value. A small
positively oriented base sphere maps to the diagonal sum
of its branch loops, even when a branch is singular. This
is Lemma 3.1's local Thom computation.

Here are the support and index checks for the second equality.
Contractibility identifies H3 of \(X^*\) with relative H4
around the removed curve fibers. Delete their finitely many
singular and intersection points; codimension six makes
this deletion irrelevant in relative degree four. The
ordinary oriented Thom isomorphism along their smooth parts
then gives one copy of \(\mathbb Z\) per irreducible curve
component. It counts irreducible components, not connected
components of a possibly reducible fiber.

Each such class can be represented near its own base fiber.
Functoriality of the Thom map and the actual factorization
put its image in the puncture group over b. This uses only
compact representative cycles and continuity, not properness
of \(\kappa\). Conversely, (3) identifies the full kernel
in the puncture block with \(T_b^{-1}(\mathbb Z\mathbf1)\).
Injectivity of \(\phi'\) and the direct decomposition by base
value show that this full kernel is the image of the b-supported
group. It is not merely a finite-index sublattice. Since
\(T_b\) is onto over \(\mathbb Q\), its inverse image of
the diagonal has rank \(q-r+1\).

Suppose now that h=1. Finiteness gives at least one source
point over each normalized base branch, so (5) makes q=r.
There is exactly one over each branch. Its ramification
index is the generic degree \(N_j\) of that component's
finite normalized cover, by the degree formula for finite
maps of smooth complex curves. Thus T is diagonal. Integer
Bezout gives
\[
\begin{gathered}
\gcd(N_i,N_j)=1\quad(i\ne j),\qquad
\ell=\operatorname{lcm}_jN_j,\\
T_b^{-1}(\mathbb Z\mathbf1)
=\mathbb Z(\ell/N_1,\ldots,\ell/N_r),\qquad
\boxed{\quad\mu_b=\ell=\prod_jN_j.\quad}
\end{gathered}
\tag{6}
\]
Indeed the order of the cokernel in the first equality of
(5) is \(\prod N_j/\operatorname{lcm}N_j\), so it is one
exactly under the stated pairwise coprimality condition.
The integral generator of the one-component source Thom
group maps to a generator of the full lattice in (6), not
to an unspecified multiple.

To identify its positive base coefficient with the whole
scheme multiplicity, choose a general smooth point of the
reduced component. The successive nilpotent layers of the
fiber are coherent modules on that reduced curve. On a
dense smooth open they are locally free, and their ranks
sum to the generic Artinian length \(\mu_b\). An actual
local parameter along the curve is regular on each layer.
Taking its zero section therefore leaves length \(\mu_b\)
on a transverse smooth complex surface. The two base
functions have an isolated common zero on that surface.
They define a finite analytic germ; regularity and the
finite complete-intersection condition make it flat.
A nearby regular value has \(\mu_b\) preimages, each
with positive complex orientation. The degree of the
transverse linking sphere is consequently \(\mu_b\).
This is the coefficient in (6). No globally proper map,
reduced whole fiber, or global section has been inserted.

## 5. The exact quadratic consequence

Under (1), each \(N_j\) in (6) is either one or two.
Pairwise coprimality permits at most one two. Hence
\[
\boxed{\quad
\text{whole reduced fiber irreducible}
\quad\Longrightarrow\quad \mu_b\in\{1,2\}.
\quad}
\tag{7}
\]
This proves the exclusion of four used in rank-everywhere95.
If a proposed fiber has multiplicity four, it automatically
lies over \(\Gamma\): outside it the product complement
has whole-fiber length one. Primitivity is not needed for
that particular placement argument. It remains an important
separate hypothesis elsewhere in rank-everywhere95.

The analogous arithmetic with the all-divisor bound three
gives \(\mu_b\in\{1,2,3,6\}\). To remove one from a fixed
fiber's list one still needs the actual nonvanishing input
or the stronger fully retained setup of92. Nothing here
assigns the whole-fiber formula to a fixed component of
a reducible fiber.

## 6. Adversarial controls for the fragile inferences

Finiteness and rationality do not by themselves make the
source normalization an affine line. An actual example is
\[
\begin{gathered}
A_0=\mathbb C[x,y,z,t]/(xz-y^2+t^2-1),\qquad
D=x\partial_y+2y\partial_z,\qquad \ker D=\mathbb C[x,t],\\
E_0=V(x)=\{y^2=t^2-1\}\times\mathbb A^1_z,
\qquad
\theta:\mathbb C^*\to\mathbb A^1_t,
\quad t=(v+v^{-1})/2 .
\end{gathered}
\tag{8}
\]
The hypersurface is smooth. Its x-localization is a polynomial
ring over \(\mathbb C[x,x^{-1}]\), and x is prime because
its quotient is \(\mathbb C[v,v^{-1},z]\). Nagata's UFD
criterion makes the Noetherian domain \(A_0\) factorial.[^2]
The displayed field is
a genuine LND. Localizing at x gives its kernel; contraction
removes every x-denominator because
\(xA_0\cap\mathbb C[x,t]=x\mathbb C[x,t]\).
This proves the asserted full kernel.

This example has a finite degree-two rational intermediate
curve with a nonzero normalization H1. It does not satisfy
the homology hypothesis. After a complex linear change,
its threefold is \(\sum_{i=1}^4 z_i^2=1\). Writing
\(z=a+ib\) identifies it with the tangent bundle of the
real sphere \(S^3\): \(a=\sqrt{1+\lVert b\rVert^2}\,s\),
\(s\in S^3\), and \(b\perp s\). Scaling b retracts it
onto that sphere, so \(H_3(X_0)=\mathbb Z\). The map
on normalization H1 is therefore not injective. This
control identifies exactly why the homology step cannot
be dropped; it is not an example satisfying (1).

A separate polynomial-map control exposes the possible
missing transverse factor. On \(\mathbb A^3_{a,b,c}\), use
the displayed base functions \(a^2,ac-b^2\). The reduced
exceptional surface a=0 has a degree-two cover
\(b\mapsto-b^2\), but the whole origin fiber has generic
length four: over \(\mathbb C(c)\), eliminate a from
\((a^2,ac-b^2)\) to obtain \((b^4)\). This does not
contradict (7). The first divisor pulls back with multiplicity
two, and \(\mathbb C[a^2,ac-b^2]\) is not the full kernel
of \(a\partial_b+2b\partial_c\). Its true kernel is
\(\mathbb C[a,ac-b^2]\). The generic geometric fiber of
the displayed map is also two lines, not the required
product-complement fiber. Thus cover degree alone would
be insufficient; the actual quotient and its reduced
prime divisor pullbacks are essential to diagram (3).

## 7. Verdict, remaining dependencies, and sources

No counterexample satisfying (1), or missing connectedness,
normality or properness hypothesis in this application, was
identified. The original92 route uses Theorem 5.2(i) to
remove bijective components and obtain affine-line
normalizations. The proof above avoids that stronger route
for the multiplicity-four exclusion. It permits arbitrary
normalization homology and degree-one exceptional components,
then proves the integral puncture reduction needed for (7).

The outstanding dependencies are explicit: the actual
all-divisor degree bound91, Kaliman's curve factorization
and integral quotient homology diagram, and standard
oriented Thom/excision and finite analytic intersection
multiplicity facts. This note reconstructs their application
and the local index calculation; it is not a new proof of
all underlying topology, a formal verification, or a
substitute for external expert review. No numerical test
or assertion about the general cancellation target is added.

### Sources and exact reading scope

1. Shulim Kaliman, *Free C+-actions on C3 are translations*,
   [author-hosted primary PDF](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).
   Fresh reading covered the complete displayed statements
   and proofs of Lemmas 2.1--2.2, 3.1, Proposition 3.2
   including every step and its integral diagram, Lemma 4.1,
   Propositions 4.2 and 5.1, and Theorem 5.2 with its displayed
   deduction. Sections 4--5 were examined adversarially but
   are not inputs to the replacement argument above.
   The access was primary extracted text. Screenshot calls
   did not expose viewable page images in this session,
   so no visual page audit is claimed. Dold, Milnor, and
   other cited foundational proofs were not freshly reread.
2. [Publisher record](https://link.springer.com/article/10.1007/s00222-003-0336-1),
   *Inventiones mathematicae* 156, 163--173 (2004),
   DOI 10.1007/s00222-003-0336-1. Metadata and abstract were
   checked. The online publication date is 16 October 2003;
   the issue date is April 2004. The subscription PDF was
   not used. A bounded correction search supplied no
   mathematical correction relied on here; no exhaustive
   literature or absence-of-corrigendum claim is made.
3. The Stacks Project,
   [Lemma 10.120.7, tag 0AFU](https://stacks.math.columbia.edu/tag/0AFU).
   The complete displayed statement and proof of Nagata's
   criterion were freshly read for the control in Section 6.
   The Noetherian hypothesis supplies factorization into
   irreducibles. Nagata's original 1957 paper was not read.

The retained33,34,46 and92 arguments were also read for
comparison, but their prior review counts are not treated
as evidence for the fresh primary reconstruction. The
controls in Section 6 and the normalization-transfer proof
were checked algebraically here; they are not quotations
of Kaliman's conclusions. All files through95 remain unchanged.

[^1]: Kaliman, author PDF, printed pages 2--7, especially
    Proposition 3.2 and Step 2. The title's free-action result
    is not the hypothesis of these earlier statements.

[^2]: Stacks 0AFU, the final factoriality statement, applied
    to the multiplicative set generated by the prime x.
