# Sharp purity restrictions on the proper second-image ideal

In the remaining rank-two residue branch, purity of the degree-four
piece with basis 1,G,G² gives a genuine restriction on the conic
coefficients, even though the full degree-two module is not pure.
In particular B1 cannot belong to the square of the proper residual
second-image ideal. If a has first base order one, B1 is a smooth
parameter and the first nonzero plinth jet is its square. A further
contact bound retains the multiplicity of the residual point ideal.

These are necessary conditions, not an exclusion of this proper-ideal
case. No statement identifies a completed model with an actual frame.

## 1. The actual proper-ideal hypotheses

Work at R=S_m with maximal ideal n in the actual collapsed mixed
(2,1), L(m) nonzero sector. The faithfully flat domain A_R has
full invariant ring R for the primitive LND N. Its whole fiber is
D[c], where D=C[G]/(G²(G−1)). The retained degree modules
Fj=ker N^(j+1) are free of rank j+1. Pass107 leaves the residue
spaces W2=C1+CG and W1=C.[^retained]

Choose F2=R+RG+RH with H having zero whole-fiber residue. Shift
a first-degree generator by its invariant constant so that it has
zero residue. In the proper residual-ideal case the exact conic data
are
\[
\begin{gathered}
F_1=R\oplus Rr,\quad r=aG+bH,\quad Nr=P\ne0,\quad
J=(a,b)\subset\mathfrak n,\quad \gcd(a,b)=1,\quad
\sqrt J=\mathfrak n,\\
NG=\epsilon br+B_1,\qquad NH=-\epsilon ar+B_2,
\qquad P=aB_1+bB_2,\qquad \epsilon\in R^*,\\
Q=\epsilon r^2-2B_2G+2B_1H\in R,\qquad
H\in\mathfrak nA_R,\quad B_1\in\mathfrak n,
\quad B_2,Q\in\mathfrak n^2.
\end{gathered}
\tag{1}
\]
Both a and b are nonzero. Their coprimality comes from the
torsion-free quotient F2/F1. The coefficient epsilon is a unit
by the height-one degree-module valuations107: I2=epsilon P(a,b)
has the same divisor valuations as I1=PR, and (a,b) is primitive.
This normalization does not use full rank of W2.[^divisor]

For completeness, the residue action of N kills W2, so the formulas
first give B1,B2 in n. Also r belongs to nA_R. The conic makes
Q+2B2G=epsilon r²+2B1H belong to n²A_R. The independent
residues of 1,G make R+RG pure in A_R, giving Q,B2 in n².
No contraction through the non-pure module F2 is used here.

## 2. A different pure piece gives the sharp ideal

The elements 1,G,G² belong to F4 and have independent whole-fiber
residues: the minimal polynomial of the actual Artin generator G
has degree three. The residue-basis purity lemma therefore applies
to their R-span inside the flat algebra A_R. Rearrange the conic
with all its signs retained:
\[
\begin{gathered}
Q+2B_2G-\epsilon a^2G^2
=2B_1H+2\epsilon abGH+\epsilon b^2H^2,\\
\mathfrak K=\mathfrak n(B_1)+\mathfrak n(ab)
                  +\mathfrak n^2(b^2),\\
\boxed{\qquad Q,\ B_2,\ a^2\in\mathfrak K.\qquad}
\end{gathered}
\tag{2}
\]
The three terms on the right belong respectively to n(B1)A_R,
n(ab)A_R, and n²(b²)A_R, because H belongs to nA_R. The
left side lies in the pure free piece with basis 1,G,G². Its
coefficients therefore belong to K. The units 2 and epsilon
permit the displayed extraction.[^purity]

This is sharper than replacing all coefficients by maximal-ideal
powers. In particular it remembers the extra normal order of H².
It is not an assertion that F2 intersect KA_R equals KF2.

## 3. A nonzero coefficient outside the ideal square

If a prime factor divided both B1 and b, (2) would make it divide
a² and hence a, contrary to gcd(a,b)=1. Since b is a nonunit,
this also rules out B1=0. Thus (B1,b) is itself a maximal-primary
complete intersection.

If B1 belonged to J², then (2) would force a² into nJ².
Write the putative membership as a²=u a²+v ab+w b², with
u,v,w in n. The element 1−u is a unit, so b would divide a²,
again contradicting coprimality. Consequently
\[
\boxed{\qquad B_1\ne0,\qquad \gcd(B_1,b)=1,
\qquad B_1\notin J^2.\qquad}
\tag{3}
\]
This explains precisely why the full-Artin quartic construction107
cannot simply be repeated: its coherent J² expression for B1 is
impossible in this remaining proper-ideal branch.

There is also an exact quotient-ideal interpretation. Let C=R/(B1)
and use a bar for its images. The a² membership in (2) gives
\[
\bar a^2-\bar b\bar u\bar a-\bar b^2\bar v=0,
\qquad u\in\mathfrak n,\quad v\in\mathfrak n^2,
\qquad
\bar a\in\overline{\bar b\,\bar{\mathfrak n}}.
\tag{4}
\]
The final bar over the ideal denotes its integral closure: the
monic relation has its first coefficient in b n and its second
coefficient in (b n)². This is a statement about an ideal of C,
which need not be normal or reduced. It does not assert membership
in b n itself in that general quotient.

## 4. Leading orders and the smooth-parameter consequence

Put alpha=ord_n(a), beta=ord_n(b), and gamma=ord_n(B1), all
finite positive integers. In the regular local surface the associated
graded ring is a polynomial domain, so the order of a² is 2alpha.
If alpha is at most beta, both n(ab) and n²(b²) have order
strictly greater than 2alpha. Equation (2) therefore forces
\[
\boxed{\quad \alpha\le\beta\ \Longrightarrow
\gamma\le2\alpha-1.\quad}
\tag{5}
\]
The qualification alpha at most beta is essential; no bound with
that conclusion is asserted without it.

In particular alpha=1 gives gamma=1. Then B1 is a regular
parameter and C=R/(B1) is a DVR. By (3), b is nonzero in C.
Divide (4) by b² in Frac(C). Normality of this DVR puts a/b
in C, and reduction of its monic equation modulo the maximal ideal
puts it in nC. Lifting back to R gives a=B1 u+bv with v in n.
Since a has order one and bv has order at least two, u is a unit.
Consequently, under this alpha=1 hypothesis,
\[
\begin{gathered}
a=B_1u+bv,\quad u\in R^*,\quad v\in\mathfrak n,
\qquad J=(B_1,b),\\
B_2,Q\in\mathfrak n(B_1)+\mathfrak n^2(b^2),\\
\operatorname{ord}_{\mathfrak n}P=2,\qquad
\operatorname{in}_{\mathfrak n}(P)
=u(m)\operatorname{in}_{\mathfrak n}(B_1)^2,\\
P\bmod B_1\in\bar b^3\bar{\mathfrak n}^{2}.
\end{gathered}
\tag{6}
\]
For the second line, substitute a=B1u+bv in n(ab) in (2).
For the third, aB1 has the indicated quadratic initial form,
whereas bB2 has order at least three. For the last, use
P=aB1+bB2 and the second line modulo B1.

This last membership is a higher contact restriction. If
k=length_R(R/J), then in the DVR C the element b has order k.
If P mod B1 is nonzero, length_R(R/(P,B1)) is at least 3k+2,
in particular at least five. If B1 divides P, the membership still
holds, but that intersection length is not finite. The argument
does not rule out either alternative or identify the normalized
exceptional curve from this transverse equation.

## 5. Scope and provenance

These restrictions use the actual whole fiber and the exact conic,
but only the independent degree-four piece R+RG+RG² is used for
purity. No equality of the two nonzero component translation speeds
is assumed. There is no spatial polynomial-degree bound, no formal
normalization substituted for A_R, and no iteration that upgrades
a finite-order membership to a vanishing assertion.

The sharp ideal and its consequences are new deductions within
this remaining branch. They neither make its J² coefficients
available for the excluded full-Artin argument nor settle the
proper residual-ideal case. The separate
[unit-ideal exclusion108](mixed-unit-second-image-exclusion-pass108.md)
now excludes J=R by an exact monic-basis coefficient intersection.
That proof was independently read through EOF; it is not used in
the conditional proper-ideal deductions above. Files through107
are unchanged.

The retained degree-image104, nonprincipal-image106 and purity107
proofs were freshly read through EOF for this deduction. The
Lazard source statements and displayed proofs supporting purity
were read in107, not reread as a new source audit here. No numerical
method or actual-frame counterexample accompanies this argument.
Independent AI reconstruction is not human expert or formal proof
certification.

[^retained]: [Mixed degree-two image104](mixed-degree-module-artin-image-pass104.md); [mixed third-degree image105](mixed-third-degree-image-pass105.md), including W1=C; and [full-Artin exclusion107](mixed-full-artin-quartic-exclusion-pass107.md). The exact whole-fiber action is retained in [actions100](quadratic-whole-fiber-actions-pass100.md).

[^divisor]: [Quadratic divisor filtration107](quadratic-constant-divisor-filtration-pass107.md) and [independent divisor gates107](quadratic-divisor-normal-form-gates-pass107.md), together with the degree-one DVR slice in [rank defect105](mixed-cubic-rank-defect-pass105.md). Only the primitive second-image normalization from [normalized image ideals107](mixed-normalized-image-ideals-pass107.md), Section 2, is used; its full-Artin residue-matrix argument for properness is replaced here by the explicitly assumed proper case.

[^purity]: [Residue-basis purity107](residue-basis-purity-pass107.md), whose local flat-module theorem applies to any finite list with independent closed residues. Its primary inputs are the Stacks Project's [Lazard theorem, 058G](https://stacks.math.columbia.edu/tag/058G) and [factorization proof, 058C](https://stacks.math.columbia.edu/tag/058C).
