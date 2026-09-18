# Quadratic fiber components have no punctures

Every reduced component of every closed fiber in the supplied
actual quadratic frame is an entire affine line. The earlier
smooth-open-line conclusion can be strengthened using ordinary
homology in one degree higher than the ramification diagram.
The argument does not exclude nonreduced fibers or fixed curves.

## 1. The precise input and statement

Let \(X=\operatorname{Spec}A\) and \(Y=\operatorname{Spec}S\)
be the actual smooth threefold and invariant affine plane of
[everywhere rank95](quadratic-quotient-rank-everywhere-pass95.md).
In particular,
\[
\begin{gathered}
A[u]=\mathbb C^{[4]},\qquad S=\mathbb C[s_1,s_2],\qquad
N\in\operatorname{LND}(A),\qquad \ker N=S,\\
\pi:X\longrightarrow Y\text{ is faithfully flat},\\
(\pi^{-1}(b))_{\rm red}=\coprod_i L_{b,i},\qquad
L_{b,i}\simeq\operatorname{Spec}
\mathbb C[U_{b,i},1/b_{b,i}(U_{b,i})]
\quad(b\in Y(\mathbb C)).
\end{gathered}
\tag{1}
\]
The components in (1) are smooth and pairwise disjoint by
the full theorem95. That input is essential to the particular
codimension-two Thom argument below. No claim is made here
about an arbitrary possibly singular curve fiber.

The cylinder makes the complex manifold X contractible:
projection \(X\times\mathbb C\to X\) is a homotopy
equivalence, and the cylinder is complex affine four-space.
All homology below is ordinary singular homology with
integer coefficients, including for noncompact spaces.

We prove that every polynomial \(b_{b,i}\) in (1) is a
nonzero constant after cancelling any redundant presentation.
Equivalently every \(L_{b,i}\) is \(\mathbb A^1\).

## 2. Product strata and the degree-four vanishing

Fix any closed value b. Choose a closed curve
\(\Gamma\subset Y\) such that the quotient is a product
off \(\Gamma\). Such a curve comes from a local slice for
the LND. Enlarge it to contain b if necessary. Restriction
of a product to a smaller open set remains a product.

The quotient-stratum construction of Kaliman's Lemma 2.2
and Notation 2.3 gives a finite set \(\Sigma\subset\Gamma\),
which can be enlarged to contain b, and smooth curves
\(\Gamma^*=\Gamma\setminus\Sigma\) and \(Z^*\), such that
\[
\begin{gathered}
L=(\pi^{-1}(\Sigma))_{\rm red},\qquad
X^*=X\setminus L,\qquad
\check X=X\setminus\pi^{-1}(\Gamma),\\
E^*=X^*\setminus\check X\simeq Z^*\times\mathbb C,\qquad
\check X\simeq(Y\setminus\Gamma)\times\mathbb C .
\end{gathered}
\tag{2}
\]
The product over \(Z^*\) is an actual stratum description,
not an assumption about the bad fibers. Removing further
finitely many base values preserves it. This use does not
require the nonbijective-branch deletion theorem5.2 or
affine-line normalizations of the exceptional curves.[^strata]

The smooth surface \(E^*\) is a closed complex codimension-one
submanifold of \(X^*\). Its normal real plane bundle is
oriented by the complex structure. The ordinary homological
Thom isomorphism and (2) give
\[
H_4(X^*,\check X;\mathbb Z)
\simeq H_2(E^*;\mathbb Z)
\simeq H_2(Z^*;\mathbb Z)=0 .
\tag{3}
\]
Every component of \(Z^*\) is a noncompact smooth curve:
the quasi-finite map to the affine curve \(\Gamma^*\)
precludes a complete component. A noncompact connected
Riemann surface has zero ordinary second homology.

Also \(Y\setminus\Gamma\) is a smooth affine surface.
Indeed a plane curve is principal, so its complement is
affine. Its homotopy type has real CW dimension at most
two, hence its fourth homology is zero. The product
description of \(\check X\) gives \(H_4(\check X)=0\).
The exact sequence of the pair in (3) therefore implies
\[
H_4(\check X)=0,\qquad H_4(X^*,\check X)=0
\quad\Longrightarrow\quad H_4(X^*)=0 .
\tag{4}
\]
This is the same type of Thom/product-complement calculation
used in the published degree-three diagram, but here only
the adjacent degree-four vanishing is needed.[^strata]

## 3. The whole deleted curves and ordinary Thom homology

By (1), L is a finite disjoint union of smooth complex
curves. It is closed in X because \(\Sigma\) is closed
and finite. Thus L is a closed smooth real codimension-four
submanifold of X, possibly disconnected and noncompact.
Its real normal bundle has a complex orientation.

Excision to a tubular neighborhood and the ordinary
homological Thom isomorphism give
\[
H_5(X,X^*;\mathbb Z)
\simeq H_1(L;\mathbb Z).
\tag{5}
\]
A noncompact L does not require replacing the right side
by Borel--Moore homology. One can choose a variable-radius
tubular neighborhood of the closed embedded submanifold.
Its pair with the deleted zero section is the oriented
rank-four disk/sphere bundle pair. The ordinary Thom
isomorphism for that pair shifts ordinary homology by
four; excision identifies it with the pair in (5).
Normal-bundle triviality is not required.

Since X is contractible, its fifth and fourth homology
vanish. The long exact sequence for \((X,X^*)\), together
with (4), makes \(H_5(X,X^*)=0\). Equation (5) now yields
\[
\begin{gathered}
H_1(L;\mathbb Z)=
\bigoplus_{a\in\Sigma}\ \bigoplus_i
H_1(L_{a,i};\mathbb Z)=0,\\
\boxed{\,L_{b,i}\simeq\mathbb A^1
\quad\text{for every closed }b\text{ and every }i.\,}
\end{gathered}
\tag{6}
\]
To see the last implication explicitly, the line component
in (1) is the complex plane minus the finitely many distinct
roots of its denominator polynomial. If it has k missing
points, its first homology is \(\mathbb Z^k\). Thus k=0.
The choice of b was arbitrary.

Nilpotent scheme structure plays no role in these topological
pairs. It was retained in theorem95 to establish the smooth,
disjoint reduced-component input, but it is not discarded
from any subsequent assertion about scheme multiplicity.

## 4. Consequences and limits

The component thickenings of a quadratic closed fiber
therefore contain actual polynomial parameter subrings,
not just localized polynomial PIDs. By the finite-free
argument95, each is a free module of rank its generic
multiplicity over that polynomial parameter ring.
The proof still does not identify its algebra structure.

A noncollapsed fixed component can no longer omit a
value of its surviving good generator. The separate
[compatibility proof96](quadratic-component-compatibility-pass96.md)
uses a closed-point finite-cover argument to prohibit
companions. Its projection-based proof does not depend
on the present puncture-removal theorem, so the two
arguments do not form a dependency cycle.

Rank-one fixed curves and nonreduced whole fibers remain
possible. The conclusion is not an affine-line fibration
with reduced fibers, a free action, or a coordinate
recognition theorem. The original-frame and arbitrary
sliced-action global obligations remain unresolved.

## Sources and proof scope

[^strata]: Shulim Kaliman,
    [*Free C+-actions on C3 are translations*, final author version](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf),
    Lemma 2.2, Notation 2.3, and the opening homology diagram
    of Proposition 3.2. Those selected statements and their
    displayed arguments were freshly read. The paper uses
    ordinary homological Thom identifications and the
    affine-surface homotopy-dimension input. Its general
    Thom and Stein/Milnor references were not freshly
    reconstructed in full. The higher-degree calculation
    (3)--(6) is the deduction written here, not a quotation
    of a theorem asserted in the selected passages.

The smooth-disjoint-fiber theorem95 and its stated
dependencies are retained inputs. Root supplied the
higher-degree argument; Geometry independently checked
its outline, including the noncompact ordinary-Thom
point, before the full note was saved. Saved-file
reviews are recorded separately. No numerical test,
formal verification, historical novelty claim, external
review or general cancellation solution is asserted.
