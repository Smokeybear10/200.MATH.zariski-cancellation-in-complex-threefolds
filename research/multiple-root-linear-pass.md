# Slice and stable-coordinate criteria for a univariate linear coefficient

Let

\[
 B=\mathbb C[x,y,z,w],\qquad
 F=p(x)y+g(x,z,w),\qquad 0\ne p\in\mathbb C[x].
\]

The degrees and the root multiplicities of \(p\) and \(g\) are unrestricted. For each distinct root \(a\) of \(p\), put

\[
 g_a(z,w)=g(a,z,w).
\]

**Theorem.** The following conditions are equivalent:

1. \(F\) is a coordinate of \(B\).
2. \(F\) is a coordinate of \(B\) along with \(x\), that is, a coordinate over \(\mathbb C[x]\).
3. \(F\) becomes a coordinate after adjoining finitely many independent variables.
4. There is a locally nilpotent derivation \(D\) of \(B\) with \(D(F)=1\).
5. Every \(g_a\), for a root \(a\) of \(p\), is a coordinate of \(\mathbb C[z,w]\).

The coordinate equivalence between 1, 2, and 5 is a published result of Maubach. In particular, the sufficiency of the root conditions is not a new claim here.[^1] The compactly supported cohomology argument below shows directly that a stable-coordinate assumption also forces those conditions. The proof uses topology of a generic fiber, not only its Euler characteristic.

If \(p\) is a nonzero constant, the result is immediate: solve polynomially for \(y\), and condition 5 is empty. Assume henceforth that \(p\) has a nonempty distinct root set

\[
 D=\{a_1,\ldots,a_d\},\qquad d\geq1.
\]

## 1. What stability supplies

Suppose \(F\) becomes a coordinate after adjoining \(N\geq0\) variables. For every \(\lambda\in\mathbb C\), its fiber

\[
 X_\lambda=\operatorname{Spec}B/(F-\lambda)
\]

satisfies

\[
 X_\lambda\times\mathbb A^N\simeq\mathbb A^{N+3}.
 \tag{1}
\]

In particular, \(X_\lambda\) is a smooth connected complex threefold, is topologically contractible, and has only constant algebraic units. Smoothness descends from the product, and the product retracts onto \(X_\lambda\). For units, the natural injection of its coordinate ring into the polynomial extension sends a unit to a unit of a polynomial ring over \(\mathbb C\), hence to a nonzero scalar.

All cohomology below has rational coefficients. Poincaré duality on the smooth oriented real six-manifold \(X_\lambda\) gives

\[
 H_c^i(X_\lambda;\mathbb Q)=
 \begin{cases}
 \mathbb Q,&i=6,\\
 0,&i\ne6.
 \end{cases}
 \tag{2}
\]

A slice has the same stable-coordinate consequence. Indeed, if \(A=\ker D\) and \(D(F)=1\), the slice theorem gives \(B=A[F]\). Thus

\[
 B[T]=A[T][F],\qquad A[T]\simeq A[F]=B,
\]

so \(F\) is a coordinate after adjoining one variable. This proves that condition 4 implies condition 3 without invoking cancellation.

## 2. No constant root specialization is possible

Suppose \(g_a\) were a constant \(c_a\) for some root \(a\). Choose \(\lambda\ne c_a\). The fiber \(X_\lambda\) has no point with \(x=a\), so \(x-a\) is an algebraic unit on this affine variety. By (1), it must be a scalar.

But on \(p(x)\ne0\), the equation uniquely determines

\[
 y=\frac{\lambda-g(x,z,w)}{p(x)}.
\]

This identifies the nonempty open subset of \(X_\lambda\) with

\[
 U\simeq(\mathbb A^1\setminus D)\times\mathbb A^2,
 \tag{3}
\]

and its \(x\)-coordinate takes every value outside \(D\). Hence \(x-a\) is not constant, a contradiction. Every \(g_a\) is therefore nonconstant.

Choose a single value \(\lambda\) that is a regular generic value of all the finitely many plane polynomials \(g_a\). Their exceptional value sets are finite.[^2] Then

\[
 C_a=\{g_a(z,w)=\lambda\}
\]

is a nonempty smooth affine curve for each \(a\). Nonemptiness follows because a nonconstant polynomial minus a scalar is not a unit in \(\mathbb C[z,w]\). From now on, write \(X=X_\lambda\).

## 3. The closed strata and their cohomology

The complement of the open set (3) is the disjoint union

\[
 Z=X\setminus U=\coprod_{a\in D}(C_a\times\mathbb A^1_y).
 \tag{4}
\]

Use the reduced closed subset in (4); multiplicities of roots of \(p\) do not change its topology. Since \(\mathbb A^1\setminus D\) has compactly supported cohomology \(\mathbb Q^d\) in degree one and \(\mathbb Q\) in degree two, the Künneth formula gives

\[
 H_c^i(U;\mathbb Q)=
 \begin{cases}
 \mathbb Q^d,&i=5,\\
 \mathbb Q,&i=6,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{5}
\]

The shift is four because the other factor in (3) is \(\mathbb A^2\). The shift for the \(\mathbb A^1\) factor in (4) is two, giving

\[
 H_c^3(Z)=\bigoplus_{a\in D}H_c^1(C_a),\qquad
 H_c^4(Z)=\bigoplus_{a\in D}H_c^2(C_a).
 \tag{6}
\]

These statements use compact supports throughout. They are not statements about ordinary cohomology of the nonproper fibers.

## 4. The exact sequence forces one affine line at every root

For the closed inclusion \(Z\subset X\) and open complement \(U\), compactly supported cohomology has the exact sequence

\[
 \cdots\longrightarrow H_c^i(U)
 \longrightarrow H_c^i(X)
 \longrightarrow H_c^i(Z)
 \longrightarrow H_c^{i+1}(U)
 \longrightarrow\cdots.
 \tag{7}
\]

First use the segment

\[
 H_c^3(X)\longrightarrow H_c^3(Z)\longrightarrow H_c^4(U).
\]

Both outer groups vanish by (2) and (5). Therefore

\[
 \bigoplus_a H_c^1(C_a)=0.
 \tag{8}
\]

Next use

\[
 H_c^4(X)\longrightarrow H_c^4(Z)
 \longrightarrow H_c^5(U)\longrightarrow H_c^5(X).
\]

Again the outside groups vanish, so the middle map is an isomorphism:

\[
 \bigoplus_a H_c^2(C_a)\simeq\mathbb Q^d.
 \tag{9}
\]

For a smooth affine complex curve, \(\dim H_c^2\) is the number of connected components. All \(d\) curves \(C_a\) are nonempty. Equation (9) therefore forces each of them to have exactly one connected component. Such a smooth connected curve is irreducible.

If its smooth projective completion has genus \(\gamma\) and omits \(n\geq1\) points, then

\[
 \dim H_c^1(C_a)=2\gamma+n-1.
\]

Equation (8) forces \(\gamma=0\) and \(n=1\). Hence every \(C_a\) is isomorphic to \(\mathbb A^1\). The value \(\lambda\) was chosen regular, so \(g_a-\lambda\) is reduced and defines this irreducible curve without a hidden power. The Abhyankar–Moh–Suzuki embedding theorem now makes \(g_a-\lambda\), and therefore \(g_a\), a plane coordinate.[^2] This proves condition 3 implies condition 5.

The argument prevents two different failures from cancelling numerically: (8) separately rules out genus and extra punctures, while (9) separately counts components. Their alternating sum would only give

\[
 \sum_a\chi_c(C_a)=d,
\]

which by itself does not force each summand to be one.

## 5. Published sufficiency and completion of the equivalences

Maubach's Theorem 4.5 applies to a polynomial linear in one variable whose coefficient is a nonzero univariate polynomial: if every root specialization of the remaining term is a coordinate, the whole polynomial is a coordinate over \(\mathbb C[x]\). It explicitly permits repeated roots. Applying it here proves 5 implies 2.[^1]

For a modern independently stated version, Dutta and Lahiri reproduce this result as Theorem 1.1 of *On Residual and Stable Coordinates*, specifying that the resulting polynomial is a coordinate along with the base variable.[^3]

A coordinate over \(\mathbb C[x]\) is an ordinary coordinate, and an ordinary coordinate is both stably a coordinate and the slice of a conjugate of a coordinate partial derivative. Together with Sections 1–4, this proves all five equivalences.

The use of Maubach's sufficiency does not assume an unresolved cancellation conjecture in dimension three. His general-dimensional discussion contains conditional statements, but Theorem 4.5 is the unconditional sufficiency theorem being used here. His four-variable Corollary 4.2 also records the coordinate classification directly.[^1]

## 6. How this sharpens the single-root and cubic cases

The theorem includes \(p=x^m\), so the arbitrary-degree single-root coordinate criterion in [the cubic appendix](cubic-linear-variable-pass.md) is contained in the published coordinate classification. That appendix still supplies a useful elementary degree-three necessity argument and an explicit truncated polynomial inverse in its positive cases. No novelty is asserted for their coordinate criterion.

If every \(g_a\) has degree at most three, the root conditions can be tested by finite linear algebra: for each \(a\), solve

\[
 \alpha_a\frac{\partial g_a}{\partial z}
 +\beta_a\frac{\partial g_a}{\partial w}=1
 \qquad(\alpha_a,\beta_a\in\mathbb C).
\]

The elementary cubic lemma proves that solvability is equivalent to being a plane coordinate. The chosen directions may differ from root to root. Maubach's theorem joins these rootwise conditions; it does not require one direction to work at every root.

## 7. Scope

This settles the slice and stable-coordinate problem for the specified family \(p(x)y+g(x,z,w)\), with any nonzero univariate \(p\). It does not show that an arbitrary polynomial slice in four variables can be transformed into this form.

The choice of a generic fiber is essential to the necessity proof: it makes all plane strata smooth simultaneously. An abstract cylinder isomorphism for only the zero fiber does not give generic fibers with the same topology, and singular plane strata may have the compactly supported cohomology of a line without being an embedded affine line. Thus this proof does not resolve the general cancellation problem or the abstract cylinder status of a Koras–Russell zero fiber.

## 8. Corollary for rank-deficient quadratic pencils

Consider

\[
 F(x,v)=v^TA(x)v+b(x)^Tv+c(x),\qquad v=(y,z,w)^T,
\]

where \(A(x)\) is symmetric with entries in \(\mathbb C[x]\), and suppose

\[
 \det A(x)\equiv0.
\]

Then every stable coordinate \(F\) of this form is an ordinary coordinate. Consequently every LND slice of this form is an ordinary coordinate too. For this rank-deficient corollary, \(A\) need not be affine in \(x\).

Indeed, the kernel of \(A\) over \(\mathbb C(x)\) contains a nonzero vector. Clear its denominators and divide its polynomial entries by their greatest common divisor to get

\[
 n(x)\in\mathbb C[x]^3,\qquad A(x)n(x)=0,
 \qquad (n_1,n_2,n_3)=\mathbb C[x].
\]

The last equality is the unimodularity condition, not just pointwise nonvanishing over the fraction field. Over the PID \(\mathbb C[x]\), the Euclidean algorithm completes \(n\) to the first column of a matrix

\[
 M(x)\in\mathrm{GL}_3(\mathbb C[x]).
\]

The substitution \(v=M(x)(Y,Z,W)^T\) is a polynomial automorphism fixing \(x\). Since \(A\) is symmetric, the first row and first column of \(M^TAM\) are both zero. Thus the transformed polynomial is

\[
 F=p(x)Y+G(x,Z,W),\qquad p(x)=b(x)^Tn(x).
 \tag{10}
\]

If \(p\ne0\), the theorem proved above applies directly, including the case of a nonzero constant \(p\). In particular, stability implies that (10), and hence the original \(F\), is a coordinate. No assumption about a constant common kernel of \(A(x)\) is required.

If \(p=0\), the polynomial belongs to \(\mathbb C[x,Z,W]\) and is independent of \(Y\). Stability in four variables then makes it a stable coordinate of this three-variable ring. The known stable-coordinate theorem over \(\mathbb C\) in three variables says that it is already a coordinate there, hence also in four variables.[^4] This is an external low-dimensional theorem, not an inference from the unresolved four-variable cancellation problem.

Combining this result with [the generic-rank-three affine-pencil theorem](affine-quadratic-pencil-pass.md) proves:

\[
 \boxed{A(x)=A_0+xA_1\text{ symmetric }3\times3:
 \quad F\text{ is a slice}
 \iff F\text{ is stably a coordinate}
 \iff F\text{ is a coordinate}.}
\]

For generic rank three, the other appendix gives the explicit criterion of no critical point and nonzero constant determinant. For lower rank, (10) reduces the nonzero-coefficient branch to the rootwise plane tests; its zero-coefficient branch uses the cited three-variable theorem. This does not give a degree reduction placing every cubic in this pencil family.

## Sources

[^1]: Stefan Maubach, [*The Commuting Derivations Conjecture*, author manuscript](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf), October 5, 2001, Theorem 4.5 and Corollary 4.2, manuscript p. 6. Published as [“The commuting derivations conjecture”](https://doi.org/10.1016/S0022-4049(02)00198-6), *Journal of Pure and Applied Algebra* **179** (2003), 159–168. Used for the rootwise coordinate sufficiency and its existing coordinate classification, not as attribution for the compact-cohomology derivation above.

[^2]: Nguyen Van Chau, [“Polynomial maps of the complex plane with the branched value sets isomorphic to the complex line”](https://math.ac.vn/uploads/files/0202197.pdf), *Acta Mathematica Vietnamica* **27** (2002), 197–202, Section 2 and Lemma 1, printed pp. 198–199. Used for finiteness of the exceptional-value set and the stated affine-line rectification consequence of Abhyankar–Moh–Suzuki.

[^3]: Amartya Kumar Dutta and Animesh Lahiri, [*On Residual and Stable Coordinates*](https://arxiv.org/html/1908.03549), Theorem 1.1; published in [*Journal of Pure and Applied Algebra*](https://doi.org/10.1016/j.jpaa.2021.106707) **225** (2021), article 106707. Used to cross-check the exact hypotheses and conclusion of Maubach's sufficiency theorem.

[^4]: V. Shpilrain and J.-T. Yu, [*Affine varieties with equivalent cylinders*](https://arxiv.org/html/math/0110324), Proposition 1.1(c) and its proof; published in *Journal of Algebra* **251** (2002), 295–307. Shigeru Kuroda, [*Initial forms of stable invariants for additive group actions*](https://arxiv.org/pdf/1304.0313), arXiv:1304.0313v2, Section 3, p. 7, explicitly records the version for arbitrarily many stabilizing variables. Used only for the zero-coefficient, three-variable branch of the corollary.
