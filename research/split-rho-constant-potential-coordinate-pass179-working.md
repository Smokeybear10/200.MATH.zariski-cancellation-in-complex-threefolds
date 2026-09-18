# An invariant coordinate when the normalized split coefficient m is rho-constant

**Status: working recognition of the normalized \(m_\rho=0\) branch.**

In the normalized nonlinear-graph split chart178, the additional
condition \(m_\rho=0\) produces an actual invariant coordinate.
Its formula is polynomial in the original normalized coordinates,
and a second explicit polynomial supplies both inverse orders.
The global slice makes the invariant ring regular, so the
Bhatwadekar--Gupta--Lokhande theorem recognizes it as
\(\mathbb C^{[3]}\).

This is a conditional subcase, not a claim that \(m_\rho\) always
vanishes. It neither uses nor reinstates the rejected determinant
cube shortcut178.

## 1. Precise actual assumptions

Retain the full actual split hypotheses175--177 and the actual
constant-good normalization of
[the coefficient note178](split-affine-graph-coefficient-normal-form-pass178-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad A=\ker E,\quad Eu=1,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad
\ker\theta_0=(\mathsf X\mathsf Z+\mathsf Y\mathsf W),\\
a=EX\ne0,\quad N=[u^3](\partial_Z|_A),\quad
L=\operatorname{Frac}(\ker_A N),\quad A_L=L[v],\quad Nv=1,\\
t=EY/a,\quad \rho=(E^2W/2)/a^2,\quad
[L:\mathbb C(t,\rho)]<\infty,\quad K=\ker_L\partial_\rho,\\
y=\gamma v+\eta,\quad \gamma\in L^*,\quad\eta\in L,\quad
\vartheta=P(y),\quad 2\le\deg P\le4,\\
r=k_\rho=0,\quad k,n_0,\ell\in K,\quad n=d\rho+n_0,\quad
d\in\mathbb C^*,\qquad m_\rho=0 .
\end{gathered}
\tag{1}
\]
The displayed \(X,Y,Z,W\) are the normalized actual coordinates,
obtained in178 by constant translations with explicit inverses.
All coefficient partials on \(L\) are its unique commuting
extensions from \(\mathbb C(t,\rho)\). The exact joint constant
field is \(\mathbb C\); \(K\) is finite algebraic over
\(\mathbb C(t)\), not assumed rational. In particular \(m\in K\).

The actual fixed-\(X\) chart, its literal split polynomial, and
the two normalized potentials are
\[
\begin{gathered}
Y=y+tX,\qquad W=w+\vartheta X+\rho X^2,\qquad H=XZ+YW,\\
H=yw+(k'y+d\rho+n_0)X+kX^2,\\
-yw+\frac{k''}{2}y^2+n_0'y+d\vartheta=\ell,\qquad
dw+\frac{k'''}6y^3+\frac{n_0''}2y^2-\ell'y=m .
\end{gathered}
\tag{2}
\]
Primes denote \(\partial_t\) on the exact field \(K\).
The coefficient equations178, on imposing \(m_\rho=0\), give
\[
k''''=0,\qquad n_0'''=0,\qquad \ell''=0 .
\tag{3}
\]
These conclusions use the positive-\(y\) determinant
coefficients only. The constant coefficient remains
\(-m_t=-a^3/(Ny)\ne0\), with its actual parameter factor.

## 2. Exact-field polynomiality of the coefficients

The joint constant field and (3) give complex constants
\(k_3,k_2,k_1,k_0,n_2,n_1,n_{00},\ell_1,\ell_0\) with
\[
\begin{aligned}
k&=k_3t^3+k_2t^2+k_1t+k_0,\\
n_0&=n_2t^2+n_1t+n_{00},\qquad
\ell=\ell_1t+\ell_0 .
\end{aligned}
\tag{4}
\]
For example \(k'''\) is killed by both coefficient partials,
so \(k'''=6k_3\) for \(k_3\in\mathbb C\). Subtract \(k_3t^3\);
its remaining second derivative is again a joint constant.
Successive explicit polynomial subtractions prove the assertion
for \(k\), and the same argument applies to \(n_0,\ell\).
There is no integration of an arbitrary algebraic function and
no assumption \(K=\mathbb C(t)\).

Define actual polynomials with these complex coefficients:
\[
\begin{aligned}
K_3(X,Y)&=k_3Y^3+k_2XY^2+k_1X^2Y+k_0X^3,\\
N_2(X,Y)&=n_2Y^2+n_1XY+n_{00}X^2,\\
Q(X,Y)&=K_3(X,Y)+N_2(X,Y)-\ell_1Y-\ell_0X,\\
I&=dW-XH+Q(X,Y).
\end{aligned}
\tag{5}
\]
The subscripts on \(K_3,N_2\) indicate homogeneous degree.
Their coefficients may vanish, subject only to the stated graph-degree assumption.

## 3. The proposed polynomial is exactly the generic coefficient m

Substitute \(Y=y+tX\) in the first two polynomials of (5).
Their full finite expansions are
\[
\begin{aligned}
K_3(X,Y)&=kX^3+k'yX^2+\frac{k''}{2}y^2X+k_3y^3,\\
N_2(X,Y)&=n_0X^2+n_0'yX+n_2y^2 .
\end{aligned}
\tag{6}
\]
Using the literal \(H\) in (2), and then its first potential,
gives
\[
\begin{aligned}
XH-K_3-N_2
&=d\rho X^2+
   \left(yw-\frac{k''}{2}y^2-n_0'y\right)X-k_3y^3-n_2y^2\\
&=d\rho X^2+(d\vartheta-\ell)X-k_3y^3-n_2y^2 .
\end{aligned}
\tag{7}
\]
Consequently the polynomial \(I\) has the following equality
in the actual localized chart:
\[
\begin{aligned}
I
&=d(w+\vartheta X+\rho X^2)
 -(XH-K_3-N_2)-\ell_1(y+tX)-\ell_0X\\
&=dw+k_3y^3+n_2y^2-\ell_1y\\
&=m .
\end{aligned}
\tag{8}
\]
The last line is the second potential in (2), using (4).
Every positive power of \(X\) has canceled by the displayed
identities. Since \(m\in L\) and \(E\) kills \(L\), this gives
\(EI=0\) in the chart. The original polynomial ring embeds in
that localization, so \(EI=0\) in \(B\). Thus (8) is a proved
integral return of this specific coefficient, not a general
descent of a generic coordinate.

## 4. A polynomial companion and both inverse orders

Writing \(H=XZ+YW\), equation (5) becomes
\[
I-Q=-X^2Z+(d-XY)W .
\]
Choose the companion
\[
J=(d+XY)Z+Y^2W,\qquad
\begin{pmatrix}I-Q\\J\end{pmatrix}
=
\begin{pmatrix}-X^2&d-XY\\d+XY&Y^2\end{pmatrix}
\begin{pmatrix}Z\\W\end{pmatrix}.
\tag{9}
\]
The matrix determinant is the nonzero complex constant
\(-d^2\). For independent target variables \(x,y_1,i,j\),
put \(U_0=i-Q(x,y_1)\) and define
\[
X=x,\quad Y=y_1,\quad
Z=\frac{(d-xy_1)j-y_1^2U_0}{d^2},\qquad
W=\frac{(d+xy_1)U_0+x^2j}{d^2}.
\tag{10}
\]
These are polynomials because \(d\in\mathbb C^*\).

Both inverse orders can be checked without any localization.
For the substitution of (9) into (10), the two numerators are
\[
\begin{aligned}
(d-XY)J-Y^2(I-Q)&=d^2Z,\\
(d+XY)(I-Q)+X^2J&=d^2W .
\end{aligned}
\tag{11}
\]
The mixed coefficients cancel, and the remaining identity is
\((d-XY)(d+XY)+X^2Y^2=d^2\).
Conversely substitute (10) into the two rows of (9).
The first row becomes \(U_0\), the second becomes \(j\);
adding \(Q(x,y_1)\) recovers \(i\), and the first two coordinates
remain \(x,y_1\). Hence
\[
B=\mathbb C[X,Y,I,J],\qquad I\in A .
\tag{12}
\]
In particular \(I\) is an actual invariant coordinate, not just
a polynomial invariant with a nonzero gradient. No claim that
the companion \(J\) is invariant is needed.

## 5. Regular-kernel recognition with its precise external input

The global slice already gives \(B=A[u]\), hence
\(A\simeq B/(u)\). Write \(E\) in the original polynomial
coordinates. The identity \(Eu=1\) expresses one as a
polynomial linear combination of the four partial derivatives
of \(u\). They therefore generate the unit ideal. The
hypersurface \(u=0\) is smooth over \(\mathbb C\), so \(A\)
is a regular ring.

Now (12) presents \(B\) as a polynomial ring in three variables
over \(\mathbb C[I]\). The original \(E\) is a nonzero
\(\mathbb C[I]\)-linear LND, since \(EI=0\) and \(Eu=1\).
Bhatwadekar--Gupta--Lokhande
[Theorem 3.5](https://arxiv.org/html/1501.01438v1)
states that a nonzero \(k[T]\)-linear LND on
\(k[T,X,Y,Z]\), in characteristic zero, has kernel
\(k[T]^{[2]}\) when that kernel is regular.
The hypotheses have now all been checked in the actual ring.
Therefore
\[
A=\mathbb C[I]^{[2]}\simeq\mathbb C^{[3]} .
\tag{13}
\]
The exact theorem statement and its displayed short proof were
freshly inspected in the primary paper. Its cited prerequisite
theorems have not been re-proved or recursively audited here.

## Scope

This recognizes the additional \(m_\rho=0\) branch of the
normalized nonlinear-graph chart178. The argument permits the
degree-three and degree-four graph coefficients in (4); it is
not restricted to the quadratic subcase already recognized
there. It does not establish that \(m_\rho=0\) holds for every
actual frame, nor address graph degree at most one, other initial
configurations, or unrestricted cancellation.

Neither \(a\) nor \(Ny\) was declared constant or a global unit.
The determinant's generic-parameter factor played no role in
the polynomial identities (5)--(12). The actual translations
that produced the normalized chart have explicit polynomial
inverses in178, so their composition with (10) gives an actual
coordinate description in the pre-normalized frame as well.

No checker was executed or imported. No178 or earlier source,
packet, or live index was edited. This is a source-dependent
working proof, not a historical novelty claim, a human expert
certification, or a proof-assistant verification.
