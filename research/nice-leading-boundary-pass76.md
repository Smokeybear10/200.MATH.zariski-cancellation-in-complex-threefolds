# A leading-divisor restriction from the homogeneous image cone

A published theorem on homogeneous quasi-translations gives a concrete
restriction on the highest spatial-degree coefficients of an actual
nice sliced action on complex four-space. In the remaining Jacobian
square-nonzero case, their common zero set has one distinguished
hypersurface component and only linear components besides it.

In particular, if their gcd has only linear irreducible factors, the
original kernel is polynomial. This is an application of a prior
geometric theorem, not a new classification of nice actions. It does
not yet control the primitive fixed-locus ideal of the action derived
from a good partial.

## 1. Exact actual-frame assumptions

Let
\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad
E=P\cdot\partial,\qquad E(s)=1,\qquad E(P)=0,
\qquad A=\ker E.
\tag{1}
\]
Thus E is nice in this actual coordinate frame and has the original
polynomial slice. Write \(J=\operatorname{Jac}P\) and
\(K=\operatorname{Frac}B\).
The [sliced nice-rank theorem](nice-slice-adjoint-rank-pass74.md)
gives \(J^3=0\) and \(\operatorname{rank}_KJ\le2\).
If \(J^2=0\), the existing double-adjoint recognition already gives
\(A\simeq\mathbb C^{[3]}\). We therefore assume \(J^2\ne0\).

In that branch J has Jordan type (3,1). The same
[vertical-adjoint exclusion](vertical-top-exclusion-pass69.md)
used in pass74 shows that its image line \(\operatorname{im}J^2\)
is not \(KP\). Indeed a nonzero column parallel to P would give
a nonzero highest second adjoint parallel to E for an actual
coordinate partial. Since \(JP=0\) and
\(\operatorname{im}J\cap\ker J=\operatorname{im}J^2\), it follows that
\[
P\notin\operatorname{im}J,\qquad
\operatorname{rank}_K[J\mid P]=3.
\tag{2}
\]
This establishes the augmented rank; ordinary rank two of J alone
would not establish it.

## 2. Homogenization and the exact source hypotheses

Let \(d=\max_i\deg P_i\), and let \(P_{i,d}\) denote the homogeneous
part of degree d, possibly zero. Here \(d\ge1\). With a new
indeterminate z, set
\[
\mathcal H(x,z)=\bigl(z^dP(x/z),0\bigr),\qquad
\mathcal H_i(x,0)=P_{i,d}(x)\quad(i\le4).
\tag{3}
\]
This is a polynomial homogeneous map. Its velocity has zero z-entry,
and the chain rule gives
\(\operatorname{Jac}\mathcal H\cdot\mathcal H=0\).
It defines a homogeneous quasi-translation in five variables.
On z nonzero, with \(u=x/z\), its full Jacobian is
\[
z^{d-1}
\begin{pmatrix}
J(u)&dP(u)-J(u)u\\
0&0
\end{pmatrix},
\qquad
\operatorname{rank}\operatorname{Jac}\mathcal H=3.
\tag{4}
\]
The last column and (2) justify the rank equality.

The original slice gives
\(\sum_i(\partial_i s)P_i=1\). Thus the components of P have
no common zero and no nonconstant common factor. It follows that
\(\gcd(\mathcal H_1,\ldots,\mathcal H_5)=1\): a homogeneous common
factor other than z would dehomogenize to a nonconstant common
factor of the \(P_i\); z is not common because d was chosen to
be the actual maximum degree.
Furthermore
\[
V(\mathcal H)\subseteq\{z=0\},\qquad
V(\mathcal H)=V(P_{1,d},\ldots,P_{4,d})\times\{0\},
\qquad \dim V(\mathcal H)\le3.
\tag{5}
\]
The last bound uses that at least one \(P_{i,d}\) is nonzero.

Let \(\mathcal W\) be the closure of the image of \(\mathcal H\).
It is an irreducible cone of dimension three by (4).
Also \(\mathcal H(\mathcal H)=0\): this is the highest power of
the flow parameter in
\(\mathcal H(X+t\mathcal H(X))=\mathcal H(X)\).
Therefore \(\mathcal W\subseteq V(\mathcal H)\).
Consequently the dimension in (5) is exactly three and
\(\mathcal W\) is an irreducible component.

De Bondt's Corollary 6.4 applies: for a homogeneous complex
quasi-translation with component gcd one and zero-set dimension
at most three, every zero-set component other than its image
closure is a three-dimensional linear subspace.[^image]
All these hypotheses have now been verified for \(\mathcal H\),
without assuming that an invariant localization is polynomial.

For the selected source proof, the required specialization of
Lemma 6.1 can be made explicit. Its use through Lemma 6.2 is on
an irreducible component X of the inverse image of a linear subspace
under a homogeneous map, with \(\mathcal H|_X\ne0\). Thus X and the closure Y of its image are
cones. For \(c\in X\), choose \(c_n\to c\) in the dense open where
\(\mathcal H(c_n)\ne0\), and normalize these image vectors to unit
norm. They still lie in Y; a subsequence converges to a nonzero
\(p\in Y\). Every polynomial invariant is constant on the lines
through \(c_n\) in those directions, and coefficientwise continuity
gives the same line identity at c. This proves the needed instance.
The printed incidence set in Lemma 6.1 does not visibly impose
\(p\in Y\); retaining that condition makes the normalization argument
complete in this conical case. No conclusion from the broader
nonhomogeneous formulation of that lemma is needed here.

## 3. The leading radical and its distinguished factor

Every component in (5) lies in the actual hyperplane z=0.
Identify that hyperplane with the original vector space
\(\mathbb C^4\). There is an irreducible homogeneous polynomial
F in four variables such that
\(\mathcal W=V(F)\times\{0\}\), because \(\mathcal W\) is an
irreducible hypersurface in that hyperplane. Each other component
is \(V(\ell_i)\times\{0\}\) for a nonzero linear form \(\ell_i\).
Discard repetitions and omit any \(\ell_i\) associated to F.
The Nullstellensatz and unique factorization give the exact radical
identity
\[
\sqrt{(P_{1,d},P_{2,d},P_{3,d},P_{4,d})B}
=\bigl(F\ell_1\cdots\ell_r\bigr)B.
\tag{6}
\]
An empty product is allowed. In particular every leading component
is divisible by F; all other distinct irreducible factors of their
gcd are linear. No assertion about their multiplicities or the
unreduced leading ideal follows from (6).

The factor F also satisfies the actual velocity relation
\[
F(P_1,P_2,P_3,P_4)=0,
\tag{7}
\]
because \(\mathcal H(x,1)=(P(x),0)\) lies in \(\mathcal W\).
Thus F is not an arbitrary selected factor at infinity: it is the
equation of the homogeneous cone over the velocity image.
Its degree may be one. No assertion that it is an invariant
polynomial \(E(F)=0\) is made.

## 4. A sufficient leading-coefficient test

Let \(G=\gcd(P_{1,d},\ldots,P_{4,d})\), ignoring zero entries.
If G is constant or all its irreducible factors over \(\mathbb C\)
are linear, then
\[
\boxed{A\simeq\mathbb C^{[3]}.}
\tag{8}
\]
For \(J^2=0\) this was already recognized. In the remaining case,
F divides G by (6), so constant G is impossible and F must be
linear. Equation (7) then says that the nonzero linear coordinate
F(x) is killed by E. The retained original-slice/invariant-coordinate
recognition theorem, as applied in
[pass74, Section 3](nice-slice-adjoint-rank-pass74.md), gives (8).
It uses the actual E and original slice; no translation theorem
for the five-variable homogenization is invoked.

If the displayed E has no nonzero linear invariant, F must instead
be nonlinear. Equation (6) then says that exactly one distinct
nonlinear factor occurs in the leading gcd, while every other
factor is linear. This is a necessary leading-boundary condition,
not a nonrecognition certificate.

## 5. Application and access limits

The theorem applies without choosing a good partial T. It therefore
constrains the one-good-partial problem but does not prove that
the primitive ideal \(J(E,[T,E]):h\) is the unit ideal.
The zero set in (5) is a boundary at infinity of the homogenized
velocity, not an intrinsic quotient fiber. Neither its irreducible
components nor (6) may be identified with the fixed components
of that intrinsic action.

The earlier [pass39 source audit](literature-scope-pass39.md)
already treats the distinct rank-at-most-two homogeneous theorem
and the failure of extracting a second invariant from rank-three
homogenization. The input here is the separate zero-set component
theorem, with its hypotheses checked through (3)--(5).
No new reusable test, full regression, historical novelty, human
expert review, or formal proof verification is claimed.
All passes through 75 and shared metadata are unchanged.

[^image]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/html/1501.04845v3), arXiv:1501.04845v3, October 18, 2017; Corollary 6.4, printed pages 31--32. Its complete statement and proof, Theorem 6.3 with proof, Lemmas 6.1--6.2 and 3.1--3.2, and Propositions 2.5--2.6 were freshly read in the [retained primary text](../tmp/pdfs/bondt-1501.04845v3.txt), with Corollary 6.4 also checked in the primary HTML. No complete re-audit of the paper's other classification proofs is claimed. [Published article](https://doi.org/10.1007/s13366-017-0358-2).
