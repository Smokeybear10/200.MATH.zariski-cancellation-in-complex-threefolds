# Stable-coordinate pass: exact low-degree gates and a cubic fiber obstruction

**Date:** 2026-09-12  
**Status:** bounded proof-and-primary-source pass; no cancellation or universal
cubic-coordinate theorem is claimed

## 1. Outcome and scope

Let

\[
B=\mathbb C[x_1,x_2,x_3,x_4],\qquad D\in\operatorname{LND}(B),
\qquad D(s)=1,
\]

and put \(K=\ker D\). Three points survived exact checking.

1. The slice theorem makes \(s\) a one-stable coordinate, but descending that
   stable coordinate in full generality is already the dimension-four stable
   coordinate problem and would imply the characteristic-zero cancellation
   statement at issue.
2. A slice of degree at most two is an actual coordinate. For a cubic slice,
   the leading cubic surface must be singular; a simple constant-direction
   condition also suffices to make it a coordinate. No primary theorem
   classifying every cubic stable coordinate or every cubic slice in four
   variables was located in this targeted pass.
3. Smoothness of all fibers is far from enough. The smooth cubic
   \(x+x^2y+z^2+w^3\), and an infinite higher-degree family containing it,
   have fibers with different Euler characteristics. They are therefore
   neither slices nor stable coordinates.

These are filters and exact bounded results, not a solution of affine
three-space cancellation and not novelty claims.

## 2. Why a slice is stably a coordinate, and why descent is the hard step

The slice theorem gives

\[
B=K[s]. \tag{1}
\]

After adjoining one indeterminate \(t\), the \(K\)-automorphism

\[
K[s,t]\longrightarrow K[s,t],\qquad s\longmapsto t,\quad t\longmapsto s
\]

is a \(\mathbb C\)-automorphism of \(B[t]\). Hence \(s\) is a one-stable
coordinate. Equivalently,

\[
K[t]\cong K[s]=B\cong\mathbb C^{[4]}. \tag{2}
\]

This observation does **not** supply an automorphism of \(B\) taking \(s\)
to an ambient variable. Makar-Limanov, van Rossum, Shpilrain, and Yu define
the stable coordinate conjecture in precisely these terms and prove that,
in each fixed dimension, it implies the cancellation conjecture.[^mlvsy]
Their proof explicitly starts with an LND with a slice and uses the same
one-variable stabilization. Thus a theorem saying that every stable
coordinate in \(\mathbb C^{[4]}\) descends would not be an innocuous lemma;
it would close the global cancellation target.

There is also a concrete warning at degree four. Blanc and Poloni consider

\[
v_{P,n}=y+x^n\bigl(xz+y(yu+P(z))\bigr).
\]

Their Proposition 2.3 proves that every \(v_{P,n}\) is a one-stable
\(k[x]\)-variable. Yet for

\[
v_{z^2,1}=y+x^2z+xy^2u+xyz^2, \tag{3}
\]

which has total degree four, their introduction records that it is still
unknown whether it is even a \(k\)-variable of \(k[x,y,z,u]\).[^bp]
This does not decide the cubic case, but it prevents treating one-stable
descent in four variables as routine.

## 3. Exact positive result through degree two

**Proposition 3.1.** Let \(k\) be algebraically closed of characteristic
different from two and let \(f\in k[x_1,\ldots,x_n]\) have degree at most
two. If \(f\) has no critical point, then \(f\) is a coordinate. In
particular, every degree-at-most-two slice of an LND is a coordinate.

**Proof.** Write

\[
f(x)=\tfrac12x^{T}Ax+b^{T}x+c
\]

with \(A\) symmetric. If \(b\in\operatorname{im}A\), then some \(u\)
satisfies \(Au=-b\), and \(u\) is a critical point. Hence
\(b\notin\operatorname{im}A\). Since

\[
\operatorname{im}A=(\ker A)^{\perp},
\]

there is a constant vector \(v\in\ker A\) with \(b^{T}v\ne0\). Therefore

\[
\partial_v f=b^{T}v\in k^*.
\]

Choose a linear coordinate \(u\) in direction \(v\) and complementary
linear coordinates \(z_2,\ldots,z_n\). Then

\[
f=(b^Tv)u+h(z_2,\ldots,z_n),
\]

so replacing \(u\) by \(f\) is a triangular polynomial automorphism.
Finally, if \(D(f)=1\), the gradient of \(f\) cannot vanish anywhere,
because \(D(f)=\sum_iD(x_i)\partial_i f\). \(\square\)

This elementary argument is valid in every dimension. Degree three is the
first degree not covered by this argument for the four-variable slice problem.

## 4. Two exact cubic gates

Write a genuine cubic as a sum of homogeneous pieces

\[
f=f_3+f_2+f_1+f_0.
\]

**Proposition 4.1 (singular leading surface).** If \(f\in
\mathbb C[x_1,x_2,x_3,x_4]\) has no critical point, then the projective
cubic surface \(V(f_3)\subset\mathbb P^3\) is singular.

**Proof.** Homogenize the four partial derivatives to quadrics in
\(\mathbb P^4_{[x_1:\cdots:x_4:h]}\):

\[
F_i=\partial_i f_3+h\,\partial_i f_2+h^2\partial_i f_1.
\]

Four homogeneous equations in \(\mathbb P^4\) have a common projective
zero: otherwise their homogeneous ideal would have radical equal to the
irrelevant ideal of height five, contrary to the height bound at most four.
If \(V(f_3)\) were smooth, the \(F_i\) would have no common zero at
\(h=0\). (Euler's identity makes a common zero of all \(\partial_i f_3\)
automatically lie on \(V(f_3)\).) A common zero must therefore have
\(h\ne0\); dehomogenizing gives a critical point of \(f\), a contradiction.
\(\square\)

Thus any cubic slice must have singular geometry at infinity.

**Proposition 4.2 (constant-direction closure).** If there is a constant
vector \(v\) such that

\[
\partial_v f_3=\partial_v f_2=0,
\qquad \partial_v f_1\ne0, \tag{4}
\]

then \(f\) is a coordinate.

**Proof.** Equation (4) says \(\partial_vf\in\mathbb C^*\). Linear
coordinates with one axis in direction \(v\) put \(f\) in the triangular
form \(cu+h\), exactly as in Proposition 3.1. \(\square\)

Condition (4) is a finite linear-algebra test on the coefficients. It is
only sufficient; the slice equation does not presently force such a
constant direction.

## 5. Why the stable Newton-polytope obstruction is silent for cubics

Kuroda proves that no stable \(\mathbb G_a\)-invariant has an intruder in
its Newton polytope.[^kuroda] His stronger Theorem 1.3, and Corollary 1.5
for stable coordinates, say the following. For every weight \(\omega\) and
every set \(S\subset\mathbb C[x_1,\ldots,x_4]\setminus\{0\}\) with
\(\operatorname{trdeg}_{\mathbb C}\mathbb C[S]=4\), some \(g\in S\) does
not divide the initial form \(f^\omega\).

For total degree at most three, this strongest divisibility condition is
automatic. Factor a nonzero initial form as

\[
f^\omega=c\prod_{j=1}^{r}p_j^{e_j}
\]

with distinct nonconstant irreducibles. Since \(\deg f^\omega\le3\), one
has \(r\le3\). If every \(g\in S\) divided \(f^\omega\), unique
factorization would put every \(g\), up to a scalar, in
\(\mathbb C[p_1,\ldots,p_r]\). This would force

\[
\operatorname{trdeg}_{\mathbb C}\mathbb C[S]\le r\le3,
\]

contrary to the choice of \(S\). The weaker no-intruder statement is even
more visibly automatic: a monomial of total degree at most three cannot be
divisible by all four variables.

Consequently, these important stable-invariant theorems yield no cubic
restriction in four variables. This is a proved limitation of this
particular method, not evidence that cubic stable coordinates always descend.

## 6. A reusable fiber test and an infinite family of exclusions

**Lemma 6.1 (fiber test).** If \(E\in\operatorname{LND}(\mathbb C^{[n]})\)
and \(E(f)=1\), then all fibers of \(f\) are algebraically isomorphic. If
\(f\) is a stable coordinate, then after stabilization every fiber is an
affine space. In either case, the fibers have constant compactly supported
Euler characteristic.

**Proof.** Since \(E^2(f)=0\),

\[
\exp(tE)^*f=f+t,
\]

so the exponential automorphism identifies any two fibers. If an
automorphism of \(\mathbb A^{n+N}\) takes \(f\) to a coordinate, then
\(f^{-1}(\lambda)\times\mathbb A^N\cong\mathbb A^{n+N-1}\). Use
additivity and multiplicativity of \(\chi_c\), together with
\(\chi_c(\mathbb A^N)=1\). \(\square\)

Now fix integers \(m,r,q\ge2\) and set

\[
P_{m,r,q}=x+x^my+z^r+w^q. \tag{5}
\]

**Theorem 6.2.** Every fiber of \(P_{m,r,q}:\mathbb A^4_{\mathbb C}
\to\mathbb A^1_{\mathbb C}\) is smooth, but \(P_{m,r,q}\) is neither a
slice of an LND nor a stable coordinate (after any finite number of added
variables).

**Proof.** If all partial derivatives vanished, \(P_y=x^m\) would give
\(x=0\), while

\[
P_x=1+mx^{m-1}y
\]

would then equal one. Thus the map has no critical point.

Let \(X_\lambda=P_{m,r,q}^{-1}(\lambda)\). On \(x\ne0\), solving for
\(y\) gives

\[
X_\lambda\cap\{x\ne0\}\cong\mathbb G_m\times\mathbb A^2,
\qquad \chi_c=0.
\]

On \(x=0\), the coordinate \(y\) is free and the remaining curve is

\[
C_\lambda=\{z^r+w^q=\lambda\}\subset\mathbb A^2.
\]

For \(\lambda\ne0\), projection to the \(w\)-line is an \(r\)-sheeted
cover away from the \(q\) distinct roots of \(w^q=\lambda\), with one
point over each branch value. Hence

\[
\chi_c(C_\lambda)=r(1-q)+q
=1-(r-1)(q-1). \tag{6}
\]

For \(\lambda=0\), let \(d=\gcd(r,q)\). The curve \(C_0\) is a union of
\(d\) irreducible monomial branches, possibly smooth. Each has normalization \(\mathbb A^1\),
the normalization parametrization is bijective, and distinct branches meet
only at the origin. Equivalently, \(C_0\) is one point plus \(d\) copies of
\(\mathbb A^1\setminus\{0\}\), so

\[
\chi_c(C_0)=1. \tag{7}
\]

Additivity over the \(x\ne0\) and \(x=0\) strata gives

\[
\chi_c(X_0)=1,
\qquad
\chi_c(X_\lambda)=1-(r-1)(q-1)\ne1\quad(\lambda\ne0). \tag{8}
\]

Lemma 6.1 now excludes both a slice and a stable coordinate. \(\square\)

The cubic specialization

\[
p=x+x^2y+z^2+w^3 \tag{9}
\]

is the Koras--Russell polynomial. Formula (8) gives

\[
\chi_c(p^{-1}(0))=1,
\qquad \chi_c(p^{-1}(\lambda))=-1\quad(\lambda\ne0). \tag{10}
\]

Thus this prominent smooth cubic is rigorously not a slice and not a stable
coordinate. This says nothing about a hypothetical *abstract* cylinder
isomorphism for its zero fiber: stable coordinateness is the stronger,
embedded assertion that an ambient automorphism straightens the polynomial.

## 7. Primary-source discrepancy audit for the cubic Euler number

Casals and Murphy, Remark 4.10, use exactly the polynomial (9), identify
the nonzero fibers up to rescaling, and print that those fibers have Euler
characteristic \(3\).[^cm] The direct algebraic stratification above instead
gives \(-1\).

For an independent one-line check, when \(r=2,q=3\), the closed stratum
\(z^2+w^3=\lambda\) for \(\lambda\ne0\) is a smooth projective elliptic
curve with its single point at infinity removed. Its Euler characteristic
is therefore \(0-1=-1\); the complementary
\(\mathbb G_m\times\mathbb A^2\) stratum contributes zero. Ordinary and
compactly supported Euler characteristics agree here. The printed \(3\)
is therefore inconsistent with both calculations and is treated in this
project as an apparent numerical typo, not as theorem input. The only fact
needed for the exclusion is that the zero and nonzero fibers differ, and
the proof of that fact above is independent of the cited remark.

## 8. Exact boundary and next tractable lemma

This pass proves:

- every slice is a one-stable coordinate;
- every slice of degree at most two is an ambient coordinate;
- a cubic slice has singular leading cubic surface;
- the constant-direction condition (4) closes a finite class of cubics;
- Kuroda's stable Newton/divisibility obstruction is automatic for all
  degree-at-most-three polynomials in four variables; and
- the whole family (5), including the cubic (9), is excluded by exact fiber
  invariants despite having no critical points.

It does **not** prove that every cubic slice is a coordinate. The concrete
remaining bounded route is to classify singular leading cubic surfaces
compatible with a critical-point-free polynomial, apply the
constant-direction test first, and compute a fiber invariant on the residual
normal forms. Any residual case must simultaneously have singular geometry
at infinity, constant fiber invariants forced by the slice action, and no
constant direction of the form (4). Passing those tests is necessary, not
sufficient.

The literature search was targeted rather than exhaustive. Exact queries
included “stable coordinate cubic four variables,” “degree three stable
variable polynomial ring,” “slice locally nilpotent derivation cubic
coordinate,” the forward references around Kuroda's stable-invariant
theorem, and the Vénéreau-polynomial literature. No inspected primary
statement classified all cubic stable coordinates or all cubic slices in
four variables. A failed search is not evidence that no such theorem exists;
specialist review and broader citation/database checking remain required.

## Primary sources

[^mlvsy]: Leonid Makar-Limanov, Peter van Rossum, Vladimir Shpilrain, and
Jie-Tai Yu, [“The Stable Equivalence and Cancellation Problems,” definition
before Theorem 1.2 and proof of Theorem 1.2](https://ems.press/content/serial-article-files/43009),
*Commentarii Mathematici Helvetici* 79 (2004), 341--349,
DOI 10.1007/s00014-003-0796-3.

[^bp]: Jérémy Blanc and Pierre-Marie Poloni,
[“Bivariables and Vénéreau Polynomials,” introduction and Proposition 2.3](https://afst.centre-mersenne.org/item/10.5802/afst.1724.pdf),
*Annales de la Faculté des Sciences de Toulouse* 31 (2022), 1391--1418,
DOI 10.5802/afst.1724. The introduction explicitly says that
\(v_{z^2,1}\) is not known even to be a \(k\)-variable, while Proposition
2.3 proves one-stability for every \(v_{P,n}\).

[^kuroda]: Shigeru Kuroda,
[“Initial Forms of Stable Invariants for Additive Group Actions,” Theorems
1.1 and 1.3 and Corollary 1.5](https://arxiv.org/pdf/1304.0313),
*Transformation Groups* 19 (2014), 853--860,
DOI 10.1007/s00031-014-9271-z.

[^cm]: Roger Casals and Emmy Murphy,
[“Legendrian Fronts for Affine Varieties,” Remark 4.10, manuscript p. 58](https://www.math.ucdavis.edu/~casals/LefsFronts_Reviewed.pdf),
*Duke Mathematical Journal* 168 (2019), 225--323,
DOI 10.1215/00127094-2018-0055. The source is cited here to make the
numerical discrepancy transparent; its value \(3\) is not used.
