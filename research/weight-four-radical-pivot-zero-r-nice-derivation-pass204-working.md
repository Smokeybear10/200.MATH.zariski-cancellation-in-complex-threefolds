# A nice commuting derivation in the zero-R radical-pivot branch

Status: bounded working reduction for a supplied actual frame. For the full
initial kernel \(\mathsf Z^2-\mathsf X^2\mathsf W\), choose the old-W
pivot. If the resulting polynomial \(R\) is identically zero on the
generic line, an explicit nonzero locally nilpotent derivation of the
original four-ring fixes \(X\), commutes with the sliced derivation, and
has square zero on every original coordinate. This is not yet a
recognition theorem for the invariant ring.

## 1. Actual hypotheses and the choice of pivot

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker\theta_0=(\mathsf Z^2-\mathsf X^2\mathsf W),\qquad
\theta_0(\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 =(a\tau,b\tau,e\tau^2,h\tau^2).
\end{gathered}
\tag{1}
\]
Here the four named generators are actual polynomial coordinates and
the displayed ideal is the entire initial kernel, not one vanishing
relation. The slice \(u\) is not assumed to be an ambient coordinate.
The coefficients \(a,b,e,h\) are nonzero elements of \(A\).

One immediate integral consequence is worth distinguishing from a
coordinate conclusion. The relation gives \(e^2=a^2h\). Thus
\(c=e/a\in\operatorname{Frac}A\) satisfies \(c^2=h\), and
\(c\in A\) because \(A\) is normal. For example, normality follows
directly from \(B=A[u]\): an element of \(\operatorname{Frac}A\)
integral over \(A\) is integral over the normal ring \(B\), hence is
in \(B\cap\operatorname{Frac}A=A\). This does not make \(c\) a
coordinate, or \(a\) an original-ring unit.

To apply the universal chart, interchange only the names of the bad
slots:
\[
\widehat Z=W,\qquad \widehat W=Z,\qquad
t=b/a,\quad \rho=e/a^2,\quad q=h/a^2=\rho^2.
\tag{2}
\]
In these names the full initial relation is
\(\mathsf{\widehat W}^{2}-\mathsf X^2\mathsf{\widehat Z}\).
The pivot is therefore the actual old partial \(\partial_W\), not
\(\partial_Z\).

The exact-shift proof in
[initial-bound157](two-linear-two-quadratic-initial-bound-pass157-working.md)
and the projection and calibration in
[universal184](weight-four-universal-chart-potentials-pass184-working.md)
give
\[
\begin{gathered}
0\ne N=[u^3](\partial_W|_A)\in\operatorname{LND}_{\mathbb C}(A),
\qquad Na=Nb=Ne=Nh=0,\\
S=\ker_A N,\qquad L=\operatorname{Frac}S,\qquad A_L=L[v],\quad Nv=1,\\
t,\rho\text{ algebraically independent over }\mathbb C,
\qquad [L:\mathbb C(t,\rho)]<\infty.
\end{gathered}
\tag{3}
\]
The finite separable field has its uniquely extended commuting
\(t,\rho\) partials. They act on \(L[v]\) while fixing \(v\).
The derivation \(N\) acts as \(\partial_v\) on this line ring.
In particular, \(q_\rho=2\rho\) and \(q_{\rho\rho}=2\), not zero.

## 2. The specialized actual potentials

The projected chart has
\[
\begin{gathered}
B_a=A_a[X],\qquad
Y=y+tX,\\
\widehat Z=z+\sigma X+\rho^2X^2,\qquad
\widehat W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad
L[y,z,w]=L[v],\qquad \mathbb C(y,z,w)=L(v),\\
J(X)=J_0=-a^3\in L^*.
\end{gathered}
\tag{4}
\]
The determinant has rows \(Y,\widehat Z,\widehat W\), columns
\(t,\rho,v\), and holds \(X\) fixed. Its sign is that of these
ordered chart variables and the selected old-W partial. It is the
calibrated actual determinant of universal184, not a separately
assumed formal Jacobian condition.

For \(c\in L\), use the divided Taylor polynomials
\[
H_j(c;U,V)=
\sum_{i=0}^j\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{5}
\]
All coefficient partials in this note keep the formal variables
\(U,V\) fixed before evaluation. Since \(q=\rho^2\), its Taylor
terms of order at least three vanish. The universal identities give
some \(k,n,\ell,m\in L\) with
\[
\begin{aligned}
\sigma&=2\rho\vartheta+k,\\
z-2\rho w&=f(y,\vartheta),
&f(U,V)&=V^2+k_tU+k_\rho V+n,\\
R w+H_2(k;y,\vartheta)+H_1(n;y,\vartheta)&=\ell,
&R&=2\vartheta+k_\rho,\\
w^2+f_\rho(y,\vartheta)w+H_3(k;y,\vartheta)
 +H_2(n;y,\vartheta)-\ell_t y-\ell_\rho\vartheta&=m.
\end{aligned}
\tag{6}
\]
In particular, the last potential contains the monic term \(w^2\).
It cannot be replaced by an absent-W potential that is linear in
\(w\).

Write
\[
\mathcal B=k_{tt}y+k_{t\rho}\vartheta+n_t,
\qquad
\mathcal C=2w+k_{t\rho}y+k_{\rho\rho}\vartheta+n_\rho.
\tag{7}
\]
At \(X=0\), the reduced determinant rows of universal184 are
\[
dy,\qquad R\,d\vartheta+\mathcal B\,dt+\mathcal C\,d\rho,
\qquad dw,
\quad
\left[dy\wedge
 (R\,d\vartheta+\mathcal B\,dt+\mathcal C\,d\rho)
 \wedge dw\right]_{dt\wedge d\rho\wedge dv}=-a^3.
\tag{8}
\]
These equations retain the actual full-line equality and scalar
calibration from (4).

## 3. If R is identically zero, the entire projected line is affine

Assume now the additional branch hypothesis
\[
R=0\quad\hbox{as an element of }L[v].
\tag{9}
\]
It first gives \(\vartheta=-k_\rho/2\in L\). The element \(y\)
cannot also belong to \(L\). If it did, the fourth identity in (6)
would be a monic quadratic equation for \(w\in L[v]\), all of
whose coefficients lie in \(L\). A nonconstant polynomial \(w\)
cannot satisfy that equation, by comparing its highest \(v\)-degree.
Thus \(w\in L\), then the second identity gives \(z\in L\),
contradicting \(L[y,z,w]=L[v]\).

Consequently \(y\) is transcendental over \(L\). The third identity
of (6), with \(R=0\), becomes
\[
\frac{k_{tt}}2y^2+(k_{t\rho}\vartheta+n_t)y
 +\frac{k_{\rho\rho}}2\vartheta^2+n_\rho\vartheta=\ell.
\tag{10}
\]
Comparing the coefficients of this polynomial in \(y\) gives
\(k_{tt}=0\) and \(k_{t\rho}\vartheta+n_t=0\). Hence
\(\mathcal B=0\). Equation (8) now factors as
\[
\mathcal C\,(y_t w_v-y_v w_t)=-a^3.
\tag{11}
\]
Both factors on the left belong to \(L[v]\); their product is a
nonzero scalar in \(L\). Thus each factor is a unit of that
polynomial ring and, in particular, \(\mathcal C\in L^*\).
From (7) and (6),
\[
w=-\frac{k_{t\rho}}2y
 +\frac{\mathcal C-k_{\rho\rho}\vartheta-n_\rho}{2},
\qquad
z=2\rho w+\vartheta^2+k_t y+k_\rho\vartheta+n.
\tag{12}
\]
Therefore \(w,z\) are affine polynomials in \(y\) over \(L\),
and the whole-line return gives \(L[y]=L[v]\). Comparing degrees
in a polynomial inverse for \(y\) shows that
\(y=\alpha v+\beta\), with \(\alpha\in L^*\) and \(\beta\in L\).
In particular,
\[
Ny\ne0,\qquad N^2y=N^2z=N^2w=0,
\qquad N\vartheta=N\sigma=0.
\tag{13}
\]
The last equality uses \(\sigma=2\rho\vartheta+k\). These are
identities on the actual localization, not conclusions that its
coefficient field consists of original polynomial coordinates.

## 4. Return an actual locally nilpotent derivation to B

Extend \(N\) from \(A\) to \(B=A[u]\) by \(Nu=0\). This extension
is a locally nilpotent derivation and commutes with \(E\). Define
\[
P=aN-(NX)E\in\operatorname{Der}_{\mathbb C}(B).
\tag{14}
\]
Every coefficient in (14) belongs to the original ring. It is not
necessary that \(NX=0\): writing \(X=x_0+au\) gives
\(NX=Nx_0\in A\), because \(Na=0\). Directly,
\[
PX=0,\qquad P|_A=aN,\qquad
[E,P]=0,
\tag{15}
\]
where the commutator follows from \(Ea=0\), \([E,N]=0\), and
\(E(NX)=N(EX)=Na=0\).

Local nilpotence is not inferred merely from a sum of two LNDs.
Since \(Na=0\), the derivation \(aN\) is locally nilpotent on
\(A_a\). In the actual polynomial presentation \(B_a=A_a[X]\),
the derivation \(P\) restricts to \(aN\) on \(A_a\) and fixes
\(X\). It is consequently locally nilpotent on \(B_a\). It
already preserves \(B\) by its definition, so every element of
\(B\) is killed by some iterate, and \(P\) is an LND of \(B\).

Equations (4) and (13), together with \(PX=0\) and \(Na=0\), give
\[
PY=aNy\ne0,\qquad
P^2X=P^2Y=P^2\widehat Z=P^2\widehat W=0.
\tag{16}
\]
For instance, \(P^2Y=a^2N^2y\) and
\(P^2\widehat W=a^2N^2w\), since \(t,\rho,\vartheta\in L\).
The analogous equality for \(\widehat Z\) uses \(\sigma\in L\).
These equalities may be checked in \(B_a\), then hold in the
original domain \(B\). Undoing the notational swap (2) proves
the asserted square-zero property on the original \(Z,W\).
Thus \(P\) is a nonzero nice LND of the original four-ring,
commuting with \(E\) and fixing the actual coordinate \(X\).
Here “nice” means precisely square zero on this displayed
polynomial coordinate system.

## 5. Exact conclusion and the remaining gate

This proves the conditional implication (9) to (14)--(16), using
the supplied actual full initial kernel and global slice. It does
not prove that \(R=0\) occurs, or that \(R\ne0\) is excluded.
For \(R\ne0\), the essential quadratic term in (6) remains.

Even in the branch (9), a nonzero nice LND \(P\) commuting with
\(E\) is not by itself an \(E\)-invariant ambient coordinate.
No theorem recognizing this commuting pair has been applied here.
The statement therefore does not yet conclude
\(A\simeq\mathbb C^{[3]}\), does not lower the original E-degree
profile, and does not transfer an absent-W recognition result to
this nonzero-radical relation.

The derivation uses only the retained actual mechanisms of157 and184,
whose cited arguments were fully reread for this note. No finite
checker has been authored or executed for it. This working proof is
not human expert review or proof-assistant verification, and it
asserts no historical novelty, unrestricted cancellation theorem,
or entry theorem. Earlier frozen artifacts are unchanged.
