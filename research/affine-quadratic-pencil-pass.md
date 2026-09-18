# Stable coordinates in an affine quadratic pencil

The following argument settles a restricted family in four variables. It does
not show that an arbitrary slice polynomial belongs to this family. The
classification is a working theorem with an explicit inverse in its positive
case; novelty and expert review are not established.

## Statement

Work over the complex numbers. Write \(v=(y,z,w)^T\), and let

\[
 F(x,v)=v^T A(x)v+b(x)^T v+c(x),\qquad A(x)=A_0+xA_1,
\]

where \(A_0,A_1\) are symmetric \(3\times3\) complex matrices,

\[
 b\in\mathbb C[x]^3,\quad c\in\mathbb C[x],\quad
 \det A(x)\not\equiv0.
\]

**Theorem.** The following are equivalent:

1. \(F\) is a polynomial coordinate of \(\mathbb A^4\).
2. \(F\) is a coordinate after adjoining finitely many independent variables.
3. \(F\) is a slice of a locally nilpotent derivation of
   \(\mathbb C[x,y,z,w]\).
4. \(F\) has no critical point and \(\det A(x)\) is a nonzero constant.

The degrees of \(b,c\) are unrestricted. For a polynomial of total degree at
most three, the degree bounds would additionally be \(\deg b\le2\) and
\(\deg c\le3\). The assumption that \(A\) is affine in \(x\), and the assumption
that its generic rank is three, are essential to the proof below.

## Necessary geometry of a stable coordinate

If \(F\) is a stable coordinate, each fiber \(F^{-1}(\lambda)\) becomes affine
space after multiplication by an affine space. It is smooth and has compactly
supported Euler characteristic one, since

\[
 \chi_c(Y\times\mathbb A^n)=\chi_c(Y),\qquad
 \chi_c(\mathbb A^n)=1.
\]

In particular, the gradient of \(F\) never vanishes. A slice has the same
properties: the slice theorem writes the ambient ring as \(K[F]\), so its
fibers are copies of \(\operatorname{Spec}K\), whose cylinder is \(\mathbb A^4\).
It is also a stable coordinate, by adjoining a variable and exchanging the
two polynomial extensions of \(K\).

We use additivity and integration of compactly supported Euler characteristic
under algebraic maps. The integration formula applies without a properness
assumption; it is the constructible-function pushforward formula, not the
proper base-change assertion for ordinary cohomology.[^1]

## Excluding a nonconstant determinant

Suppose that \(F\) has no critical point and that \(\det A\) has a nonempty
root set \(D\subset\mathbb C\). Set \(d=|D|\ge1\) and

\[
 U=\mathbb A^1\setminus D,\qquad
 h(x)=c(x)-\tfrac14 b(x)^TA(x)^{-1}b(x)\in\mathbb C(x).
\]

Completing the square over \(U\) gives

\[
 F=\left(v+\tfrac12A^{-1}b\right)^T
       A\left(v+\tfrac12A^{-1}b\right)+h(x).
\]

At the center \(v=-A^{-1}b/2\), the three \(v\)-derivatives vanish and the
\(x\)-derivative equals \(h'(x)\). Thus \(h'\) has no zero on \(U\), and \(h\)
cannot be constant. Let \(N\ge1\) be the degree of the rational map

\[
 h:\mathbb P^1\longrightarrow\mathbb P^1.
\]

Choose \(\lambda\in\mathbb C\) outside finitely many values: the branch values
of \(h\), the values of \(h\) at \(D\cup\{\infty\}\) when finite, and the
exceptional values of the finitely many quadrics over \(D\). Then \(h=\lambda\)
has exactly \(N\) solutions in \(U\).

A nondegenerate quadratic form in three complex variables has Euler
characteristic two on a nonzero fiber and one on its zero fiber. One direct
calculation uses \(uv+w^2=t\): the locus \(u\ne0\) has Euler characteristic zero;
over \(u=0\), there are two affine lines if \(t\ne0\) and one if \(t=0\).
Consequently,

\[
 \chi_c\bigl(F^{-1}(\lambda)\cap\{x\in U\}\bigr)
 =2\chi_c(U)-N=2(1-d)-N. \tag{1}
\]

We next bound the contribution over each \(a\in D\). Denote by \(A_a,b_a\) the
specializations at \(a\), and let \(r=\operatorname{rank}A_a\le2\).

If \(b_a\) is not in the image of \(A_a\), it is nonzero on the radical of the
quadratic form. A linear radical variable can be eliminated, so every fiber
over \(a\) is \(\mathbb A^2\), with Euler characteristic one.

If \(b_a\in\operatorname{im}A_a\), translation removes its linear term. For
generic \(\lambda\), the resulting quadric contributes as follows:

| Rank \(r\) | Generic fiber | \(\chi_c\) |
|---|---|---:|
| 2 | \(\mathbb G_m\times\mathbb A^1\) | 0 |
| 1 | Two disjoint copies of \(\mathbb A^2\) | 2 |
| 0 | Empty | 0 |

The rank-one case with \(b_a\in\operatorname{im}A_a\) is incompatible with
critical-point-freeness and generic rank three. Indeed, the equations
\(\partial F/\partial v=0\) at
\(x=a\) define an affine plane \(v_0+\ker A_a\). On that plane,
\(\partial F/\partial x\) is a polynomial without zeros, and hence a nonzero
constant. Its quadratic part must vanish, which gives

\[
 u^TA_1u=0\quad\text{for all }u\in\ker A_a.
\]

Polarization shows that the restriction of the bilinear form \(A_1\) to that
two-dimensional kernel is zero. In a constant basis we therefore have

\[
 A_a=\begin{pmatrix}\alpha&0&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
 A_1=\begin{pmatrix}q&r&s\\r&0&0\\s&0&0\end{pmatrix},\quad\alpha\ne0.
\]

But \(\det(A_a+tA_1)=0\) identically, contradicting the hypothesis on \(A\).
Thus every point of \(D\) contributes at most one to a generic fiber.
Together with (1), this gives

\[
 \chi_c(F^{-1}(\lambda))\le 2(1-d)-N+d
 =2-d-N\le0. \tag{2}
\]

A slice or stable coordinate would instead give Euler characteristic one.
This contradiction proves the required necessity of constant determinant.

## Constructing the coordinate when the determinant is constant

Now assume \(\det A\in\mathbb C^*\). In particular, \(A_0\) is invertible. Put

\[
 L=A_0^{-1}A_1.
\]

The identity \(\det(I+xL)=1\) implies that \(L\) is nilpotent. Since it is a
\(3\times3\) matrix, \(L^3=0\). Symmetry of \(A_0,A_1\) gives
\(L^TA_0=A_0L\). Define polynomial matrices

\[
 S=I+\tfrac{x}{2}L-\tfrac{x^2}{8}L^2,\qquad
 S^{-1}=I-\tfrac{x}{2}L+\tfrac{3x^2}{8}L^2.
\]

Direct multiplication gives

\[
 S^2=I+xL,\qquad S^TA_0S=A(x).
\]

Because \(A^{-1}\) is polynomial, the change of variables

\[
 u=S(x)\left(v+\tfrac12 A(x)^{-1}b(x)\right)
\]

is a polynomial automorphism over \(\mathbb C[x]\). It transforms \(F\) into

\[
 F=u^TA_0u+h(x),\qquad h\in\mathbb C[x].
\]

The three \(u\)-derivatives vanish precisely at \(u=0\). Critical-point-freeness
therefore says that \(h'\) has no zero in \(\mathbb C\), so

\[
 h(x)=ax+e\qquad(a\in\mathbb C^*).
\]

The coordinate system \((F,u_1,u_2,u_3)\) has the explicit polynomial inverse

\[
 x=\frac{F-u^TA_0u-e}{a},\qquad
 v=S(x)^{-1}u-\tfrac12 A(x)^{-1}b(x).
\]

This proves (4) implies (1). A coordinate is both a stable coordinate and a
slice of a conjugate of a coordinate partial derivative, completing all
equivalences.

## Controls and limits

The cubic

\[
 F=x+2yz+xz^2+w^2
\]

has constant determinant and the explicit coordinates

\[
 U=y+xz/2,\quad Z=z,\quad W=w,\quad
 F=x+2UZ+W^2.
\]

It has no constant vector \(e\) with \(\partial_eF\) a nonzero constant: the
coefficient of \(xz^2\) first forces \(e_x=e_z=0\), and the remaining quadratic
terms force \(e_y=e_w=0\). Thus the new positive criterion goes beyond the
previous constant-direction sufficient condition.

In contrast, the following polynomials have no critical points but fail the
determinant criterion:

\[
 x+y+xyz+w^2,\qquad xy^2+y+z^2+w^2,\qquad
 x+y^2+2xyz+w^2.
\]

Their generic fiber Euler characteristics are respectively \(0,0,-1\). Their
zero fibers have Euler characteristic one. They are not stable coordinates.
These examples do not decide cancellation for their abstract zero fibers.

The exact checker verifies matrix identities, explicit inverse maps, critical
point controls, and the rank-one determinant obstruction. The topological
argument and its applicability to all coefficients remain a written proof,
not a proof-assistant certificate or a finite-search result.

The generic-rank-at-most-two cases lie outside this theorem's determinant
criterion, but are settled separately by the primitive-kernel-vector reduction
in [the multiple-root appendix](multiple-root-linear-pass.md#8-corollary-for-rank-deficient-quadratic-pencils).
Together the arguments prove slice-to-coordinate descent for all symmetric
affine \(3\times3\) pencils. Cubics not expressible as such a pencil, and
arbitrary-degree slice polynomials outside the covered families, remain
unresolved here. No general degree reduction has been proved.

## Sources

[^1]: Dominic Joyce, [*Constructible functions on Artin stacks*](https://arxiv.org/html/math/0403305), arXiv:math/0403305v7 (2006), introduction and Section 3.2. Used only for compactly supported Euler-characteristic pushforward and its functoriality. The pencil classification and coordinate formulas above are the present written derivation, not a theorem attributed to this source.

1. Dominic Joyce. [*Constructible functions on Artin stacks*](https://arxiv.org/html/math/0403305). arXiv:math/0403305v7, 2006.
