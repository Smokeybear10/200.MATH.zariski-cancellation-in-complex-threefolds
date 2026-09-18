# The monic quadratic branch of the quartic reduction

Let

\[
 F=a u^2+B(v)u+C(v),\qquad a\in\mathbb C^*,\quad
 v=(v_1,v_2,v_3),\quad \deg B\le3,\quad \deg C\le4.
\]

The bounded investigation gives two necessary topological conditions and
an exact conditional descent lemma. It also gives an explicit quartic
counterexample to the proposed shortcut of averaging a slice derivation.
It does not prove that every stable coordinate in this branch is a coordinate.

## 1. Completing the square can raise the degree to six

Choose a square root of \(a\), and put

\[
 s=\sqrt a\left(u+\frac{B(v)}{2a}\right),\qquad
 G(v)=C(v)-\frac{B(v)^2}{4a}.
\]

This is a polynomial change of coordinates, and

\[
 F=s^2+G(v),\qquad \deg G\le6.
\]

If \(B_3\ne0\), then the degree-six part is exactly
\(-B_3^2/(4a)\), so \(\deg G=6\). This case occurs even for
quartic coordinates: the polynomial

\[
 F=u^2+x^3u+y+x^4
\]

is a coordinate because its coefficient of \(y\) is one, whereas its
completed remainder is \(G=y+x^4-x^6/4\). Thus stability cannot by
itself force \(\deg B\le2\) or justify a degree-four bound after the
completion. When \(\deg B\le2\), the degree-four bound is valid.

## 2. Every branch surface is smooth and mod-2 acyclic

Suppose \(H=s^2+G(v)\) is a stable coordinate. For every
\(\lambda\in\mathbb C\), its fiber

\[
 X_\lambda=\{s^2+G(v)=\lambda\}
\]

is smooth and contractible. Its involution

\[
 \sigma(s,v)=(-s,v)
\]

has fixed set
\(Y_\lambda=\{s=0,G(v)=\lambda\}\simeq G^{-1}(\lambda)\).
The fixed-set form of Smith theory implies

\[
 H^j(Y_\lambda;\mathbb F_2)=
 \begin{cases}\mathbb F_2,&j=0,\\0,&j>0.\end{cases}
 \tag{1}
\]

The relevant hypotheses are a finite-dimensional space with mod-2
cohomology of a point and an action of a finite 2-group. Complex affine
varieties with this algebraic involution admit the needed equivariant
triangulation. This is the ordinary-cohomology Smith theorem, recorded
explicitly in Symonds, Section 4 and Corollary 4.3, Remark (1).[^1]

Also \(\nabla H=(2s,\nabla G)\). A critical point of \(G\) would
give a critical point of \(H\) at \(s=0\). Consequently \(G\) has
no critical points, and all the \(Y_\lambda\) are smooth connected
affine surfaces. The conclusion (1) is stronger than the branched-cover
Euler identity

\[
 \chi_c(X_\lambda)=2-\chi_c(Y_\lambda).
\]

Smith theory alone does not assert that \(Y_\lambda\) is contractible,
isomorphic to \(\mathbb A^2\), or stably isomorphic to \(\mathbb A^2\).
In particular, it does not prove that \(G\) is a stable coordinate.

## 3. The general branch surface is integrally acyclic

The global Sebastiani–Thom theorem gives an additional necessary condition:
if \(Y\) is a general fiber of \(G\) and \(X\) a general fiber of
\(H\), then

\[
 X\simeq S^0*Y=\Sigma Y.
\]

The source is Némethi, Theorem G1 and Example 3.4(a): take the outer
polynomial \(p(c,d)=c+d\), the two inner maps \(s\mapsto s^2\) and
\(G\). Example 3.4(a) explicitly verifies the hypotheses for this sum
case. No tameness assumption on \(G\), isolated-singularity assumption,
or claim about special fibers is being imported.[^2]

Since \(X\) is contractible, the suspension homology isomorphism yields

\[
 \widetilde H_j(Y;\mathbb Z)=0\qquad(j\ge0).
 \tag{2}
\]

This is an integral homology obstruction, not a coordinate criterion.
Suspension kills fundamental-group information, so its contractibility
does not imply contractibility of \(Y\). The theorem used here concerns
general fibers and does not upgrade (1) for every exceptional value.

## 4. An equivariant slice is sufficient, even after stabilization

**Conditional descent lemma.** The following conditions are equivalent:

1. \(G\) is a coordinate in \(\mathbb C[v_1,v_2,v_3]\).
2. On \(\mathbb C[s,v_1,v_2,v_3,w_1,\ldots,w_N]\), for some
   \(N\ge0\), there is a locally nilpotent derivation \(D\) satisfying
   \(D(H)=1\) and \(D\sigma=\sigma D\), where \(\sigma\) fixes
   the extra variables and the \(v_i\), and negates \(s\).

For \(2\Rightarrow1\), commutation makes \(D(s)\) odd in \(s\),
so \(D(s)\in(s)\). Therefore the ideal \((s)\) is invariant under
\(D\). The induced derivation

\[
 \delta:\mathbb C[v,w]\longrightarrow\mathbb C[v,w]
\]

is locally nilpotent and satisfies \(\delta(G)=1\). The slice theorem
makes \(G\) a stable coordinate: if
\(\mathbb C[v,w]=K[G]\), adjoin one variable \(r\); then
\(K[r]\simeq K[G]\) is a polynomial ring and
\(K[r][G]\) exhibits \(G\) as a coordinate after that stabilization.
Stable-coordinate descent in three complex variables now makes \(G\)
a coordinate in \(\mathbb C[v]\). This is precisely the finite-
stabilization version proved by Shpilrain and Yu, Proposition 1.1(c).[^3]

For \(1\Rightarrow2\), choose polynomial coordinates \((G,p,q)\)
on \(\mathbb A^3\). The derivation \(\partial/\partial G\),
extended by \(D(s)=0\), supplies the required slice without extra
variables. In this case \((H,s,p,q)\) is a coordinate system, so the
original \(F\) is a coordinate as well.

Thus an equivariant slice would close the monic branch. Ordinary
stability supplies a slice derivation after stabilization, but it does
not supply the commutation condition established in this lemma.

## 5. Averaging a slice can destroy local nilpotence

The failure occurs for an actual quartic coordinate. Work in
\(\mathbb C[s,x,y,z]\), set

\[
 H=s^2+x+y^4,\qquad t=H,
\]

and use coordinates \((t,s,y,z)\). The involution \(\sigma\)
fixes \(t,y,z\) and negates \(s\). Define

\[
 D=\partial_t+(-ts+y)\partial_s+
       ((1-t^2)s+ty)\partial_y,\qquad D(z)=0.
\]

Put

\[
 a=(1+t^2)s-ty,\qquad b=-ts+y.
\]

The inverse formulas are
\(s=a+tb\), \(y=ta+(1+t^2)b\). Hence \((t,a,b,z)\) are
polynomial coordinates. Direct calculation gives
\(D(t)=1\), \(D(a)=D(b)=D(z)=0\), so \(D\) is locally
nilpotent and \(D(H)=1\).

Its average with the conjugate derivation is

\[
 E=\frac{D+\sigma D\sigma}{2}
  =\partial_t-ts\partial_s+ty\partial_y.
\]

Although \(E(H)=1\) and \(E\sigma=\sigma E\), it is not
locally nilpotent. Indeed

\[
 E^n(y)=P_n(t)y,\qquad
 P_0=1,\quad P_{n+1}=P_n'+tP_n.
\]

Induction gives \(\deg P_n=n\) with leading coefficient one, so
\(E^n(y)\ne0\) for every \(n\). Its induced derivation modulo
\((s)\) also fails local nilpotence. The inverse identities,
\(D(a)=D(b)=0\), and the first three iterates of \(E(y)\) were
checked with exact symbolic arithmetic. The all-iterate argument is
the degree induction above.

This disproves the averaging shortcut, not the existence of some other
equivariant slice. Here such another slice exists because
\(G=x+y^4\) is already a coordinate.

## 6. Check against the existing quartic negative control

The previously studied polynomial

\[
 H=s^2+x+x^2yz
\]

lies in this monic branch. All its fibers are smooth with Euler
characteristic one, but it fails the Smith obstruction. For
\(\lambda\ne0\), its branch surface

\[
 Y_\lambda=\{x+x^2yz=\lambda\}
\]

has \(x\ne0\). Projection to \(x\in\mathbb C^*\) has the
algebraic section

\[
 x\longmapsto\left(x,1,\frac{\lambda-x}{x^2}\right).
\]

Thus \(H^1(\mathbb C^*;\mathbb F_2)\) injects into
\(H^1(Y_\lambda;\mathbb F_2)\), contradicting (1). This supplies
a direct fixed-surface explanation of the obstruction in
[the existing negative-control note](nonaffine-quadratic-control.md).

The remaining issue is to prove coordinate descent for the restricted
remainders \(G=C-B^2/(4a)\), or to obtain an equivariant slice by a
method that preserves local nilpotence. Neither conclusion follows
from the square completion, Smith theory, the global suspension
theorem, or averaging alone.

## Sources

[^1]: Peter Symonds, [*Smith Theory for algebraic varieties*](https://personalpages.manchester.ac.uk/staff/peter.symonds/preprints/smith.pdf), Section 4, Corollary 4.3 and Remark (1); published in *Algebraic & Geometric Topology* **4** (2004), 121–131. The cited author version states the ordinary-cohomology fixed-point theorem at the beginning of Section 4 and explains the CW-complex variant after Theorem 4.2.

[^2]: András Némethi, [*Generalized local and global Sebastiani-Thom type theorems*](https://www.numdam.org/article/CM_1991__80_1_1_0.pdf), *Compositio Mathematica* **80** (1991), 1–14, Theorem G1 and Example 3.4(a), printed p. 6. The example explicitly states that the sum case satisfies the global theorem's assumptions.

[^3]: Vladimir Shpilrain and Jie-Tai Yu, [*Affine varieties with equivalent cylinders*](https://arxiv.org/html/math/0110324), Proposition 1.1(c), with its proof in Section 2. The proof explicitly permits a polynomial in three variables to become a coordinate in any larger finite number of variables.
