# Global commuting repairs and sharper two-quadratic reductions

The complex threefold cancellation question remains
\[
A[s]\simeq\mathbb C^{[4]}\quad\Longrightarrow\quad
A\simeq\mathbb C^{[3]}.
\tag{1}
\]
No proof or counterexample to (1) is supplied. The new results concern
specified coordinate configurations of a sliced polynomial action.
They construct a globally valid commuting repair, recognize two
rank-three alternatives, and exclude a rank-one projection in the
degree-two independent-defect residual.

The universal coordinate problem is kept separate. There is an exact
finite algebraic test for all coordinate changes of a prescribed
forward and inverse degree. Exhausting those tests is a positive
semidecision, not a proof that one of them succeeds. Neither exact
examples nor the number of verification methods resolves this gap.

## 1. Original ring, supplied frame and current coverage

Write \(B=\mathbb C[x_1,x_2,x_3,x_4]\), and let \(E\) be a nonzero
locally nilpotent derivation with a polynomial slice \(s\), meaning
\(Es=1\). Local nilpotence means that every individual polynomial is
killed by some finite iterate of \(E\). The slice theorem gives
\(B=(\ker E)[s]\); the original kernel is regular.[^1]

The supplied two-quadratic configuration is
\[
\operatorname{ad}_E^2\partial_{x_i}=0\ (i=1,2),\qquad
\operatorname{ad}_E^3\partial_{x_i}=0\ (i=3,4).
\tag{2}
\]
Here \(\operatorname{ad}_E T=[E,T]\). These are statements about
actual coordinate partials, not a rationally chosen basis of fields.
Put \(W_i=[E,\partial_{x_i}]\) and \(V_i=[E,W_i]\) for \(i=3,4\).

Previous complete results cover every supplied profile through the
shifted-height threshold \(H\le9\), as well as the supplied profiles
\((1,1,1,3)\) and \((0,2,2,2)\). The full profile (2) is not yet
recognized. The height statistic is not ordinary polynomial degree
and is not simply the sum of the adjoint heights.

A fixed actual ambient coordinate in \(\ker E\) would suffice:
the regular-kernel theorem then gives a polynomial kernel over that
coordinate.[^2] The arguments below never infer that coordinate just
from a nonconstant invariant, and never transfer the original slice
to an auxiliary action.

## 2. A global normalizer in the higher-degree power-law branch

Assume the two defects \(V_3,V_4\) are independent and the previous
full-companion reduction has produced
\[
E^m x=cg^m,\qquad L_0E^{m-1}x=\lambda g^{m-1},
\quad 3\le m\le5,\quad Eg=0,
\tag{3}
\]
with nonconstant \(g\), a nonzero constant good-direction vector \(c\),
and a nonzero constant bad-direction vector \(\lambda\). The selector
\(L_0\) retains the last two components. This is the nonzero lower-top
branch, not an assumption on every instance of (2).

Let \(T_c,T_\lambda\) be the associated constant partial directions,
and suppose \(T_cg=0\). Set
\[
a=(m-1)/2,\quad W=[E,T_\lambda],\quad V=[E,W].
\]
The inherited exact identities give
\[
g[E,T_c]=-aV,\qquad Wg=Vg=0,\qquad [E,V]=0.
\tag{4}
\]
In particular \(V\ne0\) is a polynomial LND.

The new field
\[
Y=gT_c+2aW
\tag{5}
\]
is a global polynomial LND. To prove the property, introduce an external
invariant parameter \(u\). The field \(P_u=gT_c+2auT_\lambda\) is
triangular in actual linear coordinates because \(T_cg=0\). Conjugating
on \(B[u,u^{-1}]\) by the actual automorphism \(\exp(E/u)\) gives
\[
\exp(\operatorname{ad}_{E/u})P_u
=gT_c+u^{-1}g[E,T_c]+2auT_\lambda+2aW+au^{-1}V
=Y+2auT_\lambda.
\tag{6}
\]
The pole cancels before specialization. This LND preserves \(B[u]\),
so its restriction is an LND; quotienting by the invariant ideal
\((u)\) proves (5). No ordinary partial is assumed to remain an LND
after arbitrary localization.

The mixed conjugated-column identity also yields
\[
[E,Y]=aV,\qquad [E,V]=[Y,V]=0,\qquad Yg=0.
\tag{7}
\]
Thus \(Y\) is a normalizer, not a field commuting with \(E\).

The complete proof is in
[the global repair note](research/quadratic-heisenberg-repair-pass43.md).
Its elementary finite models test (6)--(7), but are not asserted to
realize every hypothesis of the high-degree configuration (3).

## 3. Local nilpotence survives a compatible Heisenberg projection

Two general algebraic lemmas justify the next repair. All rings in
these lemmas are domains containing \(\mathbb Q\).

First, if \(0\ne C\) is an LND, \(D\) commutes with \(C\), and
\(D|_{\ker C}\) is locally nilpotent, then \(D\) is locally nilpotent.
Choose a local slice \(r_0\) with \(c_0=Cr_0\in\ker C\setminus\{0\}\).
For the largest \(N\) with \(D^Nc_0\ne0\), put \(c=D^Nc_0\) and
\(r=D^Nr_0\). Then \(Dc=0\), \(Cr=c\), and
\[
A_c=(\ker C)_c[r],\qquad Dr\in\ker C.
\tag{8}
\]
The extension is triangular over a base on which \(D\) is locally
nilpotent. Restriction proves the assertion. The local-slice equality
is the only standard input in this argument.[^1]

Second, suppose \(\delta,L,C\) are LNDs with
\([\delta,L]=C\), \([\delta,C]=[L,C]=0\), and an actual slice
\(\delta\sigma=1\) satisfying \(C\sigma=0\). Then
\[
b=L\sigma\in\ker\delta\cap\ker C,\qquad
D_0=L-\sigma C-b\delta
\tag{9}
\]
is an LND commuting with \(\delta,C\) and killing \(\sigma\).
On their common kernel the restriction of \(D_0\) is exactly that
of \(L\). Apply the first lemma on \(\ker\delta\), then extend by
the variable \(\sigma\). When \(C=0\) the conclusion is direct.

This proves local nilpotence, not only polynomial descent. Arbitrary
slice projections of arbitrary derivations do not satisfy the lemma.
The negative correction examples from the preceding report remain
valid because their corrected starting field is not an LND.

For (3), choose \(j\) with \(c_j\ne0\), and put
\[
\tau=(E^{m-1}x)_j/c_j,\qquad
\delta=E/g,\quad \sigma=\tau/g^{m-1},\quad
L=Y/g,\quad C=aV/g^2.
\tag{10}
\]
The actual next-to-top identities give \(E\tau=g^m\) and \(V\tau=0\).
All three localized fields are LNDs since they kill \(g\), so (9)
applies. The denominator-clearing replica is explicit:
\[
\mathcal R=g^{m+1}D_0
=g^mY-a\tau V-(Y\tau)E.
\tag{11}
\]
It is polynomial on the original \(B\), and it is an LND because
\(D_0g=0\). Directly,
\[
[E,\mathcal R]=[V,\mathcal R]=0,\qquad
\mathcal Rg=\mathcal R\tau=0.
\tag{12}
\]
This is a new global commuting construction under \(T_cg=0\);
it is not a claim that the earlier proposed normalized field itself
is locally nilpotent.

## 4. A coordinate criterion for commuting rank-three actions

Let \(D_1,D_2,D_3\) be independent commuting polynomial LNDs on
the actual complex four-ring. Suppose a nonconstant common invariant
\(g\) satisfies \(Tg=0\) for a nonzero constant coordinate direction
\(T\). Then their common kernel is generated by an ambient coordinate.

Indeed the established common-kernel theorem supplies
\(\bigcap\ker D_i=\mathbb C[p]\) with every \(p-\alpha\) irreducible.[^3]
Writing \(g=H(p)\) shows \(Tp=0\). Choose linear coordinates
\(B=R[b]\), \(R=\mathbb C[z_1,z_2,z_3]\), with \(T=\partial_b\),
so \(p\in R\).

A nonzero coefficient minor of the three fields is divisible by only
finitely many of the pairwise nonassociate primes \(p-\alpha\).
On every other fiber the three induced commuting LNDs remain
independent. The full-dimensional commuting-action theorem gives
\[
B/(p-\alpha)\simeq\mathbb C^{[3]}.
\tag{13}
\]
Consequently \((R/(p-\alpha))[b]\simeq\mathbb C^{[3]}\).
Known complex surface cancellation makes these \(R\)-fibers polynomial
planes. The three-variable general-plane-fiber theorem makes \(p\)
a coordinate of \(R\), and hence of \(B\).[^3] This uses the established
dimension-two cancellation theorem, not (1).

If \(D_1\) is sliced, its original kernel is polynomial by the
fixed-coordinate regular-kernel theorem.[^2] The
[full criterion](research/commuting-coordinate-descent-pass43.md)
records every source hypothesis.

In (3), this closes the \(T_cg=0\) branch whenever either
\[
\operatorname{rank}(E,V_3,V_4)=3
\quad\text{or}\quad
\operatorname{rank}(E,Y,V)=3.
\tag{14}
\]
The second commuting triple is \(E,V,\mathcal R\), not \(E,Y,V\).
Their ranks agree by (11).

If both ranks are two, the construction does not give an independent
second action on the quotient. Write \(B'=B_g\). More precisely, for
\(S=\ker\delta\cap\ker C\), a single invariant localization gives
\[
B'_\chi=S_\chi[z,\sigma],\qquad
\delta=\partial_\sigma,\quad C=\chi\partial_z,\quad
L=b\partial_\sigma+(\chi\sigma+h)\partial_z,\quad b,h\in S.
\tag{15}
\]
Then \(D_0=(h/\chi)C\). Every other compatible slice is
\(\sigma+q\), \(q\in S\), and replaces \(D_0\) by \(D_0-qC\).
Changing the compatible slice cannot fix the lost rank. The
[exact residual normal form](research/heisenberg-rank-two-residual-pass43.md)
does not assert that \(S\) is a polynomial plane.

## 5. A determinant action in the degree-two configuration

Assume instead \(E^3x=0\), \(h=E^2x\ne0\), and \(V_3,V_4\)
are independent. The preceding coefficient calculation proves
\[
h_3=h_4=0,\quad f=Ex_3,\quad g=Ex_4,\qquad
\operatorname{span}(E,V_3,V_4)
=\ker\operatorname{Jac}h,\quad \dim=2.
\tag{16}
\]
All displayed leading fields kill \(f,g,h\). Their restrictions
to \(A=\ker E\) have just one independent direction. If \(f,g\)
are algebraically dependent, an inherited image identity gives an
invariant ambient linear coordinate, recognizing \(A\).
Thus the remaining case has algebraically independent speeds.

Let \(C\) be the common kernel of the nonzero leading restrictions
on \(A\), and \(F=\operatorname{Frac}C\). A common translation chart
on \(B\otimes_C F\) has
\[
E=\partial_\tau,\quad V_3=\partial_r,\quad
V_4=b_4\partial_r+c_4\partial_\tau,\quad 0\ne c_4\in F.
\tag{17}
\]
As \(Ex_3=f\in C\setminus\{0\}\), write \(x_3=f\tau+q(r)\).
The polynomial determinant combination
\[
K=(V_4x_3)V_3-(V_3x_3)V_4
=c_4(f\partial_r-q'(r)\partial_\tau)
\tag{18}
\]
is an LND on the localization and therefore on the original ring.
It commutes with \(E\), kills \(x_3\), and satisfies
\(Kx_4=-\det(L_0[V_3(x)\mid V_4(x)])\).
Only invariant elements were inverted in establishing its nilpotence.

If this bad projection has rank one, \(K\) fixes the actual
coordinate pair \(x_3,x_4\). The relative-plane kernel theorem gives
\(R=\ker K=\mathbb C[x_3,x_4,z]\).[^4] Dividing the coefficient gcd
of \(E|_R\) gives a primitive two-quasi action on this actual three-ring.
Wang's classification either gives an ambient invariant linear
coordinate immediately, or yields
\[
R=\mathbb C[v,x_3,x_4],\qquad
f=d(v,j)p(v),\quad g=d(v,j)q(v),\quad
j=q(v)x_3-p(v)x_4,\quad C=\mathbb C[v,j],
\tag{19}
\]
where \(\gcd(p,q)=1\).[^4] The polynomial Bezout inverse verifies
this kernel description and retains every multiplicity of \(d\).
Algebraic independence forces \(p'q-pq'\ne0\) and \(d_j\ne0\).

The complete preliminary reduction is in
[the determinant note](research/bad-projection-determinant-pass43.md).
It does not assert that the auxiliary \(v\) is an ambient coordinate
or that \(E|_R\) inherits the original slice.

## 6. Rank-one bad projection cannot retain independent speeds

The common-factor alternative (19) can be eliminated using the
original highest field
\[
H=h\cdot\partial_x,\qquad
J_1=[E,H]=-\tfrac12(fV_3+gV_4),\qquad [E,J_1]=0.
\tag{20}
\]
Both \(v,j\) belong to \(C\), so \(E(Hv)=E(Hj)=0\).
Since \(H\) kills the actual \(x_3,x_4\), differentiating the
identity for \(j\) in (19) gives
\[
Hj=(q'x_3-p'x_4)Hv,\qquad
0=E(Hj)=d(q'p-p'q)Hv.
\tag{21}
\]
The coefficient is nonzero. Hence \(Hv=Hj=0\), so \(H\) kills \(C\).

In particular \(Hh=0\), because the components of \(h\) belong to
\(C\). Thus \(H\) lies in the plane in (16). Its bad projection is
zero. Equation (20) and \(Hf=Hg=0\) show that \(J_1\) also has
zero bad projection. Rank one of the projection makes its kernel
inside that plane one-dimensional; consequently \(J_1\) is
proportional to the nonzero \(H\).

Divide the coefficient gcd \(\gamma\) of \(H\), obtaining a primitive
polynomial field \(H_0\). The coefficients of \(H\) are \(E\)-invariant,
so \(\gamma\) is \(E\)-invariant. Polynomial primitivity gives
\([E,H_0]=\alpha H_0\) with \(\alpha\in B\), rather than just a
rational multiplier. Equation (20) then implies
\[
E\alpha=-\alpha^2.
\tag{22}
\]
Repeated differentiation gives
\(E^n\alpha=(-1)^n n!\alpha^{n+1}\). Local nilpotence forces
\(\alpha=0\), hence \(J_1=0\). This contradicts the independence
of \(V_3,V_4\) and the nonzero speeds in (20).

Therefore an independent-speed instance of this supplied degree-two
configuration must have rank-two bad projection. The rank-one
projection branch is recognized, with the independent-speed part
actually impossible. The
[separate exclusion proof](research/bad-projection-rank-closure-pass43.md)
retains all hypotheses. This is not an exclusion of the remaining
rank-two projection: genuine polynomial-quotient examples already
realize that case.

In fact the bad projection and the bad-speed Jacobian have equal
rank under these assumptions. In the remaining rank-two case, the
two genuine slice-corrected middle fields are independent on
\((f,g)\); together with one leading field they span three intrinsic
polynomial derivation directions. Local nilpotence of the middle
fields is not established, so this is not a commuting action frame.

## 7. Dependent defects require a different differential identity

If instead \(V_3=aD,V_4=bD\) share a primitive direction \(D\),
the multipliers lie in \(\ker E\cap\ker D\). A constant relation
between \(a,b\) already gives a recognized recombination. With no
such relation, use the five-dimensional companion
\[
M=\begin{pmatrix}J&-D(x)/2\\(0,0,a,b)&0\end{pmatrix},\qquad M^5=0.
\tag{23}
\]
For a nonconstant highest vector \(E^mx\), \(m\ge3\), the full
image-line argument gives \(m\in\{3,4\}\) and
\[
E^mx=cq,\quad c_3=c_4=0,\quad
q\mid\rho,\quad \rho= a(E^{m-1}x)_3+b(E^{m-1}x)_4,\quad
[E,T_c]=-\tfrac{m-1}{2}rD,\quad r=\rho/q\in B.
\tag{24}
\]
Both \(q,r\) are joint invariants. The divisibility uses valuations
of a primitive polynomial coefficient vector, not a unit ideal.

When \(r=0\), an actual constant good partial commutes with \(E\),
and the previous one-good-partial recognition theorem applies.
For nonzero \(r\), the exact differential identity is
\[
r\,dq+m q\,dr
=m\bigl((E^{m-1}x)_3\,da+(E^{m-1}x)_4\,db\bigr).
\tag{25}
\]
The last row of (23) is variable. Omitting its differential would
incorrectly reproduce the independent-defect common-power conclusion.

The [dependent-top proof](research/dependent-defect-top-line-pass43.md)
includes a genuine cubic exact-profile example with \(r=0\) and a
squarefree non-cube highest scalar. Its separate nonzero-\(r\) data
are explicitly formal identities, not a realized action. The
nonzero-\(r\), constant-top and lower-flow branches remain open.

The complete companion matrix also gives
\(T_cq=m(m-1)rt/2\), where \(D(E^{m-1}x)=ct\).
If \(D\) were parallel to \(E\), original-slice primitivity would
make \(D=\kappa E\) for a nonzero constant, hence \(t=\kappa q\).
The actual constant partial would send \(q\) to a multiple of itself,
forcing that derivative to vanish and \(r=0\). Thus a remaining
nonzero-\(r\) instance necessarily has two independent actions
\(E,D\). It is not recognized merely from that independence.

## 8. All bounded inverse pairs and the universal gap

For a fixed degree \(d\), introduce coefficients for two arbitrary
four-component polynomial maps \(F,G\), each of degree at most \(d\).
Impose every coefficient of \(G(F(x))=x\) and \(F(G(y))=y\).
This gives a finite ideal in \(8\binom{d+4}{4}\) parameters.

The pulled-back partials are the polynomial expressions
\[
T_i^F=\sum_j(\partial_{y_i}G_j)(F(x))\partial_{x_j}.
\tag{26}
\]
After imposing the inverse identities these are actual coordinate
partials. Additional coefficient equations impose any prescribed
adjoint-height bounds, or simply \(E(F_1)=0\). Existence in this
entire bounded degree class is equivalent to properness of the
corresponding ideal by the Nullstellensatz.[^5]

For coefficients in a specified number field, properness is decidable
by an exact ideal-membership computation; a successful specialization
exists over a finite algebraic extension. This avoids an assumption
about algorithms for arbitrary black-box complex numbers. The
[full finite-level note](research/universal-frame-search-pass43.md)
gives explicit spatial and parameter degree bounds.

Under the original slice hypothesis, some degree admits an invariant
ambient coordinate exactly when (1) holds for that instance. Exhausting
degrees is therefore a positive semidecision. It neither omits wild
coordinate changes nor proves a successful degree exists. No
large inverse-pair search is represented as implemented in this pass.

Current tame-automorphism results do not supply the missing universal
reduction. The recent survey's dimension-four setting is a subgroup
preserving a nondegenerate quadratic form, not all coordinate changes.[^6]
Finite-jet approximation is also insufficient: for \(E=\partial_s\),
the genuine shear \(F_N=(a+s^N,s,b,c)\) agrees with the identity
to order \(N-1\), but has exact adjoint profile \((0,N-1,0,0)\).
Arbitrarily accurate jets need not retain low adjoint height.

## 9. Remaining mathematical obligations

The complete supplied two-quadratic profile is still unrecognized.
At degree two with independent defects, the new exclusion removes
rank-one bad projection; rank-two projection with independent speeds
remains. Its known examples show that the residual is not empty,
but do not show that every such kernel is polynomial.

In the independent-defect higher-degree power law, a nonzero constant
\(T_cg\) was already recognized. At \(T_cg=0\), the global repair and
either rank-three alternative now recognize the kernel. Nonconstant
\(T_cg\), and the rank-two common-base configuration in (15), remain.
Constant highest-vector branches retain their separately stated gaps.

With dependent defects, the zero polynomial commutator multiplier is
recognized, but the variable-row nonzero multiplier requires additional
structure. No common-power assertion is substituted for (25).

Even complete recognition of (2) would leave the universal question:
why must an arbitrary sliced action admit that frame or another
recognized one? A solution to (1) must resolve this gap or bypass
the frame method entirely. None of the conditional results is a
public novelty claim, a human-reviewed theorem, or a Lean proof.

## Sources

[^1]: Nikhilesh Dasgupta and Sergey Gaifullin, [*On locally nilpotent derivations of polynomial algebra in three variables*](https://arxiv.org/pdf/2306.00510v2), Theorem 2.5 and Proposition 2.6, PDF pp. 5-6. Slice and local-slice equalities are used over characteristic-zero fields.

[^2]: S. M. Bhatwadekar, Neena Gupta and S. A. Lokhande, [*Some K-theoretic properties of the kernel of a locally nilpotent derivation on k[X1,...,X4]*](https://arxiv.org/pdf/1501.01438v1), Theorem 3.5 and proof, PDF p. 11. Original-kernel regularity and an actual invariant ambient coordinate are both required.

[^3]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), author manuscript dated October 5, 2001, Proposition 3.2, Proposition 3.4 and Theorem 2.4. The manuscript also states surface cancellation as CP(3), citing Takao Fujita, [*On Zariski problem*](https://doi.org/10.3792/pjaa.55.106), 1979. The original Fujita proof is an established external input, not newly reconstructed here.

[^4]: Nikhilesh Dasgupta and Neena Gupta, [*Nice derivations over principal ideal domains*](https://arxiv.org/pdf/1701.03635v1), Theorems 2.2 and 4.1, PDF pp. 3 and 9. These reproduce the exact Daigle-Freudenburg relative-plane kernel theorem and Wang primitive two-quasi alternatives. The original classifications are external inputs.

[^5]: Stacks Project, [Theorem 10.34.1, Hilbert Nullstellensatz, tag 00FV](https://stacks.math.columbia.edu/tag/00FV). Used only for finite-type coefficient ideals over a specified field and their algebraic closed points.

[^6]: Stéphane Lamy, [*Tame polynomial automorphisms*](https://arxiv.org/html/2609.05655v1), September 4, 2026, introduction and Section 3.1. Its four-dimensional orthogonal subgroup does not cover arbitrary sliced polynomial actions.
