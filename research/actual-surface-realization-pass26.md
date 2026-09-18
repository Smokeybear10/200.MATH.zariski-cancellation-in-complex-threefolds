# Actual surface realization: invariant replacement and projection obstructions

For the verified four-generator embedding of the fixed pinched
surface, no invariant function can replace the two invariant
generators while the other two generators are retained:
\[
\boxed{R\ne\mathbb C[j,g,h]\quad\text{for every }j\in\ker\partial.}
\tag{1}
\]
This excludes arbitrary polynomial changes within the \((d,e)\)
plane followed by deleting one coordinate, not just bounded-degree
trials. Separately, every rank-three affine-linear projection of
the given embedding \(R=\mathbb C[d,e,g,h]\) fails.

The argument uses actual distinct points and the full pinched
cotangent space. It is not another module-only countercontrol.
A rank-nine free presentation over \(\mathbb C[g,h]\) is also
obtained, making future relative generator searches a finite exact
multiplication problem.

None of these results proves that \(R\) needs four abstract algebra
generators. Nonlinear transformations that change the retained pair
\((g,h)\), or three-generator presentations unrelated to this pair,
remain outside the exclusion. The prescribed ambient primitive-LND
realization in \(\mathbb C^{[3]}\) is still unresolved.

## 1. The fixed ring and coordinate functions

Use exactly the ring and gluing from
[the four-generator proof](nodal-elimination-pass23.md):
\[
B=\mathbb C[u,y,z]/(A(u)z-y(y-1)),\qquad
A(u)=(u-1)(u-i),\qquad d=u^4-1,\qquad e=du.
\]
The pinched ring \(R\subset B\) identifies the same three conductor
pairs, with the same shared parameter \(t\):
\[
((1,0),(i,0)),\qquad ((1,1),(-i,*)),\qquad
((-1,*),(i,1)).
\tag{2}
\]
The split-line parameter is \(t=z/[u_j(2\epsilon-1)]\);
on an ordinary line it is \(t=y/[u_jA(u_j)]\).

Keep the four coefficient polynomials
\[
b(u)=\frac{1-i}{4}(u+1)(u+i),\qquad
a(u)=-\frac i2A(u)\left(u+\frac{1+i}{2}\right),
\]
\[
q(u)=-u b(u)^2,\qquad r(u)=\frac i8uA(u),
\tag{3}
\]
and the two noninvariant generators
\[
g=a(u)+b(u)y,\qquad h=q(u)z+r(u)y.
\tag{4}
\]
Thus \(R=\mathbb C[d,e,g,h]\). On the three pairs,
\[
(g,h)=(0,t),\quad(1,-t),\quad(i,-t),
\tag{5}
\]
respectively. The full kernel is
\[
T=\ker\partial=\mathbb C+(u^4-1)\mathbb C[u].
\tag{6}
\]
The inherited normalization recovery proves
\(B=\mathbb C[u,g,h]\) by actual polynomial identities, not merely
after taking fraction fields.

## 2. A global point-collision lemma

Let \(j=j(u)\in T\). Suppose there is a nonzero
\(\zeta\in\mathbb C\) satisfying
\[
j(\zeta)=j(0).
\tag{7}
\]
Then \((j,g,h)\) does not separate the closed points of
\(\operatorname{Spec}R\).

The first point in the normalization is the actual section point
\[
P_\zeta=(u,y,z)=(\zeta,0,0).
\]
It has \(g=a(\zeta)\) and \(h=0\).
At \(u=0\), the coefficients satisfy
\[
A(0)=i,\qquad a(0)=b(0)=\frac{1+i}{4},\qquad q(0)=r(0)=0.
\tag{8}
\]
Consequently \(g\) takes every complex value on the smooth line
\(u=0\), while \(h\) vanishes identically there. More explicitly,
put
\[
y_0=\frac{a(\zeta)-a(0)}{b(0)},\qquad
z_0=\frac{y_0(y_0-1)}{i}.
\tag{9}
\]
The second actual point \(P_0=(0,y_0,z_0)\) belongs to \(B\),
has \(g=a(\zeta)\), \(h=0\), and has the same \(j\)-value
by (7).

Their images in \(\operatorname{Spec}R\) are distinct. If
\(\zeta^4=1\), the first lies on the conductor, where \(d=0\),
and the second has \(d=-1\). If \(\zeta^4\ne1\), both are
outside the conductor, where the normalization is an isomorphism;
their different \(u\)-values distinguish them there.
This proves the lemma, including conductor values of \(\zeta\).

If \(j\) is constant, the same argument applies with, for example,
\(\zeta=2\).

## 3. The remaining monomial case fails a pinched cotangent test

Suppose \(j\) is nonconstant and (7) has no nonzero solution.
Since \(\mathbb C\) is algebraically closed, a polynomial whose only
root is zero is a monomial. Therefore
\[
j(u)=c u^N+c_0,\qquad c\ne0,\quad N\ge1.
\tag{10}
\]
Membership in \(T\) means that the values at \(1,-1,i,-i\)
coincide. Applying this to (10) forces \(4\mid N\).
Writing \(N=4k\), we obtain
\[
j=c(d+1)^k+c_0,\qquad k\ge1.
\tag{11}
\]

We now use the entire three-dimensional cotangent space at a
closed conductor point, not just a normalization branch.
It suffices to use the first pair in (2). Let \(g'_1(t)\) and
\(g'_i(t)\) denote the two normal derivatives with respect to
\(u\), at fixed shared conductor parameter \(t\).
The surface equation gives
\[
g'_1(t)=(1-i)t-\frac12-i,\qquad
g'_i(t)=(1-i)t-\frac12+i.
\tag{12}
\]
For a split line this follows from
\(y_u=A'(u_j)u_jt\), together with
\(g_u=a'(u_j)+b'(u_j)\epsilon+b(u_j)y_u\).
The coefficient of \(t\) is therefore determined by the original
scaled gluing.

The normal derivatives of \(d\) on the pair are \(4,-4i\).
Hence
\[
\det
\begin{pmatrix}
g'_1(t)&g'_i(t)\\
4&-4i
\end{pmatrix}
=-8t-2-2i.
\tag{13}
\]
The common tangent direction has \(d_t=g_t=0\), \(h_t=1\).
Thus \((d,g,h)\) fails to span the full pinched cotangent space
at
\[
t_*=-\frac{1+i}{4}.
\tag{14}
\]
The unknown normal derivatives of \(h\) cannot repair this:
the common tangent column already has its only nonzero entry
in the \(h\)-row.

At the conductor, (11) gives \(dj=ck\,dd\), with \(ck\ne0\).
Therefore \((j,g,h)\) fails the same cotangent test at (14).
A generating triple would induce a closed embedding and a
surjection onto every local cotangent space, so this is impossible.

Together with Section 2, this proves (1) for every invariant \(j\).
In particular it covers every \(j\in\mathbb C[d,e]\), every
polynomial shear \(e\mapsto e+F(d)\) or \(d\mapsto d+F(e)\),
and every more complicated polynomial coordinate change inside
\(\mathbb C[d,e]\) followed by keeping just one of its coordinates.

The conclusion is tied to the retained pair \((g,h)\). It is not
an intrinsic prohibition on all embeddings involving an invariant.

### An exact nonlinear counterexample, without numerical roots

Consider the legitimate polynomial coordinate change
\[
(d,e,g,h)\longmapsto(d,e+d^2,g,h)
\]
of ambient affine four-space, and then delete \(d\).
For \(j=e+d^2\), one has \(j(0)=1\) and
\[
j(u)-1
=u\bigl(u^7+u^4-2u^3-1\bigr).
\tag{15}
\]
The degree-seven factor has a root \(\zeta\), and none of its roots
is zero or a fourth root of unity: it is coprime to
\(u(u^4-1)\). Every one of these algebraic roots therefore gives
the distinct smooth point pair (9) with identical \((j,g,h)\).
This nonlinear correction passes the elementary separation of
the \(u=0\) line from the conductor at \(j=0\), but fails globally
at the explicit locus (15).

## 4. Every affine-linear three-dimensional projection also fails

This includes projections which do not retain \(g,h\) individually.
Use coordinates \((d,e,g,h)\) on the verified ambient \(\mathbb A^4\).
The annihilating covectors of the three-dimensional Zariski tangent
spaces along the three conductor lines can be chosen as
\[
\begin{array}{c|rrrr}
\text{pair}&n_d&n_e&n_g&n_h\\ \hline
1&8i&-8t-2-2i&16(1+i)&0\\
2&14i&8it+4-6i&16(1-i)&0\\
3&14i&-8it-6+4i&16(-1+i)&0 .
\end{array}
\tag{16}
\]
For verification, on a pair with roots \(r_j,r_k\), the normal
columns in the first three coordinates are
\[
(4r_j^3,4,g'_j(t)),\qquad(4r_k^3,4,g'_k(t)).
\]
Their cross product gives (16). The common tangent direction is
\((0,0,0,\sigma)\), \(\sigma=1,-1,-1\), so \(n_h=0\).
The \(n_g\)-entry is nonzero, making each displayed covector an
actual defining equation of the full tangent space.

Let a rank-three linear projection have one-dimensional kernel
spanned by \(v=(v_d,v_e,v_g,v_h)\ne0\).

If \(v_e\ne0\), each evaluation \(n(t)\cdot v\) is a
nonconstant affine-linear polynomial in \(t\).
At one of its zeros, the projection kernel lies in the surface
tangent space. The projection then fails the required
cotangent-space surjectivity.

If \(v_e=0\) and \(v_d\ne0\), normalize to
\(v=(1,0,\alpha,\beta)\). Up to an invertible change of target
coordinates the projection is
\[
(e,\ g-\alpha d,\ h-\beta d).
\tag{17}
\]
On \(u=0\), its image is \((0,g+\alpha,\beta)\), with \(g\)
arbitrary. On conductor pair \(j\), with tag \(c_j=0,1,i\)
and sign \(\sigma_j\), its image is
\((0,c_j,\sigma_jt)\).
Take \(g=c_j-\alpha\) on \(u=0\) and
\(t=\sigma_j\beta\) on that conductor line.
These are distinct actual points with the same image.

If \(v_e=v_d=0\) and \(v_g\ne0\), normalize the projection to
\((d,e,h-\beta g)\). Each conductor line maps onto the entire
line \((0,0,*)\), so different conductor components collide.
If also \(v_g=0\), the projection drops \(h\) and collapses
each conductor line. These cases exhaust nonzero \(v\).

Translations in source or target do not change any of these
failures. Thus every rank-three affine-linear projection of
this particular embedding is excluded.

## 5. A rank-nine free multiplication presentation over the retained pair

The same functions also give a tractable global algebra.
Set \(S=\mathbb C[G,H]\), where \(G,H\) will map to \(g,h\),
and define
\[
F(U,G,H)=\frac4{1-i}
 \bigl(b(U)A(U)H+
 U b(U)(G-a(U))(G-a(U)-b(U))
 -A(U)r(U)(G-a(U))\bigr).
\tag{18}
\]
Its degree in \(U\) is nine and its leading coefficient is
the nonzero constant \(-1/4\); its coefficient of \(H\) is
\(U^4-1\). The surface relation gives \(F(u,g,h)=0\).

In fact
\[
B\cong S[U]/(F).
\tag{19}
\]
The previously proved recovery gives surjectivity.
To check the only relation, \(F\) is primitive and linear in
\(H\). At each fourth root of unity \(r\), the polynomial
\(F(r,G,H)\) is nonzero in \(G\). Hence its constant coefficient
in \(H\) is coprime to its \(H\)-coefficient \(U^4-1\).
It is therefore irreducible. The kernel of the surjection to
the domain \(B\) has height one and is generated by \(F\).
In particular \(G,H\) are algebraically independent, and the
monic multiple \(-4F\) proves that \(B\) is free of rank nine
over \(S\), with basis \(1,u,\ldots,u^8\).

Write
\[
Q(G)=G(G-1)(G-i),\qquad
L_1(G)=1-i+2iG,\qquad
L_3(G)=(2-2i)G^2-2G+1+i.
\tag{20}
\]
As an \(S\)-module, the actual conductor difference quotient is
\[
B/R\cong S/(Q).
\tag{21}
\]
This is a module statement, not a ring quotient identification.
At \(G=0,1,i\), take the difference of the two restrictions in
each original pair and identify \(H\) with the common \(h\)-value.
The difference of \(u^n\) is periodic with period four, and
the four residue polynomials are
\[
0,\quad L_1,\quad 2,\quad L_3 .
\tag{22}
\]
In particular \(u^2\) has difference exactly \(2\) on every
pair, so this \(S\)-linear quotient map is surjective.

The exact kernel of this map has the following free \(S\)-basis:
\[
\begin{split}
\mathcal E=\big(&1,\ u-\tfrac12L_1u^2,\ Qu^2,\
 u^3-\tfrac12L_3u^2,\ u^4,\\
&u^5-\tfrac12L_1u^2,\ u^6-u^2,\
 u^7-\tfrac12L_3u^2,\ u^8\big).
\end{split}
\tag{23}
\]
Indeed subtract the displayed multiples of the \(u^2\)-column.
All eight other columns then have zero residue, while a
coefficient of \(u^2\) has zero residue exactly when it is
divisible by \(Q\). This proves generation and independence
directly. The change-of-basis determinant into the basis of
\(B\) is \(Q\), not a unit; this is precisely the conductor
index, not a mistaken assertion that \(B=R\).

Thus \(R\) is finite free of rank nine over \(\mathbb C[g,h]\).
Its exact multiplication is obtained by reducing products
modulo the monic polynomial \(-4F\) and then expressing them
in (23). All divisions by \(Q\) in this second operation are
exact because the product belongs to the actual subring \(R\).

This gives a finite, exact criterion for a future candidate
\(j\in R\) retaining \(g,h\). Form the nine columns
\(1,j,\ldots,j^8\) in the basis (23). Then
\[
R=S[j]\quad\Longleftrightarrow\quad
\det(1,j,\ldots,j^8)\in\mathbb C^*.
\tag{24}
\]
Cayley-Hamilton for multiplication by \(j\) shows that all
higher powers are \(S\)-linear combinations of these nine.
Therefore the determinant is a unit exactly when they span
the whole free module. This criterion includes noninvariant
\(j\), although (1) already settles every invariant \(j\).

No assertion is made that an arbitrary three-generator
presentation of \(R\) would preserve this particular \(S\).

## Verification and scope

The new [standalone checker](actual_surface_checks_pass26.py)
uses only unittest and SymPy. It checks (18) against the original
surface, all conductor differences and the exact basis
determinant, the full tangent covectors, the actual point-collision
formulas, monomial descent at the four roots, the nonlinear
counterexample (15), and the cases of the affine projection proof.

All ring-theoretic recognition, the all-degree root argument,
and the all-projection case split are written proofs.
No grid, floating-point sample, or solver-dependent module is used.

The targeted run passed all seven methods in 0.250 seconds.

~~~sh
/opt/anaconda3/bin/python research/actual_surface_checks_pass26.py
~~~

The inherited primary geometric construction is the fixed
conductor pinch, its normalization, and its local two-branch
model from [pass 20](nodal-conductor-pass20.md), with the explicit
global generator proof from [pass 23](nodal-elimination-pass23.md).
This pass invokes no new external classification of LNDs or
affine embeddings. Its statements are elementary consequences
of that actual algebra and gluing.

The bounded result stops here. The unresolved choice
\(3\le\mu_{\mathbb C}(R)\le4\) has not changed. Any further
attempt must change the retained pair or use a noninvariant
new generator not covered by (1), and must separately establish
the prescribed ambient invariant subring and primitive LND.
