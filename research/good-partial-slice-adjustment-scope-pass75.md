# A commuting LND can fix the supplied slice, but short flow need not survive

The relevant centralizer theorem does permit a polynomial adjustment
of a commuting LND so that it kills the supplied slice. Local
nilpotence survives. An actual derived-good-partial example shows
that its coordinate flow degree can nevertheless become arbitrarily
large. Thus adjustment is available, but does not by itself supply
the low-flow or nice hypotheses needed for a recognition theorem.

The source theorem was already cited in the
[global-symmetry literature note](global-symmetry-bridge-literature.md),
Section 1. The application and the exact loss-of-degree control are
the bounded purpose of this pass, not a new centralizer theorem or
an unrestricted cancellation claim.

## 1. Exact source gate and its LND consequence

Let \(B\) be a characteristic-zero domain, and suppose
\[
E,Q\in\operatorname{LND}(B),\qquad Es=1,\qquad [E,Q]=0,
\qquad A=\ker E,\qquad B=A[s].
\tag{1}
\]
The slice \(s\) is the actual supplied element. The LND property
of the auxiliary \(Q\) is a hypothesis here, not a consequence
claimed for an arbitrary bracket of two LNDs.

Bedratyuk, Chapovskyi and Petravchuk, Proposition 2, identify the
centralizer of a sliced LND as the semidirect sum of its kernel
and the derivations of that kernel.[^centralizer] In the actual
presentation (1), this is the unique decomposition into a multiple
of \(E\) and a derivation fixing \(s\).

In particular put
\[
c=Qs\in A,\qquad Q_0=Q-cE.
\]
Then
\[
Q_0s=0,\qquad [E,Q_0]=0,\qquad
Q_0|_A=Q|_A,\qquad Q_0\in\operatorname{LND}(B).
\tag{2}
\]
Here is the complete local-nilpotence justification, which must
not be replaced by closure of LNDs under subtraction. Commutation
gives \(Q(A)\subseteq A\) and \(E(Qs)=Q(Es)=0\). Restriction
therefore gives an actual LND \(Q|_A\). Since \(Q_0s=0\),
the derivation \(Q_0\) on \(A[s]\) applies this restriction
coefficientwise and kills \(s\). Each polynomial has finitely
many coefficients in \(A\), so some common iterate kills all
of them. Hence \(Q_0\) is locally nilpotent. The commutator in
(2) also follows directly from \(Ec=0\).

If \(Q\) and \(E\) were independent over \(\operatorname{Frac}B\),
then \(Q_0\ne0\) and remains independent of \(E\). Neither
polynomiality of \(A\) nor a coordinate assertion about \(s\)
was used. This is an action on the original cylinder, not
a derivation constructed only after invariant localization.

The same paper's Theorem 4 says that the full derivation
centralizer has maximal fraction-field rank. It does not make
its generators locally nilpotent or pairwise commuting.
Its proof extends transcendence-basis partials to a function
field and clears denominators. As already recorded in the
older literature note, this is not a coordinate-frame theorem.

## 2. What the adjustment does to a nice velocity

Now let \(B=\mathbb C[x_1,x_2,x_3,x_4]\), let \(P=Ex\),
and assume in addition
\[
EP=0,\qquad Q(P)=0.
\]
Commutation gives \(E(Qx_i)=Q(P_i)=0\), so \(Qx_i\in A\).
Also \(Q^j s\in A\) for \(j\ge1\). On these elements
\(Q_0\) equals \(Q\), and it kills each \(P_i\). Induction gives
the exact formula
\[
Q_0^{\,n}x_i=Q^{\,n}x_i-(Q^{\,n}s)P_i
\qquad(n\ge1).
\tag{3}
\]
The first step is the definition. Applying \(Q_0\) to the next
step uses its equality with \(Q\) on \(A\), and no derivative
of \(P_i\) remains.

Thus the short flow of \(Q\) is not the only input controlling
the flow of \(Q_0\). The \(Q\)-degree of the supplied slice
also enters. For example, if \(Q^r x=0\) and \(Q^h s=0\),
then (3) gives \(Q_0^n x=0\) for \(n\ge\max(r,h)\).
There is no uniform small value of \(h\) in (1).

## 3. Unbounded loss for the actual derived-good-partial example

Use the already recognized de Bondt example in
[the good-partial boundary note](nice-good-partial-boundary-pass75.md):
\[
a=xz-y^2+w,\qquad
P=(1,a,a^2,-a^2x+2ay-z)^t,\qquad E=P\cdot\partial.
\]
Its actual coordinates and inverse are
\[
Y=y-xa,\quad Z=z-xa^2,\qquad (x,a,Y,Z),
\]
\[
y=Y+xa,\qquad z=Z+xa^2,\qquad
w=a-xZ+Y^2+2xaY.
\tag{4}
\]
In these coordinates \(E=\partial_x\). The original partial
\(T=\partial_w\) is its sole constant good direction, and
\[
Q=[T,E]
=\partial_y+2a\partial_z+(-2ax+2y)\partial_w
=\partial_Y+2a\partial_Z
\]
in (4). In particular \(Q(P)=0\), \(Qx=Qa=0\), \(QY=1\),
and \(Q^3\) kills all four original coordinates. Those exact
original-frame facts and both orders of (4) are supplied in
the linked note, not inferred merely from commutation.

For any integer \(d\ge3\), supply the polynomial slice
\[
s_d=x+Y^d,\qquad Es_d=1,\qquad
Qs_d=dY^{d-1},\qquad
Q_0=Q-dY^{d-1}E.
\tag{5}
\]
Then \(Q_0Y=1\) and \(Q_0x=-dY^{d-1}\), whence
\[
Q_0^{\,n}x=-\frac{d!}{(d-n)!}Y^{d-n}\quad(1\le n\le d),
\qquad Q_0^{\,d+1}x=0.
\tag{6}
\]
In particular the coordinate \(x\) has exact \(Q_0\)-degree
\(d\). Formula (3), \(Q^3x_i=0\), and
\(Q^{d+1}s_d=0\) show that the full original coordinate-flow
degree of \(Q_0\) is exactly \(d\), not just bounded below
by \(d\).

There is also a complete actual coordinate check of all these
claims. Set \(R=Z-2aY\). The coordinates
\((S,A,V,R)=(s_d,a,Y,Z-2aY)\) have polynomial inverse
\[
\begin{aligned}
x&=S-V^d,&\quad y&=V+(S-V^d)A,\\
z&=R+2AV+(S-V^d)A^2,&
w&=A-(S-V^d)R+V^2 .
\end{aligned}
\tag{7}
\]
They are (4) followed by two elementary triangular changes,
so both inverse orders hold. Here \(E=\partial_S\) and
\(Q_0=\partial_V\). The adjustment is genuinely polynomial
and locally nilpotent, despite its arbitrarily high flow degree
in the original displayed frame.

The example does have an \(E\)-slice fixed by the original
\(Q\), namely \(x\). It does not disprove existence of a
replacement slice in general. Its claim is narrower: even an
auxiliary action derived from the sole good partial, with
short original flow, can lose that short-flow bound when
adjusted to fix a particular supplied slice.

## 4. Classification scope and the next valid action

The bounded search did not locate a primary classification
covering every nonhomogeneous nice sliced four-variable action
with \(J=\operatorname{Jac}P\), \(\operatorname{rank}J=2\),
\(\operatorname{rank}J^2=1\), and just one constant good
partial. This is not a claim of an exhaustive literature search.

The exact nearby gates remain distinct:

- De Bondt's Theorem 5.3 classifies homogeneous
  quasi-translations of Jacobian rank two; homogeneity is
  explicit. The retained statement and proof were reread.[^ranktwo]
- Dasgupta--Gupta's Theorem 3.6 concerns an actual polynomial
  three-ring over a PID and an irreducible nice relative LND.
  Corollary 3.8 explicitly assumes one actual invariant coordinate
  in the four-ring.[^relative]
- The spatially quadratic nice case is already closed by
  [pass74](nice-slice-adjoint-rank-pass74.md). Nothing here
  reopens that case.

In the second item, LND rank counts coordinates that can be
fixed after actual polynomial changes. It is not Jacobian
rank. A good partial has \(\operatorname{ad}_E^2T=0\);
this is not an invariant coordinate for \(E\), and it does
not give generator-wise niceness of \(Q\).
The complete pass40 nice-centralizer note was reread:
polynomiality of an auxiliary kernel does not identify the
original kernel or transfer the original slice.

Accordingly one may legitimately use (2) to arrange that the
second action fixes the supplied slice. The next missing input
is control of the resulting intrinsic action and its actual
coordinates, not existence of the adjustment itself.
Any use of a short-flow or relative nice theorem after that
adjustment needs its hypotheses proved anew. No invariant
coordinate, two-slice system, or universal degree bound follows
from the centralizer theorem alone.

## Sources and exact access

[^centralizer]: L. Bedratyuk, Y. Chapovskyi and A. Petravchuk, [*Centralizers of linear and locally nilpotent derivations*](https://arxiv.org/html/2302.02441v1), arXiv:2302.02441v1, submitted February 5, 2023; [primary PDF](https://arxiv.org/pdf/2302.02441v1). Section 4, Proposition 2 and Theorem 4, including both complete displayed proofs and the preceding Lemma 6, were freshly read. The algorithm in Section 3 is for a basic Weitzenboeck derivation, not the nonlinear \(E\) here. The same selected results were already recorded in the earlier global-symmetry note. The HTML's generated date is not treated as a new manuscript version.

[^ranktwo]: Michiel de Bondt, [*Quasi-translations and singular Hessians*](https://arxiv.org/abs/1501.05168), arXiv:1501.05168v1, Theorem 5.3. The retained primary text at [the local source path](../tmp/pdfs/bondt-1501.05168v1.txt), including Theorems 5.2--5.3 and the displayed proof of 5.3, was reread. No new complete audit of every lemma cited there is claimed.

[^relative]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/abs/1701.03635), arXiv:1701.03635v1, Theorem 3.6 and its complete proof, Corollaries 3.7--3.8, freshly reread in [the retained text](../tmp/pdfs/dg-nice-1701.03635v1.txt).

This note adds no numerical method, full regression, historical
novelty assertion, human expert review, or formal verification.
The elementary specialization (2) and the family (5)--(7)
have complete written proofs above. Independent reviews must
be recorded separately. All pass74-or-earlier artifacts and
shared metadata are unchanged.
