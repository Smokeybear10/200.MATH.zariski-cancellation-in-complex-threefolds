# Quadratic dependence with linear leading coefficient

For the pure-power expression

\[
 F=xu^n+G(x,y,z),\qquad n\ge2,
 \tag{1}
\]

an original locally nilpotent slice, or more generally stable
coordinatehood, forces \(G(0,y,z)\) to be a plane coordinate. The
cyclic quotient polynomial \(J=xw+G\) is consequently an ordinary
coordinate, with an explicit completion preserving \(x\). This does
not prove coordinatehood of the branched cover (1).

The result has no degree bound. The quadratic quartic application, a
closed subfamily, and the exact remaining relative issue follow below.

## 1. The divisible intermediate coefficient

Consider

\[
 F=xu^2+B(x,y,z)u+C(x,y,z),\qquad
 \deg B\le3,\quad\deg C\le4.
\]

If \(B=xb\), then \(\deg b\le2\) and the polynomial coordinate
change \(s=u+b/2\) gives

\[
 F=xs^2+G,\qquad G=C-\frac{x b^2}{4},\qquad\deg G\le5.
 \tag{2}
\]

If the quadratic homogeneous part \(b_2\) is nonzero, the degree-five
part of \(G\) is exactly \(-xb_2^2/4\), so the degree is five.
This happens for the genuine quartic coordinate

\[
 F=xu^2+xy^2u+z+x^4,
 \qquad G=z+x^4-\frac{xy^4}{4}.
\]

Its coefficient of \(z\) is one. Neither stability nor an original
slice justifies retaining a degree-four bound after (2).

## 2. The restriction to the leading-coefficient divisor

**Proposition.** If (1) is a stable coordinate, then
\(g(y,z)=G(0,y,z)\) is a coordinate of \(\mathbb C[y,z]\).
In fact every fiber of \(g\) is a smooth affine line.

An original LND slice satisfies the hypothesis. If \(D(F)=1\) and
\(K=\ker D\), then the slice theorem gives
\(\mathbb C[x,y,z,u]=K[F]\). After adjoining \(T\), the coefficient
ring \(K[T]\) is isomorphic to the original polynomial ring
\(K[F]\), so \(F\) is a coordinate after one stabilization. This
argument does not assume that \(K\) is already a polynomial ring.

### 2.1. Smoothness of the plane restriction

Stability makes every fiber
\(X_\lambda=\{xu^n+G=\lambda\}\) smooth and contractible.
Thus \(F\) has no critical point. At a hypothetical critical point
\((y_0,z_0)\) of \(g\), choose \(u_0\in\mathbb C\) with

\[
 u_0^n=-G_x(0,y_0,z_0).
\]

At \((0,y_0,z_0,u_0)\), all four partial derivatives of \(F\)
vanish, a contradiction. Therefore \(g\) has no critical point;
in particular it is nonconstant and each
\(C_\lambda=\{g=\lambda\}\) is a nonempty smooth affine curve.

### 2.2. The finite quotient has rational cohomology of a point

Let \(\mu_n\) act by \(u\mapsto\zeta u\), fixing \(x,y,z\).
Exactness of finite-group invariants in characteristic zero gives

\[
 X_\lambda/\mu_n
 =Y_\lambda:=\{xw+G(x,y,z)=\lambda\},\qquad w=u^n.
 \tag{3}
\]

For a finite group acting algebraically on a complex quasi-projective
variety, rational cohomology of the ordinary quotient is the invariant
part of rational cohomology upstairs. No freeness assumption is needed.
See [Florentino and Silva, Section 4.2, equation (5) and Proposition
4.3](https://arxiv.org/pdf/1711.07909). Consequently

\[
 H^j(Y_\lambda;\mathbb Q)=
 \begin{cases}\mathbb Q,&j=0,\\0,&j>0.\end{cases}
\]

Here \(Y_\lambda\) is smooth: at \(x\ne0\) its equation solves
for \(w\), and at \(x=0\) the two derivatives \(g_y,g_z\)
do not vanish simultaneously. Poincaré duality therefore gives
\(H_c^j(Y_\lambda;\mathbb Q)=0\) except for
\(H_c^6(Y_\lambda;\mathbb Q)=\mathbb Q\).

### 2.3. Compact supports force a single affine line

The open and closed parts of (3) are

\[
 U=Y_\lambda\cap\{x\ne0\}\simeq\mathbb C^*\times\mathbb A^2,
 \qquad
 E=Y_\lambda\cap\{x=0\}\simeq C_\lambda\times\mathbb A^1.
\]

Thus \(H_c^j(U;\mathbb Q)\) equals \(\mathbb Q\) in degrees
five and six and vanishes otherwise. The closed-open exact sequence
in degrees three through five yields

\[
 H_c^1(C_\lambda;\mathbb Q)=0,
 \qquad H_c^2(C_\lambda;\mathbb Q)\simeq\mathbb Q.
\]

The second equality says that the smooth curve has one component.
For its smooth completion of genus \(h\), with \(r\ge1\)
points removed, the first equality says \(2h+r-1=0\). Therefore
\(C_\lambda\simeq\mathbb A^1\). The defining polynomial
\(g-\lambda\) is reduced by smoothness and irreducible by
connectedness. The Abhyankar–Moh–Suzuki theorem rectifies this
embedded line, making \(g\) a plane coordinate. The exact plane
embedding statement is recalled in [Nguyen Van Chau, Section 2,
before Lemma 1](https://math.ac.vn/uploads/files/0202197.pdf).

This uses separate cohomology groups, not merely an Euler identity.

## 3. The quotient is polynomial, but the cover is not yet rectified

Choose a companion \(t\) to \(v=g(y,z)\). Extend this plane
coordinate system while fixing \(x\). In the new variables,

\[
 G(x,v,t)=v+xR(x,v,t).
\]

Set \(W=w+R(x,v,t)\). Then

\[
 J=xw+G=v+xW,
\]

and \((x,t,W,J)\) is a polynomial coordinate system. Its inverse
first gives \(v=J-xW\), then
\(w=W-R(x,J-xW,t)\). This also follows from Maubach's
univariate-coefficient criterion, but the inverse here is explicit.

On \(J=\lambda\), the original fiber is the cyclic cover

\[
 X_\lambda\simeq
 \left\{u^n=W-R(x,\lambda-xW,t)\right\}
 \subset\mathbb A^4_{x,t,W,u}.
 \tag{4}
\]

Its branch surface is \(G^{-1}(\lambda)\), not a surface known
from this argument to be polynomial. The normalization of the quotient
does not make the right side of (4) a coordinate.

A precise additional sufficient condition is

\[
 \mathbb C[x,y,z]=\mathbb C[x,G,t]
 \quad\text{for some }t.
 \tag{5}
\]

Under (5), \((x,F,t,u)\) is a coordinate system because
\(G=F-xu^n\). Condition (5) says that \(G\) is a coordinate
over the specified ring \(\mathbb C[x]\). Absolute coordinatehood
of \(G\) alone does not provide (5).

For every prime \(p\mid n\), Smith theory applied to the subgroup
\(\mu_p\) also makes \(G^{-1}(\lambda)\) mod-\(p\) acyclic;
the fixed set is \(u=0\). Smoothness of these surfaces follows by
evaluating \(\nabla F\) at \(u=0\). The relevant Smith statement
is [Symonds, Section 4, Corollary 4.3 and Remark
(1)](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf).
This does not assert their integral acyclicity, contractibility, or
isomorphism with \(\mathbb A^2\).

The proposition proves a relative statement only at \(x=0\):
\(X_\lambda\cap\{x=0\}\simeq\mathbb A^2\). No argument
here proves that every nonzero \(x\)-specialization is a coordinate.
No counterexample to that implication within the pure form (1) was
obtained in this pass.

The necessary condition on \(g\) alone is not sufficient, even for
genuine quartics with no critical points. For example,

\[
 F=xu^2+y+x^2y^2
\]

has \(g=y\). It has no critical point: at \(x=0\) its
\(y\)-derivative is one, while at \(x\ne0\) a critical point
would force \(u=0\), then \(y=0\) from the \(x\)-derivative,
contradicting the \(y\)-derivative. Nevertheless the fixed set of
\(u\mapsto-u\) in \(F^{-1}(0)\) is the disjoint union

\[
 \{y=0\}\ \coprod\ \{1+x^2y=0\}
 \simeq\mathbb A^2\ \coprod\ (\mathbb C^*\times\mathbb A^1).
\]

It is disconnected, contradicting Smith theory if \(F\) were stable.
Thus a smooth pure quadratic can have a polynomial cyclic quotient
and still fail stability. This is not an original-slice example.

## 4. An all-degree closed quadratic subfamily

Let

\[
 F=xu^2+p(x)z+Q(x,y),\qquad0\ne p\in\mathbb C[x].
 \tag{6}
\]

Then stable coordinatehood, existence of an original LND slice,
absolute coordinatehood, and coordinatehood over \(\mathbb C[x]\)
are all equivalent to

\[
 Q(\alpha,y)=a_\alpha y+b_\alpha,
 \qquad a_\alpha\ne0,
 \quad\text{for every root }\alpha\text{ of }p.
 \tag{7}
\]

Indeed, the stable univariate-coefficient criterion in
[multiple-root-linear-pass.md](multiple-root-linear-pass.md) reduces
the question to coordinatehood of
\(\alpha u^2+Q(\alpha,y)\) in \(\mathbb C[u,y]\).
If \(\alpha\ne0\), a critical point would occur at \(u=0\)
and any zero of \(Q_y(\alpha,y)\). A polynomial in one variable
with no zero is a nonzero constant, giving (7). When \(\alpha=0\),
the same conclusion follows because \(Q(0,y)\) alone must be a
coordinate. Conversely (7) solves for \(y\) in every root
specialization. Published sufficiency, including arbitrary root
multiplicities, is [Maubach, Corollary 4.2 and Theorem
4.5](https://www.math.ru.nl/~maubach/Papers/The_Commuting_Dervations.pdf).
For constant \(p\), one directly solves for \(z\).

For example, the genuine quartic

\[
 F=xu^2+(x-1)^2z+y+(x-1)y^3
\]

is a coordinate over \(\mathbb C[x]\), since the only distinct
root is \(\alpha=1\) and \(Q(1,y)=y\). This is a deduction
from the established univariate-coefficient theorem, not a new
general classification result.

## 5. General intermediate terms defeat residual specialization

The coordinate

\[
 F=xu^2+yu+x+z^4,\qquad D=\partial_x-u\partial_y
\]

has total degree four, \(D(F)=1\), and locally nilpotent \(D\).
Writing \(T=y+xu\) gives \(F=x+uT+z^4\), with inverse

\[
 x=F-uT-z^4,\qquad y=T-u(F-uT-z^4).
\]

Nevertheless, every specialization

\[
 F_\gamma=\gamma+u(y+\gamma u)+z^4
\]

has a critical point at \(u=y=z=0\), so none is a coordinate.
This independently checked counterexample is also recorded in
[quadratic-slice-literature.md](quadratic-slice-literature.md).
It refutes an absolute-slice-to-residual-\(x\) implication for the
general quadratic expression. Its intermediate coefficient is \(y\),
not divisible by \(x\), so it does not refute the corresponding
claim for the pure branch.

## 6. Independent source check: a closed monic binomial branch

Suppose instead that \(H=s^2+G(x,y,z)\) is stable and

\[
 G=f(x,y)z^m+h(x,y),\qquad m\ge1,\quad f\ne0.
\]

Then \(G\), and hence \(H\), is a coordinate. Here is the
precise source-dependent deduction.

For a general fiber \(Y\) of \(G\), [Némethi, Theorem G1 and
Example 3.4(a)](https://www.numdam.org/article/CM_1991__80_1_1_0.pdf)
give \(H^{-1}(\lambda)\simeq S^0*Y=\Sigma Y\) at a general
value. Contractibility upstairs implies integral acyclicity of \(Y\).
Also \(\nabla H=(2s,\nabla G)\) makes \(Y\) smooth; its
connectedness makes it irreducible.

[Kaliman and Zaidenberg, Theorem 7.2, printed pp. 28–29](https://arxiv.org/pdf/math/9801076)
applies to an irreducible smooth surface \(f(x,y)z^m+g(x,y)=0\).
It makes integral acyclicity equivalent to rectifiability. Apply it
with \(g=h-\lambda\). Since the reduced irreducible equation
\(G-\lambda\) defines the rectified plane, an ambient automorphism
sends it to a nonzero scalar times a coordinate. Thus \(G\) is a
coordinate, and adding \(s^2\) preserves coordinatehood.

This reads the theorem with its exact integral hypothesis. Its
Example 7.1 gives a rationally acyclic surface for which the conclusion
fails. The argument therefore does not apply to the pure-\(x\)
branch merely from the mod-2 fixed-set calculation above. There is no
degree restriction in this monic binomial deduction.
