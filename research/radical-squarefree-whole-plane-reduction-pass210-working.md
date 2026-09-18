# Squarefree whole radical planes have only a linear second generator

Status: working necessary reduction in the supplied actual radical chart.
A whole projected plane with nonconstant squarefree center and nonconstant
second generator has both projected degrees at most two. Its second
generator cannot be quadratic. The latter exclusion uses an irreducible
polynomial in the original four coordinates, not an assumed descent of
a generic parameter.

The remaining affine-second-generator cases are not recognized here.
This is not a proof of unrestricted cancellation.

## 1. Actual inputs and the center fiber

Retain all the actual hypotheses and notation of
[eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad a=EX\ne0,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\qquad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\\
L/\mathbb C(t,\rho)\text{ finite},\quad A_L=L[v],\quad Nv=1,\\
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2 .
\end{gathered}
\tag{1}
\]
The selected derivation is the actual coefficient of the literal
\(\partial_Z\). The field need not be rational. The two coefficient
partials commute and have joint constants \(\mathbb C\).

For independent formal \(U,V\), put
\[
\begin{gathered}
\mathcal R=2V+k_\rho,\qquad
S=\tfrac12k_{tt}U^2+k_{t\rho}UV+\tfrac12k_{\rho\rho}V^2+n_tU+n_\rho V,\\
T=\ell-S,\quad b_0=S_V,\quad
\mathcal H=T^2+\mathcal R b_0T+
\mathcal R^2\{H_3(k)+H_2(n)-\ell_tU-\ell_\rho V-m\}=GQ,\\
V_c=-k_\rho/2,\quad p(U)=S(U,V_c)-\ell,\quad
R=\mathcal R(y,\vartheta)\ne0 .
\end{gathered}
\tag{2}
\]
Here \(H_j\) is the divided Taylor polynomial in \(U,V\), and
\((G)\) is the entire evaluation kernel in \(L[U,V]\).
The actual identities from206 are
\[
\begin{gathered}
Rw+S(y,\vartheta)-\ell=0,\qquad
z=2\rho w+\vartheta^2+k_ty+k_\rho\vartheta+n,\\
0\ne Q(y,\vartheta)\mid R^3,\qquad
\mathcal H(U,V_c)=p(U)^2,\qquad
\deg G=\max(\deg_vy,\deg_v\vartheta)\le5,\\
\deg_v\vartheta=\deg_U G\le4,\qquad
\deg\mathcal H\le5,\quad \mathcal H_5=4V^2H_3(k),\\
[U^4]\mathcal H=k_{tt}^2/4,\qquad \deg_U\mathcal H\le4 .
\end{gathered}
\tag{3}
\]
In this note assume
\[
C=L[y,\vartheta]=L[v],\qquad
p\text{ nonconstant and squarefree},\qquad e:=\deg_v\vartheta>0.
\tag{4}
\]
Thus \(R\) is nonconstant. Write \(d=\deg_vy\), allowing \(y\)
to be constant when stating the upper degree bounds below.

The equality \(C=L[v]\) proves both injectivity and immersion of the
parametrization after algebraic closure. Indeed \(v=P(y,\vartheta)\)
for a polynomial \(P\) over \(L\). Equal pairs have equal parameters,
and differentiating gives
\(1=P_U(y,\vartheta)y_v+P_V(y,\vartheta)\vartheta_v\).

Use the evaluated coefficients
\[
\begin{gathered}
B_1=S_U(y,\vartheta),\quad C_1=2w+b_0(y,\vartheta),\\
\Lambda_i=\ell_i-S_i(y,\vartheta)-k_{\rho i}w,\quad i=t,\rho,\\
B_1y_v+C_1\vartheta_v+Rw_v=0,\\
R\,dw=-B_1dy-C_1d\vartheta+\Lambda_tdt+\Lambda_\rho d\rho,\\
J_0=[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw]
_{dt\wedge d\rho\wedge dv}=-a^3\in L^*,\\
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\quad
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho).
\end{gathered}
\tag{5}
\]
Coefficient derivatives in \(\Lambda_i\) are formed before evaluation.

At any root \(r\) of \(R\), one has \(\vartheta(r)=V_c\),
\(p(y(r))=0\), and \(B_1(r)=p'(y(r))\ne0\).
If \(r\) were a multiple root, then \(\vartheta_v(r)=0\);
the third identity of (5) would force \(y_v(r)=0\), contradicting
immersion. Hence \(R\) is squarefree. Injectivity makes the values
\(y(r)\) distinct for its distinct roots. Consequently
\[
e=\deg R\le\deg p\le2 .
\tag{6}
\]

Normalize \(G\) to be monic in \(U\) over \(L[V]\). To justify this,
\(L[v]\) is free over \(L[\vartheta]\) with basis
\(1,v,\ldots,v^{e-1}\): polynomial division proves spanning and
degrees modulo \(e\) prove independence. Multiplication by \(y\)
has a monic characteristic polynomial of degree \(e\). Its minimal
polynomial has that degree as well, since \(L(y,\vartheta)=L(v)\);
the characteristic polynomial is exactly \(G\).
Specialization at \(V_c\) is multiplication on \(L[v]/(R)\).
The roots of \(R\) are simple with distinct \(y\)-values, so
\[
G(U,V_c)=\prod_{R(r)=0}(U-y(r)),\qquad
G_U(y(r),V_c)\ne0 .
\tag{7}
\]
The product is over an algebraic closure, and the resulting identity
is over the exact field \(L\).

## 2. The evaluated cofactor has exactly the return divisor

Fix a root \(r\) of \(R\). Suppose \(C_1(r)=0\).
The third identity of (5) gives \(y_v(r)=0\).
Since \(\vartheta_v(r)\ne0\), differentiating \(G(y,\vartheta)=0\)
gives \(G_V(y(r),V_c)=0\).
On the other hand, \(G_U\) is nonzero there by (7).
The first gradient in (5), together with
\(\mathcal H_U(y,\vartheta)=Q(y,\vartheta)G_U(y,\vartheta)\),
therefore gives
\(\operatorname{ord}_r Q(y,\vartheta)\ge2\).
It follows that \(\mathcal H_V(y,\vartheta)\) has order at least
three at \(r\), including the case where it is identically zero.

In the second gradient in (5), \(R C_1^2\) has order at least
three. Because \(R\) is simple, comparison of the order-two term
forces \(\Lambda_\rho(r)=0\).
Now take the \(\rho\)-coefficient in the differential identity (5),
with the original \(v\) fixed. At \(r\) it says
\(0=-B_1(r)y_\rho(r)\), so \(y_\rho(r)=0\).
At that point \(dy=y_tdt\), while the middle one-form in the
calibrated wedge is \(B_1dt\). Thus \(J_0(r)=0\), impossible.

We have proved \(C_1(r)\ne0\) at every root of \(R\).
The first gradient in (5) and (7) now show that the evaluated
cofactor has order exactly one there. There are no other roots
by (3). Therefore
\[
Q(y,\vartheta)=\eta R,\qquad \eta\in L^* .
\tag{8}
\]
This is initially an evaluated identity, not a formal equality
\(Q=\eta\mathcal R\).

If \(D:=\deg G=\max(d,e)\ge3\), then
\(\deg Q\le5-D\le2<D\). The polynomial \(Q-\eta\mathcal R\)
vanishes on the parametrization and has degree less than \(G\),
so it is zero. But then \(\mathcal H(U,V_c)=0\), contradicting
\(p\ne0\). We conclude
\[
\boxed{\deg_vy\le2,\qquad 1\le\deg_v\vartheta\le2.}
\tag{9}
\]

## 3. A quadratic second generator forces a very rigid eliminant

Assume \(e=2\). Equation (6) makes \(p\) quadratic; put
\(\kappa=k_{tt}/2\ne0\). Complete the square in \(\vartheta\)
over \(L\), without taking square roots, to write
\(\vartheta=V_*+b x^2\), \(b\in L^*\), \(x=v+s\).
The degree bound and \(L[y,\vartheta]=L[x]\) give
\[
y=\mu\vartheta+\nu+c x,\quad c\in L^*,\qquad
G=(U-\mu V-\nu)^2-\tau(V-V_*),\quad \tau=c^2/b\ne0 .
\tag{10}
\]
Indeed the coefficient of \(x\) must be nonzero, or both
generators would belong to \(L[x^2]\).
In particular \(G_2=(U-\mu V)^2\) and \(G\) is monic in \(U\).

Since (8) holds and \(\deg Q\le3\), division by the kernel gives
\[
Q=\eta\mathcal R+GF,\qquad \deg F\le1,\qquad
\mathcal H=G^2F+\eta\mathcal R G .
\tag{11}
\]
The \(U\)-degree bound in (3) forces \(F_U=0\).
Write \(F=b_1V+b_0\). The coefficient of \(U^4V\) in
\(\mathcal H_5=b_1V(U-\mu V)^4\) is \(b_1\).
It is zero in the literal \(4V^2H_3(k)\), so \(b_1=0\).
The center fiber (7) and the two roots of \(p\) give
\(p=\kappa G(U,V_c)\). Hence \(F=\kappa^2\).
Thus \(\mathcal H\) has degree four and \(H_3(k)=0\).

All third coefficient partials of \(k\) vanish. The joint constants
are \(\mathbb C\), so \(k\) is a quadratic polynomial in \(t,\rho\)
with complex coefficients, and \(\kappa\in\mathbb C^*\).
The exact quartic part from206 has zero \(U^3V\) coefficient.
Comparing it with \(\kappa^2G_2^2\) gives
\(-4\kappa^2\mu=0\). Therefore \(\mu=0\), and \(y\) is affine.

Apply the actual elementary normalizations from Section5 of
[exclusion209](radical-cubic-second-projection-exclusion-pass209-working.md).
For
\(k=\kappa t^2+A t\rho+(B_0/2)\rho^2+C_0t+D_0\rho+F_0\),
translate \(X\) by \(-B_0/4\), add \((A/2)Y+(D_0/2)X\) to \(W\),
and subtract \(C_0Y+F_0X\) from \(Z\).
Their polynomial inverses are the opposite elementary operations.
They preserve the actual selected partial, \(N,L,t,\rho,a,R\),
the full initial kernel, and the projected degrees. Only scalar
terms in \(L\) change in \(y,\vartheta\); the two distinct
center values remain distinct. Relabel these actual coordinates.
Then
\[
k=\kappa t^2,\quad R=2\vartheta,\quad V_c=0,\quad
G_2=U^2,\quad \mathcal H_4=\kappa^2U^4 .
\tag{12}
\]
The literal quartic part is
\(\kappa^2U^4+2n_{tt}U^2V^2+4n_{t\rho}UV^3+
2n_{\rho\rho}V^4\).
Thus
\[
n=\alpha t+\beta\rho+\gamma,\qquad
\alpha,\beta,\gamma\in\mathbb C,\qquad
p(U)=\kappa U^2+\alpha U-\ell .
\tag{13}
\]
The monic conic (10), now with \(\mu=0\), has the form
\(G=p(U)/\kappa-\tau V\), \(\tau\in L^*\).
The literal eliminant and (11) say respectively
\[
\begin{gathered}
\mathcal H=p(U)^2-
V^2(4\ell_tU+4\ell_\rho V+\beta^2+4m),\\
\mathcal H=\kappa^2\{p(U)/\kappa-\tau V\}^2+
2\eta V\{p(U)/\kappa-\tau V\}.
\end{gathered}
\tag{14}
\]
The coefficient linear in \(V\) gives \(\eta=\kappa^2\tau\).
The remaining comparison gives
\[
\ell_t=\ell_\rho=0,\quad \ell\in\mathbb C,\quad
\beta^2+4m=\kappa^2\tau^2,\qquad
c:=2w+\beta=-\kappa\tau\in L^* .
\tag{15}
\]
The last equality follows from the third potential and
\(p(y)=\kappa\tau\vartheta\), cancelling the nonzero \(\vartheta\).

## 4. An original polynomial cannot become this square

Put \(h=\alpha/(2\kappa)\), \(d_0=\ell+\alpha^2/(4\kappa)\),
and \(\bar y=y+h\). These two constants belong to \(\mathbb C\);
squarefreeness gives \(d_0\ne0\), though the following argument
does not need it. The actual potentials now read
\[
c\vartheta=d_0-\kappa\bar y^2,\qquad
z=\rho c+\vartheta^2+2\kappa t\bar y+\gamma .
\tag{16}
\]
Expand the original expressions (1), without dividing by a
coordinate. All terms of degree at least two in \(X\) cancel, giving
\[
\boxed{c^2=(2W+\beta)^2+
4\kappa X(Y+h)^2-4X^2(Z-\gamma)-4d_0X.}
\tag{17}
\]
Each entry on the right is an original polynomial coordinate
after the specified actual elementary maps.

The right side is irreducible in \(B\). Indeed set
\(Y_0=Y+h,\ W_0=2W+\beta,\ Z_0=Z-\gamma\).
These are actual affine coordinates over \(\mathbb C\). In
\(\mathbb C[X,Y_0,W_0][Z_0]\) the polynomial is linear in \(Z_0\)
with coefficients \(-4X^2\) and
\(W_0^2+4\kappa XY_0^2-4d_0X\). Their gcd is one:
the latter coefficient is not divisible by \(X\).
It is primitive and irreducible over the coefficient fraction field,
so Gauss's lemma proves irreducibility in \(B\).

But \(c\in L\subset\operatorname{Frac}B\). A nonconstant irreducible
element of a UFD cannot be a square in its fraction field:
its prime valuation is one, whereas the valuation of a square is
even. Equation (17) is therefore impossible. This excludes \(e=2\).

Combining (9) and this exclusion proves the necessary restriction
\[
\boxed{C=L[v],\ p\text{ nonconstant squarefree},\quad
\vartheta\notin L\quad\Longrightarrow\quad
\deg_v\vartheta=1,\quad \deg_v y\le2.}
\tag{18}
\]

The argument neither declares \(v\) an ambient coordinate nor
promotes an \(L\)-unit to a polynomial unit. Affine-second-generator
recognition, the other centers, other initial kernels and arbitrary
entry remain separate tasks. The earlier209 proper-plane theorem is
not used to assume whole-plane recognition.

The complete eliminant206, conductor206, and exclusion209 sources
were reread before this note. Its root-multiplicity and cofactor
argument has an independent reconstruction; a saved-source review
and a dedicated finite checker remain separate requirements.
No earlier proof or frozen packet was edited. This is private
working mathematics, not human expert review, proof-assistant
certification, or novelty clearance.
