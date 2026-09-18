# Degree pruning at a squarefree rank-two center

Status: bounded working necessary restriction. For the actual
\(q=1/\rho\) chart remaining after212, monic specialization of the
selected plane relation gives a shorter degree list, depending on
whether its squarefree center is linear or quadratic.
This neither asserts that the plane ring is the whole line ring nor
recognizes the remaining original action.

## 1. Exact retained inputs

Retain the full hypotheses and constructions of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md).
In particular
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\quad
q=1/\rho,\quad [L:\mathbb C(t,\rho)]<\infty,\\
O=L[v],\quad C=L[y,\vartheta]\subset O,\quad
\operatorname{Frac}C=L(v),\quad
R=2\rho^{-3}\vartheta+k_\rho\ne0,\quad RO\subset C .
\end{gathered}
\tag{1}
\]
The four original generators are polynomial coordinates, the initial
ideal is the whole kernel, and the chart comes from the actual selected
partial. The coefficient field \(L\) is not assumed rational.

The zero-return and constant-second-projection branches are already
recognized. In the remaining branch,212 supplies a nonconstant
squarefree center \(p(U)\) and the exact polynomial factorization
\[
\begin{gathered}
\mathcal H=GQ_1,\qquad
\mathcal H_6=-\rho^{-11}V^6,\quad \deg\mathcal H=6,\\
V_c=-\rho^3k_\rho/2,\qquad
\mathcal H(U,V_c)=\rho^{-3}p(U)^2,\quad
m:=\deg p\in\{1,2\},\\
d=\deg_vy=\deg G,\qquad e=\deg_v\vartheta=\deg_U G,\qquad
1\le e<d\le6,\quad e\le4 .
\end{gathered}
\tag{2}
\]
Here \(G\) generates the irreducible plane evaluation ideal.
It is a simple factor of \(\mathcal H\), although that simplicity
is not needed for the specialization argument below.
The top forms of both \(G\) and \(Q_1\) are nonzero pure powers of
\(V\), since their product is the displayed top form of \(\mathcal H\).
The conductor also gives
\[
(d-1)(e-1)\le e\quad\text{when }d,e>1,\ \gcd(d,e)=1.
\tag{3}
\]
This is the elementary degree-semigroup conclusion proved in212,
not an assumption that \(C\) is normal.

## 2. Monic specialization without a reduced-fiber assumption

The module \(O\) is free over \(L[\vartheta]\) with basis
\(1,v,\ldots,v^{e-1}\).
Indeed the degree-e expression for \(\vartheta\) reduces every
higher power of \(v\), while the degrees of nonzero terms in the
proposed basis are distinct modulo \(e\).
Multiplication by \(y\) therefore has a monic characteristic
polynomial
\(\chi(U)\in L[\vartheta][U]\) of degree \(e\).

Birationality gives \(L(\vartheta)(y)=L(v)\), whose degree over
\(L(\vartheta)\) is \(e\). Thus the minimal polynomial of \(y\)
has degree \(e\), and equals \(\chi\).
The polynomial \(\chi\), regarded in \(L[V,U]\), is irreducible
by Gauss's lemma and lies in the plane evaluation kernel.
We may consequently normalize \(G\) by a unit in \(L\) so that
it is this monic polynomial.
Adjust \(Q_1\) by the inverse unit, retaining \(\mathcal H=GQ_1\).

It follows that \(G(U,V_c)\) is still monic of degree \(e\);
its degree cannot drop at this fiber.
Because the right side of (2)'s center identity is nonzero,
neither factor specializes to zero. Hence
\[
\begin{gathered}
e\le2m,\qquad
\deg_U G(U,V_c)=e,\qquad
\deg_U Q_1(U,V_c)=2m-e,\\
[U^{2m-e}]Q_1(U,V_c)=
 \rho^{-3}\bigl([U^m]p(U)\bigr)^2\ne0 .
\end{gathered}
\tag{4}
\]
These are polynomial identities over the exact field \(L\).
No reduced, smooth, or etale property of the center fiber is used.

If \(2m-e>0\), this specialization has positive U-degree.
The total degree of \(Q_1\) is \(6-d\), and its top form is a
pure power of \(V\). Thus
\(\deg_U Q_1\le(6-d)-1\), and (4) yields the decisive bound
\[
2m-e>0\quad\Longrightarrow\quad d\le5-2m+e .
\tag{5}
\]
In the case \(2m=e\), the specialized cofactor is a nonzero
constant. The positive-degree argument (5) is not applied to it.

## 3. The exact remaining degree lists

Suppose \(m=1\). Equation (4) gives \(e=1\) or two.
For \(e=1\), equation (5) gives \(d\le4\); together with \(d>e\),
this leaves \(d=2,3,4\).
For \(e=2\), the specialized cofactor is constant.
The original bounds allow \(d=3,4,5,6\), but \(d=5\) contradicts
(3). Thus the necessary list for a linear squarefree center is
\[
(d,e)=(2,1),(3,1),(4,1),(3,2),(4,2),(6,2).
\tag{6}
\]

Suppose \(m=2\). If \(e<4\), equation (5) gives \(d\le e+1\);
strict ordering makes \(d=e+1\).
When \(e>1\), these two degrees are coprime, so (3) gives
\(e(e-1)\le e\), hence \(e\le2\).
The cases are therefore \((d,e)=(2,1),(3,2)\).
If \(e=4\), the specialized cofactor is constant.
The original bounds allow \(d=5,6\); equation (3) excludes five.
The necessary list for a quadratic squarefree center is
\[
(d,e)=(2,1),(3,2),(6,4).
\tag{7}
\]
There is no existence assertion for any listed pair.

There is also an independent short check excluding \(e=3\).
The degree and conductor list in212 would force \(d=6\).
Then \(\deg G=\deg\mathcal H\), so \(\mathcal H\) is a scalar
multiple of \(G\) and would have U-degree three.
But its exact U-fourth coefficient is \(k_{tt}^2/(4\rho^3)\);
when this is nonzero the U-degree is four, and when \(k_{tt}=0\)
the full formula in212 has U-degree at most two.
Neither case permits U-degree three.

## 4. The remaining proof gap

Nothing above proves \(C=O\), removes coefficient-field
denominators, or produces an actual invariant coordinate.
Even the exceptional pair \((d,e)=(6,4)\) cannot be dismissed by
assuming that cancellation of the degree-twelve leading terms
must leave a polynomial of high degree. For the purely formal pair
\[
\vartheta=x^4+x,\qquad
y=x^6+\tfrac32x^3+\tfrac38,\qquad
y^2-\vartheta^3=\tfrac18x^3+\tfrac9{64},
\tag{8}
\]
the cancellation leaves degree three.
This elementary identity is not asserted to satisfy the actual
potentials, scalar determinant, conductor condition, or full frame.
It only prevents that unsupported next-degree inference.

A further argument must use actual differential potentials,
conductor geometry with justified hypotheses, or original-ring
descent. No recognition or exclusion of the remaining squarefree
rank-two charts is proved here.
No saved checker was executed, imported or compiled, no retained
source or index was changed, and this pass is separate from212.
The full cancellation problem, arbitrary entry, and novelty
questions remain outside this bounded working result.
