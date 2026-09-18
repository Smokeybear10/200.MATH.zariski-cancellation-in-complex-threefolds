# The actual mixed c-projection has a one-point normalization boundary

For the supplied actual quadratic mixed fiber with nonzero speed
normal, the c-projection is quasi-finite after the specified local
base change. Its finite normal closure is free of rank four, and
the actual open misses exactly one reduced closed point.

The boundary is not only that point. It contains divisors, all over
invariant base curves. A boundary divisor has residue degree one
and multiplicity one. At least one degree-one invariant curve
therefore has c-degree three on its whole generic divisor.
A degree-two constant-cover curve has no boundary divisor above
its generic point, and c has degree two on that divisor. The
missing closed point may still lie on its closure.

These conclusions require the actual whole-fiber and divisor
hypotheses below. A difference between generic rank four and
closed-fiber length three alone does not prove them.

## 1. The precise actual rings

Retain the nonconical quadratic original frame and the actual
collapsed mixed profile (2,1), with \(L(\mathfrak m)\ne0\).
The [whole-fiber theorem100](quadratic-whole-fiber-actions-pass100.md)
and [whole-plane theorem99](quadratic-whole-plane-fiber-pass99.md) give
\[
\begin{gathered}
S=\mathbb C[s_1,s_2]=\ker(N|_A),\qquad A_K=K[v],
\qquad K=\operatorname{Frac}S,\\
A/\mathfrak mA=\mathcal D[c],\qquad
\mathcal D=\mathbb C[G]/(G^2(G-1)),\\
\bar N=(\lambda\epsilon+\rho e_1)\partial_c,\qquad
\epsilon=G-G^2,\quad e_1=G^2,\quad \lambda,\rho\in\mathbb C^*,\\
Nc\notin\mathfrak mA,\qquad
\deg_v c=4,\qquad
[\operatorname{Frac}A:K(c)]=4.
\end{gathered}
\tag{1}
\]
Here A is the actual smooth affine threefold ring, hence normal;
S into A is faithfully flat, and every prime element of S stays
prime in A. The degree-four assertion is the exact
[strict projection theorem97](quadratic-weighted-rank-defect-pass97.md):
c restricts to the parameter on both components, giving whole
degree three strictly below its generic degree, which is at
most four.

Let \(\ell=\mathbb C(c)\) denote the residue field of the following
local base; it is not the fraction field K of S. Define
\[
\begin{gathered}
T=(S[c])_{\mathfrak mS[c]},\qquad
\mathfrak n=\mathfrak mT,\qquad
D=A\otimes_{S[c]}T,\\
T\text{ is a regular local domain of dimension two},\qquad
T/\mathfrak n=\ell,\qquad \operatorname{Frac}T=K(c),\\
D/\mathfrak nD
 =\ell[G]/(G^2(G-1))
 \simeq \ell[\epsilon]/(\epsilon^2)\times\ell.
\end{gathered}
\tag{2}
\]
The algebra S[c] is a polynomial ring over S since c is
transcendental over K. The map T to D is injective and finite
type. D is a localization of A, and is thus a normal domain.
The last line is the actual whole closed fiber, of dimension
three over ell, not its reduction.

## 2. Quasi-finiteness on every base stratum

Let p be any irreducible element of S in m, and write
\(k_p=\operatorname{Frac}(S/(p))\).
The [actual divisor theorem91](nonconical-residue-degree-bound-pass91.md)
supplies the entire generic divisor, not just its fraction field:
\[
\begin{gathered}
A_{S\setminus(p)}/pA_{S\setminus(p)}
 =k'_p[w],\qquad [k'_p:k_p]=N_p\in\{1,2\},\\
\overline N\ne0,\qquad
\overline{Nc}\ne0,\qquad
\bar c\in k'_p[w]\setminus k'_p,\\
D\otimes_T\kappa(pT)=k'_p(w),\qquad
n_p:=[k'_p(w):k_p(\bar c)]
 =N_p\deg_w\bar c<\infty.
\end{gathered}
\tag{3}
\]
Indeed \(pA\subset\mathfrak mA\), so (1) shows \(Nc\notin pA\).
Since pA is prime, its nonzero class remains nonzero after the
base localization. A nonzero LND on the polynomial line over
k'p has kernel k'p. Thus c is nonconstant in w, and the line
ring is finite over \(k_p[\bar c]\). Inverting its nonzero base
polynomials gives exactly the field in (3).

After clearing finitely many coefficients of monic equations
over K[c], there is a nonzero \(s\in S\) such that \(A_s\) is
finite over \(S_s[c]\). Such equations exist because
\(A_K=K[v]\) is finite over K[c]. Hence D is finite over T
away from V(s).

Any height-one prime of T containing s is pT for an
irreducible factor p of s in S that belongs to m: the
polynomial ring S[c] and its localization are UFDs, and
such a factor stays prime. Its fiber is finite by (3).
All other height-one fibers are in the finite locus.
The generic fiber is finite of degree four, and the unique
closed fiber is finite by (2). These exhaust the points of
the two-dimensional local spectrum T. The finite-type
morphism Spec(D) to Spec(T) is therefore quasi-finite
everywhere, not just near its closed fiber.

## 3. The actual finite normal closure is free of rank four

Let C be the integral closure of T in \(\operatorname{Frac}A\).
It is finite over T: T is Noetherian and normal, and the
degree-four field extension is separable in characteristic
zero. This is precisely the finite-normalization hypothesis
of [Stacks, Lemma 10.161.8](https://stacks.math.columbia.edu/tag/032L).

Every element of C is integral over D as well as T, so the
normality of D puts C inside D. Thus C is also the integral
closure of T inside D. The affine normalization version of
[Zariski's Main Theorem, Theorem 29.57.1](https://stacks.math.columbia.edu/tag/03GT)
applies to the finite-type, everywhere quasi-finite map:
\[
\begin{gathered}
\operatorname{Spec}D\ \simeq\ \mathcal U
 \subset\mathcal X:=\operatorname{Spec}C
 \quad\text{as a dense affine open},\\
C\text{ is finite and normal over }T,\qquad
\boxed{\quad C\simeq T^{\,4}\text{ as a module}.\quad}
\end{gathered}
\tag{4}
\]
To verify the last assertion, C has dimension two. Each of
its maximal local rings has dimension two, since it is
integral over T and going down over the normal domain T
gives the required length-two prime chain. Normal
Noetherian schemes of dimension at most two are
[Cohen--Macaulay](https://stacks.math.columbia.edu/tag/0B3D).
At each such local ring the T-fiber is zero-dimensional.
Thus the regular-source, Cohen--Macaulay-target and dimension
equality hypotheses of
[miracle flatness, Lemma 10.128.1](https://stacks.math.columbia.edu/tag/00R4)
hold. C is flat over T, and finite flat over the local ring T
means free. Its generic field degree is four, fixing its rank.

No assertion that an arbitrary localization \(C_P\) is a
finite T-module is used.

## 4. Exactly one omitted reduced point and its completion

The open part of the finite closed fiber in (4) is exactly
the algebra in (2). A finite Artin algebra splits into its
local factors, and an open subset selects whole such factors.
The missing factors therefore have total ell-dimension one.
Consequently there is exactly one missing closed point P, and
\[
\begin{gathered}
C/\mathfrak nC
 \simeq \ell[\epsilon]/(\epsilon^2)\times\ell\times\ell,\\
\kappa(P)=\ell,\qquad
(C/\mathfrak nC)_P=\ell,\\
\boxed{\quad \widehat{C_P}\simeq\widehat T
 \quad\text{canonically as }\widehat T\text{-algebras}.\quad}
\end{gathered}
\tag{5}
\]
For the completed assertion, the finite algebra
\(C\otimes_T\widehat T\) decomposes into its completed local
factors. This follows by lifting the finitely many Artin
idempotents through the powers of n and taking the inverse
limit. At each factor the n-adic and maximal-ideal-adic
topologies agree, since their radicals agree. Each factor is
a direct summand of the finite free module in (4), hence a
finite free module over the local ring T-hat.

The factor at P has residue dimension one, so it has rank one.
Its unit element is a module basis by Nakayama. The structural
map from T-hat is therefore the stated algebra isomorphism.
This argument uses the completed finite factor, not a false
finite-module claim for \(C_P\) before completion.

## 5. The nonempty boundary has invariant divisors

Put \(\mathcal Z=\mathcal X\setminus\mathcal U\).
It is nonempty by (5). It has pure codimension one:
both X and U are affine, X is Noetherian and separated,
and U is dense, so the hypotheses of
[Stacks, Section 31.17, Lemmas 31.17.4--5](https://stacks.math.columbia.edu/tag/0BCQ)
apply. In the present normal surface this also follows
from the height-one intersection description of regular
functions: a sole codimension-two omission would have the
same global functions as X and could not be the different
affine scheme Spec(D).

After inverting s from Section 2, D is finite and normal
over \(T_s\), so it equals \(C_s\). Integral closure commutes
with this localization. Therefore every boundary divisor
lies over a height-one factor pT of s. In particular
\[
\begin{gathered}
\mathcal Z\ne\varnothing,\qquad
\operatorname{Irr}(\mathcal Z)
 =\{\,V(Q):\operatorname{ht}Q=1,\ V(Q)\subseteq\mathcal Z\,\},
\qquad Q\subset P,\\
Q\cap T=pT
\quad\text{for an irreducible }p\in S\cap\mathfrak m.
\end{gathered}
\tag{6}
\]
The set in the first line includes only the boundary
height-one primes Q. Every closed point of each such V(Q)
is omitted, and the only omitted closed point is P.
This explains the containment in P. Finiteness over T
makes the contracted prime height one. No arbitrary
polynomial in c is being declared an invariant base curve.

## 6. A boundary divisor is a unique unramified degree-one branch

Fix a boundary Q over pT. The finite T/p-module C/Q
has nonempty closed fiber supported only at P. That fiber
is a quotient of the length-one factor of (5), so its
dimension over ell is exactly one. Its unit generates
that quotient. Nakayama and the injective base map give
\[
\boxed{\quad C/Q=T/pT.\quad}
\tag{7}
\]
More explicitly, Nakayama makes C/Q a cyclic T-module
generated by 1. The resulting surjection \(T\to C/Q\)
has kernel \(Q\cap T=pT\), proving (7) as an algebra
identity, not just a generic rank statement.

Complete its local quotient at P and use (5). The structural
isomorphism identifies the extended ideal Q with p:
\[
Q\widehat{C_P}=p\widehat{C_P},\qquad
QC_P=pC_P,\qquad
e_Q(p)=1,\qquad
[\kappa(Q):\kappa(pT)]=1.
\tag{8}
\]
The middle equality follows from faithful flatness of
Noetherian local completion. Localizing it further at Q
makes p a uniformizer in the normal height-one DVR C_Q,
giving the ramification index one. The residue degree
one is already (7).

If two boundary primes lay over the same pT, both would
be contained in P and both would give the same completed
ideal in (8). Faithfully flat contraction to C_P, then
contraction of these prime localizations to C, makes
them equal. Thus there is at most one boundary divisor
over each invariant prime p. Splitting of p after
completion is not assumed away; the quotient identity
(7) supplies exactly the completed ideal needed.

## 7. Divisor degree balance and the remaining boundary

The actual prime p remains prime in D, so there is exactly
one retained height-one prime over pT. Its valuation index
is one, since p generates its prime ideal in the normal
ring D. Its residue field is the field in (3), of degree
n_p over \(\kappa(pT)=k_p(\bar c)\).

Localize the finite normal closure C over the DVR \(T_{pT}\).
It is finite free of rank four, and its local branches are
DVRs. Reducing modulo p gives the ordinary degree formula
\[
4=n_p+b_p,\qquad
b_p=
\begin{cases}
1,&\text{a boundary divisor lies over }pT,\\
0,&\text{no boundary divisor lies over }pT.
\end{cases}
\tag{9}
\]
Indeed every height-one branch is either retained or in
the boundary. The retained one contributes \(1\cdot n_p\);
Section 6 allows at most one omitted branch, contributing
\(1\cdot1\). This accounts for all branches of the
finite normal closure, not only the chosen actual divisor.

Combining (3), (6) and (9) yields
\[
\begin{gathered}
\boxed{\quad
b_p=1\quad\Longrightarrow\quad
N_p=1,\quad \deg_w\bar c=3.
\quad}\\
\boxed{\quad
N_p=2\quad\Longrightarrow\quad
b_p=0,\quad n_p=4,\quad \deg_w\bar c=2.
\quad}\\
\text{At least one invariant prime }p\in\mathfrak m
\text{ satisfies the first line.}
\end{gathered}
\tag{10}
\]
For the first implication, \(n_p=3\) and
\(n_p=N_p\deg_w\bar c\) with \(N_p\in\{1,2\}\).
The second follows because n_p must be even. Boundary
nonemptiness and purity provide the final existence assertion.

The conclusion for degree-two constant covers excludes a
boundary DIVISOR over pT. It does not say that the omitted
CLOSED point P is absent from the closure of the retained
p-divisor. It may lie there over the common closed base
point; the proof only fixes the generic divisor degree.
Likewise no global finiteness of D, recognition of A, or
elimination of the actual mixed fiber is concluded.

There is a further finite conclusion when a boundary lies over p.
Let Q be that boundary prime and Q' the retained prime. The latter
cannot be contained in P: otherwise \(pC_P=QC_P\) from (8)
would force \(Q'C_P=QC_P\). Thus Q and Q' have no common
closed point and are comaximal. The normal surface C is
Cohen--Macaulay, so C/pC has no embedded primes; both minimal
primes have multiplicity one by the valuation calculation.
It is therefore reduced, and the Chinese remainder theorem gives
\(C/pC\simeq C/Q\times C/Q'\).
The whole retained component avoids the boundary, whose only
closed point is P. Hence \(D/pD=C/Q'\).
Together with (7), this gives
\(C/pC\simeq T/pT\times D/pD\).
Since C/pC is free of rank four over the local ring T/pT,
the complementary factor D/pD is finite free of rank three.
This statement concerns such a degree-one boundary curve,
not the degree-two curves discussed above.

## Source and proof scope

This proof uses the full actual whole-fiber formulas99--100,
strict weighted projection97 and generic-divisor theorem91.
Those hypotheses cannot be replaced by a formal local model
or by generic degree four and closed length three alone.

For this proof Jet freshly read the complete displayed
statements and proofs of Stacks tags
[03GT](https://stacks.math.columbia.edu/tag/03GT),
[00Q9](https://stacks.math.columbia.edu/tag/00Q9),
[032L](https://stacks.math.columbia.edu/tag/032L),
[00R4](https://stacks.math.columbia.edu/tag/00R4),
[0B3D](https://stacks.math.columbia.edu/tag/0B3D),
and the complete [0BCQ section](https://stacks.math.columbia.edu/tag/0BCQ).
The proof of 03GT invokes the algebraic theorem00Q9, whose
displayed induction proof was also read; the deeper conductor
lemmas within that induction were not freshly reconstructed.
The normal-surface and completion facts retain their standard
dependencies, not a claim of a complete new foundations audit.

Root supplied the rank-one omitted-factor and boundary-quotient
argument. Jet supplied the all-strata quasi-finite gate and
the completed-factor precision; both independently reconstructed
the degree balance. No numerical test verifies this universal
geometry, and no new checker is added. All files through104
remain unchanged.
