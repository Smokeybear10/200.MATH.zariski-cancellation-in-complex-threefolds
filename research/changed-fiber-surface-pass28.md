# All invariant fibers of the fixed pinched surface

For the unchanged surface and its specified descended action, an exact
criterion determines which invariant functions have a nonplanar fiber.
It excludes an infinite-dimensional class of invariant functions from
**every** three-element generating set, with no retained companion pair.

The converse is equally important: many other invariant functions,
including \(d=u^4-1\), have planar fibers at every value. Thus an
argument based only on the abstract embeddability of individual
invariant fibers cannot exclude all generating triples.

This does not decide whether the surface embeds in \(\mathbb A^3\).
It also does not construct the much stronger prescribed ambient
primitive locally nilpotent action.

## 1. Fixed ring and statement

Here and throughout this note, fibers are scheme-theoretic closed fibers
over complex values, not fibers over the generic point of the base.

Keep the exact normalization, conductor and original gluing:
\[
B=\mathbb C[u,y,z]/(A(u)z-y(y-1)),\quad
A(u)=(u-1)(u-i),\quad d=u^4-1,
\]
\[
R=B\times_{\mathbb C[t]^6}\mathbb C[t]^3,\qquad
I=dB=(d,du)R.
\tag{1}
\]
The three pairs of conductor lines are
\[
((1,0),(i,0)),\qquad ((1,1),(-i,*)),\qquad
((-1,*),(i,1)).
\tag{2}
\]
Here the split-line parameter is
\(t=z/[r(2\epsilon-1)]\), and the ordinary-line parameter is
\(t=y/[rA(r)]\). These are precisely the shared parameters of the
[original four-generator presentation](nodal-elimination-pass23.md).
No new pairing or gluing map is used.

For the fixed action
\[
\partial u=0,\quad \partial y=uA(u),\quad
\partial z=u(2y-1),
\]
the [previous quotient calculation](nodal-hypersurface-pass24.md)
gives
\[
T=\ker(\partial|_R)=\mathbb C+d\mathbb C[u].
\tag{3}
\]
Let \(j\in T\) be nonconstant. Write
\[
c_0=j(1)=j(i)=j(-1)=j(-i),\qquad
m_r=\operatorname{ord}_{u=r}(j-c_0)\ge1
\quad(r^4=1).
\tag{4}
\]
For positive integers \(m,n\), define
\[
D_{m,n}=\mathbb C[x,y]/(xy,x^m+y^n).
\tag{5}
\]
This is an Artinian local algebra of length \(m+n\).

**Theorem.** Every fiber of \(j:\operatorname{Spec}R\to\mathbb A^1\)
has the following actual global coordinate ring.

If \(c\ne c_0\), then
\[
R/(j-c)\cong
\prod_{j(\zeta)=c}
\mathbb C[t,\epsilon]/(\epsilon^{\operatorname{ord}_\zeta(j-c)}).
\tag{6}
\]
The product is over distinct roots.

At the conductor value,
\[
\begin{split}
R/(j-c_0)\cong{}&
\mathbb C[t]\otimes D_{m_1,m_i}\\
&\times\mathbb C[t]\otimes D_{m_1,m_{-i}}\\
&\times\mathbb C[t]\otimes D_{m_{-1},m_i}\\
&\times
\prod_{\substack{j(\zeta)=c_0\\\zeta^4\ne1}}
\mathbb C[t,\epsilon]/
(\epsilon^{\operatorname{ord}_\zeta(j-c_0)}).
\end{split}
\tag{7}
\]
The isomorphisms in (6) and (7) are abstract fiber-ring isomorphisms.
The variable \(t\) on different factors is independently chosen;
there is no assertion that one global generator of \(R\) realizes
all these coordinates, or that these isomorphisms vary algebraically
with \(c\).

Consequently the following are equivalent:
\[
\begin{split}
&\text{every fiber of \(j\) admits a closed embedding in \(\mathbb A^2\)},\\
&\min(m_1,m_i)=\min(m_1,m_{-i})
 =\min(m_{-1},m_i)=1.
\end{split}
\tag{8}
\]

If (8) fails, \(j\) belongs to no three-element algebra generating
set of \(R\). If (8) holds, the theorem makes no assertion that \(j\)
belongs to a generating triple.

## 2. Exact finite neighborhoods of the conductor

The computation uses finite quotient rings, not only pointwise
completed local rings. Since \(I=dB\) as a subset of \(R\),
\[
I^N=d^NB\qquad(N\ge1).
\tag{9}
\]
For the reverse containment in this identity,
\(d^Nb=d^{N-1}(db)\) is a product of \(N\) elements of \(I\).
The defining fiber product therefore gives
\[
R/I^N
\cong (B/d^NB)\times_{\mathbb C[t]^6}\mathbb C[t]^3.
\tag{10}
\]
Surjectivity here is explicit: a lift to \(B\) of any six jets whose
constant terms satisfy the three gluing equalities already belongs
to \(R\). Its kernel is exactly \(d^NB\).

The simple roots of \(d\) separate the four \(u\)-values. At \(r=1,i\),
the two roots \(y=0,1\) further separate the split lines. A nilpotent
thickening has the same decomposition into these open-and-closed
pieces as its reduction; equivalently its idempotents lift uniquely.[^idempotent]
We now give the full polynomial jet coordinates on all six pieces.

Put \(\xi=u-r\). On the split line \(y=\epsilon\), take
\(z=r(2\epsilon-1)t\) and set
\[
y=\frac{1+(2\epsilon-1)
 \sum_{k=0}^{N-1}\binom{1/2}{k}
       \bigl(4A(r+\xi)r(2\epsilon-1)t\bigr)^k}{2}
 \pmod{\xi^N}.
\tag{11}
\]
Because \(A(r+\xi)\) is divisible by \(\xi\), this finite expression
satisfies \(y(y-1)=A(r+\xi)z\) modulo \(\xi^N\).
It has the required residue \(y=\epsilon\).
The inverse coordinates are \(\xi=u-r\) and the original scaled \(z\).
Thus the whole jet component is
\(\mathbb C[t,\xi]/(\xi^N)\), not merely a collection of pointwise
formal charts.

At the ordinary roots \(r=-1,-i\), take
\[
y=rA(r)t,\qquad
z=y(y-1)A(r+\xi)^{-1}\pmod{\xi^N}.
\tag{12}
\]
The inverse in (12) is a finite geometric series, since \(A(r)\ne0\).
Again this is an actual polynomial coordinate isomorphism on the
nilpotent quotient with the original residue parameter \(t\).

For one pair, denote the two normal coordinates by \(x,y\).
The equality of the two constant terms identifies its factor in
(10) with
\[
\mathbb C[t,x,y]/(xy,x^N,y^N).
\tag{13}
\]
Here \(x\) and \(y\) are the two supported normal functions.
They are not the old normalization coordinate \(y\).

Because \(j\) depends only on \(u\), its image on this pair is
\[
c_0+F_r(x)+F_s(y),\qquad
F_r(x)=j(r+x)-c_0,\quad F_s(y)=j(s+y)-c_0.
\tag{14}
\]
There is no \(t\)-dependent coefficient in (14).

## 3. Passage from finite jets to the entire actual fiber

First consider \(c\ne c_0\). Every normalized root \(\zeta\) of
\(j-c\) lies off the conductor, so the normalization is an isomorphism
near its entire vertical line. Also \(A(\zeta)\ne0\).
If the root has multiplicity \(q\), its primary fiber component is
\[
B/(u-\zeta)^q
\cong\mathbb C[y,\xi]/(\xi^q):
\]
the inverse of \(A(\zeta+\xi)\) eliminates \(z\).
The distinct vertical lines are disjoint closed curves, so their
nilpotent thickenings give the product (6).

For \(c=c_0\), the reduced fiber consists of the three conductor
lines and the ordinary vertical lines at roots \(\zeta^4\ne1\).
They are pairwise disjoint as closed subsets of the actual surface.
The conductor identifications identify the two entire lines in each
pair, not isolated points on otherwise separate fiber components.

The finite-type ring \(R/(j-c_0)\) has nilpotent nilradical.
Its reduced ring is a product of the corresponding affine-line
rings. Lifting the idempotents gives an actual global product
decomposition into the thickened components.[^idempotent]
On the product of the three conductor components the image of
\(I\) is nilpotent. On every other component \(d\), hence \(I\),
is a unit. For sufficiently large \(N\), therefore,
\[
R/(j-c_0,I^N)
\]
is exactly the product of the three conductor components of the
full fiber. This identifies which global part the jet computation
recovers; it does not infer global equivalence merely from
isomorphic pointwise completions.

Using (13) and (14), its pair factor is
\[
\mathbb C[t,x,y]/
(xy,x^N,y^N,F_r(x)+F_s(y)).
\tag{15}
\]
Write \(F_r=x^m a(x)\) and \(F_s=y^n b(y)\), with \(a(0)b(0)\ne0\).
For \(N>\max(m,n)\), multiplying the last relation by \(x\) or \(y\)
shows, using these units, that
\[
x^{m+1}=y^{n+1}=0.
\tag{16}
\]
Choose complex roots of the nonzero leading constants. Finite
binomial series then make the invertible nilpotent coordinate changes
\[
X=x\,a(x)^{1/m},\qquad Y=y\,b(y)^{1/n}.
\tag{17}
\]
They have nonzero linear coefficients and polynomial inverses in the
truncated rings. The relation becomes \(X^m+Y^n=0\), while \(XY=0\).
Thus (15) is exactly
\[
\mathbb C[t]\otimes D_{m,n}.
\tag{18}
\]
The result is independent of all sufficiently large \(N\), as required.
Together with the ordinary components this proves (7).

## 4. The precise planar-fiber criterion

In \(D_{m,n}\), both \(x^{m+1}\) and \(y^{n+1}\) vanish.
A basis is
\[
1,x,\ldots,x^m,y,\ldots,y^{n-1},
\tag{19}
\]
so the length is \(m+n\). This basis follows directly by reducing
mixed monomials and replacing \(y^n\) by \(-x^m\); the only overlap
relations kill \(x^{m+1}\) and \(y^{n+1}\).

If \(m,n\ge2\), then at every closed point of
\(\operatorname{Spec}(\mathbb C[t]\otimes D_{m,n})\), the classes
of \(x,y,t-t_0\) are independent in the cotangent space.
Its dimension is three. Such a curve scheme cannot be a closed
subscheme of the smooth plane, whose local cotangent dimension
is at most two. This obstruction concerns the full nonreduced
fiber scheme.

If \(m=1\), eliminating \(x=-y^n\) gives
\[
D_{1,n}\cong\mathbb C[y]/(y^{n+1}).
\tag{20}
\]
Likewise \(D_{m,1}\cong\mathbb C[x]/(x^{m+1})\).
Thus every factor in (7) is a thickened affine line precisely when
each pair has an endpoint of multiplicity one.

A finite product of such thickened-line rings is itself a plane
curve ring. Given their lengths \(q_1,\ldots,q_\ell\), choose distinct
complex numbers \(\alpha_1,\ldots,\alpha_\ell\). The Chinese remainder
theorem gives
\[
\prod_{k=1}^{\ell}\mathbb C[t_k,\epsilon_k]/(\epsilon_k^{q_k})
\cong
\mathbb C[X,Y]/
\left(\prod_{k=1}^{\ell}(X-\alpha_k)^{q_k}\right).
\tag{21}
\]
On the \(k\)-th factor use \(X=\alpha_k+\epsilon_k\), \(Y=t_k\).
This proves both directions of (8).

Finally, if \(R=\mathbb C[j,f_1,f_2]\), every fiber of \(j\) is a
quotient of \(\mathbb C[f_1,f_2]\) and hence a plane curve scheme.
Failure of (8) therefore excludes **every** possible companion
pair. A constant \(j\) is also excluded, since two remaining
generators cannot span the surface's three-dimensional conductor
cotangent spaces.

## 5. Infinite-dimensional exclusions and exact surviving controls

Write
\[
j=c_0+dF(u),\qquad F\in\mathbb C[u]\setminus\{0\}.
\tag{22}
\]
For a fourth root \(r\) of unity,
\[
j'(r)=4r^3F(r).
\tag{23}
\]
The criterion fails exactly when the zero set of \(F\) among
\(1,i,-1,-i\) contains both endpoints of one edge
\[
\{1,i\},\quad\{1,-i\},\quad\{-1,i\}.
\tag{24}
\]
Equivalently, an invariant with a zero derivative at both ends of
any original pair can never be part of a generating triple.
This excludes the union of the three all-degree families
\[
c_0+d(u-r)(u-s)\mathbb C[u]
\quad\text{for the pairs \(\{r,s\}\) in (24)}.
\tag{25}
\]
The constant member of each family is excluded separately as above.
This is stronger than retaining the particular pair \(g,h\):
both companion functions are arbitrary.

For example, the actual function
\[
j=d(u-1)(u-i)
\tag{26}
\]
belongs to \(T\subset R\). Its conductor multiplicities are
\(m_1=m_i=2\), \(m_{-1}=m_{-i}=1\).
The first factor of its zero fiber is
\(\mathbb C[t,x,y]/(xy,x^2+y^2)\); it has cotangent dimension three.
No triple containing (26) generates \(R\).
The same applies to every nonconstant \(c_0+d^2F(u)\).

Two useful surviving controls are:
\[
R/(d)\cong
\prod_{k=1}^3\mathbb C[t_k,\epsilon_k]/(\epsilon_k^2),
\tag{27}
\]
and, for \(j=d(u^2-1)\),
\[
R/(j)\cong
\prod_{k=1}^3\mathbb C[t_k,\epsilon_k]/(\epsilon_k^3).
\tag{28}
\]
For (28), the critical conductor roots are \(1,-1\), which are
not an edge in (24). Every pair has multiplicities \(2,1\).
All other fibers of these functions are planar by (6), including
the nonreduced fiber \(R/(d+1)\cong\mathbb C[t,\epsilon]/(\epsilon^4)\).

The closed-fiber test is therefore completely exhausted for
invariant functions of this specified action. Passing (8) is only a
necessary condition for membership in a generating triple.
Equations (21), (27) and (28) do not glue into an ambient coordinate
system for the whole surface. In particular they do not undo the
earlier all-triples obstruction for the different, noninvariant
function \(h\).

## Verification and exact scope

The standalone checker
[changed_fiber_surface_checks_pass28.py](changed_fiber_surface_checks_pass28.py)
imports only unittest and SymPy. Its finite exact controls check
the six original scaled jet charts, actual pair quotients,
the Artinian basis and cotangent test, the positive and negative
invariant examples, finite root-coordinate changes, ordinary
thickened fibers, and the explicit Chinese-remainder plane embedding.

The all-degree claims are the finite-neighborhood argument (9)–(18)
and the written global decomposition, not a extrapolation from
bounded examples. The only external algebraic input beyond
elementary polynomial algebra is nilpotent idempotent lifting.
The [Stacks Project statement and both proofs](https://stacks.math.columbia.edu/tag/00J9)
were read directly. No classification of arbitrary locally nilpotent
actions or ambient embeddings is used.

The targeted run passed all seven unittest methods in 2.458 seconds.

Run from the project directory:

~~~sh
/opt/anaconda3/bin/python research/changed_fiber_surface_checks_pass28.py
~~~

The abstract bound \(3\le\mu_{\mathbb C}(R)\le4\) remains unchanged.
An actual generating triple replacing \(h\), or a proof that none
exists, remains unresolved. Even an embedding would leave the
prescribed ambient primitive-action realization to prove.
No cancellation solution, novelty claim, expert review or formal
proof-assistant verification is asserted.

## Sources

[^idempotent]: The Stacks Project, [Lemma 10.32.6, Tag 00J9](https://stacks.math.columbia.edu/tag/00J9), statement and both proofs read directly. Used only for the unique lifting of idempotents through a nilpotent ideal. The actual conductor and its scaled gluing are from [pass 20](nodal-conductor-pass20.md) and [pass 23](nodal-elimination-pass23.md); the invariant ring is from [pass 24](nodal-hypersurface-pass24.md). The preceding nonplanar \(h\)-fiber result is [pass 27](noninvariant-surface-pass27.md).
