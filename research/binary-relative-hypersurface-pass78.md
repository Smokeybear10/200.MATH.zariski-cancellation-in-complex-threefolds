# Two actual invariant generators over the intrinsic plane

The unit binary parameter row gives an explicit relative basis
of the three transverse coordinate directions. Its dual produces
a polynomial slice and two invariant elements which generate
the original kernel over its intrinsic plane.

The result is a global plane-hypersurface presentation over that
plane. It is not a polynomial-coordinate recognition theorem.
The basis construction uses only two Bezout identities and
cross products, not Quillen--Suslin or a Picard-group theorem.

## 1. Actual inputs after excluding proper parameters

Retain the nonlinear supplied-good-direction branch:
\[
\begin{gathered}
B=\mathbb C[x_1,x_2,x_3,w]=A[s],\qquad
E=P\cdot\partial\in\operatorname{LND}(B),\quad Es=1,\quad
A=\ker E,\quad E(P)=0,\\
T=\partial_w,\quad [E,[T,E]]=0,\quad Q=[T,E],\\
0\ne\delta=Q|_A=hD,\qquad
S=\ker D=\ker\delta\simeq\mathbb C[u,v],\qquad
S\subset A\text{ faithfully flat},\\
p,q\in S,\quad Qp=Qq=0,\quad
P_{\mathrm{tr}}=\mathcal H(p,q),\quad
\mathcal H=(h_1,h_2,h_3)^t.
\end{gathered}
\tag{1}
\]
The binary forms are coprime, homogeneous of one degree
\(e\ge2\), and linearly independent over \(\mathbb C\).
The original parameters are nonzero actual polynomials.
They may be algebraically dependent.
The completed
[normal-syzygy exclusion](binary-normal-syzygy-exclusion-pass78.md)
gives
\[
(p,q)S=S,\qquad
(P_1,P_2,P_3)S=S,\qquad P_4\in S.
\tag{2}
\]
The last inclusion follows from \(E(P_4)=Q(P_4)=0\).
Neither p nor q is assumed to be a coordinate.

## 2. A unimodular polynomial normal

In independent binary variables \(\xi,\eta\), put
\[
N=\mathcal H_\xi\times\mathcal H_\eta,\qquad
G=\gcd_{\mathbb C[\xi,\eta]}(N_1,N_2,N_3),\qquad
n=N/G.
\tag{3}
\]
Choose the nonzero homogeneous gcd G up to a complex unit.
The entries of n are homogeneous of one degree and have
gcd one. The binary-Jacobian independence proved in the
normal-syzygy note ensures \(N\ne0\).
Division by G preserves the polynomial identities
\[
n\cdot\mathcal H=n\cdot\mathcal H_\xi
 =n\cdot\mathcal H_\eta=0.
\tag{4}
\]
The first also follows directly from Euler's formula for
\(\mathcal H\).

The row \(\nu=n(p,q)\) is unimodular over S.
Indeed, homogeneous coprime binary forms of a positive
common degree have no common projective zero. Their ideal
contains a power of \((\xi,\eta)\), by the same two-form
argument used in binary descent77. Equation (2) makes
their evaluated ideal the unit ideal.
If the common degree is zero, some nonzero constant entry
gives the same conclusion immediately.

The actual polynomial
\[
c=\nu\cdot x_{\mathrm{tr}}\in S,\qquad
x_{\mathrm{tr}}=(x_1,x_2,x_3)^t
\tag{5}
\]
is killed by E and Q: both kill its coefficients, and (4)
annihilates their transverse velocity columns.
Thus c lies in A and then in \(\ker\delta=S\).
This is a polynomial invariant, not a rational one promoted
by a field calculation.

## 3. An explicit relative basis and its orientation

Abbreviate \(H=P_{\mathrm{tr}}\in S^3\).
By (2) and the unimodularity of \(\nu\), choose a row
\(\lambda\in S^{1\times3}\) and a column \(W_0\in S^3\)
with \(\lambda H=1\) and \(\nu W_0=1\).
Define
\[
W=W_0-(\lambda W_0)H,\qquad
V=\nu\times\lambda,\qquad
M=[H,V,W].
\tag{6}
\]
Rows are identified with coordinate triples for the cross
product. Since \(\nu H=0\), these formulas give
\(\nu W=1\), \(\lambda W=0\),
\(\nu V=\lambda V=0\).
The vector triple-product identity fixes the determinant:
\[
\det M
 =H\cdot\bigl((\nu\times\lambda)\times W\bigr)
 =H\cdot\bigl(\lambda(\nu W)-\nu(\lambda W)\bigr)
 =1,\qquad
M^{-1}=
\begin{pmatrix}
\lambda\\
(W\times H)^t\\
\nu
\end{pmatrix}.
\tag{7}
\]
The transposes in (7) only specify row orientation.
For instance \((W\times H)\cdot V=\det M=1\).
This proves a genuine inverse matrix over S.
It is not an appeal to the freeness of an unspecified
rank-two projective module.

## 4. Generation of the original kernel

Apply the inverse matrix in (7) to the actual transverse
coordinate column, and define
\[
y_1=\lambda x_{\mathrm{tr}},\qquad
y_2=(W\times H)\cdot x_{\mathrm{tr}},\qquad
y_3=\nu x_{\mathrm{tr}}=c,\qquad
z=w-P_4y_1.
\tag{8}
\]
Every coefficient of the matrix belongs to S and is
therefore killed by E. Equations (7)--(8) give
\(Ey_1=1\), \(Ey_2=Ey_3=0\), and \(Ez=0\).
The full reconstruction of all four original coordinates is
\[
x_{\mathrm{tr}}=Hy_1+Vy_2+Wc,\qquad
w=z+P_4y_1.
\tag{9}
\]
Both matrix compositions recover the three transverse
entries, and substitution in the second identity recovers w.
The element c already belongs to S. Since B is generated
by its four original coordinates, (8)--(9) prove
\[
B=S[y_1,y_2,z],\qquad
B=A[y_1],\qquad
\boxed{A=S[y_2,z].}
\tag{10}
\]
The middle equality is the actual slice theorem for
\(Ey_1=1\). For the last equality, put \(C_0=S[y_2,z]\subset A\).
An element of A can be expressed in \(C_0[y_1]\) by the
first equality. Its zero E-derivative forces every positive
\(y_1\)-coefficient to vanish, using characteristic zero and
the genuine polynomial extension \(B=A[y_1]\).
It therefore lies in C0.

These are relative reconstruction identities.
The coefficients of M are themselves original invariants
in B. They do not define a constant four-by-four change
of the original ambient coordinates, and \(y_1\) has not
been proved to be an ambient polynomial coordinate.

## 5. The hypersurface presentation and an explicit second velocity

The surjection \(S[Y,Z]\to A\), \(Y\mapsto y_2\),
\(Z\mapsto z\), has a height-one prime kernel.
Indeed \(S[Y,Z]\) has dimension four and A has
transcendence degree three over \(\mathbb C\).
Since \(S[Y,Z]\) is a UFD, that kernel is generated by
one irreducible polynomial F:
\[
A\simeq S[Y,Z]/(F),\qquad
B\simeq\bigl(S[Y,Z]/(F)\bigr)[y_1].
\tag{11}
\]
The kernel meets S trivially, so F is primitive over S
and is not a nonzero base polynomial.
This is an exact presentation, not a claim that F is
a coordinate over S or that the two invariant generators
are algebraically independent.

There is also an explicit actual value of the derived field.
Put \(\omega=pTq-qTp\). Since Q kills all S-coefficients,
Euler's formula and (3) give
\[
\begin{aligned}
H\times Q(x_{\mathrm{tr}})
 &=\frac{\omega}{e}N(p,q)
  =\frac{\omega G(p,q)}{e}\nu,\\
\delta(y_2)
 &= (W\times H)\cdot Q(x_{\mathrm{tr}})
  =\frac{\omega G(p,q)}{e}\ne0.
\end{aligned}
\tag{12}
\]
For nonvanishing, the actual
[Wronskian theorem](binary-wronskian-derived-rank-pass78.md)
gives \(\omega\ne0\). Then \(q/p\) is nonconstant, so
a nonzero homogeneous binary polynomial G cannot vanish
at p,q. This argument includes a dependent unit pair.
The value in (12) belongs to A. It is not asserted to
belong to S, to be a unit, or to be killed by \(\delta\).
Thus (12) is not a new slice or local-slice assertion for D.

## 6. Checks and the remaining gate

For the retained conic seed
\(a=x_1x_3-x_2^2+w\),
\(H=(1,a,a^2)^t\), one may take
\(\nu=(a^2,-2a,1)\), \(\lambda=(1,0,0)\),
\(W=(0,0,1)^t\), and \(V=(0,1,2a)^t\).
Then \(y_1=x_1\), \(y_2=x_2-ax_1\),
\(c=a^2x_1-2ax_2+x_3\), \(P_4=-c\), and
\(z=a+y_2^2\). This verifies both reconstruction formulas
in the already recognized family; it is not a new example.

A plane-hypersurface presentation alone does not force
primitive freeness. The retained intrinsic control
\(D_0=x\partial_y+2y\partial_z\) on
\(\mathbb C[x,y,z]\) has
\(S_0=\mathbb C[u,v]\), \(u=x,v=xz-y^2\), and
presentation \(S_0[y,z]/(uz-y^2-v)\), yet its primitive
coefficient ideal is the proper ideal \((x,y)\).
That control is not asserted to realize all current
original-frame data. It isolates the limitation of (11).

The new conclusion is the constructive relative generation
and its exact presentation. Polynomial recognition still
requires an additional global argument about this actual
hypersurface or the induced primitive derivation.
No historical novelty, new numerical method, regression,
human expert review or formal verification is claimed.
Frozen passes through77 and earlier stable pass78 notes
are unchanged.
