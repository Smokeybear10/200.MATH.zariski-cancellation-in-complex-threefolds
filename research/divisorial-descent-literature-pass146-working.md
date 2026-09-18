# Residual-coordinate theorems and the actual projected-ring boundary

The available coordinate and affine-line-fibration criteria require
information about the specified ring over its specified base. They do
not turn a generic plane coordinate into a coordinate on every
divisorial fiber. The actual counterexample146 makes that proposed
implication false in the supplied dense three-good setting: its
projected-good ring has a split divisor fiber while its full invariant
overring is already a polynomial line.

This is a statement-level comparison with selected primary sources,
not a classification of the remaining descent problem or a historical
novelty audit.

## 1. Keep the generic line, its model, and its overring distinct

Retain the actual sliced dense three-good hypotheses139 and the
first-tail primitivity conclusion145. With their notation,
\[
A_L=L[v]=L[y,z],\qquad
\ker(L[U,V]\longrightarrow L[v])=(g),\qquad
\Phi\in L^*g,\qquad L[U,V]=L[g]^{[1]}.
\tag{1}
\]
Here \(S=\ker_A N\), \(L=\operatorname{Frac}S\), and the
selected-speed localization has the actual three-generator
presentation \(A_s=S_s[y,z,w_0]\). The last equality in (1) is the
retained generic plane epimorphism theorem, not a conclusion over
\(S_s\).[^1]

Suppose a Noetherian coefficient domain \(R\subset L\), with
\(\operatorname{Frac}R=L\), has been chosen on which a scalar
multiple \(G\) of \(g\) is defined.
The rings to distinguish are
\[
R[U,V],\qquad C=R[U,V]/(G),\qquad D=R[y,z,w_0].
\tag{2}
\]
When the primitive contraction is valid, \(C=R[y,z]\) is an
actual subring of \(D\). Equality of their generic fibers does not
identify their special fibers, or imply \(C=D\). In applying any
theorem below, the Noetherian, flatness, factoriality, or retraction
hypothesis belongs to its displayed base and algebra. These hypotheses
are not supplied merely by changing the names of the rings in (2).

## 2. What the residual-coordinate criterion actually says

For a Noetherian domain \(R\) containing \(\mathbb Q\), with
\(K=\operatorname{Frac}R\), Bhatwadekar--Dutta's Proposition 4.4
states that a generic coordinate \(G\in R[U,V]\) is an
\(R\)-coordinate when its two partial derivatives are comaximal
in the entire polynomial ring.[^2] Babu--Das Theorem 1.1 states
the equivalent forms
\[
\begin{gathered}
K[U,V]=K[G]^{[1]},\\
(G_U,G_V)R[U,V]=R[U,V]
\quad\Longleftrightarrow\quad
G\text{ is a residual coordinate}
\quad\Longleftrightarrow\quad
R[U,V]=R[G]^{[1]}.
\end{gathered}
\tag{3}
\]
Residual here means a coordinate after passing to the residue field
at **every** prime of \(R\), not just the generic point or
height-one primes.[^3]

Their broader Theorem A requires an \(R\)-algebra retract of an
\(R\)-polynomial ring and the full ambient gradient condition.
Corollary B requires a stable polynomial presentation over that same
\(R\). Their quoted DVR theorem assumes an actual
\(\mathbb A^2\)-fibration, including all polynomial fibers.[^3]
The absolute identity \(A[u]=\mathbb C^{[4]}\) does not give
these relative presentations over \(S_s\). Likewise the known
retraction \(A[u]\to A\) does not provide a retraction
\(A_s\to S_s\).

Most importantly, the quotient condition
\((G,G_U,G_V)R[U,V]=R[U,V]\) is weaker than (3).
It controls the zero hypersurface only.

## 3. The distinction occurs in an actual dense sliced frame

The full inverse and intrinsic calculation are given in the
actual divisorial audit146.[^4] In independent variables \(h,k,a,u\),
that frame is
\[
\begin{gathered}
X=h+a^2+ku,\quad Y=a+hu,\quad Z=k-2ah-h^2u,\quad W=u,\\
E=\partial_u,\quad (EX,EY,EZ)=(k,h,-h^2),\quad
N=-h^2\partial_a,\quad S=\mathbb C[h,k],\quad R=S[1/k],\\
G=(V+hU)^2-kV+h^3,\qquad
R[y,z]\simeq R[U,V]/(G),\qquad A_k=R[y,z,w_0]=R[a].
\end{gathered}
\tag{4}
\]
The frame has a polynomial inverse, speed rank two, and dense
homogeneous speed cone. The displayed \(G\) is precisely the
primitive clearing of the canonical first tail. At the unremoved
height-one prime \((h)\), its reduction is \(V(V-k)\), whereas
the actual overring specializes with \(V=k\). Thus the projected
fiber is two disjoint lines, and the full invariant fiber is one line.

The source criterion can be checked directly in this example. Put
\(Q=V+hU\). Then
\[
G_U=2hQ,\qquad G_V=2Q-k,\qquad
(G_U,G_V)\subset(h,V-k/2)\ne R[U,V],\qquad
(G,G_U,G_V)=R[U,V].
\tag{5}
\]
For the last equality, imposing the two derivatives gives
\(Q=k/2\) and \(h=0\), since \(k\) is a unit. Then
\(V=k/2\) and \(G=-k^2/4\) is a unit. This proves the claimed
ideal equality without assuming that smoothness implies a coordinate.

Consequently neither a unit gradient on the zero level nor the
polynomiality of \(A_k\) forces (3) for the smaller projected ring.
The additional projected coordinate \(w_0\) is material, not an
optional choice of a generic parameter.

## 4. Exact positive criteria for the full invariant overring

Two classical alternatives concern the full algebra \(D\), rather
than demanding residual-coordinate descent of a possibly smaller
plane presentation.

Russell--Sathaye Theorem 2.3.1 yields \(D=R^{[1]}\) from a generic
polynomial line after inverting a set generated by prime elements,
finite generation, and their inertness conditions. In the specialization
with coefficient ring \(R\), those conditions include the generic
intersection, primality of the relevant divisor fibers, relative
algebraic closure of their coefficient fields, and the corresponding
residue-ring intersection. Their Remark 2.5.4 explains the role of
faithful flatness in the intersection conditions. Corollary 3.4 instead
assumes a relative inclusion of UFDs
\(R\subset D\subset R^{[n]}\) with relative transcendence degree
one.[^5] An absolute inclusion into \(\mathbb C^{[4]}\) is not this
relative inclusion.

Das--Dutta Theorem 3.13 assumes a Noetherian \(\mathbb Q\)-algebra
\(R\), an \(R\)-flat algebra \(D\), and an \(R\)-retraction
\(D\to R\) with finitely generated kernel. Polynomial-line fibers
at minimal primes and integral fibers at height-one primes imply an
\(\mathbb A^1\)-fibration. If \(R_{\mathrm{red}}\) is seminormal,
\(D\) is the symmetric algebra of a rank-one finite projective
\(R\)-module.[^6] Over a Noetherian UFD this module is free, so
the conclusion becomes \(D=R^{[1]}\). The retraction is an actual
additional premise; the slice retraction has the wrong base and target.

These criteria do not require retaining a particular normalized
generic parameter. This matters independently: the actual control146
with \(N=2a\partial_v\) has a curve equation that is a coordinate
on every coefficient-ring fiber, but no normalized polynomial slice
because \(N(A)=aA\).[^7]

## 5. Height-one tests and the remaining question

Even in a polynomial plane, height-one coordinate tests alone do not
amount to residual coordinates over a surface. For example, set
\[
R_0=\mathbb C[p,q],\qquad H=pU+qV+1.
\tag{6}
\]
At every height-one prime of \(R_0\), one of \(p,q\) is a unit,
so \(H\) is a coordinate over the corresponding local ring.
At \((p,q)\), it reduces to the constant one. Its zero fiber
there is empty, so this example does not satisfy faithful flatness
or the full fibration hypotheses. It is an elementary warning about
the quantifier in (3), not another claimed dense-frame realization.

The actual counterexample (4) rules out the proposed necessity of
divisorial residual-coordinate descent for the chosen cleared
first-tail equation. A viable next argument must instead control the
full overring \(S_s[y,z,w_0]\), its divisor fibers and residue constants,
or construct an appropriate relative retraction or polynomial
presentation. None of the selected source statements turns the
generic primitivity theorem145 alone into those hypotheses.
The counterexamples do not obstruct a different polynomial parameter
or prove that global descent is impossible.

## Sources

1. [Degree-controlled embedded lines139](dense-generic-embedded-line-pass139-working.md),
   Section 1, and [common Taylor integrality145](common-gauss-integrality-tail-primitivity-pass145-working.md),
   Sections 9--10. Generic-coordinate and remaining-scope inputs.
2. S. M. Bhatwadekar and A. K. Dutta,
   [*Kernel of locally nilpotent R-derivations of R[X,Y]*](https://repository.ias.ac.in/3203/1/311.pdf),
   *Transactions of the AMS* 349 (1997), 3303--3319,
   Section 4 standing hypotheses and Proposition 4.4, printed p.3314.
3. Janaki Raman Babu and Prosenjit Das,
   [*A criterion to determine residual coordinates of A2-fibrations*, v4](https://arxiv.org/pdf/2212.03488v4),
   14 February 2023, definitions and Theorem 1.1, Theorem A,
   Corollary B, and the quoted Theorem 2.6.
4. [An actual projected curve can split on an unremoved divisor146](divisorial-descent-audit-pass146-working.md),
   Sections 1--5. Full polynomial inverse, exact selected derivation,
   primitive first tail, and the distinction between the two rings.
5. Peter Russell and Avinash Sathaye,
   [*On Finding and Cancelling Variables in k[X,Y,Z]*](https://www.ms.uky.edu/~sohum/ma561/affgeom/vars_in_k3.pdf),
   *Journal of Algebra* 57 (1979), 151--166,
   Definition 2.1.2, Theorem 2.3.1, Remark 2.5.4, and Corollary 3.4.
6. Prosenjit Das and Amartya K. Dutta,
   [*On codimension-one A1-fibration with retraction*](https://arxiv.org/pdf/1302.5223),
   arXiv:1302.5223v1, Theorem 3.13 and Remark 3.14.
7. [A residual coordinate can descend while its normalized parameter has a pole146](actual-descent-controls-pass146-working.md),
   Sections 2--4. The normalized leading derivation need not have a
   polynomial slice even in the displayed actual polynomial family.

The displayed primary statements and their specified hypotheses were
checked directly. This comparison does not claim a recursive audit of
all cited proofs, exhaustive literature coverage, or a new recognition
theorem. The earlier full-gradient distinction91 is retained context,
not a newly discovered source criterion.

[^1]: Source 1.
[^2]: Source 2.
[^3]: Source 3.
[^4]: Source 4.
[^5]: Source 5.
[^6]: Source 6.
[^7]: Source 7.
