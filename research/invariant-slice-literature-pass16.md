# Invariant extensions: affine slices and the remaining lifting premise

The directly checked primary statements do not supply either of the two
general implications sought here:
\[
\begin{gathered}
E=AD+B\partial_t\text{ has a slice}
\ \Longrightarrow\ E\text{ has an affine-in-}t\text{ slice},\\
E\text{ has an affine-in-}t\text{ slice}
\ \Longrightarrow\ \ker E\cong\mathbb C^{[3]},
\end{gathered}
\]
for arbitrary \(D\in\operatorname{LND}(R)\), \(R=\mathbb C^{[3]}\),
and \(A,B\in C:=\ker D\). This is a bounded source-audit outcome,
not a claim of novelty or a designation of a named open problem.

The exact elementary affine-slice condition is useful and should remain
separate from these stronger implications.

## 1. The condition that an affine slice actually expresses

Assume \(D\ne0\) and \(A\ne0\), and write
\(I=D(R)\cap C\) for the plinth ideal. Then
\[
E\text{ has a slice of degree at most one in }t
\quad\Longleftrightarrow\quad BC+AI=C.
\tag{1}
\]
This equivalence is an elementary coefficient calculation, not a theorem
attributed to the sources below. If \(E(ut+v)=1\), the coefficient of
\(t\) gives \(Du=0\), and
\(ADv+Bu=1\). Applying \(D\) gives \(D^2v=0\), hence \(Dv\in I\).
Conversely, a representation \(1=Bu+ADv\) with \(u\in C\) and
\(Dv\in I\) provides the slice \(ut+v\).

For a principal plinth \(I=gC\), condition (1) is
\((B,Ag)=C\). It makes \(B\) a unit modulo \(gC\), but does not make
that residue a scalar. A slice with higher \(t\)-degree gives instead the
coupled equations
\[
ADv_n=0,\qquad ADv_j+(j+1)Bv_{j+1}=0\ (1\le j<n),
\qquad ADv_0+Bv_1=1.
\]
Their last equation does not establish \(Dv_0\in I\), since \(v_1\)
need not be invariant. No such step is silently assumed.

If \(A=0\), the slice condition is simply that \(B\) be a nonzero
constant. If \(B=0\), an \(E\)-slice gives an \(AD\)-slice in the
base by taking the constant coefficient in \(t\).

## 2. Freudenburg's general-extension result and its exact mismatch

Read directly: [Freudenburg, *Actions of SL2(k) on Affine k-Domains and
Fundamental Pairs*, Section 7](https://arxiv.org/pdf/2108.12021), arXiv v2,
June 2022, printed pages 23–26.

For a characteristic-zero domain \(R\), nonzero LND \(P\),
\(C=\ker P\), \(F_n=\ker P^{n+1}\), and \(I_n=P^nF_n\),
Proposition 7.1 treats \(P+B\partial_t\), \(0\ne B\in C\), assuming
\[
BC\cap I_n=BI_n\qquad\text{for every }n\ge0.
\tag{2}
\]
It identifies the kernel with \(C[\sum_{n\ge0}B^nF_n]\subset R\)
using the localized map \(\exp(-tP/B)\). Lemma 7.3 uses (2) to control
the degree modules. This is a kernel description, not an affine-slice
reduction or polynomial-kernel theorem. Principalness of \(I_1\) alone
is not the stated saturation hypothesis.

Theorem 7.6 further requires a fundamental pair \((P,U)\) and
\(B\in C_0\setminus\{0\}\) for its induced grading. Over an
algebraically closed field its quotient is surjective exactly when \(B\)
is constant. A slice therefore forces constant \(B\) under these
additional premises, not for arbitrary invariant extensions.

For comparison with (1), take \(P=AD\); its plinth is \(AI\).
This substitution does not manufacture a fundamental pair or establish (2).

## 3. An exact matrix theorem exists on an actual polynomial bundle

[Masuda, *Equivariant embeddings and semi-invariant locally nilpotent
derivations*, Lemma 2.3](https://sci-tech.ksc.kwansei.ac.jp/~kayo/cmn/papers/eembed.pdf),
was read in the original author-hosted PDF, pages 6–7, with its preceding
setup. Over characteristic zero, let \(S=Q[x_1,\ldots,x_n]\), with the
specified semi-invariant coordinates for an abelian reductive group. A
semi-invariant \(Q\)-LND \(\delta\) with a slice and all
\(\delta x_j\in Q\) has a polynomial kernel over \(Q\), with linear
semi-invariant generators, provided every equivariant vector bundle over
\(\operatorname{Spec}Q\) is trivial. Its proof completes the coefficient
row to an invertible matrix. For the trivial group this is the ordinary
polynomial-bundle statement.

This explains the matrix mechanism, but its presentation is essential.
For a local slice \(Db=g\), one only knows
\(R_g[t]=C_g[b,t]\), not \(R[t]=C[b,t]\). Even if (1) holds, applying
the polynomial-bundle argument to the subring \(C[b,t]\) does not prove
that its coordinate change preserves the larger ring \(R[t]\).
That is precisely the extra preservation verified by the pass15 scalar
congruence lift.

## 4. The principal-plinth fiber theorem is generic along the divisor

[Masuda, *Factorial affine Ga-varieties with principal plinth ideals*,
Theorem 3.9 and Lemma 3.2(2)](https://arxiv.org/html/2312.05455),
arXiv:2312.05455v1, December 9, 2023, were read with their setup and proofs.
Over an algebraically closed characteristic-zero field, suppose a factorial
affine domain has an irreducible LND, affine kernel, and principal plinth
\(\alpha^p\beta C\), with \(p>0\), \(\alpha\) prime and
\(\gcd(\alpha,\beta)=1\). Its general closed quotient fiber over
\(V(\alpha)\) is a disjoint union of at least two affine lines.

Irreducibility of the derivation and the word “general” both matter. An
arbitrary replica \(AD\) is not irreducible. More importantly, this theorem
does not describe every closed fiber at the isolated intersection points
of \(V(B)\) with a plinth component. Thus it does not itself prove the
unit-ideal condition \((B,Ag)=C\) from an extension slice. It is a
potential input to a fiber argument, not the missing argument.

## 5. Units modulo the plinth versus scalar congruence

The explicit pass15 matrix lift assumes \(B\equiv1\pmod{gC}\), after
constant scaling when appropriate. The weaker condition
\(\overline B\in(C/gC)^*\) only supplies an inverse residue
\(\overline M\), not \(\overline B=\overline M=1\).
Consequently the expressions
\[
\frac{B-1}{g}b-At,\qquad \frac{M-1}{g}b+At
\]
need not be polynomial. Completing a matrix on \(C_g[b,t]\) does not
repair that integrality issue by itself.

A basic ring-theoretic control is
\(C=\mathbb C[u,v]\), \(g=uv-1\), \(B=u\): the residue of \(B\)
is invertible and nonconstant on \(C/gC\cong\mathbb C[u,u^{-1}]\).
This illustrates the distinction only. No claim is made that these data
occur as a particular rank-three derivation's plinth and coefficient.

The bounded follow-up searched invariant extensions, affine-in-one-variable
slices, plinth unimodularity, relative matrix lifting, local-slice degree
modules, and congruence automorphisms. No primary theorem removing this
integrality premise, or proving general slice-to-affine-slice reduction,
was verified. Cohn's non-elementary row example remains only a limitation
of an elementary-word method, not a conjugacy obstruction; pass15 already
constructively bypasses it in its scalar congruence case.

## 6. A precise local-bundle criterion, and its premise gap

[Dufresne and Kraft, *Invariants and separating morphisms for algebraic
group actions*, Proposition 5.4](https://dmi.unibas.ch/fileadmin/user_upload/dmi/Personen/Kraft_Hanspeter/Separating_Morphisms.pdf)
identifies, for a factorial affine variety in characteristic zero, the
union of open trivial equivariant bundles with the complement of the
plinth variety. This is stronger than a statement restricted to principal
invariant opens. It does not state that one reduced affine-line orbit
fiber belongs to this union.

Example 8.5 is a useful control: the quotient of
\(\mathrm{SL}_2/N\) has a fiber whose support is a single free orbit,
yet it is inside the plinth variety and the morphism is not a principal
bundle. This fiber is nonreduced. Indeed, after the finite etale cover
\(\mathrm{SL}_2/T\to\mathrm{SL}_2/N\), the quotient parameter pulls
back to \(z^2\), and its fiber is doubled. Thus this example rejects a
set-theoretic single-orbit criterion, not the reduced-fiber criterion
needed here. Neither surface is the polynomial threefold under study.

## 7. A recent exact statement still takes the closure of bad fibers

Read directly: [Masuda, *Faithfully flat quotient morphisms by Ga-actions
on factorial affine varieties*, Proposition 2.5(3) and its following
remark](https://arxiv.org/html/2512.06687v1), arXiv v1, December 7, 2025.
The [journal record](https://www.sciencedirect.com/science/article/pii/S0021869325006805)
is *Journal of Algebra* 691 (2026), 577–596,
DOI 10.1016/j.jalgebra.2025.11.020.

For a smooth factorial affine variety with smooth affine quotient and
surjective equidimensional quotient map, its proof, after taking an
irreducible derivation, establishes
\[
\overline{\operatorname{Sing}(\pi)}
=V(\operatorname{pl}(D)),
\]
where \(\operatorname{Sing}(\pi)\) denotes fibers not isomorphic to
\(\mathbb A^1\), including their scheme structure. The following remark
gives the same closure equality for factorial affine source, irreducible
LND, affine kernel, and faithful flatness. These statements do not replace
the closure by the set itself. Nor does “pure codimension one” in this
formulation assert closedness.

Theorem 2.2 records that multiple fiber components lie in the fixed locus
and that reduced nonempty fibers are disjoint unions of affine lines.
It does not assert that every single reduced affine-line fiber has a
Zariski saturated trivial-bundle neighborhood. Accordingly, this recent
paper does not fill the pointwise premise left in Section 6.

## 8. Kaliman's exceptional curves give a whole-component obstruction

The [author manuscript of Kaliman, *Free C+-actions on C3 are
translations*](https://www.math.miami.edu/~kaliman/library/Ka.invent.2004.c%2B.pdf)
differs from [arXiv v1](https://arxiv.org/pdf/math/0207156).
The numbers below refer to the author manuscript, not the old arXiv draft.
For a smooth factorial affine threefold with \(H_2=H_3=0\),
Proposition 3.2 makes \(\theta:Z\to\Gamma\) finite. Theorem 5.2(i)
allows \(\Gamma\) to be chosen with nonbijective maps on every component;
each component of \(\Gamma\) normalizes to \(\mathbb A^1\).

With smooth quotient, the first paragraph of Proposition 4.2's proof
shows that a transversal at a free point maps biholomorphically to the
base. Its last paragraph uses an interior branch point of any
nonbijective component of \(\theta\), where the transversal would instead
have degree at least two.

Consequently each such \(\Gamma\)-component meets the image of the fixed
locus. This is a deduction from the printed argument: if there were a
free point over that branch point, the two transversal conclusions would
conflict. Hence a coefficient \(B\) vanishing on an entire component
prevents \(AD+B\partial_t\) from having a slice. This does not exclude
isolated intersections of \(V(B)\) with \(\Gamma\).

The curve here is the exceptional curve for the quotient morphism, not
automatically the plinth support of an arbitrary replica. A replica can
have extra fixed divisors while leaving the quotient morphism unchanged.
Identifying the two supports requires the primitive derivation and a
separate argument. No pointwise good-fiber equivalence is claimed in
this audit.

No result or status assertion from arXiv:2512.15590v2 is used, for the
source-quality reasons recorded in the preceding audit. No registry or
previous proof note was changed in this pass.
