# Finite normalization excludes total multiplicity four in the quadratic frame

Every closed fiber in the supplied actual quadratic frame has total
generic multiplicity at most three. No component has multiplicity
three, and a fiber containing a fixed component has profile (2) or
(2,1). In particular the previously conditional (3,1) and (2,2)
configurations are excluded.

The new input is a balance law for the sum of the actual Thom columns.
Saturation of the global projection bound makes a local base change
finite. Normalizing an actual prime divisor then counts every branch
above each normalized source point. The resulting row sums are even
if the total multiplicity is four, contradicting primitivity of the
sum of an integral basis. Finite-curve controls or formal local maps
alone do not provide this finite-normalization balance.

## 1. The exact saturated local cover

Retain the actual nonconical quadratic setting of
[checkpoint96](checkpoint-pass96-working.json). Write
S=C[s_1,s_2], K=Frac(S), A_K=K[v], and
A=S[A_1,A_2,c], with generic v-degrees at most 2,2,4.
The quotient X=Spec(A) -> Spec(S) is faithfully flat, X is smooth
factorial and contractible, and S is the full kernel of the canonical
primitive LND. Every irreducible p in S remains prime in A.
The whole generic divisor field is k'_p(w), where
k_p=Frac(S/p) and [k'_p:k_p] is at most two.

Fix a closed base point with ideal m and components C_i, ideals q_i,
and generic whole-fiber lengths mu_i. Suppose their sum is four.
Choose a generic complex linear combination U of A_1,A_2,c that
is nonconstant on every component. The all-component bound92 and
its [saturated finite-base-change proof94](nonconical-saturated-base-change-pass94.md),
in the total-four [quadratic application95](quadratic-double-components-disjoint-pass95.md), give
\[
\begin{gathered}
4=\sum_i\mu_i
\le\sum_i\mu_i[\kappa(\mathfrak q_i):\mathbb C(\bar U_i)]
\le\deg_vU\le4,\\
\deg_vU=4,\qquad \kappa(\mathfrak q_i)=\mathbb C(\bar U_i),\\
T=(S[U])_{\mathfrak mS[U]},\qquad
D=(S[U]\setminus\mathfrak mS[U])^{-1}A,
\qquad D\simeq T^4\text{ as a module}.
\end{gathered}
\tag{1}
\]
Here D is the entire indicated base change, not just one component
local ring. The equality-in-flat-rank argument first makes the
semilocal component localization finite free. The inclusion of D
in that localization is an integral localization and therefore an
equality. This is the retained saturation gate; no finiteness is
being inferred merely from a finite generic field extension.

Put L=C(U). The residue field of T is L. The maximal ideals of
D over mT are exactly the component points q_iD, with residue L.
There are no further closed points in this local base change.
Moreover every reduced component is an entire affine line by96.
A polynomial U on that line with function-field degree one is an
affine coordinate, so each C_i is the actual parameter line A1_U.
This last fact will permit one common generic transverse slice.

## 2. A prime divisor and its constant-field subextension

Choose a product-complement exceptional curve Gamma containing the
base value. Such a curve exists by the local-slice construction.
Let p define any irreducible component of Gamma through that value.
It remains a nonunit prime in D, since it is prime in A and belongs
to mD. With G=T/pT and R=D/pD, (1) gives
\[
\begin{gathered}
G\text{ is a one-dimensional local domain with residue }L,\\
R\text{ is a domain, finite free of rank }4\text{ over }G,\\
\operatorname{Frac}G=k_p(U),\qquad
F:=\operatorname{Frac}R=k'_p(w),\qquad
[F:k_p(U)]=4,\\
N_p=[k'_p:k_p]\in\{1,2\},\qquad
[k'_p(U):k_p(U)]=N_p,\qquad
[F:k'_p(U)]=4/N_p.
\end{gathered}
\tag{2}
\]
The injective finite-free map G -> R in particular prevents the
residue of U from becoming algebraic over k_p. Thus adjoining U
does not collapse the constant extension: a purely transcendental
extension is linearly disjoint from the finite field k'_p/k_p.
This checks the middle degree in (2) inside the actual divisor
field, rather than assigning it to a chosen model of that field.

Let C be the integral closure of G in k'_p(U), and H the integral
closure of R in F. These are finite rings over G. The first is
the localized normalized constant curve for p, after adjoining
the independent parameter U. Indeed the actual curve factorization
identifies its function field with k'_p. Its normalization is a
smooth complex curve; extending constants to C(U) preserves that
normalization, and integral closure commutes with localization.

Consequently the maximal ideals of C are exactly the normalized
source points a above the chosen base value, on the component for p.
Each has residue field L. No such label is lost: any denominator
from S[U] outside mS[U] reduces at every one of these points to
the same nonzero polynomial in U, which is a unit in L. This
also covers several normalized base branches of one irreducible p.

Both C and R are integral over G and sit in F, so their integral
closures in F agree. Thus H contains C and is its integral closure
in the extension of degree 4/N_p. Finiteness can be obtained from
finite normalization of affine varieties and localization, or from
the separable trace-dual argument over the normal curve C.[^finite]
No assumption that R or the intermediate curve Z is normal enters.

## 3. The exact degree balance above every source label

For a maximal ideal a of C, its local ring C_a is a DVR with
residue L. The ring H localized over it is finite and torsion-free
of rank 4/N_p, hence is free of that rank. Its maximal ideals P
are discrete-valuation branches. Let e_P be the order of a source
uniformizer there, and f_P=[kappa(P):L]. Reduction modulo the
uniformizer and the ordinary DVR length calculation give
\[
\sum_{P\mid a}e_P f_P=4/N_p.
\tag{3}
\]
For example, each localized branch contributes length e_P over
its residue field; its dimension over L is e_P f_P. The left side
therefore equals the dimension of a free rank 4/N_p module modulo
the source maximal ideal. Residue extensions are not being assumed
trivial at these normalization branches.

Every P contracts in R to one of the actual points q_iD/pD.
This follows from finiteness over G and the complete list of
maximal ideals in (1). In particular (3) cannot discard branches
on other components of the fiber or on a putative missing part
of the local cover.

## 4. Why this degree balance counts the actual Thom entries

This is the essential geometric identification. Normalize the
actual prime surface E_p=Spec(A/pA) globally. Its normalization
is finite and birational.[^finite] It maps to the normalized
constant curve because its map to that curve component is
dominant and its coordinate ring is normal. The branches P in
Section 3 are precisely the localizations of its irreducible
curves above the C_i.
Indeed normalization commutes with this localization: clearing
the finitely many denominators in a monic integral equation
makes a suitable denominator multiple integral before localization.

Fix such a curve over C_i and source label a. It maps finitely
to the actual line C_i=A1_U, since the surface normalization is
finite. The field degree of this curve map is f_P. In
characteristic zero it is generically separable. At a generic
complex value U_0 it therefore has exactly f_P distinct points,
with U-U_0 a local parameter along the curve.

Choose one U_0 simultaneously general for the finitely many
curves in question. Avoid their singular points, ramification
values over U, pairwise intersection points, and singular points
of the normal surface. The latter have codimension at least two
and hence form a finite set. At each selected point the normal
surface has local parameters w,U-U_0, where w cuts this curve.
A local parameter t_a of the normalized source curve pulls back
as a unit times w^{e_P}. Other components of its zero divisor
have been avoided.

Holding U=U_0 is an actual smooth transverse surface in X,
because U restricts to a coordinate on C_i. In the normalized
exceptional surface its intersection is smooth at the selected
points. It gives the normalizations of the transverse exceptional
branches there: the normalization map is finite and birational,
and a generic U-fiber is not a component of its nonisomorphism
locus. No assertion that normalization commutes with every fiber
is required. The positive winding contribution at each selected
point is exactly e_P. Summing the f_P points shows that the
actual Thom column entry satisfies
\[
(v_i)_a
=\sum_{\substack{P\mid a\\P\text{ lies over }C_i}}e_Pf_P,
\qquad
\boxed{\quad\sum_i(v_i)_a=4/N_p.\quad}
\tag{4}
\]
All points are accounted for by finite normalization. In
particular a residue field extension of degree f_P contributes
f_P geometric points at the generic complex slice; it does not
produce one point with an arbitrarily chosen label.

The e_P in (3)--(4) measures the normalized surface map to the
normalized source curve. It is different from the ramification
index e_ja of that source curve over the normalized base branch.
The latter is the weight in the supported lattice T. Keeping
these two maps separate is necessary for (4).

## 5. Primitivity excludes total four

Use the full supported lattice of96 and
[supported-lattice97](quadratic-supported-lattice-pass97.md).
Let T_ram be its weighted row map, and let N_j be the degree of
the normalized cover on base branch j. It equals N_p for the
global component p containing that branch. For the sum of the
actual component basis vectors, equation (4) says
\[
\begin{gathered}
v_{\rm tot}:=\sum_i v_i,\qquad
(v_{\rm tot})_a=4/N_j\in\{2,4\},\\
v_{\rm tot}/2\in\mathbb Z^Q,\qquad
T_{\rm ram}(v_{\rm tot}/2)=2\mathbf1,
\qquad v_{\rm tot}/2\in L_{\rm supp}.
\end{gathered}
\tag{5}
\]
There is at least one branch: a total-four fiber cannot lie
in the product complement, where the whole fiber has length one.

But the vectors v_i are a Z-basis of L_supp. Their sum has
coordinates all equal to one in that basis and is primitive.
Equation (5) would express it as twice another lattice vector,
which is impossible. Therefore
\[
\boxed{\quad\sum_i\mu_i\le3
\quad\text{for every closed quadratic fiber.}\quad}
\tag{6}
\]
Degree-one exceptional components cause no difficulty: their
row sum is four, still even. This proof does not need to delete
them or import the fully retained-curve theorem.

The same reasoning has a useful exact formulation. If the
identical saturation and actual finite-normalization gates hold
with total n and residue degree one on all component projections,
then N_j divides n and the row sum is n/N_j. Basis primitivity
forces their common gcd to be one. Hence
\[
\boxed{\quad n=\operatorname{lcm}_j N_j
\quad\text{under those saturated finite-cover hypotheses.}\quad}
\tag{7}
\]
Indeed if g=gcd_j(n/N_j)>1, division by g still gives an
integral supported lattice vector, since g divides n. The
identity gcd_j(n/N_j)=n/lcm_j(N_j) proves (7). This is not
a formula for arbitrary unsaturated closed fibers.

## 6. Surviving fixed profiles and their source columns

A multiplicity-three component would now be the whole reduced
fiber. The whole-irreducible exclusion96, with actual divisor
degrees at most two, allows only multiplicity one or two.
Thus every component has multiplicity at most two. A
multiplicity-one component has nonzero translation action by
the retained whole-fiber nonvanishing theorem54. Consequently
\[
\boxed{\quad
\text{a closed fiber containing a fixed component has profile}
\ (2)\text{ or }(2,1).
\quad}
\tag{8}
\]
In particular no closed fiber has two fixed components.
These statements concern the supplied quadratic frame and
do not prove that the remaining double component is absent.

For clarity, the supported-lattice calculation still has a
nonvacuous application. In profile (2,1), there is one split
degree-two branch and any extra branches have degree one.
The same positivity and determinant-one calculation as97 gives
\[
\begin{array}{c|cc}
\text{normalized source row}&\mu=2&\mu=1\\ \hline
\text{first split point}&1&1\\
\text{second split point}&1&0\\
\text{each degree-one point}&2&1
\end{array}
\tag{9}
\]
All these normalized source points have one common image in Z.
The intrinsic degree-two divisor locus has exactly one normalized
base branch there. The double component is collapsed by96 and
has the split column (1,1). Thus the conditional double-branch97
tangent argument remains relevant to this surviving profile.

The finite-curve and formal controls97 do not contradict this
proof. They do not supply the actual finite rank-four base change
and its degree-balanced prime-surface normalization. Previously
conditional (3,1) and (2,2) branch analyses are now superseded
at the profile level by (6), while their branch-versus-label and
formal-versus-algebraic distinctions remain valid controls.

## Sources, ownership and limitations

The actual saturation statement comes from the retained
[flat-rank93](nonconical-saturated-flat-rank-pass93.md),
base-change94 and its total-four application95, with the current
whole-fiber and product-stratum hypotheses96. The full supported
integral diagram and linking multiplicities are the audited96
inputs, restated in lattice97. They are not replaced by a finite
integer computation.

Geometry supplied the finite-normalization row balance and the
generic transverse-slice identification with the actual Thom
entries. Root strengthened the initial two-profile contradiction
to primitivity of the total column, excluding every total-four
fiber. General and Jet independently reconstructed the field
degrees, label survival and ramification-residue-to-Thom gate
before this note was saved; saved-file reviews are separate.

No numerical method is used to establish this proof. The separate
[finite arithmetic control](quadratic_source_balance_checks_pass97.py)
checks selected lattice tables, not the universal geometry.
Its scope does not include global freeness, recognition of A, or reduction of an
arbitrary sliced action to the supplied frame. Every file through96
remains unchanged.

[^finite]: The Stacks Project,
    [Lemma 33.27.1, tag 0BXR](https://stacks.math.columbia.edu/tag/0BXR)
    supplies finite birational normalization for the actual affine
    prime surface. [Lemma 10.161.8, tag 032L](https://stacks.math.columbia.edu/tag/032L)
    supplies finiteness in a finite separable field extension of
    a Noetherian normal domain, here the normalized source curve.
    Both complete displayed statements and proofs were freshly
    read for this argument. The trace-dual finiteness argument
    was checked in the source, and characteristic-zero generic
    curve separability is used explicitly above. Deeper cited
    Nagata and normalization
    dependencies were not freshly reread. No assertion that
    normalization commutes with arbitrary special fibers is used.
