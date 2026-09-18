# Quartic polynomials with smooth rationally acyclic fibers

This bounded primary-source pass concerns polynomials
\(G:\mathbb A^3_{\mathbb C}\to\mathbb A^1_{\mathbb C}\) of total
degree at most four, with every fiber smooth and rationally acyclic.
The additional condition \(G(0,y,z)\) is a plane coordinate is kept
separate. No located theorem identifies every such fiber with
\(\mathbb A^2\). This is a report of the checked sources, not a
claim that such a theorem is absent or that the question is new.

Two useful positive reductions emerged: a reduced leading form
eliminates the integral-homology obstruction, and a binomial form in
one variable proves coordinatehood without any degree bound.

## 1. Reduced leading form: an exact topological reduction

Write \(G_d\) for the leading homogeneous part and set

\[
W=\{[x:y:z]\in\mathbb P^2:
\partial_xG_d=\partial_yG_d=\partial_zG_d=0\}.
\]

[Siersma and Tibăr, *Deformations of polynomials, boundary
singularities and monodromy*](https://arxiv.org/pdf/math/0207076),
Definition 2.1 and the equivalence following (3.1), give

\[
G\text{ is FISI}\iff
\dim W\le0\quad\text{and}\quad\dim\operatorname{Sing}G\le0.
\]

FISI means that every projective fiber closure and its section at
infinity have only isolated singularities. If \(G_d\) is reduced,
its projective plane curve has finitely many singularities, so
\(W\) is finite. Smoothness of every affine fiber makes
\(\operatorname{Sing}G\) empty. Thus \(G\) is FISI.

Section 2, equation (2.1), then gives the general fiber the homotopy
type \(\bigvee S^2\), with sphere count
\(b_2=\mu+\lambda\). Rational acyclicity forces zero spheres:
the general fiber is contractible and integrally acyclic. Both
nonnegative totals vanish. The atypical-value description after
(2.2) consequently gives no bifurcation values, so all fibers have
that topology. Equation (2.4) also yields, for \(d=4\),

\[
\sum_{p\in W}(\mu_{p,\mathrm{gen}}+\mu_p^\infty)=27.
\]

This does not identify the fibers algebraically or biholomorphically
with \(\mathbb C^2\).

The hypothesis is reduced, not smooth, leading form. For example,
\(G=x+yz(y-z)(y-2z)\) is an evident quartic coordinate whose
leading projective curve consists of four concurrent lines. Thus
singularities of that reduced boundary are compatible with the
desired conclusion. Conversely, replacing \(G_d\) by its reduced
support before computing \(W\) would be invalid when \(G_d\)
has repeated factors.

Under the original no-critical-point assumption, the remaining
possible torsion issue is therefore confined to nonreduced leading
forms. The algebraic recognition issue remains even in the reduced
case.

## 2. A binomial form gives the stronger algebraic conclusion

The separately audited deduction in
[generic-rational-binomial-pass.md](generic-rational-binomial-pass.md)
proves:

\[
G=f(x,y)z^q+g(x,y),\quad f\ne0,\ q\ge1,
\quad\text{general fiber smooth and rationally acyclic}
\quad\Longrightarrow\quad G\text{ is a coordinate}.
\]

It uses [Kaliman and Zaidenberg, Section 7, Lemmas 7.4–7.6 and
Proposition 7.1](https://arxiv.org/pdf/math/9801076). Choosing a
general level makes the relevant reduced plane divisors intersect
transversely, which supplies a condition that is unavailable at an
arbitrarily selected special rationally acyclic level. This is an
audited deduction from those results, not a claim of novelty or a
verbatim published theorem.

For \(q>1\), nonconstant \(f,g\), the deduction gives simultaneous
base coordinates \((a,b)\) with \(f=p(a)\) and
\(g-\lambda=b\). For \(q=1\), it also makes \(f=p(a)\) after
a base automorphism, but does not make \(g\) a plane coordinate.
No originally designated coordinate is asserted to be preserved.

One useful global application is

\[
G=az^2+B(x,y)z+C(x,y),\qquad a\in\mathbb C^*.
\]

The polynomial substitution \(s=z+B/(2a)\) turns this into
\(as^2+C-B^2/(4a)\), so the deduction applies. The resulting
polynomial need not remain quartic, but the binomial theorem has no
degree bound. For a nonconstant coefficient of \(z^2\), division
by that coefficient is not a global polynomial substitution.

## 3. Cyclic-cover classification: exact useful scope

[Alok Maharana, *Q-homology planes as cyclic covers of
A2*](https://www.jstage.jst.go.jp/article/jmath/61/2/61_2_393/_pdf),
Main Theorem, classifies smooth rational homology planes of the
global form \(z^n-f(x,y)=0\). Lemma 3.1 gives Euler characteristic
one for their smooth branch curve; Lemma 3.2 says that an irreducible
branch curve makes the covering surface \(\mathbb A^2\).

For a generic level of a polynomial, connected total space gives
transitive monodromy on the components of the generic plane fiber.
Equal component Euler characteristics, together with total Euler
characteristic one, force one component. This explains why the
generic-level hypothesis is decisive in the monic pure-power case.

The classification is not a theorem for arbitrary quartic affine
surfaces or for models that become cyclic covers only after
localization. Its global equation and smoothness hypotheses must be
verified before using its list.

## 4. The closest quartic embedding classification assumes more

Tomoaki Ohta treats normal projective quartic closures in two
original papers:

- [*The structure of algebraic embeddings of C2 into C3, normal
  quartic case I*](https://www.i-repository.net/contents/osakacu/sugaku/111F0000002-03803-3.pdf),
  Osaka Journal of Mathematics 38 (2001), 507–532: at least one
  triple point.
- [*Normal quartic case II*](https://ir.library.osaka-u.ac.jp/repo/ouka/all/11353/ojm46_02_563.pdf),
  Osaka Journal of Mathematics 46 (2009), 563–597: no triple points.

Theorem 4 in each paper rectifies an algebraic embedding of
\(\mathbb A^2\) with the specified normal quartic closure. More
precisely, the standing assumption supporting Theorems 1–3 allows
the affine complement to be biholomorphic to \(\mathbb C^2\).
That analytic hypothesis is still much stronger than being
contractible or integrally acyclic. The argument invokes the
classification of compactifications of \(\mathbb C^2\); its
hypothesis cannot simply be replaced by homology data.

In the reduced-leading situation of Section 1, projective closures
have isolated singularities and are normal hypersurfaces. Thus the
normality obstacle is removed there, but the required analytic or
algebraic identification with the plane is not. Ohta's results do not
supply that missing implication as stated.

## 5. Other nearby degree results do not match this problem

[Blanc and van Santen, *Automorphisms of the affine 3-space of
degree 3*](https://arxiv.org/pdf/1912.02144), Proposition 2.3.5,
classifies irreducible degree-at-most-three equations whose quotient
is already a polynomial ring in two variables. It neither extends
the degree to four nor replaces that quotient condition with
rational acyclicity.

[Siersma and Smeltink, *Classification of singularities at infinity
of polynomials of degree 4 in two
variables*](https://pure.tue.nl/ws/files/4356798/461158.pdf), concerns
plane polynomials. It can inform the sections \(G(\gamma,y,z)\),
but does not classify three-variable maps or control how those
sections vary with \(\gamma\).

[Siersma and Tibăr, *Betti Bounds of
Polynomials*](https://webspace.science.uu.nl/~siers101/siersma-tibarMMJ.pdf),
Theorem 1.1, analyzes small top-Betti defect
\(\Delta_{n-1}=(d-1)^n-b_{n-1}\). Our quartic rationally acyclic
fiber has \(\Delta_2=27\), at the opposite end from the small-defect
classification. This is not the 2002 deformation paper cited in
Section 1, despite the similar authors and potentially confusing PDF
filename.

## 6. What the distinguished plane section supplies

If \(G(0,y,z)\) is a coordinate, each surface
\(Y_\lambda=G^{-1}(\lambda)\) contains the principal reduced
curve

\[
Y_\lambda\cap\{x=0\}\simeq\mathbb A^1.
\]

This is useful geometric data. It does not alone verify a global
cyclic-cover presentation, Ohta's biholomorphic-plane assumption, or
FISI. Rectifying \(G(0,y,z)\) by a nonlinear plane automorphism
may increase the total degree of \(G\), so a subsequent quartic
case split must account for that change explicitly.

## 7. Bounded conclusion and nearest precise targets

The checked sources establish the following division of work:

- A global binomial form in one variable already proves absolute
  coordinatehood from the general rationally acyclic fiber.
- Reduced leading form and no affine critical points eliminate
  torsion and give contractible fibers, but do not finish algebraic
  recognition in the checked results.
- Nonreduced leading forms require a separate argument even for
  that topological upgrade.

The nearest unfilled recognition target is therefore a smooth
contractible quartic affine surface with normal projective closure,
arising as a general fiber of a polynomial with no bifurcation
values, possibly with the specified principal affine line. A
primary-source theorem must match those hypotheses before it is
used. The searches for quartic acyclic and contractible surfaces,
normal-quartic embeddings, cyclic covers, and isolated-singularity
criteria were bounded. No statement about the complete literature
or the present open status follows from their outcome.
