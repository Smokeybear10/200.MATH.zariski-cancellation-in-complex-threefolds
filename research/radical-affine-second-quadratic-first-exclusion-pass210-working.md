# A squarefree radical center excludes an affine-second quadratic graph

Status: bounded working exclusion. In the supplied actual radical chart,
with nonconstant squarefree center and whole projected plane, the pair
\((\deg_v y,\deg_v\vartheta)=(2,1)\) is impossible. The final obstruction
is an irreducible original polynomial forced to be a square in the
original fraction field. It is not an inference that a generic parameter
is an ambient coordinate.

This leaves other whole-plane degree pairs, including two affine
projections and quadratic second projection. It supplies no arbitrary
entry or unrestricted cancellation theorem.

## 1. Actual input and the root cofactor

Retain all actual hypotheses and identities of
[radical eliminant206](weight-four-radical-nonzero-r-eliminant-pass206-working.md):
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\quad a=EX\ne0,\quad
\ker\theta_0=(\mathsf X^2\mathsf Z-\mathsf W^2),\\
L/\mathbb C(t,\rho)\text{ finite},\qquad A_L=L[v],\quad Nv=1,\\
Y=y+tX,\quad Z=z+(2\rho\vartheta+k)X+\rho^2X^2,\quad
W=w+\vartheta X+\rho X^2,\\
L[y,\vartheta]=L[v],\qquad
\deg_v y=2,\quad\deg_v\vartheta=1,\qquad J_0=-a^3\in L^*.
\end{gathered}
\tag{1}
\]
The selected partial is the literal \(\partial_Z\), and the coefficient
partials commute. The joint constants in \(L\) are \(\mathbb C\).
The leading ideal is the entire initial kernel, not merely a relation.

Use the notation of that source:
\[
\begin{gathered}
\mathcal R=2V+k_\rho,\quad
S=H_2(k;U,V)+n_tU+n_\rho V,\quad b_0=S_V,\quad T=\ell-S,\\
Q_0=H_3(k;U,V)+H_2(n;U,V)-\ell_tU-\ell_\rho V-m,\\
z=2\rho w+\vartheta^2+k_ty+k_\rho\vartheta+n,\\
Rw+S(y,\vartheta)=\ell,\qquad
w^2+b_0(y,\vartheta)w+Q_0(y,\vartheta)=0,\qquad
R=2\vartheta+k_\rho,\\
\mathcal H=T^2+\mathcal R b_0T+\mathcal R^2Q_0=GQ,\qquad
0\ne Q(y,\vartheta)\mid R^3 .
\end{gathered}
\tag{2}
\]
Here \(H_j\) is the divided Taylor polynomial, and \(k,n,\ell,m\in L\).
Set \(V_c=-k_\rho/2\) and \(p(U)=S(U,V_c)-\ell\).
Assume \(p\) is nonconstant and squarefree. In particular it has degree
one or two. The literal identity is \(\mathcal H(U,V_c)=p(U)^2\).

For clarity, the cofactor needed below can be proved directly in this
affine-second case. Write \(y=P(\vartheta)\), where
\[
G=U-P(V),\qquad P(V)=A_2V^2+A_1V+A_0,\qquad A_2\in L^*.
\tag{3}
\]
The single root \(r\in L\) of \(R\) is simple. At this root put
\(B_1=S_U(y,\vartheta)=p'(y)\ne0\),
\(C_1=2w+b_0(y,\vartheta)\), and
\(\Lambda_i=\ell_i-S_i(y,\vartheta)-\mathcal R_iw\).
Coefficient partials precede evaluation. The retained identities are
\[
\begin{gathered}
B_1y_v+C_1\vartheta_v+Rw_v=0,\\
\mathcal H_U(y,\vartheta)=-R(C_1B_1+R\Lambda_t),\qquad
\mathcal H_V(y,\vartheta)=-R(C_1^2+R\Lambda_\rho),\\
Rw_\rho=-B_1y_\rho-C_1\vartheta_\rho+\Lambda_\rho,\\
J_0=[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)\wedge dw]_{dt\,d\rho\,dv}.
\end{gathered}
\tag{4}
\]

Suppose \(C_1(r)=0\). The first identity gives \(y_v(r)=0\), hence
\(G_V(y(r),\vartheta(r))=-P'(V_c)=0\), whereas \(G_U=1\).
The \(U\)-gradient makes \(Q(y,\vartheta)\) vanish to order at least
two at \(r\). Thus \(\mathcal H_V=Q(y,\vartheta)G_V(y,\vartheta)\)
has order at least three. Its literal expression in (4) forces
\(\Lambda_\rho(r)=0\). The fixed-\(v\) coefficient derivative in (4)
then gives \(y_\rho(r)=0\). At that parameter the middle wedge factor
is \(B_1dt\), while \(dy=y_tdt\). This contradicts \(J_0\ne0\).

Therefore \(C_1(r)\ne0\). The \(U\)-gradient in (4), with \(B_1(r)\ne0\),
now gives a simple zero of \(Q(y,\vartheta)\) at \(r\).
Together with its divisibility by \(R^3\), this proves
\[
Q(y,\vartheta)=\eta R,\qquad \eta\in L^*.
\tag{5}
\]
Since \(\deg\mathcal H\le5\) and \(\deg G=2\), the polynomial
\(Q-\eta\mathcal R\) is in \((G)\), and its quotient has degree at most
one. Consequently
\[
\mathcal H=G^2D+\eta\mathcal R G,\qquad \deg D\le1.
\tag{6}
\]
This promotes only a proved vanishing polynomial through the exact
plane ideal; it does not promote arbitrary evaluated coefficients.

## 2. The center degree and the exact quadratic coefficient

If \(p\) is quadratic, \(k_{tt}\ne0\). The exact coefficient
\([U^4]\mathcal H=k_{tt}^2/4\) is nonzero. But (6), since \(G\) has
\(U\)-degree one and \(D\) is affine, has \(U\)-degree at most three.
This contradiction leaves the linear-center case \(k_{tt}=0\).
Put
\[
B_0=n_t-\frac{k_{t\rho}k_\rho}{2}\ne0 .
\tag{7}
\]
This is the coefficient of \(U\) in \(p\). The identity \(k_{tt}=0\)
also gives \(k_{ttt}=k_{tt\rho}=0\). A direct collection of the \(U^2\)
coefficient of (2) gives
\[
[U^2]\mathcal H
 =(k_{t\rho}V+n_t)^2
  -\mathcal R\,k_{t\rho}(k_{t\rho}V+n_t)
  +\frac{n_{tt}}2\mathcal R^2
 =B_0^2+\frac{(B_0)_t}{2}\mathcal R^2 .
\tag{8}
\]
Indeed \((B_0)_t=n_{tt}-k_{t\rho}^2/2\).

The literal \(U\)-degree of \(\mathcal H\) is at most two when
\(k_{tt}=0\). Equation (6) therefore forces \(D_U=0\).
Its \(U^2\) coefficient is then exactly \(D(V)\), an affine
polynomial. Equation (8) forces
\[
(B_0)_t=0,\qquad D=B_0^2,\qquad
\mathcal H=B_0^2G^2+\eta\mathcal R G .
\tag{9}
\]
In particular \(\deg\mathcal H=4\). Its fifth homogeneous part is
\(4V^2H_3(k)\), so all third coefficient partials of \(k\) vanish.
The joint-constant property now gives
\[
k=c_1t\rho+\frac{c_2}{2}\rho^2+c_3t+c_4\rho+c_5,
\qquad c_i\in\mathbb C .
\tag{10}
\]

## 3. Actual normalization and constant coefficient consequences

Use the actual elementary changes, freshly read in
[quartic-first208](radical-quartic-first-projection-unit-speed-pass208-working.md):
first \(X'=X-c_2/4\), then in those coordinates
\(W'=W+(c_1/2)Y+(c_4/2)X\), then
\(Z'=Z-c_3Y-c_5X\). Relabel afterwards. They give \(k=0\).
Each inverse subtracts its indicated addition or reverses its
translation. Only lower-time-degree terms are added. Thus the full
initial kernel, exact degrees, literal \(\partial_Z\), \(N,L,t,\rho\),
and \(a\) are unchanged. The projected \(y,\vartheta\) shift by
elements of \(L\), so their degrees and whole plane are preserved.

The nonzero center slope \(B_0\) is unchanged as well. To check this
without assuming it, an \(X'=X+s\) translation gives
\[
k'=k+2s\rho^2,\qquad
n'=n-sk+3s^2\rho^2+2s\rho k_\rho+st k_t .
\tag{11}
\]
With \(k_{tt}=0\), its new \(n_t-k_{t\rho}k_\rho/2\) is \(B_0\).
For \(W'=W+\alpha Y+\beta X\), set \(c=\alpha t+\beta\);
then \(k'=k-2\rho c\) and \(n'=n-k_\rho c+c^2\), giving the same
invariance. The final \(Z\)-addition changes neither \(n_t\) nor
the relevant \(\rho\)-derivatives of \(k\). Thus after normalization
\(B_0=n_t\ne0\). The center remains linear and squarefree, so (9)
applies in this actual chart.

Write the new graph again as \(P(V)=A_2V^2+A_1V+A_0\).
The literal eliminant for \(k=0\) is
\[
\begin{aligned}
\mathcal H={}&(\ell-n_tU)^2
 +2n_{tt}U^2V^2+4n_{t\rho}UV^3+2n_{\rho\rho}V^4\\
 &-4\ell_tUV^2-4\ell_\rho V^3-(n_\rho^2+4m)V^2 .
\end{aligned}
\tag{12}
\]
Its \(U^2\) coefficient and (9) give \(n_{tt}=0\);
the \(UV^3\) coefficient gives \(n_{t\rho}=0\). Hence
\(n_t=\gamma\in\mathbb C^*\).
The constant and linear terms in \(V\) in its \(U\) coefficient give
\(A_0=\ell/\gamma\) and \(\eta=\gamma^2A_1\). In particular \(A_1\ne0\).
The full model (9) simplifies to
\[
\mathcal H=\gamma^2\{(U-A_0-A_2V^2)^2-A_1^2V^2\}.
\tag{13}
\]
Comparing \(UV^2,V^3,V^4\) respectively with (12) yields
\[
\ell_t=\frac{\gamma^2A_2}{2},\qquad
\ell_\rho=0,\qquad
n_{\rho\rho}=\frac{\gamma^2A_2^2}{2}.
\tag{14}
\]
The second equality differentiated in \(t\) makes \((A_2)_\rho=0\).
Since \(n_t=\gamma\), differentiating the last in \(t\) makes
\((A_2)_t=0\). Thus \(A_2\in\mathbb C^*\). Put
\(\lambda=\gamma A_2/2\in\mathbb C^*\) and \(x=-\gamma A_1/2\in L^*\).
Integration over the exact field uses joint constants, not rationality:
\[
\begin{gathered}
n=\gamma t+\lambda^2\rho^2+n_1\rho+n_2,\qquad
\ell=\gamma\lambda t+\ell_0,\qquad n_1,n_2,\ell_0\in\mathbb C,\\
w=x-\lambda\vartheta-\lambda^2\rho-n_1/2,\\
y=(\ell-2\vartheta x+2\lambda\vartheta^2)/\gamma,\qquad
z=2\rho w+\vartheta^2+n .
\end{gathered}
\tag{15}
\]
The expression for \(w\) is the undivided third potential, using
\(y=P(\vartheta)\) and \(A_0=\ell/\gamma\).
Here \(x\) is a coefficient-field element. It is not an affine
generic parameter, unlike the parameter with the same name in208.

## 4. An irreducible original polynomial cannot become a square

Make the actual affine change
\[
U_0=X-\lambda,\quad W_0=W+n_1/2,\quad Z_0=Z-n_2,\quad
V_0=\gamma Y-2\lambda Z-(\ell_0-2\lambda n_2).
\tag{16}
\]
Its polynomial inverse is
\(X=U_0+\lambda,\ W=W_0-n_1/2,\ Z=Z_0+n_2,\)
\(Y=(V_0+2\lambda Z_0+\ell_0)/\gamma\).
Thus \(B=\mathbb C[U_0,V_0,Z_0,W_0]\).

Only to expand the full chart, put
\(H_0=\vartheta+2\lambda\rho\),
\(j=H_0+\rho U_0\), and
\(T_0=\gamma t-4\lambda\rho H_0+4\lambda^2\rho^2\).
Substituting (15) into the original expansions in (1) gives
\[
\begin{aligned}
W_0&=x+U_0j,\\
Z_0&=T_0+2\rho x+j^2-2\lambda\rho^2U_0,\\
V_0&=-2xH_0+T_0U_0-2\lambda\rho^2U_0^2.
\end{aligned}
\tag{17}
\]
These are identities in the actual fraction field, not proposed
coordinates \(x,t,\rho\). Direct cancellation gives
\[
I:=W_0^2+U_0V_0-U_0^2Z_0=x^2 .
\tag{18}
\]

The polynomial \(I\) is irreducible in the original four-ring.
Over the UFD \(\mathbb C[U_0,Z_0,W_0]\) it is linear in \(V_0\),
with coprime coefficient \(U_0\) and constant term
\(W_0^2-U_0^2Z_0\). It is primitive and is irreducible over that
UFD's fraction field by degree one, so Gauss's lemma applies.
But \(x\in L\subset\operatorname{Frac}A\subset\operatorname{Frac}B\).
The valuation at the prime \(I\) assigns \(I\) value one and assigns
every square in \(\operatorname{Frac}B\) an even integer.
Equation (18) is impossible. Equivalently normality would first
put \(x\) in \(B\), also contradicting irreducibility.

This excludes the stated \((2,1)\) degree pair. The only coordinate
change used in the final obstruction has the explicit original-ring
inverse (16). No division by the speed, no rationality of \(L\), and
no lifting of a coefficient-field coordinate change were assumed.

The full eliminant206 and actual normalization208 were reread before
this proof. No saved checker was executed, imported or compiled, and
no earlier source or index was changed. This is working mathematics,
not expert review, proof-assistant certification, historical novelty
clearance, or a result about unrestricted cancellation.
