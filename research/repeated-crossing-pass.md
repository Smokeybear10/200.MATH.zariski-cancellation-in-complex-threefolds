# Repeated crossing coefficients: a complete branch and a jet boundary

The subsequent [original-slice argument](repeated-crossing-slice-descent.md)
settles the entire monomial-coefficient family under \(D(F)=1\) on the
original four-variable ring. The remaining coordinate questions below
concern the stronger stable-coordinate hypothesis alone, not that
already-closed original-slice case.

Let
\[
F=x^r y^s u+H(x,y,z),\qquad r,s\geq1,
\]
over \(\mathbb C\), and put \(h(z)=H(0,0,z)\). The following conclusions are proved here.

* If \(h\) is nonconstant, stable-coordinate descent holds for every pair
  \((r,s)\), without a degree bound on \(H\). The exact criterion and a
  polynomial inverse are given below.
* If \(h\) is constant, stability forces the same reduced-divisor residues
  as in the simple crossing case. Proving this requires the integral
  residue map, since the earlier critical-point argument does not survive
  repeated factors.
* For \(xy^2u+H\) of total degree at most four, those residues leave explicit
  first-order terms along \(y=0\). Smoothness imposes no additional conditions
  on these terms. Their general coordinate status is not decided here.

In particular, this note does not claim a solution of the constant-axis
quartic family or a new result about the Vénéreau polynomial. Its inverse
construction and residue calculations are written proofs, not conclusions
from a parameter grid.

## 1. The complete nonconstant-axis theorem

Suppose \(h\) is nonconstant. Then the following conditions are equivalent:

1. \(F\) is a coordinate.
2. \(F\) is a stable coordinate.
3. There are \(a\in\mathbb C^*\), \(b\in\mathbb C\),
   \(B\in\mathbb C[x]\), \(C\in\mathbb C[y]\), and
   \(R\in\mathbb C[x,y,z]\), with \(B(0)=C(0)=0\), such that
   \[
   H=az+b+B(x)+C(y)+xyR(x,y,z).
   \tag{1}
   \]

The implication from (1) to a coordinate produces coordinates containing
both \(x\) and \(y\). An LND slice also satisfies these conditions, since a
slice is a coordinate after one stabilization.

### Necessity uses the reduced divisor only

For a stable coordinate, each fiber \(X_\lambda=V(F-\lambda)\) is smooth
and contractible, with integral compactly supported cohomology only
\(H_c^6(X_\lambda)=\mathbb Z\). Its open subset on \(xy\ne0\) is
\[
U\cong(\mathbb C^*)^2\times\mathbb A^1,
\]
and its reduced closed complement is
\[
Z_\lambda=(C_{x,\lambda}\cup C_{y,\lambda})\times\mathbb A^1_u,
\]
where
\[
C_{x,\lambda}=V(H(0,y,z)-\lambda),\qquad
C_{y,\lambda}=V(H(x,0,z)-\lambda).
\]
Neither the open set nor the reduced closed complement depends on \(r,s\).

Choose a generic \(\lambda\) for which both plane curves are smooth and
\(h(z)-\lambda\) has \(d=\deg h\) distinct roots. Their intersection consists
of exactly these \(d\) points. The closed-open sequence gives
\[
H_c^1(C_{x,\lambda}\cup C_{y,\lambda})=\mathbb Z,
\qquad
H_c^2(C_{x,\lambda}\cup C_{y,\lambda})=\mathbb Z^2.
\]
The Mayer--Vietoris calculation in the
[nonconstant simple-crossing proof](crossing-nonconstant-pass.md) now
applies verbatim to these reduced subsets. The top group makes both plane
curves connected; the degree-one sequence is
\[
0\longrightarrow\mathbb Z^d\longrightarrow\mathbb Z
\longrightarrow H_c^1(C_{x,\lambda})\oplus H_c^1(C_{y,\lambda})
\longrightarrow0.
\]
It follows that \(d=1\) and that both plane curves are affine lines.

The plane-line rectification theorem makes each plane polynomial a
coordinate. Its use is exactly the one recorded, with a source, in the
linked proof. The chosen regular fibers are reduced and irreducible, so
there is no hidden power of a line equation. Finally, a plane coordinate
\(q(t,z)\) with \(q(0,z)=az+b\) must equal \(az+Q(t)\). To recall the
short argument, choose a companion \(V\). In the \((q,V)\)-plane the line
\(t=0\) is the graph of a polynomial in \(q\). Thus \(t\) is a scalar
multiple of \(V-S(q)\), and \((t,q)\) is a coordinate pair. A one-variable
automorphism over \(\mathbb C[t]\) is affine in \(z\).

Consequently
\[
H(0,y,z)=az+b+C(y),\qquad
H(x,0,z)=az+b+B(x).
\]
Their common remainder is divisible by \(xy\), proving (1). This necessity
uses generic smooth plane fibers. It does not infer their smoothness from
cancellation of a derivative involving \(u\).

### Sufficiency lifts a finite inverse modulo the coefficient

Write
\[
A=\mathbb C[x,y],\quad p=x^r y^s,\quad n=xy,\quad
D=b+B(x)+C(y),\quad q(z)=az+D+nR(x,y,z).
\]
Let \(N=\max(r,s)\), so that \(n^N\in(p)\). Define polynomials in \(A[T]\)
by
\[
I_0(T)=\frac{T-D}{a},\qquad
I_{j+1}(T)=\frac{T-D-nR(x,y,I_j(T))}{a}.
\tag{2}
\]
Set \(I=I_{N-1}\). If \(N=1\), no update is needed. Then
\[
q(I(T))-T\in(n^N),\qquad I(q(z))-z\in(n^N).
\tag{3}
\]
For the first assertion, the initial error is in \((n)\). The difference
between successive iterates is minus the preceding error divided by
\(a\), so substitution into \(R\), followed by multiplication by \(n\),
increases its order by one. For the second assertion, the initial error
is again in \((n)\), and
\[
I_{j+1}(q(z))-z
=\frac n a\bigl(R(x,y,z)-R(x,y,I_j(q(z)))\bigr)
\]
increases that order by one. These are polynomial divisibility statements;
no convergence or completion is being invoked.

Since \(F=pu+q(z)\), (3) makes
\[
V=\frac{z-I(F)}p
\tag{4}
\]
a polynomial in \(A[z,u]\). The inverse of \((x,y,z,u)\mapsto(x,y,F,V)\)
is
\[
z=I(S)+pV,\qquad
u=\frac{S-q(I(S)+pV)}p,
\tag{5}
\]
where \(S\) is the new coordinate corresponding to \(F\). The second
expression is polynomial because its numerator is zero modulo \(p\)
by (3). Substitution verifies both compositions: (5) gives \(F=S\),
and then (4) gives the prescribed \(V\); in the other direction, (4)
first recovers \(z\), and the defining equation for \(F\) recovers \(u\).
This proves sufficiency for all exponents and all degrees.

For the requested coefficient \(xy^2\), only one update is needed:
\[
I(T)=\frac{T-D}{a}
-\frac{xy}{a}R\!\left(x,y,\frac{T-D}{a}\right).
\]

## 2. Necessary constant-axis residues for every multiplicity

Assume now \(h(z)=b\). If \(F\) is stable, then one of the following two
forms holds:
\[
\begin{aligned}
\text{A:}\quad&H=ay+cx^kz+B(x)+xyR(x,y,z),\\
\text{B:}\quad&H=ax+cy^kz+C(y)+xyR(x,y,z),
\end{aligned}
\tag{6}
\]
where \(a,c\ne0\), \(k\geq1\), and \(B(0)=C(0)=b\). This is a necessary
condition for arbitrary \(r,s\); sufficiency for arbitrary multiplicities
is not asserted.

### Generic strata and the affine-line restriction

Put \(f(y,z)=H(0,y,z)\) and \(g(x,z)=H(x,0,z)\). Both are nonconstant.
For example, if \(f=b\), then on any fiber with value different from
\(b\), the function \(x\) is a nonconstant unit. This is impossible on
a stably affine-space fiber.

For generic \(\lambda\ne b\), the two plane curves are smooth, nonempty,
and disjoint. The reduced closed complement is their disjoint union
times \(\mathbb A^1\). As in the
[constant simple-crossing calculation](crossing-coefficient-pass.md),
the compact-support groups force each to be connected, with their
\(H_c^1\) ranks summing to one. Thus one curve is \(\mathbb A^1\) and
the other is \(\mathbb C^*\).

One plane supplies the affine line for infinitely many values. Suppose
it is the \(x=0\) plane. The unit \(y\) on each such line is constant,
so these are infinitely many distinct vertical lines. Therefore
\(f_z=0\). Connected generic fibers then force \(f=ay+b\), with
\(a\ne0\). For every generic value, the other curve is \(\mathbb C^*\).
The opposite choice gives the other orientation in (6).

### The integral residue map fixes the degree of the punctured line

Fix such a generic value, and write \(X=X_\lambda\),
\(Z_x=C_{x,\lambda}\times\mathbb A^1\), and
\(Z_y=C_{y,\lambda}\times\mathbb A^1\). These are disjoint smooth
divisors of the smooth threefold \(X\). Moreover, \(x\) vanishes to
order exactly one along \(Z_x\), and \(y\) to order exactly one along
\(Z_y\). Indeed,
\[
\mathcal O(X)/(x)=\mathbb C[y,z,u]/(f-\lambda),\qquad
\mathcal O(X)/(y)=\mathbb C[x,z,u]/(g-\lambda)
\]
are reduced at the chosen regular values. The multiplicity of \(x\)
or \(y\) in the coefficient \(x^ry^s\) does not change these orders.

The ordinary integral Gysin sequence for their complement contains
\[
H^2(X;\mathbb Z)\longrightarrow H^2(U;\mathbb Z)
\xrightarrow{\operatorname{res}}
H^1(Z_x\sqcup Z_y;\mathbb Z)
\longrightarrow H^3(X;\mathbb Z).
\tag{7}
\]
Stability makes the outside groups zero, so the residue map is an
isomorphism \(\mathbb Z\to\mathbb Z\).

Let \(\alpha,\beta\) be the integral classes obtained by pulling back
the standard generator of \(H^1(\mathbb C^*;\mathbb Z)\) under \(x,y\).
Their cup product generates \(H^2(U;\mathbb Z)\). Up to a consistent
orientation sign, its residues are
\[
\operatorname{res}(\alpha\smile\beta)
=\bigl(\beta|_{Z_x},-\alpha|_{Z_y}\bigr).
\tag{8}
\]
This follows by taking a positively oriented small normal circle around
each divisor. The order-one assertions above ensure no additional
multiplicity in (8).

In orientation A, \(y\) is constant on the affine-line stratum. On the
punctured-line stratum, choose a coordinate \(t\) and write its unit
\(x=d t^m\), with \(d\ne0\). The exponent is nonzero: otherwise that
closed irreducible curve would lie in a vertical affine line and equal
that line, contrary to its being \(\mathbb C^*\). Equations (7)--(8)
show that multiplication by \(m\) is an integral isomorphism. Hence
\[
|m|=1.
\tag{9}
\]
Thus \(x:C_{y,\lambda}\to\mathbb C^*\) is an isomorphism.

For a general nonzero \(x\), the polynomial \(g(x,z)-\lambda\) now has
exactly one simple root. This forces \(\deg_z g=1\), so
\(g=A(x)z+B(x)\). Surjectivity and singleton fibers over every nonzero
\(x\) imply \(A(x)\ne0\) there: a zero would give either no root or
an entire vertical line. Therefore \(A(x)=cx^k\). The constant axis
condition gives \(k\geq1\) and \(B(0)=b\). This proves A in (6).
Interchanging the two strata in this argument proves B. The exchange
is in the argument, not an assertion that unequal coefficient
multiplicities are symmetric.

## 3. What the degree-four first jets actually leave

Now specialize to
\[
F=xy^2u+H,\qquad \deg H\leq4.
\]
After subtracting a term \(xy^2K\) from \(H\) and replacing
\(u\) by \(u+K\), the constant-axis possibilities (6) are exactly
the following necessary residue families:
\[
\begin{aligned}
\text{A:}\quad&F=xy^2u+ay+cx^kz+B(x)+xyR_0(x,z),\\
\text{B:}\quad&F=xy^2u+ax+cy^kz+C(y)+xyR_0(x,z),
\end{aligned}
\tag{10}
\]
with \(a,c\ne0\), \(1\leq k\leq3\), \(\deg B,\deg C\leq4\),
and \(\deg R_0\leq2\). The removed \(K\) has degree at most one.
The polynomial \(R_0\) records precisely the coefficient of \(y\)
in the mixed remainder modulo \(y^2\), after the two plane restrictions
have been fixed. It has the six-parameter form
\[
R_0(x,z)=A_2z^2+(A_1x+A_0)z+D_2x^2+D_1x+D_0.
\tag{11}
\]
Equations (10)--(11) are necessary under stability, not a claimed
classification of which jets are stable or ordinary coordinates.

### Smoothness adds no conditions to (10)

For the repeated coefficient,
\[
F_u=xy^2,\quad F_x=y^2u+H_x,\quad
F_y=2xyu+H_y,\quad F_z=H_z.
\tag{12}
\]
At \(y=0\), both terms involving \(u\) in the base derivatives vanish.
In particular, a critical point of \(g=H(x,0,z)\) cannot in general be
turned into a critical point of \(F\) by choosing \(u\).

Every member of (10) is nevertheless a submersion. In A, \(F_y=a\)
on \(x=0\), while \(F_z=cx^k\ne0\) on \(y=0,x\ne0\). In B,
\(F_x=a\) on \(y=0\), while \(F_z=cy^k\ne0\) on \(x=0,y\ne0\).
Away from those planes, \(F_u\ne0\). These checks apply to every choice
of the jet coefficients in (11). They therefore cannot remove any of
the remaining parameters.

### Two positive subfamilies

Orientation A with \(k=1\) is always a coordinate. Put
\[
T=cz+yR_0(x,z)+y^2u.
\]
The finite-inverse construction of Section 1, applied over
\(\mathbb C[x,y]\) with coefficient \(y^2\) and nilpotent perturbation
\(yR_0\), shows that \((x,y,T,V)\) is a coordinate system for a
polynomial companion \(V\). But
\[
F=ay+B(x)+xT,
\]
so replacing \(y\) by \(F\) is an invertible affine operation over
\(\mathbb C[x,T,V]\). This proof permits arbitrary degrees in \(R_0\).

Also, in A with arbitrary \(k\), if \(R_0\) is independent of \(z\),
then \(F\) is linear in \(z\) with coefficient \(cx^k\). Its remainder
at \(x=0\) is \(ay+b\), a coordinate. The published univariate
coefficient criterion, recorded in
[the multiple-root proof](multiple-root-linear-pass.md), applies and
gives a coordinate containing \(x\).

The remaining A cases have \(k=2\) or \(3\) and \(z\)-dependent jets;
this note does not settle B in general either. In particular,
\[
xy^2u+y+x^2z+xyz^2
\tag{13}
\]
is the specified Vénéreau candidate in A with \(k=2\) and
\(R_0=z^2\). No conclusion about its current literature status follows
from the reductions here. At \(x=0\), the constant-axis normal form is
independent of \(z,u\), so it cannot be a coordinate over
\(\mathbb C[x,y]\). The fixed-\((x,y)\) inverse of Section 1 therefore
cannot be transferred to this branch by formally dividing by \(cx^k\).

## 4. A smooth counterexample to the rank-only shortcut

Consider
\[
F_0=xy^2u+y+xz^2.
\tag{14}
\]
It is a submersion. Its derivatives are
\[
(F_{0,x},F_{0,y},F_{0,z},F_{0,u})
=(y^2u+z^2,\ 1+2xyu,\ 2xz,\ xy^2).
\]
If \(xy^2=0\), either \(x=0\) or \(y=0\), and in either case
\(F_{0,y}=1\). Elsewhere \(F_{0,u}\ne0\). Thus every fiber is smooth.

Fix \(\lambda\ne0\). Its closed strata are
\[
Z_x=\{x=0,y=\lambda\}\cong\mathbb A^2_{z,u},\qquad
Z_y=\{y=0,xz^2=\lambda\}\cong\mathbb C^*_z\times\mathbb A^1_u.
\]
They are disjoint and smooth. The ideals \((x)\) and \((y)\) in the
fiber ring have the respective reduced quotients
\[
\mathbb C[z,u],\qquad
\mathbb C[x,z,u]/(xz^2-\lambda)
\cong\mathbb C[z,z^{-1},u].
\]
Hence their orders of vanishing along these divisors are one.

The complement is again \(U\cong(\mathbb C^*)^2\times\mathbb A^1\).
All groups needed in the ordinary Gysin sequence are therefore
\[
H^1(U)=\mathbb Z^2,\quad H^2(U)=\mathbb Z,\quad H^3(U)=0,
\]
and
\[
H^0(Z_x\sqcup Z_y)=\mathbb Z^2,\quad
H^1(Z_x\sqcup Z_y)=\mathbb Z,\quad
H^j(Z_x\sqcup Z_y)=0\quad(j\geq2).
\]
The map \(H^1(U)\to H^0(Z_x\sqcup Z_y)\) is the identity matrix up
to orientation signs: \(x\) vanishes simply only on \(Z_x\), and
\(y\) simply only on \(Z_y\). Thus \(H^1(X_\lambda)=0\). On the
punctured-line stratum,
\[
x=\lambda z^{-2},
\]
so the next residue map \(H^2(U)\to H^1(Z_x\sqcup Z_y)\) is
multiplication by \(2\), up to sign. Exactness yields
\[
H^2(X_\lambda;\mathbb Z)=0,\qquad
H^3(X_\lambda;\mathbb Z)=\mathbb Z/2.
\tag{15}
\]
For completeness, the fiber is connected since its irreducible open
subset \(U\) is dense: both closed strata are divisors and neither can
contain a component of the smooth threefold. The same Gysin sequence
gives \(H^j(X_\lambda;\mathbb Z)=0\) for \(j\geq4\), since the adjacent
groups of \(U\) and of the strata vanish. Thus its ordinary integral
cohomology is \(\mathbb Z\) in degree zero, \(\mathbb Z/2\) in degree
three, and zero otherwise.

In particular, (14) is not a stable coordinate. Its generic reduced
strata have exactly the affine-line and punctured-line types demanded
by the earlier rank calculation, and its nonzero fibers are rationally acyclic.
The integral residue map detects the obstruction. This example explains
both why critical-point-freeness cannot replace the missing smoothness
argument on the repeated component and why ranks alone do not prove the
constant-axis normal form.

### The same example gives torsion of every order

More generally, set
\[
F_{r,s,q}=x^r y^s u+y+xz^q,
\qquad r\geq1,\ s\geq2,\ q\geq2.
\tag{16}
\]
Every such polynomial is a submersion. On \(xy\ne0\), its derivative
with respect to \(u\) is nonzero. On \(x=0\) or \(y=0\), its derivative
with respect to \(y\) is one; the assumption \(s\geq2\) matters here.
For \(\lambda\ne0\), its closed strata have the same types as above,
and on the second one
\[
x=\lambda z^{-q}.
\]
Both divisors are still reduced: their quotient rings are
\(\mathbb C[z,u]\) and \(\mathbb C[z,z^{-1},u]\). The first residue
matrix is again the identity up to signs, and the second map is
multiplication by \(q\). Consequently the full ordinary integral
cohomology of a nonzero fiber is
\[
H^j(F_{r,s,q}^{-1}(\lambda);\mathbb Z)=
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/q,&j=3,\\
0,&\text{otherwise}.
\end{cases}
\tag{17}
\]
The group in (17) is ordinary \(H^3\), not compactly supported
cohomology.

Every fiber of (16), including the zero fiber, has compactly supported
Euler characteristic one. For a nonzero value, the closed strata have
Euler characteristics one and zero, and the open set \(U\) has Euler
characteristic zero. At value zero, the reduced closed set is the union
of the two affine planes
\[
\{x=y=0\},\qquad\{y=z=0\}
\]
inside the four-variable ambient space, each with the free coordinate
\(u\), and their intersection is the \(u\)-line. Its Euler
characteristic is therefore \(1+1-1=1\), while the open part again
contributes zero. Thus smoothness and the Euler characteristics of all
fibers miss integral obstructions of every order \(q\).
