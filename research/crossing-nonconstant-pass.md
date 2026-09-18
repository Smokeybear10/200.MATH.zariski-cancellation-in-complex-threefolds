# The split-quadric coefficient with nonconstant axis restriction

**Status:** complete conditional-family classification; constant-axis branch out of scope

## 1. Statement

Let

\[
F(x,y,z,u)=xyu+H(x,y,z),\qquad H\in\mathbb C[x,y,z],
\]

and put

\[
h(z)=H(0,0,z).
\]

Assume that \(h\) is nonconstant.  Then the following are equivalent:

1. \(F\) is a coordinate of \(\mathbb C[x,y,z,u]\);
2. \(F\) becomes a coordinate after adjoining finitely many variables;
3. \(F\) is a slice of a locally nilpotent derivation;
4. there are \(a\in\mathbb C^*\), \(b\in\mathbb C\), polynomials
   \(B\in\mathbb C[x]\), \(C\in\mathbb C[y]\) with \(B(0)=C(0)=0\), and
   \(K\in\mathbb C[x,y,z]\) such that

   \[
   H=az+b+B(x)+C(y)+xyK(x,y,z).
   \tag{1}
   \]

In particular, stability forces \(h(z)=az+b\) to have degree one.

The implication from (1) to a coordinate is explicit.  Set

\[
U=u+K(x,y,z).
\]

Then

\[
F=xyU+az+b+B(x)+C(y),
\]

and

\[
(x,y,z,u)\longmapsto(x,y,U,F)
\]

is a polynomial automorphism, with

\[
z=\frac{F-xyU-b-B(x)-C(y)}a,\qquad
u=U-K(x,y,z).
\tag{2}
\]

The proof below establishes the converse from stable-coordinate topology.
It has no degree restriction on \(H\).

## 2. Cohomology of the crossing divisor

Put

\[
D=V(xy)\subset\mathbb A^3_{x,y,z},
\qquad
U_0=\mathbb A^3\setminus D.
\]

The divisor is the union of two affine planes,

\[
D_x=V(x),\qquad D_y=V(y),
\qquad D_x\cap D_y=L=V(x,y)\cong\mathbb A^1.
\]

The compact-support Mayer--Vietoris sequence for
\(D=D_x\cup D_y\), with integral coefficients, gives

\[
H_c^3(D;\mathbb Z)=\mathbb Z,\qquad
H_c^4(D;\mathbb Z)=\mathbb Z^2.
\tag{3}
\]

Indeed, the first group is the shift of
\(H_c^2(L)=\mathbb Z\), while the second is
\(H_c^4(D_x)\oplus H_c^4(D_y)=\mathbb Z^2\).

Apply the closed--open sequence to
\(D\subset\mathbb A^3\).  Since affine three-space has compactly supported
integral cohomology only in degree six, (3) yields

\[
H_c^4(U_0;\mathbb Z)=\mathbb Z,\qquad
H_c^5(U_0;\mathbb Z)=\mathbb Z^2.
\tag{4}
\]

## 3. The closed curve in a fiber

For \(\lambda\in\mathbb C\), set

\[
X_\lambda=V(xyu+H-\lambda)\subset\mathbb A^4.
\]

On \(xy\ne0\), the equation solves uniquely for \(u\), so the open part of
\(X_\lambda\) is \(U_0\).  Its reduced closed complement is

\[
Z_\lambda=C_\lambda\times\mathbb A^1_u,
\qquad
C_\lambda=V(xy,H-\lambda)\subset D.
\tag{5}
\]

Write

\[
\begin{aligned}
q_x(y,z)&=H(0,y,z),&
C_{x,\lambda}&=V(q_x-\lambda)\subset D_x,\\
q_y(x,z)&=H(x,0,z),&
C_{y,\lambda}&=V(q_y-\lambda)\subset D_y.
\end{aligned}
\]

Then

\[
C_\lambda=C_{x,\lambda}\cup C_{y,\lambda}.
\tag{6}
\]

Because both \(q_x\) and \(q_y\) restrict on \(L\) to the nonconstant
polynomial \(h\), both are nonconstant.  Choose one generic \(\lambda\)
such that:

* \(C_{x,\lambda}\) and \(C_{y,\lambda}\) are nonempty smooth affine
  curves; and
* \(h(z)-\lambda\) has \(d=\deg h\) distinct roots.

Such values form a nonempty Zariski-open subset of \(\mathbb A^1\).
The two curves in (6) meet exactly in the \(d\) reduced points

\[
S_\lambda=C_{x,\lambda}\cap C_{y,\lambda}
=\{(0,0,z):h(z)=\lambda\}.
\tag{7}
\]

No transversality assertion inside a smooth ambient surface is being used:
the two curves lie on the two different components of \(D\).  Only the
reduced finite intersection (7) enters the topological sequence.

## 4. Stability determines the integral cohomology of \(C_\lambda\)

Suppose \(F\) is a stable coordinate.  Then

\[
X_\lambda\times\mathbb A^N\cong\mathbb A^{N+3}
\]

for some \(N\) and every \(\lambda\).  Hence \(X_\lambda\) is a smooth,
contractible complex threefold and

\[
H_c^i(X_\lambda;\mathbb Z)=0\quad(i\ne6).
\tag{8}
\]

Use the closed--open sequence for (5).  In degrees three through five,
(4) and (8) give

\[
H_c^3(Z_\lambda;\mathbb Z)\cong H_c^4(U_0;\mathbb Z)=\mathbb Z,
\]

\[
H_c^4(Z_\lambda;\mathbb Z)\cong H_c^5(U_0;\mathbb Z)=\mathbb Z^2.
\]

The compact-support Kunneth formula for the affine-line factor in (5)
therefore yields

\[
H_c^1(C_\lambda;\mathbb Z)=\mathbb Z,\qquad
H_c^2(C_\lambda;\mathbb Z)=\mathbb Z^2.
\tag{9}
\]

Gluing finitely many points does not alter top compact-support cohomology.
Equivalently, Mayer--Vietoris for (6)--(7) gives

\[
H_c^2(C_\lambda)
\cong H_c^2(C_{x,\lambda})\oplus H_c^2(C_{y,\lambda}).
\tag{10}
\]

For a smooth affine curve, the rank of \(H_c^2\) is its number of connected
components.  Both curves in (10) are nonempty, while (9) has total rank two.
Thus each \(C_{x,\lambda}\) and \(C_{y,\lambda}\) is connected and hence
irreducible.

All three curves in (6) are noncompact, so their compactly supported
degree-zero groups vanish.  The beginning of the same Mayer--Vietoris
sequence is therefore

\[
0\longrightarrow\mathbb Z^d
\longrightarrow H_c^1(C_\lambda;\mathbb Z)
\longrightarrow
H_c^1(C_{x,\lambda};\mathbb Z)
\oplus H_c^1(C_{y,\lambda};\mathbb Z)
\longrightarrow0.
\tag{11}
\]

The middle group has rank one by (9), \(d\ge1\), and the two groups on the
right are free abelian.  Taking ranks in (11) forces

\[
d=1,\qquad
H_c^1(C_{x,\lambda};\mathbb Z)
=H_c^1(C_{y,\lambda};\mathbb Z)=0.
\tag{12}
\]

This proves first that \(h(z)=az+b\) with \(a\ne0\).  A smooth connected
affine complex curve with \(H_c^1=0\) has genus zero and one puncture, so
(12) also gives

\[
C_{x,\lambda}\cong\mathbb A^1,\qquad
C_{y,\lambda}\cong\mathbb A^1.
\tag{13}
\]

By the Abhyankar--Moh--Suzuki line-embedding theorem, one fiber (13) is
enough to make each defining plane polynomial a coordinate. The chosen
plane level is regular, so its defining polynomial is reduced. Since
the curve is irreducible, that polynomial is an irreducible generator,
not a power of one. Rectification therefore applies to the defining
polynomial itself:

\[
q_x\text{ is a coordinate of }\mathbb C[y,z],
\qquad
q_y\text{ is a coordinate of }\mathbb C[x,z].
\tag{14}
\]

## 5. The relative-coordinate lemma

We need the following elementary sharpening of (14).

**Lemma.**  If \(q(r,z)\in\mathbb C[r,z]\) is a plane coordinate and

\[
q(0,z)=az+b,\qquad a\in\mathbb C^*,
\]

then \((r,q)\) is a coordinate pair and

\[
q(r,z)=az+Q(r)
\tag{15}
\]

for some \(Q\in\mathbb C[r]\).

**Proof.** Choose a coordinate companion \(V\) with
\(\mathbb C[q,V]=\mathbb C[r,z]\).  On the line \(r=0\), the function \(q\)
is an isomorphism to \(\mathbb A^1\).  Hence this line is, in the
\((q,V)\)-plane, the graph

\[
V=R(q),\qquad
R(T)=V\!\left(0,\frac{T-b}{a}\right)\in\mathbb C[T].
\]

The irreducible polynomials \(r\) and \(V-R(q)\) have the same zero set, so
they are associates.  It follows that

\[
\mathbb C[r,q]=\mathbb C[V-R(q),q]=\mathbb C[V,q].
\]

Thus \(q\) is a coordinate over \(\mathbb C[r]\).  An automorphism of the
one-variable polynomial algebra \(\mathbb C[r][z]\) sends \(z\) to
\(\alpha z+Q(r)\), with \(\alpha\in\mathbb C^*\).  Restriction to \(r=0\)
shows \(\alpha=a\), proving (15). \(\square\)

Apply the lemma to (14).  After subtracting their common constant
\(b=h(0)\), there are \(B(0)=C(0)=0\) such that

\[
q_y(x,z)=az+b+B(x),\qquad
q_x(y,z)=az+b+C(y).
\tag{16}
\]

The polynomial

\[
H-az-b-B(x)-C(y)
\]

vanishes both on \(x=0\) and on \(y=0\).  It is therefore divisible by
\(xy\), which gives exactly (1).  Formula (2) then proves that \(F\) is a
coordinate.

An ordinary coordinate is stably a coordinate and is a slice of a conjugate
coordinate partial.  Conversely, an LND slice becomes a coordinate after
one stabilization by the slice theorem.  This completes all equivalences.

## 6. Scope and remaining branch

The proof uses \(h\) nonconstant at two essential points: it makes both plane
restrictions nonconstant and supplies the nonempty finite intersection
\(S_\lambda\).  When \(h\) is constant, the two generic curves are disjoint
and (11) has no \(\mathbb Z^d\) term.  That branch is not decided here.

Together with the separate integral-torsion obstruction for
\(P=xy-z^2\), this substantially narrows quadratic coefficients in the
linear-\(u\) cubic normal form.  It does not by itself classify the
constant-axis split-quadric branch, rank-one coefficients, or arbitrary
quadratic polynomials with lower terms.  This is a written proof without
human expert review or an originality claim.

## Source for the plane-line step

Nguyen Van Chau, [“Polynomial maps of the complex plane with the branched
value sets isomorphic to the complex line,” Section 2 and Lemma 1, printed
pp. 198--199](https://math.ac.vn/uploads/files/0202197.pdf),
*Acta Mathematica Vietnamica* **27** (2002), 197--202.  It records the
line-rectification consequence of the Abhyankar--Moh--Suzuki theorem used
in (14).  The integral Mayer--Vietoris calculation and relative-coordinate
lemma above are self-contained.
