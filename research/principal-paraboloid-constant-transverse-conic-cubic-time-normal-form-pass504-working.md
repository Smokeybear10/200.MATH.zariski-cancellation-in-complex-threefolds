# A cubic-time normal form for constant transverse conic coupling

Working necessary result: retain the FULL actual264 conic sector
of498,500,501 with \(\gamma=m_s/m^3\in\mathbb C^*\).
A licensed ACTUAL complex polynomial reframe gives
\[
\boxed{
\begin{gathered}
\gamma=1,\quad m^{-2}=\beta t^3/6-2s,\quad k=-1/m,
\quad \beta\in\mathbb C^*,\\
\theta=\frac d mP^2+\frac{\beta t^2}{4}P+c,\qquad
y=-\frac{\beta}{24d},\qquad n=(D_1t+D_0)m,\\
d=ma,\quad d\ne0,\quad d+1\ne0,\quad d_m\ne0,
\qquad D_0,D_1\in\mathbb C.
\end{gathered}}
\tag{1}
\]
The last derivative uses the exact separating basis(t,m).
The remaining coefficient functions d,c and lower potential are
not solved. This is a necessary normal form, not an existence
claim, exclusion of the whole family, or recognition theorem.

## 1. Full actual input

Retain every actual hypothesis of
[264](principal-one-affine-paraboloid-chart-pass264-working.md),
the genuine moving levels and unit minors of
[296](principal-paraboloid-fourth-potential-gradient-minors-pass296-working.md),
and the all-X return and parity of
[327](principal-paraboloid-affine-sigma-quadratic-level-parity-pass327-working.md).
In particular
\[
\begin{gathered}
\mathcal B=A[u_{\rm glob}]=\mathbb C[X,Y,Z,W],\quad
E=\partial_{u_{\rm glob}},\quad X=a_0u_{\rm glob}+x_0,\quad a_0\ne0,\\
\deg_E(X,Y,Z,W)=(1,2,2,2),\quad
I_{\rm initial}=(\mathsf X^2\mathsf Z-\mathsf Y^2)
\text{ is the ENTIRE initial kernel},\\
0\ne N=[u_{\rm glob}^4]\partial_Z|_A,\quad
L=\operatorname{Frac}\ker_A N,\quad [L:\mathbb C(t,s)]<\infty,\\
Na_0=Nt=Ns=0,\quad P=\sigma,\quad O=L[P],\quad NP=\rho\in L^*,\\
\operatorname{Frac}A=L(P),\qquad J_{t,s,P}(X)=-a_0^4/\rho\in L^*.
\end{gathered}
\tag{2}
\]
Both actual returns, the original global slice and literal selected
partial remain required. Exact coefficient partials commute and
have joint constants C. No rationality or actual-unit assumption
on a0 is imposed.

Use the held constant-gamma alternative of
[500](principal-paraboloid-transverse-conic-initial-rigidity-pass500-working.md)
and
[501](principal-paraboloid-constant-transverse-conic-slope-rigidity-pass501-working.md).
Before normalization they supply
\[
\begin{gathered}
F_0=\ker_L\partial_s\text{ finite over }\mathbb C(t),\quad
\gamma\in\mathbb C^*,\quad B,K\in F_0,\\
m^{-2}=B-2\gamma s,\quad k=K-1/(\gamma m),\quad
K=k_2t^2/2+k_1t+k_0,\quad k_i\in\mathbb C,\\
\theta=aP^2+bP+c,\quad a\ne0,\quad\delta=1+ma\ne0,\\
y=lP+r,\quad l=L_c(\delta-1)-k_2/4,\quad L_c\in\mathbb C,\quad
b=aK'+B'/(2\gamma),\\
\delta_s=m_s\kappa\ne0,\qquad \kappa\in L^*.
\end{gathered}
\tag{3}
\]
Primes on F0 mean the exact t derivative, whose constants are C.
The input includes Lc=0.

## 2. Actual normalization of gamma and K

Use the complex polynomial map and its sequential inverse
\[
\begin{aligned}
X_*&=X-k_2/4,&Y_*&=Y+k_1X/2,&Z_*&=Z-k_0X,&W_*&=W/\gamma,\\
X&=X_*+k_2/4,&Y&=Y_*-k_1X/2,&Z&=Z_*+k_0X,&W&=\gamma W_*.
\end{aligned}
\tag{4}
\]
This is in the actual filtered class of
[426](general-coupling-normalization-obstruction-pass426-working.md).
Its literal transport is
\[
\begin{gathered}
t_*=t,\quad s_*=s/\gamma,\quad m_*=\gamma m,\quad
k_*=-1/m_*,\quad\gamma_*=1,\\
P_*=P+K'/2,\quad a_*=a/\gamma,\quad\delta_*=\delta,\quad
B_*=B/\gamma^2,\quad l_*=L_c(\delta_*-1),\quad b_*=B_*'/2.
\end{gathered}
\tag{5}
\]
For example \(k_*=k-k_0-k_1t-k_2t^2/2=-1/(\gamma m)\).
The full weighted initial ideal and exact time profile are preserved.
The selected partial is unchanged, so N, a0 and rho are unchanged.
The bad-row and parameter determinants are both1/gamma. Both actual
returns follow from426's localized-quotient argument. No coefficient
function or inverse of a0 is used in an actual polynomial map.

Drop stars and put \(d=\delta-1=ma\). The normalized data are
\[
\begin{gathered}
m^{-2}=B-2s,\quad k=-1/m,\quad h=m_s=m^3,\quad
p=m_t=-B'm^3/2,\quad k_t=-B'm/2,\\
a=d/m,\quad b=B'/2,\quad
\theta=dP^2/m+B'P/2+c,\quad y=L_cdP+r,\\
d\ne0,\quad d+1\ne0,\quad d_s=m^3\kappa\ne0.
\end{gathered}
\tag{6}
\]
Because m_s is nonzero, (t,m) separates. Its exact derivatives and
the calibrated scalar satisfy
\[
\partial_s=m^3\partial_m|_t,\quad
\partial_t|_s=\partial_t|_m-\frac{B'm^3}{2}\partial_m|_t,\quad
d_m=\kappa\ne0,\quad J_{t,m,P}=-\frac{a_0^4}{\rho m^3}.
\tag{7}
\]
The m-constant field is the same F0. The element d is transcendental
over F0, since an algebraic element over F0 would have zero s
derivative in characteristic zero.

## 3. Complete cubic-level coefficients integrate n and r

The full fourth coefficient from501 gives
\[
n_{ss}=3m^2n_s+4L_cm^3.
\tag{8}
\]
The EXISTING \(D=(n_s+2L_cm)/m^3\) has zero s derivative.
Subtracting an explicit expression then gives
\[
n=Dm+2L_c/m+N_0,\qquad D,N_0\in F_0.
\tag{9}
\]
No rational antiderivative assumption is made.

For reconstruction retain the ENTIRE formal polynomial
\[
\begin{aligned}
F(P,V)&=k_{tt}P^2/2+pPV+hV^2/2+n_tP+n_sV,\\
G(U,P,V)&=\{\ell-(2P+k_t)U-F(P,V)\}/m,\\
H(U,P,V)&=U^2+F_PU+F_VG+H_3(k;P,V)+H_2(n;P,V)
-\ell_tP-\ell_sV.
\end{aligned}
\tag{10}
\]
Its actual level is \(H(y,P,\theta)=h_0\in L\), with the factorial
Taylor denominators from264. After (6) the complete cubic coefficient is
\[
[P^3]H=-\frac1{12}
(6B'am^2n_s-6B'an_{ss}+B'''m+12am^2n_t+24am^2r-12an_{ts}).
\tag{11}
\]
Neither ell nor h0 is set to zero. Their terms do not reach this degree.
The ORIGINAL partials of (9) are
\[
\begin{aligned}
n_s&=Dm^3-2L_cm,& n_{ss}&=3Dm^5-2L_cm^3,\\
n_t&=D'm-DB'm^3/2+L_cB'm+N_0',&
n_{ts}&=D'm^3-3DB'm^5/2+L_cB'm^3.
\end{aligned}
\tag{12}
\]
Thus (11) becomes
\[
[P^3]H=-m(B'''+12N_0'd+24dr)/12=0,\qquad
r=-N_0'/2-B'''/(24d).
\tag{13}
\]
Only nonzero m,d were divided. B''' may still vanish.

## 4. The full scalar forces polynomial time coefficients

In the exact(t,m,P) basis retain the COMPLETE rows
\[
\begin{aligned}
Y&=(X+L_cd)P+r+tX^2,\\
Z&=(d+1)P^2+2t(X+L_cd)P+2tr+mc+n-X/m+t^2X^2,\\
W&=w_{\rm int}+\theta X+sX^2,\qquad s=(B-m^{-2})/2,\\
mw_{\rm int}&=\ell-(2P+k_t)y-F(P,\theta).
\end{aligned}
\tag{14}
\]
All lower functions and their exact moving derivatives are retained.
The full W has quartic coefficient \(-d^2/2\) and cubic coefficient zero:
\(pa+hab=(-B'm^3/2)(d/m)+m^3(d/m)(B'/2)=0\).

The COMPLETE fifth intrinsic coefficient is
\[
\boxed{[P^5]J_{t,m,P}=
\frac{d_m}{12}(-B''''+24L_c^2d^3-12N_0''d)=0.}
\tag{15}
\]
Here is an independent hand extraction. At fixed X put A_X=X+Lc*d.
Only \(Y=A_XP+r+tX^2\), the quadratic and linear terms
\((d+1)P^2+2tA_XP\) of Z, and \(-d^2P^4/2\) of W contribute.
The remaining terms have too small a degree, not frozen coefficients.
Expanding
\(W_P\,dY\wedge dZ-Z_P\,dY\wedge dW+Y_P\,dZ\wedge dW\),
with coefficient differentials only, its fifth coefficient is
\[
2d\,dr\wedge dd+2L_c^2d^3\,dt\wedge dd.
\tag{16}
\]
The X terms cancel by \(X^2+2L_cdA_X-A_X^2=L_c^2d^2\).
Substitute (13) and \(dt\wedge dd=d_m\,dt\wedge dm\) to obtain
(15). The sixth coefficient cancels identically.

Because d_m is nonzero and d is transcendental over F0, comparison
in (15) gives
\[
\boxed{L_c=0,\qquad N_0''=0,\qquad B''''=0.}
\tag{17}
\]
Thus \(N_0=N_1t+N_{00}\), with complex N1,N00, and B is a complex
polynomial of degree at most three. Put \(\beta=B'''\in\mathbb C\).

With (17), one more COMPLETE scalar coefficient is
\[
\boxed{[XP^3]J_{t,m,P}=D''d_m=0.}
\tag{18}
\]
For direct reconstruction the full positive-P coefficients of W are
\[
\begin{aligned}
[P^4]W&=-d^2/2,&[P^3]W&=0,\\
[P^2]W&=B''/4-md(c+D)+dX/m,&
[P]W&=-D'+\beta/(12md)+B'X/2.
\end{aligned}
\tag{19}
\]
Its constant coefficient can remain arbitrary for (18), since that
part contributes P degree at most two to the determinant. Exact
differentiation of (14),(19), with all c,d derivatives, gives (18).
Consequently \(D=D_1t+D_0\), with D0,D1 complex and either allowed zero.

## 5. The cubic coefficient cannot vanish

If beta=0, (13),(17) give \(y=-N_1/2\in\mathbb C\). The ACTUAL
coordinate Y would satisfy \(Y|_{X=0}=-N_1/2\).

The ideal(X) is prime in the actual polynomial frame and does not
contain a0: otherwise additivity of E-degree contradicts
\(\deg_Ea_0=0<\deg_EX=1\). The original slice gives
\(\mathcal B_{a_0}=A_{a_0}[X]\). Evaluation at X=0 there followed
by the injection into L(P) is exactly the displayed literal
evaluation. Its kernel contracts to(X) in the actual ring, by
primality and a0 not in(X). It would follow that Y+N1/2 belongs
to(X), impossible in the polynomial quotient C[Y,Z,W].
Therefore
\[
\boxed{\beta\in\mathbb C^*.}
\tag{20}
\]
No rational generic invariant or denominator is specialized.

## 6. Final actual removal of lower complex time terms

Write
\[
B=\beta t^3/6+b_2t^2/2+b_1t+b_0,\qquad
R(t)=-(b_2t^2/2+b_1t+b_0)/2=r_2t^2+r_1t+r_0.
\tag{21}
\]
All these coefficients are complex; zeros are allowed. Use
\[
\begin{aligned}
X_*&=X,\quad Y_*=Y+N_1/2,\quad Z_*=Z-N_{00}-r_2,\\
W_*&=W+r_2(Z-N_{00})+r_1(Y+N_1/2)+r_0X^2.
\end{aligned}
\tag{22}
\]
Its polynomial inverse is
\[
X=X_*,\quad Y=Y_*-N_1/2,\quad Z=Z_*+N_{00}+r_2,\quad
W=W_*-r_2(Z_*+r_2)-r_1Y_*-r_0X_*^2.
\tag{23}
\]
This is another actual426 map, with
\(t_*=t,s_*=s+R(t),P_*=P,m_*=m,k_*=-1/m_*,d_*=d\).
Thus B*=B+2R=beta*t^3/6, b*=beta*t^2/4 and y*=-beta/(24d).
For the full first potential, the exact moving derivative is
\(k_{t_*}=k_t-R'm\) and \(\theta_*=\theta+R'P+r_2k\). Hence
\[
n_*=n-N_1t-N_{00}-r_2-mr_2k=Dm
\tag{24}
\]
because k=-1/m. This retains every complex constant.

The full initial ideal and E-profile persist. The literal selected
partial transforms as \(\partial_{Z_*}=\partial_Z-r_2\partial_W\);
426's omitted-partial bound gives the same N. Row and parameter
determinants are both one, and426 supplies both actual returns.
These maps prove (1), with all remaining hypotheses intact.
No root of d, d+1, B or D was deleted by an ambient localization.

## 7. Verification and remaining scope

The held500/501 inputs and full426/327 were read before this work.
Root fresh5df321 checks both orders of the first actual inverse,
coupling, delta, slope and row determinant. Fresh7ffc18/affa54
rebuilt the entire H and formal gradient;1074d1 verifies the full
substituted cubic coefficient. Fresh aa9d80, completed20c62f,
reconstructs the whole determinant with arbitrary c,ell and all
relevant coefficient jets, giving (15),(18). Fresh612e00 independently
checks the complete degree-five hand formula, sixth cancellation,
and XP^3 extraction, all residuals zero. Fresh1da608 verifies both
orders of the final inverse, full n transport and row determinant.
Independent saved-source review is recorded separately in the ledger.

This is a necessary actual normal form for constant gamma only.
The nonzero-beta family still must satisfy the remaining scalar,
genuine moving levels, parity and actual realization. It is not
asserted to exist or to be excluded. Nonconstant gamma, m_s=0,
the delta-zero boundary, other projected curves and arbitrary
actual entry remain separate. No general cancellation, historical
novelty, human expert review or proof-assistant certification is
claimed. All saved checkers remain frozen; none was executed,
imported, compiled or rerun. No earlier source was edited.

