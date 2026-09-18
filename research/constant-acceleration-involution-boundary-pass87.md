# Constant acceleration gives an actual affine-three-space involution

A nonzero constant acceleration makes the centered return involution
global on every original coordinate fiber. Its invariant ring is exactly
the original kernel. Linearizing even one of these fiber involutions
would therefore recognize that kernel. The available primary literature
supplies this implication under a tamizability hypothesis, but does not
supply unconditional linearization for the involutions considered here.

## 1. Exact global reduction, with only one quadratic coordinate

Let E be a locally nilpotent derivation of the actual polynomial ring
B over C with a supplied global slice s. Assume only that one original
polynomial coordinate z has nonzero constant acceleration:
\[
B=A[s]=\mathbb C^{[4]},\qquad A=\ker E,\qquad E(s)=1,
\qquad q=E^2z\in\mathbb C^*.
\tag{1}
\]
There is no E-degree bound on the other three original coordinates.
This is the broader one-coordinate setting of the
[critical-value proof](coordinate-critical-value-constraints-pass86.md),
not an assertion about a proper good-speed ideal. In the earlier
normalization q=gh, both factors are units, hence complex constants,
because A is a subring of B and B has only constant units.

Put b=Ez. Since E(b)=q and E(q)=0, the following are actual global
polynomials, not localized functions:
\[
u=\frac bq,\qquad E(u)=1,\qquad
r=z-\frac{b^2}{2q}\in A,\qquad
B=A[u],\qquad z=r+\frac q2u^2.
\tag{2}
\]
Indeed u-s lies in A, so the change from s to u is an A-translation.
The involution iota of B which fixes A and sends u to -u fixes z.
For every complex lambda it therefore induces an involution iota_lambda
on the actual coordinate fiber. Its full ring description is
\[
C_\lambda:=B/(z-\lambda)
 =A[u]/\bigl(u^2-2(\lambda-r)/q\bigr)
 =A\oplus Au\simeq\mathbb C^{[3]},\qquad
C_\lambda^{\iota_\lambda}=A.
\tag{3}
\]
The direct sum is an A-module decomposition, obtained by division by
the monic quadratic. It proves the injection of A and the fixed-ring
identity without cancellation or an assumed presentation of A as a
polynomial ring. The involution is nontrivial because its anti-invariant
free summand Au is nonzero. Each quotient map Spec C_lambda to Spec A
is finite free of degree two.

## 2. The fixed scheme is a nonempty smooth surface

The ring A is a smooth affine three-dimensional domain: it is B/(u),
and the derivation E sends u to one, so du is unimodular on B. Let
T_z be the original coordinate partial. Evaluate its restriction to A
at u=0 and call the resulting complex derivation of A D. Evaluating
T_z(z)=1 in (2) gives
\[
D(r)=1,\qquad
\operatorname{Fix}(\iota_\lambda)
 =\operatorname{Spec}\bigl(C_\lambda/(u)\bigr)
 =\operatorname{Spec}\bigl(A/(r-\lambda)\bigr).
\tag{4}
\]
Thus dr is unimodular, and every displayed fixed scheme is smooth.
It is nonempty and of pure dimension two. To see this without a
topological fixed-point theorem, note that A has only constant units
and D(r)=1 makes r nonconstant. Hence r-lambda is nonzero and not a
unit for every lambda. It cuts a nonempty smooth hypersurface in the
smooth threefold Spec A. No claim that these surfaces are affine
planes, or that D is locally nilpotent, follows from this argument.

## 3. A conditional recognition theorem

Suppose that for at least one lambda the actual polynomial involution
iota_lambda on C_lambda is algebraically linearizable. Over C a linear
involution diagonalizes with eigenvalues plus or minus one. Its fixed
scheme has dimension two by (4), so there are exactly two plus
eigenvalues and one minus eigenvalue. In suitable actual coordinates,
\[
\iota_\lambda(X_1,X_2,X_3)=(X_1,X_2,-X_3),\qquad
A\simeq\mathbb C[X_1,X_2,X_3^2]\simeq\mathbb C^{[3]}.
\tag{5}
\]
This is a direct invariant-ring calculation for a reflection, not an
application of a general smooth-quotient recognition theorem. Root
also observed an alternative elementary check: a linear involution
with k negative eigenvalues has invariant-ring embedding dimension
(3-k)+k(k+1)/2 at the origin. Smoothness of A excludes k=2,3;
nontriviality excludes k=0.

There is a precise available sufficient hypothesis. Say that an
automorphism of C^3 is tamizable if it is conjugate by a polynomial
automorphism, which may itself be wild, into the tame subgroup.
Lamy and Przytycki prove that finite subgroups of the tame group of
affine three-space over a characteristic-zero field are linearizable.
Consequently their theorem and (5) give
\[
\text{one fiber involution is tamizable}
\quad\Longrightarrow\quad A\simeq\mathbb C^{[3]}.
\tag{6}
\]
The primary statement is Corollary B in
[Lamy--Przytycki, *Almost a building for the tame automorphism group*](https://www.math.univ-toulouse.fr/~slamy/stock/translation_immeuble.pdf),
the author-hosted English translation dated 29 October 2022 of their
2021 Annales Henri Lebesgue paper, volume 4, pages 605--651. The
translation states the corollary on page 2 and proves it on page 30.
Its proof uses a fixed point for the finite group on a complete CAT(0)
space, a stabilizer decomposition, and averaging within its triangular
factor. The statement and complete short corollary proof were directly
read here, not the full metric construction or all cited dependencies.

Neither the global A-reflection on B nor the A-module expression in
(3) proves tamizability in an actual three-variable coordinate system.
In particular u is a slice for E on B, but is not thereby an ambient
polynomial coordinate. The global action u to t u of C* on B does not
preserve a fixed z-fiber for arbitrary t: it sends z to r+t^2(z-r).
Thus a theorem about C*-actions on affine three-space cannot be
applied to this four-dimensional dilation and its order-two fiber
subgroup without a new argument.

## 4. What the primary sources do and do not settle

The September 2024 version of
[Kraft--Zaidenberg, *Automorphism groups of affine varieties and their Lie algebras*](https://arxiv.org/pdf/2403.12489)
still lists nonlinearizability of cyclic prime-order actions on affine
n-space, n at least three, as an open question: Section 9.7,
Question 9.32, page 23. This includes order two. Its Corollary 9.30
on page 22 treats non-finite reductive groups and so does not apply
to an involution. The same section discusses local linearization,
which must not be substituted for global polynomial conjugacy.
Those precise passages were directly read, not the entire survey.

The more specific fixed-surface issue is not an invented obstacle.
[Kraft, *Challenging problems on affine n-space*](https://www.numdam.org/item/SB_1994-1995__37__295_0.pdf),
Bourbaki expose 802, Astérisque 237 (1996), page 309, explicitly
asks whether an involution of affine three-space with a two-dimensional
fixed set is conjugate to a plane reflection. That paragraph was
directly read. It is a historical question, not by itself a claim about
the literature in September 2026.

The bounded primary-source search for this note, performed on
14 September 2026, located no later resolution of the general
involution question and no theorem establishing linearization solely
from a smooth quotient in this three-dimensional setting. This is
a qualified search outcome, not an exhaustive proof of current open
status. In particular, openness of the broader cyclic-group question
does not logically establish openness of the narrower family (3).
The exact conclusion of the present work is
\[
\begin{gathered}
q\in\mathbb C^*\ \Longrightarrow
\text{actual degree-two covers (3), smooth fixed surfaces (4)},\\
\text{linearizability or tamizability of one such fiber}
\ \Longrightarrow\ A\simeq\mathbb C^{[3]}.
\end{gathered}
\tag{7}
\]
No unconditional recognition follows in this note. Nor is every
involution with smooth quotient asserted to arise from (1): the
actual common cylinder and all-coordinate-fiber hypotheses are kept.

## 5. Deduplication and verification scope

The retained
[quadratic-cover literature note, Section 6](quadratic-slice-literature.md)
already separates a global monic involution from a return map with a
pole. The earlier
[monic quartic branch](quartic-quadratic-variable-pass.md)
studies a polynomial three-variable coefficient base and its branch
surfaces. Here the coefficient base is the original unknown A, while
the covering coordinate fibers themselves are actual affine
three-spaces. Identifying their invariant ring with A is the specific
reduction under examination. Topological fixed-set information alone
does not replace (5).

Root proposed the constant-acceleration specialization and the
linear-representation smoothness check. Jet reconstructed the actual
fixed-ring and fixed-scheme identities and checked the primary-source
gates. This note adds no checker, numerical method, source-wide proof
audit, or full regression. It makes no novelty claim and changes no
file through pass86. Canonical packet integration, if any, is separate
Root work.
