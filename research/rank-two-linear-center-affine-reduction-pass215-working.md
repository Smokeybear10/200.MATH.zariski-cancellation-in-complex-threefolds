# An affine reduction of the remaining linear rank-two center

Status: bounded working reduction, not recognition. In the remaining
linear-center degree pair \((\deg_vy,\deg_v\vartheta)=(2,1)\),
the evaluated cofactor has exactly one return factor. Its scalar
determinant and high coefficients permit actual complex-coefficient
shears after which both \(z,w\) are affine in \(\vartheta\), while
\(y\) remains quadratic. The auxiliary original-ring derivation
then has coordinate degrees \((0,2,1,1)\). No invariant ambient
coordinate is obtained in this note.

## 1. Exact retained hypotheses

Retain the actual supplied frame and full initial kernel of
[sextic reduction212](rank-two-t-independent-sextic-reduction-pass212-working.md),
and the fixed-parameter conventions of
[affine-second reduction214](rank-two-affine-second-high-degree-exclusion-pass214-working.md):
\[
\begin{gathered}
\mathcal B=\mathbb C[X,Y,Z,W]=A[u],\quad E=\partial_u,\quad
\deg_E(X,Y,Z,W)=(1,1,2,2),\\
\ker\theta_0=(\mathsf Z\mathsf W-\mathsf X^4),\quad
N=[u^3](\partial_Z|_A)\ne0,\quad a=EX\ne0,\\
L=\operatorname{Frac}\ker_A N,\quad A_L=L[v],\quad Nv=1,\quad
[L:\mathbb C(t,\rho)]<\infty,\quad q=1/\rho,\\
Y=y+tX,\quad W=w+\vartheta X+\rho X^2,\quad
Z=z+\sigma X+\rho^{-1}X^2 .
\end{gathered}
\tag{1}
\]
In particular \(t,\rho\) are algebraically independent and their
commuting coefficient partials extend uniquely to \(L\).
Their joint constant field is \(\mathbb C\); this follows by
differentiating minimal polynomials over \(\mathbb C(t,\rho)\).
Neither one-partial constant field is assumed rational.

Assume the center is linear and the projected degrees are \((2,1)\).
Using the independent parameter \(V=\vartheta\), write
\[
\begin{gathered}
y=P(V)=p_2V^2+p_1V+p_0,\quad p_2\in L^*,\qquad
w=W_0(V)\in L[V],\\
R=2\rho^{-3}V+j,\quad j=k_\rho,\quad K=k_{t\rho},\quad
V_c=-\rho^3j/2,\\
p(U)=S(U,V_c)-\ell=b(U-U_0),\quad b\in L^*,\quad
k_{tt}=0,\\
b=n_t-\rho^3jK/2,\qquad \delta=2n_{tt}-\rho^3K^2 .
\end{gathered}
\tag{2}
\]
Here \(P,W_0\) describe projected polynomials, not original
coordinate changes. Coefficient t- and rho-partials of these
polynomials keep \(V\) fixed. Their ordinary V-derivative is
denoted by a prime.

The two exact potentials of212 are
\(RW_0+S(P,V)-\ell=0\) and
\(\rho^{-3}W_0^2+c(P,V)W_0+Q(P,V)=0\), with
\(c,Q,S\) as defined there. The third-potential numerator has
degree at most three in \(V\), since \(k_{tt}=0\) and \(\deg P=2\).
Division by the nonconstant linear \(R\) therefore gives
\(\deg W_0\le2\).

## 2. The cofactor has precisely one return factor

Let \(G=U-P(V)\) and \(\mathcal H=GQ_1\) be the exact selected
factorization212. Put \(q_1=Q_1(P,V)\ne0\).
Since \(\vartheta=a_1v+a_0\), with \(a_1\in L^*\), the
calibrated determinant in \((t,\rho,V)\) is
\(J=J_0/a_1\in L^*\). The fully retained identities in214 give
\[
R^2J=-\mathcal T q_1,\qquad
\mathcal T=P_\rho+P'P_t+P'W_0',\qquad
q_1\mid R^2 .
\tag{3}
\]
Both full potentials are used in the gradient identity leading
to (3), not just their eliminated relation.

For the following local argument, use the evaluated gradients
\(B_1=S_U(P,V)\),
\(C_1=2\rho^{-3}W_0+c(P,V)\), and
\(\Lambda_i=\ell_i-S_i(P,V)-R_iW_0\), where formal
coefficients are differentiated before evaluation. In the present
fixed-V coordinates the exact identities read
\[
\begin{gathered}
RW_0'+B_1P'+C_1=0,\qquad
-\Lambda_tP'-\Lambda_\rho+C_1W_0'=0,\\
RW_{0,\rho}=-B_1P_\rho+\Lambda_\rho,\qquad
q_1=-R(C_1B_1+R\Lambda_t),\\
J=[dP\wedge(R\,dV+B_1dt+C_1d\rho)\wedge dW_0]
                 _{dt\wedge d\rho\wedge dV} .
\end{gathered}
\tag{4}
\]
The second identity is the total V-derivative of the fourth
potential. The third is the coefficient rho-derivative of the
third potential, keeping \(V\) fixed.

At \(V=V_c\), the third potential gives \(P(V_c)=U_0\), and
\(B_1(V_c)=b\ne0\). Suppose \(C_1(V_c)=0\).
The first identity in (4) forces \(P'(V_c)=0\), the second
forces \(\Lambda_\rho(V_c)=0\), and the third then forces
\(P_\rho(V_c)=0\). Consequently, at this point the first
one-form in the final line of (4) is a multiple of \(dt\),
and the middle one-form is \(b\,dt\). Their wedge vanishes,
contradicting \(J\in L^*\).

Thus \(C_1(V_c)\ne0\). The fourth identity in (4) makes
\(q_1\) vanish to exactly first order at the simple root of \(R\).
Together with (3), this proves
\[
q_1=\eta R,\qquad \eta\in L^*,\qquad
\mathcal T=-\frac J\eta R .
\tag{5}
\]
No differentiation along the moving center \(V_c(t,\rho)\)
was substituted for a fixed-V derivative in this argument.

## 3. High coefficient identities

Use the complete coefficients proved in214:
\[
\begin{gathered}
\mathcal H=A(V)U^2+D(V)U+C(V),\qquad
A=\rho^{-3}b^2+\tfrac14\delta R^2,\\
\deg D\le4,\quad \deg C=6,\quad C_6=-\rho^{-11},\\
D_4=2\rho^{-7}(3K+\rho K_\rho),\qquad
D_3=4\rho^{-7}(b+\rho b_\rho)+2\rho^3jD_4 .
\end{gathered}
\tag{6}
\]
Subscripts on \(C,D\) indicate V-coefficients.
The selected graph and (5) give
\[
2AP+D=\eta R,\qquad C=AP^2-\eta RP .
\tag{7}
\]
If \(\delta=0\), then \(A\) is constant and the latter
polynomial has degree at most four, contrary to \(C_6\ne0\).
Hence \(\delta\ne0\). The V-sixth coefficient in the second
identity and the V-fourth coefficient in the first give
\[
\begin{gathered}
\delta p_2^2=-\rho^{-5},\qquad
T_*=3K+\rho K_\rho=-\delta\rho p_2=\rho^{-4}/p_2,\\
\delta=-\rho^3T_*^2,\qquad p_2=\rho^{-4}/T_*,\qquad T_*\ne0 .
\end{gathered}
\tag{8}
\]
As \(k_{tt}=0\), we have \(K_t=(T_*)_t=0\). Therefore
\(\delta_t=(p_2)_t=0\). Direct differentiation of (2) also gives
\(b_t=\delta/2\).

The coefficient of V-cubed in the first identity of (7), using
(6), is equivalent to
\[
p_1=\rho^3j p_2-\frac{2(b+\rho b_\rho)}{\delta\rho} .
\tag{9}
\]
Differentiating in t, using \(j_t=K\), \(b_t=\delta/2\),
and \(\delta=-\rho^3T_*^2\), gives
\[
(p_1)_t=\frac{K}{\rho T_*}-\frac4\rho
                     -2\frac{(T_*)_\rho}{T_*} .
\tag{10}
\]
All derivatives here are in the original coefficient field;
no rational-function ansatz has been imposed.

## 4. The scalar determinant supplies the remaining Euler equation

Write \(W_0=w_2V^2+w_1V+w_0\). The V-cubed coefficient in
the third potential gives
\[
w_2=\frac1{2\rho}-\frac{\rho^3Kp_2}{2}
    =\frac{T_*-K}{2\rho T_*} .
\tag{11}
\]
By (5), \(\mathcal T\) has degree one. Its V-squared
coefficient, using \((p_2)_t=0\), is therefore zero:
\[
(p_2)_\rho+2p_2(p_1)_t+4p_2w_2=0,
\qquad
(p_1)_t=\frac1\rho+\frac{K}{\rho T_*}
                         +\frac{(T_*)_\rho}{2T_*} .
\tag{12}
\]
Comparing (10) and (12) forces
\[
\frac{(T_*)_\rho}{T_*}=-\frac2\rho,
\qquad T_*=c\rho^{-2},\qquad c\in\mathbb C^* .
\tag{13}
\]
Indeed \(\rho^2T_*\) has both coefficient partials zero.
The equation \(3K+\rho K_\rho=c\rho^{-2}\), with \(K_t=0\),
then integrates exactly in \(L\) to
\[
K=c\rho^{-2}+d\rho^{-3},\qquad
k_t=c_0-c\rho^{-1}-\frac d{2\rho^2},
\qquad d,c_0\in\mathbb C .
\tag{14}
\]
For the first identity, differentiate \(\rho^3K-c\rho\);
for the second, differentiate
\(k_t+c/\rho+d/(2\rho^2)\). Both also have t-partial zero,
so their constants really are complex.

## 5. Actual shears, affine projected entries, and the auxiliary action

Apply the actual coordinate changes
\[
X'=X,\quad Y'=Y,\quad W'=W+\tfrac d2Y,\quad Z'=Z-c_0Y .
\tag{15}
\]
Their inverse is \(W=W'-dY'/2,Z=Z'+c_0Y'\), with
\(X=X',Y=Y'\). Substituting either order gives all four original
coordinates. The coefficients are complex, and the correction
terms have E-degree one. Thus the exact profile, all leading
coefficients, and the full initial kernel remain unchanged.
Moreover \(\partial_{Z'}=\partial_Z\), so the selected \(N\),
the field \(L\), \(t,\rho,a\), and their coefficient partials
are unchanged.

For completeness, an intermediate change \(W'=W+\alpha Y\)
has the exact potential transformations
\[
\vartheta'=\vartheta+\alpha t,\quad w'=w+\alpha y,\quad
k'=k+\alpha t\rho^{-2},\quad
n'=n-\alpha t k_\rho+\alpha^2t^2\rho^{-3} .
\tag{16}
\]
They follow by substitution into
\(\sigma=-\rho^{-2}\vartheta+k\) and
\(z=-\rho^{-2}w+\rho^{-3}\vartheta^2+k_ty+k_\rho\vartheta+n\).
Their center slope is exactly unchanged:
\(n'_t-\rho^3k'_\rho k'_{t\rho}/2=b\), as verified by
expanding (16). The subsequent Z-shear subtracts \(c_0t\)
from \(k'\) and leaves \(n'\) unchanged.
Also \(R'=R\) after evaluation and \(T_*'=T_*\): the
correction to \(K\) is a constant multiple of \(\rho^{-3}\),
killed by \(3+\rho\partial_\rho\).

Rebuild the actual chart and relabel the new coordinates. Equations
(8), (13)--(16) now give
\[
\begin{gathered}
k_t=-c/\rho,\quad K=T_*=c/\rho^2,\quad
\delta=-c^2/\rho,\quad n_{tt}=0,\\
p_2=\frac1{c\rho^2},\quad w_2=0,\quad
y=\frac{\vartheta^2}{c\rho^2}+p_1\vartheta+p_0,\qquad
w=\lambda\vartheta+\omega .
\end{gathered}
\tag{17}
\]
The coefficient of \(\vartheta^2\) in the second potential for
\(z\) is \(\rho^{-3}+k_tp_2=0\). Hence
\[
z=\kappa\vartheta+\zeta,
\qquad \lambda,\omega,\kappa,\zeta,p_1,p_0\in L .
\tag{18}
\]
Neither affine slope in (18) is assumed nonzero. The original
expressions below do not require that additional assumption.

The actual auxiliary construction retained in212 gives
\(\mathcal P=aN-(NX)E\), where \(N\) is extended to \(A[u]\)
by fixing \(u\). This is a nonzero polynomial LND fixing \(X\)
and commuting with \(E\). Explicitly, on
\(\mathcal B_a=A_a[X]\) it fixes \(X\) and restricts to \(aN\)
on \(A_a\), so it is locally nilpotent there and on its preserved
subring \(\mathcal B\). The coefficients \(a,NX\) are
E-invariant, which also proves commutation.

Put \(\tau=aN\vartheta\in L^*\), regarded for now only as a
coefficient-field element. The original coordinate actions are
\[
\begin{gathered}
\mathcal PX=0,\qquad
\mathcal PY=\tau\left(\frac{2\vartheta}{c\rho^2}+p_1\right),\\
\mathcal PW=\tau(X+\lambda),\qquad
\mathcal PZ=\tau(\kappa-\rho^{-2}X),\\
\mathcal P^2Y=\frac{2\tau^2}{c\rho^2}\ne0,\qquad
\mathcal P^2Z=\mathcal P^2W=\mathcal P^3Y=0 .
\end{gathered}
\tag{19}
\]
Here \(\mathcal P\tau=0\) since \(N\vartheta\in L\) and
\(\mathcal P\) kills \(L\). The displayed products are actual
polynomials because \(\mathcal P\) is actual. This is not a claim
that each factor, in particular \(\tau\) or \(\rho\), is a
regular function on the original four-space. Since \(X\) is
transcendental over \(\operatorname{Frac}A\), both expressions
for \(\mathcal PW,\mathcal PZ\) are nonzero, proving the exact
coordinate degree pattern \((0,2,1,1)\) for \(\mathcal P\).

## 6. Remaining original-ring gate

The reduction (17)--(19) is in a genuine original coordinate system,
but its coefficient-field parameters have not been descended to
ambient coordinates. The auxiliary derivation is not nice on all
four coordinates: \(\mathcal P^2Y\ne0\). Also its coefficients
need not be E-invariant; for example
\(E(\mathcal PW)=a\tau\ne0\).
Thus the invariant-coefficient criterion205 does not apply directly.
No slice for \(\mathcal P\), invariant ambient coordinate for
\(E\), or recognition of \(A\) is asserted here.

The complete212,213 and relevant214 sources were read before this
argument. New unsaved inline algebra checked (9)--(14), the
quadratic w-coefficient after (15), and the canceled quadratic
z-coefficient. These finite identities do not prove the actual
field return, local scalar argument, or original-ring endpoint.
No saved checker was executed, imported or compiled; no earlier
source, checkpoint, index or packet was changed.
