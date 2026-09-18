# Literature audit: slices of vertical extensions of a rank-three LND

**Audit date:** 2026-09-12  
**Status:** targeted post-proof screen; not an originality determination

## Question and outcome

Let `k` be a field of characteristic zero,

\[
R=k[x,y,z],\qquad B=R[w],\qquad
E=\delta+a\partial_w\quad(a\in R),\qquad T=\partial_w,
\]

where `delta` is a nonzero rank-three locally nilpotent derivation of `R`.
The questions screened here are:

1. Does a slice for `E` force
   \(a=c+\delta H\), with \(c\in k^*\) and \(H\in R\)?
2. If not, does the commuting coordinate derivation `T` at least force
   \(\ker E\cong k^{[3]}\), equivalently make `E` an ambient translation?
3. Do published results already contain the exact coefficient classifications
   proved in this project for Freudenburg's derivation?

The bounded primary-source audit found **no theorem that supplies either
implication in this generality**, and no statement matching the project's exact
coefficient classifications. The closest extension theorem treats an invariant
coefficient under additional representation-theoretic hypotheses. The closest
commuting-derivation theorems require a dual slice system, as many independent
derivations as the relevant dimension or codimension demands, an invariant
ambient coordinate, or triangulability. None of those hypotheses follows merely
from `[E,T]=0` and the existence of one `E`-slice.

This is a negative literature finding, not a novelty claim. Keyword indexing is
incomplete, and a specialist/citation review remains necessary.

## Exact algebra that fixes the comparison

Freudenburg's general extension lemma confirms that `E` is locally nilpotent
for arbitrary `a in R` and that `[E,T]=0`; no invariance assumption on `a` is
needed for these two conclusions.[^freudenburg-extension] Directly,

\[
E^{n+1}(w)=\delta^n(a),\qquad
\ker E\cap\ker T=\ker\delta.
\]

Since `delta` is nonzero, `E` and `T` are `B`-linearly independent. For the
Freudenburg rank-three example, Miyanishi's theorem gives
\(\ker\delta\cong k^{[2]}\), but this is only an abstract polynomial common
kernel. The cited theorem does not say that its two generators form an ambient,
or stably ambient, coordinate pair.[^miyanishi-modern]

There is one elementary positive normal form. If

\[
a=c+\delta H,\qquad c\in k^*,
\]

then `w'=w-H`, `t=w'/c` satisfy `E(t)=1`. In `R[t]`,
`E=delta+partial_t`, and the finite exponential

\[
r\longmapsto \exp(-t\delta)(r),\qquad t\longmapsto t
\]

is an automorphism. Its transformed `R` is killed by `E`, so `E` is conjugate
to `partial_t` and its kernel is a polynomial ring. This conclusion is an
explicit shear-and-flow calculation, not an application of a general commuting
derivations theorem.

Conversely, write a proposed slice in its original `w`-degree:

\[
s=\sum_{i=0}^n b_iw^i.
\]

The equation `E(s)=1` is exactly

\[
\begin{aligned}
\delta b_n&=0,\\
\delta b_j+(j+1)ab_{j+1}&=0 &&(1\le j<n),\\
\delta b_0+ab_1&=1.                 \tag{1}
\end{aligned}
\]

In particular, an affine-in-`w` slice whose `w` coefficient is in `k*` is
equivalent to the displayed gauge form. The unresolved algebraic possibility is
a higher-`w` slice, or an affine slice with nonconstant invariant leading
coefficient. Published slice theorems do not eliminate that possibility.

## What commutation really yields after an `E`-slice

Assume `E(s)=1` and put `C=ker E`. The slice theorem gives

\[
B=C[s],\qquad E=\partial_s.                 \tag{2}
\]

Here `C` is a finitely generated, regular three-dimensional UFD and a retract of
`B`; it satisfies `C[s]=k^[4]`. Because `T` commutes with `E`, it preserves `C`.
Set

\[
d=T|_C\in\operatorname{LND}(C),\qquad q=T(s)\in C.
\]

Then, in the presentation (2),

\[
T=d+q\partial_s,\qquad
C^d=C\cap\ker T=\ker\delta=k[f,g].          \tag{3}
\]

These identities isolate the genuine residual case:

* If `q=0`, then `s in R` and `delta(s)=1`, impossible for a rank-three
  derivation of `k^[3]`.
* If `q in k*`, then `partial_w(s)=q` forces `s=qw+h` with `h in R`; equation
  `E(s)=1` gives `a=q^-1+delta(-h/q)`.
* If `d=0`, then `T=q partial_s`. Since `T` has the slice `w`, `q` divides one
  in `C`; hence `q in k*` and the preceding case applies.
* If `d` itself has a slice, then (3) gives
  `C=k[f,g]^[1]=k^[3]`, so `E` is an ambient translation.

Thus a non-gauge slice not already settled by elementary algebra would require

\[
d\ne0,\qquad q\ne0,\qquad q\notin k,
\]

with `d` having no known slice. Notice that local nilpotence of `T` does **not**
imply `d(q)=0`; no such condition should be silently inserted into (3).

A useful projection identity makes the coupling explicit. Let

\[
\pi_E(b)=\sum_{j\ge0}\frac{(-s)^j}{j!}E^j(b)\in C.
\]

For `r in R`, commutation and `T(r)=0` give

\[
d\bigl(\pi_E(r)\bigr)=-q\,\pi_E(\delta r).  \tag{4}
\]

Neither (3) nor (4) supplies a slice for `d`.

## Why the simultaneous-slice theorems do not apply

Bavula's invariant-generator theorem assumes commuting LNDs
`D_1,...,D_m` together with elements `u_j` satisfying the full dual relations
\(D_i(u_j)=\delta_{ij}\).[^bavula] El Kahoui uses the same dual-slice mechanism
in the UFD setting.[^elkahoui] Separate ordinary slices are weaker.

For the vertical pair `(E,T)`, a dual slice system exists exactly when both

\[
\delta u=1\quad\text{for some }u\in R,
\qquad
a=-\delta r\quad\text{for some }r\in R.     \tag{5}
\]

Indeed, the first cross-slice must be killed by `T`, hence belongs to `R`; the
second must have `T(v)=1`, hence is `v=w+r`, and `E(v)=0` is the second equation
in (5). Rank three excludes the first equation. Consequently, the dual-slice
theorems are not merely unproved here: their central hypothesis fails for this
pair.

The dimension counts in the other commuting results also miss the problem.
Maubach's theorem for two independent commuting LNDs is a theorem on
`C^[3]`, where their common kernel has transcendence degree one and is generated
by a coordinate.[^maubach] In dimension four the commuting-derivations problem
uses **three**, not two, independent LNDs. Derksen--van den Essen--Maubach's
UFD theorem likewise uses `n` commuting independent LNDs on a ring of
transcendence degree `n+1`, and its translation conclusion additionally requires
fiberwise independence.[^dem] Our pair is two-on-four with a
transcendence-degree-two common kernel.

Liu--Sun give a useful warning against extrapolating from commutation: their
Example 2.13 is a UFD with a retract that is the common kernel of two commuting
independent LNDs, but the ring is not a two-variable polynomial extension of the
common kernel.[^liu-sun] Their ambient ring is a hypersurface, not `k^[4]`, and
their example is not a counterexample to the present implication. It does show
that “two commuting LNDs plus a retract” is not a sufficient abstract theorem.

## Cancellation, invariant coordinates, and properness

The ordinary slice theorem itself says only

\[
C[s]\cong k^{[4]}.
\]

Upgrading this to `C congruent k^[3]` is precisely the extra cancellation step.
Derksen--van den Essen--van Rossum formulate this distinction explicitly in
their Proposition 2.1, Corollary 2.2, and Problem 2.3.[^cancellation-report]

There is a sharp closure if an **ambient coordinate invariant** is known.
Bhatwadekar--Gupta--Lokhande, Theorem 3.5, prove that a locally nilpotent
`k[T]`-derivation of `k[T,X,Y,Z]` whose kernel is regular has kernel
`k[T]^[2]`.[^bgl] An `E`-slice makes `ker E` regular, so an ambient coordinate
fixed by `E` would settle the case. Although `E` fixes `f` and `g`, the fact that
`ker delta=k[f,g] congruent k^[2]` does not by the cited results make either one
an ambient coordinate after adjoining `w`. Treating it as one would assume the
coordinate step being sought.

Geometrically, an `E`-slice makes the action a globally trivial `Ga`-bundle over
`Spec(C)`, hence proper. “Translation on affine four-space” in the relevant
literature is stronger: it also identifies the quotient with affine three-space.
Kaliman proves that every proper `Ga`-action on `C^4` **preserving a coordinate**
is a translation.[^kaliman] Dubouloz--Finston--Jaradat prove the same conclusion
for proper **triangulable** actions.[^dfj] Neither preservation of a coordinate
nor triangulability is known for the extensions considered here.

Conversely, failure of a polynomial slice does not by itself prove that an action
is nonproper. A proper free action may initially have a nonaffine geometric
quotient; the cited triangular theorem expends substantial work to prove the
quotient affine under its additional hypotheses. The project's fixed-point-free
negative families should therefore be described as “free with no global
polynomial slice,” not as nonproper, unless properness is checked separately.

## Comparison with the exact Freudenburg families

The project fixes

\[
f=xz-y^2,
\qquad g=zf^2+2x^2yf+x^5,
\qquad r=-x^3-fy,
\qquad \Delta=\operatorname{Jac}(f,g,\mathord\cdot),
\]

with

\[
\ker\Delta=k[f,g],\qquad \Delta r=fg,
\qquad r^2+f^3=xg.
\]

Freudenburg's 1997 local-slice paper and 1998 homogeneous-action paper are the
primary sources for this construction and its rank-three behavior.[^freudenburg-local][^freudenburg-homogeneous]
Dasgupta--Gaifullin reproduce the same derivation in section 5 and prove, in
Theorem 4.5, that every LND on `k^[3]` commuting with an irreducible rank-three
LND is equivalent to it.[^dg] That theorem concerns derivations **on `R`**. It
does not classify `Delta+a partial_w` on `R[w]`, and `T=partial_w` restricts to
zero on `R`.

Sun--Liu study the image of rank-three homogeneous LNDs and prove a
Mathieu--Zhao-subspace result; their sections 4--5 explicitly use local-slice and
Fibonacci-type derivations.[^sun-liu] That is the closest primary paper found to
an image calculation for this `Delta`, but its stated result is not the project's
intersection formula

\[
\Delta(R)\cap k[x,f,g]
=L\bigl((f,g-x^5)k[x,f,g]+x^2k[f,g]\bigr),
\quad
L(P)=gP+2(xg-f^3)P_x.                       \tag{6}
\]

The audit searched the following two project statements at statement level:

1. For every `a in C=k[x,f,g]`,
   \(\Delta+a\partial_w\) has a slice exactly when
   \(a=c+\Delta H\) for `c in k*`, `H in R`; equivalently, using (6), exactly
   when \(a=c+L(P)\) with
   \(P\in(f,g-x^5)C+x^2k[f,g]\).
2. If `c in k*`, `H in R`, and `f` divides `Delta H`, then
   \(\Delta+(c+\Delta H/f)\partial_w\) has a polynomial slice exactly when
   the residue `H mod f`, written as `h(x)`, belongs to `k[x^5]`. After a
   polynomial shear this contains the family
   \(\Delta+(c+2r h'(x))\partial_w\).

No matching classification was located. Exact-expression searches for
`Delta(r)=fg`, `r^2+f^3=xg`, `2r h'(x)`, `c+Delta H/f`, and the defining pair
`xz-y^2`, `zf^2+2x^2yf+x^5` returned the original local-slice construction and
the later rank/image papers above, but not a four-variable slice theorem.

Freudenburg's later “General Extensions” section is especially important to
separate from these statements. It assumes the added coefficient lies in
`A=ker D`; Proposition 7.1 also assumes
\(aA\cap I_n=aI_n\) for all image ideals, and describes the new kernel and
degree modules.[^freudenburg-extension] Its Extension Theorem 7.6 further
assumes a fundamental pair and `a in A_0`. It is not an arbitrary-coefficient
slice criterion and does not imply (6) or either displayed classification.

A current nearby preprint by Cid associates a semisimple `G_m`-action to a
slice LND. Its Section 5 standing hypotheses and Theorem 5.4 give the general
equivalence between linearizability of that associated action and conjugacy
of the LND to a coordinate partial.[^cid] Remark 5.5 says the criterion applies
in particular to nice LNDs; niceness is not an additional hypothesis of the
displayed theorem. The missing step here is proving linearizability, not
proving niceness. The criterion therefore does not close the extension case.
The displayed coordinates are in fact not nice, since `Delta^2(x)=2f^2g`
is nonzero, but that observation is not a reason to reject Theorem 5.4.

The source has a version-date ambiguity: its arXiv header identifies version 1
as April 3, 2026, while the rendered manuscript prints August 24, 2026.
This audit records both. Theorem 6.1 also contains an apparent sign typo:
it defines `s'=s+a` but writes `exp(-aD)(s)=s-a=s'`; that separate formula
is not used here. None of these observations changes the scope of Theorem 5.4.

## Claim-status recommendation

The literature checked here does not displace the project's exact `C=k[x,f,g]`
classification or its one-denominator family. Those results should nevertheless
remain labelled **internally proved / originality unresolved**, not novel. Before
any originality language, the next audit should obtain specialist review and
search forward and backward citations of Freudenburg's 1997/1998 papers,
Sun--Liu 2021, Freudenburg's General Extensions paper, and
Dasgupta--Gaifullin 2025 in MathSciNet/zbMATH and full-text databases.

For coefficients outside the proved families, the exact mathematical gap is not
“show that the two LNDs commute.” It is one of the following genuinely stronger
steps:

* prove from (1) that some slice has constant nonzero `partial_w` derivative;
* prove that the induced `d` in (3) has a slice;
* find an ambient coordinate in `ker E`; or
* construct a higher-`w` slice showing that the gauge criterion fails.

None of the audited primary theorems provides one of these steps.

## Access record and primary sources

Full texts inspected: Freudenburg 1997 (Osaka institutional version of record),
Freudenburg 2024/arXiv:2108.12021, Maubach 2003 (author PDF),
Derksen--van den Essen--Maubach (arXiv:0806.2038), Bavula
(arXiv:math/0604083 and journal metadata), Derksen--van den Essen--van Rossum
(author-uploaded report), Bhatwadekar--Gupta--Lokhande (arXiv:1501.01438),
Liu--Sun 2022 (Czech Academy PDF), Dasgupta--Gaifullin
(arXiv:2306.00510 / published 2025 version), Kaliman 2018 (publisher PDF),
Dubouloz--Finston--Jaradat (arXiv:1303.1032), and Cid
(arXiv:2604.03471v1). Sun--Liu 2021 was inspected through the publisher's full
HTML; El Kahoui 2005 was checked at the publisher statement/metadata level and
through the precise lemma cited by the later commuting-derivations papers.

[^freudenburg-extension]: Gene Freudenburg, [“Actions of \(SL_2(k)\) on Affine \(k\)-Domains and Fundamental Pairs,” Lemma 2.2, section 7.1, Proposition 7.1, and Theorem 7.6](https://arxiv.org/pdf/2108.12021), *Transformation Groups* 29 (2024), 959--1003. Lemma 2.2 is on PDF pp. 3--4; General Extensions is on printed pp. 22--26.
[^miyanishi-modern]: Freudenburg, [ibid., Theorem 2.4(a), printed p. 4](https://arxiv.org/pdf/2108.12021), states the characteristic-zero form of Miyanishi's kernel theorem for a nonzero LND on `k^[3]`.
[^bavula]: V. V. Bavula, [“Generators and Defining Relations for Ring of Invariants of Commuting Locally Nilpotent Derivations or Automorphisms”](https://arxiv.org/pdf/math/0604083), *Journal of the London Mathematical Society* 76 (2007), 148--164, [doi:10.1112/jlms/jdm036](https://doi.org/10.1112/jlms/jdm036). The hypothesis `delta_i(x_j)=delta_ij` is stated in the abstract and developed in Theorem 2.3.
[^elkahoui]: M'hammed El Kahoui, [“UFDs with Commuting Linearly Independent Locally Nilpotent Derivations,” Lemma 2.1](https://doi.org/10.1016/j.jalgebra.2005.01.048), *Journal of Algebra* 289 (2005), 446--452. The paper's global hypotheses are affine UFD, no nonconstant units, characteristic zero; its simultaneous polynomial presentation uses the dual-slice relations, not merely separate slices.
[^maubach]: Stefan Maubach, [“The Commuting Derivations Conjecture,” Lemma 3.3 and Theorem 3.6](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), *Journal of Pure and Applied Algebra* 179 (2003), 159--168, [doi:10.1016/S0022-4049(02)00198-6](https://doi.org/10.1016/S0022-4049(02)00198-6). Theorem 3.6 is printed on p. 4.
[^dem]: Harm Derksen, Arno van den Essen, and Stefan Maubach, [“A Commuting Derivations Theorem on UFDs,” Theorem 2.1 and Propositions 3.1--3.3](https://arxiv.org/pdf/0806.2038). Theorem 2.1 is on printed p. 3; Proposition 3.3 is on printed p. 5.
[^liu-sun]: Dayan Liu and Xiaosong Sun, [“Retracts That Are Kernels of Locally Nilpotent Derivations,” Problem 2.11, Example 2.13, and Proposition 2.14](https://cmj.math.cas.cz/full/72/1/cmj72_1_11.pdf), *Czechoslovak Mathematical Journal* 72 (2022), 191--199, [doi:10.21136/CMJ.2021.0388-20](https://doi.org/10.21136/CMJ.2021.0388-20). The commuting example is on printed pp. 196--197.
[^cancellation-report]: Harm Derksen, Arno van den Essen, and Peter van Rossum, [“The Cancellation Problem in Dimension Four,” Proposition 2.1, Corollary 2.2, Problem 2.3, and Theorem 4.4](https://www.researchgate.net/publication/228571174_The_cancellation_problem_in_dimension_four), University of Nijmegen Report 0022 (2000). The first three items are on printed p. 2; Theorem 4.4 is on printed p. 8. The linked copy was uploaded by an author.
[^bgl]: S. M. Bhatwadekar, Neena Gupta, and Swapnil A. Lokhande, [“Some K-Theoretic Properties of the Kernel of a Locally Nilpotent Derivation on \(k[X_1,\ldots,X_4]\),” Theorem 3.5](https://arxiv.org/pdf/1501.01438), *Transactions of the American Mathematical Society* 369 (2017), 341--363, [doi:10.1090/tran/6649](https://doi.org/10.1090/tran/6649). The theorem is on PDF p. 11 / printed p. 350.
[^kaliman]: Shulim Kaliman, [“Proper \(G_a\)-Actions on \(\mathbb C^4\) Preserving a Coordinate,” Theorem 0.1](https://msp.org/ant/2018/12-2/ant-v12-n2-p01-s.pdf), *Algebra & Number Theory* 12 (2018), 227--266, [doi:10.2140/ant.2018.12.227](https://doi.org/10.2140/ant.2018.12.227).
[^dfj]: Adrien Dubouloz, David Finston, and Imad Jaradat, [“Proper Triangular \(G_a\)-Actions on \(\mathbb A^4\) Are Translations”](https://arxiv.org/pdf/1303.1032), *Algebra & Number Theory* 8 (2014), 1959--1984, [doi:10.2140/ant.2014.8.1959](https://doi.org/10.2140/ant.2014.8.1959). The affine-four-space conclusion is the main corollary stated in the abstract/introduction.
[^freudenburg-local]: Gene Freudenburg, [“Local Slice Constructions in \(k[X,Y,Z]\)”](https://ir.library.osaka-u.ac.jp/repo/ouka/all/4752/ojm34_04_02.pdf), *Osaka Journal of Mathematics* 34 (1997), 757--767, [doi:10.18910/4752](https://doi.org/10.18910/4752).
[^freudenburg-homogeneous]: Gene Freudenburg, “Actions of \(G_a\) on \(A^3\) Defined by Homogeneous Derivations,” *Journal of Pure and Applied Algebra* 126 (1998), 169--181, [doi:10.1016/S0022-4049(96)00143-0](https://doi.org/10.1016/S0022-4049(96)00143-0).
[^dg]: Nikhilesh Dasgupta and Sergey A. Gaifullin, [“On Locally Nilpotent Derivations of Polynomial Algebra in Three Variables,” Theorem 4.5 and section 5](https://arxiv.org/pdf/2306.00510), *Sbornik: Mathematics* 216 (2025), 456--484, [doi:10.4213/sm10094e](https://doi.org/10.4213/sm10094e).
[^sun-liu]: Xiaosong Sun and Dayan Liu, [“Images of Locally Nilpotent Derivations of Polynomial Algebras in Three Variables,” sections 4--5](https://doi.org/10.1016/j.jalgebra.2020.10.025), *Journal of Algebra* 569 (2021), 401--415.
[^cid]: Luis Cid, [“On Nice \(G_m\)-Actions Arising from Locally Nilpotent Derivations with Slice,” Section 5, Theorem 5.4, and Remark 5.5](https://arxiv.org/html/2604.03471v1), arXiv header: version 1, April 3, 2026; rendered manuscript date: August 24, 2026. Date discrepancy retained rather than resolved by assumption.
