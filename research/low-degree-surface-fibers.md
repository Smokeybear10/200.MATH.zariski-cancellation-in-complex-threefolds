# Low-degree polynomials with rationally acyclic surface fibers

Let \(G\in\mathbb C[x,y,z]\) be nonconstant. If its general fiber is
smooth and rationally acyclic and \(\deg G\le3\), then \(G\) is a
coordinate. The corresponding degree-four argument only gives a
quadratic-in-one-variable normal form. It does not classify quartics.

Here a general fiber means a fiber over a nonempty Zariski open subset
of the parameter line. The cubic conclusion uses the general-fiber
binomial result in [generic-rational-binomial-pass.md](generic-rational-binomial-pass.md).
The infinity argument below needs only one smooth fiber of Euler
characteristic one, but that weaker hypothesis is not substituted for
generic rational acyclicity in the coordinate conclusion.

## 1. The surface infinity lemma

Write \(G=g_d+g_{d-1}+\cdots+g_0\), where \(g_i\) is homogeneous
of degree \(i\), and assume \(d\ge3\). Define

\[
J(g_d)=V(\partial_xg_d,\partial_yg_d,\partial_zg_d)
\subset\mathbb P^2.
\]

If some fiber \(X_\lambda=G^{-1}(\lambda)\) is smooth and
\(\chi(X_\lambda)=1\), then

\[
J(g_d)\cap V(g_{d-1})\ne\varnothing.                 \tag{1}
\]

The Jacobian locus here is that of the actual leading polynomial,
including its multiplicities. Replacing \(g_d\) by its squarefree
part before forming this locus would change the assertion.

Suppose, to the contrary, that the intersection in (1) is empty.
Every positive-dimensional projective closed subset of \(\mathbb
P^2\) meets every positive-degree projective hypersurface. Hence
\(J(g_d)\) is finite or empty. If \(g_{d-1}=0\), the assumed
empty intersection already says \(J(g_d)=\varnothing\).

The plane curve \(S=V(g_d)\) is therefore reduced: a repeated
irreducible factor of \(g_d\) would put its entire curve in the
Jacobian locus. Euler's homogeneous identity shows that
\(J(g_d)\subset S\), so \(S\) has only isolated singularities.
It need not be irreducible. Reduced plane curves with several
components can have finite singular locus.

Homogenize the selected fiber in \(\mathbb P^3\), with coordinate
\(t\) at infinity:

\[
Y_\lambda=V\bigl(g_d+t g_{d-1}+\cdots+
t^{d-1}g_1+t^d(g_0-\lambda)\bigr).
\]

At \(t=0\), its gradient consists of the three partial derivatives
of \(g_d\) and \(g_{d-1}\). Thus the contrary assumption makes
\(Y_\lambda\) smooth at infinity. It is smooth on \(t\ne0\)
because \(X_\lambda\) is smooth. Consequently \(Y_\lambda\)
is a smooth degree-\(d\) projective surface, with boundary \(S\).

The Euler characteristics of a smooth degree-\(d\) surface in
\(\mathbb P^3\) and a smooth degree-\(d\) curve in
\(\mathbb P^2\) are respectively

\[
E_2(d)=d(d^2-4d+6),\qquad E_1(d)=d(3-d).
\]

For a reduced plane curve with isolated singularities, smoothing
gives

\[
\chi(S)=E_1(d)+\sum_{p\in\operatorname{Sing}S}\mu_p.
\]

These are the cases of complex dimensions two and one in
[Maxim, Păunescu and Tibăr, *Vanishing cohomology and Betti bounds
for complex projective hypersurfaces*, (1.3) and Remark 3.2,
(3.11)](https://www.numdam.org/item/10.5802/aif.3486.pdf).
The sign is positive for the singular boundary curve: a local curve
Milnor fiber has Euler characteristic \(1-\mu_p\). The formulas
do not require the reduced boundary curve to be irreducible.

Additivity of compactly supported Euler characteristic now gives

\[
\begin{aligned}
\chi_c(X_\lambda)
 &=E_2(d)-E_1(d)-\sum_p\mu_p\\
 &=1+(d-1)^3-\sum_p\mu_p.
\end{aligned}                                                   \tag{2}
\]

For the reduced plane curve \(S\), the polar-degree identity is

\[
\deg(\operatorname{grad}g_d)=(d-1)^2-\sum_p\mu_p\ge0.
\]

See [Huh, *Milnor numbers of projective hypersurfaces with isolated
singularities*, Section 1.1, first displayed polar-degree
formula](https://arxiv.org/pdf/1210.2690). A nondominant gradient
map has polar degree zero, so cones are included in this bound.
The cone exclusion in Huh's stronger theorem is not used here.
Combining this bound with (2) yields

\[
\chi_c(X_\lambda)
\ge 1+(d-1)^2(d-2)>1.                              \tag{3}
\]

Since \(X_\lambda\) is a smooth complex surface with finite Betti
numbers, Poincaré duality in even real dimension gives
\(\chi_c(X_\lambda)=\chi(X_\lambda)\). This contradicts the
hypothesis and proves (1).

### An independent boundary check

The required bound can also be proved without polar maps. Let
\(r\) be the number of irreducible components of the reduced
plane curve \(S\), and let their normalizations have genera
\(h_1,\ldots,h_r\). If \(b_p\) is the number of local branches
at a singular point, normalization gives

\[
\chi(S)=2r-2\sum_i h_i-\sum_p(b_p-1).
\]

A projective plane curve is connected. The incidence graph of its
normalization components and singular points is therefore connected,
which implies \(\sum_p(b_p-1)\ge r-1\). Thus

\[
\chi(S)\le r+1\le d+1
=E_1(d)+(d-1)^2.
\]

Subtracting from \(E_2(d)\) reproduces (3), including the
reducible and cone cases. For example, three concurrent lines have
\(\chi(S)=4\), one ordinary triple point with \(\mu=4\),
and polar degree zero. A smooth cubic surface with this boundary
has affine Euler characteristic \(9-4=5\), not one.

## 2. A direction with lower polynomial degree

Choose a point from (1) and make it the \(u\)-axis by a linear
change of the three affine variables. Denote the other variables
by \(x,y\). Write the two highest homogeneous pieces as

\[
g_d=a u^d+u^{d-1}L(x,y)+R_d,
\qquad \deg_u R_d\le d-2,
\]

\[
g_{d-1}=b u^{d-1}+R_{d-1},
\qquad \deg_u R_{d-1}\le d-2.
\]

The vanishing of the three derivatives of \(g_d\) at the chosen
axis point gives \(a=0\) and \(L=0\). The other condition in
(1) gives \(b=0\). All remaining homogeneous pieces already
have \(u\)-degree at most \(d-2\). Hence

\[
\deg_uG\le d-2.                                    \tag{4}
\]

Only a linear change was used, so total degree has not increased.

## 3. Degrees one and two

A nonconstant degree-one polynomial is a coordinate. For degree
two, write \(G=q+\ell+c\) with quadratic part \(q\), of rank
\(r\).

If \(\ell\) is nonzero on the radical of \(q\), choose a
radical direction on which \(\ell\) is nonzero. In suitable
linear coordinates, \(G=a u+H(x,y)\), with \(a\ne0\), so
\(G\) is a coordinate.

Otherwise an affine change completing squares removes the linear
part in the nondegenerate directions, leaving a nondegenerate
rank-\(r\) quadratic form plus a constant, independent of the
remaining \(3-r\) variables. At a general level the possibilities
are as follows.

| Rank | General fiber | Euler characteristic |
| --- | --- | --- |
| 1 | Two disjoint copies of \(\mathbb A^2\) | 2 |
| 2 | \(\mathbb C^*\times\mathbb A^1\) | 0 |
| 3 | A smooth affine quadric surface | 2 |

For the last entry, the projective closure is a smooth quadric
surface with Euler characteristic four, and its boundary is a
smooth conic with Euler characteristic two. Thus none of these
cases has generic Euler characteristic one. This argument uses
the generic fiber, not an unsupported assertion that every
quadratic polynomial under consideration is a submersion.

## 4. Cubic coordinatehood

Assume \(\deg G=3\) and the general fiber is smooth and
rationally acyclic. By (4), after a linear change,

\[
G=P(x,y)u+Q(x,y),\qquad \deg P\le2,\quad\deg Q\le3.
\]

If \(P\ne0\), apply the general rationally acyclic binomial
criterion with exponent one. This gives that \(G\) is a
coordinate. The required generic-level transversality and the
constant-coefficient cases are proved in
[generic-rational-binomial-pass.md, Sections 1 to 3 and
5](generic-rational-binomial-pass.md), using
[Kaliman and Zaidenberg, *Affine modifications and affine
hypersurfaces with a very transitive automorphism group*, Lemmas
7.5(b), 7.6(b) and Proposition 7.1](https://arxiv.org/pdf/math/9801076).
No integral-acyclicity assumption is added in this application.

If \(P=0\), a general fiber is
\(V(Q-\lambda)\times\mathbb A^1\). Its smoothness and rational
acyclicity make the plane curve \(V(Q-\lambda)\) smooth,
connected and rationally acyclic. A smooth connected affine curve
with Euler characteristic one has genus zero and exactly one
point at infinity, hence is isomorphic to \(\mathbb A^1\).
Plane-line rectification makes \(Q\) a coordinate of
\(\mathbb C[x,y]\), and therefore makes \(G\) a coordinate
of \(\mathbb C[x,y,u]\). The needed rectification theorem is
stated in [Nguyen Van Chau, *Polynomial maps of the complex plane
with the branched value sets isomorphic to the complex line*,
Section 2, before Lemma 1](https://math.ac.vn/uploads/files/0202197.pdf).

Together with Section 3, this proves the degree-at-most-three
claim. The proof establishes absolute coordinatehood. It does not
preserve an arbitrarily specified original variable or establish
a relative coordinate pair with that variable.

## 5. The exact degree-four output

For a degree-four polynomial with a smooth fiber of Euler
characteristic one, the same argument gives

\[
G=A(x,y)u^2+B(x,y)u+C(x,y),
\qquad \deg A\le2,\quad\deg B\le3,\quad\deg C\le4.
\]

If \(A=0\) and the general fiber is rationally acyclic, the
binomial criterion again proves coordinatehood. If \(A\ne0\),
the infinity lemma alone does not settle the quadratic branch.
In particular, neither Euler characteristic one nor this normal
form is a quartic coordinate criterion.

For arithmetic validation, six exact SymPy assertions checked the
curve and surface Chern-class formulas, their difference, the
simplified lower bound, and the numerical bounds five and nineteen
for degrees three and four. These checks validate the displayed
arithmetic, not the geometric inputs to the proof.
