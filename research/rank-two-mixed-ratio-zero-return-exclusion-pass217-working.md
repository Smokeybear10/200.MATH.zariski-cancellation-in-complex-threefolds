# The zero-return branch for the mixed leading ratio

**Status: new working exclusion, pending independent saved-source review.**

For an actual exact1122 frame whose full initial kernel is
\((\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2)\), the return coefficient
\(R\) in the universal184 chart cannot vanish identically. The proof
uses the scalar Jacobian to make all projected entries affine in one
line parameter. An actual nice derivation then contradicts the
fixed-linear-form theorem over \(\mathbb C(X)\).

This is not an application of the \(q_t=0\) theorem205. It proves
neither that a nonzero \(R\) has no zeros nor recognition of the
remaining branches. No coefficient-field element is declared an
original polynomial coordinate or an original-ring unit.

## 1. Actual hypotheses and the specialized potentials

Assume
\[
\begin{gathered}
B=\mathbb C[X,Y,Z,W]=A[u],\qquad E=\partial_u,\qquad A=\ker E,\\
(\deg_E X,\deg_E Y,\deg_E Z,\deg_E W)=(1,1,2,2),\\
a=EX,\quad b=EY,\quad e=E^2Z/2,\quad h=E^2W/2,\\
\ker\bigl((\mathsf X,\mathsf Y,\mathsf Z,\mathsf W)
 \mapsto(a\tau,b\tau,e\tau^2,h\tau^2)\bigr)
 =(\mathsf Z\mathsf W-\mathsf X^2\mathsf Y^2).
\end{gathered}
\tag{1}
\]
The full kernel, rather than just one relation among the leaders,
is part of the hypothesis. The actual selected partial and exact
projection from [universal184](weight-four-universal-chart-potentials-pass184-working.md),
Sections 1--4, give
\[
\begin{gathered}
0\ne N=[u^3](\partial_Z|_A)\in\operatorname{LND}(A),\qquad
Na=Nb=Ne=Nh=0,\\
L=\operatorname{Frac}(\ker_A N),\qquad A_L=L[v],\qquad Nv=1,\\
t=b/a,\quad \rho=h/a^2,\quad q=e/a^2=t^2/\rho,\qquad
[L:\mathbb C(t,\rho)]<\infty,\\
Y=y+tX,\quad Z=z+\sigma X+qX^2,\quad
W=w+\vartheta X+\rho X^2,\\
y,z,w,\sigma,\vartheta\in L[v],\qquad L[y,z,w]=L[v],\qquad
J_0=-a^3\in L^*.
\end{gathered}
\tag{2}
\]
Here \(t,\rho\) are algebraically independent. Their two partials
extend uniquely to the finite separable field \(L\), commute there,
and fix \(v\). The determinant \(J_0\) has rows \(y,z,w\) and
columns \(t,\rho,v\). Also \(X=x_0+au\), with \(x_0\in A\),
so \(X\) is transcendental over \(\operatorname{Frac}A\), hence
over \(L\).

Put \(p=t/\rho\). In particular \(p\ne0\), and \(p\) is
transcendental over \(\mathbb C\). Define
\[
\begin{gathered}
q_t=2p,\qquad q_\rho=-p^2,\qquad
q_{t\rho}=-2p/\rho,\qquad q_{\rho\rho}=2p^2/\rho,\\
f(U,V)=\frac{(U-pV)^2}{\rho}+k_tU+k_\rho V+n,\\
\sigma=2py-p^2\vartheta+k,\qquad
z=-p^2w+f(y,\vartheta),\qquad k,n\in L,\\
R=f_V(y,\vartheta)
 =k_\rho-\frac{2t}{\rho^2}(y-p\vartheta).
\end{gathered}
\tag{3}
\]
The partials \(f_t,f_\rho\) below differentiate coefficients with
the independent formal variables \(U,V\) fixed, before evaluation.
In the notation of universal184, put
\[
\begin{gathered}
B_1=f_t(y,\vartheta)+q_{t\rho}w,\qquad
C_1=f_\rho(y,\vartheta)+q_{\rho\rho}w,\\
g_3=H_3(q)+H_2(k)+H_1(n),\qquad
g_4=H_4(q)+H_3(k)+H_2(n),\\
Rw+g_3(y,\vartheta)=\ell,\\
\frac{q_{\rho\rho}}2w^2+f_\rho(y,\vartheta)w
 +g_4(y,\vartheta)-\ell_t y-\ell_\rho\vartheta=m,
\qquad \ell,m\in L.
\end{gathered}
\tag{4}
\]
Here \(H_j(c;U,V)=\sum_{i=0}^j
c_{t^i\rho^{j-i}}U^iV^{j-i}/(i!(j-i)!)\).
The final equation in (4) is the fourth potential, including its
nonzero quadratic term in \(w\).

## 2. The zero-return assumption and the scalar factor

Suppose, for contradiction, that \(R=0\) in \(L[v]\). Then
\[
\xi:=y-p\vartheta=\frac{\rho^2k_\rho}{2t}\in L,
\qquad y=p\vartheta+\xi.
\tag{5}
\]
If \(\vartheta\in L\), then \(y\in L\). All coefficients of
the fourth potential in (4), viewed as a polynomial in \(w\),
would be in \(L\); its quadratic coefficient is
\(q_{\rho\rho}/2=t^2/\rho^3\ne0\). A positive-degree polynomial
\(w\in L[v]\) cannot satisfy that equation, by its highest
\(v\)-degree term. Thus \(w\in L\), and (3) then gives
\(z\in L\), contrary to \(L[y,z,w]=L[v]\). Consequently
\(\vartheta_v\ne0\), and \(y_v=p\vartheta_v\).

Differentiate the third potential in (4) with respect to \(v\).
The exact universal derivative identity is
\[
Rw_v+B_1y_v+C_1\vartheta_v=0.
\qquad\text{Hence, under (5),}\qquad C_1=-pB_1.
\tag{6}
\]
There is no division by a projected coordinate derivative before
its nonvanishing has been established.

The remaining universal determinant, with its calibrated sign, is
\[
\begin{aligned}
-a^3=J_0
 &=\left[dy\wedge(R\,d\vartheta+B_1dt+C_1d\rho)
                   \wedge dw\right]_{dt\wedge d\rho\wedge dv}\\
 &=B_1\left\{y_v(w_\rho+p w_t)
                    -(y_\rho+p y_t)w_v\right\}.
\end{aligned}
\tag{7}
\]
For example, the second factor is the determinant with middle row
\((1,-p,0)\); this fixes the sign in (7). Both factors are in
the polynomial ring \(L[v]\), while their product is in \(L^*\).
Therefore \(B_1\in L^*\). This is a unit conclusion only in the
coefficient-field line ring, not in \(B\).

The literal coefficient derivative of (3) gives
\[
\begin{aligned}
B_1={}&\left(pk_{tt}+k_{t\rho}-\frac{2\xi}{\rho^2}\right)
             \vartheta+k_{tt}\xi+n_t-\frac{2p}{\rho}w,\\
w={}&\lambda\vartheta+\omega,\\
\lambda={}&\frac{\rho}{2p}
       \left(pk_{tt}+k_{t\rho}-\frac{2\xi}{\rho^2}\right),
\qquad
\omega=\frac{\rho}{2p}(k_{tt}\xi+n_t-B_1).
\end{aligned}
\tag{8}
\]
Thus \(\lambda,\omega\in L\), with no nonzero-slope assumption.
The first two potentials now give
\[
\begin{gathered}
z=\kappa\vartheta+\zeta,\qquad
\kappa=pk_t+k_\rho-p^2\lambda,\\
\zeta=\xi^2/\rho+k_t\xi+n-p^2\omega,\qquad
\sigma=p^2\vartheta+2p\xi+k,\\
L[y,z,w]=L[\vartheta]=L[v].
\end{gathered}
\tag{9}
\]
In the last equality, \(p\ne0\) allows recovery of \(\vartheta\)
from \(y\). Polynomial degree under composition shows that
\(L[\vartheta]=L[v]\) forces \(\deg_v\vartheta=1\). In
particular \(N\vartheta\in L^*\), and \(N^2\) kills all the
intercepts in (9), as well as \(y,w\).

## 3. An actual nice derivation

Extend \(N\) to the actual ring \(B=A[u]\) by \(Nu=0\), and set
\[
\mathcal P=aN-(NX)E.
\qquad \mathcal P X=0,\qquad
\mathcal P|_A=aN,\qquad [E,\mathcal P]=0.
\tag{10}
\]
This is an actual polynomial derivation: \(a,NX\in A\subset B\),
and \(Na=0\). Its local nilpotence is not inferred from a sum of
locally nilpotent derivations. Instead, on
\(B_a=A_a[X]\) it fixes \(X\) and acts as the locally nilpotent
derivation \(aN\) on \(A_a\). It is therefore locally nilpotent
on \(B_a\), hence on the stable subring \(B\). The commutator
in (10) follows from \([E,N]=0\) and \(E(NX)=N(EX)=0\).

Put \(\tau=aN\vartheta\in L^*\). This symbol is unrelated to the
initial grading parameter in (1). The formulas above give the
literal original-coordinate row
\[
\mathcal P X=0,\qquad
\mathcal P Y=\tau p,\qquad
\mathcal P Z=\tau(p^2X+\kappa),\qquad
\mathcal P W=\tau(X+\lambda).
\tag{11}
\]
The displayed products are actual polynomials because
\(\mathcal P\) is already an actual derivation. It is neither
necessary nor asserted that the individual field factors are
regular in \(B\).

All elements of \(L\) and \(X\) are killed by \(\mathcal P\).
It follows that
\[
\mathcal P^2X=\mathcal P^2Y=\mathcal P^2Z=\mathcal P^2W=0,
\qquad \mathcal P\ne0,\qquad E(\mathcal P W)=a\tau\ne0.
\tag{12}
\]
Thus \(\mathcal P\) is nice, but its coefficient row is not
\(E\)-invariant. In particular the extra hypothesis in
[criterion205](nice-commuting-invariant-coefficients-recognition-pass205-working.md)
has not been obtained and is not used.

## 4. The fixed-linear-form contradiction

Since \(\mathcal P X=0\), localize at
\(\mathbb C[X]\setminus\{0\}\). The result is a nonzero nice
\(\mathbb C(X)\)-locally nilpotent derivation of
\(\mathbb C(X)[Y,Z,W]\). Theorem 3.1(i) of
[Dasgupta--Gupta, *Nice derivations over principal ideal domains*](https://arxiv.org/html/1701.03635v1)
states that such a derivation fixes a nonzero linear form in the
three polynomial generators. This part of the theorem does not
require irreducibility. We use that field statement, not the
stronger PID conclusion or an asserted actual slice.

Clearing denominators of the resulting linear form supplies
\(l,m,n\in\mathbb C[X]\), not all zero. Dividing its derivative
by \(\tau\) in the fraction field gives the identity in \(L[X]\)
\[
l(X)p+m(X)(p^2X+\kappa)+n(X)(X+\lambda)=0.
\tag{13}
\]
Let \(d=\max(\deg l,\deg m+1,\deg n+1)\), where the degree of
the zero polynomial is \(-\infty\). Then \(d\ge0\). The terms
\(m\kappa+n\lambda\) have degree at most \(d-1\), because
\(\kappa,\lambda\in L\) are independent of \(X\). The
coefficient of \(X^d\) in (13) is consequently
\[
l_d p+m_{d-1}p^2+n_{d-1}=0.
\tag{14}
\]
An absent or negative-index coefficient is zero. At least one
displayed coefficient is nonzero by the definition of \(d\), and
all three belong to \(\mathbb C\). This contradicts the
transcendence of \(p=t/\rho\) over \(\mathbb C\).

Hence \(R\ne0\) in every actual supplied frame (1).

## 5. Scope and source checks

The proof has not changed \(\xi=y-(t/\rho)\vartheta\) into an
ambient coordinate. It uses no regularity of \(t,\rho,\lambda\),
\(\kappa\), or \(\tau\) individually in the original ring. It
does not transfer a selected partial or a return coefficient
between different pivots. It does not rule out zeros of a
nonidentically-zero \(R\), settle the nonzero-return branch,
or establish an entry theorem for arbitrary sliced actions.

The universal184 source and criterion205 were fully reread before
this derivation. Universal184 received a further complete saved
read while the signs in (6)--(8) were checked. The precise
published field theorem used above was freshly checked in the
primary arXiv HTML, Theorem 3.1(i), including its hypotheses and
the separate irreducibility condition in part (iii). This is a
read of the Dasgupta--Gupta restatement of Wang's theorem, not a
claim to have inspected the original Wang article.

No saved checker was executed, imported, or compiled in authoring
this note. Finite algebra controls, if later supplied separately,
will not certify the actual projection theorem or the published
nice-derivation theorem. This is neither human expert review nor
proof-assistant certification, historical novelty clearance, or
an unrestricted cancellation solution. All216 and earlier held
or frozen artifacts remain unchanged.
