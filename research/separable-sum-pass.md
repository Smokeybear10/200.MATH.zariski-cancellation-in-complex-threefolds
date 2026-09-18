# Separated sums with a binomial remainder

Let \(h\in\mathbb C[s]\) have degree \(N\ge2\), let
\(0\ne f\in\mathbb C[x,y]\), let \(g\in\mathbb C[x,y]\), and let
\(q\ge1\) be an integer. Set
\[
G=f(x,y)z^q+g(x,y),\qquad F=h(s)+G.
\]
Then
\[
\boxed{F\text{ is a stable coordinate}
\ \Longleftrightarrow\
G\text{ is a coordinate}
\ \Longleftrightarrow\
F\text{ is a coordinate}.}
\tag{1}
\]
There is no upper degree bound. In particular, the conclusion applies
if \(F\) is a slice of a locally nilpotent derivation on the original
four-variable polynomial ring.

This is a deduction from the global sum theorem and an existing
binomial-surface rectification theorem. It is not an assertion of a
new general cancellation theorem. No reduction of arbitrary slices to
this separated presentation is supplied.

## Proof

Suppose \(F\) is a stable coordinate. Its fibers become affine spaces
after multiplication by an affine space, so every fiber is smooth
and contractible.

Let \(Y\) be a general fiber of \(G\). The general fiber of \(h\)
is a discrete set \(D_N\) of \(N\) points. The global sum theorem
identifies a general fiber of \(F\), up to homotopy, with
\(D_N*Y\). The theorem applies to arbitrary polynomial summands
in disjoint variables, without a tameness condition.[^1]

For every \(j\ge0\), the integral join formula gives
\[
\widetilde H_{j+1}(D_N*Y;\mathbb Z)
\cong
\widetilde H_j(Y;\mathbb Z)^{\oplus(N-1)}.
\tag{2}
\]
For clarity, the reduced integral homology of \(D_N\) is free of
rank \(N-1\) in degree zero. In the augmented-chain tensor formula
for the join, this gives the displayed shift and no Tor terms.
Equation (2) includes \(j=0\), even when \(Y\) has not yet been
shown connected. Since \(N-1>0\), contractibility of the general
\(F\)-fiber implies that \(Y\) is integrally acyclic.

There is a point \(s_0\) with \(h'(s_0)=0\), because \(N\ge2\)
and the field is \(\mathbb C\). If \(G\) had a critical point
\(p\), then \(F\) would have a critical point \((s_0,p)\).
Thus \(G\) has none. In particular \(Y=V(G-\lambda)\) is smooth
and reduced. Its connectedness from (2) makes it irreducible.

The surface rectification theorem for
\(f(x,y)z^q+g(x,y)-\lambda=0\) identifies integral acyclicity,
for a smooth irreducible surface of this form, with rectifiability
in \(\mathbb A^3\).[^2] Apply it to \(Y\). An ambient automorphism
therefore carries the prime ideal \((G-\lambda)\) to the ideal
of a coordinate plane. Its generator is a nonzero scalar times
that coordinate, since units of a polynomial ring over
\(\mathbb C\) are constants. Reducedness excludes a higher power.
Consequently \(G\) itself is a coordinate.

This invokes the rectifiability part of the surface theorem. Abstract
isomorphism of \(Y\) with \(\mathbb A^2\) alone would not be the
claimed argument about its defining polynomial.

Conversely, if \(\mathbb C[x,y,z]=\mathbb C[G,U,V]\), then
\[
\mathbb C[s,x,y,z]
=\mathbb C[s,G,U,V]
=\mathbb C[s,F,U,V],
\]
with inverse \(G=F-h(s)\). Thus \(F\) is a coordinate. Coordinatehood
implies stable coordinatehood, completing (1).

For an original LND slice \(D(F)=1\), put \(K=\ker D\).
The slice decomposition is \(T=K[F]\), where \(T=\mathbb C^{[4]}\).
Adjoining an indeterminate \(v\) gives
\(T[v]=K[v][F]\), and \(K[v]\cong K[F]=T\).
This proves that \(F\) is one-stable without assuming \(K\) is
polynomial beforehand. Hence (1) applies, and also proves
\(K\cong\mathbb C^{[3]}\) in this family.

## Constant cases and boundary conditions

The surface theorem permits constant coefficients in its statement,
but its proof sets these elementary cases aside. They can be checked
directly here.

If \(q=1\) and \(f=c\ne0\), then \(G=cz+g\) is a coordinate.
If \(q\ge2\) and \(f=c\ne0\), the established acyclicity of a
general \(G\)-fiber and a second application of (2), now to
\(cz^q+g(x,y)\), make a general \(g\)-fiber an acyclic smooth
connected affine curve. It is an affine line, and plane-line
rectification makes \(g\) a coordinate. Adding \(cz^q\) then
completes \(G\) explicitly.

If \(g\) is constant and \(q\ge2\), \(G\) has critical points
on \(z=0\), so stability is impossible. If \(g\) is constant,
\(q=1\), and \(f\) is nonconstant, a zero of \(f\), together
with \(z=0\), is a critical point. The only stable constant-\(g\)
case is therefore \(q=1\) and nonzero constant \(f\).

The condition \(\deg h\ge2\) is essential to the implication
from \(F\) to \(G\). For example,
\[
F=s+z^2+xy
\]
is a coordinate, whereas \(G=z^2+xy\) has a critical point.
Joining with a single point gives a cone and no restriction on
the homology of \(Y\).

The integral coefficient ring in (2) is essential as well. Rational
acyclicity cannot replace it in the surface step. The cited surface
paper's Example 7.1 explicitly exhibits the distinction.[^2]

For \(q\ge2\), the pair assertion of the same surface theorem
also yields the following criterion: an automorphism of
\(\mathbb C[x,y]\) carries \((f,g)\) to \((p(x),y+b)\), with
\(p\ne0\). This is sufficient by an explicit triangular shear.
It is not a criterion for \(q=1\). Indeed,
\[
G=xz+y+xy^2=x(z+y^2)+y
\]
is a coordinate, although \(g=y+xy^2\) has general fiber
\(\mathbb C^*\) and is not a plane coordinate.

## Scope and verification

The proof closes a genuine monic-power branch, including
\(s^2+f(x,y)z^q+g(x,y)\), at every degree. It does not close
\(s^2+G\) for arbitrary three-variable \(G\), or
\(xu^2+G\) with nonconstant leading coefficient.

The separate [proof audit](separable-sum-independent-audit.md)
reconstructs the integral homology argument, the treatment of
disconnected fibers, the constant cases and the passage from
rectification of a fiber to its defining polynomial. This is a
written proof checked by separate model agents, not formal
proof-assistant verification or human expert review. The associated
exact tests check explicit inverse identities and boundary
counterexamples, not the general topological theorems.

## Sources

[^1]: András Némethi. [*Global Sebastiani-Thom theorem for polynomial
maps*](https://www.jstage.jst.go.jp/article/jmath1948/43/2/43_2_213/_pdf/-char/en).
Journal of the Mathematical Society of Japan 43 (1991), 213–218.
Theorem 2.4 and Corollary 2.5, p. 216. An alternative source is
[*Generalized local and global Sebastiani-Thom type theorems*](https://www.numdam.org/article/CM_1991__80_1_1_0.pdf),
Compositio Mathematica 80 (1991), Theorem G1 and Example 3.4(a).

[^2]: Shulim Kaliman and Mikhail Zaidenberg.
[*Affine modifications and affine hypersurfaces with a very transitive
automorphism group*](https://arxiv.org/pdf/math/9801076v2).
Theorem 7.2, pp. 28–29, especially rectifiability (iv) and the
pair statement (v); Example 7.1 for the rational/integral distinction.
