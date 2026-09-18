# The conic involution: exact source gates for recognition

The polynomial invariant ring does not supply a checked linearization
theorem. There is, however, a sufficient surface criterion specific to
the actual conic: if its fixed surface is an affine plane, the
Sathaye--Russell linear-plane theorem recognizes the threefold. This
note records that criterion and the precise scope of the closest
degree-two-cover results.

## 1. The actual cover and its fixed surface

Use the global conclusion of
[conic patching115, Sections 3--5](quadratic-global-conic-patching-pass115.md).
Write

\[
\begin{gathered}
S=\mathbb C[s,t],\quad 0\ne P\in S,\quad \eta\in S,\qquad
A=S[U,r]/(r^2-2PU+\eta),\\
B=A[u]\simeq\mathbb C^{[4]},\quad
C=S[U,u]\simeq\mathbb C^{[4]},\quad F=2PU-\eta,\\
B=C\oplus Cr,\quad r^2=F,\qquad
\sigma|_C=\operatorname{id},\quad\sigma(r)=-r,\quad B^\sigma=C,\\
D=\operatorname{Spec}(S[U]/(F)),\qquad
\operatorname{Fix}(\sigma)=\operatorname{Spec}(B/(r))=D\times\mathbb A^1_u.
\end{gathered}
\tag{1}
\]

The direct sum follows from the monic relation, so the quotient map is
finite free of degree two. Its fixed ideal is exactly (r), since 2 is
invertible. Its branch hypersurface in Spec C is F=0. It is smooth:
a singular point of F=0 would give a singular point of the hypersurface
r squared minus F at r=0, contrary to the smoothness of B. Thus D is a
nonempty smooth surface. Smoothness is not an affine-plane conclusion.

There is an elementary exact equivalence:

\[
F\text{ is a coordinate of }C
\quad\Longleftrightarrow\quad
\sigma\text{ is polynomially linearizable on }B.
\tag{2}
\]

For the forward direction choose C=\mathbb C[F,v2,v3,v4]. Substituting
F=r squared gives B=\mathbb C[r,v2,v3,v4] and the reflection form.
Conversely, a linearized involution has a three-dimensional fixed
space by (1), so exactly one eigenvalue is negative. In eigen-coordinates
w,v2,v3,v4 its fixed ideal is (w). Equality with the actual ideal (r)
gives r=alpha w for alpha in \mathbb C*, since the units of B are
constants. Consequently F=alpha squared w squared is a coordinate of
the invariant ring \mathbb C[w squared,v2,v3,v4]. In particular,
linearization would make r an actual coordinate of B; it is not an
assumption permitted in proving (2).

## 2. What the degree-two-cover theorem supplies

Zbigniew Jelonek's
[*On finite regular and holomorphic mappings*](https://arxiv.org/pdf/1404.7466v4)
has the following distinct conclusions. The numbering is that of
arXiv:1404.7466v4, whose submission record is dated 8 March 2015;
the paper was published in
[Advances in Mathematics 306 (2017), 1377--1391](https://doi.org/10.1016/j.aim.2016.11.006).

| Result | Hypothesis beyond the indicated category | Conclusion |
| --- | --- | --- |
| Corollaries 1.7--1.8 | Finite degree-two map, smooth source and smooth or normal target as stated | A global order-two deck automorphism and the quotient presentation |
| Corollary 1.5 | Proper polynomial self-map of \(\mathbb A^n\), branch locus already a coordinate hyperplane | Standard power map, up to polynomial source equivalence |
| Theorem 1.15 | Proper degree-two holomorphic map of smooth germs | Standard square map up to local biholomorphisms |
| Theorem 1.16 | Proper degree-two polynomial self-map and the involution Linearization Conjecture | Standard square map up to polynomial source and target automorphisms |

Thus the global unconditional statement about an arbitrary double
cover gives the deck involution, which (1) already has. The local
holomorphic result is not a polynomial global conjugator. Corollary
1.5 becomes usable here if the branch is a coordinate hyperplane;
that condition is the recognition gate in (2), not a consequence of
smoothness of the branch.

## 3. Scope of the linearization question

[Kraft--Zaidenberg, *Automorphism groups of affine varieties and their
Lie algebras*, Section 9.7, Question 9.32](https://arxiv.org/pdf/2403.12489v2)
lists the existence of nonlinearizable prime-cyclic actions on affine
spaces of dimension at least three as an open question. The same
section distinguishes local linearization, positive results with
additional hypotheses, and nonabelian finite-group counterexamples.
Those counterexamples are not involution counterexamples.

This survey does not by itself establish that the narrower condition
B^sigma polynomial is open. The bounded source verdict is only that
the checked theorems do not turn (1) into (2). Applying a theorem for
linear group actions to sigma before constructing a polynomial
linearizing coordinate system would assume the missing step. The
retained [Reynolds gate87](involution-reynolds-source-gate-pass87.md)
also keeps its spatial degree-band and tame hypotheses separate from
the time-degree bounds in the original frame.

## 4. The affine-plane fixed-surface criterion is sufficient

The precise positive theorem needed here is the coordinate conclusion of
[Russell, *Simple birational extensions of two dimensional affine
rational domains*, Theorem 2.3, printed pages 203--204](https://www.numdam.org/item/CM_1976__33_2_197_0.pdf).
The characteristic-zero predecessor is Sathaye's *On linear planes*,
Proc. Amer. Math. Soc. 56 (1976), 1--7. A current research restatement is
[Ghosh--Gupta--Pal, *On the family of affine threefolds
a(x)y=F(x,z,t)*, Introduction, the two paragraphs following Question 3](https://arxiv.org/html/2403.17397v2#S1).
For k a characteristic-zero field, B0=k^[2], and
H=aY+b in B0[Y] with a nonzero, it states

\[
B_0[Y]/(H)\simeq k^{[2]}
\quad\Longrightarrow\quad
B_0[Y]=k[H]^{[2]}.
\tag{3}
\]

One can also choose coordinates X,Z of B0 with a in k[X] and
B0[Y]=k[X,H]^[1]. The original argument first applies Theorem 1.3
to the simple birational extension defined by H. Proposition 1.1
then makes the coefficient of Z in H a unit modulo a, with its
higher Z-coefficients nilpotent modulo a. Proposition 2.2 constructs
the complementary coordinate over k[X]. This proves the coordinate
conclusion without requiring that this unit coefficient be congruent
to one scalar modulo the nilradical. That additional normalization
appearing in the printed Theorem 2.3 argument is not used here.

Apply (3) with B0=S, Y=U, a=2P and b=-eta. If D is an affine plane,
choose S[U]=\mathbb C[F,X,Y]. The original conic then becomes

\[
D\simeq\mathbb A^2
\ \Longrightarrow
A\simeq\mathbb C[F,X,Y,r]/(r^2-F)
 =\mathbb C[r,X,Y].
\tag{4}
\]

This is an actual coordinate conclusion before adjoining u. It uses
the linearity of F in U, not a general assertion about embeddings of
affine planes or smooth hypersurfaces. In particular, D being an
affine plane must not be dismissed as insufficient in this special
conic. Conversely, neither (1) nor the cited local double-cover
theorem proves that D is a plane. No supplied-frame recognition or
arbitrary-frame entry theorem is claimed here.

## Source and verification scope

The selected Jelonek statements and complete displayed proofs of
Theorem 1.3, Corollaries 1.5--1.8, and Theorems 1.15--1.16 were read.
Their earlier topological and analytic references were not separately
reproved. The elementary reflection step used in (2) is diagonalization
of an order-two linear operator in characteristic zero.

The selected Kraft--Zaidenberg section and Question 9.32 were read.
The complete two-paragraph linear-plane restatement and its cited
bibliographic entries were independently read in the Ghosh--Gupta--Pal
v2 HTML, dated 3 August 2024. The original Russell Theorem 2.3 and its
complete displayed proof, Proposition 2.2, Proposition 1.1, Corollary
1.2, and the common argument and Case 1 of Theorem 1.3 were then read
visually on printed pages 198--200 and 203--204. This includes the
formulas omitted by text extraction. The earlier field-generator
results cited in Theorem 1.3, its separate Case 3, and Sathaye's original
proof were not newly reconstructed. The direct substitution in (4)
is proved above. No numerical check can establish the missing plane
or linearization premise, and no checker was added or executed.
