# Post-proof collision audit for cubic stable coordinates in four variables

## Exact statement screened

This audit screens the following field- and degree-specific assertion:

> If \(f\in\mathbb C[x_1,x_2,x_3,x_4]\) has total degree at most three and
> becomes a coordinate after adjoining finitely many variables, then \(f\) is
> already a coordinate.

It would imply the same conclusion for every degree-at-most-three LND slice,
because the slice theorem makes a slice a coordinate after one stabilization.
The search also used the geometric phrasings “stably rectifiable cubic
hypersurface” and “cubic embedding \(\mathbb A^3\subset\mathbb A^4\).”  These
phrasings are not logically interchangeable without their stated hypotheses:
an actual hyperplane \(V(f)\simeq\mathbb A^3\), a stable coordinate, and a
single stably trivial fiber are different inputs.

**Bounded result.** No exact published theorem matching the displayed
four-variable stable-coordinate statement was located in the primary sources
inspected below.  This is not evidence that the statement is open or novel.
It means only that the present proof does not collide with a theorem found by
this targeted search.

## 1. What the current proof adds up to

The candidate proof has two independent pieces.

### 1.1 Reduction of any cubic stable coordinate to a quadratic coefficient

Write \(f=f_3+f_2+f_1+f_0\), with homogeneous pieces.  Stability gives a
smooth affine fiber \(X_\lambda=V(f-\lambda)\) with
\(\chi_c(X_\lambda)=1\) for every \(\lambda\).

The new infinity lemma asserts that some
\(p\in\operatorname{Sing}V(f_3)\subset\mathbb P^3\) satisfies \(f_2(p)=0\).
The proof separates two cases.

* If the singular locus is positive-dimensional, its intersection with the
  quadric \(V(f_2)\) is nonempty.  This also includes the case where the
  restriction of \(f_2\) vanishes identically.
* Otherwise the singularities are isolated.  If \(f_2\) were nonzero at all
  of them, the projective closure \(Y_\lambda\subset\mathbb P^4\) would be a
  smooth cubic threefold: the affine part is smooth, and the derivative in the
  homogenizing direction equals \(f_2\) at a singular point of the boundary.
  Direct Chern-class arithmetic gives
  \(\chi(Y_\lambda)=-6\).  For the boundary cubic surface
  \(S=V(f_3)\), smoothing isolated surface singularities gives
  \(\chi(S)=9-\sum_p\mu_p\).  The polar-degree formula
  \[
    \deg(\operatorname{grad}f_3)=2^3-\sum_p\mu_p\ge0
  \]
  gives \(\sum_p\mu_p\le8\).  Hence
  \[
    \chi_c(X_\lambda)=\chi(Y_\lambda)-\chi(S)
      =\sum_p\mu_p-15\le-7,
  \]
  contradicting \(\chi_c(X_\lambda)=1\).  Huh records the required
  isolated-singularity polar formula explicitly in the introduction; the formula
  is attributed there to Dimca--Papadima.[^huh]

After sending \(p\) to \([1:0:0:0]\), with distinguished variable \(u\),
singularity eliminates the \(u^3\) and \(u^2v_i\) terms of \(f_3\), while
\(f_2(p)=0\) eliminates the \(u^2\) term of \(f_2\).  Collecting the remaining
terms gives the exact form

\[
 f=P(v_1,v_2,v_3)u+H(v_1,v_2,v_3),\qquad\deg P\le2.    \tag{1}
\]

This step is more than the earlier observation that \(V(f_3)\) is singular:
the extra condition \(f_2(p)=0\) is what removes the final quadratic power of
\(u\).

### 1.2 Descent for every quadratic coefficient

[quadratic-coefficient-theorem.md](quadratic-coefficient-theorem.md)
classifies (1) by the rank of the quadratic part of \(P\), with its linear
and constant terms accounted for. Constant, coordinate, and rank-one
cases reduce to three-variable stable descent or Maubach's univariate
coefficient theorem.[^sy][^maubach]  Rank two is treated by the smooth
hyperbola and crossing-divisor arguments, with explicit polynomial inverses.
Rank-three smooth quadrics are excluded by rational compactly supported
cohomology, and the rank-three quadric cone is excluded by its integral
\(\mathbb Z/2\) class.  Thus every stable coordinate of the form (1) is a
coordinate.

The implication “cubic stable coordinate \(\Rightarrow\) coordinate” follows
if both pieces are correct.  The literature audit does not verify the internal
topological arguments.  It only checks whether the assembled conclusion or
one of its decisive general subtheorems is already explicitly published.

## 2. Closest primary theorems and their exact boundaries

### Stable coordinates and slices

Shpilrain--Yu formulate stable-coordinate descent and prove their Proposition
1.1(c) only for ambient dimensions two and three.[^sy]  Their dimension-three
argument uses affine-surface cancellation and Kaliman's theorem on
\(\mathbb A^2\)-fibers; it does not contain a degree-bounded four-variable
extension.

Makar-Limanov--van Rossum--Shpilrain--Yu state the general stable-coordinate
conjecture, prove its implication toward cancellation in Theorem 1.2, and
explain the LND-with-slice reduction on printed pp. 347--348.[^mlvsy]  No cubic
four-variable exception theorem appears there.  This is the primary source
that most clearly confirms that “has an LND slice” does not by itself justify
descent in dimension four.

### Cubic and low-degree embeddings

The strongest exact degree-three collision is in one lower ambient dimension.
Ohta proves rectifiability for cubic hypersurface embeddings
\(\mathbb C^2\hookrightarrow\mathbb C^3\); the title and Theorem 1 explicitly
say \(\mathbb C^2\) into \(\mathbb C^3\).[^ohta]  Kishimoto's later account
also records Ohta's nine cubic types in that three-variable setting.[^kish]

Blanc--van Santen give a modern, characteristic-aware classification in the
same ambient dimension.  Corollary 2.2.3 says that for
\(g\in k[x,y,z]\), \(\deg g\le3\), the condition
\(V(g)\simeq\mathbb A^2\) is equivalent to \(g\) being a variable;
Proposition 2.3.5 gives the normal forms.[^bvs]  Their later classification of
degree-at-most-three morphisms \(\mathbb A^3\to\mathbb A^n\) concerns maps
whose inverse images of hyperplanes are affine planes.  Neither result is a
classification of cubic hypersurfaces \(\mathbb A^3\subset\mathbb A^4\).

### Linear-hypersurface families

Kaliman--Vénéreau--Zaidenberg prove rectifiability for specified polynomials
\(a(x,y)u+g(x,y,z)\), including a jointly-linear class, under actual
\(\mathbb A^3\)-hypersurface or smooth/irreducible/acyclic hypotheses.[^kvz]
Maubach proves the full root-specialization coordinate criterion when the
coefficient is univariate.[^maubach]  Ghosh--Gupta--Pal's Theorem 4.11 gives
genuine stable-polynomial descent for their structured linear hypersurfaces,
but retains factor and divisibility hypotheses; in four ambient variables its
coefficient side is univariate.[^ggp]

Vénéreau's Main Theorem closes the class jointly affine-linear in two
variables over a two-variable base: smooth, irreducible, acyclic zero fiber is
equivalent to coordinate there.[^ven]  These papers overlap multiple branches
of the quadratic-coefficient theorem, but none of their statements covers an
arbitrary ternary quadratic coefficient.  In particular, a rank-three ternary
quadratic cannot be made to depend on only two affine-linear coordinates,
because Hessian rank is preserved by affine-linear change.

### The degree-four warning

Blanc--Poloni prove stable-variable results for Vénéreau polynomials and record
the unresolved coordinate status, in that paper, of \(v_{z^2,1}\).[^bp]  That
polynomial has total degree four.  It is a boundary warning against assuming
stable descent, not a collision with the candidate cubic theorem.

## 3. Search record and false-positive controls

The second pass used exact and synonym searches across Google Scholar, arXiv,
Crossref, and public bibliographic indexing, including:

* `"degree three" "Abhyankar-Sathaye"`
* `Abhyankar-Sathaye conjecture cubic polynomial four variables`
* `"degree 3" "stable coordinate" polynomial`
* `"cubic hyperplane" affine space coordinate polynomial`
* `"cubic embedding" "C^3" "C^4" rectifiable`
* `cubic LND slice coordinate four variables`
* `stably rectifiable cubic hypersurface A3 A4`

Plausible hits were opened and checked against their ambient dimension,
coefficient ring, and whether the hypothesis was an actual hyperplane or only
stable polynomiality.  The main false positives were Ohta and
Blanc--van Santen (ambient \(\mathbb A^3\), not \(\mathbb A^4\));
Kaliman--Vénéreau--Zaidenberg and Ghosh--Gupta--Pal (special linear forms);
and projective papers in which “cubic hyperplane section” has no relation to
polynomial coordinates.

An Oberwolfach report surfaced with the internally inconsistent phrase that
stable-coordinate descent is “true for \(n\ge3\)” and “open for \(n>3\).”  It
is not used.  The cited primary Shpilrain--Yu proposition says dimensions two
and three.  Search results from anonymous repositories, AI-generated paper
summaries, or unreviewed claimed resolutions were likewise excluded from the
evidence base.

This was a bounded theorem-collision pass, not a complete citation-tree,
thesis, or foreign-language audit.  An unsuccessful query does not establish
originality.  The appropriate current label is:

\[
 \boxed{\text{proved in the working manuscript, independently checkable,
 but novelty not established.}}
\]

Before any public “new theorem” claim, the infinity lemma and the two
rank-three compact-support obstructions need a clean integrated proof,
independent human reconstruction, a broader second novelty audit, and expert
review.

## Primary sources

[^huh]: June Huh, [*Milnor Numbers of Projective Hypersurfaces with Isolated Singularities*](https://arxiv.org/pdf/1210.2690), version 2, p. 1, displayed polar-degree identity; *Duke Mathematical Journal* **163** (2014), 1525--1548, [DOI 10.1215/00127094-2713700](https://doi.org/10.1215/00127094-2713700).

[^sy]: V. Shpilrain and J.-T. Yu, [*Affine varieties with equivalent cylinders*](https://arxiv.org/pdf/math/0110324), Proposition 1.1(c), *Journal of Algebra* **251** (2002), 295--307.

[^mlvsy]: L. Makar-Limanov, P. van Rossum, V. Shpilrain, and J.-T. Yu, [*The Stable Equivalence and Cancellation Problems*](https://ems.press/content/serial-article-files/43009?nt=1), Theorem 1.2 and pp. 347--348, *Commentarii Mathematici Helvetici* **79** (2004), 341--349, [DOI 10.1007/s00014-003-0796-3](https://doi.org/10.1007/s00014-003-0796-3).

[^ohta]: Tomoaki Ohta, [*The structure of algebraic embeddings of \(\mathbb C^2\) into \(\mathbb C^3\) (the cubic hypersurface case)*](https://doi.org/10.2206/kyushujm.53.67), Theorem 1, *Kyushu Journal of Mathematics* **53** (1999), 67--106.

[^kish]: Takashi Kishimoto, [*Abhyankar--Sathaye embedding problem in dimension three*](https://projecteuclid.org/journals/kyoto-journal-of-mathematics/volume-42/issue-4/Abhyankar-Sathaye-embedding-problem-in-dimension-three/10.1215/kjm/1250283749.full), *Journal of Mathematics of Kyoto University* **42** (2002), 641--669, especially the introduction's scope summary.

[^bvs]: Jérémy Blanc and Immanuel van Santen, [*Automorphisms of the affine 3-space of degree 3*](https://arxiv.org/pdf/1912.02144v2), Corollary 2.2.3 and Proposition 2.3.5.

[^kvz]: Shulim Kaliman, Stéphane Vénéreau, and Mikhail Zaidenberg, [*Simple birational extensions of the polynomial ring \(\mathbb C^{[3]}\)*](https://arxiv.org/pdf/math/0104204), Theorems 3.24 and 4.2, *Transactions of the American Mathematical Society* **356** (2004), 509--555, [DOI 10.1090/S0002-9947-03-03398-1](https://doi.org/10.1090/S0002-9947-03-03398-1).

[^maubach]: Stefan Maubach, [*The Commuting Derivations Conjecture*](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), Theorem 4.5 and Corollary 4.2; *Journal of Pure and Applied Algebra* **179** (2003), 159--168, [DOI 10.1016/S0022-4049(02)00198-6](https://doi.org/10.1016/S0022-4049(02)00198-6).

[^ggp]: Parnashree Ghosh, Neena Gupta, and Ananya Pal, [*On embedding of linear hypersurfaces*](https://arxiv.org/pdf/2405.07205), Theorem 4.11.

[^ven]: Stéphane Vénéreau, [*Hyperplanes of the Form \(f_1(x,y)z_1+\cdots+f_k(x,y)z_k+g(x,y)\) Are Variables*](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1FDA642B44D2C4591B3D94776038D8AE/S0008439500002939a.pdf/hyperplanes-of-the-form-f1x-yz1-fkx-yzk-gx-y-are-variables.pdf), Main Theorem, *Canadian Mathematical Bulletin* **48** (2005), 622--635, [DOI 10.4153/CMB-2005-058-7](https://doi.org/10.4153/CMB-2005-058-7).

[^bp]: Jérémy Blanc and Pierre-Marie Poloni, [*Bivariables and Vénéreau polynomials*](https://afst.centre-mersenne.org/item/10.5802/afst.1724.pdf), Proposition 2.3 and Introduction, *Annales de la Faculté des sciences de Toulouse* **31** (2022), 1391--1418, [DOI 10.5802/afst.1724](https://doi.org/10.5802/afst.1724).
