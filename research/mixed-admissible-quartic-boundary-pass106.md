# Every admissible quartic has an actual normalization boundary

In the actual collapsed mixed quadratic sector with nonzero speed
normal, the normalization-boundary theorem105 applies to every
element of the fourth degree module that is nonconstant on both
reduced components. A nilpotent coefficient in its whole-fiber
residue does not obstruct the argument. Every such projection
misses one reduced point in a finite rank-four normal closure and
has a degree-one boundary divisor on which its degree is three.

There is a uniform consequence as well: on any fixed invariant
divisor with constant-field degree two, every fourth-degree
element has residue degree at most two. These are restrictions
inside the supplied original frame, not a recognition theorem.

## 1. Actual hypotheses and local parameters

Retain the complete actual setting of
[boundary105](mixed-c-parameter-normalization-boundary-pass105.md).
The original sliced three-good-coordinate frame supplies a smooth
affine domain A with A[u] a polynomial ring in four variables,
the primitive LND N, and the faithfully flat full kernel plane S.
At the specified closed base point m the profile is (2,1), both
components are collapsed, and the speed normal L(m) is nonzero.
In particular
\[
\begin{gathered}
S=\mathbb C[s_1,s_2]=\ker(N|_A),\qquad R=S_{\mathfrak m},
\qquad K=\operatorname{Frac}S,\qquad A_K=K[v],\\
F_j=\ker(N^{j+1}|_A),\qquad
\deg_N c=\deg_v c=4,\\
A/\mathfrak mA=\mathcal D[c],\quad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\quad
\epsilon=G-G^2,\quad e_1=G^2,\\
\bar N=(\lambda\epsilon+\rho e_1)\partial_c,
\qquad \lambda,\rho\in\mathbb C^*.
\end{gathered}
\tag{1}
\]
Every irreducible element of S remains prime in A. The entire
generic divisor is the polynomial line over its finite constant
extension, with degree at most two, as in
[divisor91](nonconical-residue-degree-bound-pass91.md).
The any-function strict inequality of
[weighted-defect97, Section 2](quadratic-weighted-rank-defect-pass97.md)
is an additional actual geometric input. It is not deduced here
from flatness or from the displayed fiber algebra.

Allow U in (F4)_R, not only in F4. Its reduced values on the
double and simple lines are assumed nonconstant. Such a U is
called admissible. A denominator in S outside m can be cleared;
it is a unit at every base divisor through m and has nonzero
constant residue at m. If U=V/d with d outside m, then
R[U]=R[V]. Thus the arguments below concern actual invariant
base localizations and also apply to these localized elements.

## 2. The whole-fiber change of parameter

Write d2 and d1 for the positive degrees of the two reduced
values of U. Strict97, after clearing the preceding denominator,
gives 2d2+d1 less than deg_v U, which is at most four. Therefore
\[
\begin{gathered}
\deg_vU=4,\qquad d_2=d_1=1,\\
\bar U=(a_2c+b_2+\epsilon\beta(c),\ a_1c+b_1),
\quad a_1,a_2\in\mathbb C^*,\quad b_i\in\mathbb C,
\quad\beta\in\mathbb C[c],\\
\text{on the double factor,}\qquad
t=(\bar U-b_2)/a_2,\qquad
c=t-\epsilon\beta(t)/a_2,\\
\mathcal D[c]\simeq
\mathbb C[\bar U,\epsilon]/(\epsilon^2)
\ \times\ \mathbb C[\bar U].
\end{gathered}
\tag{2}
\]
The inverse on the simple factor is c=(Ubar-b1)/a1.
For the double inverse, substitution changes beta(c) only by
a multiple of epsilon, which disappears after multiplication
by epsilon. This proves the algebra isomorphism over C[Ubar],
not merely a statement about the two reduced lines. In particular
the whole fiber is free of rank three over C[Ubar].

There is also a useful assertion for elements that were not
initially admissible. If V belongs to (F4)_R, then V+alpha c is
nonconstant on both lines for all but at most two complex numbers
alpha. Applying (2) to one such alpha proves that both reduced
values of every V in (F4)_R are affine in c. This does not bound
its nilpotent coefficient by itself.

Define the actual projection rings
\[
\begin{gathered}
T_U=(R[U])_{\mathfrak mR[U]},\qquad
\mathfrak n_U=\mathfrak mT_U,\qquad
D_U=A_R\otimes_{R[U]}T_U,\qquad \ell_U=\mathbb C(U),\\
\dim T_U=2,\qquad \operatorname{Frac}T_U=K(U),\qquad
[\operatorname{Frac}A:K(U)]=4,\\
D_U/\mathfrak n_UD_U
\simeq\ell_U[\epsilon]/(\epsilon^2)\times\ell_U,\\
\overline{NU}=(\lambda a_2\epsilon,\rho a_1)\ne0,
\qquad NU\notin\mathfrak mA_R.
\end{gathered}
\tag{3}
\]
Here T_U is a regular local domain: U is transcendental over K,
so R[U] is a polynomial ring over R. The ring D_U is a normal
domain, being a localization of the actual A. The nilpotent term
in (2) contributes zero to Nbar Ubar because epsilon squared is
zero. No condition that beta be constant was used.

## 3. All-strata quasi-finiteness survives

Fix an invariant irreducible p in m, and let k_p be Frac(S/(p)).
The actual divisor theorem gives
\[
\begin{gathered}
A_{S\setminus(p)}/pA_{S\setminus(p)}=k'_p[w],\qquad
N_p=[k'_p:k_p]\in\{1,2\},\qquad \bar N\ne0,\\
\overline{NU}\ne0,\qquad
\bar U\in k'_p[w]\setminus k'_p,\\
D_U\otimes_{T_U}\kappa(pT_U)=k'_p(w),\qquad
n_p(U)=N_p\deg_w\bar U.
\end{gathered}
\tag{4}
\]
Indeed pA_R is contained in mA_R, so (3) excludes NU from pA_R.
Its nonzero residue remains nonzero at the generic divisor,
because p remains prime. The localized denominator of U is an
invariant unit there. The nonzero LND on k'p[w] is a translation
with kernel k'p. Hence Ubar is a nonconstant polynomial in w;
the line algebra is finite over k_p[Ubar], and inverting the
nonzero polynomials in Ubar gives the field in (4).

Since A_K=K[v] is finite over K[U], finitely many monic equations
for generators of A_R become defined after inverting some nonzero
s in R. Thus (D_U)_s is finite over (T_U)_s. The height-one primes
of T_U containing s are exactly pT_U for invariant prime factors
p of s. The ring R[U] is a UFD, and each such p stays prime in it.
Their fibers are finite by (4). All other height-one fibers are
already in the finite locus. The generic fiber is finite of degree
four; the unique closed fiber is finite by (3). These exhaust
the points of Spec(T_U), so D_U is everywhere quasi-finite over
T_U. No finiteness conclusion was inferred just from its closed
fiber or from generic finiteness.

## 4. Finite closure, omitted point and actual boundary

Let C_U be the integral closure of T_U in Frac A. It is finite:
T_U is Noetherian and normal, and the field extension is finite
separable, precisely the hypotheses of
[Stacks 032L](https://stacks.math.columbia.edu/tag/032L).
Normality of D_U puts C_U inside D_U. The finite-type affine
normalization form of
[Zariski's Main Theorem, 03GT](https://stacks.math.columbia.edu/tag/03GT)
then identifies Spec(D_U) with a dense affine open in Spec(C_U).

The finite normal ring C_U has dimension two, and each maximal
local ring has dimension two by going down over normal T_U.
Those local rings are Cohen--Macaulay by
[0B3D](https://stacks.math.columbia.edu/tag/0B3D).
Their T_U fibers have dimension zero, so all hypotheses of
[miracle flatness, 00R4](https://stacks.math.columbia.edu/tag/00R4)
hold. Thus C_U is finite free of rank four. Its closed Artin
fiber contains the whole open fiber (3), of length three.
Consequently there is one omitted closed point P_U, and
\[
\begin{gathered}
C_U\simeq T_U^{\,4}\quad\text{as a module},\qquad
C_U/\mathfrak n_UC_U
\simeq\ell_U[\epsilon]/(\epsilon^2)\times\ell_U\times\ell_U,\\
\kappa(P_U)=\ell_U,\qquad
\widehat{(C_U)_{P_U}}\simeq\widehat{T_U}
\quad\text{canonically over }\widehat{T_U}.
\end{gathered}
\tag{5}
\]
For the last statement, complete the finite algebra over T_U.
Lifting its closed-fiber idempotents splits it into completed
local factors. Each is a finite free summand over the completed
local base. The P_U factor has residue dimension one, hence
rank one, with its unit as a module basis. This proves (5).
It does not assert that (C_U) at P_U before completion is a
finite T_U-module.

The nonempty complement is pure codimension one by the affine-open
complement theorem [0BCQ, Lemmas 31.17.4--5](https://stacks.math.columbia.edu/tag/0BCQ).
Both schemes are affine and Noetherian, the larger is separated,
and the open is dense. Since (D_U)_s=(C_U)_s, all boundary
divisors lie over invariant factors pT_U of s. Every boundary
divisor Q specializes only to the omitted closed point P_U,
because C_U is finite over a local ring and the boundary is
closed. Its quotient C_U/Q has one-dimensional closed fiber,
with unit spanning it. Nakayama therefore gives the actual
algebra identity C_U/Q=T_U/pT_U.

Completing this quotient at P_U in the canonical identification
(5) gives Q times the completion equal to p times the completion.
Faithfully flat contraction gives Q(C_U)_(P_U)=p(C_U)_(P_U).
Thus its DVR ramification index is one and its residue degree
over pT_U is one. Two boundary primes over the same p would
have equal ideals after this localization and hence be equal.
The prime p stays prime in D_U, so there is one retained branch
over pT_U, also of ramification index one, with residue degree
n_p(U). Reducing the finite free closure over the DVR at pT_U
therefore counts every branch and gives
\[
\begin{gathered}
4=n_p(U)+b_p(U),\qquad b_p(U)\in\{0,1\},\\
b_p(U)=1\ \Longrightarrow
N_p=1,\quad \deg_w\bar U=3,\\
N_p=2\ \Longrightarrow
b_p(U)=0,\quad \deg_w\bar U=2,\\
\boxed{\text{For each admissible U, some invariant }p\in\mathfrak m
\text{ has }b_p(U)=1.}
\end{gathered}
\tag{6}
\]
Boundary purity and nonemptiness give the final existence claim.
The chosen p can depend on U. Absence of a boundary divisor
over a degree-two constant-cover curve does not exclude P_U
from the closure of the retained divisor over that curve.

For completeness, the final splitting in boundary105 also
persists. If Q is the boundary prime over p and Q' is retained,
then Q' is not contained in P_U: otherwise the preceding local
ideal equality would identify Q' and Q. Hence Q and Q' are
comaximal. The normal surface C_U is Cohen--Macaulay, so C_U/pC_U
has no embedded primes. Both generic lengths are one, making
that quotient reduced. The retained component avoids the entire
boundary. Chinese remaindering then gives
\[
C_U/pC_U\simeq T_U/pT_U\times D_U/pD_U,
\qquad D_U/pD_U\text{ is finite free of rank three over }T_U/pT_U.
\tag{7}
\]
The freeness follows from its being the complementary direct
summand of the free rank-four quotient over the local ring T_U/pT_U.

## 5. A restriction uniform in the parameter

Fix any invariant p through m with N_p=2. For each V in (F4)_R,
choose alpha in C so that U=c+alpha V is admissible. All but
finitely many alpha work, since the two reduced values of V
are affine. Equation (6) makes Ubar have degree two in w.
Since cbar already has degree two by boundary105, a residue
Vbar of degree greater than two is impossible: for every
nonzero alpha it would give Ubar that larger degree. Thus
\[
\begin{gathered}
\operatorname{im}\big((F_4)_R\longrightarrow k'_p[w]\big)
\subseteq k'_p+k'_p w+k'_p w^2,\\
N^3((F_4)_R)\subseteq pA_R,\qquad
N^3((F_3)_R)\subseteq pR,\qquad
N^4((F_4)_R)\subseteq pR.
\end{gathered}
\tag{8}
\]
The first derivative inclusion follows because the divisor LND
is a translation. Its generic-divisor vanishing contracts to
pA_R since that prime remains prime under the invariant
localizations. For the last two inclusions, the derivatives
are invariant, and faithful flatness contracts pA_R to pR.
This does not say that N cubed of every F4 element is invariant.

The uniform conclusion distinguishes these degree-two constant
divisors from the mandatory degree-one boundary divisors of
individual projections. It does not make the latter independent
of U or turn any of the quasi-finite maps into a finite map.

## Source and proof scope

The complete boundary105 and strict weighted-defect97 proofs
were reread before this extension. The retained actual divisor91
and whole-fiber99--100 hypotheses remain essential. In this pass
the complete displayed statements and proofs of Stacks tags
032L, 03GT, its algebraic input
[00Q9](https://stacks.math.columbia.edu/tag/00Q9), 0B3D and 00R4,
and the complete 0BCQ section were read. Their deeper conductor,
completion and foundational dependencies were not freshly rebuilt.
The source applications are the existing normalization, flatness
and affine-boundary theorems, not new versions of them.

The new input checks are the nilpotent polynomial inverse in (2),
the all-parameter nonvanishing in (3)--(4), and the resulting
uniform specialization restriction (8). Root and General pursue
the separate consequences for derivative-image ideals. No
numerical method accompanies this geometric proof. It does not
exclude the mixed fiber, identify an ambient invariant coordinate,
recognize A, or remove the arbitrary-frame entry gap. All files
through105 are unchanged.
