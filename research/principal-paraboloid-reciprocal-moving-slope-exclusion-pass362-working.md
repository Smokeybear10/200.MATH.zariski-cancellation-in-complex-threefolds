# The reciprocal first-slope family has a zero Jacobian column

Working exclusion: the reciprocal B family left by353 cannot occur in
the full actual moving-slope chart. After two explicit original-ring
automorphisms, four coefficients of the full determinant force its
entire t-column at X=0 to vanish. Both values of the remaining complex
constant slope are included.

The proof uses exact coefficient derivatives in a finite field and does
not assume that its arbitrary functions are rational. It excludes the
reciprocal family only; composition with the other branches is separate.

## 1. Actual entry and the supplied reciprocal family

Retain the full actual chart264, fourth-potential theorem296 and
moving-slope hypotheses349, as explicitly stated in
[361](principal-paraboloid-moving-first-slope-affine-line-reduction-pass361-working.md).
Thus the original four-ring is C[X,Y,Z,W]=A[u], E=partial_u, the exact
degrees are1222, the full initial kernel is X^2Z-Y^2, and the selected
N from the literal Z-partial gives
\[
O=L[v],\quad Nv=1,\quad [L:\mathbb C(t,s)]<\infty,
\quad K=L(v)=\mathbb C(y,z,w),\quad J(X)=-a_0^4\in L^*.
\tag{1}
\]
Here a0=EX. By361 and
[353](principal-paraboloid-affine-sigma-moving-slope-frontier-pass353-working.md),
sigma is affine nonconstant in v, y=j sigma+k0 with j in C, and
theta is affine in sigma. In the reciprocal alternative of353,
write T=t-tau. Its necessary data are
\[
\begin{aligned}
B&=B_0+\gamma/T,\quad \gamma\in\mathbb C^*,\quad\tau,B_0\in\mathbb C,\\
f&=(-j^2+2B_0j)T^2-\gamma\rho/T+f_1T+f_0,\\
\theta&=(\kappa-4Tj)\sigma+e_{\rm old},\qquad
s=\kappa T-2jT^2+\rho,
\end{aligned}
\tag{2}
\]
where j,rho,f1,f0 are complex, kappa is nonconstant in the exact
coefficient field, and n=Bs+f. The coefficients k0,e_old are in L.

## 2. The normalizations are actual polynomial automorphisms

First use the actual map
\[
X_1=X,\quad Y_1=Y-\tau X^2,\quad
Z_1=Z-2\tau Y+\tau^2X^2,\quad W_1=W.
\tag{3}
\]
Its inverse is obtained by replacing tau with -tau. It gives t1=T,
s1=s, sigma1=sigma, y1=y, k1=s1, and n1=n expressed in T,s.
It preserves the full weighted initial relation exactly, since
X1^2 Z1-Y1^2=X^2Z-Y^2. The new literal Z-partial equals the old one.

Next set
\[
X_2=X_1+j,\quad Y_2=Y_1,\quad Z_2=Z_1,
\quad W_2=W_1+2jZ_1.
\tag{4}
\]
The inverse subtracts j and 2jZ2. All coefficients in(3),(4) are
complex. In the new fixed-X2 expansion,
\[
\begin{aligned}
t_2&=T,\quad s_2=s+2jT^2,\quad k_2=s_2,\\
\sigma_2&=\sigma-2jT,\quad
y_2=y-j\sigma+j^2T\in L,\\
\theta_2&=\theta+4jT\sigma-4j^2T^2,
\end{aligned}
\tag{5}
\]
so theta2 is affine in sigma2 with slope kappa. Direct substitution
in the first two literal potentials gives
\[
B_2=B-j,\qquad f_2=f-2jBT^2+j^2T^2.
\tag{6}
\]
Using(2), these become B2=(B0-j)+gamma/T and
f2=-gamma rho/T+(f1-2j gamma)T+f0.

Every actual chart gate survives. The leader of W2 is s2 times a0^2,
and (T,s2) remains a transcendence basis with coefficient Jacobian one.
The full initial ideal is unchanged under the invertible weighted
leading changes. The new Z2-partial is partial_Z1-2j partial_W1;
the latter has intrinsic shift at most three in264, while the former
has exact shift four. Thus the selected N, L and a0 are unchanged.
The coordinate and coefficient Jacobians of(3),(4) are one, so the
calibration in(1) is retained. Actual intercept returns are rebuilt
from the new polynomial frame, not assumed for arbitrary formal maps.

Drop subscripts and rename the resulting complex constants. The exact
normalized situation is
\[
\begin{gathered}
y\in L,\quad P:=\sigma,\quad O=L[P],\quad P_v\in L^*,\\
B=\beta+\gamma/t,\quad
n=\beta s+\gamma(s-\rho)/t+f_1t+f_0,\\
\theta=rP+e,\qquad r=(s-\rho)/t,\qquad
\beta,\gamma,\rho,f_1,f_0\in\mathbb C,\quad\gamma\ne0.
\end{gathered}
\tag{7}
\]
No condition beta nonzero has been added. The replacement r is a
coefficient-field parameter only, not an original polynomial coordinate.

## 3. Exact separating variables and the literal determinant

The parameters t,r are algebraically independent, and L is finite
over C(t,r), since s=rt+rho. The coefficient partials in these new
parameters extend uniquely, commute, and fix P. On L they are
\[
\partial_{t\mid r}=\partial_{t\mid s}+r\partial_s,
\qquad\partial_r=t\partial_s.
\tag{8}
\]
The nonzero element t may be divided by in L. This is not a
localization assertion about the original polynomial ring. The full
new scalar is
\[
J_{t,r,P}(X)=-t a_0^4/P_v\in L^*.
\tag{9}
\]
In particular it is independent of P and X.

The first potential uses n_t differentiated at fixed original s:
n_t=f1-gamma r/t. Hence, with
\[
h=2y+\beta r+f_1,\qquad w_0=\ell-Be,
\tag{10}
\]
the exact intercepts and literal map are
\[
\begin{aligned}
z&=P^2+rP+t h+e+\gamma r+\beta\rho+f_0,\qquad
w=w_0-hP,\\
Y&=y+PX+tX^2,\\
Z&=z+(2tP+rt+\rho)X+t^2X^2,\\
W&=w+(rP+e)X+(rt+\rho)X^2.
\end{aligned}
\tag{11}
\]
The functions y,e,w0 belong to L and can depend on both t and r.
No further integration or rational-field assumption has been made.

All derivatives from now on mean the commuting t,r partials in(8),
holding P fixed. Direct differentiation of(11) gives the following
four full polynomial coefficients, where J0 denotes the X=0 coefficient:
\[
\begin{aligned}
[X^2]J&=-(\beta t+\gamma)(h+e_t)-t(w_0)_t,\\
[XP]J&=-\beta(h+e_t)+2(\beta t+\gamma)y_t-(w_0)_t,\\
[P^2]J_0&=2\beta y_t,\\
[P]J_0&=-(h-\beta r)y_t-2(w_0)_r y_t+2(w_0)_t y_r.
\end{aligned}
\tag{12}
\]
Here [X^2]J is already independent of P. Every expression in(12)
vanishes by(9). In the last expression the term beta r y_t must
be retained before the case split; writing -h y_t there would not
be a correct general coefficient.

## 4. Nonzero beta forces an immediate zero column

If beta is nonzero, the third equation in(12) gives y_t=0. The second
then gives (w0)_t=-beta(h+e_t). Substituting in the first leaves
-gamma(h+e_t)=0. Therefore
\[
y_t=0,\qquad e_t=-h,\qquad (w_0)_t=0.
\tag{13}
\]
Since h_t=2y_t=0, equation(11) implies z_t=h+e_t=0 and w_t=0.
The entire t-column of the intercept Jacobian of (y,z,w) is zero.
Thus J0=0, contradicting(9).

## 5. Zero beta still forces the same zero column

Suppose beta=0. The first two equations in(12) instead give
\[
(w_0)_t=2\gamma y_t,\qquad e_t=-h-2t y_t.
\tag{14}
\]
Define D=w0-2gamma y in L. This definition, not an assumed rational
primitive, gives D_t=0. The last coefficient in(12) becomes
\[
0=-y_t(h+2D_r),\qquad h=2y+f_1.
\tag{15}
\]
If y_t were nonzero as an element of the field, this would give
y=-f1/2-D_r. But the derivatives commute and D_t=0, so differentiating
that equality in t gives y_t=0, a contradiction. Hence y_t=0.
Equation(14) now gives the same identities(13), and again the entire
intercept t-column vanishes. This contradicts(9).

The two beta cases exhaust the complex constant, proving that no
actual reciprocal family(2) exists. Values rho=0, j=0, tau=0 and
zero integration constants have not been divided away.

## 6. Evidence and scope

Fresh unsaved root calculation72a801 reconstructed all determinant
coefficients of(11). Independent reconstructions40ec62 and0a81ea
verified the corrected four coefficients and the zero-column endpoint.
Those independent calculations caught the missing beta r y_t term in
an earlier unsaved outline; it is retained in(12). It does not alter
either case because beta y_t vanishes in both.

The exact coefficient-field argument, actual transformations and
holding-variable conventions are part of the written proof, not
conclusions from a few examples. Separate review of this saved source
is recorded only after completion. No saved checker was executed,
imported, compiled or rerun for this note. This excludes one supplied
family and asserts no unrestricted cancellation, novelty, external
expert review, or proof-assistant certification.
