# Zero return is impossible for the product-radical initial kernel

Status: bounded working exclusion for a supplied actual frame. For the
full initial kernel \((\mathsf Z^2-\mathsf X\mathsf Y\mathsf W)\),
the return polynomial in the literal \(\partial_Z\) chart is not
identically zero. The proof uses the fourth potential, the calibrated
Jacobian, and an actual nice auxiliary derivation. It makes no claim
about the remaining nonzero-return branches or arbitrary entry.

## 1. Actual hypotheses and the exact coefficient field

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
\longmapsto(aT,bT,eT^2,hT^2)\bigr)
=(\mathsf Z^2-\mathsf X\mathsf Y\mathsf W),
\end{gathered}
\tag{1}
\]
where \(T\) is independent and the named capital letters are actual
polynomial coordinates. The entire initial kernel is a hypothesis;
the scalar identity \(e^2=abh\) alone does not suffice.

The literal selected partial \(\partial_Z\) and
[universal184](weight-four-universal-chart-potentials-pass184-working.md),
Sections 1--4, give
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A)\in\operatorname{LND}(A),
\qquad N(a)=N(b)=N(e)=N(h)=0,\\
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2,\qquad q^2=t\rho,
\qquad [L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad
L[y,z,w]=L[v],\qquad J_0=-a^3\in L^*.
\end{gathered}
\tag{2}
\]
Here \(t,\rho\) are algebraically independent. Their partials extend
uniquely to the finite separable field \(L\), commute, and fix \(v\).
In particular \(q\) is an element of this exact field, not a newly
adjoined formal square root. Neither rationality of \(L\) nor
regularity of its individual elements in \(B\) is assumed.

The determinant \(J_0\) has rows \(y,z,w\) and columns
\(t,\rho,v\). The full fixed-\(X\) determinant also equals \(J_0\).
Moreover \(X=x_0+au\), with \(x_0\in A\) and \(a\ne0\), so
\(X\) is transcendental over \(\operatorname{Frac}A\), and hence
over \(L\).

## 2. The full potentials and the zero-return line

For formal independent variables \(U,V\), use
\[
H_j(c;U,V)=\sum_{i=0}^j
\frac{c_{t^i\rho^{j-i}}}{i!(j-i)!}U^iV^{j-i}.
\tag{3}
\]
Differentiating \(q^2=t\rho\) gives
\[
\begin{gathered}
q_t=\frac q{2t},\quad q_\rho=\frac q{2\rho},\quad
q_{t\rho}=\frac q{4t\rho},\quad
q_{\rho\rho}=-\frac q{4\rho^2},\\
H_2(q;U,V)=-\frac q8\left(\frac Ut-\frac V\rho\right)^2,\\
f=H_2(q)+H_1(k)+n,\quad
g_3=H_3(q)+H_2(k)+H_1(n),\quad
g_4=H_4(q)+H_3(k)+H_2(n),
\end{gathered}
\tag{4}
\]
for \(k,n\in L\). The universal integrated identities, with
\(\ell,m\in L\), are
\[
\begin{gathered}
\sigma=q_t y+q_\rho\vartheta+k,\qquad
z=q_\rho w+f(y,\vartheta),\\
R=f_V(y,\vartheta)
=\frac q{4t\rho^2}(\rho y-t\vartheta)+k_\rho,\\
Rw+g_3(y,\vartheta)=\ell,\\
-\frac q{8\rho^2}w^2+f_\rho(y,\vartheta)w
+g_4(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m.
\end{gathered}
\tag{5}
\]
Coefficient partials such as \(f_\rho\) are taken with \(U,V\)
fixed, before evaluating. The quadratic term in \(w\) in (5) is
retained throughout.

Suppose for contradiction that \(R=0\) in \(L[v]\). Put
\[
p=\rho/t,\qquad c=\frac{4\rho^2 k_\rho}{q},\qquad
\vartheta=py+c,\qquad
\mathcal D=\partial_t+p\partial_\rho,\qquad K=\mathcal Dk.
\tag{6}
\]
The sign and factor in \(c\) follow by solving the displayed
return equation in (5). Notice \(\mathcal Dp=0\).

If \(y\in L\), then \(\vartheta\in L\). The fourth potential
is then a polynomial equation in \(w\) over \(L\) with nonzero
quadratic coefficient \(-q/(8\rho^2)\). If \(w\) had positive
\(v\)-degree, its squared term would have strictly greater degree
than every other term, which is impossible. Thus \(w\in L\), and
the second potential gives \(z\in L\). This contradicts the
whole-line equality in (2). We have proved
\[
y\notin L,\qquad y_v\ne0,\qquad \vartheta_v=py_v.
\tag{7}
\]

For explicit radial checks, the higher leading potentials on this
line are
\[
\begin{aligned}
H_2(q;y,py+c)&=-\frac{qc^2}{8\rho^2},\\
H_3(q;y,py+c)&=\frac{qc^2y}{8t\rho^2}
                         +\frac{qc^3}{16\rho^3},\\
H_4(q;y,py+c)&=-\frac{qc^2y^2}{8t^2\rho^2}
-\frac{qc^3y}{8t\rho^3}-\frac{5qc^4}{128\rho^4}.
\end{aligned}
\tag{8}
\]
In particular the third potential, as a polynomial in the
nonconstant \(y\), has coefficients
\[
\begin{gathered}
\mathcal D^2k=0,\qquad
c\mathcal D(k_\rho)+\mathcal Dn+
                  \frac{qc^2}{8t\rho^2}=0,\\
\ell=\frac{c^2}2k_{\rho\rho}+c n_\rho
                         +\frac{qc^3}{16\rho^3}.
\end{gathered}
\tag{9}
\]
These are necessary exact-field identities, not an integration that
declares their coefficients complex. The exclusion below does not
require solving them.

## 3. The actual scalar determinant forces affine intercepts

Define the literal universal coefficients
\[
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w.
\tag{10}
\]
Differentiating the third potential in \(v\) gives
\(Rw_v+B_1y_v+C_1\vartheta_v=0\). Under (6)--(7), this implies
\(B_1=-pC_1\). The reduced universal determinant therefore reads
\[
\begin{aligned}
-a^3=J_0
&=\left[dy\wedge(B_1dt+C_1d\rho)\wedge dw
                                      \right]_{dt\wedge d\rho\wedge dv}\\
&=C_1\bigl((\mathcal Dy)w_v-y_v\mathcal Dw\bigr).
\end{aligned}
\tag{11}
\]
The sign follows by using the middle row \((-pC_1,C_1,0)\).
Both factors belong to \(L[v]\), and their product is a nonzero
scalar. Hence \(C_1\in L^*\). This conclusion is a unit statement
in \(L[v]\), not in the original ring.

Taking the coefficient derivative before evaluation gives exactly
\[
\begin{aligned}
C_1&=-\frac q{4\rho^2}w+K_\rho y+\Omega,\\
\Omega&=c k_{\rho\rho}+n_\rho+
                              \frac{3qc^2}{16\rho^3},\\
w&=\lambda y+\omega,\qquad
\lambda=\frac{4\rho^2}qK_\rho,\qquad
\omega=\frac{4\rho^2}q(\Omega-C_1).
\end{aligned}
\tag{12}
\]
For example, the coefficient of \(y\) before collecting is
\(\mathcal D(k_\rho)+qc/(4t\rho^2)\).
Since \(qc/(4t\rho^2)=k_\rho/t\), this is precisely
\(K_\rho\). This calculation differentiates neither the substituted
line nor its coefficient \(c\) inside the formal partial.

The first two potentials now become
\[
\begin{gathered}
f(y,\vartheta)=Ky+n+\frac{2\rho^2k_\rho^2}{q},\\
z=\kappa y+\zeta,\qquad
\kappa=K+\frac q{2\rho}\lambda=K+2\rho K_\rho,\qquad
\zeta=\frac q{2\rho}\omega+n+\frac{2\rho^2k_\rho^2}{q},\\
\sigma=\frac qt y+2\rho k_\rho+k.
\end{gathered}
\tag{13}
\]
All new coefficients belong to \(L\). Consequently
\(L[y,z,w]=L[y]\), and (2) gives \(L[y]=L[v]\). The degree of
a polynomial composition shows that \(\deg_vy=1\). Thus
\[
Ny\in L^*,\qquad
\deg_v(y,z,w,\vartheta,\sigma)\le1.
\tag{14}
\]
No assumption that \(\lambda\) or \(\kappa\) is nonzero is needed.

## 4. An actual nice derivation and its impossible linear row

Extend \(N\) to \(B=A[u]\) by \(Nu=0\), and put
\[
\mathcal P=aN-(NX)E,
\qquad \mathcal PX=0,\qquad \mathcal P|_A=aN,
\qquad [E,\mathcal P]=0.
\tag{15}
\]
This is an actual derivation of \(B\), since \(NX=Nx_0\in A\).
To prove local nilpotence, use the actual equality \(B_a=A_a[X]\).
On this localization \(\mathcal P\) fixes \(X\) and acts as
\(aN\) on \(A_a\). Because \(Na=0\), that restriction is locally
nilpotent. Hence \(\mathcal P\) is locally nilpotent on the stable
subring \(B\). This proof does not assume \(NX=0\).
Commutation in (15) follows from \([E,N]=0\) and \(E(NX)=Na=0\).

Set \(\tau=aNy\in L^*\) and \(s=q/t\), so \(s^2=\rho/t=p\).
The actual coordinate derivatives are
\[
\mathcal PX=0,\quad
\mathcal PY=\tau,\quad
\mathcal PZ=\tau(sX+\kappa),\quad
\mathcal PW=\tau(s^2X+\lambda).
\tag{16}
\]
The products in (16) are original polynomials because \(\mathcal P\)
was constructed in \(\operatorname{Der}_{\mathbb C}(B)\).
Individual field factors are not declared regular. Since \(\mathcal P\)
kills \(L\) and \(X\), it is nonzero and its square kills all four
original coordinates.

Localize at \(\mathbb C[X]\setminus\{0\}\), and write
\(K_X=\mathbb C(X)\). This gives a nonzero nice derivation of
\(K_X[Y,Z,W]\). If desired, divide its three coefficients by their
greatest common divisor \(g\) in this polynomial UFD, obtaining an
irreducible derivation \(D\). Indeed \(g\mid\mathcal P(g)\), and
local nilpotence forces \(\mathcal P(g)=0\) by the derivation-degree
rule. Hence \(Dg=0\), \(\mathcal P^j=g^jD^j\), and \(D\) is
locally nilpotent with \(D^2Y=D^2Z=D^2W=0\). The two kernels agree.

Theorem3.1(i) of
[Dasgupta--Gupta, *Nice derivations over principal ideal domains*](https://arxiv.org/html/1701.03635v1)
says that a nonzero nice derivation of a three-variable polynomial
ring over a characteristic-zero field fixes a nonzero linear form
in those variables. Part(i) itself does not require irreducibility;
the primitive division above also verifies the stronger optional
hypothesis. No coordinate from this field theorem is lifted to \(B\).

Clear the \(X\)-denominators of the fixed linear form. There are
\(l,m,n\in\mathbb C[X]\), not all zero, for which (16), divided
by \(\tau\) in the fraction field, gives
\[
l(X)+m(X)(sX+\kappa)+n(X)(s^2X+\lambda)=0
\quad\hbox{in }L[X].
\tag{17}
\]
Let \(d=\max(\deg l,\deg m+1,\deg n+1)\), with zero polynomials
assigned degree \(-\infty\). Then \(d\ge0\), the terms
\(m\kappa+n\lambda\) have degree at most \(d-1\), and the
coefficient of \(X^d\) is
\[
l_d+m_{d-1}s+n_{d-1}s^2=0.
\tag{18}
\]
Missing or negative-index coefficients are zero. At least one of
the three coefficients is nonzero, and all belong to \(\mathbb C\).
But \(s\) is transcendental over \(\mathbb C\): otherwise
\(s^2=\rho/t\) would be algebraic over \(\mathbb C\), contrary
to the algebraic independence of \(t,\rho\). This contradiction
proves that \(R\) cannot vanish identically.

## 5. Verification and scope

The universal184 source was freshly read through EOF. The structurally
related [mixed zero-return217](rank-two-mixed-ratio-zero-return-exclusion-pass217-working.md)
was also freshly read, but its specialized coefficient formulas were
not transplanted. The square-root derivatives, all three radial
identities (8), the third-potential coefficients, the literal \(C_1\),
the first two potentials, and the sign in (11) were independently
reconstructed. A fresh unsaved symbolic calculation returned zero
for each of those exact residuals.

The precise nice-field theorem and its separate irreducibility clause
were freshly read in the primary Dasgupta--Gupta text. This is reliance
on that restatement of Wang, not a claim to have read Wang's original
article. No saved checker was executed, imported, or compiled.

The conclusion excludes only the identically-zero return branch for
the actual full kernel in (1). It does not assert that a nonzero return
polynomial has no roots, prove recognition of the other branches, or
prove that arbitrary sliced actions admit this frame. It uses no
coefficient-field-to-ambient coordinate inference, no original unit
assumption on \(a\), and no change of selected pivot. Earlier sources,
indices, and packets are unchanged. This is a working proof, not human
expert review, proof-assistant certification, or historical novelty
clearance.
