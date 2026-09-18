# Every normalized exceptional-cover branch is reached

In the actual contractible quotient setting, the map from the normalized
exceptional surface to the normalized finite intermediate curve is surjective.
This is stronger than surjectivity before normalization. It follows from the
peripheral-cycle argument, without assuming that any special fiber is reduced,
smooth, irreducible or an affine line.

The deduction separates two steps in the earlier
[pointwise proof](pointwise-plinth-pass17.md): smoothness of a whole affine-line
fiber was used to produce an unreached branch; the topological contradiction
to an unreached branch does not require that smoothness. No general implication
from surjectivity to normalized surjectivity is being asserted.

## 1. Actual hypotheses and finite normalizations

Let \(A\) be a complex domain with \(A[s_*]\simeq\mathbb C^{[4]}\), and let
\(D\ne0\) be a primitive locally nilpotent derivation with
\(C=\ker D\simeq\mathbb C^{[2]}\). Put
\[
X=\operatorname{Spec}A,\qquad S=\operatorname{Spec}C,
\qquad \pi:X\longrightarrow S.
\tag{1}
\]
The cylinder gives a smooth factorial affine threefold and
\(H_2(X;\mathbb Q)=H_3(X;\mathbb Q)=H_4(X;\mathbb Q)=0\), as checked in
[the intrinsic pointwise extension](intrinsic-pointwise-plinth-pass47.md).
In particular this statement does not assume \(A\simeq\mathbb C^{[3]}\).

Use the actual exceptional factorization
\[
E\xrightarrow{\kappa}Z\xrightarrow{\theta}\Gamma,
\qquad E=\pi^{-1}(\Gamma)_{\mathrm{red}}.
\tag{2}
\]
Here \(\Gamma\) is the retained reduced plinth support. Its irreducible
component pullbacks are reduced irreducible surfaces. Kaliman's construction
uses a proper compactification and its Stein factorization, then takes the
image of \(E\). Its curve \(Z\) is not defined as the full invariant spectrum.
The actual geometry supplies finite \(\theta\), surjective \(\kappa\), a
dense product \(E^*\simeq Z^*\times\mathbb A^1\), and
\(X\setminus E\simeq(S\setminus\Gamma)\times\mathbb A^1\).[^kal]

Normalize all components, writing
\[
\nu_E:E^\nu\longrightarrow E,\qquad
\nu_Z:Z^\nu\longrightarrow Z.
\]
These are finite maps of complex affine varieties. The dominant maps of each
normal surface component factor through the corresponding normalized curve,
so there is an actual morphism
\[
\kappa^\nu:E^\nu\longrightarrow Z^\nu.
\tag{3}
\]
The normalized covers also factor as finite positive-degree maps
\(Z_i^\nu\to\Gamma_i^\nu\). The normalization factorization is the usual
normal-source universal property.[^norm] Its existence does not imply its
surjectivity.

The assertion to prove is
\[
\boxed{\quad\kappa^\nu:E^\nu\longrightarrow Z^\nu
\text{ is surjective, component by component.}\quad}
\tag{4}
\]

## 2. The homology implication and whole-fiber support

Choose a finite \(F\subset\Gamma\) containing a specified point \(q\),
all singular and ramification values, and every exceptional value needed for
the product chart. Write
\[
X^*=X\setminus\pi^{-1}(F),\quad S^*=S\setminus F,
\quad\Gamma^*=\Gamma\setminus F,\quad Z^*=\theta^{-1}(\Gamma^*),
\]
\[
\widehat X=X\setminus E,\qquad\widehat S=S\setminus\Gamma.
\]
On these opens the normalized and unnormalized curves agree. The relevant
exact diagram is
\[
\begin{array}{ccccc}
H_3(X^*)&\xrightarrow{\phi'}&H_1(Z^*)&\xrightarrow{\psi'}&H_2(\widehat X)\\
\downarrow&&\downarrow\theta_*&&\downarrow\cong\\
H_3(S^*)&\xrightarrow{\phi}&H_1(\Gamma^*)&\xrightarrow{\psi}&H_2(\widehat S).
\end{array}
\tag{5}
\]
The Thom maps have the ordinary curve pushforward in the middle because the
component pullback divisors are reduced. The right map is an isomorphism from
the product complement. Thus
\[
\theta_*\beta\in\operatorname{im}\phi
\quad\Longrightarrow\quad\beta\in\operatorname{im}\phi'.
\tag{6}
\]
All homology here has rational coefficients.

Let \(L=\pi^{-1}(F)\). The vanishings of \(H_4(X)\) and \(H_3(X)\) identify
\(H_3(X^*)\) with \(H_4(X,X^*)\). Excision and naturality of the Thom map
under open inclusions show that, for a sufficiently small open neighborhood
\(U\) of the entire \(L\),
\[
\operatorname{im}\phi'
\subseteq\operatorname{im}\bigl(H_1(E^*\cap U)\to H_1(Z^*)\bigr).
\tag{7}
\]
This is the source's support argument, also reconstructed in pass 17,
Sections 2 and 4. It applies to the entire fiber supports, regardless of
nilpotents or singularities in their scheme structures.

## 3. Excluding an arbitrary unreached normalized point

Suppose \(\zeta_0\in Z^\nu\) over \(q\) is not in the image of (3).
There are finitely many normalized points above \(F\). Call such a point
*reached* if it is the image under (3) of a point of \(\nu_E^{-1}(L)\).
Choose disjoint small disks around all these normalized points and let
\(V\) be the union of disks centered at reached points only. Then
\[
O=(\kappa^\nu)^{-1}(V)
\]
is open in \(E^\nu\) and contains the whole \(\nu_E^{-1}(L)\), by the
definition of reached. No assertion about the number of normalized copies of
a fiber is needed.

The finite normalization \(\nu_E\) is proper in the complex topology. Hence
\[
E\setminus\nu_E(E^\nu\setminus O)
\tag{8}
\]
is an open neighborhood of the whole \(L\). Choose \(U\subset X\) meeting
\(E\) only in (8), and shrink within the inverse images of small disjoint
neighborhoods of the points of \(F\). On \(E^*\cap U\), normalization is an
isomorphism and the image lies in the punctured disks around reached points.
Consequently (7) implies that \(\operatorname{im}\phi'\) lies in the span
of their peripheral loops. In particular its coefficient at the loop around
\(\zeta_0\) is zero.

These finite peripheral loops are independent in \(H_1(Z^*)\). On each
smooth affine normalized component, the only relation among all puncture
loops in its smooth compactification is their total sum. At least one
puncture lies at infinity and is not among the points above \(F\), so there
is no relation among the finite loops under consideration.

Let \(\gamma_1,\ldots,\gamma_k\) be the loops of all normalized base
branches at \(q\). The small sphere class \(\omega_q\) satisfies
\(\phi(\omega_q)=\sum_j\gamma_j\). Select a normalized cover point above
each branch, using \(\zeta_0\) for its branch. Let \(\beta_j\) be its loop
and \(e_j>0\) its ramification index. Then
\[
\beta=\sum_{j=1}^k e_j^{-1}\beta_j,
\qquad\theta_*\beta=\sum_j\gamma_j=\phi(\omega_q).
\tag{9}
\]
By (6), \(\beta\in\operatorname{im}\phi'\), contradicting its nonzero
coefficient at the unreached loop. This proves (4). Away from \(F\),
surjectivity already follows from the dense product chart.

This proof uses neither properness of \(\pi\) nor compactness of its fiber.
Properness is used only for the finite normalization in (8). It also does not
require a free action on the special fiber. Surjectivity before normalization
alone would not supply (7) or (6), which are the essential extra conditions.

## 4. No poles and the full exceptional invariant ring

Fix an exceptional component \(E_i\), and let \(D_i\) be its induced
nonzero derivation. Primitivity in the actual factorial setting ensures it
does not vanish identically on \(E_i\). Write
\[
T_i=\mathcal O(E_i)^{D_i},\qquad
N_i=\mathcal O(Z_i^\nu),\qquad B_i=\mathcal O(\Gamma_i).
\]
The dense product chart identifies the rational invariant field with
\(\mathbb C(Z_i)\). Thus every element of \(T_i\) is a rational function
on \(Z_i^\nu\) whose pullback is regular on \(E_i^\nu\).

Such a function cannot have a pole at a point \(\zeta\). By (4) choose
\(x\in E_i^\nu\) above it. If its pole order were \(n>0\), a local
parameter \(t\) at \(\zeta\) would satisfy \(t^nf=u\) for a local unit
\(u\). Pulling back to the local ring at \(x\), the left side lies in its
maximal ideal and the right side is a unit. This is impossible. Therefore
\[
B_i\subseteq T_i\subseteq N_i.
\tag{10}
\]
Since \(N_i\) is finite over the Noetherian ring \(B_i\), (10) makes
\(T_i\) finite over \(B_i\). Localizing at an invariant base function
defining the dense product chart gives its invariant curve ring. Passing
to fraction fields therefore gives \(\operatorname{Frac}T_i=\mathbb C(Z_i)\).
The normal ring \(N_i\) is
integral over \(B_i\), hence over \(T_i\), and is its integral closure.

This proves finiteness of the full exceptional invariant ring in this actual
setting. It still does not assert \(Z_i=\operatorname{Spec}T_i\); these may
be different finite, nonnormal models of the same normalized curve.

A useful local form of the same conclusion is this: if an actual invariant
\(f\) vanishes on the whole fiber \(\pi^{-1}(q)\), its function on
\(Z_i^\nu\) is regular and vanishes at every point over every normalized
base branch of \(q\). The values follow by pulling back to reached points.
This allows a quadratic minimal polynomial of an actual invariant to detect
an impossible nonzero second residue value, without first identifying the
fiber as an affine line.

## 5. Scope and attribution

The result is a source-dependent extension of the existing whole-fiber support
argument. It is not stated here as a theorem quoted verbatim from Kaliman or
as a historical novelty claim. The elementary nodal example in pass 17,
Section 6, still shows that finite \(\theta\), surjective \(\kappa\) and a
smooth individual fiber do not imply (4) without the actual diagram.

No numerical checker is attached: the new assertion is the universal
topological support implication, not a finite polynomial identity. The
argument was independently reconstructed by the root agent and the jet
reviewer. That review is not external expert certification. No frozen earlier
file or shared metadata is changed. Applications still have to identify the
actual quadratic invariant field and an actual normalized point with the
forbidden value; a curve relation inside a smaller subalgebra is not enough.

## Sources

[^kal]: Shulim Kaliman, [*Free C+-actions on C3 are translations*, final author PDF](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf), *Inventiones Mathematicae* 156 (2004), 163–173. Lemmas 2.1–2.2, Lemma 3.1, and Proposition 3.2, especially diagram (*) and the full excision/support argument on PDF pages 5–7, were directly reread. The general theorem is applied to the unknown intrinsic threefold using the precise hypotheses established in pass 47, not by assuming its coordinate ring polynomial.

[^norm]: The Stacks Project, [Lemma 29.55.5, 035Q](https://stacks.math.columbia.edu/tag/035Q), especially part (4), [Lemma 33.41.2, 0C1R](https://stacks.math.columbia.edu/tag/0C1R), and [Lemma 29.55.11, 035S](https://stacks.math.columbia.edu/tag/035S), directly read with their displayed proofs. These supply the normal-source factorization, the curve's local integral-closure description, and finiteness of normalization for Nagata schemes. The exceptional surfaces are affine varieties over \(\mathbb C\), hence Nagata.
