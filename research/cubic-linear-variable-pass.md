# Cubic slices with a variable occurring linearly

Let

\[
 B=\mathbb C[x,y,z,w],\qquad
 F=x^2y+g(x,z,w),\qquad \deg g\leq3,
\]

and put \(g_0(z,w)=g(0,z,w)\). There is a complete criterion for this family:

\[
 \boxed{\text{There is an LND }D\text{ of }B\text{ with }D(F)=1
 \iff g_0\text{ is a coordinate of }\mathbb C[z,w].}
 \tag{1}
\]

In the positive case, \(F\) itself is a coordinate of \(B\), with an explicit polynomial inverse given below. In the negative case, the Euler characteristic of a generic fiber already excludes a slice and excludes making \(F\) a coordinate by adjoining any finite number of variables. This concerns the specified polynomial \(F\), not every possible presentation of an abstract threefold cylinder.

For the degree bound here, (1) also has a finite linear-algebra formulation:

\[
 \boxed{\exists\alpha,\beta\in\mathbb C:
 \alpha\frac{\partial g_0}{\partial z}
 +\beta\frac{\partial g_0}{\partial w}=1.}
 \tag{2}
\]

Equivalently, after an affine linear change of the plane variables,

\[
 g_0=u+P(v),\qquad \deg P\leq3.
 \tag{3}
\]

The coefficient of \(u\) can initially be any nonzero constant and is normalized by rescaling. The bound of three is important for equivalence with the constant-direction test (2). Section 7 gives a separately sourced extension of (1), but not of (2), to arbitrary degree and to the coefficient \(x^m\). The coordinate criterion itself is contained in Maubach's published classification, as documented in [the multiple-root continuation](multiple-root-linear-pass.md); it is not a novelty claim.

## 1. Slice consequences and the fiber calculation

Suppose \(D(F)=1\) for a locally nilpotent derivation and let \(A=\ker D\). The slice theorem gives

\[
 B=A[F].
\]

Consequently every fiber \(X_\lambda=\{F=\lambda\}\) is isomorphic to \(\operatorname{Spec}A\), and

\[
 X_\lambda\times\mathbb A^1\simeq\mathbb A^4.
 \tag{4}
\]

In particular, \(X_\lambda\) is contractible as a complex topological space and its compactly supported Euler characteristic is one. The Euler assertion follows directly from multiplicativity and \(\chi_c(\mathbb A^n)=1\), without needing contractibility. Also, adjoining one independent variable makes \(F\) a coordinate: \(B[T]=A[T][F]\), and \(A[T]\simeq A[F]=B\).

There is an elementary Euler formula valid without assuming a slice. On \(x\ne0\), one can solve uniquely for \(y\), so

\[
 X_\lambda\cap\{x\ne0\}\simeq\mathbb C^*\times\mathbb A^2.
\]

On \(x=0\), the variable \(y\) is free and the remaining equation is \(g_0(z,w)=\lambda\). Thus additivity gives

\[
 \boxed{\chi_c(X_\lambda)=\chi_c\{g_0=\lambda\}.}
 \tag{5}
\]

Indeed, the open stratum contributes zero and the closed stratum contributes the Euler characteristic of its plane-curve factor. If \(g_0\) is constant, its generic fiber is empty, so (5) already excludes a slice. Otherwise a slice forces every plane fiber, and in particular a generic one, to have Euler characteristic one.

## 2. An elementary cubic plane-curve lemma

**Lemma.** For \(h\in\mathbb C[z,w]\) of degree at most three, the following are equivalent:

1. A generic fiber of \(h\) has Euler characteristic one.
2. \(h\) is a plane coordinate.
3. Some constant directional derivative of \(h\) is a nonzero constant.
4. After an affine linear plane change, \(h=u+P(v)\).

Here a generic fiber means a fiber outside a finite exceptional set. The implications from 4 to 3 and 2, and from 2 to 1, are immediate. To prove 1 implies 4, the only substantive issues are generic reducibility and the possible cubic embedding of a line.

### Reducible fibers

If infinitely many distinct fibers \(h=\lambda\) are reducible, each contains an affine line: a reducible polynomial of degree two or three has a linear factor. Choose one such line for each of infinitely many distinct values. Lines lying in different fibers cannot meet in \(\mathbb A^2\), so all these lines are parallel.

Choose affine linear coordinates \((u,v)\) in which they have equations \(v=c_i\), with infinitely many distinct \(c_i\). Since \(h(u,c_i)\) is constant in \(u\), the polynomial \(\partial h/\partial u\) vanishes on every one of these lines. Every coefficient in its expansion in powers of \(u\) therefore vanishes at infinitely many \(c_i\). It follows that \(\partial h/\partial u=0\), so \(h=P(v)\).

For a generic value, \(P(v)=\lambda\) has \(\deg P\) distinct roots. That fiber is a disjoint union of \(\deg P\) affine lines and has Euler characteristic \(\deg P\). Euler characteristic one forces \(\deg P=1\), which gives 4.

Otherwise only finitely many fibers are reducible. Choose a generic fiber that is both irreducible and smooth. Smoothness outside finitely many values follows, for example, by noting that the critical locus has finitely many irreducible components and \(h\) is constant on each positive-dimensional component of that locus. Its image, together with the images of its isolated points, is finite.

### The smooth irreducible fiber

Let \(C\) be this smooth irreducible affine curve. Let \(\overline C\) be its smooth projective completion, of genus \(\gamma\), and let \(n\geq1\) be the number of omitted points. Then

\[
 \chi_c(C)=2-2\gamma-n=1.
\]

Hence \(\gamma=0\) and \(n=1\), giving \(C\simeq\mathbb A^1\). Its embedding in the plane is a polynomial parametrization

\[
 t\longmapsto(p(t),q(t))
\]

that is a closed immersion. The maximum of the two polynomial degrees equals the degree \(d\leq3\) of the plane curve. To see this, homogenize the parametrization to a morphism from \(\mathbb P^1\) to the projective closure of \(C\). The homogeneous coordinate polynomials have no common zero and degree \(\max(\deg p,\deg q)\). The morphism is birational, so pulling back a generic projective line gives exactly \(d\) points counted with multiplicity.

After a linear plane change, the nonconstant degrees can be arranged as \(\deg p=d\), \(\deg q<d\), by cancelling leading coefficients if necessary. A constant \(q\) forces \(d=1\): the embedding then identifies \(\mathbb C[p(t)]\) with \(\mathbb C[t]\). Apart from this linear case, the only way both remaining degrees can exceed one is

\[
 (\deg p,\deg q)=(3,2).
\]

That case is impossible. Translate and scale the parameter and apply affine linear changes to the plane coordinates to arrange

\[
 q(t)=t^2,\qquad p(t)=at^3+bt,\qquad a\ne0.
\]

If \(b\ne0\), choose a nonzero root of \(at^2+b=0\). The distinct parameters \(t,-t\) have the same two coordinates, contradicting injectivity. If \(b=0\), both coordinate derivatives vanish at zero, contradicting the tangent injectivity of a closed immersion.

Therefore one plane coordinate is linear in \(t\). The embedded curve is a graph \(u=P(v)\) after an affine linear plane change. Since \(h-\lambda\) is an irreducible reduced defining polynomial of this graph, it is a nonzero scalar multiple of \(u-P(v)\). This proves 4, with the scalar absorbed into \(u\).

This low-degree argument proves the needed special case of line rectification directly. It does not assume the higher-dimensional embedding or cancellation conjectures, and does not need the general Abhyankar–Moh–Suzuki theorem.

## 3. Explicit coordinate construction

Write

\[
 g=g_0+xg_1+x^2g_2+x^3g_3.
\]

First replace \(y\) by \(y+g_2+xg_3\). If \(g_0\) is a plane coordinate, change the plane coordinates so that it becomes \(z\). Renaming the transformed variables gives

\[
 F=z+xQ(z,w)+x^2y
 \tag{6}
\]

for some polynomial \(Q\). A nonlinear plane change can increase the degree of \(Q\); the following construction puts no degree bound on it.

Keep \(x,w\), and define two new coordinates by

\[
 Z=F,
 \qquad
 Y=\frac{z-Z+xQ(Z,w)}{x^2}
   =-y+\frac{Q(Z,w)-Q(z,w)}x.
 \tag{7}
\]

The displayed quotient is polynomial because \(Z-z=xQ(z,w)+x^2y\) is divisible by \(x\), and \(Q(Z,w)-Q(z,w)\) is divisible by \(Z-z\).

The inverse is

\[
 z=Z-xQ(Z,w)+x^2Y,
 \qquad
 y=-Y+\frac{Q(Z,w)-Q(z,w)}x,
 \tag{8}
\]

where the expression for \(z\) in (8) is used on its right-hand side. These are again polynomials, because the new \(Z-z\) is divisible by \(x\). Substitution in either direction gives the identity. Thus

\[
 \mathbb C[x,y,z,w]=\mathbb C[x,Y,Z,w],\qquad Z=F.
\]

Transporting \(\partial/\partial Z\) through this explicit coordinate system gives an LND with \(D(F)=1\). Its kernel is exactly \(\mathbb C[x,Y,w]\).

For a direct formula in the normalized variables, put \(Q_z=\partial Q/\partial z\). Then this transported derivation is

\[
 \begin{aligned}
 D(x)&=D(w)=0,\\
 D(z)&=1-xQ_z(F,w),\\
 D(y)&=\frac{Q_z(F,w)-Q_z(z,w)}x
          +Q_z(z,w)Q_z(F,w).
 \end{aligned}
 \tag{9}
\]

The quotient is polynomial for the same reason as before. Formula (9) gives \(D(F)=1\) by direct differentiation; local nilpotence follows from the coordinate conjugation, not merely from that identity.

## 4. An exact finite gate

To test an input in this cubic family, compute \(g_0\) and solve the linear system obtained by comparing coefficients in

\[
 \alpha(g_0)_z+\beta(g_0)_w=1.
\]

This has just two unknown constants. A solution certifies the positive case: choose an affine coordinate \(u\) along the direction \((\alpha,\beta)\) and a nonzero linear coordinate \(v\) annihilating that direction. Then \(g_0=u+P(v)\), and (7) supplies the four-variable coordinate construction after the elementary preliminary changes.

Inconsistency certifies that there is no slice and that \(F\) is not stably a coordinate. This conclusion uses the proven degree-three classification; it is not a degree-bounded search for a derivation.

The coordinate identities (7)–(8) were also checked by exact symbolic substitution in both directions for

\[
 Q=7,\quad z+w,\quad z^2+zw+w^2,\quad z^3+zw^2+w^4.
\]

All four tests passed. The proof of the inverse is uniform in \(Q\); these finite checks are supplementary, not its justification.

## 5. What the derivative at \(x=0\) does and does not imply

At \(x\ne0\), \(\partial F/\partial y=x^2\ne0\). At \(x=0\), the only possibly nonzero gradient entries are

\[
 \left.\frac{\partial F}{\partial x}\right|_{x=0}=g_1(z,w),
 \quad (g_0)_z(z,w),\quad (g_0)_w(z,w).
\]

Therefore \(F:\mathbb A^4\to\mathbb A^1\) has no critical points precisely when

\[
 V\bigl(g_1,(g_0)_z,(g_0)_w\bigr)=\varnothing
 \quad\text{in }\mathbb A^2.
 \tag{10}
\]

A choice of \(g_1\) can remove critical points even when \(g_0\) is very far from a coordinate. For instance,

\[
 F=x^2y+x+zw
\]

is a submersion everywhere, because \(g_1=1\). Its zero fiber has Euler characteristic one: \(\{zw=0\}\) is two affine lines meeting at a point. But for every \(\lambda\ne0\), the plane curve \(zw=\lambda\) is \(\mathbb C^*\), so \(\chi_c(X_\lambda)=0\). Hence it has no slice and is not stably a coordinate.

Thus smoothness of all fibers together with Euler characteristic one of the zero fiber is insufficient. In this particular cubic family, Euler characteristic one of a **generic** fiber is sufficient, by Sections 2–3. No fundamental-group calculation is needed to close the criterion. There is also no claim that the fundamental group of the threefold fiber can be read directly from that of its plane stratum.

## 6. Limits of the conclusion

The result classifies the displayed polynomials and constructs polynomial kernels for every positive case. It does not prove that an arbitrary slice polynomial in four variables can be transformed into this family. Nor does it decide whether a particular negative-case zero fiber has an abstract cylinder isomorphic to \(\mathbb A^4\). Such an isomorphism would not identify the given polynomial's other fibers.

The degree-three affine-direction test does not persist in all degrees. For example,

\[
 h(z,w)=w+(z+w^2)^2
\]

is a plane coordinate, by composing two triangular plane automorphisms, but no nonzero constant directional derivative of \(h\) is constant. Indeed, the \(zw\) term in \(h_w\) forces its coefficient in such a linear combination to be zero, after which the \(z\) term in \(h_z\) forces the other coefficient to be zero.

## 7. Extension to arbitrary degree and \(x^m\)

With two standard plane-curve results, the same criterion extends beyond cubics:

\[
 \boxed{F=x^m y+g(x,z,w),\quad m\geq1:
 \quad F\text{ has an LND slice}
 \iff F\text{ is a coordinate}
 \iff g(0,z,w)\text{ is a plane coordinate}.}
 \tag{11}
\]

Here \(g\) is any complex polynomial independent of \(y\). A finite stable-coordinate assumption on \(F\) is equivalent to these conditions as well.

### General plane necessity and its source

For any nonconstant plane polynomial \(h\), polynomial Stein factorization writes \(h=\varphi(r)\), where \(\varphi\in\mathbb C[t]\) and the generic fiber of \(r\) is connected. Outside finitely many values, \(h=\lambda\) is the disjoint union of \(d=\deg\varphi\) generic fibers of \(r\). Thus

\[
 \chi_c(h^{-1}(\lambda))=d\,\chi_c(r^{-1}(\mu)).
\]

If the left side is one, integrality forces \(d=1\). The connected smooth generic curve then has genus zero and one puncture, so is \(\mathbb A^1\). The Abhyankar–Moh–Suzuki embedding theorem makes its defining polynomial, and hence \(h\), a coordinate. Polynomial factorization and the required line-rectification statement appear in Nguyen Van Chau, Section 2 and Lemma 1, printed pp. 198–199.[^1]

Formula (5) works unchanged for \(x^m y+g\), for every \(m\geq1\). A slice or stable coordinate forces generic Euler characteristic one, so the preceding plane argument proves necessity in (11).

### The truncated polynomial inverse proves sufficiency

After a plane coordinate change, arrange \(g(0,z,w)=z\), and write

\[
 g(x,z,w)=h(x,z,w)=z+xQ(x,z,w).
\]

The substitution \(z\mapsto h(x,z,w)\) is an automorphism over \(\mathbb C[x,w]/(x^m)\). Concretely, recursively choose

\[
 R(x,Z,w)=Z+\sum_{j=1}^{m-1}x^jR_j(Z,w)
\]

such that

\[
 h(x,R(x,Z,w),w)\equiv Z\pmod{x^m}.
 \tag{12}
\]

At step \(j\), adding \(x^jR_j\) to the current inverse changes the degree-\(j\) error by exactly \(x^jR_j\), since \(h_z\equiv1\pmod x\). Taking the negative of the current error coefficient therefore determines \(R_j\) polynomially. This is a finite recursion. It also gives

\[
 R(x,h(x,z,w),w)\equiv z\pmod{x^m}:
\]

modulo \(x^m\), the difference \(h(x,U,w)-h(x,V,w)\) is \((U-V)\) times a unit of the form \(1+xA\), so a right inverse is a left inverse too.

Define

\[
 Z=F=h(x,z,w)+x^my,
 \qquad Y=\frac{z-R(x,Z,w)}{x^m}.
 \tag{13}
\]

These are polynomials by (12) and its left-inverse version. The inverse is

\[
 z=R(x,Z,w)+x^mY,
 \qquad y=\frac{Z-h(x,z,w)}{x^m}.
 \tag{14}
\]

The second expression in (14) is polynomial because substituting its first expression into \(h\) gives \(Z\) modulo \(x^m\). Both coordinate compositions are the identity. Thus (13)–(14) prove the positive direction in (11) with an actual polynomial inverse; an infinite formal inverse is never being asserted to be polynomial.

The coefficient \(x^m\) has a single distinct zero. For a general coefficient in \(x\) with multiple distinct zeros, the Euler calculation contains multiple plane-curve contributions, and the necessity argument above no longer applies in this form.

## Sources

[^1]: Nguyen Van Chau, [“Polynomial maps of the complex plane with the branched value sets isomorphic to the complex line”](https://math.ac.vn/uploads/files/0202197.pdf), *Acta Mathematica Vietnamica* **27** (2002), 197–202, Section 2 and Lemma 1, pp. 198–199. The general extension uses its explicit polynomial Stein factorization and its line-rectification lemma. The cubic proof in Section 2 does not need these external structure theorems.
