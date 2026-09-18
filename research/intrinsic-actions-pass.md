# Intrinsic additive actions forced by stable affineness

**Date:** 2026-09-12

**Status:** proved reduction and exact controls; cancellation remains open

## 1. Result of this pass

**Later strengthening:** the [quotient-surface
argument](intrinsic-quotient-surface-pass.md) identifies every intrinsic
nonzero LND kernel with \(\mathbb C^{[2]}\), proves the quotient
surjective and faithfully flat, and shows that a fixed-point-free
intrinsic action already closes cancellation. The
[frame continuation](coordinate-frame-minimization-pass.md) gives
additional low-height closing conditions. The general action-existence
gap remains.

Let

\[
B=\mathbb C[x_1,x_2,x_3,x_4]=K[s],\qquad E=\partial_s,
\]

where \(K\) is a finitely generated domain of transcendence degree three.
Then \(K\) is **not rigid**. Equivalently, there is a nonzero

\[
d\in\operatorname{LND}_{\mathbb C}(K).
\tag{1}
\]

Extending \(d\) by \(d(s)=0\) gives a nonzero LND of \(B\) which commutes
with \(E\). This conclusion is intrinsic: it does not assume that an ambient
coordinate is invariant, or that some coordinate partial already commutes
with \(E\).

This corrects the earlier bridge map, but it is not cancellation. If
\(K\not\cong\mathbb C^{[3]}\), then every nonzero additive action on
\(\operatorname{Spec}K\) must be nonproper and slice-free, and \(K\) cannot
admit a nontrivial \(SL_2(\mathbb C)\)-action. Thus the residual case is not
rigid; rather, it has only additive actions of the difficult kind.

There is also a conditional amplification. The four ambient coordinate
partials yield four commuting leading LNDs on \(K\). If their generic rank is
three, then \(K\cong\mathbb C^{[3]}\). An exact polynomial-coordinate example
below shows that their rank can collapse to one and that every resulting
leading LND can have a proper, nonunit plinth ideal, even when \(K\) already
is \(\mathbb C^{[3]}\). That is the precise obstruction to turning the new
intrinsic action into a solution by filtration alone.

## 2. The one-cylinder rigidity theorem

For an affine domain \(A\) over a characteristic-zero field, rigidity means
\(\operatorname{LND}(A)=\{0\}\). The exact one-variable theorem is

\[
A\text{ rigid}\quad\Longrightarrow\quad
\operatorname{LND}(A[t])
=\{a\partial_t:a\in A\},
\qquad \operatorname{ML}(A[t])=A.
\tag{2}
\]

Crachiola and Makar-Limanov prove the corresponding statement
\(\operatorname{AK}(A[t])=A\) for a finitely generated domain with
\(\operatorname{AK}(A)=A\), using exponential maps and allowing arbitrary
characteristic.[^cml] In characteristic zero, (2) is also stated and proved
in LND-filtration language by Alhajjar.[^alhajjar]

Here is the relevant characteristic-zero proof. Give \(A\) degree zero and
\(t\) degree one. For \(D\in\operatorname{LND}(A[t])\), use a finite
homogeneous generating set to form its highest homogeneous derivation
\(\widehat D\). The usual associated-graded argument shows that
\(\widehat D\) is again locally nilpotent.

Suppose \(D\) moves \(A\). Its filtration degree \(q\) is nonnegative.
Homogeneity gives

\[
\widehat D(t)=h t^{q+1}\quad(h\in A).
\]

For an LND on a characteristic-zero domain, \(u\mid D(u)\) implies
\(D(u)=0\): otherwise the additive LND degree gives

\[
\deg_D(Du)=\deg_D(u)-1
 =\deg_D(Du/u)+\deg_D(u)\geq \deg_D(u),
\]

a contradiction. Hence \(\widehat D(t)=0\). Since \(\widehat D\ne0\), its
restriction to \(A\) has the form

\[
\widehat D(a)=t^q\delta(a),\qquad
0\ne\delta\in\operatorname{Der}(A).
\]

Moreover

\[
\widehat D^{\,n}(a)=t^{nq}\delta^n(a),
\]

so \(\delta\) is locally nilpotent. This contradicts rigidity. Therefore
every LND \(D\) kills \(A\). It is then \(p(t)\partial_t\), and local
nilpotence in a characteristic-zero domain forces \(p(t)\in A\). Conversely,
every \(a\partial_t\) is locally nilpotent. This proves (2). Notice that
\(a\partial_t\) has a slice exactly when \(a\in A^*\).

The phrase “stable rigidity” needs care. The one-added-variable result (2)
is settled, not open. If stable rigidity means the analogous equality after
*every* number of polynomial variables, it is false in general: Dubouloz
constructs a smooth rigid affine complex surface \(S\) for which
\(S\times\mathbb A^2\) is flexible in codimension one and hence has trivial
Makar-Limanov invariant.[^dubouloz-flexible] Thus the exact boundary is one
variable versus two or more, not “known” versus “open.”

## 3. Application to a hypothetical cancellation kernel

The four coordinate partials of \(\mathbb C^{[4]}\) have common kernel
\(\mathbb C\), so

\[
\operatorname{ML}(B)=\mathbb C.
\tag{3}
\]

If \(K\) were rigid, (2) would instead give
\(\operatorname{ML}(K[s])=K\). Equations (3) and \(B=K[s]\) would force
\(K=\mathbb C\), contradicting \(\operatorname{trdeg}_{\mathbb C}K=3\).
This proves (1).

For any such \(d\), its coefficientwise extension

\[
\widetilde d\!\left(\sum_j a_js^j\right)
 =\sum_jd(a_j)s^j
\]

is locally nilpotent and satisfies

\[
[\widetilde d,E]=0,
\qquad
\ker\widetilde d=(\ker d)[s].
\tag{4}
\]

Equation (4) derives a commuting LND, but not a **coordinate** LND.
Nothing in (2) gives \(\ker\widetilde d\cong\mathbb C^{[3]}\), a slice for
\(d\), or properness of its action.

Only the strict containment

\[
\mathbb C\subseteq\operatorname{ML}(K)\subsetneq K
\tag{5}
\]

follows. In particular, \(\operatorname{ML}(K)=\mathbb C\) does not follow
from (3). The logical warning is realized in nearby geometry by the
Koras--Russell cubic: its Makar-Limanov invariant is
\(\mathbb C[x]\), while the invariant of its one-cylinder is
\(\mathbb C\).[^dubouloz-cylinder] That cylinder is not known to be
\(\mathbb A^4\), so this is a warning about the invariant, not a cancellation
counterexample.

## 4. What properness, a slice, or an \(SL_2\)-action would do

Stable affineness gives

\[
K\text{ smooth and factorial},\qquad K^*=\mathbb C^*.
\tag{6}
\]

Gurjar--Masuda--Miyanishi prove that a stably affine threefold admitting a
proper \(\mathbb G_a\)-action is \(\mathbb A^3\).[^gmm] Consequently, in a
hypothetical exotic \(K\), **every** nonzero LND in (1) is nonproper. An LND
with a slice gives a globally trivial translation action and is proper, so
every such LND is also slice-free.

Freudenburg proves the parallel semisimple closure: if an affine threefold
\(X\) satisfies \(X\times\mathbb A^1\cong\mathbb A^4\) and admits a
nontrivial \(SL_2\)-action, then \(X\cong\mathbb A^3\).[^freudenburg]
Therefore an exotic \(K\), if one exists, has nontrivial \(\mathbb G_a\)
actions but no nontrivial \(SL_2\)-action. A single LND cannot be assumed to
extend to an \(\mathfrak{sl}_2\)-triple.

Let \(A_d=\ker d\) and define the plinth ideal

\[
\operatorname{pl}(d)=d(K)\cap A_d.
\]

It is nonzero: choose a local slice \(r\) with \(d^2r=0\ne dr\). In an
exotic case it is proper, because \(1\in\operatorname{pl}(d)\) is exactly
the existence of a slice. Moreover, coefficient comparison in \(s\) gives
the exact cylinder identity

\[
\operatorname{pl}(\widetilde d)
 =\operatorname{pl}(d)[s].
\tag{7}
\]

The kernel \(A_d\) is factorially closed in the UFD \(K\), hence is itself a
UFD. It is also finitely generated. Indeed, with
\(L=\operatorname{Frac}(K)^d\), one has
\[
A_d=K\cap L=B\cap L,
\]
and \(\operatorname{trdeg}_{\mathbb C}L=2\); Zariski's finiteness theorem
applied inside the normal affine ring \(B=\mathbb C^{[4]}\) now applies
directly.[^zariski] But a UFD need not have every ideal principal, and
(6)--(7) do not force the plinth ideal to be a unit. Stable affineness
therefore supplies no hidden slice at this step.

## 5. Four commuting leading actions and a rank-three closure

Return to the coordinate partials \(T_i=\partial_{x_i}\) on \(B\), and use
the \(s\)-degree filtration. Let \(q_i\) be the degree of \(T_i\) as a
filtered derivation. Necessarily \(q_i\geq-1\).

If \(q_i=-1\), then \(T_i(K)=0\) and \(T_i=f\partial_s\) for some \(f\in K\).
Since \(T_i\) has a slice, \(f\) is a unit; by (6), \(f\in\mathbb C^*\).
Thus

\[
K=\ker T_i\cong\mathbb C^{[3]},
\]

and cancellation is finished.

Otherwise \(q_i\geq0\). The argument of Section 2 yields

\[
\widehat T_i=s^{q_i}\delta_i,\qquad
0\ne\delta_i\in\operatorname{LND}(K).
\tag{8}
\]

Because the \(T_i\) commute, their highest commutators vanish. Since every
\(\delta_i\) kills \(s\), (8) gives

\[
[\delta_i,\delta_j]=0.
\tag{9}
\]

If the \(\delta_i\) span a three-dimensional space over
\(\operatorname{Frac}K\), three commuting flows give a \(\mathbb G_a^3\)
action with a three-dimensional orbit on \(X=\operatorname{Spec}K\). The
orbit is open. Orbits of a unipotent algebraic group on an affine variety
are closed, so it is also closed and hence equals irreducible \(X\). Its
stabilizer is finite and therefore trivial in a vector group over
\(\mathbb C\). It follows that

\[
X\cong\mathbb G_a^3\cong\mathbb A^3.
\tag{10}
\]

The closed-orbit input is the Kostant--Rosenlicht theorem; a primary modern
source explicitly recalls it in this form.[^arzhantsev]

Thus every unresolved case has generic leading-symbol rank one or two.

## 6. Exact rank-one and nonunit-plinth control

Neither rank three nor a unit plinth can be inferred from the fact that the
original four \(T_i\) are coordinate translations. Take

\[
K=\mathbb C[a,b,c],\qquad
x_1=a,\quad x_2=b+a^2s,\quad x_3=c+bs,\quad x_4=s.
\tag{11}
\]

This is a polynomial coordinate system, with

\[
a=x_1,\quad s=x_4,\quad b=x_2-x_1^2x_4,\quad
c=x_3-x_2x_4+x_1^2x_4^2.
\]

Its coordinate partials, expressed in \((a,b,c,s)\), are

\[
\begin{aligned}
T_1&=\partial_a-2as\partial_b+2as^2\partial_c,\\
T_2&=\partial_b-s\partial_c,\\
T_3&=\partial_c,\\
T_4&=\partial_s-a^2\partial_b+(a^2s-b)\partial_c.
\end{aligned}
\tag{12}
\]

Now make the invertible linear ambient change

\[
y_1=x_1-x_2-x_3-x_4,\qquad
y_2=x_2,\quad y_3=x_3,\quad y_4=x_4.
\]

The new coordinate partials are

\[
U_1=T_1,\quad U_2=T_1+T_2,\quad
U_3=T_1+T_3,\quad U_4=T_1+T_4.
\]

Every \(U_i\) is a commuting coordinate LND with a slice. Nevertheless, all
four have filtration degree two and the same leading form

\[
\widehat U_i=2as^2\partial_c,\qquad
\delta_i=2a\partial_c.
\tag{13}
\]

Thus their generic rank is one. In addition,

\[
\ker(2a\partial_c)=\mathbb C[a,b],\qquad
\operatorname{pl}(2a\partial_c)=(a),
\]

so none of the four leading LNDs has a slice. This is not an exotic
threefold: \(K\) is already polynomial. That makes it a decisive control:
the desired rank and plinth conclusions do not follow formally from the
ambient coordinate-partial data.

## 7. Exact residual gap

The proved global information is now:

1. \(K\) has a nonzero intrinsic LND, and hence a nontrivial
   \(\mathbb G_a\)-action.
2. Every intrinsic LND extends to one commuting with the original slice
   action on \(B\).
3. A proper intrinsic \(\mathbb G_a\)-action, an intrinsic slice, a
   nontrivial \(SL_2\)-action, a vertical ambient coordinate partial, or
   generic rank three in (8) each closes cancellation.
4. In the unresolved case all intrinsic LNDs are nonproper and slice-free,
   no nontrivial \(SL_2\)-action exists, every plinth ideal is nonzero proper,
   and the four leading coordinate directions have generic rank at most two.

What remains is to upgrade weak, nonproper additive symmetry to one of the
closing conditions. Equations (11)--(13) show why leading-term extraction
alone cannot perform that upgrade. This is a reduction, not a solution or a
novelty claim.

## Primary sources

[^cml]: Anthony J. Crachiola and Leonid G. Makar-Limanov, [“An Algebraic Proof of a Cancellation Theorem for Surfaces,” Theorem 3.1](https://doi.org/10.1016/j.jalgebra.2008.03.037), *Journal of Algebra* 320 (2008), 3113--3119. [Accessible manuscript](https://cds.cern.ch/record/905059/files/cer-002575268.pdf). The theorem is stated for exponential maps; in characteristic zero these correspond to LNDs.
[^alhajjar]: Bachar Alhajjar, [“LND-Filtrations and Semi-Rigid Domains,” Proposition 3.4, PDF p. 6](https://arxiv.org/pdf/1501.00445), arXiv:1501.00445 (2015). It attributes the semi-rigidity result to Makar-Limanov and gives the filtration proof.
[^dubouloz-flexible]: Adrien Dubouloz, [“Flexible Bundles over Rigid Affine Surfaces,” Theorem 1.1 and Section 2.1.2](https://ems.press/content/serial-article-files/43375), *Commentarii Mathematici Helvetici* 90 (2015), 121--137, DOI [10.4171/CMH/348](https://doi.org/10.4171/CMH/348).
[^dubouloz-cylinder]: Adrien Dubouloz, [“The Cylinder over the Koras--Russell Cubic Threefold Has a Trivial Makar-Limanov Invariant”](https://arxiv.org/abs/0807.4085), *Transformation Groups* 14 (2009), 531--539, DOI [10.1007/s00031-009-9051-3](https://doi.org/10.1007/s00031-009-9051-3).
[^gmm]: R. V. Gurjar, Kayo Masuda, and Masayoshi Miyanishi, [*Affine Space Fibrations*, Theorem 4.1.1, printed p. 44](https://oa.tib.eu/renate/bitstreams/2db0f47c-00f9-4195-9c8a-a46722165a99/download), Oberwolfach Preprint OWP-2018-19, DOI [10.14760/OWP-2018-19](https://doi.org/10.14760/OWP-2018-19).
[^freudenburg]: Gene Freudenburg, [“Actions of \(SL_2(k)\) on Affine \(k\)-Domains and Fundamental Pairs,” Theorem 6.6](https://arxiv.org/html/2108.12021#S6.SS3), *Transformation Groups* 29 (2024), 959--1003.
[^zariski]: Oscar Zariski, “Interprétations algébrico-géométriques du quatorzième problème de Hilbert,” *Bulletin des Sciences Mathématiques* 78 (1954), 155--168. Applied to \(B\cap L\) for the transcendence-degree-two subfield \(L=\operatorname{Frac}(K)^d\).
[^arzhantsev]: Ivan Arzhantsev, [“Limit Points and Additive Group Actions,” Introduction](https://arxiv.org/html/2102.11330v1), arXiv:2102.11330v1. It recalls that every orbit of a unipotent group acting on an affine variety is closed.
