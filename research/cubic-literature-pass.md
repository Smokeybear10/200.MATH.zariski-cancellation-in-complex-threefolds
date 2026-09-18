# Cubic stable coordinates and slices in four variables: bounded literature audit

Subsequent mathematical work is recorded in [the cubic descent proof](../deep-pass-07.md).
It closes the local proof gaps below, but does not change this audit into
evidence of originality. See the separate [post-proof audit](cubic-postproof-literature.md)
for searches directed at the completed statement.

**Field and ambient ring throughout:** \(\mathbb C\), unless a cited result is
stated more generally.

## Outcome

This pass did **not** locate a primary-source theorem saying that every
degree-three stable coordinate, or every degree-three locally nilpotent
derivation (LND) slice, in \(\mathbb C[x_1,x_2,x_3,x_4]\) is a coordinate.
That is a report about the bounded searches and papers inspected below, **not**
a proof that the cubic question is open.  Several superficially close results
have materially narrower hypotheses:

* Kaliman's theorem concerns a polynomial in **three** variables whose general
  fiber is \(\mathbb C^2\), not a polynomial in four variables with
  three-dimensional fibers.[^kaliman]
* Kaliman--Vénéreau--Zaidenberg study actual affine-space
  hypersurface embeddings for polynomials linear in one variable, with extra
  hypotheses; a stable coordinate or an LND slice only supplies a stabilized
  hypersurface and does not supply the required unstabilized embedding.[^kvz]
* Maubach gives an unconditional and very strong theorem for
  \(p(x)y+g(x,z,w)\), but its coefficient depends on a single base variable.[^m]
* Vénéreau gives a genuine four-variable positive theorem for
  polynomials jointly affine-linear in two variables over a two-variable base,
  but an arbitrary cubic need not admit that presentation.[^ven]
* de Bondt's homogeneous quasi-translations correspond to the special
  condition \(D^2(x_i)=0\) on the coordinate functions; they are not arbitrary
  LNDs with a cubic slice.[^db]

There is nevertheless a useful exact reduction.  If a genuine cubic has no
critical point (hence, in particular, if it is a slice or a stable coordinate),
then after a linear change it has the form

\[
 f=a u^2+uP(v_1,v_2,v_3)+H(v_1,v_2,v_3),
 \qquad \deg P\leq2,\quad \deg H\leq3.                 \tag{1}
\]

The two residual branches not covered by the presently proved normal-form
theorems are:

1. \(a=0\), where the coefficient \(P\) is an arbitrary quadratic polynomial
   in **three** variables, rather than a univariate \(p(x)\); and
2. \(a\ne0\), where completing the square reduces the question to
   \(aU^2+K(v_1,v_2,v_3)\) with \(\deg K\leq4\).

This is an exact uncovered normal-form class, not a counterexample and not an
assertion of literature-level openness.

## 1. Logical boundary: slice, stable coordinate, and hyperplane

If \(D(f)=1\) for an LND \(D\) and \(A=\ker D\), the slice theorem gives

\[
 \mathbb C[x_1,x_2,x_3,x_4]=A[f].
\]

Adjoining one variable makes \(f\) a coordinate, since
\(A[T]\simeq A[f]\).  Thus an LND slice is a one-stable coordinate.  It does
**not** follow, without cancellation, that \(A\simeq\mathbb C^{[3]}\), or that
one fiber \(f=0\) is already \(\mathbb A^3\).  This distinction prevents the
direct use of theorems whose hypothesis is an actual embedding
\(V(f)\simeq\mathbb A^3\).

Makar-Limanov, van Rossum, Shpilrain, and Yu make the global connection
explicit: stable-coordinate statements imply corresponding cancellation
statements, while their concrete stable-equivalence theorem is for
two-variable polynomials, not cubic polynomials in four variables.[^mlrsy]
Poloni likewise constructs stable-equivalence counterexamples, but not
hyperplane counterexamples and not a four-variable cubic classification.[^pol]

## 2. Precise positive theorems found

### 2.1 The complete univariate-coefficient family

For

\[
 F=p(x)y+g(x,z,w),\qquad 0\ne p\in\mathbb C[x],
\]

Maubach's Theorem 4.5 proves that if every root specialization
\(g(a,z,w)\) is a coordinate of \(\mathbb C[z,w]\), then \(F\) is a
coordinate over \(\mathbb C[x]\); repeated roots of \(p\) are allowed.
His Corollary 4.2 records the associated four-variable coordinate
classification.[^m]  Dutta--Lahiri's Theorem 1.1 restates the same
root-specialization sufficiency, and their Theorem 3.2 extends the residual
coordinate construction over certain one-dimensional affine base rings.[^dl]

This directly overlaps the positive direction of
[`multiple-root-linear-pass.md`](multiple-root-linear-pass.md).  That note's
compactly supported cohomology argument adds a direct implication from
stable-coordinate (and therefore slice) to the rootwise plane-coordinate
conditions.  The resulting equivalence is useful, but its coordinate
classification must not be advertised as new: its constructive positive
half is Maubach's published theorem.

The special family \(x^m y+g(x,z,w)\), for every \(m\geq1\) and arbitrary
degree \(g\), is therefore closed: slice, stable coordinate, coordinate, and
the plane-coordinate condition on \(g(0,z,w)\) are equivalent.  This result
does not cover (1) when the coefficient of \(u\) is a genuinely
multivariate quadratic \(P(v_1,v_2,v_3)\).

### 2.2 More general linear hypersurfaces, with hypotheses retained

Ghosh--Gupta--Pal consider
\(H=\alpha(X)Y-f(Z,T)-h(X,Z,T)\).  Their Theorem 4.11 gives coordinate,
hyperplane, fibration, and stable-polynomial equivalences under stated
factor/divisibility hypotheses on \(\alpha\) and \(h\).  In the repeated-root
regime, the relevant alternatives include stronger divisibility such as a
square of a prime factor dividing \(h\).  Their broader Theorem 5.29 attaches
Makar-Limanov or Derksen-invariant hypotheses to the stable-polynomial
condition.[^ggp]  Dropping those qualifications would falsely turn their
theorems into the desired general cubic theorem.

For \(\alpha=x^m\), Theorem 4.11 covers, among other cases, \(m=1\) and
appropriate higher divisibility of \(h\).  It is not a theorem about an
arbitrary quadratic coefficient in three base variables.

### 2.3 Actual embeddings linear in one variable

Kaliman--Vénéreau--Zaidenberg study
\(p=f(x,y)u+g(x,y,z)\).  Their hypotheses and conclusions concern simple
birational extensions and, in the relevant cases, the assumption that the
zero hypersurface is actually \(\mathbb C^3\).  They prove strong coordinate
conclusions for specified coefficient classes, including the univariate
coefficient setting, but their introduction also separates those results
from the unrestricted linear-in-one-variable problem.[^kvz]  A slice only
gives a cylinder over its kernel, so this actual-embedding hypothesis cannot
be inserted automatically.

### 2.4 Lower ambient dimension

Kaliman proves that a polynomial on \(\mathbb C^3\) whose general fibers are
\(\mathbb C^2\) is a variable.[^kaliman]  Daigle--Kaliman give a related
locally-nilpotent-derivation/variable result explicitly in
\(k[X,Y,Z]\).[^dk]  Shpilrain--Yu's Proposition 1.1(c), with the arbitrarily
many stabilizers version also recorded by Kuroda, supplies stable-coordinate
descent in three variables.[^sy][^kuroda]  These results correctly close a
branch after a polynomial has been reduced to three variables; they do not
perform that reduction for an arbitrary cubic in four variables.

Blanc--van Santen sharpen the degree-three statement in that lower ambient
dimension: over an algebraically closed field, their Corollary 2.2.3 says that
for \(h\in k[x,y,z]\) of degree at most three, \(h\) is a variable exactly
when \(V(h)\simeq\mathbb A^2\); Proposition 2.3.5 gives explicit affine normal
forms, represented by
\(x+r_2(y,z)+r_3(y,z)\),
\(xy+yr_2(y,z)+z\), and
\(xy^2+y(z^2+az+b)+z\), with the qualifications stated in that
proposition.[^bvs]  This is a classification of affine-plane hypersurfaces in
\(\mathbb A^3\), not affine-threefold hypersurfaces in \(\mathbb A^4\).

### 2.5 A genuine four-variable jointly linear class

Vénéreau's Main Theorem applies to

\[
 p=f_1(x,y)z_1+\cdots+f_k(x,y)z_k+g(x,y),
\]

with the \(f_i\) not all zero.  Over \(\mathbb C\), it makes the following
equivalent: \(V(p)\) is smooth, irreducible, and acyclic;
\(V(p)\simeq\mathbb C^{k+1}\); and \(p\) is a variable.[^ven]  If such a
polynomial is a stable coordinate or an LND slice, its zero fiber is smooth,
irreducible, and acyclic, so this theorem really does prove descent.  With
\(k=2\), it closes every four-variable polynomial jointly affine-linear in two
variables over a two-variable base.  There is no degree restriction in this
positive class.

This is stronger than a univariate coefficient theorem in one direction, but
it still does not cover a general expression \(uP(v_1,v_2,v_3)+H(v)\): the
quadratic coefficient and the residual term need not admit two jointly linear
variables after an affine change.

### 2.6 A current squarefree linear-hypersurface cross-check

Ghosh--Gupta--Pal's companion paper on
\(a(x)y=F(x,z,t)\) proves in Theorem 4.1 that stable polynomiality forces the
specialization at every simple root of \(a\) to define a line; in
characteristic zero those lines are plane coordinates.  Theorem 4.8 gives a
coordinate characterization, while its broader stable-polynomial
equivalences retain ML or Derksen-invariant assumptions in the repeated-root
setting.[^family]  Thus their paper independently closes the squarefree
coefficient case.  Maubach's earlier theorem, combined with the direct
cohomological necessity in the local note, is what closes arbitrary root
multiplicity here; one should not cite Theorem 4.8 alone as doing so.

## 3. Nearby results that do not settle the cubic case

Blanc--Poloni prove that their Vénéreau polynomials

\[
 v_{P,n}=y+x^n\bigl(xz+y(yu+P(z))\bigr)
\]

are one-stable \(k[x]\)-variables (Proposition 2.3).  Their introduction
records that \(v_{z^2,1}\), of total degree four, was still not known to be a
\(k\)-variable.[^bp]  This is a sharp warning against treating stable descent
in four variables as formal, but it is a degree-four boundary example, not a
cubic theorem or counterexample.

de Bondt classifies special homogeneous quasi-translations in dimension five.
The defining identity \(JH\,H=0\) corresponds to a very restricted LND
behavior (the associated derivation squares to zero on the coordinate
generators).  An arbitrary LND possessing a degree-three slice need not have
this form.[^db]

Kuroda's Theorem 1.3 and Corollary 1.5 give a divisibility obstruction for
initial forms of stable invariants and stable coordinates.  In degree at most
three, factor a nonzero initial form as
\(c\prod_{j=1}^r p_j^{e_j}\).  There are at most three distinct nonconstant
irreducible factors.  If every member of a set \(S\) divided that initial
form, unique factorization would place every member of \(S\), up to a scalar,
in \(\mathbb C[p_1,\ldots,p_r]\), whose transcendence degree is at most
\(r\leq3<4\).  Thus Kuroda's required conclusion for a set of transcendence
degree four is automatic in the cubic four-variable case.  Its silence is a
limitation of that obstruction, not evidence for descent.[^kuroda]

Shpilrain--Yu themselves formulate stable-coordinate descent as a conjecture
and prove Proposition 1.1(c) only in dimensions two and three.[^sy]  This is
direct primary-source confirmation of the dimensional boundary; it does not
say whether the total-degree-three subcase in dimension four has since been
settled.

No inspected polynomial-submersion theorem turns critical-point-freeness by
itself into a variable in four variables.  Indeed the local Euler-family
calculation in [`stable-coordinate-pass.md`](stable-coordinate-pass.md)
supplies smooth polynomials whose generic and special fiber Euler
characteristics differ, so submersion alone cannot be the missing implication.

## 4. Independent scope audit of the cubic linear-variable lemma

The elementary lemma in
[`cubic-linear-variable-pass.md`](cubic-linear-variable-pass.md) was checked
independently at the proof level.  Its key implication is:

\[
 h\in\mathbb C[z,w],\quad\deg h\leq3,\quad
 \chi_c(h^{-1}(\lambda))=1\text{ generically}
 \Longrightarrow h\text{ is a coordinate}.             \tag{2}
\]

The reducible generic-fiber branch is sound: infinitely many line factors in
distinct fibers must be parallel, forcing \(h\) to be univariate, and generic
Euler characteristic one then forces degree one.  In the irreducible branch,
Euler characteristic one makes the smooth generic curve \(\mathbb A^1\).
For a polynomial plane embedding of degree at most three, the only potentially
nontriangular degree pair is \((3,2)\).  Normalizing it to
\((at^3+bt,t^2)\) produces either a collision at \(t\) and \(-t\), when
\(b\ne0\), or a nonimmersive point at zero, when \(b=0\).  Thus a linear
coordinate remains, giving the triangular form.

Accordingly, for degree at most three the plane-coordinate condition is
equivalent to a constant directional derivative.  This elementary low-degree
test is a valid bounded lemma.  It does not extend to arbitrary-degree plane
coordinates, and it does not classify every cubic in four variables.  The
general rootwise positive direction collides with Maubach, while the
cohomological necessity argument should be described as a reconstruction or
refinement unless a separate novelty audit establishes more.

## 5. Exact residual normal form for a genuine cubic

Write \(f=f_3+f_2+f_1+f_0\), with \(f_i\) homogeneous.  If \(f\) has no
critical point, then the projective cubic surface
\(V(f_3)\subset\mathbb P^3\) is singular.  Indeed, homogenize the four affine
partials to four quadrics in \(\mathbb P^4\).  Four homogeneous equations in
five projective coordinates have a common zero by the height bound.  If
\(V(f_3)\) were smooth, no common zero could lie at infinity, so a common zero
would dehomogenize to a critical point.  This is the exact argument recorded
in [`stable-coordinate-pass.md`](stable-coordinate-pass.md); it uses only
projective height and Euler's identity.

Choose a singular point of \(V(f_3)\) and send it by a linear change to
\([1:0:0:0]\), using coordinates \([u:v_1:v_2:v_3]\).  Before imposing
singularity, write

\[
 f_3=a_3u^3+u^2L_1(v)+uQ_2(v)+H_3(v).
\]

Vanishing of all first partials at \([1:0]\) gives \(a_3=0\) and
\(L_1=0\).  Collecting the lower-degree terms according to their power of
\(u\) proves (1), where \(P\) and \(H\) are not asserted homogeneous.

If \(a=0\), the polynomial is linear in \(u\), but its coefficient is the
arbitrary quadratic \(P(v_1,v_2,v_3)\).  Neither Maubach's univariate
coefficient theorem nor the cited linear-hypersurface theorems remove this
three-variable coefficient without extra hypotheses.

If \(a\ne0\), the triangular change

\[
 U=u+\frac{P(v)}{2a}
\]

gives

\[
 f=aU^2+K(v),\qquad K=H-\frac{P^2}{4a},\quad\deg K\leq4. \tag{3}
\]

The new expression can have degree four even though the original expression
had degree three.  Kaliman's theorem in \(\mathbb C^{[3]}\), Maubach's
linear-variable theorem, and the affine quadratic-pencil theorem therefore do
not automatically settle (3).  Equations (1)--(3) identify the exact
remaining normal forms after the present reductions; they make no claim that
either branch contains a noncoordinate slice.

## 6. Search log and limits

The following exact search families were run in Google Scholar, arXiv, Crossref,
and zbMATH Open, then followed to primary papers where a plausible hit existed:

* `"stable coordinate" cubic polynomial`
* `"degree three" "stable coordinate"`
* `cubic slice locally nilpotent derivation`
* `Abhyankar Sathaye degree 3 polynomial`
* `cubic hypersurface affine 3-space coordinate polynomial`
* `Blanc Poloni cubic stable coordinate`
* `Kaliman cubic polynomial variable C4`
* `de Bondt stable coordinate cubic`
* `Shpilrain Yu stable coordinate three variables`

The zbMATH Open exact phrase search for `"stable coordinate"` returned a small
set dominated by stable/residual-coordinate and stable-equivalence papers; no
universal cubic four-variable classification was among the inspected records.
Semantic Scholar's public API returned HTTP 429 during this pass, so it is
recorded as **failed access**, not as search coverage.  MathSciNet was not
available without credentials.  No failed interface and no unsuccessful query
is evidence of originality or openness.

The source versions checked were the author/arXiv manuscripts linked below and,
where available, the journal DOI or publisher version.  This was a bounded,
targeted audit, not an exhaustive citation-tree or thesis search.  The
defensible conclusion is only that the exact universal cubic theorem was not
found in the inspected primary literature and that the residual forms (1) and
(3) are not covered by the hypotheses of the theorems actually checked.

A follow-up search targeted the exact form
\(P(v_1,v_2,v_3)u+H(v_1,v_2,v_3)\) with \(P\) quadratic, including
`quadric cone affine modification`, `quadratic coefficient simple birational
extension`, and exact equation searches.  The closest primary sources found
do not provide the desired rank-three coefficient classification.
Kaliman--Zaidenberg develop general affine modifications and topological
preservation criteria, and treat hypersurfaces such as
\(uv=p(x_1,\ldots,x_k)\); they do not state slice/stable-coordinate descent for
an arbitrary center \(V(P,H-\lambda)\) on a quadratic divisor.[^kzmod]
Kaliman--Vénéreau--Zaidenberg's threefold classification instead assumes the
coefficient is \(f(x,y)\), so the modification divisor is cylindrical in its
third base coordinate.[^kvz]  Their Problem 4.1, Theorem 4.2, Corollary 4.3,
and Theorem 3.24 give strong results under that two-variable coefficient
hypothesis, including powers of one irreducible coefficient and the jointly
linear case.  A ternary quadratic of Hessian rank three cannot be made to
depend on only two variables by an affine-linear change, because Hessian rank
is invariant.  Vénéreau closes the separately identifiable jointly-linear
subfamily.

Mulay's 2026 online paper on monolinear hyperplanes treats
\(X^dY+h(X,Z_1,\ldots,Z_n)\), not arbitrary \(P(v)u+H(v)\).  Its main theorem
gives a necessary separable-uniruledness condition for an actual hyperplane;
it does not assert stable-coordinate descent for a rank-three quadratic
coefficient.[^mulay]  No inspected theorem directly classifies the remaining
rank-three quadric-cone or smooth-affine-quadric coefficient cases.  This is
again bounded noncoverage, not an openness or novelty claim.

## 7. Ranked next mathematical routes

1. **Quadratic coefficient in the \(a=0\) branch.**  Classify the quadratic
   \(P(v_1,v_2,v_3)\) by affine rank and analyze the fibers over its critical
   values.  Rank-one/univariate cases return to Maubach, and any presentation
   jointly linear in two variables returns to Vénéreau; the residual
   rank-two and rank-three cases should be recorded only after those overlaps
   are removed.
2. **Quadratic suspension in the \(a\ne0\) branch.**  For
   \(aU^2+K(v)\), use the slice-implied equality of every fiber and compare
   vanishing cycles of the double cover.  Any use of a three-variable variable
   theorem must first prove that \(K\) satisfies its actual fiber hypotheses.
3. **Normal-form coverage audit.**  Compare the two residual branches against
   published classifications of singular cubic surfaces.  This is worthwhile
   only if the affine lower terms and the slice action are tracked; classifying
   \(V(f_3)\) alone cannot prove that \(f\) is a coordinate.

## Primary sources

[^m]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 4.5 and Corollary 4.2; published in *Journal of Pure and Applied Algebra* **179** (2003), 159--168, [DOI 10.1016/S0022-4049(02)00198-6](https://doi.org/10.1016/S0022-4049(02)00198-6).

[^dl]: Amartya Kumar Dutta and Animesh Lahiri, [*On Residual and Stable Coordinates*](https://arxiv.org/pdf/1908.03549), Theorems 1.1 and 3.2; *Journal of Pure and Applied Algebra* **225** (2021), 106707, [DOI 10.1016/j.jpaa.2021.106707](https://doi.org/10.1016/j.jpaa.2021.106707).

[^ggp]: Parnashree Ghosh, Neena Gupta, and Ananya Pal, [*On embedding of linear hypersurfaces*](https://arxiv.org/pdf/2405.07205), arXiv:2405.07205v3 (2024), Theorems 4.11 and 5.29.

[^kvz]: Shulim Kaliman, Stéphane Vénéreau, and Mikhail Zaidenberg, [*Simple birational extensions of the polynomial ring \(\mathbb C^{[3]}\)*](https://arxiv.org/pdf/math/0104204), *Transactions of the American Mathematical Society* **356** (2004), 509--555, [DOI 10.1090/S0002-9947-03-03398-1](https://doi.org/10.1090/S0002-9947-03-03398-1).

[^kaliman]: Shulim Kaliman, [*Polynomials with general \(\mathbb C^2\)-fibers are variables. I*](https://arxiv.org/pdf/math/9912058), *Pacific Journal of Mathematics* **203** (2002), 161--190.

[^dk]: Daniel Daigle and Shulim Kaliman, [*A note on locally nilpotent derivations and variables of \(k[X,Y,Z]\)*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BCC1689DEBE515C48EBA1909E44BBA4E/S0008439500014752a.pdf/div-class-title-a-note-on-locally-nilpotent-derivations-and-variables-of-em-class-italic-k-em-em-class-italic-x-em-em-class-italic-y-em-em-class-italic-z-em-div.pdf), *Canadian Mathematical Bulletin* **52** (2009), 535--543.

[^bvs]: Jérémy Blanc and Immanuel van Santen, [*Automorphisms of the affine 3-space of degree 3*](https://arxiv.org/pdf/1912.02144v2), Corollary 2.2.3 and Proposition 2.3.5.

[^ven]: Stéphane Vénéreau, [*Hyperplanes of the Form \(f_1(x,y)z_1+\cdots+f_k(x,y)z_k+g(x,y)\) Are Variables*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1FDA642B44D2C4591B3D94776038D8AE/S0008439500002939a.pdf/hyperplanes-of-the-form-f1x-yz1-fkx-yzk-gx-y-are-variables.pdf), Main Theorem, *Canadian Mathematical Bulletin* **48** (2005), 622--635, [DOI 10.4153/CMB-2005-058-7](https://doi.org/10.4153/CMB-2005-058-7).

[^family]: Parnashree Ghosh, Neena Gupta, and Ananya Pal, [*On the family of affine threefolds \(a(x)y=F(x,z,t)\)*](https://arxiv.org/pdf/2403.17397v2), Theorems 4.1 and 4.8.

[^sy]: V. Shpilrain and J.-T. Yu, [*Affine varieties with equivalent cylinders*](https://arxiv.org/html/math/0110324), Proposition 1.1(c), *Journal of Algebra* **251** (2002), 295--307.

[^kuroda]: Shigeru Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313), Section 3, arXiv:1304.0313v2.

[^bp]: Jérémy Blanc and Pierre-Marie Poloni, [*Bivariables and Vénéreau polynomials*](https://afst.centre-mersenne.org/item/10.5802/afst.1724.pdf), Proposition 2.3 and Introduction, *Annales de la Faculté des sciences de Toulouse* **31** (2022), 1391--1418, [DOI 10.5802/afst.1724](https://doi.org/10.5802/afst.1724).

[^db]: Michiel de Bondt, [*Homogeneous quasi-translations in dimension 5*](https://arxiv.org/pdf/1501.04845), *Beiträge zur Algebra und Geometrie* (2017), [DOI 10.1007/s13366-017-0358-2](https://doi.org/10.1007/s13366-017-0358-2).

[^mlrsy]: L. Makar-Limanov, P. van Rossum, V. Shpilrain, and J.-T. Yu, [*The Stable Equivalence and Cancellation Problems*](https://ems.press/content/serial-article-files/43009), *Commentarii Mathematici Helvetici* **79** (2004), [DOI 10.1007/s00014-003-0796-3](https://doi.org/10.1007/s00014-003-0796-3).

[^pol]: Pierre-Marie Poloni, [*A note on the stable equivalence problem*](https://hal.science/hal-00851110/document), *Journal of the Mathematical Society of Japan* **67** (2015), 753--769, [DOI 10.2969/jmsj/06720753](https://doi.org/10.2969/jmsj/06720753).

[^kzmod]: Shulim Kaliman and Mikhail Zaidenberg, [*Affine modifications and affine hypersurfaces with a very transitive automorphism group*](https://arxiv.org/pdf/math/9801076), arXiv:math/9801076v2.

[^mulay]: Shashikant Mulay, [*Monolinear hyperplanes*](https://doi.org/10.1016/j.jalgebra.2026.05.043), *Journal of Algebra* **709** (2027), 302--345; published online in 2026. The publisher abstract and Main Theorem were checked for scope.
