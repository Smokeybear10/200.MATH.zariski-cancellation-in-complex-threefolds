# The Heisenberg common base is already known globally

This is a source and applicability audit, not a new polynomial-plane
theorem. It resolves a misleading formulation of the remaining pass-43
problem: the global common invariant ring is already a polynomial plane.
The unresolved part is its actual inclusion in the threefold and the
exceptional fibers. The localized common ring is an open plane, not a
polynomial plane.

## 1. Exact identification and prior-work boundary

Retain the actual hypotheses of
[the polynomial Heisenberg repair](quadratic-heisenberg-repair-pass43.md).
Write
\[
B=A[s_*]=\mathbb C^{[4]},\qquad Es_*=1,\qquad A=\ker E,
\]
and let \(V\ne0\) be its central LND. The compatible element
\(\tau\) satisfies \(E\tau=g^m\ne0\) and \(V\tau=0\).
Consequently \(E,V\) are fraction-field independent: a relation
\(V=fE\) would give \(fg^m=0\). In particular
\[
d:=V|_A\ne0,\qquad S_0:=A\cap\ker V=\ker_A d.
\tag{1}
\]

The earlier [intrinsic quotient proof](intrinsic-quotient-surface-pass.md)
already applies to every such \(d\), not only to a known polynomial
threefold. Here is the precise source gate again. The cylinder makes
\(X=\operatorname{Spec}A\) smooth and contractible. Its smooth
surjection \(\mathbb A^4\to X\) restricts to a dominant morphism
from an affine linear three-plane: choose its tangent space complementary
to the one-dimensional differential kernel at any point. Thus the source
is \(\mathbb A^1\times\mathbb A^2\), as required by
Kaliman--Saveliev Corollary 2.8(2). It follows that
\[
S_0\simeq\mathbb C^{[2]}.
\tag{2}
\]
Their Lemma 2.1 gives nonempty curve fibers. Smoothness of \(X\),
smoothness of the plane base, and the local dimension formula give
faithful flatness of \(S_0\to A\) by miracle flatness, exactly as
in the earlier note. Neither an intrinsic slice nor freeness is inserted.

On \(B_g\), the pass-43 fields are
\[
\delta=E/g,\qquad C=aV/g^2,\qquad a=(m-1)/2\ne0.
\]
Since \(Eg=Vg=0\), taking either kernel commutes with this
localization. For example \(E(b/g^N)=0\) means \(Eb=0\).
Therefore the common ring denoted \(S\) in the rank-two normal form is
exactly
\[
S=\ker_{B_g}\delta\cap\ker_{B_g}C=(S_0)_g.
\tag{3}
\]
There is no finite-generation or surface-recognition gap in (3).
However, because \(g\) is nonconstant, \(S\) contains the
nonconstant unit \(g\) and cannot be isomorphic as a complex algebra
to \(\mathbb C^{[2]}\). It is the coordinate ring of the complement
of \(g=0\) in the plane (2). The earlier caution that the local-slice
calculation itself did not assert polynomiality remains correct; (2)
supplies the missing global context by a separate, previously used theorem.

The omitted actual direction \(T_cg=0\) is not needed for (1)--(3).
It does not say \(T_cS_0=0\), that \(S_0\) is an ambient coordinate
plane, or that the inclusion \(S_0\subset A\) splits.

## 2. The remaining published sufficient hypothesis, in exact algebra

For any nonzero LND \(U\) on \(B\) commuting with \(E\), with
nonzero restriction \(d_U=U|_A\), define the ambient ideal
\[
J(E,U)=
\big(E(x_i)U(x_j)-E(x_j)U(x_i):1\le i<j\le4\big)B.
\tag{4}
\]
This does not depend on the displayed polynomial coordinates: it is
the image ideal of the alternating biderivation \(E\wedge U\).
In the actual presentation \(B=A[s_*]\), write
\(U=d_U+q\partial_{s_*}\), where \(q=U(s_*)\in A\).
The \(q\)-terms cancel from the wedge. Its values on
\((s_*,a)\), \(a\in A\), are \(d_U(a)\), while all its
values belong to the ideal those elements generate. Hence
\[
J(E,U)=(d_U(A))A\cdot B.
\tag{5}
\]
This is the same coordinate-independent calculation used in
[pass 15](commuting-quotient-pass15.md), now without requiring the
second ambient field to be a coordinate partial.

Faithful flatness of adjoining \(s_*\) makes
\[
J(E,U)=B
\quad\Longleftrightarrow\quad
(d_U(A))A=A.
\tag{6}
\]
In characteristic zero the latter says that the actual intrinsic
additive action has no fixed point and is free. Kaliman--Saveliev
Corollary 2.8(1),(3), with the verified domination above, then gives
\(A\simeq\mathbb C^{[3]}\). Thus (6) is a finite ideal-membership
certificate for a genuine published sufficient hypothesis. It is not
claimed to follow automatically from the cylinder or from rank two.

For the unreduced pass-43 field \(V\), this particular test cannot
succeed. The actual identity is
\[
V=-\frac ga[E,T_c].
\tag{7}
\]
The field \([E,T_c]\) is a polynomial LND centralizing \(E\),
by the good-column adjoint bound and the leading-coefficient argument.
Consequently \(J(E,V)\subseteq gB\ne B\), and its intrinsic
restriction is \(g\)-divisible. Any freeness attempt must at least
remove this invariant factor, and potentially further invariant factors,
before applying (6). The rank-two Heisenberg repair may still be an
invariant replica of the same primitive direction; its existence alone
does not make (6) a unit ideal.

## 3. Existing exact control for the geometric shortcut

Reuse the actual triangular action from the earlier intrinsic-quotient
note, rather than count it again as a new example. On
\(B=\mathbb C[x,y,z,s_*]\), put
\[
E=\partial_{s_*},\qquad
V=x\partial_y+2y\partial_z,\qquad Y=s_*V,
\qquad g=x,\qquad T=\partial_z.
\tag{8}
\]
These are LNDs, \([E,Y]=V\), \([E,V]=[Y,V]=0\), and their
fraction-field rank is two. The actual constant direction \(T\)
kills \(g\). Nevertheless
\[
S_0=\mathbb C[x,xz-y^2],\qquad
J(E,V)=(x,y)B\ne B.
\tag{9}
\]
The field \(V\) is already primitive. Thus even a global sliced
Heisenberg action, a polynomial common base, and an omitted constant
direction do not force its primitive intrinsic direction to be free.
This example is already polynomial and is not claimed to realize the
additional high-degree full-frame hypotheses.

Its natural invariant inclusion has no algebra retraction: if it did,
images \(Y_0,Z_0\in\mathbb C[x,v]\) of \(y,z\) would satisfy
\(xZ_0-Y_0^2=v\); modulo \(x\) this would make \(-v\) a
polynomial square in \(\mathbb C[v]\). The fibers over
\((x,v)=(0,\beta)\) are two disjoint lines for \(\beta\ne0\)
and a double line for \(\beta=0\). These are precisely the kinds
of phenomena that faithful flatness and (2) do not remove.

For completeness, the localized projection can collapse even in this
actual Heisenberg control. With \(\delta=E/x\), \(L=Y/x\),
\(C=V/x^2\), and \(\sigma=xs_*\), one has
\(\delta\sigma=1\), \(C\sigma=0\), \(L\sigma=0\), and
\(L-\sigma C=0\). This is not an obstruction to recognizing
\(A\); it is a scope control for the selected repair.

## 4. Source audit and stopping boundary

The author-hosted final Kaliman--Saveliev text was directly reread:
Lemma 2.1, Theorem 2.7 with its proof, Corollary 2.8 with its proof,
and the alternative argument in Section 3. The exact theorem applies
to \(X\), not just to \(\mathbb A^3\).

A seemingly relevant later lead,
Gurjar--Koras--Miyanishi--Russell, *Affine threefolds admitting
Ga-actions*, arXiv:1502.01849, is explicitly withdrawn. Its current
arXiv record says Theorem 3.1 is false in the posted version.
No recognition statement from that preprint is used here.

The bounded outcome is therefore a precise deduplication and a finite
global sufficient test, not a new recognition regime. The relevant
unproved obligation is to control the actual primitive fixed-locus
ideal, find an independent intrinsic direction, or exploit further
full-frame equations. Proving the common base polynomial again cannot
close that gap. No new executable suite or method count is claimed.

## Sources

- Shulim Kaliman and Nikolai Saveliev,
  [*C+-actions on contractible threefolds*](https://www.math.miami.edu/~kaliman/library/KaSa.michigan.2004.quotient.pdf),
  Lemma 2.1, Theorem 2.7, Corollary 2.8 and Section 3. The geometric
  conclusions in Sections 1--2 are applications of this prior theorem.
- [Stacks Project, Tag 00R4](https://stacks.math.columbia.edu/tag/00R4),
  miracle flatness, used with regular local base and Cohen--Macaulay
  local total space as in the linked earlier proof.
- [arXiv:1502.01849 current record](https://arxiv.org/abs/1502.01849),
  directly checked withdrawal statement. This source supplies only
  the exclusion from the proof dependency list.
