# Irreducible fixed fibers and the retained ramification lattice

In the actual nonconical frame, a whole irreducible reduced exceptional
fiber has multiplicity two when the relative equation has degree two,
and multiplicity two, three or six when it has degree three. Consequently
the quotient differential cannot have rank zero along such a fiber in
degree two. In degree three, rank zero leaves only multiplicity six,
with one retained degree-two branch and one retained degree-three branch.

These are conditional statements about the **entire reduced fiber**.
They do not apply to one fixed component of a reducible fiber. The
topological source gate was already established for the unknown
threefold in pass46; the new use here combines that gate and the
pass33--34 integral lattice with the actual pass91 degree bound and
the local rank-zero condition. No cancellation theorem is added.

## 1. The actual hypotheses, before recognition

Retain the exact primitive field from
[global-Jacobian91](nonconical-global-jacobian-field-pass91.md) and the
[all-divisor degree bound](nonconical-residue-degree-bound-pass91.md):
\[
\begin{gathered}
B=A[u]=\mathbb C^{[4]},\qquad
0\ne N\in\operatorname{LND}(A),\qquad
\ker N=S=\mathbb C[s_1,s_2],\\
\pi:X=\operatorname{Spec}A\longrightarrow Y=\operatorname{Spec}S,
\qquad d\in\{2,3\},\\
A_{S_{(p)}}/pA_{S_{(p)}}=k_p'[t],\qquad
k_p=\operatorname{Frac}(S/pS),\qquad
[k_p':k_p]\le d
\quad(p\in S\text{ irreducible}).
\end{gathered}
\tag{1}
\]
Here A is smooth, factorial and affine, and its complex points are
contractible. Indeed the cylinder is a polynomial ring, and projection
\(X\times\mathbb C\to X\) is a homotopy equivalence. Thus all its
positive-degree integral homology groups vanish. The quotient is
faithfully flat with nonempty pure curve fibers, and every irreducible
p in S remains prime in A. None of these assertions assumes
\(A=\mathbb C^{[3]}\).

Kaliman's Notation 2.3 and Theorem 5.2(i) apply to this X: their
threefold hypotheses are factoriality, smoothness and the specified
vanishing of \(H_2,H_3\), not a polynomial presentation of A.
Choose the resulting fully retained exceptional curve \(\Gamma\).
Write \(E_\Gamma=\pi^{-1}(\Gamma)\). There is a factorization
\[
E_\Gamma\xrightarrow{\kappa}Z
 \xrightarrow{\theta}\Gamma,\qquad
\theta\text{ finite},\qquad
Z_i^{\rm norm}\simeq\Gamma_i^{\rm norm}\simeq\mathbb A^1,
\qquad 2\le N_i:=\deg(\theta_i)\le d.
\tag{2}
\]
The product complement is \(X\setminus E_\Gamma\simeq
(Y\setminus\Gamma)\times\mathbb A^1\) over the base.
For precision, the source first gives polynomial base curves and
rational source curves. Proposition 3.2, Step 2, equates the first
Betti numbers of their total normalizations. The base number is zero;
a smooth affine curve with genus g and r omitted points has
\(b_1=2g+r-1\). Hence every source normalization is also an affine
line. The retained maps are nonbijective and, by the same proposition's
argument, nonbirational, giving \(N_i\ge2\).[^kaliman]

The upper bound in (2) uses the **actual** generic divisor ring in
(1). Its function field is \(k_p'(t)\). The generic cylinder of
the intermediate factorization instead writes this field as
\(\mathbb C(Z_i)(t')\). Taking the relative algebraic closure of
\(k_p\) identifies \(\mathbb C(Z_i)=k_p'\), so the cover degree
is exactly \([k_p':k_p]\). This is the field-identification argument
already retained in [monodromy46, Sections 2--3.1](quadratic-monodromy-pass46.md).

A fixed point of this primitive N lies over \(\Gamma\). To check
this without assuming a preferred plinth equation, on the product
complement write \(A_f=S_f[w]\) and \(N=a\partial_w\), with
\(a\in S_f\). A nonunit factor of a would divide every N-value
after localization and, by prime saturation, globally. Primitivity
excludes it. Thus a is a unit and there are no fixed points there.

## 2. The integral support diagram on the unknown threefold

Choose a finite set \(\Sigma\subset\Gamma\) containing all
singular and exceptional values required for the product and smooth
curve strata. Set \(X^*=X\setminus\pi^{-1}(\Sigma)\),
\(Y^*=Y\setminus\Sigma\), and put checks on the product
complements. All homology in this section has integral coefficients.
The source's pair sequences and Thom identifications give
\[
\begin{array}{ccccc}
0\longrightarrow H_3(X^*)&\xrightarrow{\phi'}&H_1(Z^*)&
 \longrightarrow&H_2(\check X)\longrightarrow0\\
\phantom{0\longrightarrow}\downarrow&&\downarrow\theta_1&&
 \downarrow\simeq\\
0\longrightarrow H_3(Y^*)&\xrightarrow{\phi}&H_1(\Gamma^*)&
 \longrightarrow&H_2(\check Y)\longrightarrow0.
\end{array}
\tag{3}
\]
The right-hand isomorphism comes from the product complement. Removing
complex curves from the smooth contractible threefold leaves
\(H_2(X^*)=0\); similarly \(H_2(Y^*)=0\). For example the
relative groups in degrees two and three vanish by excision and
real codimension four. The zero at the left uses vanishing of
\(H_3(\check Y)\) for an affine complex surface and the same
product identification. These are precisely the inputs used in the
source diagram and [branch-count33](all-speed-ambient-obstruction-pass33.md).

For a value \(b\in\Sigma\), let r be the number of normalized
base branches there and q the number of normalized source points
over them. Since both normalizations in (2) are unions of affine
lines, their puncture loops are integral bases of first homology.
There are no remaining genus or infinity classes. Each source loop
maps to its ramification index times the loop of its base branch.
The base sphere at b maps to the diagonal sum of the r branch loops.

Partition the q source points by their base branches. Let their
positive indices be \(e_a\), and let \(m_j\) be the gcd in
branch j. In the corresponding block, put
\[
T:\mathbb Z^q\longrightarrow\mathbb Z^r,
\quad v_a\longmapsto e_a w_j,\quad
\mathbf1=\sum_jw_j,\qquad
\left|\frac{\mathbb Z^r}{\operatorname{im}T+\mathbb Z\mathbf1}\right|
=\frac{\prod_jm_j}{\operatorname{lcm}_j(m_j)}=1.
\tag{4}
\]
Indeed the right-hand isomorphism in (3) makes the map onto
\(H_1(\Gamma^*)/\operatorname{im}\phi\) surjective.
The puncture bases and the base sphere classes split this assertion
by b. In each block, integer Bezout gives
\(\operatorname{im}T=\bigoplus_jm_j\mathbb Z w_j\).
The diagonal element in \(\bigoplus_j\mathbb Z/m_j\) has order
\(\operatorname{lcm}_jm_j\), proving (4). Thus the distinct
branch gcds are pairwise coprime. This is exactly the integral
argument of [ramification34](integral-ramification-pass34.md), with
its actual homological hypotheses verified here.

## 3. A whole irreducible fiber, not merely a fixed component

Let \(c_b\) be the number of irreducible components of the entire
reduced fiber at b. Excision and complex orientation identify the
b-supported summand of \(H_3(X^*)\) with
\(\mathbb Z^{c_b}\): equivalently it is relative degree four
around the curve fiber. Removing its finitely many singular or
intersection points does not change this degree. Functoriality of
the Thom map keeps this summand supported on the q punctures over b.

Exactness and the right-hand isomorphism in (3) identify its image
with the full lattice \(T^{-1}(\mathbb Z\mathbf1)\).
Over \(\mathbb Q\), T is onto, so this lattice has rank
\(q-r+1\). Hence \(c_b=q-r+1\), as in pass33.

Now assume \(c_b=1\). Then \(q=r\), so every base branch has
exactly one source normalization point. Its index is the degree
\(N_j\) of that component's finite affine-line cover. Consequently
\[
\begin{gathered}
T=\operatorname{diag}(N_1,\ldots,N_r),\qquad
\gcd(N_i,N_j)=1\quad(i\ne j),\\
T^{-1}(\mathbb Z\mathbf1)
=\mathbb Z(\ell/N_1,\ldots,\ell/N_r),\qquad
\mu_b=\ell=\operatorname{lcm}_jN_j=\prod_jN_j.
\end{gathered}
\tag{5}
\]
The last equality with \(\mu_b\), the generic scheme multiplicity
of this irreducible fiber, is the integral linking calculation.
The source support group is \(\mathbb Z\), and exactness identifies
its image with the entire lattice just displayed, not a finite-index
sublattice. Its positive generator therefore maps on the base side
to \(\ell\) times the sphere at b. At a general smooth point of
the reduced fiber, take a transverse complex surface. The restriction
of \(\pi\) is a finite germ with an isolated zero. Its local
degree is the length of the two-parameter quotient, namely
\(\mu_b\): a finite map between smooth surfaces is flat, and a
nearby regular value has that many positively oriented preimages.
The induced linking-sphere degree is the same integer. This proves
the claimed identification and its positive sign.

Repeated branches from one retained component are impossible here:
they would repeat the same \(N_i\ge2\), violating coprimality.
The degree bound in (2) now gives
\[
\begin{array}{c|c|c}
d&\text{possible branch degrees}&\mu_b\\ \hline
2&(2)&2\\
3&(2),\ (3),\ (2,3)&2,\ 3,\ 6.
\end{array}
\tag{6}
\]
In the last case the two branches belong to distinct retained
components. No embedded smoothness of these base branches is implied:
an affine-line normalization does not make the plane curve smooth.

## 4. The rank-zero sector

Suppose the whole reduced fiber is irreducible and fixed by N.
Let \(\mathfrak q\) be its generic prime and
\(O=A_{\mathfrak q}\), a regular local ring of dimension two
with residue field \(L=\kappa(\mathfrak q)\). Its maximal ideal
is \(\mathfrak n\). Write \(m\subset S\) for the maximal
ideal of b; its two base parameters generate the
\(\mathfrak n\)-primary complete intersection \(mO\).

If \(ds_1,ds_2\) both vanish in
\(\Omega_{A/\mathbb C}\otimes_A L\), then
\(mO\subset\mathfrak n^2\). Indeed the conormal sequence of
the generically smooth curve in the smooth threefold is injective
on \(\mathfrak n/\mathfrak n^2\), and sends the two parameter
classes to these differentials. Since
\(\operatorname{gr}_{\mathfrak n}O=L[\xi,\eta]\), two
generators in \(\mathfrak n^2\) impose at most two independent
relations on its three-dimensional quadratic part. Therefore
\[
\mu_b=\operatorname{length}(O/mO)\ge1+2+1=4.
\qquad
\begin{cases}
d=2:\ \text{such an irreducible rank-zero fiber is impossible};\\
d=3:\ \mu_b=6\text{ and the retained branch degrees are }2,3.
\end{cases}
\tag{7}
\]
The independent [local multiplicity proof92](nonconical-closed-fiber-multiplicity-pass92.md),
read through EOF, gives \(4\le\mu_b\le2d\) for any rank-zero
component, without requiring the whole fiber to be irreducible.
It also proves that both relative generators \(A_1,A_2\) become
constants there and that the reduced component is
\(\operatorname{Spec}\mathbb C[\bar c]\).
Thus its degree-two list is \(\{4\}\), whose intersection with
the whole-irreducible topological list \(\{2\}\) is empty.
Its degree-three list \(\{4,5,6\}\) intersects (6) only in six.
This is an exclusion of the stated sector, not an assertion that
every fixed component belongs to that sector. The topological list
already suffices for (7) together with the elementary lower bound;
the local result also describes the surviving reduced component.

The subsequent [total-fiber bound92](nonconical-total-fiber-multiplicity-pass92.md)
strengthens the degree-two consequence. Its sum over every component
is at most four, so one generic rank-zero component of multiplicity
four leaves no other component. Applying (7) then excludes **all
generic rank-zero components in degree two**, without an initial
whole-fiber irreducibility assumption. This is a forward consequence
using the present theorem, not an extra input to its proof. It still
does not exclude isolated rank drops on a generically rank-one curve.

In particular, degree two does not become fixed-point-free: a
rank-one irreducible fixed fiber of multiplicity two is allowed,
as are fixed components in reducible fibers. Nor does degree three
produce a contradiction from (7): a multiplicity-six crossing is
left open. The fixed-scheme thickness is a different invariant and
remains uncontrolled by (6), as the actual polynomial comparisons in
[fixed-scheme92](nonconical-fixed-scheme-structure-pass92.md) show.

## 5. Read and proof provenance

The full retained pass33 branch-count note, pass34 integer-ramification
note and pass46 quadratic-monodromy note were read for this transfer.
The cylinder applicability in Section 1 is explicitly deduplicated
to pass46. The present contribution is the scoped combination (6)--(7),
not a new general topological theorem. Root requested the comparison
with the new rank-zero local bound; Geometry reconstructed the
integral support argument and the source hypotheses.

No numerical method was introduced or run. No frozen pass91 or
earlier file was changed. The conclusion concerns the supplied
special frame and does not provide a bridge to arbitrary sliced
actions.

[^kaliman]: Shulim Kaliman,
    [*Free C+-actions on C3 are translations*, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf).
    Fresh source reads comprise the complete displayed statements
    and proofs of Lemmas 2.1--2.2 and 3.1, all three steps of
    Proposition 3.2, Lemma 4.1, Propositions 4.2 and 5.1, together
    with Notation 2.3 and the complete Theorem 5.2 statement and its
    displayed deduction from those propositions. The source's
    underlying Milnor, Thom/excision, Stein and surface-contraction
    dependencies were not all freshly re-proved. Section 2 uses its
    exact homology diagram; (4)--(7) are the derived lattice and
    local-length arguments, not quotations of a published theorem.
